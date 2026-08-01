# Estudo — Antecipação: o que os donos querem, o que a IA consegue, e onde a ABBA aposta

> **Camada:** interno (pesquisa). Origem: observação do sócio (2026-08-01): *"temos que mirar no que todas as empresas e seus líderes querem ter: previsão, organização, planos concretizados, soluções diárias, visão, atualidade e estar um passo sempre à frente."* Este estudo consolida três pesquisas (inventário dos nossos 4 repositórios · o que executivos declaram querer · trajetória dos modelos até 2030) e fundamenta a decisão registrada em [V2u](registro-de-decisoes.md).
>
> **Etiquetas de fonte:** [ACAD] revisado por pares · [INDEP] medição independente · [CONS] consultoria/analista (trabalho de campo real, interesse comercial) · [FORN] alegação de fornecedor · [NÃO-VERIF] número em circulação sem fonte primária rastreável. **Número sem etiqueta não entra em material de cliente.**
>
> Dono: sócios. Revisar a cada 6 meses junto com a [Visão 2029](../00-identidade/visao-2029.md).

---

## 0. O diagnóstico de casa, com número

O inventário temporal dos nossos quatro repositórios classificou **~30 mecanismos**: **1 prevê** (`simulate` — uma chamada de LLM, sem intervalo, sem validação), **~6 avisam** (`reconfirm`, recheck de barreiras, lembretes, cadência da Bússola), **~23 registram o passado**.

**A ABBA é uma máquina de memória e prova — e era quase muda em antecipação.** A intuição do sócio, confirmada. O substrato para mudar isso já existia parado: o diário `decisions → decision_outcomes` já é um conjunto supervisionado; a série de auditoria já tem a idade do engajamento como variável; a fila de reconfirmação já olhava 7 dias à frente. A resposta (§6) foi construída **sobre** essas tabelas, não ao lado delas.

---

## 1. A evidência de foresight — a única palavra da lista com prova acadêmica forte

**Rohrbeck & Kum (2018), *Technological Forecasting and Social Change*** [ACAD — longitudinal]: maturidade de foresight medida em 2008, desempenho medido em 2015 (defasagem de 7 anos, o que enfraquece a causalidade reversa). Firmas **"vigilantes"** (preparadas para o futuro na medida da incerteza que enfrentam): **+33% de lucratividade e +200% de crescimento de valor de mercado** contra a média. Firmas deficientes: desconto de desempenho de **37% a 108%**. Migração: **40% das vigilantes subiram** de posição de lucratividade; **só 9% das deficientes**.

**Ressalvas obrigatórias** (dizer junto com o número, sempre): n≈90, multinacionais europeias, maturidade autorrelatada, 8 anos sem replicação encontrada. Sustenta uma afirmação forte, não uma inquebrável.

**O mercado confirma a demanda e a vaga:**
- **51% dos CFOs** põem *melhorar a acurácia e a qualidade da previsão financeira* no top-5 de prioridades de 2026 [CONS — Gartner, ago/2025]. E a própria Gartner declara o cenário-planejamento tradicional obsoleto ("premissas estáticas, superpeso de fatores internos, resposta lenta a choques").
- Só **25% da Fortune 500** pratica foresight [INDEP-ish — Houston Foresight]; mesmo entre grandes firmas que têm unidade dedicada (42%), a maioria a transforma em teatro de metas — só ~40% usam para exploração real [ACAD/institucional, 2025].
- *Decision intelligence*: categoria nomeada pela Gartner (1º Magic Quadrant em fev/2026), adoção estimada em **5–20%**, plataformas de **US$ 100k–1M/ano** [CONS]. **Ninguém vende isso na faixa R$ 50–500 mi.**
- S&OP/IBP maduro (McKinsey, 170+ empresas, 5 anos) [CONS]: **+1–2 pontos de EBIT**, níveis de serviço +5–20 pp, penalidades e vendas perdidas −40–50% — e a maioria das empresas **nunca passa dos níveis 1–2** da maturidade, onde o valor ainda não chegou.

