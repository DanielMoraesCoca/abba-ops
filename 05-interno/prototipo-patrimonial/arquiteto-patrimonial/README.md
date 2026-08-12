# Arquiteto Patrimonial

Ferramenta **B2B** de apoio ao **profissional** (advogado / contador / planejador patrimonial) para desenhar planejamento patrimonial internacional — **100% declarado e tributado**, com fonte citada e riscos atacados antes de chegar à mesa do profissional. A IA propõe; **o profissional revisa e assina**.

> **Naming:** `arquiteto-patrimonial` é o nome de trabalho do repositório. O nome comercial do produto é decisão de sócios (deferido).
>
> **Doutrina e plano de negócio:** vivem no `abba-ops` — [`produtizacao.md`](https://github.com/DanielMoraesCoca/abba-ops) e o pacote `prototipo-patrimonial/` (plano, corpus, avaliação, fronteira). Este repo é o **código do produto**.

## O que este produto NÃO faz (fronteira EOAB)
Não dá conselho jurídico ao leigo. É ferramenta do profissional habilitado, que assina cada saída. Sem essa assinatura, a minuta é apenas apoio. (Caminho B2B — o mesmo dos comparáveis Wealth.com/Vanilla; o B2C direto ao consumidor cruzaria o exercício ilegal da advocacia no Brasil.)

## Estrutura
```
flow/   — o runtime CrewAI (Flow: intake → gate de red flags → análise → desenho → obrigações → gate humano → minuta). Deploya no CrewAI AMP.
app/    — Next.js + BFF: contas multi-tenant, intake (upload/wizard), fila de revisão do advogado (HITL), render da minuta.
deploy/ — como deployar o Flow no AMP.
docs/   — arquitetura e costuras.
```

## Estado (Fase 0 — fundação)
**Implementado:** gate de red flags (código), guardrails, aritmética dos cenários, hook de PII pré-LLM, metadados de corpus vivo, schemas de produto (tenant/caso/fila), esqueleto do app + BFF (kickoff/status/webhook/resume) + `schema.sql` com RLS.
**Stub / próximos gatilhos:** ingerir o corpus real (precisa do advogado curando as fontes) · deploy no AMP (precisa das credenciais) · auth/Postgres/Presidio/Langfuse reais (Fases 1–2) · rodar com LLM real.

## Como verificar agora (sem infra, sem segredos)
```bash
cd flow && python -m compileall src   # o Flow compila
```
O corpus real, o deploy e as chaves são os próximos gatilhos — ver [`deploy/amp.md`](deploy/amp.md) e [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Guarda-corpos inegociáveis
Modelo centauro (profissional assina) · conformidade-primeiro (red flags em código) · citação-ou-abstenção · **PII nunca crua ao LLM** · LGPD por desenho (TTL/deleção) · corpus só de fonte pública/oficial curada por advogado.
