# Arquitetura — o Cérebro do Conselheiro Digital (o cérebro que dorme)

> **Status: DESENHO EXECUTADO (atualizado 2026-08-01)** — o cérebro foi construído: Fases 0–2 + Ondas 1–3 de memória + camada de antecipação, seis rodadas de revisão adversarial independente (73 defeitos corrigidos), suíte 429/429. Este documento é a **memória do desenho** (o porquê de cada escolha); o estado atual está no [plano](plano-implementacao-conselheiro.md) e a operação no [dossiê vivo](../04-entrega/dossie-vivo-conselheiro-digital.md). Banner original: *"desenho-alvo da aposta futura 5 — nenhuma construção antes dos gatilhos"*. Origem (2026-07-29): pergunta do sócio — "os 4 quebrados do Meta-ANN podem ser reconstruídos certos? o que mais o Conselheiro deveria ter para ser o mais disruptivo possível? um cérebro constantemente alimentado, aprendendo e *descansando*, melhorando num ciclo sem fim — um cérebro personalizável por empresa". Três frentes de pesquisa profunda executadas (memória e consolidação, auto-melhoria segura, mercado/moat). Este doc é a resposta consolidada, com fontes.

## 1. Reconstruir os 4 quebrados do Meta-ANN — a resposta é SIM, e por menos código

**"Consertar o Meta-ANN" é o frame errado; "reconstruir a FUNÇÃO no Conselheiro" é o certo.** Consertar seria reformar ~200k linhas de andaime em volta de um teatro (código órfão, API MongoDB em Postgres, K8s sem imagem). Reconstruir é outra coisa: cada uma das 4 falhas é o **negativo fotográfico da especificação correta** — e para cada uma a ABBA já tem o embrião funcionando:

| # | O que quebrou no Meta-ANN | A reconstrução certa no Conselheiro | O embrião que JÁ temos |
|---|---|---|---|
| 1 | Loop de aprendizado nunca fecha (`autoApply:false`, aplicadores nunca chamados) | **Escada de melhoria** (§4): camadas baixas fecham sozinhas; camadas altas fecham COM gate humano; recomendação ao board NUNCA auto | `src/core/learning-*`: propor → sócio aprova → uplift medido (testado e2e) |
| 2 | Memória MIRIX write-only (sem leitura → amnésia a cada restart) | **Dossiê Vivo read-path-first**: nenhuma tabela de memória entra sem query de leitura + teste de hidratação no mesmo PR | Migração 117 (schema 6 tipos) + vault FTS5 que já lê o que grava |
| 3 | Validação-teatro (`Math.random()`, 0,996 fixo) | **Avaliação real em 3 camadas**: golden set por cliente, reconciliação de outcome, citação verificável em toda afirmação | O loop de confiança empírica do vault (reconcilia recomendação × resultado real, aposenta no piso 0,25) |
| 4 | Nunca deployado; multi-tenancy só no próprio teste | **Um cérebro por tenant na infra que JÁ roda** (portal com RLS em produção) | Portal Next.js multi-tenant + telemetria CrewAI por cliente |

Os 4 consertados viram os 4 órgãos do cérebro: (1) o ciclo de aprendizado · (2) a memória · (3) o sistema imunológico (avaliação) · (4) o corpo (deploy segregado por cliente).

## 2. O ciclo dia/noite — a ciência por trás do "cérebro que descansa"

