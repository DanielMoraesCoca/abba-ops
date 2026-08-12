"""Guardrails de task — funções determinísticas (especificacao-agentes.md §4).

Assinatura CrewAI: (TaskOutput) -> tuple[bool, Any]
  (True, resultado)  -> passa (pode transformar)
  (False, feedback)  -> feedback volta ao agente e a task reexecuta (<= guardrail_max_retries)
"""

from __future__ import annotations

import re
from typing import Any

# Padrões de linguagem de ocultação — bloqueiam SEMPRE (conformidade-primeiro).
PADROES_PROIBIDOS = [
    r"sem\s+aparecer",
    r"fora\s+do\s+radar",
    r"n[aã]o\s+declarar",
    r"em\s+nome\s+de\s+terceiro",
    r"laranja",
    r"ocult(ar|a[cç][aã]o)",
    r"invis[ií]vel\s+ao\s+fisco",
]


def make_anti_citacao_orfa(chunks_recuperados: list[str]):
    """Fábrica: guardrail que rejeita claims citando chunk_id não recuperado nesta execução."""

    def anti_citacao_orfa(task_output: Any) -> tuple[bool, Any]:
        modelo = getattr(task_output, "pydantic", None)
        if modelo is None:
            return False, "Output sem modelo Pydantic; produza o schema exigido."
        recuperados = set(chunks_recuperados)
        orfas: list[str] = []
        for claim in getattr(modelo, "claims", []):
            if claim.nao_coberto:
                continue  # abstenção honesta é válida
            if not claim.source_ids:
                orfas.append(f"claim sem fonte: '{claim.text[:60]}...'")
                continue
            for sid in claim.source_ids:
                if sid not in recuperados:
                    orfas.append(f"source_id '{sid}' não foi recuperado nesta execução")
        if orfas:
            return False, (
                "Citações inválidas — cite APENAS chunks fornecidos pela tool de corpus, "
                "ou marque nao_coberto=true com a lacuna: " + "; ".join(orfas[:5])
            )
        return True, task_output

    return anti_citacao_orfa


def sem_linguagem_de_ocultacao(task_output: Any) -> tuple[bool, Any]:
    """Rejeita qualquer output com linguagem de ocultação patrimonial."""
    texto = str(getattr(task_output, "raw", "") or "")
    for padrao in PADROES_PROIBIDOS:
        if re.search(padrao, texto, flags=re.IGNORECASE):
            return False, (
                f"Linguagem de ocultação detectada (padrão: {padrao}). "
                "Este sistema desenha apenas estruturas integralmente declaradas e tributadas. "
                "Reescreva em termos de conformidade."
            )
    return True, task_output


def minuta_tem_secoes_obrigatorias(task_output: Any) -> tuple[bool, Any]:
    """Minuta final: seções fixas + rodapé obrigatório presentes."""
    modelo = getattr(task_output, "pydantic", None)
    if modelo is None:
        return False, "Produza MinutaFinal (output_pydantic)."
    corpo = modelo.corpo_markdown.lower()
    faltando = [s for s in ("limites", "fontes", "obriga") if s not in corpo]
    if faltando:
        return False, f"Minuta sem seções obrigatórias: {faltando}"
    if not modelo.limites_da_analise:
        return False, "limites_da_analise vazio — toda minuta declara seus limites."
    return True, task_output