**EY Brasil** enquadra a dor do nosso mercado literalmente como **"falta de previsibilidade"** [CONS]; a KPMG Brasil descreve a profissionalização da empresa familiar como necessidade de **"maior previsibilidade"**, com o remédio nomeado: papéis claros, **rotinas de gestão**, indicadores e metas [CONS, 2026]. É a tese do sócio, publicada na imprensa de negócios brasileira, no nosso vocabulário.

---

## 2. A fronteira honesta — onde a IA prevê e onde nos recusamos

A tabela que separa o que podemos vender do que seria vendido para ser desmentido:

| Tipo de pergunta | Estado honesto em 2026 | Vendemos? |
|---|---|---|
| Eventos com classe de referência (há base histórica comparável) | **Bom.** LLMs no top ~3% de 1.130 humanos no torneio Metaculus (primavera/2026) [INDEP]; paridade com superforecasters *alegada* por quem opera o benchmark [conflito de interesse — a meta-análise independente ainda dá vantagem de 0,017 Brier aos humanos de elite] | ✅ Com humano no circuito |
| Análise de demonstrativo financeiro padronizado | **Genuinamente bom.** 60,35% de acerto direcional de lucro vs ~53% dos analistas, em demonstrativos **anonimizados** (sem memorização), com a vantagem maior onde o analista erra [ACAD — Kim, Muhn & Nikolaev, Chicago Booth] | ✅ |
| Séries de demanda/volume rotineiras com histórico | **Bom — mas do ML clássico.** Modelos de fundação de série temporal: vantagem real de **0,3–14% em dado limpo**; os números espetaculares (47–184%) eram **vazamento de pré-treino** [ACAD] | ✅ Sem prometer milagre |
| **Mudança de regime, cauda, crescimento superlinear** | **Modelos mais capazes preveem PIOR** (*inverse scaling*, replicado em COVID, sarampo, imóveis, hiperinflação) [ACAD, 2026]. **É a descrição do macro brasileiro: câmbio, crédito, eleição, reforma** | ❌ **Recusa publicada** |
| **"O que acontece se fizermos X"** (causal/contrafactual) | **Não.** Extração causal de texto real: F1 ≈ 0,535; modelos recuperam relações conhecidas, **não descobrem estrutura nem estimam efeito de ação** [ACAD] | ❌ **Recusa publicada** |
| Clientes sintéticos / pesquisa simulada para decisão de peso | **Não.** Falhas replicam entre domínios, modelos e famílias [ACAD, 2026] | ❌ |
| Gêmeo digital da operação da empresa | **Não existe em 2026.** >US$ 3 bi investidos em world models que simulam espaços 3D, não processos de negócio | ❌ |

**Por que a recusa é estratégia e não modéstia:** num mercado onde toda agência promete prever, a firma que publica *onde a IA não funciona* — com fonte — é a que o comprador cético contrata. E nunca seremos a firma que disse ao cliente que a receita dele estava segura atravessando uma mudança de regime.

**O que a nossa previsão é, então:** (a) probabilidade declarada **por humano nomeado** em cada recomendação, pontuada contra o resultado medido (o placar de calibração — §6); (b) gatilhos combinados ("se o indicador cruzar o limiar, revisamos") que fazem a decisão acordar; (c) aritmética honesta sobre o que já sabemos (vencimentos, obsolescência projetada). Previsão como **disciplina auditável**, não como oráculo.

---

## 3. Cadência humana × cutucão automatizado — a evidência que define o formato

**A descoberta mais importante do estudo para uma firma de dois sócios:**

- **Nudges (cutucões impessoais — dashboards, alertas, e-mails automáticos):** meta-análise de segunda ordem [ACAD — Hu et al., *JBDM* 2025; 1.638 estudos primários, ~30 milhões de participantes]: efeito agregado **d = 0,27 que colapsa para d = 0,004** após correção de viés de publicação. (Em conflito com Mertens 2022, d=0,45 [ACAD] — o campo disputa, mas a análise mais recente e conservadora dá ~zero.)
- **Coaching (contato humano recorrente em agenda):** meta-análise **só de RCTs** [ACAD — *AMLE* 2023; 37 RCTs, 2.528 participantes]: **g = 0,59**. Theeboom 2014: g = 0,66 geral, **g = 0,74 para autorregulação orientada a meta**, g = 1,29 para atingimento de meta.

