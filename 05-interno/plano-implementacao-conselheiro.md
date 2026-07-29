# Plano de Implementação — Conselheiro Digital (do produto de hoje ao cérebro)

> **Status: PLANO APROVADO EM EXECUÇÃO FASEADA — construção estritamente por gatilho.** Origem (2026-07-29): pedido do sócio — plano real de implementação incorporando as inspirações do Meta-ANN (portar o que funciona; reconstruir certo o que não funciona). Base: [arquitetura do cérebro](arquitetura-cerebro-conselheiro.md) (aprovada) + [estudo](estudo-conselheiro-digital.md) + varredura de código dos 3 repositórios. Pesquisa das big techs consolidada em [estudo-big-techs-company-brain.md](estudo-big-techs-company-brain.md) e **mergeada neste plano em 2026-07-29** (§12: 4 marcadores resolvidos, 8 adições, 3 rejeições conscientes).

## 1. Sumário executivo

O Conselheiro de IA vendido hoje (CAIO fracionário, [produto](../03-comercial/conselheiro-de-ia.md)) não muda. Este plano constrói, por gatilho, o **cérebro que abastece a cadeira**: modelo centauro (IA rascunha → sócio assina → diretoria decide), ciclo dia/noite (ingestão de dia, consolidação/"sonho" de noite, fila de curadoria de manhã), memória em 7 stores sobre Postgres, e a escada de melhoria com gates humanos. Custo-alvo por cérebro: ~US$ 10–40/mês.

## 2. Gatilhos de fase (inalterados — nada se constrói antes)

| Fase | Gatilho | Entrega |
|---|---|---|
| 0 | — (agora) | ✅ **FEITA (2026-07-29)** — fundações no assessment-brain, ver §4 |
| 1 | 1º cliente em manutenção | Dossiê Vivo v1: episódios→fatos, brief mensal rascunhado pela noite |
| 2 | 1º cliente na camada Estratégia | Loop de aprendizado completo (port do legado consertado) + golden set |
| 3 | 3+ clientes | Iris-Empresa lê o cérebro; otimizador semanal em envelope |
| 4 | 10+ clientes | Produto nomeado; diário de calibração como ativo comercial |

## 3. Estado atual (verificado no código, 2026-07-29)

**assessment-brain (vivo, testado — a base):** loop de outcome do vault JÁ real (`src/feedback/outcome-reconciler.js` → confiança empírica Laplace → piso 0,25 em `src/knowledge-vault/query.js`; proveniência `run_pattern_injections`). Ingestão whole-document com FTS5, dedupe SHA-256, redação PII one-way. Runs com `trace_id`/`heartbeat`. **Sem embeddings/chunking** (suficiente até a Fase 1). Suíte 332 testes.

**ABBA legado (fonte de ports — congelado, nunca modificado):**

| Ativo | Saúde | Detalhe decisivo |
|---|---|---|
| `backend/src/core/learning-*` (4 tabelas mig. 118) | ⚠️ real e testado e2e, MAS produtor-sem-consumidor | **nada lê `getActive()` em runtime** — prompt aprovado nunca era usado; scores empurrados à mão |
| MIRIX (mig. 117: 2 tabelas, enum 6 tipos) | ⚠️ API REST lê; camada cognitiva NÃO reidrata no boot | write-through sem hydration = amnésia no restart |
| Hebbiano (`agent_connection_strengths`) | ⚠️ meio-vivo | recompensa→pesos VIVO no agent-runner; pesos→roteamento MORTO (`getBestNextAgent` órfão). 70/30 = performance×conexão |
| crew-spec-compiler | ✅ puro, determinístico, 13 testes | gate `requires_human_approval` em ferramentas de impacto — o melhor ativo |
| Soul (JSONB + sanitização) | ✅ 22 testes | identidade de agente injetável em prompt, anti-injeção |
| eval-store | ❌ só memória | reconstruir persistente |

**abba-portal:** multi-tenant real por `client_code` (RLS staged), `agent_runs` já captura I/O por tenant (o episódio do lado portal), Iris recompõe contexto por request **sem memória de longo prazo**, `events` com allowlist fechada (zero PII).

## 4. Fase 0 — ENTREGUE (assessment-brain, branch `claude/abba-consulting-structure-kdyfga`, commits `8240224` + `e642f57`)

