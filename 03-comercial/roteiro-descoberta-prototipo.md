# Roteiro de Descoberta Técnica. Protótipo de Caso de Uso

> **Camada:** comercial (processo). **instrumento oficial de entrevista** para qualquer pessoa da ABBA conduzir a descoberta de protótipo em qualquer empresa, de qualquer setor, **sem developer na sala** (V3s, 2026-08-06). O objetivo da reunião NÃO é desenhar a solução, é sair com informação suficiente para o time de engenharia desenhar o protótipo **sem uma segunda reunião de descoberta**.
>
> Cartão de mesa (A4, 2 págs): [`../08-materiais/modelos/cartao-descoberta-prototipo.pdf`](../08-materiais/modelos/cartao-descoberta-prototipo.pdf) · Alimenta: [estágio 07](../02-jornada-do-cliente/07-construcao-e-implantacao.md) · [relatório do protótipo](../08-materiais/modelos/relatorio-prototipo-modelo.docx) (os critérios do Bloco 2 viram a seção 2 dele) · [ficha da ferramenta de agentes](../06-ferramentas/ferramenta-agentes.md) · deck do serviço 3 retirado na V5: a descoberta de protótipo vive dentro das fases 1–2 do Programa ([tabela v3](tabela-de-precos.md))

## Por que estas perguntas: o mapa pergunta → engenharia

Cada bloco existe porque alimenta uma decisão concreta de quem constrói. A stack de criação é **CrewAI + roteamento de LLMs** ([ficha](../06-ferramentas/ferramenta-agentes.md)): a solução é um conjunto de **agentes com papel, objetivo e contexto**, executando **tarefas encadeadas**, usando **ferramentas** (integrações, leitura de documentos), consultando uma **base de conhecimento**, com **pontos de aprovação humana** e **limites de custo por agente**. A entrevista coleta exatamente os insumos desse desenho:

| O que a pergunta coleta | O que o time faz com isso |
|---|---|
| O processo passo a passo + gatilho + ritmo | O desenho do fluxo: quais passos viram tarefas de agente, o que dispara a execução, se roda em tempo real ou em lote (arquitetura e custo por execução) |
| As exceções reais | Os casos de teste do protótipo · protótipo que só vê o caminho feliz é demonstração |
| "O que o estagiário brilhante erraria" | O papel, o objetivo e o contexto de cada agente · e o conhecimento tácito que precisa virar instrução explícita |
| "Onde está escrito como fazer certo" | A base de conhecimento que os agentes consultam (manuais, políticas, tabelas, históricos) · o que não está escrito precisa ser extraído do especialista antes do desenho |
| Regra × julgamento, passo a passo | O que se automatiza com lógica determinística, onde entra o modelo, e onde entra gente |
| O custo do erro, por tipo | Onde ficam os **pontos de aprovação humana** e o nível de autonomia de cada agente (erro inaceitável = aprovação obrigatória antes de sair) |
| Baseline + meta + gabarito | O conjunto de avaliação: como o protótipo será MEDIDO (a régua do GO/NO-GO, combinada antes) |
| Sistemas + formatos + destino da saída | As ferramentas/integrações dos agentes · e o de-risk do protótipo: exportação manual serve para a prova; integração de verdade é fase de construção |
| Sensibilidade dos dados + IA em nuvem permitida | A escolha de modelos e do ambiente (nuvem gerenciada × on-premise · temos as duas vias) e a anonimização da amostra |
| Horas do especialista | O gargalo real de todo protótipo: sem o dono do conhecimento disponível, o cronograma é ficção |

## A postura (dizer no início, palavra por palavra)

> *"Hoje o meu papel é entender o problema de vocês a fundo: vou fazer bastante pergunta, algumas bem básicas. É de propósito: o nosso time de engenharia vai desenhar o protótipo em cima do que eu levar daqui, e quanto melhor eu entender, mais certeiro e mais rápido ele volta para vocês."*

Regras de ouro: **pedir para MOSTRAREM, não só contarem** (5 min vendo a tela real valem 30 min de descrição) · anotar **todo nome próprio** (sistema, tela, campo, relatório) · **não prometer prazo nem arquitetura na hora**. *"nosso time volta com o desenho, cronograma e critérios por escrito"*.

---

## Os 7 blocos, em ordem (~60 min)

### Bloco 1. O problema e o processo (12 min)