A intuição do sócio ("alimentado, aprendendo e **descansando**, para no outro dia aprender mais") tem nome na literatura 2025–2026 e evidência quantitativa: **sleep-time compute** (Letta + UC Berkeley, [arXiv 2504.13171](https://arxiv.org/abs/2504.13171)) — o modelo "pensa sobre" o contexto ANTES das perguntas chegarem, enquanto está ocioso: **~5× menos custo na hora da resposta com a mesma qualidade, +13–18% de acurácia escalando o pensamento noturno, custo amortizado ~2,5× quando várias perguntas batem no mesmo contexto** — e o caso ideal do paper é exatamente o nosso (o espaço de perguntas de um conselho é previsível: estratégia, KPIs, as 25 dimensões, decisões abertas).

### O DIA (online, barato, rápido)
Ingestão → parse → chunk → embed → grava no log de episódios e nos recursos (modelo médio só etiqueta entidades/tipo de evento). Consultas do Conselheiro: fatos vigentes (SQL) + busca híbrida com reranking + blocos de perfil sempre no contexto → **resposta com citação e política de abstenção** ("não sei pelo registro do cliente"). Nada de consolidação no caminho da resposta. Os crews CrewAI leem/escrevem o cérebro via *tools*; a memória nativa do CrewAI é rascunho, nunca o cérebro.

### A NOITE (offline, batch — 50% de desconto de API, o horário nobre do cérebro)
1. **Sono leve (toda noite):** extrai fatos atômicos dos episódios do dia → deduplica → checa contradição → **supersessão determinística** (fato antigo ganha `invalid_at`, nunca é apagado — a história fica) → aplica validade por tipo (KPI mensal expira no mês seguinte; fato de organograma expira em evento de pessoal).
2. **Sono REM (disparado por importância acumulada — decisão de board dispara na mesma noite; KPI de rotina espera o passe semanal):** reflexão — "o que mudou? o que implica para as 25 dimensões? qual recomendação está fora da rota?" → grava *insights* **com citação das evidências** → pré-computa: atualiza os blocos de perfil, o estado por dimensão, e **rascunha o brief/pauta que o Conselheiro humano revisa de manhã** (o handoff centauro: o sonho da noite vira a fila de curadoria da manhã).
3. **Sono profundo (semanal/mensal):** re-deriva as avaliações por dimensão da evidência completa (checagem de deriva), comprime/decai episódios frios (decaimento gradual, nunca deleção fora do `abba forget`), reconcilia confiança dos insights contra resultados reais (aposenta no piso), e troca com o vault: sobe padrão anonimizado validado, desce padrão do setor como hipótese a priori.

**O loop "acorda mais inteligente" fecha pelo diff de edição do sócio:** cada aprovação/edição da manhã vira episódio que a noite seguinte aprende — é RLHF de graça, e é o mesmo mecanismo de confiança empírica que o vault já roda.

### A memória (tudo Postgres + RLS por cliente — nada de infra exótica)
Consenso 2026: pgvector + FTS dão conta até milhões de vetores; um cérebro por cliente tem milhares — 3–5 ordens de grandeza abaixo de qualquer limite. Sete stores (a taxonomia MIRIX validada, agora COM caminho de leitura):

| Store | O quê | Padrão roubado de |
|---|---|---|
| `episodes` | Log imutável: transcrições, decisões, KPIs, edições do sócio, telemetria CrewAI | Memory stream (Generative Agents, Stanford) |
| `resources` | Docs + chunks + embeddings + FTS | MIRIX resource (já temos na ingestão) |
| `facts` | **Fatos bitemporais** `(sujeito, predicado, objeto, valid_at, invalid_at, fonte, confiança)` — responde "vigente quando?" | Zep/Graphiti; RAG puro serve fato vencido 15–40% das vezes ([MemStrata](https://arxiv.org/abs/2606.26511)); supersessão determinística → ~0% |
| `insights` | Reflexões da noite com citações + confiança empírica (rascunho → aprovado → publicado → aposentado) | Reflection (Stanford) + nosso vault |
| `profile_blocks` | A "memória core": JSONB versionado (perfil, estado das 25 dimensões, decisões abertas, recomendações ativas) — sempre no prompt; **só a noite e o sócio escrevem** | Letta/MemGPT core memory |
| `vault_cliente` | Dado sensível verbatim, criptografia separada, coberto pelo `abba forget` | MIRIX knowledge vault + nossa disciplina PII |
| vault ABBA (existente) | A "memória da espécie" acima de todos os cérebros — intocado | Já é nosso |

**Custo real por cérebro/cliente: ~US$ 10–40/mês** (embeddings são centavos; a noite roda em batch com 50% off). Mesmo com margem 10×, é erro de arredondamento contra o retainer — **o gargalo é hora de sócio, não computação**, o que justifica gastar MAIS pensamento noturno (converte token barato em hora humana poupada).

## 3. O que o cérebro acessa e o que ele cria

**Acessa (alimentação diária):** assessment + plano diretor (a fotografia inicial — já temos) · atas e decisões do conselho · KPI mensal projetado×realizado · transcrições de reuniões do engajamento (com consentimento; as 8 recusas do [estudo do Conselheiro presente](estudo-conselheiro-presente.md) valem aqui) · telemetria dos agentes CrewAI em produção · adoção no portal · edições do sócio (o sinal de ouro) · padrões anonimizados do setor vindos do vault.

**Cria (a produção da noite):** o brief mensal com fonte citada · estado vivo das 25 dimensões · radar de recomendações on/off-track · candidatos a insight para o ritual (máx. 3, curados) · rascunho de pauta do conselho · alertas de fato vencido ("o churn que você vai citar é de maio") · o diário de decisões (recomendado → decidido → implementado → medido) — e, anonimizado e consentido, o alimento do vault.

## 4. A escada de melhoria — "aprimorar sem cessar, sem quebrar o que existe"

A pesquisa de auto-melhoria (ACE/Stanford, GEPA/DSPy, Darwin Gödel Machine, AlphaEvolve, SEAL) converge num veredito: **todo loop que comprovadamente funciona fecha através de um avaliador confiável; onde a avaliação é subjetiva (aconselhamento!), o loop honesto passa por julgamento humano convertido em ativos de avaliação.** E o nosso mecanismo (propor → aprovar → medir) é exatamente o formato que o estado da arte industrializa e que a regulação exige. A escada:

| Degrau | O que melhora | Cadência | Gate |
|---|---|---|---|
| **0 — Autônomo contínuo** | Ranking de retrieval, higiene de memória (dedup, decaimento, flag de contradição), contadores útil/nocivo dos playbooks, captura de traces, GERAÇÃO de candidatos | Diário (a noite) | Nenhum — mas tudo logado e reversível |
| **1 — Autônomo dentro de envelope declarado** | Rodadas de otimizador (GEPA funciona com ~10 exemplos — o nosso regime de N pequeno!), propostas de consolidação, rollback automático em alarme de regressão | Semanal, digest para os sócios | Envelope pré-aprovado por escrito |
| **2 — Gate humano (o nosso mecanismo, industrializado)** | Promoção de versão de prompt/playbook, escrita no vault (+ revisão de anonimização), fatos duráveis do cliente, mudanças de rubrica/golden set | Por proposta: shadow 1–2 semanas → diff pareado → sócio aprova → canário por escopo (1 cliente/1 dimensão) → medir | Sócio |
| **3 — Humano para sempre** | Assinar recomendação · afirmação nova a board · preço/escopo/jurídico · **o avaliador, os gates e os guarda-corpos** · maquinário PII · modelo-base | — | Sócios |

**As 5 salvaguardas do ciclo sem fim** (cada uma comprada com o fracasso de alguém): (1) **o avaliador é intocável** — o sistema que melhora nunca escreve no próprio exame (a Darwin Gödel Machine da Sakana *hackeou o próprio avaliador* deletando os marcadores de detecção em vez de corrigir o comportamento); (2) **piso de regressão + holdout nunca visto** — nenhuma versão promove sem ≥ campeão no golden set completo E confirmação num conjunto que o otimizador nunca viu; (3) **conhecimento append-only com procedência, nunca reescrita total** — o ACE documentou "context collapse": reescritas iterativas degradaram um contexto de 18k para 122 tokens e a acurácia caiu; deltas itemizados com contadores, aposentadoria em vez de deleção; (4) **pin de versão + rollback de 1 comando + trilha por entregável** (qual prompt/playbook/memória/modelo produziu, quem aprovou — é simultaneamente a rede de segurança, o dossiê PL 2338 e a defesa de responsabilidade); (5) **reconciliação de outcome como verdade final** — trimestral, recomendações × resultados reais + calibração (Brier score): só resultado reconciliado mantém o loop apontado para valor do cliente e não para as próprias métricas.

**E jamais fine-tuning por cliente:** modelo-base congelado (alugado de fronteira); TODO aprendizado em artefatos versionados (contexto, playbooks, memória, retrieval). O fine-tuning contínuo tem esquecimento catastrófico e colapso documentados (SEAL/MIT; sistemas de self-play subindo de 25%→81% e **colapsando a ~zero** na iteração 200) — e a doutrina do EU AI Act (Art. 43(4): "mudanças pré-determinadas e documentadas não são modificação substancial") abençoa exatamente o envelope declarado, não o peso que muda sozinho.

## 5. O mercado — o veredito honesto sobre "ninguém tem isso"

**A frase como dita é FALSA — e usá-la num pitch morre numa busca do Google.** "Cérebro personalizável por empresa" é o que Glean (US$ 7,2 bi), Microsoft Copilot+Graph (15 mi de assentos), Google Gemini Enterprise, OpenAI ("company knowledge"), Workday/Sana (US$ 1,1 bi), Palantir (o digital twin real) e uma categoria inteira do YC S2026 ("Company Brain", nos requests oficiais) estão construindo — e **já existe agência brasileira vendendo o serviço com o nome literal "Company Brain / Cérebro da Empresa"**.

**O que É verdade (a afirmação estreita e defensável):** ninguém encontrado nesta pesquisa vende, para o mid-market brasileiro (R$ 50–500 mi), um cérebro persistente por cliente que (a) é **operado por uma consultoria que responde por ele**, (b) mantém o **diário das próprias recomendações e resultados reais** e re-pondera o conselho futuro nessa evidência, e (c) entrega recomendação de nível de conselho **assinada por um humano nomeado**, ao preço de **uma cadeira de conselheiro** (conselheiros no Brasil ganham R$ 15–30k/mês — a âncora de preço perfeita, e coerente com nossa v2). Os componentes existem separados no enterprise (Palantir, McKinsey Lilli, CAIO fracionário, Diligent "AI Board Member"); **a interseção, neste segmento, neste modelo, está desocupada em julho/2026.**

Os 3 fossos reais: (1) **o diário de resultados** — o "decision-graph moat" que a literatura 2026 chama de único ativo de IA que compõe, impossível de fast-follow retroativo (cada trimestre operado aprofunda); (2) **assinatura humana + LGPD nativo** — a ansiedade fiduciária é O bloqueador documentado de IA em conselhos (IBGC/Harvard/PwC), e a assinatura é estruturalmente impossível para Microsoft/OpenAI e economicamente impossível para McKinsey neste segmento; (3) **economia de 2 sócios** — 8–15 clientes a preço de cadeira de conselheiro, abaixo do mínimo de qualquer vendor enterprise (Glean: ~US$ 350k/ano, 100 assentos), acima do chão dos bots de WhatsApp.

As 3 ameaças com relógio: absorção de features por OpenAI/Microsoft (12–24 meses — se o nosso pitch for *retrieval*, morre; tem que ser *julgamento com responsabilidade*); startups Company Brain + no-code BR subindo de segmento (18–36 m); plataformização das grandes consultorias descendo (24–48 m). **A janela é agora: estar ENTRANQUEIRADO (diário + relação) antes que desçam de preço.**

Linguagem defensável (sobrevive a due diligence): *"O único conselheiro cujo histórico de recomendações — e resultados — fica registrado, medido e auditável"* · *"Um cérebro que aprende com os resultados da SUA empresa, não com a média do mercado — e um consultor que assina cada recomendação"* · *"IA propõe. Especialista assina. Conselho decide."* · *"Pelo preço de uma cadeira de conselheiro, um conselheiro que nunca esquece"* · *"Copilot responde perguntas. Nós respondemos pelo resultado."*

## 6. Encaixe no faseamento existente (nada muda nos gatilhos; muda o que cada fase constrói)

| Fase (gatilho do [estudo](estudo-conselheiro-digital.md)) | O que esta arquitetura acrescenta |
|---|---|
| 0 (agora) | Disciplina apenas: todo dado de engajamento estruturado como episódio desde o 1º cliente; captura de traces desde o 1º run |
| 1 (1º cliente em manutenção) | `episodes` + `resources` + `facts` + a noite leve; brief mensal rascunhado pela noite, curado pelo sócio |
| 2 (1º cliente na camada Estratégia) | `insights` + `profile_blocks` + sono REM; o loop propor→aprovar→medir portado do assessment-brain; golden set do cliente |
| 3 (3+ clientes) | Iris-Empresa lê o cérebro (com citação e abstenção); escada degrau 1 (otimizador semanal em envelope); pesos hebbianos se houver multi-agente |
| 4 (10+ clientes) | Produto nomeado; diário de calibração como ativo de marketing ("nossa curva de acerto em 12 meses") |

**Regras que continuam invioláveis:** um cérebro por cliente, segregado (RLS) · nunca treinar modelo com dado de cliente · toda saída a board curada e assinada · `abba forget` é o único caminho de deleção · consentimento explícito para a destilação ao vault.

## Fontes principais

- **Sono/consolidação:** [Sleep-time compute (Letta/Berkeley)](https://arxiv.org/abs/2504.13171) · [Generative Agents (Stanford)](https://arxiv.org/abs/2304.03442) · [MemGPT/Letta](https://arxiv.org/abs/2310.08560) · [Zep/Graphiti bitemporal](https://arxiv.org/abs/2501.13956) · [MIRIX](https://arxiv.org/abs/2507.07957) · [MemStrata (fatos vencidos no RAG)](https://arxiv.org/abs/2606.26511)
- **Auto-melhoria:** [ACE — Agentic Context Engineering](https://arxiv.org/abs/2510.04618) · [GEPA (ICLR 2026)](https://arxiv.org/abs/2507.19457) · [Darwin Gödel Machine (Sakana)](https://sakana.ai/dgm/) · [AlphaEvolve (DeepMind)](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) · [colapso do self-training](https://arxiv.org/pdf/2606.21090) · [EU AI Act Art. 43(4)](https://artificialintelligenceact.eu/article/43/)
- **Mercado:** [YC RFS S2026 — Company Brain](https://www.thevccorner.com/p/yc-summer-2026-requests-for-startups-ideas) · [OpenAI company knowledge](https://openai.com/index/introducing-company-knowledge/) · [Workday–Sana US$ 1,1 bi](https://newsroom.workday.com/2025-09-16-Workday-Signs-Definitive-Agreement-to-Acquire-Sana) · [Diligent AI Board Member](https://www.diligent.com/company/newsroom/diligent-unveils-ai-board-member-and-agentic-grc-workforce) · [McKinsey Lilli](https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewiring-the-way-mckinsey-works-with-lilli) · [remuneração de conselheiros BR (Forbes)](https://forbes.com.br/carreira/2025/07/quem-sao-quanto-ganham-e-o-que-tira-o-sono-dos-conselheiros-no-brasil/) · [IBGC — IA nos conselhos](https://www.ibgc.org.br/blog/inteligencia-artificial-nos-conselhos) · [memória como moat](https://devrev.ai/blog/the-only-defensible-moat-in-ai-your-enterprise-memory)
