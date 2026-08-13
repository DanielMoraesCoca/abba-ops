# Arquiteto Patrimonial — Plano de Produtização (protótipo → SaaS B2B)

> **Camada:** interno (estratégia + engenharia). Fonte de verdade de negócio da produtização do [protótipo patrimonial](plano-de-construcao.md). O código do produto vive no **repositório próprio no ar** — `github.com/DanielMoraesCoca/arquiteto-patrimonial` (privado, publicado 2026-08-12) — com uma cópia-espelho staged em [`arquiteto-patrimonial/`](arquiteto-patrimonial/README.md) neste abba-ops. Este documento é o porquê e o quê (ver §10 para o estado da Fase 0).
>
> **Decisão-âncora do sócio (2026-08-12):** o usuário do produto é **o PROFISSIONAL** (advogado / contador / planejador patrimonial), não o consumidor final. "Disponível a qualquer um" = qualquer profissional assina e usa com os clientes dele. Preserva EOAB + modelo centauro. Produto **B2B SaaS**.
>
> Gate: decisão "produto vs. empresa" e qualquer societário seguem gateados no advogado próprio (P4). Moratória do cérebro/portal intocada — produto comercial novo, autorizado.

---

## 1. Por que B2B (a pesquisa confirmou a decisão)

Todos os comparáveis de estate/wealth planning com IA vendem para o **profissional**, não para o leigo — Wealth.com (IA "Ester"), Vanilla, FP Alpha, Luminary, Estateably. A única exceção B2C (Trust & Will) sobrevive porque se declara *"não é escritório de advocacia; formulários self-help; não substitui advogado; sem relação advogado-cliente"*. No Brasil a fronteira é **mais restritiva**: a OAB-RJ representou contra site que vendia petições por IA (exercício ilegal da advocacia; o STJ manteve o site no ar em jun/2025, então a fronteira está em disputa) e a Recomendação OAB 01/2024 afirma que **IA não substitui o advogado**. Entregar desenho/estratégia jurídica direto ao leigo tem exposição a exercício ilegal. **B2B é o caminho seguro e o de maior ticket** — e a razão comercial que sustenta o preço é conhecida: o profissional usa o produto para **reter e crescer a carteira** (planejamento sucessório retém o patrimônio na transição geracional).

## 2. A jornada real do profissional (o produto, ponta a ponta)

1. **Conta e workspace multi-tenant** — o profissional cria conta; `tenant_id` isola tudo dele.
2. **Novo caso → intake híbrido** (o padrão vencedor da pesquisa, não escolher um só):
   - **Upload** dos documentos do cliente (contrato social, IR, estruturas existentes) → extração por IA, com **PII mascarada ANTES do LLM**. É o "aha": o documento vira resumo estruturado em segundos.
   - **OU wizard guiado** (o [questionário de 38 perguntas](questionario-perfil.md) já existe) para casos do zero. Formulário monolítico causa abandono — por isso wizard progressivo.
3. **Gate de conformidade** (determinístico, já construído em `gates.py`): red flags em código; caso bloqueado → relatório ao profissional, sem desenho.
4. **Análise + desenhos + obrigações** — as crews produzem 2–3 estruturas, **cada afirmação com fonte citada** (link para o artigo do corpus, à la Ester), + pacote de obrigações (14.754/DCBE/ITCMD).
5. **Revisão e assinatura (HITL real)** — o Flow pausa; item entra na **fila de revisão** do profissional; ele aprova/edita/rejeita na UI; o Flow retoma. A minuta sai com "revisão e assinatura: [profissional, OAB]".
6. **Entrega + trilha** — minuta em PDF/DOCX no padrão visual, com trilha de auditoria (versão do corpus, fontes, quem aprovou). Documento-fonte **apagado após extração** (padrão FP Alpha).
7. **Retenção** — o caso fica vivo: alertas de **evento de vida** (casamento, filho, novo ativo, liquidez), **mudança de lei** (o corpus vivo dispara "a estrutura X pode ter sido afetada pela norma Y") e **plano desatualizado**. É o que traz o profissional de volta.

## 3. Arquitetura do produto (MVP real)

