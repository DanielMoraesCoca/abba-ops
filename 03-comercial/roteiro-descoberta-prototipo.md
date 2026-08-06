# Roteiro de Descoberta Técnica — Protótipo de Caso de Uso

> **Camada:** comercial (processo). Para a reunião em que o cliente já decidiu que quer um **protótipo** (veio do assessment gratuito ou chegou com o problema pronto) e o sócio conduz **sem developer na sala**. O objetivo da reunião NÃO é desenhar a solução — é sair com informação suficiente para o time de engenharia desenhar o protótipo sem uma segunda reunião de descoberta.
>
> Cartão de mesa (A4, 2 págs): [`../08-materiais/modelos/cartao-descoberta-prototipo.pdf`](../08-materiais/modelos/cartao-descoberta-prototipo.pdf) · Alimenta: [estágio 07](../02-jornada-do-cliente/07-construcao-e-implantacao.md) · [relatório do protótipo](../08-materiais/modelos/relatorio-prototipo-modelo.docx) (os critérios de sucesso acordados aqui viram a seção 2 dele) · [deck do serviço 3](../08-materiais/modelos/servico-3-prototipo-deck.pdf)

## A postura (dizer no início, palavra por palavra)

> *"Hoje o meu papel é entender o problema de vocês a fundo — vou fazer bastante pergunta, algumas bem básicas. É de propósito: o nosso time de engenharia vai desenhar o protótipo em cima do que eu levar daqui, e quanto melhor eu entender, mais certeiro e mais rápido ele volta para vocês."*

Isso transforma "não ter o técnico na sala" de fraqueza em método. E uma regra de ouro: **pedir para MOSTRAREM, não só contarem** — 5 minutos vendo a tela real, a planilha real ou o documento real valem 30 minutos de descrição. Anotar todos os nomes próprios: do sistema, da tela, do campo, do relatório.

---

## Os 6 blocos, em ordem (~55 min)

### Bloco 1 — O problema e o processo (15 min)

1. *"Me contem o processo do início ao fim, como se eu fosse fazer esse trabalho amanhã: o que chega, quem pega, o que a pessoa faz, para onde vai o resultado?"*
2. *"Isso acontece quantas vezes por dia/semana? Quantos itens por mês?"* (volume)
3. *"Quanto tempo leva cada um? Quantas pessoas tocam nisso?"* (custo hoje)
4. *"O que acontece quando dá errado? Com que frequência dá errado? Quanto custa o erro?"*
5. *"E quando NÃO segue o padrão? Me deem dois exemplos reais de exceção."* — **as exceções são onde protótipos morrem; é a pergunta que o time mais agradece**
6. Se trouxerem vários problemas: *"se só um pudesse ser resolvido este mês, qual tira mais dinheiro/sono de vocês?"* — **protótipo é UM caso**. Os outros ficam registrados para a fila.

### Bloco 2 — O número do sucesso (10 min) — o bloco mais importante

7. *"Qual é o número de hoje?"* — tempo por item, erros por mês, custo, atraso. **Baseline.**
8. *"Esse número já é medido? Onde? Quem mede?"* (se não é medido, medir o estado atual é a primeira tarefa do protótipo)
9. *"Que número faria vocês dizerem 'aprovado, vamos investir'?"* — **a meta que define GO/NO-GO, combinada ANTES. É doutrina: sem esse número não há protótipo, há demonstração.**
10. *"Quem aqui dentro bate o martelo de que funcionou?"* (o dono da validação)

### Bloco 3 — Os sistemas (10 min)

11. *"Onde esse processo mora? Que sistemas, planilhas ou ferramentas vocês usam nele?"* — anotar **nome e versão**: ERP (qual?), CRM, sistema próprio, Excel, e-mail, WhatsApp, papel
12. *"Esses sistemas são na nuvem ou instalados aí no servidor de vocês?"*
13. *"Como a informação entra e sai de cada um? Alguém digita? Ele exporta relatório (Excel/PDF)? Tem integração automática com outro sistema?"* — se surgir a palavra **API** (a "tomada" que deixa um sistema conversar com outro), perguntar: *"vocês já usam? quem sabe mexer?"*
14. *"Quem administra esses sistemas — TI interna, o fornecedor do sistema, uma terceirizada?"* (é de quem virá o acesso)

