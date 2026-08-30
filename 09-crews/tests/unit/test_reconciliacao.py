"""Testes do reconciliador — o modulo que vale dinheiro.

Tres familias, e a segunda e a que manda:

1. **Positivos** — credito legitimo omitido pela proposta. O produto tem de achar.
2. **Negativos** — o produto tem de **nao** inventar divergencia onde nao ha.
   Falso positivo aqui manda o cliente pleitear o que nao e dele: e pior que falso
   negativo, e por isso a precisao nos negativos e a metrica que manda.
3. **Simetria** — divergencia desfavoravel ao cliente aparece igual. Conferir e calar
   sobre o que pesa contra e divulgacao seletiva.

O teste de propriedade (`test_invariante_*`) e o mais importante do arquivo: uma
apuracao derivada dos proprios documentos tem de produzir ZERO divergencias, para
qualquer conjunto de documentos. Se um dia produzir outra coisa, o reconciliador
regrediu — e o teste pega antes do cliente.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from abba_crews.core.modelos import (
    ApuracaoFisco,
    DocumentoFiscal,
    ItemDocumento,
    LinhaApuracao,
    Papel,
    dinheiro,
)
from abba_crews.core.reconciliacao import (
    Sentido,
    TipoDivergencia,
    apuracao_a_partir_de,
    reconciliar,
)

CNPJ = "00000000000191"
OUTRO_CNPJ = "11444777000161"
COMPETENCIA = "2027-03"


def chave(n: int) -> str:
    """Chave de acesso sintetica de 44 digitos, estavel e distinta por n."""
    return f"{n:044d}"


def item(numero: int, ibs_uf: str, ibs_mun: str, cbs: str) -> ItemDocumento:
    return ItemDocumento(
        numero=numero,
        descricao=f"item {numero}",
        cst="000",
        c_class_trib="000001",
        vbc="1000.00",
        v_ibs_uf=ibs_uf,
        v_ibs_mun=ibs_mun,
        v_cbs=cbs,
    )


def documento(
    n: int, papel: Papel, itens: tuple[ItemDocumento, ...] | None = None
) -> DocumentoFiscal:
    return DocumentoFiscal(
        chave=chave(n),
        papel=papel,
        emitente_cnpj=OUTRO_CNPJ if papel is Papel.ENTRADA else CNPJ,
        destinatario_cnpj=CNPJ if papel is Papel.ENTRADA else OUTRO_CNPJ,
        data_emissao=date(2027, 3, 15),
        itens=itens or (item(1, "1.00", "9.00", "88.00"),),
    )


# --------------------------------------------------------------------------- #
# Familia 2 — negativos: o produto tem de NAO achar o que nao existe
# --------------------------------------------------------------------------- #


def test_apuracao_igual_aos_documentos_nao_gera_divergencia() -> None:
    """O caso limpo. E tambem o caminho barato: zero custo de LLM."""
    docs = (documento(1, Papel.ENTRADA), documento(2, Papel.SAIDA))
    apuracao = apuracao_a_partir_de(docs, CNPJ, COMPETENCIA)

    r = reconciliar(docs, apuracao)

    assert r.conforme
    assert r.divergencias == ()
    assert not r.requer_julgamento
    assert r.itens_conferidos == 2


def test_documento_de_outra_competencia_e_ignorado() -> None:
    """Nota de fevereiro nao pode virar divergencia na apuracao de marco."""
    de_marco = documento(1, Papel.ENTRADA)
    de_fevereiro = DocumentoFiscal(
        chave=chave(2),
        papel=Papel.ENTRADA,
        emitente_cnpj=OUTRO_CNPJ,
        destinatario_cnpj=CNPJ,
        data_emissao=date(2027, 2, 10),
        itens=(item(1, "5.00", "5.00", "50.00"),),
    )
    apuracao = apuracao_a_partir_de((de_marco,), CNPJ, COMPETENCIA)

    r = reconciliar((de_marco, de_fevereiro), apuracao)

    assert r.conforme, "documento fora da competencia nao pode gerar achado"
    assert r.itens_conferidos == 1


def test_diferenca_dentro_da_tolerancia_nao_vira_divergencia() -> None:
    """Centavo de arredondamento entre sistemas nao e divergencia."""
    doc = documento(1, Papel.ENTRADA)
    apuracao = ApuracaoFisco(
        cnpj=CNPJ,
        competencia=COMPETENCIA,
        linhas=(
            LinhaApuracao(
                chave=chave(1), item=1, papel=Papel.ENTRADA, v_ibs="10.00", v_cbs="87.99"
            ),
        ),
    )

    com_folga = reconciliar((doc,), apuracao, tolerancia_brl=Decimal("0.01"))
    sem_folga = reconciliar((doc,), apuracao)

    assert com_folga.conforme
    assert not sem_folga.conforme, "tolerancia zero tem de enxergar o centavo"


def test_tolerancia_negativa_e_recusada() -> None:
    docs = (documento(1, Papel.ENTRADA),)
    apuracao = apuracao_a_partir_de(docs, CNPJ, COMPETENCIA)
    with pytest.raises(ValueError, match="negativa"):
        reconciliar(docs, apuracao, tolerancia_brl=Decimal("-1"))


# --------------------------------------------------------------------------- #
# Familia 1 — positivos: o dinheiro
# --------------------------------------------------------------------------- #


def test_credito_omitido_pela_proposta_e_achado_como_favoravel() -> None:
    """O achado que sustenta o produto: credito que o silencio faria perder."""
    entrada = documento(1, Papel.ENTRADA)
    apuracao = ApuracaoFisco(cnpj=CNPJ, competencia=COMPETENCIA, linhas=())

    r = reconciliar((entrada,), apuracao)

    assert len(r.divergencias) == 1
    d = r.divergencias[0]
    assert d.tipo is TipoDivergencia.CREDITO_OMITIDO
    assert d.sentido is Sentido.FAVORAVEL
    assert d.valor_brl == dinheiro("98.00")  # 1.00 + 9.00 + 88.00
    assert d.chave == chave(1)
    assert r.total_favoravel == dinheiro("98.00")
    assert r.total_desfavoravel == dinheiro("0.00")


def test_credito_a_menor_na_proposta_e_favoravel() -> None:
    """Proposta reconhece menos credito do que o documento comprova."""
    entrada = documento(1, Papel.ENTRADA)
    apuracao = ApuracaoFisco(
        cnpj=CNPJ,
        competencia=COMPETENCIA,
        linhas=(
            LinhaApuracao(
                chave=chave(1), item=1, papel=Papel.ENTRADA, v_ibs="10.00", v_cbs="50.00"
            ),
        ),
    )

    r = reconciliar((entrada,), apuracao)

    d = r.divergencias[0]
    assert d.tipo is TipoDivergencia.VALOR_DIVERGENTE
    assert d.sentido is Sentido.FAVORAVEL
    assert d.valor_brl == dinheiro("38.00")


# --------------------------------------------------------------------------- #
# Familia 3 — simetria: o que pesa contra o cliente aparece igual
# --------------------------------------------------------------------------- #


def test_debito_omitido_e_reportado_como_desfavoravel() -> None:
    """Conferir e calar sobre o que pesa contra e divulgacao seletiva."""
    saida = documento(1, Papel.SAIDA)
    apuracao = ApuracaoFisco(cnpj=CNPJ, competencia=COMPETENCIA, linhas=())

    r = reconciliar((saida,), apuracao)

    d = r.divergencias[0]
    assert d.tipo is TipoDivergencia.DEBITO_OMITIDO
    assert d.sentido is Sentido.DESFAVORAVEL
    assert r.total_desfavoravel == dinheiro("98.00")
    assert r.total_favoravel == dinheiro("0.00")


def test_debito_a_maior_na_proposta_e_favoravel_ao_cliente() -> None:
    """Fisco cobra mais do que o documento sustenta: favoravel contestar."""
    saida = documento(1, Papel.SAIDA)
    apuracao = ApuracaoFisco(
        cnpj=CNPJ,
        competencia=COMPETENCIA,
        linhas=(
            LinhaApuracao(chave=chave(1), item=1, papel=Papel.SAIDA, v_ibs="10.00", v_cbs="150.00"),
        ),
    )

    r = reconciliar((saida,), apuracao)

    d = r.divergencias[0]
    assert d.tipo is TipoDivergencia.VALOR_DIVERGENTE
    assert d.sentido is Sentido.FAVORAVEL
    assert d.valor_brl == dinheiro("62.00")


def test_papel_divergente_nao_e_classificado_como_favoravel() -> None:
    """Entrada de um lado e saida do outro e erro de dado — ninguem chuta o sentido."""
    entrada = documento(1, Papel.ENTRADA)
    apuracao = ApuracaoFisco(
        cnpj=CNPJ,
        competencia=COMPETENCIA,
        linhas=(
            LinhaApuracao(chave=chave(1), item=1, papel=Papel.SAIDA, v_ibs="10.00", v_cbs="88.00"),
        ),
    )

    r = reconciliar((entrada,), apuracao)

    d = r.divergencias[0]
    assert d.tipo is TipoDivergencia.PAPEL_DIVERGENTE
    assert d.sentido is Sentido.INDETERMINADO


def test_documento_desconhecido_na_proposta_e_achado() -> None:
    """Proposta traz nota que a empresa nao escriturou."""
    apuracao = ApuracaoFisco(
        cnpj=CNPJ,
        competencia=COMPETENCIA,
        linhas=(
            LinhaApuracao(chave=chave(9), item=1, papel=Papel.SAIDA, v_ibs="10.00", v_cbs="90.00"),
        ),
    )

    r = reconciliar((), apuracao)

    d = r.divergencias[0]
    assert d.tipo is TipoDivergencia.DOC_DESCONHECIDO
    assert d.sentido is Sentido.DESFAVORAVEL
    assert d.valor_brl == dinheiro("100.00")


# --------------------------------------------------------------------------- #
# Invariantes estruturais
# --------------------------------------------------------------------------- #


def test_toda_divergencia_carrega_a_chave_que_a_comprova() -> None:
    """Achado sem documento apontado nao pode existir — e o guardrail do dossie."""
    docs = (documento(1, Papel.ENTRADA), documento(2, Papel.SAIDA))
    apuracao = ApuracaoFisco(
        cnpj=CNPJ,
        competencia=COMPETENCIA,
        linhas=(
            LinhaApuracao(chave=chave(3), item=1, papel=Papel.SAIDA, v_ibs="1.00", v_cbs="1.00"),
        ),
    )

    r = reconciliar(docs, apuracao)

    assert len(r.divergencias) == 3
    for d in r.divergencias:
        assert len(d.chave) == 44 and d.chave.isdigit()
        assert d.valor_brl > 0, "divergencia sem valor nao ajuda ninguem a decidir"
        assert d.detalhe.strip()


def test_divergencias_saem_ordenadas_por_valor() -> None:
    """O contador tem prazo curto: o R$ maior aparece primeiro."""
    pequeno = documento(1, Papel.ENTRADA, (item(1, "1.00", "1.00", "1.00"),))
    grande = documento(2, Papel.ENTRADA, (item(1, "100.00", "100.00", "100.00"),))
    apuracao = ApuracaoFisco(cnpj=CNPJ, competencia=COMPETENCIA, linhas=())

    r = reconciliar((pequeno, grande), apuracao)

    valores = [d.valor_brl for d in r.divergencias]
    assert valores == sorted(valores, reverse=True)


def test_reconciliar_e_deterministico() -> None:
    """Mesmas entradas, mesma saida — e o que permite reexecutar uma competencia."""
    docs = (documento(1, Papel.ENTRADA), documento(2, Papel.SAIDA))
    apuracao = ApuracaoFisco(cnpj=CNPJ, competencia=COMPETENCIA, linhas=())

    assert reconciliar(docs, apuracao) == reconciliar(docs, apuracao)


def test_nenhum_tipo_estrutural_pede_julgamento() -> None:
    """So CLASSIFICACAO_DUVIDOSA abre a porta do modelo. E o que faz a conta fechar."""
    docs = (documento(1, Papel.ENTRADA), documento(2, Papel.SAIDA))
    apuracao = ApuracaoFisco(
        cnpj=CNPJ,
        competencia=COMPETENCIA,
        linhas=(
            LinhaApuracao(chave=chave(3), item=1, papel=Papel.SAIDA, v_ibs="1.00", v_cbs="1.00"),
        ),
    )

    r = reconciliar(docs, apuracao)

    assert r.divergencias
    assert not r.requer_julgamento


# --------------------------------------------------------------------------- #
# O invariante de propriedade — o teste mais importante do arquivo
# --------------------------------------------------------------------------- #

valores = st.decimals(
    min_value=Decimal("0.00"), max_value=Decimal("99999.99"), places=2, allow_nan=False,
    allow_infinity=False,
)


@st.composite
def documentos(draw: st.DrawFn) -> tuple[DocumentoFiscal, ...]:
    quantos = draw(st.integers(min_value=1, max_value=6))
    docs = []
    for n in range(1, quantos + 1):
        n_itens = draw(st.integers(min_value=1, max_value=4))
        itens = tuple(
            ItemDocumento(
                numero=i,
                cst="000",
                c_class_trib="000001",
                vbc="1000.00",
                v_ibs_uf=str(draw(valores)),
                v_ibs_mun=str(draw(valores)),
                v_cbs=str(draw(valores)),
            )
            for i in range(1, n_itens + 1)
        )
        docs.append(documento(n, draw(st.sampled_from(list(Papel))), itens))
    return tuple(docs)


@settings(max_examples=200, deadline=None)
@given(docs=documentos())
def test_invariante_apuracao_derivada_nao_diverge(docs: tuple[DocumentoFiscal, ...]) -> None:
    """Para QUALQUER conjunto de documentos, a apuracao derivada deles nao diverge.

    Este e o teste que pega regressao silenciosa no coracao do produto. Se ele
    quebrar, o reconciliador passou a inventar divergencia onde nao ha — e um falso
    positivo fiscal manda o cliente pleitear o que nao e dele.
    """
    apuracao = apuracao_a_partir_de(docs, CNPJ, COMPETENCIA)
    r = reconciliar(docs, apuracao)

    assert r.conforme, f"divergencia fantasma: {[d.detalhe for d in r.divergencias]}"
    assert r.total_favoravel == dinheiro("0.00")
    assert r.total_desfavoravel == dinheiro("0.00")


@settings(max_examples=100, deadline=None)
@given(docs=documentos())
def test_invariante_proposta_vazia_acha_tudo(docs: tuple[DocumentoFiscal, ...]) -> None:
    """Proposta vazia: toda linha documentada vira exatamente uma divergencia."""
    apuracao = ApuracaoFisco(cnpj=CNPJ, competencia=COMPETENCIA, linhas=())
    r = reconciliar(docs, apuracao)

    esperado = sum(len(d.itens) for d in docs)
    assert len(r.divergencias) == esperado
    assert r.itens_conferidos == esperado
