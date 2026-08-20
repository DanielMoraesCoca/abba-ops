# Oficina de Casos — como os processos reais do cliente entram nas aulas

> **O que resolve:** a promessa comercial *"a trilha de vocês se monta
> com os casos de vocês"* ([falas](../03-comercial/falas-treinamento.md))
> não tinha protocolo. O portal já sabe receber conteúdo específico por
> cliente — a tela `/admin/lesson-overrides` guarda um override por
> (cliente × aula) — mas ninguém tinha escrito **como se colhe o caso e
> como ele vira aula**. Este é o documento que fecha esse buraco.
>
> **Quando acontece:** entre a assinatura e o kickoff, idealmente 10 a 14
> dias antes. Nunca depois do kickoff — as aulas da semana 1 precisam já
> estar com a cara deles.
>
> **Quem entra:** 6 a 10 pessoas do cliente (as que fazem o trabalho, não
> só as que mandam nele) + 1 facilitador ABBA + 1 pessoa de TI ou
> segurança da informação no bloco 4.
>
> **Duração:** 90 minutos. Presencial se possível; funciona por chamada.

---

## Por que existe

Aula com exemplo genérico ensina o movimento e não muda o trabalho. A
pessoa entende o princípio, concorda com ele e volta para a mesa fazer
tudo igual, porque o exemplo era de outra empresa, de outro cargo, de
outro problema.

O que trava a transferência quase nunca é a compreensão. É a distância.
A Oficina de Casos é o instrumento que encurta essa distância antes de a
turma começar — e tem um efeito secundário grande: as 6 a 10 pessoas que
participam chegam ao kickoff **já comprometidas**, porque o conteúdo tem
a mão delas.

---

## Preparação (facilitador, 1 hora antes)

- [ ] Ler o organograma da área e os cargos que entram na turma
- [ ] Ter a lista das aulas da trilha que aquele público vai fazer
- [ ] Levar 40 fichas em branco (papel — a coleta é manual, de propósito:
      papel força a frase curta e todo mundo escreve ao mesmo tempo)
- [ ] Levar impressos: Lente de Oportunidade, Semáforo de Dados, Bússola
      ([artefatos](../08-materiais/artefatos-impressos.md))
- [ ] Combinar com o patrocinador que ele **abre e sai**. A presença do
      chefe na sala inteira faz as pessoas trazerem tarefa nobre em vez
      de tarefa chata — e a tarefa chata é a que rende

---

## Roteiro (90 min)

| Bloco | Min | O que acontece | Saída |
|---|---|---|---|
| 0 · Abertura do patrocinador | 5 | *"Vocês vão dizer o que realmente fazem. Não existe tarefa pequena demais para entrar aqui."* Ele sai | tom |
| 1 · Inventário da semana | 20 | Cada um escreve **8 tarefas recorrentes** da própria semana, uma por ficha: o que é, com que frequência, quanto tempo leva. Sem discutir, sem filtrar | 50–80 fichas |
| 2 · A Lente na mesa | 25 | Em duplas, passam as fichas pela Lente de Oportunidade (4 perguntas, 1 ponto cada). Fichas de 4 pontos numa pilha, 2–3 noutra, 0–1 na terceira | pilhas pontuadas |
| 3 · As doze | 20 | O grupo escolhe as **12 tarefas** que mais se repetem entre pessoas diferentes. Critério explícito: aparece na ficha de mais de uma pessoa · é frequente · dá para conferir. Cada uma ganha um nome curto | as 12 tarefas-âncora |
| 4 · O Semáforo deles | 15 | Com TI/segurança na sala: para cada uma das 12, qual dado ela toca e em que faixa cai — verde, amarelo, vermelho — **segundo a política da empresa**, não a nossa | Semáforo preenchido |
| 5 · Fechamento | 5 | Ler as 12 em voz alta. Combinar que elas vão aparecer nas aulas | compromisso |

