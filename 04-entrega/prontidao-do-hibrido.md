# Prontidão do híbrido: o que existe, o que falta, o que quebra na escala

> **Para que serve:** responder, com número e caminho de arquivo, à
> pergunta que antecede qualquer proposta de turma grande: *o que
> exatamente nós temos no treinamento híbrido, e o que exatamente
> falta?* Levantado em **2026-08-26** contra o cenário real em mesa:
> **Brasal, ~70 pessoas, modelo híbrido, kickoff na semana seguinte**.
>
> **Regra deste documento:** nada aqui é aspiração. Cada linha da
> coluna "existe" aponta para um arquivo que se abre hoje; cada linha
> de "falta" diz quem destrava e em quanto tempo.

---

## 0. A resposta curta

O **conteúdo e a máquina estão prontos** para uma turma real. O que
**não** está pronto é a **capacidade de sala** para 70 pessoas e a
**janela de tempo** de um kickoff na semana seguinte.

Passar de 25 para 70 pessoas **não** exige reescrever o programa: a
turma continua sendo de até 25 e o portal escala sozinho. O que muda é
**quantas vezes o sócio entra na sala** e **quantas pessoas circulam na
Clínica**. É aí que quebra, e quebra antes do que parece: já numa
única turma de 25.

---

## 1. A conta de 70 pessoas no híbrido

| | |
|---|---|
| Pessoas | ~70 |
| Turmas (até 25 por turma, decisão E4) | **3** (25 · 25 · 20) |
| Investimento | **R$ 91.000**: R$ 35.000 (1ª turma) + 2 × R$ 28.000 (adicionais, −20%) |
| Pagamento | 50% na assinatura · 50% na formatura da Fundação |
| Acesso ao portal | 12 meses, todas as 70 pessoas |
| **Meios-períodos de sala** | **12** (4 encontros × 3 turmas) |

**Turmas em paralelo** (mesmo calendário): 4 semanas de marco, 3 dias
de sala cada. **Turmas em série:** o programa de 8 semanas vira ~24
semanas de calendário. A escolha é comercial e precisa estar na
proposta: não é detalhe de execução.

---

## 2. O que EXISTE (e onde)

### 2.1 Trilho assíncrono: o portal

| O quê | Quanto | Onde |
|---|---|---|
| Aulas em pt-BR, 4 blocos (gancho · leitura · faça você · reflexão) | **27**: Fundação 8 · Operacional 6 · Gestor 5 · Especialista 8 | `abba-portal/docs/platform/content/lessons/` |
| Desafios no catálogo | **27**: 14 exigíveis (contam para subir) + 8 drills + 5 Prompt Golf + 3 cenários de decisão | `abba-portal/src/lib/challenges.ts` |
| Biblioteca de Pedidos | **40** pedidos por área, todos terminando em conferência | `abba-portal/src/lib/prompt-library.ts` |
| Boletim ABBA (estudo semanal) | **8 números**, publicação automática às segundas | `abba-portal/docs/platform/content/boletim/` |
| Bússola (PARAR · COMEÇAR · SÓ EU) | instrumento + cadência d7/d30/d60/d90 | portal, `/compass` e `/me/cadence` |
| Iris (guia em português) | disponível em toda tela | portal |
| Graduação com máquina | portão base comum 8/8 + ≥6/8 drills, emissão de credenciais **em lote** | `/admin/graduacao` |
| Credencial verificável | pt-BR de ponta a ponta, sem índice de fluência | `/verify` |
| Corroboração de aplicação | **5 sinais medidos** (aulas · desafios exigíveis · Bússolas visíveis · aplicou com evidência de 30 dias · ajudou um colega); **o gestor confirma o que viu** | `/manager/cohort` |

### 2.2 Trilho síncrono: a sala

