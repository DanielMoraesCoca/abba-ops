# O Contrato da Máquina — leitura executiva

> Fonte técnica completa: `assessment-brain/docs/contrato-da-maquina.md` · Registro executável: `src/core/contract.js` · Comando: `abba contract` · Trava: `test/unit/contract.test.js`.
>
> Este documento resume a decisão e o porquê. O conteúdo vive no repo da ferramenta, pela regra do [FONTE_DA_VERDADE](https://github.com/DanielMoraesCoca/assessment-brain/blob/main/docs/FONTE_DA_VERDADE.md): engenharia da ferramenta no repo da ferramenta, decisão de negócio aqui.

## O que é

**119 invariantes** organizados em 8 camadas: o que precisa ser verdade em qualquer implementação da ferramenta de assessment, em qualquer linguagem. Cada um traz a garantia, o motivo pelo qual ela existe (quase sempre um defeito real que já custou algo) e o teste que a prova.

Não é a anatomia (que descreve ESTE código, com arquivo e linha, e envelhece a cada commit) nem o framework (que descreve o método). É a terceira coisa, e a única que sobrevive a uma troca de linguagem.

## De onde ele veio

Dos testes. Um teste não é código, é uma intenção escrita, e os nomes dos 740 que já existiam liam como invariantes: *"mock output cannot pass as a real run"*, *"a wrong link is worse than an absent one"*, *"the delivered ranking is frozen, and the harness can prove it"*.

Foi **transcrição, não invenção**. É por isso que ele é confiável, e por isso que custou dias em vez de semanas.

## Por que ele vem ANTES do repositório novo

Porque **ele é o critério de aceitação do porte**.

Hoje, "portamos para Python/CrewAI?" é uma pergunta de meses, porque ninguém consegue dizer o que o porte precisa entregar. Com o contrato, vira: *"estes 114 invariantes marcados `porte` passam na implementação nova? sim ou não"* — uma pergunta de um dia, respondida por `abba contract --portable`.

E ele sobrevive a todos os ramos da decisão:

- Se portarmos, é a especificação.
- Se não portarmos, é o onboarding de quem entrar no motor.
- Em qualquer caso, é o que responde **"o que está faltando"**, que era o objetivo declarado quando o CrewAI foi levantado.

## O que ele NÃO dá, e está escrito nele

O contrato cobre o que a máquina garante. Ele não cobre **se a análise é boa**, porque a ferramenta nunca leu uma empresa real. A simulação nunca trunca, nunca falha, nunca é limitada por taxa e nunca varia. Toda garantia é verdadeira sob simulação e sob os caminhos de erro forçados pelos testes; nenhuma foi vista contra a saída de um modelo real lendo os documentos de uma empresa de verdade.

A Parte IV do documento técnico lista o que espera a chave, e nomeia quais portões o primeiro run **deve** reprovar, para que um veredito vermelho seja lido como o sistema funcionando e não como a ferramenta quebrando.

## A decisão do repositório novo

**Não agora.** O desenho está pronto e inerte na Parte V: estrutura proposta, o que migra e o que não migra, o custo medido (3 a 6 meses, 57.851 linhas de código e teste) e o critério de aceitação.

Os quatro gatilhos que autorizam começar:

1. O Pedro assumir a manutenção do motor e trabalhar só em Python. É o argumento mais forte e o único que não se mede de dentro do código.
2. O motor precisar virar agêntico de verdade: delegação, decomposição dinâmica, negociação entre agentes.
3. A parceria amarrar valor comercial material ao porte, ou exigi-lo.
4. A ferramenta precisar rodar dentro da infraestrutura Python de um cliente.

Enquanto nenhum for verdade, a ordem é: **o primeiro voo → a visibilidade que motivou o pedido (rastro de run legível + o painel que já existe) → só então a decisão do porte, contra esta lista.**

## O que muda na prática, hoje

- `abba contract` imprime os 119 invariantes; `--portable` imprime a lista de aceitação; `--layer <id>` filtra uma camada.
- Se alguém apagar ou renomear um teste que sustenta um invariante, **a construção quebra**. O documento não pode apodrecer em silêncio, que é o modo de falha de todo documento técnico que esta empresa já escreveu.
- A lista de aceitação do porte é **derivada** do registro, nunca escrita à mão. Lista escrita à mão é lista que envelhece errado, e já pagamos por essa lição duas vezes.
