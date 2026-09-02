# Vale a pena reescrever o assessment em Python/CrewAI?

> **Camada:** interno / decisão. Estudo pedido pelo Daniel em 2026-09-02: analisar, "como matemático e como líder tomador de decisões", se compensa transportar a ferramenta de assessment pago para CrewAI. Fato que entra na conta: **a ABBA tem parceria com a CrewAI, pelo Pedro.**
>
> **Veredito: não agora.** Os gatilhos que invertem a resposta estão no fim. Todo número aqui foi medido no repositório, não estimado, e o comando que reproduz cada um está na última seção.

---

## A motivação era boa, e ela tem uma resposta mais barata

A razão declarada foi visibilidade: "lá conseguimos mexer com mais facilidade, entender o que está faltando". Esse é um problema real e vale ser resolvido. Só que ele é de **opacidade**, não de linguagem: a ferramenta nunca leu uma empresa de verdade, então não há o que enxergar ainda, em Python ou em Node. O que falta é o primeiro voo, não um porte.

## 1. O que a ferramenta é, em números

| Camada | Linhas |
|---|---:|
| `src/` | **41.044** |
| `test/` (137 arquivos, 740 testes) | **15.552** |
| `web/` (dashboard Next.js) | 8.057 |
| `eval/` + `bin/` | 464 |
| **Total** | **~65.000** |

Mais: **59 migrações**, **100 comandos de CLI**, e a IP travada em apenas **685 linhas** (`prompts.js` 253 + `framework.js` 432).

## 2. A conta que decide: o CrewAI substituiria 7%

CrewAI é framework de **orquestração de agentes**. O que ele substituiria é exatamente a orquestração:

| Módulo | Linhas |
|---|---:|
| `pipeline.js` | 1.188 |
| `llm-client.js` | 1.075 |
| `json-extractor.js` | 317 |
| `dimension-analyzer.js` | 282 |
| **Total** | **2.862** |

**2.862 de 41.044 = 7,0%.** Os outros 93% são determinísticos e o CrewAI não faz nada por eles:

- **`src/report/` inteiro: 0 de 14 arquivos usam LLM.** Toda a camada que o cliente vê — relatório, one-pager, anexo visual, Mapa da Casa, maturidade, moeda, princípios, completude — é código puro: 6.349 linhas.
- **`src/brain/`: 3 de 18 arquivos usam LLM.**
- Núcleo determinístico, zero LLM: detector de contradições 613 · gerador 1.830 · mapa da casa 1.032 · anexo 879 · validate 415 · rank-whatif 359 · prioritizer 336 · forget 238 · snapshot 220 · rank-pins 193 · maturidade 193 · run-ranking 196 · calibração 167 = **6.671 linhas**.

**E o assessment não usa a função principal do CrewAI.** Não há delegação, autonomia de agente, decomposição dinâmica nem negociação entre agentes: são ~40 chamadas single-shot com saída JSON estruturada, em sequência fixa e concorrência fixa. Adotar o framework pelos 7% e não usar aquilo que ele existe para fazer é o pior dos dois mundos.

## 3. O argumento matemático: a ordem importa mais que a escolha

Seja **C** o custo de portar (constante, aconteça quando acontecer), **I** o custo do primeiro run real (US$ 10–30, uma tarde), **p** a probabilidade de o run real mudar o desenho do motor e **r** a fração do porte a refazer nesse caso.

- Portar agora: `C + p·r·C`
- Voar antes, portar depois: `I + C`

Voar antes domina sempre que `p·r·C > I`. Com C em meses e I em vinte dólares, só falha se `p·r ≈ 0`.

**E p não é ~0.** Quatro itens estão em `abba pending` justamente porque se espera que mudem, e o `abba validate` declara dois portões que **devem** bloquear no dia 1. **Portar antes de voar é pagar duas vezes pela mesma incerteza.**

## 4. Custo, honestamente

Escopo: `src` + `test` = **56.596 linhas** (o `web/` fica).

O termo dominante não é digitação, é **re-prova**. A regra da casa é que toda trava falhe sob sabotagem, e as 740 foram provadas assim. Um teste não se traduz: ele codifica intenção. A régua recente é dura — **três rodadas adversariais sobre UM subsistema novo acharam 13 + 9 defeitos**, incluindo a mesma garantia falhando três vezes.

