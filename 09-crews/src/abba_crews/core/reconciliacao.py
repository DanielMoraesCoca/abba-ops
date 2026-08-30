"""Reconciliacao: a proposta do Fisco contra os documentos da empresa.

Este e o modulo que vale dinheiro. Ele e deterministico, nao usa LLM, e nao chama
rede. Dado o mesmo par (documentos, apuracao), devolve sempre a mesma lista.

## A regra etica que molda a taxonomia

O produto reporta **toda** divergencia, inclusive as que custam caro ao cliente.
Manifestar so o que e favoravel e divulgacao seletiva: quem confere a apuracao e
cala sobre um debito omitido esta ajudando a empresa a errar contra si mesma, e
o passivo continua sendo dela. Por isso toda divergencia carrega `sentido`, e o
dossie apresenta os dois lados separados e somados.

Nao e escrupulo abstrato: e o que torna o dossie assinavel por um contador.

## A taxonomia, fechada

Cinco tipos estruturais, todos deterministicos, mais um sexto que e a **unica**
porta para julgamento por modelo. Quatro em cada cinco execucoes nao passam por
essa porta — e o que faz a conta fechar em centenas de CNPJs por mes.
"""

from __future__ import annotations

from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field

from abba_crews.core.modelos import (
    ApuracaoFisco,
    DocumentoFiscal,
    LinhaApuracao,
    Papel,
)

ZERO = Decimal("0.00")


class TipoDivergencia(str, Enum):  # noqa: UP042
    """O que difere entre a proposta do Fisco e os documentos da empresa."""

    CREDITO_OMITIDO = "credito_omitido"
    """Entrada da empresa ausente da proposta. E aqui que mora o dinheiro."""

    DEBITO_OMITIDO = "debito_omitido"
    """Saida da empresa ausente da proposta. Desfavoravel — e se reporta assim mesmo."""

    VALOR_DIVERGENTE = "valor_divergente"
    """Mesma chave e item nos dois lados, valor diferente."""

    PAPEL_DIVERGENTE = "papel_divergente"
    """A empresa registra entrada e o Fisco saida (ou o contrario). Erro de dado grave."""

    DOC_DESCONHECIDO = "doc_desconhecido"
    """A proposta traz documento que a empresa nao tem. Pode ser nota nao escriturada."""

    CLASSIFICACAO_DUVIDOSA = "classificacao_duvidosa"
    """Creditabilidade incerta. **Unica rota para julgamento por modelo.**"""


class Sentido(str, Enum):  # noqa: UP042
    """Para que lado a divergencia pesa, do ponto de vista do contribuinte."""

    FAVORAVEL = "favoravel"
    """Aumenta credito ou reduz debito — dinheiro que a empresa deixaria na mesa."""

    DESFAVORAVEL = "desfavoravel"
    """Reduz credito ou aumenta debito — passivo que a empresa assumiria calada."""

    INDETERMINADO = "indeterminado"
    """Precisa de conferencia humana para saber de que lado pesa."""


class Divergencia(BaseModel):
    """Uma diferenca achada, sempre com o documento que a comprova.

    Invariante do produto: **nao existe divergencia sem chave de documento**. Um
    guardrail barra qualquer item sem `chave` antes de o dossie sair.
    """

    model_config = {"frozen": True}

    tipo: TipoDivergencia
    sentido: Sentido
    chave: str = Field(min_length=44, max_length=44, description="A evidencia. Nunca vazia.")
    item: int = Field(ge=1)
    valor_brl: Decimal = Field(description="O R$ em jogo, sempre positivo")
    detalhe: str

    @property
    def requer_julgamento(self) -> bool:
        return self.tipo is TipoDivergencia.CLASSIFICACAO_DUVIDOSA


class ResultadoReconciliacao(BaseModel):
    """O que a conferencia de uma competencia produziu."""

    model_config = {"frozen": True}

    cnpj: str
    competencia: str
    divergencias: tuple[Divergencia, ...]
    itens_conferidos: int

    @property
    def conforme(self) -> bool:
        """Nada a manifestar. Este e o caminho barato: zero custo de LLM."""
        return not self.divergencias

    @property
    def requer_julgamento(self) -> bool:
        """Alguma divergencia precisa de modelo? Se nao, o dossie sai por template."""
        return any(d.requer_julgamento for d in self.divergencias)

    @property
    def total_favoravel(self) -> Decimal:
        return sum(
            (d.valor_brl for d in self.divergencias if d.sentido is Sentido.FAVORAVEL), ZERO
        )

    @property
    def total_desfavoravel(self) -> Decimal:
        return sum(
            (d.valor_brl for d in self.divergencias if d.sentido is Sentido.DESFAVORAVEL), ZERO
        )

    def por_tipo(self, tipo: TipoDivergencia) -> tuple[Divergencia, ...]:
        return tuple(d for d in self.divergencias if d.tipo is tipo)


def _chave_item(doc: DocumentoFiscal, numero: int) -> tuple[str, int]:
    return (doc.chave, numero)


def apuracao_a_partir_de(
    documentos: tuple[DocumentoFiscal, ...], cnpj: str, competencia: str
) -> ApuracaoFisco:
    """Monta a apuracao que o Fisco proporia se enxergasse exatamente estes documentos.

    Serve a duas coisas: gerar o caso limpo do golden set, e sustentar o invariante
    de propriedade — reconciliar documentos contra a apuracao derivada deles proprios
    tem de dar **zero divergencias**. Se um dia der outra coisa, o reconciliador
    regrediu, e o teste pega antes do cliente.
    """
    linhas = tuple(
        LinhaApuracao(
            chave=doc.chave,
            item=item.numero,
            papel=doc.papel,
            v_ibs=item.v_ibs,
            v_cbs=item.v_cbs,
        )
        for doc in documentos
        if doc.competencia == competencia
        for item in doc.itens
    )
    return ApuracaoFisco(cnpj=cnpj, competencia=competencia, linhas=linhas)