### Bloco 4 — Os dados (10 min)

15. *"Que documentos e dados esse processo usa e produz?"* — e **pedir para ver um exemplar real na hora**
16. *"Nesse formato mesmo? PDF escaneado ou digital? Planilha padronizada ou cada um preenche de um jeito?"* (a resposta muda o protótipo inteiro)
17. *"Quantos por mês? Vocês guardam desde quando? Onde?"* (volume + histórico)
18. *"Tem dado pessoal aí — nome, CPF, salário, saúde?"* (LGPD: define anonimização e o desenho do acesso)
19. **O pedido que fecha o bloco:** *"para o protótipo usar a realidade de vocês, precisamos de uma amostra: uns 20 a 50 exemplos reais — anonimizados se precisar — e, para cada um, qual era a resposta certa. Tipo um gabarito. Quem consegue montar isso, e até quando?"*

### Bloco 5 — As pessoas (5 min)

20. *"Quem faz esse trabalho hoje?"* e *"quem conhece as exceções de cor?"* — **essa segunda pessoa precisa participar do protótipo**
21. *"No fluxo novo, quem seria a pessoa de confiança que revisa e aprova o que a IA fizer?"* (nosso modelo: a IA executa, gente da confiança de vocês valida — dito assim na reunião)
22. *"Quem é o nosso ponto focal técnico — a pessoa que nosso time chama quando precisar de acesso ou tirar dúvida?"* (nome + canal)

### Bloco 6 — Restrições e logística (5 min)

23. *"Os dados podem sair da empresa para um ambiente nosso de nuvem, ou precisam ficar aí dentro?"* (muda a arquitetura — e temos as duas vias)
24. *"Precisa de NDA antes da amostra? Quem autoriza acessos aí dentro?"*
25. *"Se o protótipo bater a meta, quem decide o passo seguinte — e em que fórum?"* (prepara o GO)
26. Expectativa de prazo deles — sem prometer data na hora: *"nosso time volta com o desenho do protótipo, o cronograma e os critérios por escrito."*

---

## Não saia da reunião sem (o checklist dos 10)

1. **UM** caso escolhido (os demais anotados para a fila)
2. O processo narrado passo a passo — teste: você conseguiria explicá-lo ao time em 5 minutos
3. O **baseline** em número, e onde ele é medido
4. A **meta que define GO**, dita por eles
5. Os sistemas com **nome próprio** (e nuvem × local)
6. O formato **real** dos dados — visto com os próprios olhos
7. Volume/mês e histórico disponível
8. A promessa da **amostra com gabarito** (quem monta, até quando, por onde chega)
9. Nome do **usuário-chave** (quem conhece as exceções) e do **ponto focal técnico**
10. A restrição de dados (pode sair? nuvem ok?) e quem autoriza acesso

## Sinais de alerta (não matam a reunião — mudam a conversa)

- **Caso sem dado acessível** → o protótipo começa pela captura do dado; dizer isso com honestidade
- **Sem número e sem como medir** → primeira semana do protótipo = medir o hoje; sem baseline não existe GO
- **"Queremos automatizar tudo"** → devolver: *"tudo começa por um. Qual?"*
- **Ninguém na sala conhece as exceções** → pedir a pessoa certa para uma chamada de 30 min antes do desenho
- **Dado não pode sair + não têm infraestrutura** → protótipo precisa de desenho especial; não prometer prazo na hora

## Depois da reunião (mesmo dia, 15 min)

Preencher e mandar ao time o **registro de descoberta** (estrutura = os 6 blocos + checklist acima; uma mensagem longa no canal do projeto resolve). O que faltou vira pergunta ao ponto focal — não segunda reunião. Os critérios do Bloco 2 entram como "Critérios de sucesso acordados" no [relatório do protótipo](../08-materiais/modelos/relatorio-prototipo-modelo.docx), seção 2.

## Ligações

[Deck do serviço 3 — Protótipo](../08-materiais/modelos/servico-3-prototipo-deck.pdf) · [Estágio 07](../02-jornada-do-cliente/07-construcao-e-implantacao.md) · [Coreografia da conversão](coreografia-da-conversao.md) · [Kit de presença](kit-de-presenca.md)
