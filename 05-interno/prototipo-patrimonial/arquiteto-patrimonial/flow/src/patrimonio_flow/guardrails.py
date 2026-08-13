"""Guardrails de task — funções determinísticas (especificacao-agentes.md §4).

Assinatura CrewAI: (TaskOutput) -> tuple[bool, Any]
  (True, resultado)  -> passa (pode transformar)
  (False, feedback)  -> feedback volta ao agente e a task reexecuta (<= guardrail_max_retries)
"""

from __future__ import annotations

import re
from typing import Any, Optional

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

# Fração mínima de termos-de-conteúdo da claim que precisam aparecer nos chunks
# citados. Abaixo disso, o source_id existe mas NÃO sustenta a afirmação
# ("alucinação com cara de citação"): ID real, conteúdo não amparado.
MIN_SUSTENTACAO = 0.30


def _tokens(texto: str) -> list[str]:
    return [t for t in re.split(r"[^0-9a-zà-ú]+", texto.lower()) if len(t) > 3]


def make_anti_citacao_orfa(
    chunks_recuperados: list[str],
    textos: Optional[dict] = None,
    min_sustentacao: float = MIN_SUSTENTACAO,
):
    """Fábrica do guardrail de citação. Três camadas, todas determinísticas:

    1. ABSTENÇÃO ESTRUTURAL — claim sem fonte e sem nao_coberto=true é rejeitada
       (o agente é OBRIGADO a se abster quando o corpus não cobre; abster-se é
       resposta correta, não falha).
    2. ANTI-ÓRFÃ — source_id que não foi recuperado nesta execução é rejeitado.
    3. SUSTENTAÇÃO A NÍVEL DE TRECHO — se `textos` (chunk_id -> texto) for dado,
       a claim precisa compartilhar ao menos `min_sustentacao` dos seus termos
       de conteúdo com o texto dos chunks citados. Pega o caso em que o ID é
       real mas o chunk não ampara a afirmação.
    `textos` é uma referência viva (populada pela RagCorpusTool durante a
    execução); None mantém o comportamento só-ID (retrocompatível)."""

    def anti_citacao_orfa(task_output: Any) -> tuple[bool, Any]:
        modelo = getattr(task_output, "pydantic", None)
        if modelo is None:
            return False, "Output sem modelo Pydantic; produza o schema exigido."
        recuperados = set(chunks_recuperados)
        problemas: list[str] = []
        for claim in getattr(modelo, "claims", []):
            if claim.nao_coberto:
                continue  # abstenção honesta é válida
            # (1) abstenção estrutural
            if not claim.source_ids:
                problemas.append(f"claim sem fonte: '{claim.text[:60]}...' — marque nao_coberto=true")
                continue
            # (2) anti-órfã
            orfaos = [sid for sid in claim.source_ids if sid not in recuperados]
            if orfaos:
                problemas.append(f"source_ids não recuperados nesta execução: {orfaos}")
                continue
            # (3) sustentação a nível de trecho
            if textos:
                base = " ".join(textos.get(sid, "") for sid in claim.source_ids)
                base_toks = set(_tokens(base))
                claim_toks = _tokens(claim.text)
                if claim_toks and base_toks:
                    cobertos = sum(1 for t in claim_toks if t in base_toks)
                    if cobertos / len(claim_toks) < min_sustentacao:
                        problemas.append(
                            f"claim não sustentada pelos chunks citados "
                            f"({cobertos}/{len(claim_toks)} termos): '{claim.text[:60]}...'")
        if problemas:
            return False, (
                "Citações inválidas — cite APENAS chunks fornecidos pela tool de corpus e "
                "só afirme o que o texto deles sustenta; senão marque nao_coberto=true com a "
                "lacuna: " + "; ".join(problemas[:5])
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
