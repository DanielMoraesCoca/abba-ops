# Plano de Implementação: Conselheiro Digital (do produto de hoje ao cérebro)

> **Status: PLANO APROVADO EM EXECUÇÃO FASEADA: construção estritamente por gatilho.** Origem (2026-07-29): pedido do sócio: plano real de implementação incorporando as inspirações do Meta-ANN (portar o que funciona; reconstruir certo o que não funciona). Base: [arquitetura do cérebro](arquitetura-cerebro-conselheiro.md) (aprovada) + [estudo](estudo-conselheiro-digital.md) + varredura de código dos 3 repositórios. Pesquisa das big techs consolidada em [arquivo/estudo-big-techs-company-brain.md](arquivo/estudo-big-techs-company-brain.md) e **mergeada neste plano em 2026-07-29** (§12: 4 marcadores resolvidos, 8 adições, 3 rejeições conscientes).

## 1. Sumário executivo

O Conselheiro de IA vendido hoje (CAIO fracionário, [produto](../03-comercial/conselheiro-de-ia.md)) não muda. Este plano constrói, por gatilho, o **cérebro que abastece a cadeira**: modelo centauro (IA rascunha → sócio assina → diretoria decide), ciclo dia/noite (ingestão de dia, consolidação/"sonho" de noite, fila de curadoria de manhã), memória bitemporal com autoridade de origem e consolidação em tiers, e a escada de melhoria com gates humanos. Custo-alvo por cérebro: ~US$ 10–40/mês.

## 2. Gatilhos de fase (inalterados: nada se constrói antes)

| Fase | Gatilho | Entrega |
|---|---|---|
| 0 | (agora) | ✅ **FEITA (2026-07-29)**: fundações no assessment-brain, ver §4 |
| 1 | ~~1º cliente em manutenção~~ **ANTECIPADA por decisão do sócio** | ✅ **FEITA (2026-07-30)**: Dossiê Vivo v1 construído e testado (ver §5); o gatilho original passa a marcar a ATIVAÇÃO com dados reais, não a construção |
| 2 | ~~1º cliente na camada Estratégia~~ **ANTECIPADA por decisão do sócio** | ✅ **FEITA (2026-07-30)**: loop de aprendizado + soul construídos (ver §6); a CALIBRAÇÃO do golden set (notas dos sócios sobre saídas reais) continua gateada no cliente real |
| 3 | 3+ clientes | Iris-Empresa lê o cérebro; otimizador semanal em envelope |
| 4 | 10+ clientes | Produto nomeado; diário de calibração como ativo comercial |

## 3. Estado atual (verificado no código, 2026-07-29)

**assessment-brain (vivo, testado: a base):** loop de outcome do vault JÁ real (`src/feedback/outcome-reconciler.js` → confiança empírica Laplace → piso 0,25 em `src/knowledge-vault/query.js`; proveniência `run_pattern_injections`). Ingestão whole-document com FTS5, dedupe SHA-256, redação PII one-way. Runs com `trace_id`/`heartbeat`. **Sem embeddings/chunking** (suficiente até a Fase 1). *(Estado de 2026-07-29. Hoje: suíte 429/429 nos 2 modos, migrações 029–047, Fases 0–2 + Ondas 1–3 entregues.)*

**ABBA legado (fonte de ports: congelado, nunca modificado):**

| Ativo | Saúde | Detalhe decisivo |
|---|---|---|
| `backend/src/core/learning-*` (4 tabelas mig. 118) | ⚠️ real e testado e2e, MAS produtor-sem-consumidor | **nada lê `getActive()` em runtime**: prompt aprovado nunca era usado; scores empurrados à mão |
| MIRIX (mig. 117: 2 tabelas, enum 6 tipos) | ⚠️ API REST lê; camada cognitiva NÃO reidrata no boot | write-through sem hydration = amnésia no restart |
| Hebbiano (`agent_connection_strengths`) | ⚠️ meio-vivo | recompensa→pesos VIVO no agent-runner; pesos→roteamento MORTO (`getBestNextAgent` órfão). 70/30 = performance×conexão |
| crew-spec-compiler | ✅ puro, determinístico, 13 testes | gate `requires_human_approval` em ferramentas de impacto: o melhor ativo |
| Soul (JSONB + sanitização) | ✅ 22 testes | identidade de agente injetável em prompt, anti-injeção |
| eval-store | ❌ só memória | reconstruir persistente |

