# Arquitetura — as costuras

Detalhe de negócio e o plano por fases: `abba-ops/05-interno/prototipo-patrimonial/produtizacao.md`.

## Fluxo de um caso (ponta a ponta)
```
Profissional (app)                CrewAI AMP (Flow)                 Backend (BFF + Postgres)
   │  novo caso (upload/wizard)                                       │
   │─ POST /api/cases/kickoff ───────────────────────────────────────▶ guarda de orçamento
   │                              ◀─ /kickoff (inputs pseudonimizados) │  (token só aqui)
   │  polling status ────────────▶ /status/{id}                        │
   │                                                                   │
   │                              Flow: gate red flags (código)        │
   │                              → análise/desenho/obrigações         │
   │                              → PAUSA no gate humano ── webhook ───▶ /api/hitl/webhook
   │                                                                   │  cria item na fila
   │  fila de revisão ◀──────────────────────────────────────────────  │  (RLS por tenant)
   │  aprova/edita/rejeita ─ POST /api/hitl/resume ─▶ /resume ────────▶ (reenvia webhookUrl!)
   │                              Flow: Crew de redação → minuta        │
   │  minuta (PDF/DOCX) ◀─────────────────────────────────────────────  render + trilha
```

## As costuras que importam
1. **Token da AMP só no BFF** (`app/src/lib/amp-client.ts`) — nunca no browser.
2. **PII**: mascarada antes do LLM (`flow/.../pii.py`); o de-para vive no backend; o estado do Flow é pseudonimizado (`caso_id`). PII em claro só no Postgres do app, cifrada.
3. **Isolamento de tenant**: `tenant_id` propagado em todo kickoff + **RLS no Postgres** (`app/db/schema.sql`) — não só filtro de aplicação.
4. **HITL**: webhook→fila→`/resume`; a `webhookUrl` é reenviada no resume (a AMP não a carrega do kickoff).
5. **Corpus vivo**: cada chunk carrega `FrescorDoc` (`last_verified`/`supersedes`/`is_current`); job de frescor alerta quando a lei muda.
6. **Custo/LGPD**: guarda de orçamento por caso no BFF (Langfuse por tenant); TTL + job de deleção (`expira_em`).

## O que é stub e por quê
`rag_corpus._buscar` (precisa do corpus ingerido — advogado cura as fontes) · `amp-client` real (precisa das credenciais do AMP) · db/auth/Presidio/Langfuse (Fases 1–2). O que dá para verificar hoje: o Flow compila; os contratos estão fechados.
