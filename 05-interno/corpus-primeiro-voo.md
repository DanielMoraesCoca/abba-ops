# Corpus do primeiro voo — o que a máquina vai ler, e por quê

> **Camada:** interno. Prepara a Etapa 1 do [runbook do primeiro run real](../06-ferramentas/runbook-primeiro-run-real.md), que segue **bloqueada em uma variável**: o ambiente do Claude não tem `ANTHROPIC_API_KEY` ([log do Cliente Zero](cliente-zero-execucao.md)). Verificado de novo em 2026-09-05: o `.env` é o template, com os valores vazios.
>
> Dono: Entrega. O corpus é montado por [script](../scripts/montar-corpus-primeiro-voo.sh), não commitado: ele é uma **vista** dos documentos vivos, e uma cópia envelheceria em silêncio até a máquina ler uma ABBA que não existe mais.

## A regra de curadoria

> **O corpus carrega EVIDÊNCIA, nunca conclusão alheia.**

Ficaram de fora, de propósito, o [parecer do conselho](parecer-conselho-2026-08.md), a [auditoria de prontidão](auditoria-prontidao-2026-08-18.md) e o [plano de ação](plano-de-acao.md). Os três são análises **prévias** da ABBA. Alimentar a máquina com a conclusão de outra pessoa a faria lavar aquela conclusão como achado próprio, e o primeiro voo deixaria de medir a única coisa que ele existe para medir: se ela sabe LER uma empresa. Um engajamento real não recebe o relatório do consultor anterior como fonte; se receber, entra com `--level consultant` e sabendo o que isso significa.

Também fora: tudo que descreve a **ferramenta** em vez da **firma** (runbooks, dossiês técnicos, contrato da máquina). A empresa a ser lida é a ABBA que vende e entrega.

## O que entra, e em que nível

19 documentos, **84 KB** armazenados. Para calibrar: a fixture MediFlow do eval tem 8 documentos e 51 KB.

| Nível | Fase | O que é | Docs |
|---|---|---|---|
| `ceo_board` | 1 | A posição declarada dos sócios: o que a empresa é, o modelo, o acordo | 4 |
| `c_suite` | 2 | Os chapéus, que são vozes funcionais distintas mesmo com duas pessoas | 6 |
| `dept_head` | 3 | Quem opera o processo: ritual semanal, SLA, pipeline, imersão | 4 |
| `internal_data` | 0 | O estado medido: riscos, finanças, planilha de preço, mapa de ferramentas | 4 |
| `external` | 2 | A única reunião real registrada com alguém de fora | 1 |

**`front_line` e `consultant` não existem, e o `assess` avisa isso.** É honesto: a ABBA não tem linha de frente. Vale registrar o que isso custa — a detecção de contradições cruza níveis, e o par mais revelador do método (topo × operação) não existe aqui.

## O que este voo mede bem, e o que não mede

**Mede bem a MÁQUINA:** o pipeline sobrevive a saída real? As 25 dimensões chegam? O JSON aguenta? A confissão dispara? O custo bate? O `--resume` funciona depois de uma queda? São exatamente os caminhos que o mock nunca alcança.

**Mede mal a ANÁLISE.** A ABBA é uma firma de dois sócios sem receita, sem sistemas operacionais e sem departamentos. Um framework de 25 dimensões desenhado para o mid-market vai achar pouco o que quantificar. Quem mede qualidade de análise é o **passo 1 da Etapa 1: `npm run eval` sobre a fixture MediFlow**, com linha de base commitada. Os dois passos são necessários e não se substituem.

## Custo medido, não estimado no olho

`assess --dry-run` sobre este corpus exato:

```
Sources: 19 (82.4 KB)
Input tokens:  756.880 · Output: 77.000
Estimated cost: $1.37  (bruto $1.14 × 1,2 de folga)
```

O `--budget 8` do runbook é folgado de propósito. O custo da análise fica em **dólar** (é o que a Anthropic cobra); os números do relatório saem em **real**, porque o engajamento declara `--currency BRL`.

## Dois defeitos que o ensaio achou antes de a chave chegar

Os dois só aparecem com documento de verdade. Os dois estavam invisíveis porque a fixture do eval é americana e enxuta.

