# Assessment Report: Nortex Componentes (empresa fictícia)

**Engagement:** Demonstração do método ABBA
**Date:** 2026-08-30
**Industry:** manufacturing
**Model:** claude-haiku | **Dimensions:** 25/25 | **Confidence:** 0.78 | **Cost:** $3.18

---

## The Verdict in 60 Seconds

- **AI maturity:** level 3/5 — Structured (Estruturado), from 6 of 6 pillars with a reading
- **Weakest pillar:** Technology & Integration (level 2/5)
- **Data foundation:** FRAGILE (data and process) — build on it and the build fails
- **Largest detected leak:** Retrabalho de cotação por especificação incompleta (~R$ 920.000/yr)
- **First move on the ranking:** Reconciliação automática entre planilha, ERP e chão

*Every line above is expanded — with evidence, confidence and method — in the sections below.*

---

## AI Maturity by Pillar

**Overall: level 3/5 — Structured (Estruturado)** · score 2.65 · based on 6 of 6 pillars with a reading

| Pillar | Level | Score | Read | What unlocks the next level |
|---|---|---|---|---|
| Strategy & Future-Readiness | **3/5 Structured** | 2.86 | solid (conf. 0.74) | D10 The AI Vision Gap · D11 Competitive Intelligence · D22 The Scalability Cliff |
| Operations & Decisions | **3/5 Structured** | 2.93 | solid (conf. 0.81) | D02 How the Company Actually Works · D12 Information Flow Topology · D19 Failure Mode Analysis |
| Technology & Integration | **2/5 Aware** | 1.5 | solid (conf. 0.83) | D03 The Technology Landscape · D21 Integration Gravity |
| People & Knowledge | **2/5 Aware** | 2.31 | solid (conf. 0.79) | D15 The Knowledge Decay Rate · D18 Power Structure & Politics · D06 The People Reality |
| Data & Governance | **3/5 Structured** | 3.24 | solid (conf. 0.79) | D09 Risk & Compliance · D08 Hidden Data Assets |
| Value & Customer | **3/5 Structured** | 3.09 | solid (conf. 0.76) | D25 The Measurement Baseline · D14 The Trust Architecture · D04 The Money Map |

*Method: Confidence-weighted aggregation of per-dimension verdicts (automate 4.5 · augment 3.5 · leave_alone 3.0 · investigate 2.5 · fix_data_first 1.5; penalties for contradictions/gaps). Derived from THIS assessment — not an industry benchmark.*

## Data Foundation Verdict

**FRAGILE.** Building AI on this foundation now would join the failure statistics. Fix the named data and process gaps first — that IS the first AI project.

- Data & Governance pillar: level 3/5
- Dimensions where the verdict was "fix the data first": 5 of 25

*Why this section leads the plan: ~80% of AI projects fail (RAND, 2024) and the dominant causes are foundational, not algorithmic; Gartner projects 60% of AI projects without AI-ready data will be abandoned through 2026. Counting the cost of the foundation before building is the whole method.*

---

## Silent Financial Leaks Detected

*Money the company is losing — much of it without realizing. Each row maps to a recommended AI intervention below.*

**Bottom-up leak sum: R$ 2.340.000/yr** *(6 leaks total, 0 unquantified)*

| # | Category | Leak | Annual Cost | Severity | Awareness | Related |
|---|---|---|---|---|---|---|
| 1 | rework | Retrabalho de cotação por especificação incompleta | R$ 920 mil/ano | critical | known_but_unaddressed | D11, D07, D13 |
| 2 | decision_latency | Peça parada esperando aprovação de desvio | R$ 610 mil/ano | high | known_but_unaddressed | D20, D05, D18 |
| 3 | coordination_drag | Reconciliação semanal entre PCP, compras e produção | R$ 265 mil/ano | high | partially_addressed | D16, D12, D02 |
| 4 | hidden_labor | Consolidação manual do apontamento de produção | R$ 140 mil/ano | high | known_but_unaddressed | D12, D03, D21 |
| 5 | knowledge_concentration | Roteiro de processo real na cabeça de dois planejadores | R$ 240 mil/ano (exposição a risco, não despesa de caixa) | medium | unknown_to_company | D15, D06, D05 |
| 6 | integration_brittleness | ERP e MES reconciliados em planilha | R$ 165 mil/ano | medium | partially_addressed | D21, D03, D19 |

<details><summary>Leak detail — evidence + methodology</summary>

**1. Retrabalho de cotação por especificação incompleta**

Cada cotação passa em média 2,4 vezes pela engenharia de aplicação porque a especificação chega incompleta do comercial. O tempo é de engenheiro sênior, e o cliente espera.

*Methodology (calculated):* Premissa: 1.400 cotações/ano x 1,4 passagens extras x 4,2h por passagem x R$ 112/h de engenheiro sênior carregado. As 1.400 cotações vieram do ERP; as passagens extras e as horas vieram da entrevista com a engenharia de aplicação; a hora carregada veio da folha.

**2. Peça parada esperando aprovação de desvio**

Um desvio de engenharia leva 3,4 dias em média para ser aprovado. A ordem fica parada e o prazo prometido ao cliente já está correndo.

*Methodology (estimated):* Premissa: 560 desvios/ano x 2,1 dias de espera evitável x R$ 520/dia de custo de atraso (expedição extra e multa contratual rateada). O custo por dia é média da carteira, não por peça, então este número é uma faixa e não um ponto.

**3. Reconciliação semanal entre PCP, compras e produção**

