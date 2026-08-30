# Estudo — O Conselheiro Corporificado: o que significaria dar um corpo ao cérebro da empresa

> **Camada:** interno (pesquisa + registro de aposta). Origem: pedido do sócio (2026-08-30) — *"imagine se nós conseguíssemos materializar um conselheiro dentro da empresa... um humanoide mesmo, ajudando as pessoas, visitando as partes da empresa, com câmeras e acesso a tudo que está acontecendo... fazendo o gerenciamento... e o treinamento das empresas, que nem sempre eu e Pedro poderemos estar presencialmente."*
>
> **O que este documento é:** a pesquisa diligente que responde à pergunta — o que existe de humanoide em 2026, o que custaria, o que a doutrina da casa permite, e qual é o potencial real para a ABBA — mais o plano em degraus com gatilhos. **Nada aqui está construído nem é promessa comercial.** Este estudo alimenta a [Aposta 7](../00-identidade/apostas-futuras.md) e obedece à regra das apostas: registrar, não investir.
>
> **Como ele se encaixa:** este é o terceiro estudo da mesma pergunta. O [estudo do Conselheiro presente](estudo-conselheiro-presente.md) respondeu *como ele se senta, escuta e responde* (O Assento, 5 camadas). O [estudo do dia a dia](estudo-conselheiro-dia-a-dia.md) respondeu *quando e por onde ele aparece* (4 relógios, 24 situações). Este responde: **e se ele tivesse um corpo?**
>
> Dono: chapéu Tecnologia (arquitetura) + Comercial (o que pode ser dito). Revisar quando a ISO 25785-1 for publicada ou quando o primeiro humanoide comercial de escritório existir de verdade.

---

## 1. A resposta curta, antes da pesquisa longa

**O humanoide imaginado — que circula pela empresa do cliente, observa com câmeras, conversa com diretores sobre tudo o que viu e treina as equipes — não existe como produto em 2026.** Nenhum humanoide no mundo opera comercialmente "andando num escritório e conversando". Tudo o que funciona de verdade hoje é fábrica e galpão: tarefa repetitiva, ambiente controlado e cercado, ROI medido em caixas movidas.

Mas a pesquisa devolve três achados que valem mais do que um "ainda não":

1. **~90% do valor do cenário imaginado é software — e é exatamente o software que a ABBA já construiu.** A memória que nunca esquece, o diário de decisões com resultado medido, a fila da manhã, a resposta fundada nos dados reais da empresa: isso é o assessment-brain e o Conselheiro Digital, que existem em código hoje. O corpo é os 10% restantes — e é a parte mais cara, mais imatura e mais arriscada juridicamente.
2. **A parte do corpo que já funciona não precisa ser humana.** "Olhos que circulam" existem comercialmente (quadrúpedes de inspeção, 1.500+ Spots implantados); "boca e ouvido" existem (avatar/quiosque com voz sobre RAG); "presença do consultor à distância" existe (telepresença). O que não existe é o pacote inteiro num bípede confiável — e não existirá em condição comprável e segurável antes de **~2029–2031**.
3. **O timing da aposta coincide com o Horizonte 3 da [Visão 2029](../00-identidade/visao-2029.md).** Se a ABBA cumprir o caminho (provar → compor → ser infraestrutura), ela chega em 2029 com o único componente do humanoide que ninguém vende: um cérebro por cliente com anos de memória curada e resultado medido. Quem tiver isso **pluga o corpo quando o corpo ficar pronto**. Quem não tiver, terá um manequim caro com um chatbot dentro.

A reformulação que este estudo defende, no mesmo espírito do [Assento](estudo-conselheiro-presente.md):

> **O corpo não é o produto. O corpo é uma superfície futura do mesmo Conselheiro — e só vale alguma coisa se o cérebro chegar lá com anos de memória acumulada. A corrida de agora não é comprar um robô: é acumular o que fará qualquer robô valer a pena.**

---

## 2. O estado real dos humanoides em agosto de 2026

Pesquisa de mercado completa (17 buscas, fontes citadas ao fim). Legenda: **[FATO]** = verificado em operação/documento público · **[PROJEÇÃO]** = plano anunciado · **[HYPE]** = demo sem operação real.