**1. O redator comia toda data de documento.** O padrão `DOB` prometia no comentário "só quando é claramente forma de data de nascimento" e não discriminava nada: casava qualquer data ISO. Medido: **331 datas no abba-ops, todas de revisão e reunião, zero nascimentos** — 21 delas dentro deste corpus. "Última revisão: 2026-07-22" chegava ao modelo como "Última revisão: [DOB_1]". Não é cosmético: cadência, atraso, o que está velho e sobretudo **contradição entre níveis** leem datas. Corrigido nos dois motores com um corte que é **constante, nunca o ano corrente** (ler o relógio faria a anonimização mudar na virada do ano, e o oráculo diferencial compara texto byte a byte).

**2. A detecção de contradições transformava mobília de markdown em fala de stakeholder.** O separador de frases corta em pontuação, e título e linha de tabela não têm nenhuma — então o título colava no bloco de baixo e virava "asserção". Sobre este corpus: **429 contradições, 76% com estrutura de markdown de pelo menos um lado**, e o relatório imprimia isso sob a frase mais forte que ele tem: *"no model judgement involved, both quotes are verbatim from the ingested material"*. Uma das citações verbatim era `## Checklist de existência`; dois itens de checkbox sem relação viravam divergência de quantidade **entre níveis**.

Corrigido, e medido nos três corpora antes de entrar, porque uma guarda que tirasse SINAL seria pior que o ruído:

| Corpus | Antes | Depois |
|---|---:|---:|
| ABBA, 19 documentos | 431 | **86** |
| MediFlow, 8 documentos EN | 123 | **123** |
| Nortex demo, 5 fontes PT (contradição plantada) | 1 | **1** |

**Isto não é específico da ABBA.** O [checklist de documentos](../04-entrega/checklist-documentos-assessment.md) pede política, manual de processo e POP a todo cliente, e um PDF convertido carrega a mesma mobília.

## Duas coisas registradas, e não consertadas

1. **As 86 que sobram ainda são majoritariamente ruído.** O método `negation_vs_evidence` assume alguém afirmando um valor; documentação de processo não faz isso. O provável certo é o detector rodar só sobre fontes de entrevista, nunca sobre `internal_data`. É decisão de sócio sobre o método, não conserto de bug — **não leia a seção de contradições do relatório deste voo**.
2. **O detector lê dígito, não número por extenso.** "cinco dias" contra "doze dias" não casa; "5" contra "12" casa. Fala brasileira de entrevista é cheia de número por extenso, e as próprias fontes PT do demo são assim. Medido, anterior a qualquer mudança desta rodada.

## A sequência do dia da chave

Nada aqui roda sem `ANTHROPIC_API_KEY` no ambiente. **Nunca colar a chave no chat.**

```bash
cd assessment-brain
export ANTHROPIC_API_KEY=...          # no ambiente, ou .env com chmod 600
export ABBA_DB_PASSPHRASE=...         # regra zero do runbook de ativação
export ABBA_DATA_DIR=/caminho/absoluto/para/dados-reais
unset USE_MOCK_LLM

node bin/abba.js doctor --live        # a chave responde de verdade?

sh ../abba-ops/scripts/montar-corpus-primeiro-voo.sh /caminho/para/corpus

node bin/abba.js client create "ABBA" --industry consultoria
node bin/abba.js engagement create "ABBA" "Ensaio interno" --profile general --currency BRL
for N in ceo_board:1 c_suite:2 dept_head:3 internal_data:0 external:2; do
  node bin/abba.js ingest "Ensaio interno" /caminho/para/corpus/${N%%:*} \
    --level ${N%%:*} --phase ${N##*:}
done

node bin/abba.js assess "Ensaio interno" --dry-run     # deve dizer ~$1,37
node bin/abba.js assess "Ensaio interno" --budget 8
node bin/abba.js validate "Ensaio interno"
```

Depois, o passo que mede análise e é o mais pulado:

```bash
npm run eval        # com chave real, sobre a fixture MediFlow; commite a linha de base
```

**O que É PARA reprovar no dia um** está na [Etapa 3 do runbook](../06-ferramentas/runbook-primeiro-run-real.md): `roi.reconciled` e `recommender.coverage`. Qualquer terceiro bloqueio é regressão.
