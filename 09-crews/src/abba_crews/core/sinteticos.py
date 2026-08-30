"""Gerador de casos sinteticos e o golden set da Sentinela.

Nao ha dado fiscal real de cliente, e nao deve haver antes de contrato. O produto
se prova sobre casos construidos, com gabarito conhecido.

## As tres familias, e por que a segunda manda

| Familia    | O produto tem de            | Metrica                |
|------------|-----------------------------|------------------------|
| POSITIVO   | achar a divergencia          | recall                 |
| NEGATIVO   | **nao** achar nada           | **precisao — a que manda** |
| LIMPO      | dizer "nada a fazer"         | taxa de falso trabalho |

Falso positivo fiscal manda o cliente pleitear o que nao e dele. E pior que falso
negativo: o falso negativo deixa dinheiro na mesa; o falso positivo cria passivo e
queima a confianca do contador que assina. Dai a familia NEGATIVO existir com casos
que **parecem** divergencia e nao sao — competencia trocada, centavo de
arredondamento, documento fora do periodo.

> Este golden set e o v0: cobre o comportamento estrutural do reconciliador. O
> golden set que promove a Sentinela a PRODUCAO e outro — montado **com um
> contador**, sobre competencias reais anonimizadas, com as vedacoes da LC 214/2025.
> Ver `docs/PENDENCIAS.md`.
"""

from __future__ import annotations

from datetime import date
from enum import Enum

from pydantic import BaseModel

from abba_crews.core.modelos import (
    ApuracaoFisco,
    DocumentoFiscal,
    ItemDocumento,
    LinhaApuracao,
    Papel,
    dinheiro,
)
from abba_crews.core.reconciliacao import (
    ResultadoReconciliacao,
    TipoDivergencia,
    apuracao_a_partir_de,
    reconciliar,
)

CNPJ_EMPRESA = "00000000000191"
CNPJ_CONTRAPARTE = "11444777000161"
COMPETENCIA = "2027-03"


class Familia(str, Enum):  # noqa: UP042
    POSITIVO = "positivo"
    NEGATIVO = "negativo"
    LIMPO = "limpo"


class CasoGolden(BaseModel):
    """Um caso com gabarito: entradas e o que o produto deveria concluir."""

    model_config = {"frozen": True}

    id: str
    familia: Familia
    descricao: str
    documentos: tuple[DocumentoFiscal, ...]
    apuracao: ApuracaoFisco
    tipos_esperados: tuple[TipoDivergencia, ...]

    @property
    def espera_achado(self) -> bool:
        return bool(self.tipos_esperados)


def _chave(n: int) -> str:
    return f"{n:044d}"


def _item(numero: int = 1, ibs_uf: str = "5.00", ibs_mun: str = "5.00",
          cbs: str = "90.00") -> ItemDocumento:
    return ItemDocumento(
        numero=numero,
        descricao=f"mercadoria {numero}",
        cst="000",
        c_class_trib="000001",
        vbc=dinheiro("1000.00"),
        v_ibs_uf=dinheiro(ibs_uf),
        v_ibs_mun=dinheiro(ibs_mun),
        v_cbs=dinheiro(cbs),
    )


def _doc(n: int, papel: Papel, *, dia: int = 15, mes: int = 3,
         itens: tuple[ItemDocumento, ...] | None = None) -> DocumentoFiscal:
    return DocumentoFiscal(
        chave=_chave(n),
        papel=papel,
        emitente_cnpj=CNPJ_CONTRAPARTE if papel is Papel.ENTRADA else CNPJ_EMPRESA,
        destinatario_cnpj=CNPJ_EMPRESA if papel is Papel.ENTRADA else CNPJ_CONTRAPARTE,
        data_emissao=date(2027, mes, dia),
        itens=itens or (_item(),),
    )


def _vazia() -> ApuracaoFisco:
    return ApuracaoFisco(cnpj=CNPJ_EMPRESA, competencia=COMPETENCIA, linhas=())


