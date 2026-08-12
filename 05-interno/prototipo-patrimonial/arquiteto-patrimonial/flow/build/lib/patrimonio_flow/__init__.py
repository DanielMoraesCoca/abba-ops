"""Protótipo ABBA — planejamento patrimonial internacional.

Regras inegociáveis deste código (ver especificacao-agentes.md):
- Saída é minuta PARA advogado nomeado; nunca conselho direto a cliente final.
- Conformidade-primeiro: red flags duros bloqueiam o desenho (gates.py).
- Citação ou abstenção: claim sem source_id recuperado não passa (guardrails.py).
- Memória CrewAI OFF; dados do caso vivem só no estado do Flow.
"""

__version__ = "0.1.0"