Três reuniões por semana existem para alinhar o que cada área acha que está acontecendo. Nenhuma decide nada novo: elas corrigem a divergência entre planilha, ERP e chão.

*Methodology (calculated):* Premissa: 12 pessoas x 3 reuniões x 1,5h x 46 semanas x R$ 98/h carregado, mais 6h/semana de preparação de planilha do PCP a R$ 85/h. A contagem de participantes foi conferida na agenda.

**4. Consolidação manual do apontamento de produção**

Duas pessoas passam parte do dia transcrevendo apontamento de chão para a planilha e da planilha para o ERP. O ERP fica sempre um dia atrás do que é verdade.

*Methodology (calculated):* Premissa: 2 pessoas x 3,5h/dia x 230 dias x R$ 78/h carregado, mais o retrabalho de digitação medido em 3 semanas de amostra.

**5. Roteiro de processo real na cabeça de dois planejadores**

O roteiro que funciona não é o do sistema: é o que dois planejadores com 20 anos de casa sabem de cor. Um deles se aposenta em 18 meses.

*Methodology (estimated):* Premissa: custo esperado de perda de produtividade na transição, estimado a partir do que a empresa relatou ter perdido na última aposentadoria no PCP. É exposição a risco, não despesa recorrente, e está rotulado assim no plano.

**6. ERP e MES reconciliados em planilha**

A ponte entre os dois sistemas é uma planilha mantida por uma pessoa. Quando ela falha, o planejamento da semana seguinte sai errado.

*Methodology (estimated):* Premissa: 11 incidentes relatados no último ano x 1,5 dia de replanejamento x R$ 10 mil/dia de custo de reprogramação. O número de incidentes veio do relato do PCP, não de um registro, então a confiança é baixa.

</details>

---

## Revenue & Value-Creation Opportunities

*The other side of the ledger — money the company could **make**, not just the money it is losing. These are build-new candidates for AI, not cost cuts.*

**Total estimated annual upside: R$ 3.100.000** *(2 opportunities)*

| # | Category | Opportunity | Annual Upside | Value Profile | Time to Value |
|---|---|---|---|---|---|
| 1 | pricing_packaging | Disciplina de preço por família de produto | R$ 1,1 mi–R$ 2,5 mi (expected R$ 1,7 mi) | recurring | 1 a 2 trimestres |
| 2 | capacity_unlock | Capacidade de cotação destravada | R$ 630 mil–R$ 2,4 mi (expected R$ 1,4 mi) | recurring | 2 a 3 trimestres |

<details><summary>Opportunity detail — evidence + methodology</summary>

**1. Disciplina de preço por família de produto**

A margem por família existe no ERP e não entra na negociação. O desconto sai na hora, com base histórica e não com base na margem real da peça.

*Methodology (estimated):* Premissa: 0,6 a 1,4 ponto percentual de margem recuperada sobre R$ 180 milhões de faturamento, aplicando às famílias hoje descontadas abaixo da média. A margem por família vem do ERP; o comportamento de desconto vem de entrevista, e é o lado fraco da estimativa.

**2. Capacidade de cotação destravada**

A demanda existe e o gargalo é a engenharia de aplicação. Cada dia de prazo de cotação recuperado devolve propostas que hoje o concorrente responde primeiro.

*Methodology (estimated):* Premissa: R$ 9 a 24 milhões de faturamento hoje perdido por prazo de cotação, recuperando de 25% a 35% disso, com margem de contribuição de 28%. É MARGEM, não faturamento. A faixa é larga de propósito: o quanto se perde por prazo é relato comercial, não medição, e é a primeira coisa a instrumentar.

</details>

---

## AI Intervention Plan

*Concrete AI builds — one per leak, plus build-new opportunities for money-making loops that do not exist yet. Ranked by Breach Score; each is sized with cost, payback, and a measurement plan.*

*These are the most valuable hypotheses, not the only ones — the first hypothesis is rarely the best, just the fastest. Challenge the plan before committing: `abba red-team <engagement>`.*

**Combined Year-1 recovery if all interventions ship: R$ 1.572.000** *(total implementation cost: R$ 1.079.000)*

| # | Intervention | Capability | Impl Cost | Annual Recovery | Payback | Loaded Payback | Readiness | Sensitivity |
|---|---|---|---|---|---|---|---|---|
| 1 | Reconciliação automática entre planilha, ERP e chão | reconciliation | R$ 145.000 | R$ 190.000 | 9.2 mo | — | high | low |
| 2 | Leitura automática do apontamento de chão | extraction | R$ 98.000 | R$ 112.000 | 10.5 mo | — | high | low |
| 3 | Ponte monitorada entre ERP e MES | reconciliation | R$ 135.000 | R$ 116.000 | 14.0 mo | — | high | low |
| 4 | Checagem de completude da especificação antes da engenharia | extraction | R$ 320.000 | R$ 644.000 | 6.0 mo | — | medium | medium |
| 5 | Captura do roteiro real antes da aposentadoria | summarization | R$ 96.000 | R$ 144.000 | 8.0 mo | — | medium | medium |
| 6 | Dossiê de desvio pronto para a engenharia decidir | decision_support | R$ 285.000 | R$ 366.000 | 9.3 mo | — | medium | high |

### Why this ranking

*Breach-Score factors (multiplicative; 1.00 is neutral). Prize is the log-damped annual recovery; the rest scale it up or down.*