Faixa realista com assistência de IA: **3 a 6 meses da única capacidade técnica da firma**, para chegar à mesma funcionalidade, com **zero** capacidade nova visível ao cliente. Pela tabela vigente, 3 meses ≈ um Programa (R$ 185k) ou a aterrissagem do primeiro cliente.

## 5. O que é caro de re-provar

1. **SQLite cifrado em repouso** e o **certificado de deleção LGPD**, que atesta resíduo zero varrendo o esquema vivo. Artefato jurídico, não conveniência.
2. **59 migrações** com reversibilidade travada por teste.
3. Ranking congelado, confissão de falha por estágio, cerca anti-injeção por run, vocabulário único de arquétipo, moeda como rótulo, a fronteira do cliente no Mapa da Casa.
4. **740 testes sabotados um a um.**

## 6. A coluna a favor, sem maquiagem

1. **A parceria pelo Pedro** é ativo real: suporte, visibilidade, co-marketing.
2. **Um ganho técnico específico e verdadeiro:** o `re` do Python trata fronteira de palavra em Unicode nativamente. O defeito que deixou o raio-x cego em português — `\bé\b` nunca casa em JS porque `\b` é ASCII — **não existe em Python**. Vale 613 linhas.
3. Ecossistema Python para PDF, OCR e dados é mais forte.
4. **Se o Pedro assumir a manutenção do motor e trabalhar em Python**, esse é o argumento organizacional mais forte de todos, e é o único que não dá para medir a partir do código.
5. Se um dia o motor precisar ser agêntico de verdade, o CrewAI passa a ser a forma certa.

## 7. A parceria já está honrada onde ela é vista

- **`abba export <eng> --target crewai --format project`** emite um **projeto CrewAI rodável**: README, `crew.py`, `main.py`, `agents.yaml`, `tasks.yaml` e stubs de ferramenta. Cada checkpoint humano vira portão literal no `tasks.yaml`, cada integração vira stub NOMEADO que levanta exceção até alguém ligar, e o README carrega o vazamento, o número e a premissa.
- **`abba mcp <eng>`** serve um engajamento a runtimes de agente (CrewAI, Claude Code, Cursor) com sete ferramentas de leitura.

**A construção para o cliente já sai em CrewAI**, que é a decisão registrada desde 2026-07-22. O motor interno ser Node não enfraquece isso em nada.

## 8. Veredito e o que fazer em vez disso

**Não vale a pena agora.** Custa 3 a 6 meses, substitui 7% do código por um framework cuja função principal não é usada, exige re-provar 740 travas e um certificado jurídico, e entrega zero capacidade nova ao cliente — partindo de uma ferramenta que nunca leu uma empresa real.

Na ordem:

1. **O primeiro voo** (Fase 0 do [plano da águia](plano-da-aguia.md)): uma tarde, US$ 10–30, empresa que não seja cliente pagante. É o que responde "o que está faltando" com dado real.
2. **A visibilidade, sem reescrever nada:** rastro de run legível (cada chamada, o que entrou, o que voltou, o que foi descartado e por quê) mais o dashboard em `web/` que já existe e nunca foi aberto. Dias, não meses.
3. **Capturar a parceria onde ela rende:** levar ao Pedro e à CrewAI o export que já existe. Um projeto CrewAI gerado a partir de um assessment real é peça de parceria melhor que "reescrevemos nosso backend".

## Gatilhos que invertem esta resposta

- O Pedro assumir a manutenção do motor e trabalhar só em Python.
- O motor precisar virar agêntico de verdade (delegação, decomposição dinâmica).
- A parceria oferecer valor comercial material amarrado ao porte, ou exigi-lo.
- A ferramenta precisar rodar dentro da infra Python de um cliente.

## Como reproduzir cada número

```
find src -name '*.js' -o -name '*.sql' | xargs cat | wc -l      # 41.044
find test -name '*.test.js' | wc -l                              # 137
wc -l src/analysis/pipeline.js src/core/llm-client.js \
      src/analysis/json-extractor.js src/analysis/dimension-analyzer.js   # 2.862
find src/report -name '*.js' | xargs grep -l callLLM | wc -l     # 0 de 14
ls src/db/migrations/*.sql | grep -v down | wc -l                # 59
grep -c '\.command(' src/cli/index.js                            # 100
```
