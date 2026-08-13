"""HITL assíncrono — o contrato da fila de revisão do advogado.

Num produto REST, o gate humano NÃO pode bloquear a requisição (se o advogado
fecha a aba, mataria a execução). O padrão é assíncrono: o Flow pausa e persiste
o estado; o backend monta um ITEM DE REVISÃO para o profissional; quando ele
decide, o backend aplica a decisão e retoma o Flow.

Wiring no CrewAI (verificado na 1.15.15): o Flow expõe `from_pending(flow_id)` +
`resume()`/`resume_async()`. O fluxo do app:
  1. kickoff → Flow pausa no gate → webhook do AMP → o BFF cria o item na fila
     (montar_item_revisao).
  2. o profissional aprova/edita/rejeita na UI.
  3. o BFF: aplicar_decisao(...) → Flow.from_pending(flow_id).resume() (reenviando
     a webhookUrl, que a AMP não carrega do kickoff).

Este módulo é a parte DETERMINÍSTICA e testável (montar item + aplicar decisão);
a plumbing de resume é do app/deploy. Nada de LLM aqui.
"""

from __future__ import annotations

DECISOES_VALIDAS = {"aprovado", "rejeitado", "revisar"}


def montar_item_revisao(state) -> dict:
    """O que o advogado vê na fila: os desenhos, obrigações e cenários do caso,
    com o contexto de tenant. Nunca inclui PII crua (o caso é pseudonimizado)."""
    return {
        "caso_id": state.caso_id,
        "tenant_id": state.tenant_id,
        "profissional_id": state.profissional_id,
        "versao_corpus": state.versao_corpus,
        "desenhos": [d.model_dump() for d in state.desenhos],
        "obrigacoes": [o.model_dump() for o in state.obrigacoes],
        "cenarios": [c.model_dump() for c in state.cenarios],
    }


def aplicar_decisao(state, decisao: str, feedback: str = "") -> str:
    """Aplica a decisão do advogado ao estado e devolve o sinal que o Flow deve
    retomar ('aprovado'|'rejeitado'|'revisar'). Valida a decisão (nada de sinal
    inventado). 'aprovado' libera o render (gate_humano_ok)."""
    d = (decisao or "").strip().lower()
    if d not in DECISOES_VALIDAS:
        raise ValueError(f"decisão inválida: {decisao!r} — use {sorted(DECISOES_VALIDAS)}")
    if feedback:
        state.feedback_advogado.append(feedback)
    if d == "aprovado":
        state.gate_humano_ok = True
    return d