| O quê | Estado | Onde |
|---|---|---|
| **Os 4 encontros roteirizados** (Kickoff · Marco 1 · Marco 2 · Graduação) | run-of-show minuto a minuto, falas word-for-word, contingências, 8 perguntas céticas com resposta pronta, briefing do patrocinador | [kit-do-facilitador.md](kit-do-facilitador.md) |
| **Oficina de Casos** | 90 min com 6–10 pessoas, **10 a 14 dias antes do kickoff**: produz as 12 tarefas-âncora que tiram o programa do genérico | [oficina-de-casos.md](oficina-de-casos.md) |
| **Ficha de Linha de Base** | Partes A/B/C: sem ela não há relatório d90 | [../08-materiais/ficha-linha-de-base.md](../08-materiais/ficha-linha-de-base.md) |
| Kit da turma (cronograma, cerimônia) | escrito | [kit-da-turma.md](kit-da-turma.md) |
| Plano de capacitação (checklist de montagem) | escrito | [plano-de-capacitacao.md](plano-de-capacitacao.md) |
| Artefatos impressos (6 cards do Kickoff) | **texto final**; arte e gráfica pendentes | [../08-materiais/artefatos-impressos.md](../08-materiais/artefatos-impressos.md) |
| Certificados | modelo pronto | `../08-materiais/modelos/certificados-modelo.pptx` |

### 2.3 A prova (o que se assina)

Linha de base no dia 0 → checkpoints d30/d60/d90 cobrados pelo portal →
**[relatório de durabilidade de 90 dias](relatorio-d90-modelo.md)**,
assinado. É o fecho do serviço 5 e a ponte comercial.

---

## 3. O que FALTA: por risco para esta venda

### 🔴 3.1 Capacidade de sala (o que quebra na escala)

O kit do facilitador especifica, na **Clínica da Primeira Vitória** do
Kickoff (55 min): *"facilitadores circulantes: **1 por ~6 pessoas**"*.

- Turma de 25 → **4 a 5 pessoas circulando**.
- A ABBA tem **2 sócios**.

**Isto quebra já na primeira turma**, antes de qualquer conta de 70. É
o único item desta lista que nenhum documento resolve: é decisão de
operação. Saídas possíveis, em ordem de honestidade:

1. **Turmas em série**, começando pela de 25: os 2 sócios cobrem a
   Clínica com razão 1:12 e a qualidade cai de forma declarada;
2. **Campeões da turma anterior circulam** na turma seguinte: é o
   desenho do programa (o campeão sai "com encargo de formar dois"),
   mas **não existe na Turma 1**;
3. **Contratar/formar facilitadores** antes do kickoff: prazo que a
   semana que vem não comporta;
4. **Reduzir a Clínica** e trocar por trabalho em duplas: muda o
   roteiro e precisa ser escrito, não improvisado na sala.

### 🔴 3.2 O estoque do Boletim acaba antes da formatura

Os 8 números vão até **05/10/2026**. Com kickoff na semana de 02/09, a
graduação (semana 8) cai por volta de **28/10**: o Boletim seca
**~3 semanas antes da formatura**, e a proposta vende **12 meses de
academia**. É dívida editorial com data marcada.

**Destrava:** um número novo por semana, dono são os sócios; o
`turma:preflight` já avisa quando não há número futuro no estoque.

### 🔴 3.3 A janela da Oficina de Casos já colide com o kickoff

A Oficina exige **10 a 14 dias antes** do kickoff. Kickoff na semana
que vem significa que **a janela já passou ou está passando agora**.
Sem Oficina, a turma roda com exemplo genérico, e é exatamente o que o
Marco 1 existe para não ser.

**Destrava:** agendar a Oficina esta semana (é 90 min com 6–10 pessoas
da Brasal) **ou** mover o kickoff uma semana.

### 🔴 3.4 Os itens do dono (sem eles a turma não abre)