**abba-portal:** multi-tenant real por `client_code` (RLS staged), `agent_runs` já captura I/O por tenant (o episódio do lado portal), Iris recompõe contexto por request **sem memória de longo prazo**, `events` com allowlist fechada (zero PII).

## 4. Fase 0: ENTREGUE (assessment-brain, branch `claude/abba-consulting-structure-kdyfga`, commits `8240224` + `e642f57`)

1. **Migração 029 `episodes`:** log append-only por engajamento, 8 tipos fechados, 7 pontos de emissão (ingestão, run início/fim, feedback CLI+API, reconciliação, relatório, overrides). Regra read-path-first cumprida: writer + reader + CLI `abba episodes` + 5 testes no mesmo commit. `recordEpisode` nunca lança (observabilidade não quebra o caminho hospedeiro). Deleção só via cascade do `abba forget`.
2. **Migração 030 `prompt_addenda`:** **a costura de consumo que conserta o gap do legado ANTES do port**: orientação aprovada por cliente é anexada DEPOIS dos prompts canônicos (IP travado jamais tocado. Teste de byte-equality garante prompt idêntico com zero addenda). Gate humano: ativar exige nome do aprovador. CLI `abba addenda list|add|approve|retire`. Proveniência: ids ativos gravados no episódio `run.started`. Na Fase 2, o proposer portado vira PRODUTOR de drafts desta tabela: o anti-padrão "produtor-sem-consumidor" fica estruturalmente impossível.
3. **IP preservado**: `docs/ABBA_COMPLETE_ASSESSMENT_FRAMEWORK.md` (1.469 linhas) copiado por conteúdo da branch órfã do ABBA (commit de origem `4fa6814f` no cabeçalho de proveniência).

Critério de pronto: ✅ suíte 332/332 (à época) · ✅ migrações reversíveis (down/up) · ✅ ranking-regression intocado · ✅ zero diff em `prompts.js`.

## 5. Fase 1 (Dossiê Vivo v1) ✅ ENTREGUE ANTECIPADA (2026-07-30, commit `28f85f6` na branch)

> Decisão do sócio (porta de 2 vias): construir antes do gatilho: o código não depende de cliente para existir, só para gerar valor; será exercitado no Cliente Zero e ativado com dados reais no 1º cliente em manutenção. Tudo abaixo está construído, testado (suíte 348/348 em modo mock E com criptografia at rest) e com smoke de CLI completo (ingest → sleep → facts → decision → health → brief → forget).

- **`facts` bitemporais** (migrações 032/038/040/041, entregues): `(sujeito, predicado, objeto, valid_at, invalid_at, learned_at, source_episode_ids, confidence)` + supersessão determinística (fato novo invalida o antigo, nunca apaga). Extractor noturno v1: job batch (LLM médio, 50% off) lê os episódios do dia → extrai fatos atômicos → dedupe → contradição → TTL por tipo (KPI mensal expira no mês seguinte).
- **`profile_blocks`**: JSONB versionado (perfil, estado das 25 dimensões, decisões abertas, recomendações ativas): só a noite e o sócio escrevem.
- **Brief mensal rascunhado pela noite**, curado pelo sócio (o handoff centauro): reutiliza `src/report/` como renderizador.
- **`decisions` + `outcomes` como tabelas de 1ª classe** (✅ merge 2026-07-29, padrão action-log da Palantir): recomendado → decidido → implementado → medido, no mesmo substrato dos dados: é o white space que nenhuma empresa da pesquisa cobre, e o alicerce do lock-in legítimo.
- **Brief auto-atualizável** (✅ merge, padrão Briefs do Memory Store): o brief re-renderiza na INGESTÃO, não só na consulta: o one-pager do cliente que se mantém sozinho.
- **Ciclo noturno com teto de gasto e health score** (✅ merge, padrão autopilot/doctor do GBrain): todo job autônomo roda com `--max-usd`; o pipeline do assessment-brain já tem o padrão de budget para reutilizar.
- **Classificador na porta da ingestão** (✅ merge, lição Hyper): só entra o que merece memória, nunca espelhar caixa/workspace inteiros (ingest-tudo mata a confiança no cérebro).
- **Ponto de decisão Postgres**: o `connection.js` foi escrito para essa troca (convenção async). Migrar quando o Dossiê nascer OU adiar: decidir no gatilho. **Busca** (✅ pesquisa resolvida): FTS5 atual até o corpus real provar insuficiente; aí, híbrido pgvector+FTS com RRF, **config de português obrigatória** (unaccent + stemmer pt: receita documentada no GBrain), SEM reranker cross-encoder até a escala exigir.
- **Cadência de extração de fatos** (✅ pesquisa resolvida): noturna em batch (API 50% off) + disparo por importância: evento de decisão consolida na mesma noite; KPI de rotina espera o passe (padrão Memory Bank event-sourced + dream cycle).

