"""A classificacao de creditabilidade — e a regra de seguranca que a desenha.

Ate o M3a o par (CST, cClassTrib) era carregado, validado como nao-vazio e **lido por
ninguem**: o produto achava divergencia estrutural e nao dizia uma palavra sobre se o
credito era legitimo. `CLASSIFICACAO_DUVIDOSA` existia no enum e nada a construia — a
rota de julgamento do Flow era codigo morto.

O que estes testes travam, em ordem de importancia:

1. **codigo desconhecido nunca vira creditavel** — presumir creditabilidade de um par
   que nao conhecemos e o falso positivo fiscal, que manda o cliente pleitear o que nao
   e dele e cria passivo onde nao havia;
2. **linha `a_confirmar` nao decide** — indicio levantado nao e dispositivo conferido;
3. **sem classificador nada muda** — o M2 inteiro continua valendo.
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path

import pytest
from hypothesis import given
from hypothesis import strategies as st
from pydantic import ValidationError

from abba_crews.core.creditabilidade import (
    TABELA_PADRAO,
    Classificacao,
    Regra,
    TabelaCreditabilidade,
    Veredito,
    carregar,
)
from abba_crews.core.reconciliacao import TipoDivergencia, reconciliar
from abba_crews.core.sinteticos import TABELA_ENSAIO, golden_set

# --------------------------------------------------------------------------- #
# 1. A regra de seguranca
# --------------------------------------------------------------------------- #

VAZIA = TabelaCreditabilidade(versao="vazia", fonte="teste", regras=())


def test_par_desconhecido_e_duvidoso() -> None:
    c = VAZIA.classificar("000", "000001")
    assert c.veredito is Veredito.DUVIDOSO
    assert c.requer_julgamento


def test_tabela_vazia_nunca_decide_nada() -> None:
    """Com tabela vazia TUDO e duvidoso. Nao e defeito — e o estado real do saber."""
    for cst, ct in (("000", "000001"), ("999", "999999"), ("020", "200001")):
        assert VAZIA.classificar(cst, ct).veredito is Veredito.DUVIDOSO


@given(
    cst=st.text(alphabet="0123456789", min_size=1, max_size=4),
    ct=st.text(alphabet="0123456789", min_size=1, max_size=8),
)
def test_propriedade_par_fora_da_tabela_jamais_e_creditavel_ou_vedado(cst: str, ct: str) -> None:
    """A propriedade que sustenta o produto inteiro: sem regra, sem afirmacao."""
    conhecidos = {(r.cst, r.c_class_trib) for r in TABELA_ENSAIO.regras}
    cst_com_curinga = {r.cst for r in TABELA_ENSAIO.regras if r.curinga}
    if (cst, ct) in conhecidos or cst in cst_com_curinga:
        return
    assert TABELA_ENSAIO.classificar(cst, ct).veredito is Veredito.DUVIDOSO


# --------------------------------------------------------------------------- #
# 2. a_confirmar: indicio nao e decisao
# --------------------------------------------------------------------------- #


def _regra(**kw: object) -> Regra:
    base: dict[str, object] = {
        "cst": "000",
        "c_class_trib": "000001",
        "veredito": Veredito.CREDITAVEL,
        "razao": "razao de teste",
        "doc": "fonte de teste",
    }
    base.update(kw)
    return Regra.model_validate(base)


def test_linha_a_confirmar_rebaixa_para_duvidoso() -> None:
    t = TabelaCreditabilidade(
        versao="t", fonte="teste", regras=(_regra(a_confirmar=True),)
    )
    c = t.classificar("000", "000001")
    assert c.veredito is Veredito.DUVIDOSO, (
        "linha marcada a_confirmar nao pode decidir: foi levantada, nao conferida"
    )
    assert "a_confirmar" in c.razao
    assert t.ativas == () and len(t.pendentes) == 1


def test_linha_conferida_decide() -> None:
    t = TabelaCreditabilidade(versao="t", fonte="teste", regras=(_regra(),))
    assert t.classificar("000", "000001").veredito is Veredito.CREDITAVEL


def test_regra_com_veredito_duvidoso_e_recusada() -> None:
    """DUVIDOSO e o que sobra, nao o que se declara — senao a duvida vira regra."""
    with pytest.raises(ValidationError, match="DUVIDOSO"):
        _regra(veredito=Veredito.DUVIDOSO)


# --------------------------------------------------------------------------- #
# 3. Curinga e integridade da tabela
# --------------------------------------------------------------------------- #


def test_regra_exata_vence_curinga() -> None:
    """Sem esta precedencia, uma generalizacao ampla apagaria excecao conferida."""
    t = TabelaCreditabilidade(
        versao="t",
        fonte="teste",
        regras=(
            _regra(c_class_trib="*", veredito=Veredito.CREDITAVEL),
            _regra(c_class_trib="000123", veredito=Veredito.VEDADO, razao="excecao"),
        ),
    )
    assert t.classificar("000", "000999").veredito is Veredito.CREDITAVEL
    assert t.classificar("000", "000123").veredito is Veredito.VEDADO


def test_par_repetido_reprova_a_tabela() -> None:
    """Tabela contraditoria e pior que vazia: a vazia declara duvida."""
    with pytest.raises(ValidationError, match="repetido"):
        TabelaCreditabilidade(versao="t", fonte="teste", regras=(_regra(), _regra()))


def test_classificacao_sempre_carrega_fonte() -> None:
    for t in (VAZIA, TABELA_ENSAIO):
        c: Classificacao = t.classificar("abc", "def")
        assert c.fonte.strip(), "veredito sem fonte e opiniao disfarcada de fato"
        assert c.razao.strip()


# --------------------------------------------------------------------------- #
# 4. A tabela que vai no pacote
# --------------------------------------------------------------------------- #


def test_tabela_do_pacote_carrega() -> None:
    t = carregar()
    assert t.versao and t.fonte and t.nota


def test_nenhuma_linha_decide_enquanto_a_fonte_disser_A_CONFERIR() -> None:
    """A trava contra o pior desfecho possivel deste marco.

    Se alguem tirar `a_confirmar` de uma linha cuja fonte ainda diz "A CONFERIR", o
    produto passa a afirmar creditabilidade com a confianca de uma tabela e a base de
    um levantamento. Fechar a P2 significa trocar a citacao pela conferida — nunca
    apenas apagar a marca.
    """
    for r in carregar().regras:
        if "A CONFERIR" in r.doc.upper():
            assert r.a_confirmar, (
                f"CST {r.cst}/{r.c_class_trib}: a fonte ainda diz A CONFERIR e a linha "
                f"esta decidindo. Ver docs/PENDENCIAS.md, P2."
            )


def test_toda_linha_da_tabela_do_pacote_cita_fonte() -> None:
    for r in carregar().regras:
        assert r.doc.strip(), "linha sem fonte nao entra na tabela"


def test_tabela_malformada_falha_alto(tmp_path: Path) -> None:
    ruim = tmp_path / "ruim.json"
    ruim.write_text("{isto nao e json", encoding="utf-8")
    with pytest.raises(ValueError, match="malformada"):
        carregar(ruim)


def test_tabela_ausente_falha_alto(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        carregar(tmp_path / "nao-existe.json")


def test_json_do_pacote_e_o_mesmo_que_o_modelo_le() -> None:
    """Guarda contra chave escrita errada no JSON e ignorada em silencio."""
    bruto = json.loads(TABELA_PADRAO.read_text(encoding="utf-8"))
    assert set(bruto) <= {"versao", "fonte", "nota", "regras"}
    assert len(bruto["regras"]) == len(carregar().regras)


# --------------------------------------------------------------------------- #
# 5. Integracao com o reconciliador
# --------------------------------------------------------------------------- #


def _caso(caso_id: str):  # type: ignore[no-untyped-def]
    return next(c for c in golden_set() if c.id == caso_id)


def test_cst_vedado_nao_vira_divergencia_e_aparece_como_descarte() -> None:
    c = _caso("negativo-cst-vedado")
    r = reconciliar(c.documentos, c.apuracao, classificador=TABELA_ENSAIO)
    assert r.divergencias == (), "credito vedado nao pode virar pleito"
    assert len(r.descartados) == 1
    d = r.descartados[0]
    assert d.fonte.strip() and d.razao.strip()
    assert r.total_descartado == Decimal("100.00")


def test_credito_descartado_nao_infla_o_total_favoravel() -> None:
    """O R$ que abre o dossie tem de ser o R$ que se vai pleitear, e nada alem."""
    c = _caso("negativo-cst-vedado")
    r = reconciliar(c.documentos, c.apuracao, classificador=TABELA_ENSAIO)
    assert r.total_favoravel == Decimal("0.00")


def test_cst_desconhecido_abre_a_rota_de_julgamento() -> None:
    c = _caso("positivo-cst-desconhecido")
    r = reconciliar(c.documentos, c.apuracao, classificador=TABELA_ENSAIO)
    assert r.requer_julgamento
    assert {d.tipo for d in r.divergencias} == {TipoDivergencia.CLASSIFICACAO_DUVIDOSA}
    assert r.cobertura < 1.0


def test_sem_classificador_o_comportamento_do_m2_e_preservado() -> None:
    """O parametro e aditivo: sem ele, byte a byte o que o M2 fazia."""
    for c in golden_set():
        r = reconciliar(c.documentos, c.apuracao)
        assert r.descartados == ()
        assert not r.requer_julgamento
        assert r.cobertura == 1.0


def test_classificador_nao_toca_em_saida() -> None:
    """Debito omitido nao depende de direito a credito — depende de ter havido operacao."""
    c = _caso("positivo-debito-omitido-desfavoravel")
    com = reconciliar(c.documentos, c.apuracao, classificador=VAZIA)
    sem = reconciliar(c.documentos, c.apuracao)
    assert com.divergencias == sem.divergencias
    assert com.descartados == ()


def test_credito_creditavel_segue_como_credito_omitido() -> None:
    c = _caso("positivo-credito-omitido")
    r = reconciliar(c.documentos, c.apuracao, classificador=TABELA_ENSAIO)
    assert {d.tipo for d in r.divergencias} == {TipoDivergencia.CREDITO_OMITIDO}
    assert not r.requer_julgamento
