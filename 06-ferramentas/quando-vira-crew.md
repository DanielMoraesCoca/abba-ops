# A régua do crew: o que vira agente e o que não vira

> **Camada:** ferramenta. Complementa a [ficha de Agentes](ferramenta-agentes.md), que diz *o que prometemos*; esta régua diz *o que construímos como agente*. Origem: decisão de 2026-09-05, provocada por material de marketing da própria CrewAI sugerindo que todo fluxo repetitivo é candidato a crew.
>
> **Por que existe:** a pergunta "isso vira crew?" volta toda semana, e responder de novo a cada vez produz respostas diferentes. Régua escrita é o que impede o sócio de hoje discordar do sócio de três meses atrás.

## A pergunta que decide

**A mesma entrada precisa dar a mesma saída?**

Se precisa, não é agente. Não importa quantas vezes por semana se repete, e é aí que o argumento de marketing engana: repetição é sinal de que vale *automatizar*, não de que vale *agentificar*. Fluxo repetitivo com resposta única é função. Agente entra onde a resposta legítima varia.

## A régua

| Sinal na tarefa | Veredito | Doutrina |
|---|---|---|
| A saída é número, quantidade, valor ou prazo | **Não é agente** | Conta se faz com código. Modelo erra em silêncio e o erro chega ao cliente somado a outros |
| A saída vira ordem de serviço, medição, pagamento ou documento com efeito legal | **Não é agente** | Erro caro e difícil de reverter exige determinismo e rastro |
| A regra cabe escrita, e o cliente pode querer discordar de uma regra específica | **Não é agente** | Regra em código é auditável e negociável item a item; prompt não é |
| Ler prosa e devolver estrutura | **Agente, com esquema e trava de fonte** | Leitura é o que o modelo faz bem. A trava (trecho citado tem que existir no documento) é o que impede invenção virar dado |
| Redigir para uma pessoa ler | **Agente** | Redação com regra é trabalho de modelo |
| Conciliar posições de especialidades diferentes sobre o mesmo objeto | **Tripulação** | Único caso em que multiagente ganha de um agente só: cada papel defende um interesse real e distinto |
| Ambiguidade que a regra determinística não resolveu | **Agente, e ele só propõe** | Quem decide continua sendo o contrato, a norma ou a pessoa |

**Regra de ouro do desenho:** o agente lê, a regra decide, a pessoa aprova. Quem transforma a decisão em agente compra alucinação onde precisava de conta. Quem transforma a negociação em regra compra rigidez onde precisava de julgamento.

## Onde cada peça da ABBA cai

| Peça | Veredito | Por quê |
|---|---|---|
| `assessment-brain` (o Conselheiro) | **Fica onde está. Não migra.** | É sistema de registro da verdade sobre cliente. As garantias construídas ali — supersessão bitemporal, ciclo de decisão só para frente, portão de humano nomeado, autoridade de origem, teto de gasto, calibração — não são replicáveis por um runner hospedado. Migrar seria trocar garantia por painel |
| `abba-portal` | Não é crew | Aplicação web |
| `abba-ops` | Não é crew | Documentação; a régua do revisor já cobre o que é automatizável aqui |
| `abba-canteiro` (as demos) | **Já é, e está certo** | A parte de agente delas é genuinamente de agente: a mesa de compatibilização, a RFI, o parecer. O motor de regras e a medição não passam por modelo |

## O que isso significa para o CrewAI AMP

O AMP é **destino de publicação**, não arquitetura. A distinção é prática, não filosófica: nas demos do canteiro a lógica de domínio é Python puro, e por isso trocar de plataforma custa reescrever o `main.py` de cada projeto, não o produto. Se a lógica estivesse dentro dos agentes, sair custaria refazer tudo.

Mantida essa fronteira, a parceria com a CrewAI é vantagem sem virar dependência: ganhamos o painel, a interface para o cliente e a relação comercial, sem entregar a operação. **Vitrine e painel de controle no AMP; memória e verdade da empresa, não.**

Isso também muda a conta que está aberta na [ficha de Agentes](ferramenta-agentes.md): a escolha entre plano Enterprise e self-host deve ser dimensionada pelo que de fato roda lá — as camadas de julgamento —, não pela operação inteira.

## O custo de errar para cada lado

Errar para o lado do agente é o erro caro: alucinação onde se precisava de aritmética, custo de token multiplicado por toda a operação, e resultado que não se audita. Errar para o lado da regra é o erro barato: rigidez, e trabalho manual que sobra até alguém escrever a regra melhor.

**Na dúvida, comece determinístico.** Promover uma função a agente é fácil; rebaixar um agente a função depois que o cliente já viu é conversa difícil.

## Dono e lacunas

**Stack:** chapéu [Tecnologia](../01-setores/tecnologia.md). Aplicar antes de prometer qualquer automação a cliente e antes de abrir projeto novo no AMP. Lacuna ativa: a decisão de plano da CrewAI (R9 na [ficha de Agentes](ferramenta-agentes.md)) continua aberta e agora tem critério para ser dimensionada.