## 6. Fase 2 (o loop de aprendizado completo) ✅ ENTREGUE ANTECIPADA (2026-07-30, commits `795013f` + `611595c`)

> Decisão do sócio (porta de 2 vias). Construído: `learning_feedback` (verdicts nomeados; reject produz DRAFT de addendum no seam da Fase 0 + eval case de regressão), `run_scores` (reward determinístico da telemetria do run: conserta o "score empurrado à mão"), `uplift` por proveniência (runs com o addendum × runs antes dele), `soul` por cliente (sanitizado anti-injeção, injetado no brief). CLI `abba learn feedback|scores|uplift|cases|soul`. **E a re-análise adversarial das Fases 0–2 encontrou e corrigiu 13 defeitos confirmados** (fato antigo sobrescrevendo verdade atual, KPI reconfirmado expirando, abort de budget re-pagando chunks, approve de brief sem efeito, vazamento de addendum entre firmas, mutação cross-cliente de decisão, etc.): todos com trava de regressão em `review-regressions.test.js`. Suíte 361/361 nos 2 modos. O que RESTA gateado no cliente real: calibração do golden set com notas dos sócios.

Port do legado COM os consertos (padrão, não código literal: SQLite/convenções da casa):

- `learning-store` + as 4 tabelas (mig.-118-equivalente) → **produtores de `prompt_addenda`**: o proposer gera DRAFT de addendum; `abba addenda approve` é o gate; o uplift compara runs antes/depois da versão ativa. O gap do `getActive` não pode voltar: o caminho de leitura já existe desde a Fase 0.
- `reward`/`run-reward` → **alimentados pelos episódios `run.completed`** (payload já carrega custo/erros/duração): conserta o "score empurrado à mão" do legado.
- **Soul** portado: identidade do Conselheiro por cliente (JSONB + sanitização anti-injeção, 22 testes viajam juntos).
- **eval-store reconstruído persistente** + golden set por cliente (20–50 casos congelados com saída aprovada pelo sócio): nenhuma versão promove sem ≥ campeão no golden set + holdout nunca visto.
- **Scoring de insights** (✅ pesquisa resolvida): contrato de evidência em todo resultado (por que casou + confiança de existência), juiz-LLM calibrado contra ~50 notas dos sócios (família de modelo diferente do gerador, posições trocadas), reconciliação empírica do vault como verdade final; o esboço takes/calibração Brier do GBrain fica como referência da F4.

## 7. Fase 3: o cérebro fala e roteia (gatilho: 3+ clientes; ~2 sprints)

- **crew-spec-compiler portado como está** (13 testes juntos; o gate `requires_human_approval` vira padrão do runtime CrewAI da Construção).
- **MIRIX-equivalente reconstruído** sobre `facts`+`insights` (enum de 6 tipos aproveitado como taxonomia; reidratação POR DESENHO: `profile_blocks` carregados a cada sessão. Teste de restart obrigatório).
- **Iris-Empresa** no portal lê o cérebro com citação e abstenção (padrões do portal: `client_code`, allowlist de eventos, budget cap): **com ACL como coluna + trim-at-retrieval** (✅ merge, consenso das 6 empresas pesquisadas: permissão é dado filtrado na consulta, nunca índice por usuário).
- **Dois verbos** (✅ merge, padrão GBrain): `search` (retrieval cru, barato) × `think` (síntese + citações + **análise de lacunas**: "o cérebro está cego nas dimensões 12, 17, 23"; a lacuna vira ferramenta de scoping do próximo engajamento).
- Escada degrau 1: otimizador semanal em envelope declarado (GEPA-like funciona com ~10 exemplos), digest para os sócios.
- **Onboarding botmaster** (✅ merge, prática GBrain): nunca dar acesso frio a usuário do cliente: pré-popular a fatia dele + conduzir 3 fluxos-uau ao vivo antes de liberar ("vira a taxa de conversão"; e é exatamente o formato de entrega de uma consultoria).
- **Compactação de profile_blocks** (✅ pesquisa resolvida): split `compiled_truth` × `timeline` (a melhor ideia de schema do GBrain): a crença atual compilada separada da evidência append-only; decaimento gradual, nunca deleção.

