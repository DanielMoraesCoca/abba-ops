"""O registro de produtos e a defesa contra vender o que nao esta pronto.

Estes testes existem para que a defesa nao possa ser desligada por descuido:
se alguem promover um produto sem preencher o que a promocao exige, a CI reprova.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from abba_crews.core.produtos import PRODUTOS, Maturidade, Produto, listar, por_id, vendaveis

# Os dois produtos que a lei estacionou em 2027, e o motivo de cada um.
# Se este par mudar, alguem mexeu na leitura juridica — e isso e uma decisao,
# nao um refactor. O teste forca a conversa.
ESTACIONADOS_ESPERADOS = {"devolucao", "saude_fornecedor"}


def test_ids_sao_unicos() -> None:
    ids = [p.id for p in PRODUTOS]
    assert len(ids) == len(set(ids)), "id de produto duplicado"


def test_os_sete_produtos_existem() -> None:
    assert len(PRODUTOS) == 7, "a escada da Camada de Caixa tem 7 produtos"


def test_por_id_erra_com_lista_de_validos() -> None:
    with pytest.raises(KeyError, match="sentinela"):
        por_id("inexistente")


@pytest.mark.parametrize("produto", PRODUTOS, ids=lambda p: p.id)
def test_todo_produto_declara_metrica_e_gate(produto: Produto) -> None:
    """Sem metrica nao ha prova; sem gate a maturidade sobe por opiniao."""
    assert produto.metrica.strip(), f"{produto.id} sem metrica"
    assert produto.gate.strip(), f"{produto.id} sem gate de promocao"


def test_estacionados_explicam_o_motivo() -> None:
    """Produto estacionado sem motivo escrito vira produto esquecido."""
    estacionados = {p.id for p in PRODUTOS if p.maturidade is Maturidade.ESTACIONADO}
    assert estacionados == ESTACIONADOS_ESPERADOS

    for p in PRODUTOS:
        if p.maturidade is Maturidade.ESTACIONADO:
            assert p.observacao, f"{p.id} estacionado sem observacao explicando por que"
            assert p.base_legal, f"{p.id} estacionado sem base legal citada"


def test_produto_em_producao_precisa_de_crew_e_flow() -> None:
    """Promover a PRODUCAO sem ter o que roda e a forma mais facil de mentir."""
    for p in PRODUTOS:
        if p.maturidade is Maturidade.PRODUCAO:
            assert p.crew, f"{p.id} em PRODUCAO sem crew declarada"
            assert p.flow, f"{p.id} em PRODUCAO sem flow declarado"


def test_listar_ordena_por_prontidao() -> None:
    ordens = [p.maturidade.ordem() for p in listar()]
    assert ordens == sorted(ordens)


def test_listar_filtra_por_maturidade() -> None:
    estacionados = listar(Maturidade.ESTACIONADO)
    assert {p.id for p in estacionados} == ESTACIONADOS_ESPERADOS


def test_vendaveis_reflete_o_estado_real() -> None:
    """Hoje nenhum produto esta em PRODUCAO. Quando um estiver, este teste muda junto."""
    assert vendaveis() == tuple(p for p in PRODUTOS if p.maturidade is Maturidade.PRODUCAO)


def test_produto_e_imutavel() -> None:
    """Estado de maturidade nao se muda em tempo de execucao."""
    p = por_id("sentinela")
    with pytest.raises(ValidationError):
        p.maturidade = Maturidade.PRODUCAO  # type: ignore[misc]