**A regra que faz a oficina funcionar:** no bloco 1, ninguém julga
tarefa. A tarefa que a pessoa tem vergonha de dizer que faz — conferir
planilha na mão, redigir o mesmo e-mail pela vigésima vez, reformatar
relatório — é a mais valiosa da sala. Se o facilitador reagir a uma
ficha com surpresa, a próxima pessoa esconde a dela.

---

## O que sai da oficina (as quatro saídas)

### 1. As 12 tarefas-âncora

Uma linha cada: nome curto · quem faz · frequência · tempo · pontuação
da Lente · faixa do Semáforo. É o documento-mãe de tudo o que vem
depois.

### 2. Os overrides de aula

As tarefas-âncora entram nas aulas por `/admin/lesson-overrides` (um
override por cliente × aula). **O que se troca e o que nunca se troca:**

| Trocar | Manter intacto |
|---|---|
| o exemplo do Gancho, quando existir uma tarefa-âncora que caiba | a estrutura de blocos e os minutos |
| os `placeholder_slots` do Faça Você (o "[seu cargo]" vira o cargo real) | os três princípios da Leitura |
| o vocabulário: nome do sistema, do documento, da área | a Rubrica ABBA e a redação da Bússola |
| o artefato pedido para colar | os critérios da rubrica de avaliação |

> **A regra da coerência:** override muda **a roupa** do exemplo, nunca
> **o osso** da aula. Se um caso do cliente exigir mudar o princípio, o
> princípio está errado para todo mundo — corrige-se na aula canônica, não
> no override.

### 3. Os desafios da turma

Duas das 12 viram desafio da semana no
[banco de desafios](../../abba-portal/docs/platform/content/banco-de-desafios.md),
com o gabarito escrito por quem faz a tarefa. Um desafio com o nome do
sistema deles vale por dez genéricos.

### 4. A pauta do kickoff

O facilitador entra na sala do kickoff citando três tarefas-âncora nos
primeiros dez minutos. O efeito é imediato e é o objetivo inteiro da
oficina: *"eles não vieram falar de IA, vieram falar do nosso
trabalho."*

---

## Depois da oficina — o trabalho do facilitador (4 a 6 horas)

1. Digitar as 12 âncoras na tabela-mãe → `02 Clientes/<Nome>/02 Onboarding/`
2. Escrever os overrides das aulas da semana 1 e 2 (as demais podem
   esperar a turma começar)
3. Escrever os 2 desafios com gabarito
4. Preencher o Semáforo do cliente no material impresso da turma
5. Mandar ao patrocinador **as 12 âncoras** — não o material — com uma
   linha: *"é isto que a turma vai atacar; se faltou alguma, me diga até
   sexta"*

---

## Sinais de que a oficina falhou

- Saíram menos de 8 âncoras: o grupo trouxe projeto em vez de tarefa.
  Refazer o bloco 1 pedindo explicitamente **"o que você fez ontem"**.
- Todas as âncoras são de uma pessoa só: o grupo estava desbalanceado ou
  alguém dominou a sala.
- Nenhuma âncora é chata: o patrocinador ficou na sala, ou o facilitador
  reagiu mal a uma ficha.
- O Semáforo saiu todo verde: TI não estava presente de verdade. Sem o
  Semáforo real, a aula de dados não pode ser específica — e é a aula
  que mais protege o cliente.

---

## Preço e posicionamento

A oficina é **parte da entrega**, não item vendido à parte — mas é dita
em voz alta na proposta, porque é o que a concorrência não faz. A frase
da mesa:

> *"Antes da primeira aula, a gente passa noventa minutos com as pessoas
> que fazem o trabalho e sai com as doze tarefas que a turma vai atacar.
> As aulas de vocês vão ter o nome dos sistemas de vocês. Não é
> treinamento adaptado — é treinamento construído em cima do que vocês
> fazem."*