**Tradução:** o que muda comportamento de gestão é **uma pessoa aparecendo num ritmo**, não um sistema pingando. Para dois sócios isso é a melhor notícia possível: **a coisa escassa e cara — a atenção deles, em cadência — é exatamente a que funciona, e ela não é comoditizável por dashboard.** Decisão do sócio: **ritual semanal de 20 minutos** nos degraus 3–4 da escada ([ritual](../04-entrega/ritual-semanal.md)).

**Números proibidos** (folclore sem fonte primária — não usar em nenhum material): "95% de atingimento de meta com accountability partner" [NÃO-VERIF] · "90% das estratégias falham" [NÃO-VERIF, com refutação revisada por pares no *Journal of Management & Organization*] · "15 min semanais > 90 min mensais" [NÃO-VERIF]. **Usar no lugar:** só **28% dos gestores** conseguem citar três prioridades estratégicas da própria empresa [MIT Sloan/HBR 2015, 124 organizações]; só **30% das organizações** realocam recursos de forma ampla, e o alto realocador valeu **>2×** em 20 anos [CONS — McKinsey]. **OKR não tem evidência controlada** — vender a cadência, não a sigla.

**Mecanismo de custo zero com a melhor evidência de todo o estudo:** o **pré-mortem** ("estamos 12 meses à frente e isto fracassou — por quê?"): +30% de identificação correta de causas [ACAD — Mitchell, Russo & Pennington 1989]; ~dobra os riscos que aparecem numa sessão [Klein, HBR 2007]. 30 minutos, custo zero. Agora obrigatório no [kickoff](../04-entrega/kickoff-roteiro.md).

---

## 4. O que fica MAIS valioso conforme os modelos melhoram

A régua para decidir onde investir hora: o insumo (inteligência bruta) despenca de preço — 9× a 900×/ano dependendo da tarefa [INDEP — Epoch AI]; o valor migra para os **complementos**. Cinco, com evidência:

1. **Assinatura responsável.** O mercado segurador está **retirando** cobertura de dano por IA generativa: formulário ISO **CG 40 47 01 26** vigente desde jan/2026; AIG, WR Berkley e Chubb adicionando exclusões nas renovações [imprensa jurídica]. A Deloitte Austrália devolveu ~A$ 97 mil por relatório com citações fabricadas por IA (out/2025). **Quem assina embaixo de uma decisão apoiada em IA vende algo que o mercado acabou de declarar escasso** — e o modelo não pode competir: não tem patrimônio nem pode ser processado. É o nosso gate de humano nomeado, precificado.
2. **Verificação.** Times com agentes: +98% de PRs, +91% de tempo de revisão, mediana **+441%** [ACAD/indústria]. Geração escala com computação; conferência exige atenção sênior — **o preço dela sobe quando o insumo barateia.**
3. **Medição independente.** O RCT da METR [INDEP]: desenvolvedores experientes **19% mais lentos** com IA enquanto **relatavam 20% mais rápidos** — 39 pontos entre percebido e medido. E a METR **retirou a confiança do próprio follow-up** (fev/2026) por efeitos de seleção. *Ganho autorrelatado de IA não é evidência* — e medir de verdade é um serviço.
4. **Desenho de processo.** MAST [ACAD — 1.600+ traços, κ=0,88]: **41,8%** das falhas multiagente são de especificação/desenho, **36,9%** de coordenação, **21,3%** de verificação — *"robustez exige melhor orquestração, não modelos maiores"*. **~79% das falhas são trabalho de consultoria** e não somem com modelo melhor. Gartner: >40% dos projetos agênticos cancelados até fim de 2027; só ~130 de milhares de fornecedores "agentic" são reais.
5. **Memória organizacional com proveniência.** Os laboratórios entregam memória de *sessão/usuário/agente* — o Google **cobra por memória** (US$ 0,25/1.000 desde jan/2026), a Oracle lançou a dela em mar/2026. **Nenhum entrega memória de *decisão organizacional*, bitemporal, com autoridade de origem e trilha legal** — porque isso exige conhecer o negócio do cliente. É o Conselheiro. (Honestidade: a tese "memória proprietária é fosso" é o melhor palpite disponível, **não um fato demonstrado** — nenhum estudo rigoroso prova vantagem durável. Dizemos isso também.)

