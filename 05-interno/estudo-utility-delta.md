# A ABBA é útil? — o cálculo do utility delta

> ⚠️ **NOTA DE ATUALIZAÇÃO (V5, 2026-08-31) — ler antes de usar este
> estudo.** Este estudo fundamentou a decisão V4a e, na sequência, a Virada
> V5 — ver [estudo da virada](estudo-virada-v5.md) e
> [tabela v3](../03-comercial/tabela-de-precos.md). Menções no corpo a
> "protótipo avulso R$ 26 mil como porta" agora correspondem à **fase 1 do
> Programa** (mesmo valor, nova estrutura). A "jornada R$ 260 mil" virou o
> **Programa por porte** (P/M/G: R$ 218/278/378 mil).

> **Camada:** interno (estudo). Origem: pedido do sócio (2026-08-23) —
> *"me ajude a fazer esse cálculo e ver se a ABBA mesmo é algo útil"*.
> **Este é o estudo que originou a decisão V4a**: a
> [base de evidências](../00-identidade/base-de-evidencias.md), as 3
> verdades operacionais, as regras comerciais propostas e o
> [plano de ataque](../03-comercial/plano-de-ataque.md) saíram daqui.
> Números de cliente (ABC) são confidenciais — este documento não sai da
> firma e não vira material.

**Impacto = (Utilidade da nossa solução − Utilidade do estado da arte) ×
Número de pessoas afetadas**

Documento interno, escrito para ser honesto e não para ser agradável.
Base: repositórios, doutrina, transcrições das reuniões (Brasal, BDL
Hub, ABC DataSaúde), dashboards da ABC, e duas pesquisas de mercado com
auditoria de fonte (18 e 23/08/2026).

---

## 1. A regra do jogo (como não trapacear no próprio cálculo)

A fórmula tem uma armadilha: quase todo mundo infla o ΔU comparando a
própria solução com **fazer nada**. Isso é fraude intelectual. O
denominador correto é **a melhor alternativa que o cliente tem hoje**, e
ela é bem melhor do que "nada".

Segunda regra: **utilidade prometida não entra na conta.** Só entra o que
foi entregue e verificado. Método não é resultado enquanto não produzir
resultado.

Terceira: N não é o tamanho do mercado endereçável. É **o número de
pessoas cuja vida ou trabalho muda de verdade** por causa do que a gente
fez.

Com essas três regras, vamos.

---

## 2. O inventário honesto: o que a ABBA é HOJE

**O que existe e funciona (verificável):**

- **assessment-brain**: framework de 25 dimensões, motor de análise,
  cérebro do Conselheiro (fatos bitemporais, decisões com humano nomeado,
  calibração por Brier, consolidação de memória, auditoria noturna).
  É software real, testado, sofisticado. Rodou 3 assessments de teste.
- **abba-portal**: plataforma de capacitação com trilhas, desafios,
  fluency score, tiers, **durabilidade d30/60/90** e benchmark entre
  clientes com pisos de privacidade. Arquitetura pronta. **Sem conteúdo.**
- **Stack de agentes** (CrewAI): dois protótipos construídos. Um
  deployado e Online. 36 testes verdes no segundo.
- **Doutrina comercial completa**: escada de 7 serviços, tabela de preços
  com racional de engenharia, mapa de vazamento, protocolo de prova,
  coreografia da conversão, régua do que nunca dizer.
- **Rede**: Pedro dentro da CrewAI, parceria com Microsoft e CrewAI,
  acesso a conversas que ninguém de fora consegue.

**O que NÃO existe (e precisa ser dito):**

- **Zero engajamentos pagos concluídos. Zero resultados medidos.**
- O protótipo da ABC **falhou na validação** — e falhou exatamente na
  competência que vendemos: enquadrar o problema certo.
- O portal de treinamento **não pode treinar ninguém hoje**: sem aulas,
  sem conteúdo.
- O assessment web não está público.
- Duas pessoas. Capacidade real: 5 a 6 clientes simultâneos, no limite.

**Tempo de existência:** 3 a 4 meses.

Isso não é um julgamento moral — é o denominador do próprio cálculo. Uma
empresa de 4 meses não deveria ter resultado medido ainda. Mas ela também
não pode inflar o ΔU com o que ainda não provou.

---

## 3. O denominador: qual é o estado da arte de verdade

Uma empresa brasileira de médio porte que quer usar IA na operação hoje
tem, no mínimo, seis alternativas. O ΔU da ABBA é diferente contra cada
uma — e essa é a parte que a maioria das consultorias nunca faz.

