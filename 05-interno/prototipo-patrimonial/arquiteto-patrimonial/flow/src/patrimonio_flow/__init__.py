"""Protótipo ABBA — planejamento patrimonial internacional.

Regras inegociáveis deste código (ver especificacao-agentes.md):
- Saída é minuta PARA advogado nomeado; nunca conselho direto a cliente final.
- Conformidade-primeiro: red flags duros bloqueiam o desenho (gates.py).
- Citação ou abstenção: claim sem source_id recuperado não passa (guardrails.py).
- Memória CrewAI OFF; dados do caso vivem só no estado do Flow.
"""

import os as _os

# Modelo padrão: Claude Sonnet (a conexão de LLM do AMP é Anthropic). Sonnet
# segue "cite ou abstenha" com muito mais rigor que o haiku — essencial para o
# guardrail anti-citação-órfã não rejeitar a análise. Sem isto o CrewAI cai no
# default OpenAI e falha por falta de OPENAI_API_KEY.
# setdefault → uma env MODEL explícita no deploy ainda sobrescreve (ex.: haiku
# para reduzir custo em etapas menos sensíveis).
_os.environ.setdefault("MODEL", "anthropic/claude-sonnet-4-5")

__version__ = "0.1.0"
