"""O Flow ponta a ponta. Unico arquivo de teste que importa crewai — core/ nao pode."""

from __future__ import annotations

import pytest

from abba_crews.core.sinteticos import golden_set
from abba_crews.flows.sentinela_flow import Fonte, SentinelaFlow

CNPJ = "00000000000191"
COMP = "2027-03"


def fonte_do(caso_id: str) -> Fonte:
    c = next(x for x in golden_set() if x.id == caso_id)
    return Fonte(documentos=c.documentos, apuracao=c.apuracao, origem=f"golden:{caso_id}")


def roda(caso_id: str, hoje: str = "2027-04-20") -> SentinelaFlow:
    f = SentinelaFlow(fonte=fonte_do(caso_id))
    f.kickoff({"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": hoje}})
    return f


def test_gatilho_incompleto_falha_antes_de_qualquer_custo() -> None:
    with pytest.raises(ValueError, match="competencia"):
        SentinelaFlow().kickoff({"crewai_trigger_payload": {"cnpj": CNPJ}})


def test_sem_fonte_recusa_citando_o_gate_do_m6() -> None:
    """Recusa honesta: um Flow que finge trabalhar e pior que um que recusa."""
    with pytest.raises(NotImplementedError, match="M6"):
        SentinelaFlow().kickoff(
            {"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP}}
        )


def test_ponta_a_ponta_produz_dossie_rascunho() -> None:
    f = roda("positivo-credito-omitido")
    assert f.state.dossie is not None
    assert f.state.markdown.startswith("# RASCUNHO")
    assert "R$ 100,00" in f.state.markdown


def test_caminho_sem_divergencia_tambem_produz_dossie() -> None:
    f = roda("limpo-proposta-bate")
    assert f.state.resultado is not None and f.state.resultado.conforme
    assert "Nada a manifestar" in f.state.markdown


def test_idempotencia_mesma_entrada_mesma_chave_e_mesmo_dossie() -> None:
    """Reexecutar uma competencia durante a janela nao pode mudar o documento."""
    a, b = roda("positivo-credito-omitido"), roda("positivo-credito-omitido")
    assert a.state.chave_execucao == b.state.chave_execucao
    assert a.state.markdown == b.state.markdown


def test_entrada_diferente_muda_a_chave_de_execucao() -> None:
    a, b = roda("positivo-credito-omitido"), roda("positivo-debito-omitido-desfavoravel")
    assert a.state.chave_execucao != b.state.chave_execucao


def test_config_do_cliente_entra_no_dossie() -> None:
    f = roda("positivo-credito-omitido")
    assert f.state.config is not None
    assert f.state.config.aprovacao.responsavel_nome in f.state.markdown


def test_fora_do_prazo_o_dossie_muda_de_natureza() -> None:
    dentro = roda("positivo-credito-omitido", hoje="2027-04-20")
    fora = roda("positivo-credito-omitido", hoje="2027-05-10")
    assert "Registro de perda" in fora.state.markdown
    assert "Registro de perda" not in dentro.state.markdown


# --------------------------------------------------------------------------- #
# A rota de julgamento — codigo morto ate o M3a
# --------------------------------------------------------------------------- #


def test_rota_de_julgamento_e_alcancavel_e_recusa_citando_o_m3b() -> None:
    """A regressao mais importante deste marco.

    Ate o M3a `decidir_rota` podia devolver "julgamento" e **nada** conseguia
    dispara-la: `requer_julgamento` nunca era verdadeiro porque ninguem construia uma
    divergencia de classificacao duvidosa. Construir a crew de julgamento antes disto
    teria sido construir agentes para uma rota que nada alcanca.

    Se este teste voltar a passar por acidente — porque parou de levantar — a rota
    virou codigo morto de novo.
    """
    from abba_crews.core.sinteticos import TABELA_ENSAIO

    f = SentinelaFlow(fonte=fonte_do("positivo-cst-desconhecido"), classificador=TABELA_ENSAIO)
    with pytest.raises(NotImplementedError, match="M3b"):
        f.kickoff({"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP}})


def test_cst_vedado_nao_vai_a_julgamento_e_produz_dossie() -> None:
    """Vedado e resposta, nao duvida: resolve na regra e nao custa modelo."""
    from abba_crews.core.sinteticos import TABELA_ENSAIO

    f = SentinelaFlow(fonte=fonte_do("negativo-cst-vedado"), classificador=TABELA_ENSAIO)
    f.kickoff({"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": "2027-04-20"}})
    assert f.state.resultado is not None and len(f.state.resultado.descartados) == 1
    assert "Descartados e por que" in f.state.markdown


def test_sem_classificador_nenhum_caso_do_golden_set_vai_a_julgamento() -> None:
    """O padrao desligado e o que mantem o M2 inteiro valido — e e deliberado."""
    from abba_crews.core.sinteticos import golden_set as _gs

    for caso in _gs():
        f = SentinelaFlow(fonte=fonte_do(caso.id))
        f.kickoff(
            {"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": "2027-04-20"}}
        )
        assert f.state.markdown, f"{caso.id} terminou sem dossie"