### 2.1 O que opera de verdade (não em demo)

| Robô | Status ago/2026 | Operação real |
|---|---|---|
| **Figure 03** (Helix) | [FATO] contrato comercial pago | BMW Spartanburg: ~40 unidades em sequenciamento logístico; o Figure 02 participou da montagem de ~30.000 carros em 2025 |
| **Agility Digit** | [FATO] 1º RaaS humanoide da história | GXO (galpão Spanx, desde jun/2024): >100.000 totes movidos, contrato plurianual |
| **Apptronik Apollo** | [FATO] piloto medido | Mercedes-Benz (Berlim + Hungria), intralogística; case de abr/2026 reporta **+14% de throughput** |
| **Boston Dynamics Atlas** | [FATO] produção iniciada jan/2026 | Hyundai Metaplant; manuseio de painéis em fábrica |
| **UBTech Walker S2** | [FATO] produção em massa | Pedidos > ¥800 mi; centenas entregues a BYD, Foxconn, SF Express; troca a própria bateria |
| **AgiBot/Zhiyuan** | [FATO] maior volume mundial | >5.100 unidades entregues em 2025 (~40% do mercado global) |
| **Unitree G1/R1/H2** | [FATO] venda direta (China) | Na prática é **plataforma de P&D**, não trabalhador autônomo; pilotos de bagagem (Japan Airlines) e limpeza |
| **Tesla Optimus** | [PROJEÇÃO] | >1.000 unidades **de uso interno** (coleta de dados); 8-K de jul/2026 confirma que produção formal não começou; zero clientes externos; preço-alvo US$ 20–30 mil = [HYPE] |
| **1X NEO** (doméstico) | [PROJEÇÃO] pré-venda | US$ 20 mil ou US$ 499/mês; >10.000 pré-vendas; **nenhuma entrega verificada**; autonomia ~60–70% — o resto é **teleoperador humano olhando pela câmera** (polêmica grande de privacidade) |

**O padrão que importa:** tudo que funciona é tarefa estreita em ambiente controlado. Os robôs que **conversam** bem (recepcionistas com LLM demonstrados no CES 2026) são bustos e quiosques que não andam. O robô que anda não conversa; o que conversa não anda.

### 2.2 Os "cérebros" de prateleira (modelos de fundação para robótica)

- **NVIDIA Isaac GR00T N1.7** — [FATO] aberto sob Apache 2.0 (uso comercial liberado); exige pós-treino com dados do próprio robô + stack Isaac/Jetson. O caminho mais "comprável" para quem constrói.
- **Google Gemini Robotics-ER** — [FATO] o modelo de **raciocínio incorporado** está disponível via API em preview público: planejamento espacial, apontar objetos, orquestrar ferramentas. **A peça mais útil para o caso ABBA** (analisar o que a câmera vê). O VLA de controle motor fica restrito a parceiros.
- **Physical Intelligence π0/π0.5** — [FATO] pesos abertos para pesquisa; comercial via parceria; estado da arte em generalização de manipulação.
- **Figure Helix** — [HYPE para terceiros]: impressionante (voz→ação de corpo inteiro), mas 100% proprietário. Não se compra.

**Tradução:** o cérebro *conversacional/analítico* se compra por API hoje — e a ABBA já opera essa camada. O cérebro *motor confiável* não se compra: quem tem não vende; quem abre exige equipe de robótica.

### 2.3 Preços e modelos de contratação

| Item | Ordem de grandeza |
|---|---|
| Humanoide de trabalho ocidental (RaaS) | **~US$ 8.500/mês/robô (~US$ 100k/ano)** no modelo GXO/Agility; faixa geral estimada US$ 10–30/hora |
| Compra + integração | US$ 150k+ o robô, e a integração (célula, segurança, Wi-Fi, docas, gestão de mudança) custa outro tanto |
| Unitree G1 nos EUA/China | US$ 13,5–16k (EDU com mãos: US$ 43,9k) |
| **Unitree G1 no Brasil** | **R$ 265.050 a R$ 615.600** (representante oficial XD4Solutions/SP, entrega ~4 meses) — o multiplicador é imposto + margem. O regime **Ex-Tarifário pode zerar o II** para bem de capital sem similar nacional; estudar antes de qualquer importação |
| Unitree R1 (plataforma leve) | ~US$ 5,9k |
| Degraus não-humanoides | quiosque-avatar < US$ 5k · telepresença US$ 2–8k · Unitree Go2 (quadrúpede) US$ 11–24k · Boston Dynamics Spot US$ 74,5k base |