`abba-portal/docs/operational/PENDING_FOUNDER_ACTIONS.md` §0: nenhum é
meu, todos são seus: migrações de agosto · template do magic link com
`{{ .TokenHash }}` · `RESEND_API_KEY` + SMTP próprio · `ANTHROPIC_API_KEY`
· `NEXT_PUBLIC_APP_URL` · plano do Vercel · ensaio da demo no ambiente
real (`npm run demo:rehearsal`).

### 🟠 3.5 Vídeos: zero gravados

14 de 27 roteiros escritos (Fundação 8 + Operacional 6); faltam Gestor
5 e Especialista 8. **Nenhum vídeo gravado.**

Isto **não** bloqueia a turma: a aula é completa por desenho sem vídeo
(4 blocos) e a proposta já diz que o serviço "não é biblioteca de
vídeo". Mas é a diferença entre o produto de hoje e o produto que a
gente diz que quer. **Nunca prometer vídeo com data.**

### ✅ 3.6 O degrau vazio deixou de existir (fechado em 03/09)

Este item registrava que o topo da escada tinha máquina completa
(capstone, portão de atestação, workspace) e **zero conteúdo**. A
escada inteira foi revogada em 26/08 e a segmentação por papel em
02/09: hoje são **27 aulas e 15 desafios exigíveis, os mesmos para
todo mundo**, sem degrau nenhum. O capstone continua existindo como
desafio de entrega, e o desbloqueio da ferramenta de agentes passou a
depender de **concluir a formação**, que é coisa que qualquer pessoa
da turma pode fazer.

### 🟠 3.7 Cards impressos na gráfica

Texto final pronto; falta arte final + gráfica: **prazo externo**, que
é o tipo que não se recupera na véspera.

---

## 4. "O conteúdo está tão bom quanto poderia?": leitura honesta

**O que está genuinamente bom:** as 27 aulas em pt-BR com tarefa real
da pessoa, os 4 blocos, a Rubrica ABBA como régua única, a Bússola com
cadência cobrada, o kit de sala com fala word-for-word, e a medição de
ponta a ponta (linha de base → d90 assinado). Isso é mais do que a
maioria dos concorrentes entrega.

**Onde o conteúdo fica devendo, de verdade:**

1. **Profundidade além de 8 semanas.** O programa vende 12 meses. O
   Boletim tem 2 meses de estoque e a Prática de Hoje **rotaciona** um
   acervo fixo (8 drills + 5 golfs + 40 pedidos): no mês 6 a pessoa
   revê o que já viu. A academia diária é excelente por desenho e
   **rasa por acervo**.
2. **Personalização com os casos do cliente.** O instrumento existe (a
   Oficina + o override de conteúdo por tenant), mas exige a janela do
   item 3.3. Sem ela, o conteúdo é bom e genérico.
3. **Vídeo.** É o que o comprador espera ver e não vê.

---

## 5. O caminho para a Brasal (recomendação)

**Vender 3 turmas em série, não em paralelo:** a primeira de 25, e as
seguintes puxadas pelos campeões formados na anterior. Isso resolve a
capacidade de sala com o próprio desenho do programa em vez de
improviso, e transforma a limitação em argumento: *"a segunda turma é
conduzida pelos campeões da primeira: é assim que a capacidade fica
na casa de vocês."*

**Antes de enviar a proposta, fechar três coisas:**

1. Kickoff **uma semana depois** do que se pensou, para caber a Oficina
   de Casos (ou Oficina agendada nesta semana);
2. Os itens do §0 confirmados no ambiente da demo;
3. A decisão série × paralelo, porque ela muda o cronograma e o preço
   na página.

---

## Histórico

| Versão | Data | Mudança |
|---|---|---|
| v1 | 2026-08-26 | Criado para responder "o que temos e o que falta no híbrido" antes da proposta de ~70 pessoas da Brasal. Achado principal: a razão 1:6 da Clínica da Primeira Vitória quebra já numa turma de 25 com 2 sócios |
