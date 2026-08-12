"""Runner do golden set (stub — Sprint 4).

Camadas de avaliação (avaliacao-e-metrica.md):
1. DETERMINÍSTICA (esta aqui, sem LLM-judge): gate 1 contra gabarito (bloqueado/flags),
   zero citações órfãs, obrigações mínimas presentes, seções da minuta.
2. ESPECIALISTA: advogado nomeado pontua concordância de desenho (rubrica 0-2 por eixo).
3. LLM-judge (só qualidade textual) via crewai.experimental.evaluation.ExperimentRunner.

O gate 1 é testável HOJE sem nenhuma chamada de LLM — é código puro.
"""

from __future__ import annotations

import json
import pathlib

GOLDEN = pathlib.Path(__file__).parent / "golden_personas.json"


def carregar_personas() -> list[dict]:
    return json.loads(GOLDEN.read_text(encoding="utf-8"))["personas"]


def avaliar_gate1() -> dict:
    """Camada 1 parcial: red flags contra gabarito. TODO(Sprint 2): montar
    PerfilEstruturado completo por persona (hoje campos_chave são parciais)."""
    resultados = {"total": 0, "ok": 0, "falhas": []}
    for persona in carregar_personas():
        resultados["total"] += 1
        # TODO: perfil = montar_perfil(persona); report = triagem_red_flags(perfil)
        # comparar report.bloqueado e códigos com persona["gabarito"]
        resultados["falhas"].append(f"{persona['id']}: pendente de montagem de perfil completo")
    return resultados


if __name__ == "__main__":
    print(json.dumps(avaliar_gate1(), indent=2, ensure_ascii=False))
