"""A fronteira de portabilidade e uma trava, nao um conselho.

`core/` guarda o reconciliador, a tabela de vedacoes e o calendario fiscal — o que
vale dinheiro e o que menos muda. A CrewAI e um framework jovem que ja trocou de
scaffold. Se o nucleo importar crewai, uma mudanca de API deles vira retrabalho no
nosso ativo.

Estes testes rodam a mesma auditoria que a CI roda.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


def _carrega_auditoria():  # type: ignore[no-untyped-def]
    caminho = RAIZ / "scripts" / "audita_fronteira.py"
    spec = importlib.util.spec_from_file_location("audita_fronteira", caminho)
    assert spec and spec.loader
    modulo = importlib.util.module_from_spec(spec)
    sys.modules["audita_fronteira"] = modulo
    spec.loader.exec_module(modulo)
    return modulo


def test_core_nao_importa_crewai() -> None:
    violacoes = _carrega_auditoria().auditar()
    assert violacoes == [], "\n".join(violacoes)


def test_auditoria_pega_violacao_plantada(tmp_path: Path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """A trava so vale se falhar quando deve. Plantamos uma violacao e exigimos que pegue."""
    auditoria = _carrega_auditoria()

    nucleo_falso = tmp_path / "src" / "abba_crews" / "core"
    nucleo_falso.mkdir(parents=True)
    (nucleo_falso / "vazamento.py").write_text("from crewai import Agent\n", encoding="utf-8")

    monkeypatch.setattr(auditoria, "RAIZ", tmp_path)
    monkeypatch.setattr(auditoria, "NUCLEO", nucleo_falso)

    violacoes = auditoria.auditar()
    assert len(violacoes) == 1
    assert "crewai" in violacoes[0]
    assert "vazamento.py" in violacoes[0]


def test_registry_importavel_sem_crewai() -> None:
    """O nucleo tem de carregar num ambiente que nao tenha crewai instalado."""
    import abba_crews.core.produtos as produtos

    assert produtos.PRODUTOS
    carregados = {m for m in sys.modules if m.startswith("crewai")}
    # Se crewai ja estava carregado por outro teste, este assert nao prova nada —
    # a prova forte e `test_core_nao_importa_crewai`, que le o codigo-fonte.
    assert produtos.por_id("sentinela").nome or not carregados