def reconciliar(
    documentos: tuple[DocumentoFiscal, ...],
    apuracao: ApuracaoFisco,
    *,
    tolerancia_brl: Decimal = ZERO,
) -> ResultadoReconciliacao:
    """Confronta os documentos da empresa contra a proposta do Fisco.

    `tolerancia_brl` descarta diferenca de centavos vinda de arredondamento em
    sistemas diferentes. **Cuidado ao configurar:** tolerancia alta esconde
    divergencia real. O padrao e zero — quem quiser folga, declara e assume.
    """
    if tolerancia_brl < ZERO:
        raise ValueError("tolerancia nao pode ser negativa")

    da_competencia = tuple(d for d in documentos if d.competencia == apuracao.competencia)
    proposta = apuracao.por_chave_item()
    vistos: set[tuple[str, int]] = set()
    achados: list[Divergencia] = []
    conferidos = 0

    for doc in da_competencia:
        for item in doc.itens:
            conferidos += 1
            ref = _chave_item(doc, item.numero)
            linha = proposta.get(ref)

            if linha is None:
                achados.append(_ausente_na_proposta(doc, item.numero, item.tributo_total))
                continue

            vistos.add(ref)

            if linha.papel is not doc.papel:
                achados.append(
                    Divergencia(
                        tipo=TipoDivergencia.PAPEL_DIVERGENTE,
                        sentido=Sentido.INDETERMINADO,
                        chave=doc.chave,
                        item=item.numero,
                        valor_brl=item.tributo_total,
                        detalhe=(
                            f"a empresa registra {doc.papel.value} e a proposta do Fisco "
                            f"registra {linha.papel.value}. Erro de dado em um dos lados — "
                            f"conferir antes de qualquer manifestacao."
                        ),
                    )
                )
                continue

            diferenca = item.tributo_total - linha.tributo_total
            if abs(diferenca) > tolerancia_brl:
                achados.append(_valor_divergente(doc, item.numero, diferenca, item.tributo_total,
                                                 linha.tributo_total))

    for ref, linha in proposta.items():
        if ref in vistos:
            continue
        if any(d.chave == ref[0] and d.item == ref[1] for d in achados):
            continue
        achados.append(
            Divergencia(
                tipo=TipoDivergencia.DOC_DESCONHECIDO,
                sentido=(
                    Sentido.INDETERMINADO
                    if linha.papel is Papel.ENTRADA
                    else Sentido.DESFAVORAVEL
                ),
                chave=linha.chave,
                item=linha.item,
                valor_brl=linha.tributo_total,
                detalhe=(
                    f"a proposta do Fisco traz {linha.papel.value} de "
                    f"R$ {linha.tributo_total} que a empresa nao tem escriturada. "
                    f"Pode ser nota de entrada nao recebida — conferir na Distribuicao DF-e."
                ),
            )
        )

    achados.sort(key=lambda d: (-d.valor_brl, d.chave, d.item))
    return ResultadoReconciliacao(
        cnpj=apuracao.cnpj,
        competencia=apuracao.competencia,
        divergencias=tuple(achados),
        itens_conferidos=conferidos,
    )


def _ausente_na_proposta(doc: DocumentoFiscal, numero: int, valor: Decimal) -> Divergencia:
    """Documento da empresa que a proposta do Fisco nao contemplou."""
    if doc.papel is Papel.ENTRADA:
        return Divergencia(
            tipo=TipoDivergencia.CREDITO_OMITIDO,
            sentido=Sentido.FAVORAVEL,
            chave=doc.chave,
            item=numero,
            valor_brl=valor,
            detalhe=(
                f"credito de R$ {valor} documentado pela empresa e ausente da proposta "
                f"do Fisco. Sem manifestacao ate o prazo, o silencio consolida a proposta "
                f"e este credito e perdido."
            ),
        )
    return Divergencia(
        tipo=TipoDivergencia.DEBITO_OMITIDO,
        sentido=Sentido.DESFAVORAVEL,
        chave=doc.chave,
        item=numero,
        valor_brl=valor,
        detalhe=(
            f"debito de R$ {valor} documentado pela empresa e ausente da proposta do "
            f"Fisco. Desfavoravel ao contribuinte, e entra no dossie assim mesmo: "
            f"conferir e calar sobre o que pesa contra e divulgacao seletiva."
        ),
    )


def _valor_divergente(
    doc: DocumentoFiscal, numero: int, diferenca: Decimal, na_empresa: Decimal, na_proposta: Decimal
) -> Divergencia:
    """Mesma chave e item nos dois lados, valor diferente."""
    if doc.papel is Papel.ENTRADA:
        sentido = Sentido.FAVORAVEL if diferenca > ZERO else Sentido.DESFAVORAVEL
    else:
        sentido = Sentido.DESFAVORAVEL if diferenca > ZERO else Sentido.FAVORAVEL

    return Divergencia(
        tipo=TipoDivergencia.VALOR_DIVERGENTE,
        sentido=sentido,
        chave=doc.chave,
        item=numero,
        valor_brl=abs(diferenca),
        detalhe=(
            f"{doc.papel.value}: documento da empresa diz R$ {na_empresa}, proposta do "
            f"Fisco diz R$ {na_proposta}. Diferenca de R$ {abs(diferenca)}."
        ),
    )