**O que a pesquisa proíbe construir** (será grátis ou desmentido em ~18 meses): framework/orquestrador/camada de memória de agentes · geração de deck e síntese de pesquisa como serviço · "avaliação de maturidade de IA" genérica · revenda fina de modelo (a OpenAI capitalizou a **DeployCo** com ~US$ 4 bi em mai/2026 — o próprio laboratório virou consultoria de implantação, com McKinsey, Bain e Capgemini como investidores) · simulador de negócio/gêmeo digital · painéis de clientes sintéticos · produto de leaderboard.

---

## 5. O calendário — as datas que convertem vitamina em analgésico

| Data | O quê | A conversa que abre |
|---|---|---|
| **já em vigor** | **LGPD Art. 20** com poder de auditoria da ANPD + **IA como eixo de fiscalização 2026–27** (Mapa de Temas Prioritários, dez/2025) | Governança auditável **hoje**, sem esperar o PL 2338 |
| **02/08/2026** | **EU AI Act Art. 50** (transparência) em aplicação — extraterritorial via *output usado na UE*; chega ao exportador **como cláusula contratual** ("a multa europeia não chega ao Brasil; a cláusula sim" — Conjur, jul/2026) | Qualquer cliente que exporta ou fornece para quem exporta |
| **03/08/2026** | Campos IBS/CBS **validados em produção** — sem preenchimento correto, **a nota não sai** | Toda empresa do regime regular, agora. Grandes estão ~89% prontas [CONS — Deloitte]; a nossa faixa, entre 11% e 40% [fontes conflitam — o conflito É o insight: a despreparação está concentrada no R$ 50–500 mi] |
| set/2026 | Prazo de decisão de regime tributário | CFO |
| 2027 | CBS plena; PIS/Cofins extintos · EU AI Act alto risco (dez/2027) | Reprecificação, margem, modelo operacional |
| 2028–29 | Vigência plena esperada do PL 2338 (aprovado no Senado dez/2024; na Câmara; até R$ 50 mi/violação; explicação em 15 dias; revisão humana) | O dossiê que satisfaz o regulador — que já construímos por convicção |
| até 2032 | Convivência dos dois sistemas tributários | Anos de complexidade dobrada = anos de demanda |

**Não construir negócio que dependa do PL 2338 passar no prazo** — ele já atrasou várias vezes. A LGPD Art. 20 + ANPD bastam para vender auditabilidade hoje.

---

## 6. O que foi construído em resposta (2026-08-01)

Migração 046 no assessment-brain + doutrina. Tudo determinístico, custo zero de LLM:

| Peça | O que faz | Comando |
|---|---|---|
| **Gatilho por decisão** | "Se [indicador] cruzar [limiar], revisamos em N dias." A decisão acorda sozinha — na fila, com conferência humana. Nada dispara no mundo real | `abba decision trigger <eng> <id> --metric dso --threshold 45 --direction above --review-in 30` |
| **Probabilidade declarada** | Quem recomenda diz quanto acredita (0–1), com nome, **antes** — prever depois de medir é bloqueado no código | `abba decision predict <eng> <id> --probability 0.7 --by "Nome"` |
| **Placar de calibração** | Brier + baldes (dissemos 70% → aconteceu ~70%?). Abaixo de 20 pares medidos: **"indisponível"**, nunca um número instável. O placar consolidado da firma ("nossas recomendações acertam X%") exige massa de decisões medidas — gatilho de 10+ clientes; por engajamento ele serve ao ritual, não ao marketing | `abba brain calibration <eng>` |
| **Fila de antecipação** | A tela da manhã: o que venceu · o que vai vencer (horizonte padrão de **14 dias**, ajustável com `--horizon`) · gatilho disparado (baixa com `--checked`) · decisão parada (30 dias) · claim contestado · obsolescência projetada (aritmética sobre TTLs, **não previsão**). Ordenada por prazo, nunca por "importância" | `abba brain next <eng>` |
| **Seção "Antecipação" no brief** | A mesma fila entra no brief mensal rascunhado pelo ciclo noturno | automático |
| **Ritual semanal de 20 min** | O formato humano que a evidência do §3 sustenta — roteiro de 4 itens | [ritual-semanal.md](../04-entrega/ritual-semanal.md) |
| **Pré-mortem no kickoff** | Obrigatório, 30 min | [kickoff-roteiro.md](../04-entrega/kickoff-roteiro.md) |

