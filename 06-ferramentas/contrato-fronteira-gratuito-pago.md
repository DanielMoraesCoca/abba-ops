# Contrato de Fronteira — Assessment Gratuito × Avaliação Paga

Uma página para responder de vez: **como o gratuito se separa do pago, o que um entrega ao outro, e de quem é cada pendência.** Complementa a [ferramenta-avaliacao.md](ferramenta-avaliacao.md) (estado e promessas) e a [spec de alinhamento web](spec-alinhamento-assessment-web.md) (execução dev) sem repeti-las.

## O mapa em uma frase

O **gratuito** (`assessment.abbaservices.com.br`, deploy do Pedro) é o método olhando a empresa **de fora**, por informação pública: é degustação e porta de entrada. A **Avaliação de Prontidão** (assessment-brain, R$ 45k) é o mesmo método olhando **de dentro**, com dados reais e gente real: é o produto. Um alimenta o outro; nenhum substitui o outro.

## O que o PAGO entrega que o gratuito não pode entregar

A resposta curta para qualquer prospect (e para nós mesmos):

| | Gratuito (Análise ABBA) | Pago (Avaliação de Prontidão) |
|---|---|---|
| Fonte | Informação pública + curadoria dos sócios | Documentos internos + entrevistas do conselho à linha de frente |
| Vozes ouvidas | Nenhuma de dentro | 6 níveis hierárquicos (13 a 21 conversas) |
| O diferencial técnico | Hipóteses a verificar | **Detector de contradições entre níveis**: o que o CEO diz × o que a linha de frente vive; os gaps são o diagnóstico |
| Números | Faixa em R$ com premissas públicas | Vazamentos quantificados com evidência interna rastreável (todo número com premissa citada) |
| Profundidade | Mapa de Vazamento + hipóteses | 25 dimensões, maturidade em 6 pilares, veredito de fundação de dados, plano priorizado com TCO honesto |
| Método humano | Nenhum compromisso | Kickoff, [imersão em campo](../04-entrega/protocolo-de-imersao.md), workshop de 3h, **sessão de validação de achados** |
| Depois | Termina no PDF | Vira ciclo vivo: decisões, revisões, portal de acompanhamento (contrato de handoff já existe entre as ferramentas, versão 0.1.0) |

Frase-ponte oficial (do [modelo de serviço](../00-identidade/modelo-de-servico.md)): *"isto foi feito de fora — imagine com os dados de dentro."*

## O que o GRATUITO entrega ao funil (e como recebemos)

1. **O lead.** Toda análise gerada no site = lead novo no estágio [01](../02-jornada-do-cliente/01-visitante-e-lead.md). Notificação chega em `comercial@`. **Triagem em 24h, dono: Daniel** — aplicar o teste de alvo de 5+1 perguntas ([alvo](../00-identidade/alvo.md)), registrar no [pipeline](../03-comercial/pipeline-modelo.md), responder com convite para a conversa T1. Lead sem placar não avança.
2. **O relatório público como ponto de partida do pago.** Fechado o contrato, o relatório gratuito é ingerido no engajamento como pesquisa externa: `abba ingest <relatorio> --level external --phase 0`. A avaliação paga começa com as hipóteses do gratuito já no contexto e as confirma ou derruba com dados internos — nada se refaz do zero.
3. **A reunião muda de natureza.** Lead do site JÁ tem o relatório; o T2 vira **apresentação comentada** + ponte para o que só a avaliação profunda revela ([pauta 2](../03-comercial/pautas-de-reuniao.md)). Nunca reapresentar o PDF como novidade.

## Regras de fronteira (o que NUNCA cruza)

- Dados internos de cliente **nunca** alimentam o gratuito: o gratuito é público por definição, e a mistura quebraria a promessa das duas pontas.
- O gratuito **nunca se cobra** e nunca promete o que só o pago faz (causa dos vazamentos, veredito de fundação, plano priorizado) — [escada](../03-comercial/escada-abba.md): degrau 0 aponta onde vaza, não prova a causa.
- O relatório completo do gratuito é entregue **na apresentação ao vivo**, nunca por download ([spec §4](spec-alinhamento-assessment-web.md)) — enquanto o gating não existe, vale a regra de contorno da [jornada 02](../02-jornada-do-cliente/02-diagnostico-gratuito.md).

## Direção de longo prazo (norte, não trabalho desta onda)

A decisão registrada no plano mestre do portal: o futuro mini-assessment self-serve deve nascer **do pipeline do assessment-brain** (mesma engine, versão reduzida), não como terceira ferramenta. Quando esse dia chegar, este contrato de fronteira vira o contrato entre dois modos da MESMA ferramenta — e a regra "dados internos nunca alimentam o gratuito" continua valendo letra por letra.

## Pendências nomeadas (dono: Pedro, chapéu Tecnologia)

Nenhuma delas é trabalho do assessment-brain ou dos docs; são o que falta na ponta do site:

| # | Pendência | Referência |
|---|---|---|
| P1 | **Trazer o site público para o repositório** (hoje só existe no deploy) — regra permanente: produção só roda código versionado | [R16](../05-interno/registro-de-riscos.md) |
| P2 | **Implementar o gating**: teaser público de 5–8 páginas; relatório completo só na apresentação | [spec §4](spec-alinhamento-assessment-web.md) |
| P3 | **Captura de e-mail corporativo + notificação a `comercial@`** a cada análise gerada (sem isso, o funil do gratuito não existe de fato) | [spec §3](spec-alinhamento-assessment-web.md) |

Item de pauta da [reunião semanal dos sócios](../05-interno/pauta-reuniao-semanal.md) até as três fecharem.

## Backlog registrado (fora desta onda, decisão consciente)

Conectores de ingestão (Drive/e-mail), parser de PPTX/EML, metadados por arquivo em lote, e o próprio mini-assessment self-serve — anotados aqui para não se perderem, adiados por custo × valor.