### 2.4 As limitações que nenhum vendedor menciona

- **Bateria:** 1–4 h de uso ativo (típico 90–120 min em movimento). Um "turno" de escritório não fecha.
- **Confiabilidade:** melhor caso público mensurado ~78% de conclusão de tarefas (AgiBot GO-1, depois de 1 milhão de trajetórias de treino); indústria exige 95%+ para operar sem supervisão. Uptime real de muitos robôs: 30–90 min entre intervenções humanas.
- **Teleoperação oculta:** dependência alta e frequentemente não divulgada. Pergunta obrigatória a qualquer fornecedor: *"qual o índice de intervenção humana?"* — no 1X NEO, ~30–40% do tempo é um operador humano **olhando pela câmera dentro da casa do cliente**.
- **Norma de segurança:** a **ISO 25785-1** (robôs móveis dinamicamente estáveis — o primeiro padrão para humanoides; o risco novo é a queda de um bípede de 70–90 kg) ainda é **rascunho**; publicação esperada fim de 2026–2027. **Sem norma → sem base clara de seguro e compliance** para um humanoide transitando livre entre pessoas. É por isso que toda implantação real cerca e zoneia o robô.
- **Manipulação genérica:** não confiável fora do treinado. "Pega qualquer coisa em qualquer lugar" é a fronteira de pesquisa, não produto.

### 2.5 Mercado e linha do tempo

- Projeções: Goldman Sachs US$ 38 bi até 2035; Morgan Stanley US$ 5 tri até 2050 (~90% industrial até os anos 2030); Omdia (conservador) 38 mil embarques/ano em 2030. Dispersão de 4×+ entre as casas = especulação. A IEEE Spectrum chama o mercado de "quase inteiramente hipotético".
- **China lidera volume e preço; EUA lideram software de ponta.**
- **2027:** primeiros humanoides realmente à venda no Ocidente (Apollo 3; Atlas em escala Hyundai); ISO publicada.
- **2027–2028:** expansão em logística/manufatura; escritório segue nicho experimental.
- **2029–2031:** estimativa razoável para um "conselheiro corporificado" **comprável e segurável** em ambiente de escritório — o que exige justamente o que menos evoluiu: interação social segura, manipulação genérica, bateria de turno e custo < US$ 50k.
- [HYPE] Qualquer promessa de humanoide generalista de escritório "ano que vem".

---

## 3. A visão do sócio, testada capacidade por capacidade

O cenário imaginado, decomposto contra o que 2026 entrega:

| Capacidade desejada | Viável em 2026? | A realidade |
|---|---|---|
| **Circular pela empresa** | PARCIAL | Navegação autônoma em ambiente mapeado funciona (quadrúpedes fazem comercialmente). Em bípede: 1–2 h de bateria, risco de queda, sem norma para trânsito livre entre pessoas |
| **Observar operações e detectar falhas** | SIM* | *Como câmera móvel + VLM analisando o feed (é o que o Spot já faz em inspeção industrial). **Não exige forma humana** — e no escritório esbarra na §5 |
| **Conversar com diretores fundado nos dados reais da empresa** | **SIM — e é software** | RAG + voz sobre o cérebro por cliente. Roda em qualquer corpo, ou em nenhum. **É o core da ABBA** |
| **Acesso aos protótipos, deploys e gerenciamento dos serviços** | SIM — e é software | É a camada 3 do Assento ("Os Olhos", conectores só-leitura via MCP) + o Dossiê Vivo. Nada disso precisa de pernas |
| **Treinar as equipes do cliente** | NÃO [HYPE] | Nenhum humanoide entrega treinamento autônomo comercialmente. O que existe são avatares/quiosques com LLM — e a evidência da casa (abaixo) pesa contra |
| **Demonstrar tarefas físicas** | NÃO | Manipulação genérica não confiável fora do treinado |