**O que fica especificado e NÃO construído — o Radar:** varredura mensal por cliente de mudança regulatória e sinal fraco setorial (a fase de varredura ficou barata com LLM; a curadoria continua humana), entrando como seção do brief. Gatilhos para construir: 1º cliente pagante em manutenção **+** provedor de busca do scout resolvido (pendência Pedro) **+** custo estimado por cliente/mês medido. Registrado em [apostas futuras](../00-identidade/apostas-futuras.md) — não é promessa comercial até lá.

---

## 7. Síntese em uma página (para reler antes de reunião)

1. **O dono quer previsibilidade, e ninguém vende isso na nossa faixa.** A única evidência acadêmica forte de toda a lista de desejos é a de foresight (+33% lucro, +200% valor). A Gartner acabou de nomear a categoria e as plataformas custam 10× o nosso programa.
2. **A IA prevê bem onde há classe de referência e demonstrativo padronizado — e piora onde o Brasil mais precisa** (regime, cauda, causal). Por isso a nossa previsão é probabilidade declarada + gatilho + placar, não oráculo. **A recusa é publicada e é argumento de venda.**
3. **O formato que funciona é gente em cadência** (g=0,59) **, não dashboard** (d=0,004). O ritual semanal de 20 min é o produto; a IA prepara a pauta em segundos (`brain next`).
4. **Conforme os modelos melhoram, sobe o valor do que já temos:** assinatura nomeada, verificação, medição independente, desenho de processo, memória de decisão com trilha. **Não construir o que os laboratórios dão de graça.**
5. **O calendário trabalha para nós:** IBS/CBS depois de amanhã, ANPD já fiscalizando, EU AI Act chegando por cláusula. Obrigação com data é o conversor mais barato de vitamina em analgésico.

---

## Fontes

Consolidadas das três pesquisas de 2026-08-01 (~90 buscas EN+PT). Principais, por seção — §1: Rohrbeck & Kum 2018 (TFSC 129) · Gartner CFO ago/2025 e MQ Decision Intelligence fev/2026 · State of Corporate Foresight 2025 (THI) · McKinsey IBP · EY Desafios e Tendências · KPMG Brasil 2026. §2: Metaculus Cup 2026 · ForecastBench/FRI (com o conflito de interesse anotado) · Kim, Muhn & Nikolaev (arXiv 2407.17866) · inverse scaling (arXiv 2605.22672) · causal (arXiv 2505.18931, 2505.13770) · TSFM leakage (arXiv 2510.13654) · synthetic users (arXiv 2607.26348). §3: Hu et al. 2025 (JBDM) · Mertens 2022 (PNAS) · AMLE 2023 RCT meta · Theeboom 2014 · Sull HBR 2015 · McKinsey State of Organizations 2026 e realocação · Klein HBR 2007. §4: Epoch AI · ISO CG 40 47 01 26 / Fenwick / ABA · METR RCT 2025 + update fev/2026 · MAST (arXiv 2503.13657) · Gartner jun/2025 · Axios/CNBC (DeployCo, mai/2026) · Google Memory Bank pricing. §5: Senado/Câmara (PL 2338) · ANPD Mapa 2026-27 · Gibson Dunn/Freshfields (Digital Omnibus) · Conjur fev e jul/2026 · Deloitte Tax do Amanhã 2026 · CRCSP · CNI jul/2026 · Cetic.br TIC Empresas 2025 (a única amostra probabilística de adoção de IA no Brasil: **17%** — ancorar nela, não nos 61% de fornecedor).
