# Princípios do método de assessment

> **Uso interno.** Esta é a camada de sabedoria que fundamenta o método de avaliação da ABBA. Regra de uso público, coerente com a [decisão de não registrar religiosidade na marca](marca-e-nomenclatura.md): em material de cliente e de marketing, o princípio aparece como **sabedoria universal, sem citação de versículo**; a fonte fica aqui, para os sócios. No anexo visual, por exemplo, a página "Contar o custo" abre com a pergunta da torre sem referência — quem conhece, reconhece; quem não conhece, entende do mesmo jeito.

## Por que esta camada existe

O método da ABBA não nasceu de um framework de consultoria — nasceu da convicção de que sabedoria antiga sobre construir, contar, inspecionar e discernir continua sendo o melhor antídoto para o padrão de falha documentado do mercado (~80% dos projetos de IA falham, e as causas dominantes são de fundação, não de algoritmo — fontes no [doc de pesquisa](../05-interno/pesquisa-assessment-mercado.md)). Cada princípio abaixo tem um lugar onde **vira produto**: não é decoração, é arquitetura.

## Os princípios e onde cada um vira produto

| Princípio | Fonte | Onde vira produto |
|---|---|---|
| **Contar o custo antes de construir a torre** | Lc 14:28-30 | Seção "Contar o custo" no relatório e página 6 do anexo visual: TCO honesto (construir + operar + manter + pessoas) ANTES do GO/NO-GO. O mercado inteiro esconde o custo de manutenção até depois da assinatura; nós mostramos antes. Também é o argumento de venda dos 80%. |
| **Inspecionar os muros à noite, antes de anunciar** | Ne 2:11-15 | O scout / Mapa de Vazamento: diagnóstico silencioso por informação pública, feito antes da primeira reunião. Neemias examinou os muros de noite e só depois falou com os líderes. |
| **Na multidão de conselheiros há segurança** | Pv 15:22 / 11:14 | Entrevistas multi-nível (conselho → linha de frente), seção de contradições entre níveis, red-team da análise. Uma só voz nunca é a verdade da empresa. |
| **Conhece o estado das tuas ovelhas** | Pv 27:23 | Veredito de Fundação de Dados (FRÁGIL / PARCIAL / PRONTA): antes de propor a obra, saber com precisão o estado do rebanho — os dados, os sistemas, as pessoas. |
| **Coração que discerne (o pedido de Salomão)** | 1Rs 3:9 | Priorização por Breach Score: o problema mais valioso primeiro. Salomão não pediu mais recursos, pediu discernimento para julgar o que importa. |
| **Os 7 anos de José: prever, quantificar, armazenar** | Gn 41 | Roadmap em 3 horizontes com buffers de risco: agir agora no que paga rápido, preparar o que vem, esperar o tempo certo do que ainda não amadureceu. |
| **Com sabedoria se edifica a casa** | Pv 24:3-4 | Os 3 pés da instalação (tecnologia / processos / pessoas). A casa se edifica com sabedoria, se firma com entendimento e se enche com conhecimento — nunca só com ferramenta. |

## A melhoria real derivada (não decoração)

**"Contar o custo"** é o diferencial defensável desta camada: uma seção do entregável que mostra o custo total honesto de cada intervenção — incluindo operação, manutenção e pessoas — antes de o cliente decidir. É coerente com "prova, não impressão", é rara no mercado (a dor nº 1 documentada de quem contrata consultoria de IA é descobrir o custo real depois), e é diretamente pregável na conversa de venda sem citar fonte nenhuma.

## A doutrina agora é executável (2026-08-20)

Os princípios deixaram de ser só documento: viraram o registro `src/report/principles.js` no assessment-brain — **15 princípios em 3 camadas** (7 bíblicos acima + 4 de campo da [reunião Rafael/Brasal](../05-interno/reuniao-rafael-brasal-2026-08-18.md) + 4 de mercado da análise da Sophy Works), cada um com verificação determinística de onde vive no produto.

**Como conferir que tudo está dentro da ferramenta:**
- `abba principles` — imprime a doutrina (redação universal, fontes internas nos ids)
- `abba principles "<engajamento>"` — tabela de conformidade contra o último run real (15/15 vivos no ensaio mock de 20/08)
- O relatório do consultor ganhou a seção **Method Integrity**: os princípios checados contra o próprio relatório
- `test/unit/principles.test.js` trava no CI: remover a seção/página/módulo que sustenta um princípio quebra a suíte

**Os 8 princípios novos (campo + mercado):**

| id no código | Princípio (redação universal) | Fonte | Onde vira produto |
|---|---|---|---|
| `dados-e-processos` | A fundação que falha nunca é só o dado: é o processo que o produz | Rafael/Brasal #1 | Veredito de fundação "dados e processos" |
| `area-disposta-primeiro` | O humano no loop ou ajuda ou vira detrator: começar pela área mais disposta | Rafael/Brasal #2 | Willing-area gate no plano de adoção + tags no roadmap |
| `adaptar-ao-processo-real` | Solução de prateleira quebra no processo real | Rafael/Brasal #3 (Spring Globo) | Loops de decisão reais mapeados |
| `imersao-e-licoes` | O que se vende é a imersão e as lições acumuladas | Rafael/Brasal #4 | Priors do vault citados no relatório |
| `sistema-vivo-nao-slide` | A análise não morre como documento: entra no ciclo vivo de decisão | Sophy (Decision Stack "living system") | **`abba decision seed`**: intervenções ranqueadas viram decisões no cérebro, com trigger/outcome/Brier |
| `primeira-hipotese-mais-rapida` | A primeira hipótese raramente é a melhor: é só a mais rápida | Sophy | Nota no plano + `abba red-team` |
| `por-que-este-trabalho-existe` | Toda construção carrega por que existe e se continua sendo a aposta certa | Sophy ("why does this work exist") | Decisões semeadas carregam vazamento + número + premissa |
| `transparencia-de-custo` | O custo do próprio trabalho é visível até o centavo | Sophy (token transparency) | Custo do run no rodapé + reliability |

Os 7 bíblicos da tabela acima têm ids: `contar-o-custo`, `inspecionar-de-noite`, `multidao-de-conselheiros`, `conhece-tuas-ovelhas`, `coracao-que-discerne`, `sete-anos-de-jose`, `sabedoria-edifica-a-casa`.

## Regras de aplicação

1. **Interno + sutil** (decisão do Daniel, 2026-08-19): a camada existe no método e nos documentos internos; em material público aparece só como sabedoria universal.
2. Nenhum princípio substitui evidência: o princípio orienta ONDE olhar; o número que sai tem premissa citável ou não sai.
3. Se um princípio e um dado real entrarem em conflito, o dado vence — e o conflito vira aprendizado registrado.
