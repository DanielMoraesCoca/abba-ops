"""Entrada que a CrewAI executa.

Os nomes `kickoff`, `plot` e `run_with_trigger` sao convencao da CrewAI e estao
declarados em `[project.scripts]` — nao renomear: e por eles que o AMP roda o projeto.
O `crewai_trigger_payload` no `@start()` e como o AMP passa CNPJ e competencia.

A logica toda mora em `flows/sentinela_flow.py`; este arquivo e so a casca.
"""

from __future__ import annotations

import json
import sys
from typing import Any

from abba_crews.flows.sentinela_flow import SentinelaFlow


def kickoff() -> None:
    SentinelaFlow().kickoff()


def plot() -> None:
    SentinelaFlow().plot()


def run_with_trigger() -> Any:
    """Executa o Flow com o payload do gatilho (o caminho que o AMP usa)."""
    if len(sys.argv) < 2:
        raise SystemExit(
            "payload ausente. Uso: run_with_trigger "
            '\'{"cnpj":"...","competencia":"2027-03"}\''
        )
    try:
        payload = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        raise SystemExit(f"payload nao e JSON valido: {e}") from e
    return SentinelaFlow().kickoff({"crewai_trigger_payload": payload})


if __name__ == "__main__":
    kickoff()
