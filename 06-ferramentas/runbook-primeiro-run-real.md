# Runbook do primeiro run real — o dia da chave

> **Camada:** entrega/ferramenta. Cobre o que o [runbook de ativação](runbook-ativacao.md) não cobre: aquele ensina a **ligar e não perder** o cérebro; este ensina a **gastar a primeira chave sem queimar um cliente**.
>
> **Por que existe:** a ferramenta está construída e testada com muito rigor **em mock**. Mock nunca trunca, nunca toma 429, nunca falha no meio e nunca é retomado depois de uma queda. Tudo que sabemos hoje é que a máquina está montada. Nada do que sabemos é sobre a **qualidade da análise**.
>
> Dono: Entrega (Daniel). Executar uma vez, na ordem, e marcar o checklist.

---

## Regra zero — a que protege a reputação

> **O primeiro run com chave real NÃO é um cliente pagante.**

Seis defeitos foram encontrados só **lendo** os caminhos que mock não alcança (limite de taxa, resposta cortada, morte no meio do run, retomada depois de queda). Eles foram corrigidos e nenhum deles foi observado em produção. O primeiro run é um **experimento**, e um experimento tem que poder falhar.

Custo de seguir esta regra: alguns dólares e uma tarde. Custo de ignorá-la: descobrir num relatório de cliente pago que seis dimensões erraram na mesma janela de rate limit.

---

## Etapa 0 — Ensaio, hoje, sem chave nenhuma

Nada aqui gasta um centavo. O objetivo é que no dia da chave **você já conheça o vermelho**.

```bash
cd /caminho/para/assessment-brain
export USE_MOCK_LLM=true
export ABBA_DATA_DIR=/caminho/absoluto/para/dados-ensaio

node bin/abba.js demo                              # a empresa fictícia
node bin/abba.js report "Demonstração do método ABBA"
node bin/abba.js report "Demonstração do método ABBA" --client
node bin/abba.js report "Demonstração do método ABBA" --visual
node bin/abba.js validate "Demonstração do método ABBA"
node bin/abba.js pending
```

**Leia os três artefatos inteiros, de ponta a ponta.** Esta é a etapa que as pessoas pulam, e foi exatamente ela que revelou os dois últimos defeitos client-facing: um erro de concordância no one-pager e os títulos das dimensões em inglês dentro de um documento em português. Nenhum dos dois era invisível. Ninguém tinha lido.

**O que você deve ver no `validate` do demo:**

```
Validation — Nortex Componentes (empresa fictícia) / ... (DEMO)
  ✗ Output came from a real model, not the mock
      this engagement is a DEMONSTRATION: ... a company that does not exist
```

Isso é a ferramenta funcionando. A peça de demonstração é a única que **nenhuma chave pode certificar**, e ela reprova de propósito.

---

## Etapa 1 — O primeiro run pago, sobre corpus interno

```bash
unset USE_MOCK_LLM
export ANTHROPIC_API_KEY=...            # no .env, chmod 600
export ABBA_DATA_DIR=/caminho/absoluto/para/dados-reais
export ABBA_DB_PASSPHRASE=...           # regra zero do runbook de ativação

node bin/abba.js doctor --live          # a chave responde? qual renderizador de PDF existe?
node bin/abba.js engagement create "Ensaio interno" --client "ABBA" --profile manufacturing-mid-market
node bin/abba.js ingest "Ensaio interno" ./corpus --level c_suite --phase 2
node bin/abba.js assess "Ensaio interno" --dry-run          # estimativa, zero gasto
node bin/abba.js assess "Ensaio interno" --budget 8
```

**Corpus:** documentos da própria ABBA, ou o Cliente Zero. Nada de cliente pagante.

**Antes de o dinheiro sair, o `assess` vai avisar sobre:**
- documentos entregues que não puderam ser lidos (PDF escaneado sem camada de texto) — este é o momento mais barato de corrigir: rode OCR e reingira;
- menos de dois níveis internos ouvidos, ou fontes sem `--level` — uma fonte sem nível é invisível para a detecção de contradições, que é a assinatura do método.

**Se aparecer `rateLimitHits` no resumo:** baixe `ABBA_DIMENSION_CONCURRENCY` (padrão 6) para 3 e rode de novo. Seis chamadas simultâneas caindo na mesma janela de limite viram um assessment parcial pago por inteiro.

**Se o run morrer no meio:** `abba assess "Ensaio interno" --resume`. O custo já gasto foi gravado, então o `--budget` continua honesto e você não paga duas vezes.

---

## Etapa 2 — A linha de base do eval (a mais importante, e a mais pulada)

```bash
npm run eval                             # com chave real, sobre a fixture mediflow
```