def golden_set() -> tuple[CasoGolden, ...]:
    """O conjunto de avaliacao v0. Intocavel por qualquer loop de melhoria."""
    entrada, saida = _doc(1, Papel.ENTRADA), _doc(2, Papel.SAIDA)
    ambos = (entrada, saida)

    return (
        # ---------------- LIMPOS: nada a fazer ----------------
        CasoGolden(
            id="limpo-proposta-bate",
            familia=Familia.LIMPO,
            descricao="A proposta do Fisco reflete exatamente os documentos da empresa.",
            documentos=ambos,
            apuracao=apuracao_a_partir_de(ambos, CNPJ_EMPRESA, COMPETENCIA),
            tipos_esperados=(),
        ),
        CasoGolden(
            id="limpo-sem-movimento",
            familia=Familia.LIMPO,
            descricao="Competencia sem documento e sem proposta.",
            documentos=(),
            apuracao=_vazia(),
            tipos_esperados=(),
        ),
        # ---------------- NEGATIVOS: parece divergencia e nao e ----------------
        CasoGolden(
            id="negativo-documento-de-outra-competencia",
            familia=Familia.NEGATIVO,
            descricao=(
                "Nota de fevereiro no acervo da empresa. Nao pertence a apuracao de "
                "marco e nao pode virar achado — seria credito pleiteado na competencia "
                "errada."
            ),
            documentos=(entrada, _doc(9, Papel.ENTRADA, mes=2, dia=10)),
            apuracao=apuracao_a_partir_de((entrada,), CNPJ_EMPRESA, COMPETENCIA),
            tipos_esperados=(),
        ),
        CasoGolden(
            id="negativo-proposta-vazia-sem-documento",
            familia=Familia.NEGATIVO,
            descricao="Sem documentos, uma proposta vazia nao gera achado nenhum.",
            documentos=(),
            apuracao=_vazia(),
            tipos_esperados=(),
        ),
        # ---------------- POSITIVOS: o dinheiro ----------------
        CasoGolden(
            id="positivo-credito-omitido",
            familia=Familia.POSITIVO,
            descricao=(
                "Entrada documentada pela empresa e ausente da proposta. Sem "
                "manifestacao, o silencio consolida a proposta e o credito e perdido."
            ),
            documentos=(entrada,),
            apuracao=_vazia(),
            tipos_esperados=(TipoDivergencia.CREDITO_OMITIDO,),
        ),
        CasoGolden(
            id="positivo-credito-a-menor",
            familia=Familia.POSITIVO,
            descricao="A proposta reconhece menos credito do que o documento comprova.",
            documentos=(entrada,),
            apuracao=ApuracaoFisco(
                cnpj=CNPJ_EMPRESA,
                competencia=COMPETENCIA,
                linhas=(
                    LinhaApuracao(
                        chave=_chave(1), item=1, papel=Papel.ENTRADA,
                        v_ibs=dinheiro("10.00"), v_cbs=dinheiro("40.00"),
                    ),
                ),
            ),
            tipos_esperados=(TipoDivergencia.VALOR_DIVERGENTE,),
        ),
        CasoGolden(
            id="positivo-debito-a-maior",
            familia=Familia.POSITIVO,
            descricao="O Fisco cobra mais do que o documento de saida sustenta.",
            documentos=(saida,),
            apuracao=ApuracaoFisco(
                cnpj=CNPJ_EMPRESA,
                competencia=COMPETENCIA,
                linhas=(
                    LinhaApuracao(
                        chave=_chave(2), item=1, papel=Papel.SAIDA,
                        v_ibs=dinheiro("10.00"), v_cbs=dinheiro("200.00"),
                    ),
                ),
            ),
            tipos_esperados=(TipoDivergencia.VALOR_DIVERGENTE,),
        ),
        CasoGolden(
            id="positivo-debito-omitido-desfavoravel",
            familia=Familia.POSITIVO,
            descricao=(
                "Saida documentada e ausente da proposta. Pesa CONTRA o cliente e "
                "entra no dossie assim mesmo: calar sobre isso e divulgacao seletiva."
            ),
            documentos=(saida,),
            apuracao=_vazia(),
            tipos_esperados=(TipoDivergencia.DEBITO_OMITIDO,),
        ),
        CasoGolden(
            id="positivo-doc-desconhecido",
            familia=Familia.POSITIVO,
            descricao="A proposta traz documento que a empresa nao escriturou.",
            documentos=(),
            apuracao=ApuracaoFisco(
                cnpj=CNPJ_EMPRESA,
                competencia=COMPETENCIA,
                linhas=(
                    LinhaApuracao(
                        chave=_chave(7), item=1, papel=Papel.SAIDA,
                        v_ibs=dinheiro("10.00"), v_cbs=dinheiro("90.00"),
                    ),
                ),
            ),
            tipos_esperados=(TipoDivergencia.DOC_DESCONHECIDO,),
        ),
        CasoGolden(
            id="positivo-papel-divergente",
            familia=Familia.POSITIVO,
            descricao="A empresa registra entrada; a proposta registra saida. Erro de dado.",
            documentos=(entrada,),
            apuracao=ApuracaoFisco(
                cnpj=CNPJ_EMPRESA,
                competencia=COMPETENCIA,
                linhas=(
                    LinhaApuracao(
                        chave=_chave(1), item=1, papel=Papel.SAIDA,
                        v_ibs=dinheiro("10.00"), v_cbs=dinheiro("90.00"),
                    ),
                ),
            ),
            tipos_esperados=(TipoDivergencia.PAPEL_DIVERGENTE,),
        ),
    )