| Alternativa | O que ela entrega | ΔU da ABBA contra ela |
|---|---|---|
| **Não fazer nada / ChatGPT avulso** | Ganho individual, zero transformação | **Altíssimo** — mas esse cliente raramente compra consultoria |
| **Time interno construindo com IA** | Rápido, barato, feito por quem conhece o processo | **Baixo e caindo** ⚠️ |
| **Consultoria grande** (Accenture, Deloitte, KPMG) | Marca, método, relatório | **Alto**: preço (45k vs 80k+), sistema em vez de slide, medição |
| **Fábrica de software / dev shop** | Constrói o que você pedir | **Alto**: eles constroem o que você pede; nós descobrimos o que pedir |
| **SaaS vertical / no-code** | Barato, imediato, genérico | **Médio-alto**: cabe no processo real em vez de forçar o processo a caber |
| **Provedores de treinamento** (StartSe, Alura/FIAP, IFTL) | Conteúdo pronto, escala, marca | **Negativo hoje** ⚠️ — nosso portal não tem conteúdo |

### O alerta: a alternativa nº 2 está subindo — mas menos do que parece

Duas provas colhidas nesta semana, dentro dos nossos próprios clientes:

- **Brasal**: o time do Rafa (5 devs) refez internamente, **em 2,5 a 3
  semanas com IA**, o aplicativo de força de vendas que um fornecedor
  levou 1 ano e meio e cobrava **R$ 200 mil por atualização**. Setenta
  páginas de regra de negócio. Sem bug crítico.
- **ABC DataSaúde**: o Alan construiu **sozinho** o GMPC inteiro — CRM,
  regulação, expedição, logística, faturamento, integração com Correios.

**Conclusão que se mantém: "capacidade de construir com IA" não é mais um
diferencial vendável.** Quem tem um Alan ou um Rafa não precisa de nós
para construir.

**Mas a pesquisa mostrou que a história é mais interessante do que
"todo mundo vai construir sozinho".** Os três estudos sérios que existem
sobre produtividade de dev com IA não concordam entre si — e é justamente
a discordância que é útil:

| Estudo | Amostra | Resultado |
|---|---|---|
| **Cui et al.**, *Management Science* (revisado por pares) | 3 experimentos randomizados, **4.867 desenvolvedores** (Microsoft, Accenture, Fortune 100) | **+26% de tarefas concluídas.** Os menos experientes ganharam mais |
| **Google**, RCT interno | 96 engenheiros | ~21% mais rápido, com intervalo de confiança largo |
| **METR** (jul/2025) | 16 devs experientes, 246 tarefas reais, código que dominavam há ~5 anos | **19% MAIS LENTOS com IA** |

A reconciliação honesta: **a IA acelera quem tem menos domínio do
contexto e atrapalha quem já domina.** E o **DORA 2025** (Google, ~5.000
respondentes) explica o mecanismo com uma frase que vale a estratégia
inteira: **"a IA não conserta um time; ela amplifica o que já está lá"**
— adoção de IA correlaciona **positivamente com throughput e
negativamente com estabilidade** (mais falhas, mais retrabalho).

**E o achado que é munição direta para nós:** no estudo do METR, os
desenvolvedores **previram +24% de ganho antes e estimaram +20% depois —
enquanto na verdade tinham ficado 19% mais lentos.** Um erro de percepção
de quase 40 pontos. **Ninguém sabe se a IA ajudou, nem quem está fazendo
o trabalho.** Isso não é opinião nossa: é medição publicada. E é a prova
de que **autorrelato não vale nada e medição externa é necessária** — que
é exatamente o que a ABBA vende.

**O contrapeso de risco do caminho interno** (relevante especialmente na
ABC, que trata dado de saúde): varredura de 5.600 aplicações construídas
por "vibe coding" em produção encontrou ~2.000 vulnerabilidades críticas,
400 segredos expostos e 175 casos de exposição de dados pessoais,
incluindo prontuários médicos. Incidentes com CVE registrado: inversão de
controle de acesso em 170 apps (Lovable), bypass de autenticação em
plataforma inteira (Base44), agente apagando base de produção (Replit).
Construir rápido sozinho tem um custo que só aparece depois.

---

## 4. ΔU decomposto: onde a ABBA é realmente melhor

Separando o que sobrevive ao escrutínio do que não sobrevive:

### ΔU real e defensável