| Camada | Escolha | Racional (pesquisa) |
|---|---|---|
| **Runtime** | Flow no **CrewAI AMP** (deploy via GitHub) | Herda REST `kickoff/status/resume`, tracing, secrets, HITL webhook, PII-redaction de traces — sem operar infra de agentes no dia 1 |
| **App** | **Next.js + BFF** | AMP dá API, não produto. Bearer token só no backend; polling do status; UI do profissional |
| **Multi-tenancy** | `tenant_id` + **RLS no Postgres** + namespace por tenant no vector store (Qdrant) | Isolamento na infra, não na aplicação (filtro em app é burlável) |
| **PII pré-LLM** | **LiteLLM + Presidio** (mascara CPF/nome/endereço antes do modelo) | A redaction do AMP só cobre *traces*, não o prompt. Resolve o pior risco LGPD |
| **HITL** | webhook do AMP → **fila de revisão** → UI approve/reject/revise → `/resume` (reenviar a webhook URL) | Auditável; o gate do advogado é o coração do modelo centauro |
| **Corpus vivo** | ingestão real + metadados `last_verified`/`supersedes`; uma versão "current" | RAG que não mantém frescor falha quando a lei muda |
| **Observabilidade/custo** | **Langfuse** por `tenant_id` + guarda de orçamento por caso no BFF | LLM domina o custo (~US$0,10–5/execução); sem hard-cap nativo confiável |
| **LGPD mínimo** | TTL + job de deleção por tenant/usuário; retenção declarada | Não há "LGPD nativo"; implementa-se right-to-erasure |

## 4. Lacunas a fechar (protótipo → produto)

**Já existe (scaffold real):** schemas, gates (red flags reais), guardrails (anti-citação-órfã), Flow, 3 crews + YAML, golden set.
**Stub/ausente:** RAG corpus (`_buscar` = NotImplementedError; corpus não ingerido) · hook de PII · aritmética dos cenários · eval runner completo · **front-end real** (a demo é 100% simulada client-side) · auth/multi-tenancy · deploy · HITL UI · retenção/deleção LGPD.

## 5. Fases

| Fase | Foco | Critério de saída |
|---|---|---|
| **0 · Fundação (sem. 1–2)** | repo próprio + implementar stubs (`_buscar` real, **ingerir corpus** — precisa do advogado, hook PII, cenários) + deploy staging no AMP | um caso ponta a ponta com LLM e corpus reais |
| **1 · App + HITL (sem. 3–5)** | Next.js + BFF + auth + RLS; intake upload+wizard; fila de revisão via webhook→`/resume`; render PDF/DOCX | um profissional externo cria conta, roda, revisa e assina |
| **2 · Confiança/conformidade (sem. 6–7)** | citação com link à fonte; disclaimers EOAB (molde Trust & Will); LGPD (TTL/deleção/termos); Langfuse + guarda de custo; corpus vivo v1 | disclaimers e deleção testados; custo por caso medido |
| **3 · Retenção + GO/NO-GO (sem. 8+)** | triggers de evento de vida / mudança de lei; golden set sobre o produto; métrica assinada por advogado | GO/NO-GO de [avaliacao-e-metrica](avaliacao-e-metrica.md) aplicado ao produto → só então pricing e pagantes |

## 6. Modelo de negócio (direção, a confirmar com dado)

**Assinatura por profissional (seat)** como espinha + **por-caso** como porta de baixo comprometimento (espelha FP Alpha: US$1.995/ano OU US$179/caso). Preço ancorado no valor (uma estrutura patrimonial vale muito) e na tabela ABBA. **Naming: decisão de sócios** (doutrina de marca), deferido.

## 7. Guardrails inegociáveis

Modelo centauro (profissional assina) · conformidade-primeiro (red flags em código) · citação-ou-abstenção · **PII nunca crua ao LLM** · LGPD por desenho (deleção comprovável) · **o produto nunca dá conselho jurídico ao leigo** (é ferramenta do profissional; disclaimers EOAB) · corpus só de fonte pública/oficial curada por advogado.

## 8. Dependências humanas