## 7b. As Ondas de Memória: merge do [estudo de memória agêntica](arquivo/estudo-memoria-agentica.md) (2026-07-30)

A estratégia de adoção das melhorias de memória, casada com os gatilhos para nunca construir produtor sem consumidor:

| Onda | Gatilho | Itens | Status |
|---|---|---|---|
| **1: Blindagem** | AGORA (antes do 1º cliente: docs de cliente = input não-confiável) | **Autoridade de origem** (origem fraca nunca superseda verdade forte, nem pela era expirada, nem retrodatando o passado; claim vira 'contested' inerte, visível no sleep e em `abba brain facts --contested`, resolvível por humano nomeado via `abba brain fact --by`) + **certificado de deleção comprovável** no `abba forget` (mede o schema vivo + arquivos em disco; retenção por design declarada) | ✅ **ENTREGUE (2026-07-30, `b4f0aa1`) + endurecida pela re-análise rodada 4 (2026-07-31, `586a450`, migração 040, suíte 378/378)** |
| **2: Fortalecimento** | Ativação (1º cliente): **antecipada por decisão do sócio** | **Reforço uso+outcome**: cada decisão nasce com o retrato dos fatos que a informaram; resultado medido `better` renova o TTL e sobe a confiança (teto 0,95), resultado `worse` só abre dúvida para o humano (nunca rebaixa verdade em silêncio) + **score de consolidação** portado do legado com os 3 defeitos corrigidos (recência × sobrevivência como variáveis independentes, score recalculado no portão, ledger de promoção efetivamente escrito) e tiers working→consolidated→bedrock + **ganho informacional** como telemetria (saturação avisa, nunca bloqueia escrita) | ✅ **ENTREGUE (2026-08-01, migrações 041–045, suíte 413/413) + endurecida pela re-análise rodada 5 (8 defeitos)** |
| **3: Prova** | Escala (3+ clientes): **antecipada por decisão do sócio** | **Auditoria noturna**: sondas de consistência bitemporal determinísticas e grátis toda noite (rotuladas coerência, NUNCA "acurácia") + sondas de grounding pagas opt-in (`--audit-grounding-usd`) que comparam o fato com o texto-fonte; a auditoria é leitura e jamais derruba a noite + **tier procedural**: playbooks rascunhados só de vitórias medidas, ativados por humano nomeado + **benchmark longitudinal** (`abba brain benchmark`): acerto da memória contra o tempo de casa: o artefato publicável | ✅ **ENTREGUE (2026-08-01) + endurecida pela re-análise rodada 5** |

**Comandos novos**: `abba brain audit` · `abba brain benchmark --json` · `abba brain reconfirm` · `abba brain playbook [--approve --by]` · `abba brain sleep [--audit-grounding-usd]`. O brief mensal ganhou 4 seções determinísticas: **R$ verificado no período** (baseline → medido, total só de pares numéricos: o to-do do [estudo financeiro](estudo-ia-financeira.md)), reconfirmações recomendadas, playbooks aprovados e rodapé de auditoria/saturação. Saúde do cérebro passou a 9 componentes (soma 100) com `audit_pass` e `memory_reinforcement`.

## 8. Fase 4: parqueado até precisar

**Hebbiano**: só se houver roteamento multi-agente real em produção, e portando o CONSERTO (fechar a aresta pesos→roteamento, o lado morto do legado). Produto nomeado + curva de calibração (Brier) como ativo de marketing = decisão de sócios.

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
| Multi-tenancy | já existe certo |  | portal `client_code` + RLS staged |

## 10. Estimativas

Fase 0: **1 sprint: entregue**. Fase 1: 2 sprints. Fase 2: 2–3 sprints. Fase 3: 2 sprints. Fase 4: não estimar (gatilho distante). Cada fase só começa no gatilho e termina com o critério: **suíte verde + teste de restart + golden set ≥ campeão**.

## 11. Riscos e gates invioláveis

- **Byte-equality dos prompts canônicos** (teste em `test/unit/prompt-addenda.test.js`): o IP 25/25 nunca muda por caminho lateral.
- **Aprovação sempre nomeada** (addenda, overrides): a trilha que defende o assessment e o PL 2338.
- **Append-only × LGPD**: episódios nunca editados; deleção SÓ pelo cascade do `abba forget` (testado).
- **O avaliador é intocável**: golden sets, ranking-regression e gates ficam fora do alcance de qualquer loop de melhoria (lição Darwin Gödel Machine).
- **Nunca fine-tuning por cliente**; modelo-base congelado, aprendizado só em artefatos versionados.
- **Nunca mutação de memória mediada por LLM** (✅ confirmado pela pesquisa: o Mem0 recuou publicamente de update/delete-via-LLM para ADD-only: corrompia em silêncio): append + invalidação temporal + consolidação em batch com promoção gateada.

