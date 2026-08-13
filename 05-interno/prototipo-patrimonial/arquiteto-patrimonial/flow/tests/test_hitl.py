"""HITL assíncrono — montagem do item de revisão e aplicação da decisão. Zero LLM."""

from __future__ import annotations

import pytest

from patrimonio_flow.hitl import aplicar_decisao, montar_item_revisao
from patrimonio_flow.schemas import (
    DesenhoEstrutura, EstadoCaso, ObrigacaoItem, PacoteObrigacoes,
)


def _estado():
    st = EstadoCaso(caso_id="c1", tenant_id="t1", profissional_id="p1",
                    versao_corpus="corpus-demo")
    st.desenhos = [DesenhoEstrutura(nome="Holding + conta declarada", elementos=[],
                                    sequencia_implantacao=["passo 1"],
                                    custo_manutencao_anual_estimado_brl=10000.0,
                                    trade_offs="simples")]
    st.obrigacoes = [PacoteObrigacoes(desenho_nome="Holding + conta declarada",
                                      itens=[ObrigacaoItem(obrigacao="DCBE anual",
                                                           fundamento_doc_id="demo-dcbe",
                                                           prazo="anual", recorrencia="anual")])]
    return st


def test_item_revisao_tem_desenhos_e_tenant():
    item = montar_item_revisao(_estado())
    assert item["caso_id"] == "c1"
    assert item["tenant_id"] == "t1"
    assert len(item["desenhos"]) == 1
    assert item["obrigacoes"][0]["desenho_nome"] == "Holding + conta declarada"


def test_aprovar_libera_render():
    st = _estado()
    assert st.gate_humano_ok is False
    sinal = aplicar_decisao(st, "aprovado", feedback="ok, ajustar cláusula X")
    assert sinal == "aprovado"
    assert st.gate_humano_ok is True
    assert st.feedback_advogado == ["ok, ajustar cláusula X"]


def test_rejeitar_nao_libera_render():
    st = _estado()
    sinal = aplicar_decisao(st, "rejeitado")
    assert sinal == "rejeitado"
    assert st.gate_humano_ok is False


def test_revisar_volta():
    st = _estado()
    assert aplicar_decisao(st, "revisar", "detalhar cenário 10 anos") == "revisar"
    assert st.gate_humano_ok is False
    assert st.feedback_advogado == ["detalhar cenário 10 anos"]


def test_decisao_invalida_recusada():
    with pytest.raises(ValueError):
        aplicar_decisao(_estado(), "talvez")