**(a) Diagnóstico que acha o que a empresa nega.** Este é o mais forte, e
agora tem **prova empírica de um dia**: na visita à ABC, o Bernardo disse
que o problema era a expedição, o Alan disse que a operação era "redonda,
curta demais pra otimizar" — e os painéis mostraram **37% das entregas em
trânsito atrasadas e 58 pedidos parados sem nenhuma pendência**. Nenhum
dos dois tinha feito essa leitura. Ela custou um dia de trabalho.

Isso é utilidade entregue, verificável, e ninguém no mercado vende
explicitamente "encontrar a contradição entre o que o dono acredita e o
que a operação faz".

**(b) Disciplina de medição — e agora com a melhor fonte disponível
dizendo exatamente isso.** A pesquisa mais rigorosa que existe sobre por
que projetos de IA falham é da **RAND** (65 entrevistas com cientistas de
dados e engenheiros de ML com 5+ anos de experiência): **mais de 80% dos
projetos de IA falham, o dobro da taxa de projetos de TI sem IA.** E a
**causa número 1** não é técnica:

> projetos iniciados **sem critério de sucesso definido**, com
> desconexão entre o que o projeto tentava alcançar e o que a
> organização precisava.

Isso é, palavra por palavra, a doutrina da casa ("número combinado
antes, medido depois") validada pela fonte mais séria do assunto. Some a
isso o gap de percepção do METR (ninguém sabe se funcionou sem medir) e
o DORA (a IA amplifica a base que já existe), e você tem **três linhas
independentes de evidência convergindo no nosso posicionamento**.

Honestidade metodológica: não existe um experimento controlado provando
que "adicionar medição aumenta a taxa de sucesso em X%". O argumento é
por convergência de evidência, não por prova causal. Vale dizer assim.

O portal já mede **durabilidade de comportamento em 30/60/90 dias**, que
é a métrica que o mercado recomenda e quase ninguém tem.

**(c) Enquadramento do problema certo.** Que a gente errou uma vez e
corrigiu com método é, ironicamente, evidência de que o método funciona:
a visita produziu o diagnóstico de por que o protótipo falhou (frete
tabelado = decisão já tomada por contrato) e três candidatos melhores.

**(d) Legitimidade externa.** O Alan não vai dizer ao Bernardo que a
operação dele tem 37% de atraso. Um terceiro diz. Isso não é técnico, é
político, e é insubstituível por ferramenta.

**(e) Memória institucional auditável** (o Conselheiro). Ninguém no
segmento de PME brasileira tem fatos bitemporais, decisões com dono
nomeado e calibração de previsão. É genuinamente à frente — **e
genuinamente não vendido ainda**.

**(f) A lacuna de mercado, confirmada pela pesquisa.** Preço por
resultado já é mainstream no topo (a McKinsey declarou que ~25% da
receita global de 2025 veio de contratos baseados em resultado). Mas no
segmento de média empresa brasileira a lacuna é real e tem três causas
estruturais: **as Big 4 não descem** (o piso de ticket delas não fecha),
**as boutiques locais não publicam método** (repetem "ROI de 3x a 8x"
sem fonte — literalmente a mesma frase copiada entre sites), e **as
fábricas de software vendem hora, não resultado**.

Uma ressalva de honestidade que vale para o pitch: a medição que existe
no mercado é quase toda **do próprio vendedor** — quem define a métrica,
mede a métrica e reporta a métrica é quem está vendendo. E é frouxa:
segundo a Wharton (out/2025), 72% dos líderes dizem ter acompanhamento
estruturado de retorno, mas metade usa "melhoria de qualidade de dados"
como métrica e 53% reportam retorno de apenas 1 a 5%. **A lacuna
específica não é "medir IA" — é medição independente, combinada antes,
para a média empresa brasileira.** Esse é o espaço exato da ABBA.

### ΔU frágil ou negativo (a parte desconfortável)

- **"Sabemos construir com IA"** → encolhendo, como mostrado acima.
- **"Temos plataforma de treinamento"** → o portal não tem conteúdo.
  Contra a StartSe ou a Alura/FIAP, hoje, o ΔU é **negativo**. Vender
  treinamento antes de resolver isso é vender o que não temos.
- **"Método validado"** → validado em experimento, não em cliente.
- **Capacidade de entrega** → duas pessoas. Contra qualquer fornecedor
  com equipe, o ΔU de capacidade é negativo.

---

## 5. O cálculo com números reais: o caso ABC DataSaúde

É o único cliente onde tenho números de verdade. Vamos fazer a conta que
nunca fazemos.

**Dados observados (agosto/2026):** 3.106 entregas/mês · R$ 29,7 milhões
faturados/mês · ticket médio R$ 9.564/entrega · 21 a 50 funcionários ·
37% do que está em trânsito, atrasado.

### Caso B — nota fiscal (redigitação no Vetor)

- 3.106 notas/mês, cada uma exigindo recadastro completo (paciente,
  medicamento, preço, endereço).
- A 4 minutos cada: **207 horas/mês** ≈ 1,3 pessoa em tempo integral.
- A R$ 34/hora (custo cheio de operacional em Brasília): **~R$ 7.000/mês
  = R$ 84 mil/ano**.

### Caso A — guias (redigitação + consulta de hora em hora)

Volume ainda desconhecido. **Não invento.** É uma das 19 perguntas
pendentes. Mas o comportamento já observado — pessoas atualizando um
portal de hora em hora — é puro desperdício de espera.

### Caso C — o atraso

37% de R$ 29,7 milhões ≈ **R$ 11 milhões por mês de medicamento
oncológico entregue fora do prazo**. Isso NÃO é perda; é **exposição**:
multa contratual, reentrega, demanda judicial, risco de perder convênio,
e paciente sem remédio de uso contínuo. A perda real é uma fração disso,
e **não tenho como calcular sem os dados deles.**

### A conclusão que essa conta produz (corrigida com preço de mercado)

A pesquisa trouxe as faixas praticadas no Brasil, o que permite fechar a
conta de verdade. Contra o que competimos, para um trabalho do tamanho do
Caso B (integrar dois sistemas / automatizar emissão):

| Alternativa | Faixa |
|---|---|
| Fábrica de software (80 a 300 h) | **R$ 15 mil a R$ 60 mil** |
| Automação RPA por boutique | R$ 12 mil a R$ 40 mil |
| Diagnóstico de boutique de IA | R$ 3 mil a R$ 40 mil |
| Primeiro caso de uso (piloto + implantação) | R$ 30 mil a R$ 120 mil |
| **Protótipo ABBA** | **R$ 26 mil** |
| **Assessment ABBA** | **R$ 45 mil** |
| **Jornada completa ABBA** | R$ 260 mil (faixa 220–320, [tabela v2](../03-comercial/tabela-de-precos.md)) |

*(Ressalva importante: essas faixas vêm de blogs dos próprios
fornecedores. Ninguém no Brasil publica preço auditado. Use como ordem
de grandeza.)*

Isso muda o veredito em duas direções opostas:

**✅ O protótipo avulso FECHA.** R$ 26 mil contra R$ 84 mil/ano de
economia é **payback em 4 meses** — e o nosso preço está no meio da
faixa de fábrica de software, com diagnóstico e medição incluídos, que
fábrica nenhuma entrega. **Essa venda se sustenta sozinha, hoje, com o
número que já temos.**

**❌ A jornada completa NÃO fecha** com o argumento de digitação. R$ 260
mil contra R$ 84 mil/ano é payback de quase 4 anos. Para vender a
jornada, é obrigatório o **Caso C** — o atraso, a exposição, a capacidade
de crescer sem contratar. E é justamente o caso que eles **não pediram e
não enxergam**, e para o qual **ainda não temos o número**.

**⚠️ E um alerta de posicionamento:** nosso Assessment a R$ 45 mil está
**no topo ou acima** da faixa de diagnóstico praticada por boutiques
brasileiras (R$ 3 a 40 mil) — e nós ainda não temos um único caso medido.
Preço de topo de mercado sem prova é a combinação mais difícil de vender
que existe. Ou o Assessment entra creditado no protótipo, ou entra depois
da prova, ou vira um degrau menor.

Isso reordena a estratégia: as 19 perguntas não são "complemento de
diagnóstico" — **são a condição de existência da venda grande.** E o
caminho de entrada correto na ABC é **um protótipo de R$ 26 mil que se
paga em 4 meses**, não a jornada.

---

## 6. N: quem é afetado de verdade

Aqui está a correção mais importante do cálculo, e ela funciona a nosso
favor — desde que a gente escolha os clientes certos.

**O erro comum:** contar funcionários do cliente. Na ABC seriam 21 a 50
pessoas. N pequeno, impacto pequeno.

**A conta certa:** na ABC, quem é afetado por entrega confiável de
medicamento oncológico são **~3.100 pacientes ativos por mês, cerca de
37 mil entregas por ano** — pessoas em tratamento contínuo de câncer e
doença crônica, para quem atraso não é inconveniência, é interrupção de
tratamento.

**N na ABC ≈ 3.100 pessoas, com utilidade por pessoa altíssima.**

Agora compare as três frentes de hoje, honestamente:

| Frente | N real | ΔU por pessoa | Impacto |
|---|---|---|---|
| **ABC DataSaúde** | ~3.100 pacientes oncológicos/crônicos | **Altíssimo** (continuidade de tratamento) | 🟢 **O maior de longe** |
| **Brasal** | 70 a 200 treinados; e a operação de refrigerantes toca milhares de pontos de venda | Médio (capacidade, eficiência) | 🟡 Alto se for capacitação com aplicação real |
| **BDL Hub** | ~500 a 2.000 convidados por evento | **Baixo** (conveniência de convite de festa) | 🔴 **O menor dos três** |

**E aqui está a ironia que precisa ser dita:** a frente comercialmente
mais avançada — proposta enviada, escopo fechado, régua pronta — é a de
**menor utilidade social e menor ΔU**. Convite de festa é conveniência.
Medicamento oncológico chegando no prazo é outra categoria de coisa.

Isso não significa abandonar o BDL Hub. Ele tem valor real: primeiro caso
pago, primeira prova medida, e o Bruno é um conector. Mas se a pergunta é
"a ABBA é útil?", a resposta honesta é: **ela é utilíssima na ABC,
razoavelmente útil na Brasal, e marginalmente útil no BDL Hub.**

---

## 7. O veredito

**A ABBA é útil? Sim — mas não pelo motivo que está no pitch, e ainda
não provado.**

**O que é verdade hoje:**

1. **A utilidade comprovada da ABBA é diagnóstica, não construtiva.** Em
   um dia de visita, encontramos numa empresa o que o dono e o líder
   técnico dela negavam existir. Isso tem valor real e escasso.
2. **O ΔU de "construir com IA" está evaporando** e não deve ser o eixo
   do posicionamento. Alan e Rafa provam isso dentro dos nossos próprios
   clientes.
3. **A disciplina de medição é o ativo mais defensável**, porque o
   mercado inteiro falha nela por escolha (é mais fácil vender sem
   medir) e nós escolhemos o contrário.
4. **Nada disso está provado com resultado medido em cliente.** Enquanto
   não houver um número medido, o ΔU é hipótese bem fundamentada — não
   fato.
5. **O treinamento, hoje, tem ΔU negativo.** É a única linha da escada
   onde somos objetivamente piores que a alternativa. Reestruturar isso
   antes de vender é decisão de integridade, não de produto.

**A pergunta que decide o futuro da empresa** não é "a ABBA é útil?" —
é: **a ABBA consegue provar utilidade medida em um cliente antes que a
alternativa interna fique boa demais?** Essa é uma corrida real, e o
relógio está andando.

---

## 8. O que isso implica na estratégia (a parte acionável)

**(a) Escolher clientes por ΔU × N, não por facilidade de venda.**
Critérios onde o nosso delta é maior:
- Operação **de alto risco e alto volume** (saúde, logística, financeiro)
- Cliente **sem capacidade técnica interna forte** (sem um Alan)
- Problema que **atravessa departamentos** (interno não consegue por
  política)
- Onde **prova importa** (regulado, com contrato, com auditoria)

Onde o nosso delta é menor: empresa com bom time interno, problema
pequeno e técnico, cliente que só quer uma ferramenta.

**(b) Vender diagnóstico e prova, não capacidade de construção.**
O produto de maior ΔU da casa é o Assessment + o Mapa de Vazamento —
achar o problema certo e provar o resultado. A construção é consequência,
não a promessa.

**(c) Priorizar o Caso C da ABC.** Precisa dos números das 19 perguntas.
Sem eles não há venda, e com eles há uma venda de outra ordem de
grandeza.

**(d) Resolver o portal antes de vender treinamento.** ΔU negativo não
se vende — se conserta.

**(e) Decidir conscientemente o caminho da escala.** A provocação do
utility delta fala de dois caminhos. Hoje a ABBA está no de **alto impacto,
baixa escala** (5-6 clientes profundos), que é coerente com boutique.
Mas as **ferramentas** (assessment-brain, portal, Mapa de Vazamento
gratuito) são ativos de **alta escala** — o Mapa de Vazamento poderia
tocar centenas de empresas em vez de seis. São dois negócios diferentes
dentro da mesma casa, e vale escolher explicitamente qual está sendo
construído, em vez de deixar a resposta emergir do acaso.

**(f) O prazo que importa:** um resultado medido em cliente, publicável
com autorização. Enquanto não existir, tudo acima é análise. Depois que
existir, tudo acima vira ativo comercial.