1. *"Me contem o processo do início ao fim, como se eu fosse fazer esse trabalho amanhã: o que chega, quem pega, o que a pessoa faz, para onde vai o resultado?"*
2. *"O que DISPARA esse processo: chega um e-mail, cai um arquivo, alguém pede, é uma data do mês?"* → **a entrada do fluxo**
3. *"Precisa de resposta na hora (minutos), ou pode processar em lote: de noite, por exemplo?"* → **ritmo: arquitetura e custo**
4. *"Quantas vezes por dia/semana? Quantos itens por mês? Quanto tempo cada um? Quantas pessoas tocam?"*
5. *"E quando NÃO segue o padrão? Me deem dois exemplos reais de exceção."* → **os casos de teste; onde protótipos morrem**
6. Se trouxerem vários problemas: *"se só um pudesse ser resolvido este mês, qual tira mais dinheiro/sono de vocês?"*. **protótipo é UM caso**; os demais ficam na fila

### Bloco 2. O número do sucesso e o custo do erro (10 min): o bloco mais importante

7. *"Qual é o número de hoje?"*: tempo por item, erros/mês, custo, atraso. **Baseline.** *"Já é medido? Onde? Quem mede?"* (se não é: medir o hoje é a 1ª tarefa do protótipo)
8. *"Que número faria vocês dizerem 'aprovado, vamos investir'?"* → **a meta que define GO/NO-GO, combinada ANTES. Doutrina: sem esse número não há protótipo, há demonstração**
9. *"Que tipo de erro seria INACEITÁVEL: daqueles que não podem sair de jeito nenhum? E que erro é tolerável, se alguém pegar na revisão?"* → **define onde vão os pontos de aprovação humana e a autonomia da solução**
10. *"Quem aqui dentro bate o martelo de que funcionou?"*

### Bloco 3. A inteligência do trabalho (10 min): o bloco que desenha os agentes

11. **A pergunta do estagiário brilhante:** *"Se eu colocasse aqui amanhã um estagiário brilhante, mas sem nenhuma experiência da casa: o que vocês diriam para ele fazer, em que ordem? **E o que ele erraria no primeiro mês, e por quê?**"* → o que ele acertaria de cara = automatizável direto; o que ele erraria = o conhecimento tácito que precisa virar instrução, exemplo ou revisão humana
12. *"Onde está ESCRITO como fazer certo: manual, política, tabela de preços, catálogo, contratos, histórico de casos? E o que só existe na cabeça de alguém?"* → **a base de conhecimento consultável**; o que está só na cabeça precisa de sessão com o especialista antes do desenho
13. *"Desses passos todos, quais são 'seguir regra' e quais têm decisão de verdade: onde alguém pondera, compara, negocia?"* → regra → lógica; julgamento → modelo + revisão
14. *"Como vocês reconhecem um resultado BEM feito, e um que parece certo mas está errado?"* → os critérios de revisão (e o teste mais duro do protótipo)

### Bloco 4. Os sistemas e o destino (8 min)

15. *"Onde esse processo mora? Que sistemas, planilhas ou ferramentas?"*. **nome e versão**: ERP (qual?), CRM, sistema próprio, Excel, e-mail, WhatsApp, papel. *"Na nuvem ou no servidor de vocês?"*
16. *"Como a informação entra e sai de cada um? Alguém digita? Exporta relatório (Excel/PDF)? Tem integração automática?"*: se surgir **API** (a "tomada" que liga sistemas): *"já usam? quem sabe mexer?"*
17. *"E o resultado final: precisa chegar ONDE, em que formato, para quem?"* → **o destino da saída**: lançamento no sistema, e-mail pronto, planilha, mensagem: quem consome define a última tarefa do fluxo
18. **O de-risk do protótipo:** *"para a fase de prova, podemos trabalhar com exportações manuais: alguém extrai os dados e nos manda? A integração de verdade vem depois, na construção."* (tira a TI do caminho crítico da prova)
19. *"Quem administra esses sistemas. TI interna, fornecedor, terceirizada?"* (é de quem virá o acesso na construção)

### Bloco 5. Os dados e a amostra (10 min)

20. *"Que documentos e dados o processo usa e produz?"*. **pedir para ver um exemplar real na hora**
21. *"Nesse formato mesmo? PDF **escaneado ou digital**? Foto? Áudio? Planilha padronizada ou cada um preenche de um jeito?"* → escaneado/foto = leitura visual; a resposta muda o protótipo inteiro
22. *"Quantos por mês? Guardado desde quando? Onde?"* (volume + histórico)
23. *"Tem dado pessoal: nome, CPF, salário, saúde?"* → LGPD: anonimização da amostra + inventário Art. 20 na construção
24. *"A empresa permite usar IA em nuvem: os grandes provedores: sobre esses dados, ou precisa ficar tudo dentro de casa?"* → **escolha de modelos e ambiente; temos as duas vias**
25. **O pedido que fecha o bloco:** *"para o protótipo usar a realidade de vocês, precisamos de uma amostra: uns 20 a 50 exemplos reais: anonimizados se precisar: e, para cada um, qual era a resposta certa. Um gabarito. Quem monta, e até quando?"* → **é a régua com que o protótipo será medido**