Hoje o eval compara **mock contra mock**. É um portão de regressão real da máquina e não diz absolutamente nada sobre qualidade de análise. **Enquanto esta linha de base não existir, toda mudança de prompt daqui para frente é fé.**

Commite a baseline. A partir dela, `abba pending` deixa de ser uma lista de dúvidas e vira uma lista de coisas mensuráveis.

---

## Etapa 3 — O veredito, e o vermelho que é normal

```bash
node bin/abba.js validate "Ensaio interno"
```

**Dois portões que É PARA reprovar no dia um.** Se reprovarem, o sistema está funcionando, não quebrando:

| Portão | Por que reprova | O que fazer |
|---|---|---|
| `roi.reconciled` | A soma dos vazamentos e a estimativa top-down são cálculos independentes. Divergiram 70% na fixture e 91% no smoke de julho. | É o portão humano: reconcilie antes de a firma citar um número. Divergência vira **faixa**, nunca um ponto. |
| `recommender.coverage` | Um vazamento crítico ou alto sem construção atrás. | Leia o bloco de completude antes: se o recomendador **registrou** ter perdido aquele lote, é degradação declarada e vira aviso, não lacuna de análise. |

**Qualquer terceiro bloqueio é regressão, e aí vale parar.**

O que só você pode julgar está impresso como checklist no fim do relatório e termina em *"você assinaria seu nome embaixo disso?"*. **Checklist não assinado significa cabeado, não validado.**

---

## Etapa 4 — Ler tudo inteiro, de novo

Os três artefatos, de ponta a ponta, com olho de cliente. A lição da onda anterior é que os defeitos que chegam ao cliente não são sutis: são óbvios para quem lê e invisíveis para quem só roda testes.

Anote o que soar falso. É o único momento em que a diferença entre "a máquina rodou" e "eu assinaria isso" fica visível.

---

## Etapa 5 — Os itens que estavam esperando a chave

Com a linha de base no lugar, na ordem:

1. **Fence de documentos do cliente** — está **LIGADO em todo run desde já** e mudou seis prompts. Compare captura e recall de vazamento contra a baseline. Deveria custar zero; se a captura cair, o cabeçalho do fence está competindo com as instruções.
2. **Cache de prompt** (`ABBA_PROMPT_CACHE`) — rode o eval ligado e desligado. A taxa de captura não pode se mexer. Economia grande, mas o texto cacheado é uma permutação da IP validada.
3. **Espinha loop-native** (`ABBA_RECOMMENDER_SPINE=loops`) — rode as duas espinhas no mesmo engajamento real. A espinha de loops ganha se as construções dela forem as que um sócio recomendaria e a espinha de vazamentos tiver perdido.
4. **Prioridades de upside por setor** — ratificar com o Pedro primeiro, ligar depois de medir sem elas.
5. **Peso do prêmio** (`abba rank whatif --prize`) — leia o breakeven em cada run real. Critério de decisão: quantas vezes a confissão do prêmio enterrado apontou uma construção que você promoveu na mão.
6. **Exposição de integração por construção** (`abba rank whatif`) — leia as duas colunas. Se a ordem simulada for a que um sócio defenderia, ligue; se não, o que muda é o texto do relatório.

`abba pending` mantém essa lista viva e diz como julgar cada uma. Um item sem critério de julgamento fica pendente para sempre.

---

## Etapa 6 — Só então, o primeiro cliente pagante

Pré-requisitos, todos:

- [ ] Etapa 1 rodou inteira sem run parcial
- [ ] Baseline real do eval commitada
- [ ] `validate` sem bloqueio inesperado
- [ ] Os três artefatos lidos de ponta a ponta
- [ ] Checklist humano assinado por Daniel e Pedro
- [ ] Passphrase em custódia dupla (regra zero do runbook de ativação)
- [ ] Contrato com o anexo de contribuição anonimizada assinado **antes** do primeiro dado entrar

---

## Checklist do dia (imprimir e marcar)

```
[ ] 0. Ensaio em mock: demo + 3 artefatos lidos + validate + pending
[ ] 1. doctor --live responde
[ ] 2. Corpus interno ingerido, avisos de ingestão zerados
[ ] 3. assess --dry-run: estimativa conferida
[ ] 4. assess --budget apertado, modelo barato
[ ] 5. rateLimitHits == 0 (senão: baixar ABBA_DIMENSION_CONCURRENCY e repetir)
[ ] 6. npm run eval com chave real, baseline commitada
[ ] 7. validate: só roi.reconciled e/ou recommender.coverage bloqueando
[ ] 8. Três artefatos lidos inteiros, anotações feitas
[ ] 9. Checklist humano assinado
```

---

## O que este runbook não promete

Ele não promete que a análise vai ser boa. Promete que, se ela não for, você vai **saber** — e vai saber no dia em que isso custa uma tarde, não no dia em que custa um cliente.