- **Advogado nomeado (gate P4)** — cura o corpus, valida o golden set, é o "profissional de referência" dos disclaimers. **Caminho crítico da Fase 0.**
- **Engenheiro** (implementador CrewAI) — app e deploy.
- **Sócios** — naming, pricing, decisão "produto vs. empresa" pós-GO.

## 9. O que NÃO fazer agora

CrewAI Factory/VPC, login federado corporativo, versionamento em grafo do corpus, RBAC granular, on-prem. Um deployment AMP multi-tenant + isolamento no banco/vector store resolve o MVP; migra-se para Factory só quando um cliente exigir dados na própria infra.

## 10. Estado da Fase 0 (2026-08-12) — o que foi feito nesta rodada

**Bundle do produto montado, versionado e publicado** (38 arquivos). Vive em dois lugares: a cópia-espelho staged em [`arquiteto-patrimonial/`](arquiteto-patrimonial/README.md) neste abba-ops, e agora também no **repo próprio no ar** — `github.com/DanielMoraesCoca/arquiteto-patrimonial` (privado), populado 1:1 em 2026-08-12 por uma sessão-irmã do Claude Code escopada nos dois repos. A raiz do repo é `README.md`/`flow/`/`app/`/`docs/`/`deploy/`, como o deploy do AMP espera. O que entrou:

- **Flow (runtime CrewAI):** o scaffold + os stubs sem-infra **implementados** — aritmética real dos cenários ([`obrigacoes.py`](arquiteto-patrimonial/flow/src/patrimonio_flow/tools/obrigacoes.py): alíquota controlada 15%, rendimento estimado, câmbio e ITCMD por UF, custo tributário × sucessório em horizontes de 5/10 anos com premissas declaradas); **hook de PII pré-LLM** ([`pii.py`](arquiteto-patrimonial/flow/src/patrimonio_flow/pii.py): mascara CPF/CNPJ/e-mail/telefone/RG antes do modelo, de-para só no backend); **metadados de corpus vivo** (`FrescorDoc`: `is_current`/`supersedes`/`last_verified`/`ttl_dias` em `rag_corpus.py`); campos de produto nos schemas (`tenant_id`/`profissional_id`/`teto_usd_caso`). `python -m compileall` limpo.
- **App (Next.js + BFF), esqueleto:** cliente AMP só-backend (`amp-client.ts`, Bearer no servidor), rotas BFF `kickoff`/`status`/`hitl/webhook`/`hitl/resume`, `schema.sql` Postgres com **RLS por `tenant_id`** (via `current_setting('app.tenant_id')`) + nome do cliente cifrado + `expira_em` (TTL LGPD), guarda de orçamento, telas stub de intake e revisão, tipos de domínio.
- **Docs do repo:** `README.md` (fronteira EOAB, guarda-corpos), `docs/ARCHITECTURE.md` (as costuras ponta a ponta), `deploy/amp.md` (deploy do Flow no AMP), `.gitignore` (exclui `.env`/`*.key`/`*.db`/`uploads/`).
- **Guardas:** nada roda com LLM real nem segredo; nenhum PII no bundle; docs passaram no **Revisor** (régua v1.2.1).

**Bloqueio resolvido (2026-08-12):** a criação do repo pela integração desta sessão havia falhado por permissão (403, sem escopo de criar repo); o sócio criou o repo vazio no GitHub e uma **sessão-irmã** (escopada em `arquiteto-patrimonial` + `abba-ops`) subiu o bundle 1:1 para a branch `main`. A cópia-espelho segue aqui no abba-ops como fonte-verdade de negócio; a partir de agora, mudanças no **código** do produto vão no repo próprio, e este pacote de doutrina permanece a referência.

**Deploy no CrewAI AMP — VIVO e validado ao vivo (2026-08-12).** O Flow está deployado (`arquiteto-patrimonial-*.crewai.com`), status Online, endpoints `/healthcheck`·`/inputs`·`/kickoff`·`/status/{id}`. Primeiro caso disparado ao vivo (`POST /kickoff` com um perfil que fere o red flag duro RF6 — `aceite_transparencia:false`): retorno `state:SUCCESS`, `result` = o relatório determinístico `CASO BLOQUEADO … RF6_recusa_transparencia (lei-14754)`, **`usage_metrics:null`** — ou seja, o gate disse "não" ao caso errado **sem gastar LLM**, ao vivo. O caminho determinístico (intake→gate1→relatório) está provado ponta a ponta no deploy real.