### Bloco 6. As pessoas (5 min)

26. *"Quem faz esse trabalho hoje? E quem conhece as exceções de cor?"* → **essa segunda pessoa participa do protótipo**
27. *"Quantas horas por semana essa pessoa consegue nos dar durante o protótipo?"* → **o gargalo real de cronograma: perguntar SEMPRE**
28. *"No fluxo novo, quem revisa e aprova o que a IA fizer?"* (nosso modelo, dito na mesa: **a IA executa, gente da confiança de vocês valida**)
29. *"Quem é o nosso ponto focal técnico: a pessoa que nosso time chama para acesso e dúvida?"* (nome + canal)

### Bloco 7. Restrições e logística (5 min)

30. *"Os dados podem sair da empresa para um ambiente nosso de nuvem, ou precisam ficar aí dentro?"* (confirma o 24: muda a arquitetura)
31. *"Precisa de NDA antes da amostra? Quem autoriza acessos aí dentro?"*
32. *"Se o protótipo bater a meta, quem decide o passo seguinte, e em que fórum?"* (prepara o GO)
33. Expectativa de prazo deles, sem prometer data: *"nosso time volta com o desenho do protótipo, o cronograma e os critérios por escrito."*

---

## Não saia da reunião sem (o checklist dos 12)

1. **UM** caso escolhido (os demais anotados para a fila)
2. O processo narrado passo a passo + **o gatilho** que o dispara + o **ritmo** (na hora × lote)
3. O **baseline** em número, e onde ele é medido
4. A **meta que define GO**, dita por eles
5. O **erro inaceitável** nomeado (e o tolerável)
6. **O que o estagiário brilhante erraria**: o conhecimento tácito mapeado
7. **Onde está escrito** como fazer certo (e o que só existe na cabeça de alguém)
8. Os sistemas com **nome próprio** (nuvem × local)
9. O formato **real** dos dados visto com os olhos + **o destino da saída**
10. A promessa da **amostra com gabarito** (quem monta, até quando) + **as horas/semana do especialista**
11. **Usuário-chave** + **aprovador** do fluxo novo + **ponto focal técnico**
12. Dados podem sair? **IA em nuvem permitida?** Quem autoriza acesso?

## Sinais de alerta (não matam a reunião: mudam a conversa)

- **Caso sem dado acessível** → o protótipo começa pela captura do dado; dizer com honestidade
- **Sem número e sem como medir** → 1ª semana do protótipo = medir o hoje; sem baseline não existe GO
- **"Queremos automatizar tudo"** → devolver: *"tudo começa por um. Qual?"*
- **Ninguém na sala conhece as exceções** → chamada de 30 min com a pessoa certa antes do desenho
- **O conhecimento está todo na cabeça de uma pessoa** → o protótipo inclui sessões de extração com ela; sem isso, o agente aprende errado
- **Especialista "sem tempo"** → cronograma é ficção; renegociar antes de começar
- **Dado não pode sair + não têm infraestrutura** → desenho especial (via on-premise); não prometer prazo na hora
- **Erro inaceitável em tudo** → o fluxo nasce com aprovação humana em tudo: dizer que é assim que começa, e a autonomia cresce com a confiança medida

## Depois da reunião (mesmo dia, 15 min)

Preencher e mandar ao time o **[registro de descoberta](registro-de-descoberta-modelo.md)** (modelo pronto; a instância com nome do cliente vai para o Drive, **nunca para o git**). O que faltou vira pergunta ao ponto focal. **não segunda reunião**. Os critérios do Bloco 2 entram como "Critérios de sucesso acordados" no [relatório do protótipo](../08-materiais/modelos/relatorio-prototipo-modelo.docx), seção 2. Se surgiu reação a preço, registrar na [planilha de precificação](precificacao-planilha.md) §6.

## Ligações

[Ficha da ferramenta de agentes](../06-ferramentas/ferramenta-agentes.md) · [Tabela v3](tabela-de-precos.md) (deck do serviço 3 retirado na V5: a descoberta de protótipo vive dentro das fases 1–2 do Programa) · [Estágio 07](../02-jornada-do-cliente/07-construcao-e-implantacao.md) · [Coreografia da conversão](coreografia-da-conversao.md) · [Kit de presença](kit-de-presenca.md)
