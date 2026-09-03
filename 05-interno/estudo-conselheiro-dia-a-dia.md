# O Conselheiro no dia a dia: onde ele senta, por onde falam com ele, e o parecer que falta

> **Camada:** interno (pesquisa + plano de produto). Origem: pedido do sócio (2026-08-04). *"pesquise como é o dia a dia de uma empresa e valide em quais situações ele deve estar... até os mais simples, como 'queremos desativar esse sistema multi-agêntico para não gastar, pois vamos mudar a estrutura dessa parte da empresa': ele precisa estar, entender e falar se vale a pena. E por onde iriam contatá-lo?"*
>
> Complementa o [estudo do Conselheiro presente](estudo-conselheiro-presente.md) (que respondeu *como* ele se senta, com as travas legais). Este responde **quando**, **em quê**, **por onde**, e cria o entregável que faltava.
>
> Dono: chapéu Entrega (protocolo) + Comercial (o que se vende). Nada aqui está construído; é desenho com gatilhos.

---

## 1. O achado que reorganiza o produto

A pesquisa sobre desperdício de software encontrou a frase que define o valor do Conselheiro melhor do que qualquer coisa que já escrevemos:

> **As empresas recuperam apenas 5 a 15% do desperdício que elas mesmas já identificaram, porque a licença é sinalizada numa auditoria, o relatório é arquivado, e nada acontece: ninguém é dono do acompanhamento.** ([License Logic](https://licenselogic.co/blog/software-spend-optimization))

O gargalo do mercado **não é descobrir**. É **ser dono do seguimento**. Isso muda a frase do produto:

> O Conselheiro não é quem descobre o problema. É **quem não deixa a decisão morrer**: a que foi tomada, a que venceu o prazo, e a que ninguém percebeu que precisava ser revista.

E o contexto de desperdício é grande no nosso alvo: **25–40% de licenças compradas e não usadas em empresas de médio porte** (Gartner, 2024), **53% dos aplicativos SaaS subutilizados ou parados**, **~30% do orçamento de software desperdiçado** ([SMC](https://www.smcconsulting.be/news/saas-spend-optimization-2026) · [License Logic](https://licenselogic.co/blog/saas-spend-optimization)), e até **75% do orçamento de software indo para manutenção contínua** do que já existe ([Application retirement](https://en.wikipedia.org/wiki/Application_retirement)).

---

## 2. O relógio de uma empresa média brasileira

A intuição do sócio. *"ele deve estar onde tem números"*: está certa, e tem endereço exato: **o fechamento mensal é o pulso da empresa.** Mas há quatro relógios, não um, e o Conselheiro precisa estar acoplado aos quatro.

### Relógio 1. O pulso mensal (onde os números nascem)

| Momento | Quando | O que acontece | Onde o Conselheiro entra |
|---|---|---|---|
| Fechamento contábil/gerencial | ~D+5 a D+10 do mês seguinte | DRE, margem, desvio vs. orçamento | **Depois do fechamento, antes da reunião de resultados** |
| Reunião mensal de resultados | logo após o fechamento | A diretoria olha o que aconteceu | **Chega com o confronto decisão × resultado**, não com opinião |

**A regra de ouro do encaixe:** o Conselheiro nunca compete com o controller. Ele não traz *o número*: o cliente já tem. Ele traz **o número ao lado da decisão que prometeu movê-lo**. Ninguém mais na sala tem esse par.

### Relógio 2. O calendário fiscal (que decide quando NÃO mexer)

O mês fiscal brasileiro tem **sequência obrigatória**: eSocial (dia 7) → EFD-Reinf (dia 15) → DCTFWeb (último dia útil do mês seguinte); sem respeitar a ordem, a declaração seguinte não transmite. Somam-se INSS e DIRBI (dia 20) e EFD-Contribuições (10º dia útil do 2º mês). No ano: ECD e IRPF dos sócios em **maio**. *o mês mais pesado do calendário*, e ECF em julho. Em 2026, IBS e CBS já aparecem destacados nas notas em caráter informativo. ([Contábeis](https://www.contabeis.com.br/noticias/77969/calendario-fiscal-2026-organize-as-obrigacoes-do-semestre/) · [Dattos](https://www.dattos.com.br/en/blog/obrigacoes-fiscais-2026) · [Pactum](https://www.pactum.com.br/conteudos/calendario-tributario-2026))

**Isso não é trabalho nosso: somos consultoria de IA, não escritório contábil.** Mas é o relógio que diz **quando a empresa tem cabeça**. Propor go-live de sistema fiscal na primeira semana de maio é queimar o projeto. É a dimensão D17 do nosso próprio framework (*Sazonalidade e Ritmo*) virando operação: *"IA implantada bem antes do pico sem tempo de estabilização é desastre; IA que aguenta o pico é heroína."*

### Relógio 3. O ciclo orçamentário (a janela de maior valor do ano)

Entre setembro e novembro decide-se **o que vive e o que morre** no ano seguinte. É a única janela em que a diretoria olha, de uma vez, todo o custo recorrente. **É onde o Conselheiro deve chegar com o inventário de custo × valor de tudo o que roda**, e é o momento em que o retainer se paga sozinho.

### Relógio 4. As datas que ninguém lembra (o relógio oculto)

Renovações automáticas de contrato e licença. A pesquisa é direta: *"se a área de compras só revisa o contrato poucos dias antes da renovação, não há tempo de checar uso, comparar alternativas ou reduzir quantidade"* ([Spendflo](https://www.spendflo.com/blog/software-renewal-management) · [Zylo](https://zylo.com/blog/guide-saas-renewal)).

**Este relógio é literalmente o mecanismo que já construímos**: gatilho por decisão com data de revisão (`review_due_at`), fila da manhã, e a baixa manual do gatilho (`--checked`). O que falta não é código, é **carregar as datas do cliente na ativação**.

---

## 3. O mapa de presença: as 24 situações

### A. Ritmo previsível (agendável)

| # | Situação | Cadência | Papel dele |
|---|---|---|---|
| 1 | Fechamento → reunião de resultados | mensal | Confronto decisão × resultado medido |
| 2 | Ritual semanal de 20 min | semanal | O que venceu · gatilho · decidimos · vamos medir |
| 3 | Conselho / diretoria | trimestral | Máx. 3 recomendações, com probabilidade declarada |
| 4 | Ciclo orçamentário | anual (set–nov) | Inventário custo × valor de tudo que roda |
| 5 | Fechamento de ano / metas | anual | Reconciliação do prometido × entregue |
| 6 | Janela de renovação de contratos e licenças | por data | Aviso com antecedência + parecer |
| 7 | Pico sazonal do negócio | por setor | Congelamento de mudanças; nada entra em produção |
| 8 | Maio fiscal (ECD/IRPF/DCTFWeb) | anual | Não propor nada que exija a área fiscal |
| 9 | Reajustes (dissídio, IPCA, indexados) | anual | Impacto no caso de negócio dos sistemas |
| 10 | Auditoria / due diligence / exigência de cliente grande | por evento previsto | Dossiê do guardião + prontidão ISO 42001 |

### B. Eventos que disparam (precisam de porta de entrada)

| # | Situação | Quem costuma trazer | Papel dele |
|---|---|---|---|
| 11 | **"Vamos desligar isso para economizar"** | CFO, TI, dono da área | **Parecer de Permanência** (§4) |
| 12 | Chegou proposta de fornecedor de IA | qualquer diretor | Arbitragem (já é produto) |
| 13 | Fornecedor subiu o preço na renovação | Compras | Parecer + alternativa comparada |
| 14 | "Compramos 50 licenças e usamos 12" | TI/Financeiro | Redução de escopo com número |
| 15 | Vamos trocar/atualizar o ERP | TI | Mapa de integrações que quebram |
| 16 | Um agente/automação começou a errar ou custar mais | operação | Circuit breaker + revisão de decisão |
| 17 | **Vamos reestruturar a área** | diretoria | Os sistemas servem o processo velho ou o novo? |
| 18 | A pessoa que mantinha o automatismo saiu | RH/TI | Risco de conhecimento (D15) + plano |
| 19 | Saiu regra nova (ANPD, CBS/IBS, setorial) | jurídico | O que muda no que já roda |
| 20 | Cliente grande exigiu cláusula de IA/segurança | comercial | Dossiê + o que precisa existir |
| 21 | Incidente com IA em produção | TI | Protocolo de incidente + registro |
| 22 | "Queremos liberar IA para a empresa toda" | CEO | Caso de negócio + governança + IA-sombra |
| 23 | Concorrente anunciou algo | CEO | Leitura fria: é real, é para vocês? |
| 24 | Um indicador cruzou o limiar combinado | **o próprio sistema** | O gatilho dispara e ele chama · canal invertido |

### C. Onde ele NÃO entra (a lista que dá credibilidade)

Reunião sobre pessoas (desempenho, demissão, saúde) · comitê de ética ou investigação · negociação sindical · reunião com advogado sob sigilo · conversas 1:1. **Escrito no contrato, dito na primeira reunião.**

---

## 4. O entregável que falta: o **Parecer de Permanência**

Hoje o produto tem a **Arbitragem de Fornecedores**: que responde *"devemos comprar?"*. Falta o espelho, que é a pergunta do sócio: **"devemos manter, reduzir, pausar ou desligar?"**

É um vazio real de mercado: existe disciplina formal para aposentar sistemas (*application retirement / decommissioning*, incluindo a obrigação de **preservar o dado histórico** ao desligar), e o quadro de FinOps 2026 trata explicitamente de saída de escopo com métricas de sucesso pré-definidas e realocação de compromissos ([FinOps 2026](https://www.finops.org/insights/2026-finops-framework/) · [Virtasant](https://www.virtasant.com/blog/finops-framework-2026)). Mas **ninguém empacota isso para o médio porte brasileiro**, e ninguém tem o que nós temos: o baseline do que o sistema produziu.

### A assimetria que ninguém explora

> **Toda empresa mede o ROI de ligar um sistema. Nenhuma mede o resultado de desligá-lo.**

A decisão de desligar é uma decisão como qualquer outra: tem hipótese ("vamos economizar R$ X sem perder Y"), tem prazo e tem resultado verificável. Tratá-la com o mesmo rigor da decisão de ligar é a coisa mais ABBA que existe, e o Conselheiro é o único capaz, porque só ele tem o registro do que aquilo produziu.

### O que o parecer responde (as 7 perguntas)

1. **Quanto custa de verdade?** Custo unitário (por documento, transação, usuário), não o total. E o total honesto: no mundo de agentes, *a fatura de tokens é apenas um dos nove baldes de custo* ([FinOps X 2026](https://www.mavvrik.ai/blog/finops-x-2026-ai-token-economics/)): somam-se infraestrutura, integração, suporte, licença, o tempo das pessoas que operam e o custo de errar.
2. **Quanto rende?** O valor medido no diário: baseline combinado antes, resultado medido depois. Se nunca foi medido, o parecer diz isso **em vez de estimar**.
3. **Quem depende disso?** O que quebra a jusante: relatório, integração, obrigação, cliente.
4. **O motivo declarado sobrevive ao exame?** Se a área vai ser reestruturada: o sistema serve o processo **velho** (então desligar é consequência, não causa) ou o **novo** (então desligar é erro caro)?
5. **Quais são as saídas?** Sempre quatro, nunca duas: **manter · reduzir escopo · pausar com data de revisão · desligar com plano de retirada.** A resposta "reduzir para 12 licenças" costuma valer mais que "desligar".
6. **O que se preserva ao desligar?** Dado histórico, obrigação de retenção, trilha de auditoria: a regra do *application retirement*. Desligar sem preservar é criar passivo.
7. **Como saberemos que acertamos?** A decisão nasce com hipótese, prazo e métrica, e com **gatilho de revisão em 90 dias**. Se a economia não veio, ou a perda veio, está no registro.

### O formato

Uma página, entregue em até 5 dias úteis (mesmo SLA da arbitragem): situação · custo real com os baldes abertos · valor medido (ou o registro honesto de que nunca foi medido) · dependências · as 4 saídas com consequência de cada uma · **recomendação com probabilidade declarada** · plano de retirada se for o caso · a métrica e a data da revisão.

**Onde entra comercialmente:** entregável do Conselheiro (nas duas portas) e artefato-estrela do ciclo orçamentário. **Não é produto avulso**, é a razão de o retainer existir.

---

## 5. A caixa de entrada do Conselheiro: por onde falam com ele

Seis canais, cada um com regra e prazo. O princípio: **nenhuma ferramenta nova para o cliente aprender.**

| # | Canal | Para quê | Regra | Prazo |
|---|---|---|---|---|
| 1 | **E-mail dedicado** (`conselheiro@` do cliente ou nosso) | A porta principal do formal: encaminhar a proposta do fornecedor, pedir parecer, mandar documento | Encaminhar já cria o registro · atrito zero, e é o canal oficial da nossa própria política | Aviso de recebimento em 1 dia útil |
| 2 | **WhatsApp** | A pergunta rápida do diretor e o alerta do gatilho | **Nunca conteúdo sensível, valores ou decisão contratual** · leva a pergunta e o link ([política vigente](comunicacao.md)) | Resposta ou encaminhamento em 1 dia útil |
| 3 | **Portal · área do conselho** | Onde a resposta com conteúdo vive: pareceres, decisões, gatilhos, brief | Autenticado, por perfil, auditado | · |
| 4 | **O assento na reunião** | Semanal, mensal de resultados, trimestral | Por convite, anunciado, com hora de entrar e sair | Pauta enviada antes |
| 5 | **Canal do projeto** (Teams/Slack do cliente) | O campeão e a operação | Só o que já é do projeto; nada de dado pessoal | Dias úteis |
| 6 | **O gatilho · o canal invertido** | **Ele** procura **eles**: prazo vencendo, renovação chegando, indicador cruzado, decisão parada | Deadline-ordenado, sem LLM, humano confere e dá baixa | Antecedência declarada por tipo |

**O canal 6 é o produto.** Os cinco primeiros são atendimento: qualquer consultor tem. O sexto é o que resolve os "5 a 15%" do §1: é ele que impede a decisão de morrer.

### A régua: o que merece o Conselheiro

Sem filtro, a cadeira vira help desk e a margem morre (risco já apontado pelo conselho consultivo). Vai ao Conselheiro o que atender a **pelo menos um** critério:

1. Envolve **dinheiro recorrente** acima do limiar combinado no contrato;
2. Muda **quem decide o quê** (governança);
3. Cria ou remove **dependência de fornecedor**;
4. Tem **prazo externo** (renovação, obrigação, exigência de cliente);
5. Toca **dado pessoal ou regulado**.

O resto é do campeão, e **ensinar essa régua ao cliente é parte da entrega**, não um jeito de dizer não.

---

## 6. O plano de melhoria: 6 movimentos, com gatilho

| # | Movimento | O que é | Depende de | Quando |
|---|---|---|---|---|
| 1 | **Mapa de presença do cliente** | No kickoff, carregar o relógio dele: data do fechamento, reunião de resultados, janela orçamentária, pico sazonal, **todas as renovações com a data-limite de opt-out**, obrigações com data | Nada · usa gatilho + fila da manhã já construídos | **Agora** (entra no roteiro de kickoff) |
| 2 | **Inventário de custo × valor** | Uma linha por sistema/agente/licença: custo unitário, os baldes abertos, valor medido (ou "nunca medido"), dono, dependências, data de renovação | Levantamento no onboarding | Com o 1º cliente |
| 3 | **Parecer de Permanência** | O processo (§4) + modelo DOCX no padrão, irmão do de arbitragem | Movimento 2 | Com o 1º cliente |
| 4 | **A caixa de entrada** | Os 6 canais com prazos, publicados ao cliente no kickoff + a régua do §5 | E-mail + portal; WhatsApp na onda 2 | **Agora** (doutrina) |
| 5 | **Decisão de desligar vira registro medido** | Toda recomendação de desligar/reduzir nasce com hipótese, probabilidade declarada e gatilho de 90 dias | Nada · é o motor atual | Com o 1º cliente |
| 6 | **Pauta ancorada no relógio** | As pautas do ritual e do conselho passam a abrir pelo que **venceu** e pelo que **vence** · não pelo que aconteceu | Movimento 1 | Junto com 1 e 4 |

Os movimentos 1, 4 e 6 **não exigem código nem cliente**: são doutrina e podem ser escritos esta semana. Os 2, 3 e 5 entram com o primeiro cliente em manutenção.

---

## 7. O que isso muda no discurso (e o que ainda não pode ser dito)

**Pode ser dito hoje, e é forte:** *"Empresas do porte de vocês desperdiçam entre 25% e 40% do que pagam em licença, e recuperam menos de 15% disso, porque alguém aponta e ninguém acompanha. O Conselheiro é o dono do acompanhamento: cada decisão nasce com um número e uma data, e é ele que volta na data."*

**Pode ser dito, com a fonte junto:** os números de desperdício e de recuperação (§1), sempre citando a origem: doutrina do repo.

**Não pode ser dito ainda:** que o Conselheiro "conhece todos os custos da empresa" ou "monitora seus sistemas": os movimentos 2 e 3 não existem, e integração é a camada 3 do [Assento](estudo-conselheiro-presente.md), gateada.

**Nunca:** que garantimos economia. Recomendamos com convicção e probabilidade declarada; a decisão é do cliente e o resultado é medido: inclusive quando dá errado.

---

## Ligações

[Conselheiro de IA](../03-comercial/conselheiro-de-ia.md): o produto · [O Conselheiro presente](estudo-conselheiro-presente.md): como ele se senta (travas legais) · [Arbitragem de fornecedores](../04-entrega/arbitragem-de-fornecedores.md): o irmão do Parecer de Permanência · [Ritual semanal](../04-entrega/ritual-semanal.md) · [Protocolo de prova](../04-entrega/protocolo-de-prova.md): de onde vem o valor medido · [Estudo de IA financeira](estudo-ia-financeira.md): a porta do dinheiro
