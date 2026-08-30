"""Entrada que a CrewAI executa.

Os nomes `kickoff`, `plot` e `run_with_trigger` sao convencao da CrewAI e estao
declarados em `[project.scripts]` — nao renomear: e por eles que o AMP roda o projeto.

Estado atual (M0): o esqueleto do Flow existe e valida a entrada. Os passos de
coleta, reconciliacao e julgamento chegam em M1–M3 — ate la eles falham alto, de
proposito. Um Flow que finge trabalhar e pior que um que recusa.
"""

from __future__ import annotations

import json
import sys
from typing import Any

from crewai.flow import Flow, listen, start
from pydantic import BaseModel

from abba_crews.core.produtos import Maturidade, por_id


class EstadoSentinela(BaseModel):
    """Estado da conferencia de uma competencia, para um CNPJ."""

    cnpj: str = ""
    competencia: str = ""  # "AAAA-MM"
    entrega_dere: bool = False


class SentinelaFlow(Flow[EstadoSentinela]):
    """Confere a apuracao assistida dentro da janela de manifestacao.

    Nunca transmite ao Fisco: a manifestacao e ato do contribuinte.
    """

    @start()
    def abrir_competencia(self, crewai_trigger_payload: dict[str, Any] | None = None) -> None:
        """Recebe o gatilho (CNPJ + competencia) e valida antes de qualquer custo."""
        payload = crewai_trigger_payload or {}
        self.state.cnpj = str(payload.get("cnpj", "")).strip()
        self.state.competencia = str(payload.get("competencia", "")).strip()
        self.state.entrega_dere = bool(payload.get("entrega_dere", False))

        faltando = [c for c in ("cnpj", "competencia") if not getattr(self.state, c)]
        if faltando:
            raise ValueError(
                f"gatilho incompleto: falta {', '.join(faltando)}. "
                'Esperado: {"cnpj": "...", "competencia": "AAAA-MM"}'
            )

    @listen(abrir_competencia)
    def coletar(self) -> None:
        produto = por_id("sentinela")
        if produto.maturidade is not Maturidade.PRODUCAO:
            raise NotImplementedError(
                f"A Sentinela esta em '{produto.maturidade.value}', nao em producao.\n"
                f"Gate para avancar: {produto.gate}\n"
                "Rode `abba-crews produtos --detalhe` para o estado de cada produto."
            )
        raise NotImplementedError("coleta chega em M6 (API RTC + Distribuicao DF-e)")


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