| Intervention | Prize | Feasibility | Payback | Compounding | Measurability | Risk |
|---|---|---|---|---|---|---|
| Reconciliação automática entre planilha, ERP e chã | 5.28 | 0.53 | 0.57 | 1.00 | 1.00 | 0.69 |
| Leitura automática do apontamento de chão | 5.05 | 0.53 | 0.53 | 1.00 | 1.00 | 0.69 |
| Ponte monitorada entre ERP e MES | 5.06 | 0.53 | 0.46 | 1.00 | 1.00 | 0.67 |
| Checagem de completude da especificação antes da e | 5.81 | 0.19 | 0.67 | 1.00 | 1.00 | 0.66 |
| Captura do roteiro real antes da aposentadoria | 5.16 | 0.19 | 0.60 | 1.00 | 1.00 | 0.60 |

**Bigger prizes that did not lead:**

- **Checagem de completude da especificação antes da engenharia** recovers R$ 644.000/yr, 3.4x the money of the #1 build, and ranks #4. The Breach Score damps the prize on purpose, so 3.4x the money is only 1.10x the prize factor. Then its feasibility markers (`readiness: medium`, `sensitivity: medium`) cost it another 2.8x.

*A marking is a judgement someone made in an interview, not a measurement. If one of these is wrong, the plan is wrong, and this is the cheapest moment to catch it: re-check the marking with the client, then `abba rerun` or override it. If the markings are right, this ordering is the method working as intended (start where the organization is willing, not where the number is biggest).*

*Run-level signals: integration gravity (D21, fix-first verdict) discounts every build's feasibility by 25%.*

*Order frozen at the end of the run (snapshot `rnk_7LK1A4iilKM`, prioritizer `breach-1`). The signals above are the ones in force when it was taken. Later measured outcomes change the NEXT assessment, not the plan already delivered; `abba report --refresh-ranking` re-takes it and preserves the previous order beside it.*

<details><summary>Intervention specs — architecture, data, integrations, HITL</summary>

### 1. Reconciliação automática entre planilha, ERP e chão

*Value: Recurring (repeats yearly)*

Um agente lê o apontamento, o ERP e a planilha do PCP, aponta apenas as divergências e propõe a correção. As três reuniões semanais viram uma, e ela decide em vez de reconciliar.

**Architecture:** Extração agendada dos dois sistemas, comparação determinística, e o modelo apenas para explicar a divergência em linguagem de negócio. Nada é escrito de volta sem aprovação.

**Data prerequisites:**
- Acesso de leitura ao ERP
- Export do MES
- Histórico de 6 meses da planilha do PCP

**Integration points:**
- ERP
- MES

**Human-in-the-loop checkpoints:**
- O PCP aprova toda correção antes de ela entrar no ERP

**Measurement plan:** Horas de reunião por semana e número de divergências abertas na segunda-feira. Linha de base coletada nas 3 semanas antes do piloto.

**Cascade effects:** Reduz também a latência de decisão, porque a divergência deixa de ser descoberta na reunião.

### 2. Leitura automática do apontamento de chão

*Value: Recurring (repeats yearly)*

O apontamento passa a ser lido direto do registro de chão e conferido, em vez de transcrito duas vezes. O ERP deixa de ficar um dia atrás.

**Architecture:** Extração estruturada com validação por regra; o que não bater vai para uma fila humana em vez de entrar torto.

**Data prerequisites:**
- Formato do registro de chão
- Regras de validação por centro de trabalho

**Integration points:**
- MES

**Human-in-the-loop checkpoints:**
- Fila de exceções revisada diariamente por quem hoje digita

**Measurement plan:** Horas de digitação por semana e defasagem do ERP em horas.

**Cascade effects:** É pré-requisito de qualidade de dado para a reconciliação e para o sequenciamento.

### 3. Ponte monitorada entre ERP e MES

A planilha que hoje é a ponte vira uma integração com monitoramento: quando quebra, alguém sabe no mesmo dia em vez de descobrir no planejamento da semana seguinte.

**Architecture:** Integração determinística com alerta. Nada aqui precisa de modelo, e dizer isso é parte do trabalho.

**Data prerequisites:**
- Esquema dos dois sistemas
- Janela de manutenção

**Integration points:**
- ERP
- MES

**Human-in-the-loop checkpoints:**
- O responsável de TI confirma cada reprocessamento

**Measurement plan:** Incidentes por trimestre e tempo até detectar uma quebra.

**Cascade effects:** Sustenta a reconciliação: sem esta ponte, o agente reconcilia dado que vai quebrar de novo.

### 4. Checagem de completude da especificação antes da engenharia

*Value: Compounding (grows each cycle)*

Na entrada da cotação, o modelo confere a especificação contra os 20 anos de cotações anteriores e devolve ao comercial o que está faltando, antes de consumir hora de engenheiro sênior.

**Architecture:** RAG sobre o histórico de cotações com desfecho, mais um checklist determinístico por família de peça. O modelo nunca aprova: ele lista o que falta.

**Data prerequisites:**
- Histórico de cotações com ganho/perda
- Checklist por família de peça

**Integration points:**
- ERP
- CRM
- Repositório de desenhos

**Human-in-the-loop checkpoints:**
- A engenharia mantém a palavra final sobre viabilidade
- O comercial revisa a lista antes de voltar ao cliente

**Measurement plan:** Passagens por cotação (hoje 2,4) e prazo de resposta ao cliente. Ambas medidas antes do piloto.

**Cascade effects:** Encurta o prazo de cotação, que é o que o cliente enxerga.

### 5. Captura do roteiro real antes da aposentadoria

*Value: Compounding (grows each cycle)*

O que os dois planejadores sabem vira consultável: por que esta peça vai nesta máquina, o que dá errado quando não vai. Capturado com eles, não sobre eles.