**Veredito da tabela:** as duas linhas de maior valor (conversar fundado nos dados; gerenciar o que foi construído) **já são o produto da ABBA e não precisam de corpo**. As linhas que precisam de corpo ou não existem (treinar, demonstrar) ou não precisam de *corpo humano* (observar) ou são juridicamente as mais perigosas (circular observando — §5).

---

## 4. O ponto do treinamento — a parte da visão com a tensão mais honesta

A motivação é real: *"nem sempre eu e Pedro poderemos estar presencialmente em todas as empresas."* O gargalo de escala existe e está registrado — o presencial custa presença de sócio (é o que justifica o híbrido a R$ 35 mil contra R$ 15 mil do online), e a capacidade dos dois sócios é o gargalo nº 3 apontado pelo [conselho](parecer-conselho-2026-08.md).

Mas três fatos da própria casa pesam contra "o humanoide treina":

1. **A evidência que fundamenta o produto aponta o contrário.** O [estudo de antecipação](estudo-antecipacao.md) cravou: coaching humano em cadência muda comportamento (g = 0,59); nudge automatizado não muda (d = 0,004 após correção de viés). *"O que muda comportamento de gestão é uma pessoa aparecendo num ritmo."* Um humanoide dando aula é, na melhor hipótese de 2026, um nudge caro com pernas — a menos que seja teleoperado, e aí é um sócio trabalhando do mesmo jeito, com um custo de RaaS de ~US$ 100k/ano no meio.
2. **O que escala o treinamento já foi construído e está travado por outra coisa.** A escala do treinamento da ABBA é o **portal + turma nomeada + campeões**: a plataforma instala o assíncrono, o presencial dos fundadores vira o momento de marco (kickoff e graduação), e os **campeões graduados** — o nível 4 se chama, não por acaso, **Arquiteto/Multiplicação** — carregam o dia a dia. O bloqueio real hoje não é falta de corpo: é **R5 (vídeos não gravados)** e a trava V4a (turma não se vende sem conteúdo no ar). Gravar 3 vídeos custa um fim de semana; um humanoide custa meio milhão.
3. **A doutrina de vocabulário.** *"Nunca parear ABBA + treinamento como produto."* Um robô-instrutor seria a materialização máxima do erro: posicionaria a ABBA no orçamento de RH/L&D — e na prateleira de gadget.

**A versão defensável da intuição:** quando houver humanoide viável (2029+), o papel dele no treinamento não é *dar a aula* — é ser **o rosto do Conselheiro nos momentos de marco** quando o sócio não puder ir: abrir o kickoff com o dossiê daquele cliente, responder perguntas na graduação fundado na memória daquele engajamento. Presença episódica, anunciada, com conteúdo que só a ABBA tem. Isso preserva a tese (a pessoa em cadência continua sendo o campeão + o ritual com sócio) e usa o corpo para o que corpo serve: ocasião, não cadência.

---

## 5. O confronto com a doutrina — o que um humanoide pode e não pode ser na casa

A ABBA já escreveu as regras que qualquer corporificação herda. Elas não proíbem o corpo; proíbem **um jeito específico de usá-lo** — que é exatamente o jeito imaginado ("vigiando, estando lá, tempo que for disponível").

### 5.1 As 8 recusas do Assento, aplicadas ao robô

Um humanoide circulando permanentemente com câmeras viola de cara as recusas 1 (captura ambiente permanente), 3 (análise de indivíduos) e 7 (guardar o bruto) — e o [estudo do Assento](estudo-conselheiro-presente.md) já mostrou o porquê com dados: presença de gravador degrada o dado (84% mudam de comportamento), diarização erra (5–30%), memória total é exposição total, e no Brasil monitorar sem ciência prévia e expressa é **passivo trabalhista** (TST), com a LGPD exigindo base legal documentada e o PL 2338 trazendo avaliação de impacto algorítmica e multa de até R$ 50 mi — com monitoramento de trabalhadores entre os usos sensíveis. Um robô é, para o DPO do cliente, **uma câmera andante com microfone**: a superfície de captura mais agressiva possível.

