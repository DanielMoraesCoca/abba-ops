#!/usr/bin/env python
"""Auditoria de fronteira: `core/` nao pode depender da CrewAI.

Por que existe: o nucleo deterministico (reconciliador, creditabilidade, calendario)
e o ativo que vale dinheiro e o que menos muda. A CrewAI e um framework jovem que
ja trocou de scaffold uma vez. Se o nucleo importar crewai, uma mudanca de API deles
vira retrabalho no nosso ativo — e um dia em que quisermos sair fica caro.

Esta auditoria roda na CI e reprova o build. Nao e conselho: e trava.

Uso:
    python scripts/audita_fronteira.py          # audita e sai 1 se houver violacao
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NUCLEO = RAIZ / "src" / "abba_crews" / "core"

# Pacotes que `core/` nao pode importar, direta ou indiretamente pelo nome do modulo.
PROIBIDOS = frozenset({"crewai", "crewai_tools", "litellm"})


def _modulos_importados(arquivo: Path) -> set[tuple[str, int]]:
    """Devolve {(modulo_raiz, linha)} de todo import do arquivo."""
    arvore = ast.parse(arquivo.read_text(encoding="utf-8"), filename=str(arquivo))
    achados: set[tuple[str, int]] = set()
    for no in ast.walk(arvore):
        if isinstance(no, ast.Import):
            for alias in no.names:
                achados.add((alias.name.split(".")[0], no.lineno))
        elif isinstance(no, ast.ImportFrom):
            # `from . import x` tem module None; import relativo nunca sai do pacote.
            if no.level == 0 and no.module:
                achados.add((no.module.split(".")[0], no.lineno))
    return achados


def auditar() -> list[str]:
    """Devolve a lista de violacoes, vazia se tudo certo."""
    if not NUCLEO.is_dir():
        return [f"diretorio do nucleo nao encontrado: {NUCLEO}"]

    violacoes: list[str] = []
    for arquivo in sorted(NUCLEO.rglob("*.py")):
        for modulo, linha in sorted(_modulos_importados(arquivo)):
            if modulo in PROIBIDOS:
                relativo = arquivo.relative_to(RAIZ)
                violacoes.append(
                    f"{relativo}:{linha}: `core/` importou {modulo!r} — "
                    f"a fronteira de portabilidade proibe isto"
                )
    return violacoes


def main() -> int:
    violacoes = auditar()
    if violacoes:
        print("FRONTEIRA VIOLADA — core/ tem de continuar independente da CrewAI:\n")
        for v in violacoes:
            print(f"  {v}")
        print(
            "\nComo corrigir: mova a logica para core/ (sem crewai) e deixe a crew "
            "chama-la por uma BaseTool fina em src/abba_crews/tools/."
        )
        return 1

    n = len(list(NUCLEO.rglob("*.py")))
    print(f"fronteira intacta: {n} arquivo(s) em core/ sem dependencia de CrewAI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
