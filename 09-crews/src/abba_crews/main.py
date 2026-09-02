"""Entrada que a CrewAI executa.

Os nomes `kickoff`, `plot` e `run_with_trigger` sao convencao da CrewAI e estao
declarados em `[project.scripts]` — nao renomear: e por eles que o AMP roda o projeto.
O `crewai_trigger_payload` no `@start()` e como o AMP passa CNPJ e competencia.

A logica toda mora em `flows/sentinela_flow.py`; este arquivo e so a casca.
"""

from __future__ import annotations

import contextlib
import json
import sys
from typing import Any

from abba_crews.flows.sentinela_flow import SentinelaFlow


def _montar_flow() -> SentinelaFlow:
    """Monta o Flow como a producao precisa dele — nao como um esqueleto vazio.

    Ate 2026-09-02 este arquivo fazia `SentinelaFlow()` puro: sem classificador e sem
    arquivo. Tudo o que o M3a e o M4a construiram — creditabilidade e o gate humano —
    era alcancavel **so pela nossa CLI**, e o entrypoint que a CrewAI executa nao
    conhecia nenhum dos dois. A "casca" tinha divergido do produto inteiro.

    O arquivo so entra se houver senha configurada: sem `ABBA_DB_PASSPHRASE` este
    projeto nao grava dado fiscal em claro, e recusar dentro do AMP e melhor do que
    rodar sem deixar rastro do que foi conferido.

    O classificador segue **desligado** ate a tabela de vedacoes ter linha conferida
    (`docs/PENDENCIAS.md`, P2) — ligado hoje, mandaria todo credito a uma rota que so
    o M3b atende.
    """
    from abba_crews.core.arquivo import Arquivo, RaizInsegura
    from abba_crews.core.cofre import senha_do_ambiente

    arquivo = None
    if senha_do_ambiente():
        with contextlib.suppress(RaizInsegura):
            arquivo = Arquivo()
    return SentinelaFlow(arquivo=arquivo)


def kickoff() -> None:
    _montar_flow().kickoff()


def plot() -> None:
    _montar_flow().plot()


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
    return _montar_flow().kickoff({"crewai_trigger_payload": payload})


if __name__ == "__main__":
    kickoff()