**A consequência de desenho, não de covardia:** o humanoide da ABBA, se existir, será **o corpo do Assento — convidado, anunciado, com hora de entrar e sair. Nunca "no ar".** Ele toma assento na reunião de conselho, abre o kickoff, atende na sala que o cliente designou. Ele não patrulha corredor. O que patrulha (se o cliente contratar inspeção física de ativos — fábrica, estoque, obra) é caso de uso industrial com quadrúpede, zona demarcada e política própria — outro produto, outra prateleira, provavelmente outro fornecedor com a ABBA como árbitro.

### 5.2 Os invariantes de arquitetura que o corpo herda

Já estão em código e não se negociam:

- **Autoridade de origem:** tudo que o robô vê e ouve entra como `llm_inference`/`tool_output` — **nunca** vira verdade sem confirmação humana nomeada. O robô não escreve fatos; ele propõe.
- **Gate de humano nomeado:** o robô não assina recomendação, não aprova brief, não declara probabilidade. A IA propõe, o especialista assina, a diretoria decide — com corpo ou sem.
- **Nada dispara sozinho:** o robô não age no mundo do cliente por conta própria. Fila da manhã, conferência humana.
- **Um cérebro por cliente, segregado:** o corpo que visita o cliente A não carrega nada do cliente B. E `abba forget` precisa alcançar tudo que o corpo capturou — áudio e vídeo inclusive, descartados por padrão após extração.
- **Nunca prometer o que não medimos:** "o robô conhece sua empresa" só se diz quando a curva de tenure provar.

### 5.3 O inegociável nº 7 e a prateleira

*"Não virar agência generalista — uma espinha, um segmento."* Construir robótica própria seria a violação máxima: outra engenharia, outra cadeia de suprimento, outro regulatório, outro capital. **A ABBA nunca constrói humanoide.** Se um dia operar um, será comprado/alugado (RaaS), como hoje se compra API de LLM — e a [Visão 2029](../00-identidade/visao-2029.md) já deu o modelo mental: *"a infraestrutura é grátis (ou de prateleira); a autoridade sobre o conteúdo não é."* O corpo vai virar commodity como a memória virou. **O que não vira commodity é o que o corpo diria** — a memória curada, o diário de decisões, a prova. Essa é a parte da ABBA, e ela já está em construção.

---

## 6. O potencial real — por que a intuição está certa, apesar de tudo

Depois de todos os "ainda não", o que sobra é substancial:

1. **A ABBA já tem a peça que faltará a todo mundo.** Quando o corpo virar commodity (2029+), o mercado vai descobrir o que o mercado de LLM descobriu: o hardware sem contexto é um brinquedo de demonstração. Um humanoide genérico na recepção responde generalidades. Um humanoide plugado num cérebro com 3 anos de `facts` bitemporais, decisões com resultado medido e playbooks daquele cliente é **o Conselheiro de pé**. A fronteira dos "Company Brains" da Visão 2029 (§1.4) vale idêntica para robôs: *não capturam o que nunca foi escrito, não decidem o que é verdade, não assinam perante o regulador*. O robô agrava essa fronteira; a ABBA vive dela.
2. **O slogan fecha.** "O cérebro da sua empresa" materializado num corpo que toma assento no conselho é a imagem de marketing mais forte que a ABBA poderia ter — e diferente de 2026-hype, ela é **honesta se for episódica**: o corpo aparece nos marcos, o cérebro trabalha todas as noites. A onipresença continua sendo a memória, não o microfone.
3. **A governança vira produto de novo.** Quando humanoides chegarem às empresas brasileiras, chegarão sem política, sem LIA, sem base legal — como a IA generativa chegou (63% das empresas sem política de IA). A ABBA, que já vende Sprint LGPD e governança de IA, estará posicionada para vender **governança de robótica incorporada** — avaliação de impacto, política de captura, zona e protocolo — antes de vender ou operar qualquer robô. É a porta com data: a ISO 25785-1 e o PL 2338 criam a obrigação; a ABBA já é a firma da obrigação com data.
4. **O caminho tem degraus que pagam a si mesmos** (§7): cada passo de corporificação abaixo do humanoide já entrega valor vendável hoje e acumula exatamente o ativo que o humanoide precisará.