**Architecture:** Entrevistas estruturadas transcritas e indexadas por peça e centro de trabalho, revisadas pelos próprios planejadores antes de publicar.

**Data prerequisites:**
- Agenda dos dois planejadores
- Lista de peças por criticidade

**Integration points:**
- Repositório interno

**Human-in-the-loop checkpoints:**
- Os planejadores aprovam cada roteiro antes de ele ficar consultável

**Measurement plan:** Cobertura das peças críticas e tempo que um planejador novo leva para sequenciar sozinho.

**Cascade effects:** Reduz a exposição da aposentadoria e alimenta o dossiê de desvio.

### 6. Dossiê de desvio pronto para a engenharia decidir

*Value: Recurring (repeats yearly)*

Quando um desvio abre, o sistema monta o dossiê (peça, histórico de desvios parecidos, impacto no prazo, decisão anterior) e entrega pronto. A engenharia decide, não pesquisa.

**Architecture:** Recuperação sobre o histórico de desvios com o desfecho de cada um. Sem decisão automática: a engenharia tem veto informal e tirá-lo dela mataria a adoção.

**Data prerequisites:**
- Histórico de desvios com desfecho
- Impacto de prazo por família

**Integration points:**
- ERP
- PLM

**Human-in-the-loop checkpoints:**
- Toda aprovação continua sendo da engenharia, com o dossiê ao lado

**Measurement plan:** Dias entre abertura e aprovação do desvio (hoje 3,4) e ordens paradas por semana.

**Cascade effects:** Se a engenharia adotar, é a porta de entrada para o resto do plano. Se rejeitar, nada mais passa.

</details>

---

## What Changes for the Organization

*The Stop / Start / Keep-doing matrix. What AI does for them now, what AI enables them to start doing, what only humans can still do.*

> Nenhum papel desaparece. O que muda é onde a atenção das pessoas é gasta: menos reconciliação e digitação, mais decisão sobre exceção. A engenharia continua com a palavra final, e isso é uma escolha de projeto, não uma concessão.

### Company-wide

| Stop Doing (AI handles it) | Start Doing (AI unlocks it) | Must Still Do (only humans) |
|---|---|---|
| Reconciliar planilha, ERP e chão em reunião | Medir prazo de cotação e aderência ao plano | Julgar viabilidade técnica |
| Transcrever apontamento duas vezes | Decidir desvio com o histórico ao lado | Negociar prazo com o cliente |

<details><summary>By role</summary>

#### PCP

**Stop doing:**
- Montar a planilha de divergências toda segunda
- Perseguir apontamento por WhatsApp

**Start doing:**
- Revisar a fila de divergências que o sistema levanta
- Sequenciar com o roteiro real consultável

**Must still do:**
- Decidir a sequência quando o cliente muda a prioridade

#### Engenharia de aplicação

**Stop doing:**
- Descobrir na segunda passagem que faltava tolerância

**Start doing:**
- Receber a cotação já conferida quanto a completude
- Decidir desvio com o dossiê pronto

**Must still do:**
- Aprovar ou recusar o desvio
- Julgar viabilidade de peça nova

#### Comercial

**Stop doing:**
- Mandar especificação incompleta e esperar o retorno

**Start doing:**
- Fechar a especificação com a lista do que falta, antes de abrir a cotação

**Must still do:**
- Negociar preço e prazo

#### Líder de turno

**Stop doing:**
- Anotar no papel para alguém digitar depois

**Start doing:**
- Confirmar o apontamento lido pelo sistema

**Must still do:**
- Chamar a exceção quando a máquina não responde como esperado

</details>

<details><summary>By process</summary>

#### Cotação

**Stop doing:**
- Duas a três passagens pela engenharia

**Start doing:**
- Checagem de completude na entrada

**Must still do:**
- Aprovação técnica final

#### Planejamento semanal

**Stop doing:**
- Três reuniões de reconciliação

**Start doing:**
- Uma reunião de decisão sobre a fila de divergências

**Must still do:**
- Repriorizar quando entra pedido urgente

</details>

---

## Adoption & Change-Management Plan

*The best technical plan dies in the hallway. Land the change: bring the right people along, retrain rather than replace, and keep humans in control while trust builds.*

### 1. Retrain, don't replace
*What each role should START doing once AI takes the routine work — the curriculum for the transition.*

- **PCP:** Revisar a fila de divergências que o sistema levanta; Sequenciar com o roteiro real consultável
- **Engenharia de aplicação:** Receber a cotação já conferida quanto a completude; Decidir desvio com o dossiê pronto
- **Comercial:** Fechar a especificação com a lista do que falta, antes de abrir a cotação
- **Líder de turno:** Confirmar o apontamento lido pelo sistema

### 2. What stays irreplaceably human
*Say this out loud early — it is the reassurance that makes adoption possible.*

- Julgar viabilidade técnica
- Negociar prazo com o cliente

### 3. Keep humans in control while trust builds
*Every checkpoint where a person reviews AI output before it counts — start here, loosen as the track record earns it.*

- O PCP aprova toda correção antes de ela entrar no ERP
- Fila de exceções revisada diariamente por quem hoje digita
- O responsável de TI confirma cada reprocessamento
- A engenharia mantém a palavra final sobre viabilidade
- O comercial revisa a lista antes de voltar ao cliente
- Os planejadores aprovam cada roteiro antes de ele ficar consultável
- Toda aprovação continua sendo da engenharia, com o dossiê ao lado