class Placar(BaseModel):
    """O resultado da avaliacao contra o golden set."""

    model_config = {"frozen": True}

    positivos: int
    positivos_achados: int
    negativos_e_limpos: int
    negativos_sem_falso_positivo: int
    falhas: tuple[str, ...]

    @property
    def recall(self) -> float:
        """Dos casos que tinham divergencia, quantos o produto achou."""
        return self.positivos_achados / self.positivos if self.positivos else 1.0

    @property
    def precisao_nos_negativos(self) -> float:
        """**A metrica que manda.** Dos casos sem divergencia, quantos ficaram limpos."""
        if not self.negativos_e_limpos:
            return 1.0
        return self.negativos_sem_falso_positivo / self.negativos_e_limpos

    @property
    def aprovado(self) -> bool:
        """v0 exige perfeicao nos dois eixos — o conjunto e pequeno e deterministico."""
        return not self.falhas


def rodar(casos: tuple[CasoGolden, ...] | None = None) -> Placar:
    """Roda o golden set e devolve o placar, com a razao de cada falha."""
    casos = casos or golden_set()
    falhas: list[str] = []
    positivos = achados = negativos = limpos_ok = 0

    for caso in casos:
        r: ResultadoReconciliacao = reconciliar(caso.documentos, caso.apuracao)
        tipos = {d.tipo for d in r.divergencias}

        if caso.espera_achado:
            positivos += 1
            faltando = set(caso.tipos_esperados) - tipos
            if faltando:
                falhas.append(
                    f"{caso.id}: esperava {sorted(t.value for t in faltando)}, "
                    f"achou {sorted(t.value for t in tipos)}"
                )
            else:
                achados += 1
        else:
            negativos += 1
            if r.conforme:
                limpos_ok += 1
            else:
                falhas.append(
                    f"{caso.id}: FALSO POSITIVO — deveria ficar limpo, achou "
                    f"{[d.detalhe for d in r.divergencias]}"
                )

    return Placar(
        positivos=positivos,
        positivos_achados=achados,
        negativos_e_limpos=negativos,
        negativos_sem_falso_positivo=limpos_ok,
        falhas=tuple(falhas),
    )