O que **não** fazer com esse potencial: anunciá-lo. A régua do Revisor já bloquearia "presente em todos os lugares" — e o parecer do conselho foi unânime: a ABBA precisa de **um caso medido**, não de mais uma fronteira. Este estudo existe para que a aposta não se perca e para que nenhuma decisão de hoje a impossibilite — não para virar slide.

---

## 7. A escada de corporificação — do que existe hoje ao corpo

No espírito da escada ABBA: **cada degrau entrega valor inteiro sozinho e produz o insumo do degrau seguinte.** Nenhum degrau começa sem o anterior fechado — e os degraus 1+ só depois do 1º caso medido (a moratória do conselho vale aqui em dobro).

| Degrau | O quê | Custo (ordem de grandeza) | O que entrega sozinho | Gatilho |
|---|---|---|---|---|
| **0 — O cérebro ativado** (em curso) | Validação com LLM real, golden set, cron do sono, 1º caso medido | ~US$ 1 + horas de sócio | Tudo. É o pré-requisito de todos os outros | [runbook](../06-ferramentas/runbook-ativacao.md) |
| **1 — A Voz** (camada 2 do Assento) | Portal (área do conselho) + WhatsApp para avisos | baixo (meses de calendário, não de custo) | O diretor conversa com o Conselheiro — sem corpo | 1º cliente em manutenção |
| **2 — O Rosto** | Quiosque-avatar na sala de conselho do cliente: tela + voz + RAG sobre o cérebro daquele cliente. Presença episódica, anunciada, operada | < US$ 5k + API | 80% da experiência "conversar com o Conselheiro em pessoa"; testa TUDO da interação (latência, voz, protocolo, LGPD) por 1% do preço do robô | Cliente na camada Estratégia pede; protocolo do Assento escrito |
| **3 — Os Olhos móveis** | Telepresença (US$ 2–8k) para sócio "andar" remoto em marcos; e/ou, em cliente industrial, quadrúpede de inspeção com zona demarcada alimentando o cérebro | US$ 2–25k | O sócio multiplica presença sem viajar; inspeção vira episódio ingerível | Cliente com operação física pede; TI homologa; DPO aprova |
| **4 — O Corpo alugado** | Humanoide via RaaS para **ocasiões**: assento no conselho, kickoff, graduação. Nunca compra na 1ª fase, nunca patrulha | ~US$ 100k/ano RaaS (2026) — reavaliar preço em 2028 | O Conselheiro de pé nos marcos; diferenciação absoluta no mercado brasileiro | ISO 25785-1 publicada + seguro disponível + 5+ clientes de recorrência + custo < teto que os sócios definirem |
| **5 — (não fazer)** | Construir humanoide próprio; robô residente permanente no cliente; robô que "vigia" | — | — | Violaria inegociável 7, as recusas 1/3/7 e a prateleira. Registrado como recusa, não como degrau |

**Regra que atravessa a escada:** nenhum degrau vira frase de venda antes de existir — e todo degrau herda os invariantes da §5.2.

---

## 8. Custos de referência (para a conversa de sócios, não para tabela)

| Item | Número | Estado |
|---|---|---|
| Humanoide RaaS ocidental | ~US$ 8,5k/mês (~US$ 100k/ano) | [FATO] modelo GXO/Agility, jun/2026 |
| Unitree G1 no Brasil (compra) | R$ 265–616 mil | [FATO] representante oficial; Ex-Tarifário pode reduzir |
| Quiosque-avatar (degrau 2) | < R$ 30 mil + API | estimativa; **{{MEDIR}}** se o degrau abrir |
| Telepresença | R$ 15–50 mil | [FATO] mercado maduro |
| Quadrúpede de inspeção | R$ 60–150 mil (Go2 importado) a R$ 400 mil+ (Spot) | [FATO] |
| O item dominante | **hora de sócio** em protocolo, curadoria e operação — como em tudo na casa | decidir teto antes de qualquer degrau |

