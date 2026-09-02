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


# --------------------------------------------------------------------------- #
# submeter_a_humano — o passo que a docstring prometia desde o M2
# --------------------------------------------------------------------------- #


def test_o_flow_guarda_o_dossie_quando_ha_arquivo(tmp_path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """Ate o M4a o Flow montava o markdown e jogava fora. Nao havia o que assinar."""
    from abba_crews.core.arquivo import Arquivo
    from abba_crews.core.dossie import EstadoDossie

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", "senha-de-teste")
    arq = Arquivo(tmp_path / "dossies")

    f = SentinelaFlow(fonte=fonte_do("positivo-credito-omitido"), arquivo=arq)
    f.kickoff({"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": "2027-04-20"}})

    assert f.state.registro is not None
    assert f.state.registro.estado is EstadoDossie.RASCUNHO
    assert arq.markdown(f.state.registro) == f.state.markdown


def test_sem_arquivo_o_flow_nao_grava_nada(tmp_path) -> None:  # type: ignore[no-untyped-def]
    """Padrao aditivo, como o classificador: a CLI decide onde as coisas caem."""
    f = roda("positivo-credito-omitido")
    assert f.state.registro is None
    assert f.state.markdown


def test_reexecutar_na_janela_nao_duplica_o_dossie(tmp_path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """Idempotencia com disco: mesmas entradas, mesmo arquivo, nao dois."""
    from abba_crews.core.arquivo import Arquivo

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", "senha-de-teste")
    arq = Arquivo(tmp_path / "dossies")
    for _ in range(3):
        f = SentinelaFlow(fonte=fonte_do("positivo-credito-omitido"), arquivo=arq)
        f.kickoff(
            {"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": "2027-04-20"}}
        )
    assert len(arq.listar()) == 1


def test_dois_dias_geram_dois_dossies_e_nenhum_e_destruido(tmp_path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """A idempotencia era falsa, e o rascunho anterior era apagado.

    A impressao era o hash das ENTRADAS, mas o conteudo depende tambem de `hoje` — dias
    restantes, data de geracao, e ate a `natureza`. Verificado no review de 2026-09-02:
    um dossie de 27/04 dizendo "manifeste-se, faltam 3 dias" era substituido, sob a
    mesma chave, por um de 03/05 dizendo "prazo perdido". Um arquivo no disco, o
    anterior perdido, e duas docstrings minhas mentindo ao mesmo tempo.
    """
    from abba_crews.core.arquivo import Arquivo

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", "senha-de-teste")
    arq = Arquivo(tmp_path / "dossies")

    for hoje in ("2027-04-27", "2027-05-03"):
        f = SentinelaFlow(fonte=fonte_do("positivo-credito-omitido"), arquivo=arq)
        f.kickoff(
            {"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": hoje}}
        )

    registros = arq.listar()
    assert len(registros) == 2, "rodar noutro dia tem de criar registro AO LADO"
    assert len({r.impressao for r in registros}) == 2
    for r in registros:
        assert arq.markdown(r), f"{r.chave} ficou ilegivel — o anterior nao pode sumir"


def test_o_mesmo_dia_continua_idempotente(tmp_path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """A data entrou na chave sem custar a idempotencia dentro da janela do dia."""
    from abba_crews.core.arquivo import Arquivo

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", "senha-de-teste")
    arq = Arquivo(tmp_path / "dossies")
    for _ in range(3):
        f = SentinelaFlow(fonte=fonte_do("positivo-credito-omitido"), arquivo=arq)
        f.kickoff(
            {"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": "2027-04-20"}}
        )
    assert len(arq.listar()) == 1


def test_a_data_padrao_nao_congela_no_import() -> None:
    """`date.today()` como default do Pydantic e avaliado UMA vez, na definicao da classe.

    Num processo longo — que e como o AMP roda — a data envelhecia sozinha. E e ela que
    decide o prazo, a `natureza` e os dias restantes.
    """
    from abba_crews.flows.sentinela_flow import EstadoSentinela

    campo = EstadoSentinela.model_fields["hoje"]
    assert campo.default_factory is not None, (
        "use default_factory=date.today; um default fixo congela a data no import"
    )