## 12. To-do de oferta: "Resgate de IA" (decisão do sócio, 2026-07-31)

- [ ] **Lançar o "Resgate de IA"**: a única mudança de empacotamento aprovada por ora, vinda do [estudo de mercado](arquivo/estudo-mercado-ofertas.md): auditoria forense do piloto de IA que falhou (preço fixo, 2–3 semanas) → sprint de reconstrução. Reusa a máquina das 25 dimensões com o frame "por que falhou"; pitch pronto (externo acerta 2×: MIT); zero concorrência empacotada no BR. Passos: (1) one-pager comercial em `03-comercial/`, (2) roteiro de auditoria forense mapeado sobre as 25 dimensões, (3) preço na tabela (proposta v2, sócios), (4) alimentar o Conselheiro com cada resgate (episódios `run.completed` + facts de "por que falhou").
- As **outras 4 mudanças de empacotamento** do estudo (portas avulsas, máx. 3 visíveis, recorrência como centro, governança/Conselheiro re-precificado) permanecem **candidatas: pauta de sócios**, sem execução por ora.

## 13. Protocolo de merge do estudo das big techs: ✅ EXECUTADO (2026-07-29)

Os 4 marcadores `⏳PESQUISA` foram resolvidos e 8 adições entraram nas fases (marcadas "✅ merge" acima), por decisão do sócio. A tabela completa de candidatos: incluindo os 3 **rejeitados conscientemente** (markdown-em-git como system of record, embedding fine-tunado por cliente, conectores live) e o porquê: está na seção final do [estudo](arquivo/estudo-big-techs-company-brain.md). Zero marcador pendente.

## 14. Conselheiro Vertical: ✅ SPRINT 1–3 ENTREGUES (2026-08-04, decisão do sócio "tudo agora", V3g)

O upgrade que unifica a visão do Conselheiro sobre TUDO o que a ABBA produz: construído fora da sequência de gatilhos por decisão explícita do sócio (contrariando conscientemente a moratória de engenharia do conselho consultivo; registrado em V3g).

| Bloco | O que é | Estado |
|---|---|---|
| **A: O Revisor** | Gate determinístico de doutrina ([régua](../06-ferramentas/regua-do-revisor.md)) + pass LLM de coerência com a memória (consultivo, nunca bloqueia sozinho). `abba revise` + `abba report --revise` + episódio `revisor.reviewed` (migração 048) | ✅ código + testes |
| **B: Instância ABBA** | O Cliente Zero do próprio produto: nossas decisões viram diário com gatilho, ciclo noturno com LLM real mede custo (R20) e valida extração (R17) | ✅ [runbook](abba-interna-runbook.md) · ⬜ sócios rodam 4 semanas |
| **C: Portal→cérebro** | Snapshot AGREGADO do portal (rota staff nova) → `abba portal import` → fatos `tool_output` com TTL mensal (snapshot velho expira e cobra re-sync). Autoridade de origem preservada (humano nunca é sobrescrito: testado) | ✅ código + testes nos 2 repos |
| **D: Outside view** | Vault semeado com 10 padrões curados DOS NOSSOS estudos (`scripts/seed-market-patterns.js`), tags `market_research`+fonte: o Stage 0 já injeta como priors desde o cliente 1, declarado como pesquisa | ✅ |
| **E: Memória→análise** | `formatFactsBlock` atrás de `ABBA_INJECT_FACTS` (default OFF): fatos human_stated/client_doc ≥0,8, máx 10, byte-equality preservada com flag off (testado) | ✅ construído · 🔒 ligar só após eval com flag |
| **Gateado (3+ clientes)** | Voz visível "O que o Conselheiro observa" nos relatórios (decisão do sócio: interna primeiro) + verbos search/think da Fase 3 | 🔒 |

Suíte: **443/443 nos dois modos** (429 + 14 novos). Guard-rails intocados: segregação por engajamento, prompts canônicos byte-idênticos, gate humano nomeado, pisos 5/5 do benchmark, nunca dado bruto entre clientes: o "topo da montanha" vê os dados DA ABBA + agregados anonimizados + doutrina.