---

## 9. Gatilhos de reavaliação (o que acorda esta aposta)

Registrados também na [Aposta 7](../00-identidade/apostas-futuras.md):

- [ ] **ISO 25785-1 publicada** e seguradora brasileira aceitando cobrir humanoide em ambiente com pessoas
- [ ] Primeiro humanoide comercial operando em **escritório** (não fábrica) em qualquer lugar do mundo, com índice de intervenção humana divulgado
- [ ] RaaS de humanoide disponível no Brasil por **< R$ 30 mil/mês**
- [ ] 5+ clientes de recorrência com cérebro ativo (a pré-condição interna — sem ela o corpo não tem o que dizer)
- [ ] Um cliente da camada Estratégia **pede** presença corporificada (o gatilho comercial honesto)

Enquanto nenhum acender: a regra das apostas — manter este registro e **não tomar hoje nenhuma decisão que impossibilite o corpo amanhã** (ex.: contratos de captura que não prevejam extensão a novas superfícies; arquitetura de voz do degrau 1 que não separe canal de conteúdo).

## 10. O que fazer nos próximos 30 dias

**Nada que custe dinheiro ou hora além disto:**

1. Registrar a Aposta 7 (feito junto com este estudo).
2. Seguir o [plano de ataque](../03-comercial/plano-de-ataque.md) — o 1º caso medido é o pré-requisito de todos os degraus, inclusive deste.
3. Assinar dois alertas de acompanhamento passivo (newsletter/RSS): publicação da ISO 25785-1 e lançamentos comerciais Apollo 3 / Atlas / NEO. Custo: zero.
4. Quando o degrau 1 (A Voz) for desenhado, desenhá-lo **já separando superfície de conteúdo** — a mesma resposta do cérebro deve poder sair por portal, WhatsApp, avatar ou corpo sem retrabalho. É a única decisão de hoje que o futuro corpo agradece.

---

## Ligações

[Aposta 7](../00-identidade/apostas-futuras.md) — o registro desta aposta · [Estudo do Conselheiro presente](estudo-conselheiro-presente.md) — o Assento, as 5 camadas e as 8 recusas que o corpo herda · [Estudo do dia a dia](estudo-conselheiro-dia-a-dia.md) — os relógios e situações onde a presença vale · [Visão 2029](../00-identidade/visao-2029.md) — §1.4 (a fronteira dos company brains, idêntica para robôs) e Horizonte 3 · [Dossiê Vivo](../04-entrega/dossie-vivo-conselheiro-digital.md) — o cérebro que o corpo plugaria · [Parecer do conselho](parecer-conselho-2026-08.md) — a moratória que este estudo respeita · [Registro de riscos](registro-de-riscos.md) — R1/R17 (o cérebro ainda não rodou com dados reais)

### Fontes da pesquisa de mercado (ago/2026)

BMW Group Press / The Robot Report (Figure 03 em Spartanburg) · Agility Robotics / GXO (Digit RaaS, >100k totes) · Apptronik/Mercedes (+14% throughput) · Tesla 8-K jul/2026 (SEC) · The Register / Boston Dynamics (Atlas em produção) · The Robot Report / eWeek (1X NEO e teleoperação) · PRNewswire (UBTech Walker S2, ¥800 mi) · RoboZaps / The Construct (preços Unitree) · NVIDIA (Isaac GR00T N1.7, Apache 2.0) · Google AI (Gemini Robotics-ER, API) · Physical Intelligence (π0) · ISO.org (ISO/CD 25785-1) · Goldman Sachs, Morgan Stanley, Omdia, IEEE Spectrum (projeções e ceticismo) · Economic News Brasil / XD4Solutions / Lili Vendas (Unitree no Brasil, R$ 265–616 mil) · Guelcos (tributos de importação e Ex-Tarifário) · RobotSourced (preços Spot) · Frontiers in Robotics (limites de interação por voz).
