"""Portão de CI do gate de conformidade — zero LLM.

Prova que o gate 1 (red flags determinísticos) bate com o gabarito das 12
personas do golden set. É o critério eliminatório nº1 da métrica de GO/NO-GO
(avaliacao-e-metrica.md): um caso de fraude que passa é falha de produto.
"""

from __future__ import annotations

from run_eval import avaliar_gate1  # eval/ é posto no path pelo conftest


def test_gate1_bate_com_todas_as_personas():
    r = avaliar_gate1()
    assert r["total"] == 12
    assert r["ok"] == 12, f"gate divergiu do gabarito: {r['falhas']}"
    assert r["falhas"] == []
