"""Guarda de custo — estimativa determinística e abort ao estourar o teto. Zero LLM."""

from __future__ import annotations

from patrimonio_flow.main import PRECO_USD_1K_COMPLETION, PRECO_USD_1K_PROMPT, estimar_custo_usd


def test_estimar_custo_zero():
    assert estimar_custo_usd(0, 0) == 0.0


def test_estimar_custo_valores():
    # 1000 prompt + 1000 completion = preço de 1k de cada
    esperado = PRECO_USD_1K_PROMPT + PRECO_USD_1K_COMPLETION
    assert abs(estimar_custo_usd(1000, 1000) - esperado) < 1e-9


def test_estimar_custo_negativos_sao_zero():
    assert estimar_custo_usd(-100, -100) == 0.0


def test_acumulacao_cruza_teto():
    teto = 5.0
    # completion domina o custo; muitos tokens estouram o teto
    acumulado = 0.0
    for _ in range(3):
        acumulado += estimar_custo_usd(50_000, 150_000)
    assert acumulado > teto  # a guarda em _cobrar_custo abortaria aqui
