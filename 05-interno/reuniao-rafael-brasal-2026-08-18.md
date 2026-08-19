# Reunião Rafael (Brasal) — 18/08/2026, 17h07

> Extração da transcrição (3.570 linhas; Daniel + Rafael, Pedro ausente — viagem a São Francisco). Rafael é aliado dando opinião franca, não uma conversa de venda formal. Cada insight abaixo tem o minuto da fala. O que virou produto está marcado; o que é ação comercial está na lista do fim.

## Os 7 insights (com minuto)

### 1. Fundação = dados E processos [17:16–17:19]
Data lakes da Brasal ainda em desenvolvimento, dados não validados. Exemplo concreto: **financeiro e comercial mantêm DOIS Excel lendo os mesmos dados de venda de formas diferentes** — "desse jeito a gente não vai conseguir construir solução nenhuma". "Não é só chegar e aplicar IA num processo mal feito — a gente vai ter um resultado ruim." Os projetos que trazem ROI são os preditivos, e preditivo exige grandes fontes de dados organizadas. Todo projeto começa com "um passo atrás": ajustar fundação — **fontes de dados E processos internos da área**.
→ **Virou produto:** veredito de fundação agora fala "dados e processos" (relatório + anexo visual). O exemplo dos dois Excel é padrão que a dimensão de topologia de fluxo de informação deve capturar — item de verificação na rodada real.

### 2. O gate real é a DISPOSIÇÃO DA ÁREA, não a empresa [17:20–17:21, 17:43–17:45]
Mudar processo em empresa tradicional "parece impossível" (burocracia + "IA é hype" de quem sempre fez de um jeito). **"O humano no loop ou está disposto a ajudar e mudar, ou pode ser um detrator de qualquer solução de IA."** Em vários projetos Rafael concluiu: "a empresa não vai mudar — você acaba tendo que ir atrás de áreas que estejam dispostas": aval do diretor + equipe alinhada ANTES de entrar. A estratégia que funcionou na Brasal foi adoção **puxada**: líderes usando → equipe viu diferença real → hoje ~10 pedidos/dia de licença Claude ("parece padaria").
→ **Virou produto:** roadmap do anexo declara "começamos pela área mais disposta a mudar, não pela mais quebrada" + cards com prontidão/sensibilidade; próximo passo do anexo inclui "escolher a primeira área disposta".

### 3. Caso Spring Globo — a prova da tese, citável anonimizado [17:22–17:25]
App de força de vendas usado pelas engarrafadoras Coca-Cola: **1,5 ano** tentando implementar, **R$200 mil POR atualização**, todas as engarrafadoras do Brasil abandonando. Sala de guerra interna (5 devs + 1 analista de negócio que conhecia os processos REAIS, inclusive os não-padronizados) reconstruiu o aplicativo **com IA em ~3 semanas**, validando ~70 páginas de regras de negócio, zero bug crítico, no ar.
→ **Uso:** narrativa de venda (anonimizada: "uma engarrafadora de bebidas do DF..."): solução adaptada ao processo real vence solução de prateleira; IA multiplica um time pequeno que ENTENDE o negócio. É exatamente o pitch da ABBA.

### 4. O serviço é o processo de imersão [17:41–17:43]
"O serviço tem que ser além de simplesmente implementar IA." O que o cliente compra é a segurança de **"já pegamos empresas com processos bagunçados e dados mal estruturados e saímos com case de sucesso"** — as lições aprendidas são o diferencial competitivo. Rafael estima **>90% dos projetos de IA falhando** por correria de hype sem olhar o background (bate com RAND 80% / MIT 95% — [pesquisa](pesquisa-assessment-mercado.md)).

### 5. Objeção nova mapeada: "já sei meus 10 problemas" [17:14–17:15]
Empresas chegam com gargalos na mão e querem pular o assessment. Resposta em 3 tempos registrada na [coreografia (objeção 11)](../03-comercial/coreografia-da-conversao.md): validamos os 10 com número e premissa + achamos o que a liderança não vê (temos a métrica `invisível para a diretoria`) + testamos se a fundação aguenta antes de gastar. Rafael validou o assessment como "exatamente a solução desse problema... a clareza do problema" [17:46].

### 6. Sophy Works em primeira mão [17:47–17:53]
Fundador brasileiro ex-Serpro, exits anteriores, "um geniozinho". **SaaS US$49/mês** + opções on-premise/VPS (único ou compartilhado). Site e produto **em inglês com preço em dólar** — estratégia deliberada. Foco real: **gestão de produto** (discovery, planejamento, mapeamento de processos, arquitetura de projeto), com memória persistente de contexto e **rastreabilidade de decisão** ("você propôs X, mas baseado no contexto de 2 anos atrás, vai impactar"). No fim, o output vai para Claude Code/CrewAI construir. Brasal tem licença; Rafael acha que "vai ganhar muito mercado".
→ **Leitura ABBA:** não é concorrente do assessment profundo (eles não entram com dados reais da empresa; nós sim) — é régua de legibilidade e uma peça de fluxo parecida com o nosso `export --target crewai`, que já existe e deve aparecer na venda. Detalhes incorporados na [pesquisa](pesquisa-assessment-mercado.md) §3.

### 7. Oportunidade comercial QUENTE: treinamento/portal [17:32–17:36, 17:55–17:57]
- Brasal já fez letramento com a Starts: ~70–80 pessoas (C-level + gerência), **~R$200 mil** — e a proposta nova veio igualmente cara.
- Proposta concorrente na mesa: Keiros (SP), **~R$30 mil**, 2 encontros presenciais + plataforma.
- Rafael QUER uma **"trilha de Claude"**: a pessoa só ganha a licença corporativa se completar a trilha — encaixa exatamente no portal ABBA (desafios, quizzes, detecção de quem avança) + parceria CrewAI (ferramenta grátis para os que se destacam).
- **Rafael pediu reunião NA PRÓXIMA SEMANA** (semana de 24/08) para ver o portal e o treinamento. Ele vai conversar com o Carlos. Direcional do Daniel citado por ele: "focar em economia de custo".

## Ações (donas: sócios)

| # | Ação | Quem | Quando |
|---|---|---|---|
| 1 | Marcar a reunião do portal/treinamento com o Rafael | Daniel | Semana de 24/08 (ele pediu para agilizar) |
| 2 | Montar proposta de treinamento Brasal com âncoras de preço (mercado: R$30k Keiros ↔ R$200k Starts) + desenho da "trilha de Claude" com gate de licença | Daniel + Pedro | Antes da reunião |
| 3 | Liberar o e-mail do Rafael no assessment web (gate de acesso é do Pedro) e enviar o resultado do assessment da Brasal que rodou ao vivo | Pedro | Esta semana |
| 4 | Pedir demo/testar a Sophy Works (Brasal tem licença; Rafael sugeriu pedir demo) | Daniel | Oportuno |
| 5 | Na rodada real do Cliente Zero: conferir se a análise captura o padrão "dois Excel com os mesmos dados" (topologia de fluxo) | Claude + sócios | Etapa 1 |
