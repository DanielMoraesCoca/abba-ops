# Scaffold — Protótipo Patrimonial (CrewAI 1.x)

Esqueleto pronto para implementação (Sprints 1–4 no [plano de construção](../plano-de-construcao.md)). **Nada aqui roda com LLM real ainda** — os stubs marcam exatamente o que falta (`TODO(Sprint N)`).

## Mapa

```
src/patrimonio_flow/
  main.py            # o Flow: intake → gate1 → análise → desenho → obrigações → gate2 humano → redação → render
  schemas.py         # EstadoCaso e todos os contratos (Pydantic) — a fonte da verdade dos dados
  gates.py           # gate 1: triagem de red flags (código puro, testável sem LLM)
  guardrails.py      # anti-citação-órfã, anti-ocultação, seções da minuta
  crews/             # 3 crews (@CrewBase + YAML): análise, desenho (com crítico adversarial), redação
  tools/
    rag_corpus.py    # RAG-como-tool com proveniência (chunk_ids) — NÃO usar Knowledge nativo
    obrigacoes.py    # pacote de obrigações + cenários (determinístico)
eval/
  golden_personas.json  # 12 personas sintéticas com gabarito (validar com advogado nomeado)
  run_eval.py           # runner (camada determinística primeiro)
```

## Regras inegociáveis (antes de escrever qualquer linha)

1. **Memória CrewAI OFF em tudo** (`memory=False`) — a nota de privacidade oficial: conteúdo memorizado é enviado ao LLM/embedder de análise. Dados do caso vivem SÓ no `EstadoCaso` (`@persist`, apagável).
2. **Citação ou abstenção** — claim sem `source_id` recuperado não passa (guardrail); `nao_coberto=true` é resposta válida e vira a seção "limites" da minuta.
3. **Gates são código** — red flags e obrigações nunca viram agente.
4. **Saída é minuta para advogado nomeado** — o rodapé obrigatório não se remove.
5. **PII direta não vai ao provedor** — caso trafega pseudonimizado (`caso_id`); implementar hook `@before_llm_call` de redação no Sprint 1.
6. **`learn=False` no `@human_feedback`** — correções do advogado não entram em memória adaptativa.

## Setup (Sprint 1)

```bash
uv venv && uv pip install -e .
export CREWAI_STORAGE_DIR=./storage        # nunca o default silencioso
export CREWAI_TRACING_ENABLED=true         # tracing AMP desde o dia 1
# embedder EXPLÍCITO na config do RAG (corpus-conhecimento.md §6)
python -m compileall src                    # sanidade
python eval/run_eval.py                     # camada determinística do eval
```

## Ordem de implementação

S1: corpus ingerido + `RagCorpusTool._buscar` real + hook PII → S2: crews análise/desenho + `run_eval` completo (perfis inteiros por persona) + aritmética de cenários → S3: `@human_feedback` com provider async + render DOCX → S4: eval completo com advogado + GO/NO-GO ([métrica](../avaliacao-e-metrica.md)).

Teto de custo por caso: `TETO_USD_POR_CASO` em `main.py` (padrão US$ 5) — medir com `flow.usage_metrics` (agrega todas as crews; não usar o token_usage da última).