**Aprendizados de deploy no AMP (memória de engenharia — o 1º deploy quebrou 2×):**
1. **Working Directory = `flow/`** (monorepo — o `pyproject.toml` não está na raiz do repo).
2. **Projeto Flow precisa de marcação e lock:** `[tool.crewai] type = "flow"` + `[project.scripts]` (`kickoff`/`run_crew`/`plot`) no `pyproject.toml`, e um **`uv.lock`** commitado (gerado com `uv lock`). Sem isso o detector procura o layout de *Crew* (`crew.py`+`config/`) e falha.
3. **Imports absolutos, não relativos:** o runtime do AMP carrega o módulo sem contexto de pacote → `from .` quebra com `ImportError: attempted relative import`. Todo import intra-pacote é `from patrimonio_flow.X import Y`. Verificável instalando o pacote num venv isolado (`uv pip install .`) e importando o entrypoint de fora do `src`.
4. **Kickoff pela rede:** a UI "Test Endpoints" do AMP (formulário de checkbox) **não** expressa objeto aninhado no `perfil` → "Invalid JSON syntax". Usar `POST /kickoff` com corpo `{"inputs":{"perfil":{…}}}` via `curl`. **As sessões Claude não alcançam `*.crewai.com`** (egress da org bloqueia) — disparar do laptop do sócio ou liberar o host na allowlist do environment.

**Único gatilho restante da Fase 0 (caminho crítico):** ingerir o **corpus real** — precisa do **advogado nomeado (Héctor)** curando as fontes. Sem ele, um caso *liberado* (`aceite_transparencia:true`, sem red flags) para no RAG stub (`NotImplementedError`). Depois: rodar um caso liberado ponta a ponta com LLM + corpus reais.

## Ligações

[Plano do protótipo](plano-de-construcao.md) · [Especificação dos agentes](especificacao-agentes.md) · [Questionário](questionario-perfil.md) · [Corpus](corpus-conhecimento.md) · [Avaliação e métrica](avaliacao-e-metrica.md) · [Bundle do produto (espelho)](arquiteto-patrimonial/README.md) · [Scaffold (degrau-2)](scaffold/README.md) · Repo de produto (no ar): `github.com/DanielMoraesCoca/arquiteto-patrimonial` · [Registro de decisões](../registro-de-decisoes.md)

## Fontes da pesquisa (2026-08-12)

Mercado/UX: [wealth.com/ester](https://www.wealth.com/ester/) · [Vanilla pricing](https://www.justvanilla.com/pricing) · [FP Alpha](https://fpalpha.com/pricing/) · [Luminary](https://www.withluminary.com/) · [Estateably](https://www.estateably.com/) · [Trust & Will Terms](https://trustandwill.com/security/terms) · UPL: [OAB-RJ vs. petições IA (ConJur)](https://www.conjur.com.br/2025-abr-29/oab-rj-investiga-venda-online-de-peticoes-feitas-por-ia/) · [STJ mantém site (ConJur)](https://www.conjur.com.br/2025-jun-02/stj-nega-pedido-da-oab-rj-e-mantem-no-ar-site-que-que-vende-peticoes-feitas-por-ia/) · [Estatuto OAB](https://www.oab.org.br/publicacoes/AbrirPDF?LivroId=0000002837)
Engenharia: [CrewAI AMP](https://docs.crewai.com/en/enterprise/introduction) · [API kickoff](https://docs.crewai.com/en/api-reference/kickoff) · [HITL Enterprise](https://docs.crewai.com/en/enterprise/guides/human-in-the-loop) · [CopilotKit AG-UI + CrewAI](https://www.copilotkit.ai/blog/how-to-add-a-frontend-to-any-crewai-agent-using-ag-ui-protocol) · [Presidio + LiteLLM PII](https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2) · [Langfuse ↔ CrewAI](https://langfuse.com/docs/integrations/crewai) · [Knowledge](https://docs.crewai.com/en/concepts/knowledge)