1. **Migração 029 `episodes`** — log append-only por engajamento, 8 tipos fechados, 7 pontos de emissão (ingestão, run início/fim, feedback CLI+API, reconciliação, relatório, overrides). Regra read-path-first cumprida: writer + reader + CLI `abba episodes` + 5 testes no mesmo commit. `recordEpisode` nunca lança (observabilidade não quebra o caminho hospedeiro). Deleção só via cascade do `abba forget`.
2. **Migração 030 `prompt_addenda`** — **a costura de consumo que conserta o gap do legado ANTES do port**: orientação aprovada por cliente é anexada DEPOIS dos prompts canônicos (IP travado jamais tocado — teste de byte-equality garante prompt idêntico com zero addenda). Gate humano: ativar exige nome do aprovador. CLI `abba addenda list|add|approve|retire`. Proveniência: ids ativos gravados no episódio `run.started`. Na Fase 2, o proposer portado vira PRODUTOR de drafts desta tabela — o anti-padrão "produtor-sem-consumidor" fica estruturalmente impossível.
3. **IP preservado**: `docs/ABBA_COMPLETE_ASSESSMENT_FRAMEWORK.md` (1.469 linhas) copiado por conteúdo da branch órfã do ABBA (commit de origem `4fa6814f` no cabeçalho de proveniência).

Critério de pronto: ✅ suíte 332/332 · ✅ migrações reversíveis (down/up) · ✅ ranking-regression intocado · ✅ zero diff em `prompts.js`.

## 5. Fase 1 — Dossiê Vivo v1 (gatilho: 1º cliente em manutenção; ~2 sprints)

- **`facts` bitemporais** (mig. futura): `(sujeito, predicado, objeto, valid_at, invalid_at, learned_at, source_episode_ids, confidence)` + supersessão determinística (fato novo invalida o antigo, nunca apaga). Extractor noturno v1: job batch (LLM médio, 50% off) lê os episódios do dia → extrai fatos atômicos → dedupe → contradição → TTL por tipo (KPI mensal expira no mês seguinte).
- **`profile_blocks`**: JSONB versionado (perfil, estado das 25 dimensões, decisões abertas, recomendações ativas) — só a noite e o sócio escrevem.
- **Brief mensal rascunhado pela noite**, curado pelo sócio (o handoff centauro) — reutiliza `src/report/` como renderizador.
- **`decisions` + `outcomes` como tabelas de 1ª classe** (✅ merge 2026-07-29, padrão action-log da Palantir): recomendado → decidido → implementado → medido, no mesmo substrato dos dados — é o white space que nenhuma empresa da pesquisa cobre, e o alicerce do lock-in legítimo.
- **Brief auto-atualizável** (✅ merge, padrão Briefs do Memory Store): o brief re-renderiza na INGESTÃO, não só na consulta — o one-pager do cliente que se mantém sozinho.
- **Ciclo noturno com teto de gasto e health score** (✅ merge, padrão autopilot/doctor do GBrain): todo job autônomo roda com `--max-usd`; o pipeline do assessment-brain já tem o padrão de budget para reutilizar.
- **Classificador na porta da ingestão** (✅ merge, lição Hyper): só entra o que merece memória — nunca espelhar caixa/workspace inteiros (ingest-tudo mata a confiança no cérebro).
- **Ponto de decisão Postgres**: o `connection.js` foi escrito para essa troca (convenção async). Migrar quando o Dossiê nascer OU adiar — decidir no gatilho. **Busca** (✅ pesquisa resolvida): FTS5 atual até o corpus real provar insuficiente; aí, híbrido pgvector+FTS com RRF, **config de português obrigatória** (unaccent + stemmer pt — receita documentada no GBrain), SEM reranker cross-encoder até a escala exigir.
- **Cadência de extração de fatos** (✅ pesquisa resolvida): noturna em batch (API 50% off) + disparo por importância — evento de decisão consolida na mesma noite; KPI de rotina espera o passe (padrão Memory Bank event-sourced + dream cycle).

## 6. Fase 2 — o loop de aprendizado completo (gatilho: camada Estratégia; ~2–3 sprints)

Port do legado COM os consertos (padrão, não código literal — SQLite/convenções da casa):

- `learning-store` + as 4 tabelas (mig.-118-equivalente) → **produtores de `prompt_addenda`**: o proposer gera DRAFT de addendum; `abba addenda approve` é o gate; o uplift compara runs antes/depois da versão ativa. O gap do `getActive` não pode voltar: o caminho de leitura já existe desde a Fase 0.
- `reward`/`run-reward` → **alimentados pelos episódios `run.completed`** (payload já carrega custo/erros/duração) — conserta o "score empurrado à mão" do legado.
- **Soul** portado: identidade do Conselheiro por cliente (JSONB + sanitização anti-injeção, 22 testes viajam juntos).
- **eval-store reconstruído persistente** + golden set por cliente (20–50 casos congelados com saída aprovada pelo sócio) — nenhuma versão promove sem ≥ campeão no golden set + holdout nunca visto.
- **Scoring de insights** (✅ pesquisa resolvida): contrato de evidência em todo resultado (por que casou + confiança de existência), juiz-LLM calibrado contra ~50 notas dos sócios (família de modelo diferente do gerador, posições trocadas), reconciliação empírica do vault como verdade final; o esboço takes/calibração Brier do GBrain fica como referência da F4.

## 7. Fase 3 — o cérebro fala e roteia (gatilho: 3+ clientes; ~2 sprints)