### 4. The willing-area gate — before any build starts
*Start with the most willing area, not the most broken one. For each of the top-ranked builds, tick all three in the meeting:*

- **Reconciliação automática entre planilha, ERP e chão:** [ ] named owner · [ ] area director's aval · [ ] team aligned (not just informed)
- **Leitura automática do apontamento de chão:** [ ] named owner · [ ] area director's aval · [ ] team aligned (not just informed)
- **Ponte monitorada entre ERP e MES:** [ ] named owner · [ ] area director's aval · [ ] team aligned (not just informed)

## Cross-Dimensional Connections

*No dimension is an island. These connections show how findings reinforce each other.*

- **D01 → D10:** Company DNA determines what AI vision is realistic *(The Company's DNA conf 0.86 → The AI Vision Gap conf 0.71)*
- **D01 → D11:** DNA determines competitive positioning and vulnerability *(The Company's DNA conf 0.86 → Competitive Intelligence conf 0.64)*
- **D10 → D11:** AI vision gap creates competitive blind spots *(The AI Vision Gap conf 0.71 → Competitive Intelligence conf 0.64)*
- **D02 → D12:** How work flows determines how information flows *(How the Company Actually Works conf 0.88 → Information Flow Topology conf 0.83)*
- **D02 → D13:** Normal operations define what counts as an exception *(How the Company Actually Works conf 0.88 → The Exception Landscape conf 0.79)*
- **D12 → D16:** Information gaps create coordination overhead *(Information Flow Topology conf 0.83 → The Coordination Tax conf 0.84)*
- **D13 → D20:** Exception handling creates latency bottlenecks *(The Exception Landscape conf 0.79 → The Latency Map conf 0.80)*
- **D03 → D21:** Technology landscape determines integration gravity *(The Technology Landscape conf 0.85 → Integration Gravity conf 0.82)*
- **D04 → D25:** Money map provides the measurement baseline *(The Money Map conf 0.81 → The Measurement Baseline conf 0.68)*
- **D05 → D19:** Decision architecture determines failure modes *(The Decision Map conf 0.83 → Failure Mode Analysis conf 0.72)*
- **D06 → D15:** People reality drives knowledge concentration risk *(The People Reality conf 0.80 → The Knowledge Decay Rate conf 0.86)*
- **D06 → D22:** People capacity determines scalability ceiling *(The People Reality conf 0.80 → The Scalability Cliff conf 0.73)*
- **D15 → D18:** Knowledge holders accumulate political power *(The Knowledge Decay Rate conf 0.86 → Power Structure & Politics conf 0.70)*
- **D07 → D14:** Customer experience reflects the trust architecture *(The Customer Experience conf 0.75 → The Trust Architecture conf 0.78)*
- **D08 → D09:** Hidden data assets are constrained by compliance *(Hidden Data Assets conf 0.76 → Risk & Compliance conf 0.81)*
- **D17 → D20:** Seasonal rhythms create predictable latency spikes *(Seasonality and Rhythm conf 0.77 → The Latency Map conf 0.80)*
- **D22 → D24:** Scalability cliffs determine what to build now vs later *(The Scalability Cliff conf 0.73 → Build Today vs. Tomorrow conf 0.79)*
- **D14 → D23:** Trust architecture shapes ethical AI deployment boundaries *(The Trust Architecture conf 0.78 → The Ethical Dimension conf 0.74)*
- **D18 → D05:** Power structure determines which decisions get made *(Power Structure & Politics conf 0.70 → The Decision Map conf 0.83)*
- **D16 → D06:** Coordination tax reveals where people spend time on non-value work *(The Coordination Tax conf 0.84 → The People Reality conf 0.80)*

---

---

---

# Appendix: The Full Evidence

*Everything above rests on what follows: the organism read, all dimensions one by one, evidence density, cross-engagement baselines and the decision loops. This is the sustaining detail, not the argument.*

---

## Findings by Cluster

### Strategic Foundation

*Before asking about processes, you need to understand what the organism is, what world it competes in, and whether AI can actually do what they think it can.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D01 The Company's DNA | 0.86 | leave_alone | Empresa familiar de segunda geração, decisão concentrada no diretor industrial. Identidade é qualidade de usinagem e prazo, e isso é verdade no chão. |
| D10 The AI Vision Gap | 0.71 | investigate_further | Não existe visão de IA declarada. A diretoria fala em "automatizar o PCP" sem definir o que isso significa, e ninguém no time sabe dizer o que já foi ... |
| D11 Competitive Intelligence | 0.64 | investigate_further | Dois concorrentes diretos passaram a oferecer cotação em 48 horas. A Nortex leva de 5 a 12 dias e sabe disso por relato de cliente, não por medição. |

### Operational Reality

*Not the org chart. Not the process manual. How work actually flows, where it breaks, where it leaks value, and how it coordinates across people and departments.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D02 How the Company Actually Works | 0.88 | fix_data_first | O processo real diverge do processo documentado em três pontos críticos, todos no fluxo cotação -> ordem. O roteiro oficial descreve uma fábrica que p... |
| D12 Information Flow Topology | 0.83 | fix_data_first | Informação de produção viaja por planilha e WhatsApp entre PCP, compras e chão. O ERP recebe o consolidado no dia seguinte. |
| D13 The Exception Landscape | 0.79 | augment | Exceção é o volume, não a exceção: cerca de 40% das ordens sofrem algum desvio de engenharia. O tratamento é individual e depende de quem atende. |
| D16 The Coordination Tax | 0.84 | automate | Três reuniões semanais existem para reconciliar o que PCP, compras e produção acham que está acontecendo. Nenhuma delas produz decisão nova. |
| D17 Seasonality and Rhythm | 0.77 | leave_alone | Sazonalidade conhecida e bem administrada: pico de linha branca no segundo semestre, planejado com antecedência. |
| D20 The Latency Map | 0.80 | augment | A latência que dói não é de máquina, é de decisão: aprovação de desvio leva em média 3,4 dias, e a peça espera. |

### Technology & Integration

*Not just what software they use — the real state of their technology, what connects to what, and how tangled the integrations actually are.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D03 The Technology Landscape | 0.85 | fix_data_first | ERP consolidado, MES entregue pela metade em 2021, e uma planilha central que é a fonte de verdade real do planejamento. |
| D21 Integration Gravity | 0.82 | fix_data_first | ERP e MES não conversam. A reconciliação é feita à mão toda semana, e toda construção nova vai encontrar essa gravidade. |

### Financial Intelligence

*Where money flows, where it leaks, where it could be created — and whether you can prove ROI before, during, and after.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D04 The Money Map | 0.81 | augment | Margem por família de produto existe no ERP mas não é usada para decidir preço. O orçamento sai de tabela histórica com desconto negociado na hora. |
| D25 The Measurement Baseline | 0.68 | investigate_further | Quase nada tem linha de base medida. Prazo de cotação, taxa de retrabalho e aderência ao plano são estimativas de quem opera. |

### Decision Architecture

*AI's biggest value is not automating tasks — it is improving decisions. Most assessments map processes but not the decisions that run through them.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D05 The Decision Map | 0.83 | augment | Decisões de sequenciamento acontecem duas vezes ao dia, na cabeça de dois planejadores, sem registro do porquê. |
| D19 Failure Mode Analysis | 0.72 | investigate_further | O modo de falha mais caro é aceitar um pedido com prazo que a fábrica não consegue cumprir. Acontece, e ninguém contabiliza. |

### People & Knowledge

*AI replaces tasks, not people. Understanding the task composition of each role, how knowledge is held, and who has real power — not org-chart power.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D06 The People Reality | 0.80 | leave_alone | Time estável, baixa rotatividade no chão. A resistência não é a pessoas, é a sistema: a memória do MES de 2021 está viva. |
| D15 The Knowledge Decay Rate | 0.86 | fix_data_first | Roteiro de processo real mora na experiência de dois planejadores com 20 anos de casa. Um deles se aposenta em 18 meses. |
| D18 Power Structure & Politics | 0.70 | investigate_further | A engenharia detém o poder de veto informal sobre qualquer mudança de processo. Nenhuma construção passa sem ela. |

### Customer & Trust

*The outside-in view of where AI improves the customer experience — and the trust architecture that determines what level of AI autonomy the company is ready for.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D07 The Customer Experience | 0.75 | augment | Cliente percebe a empresa pelo prazo de resposta na cotação, que é o ponto mais lento da cadeia inteira. |
| D14 The Trust Architecture | 0.78 | leave_alone | Confiança técnica alta: cliente aceita a palavra da engenharia sobre viabilidade sem segunda opinião. |

### Data & Compliance

*Every company sits on data they don't use. And every company has constraints on what AI can do with it.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D08 Hidden Data Assets | 0.76 | augment | Vinte anos de histórico de cotação com desfecho ganho ou perdido, nunca usados. É o ativo de dado mais subaproveitado da empresa. |
| D09 Risk & Compliance | 0.81 | leave_alone | Certificação em dia, rastreabilidade de lote funcionando. Não é aqui que a empresa corre risco. |

### Future-Readiness

*Where the company breaks when it grows, what ethical constraints shape what AI should do, and what to build now versus what to wait on.*

| Dimension | Confidence | Action | Finding |
|---|---|---|---|
| D22 The Scalability Cliff | 0.73 | investigate_further | Dobrar o volume esbarra na engenharia de aplicação antes de esbarrar em máquina. O gargalo é cognitivo, não de capacidade instalada. |
| D23 The Ethical Dimension | 0.74 | leave_alone | Nenhuma decisão automatizada afeta pessoa física. O risco ético relevante aqui é baixo e declarado como tal. |
| D24 Build Today vs. Tomorrow | 0.79 | augment | O que vale construir hoje é extração e reconciliação, tecnologia provada. O que vale esperar é qualquer coisa que dependa do MES completo. |

## Evidence Density

| Dimension | Confidence | Evidence | Contradictions | Action |
|---|---|---|---|---|
| D01 The Company's DNA | 0.86 (Strong) | 0 items | 0 | leave_alone |
| D02 How the Company Actually Works | 0.88 (Strong) | 0 items | 1 | fix_data_first |
| D03 The Technology Landscape | 0.85 (Strong) | 0 items | 0 | fix_data_first |
| D04 The Money Map | 0.81 (Strong) | 0 items | 0 | augment |
| D05 The Decision Map | 0.83 (Strong) | 0 items | 0 | augment |
| D06 The People Reality | 0.80 (Strong) | 0 items | 0 | leave_alone |
| D07 The Customer Experience | 0.75 (Strong) | 0 items | 0 | augment |
| D08 Hidden Data Assets | 0.76 (Strong) | 0 items | 0 | augment |
| D09 Risk & Compliance | 0.81 (Strong) | 0 items | 0 | leave_alone |
| D10 The AI Vision Gap | 0.71 (Strong) | 0 items | 0 | investigate_further |
| D11 Competitive Intelligence | 0.64 (Moderate) | 0 items | 0 | investigate_further |
| D12 Information Flow Topology | 0.83 (Strong) | 0 items | 0 | fix_data_first |
| D13 The Exception Landscape | 0.79 (Strong) | 0 items | 0 | augment |
| D14 The Trust Architecture | 0.78 (Strong) | 0 items | 0 | leave_alone |
| D15 The Knowledge Decay Rate | 0.86 (Strong) | 0 items | 0 | fix_data_first |
| D16 The Coordination Tax | 0.84 (Strong) | 0 items | 0 | automate |
| D17 Seasonality and Rhythm | 0.77 (Strong) | 0 items | 0 | leave_alone |
| D18 Power Structure & Politics | 0.70 (Strong) | 0 items | 1 | investigate_further |
| D19 Failure Mode Analysis | 0.72 (Strong) | 0 items | 0 | investigate_further |
| D20 The Latency Map | 0.80 (Strong) | 0 items | 0 | augment |
| D21 Integration Gravity | 0.82 (Strong) | 0 items | 0 | fix_data_first |
| D22 The Scalability Cliff | 0.73 (Strong) | 0 items | 0 | investigate_further |
| D23 The Ethical Dimension | 0.74 (Strong) | 0 items | 0 | leave_alone |
| D24 Build Today vs. Tomorrow | 0.79 (Strong) | 0 items | 0 | augment |
| D25 The Measurement Baseline | 0.68 (Moderate) | 0 items | 0 | investigate_further |

## Deep Organism Diagnosis

*The company analyzed as a living organism — 7 biological systems assessed.*

> Empresa saudável no produto e travada na coordenação. O dado ruim não é a causa: é o sintoma de um processo de planejamento que nunca foi desenhado para o mix atual. Qualquer construção que ignore isso vai automatizar a confusão.

### Immune System
*What inefficiencies protect the company? What would break if you removed them?*

**active Mechanisms:**
- Comitê de investimento mensal
- Aprovação de desvio pela engenharia

**overactive Responses:**
- Toda exceção sobe para a diretoria industrial

**compromised Areas:**
- Planejamento de produção depende de duas pessoas

**surgery Risk:** medium

**surgery Risk Level:** medium

### Homeostasis
*What keeps the company stable? What could destabilize it?*

**stabilizing Forces:**
- Carteira de clientes longa
- Time de chão de fábrica estável

**destabilizing Forces:**
- Mix de produtos crescendo mais rápido que o PCP consegue planejar

**tipping Points:**
- Entrada de um cliente automotivo de grande volume

### Scar Tissue
*Past traumas that shaped current behavior*

**past Traumas:**
- Implantação de MES em 2021 entregue pela metade

**behavioral Consequences:**
- Ceticismo com projeto de sistema; planilha é vista como o que funciona

**healing Status:** partial

### Growth Edges
*Where the company is actively evolving*

**active Growth:**
- Linha branca crescendo 18% ao ano

**blocked Growth:**
- Engenharia de aplicação é o gargalo para atender novos clientes

**growth Capacity:** medium

### Decay Edges
*Where the company is deteriorating*

**active Deterioriation:**
- Roteiros de processo desatualizados em relação ao chão

**early Warnings:**
- Aumento de retrabalho em cotação nos últimos dois trimestres

**time Horizon:** near

**time Horizon Band:** near

### Metabolism
*How fast the company can absorb change*

**change Absorption Rate:** slow

**bottlenecks:**
- PCP
- Engenharia de aplicação

**ai Readiness:** medium

**ai Readiness Level:** medium

### Nervous System
*How information travels — and where it doesn't*

**information Flow Health:** fragmented

**dead Nerves:**
- Apontamento de produção chega ao ERP com um dia de atraso

**pain Signals:**
- Cliente reclama de prazo antes de o PCP saber que atrasou

---

## Confidence Audit

*A line per major claim with its current confidence, evidence count, whether the consultant has applied an override, and any validator warning (corruption / prompt-injection / unparseable output). Use this to defend the assessment under questioning.*

| Source | Confidence | Evidence items | Override? | Warning | Title |
|---|---|---|---|---|---|
| D01 (dim) | 0.86 | 0 | — | — | The Company's DNA |
| D02 (dim) | 0.88 | 0 | — | — | How the Company Actually Works |
| D03 (dim) | 0.85 | 0 | — | — | The Technology Landscape |
| D04 (dim) | 0.81 | 0 | — | — | The Money Map |
| D05 (dim) | 0.83 | 0 | — | — | The Decision Map |
| D06 (dim) | 0.80 | 0 | — | — | The People Reality |
| D07 (dim) | 0.75 | 0 | — | — | The Customer Experience |
| D08 (dim) | 0.76 | 0 | — | — | Hidden Data Assets |
| D09 (dim) | 0.81 | 0 | — | — | Risk & Compliance |
| D10 (dim) | 0.71 | 0 | — | — | The AI Vision Gap |
| D11 (dim) | 0.64 | 0 | — | — | Competitive Intelligence |
| D12 (dim) | 0.83 | 0 | — | — | Information Flow Topology |
| D13 (dim) | 0.79 | 0 | — | — | The Exception Landscape |
| D14 (dim) | 0.78 | 0 | — | — | The Trust Architecture |
| D15 (dim) | 0.86 | 0 | — | — | The Knowledge Decay Rate |
| D16 (dim) | 0.84 | 0 | — | — | The Coordination Tax |
| D17 (dim) | 0.77 | 0 | — | — | Seasonality and Rhythm |
| D18 (dim) | 0.70 | 0 | — | — | Power Structure & Politics |
| D19 (dim) | 0.72 | 0 | — | — | Failure Mode Analysis |
| D20 (dim) | 0.80 | 0 | — | — | The Latency Map |
| D21 (dim) | 0.82 | 0 | — | — | Integration Gravity |
| D22 (dim) | 0.73 | 0 | — | — | The Scalability Cliff |
| D23 (dim) | 0.74 | 0 | — | — | The Ethical Dimension |
| D24 (dim) | 0.79 | 0 | — | — | Build Today vs. Tomorrow |
| D25 (dim) | 0.68 | 0 | — | — | The Measurement Baseline |
| leak (critical) | 0.78 | 0 | — | — | Retrabalho de cotação por especificação incompleta |
| leak (high) | 0.61 | 0 | — | — | Peça parada esperando aprovação de desvio |
| leak (high) | 0.82 | 0 | — | — | Reconciliação semanal entre PCP, compras e produção |
| leak (high) | 0.85 | 0 | — | — | Consolidação manual do apontamento de produção |
| leak (medium) | 0.55 | 0 | — | — | Roteiro de processo real na cabeça de dois planejadores |
| leak (medium) | 0.52 | 0 | — | — | ERP e MES reconciliados em planilha |
| intervention | 0.79 | (derived) | — | — | Reconciliação automática entre planilha, ERP e chão |
| intervention | 0.81 | (derived) | — | — | Leitura automática do apontamento de chão |
| intervention | 0.74 | (derived) | — | — | Ponte monitorada entre ERP e MES |
| intervention | 0.72 | (derived) | — | — | Checagem de completude da especificação antes da engenharia |
| intervention | 0.58 | (derived) | — | — | Captura do roteiro real antes da aposentadoria |
| intervention | 0.63 | (derived) | — | — | Dossiê de desvio pronto para a engenharia decidir |

---

## Assessment Coverage

**Sources analyzed:** 5

**Stakeholder levels covered:**
- ceo_board: 1 source(s)
- dept_head: 2 source(s)
- front_line: 1 source(s)
- internal_data: 1 source(s)

**Missing levels:** c_suite, external, consultant

**Missing interview phases:**
- Phase 4: The Calibration (Synthesis)

---

## Method Integrity

*The principles behind this method, checked against THIS report. "Not in this artifact" means the principle lives in a companion artifact (visual annex, CLI) — run `abba principles <engagement>` for the full compliance view.*

| Principle | Alive in this report | Where |
|---|---|---|
| Quem começa uma torre sem antes calcular a despesa? O custo total se conta antes de construir, nunca depois. | ✓ | seção AI Intervention Plan com custo carregado |
| Inspecionar os muros em silêncio, antes de anunciar o plano: o diagnóstico vem antes do discurso. | ✓ | abba scout (Mapa de Vazamento pré-reunião) |
| Na multidão de conselheiros há segurança: ouvir do conselho à linha de frente, e registrar onde eles se contradizem. | ✓ | abba red-team (a análise desafiada) |
| Procura conhecer o estado do teu rebanho antes de prometer a colheita: o veredito de fundação vem antes do plano. | ✓ | seção Data Foundation Verdict |
| Mais que recursos, discernimento para julgar o que importa: o problema mais valioso vem primeiro, com o porquê auditável. | ✓ | plano ranqueado por Breach Score |
| Prever, quantificar e armazenar no tempo certo: o caminho se planta em horizontes, com folga para o que não se controla. | not in this artifact | roadmap em três horizontes · trajetória entre rodadas |
| A casa se edifica com sabedoria e se firma com entendimento: tecnologia, processos e pessoas, nunca ferramenta sozinha. | ✓ | plano de adoção (land the change) |
| A fundação que falha nunca é só o dado: é o processo que o produz. Estruturar os dois antes de construir. | ✓ | veredito de fundação computado (dados e processos) · seção Data Foundation Verdict |
| O humano no meio do processo ou ajuda ou vira detrator: começar pela área mais disposta a mudar, não pela mais quebrada. | ✓ | prontidão e sensibilidade por intervenção · checklist de adoção no plano |
| Solução de prateleira quebra no processo real: entender como a empresa de fato funciona antes de propor a construção. | not in this artifact | loops de decisão reais mapeados |
| O que se vende é a imersão e as lições acumuladas: cada engajamento novo herda os padrões anonimizados dos anteriores. | ✓ | knowledge vault (padrões entre engajamentos) |
| A análise não pode morrer como documento: as recomendações entram num ciclo vivo de decisão, revisão e resultado medido. | ✓ | abba decision seed (assessment → cérebro) · decisões com trigger de revisão e outcome |
| A primeira hipótese raramente é a melhor: é só a mais rápida. Toda recomendação sobrevive a um desafio antes de virar plano. | ✓ | abba red-team · auditoria de confiança da própria análise |
| Toda construção carrega a resposta de por que existe e continua sendo a aposta certa: evidência do vazamento, número e premissa. | ✓ | vazamentos como evidência do plano · intervenções ligadas a vazamentos (leak_id) |
| O custo do próprio trabalho é visível até o centavo, e a confiança de cada leitura é declarada, nunca inflada. | ✓ | a análise auditando a si mesma (reliability) |

*This analysis is executable, not a slide deck: seed the ranked builds into the decision journal with `abba decision seed <engagement> --by "Name"`, and export build specs with `abba export <engagement> --target crewai`.*

---

*Generated by ABBA Assessment Brain on 2026-08-30. Model: claude-haiku. Cost: $3.18.*
