# Deploy do Flow no CrewAI AMP

O runtime dos agentes NÃO roda no nosso servidor — roda no **CrewAI AMP**, que expõe o Flow como API REST. O app (Next.js/BFF) chama essa API.

## Passos (próximo gatilho — precisa das credenciais)
1. Push deste repo para o GitHub (feito).
2. No AMP: **Connect GitHub** → selecionar este repo → apontar o projeto do Flow (`flow/`).
3. Setar **env vars/secrets** no AMP: chave do provedor de LLM, config do vector store (Qdrant, namespace por tenant), Langfuse.
4. Deploy (10–15 min no primeiro). Ganha-se: `POST /kickoff`, `GET /status/{id}`, `POST /resume`, tracing, PII-redaction de traces, HITL webhook.
5. Copiar a URL do deployment (`https://<flow>.crewai.com`) e o **Bearer token** para o `.env` do app (`AMP_BASE_URL`, `AMP_BEARER_TOKEN`) — **só no backend**.

## Guarda-corpos que já estão no código do Flow
- Gate de red flags determinístico (`gates.py`) — barato, sem LLM.
- Guardrails anti-citação-órfã e anti-linguagem-de-ocultação.
- Hook de PII pré-LLM (`pii.py`) — mascara antes do provedor (a redaction do AMP só cobre traces).
- `EstadoCaso` carrega `tenant_id`/`profissional_id`/`teto_usd_caso`.

## O que fica no app, não no AMP
Auth/contas, Postgres com RLS (tenants/casos/fila de revisão), a UI de intake e de revisão do advogado, o de-para de PII (nunca no LLM), o TTL/deleção LGPD, e a guarda de orçamento por caso.

## Alternativa (só quando um cliente exigir dados na própria infra)
CrewAI **Factory** (containerizado no VPC/região do cliente) — mesmo runtime, self-hosted. Overengineering para o MVP; não fazer agora.