- **crew-spec-compiler portado como está** (13 testes juntos; o gate `requires_human_approval` vira padrão do runtime CrewAI da Construção).
- **MIRIX-equivalente reconstruído** sobre `facts`+`insights` (enum de 6 tipos aproveitado como taxonomia; reidratação POR DESENHO: `profile_blocks` carregados a cada sessão — teste de restart obrigatório).
- **Iris-Empresa** no portal lê o cérebro com citação e abstenção (padrões do portal: `client_code`, allowlist de eventos, budget cap) — **com ACL como coluna + trim-at-retrieval** (✅ merge, consenso das 6 empresas pesquisadas: permissão é dado filtrado na consulta, nunca índice por usuário).
- **Dois verbos** (✅ merge, padrão GBrain): `search` (retrieval cru, barato) × `think` (síntese + citações + **análise de lacunas** — "o cérebro está cego nas dimensões 12, 17, 23"; a lacuna vira ferramenta de scoping do próximo engajamento).
- Escada degrau 1: otimizador semanal em envelope declarado (GEPA-like funciona com ~10 exemplos), digest para os sócios.
- **Onboarding botmaster** (✅ merge, prática GBrain): nunca dar acesso frio a usuário do cliente — pré-popular a fatia dele + conduzir 3 fluxos-uau ao vivo antes de liberar ("vira a taxa de conversão"; e é exatamente o formato de entrega de uma consultoria).
- **Compactação de profile_blocks** (✅ pesquisa resolvida): split `compiled_truth` × `timeline` (a melhor ideia de schema do GBrain) — a crença atual compilada separada da evidência append-only; decaimento gradual, nunca deleção.

## 8. Fase 4 — parqueado até precisar

**Hebbiano**: só se houver roteamento multi-agente real em produção — e portando o CONSERTO (fechar a aresta pesos→roteamento, o lado morto do legado). Produto nomeado + curva de calibração (Brier) como ativo de marketing = decisão de sócios.

## 9. A matriz porta / conserta / reconstrói

| Ativo legado | Veredito | Fase | Conserto necessário |
|---|---|---|---|
| crew-spec-compiler | porta como está | 3 | nenhum |
| Soul (JSONB + sanitize) | porta como está | 2 | nenhum |
| learning-store (mig. 118) | porta com conserto | 2 | consumo via `prompt_addenda` (seam já entregue na Fase 0) |
| prompt-proposer | porta com conserto | 2 | saída vira draft de addendum + gate humano nomeado |
| reward / run-reward | porta com conserto | 2 | alimentado por episódios `run.completed`, não manual |
| eval-store | reconstrói | 2 | persistência (era só memória) |
| MIRIX (mig. 117) | reconstrói | 1+3 | vira `facts` bitemporal + `insights`; reidratação por desenho |
| Hebbiano | parqueia | 4 | aresta pesos→roteamento morta; fechar se/quando houver multi-agente |
| Validação (`Math.random`) | reconstrói | 2 | golden set + reconciler (já existe) + citação verificável |
| Multi-tenancy | já existe certo | — | portal `client_code` + RLS staged |

## 10. Estimativas

Fase 0: **1 sprint — entregue**. Fase 1: 2 sprints. Fase 2: 2–3 sprints. Fase 3: 2 sprints. Fase 4: não estimar (gatilho distante). Cada fase só começa no gatilho e termina com o critério: **suíte verde + teste de restart + golden set ≥ campeão**.

## 11. Riscos e gates invioláveis

- **Byte-equality dos prompts canônicos** (teste em `test/unit/prompt-addenda.test.js`) — o IP 25/25 nunca muda por caminho lateral.
- **Aprovação sempre nomeada** (addenda, overrides) — a trilha que defende o assessment e o PL 2338.
- **Append-only × LGPD**: episódios nunca editados; deleção SÓ pelo cascade do `abba forget` (testado).
- **O avaliador é intocável**: golden sets, ranking-regression e gates ficam fora do alcance de qualquer loop de melhoria (lição Darwin Gödel Machine).
- **Nunca fine-tuning por cliente**; modelo-base congelado, aprendizado só em artefatos versionados.
- **Nunca mutação de memória mediada por LLM** (✅ confirmado pela pesquisa: o Mem0 recuou publicamente de update/delete-via-LLM para ADD-only — corrompia em silêncio): append + invalidação temporal + consolidação em batch com promoção gateada.

## 12. Protocolo de merge do estudo das big techs — ✅ EXECUTADO (2026-07-29)

Os 4 marcadores `⏳PESQUISA` foram resolvidos e 8 adições entraram nas fases (marcadas "✅ merge" acima), por decisão do sócio. A tabela completa de candidatos — incluindo os 3 **rejeitados conscientemente** (markdown-em-git como system of record, embedding fine-tunado por cliente, conectores live) e o porquê — está na seção final do [estudo](estudo-big-techs-company-brain.md). Zero marcador pendente.
