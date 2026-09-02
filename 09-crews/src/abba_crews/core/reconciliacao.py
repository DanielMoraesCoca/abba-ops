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
porta para julgamento por modelo. Quanto do trabalho **nao** passa por essa porta e o
que decide se a conta fecha em centenas de CNPJs por mes — e esse numero **se mede**,
nao se afirma: `abba-crews cobertura`.
Com a tabela de vedacoes como ela nasce (sem uma linha conferida), quase tudo cai em
DUVIDOSO. O numero sobe conforme o contador preenche a tabela.

## A classificacao de creditabilidade e opcional, e isso e deliberado

Ate o M2 `CLASSIFICACAO_DUVIDOSA` existia no enum e **nada a construia**: a porta
do julgamento estava trancada por dentro. Passando um `classificador`
(`core/creditabilidade`), cada credito ausente da proposta e conferido contra a
tabela de vedacoes e pode virar descarte (vedado) ou duvida (desconhecido).

Sem classificador o comportamento e identico ao do M2 — o que mantem todo o
regime de testes estrutural valido e permite rodar a conferencia estrutural mesmo
sem tabela nenhuma.
"""

from __future__ import annotations

from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field

from abba_crews.core.creditabilidade import Classificador, Veredito
from abba_crews.core.modelos import (
    ApuracaoFisco,
    DocumentoFiscal,
    ItemDocumento,
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

    Invariante do produto: **nao existe divergencia sem chave de documento**. Quem
    garante isso e a validacao do proprio campo (`chave` com exatamente 44 digitos):
    uma `Divergencia` sem documento **nao chega a ser construida**.

    A versao anterior desta docstring falava de "um guardrail que barra qualquer item
    sem chave antes de o dossie sair". Esse guardrail nunca existiu — nao havia nada
    entre `reconciliar()` e `renderizar()`. A invariante era verdadeira e a explicacao
    era falsa, o que e pior do que nao explicar: manda procurar defesa onde nao ha.
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


class ItemDescartado(BaseModel):
    """Um credito que a empresa tem documentado e que **nao** entra no dossie.

    Existe para ser mostrado, nao para ser escondido. Um dossie que so lista o que
    entra pede fe; um que lista tambem o que ficou de fora, e sob qual dispositivo,
    pode ser conferido — e e isso que o contador precisa para assinar o resto.
    """

    model_config = {"frozen": True}

    chave: str = Field(min_length=44, max_length=44)
    item: int = Field(ge=1)
    valor_brl: Decimal = Field(description="O R$ que NAO sera pleiteado")
    cst: str
    c_class_trib: str
    razao: str
    fonte: str = Field(min_length=1, description="Dispositivo citado. Nunca vazio.")


class ResultadoReconciliacao(BaseModel):
    """O que a conferencia de uma competencia produziu."""

    model_config = {"frozen": True}

    cnpj: str
    competencia: str
    divergencias: tuple[Divergencia, ...]
    itens_conferidos: int
    tolerancia_brl: Decimal = ZERO
    """A folga aplicada. Aparece no dossie: o contador tem de saber o que foi ignorado."""
    suprimidos_por_tolerancia: int = 0
    """Quantos itens divergiam menos que a tolerancia e por isso nao viraram achado."""
    valor_suprimido_brl: Decimal = ZERO
    """Quanto, em R$, a tolerancia engoliu. Zero quando a tolerancia e zero."""
    descartados: tuple[ItemDescartado, ...] = ()
    """Vazio quando se reconcilia sem classificador — o padrao ate a tabela existir."""

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

    @property
    def total_descartado(self) -> Decimal:
        """R$ que a classificacao tirou do dossie. Aparece no documento, somado."""
        return sum((d.valor_brl for d in self.descartados), ZERO)

    @property
    def itens_em_julgamento(self) -> int:
        return sum(1 for d in self.divergencias if d.requer_julgamento)

    @property
    def cobertura(self) -> float:
        """Fracao dos itens resolvida sem julgamento por modelo.

        E a resposta direta a pergunta de custo: que parte do trabalho a regra
        resolve sozinha? Com a tabela de vedacoes vazia isto tende a zero, e esse
        zero e o numero honesto — cada linha que o contador acrescenta o move.
        """
        if not self.itens_conferidos:
            return 1.0
        return (self.itens_conferidos - self.itens_em_julgamento) / self.itens_conferidos

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
    classificador: Classificador | None = None,
) -> ResultadoReconciliacao:
    """Confronta os documentos da empresa contra a proposta do Fisco.

    `tolerancia_brl` descarta diferenca de centavos vinda de arredondamento em
    sistemas diferentes. **Cuidado ao configurar:** tolerancia alta esconde
    divergencia real. O padrao e zero — quem quiser folga, declara e assume.

    E o "assume" agora tem onde acontecer: o resultado registra a tolerancia aplicada,
    quantos itens ela engoliu e quanto em R$, e o dossie mostra isso ao contador. Ate
    2026-09-02 uma tolerancia de R$ 999.999.999 no YAML zerava as divergencias e o
    documento nao dizia uma palavra — o profissional assinava "nada a manifestar" sem
    saber que havia sido cegado por configuracao. E a mesma forma do `DEBITO_OMITIDO`:
    o documento nao pode calar sobre o que escondeu.

    `classificador` (opcional) confere a creditabilidade de cada credito ausente da
    proposta. Sem ele, a conferencia e puramente estrutural — o comportamento do M2.
    Com ele, credito vedado sai do dossie para a lista de descartados e credito de
    codigo desconhecido vira `CLASSIFICACAO_DUVIDOSA`.

    **Limite deliberado deste marco:** a classificacao se aplica so ao credito
    *inteiramente ausente* da proposta. Um `VALOR_DIVERGENTE` de entrada tambem
    depende de creditabilidade, mas ali o Fisco ja reconheceu o item — a duvida e
    de quantia, nao de direito. Ampliar isso exige a tabela preenchida (P2).
    """
    if not tolerancia_brl.is_finite() or tolerancia_brl < ZERO:
        raise ValueError(f"tolerancia invalida: {tolerancia_brl!r}. Deve ser finita e >= 0.")

    _exige_documentos_do_contribuinte(documentos, apuracao.cnpj)
    da_competencia = tuple(d for d in documentos if d.competencia == apuracao.competencia)
    proposta = apuracao.por_chave_item()
    vistos: set[tuple[str, int]] = set()
    achados: list[Divergencia] = []
    descartados: list[ItemDescartado] = []
    conferidos = 0
    suprimidos = 0
    valor_suprimido = ZERO

    for doc in da_competencia:
        for item in doc.itens:
            conferidos += 1
            ref = _chave_item(doc, item.numero)
            linha = proposta.get(ref)

            if linha is None:
                achado = _ausente_na_proposta(doc, item, classificador)
                if isinstance(achado, ItemDescartado):
                    descartados.append(achado)
                else:
                    achados.append(achado)
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
            if abs(diferenca) <= tolerancia_brl:
                if diferenca != ZERO:
                    suprimidos += 1
                    valor_suprimido += abs(diferenca)
            else:
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
    descartados.sort(key=lambda d: (-d.valor_brl, d.chave, d.item))
    return ResultadoReconciliacao(
        cnpj=apuracao.cnpj,
        competencia=apuracao.competencia,
        divergencias=tuple(achados),
        itens_conferidos=conferidos,
        descartados=tuple(descartados),
        tolerancia_brl=tolerancia_brl,
        suprimidos_por_tolerancia=suprimidos,
        valor_suprimido_brl=valor_suprimido,
    )


class DocumentoDeTerceiro(ValueError):
    """Chegou documento que nao envolve o CNPJ sendo apurado."""


def _exige_documentos_do_contribuinte(
    documentos: tuple[DocumentoFiscal, ...], cnpj: str
) -> None:
    """O contribuinte tem de ser parte em todo documento conferido.

    **O guarda contra o pior erro possivel deste produto** — palavras do proprio
    `core/clientes.py`, que ate aqui so as aplicava ao nome do arquivo de configuracao.

    Ate 2026-09-02 `reconciliar()` filtrava apenas por competencia. Uma nota de outra
    empresa entrava no dossie deste cliente e virava pleito de credito, sem um aviso —
    verificado: documento do CNPJ 11222333000181 gerou R$ 100,00 "a favor" na apuracao
    do CNPJ 00000000000191. `emitente_cnpj` e `destinatario_cnpj` existiam no modelo,
    validados a 14 digitos, e nenhuma linha os lia.

    Isso deixa de ser hipotetico no M6: a Distribuicao DF-e responde por certificado, e
    uma consulta mal escopada ou um certificado de escritorio contabil trazem documento
    de terceiro. Recusar alto e a unica resposta — um falso positivo fiscal desses manda
    o cliente pleitear credito de outra empresa.
    """
    intrusos = [
        d for d in documentos if cnpj not in (d.emitente_cnpj, d.destinatario_cnpj)
    ]
    if not intrusos:
        return
    d = intrusos[0]
    raise DocumentoDeTerceiro(
        f"{len(intrusos)} documento(s) nao envolvem o CNPJ apurado.\n"
        f"  apuracao do CNPJ: {cnpj}\n"
        f"  documento {d.chave}: emitente {d.emitente_cnpj}, "
        f"destinatario {d.destinatario_cnpj}\n"
        f"Conferir a apuracao com documento de terceiro e o pior erro possivel deste "
        f"produto: o cliente pleitearia credito que nao e dele. Conferir a origem da "
        f"coleta antes de rodar de novo."
    )


def _ausente_na_proposta(
    doc: DocumentoFiscal, item: ItemDocumento, classificador: Classificador | None
) -> Divergencia | ItemDescartado:
    """Documento da empresa que a proposta do Fisco nao contemplou.

    Entrada passa pela creditabilidade quando ha classificador; saida nao, porque
    debito omitido nao depende de direito a credito — depende de ter havido a
    operacao, e ela esta documentada.
    """
    numero, valor = item.numero, item.tributo_total

    if doc.papel is Papel.ENTRADA:
        if classificador is not None:
            c = classificador.classificar(item.cst, item.c_class_trib)

            if c.veredito is Veredito.VEDADO:
                return ItemDescartado(
                    chave=doc.chave,
                    item=numero,
                    valor_brl=valor,
                    cst=item.cst,
                    c_class_trib=item.c_class_trib,
                    razao=c.razao,
                    fonte=c.fonte,
                )

            if c.veredito is Veredito.DUVIDOSO:
                return Divergencia(
                    tipo=TipoDivergencia.CLASSIFICACAO_DUVIDOSA,
                    sentido=Sentido.INDETERMINADO,
                    chave=doc.chave,
                    item=numero,
                    valor_brl=valor,
                    detalhe=(
                        f"credito de R$ {valor} ausente da proposta do Fisco, com "
                        f"creditabilidade NAO resolvida pela tabela (CST {item.cst}, "
                        f"cClassTrib {item.c_class_trib}). {c.razao} "
                        f"Fonte: {c.fonte}. Nao pleitear sem conferencia: pleitear "
                        f"credito indevido cria passivo onde nao havia."
                    ),
                )

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
