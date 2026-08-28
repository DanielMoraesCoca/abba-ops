# Engenharia Reversa da Máquina de Assessment — leitura executiva

**Data: 2026-08-25 · commit do dossiê técnico: `cd44014`.** A máquina foi desmontada no papel, peça por peça, por três varreduras independentes com referência de arquivo e linha. Este documento é a leitura de negócio; a anatomia técnica completa (fórmulas, variáveis, cada truncamento) vive em `assessment-brain/docs/anatomia-da-maquina.md`. Nada foi deletado; o objetivo foi entender para melhorar.

## A máquina em 10 passos (como ela realmente funciona)

1. **Entrada**: documentos e entrevistas viram texto no banco, com redação automática de CPF/CNPJ/nomes. Cada fonte carrega nível hierárquico e fase; sem nível, a fonte fica invisível para a comparação entre camadas.
2. **Enriquecimento**: cinco agentes leem TODAS as fontes e produzem mapas (entidades, contradições entre níveis, financeiro, loops de decisão). Cada mapa é rico ao nascer e é resumido de forma agressiva antes de seguir adiante: o que os estágios seguintes veem é uma projeção, não o mapa.
3. **As 25 dimensões**: cada dimensão recebe o corpus inteiro + os três resumos do enriquecimento e devolve achado, evidência e uma confiança auto-declarada (que ninguém confere). Seis rodam em paralelo; uma que falha vira linha de erro e a análise segue.
4. **Síntese**: recebe SÓ número, título, texto e confiança de cada dimensão (perde evidências, lacunas e a resposta à pergunta-chave de cada uma) e produz o resumo executivo e os movimentos estratégicos.
5. **Caça ao dinheiro**: dois passes de vazamentos (12 arquétipos, focados pelo perfil do setor) + dois de receita. Sobreposições entre vazamentos são descontadas só nos TOTAIS, nunca no ranking. O registro de receita hoje não alimenta nenhuma etapa seguinte.
6. **Recomendador**: vazamentos viram builds em lotes de 6 (ou loops em lotes de 4). Cada build recebe do modelo os números (custo, recuperação, payback) e meia dúzia de rótulos de uma palavra (moat, compounding, readiness...).
7. **Breach Score**: a fórmula é um PRODUTO de ~13 fatores. O dinheiro entra amortecido (log); os rótulos entram multiplicando. Consequência medida: os rótulos movem o ranking até 12x; a diferença entre um prêmio de $10 mil e um de $10 milhões move 1,75x. No teste travado, um build de $120k vence um de $900k por causa de duas palavras.
8. **Maturidade**: as 25 dimensões viram 6 pilares × 5 níveis + o veredito de fundação de dados. Pilares têm 2 a 8 dimensões, e a média geral é por pilar, então uma dimensão de "dados" pesa 4x uma de "operações".
9. **Superfícies**: relatório do consultor (35 seções), one-pager, anexo visual de 7 páginas, deck, MCP para agentes, manifest CrewAI, share-link. Cada uma corta e formata por conta própria.
10. **O ciclo que aprende**: outcomes medidos calibram o ranking por arquétipo (teto ±25%), e o vault deveria devolver padrões de clientes passados. Hoje o vault só grava depois de um `y` digitado no `abba feedback`, e (até esta onda) as queries de priors de solução nunca casavam por diferença de grafia da indústria.

## O que esta onda corrigiu (P0 — integridade numérica client-facing)

| # | Defeito | Dano | Status |
|---|---|---|---|
| C1 | O mesmo vazamento aparecia com DOIS valores no MESMO relatório (descontado no veredito, cru na tabela) | Cliente confere e acha inconsistência na página 1 vs 4 | ✅ corrigido |
| C2 | O "primeiro movimento" do veredito vinha de OUTRA tabela que não o plano ranqueado; capa do anexo dizia um terceiro | Três "nº 1" diferentes no mesmo pacote de entrega | ✅ corrigido |
| C3 | "Um ranking por run" era falso: relatório, one-pager e CrewAI reimplementavam o ranking com receitas diferentes; com track record, o one-pager divergiria do relatório | A falha exata que o módulo run-ranking foi criado para eliminar | ✅ corrigido + teste de consistência entre 6 superfícies |
| C4 | MCP e manifest CrewAI entregavam o número único de vazamento que o próprio relatório manda não citar quando os dois métodos de cálculo divergem | O agente/dev cita o número proibido | ✅ corrigido (banda quando divergido) |
| C5 | O vault gravava a indústria normalizada mas as queries de priors comparavam com a grafia crua: zero priors devolvidos, sempre | "Fica mais esperto a cada cliente" não funcionava na prática | ✅ corrigido |
| C6 | Build cujo modelo esqueceu a confiança levava desconto de 50% no score (o default de 0.5 era inalcançável por um bug de validação) | Ranking punia omissão de campo como se fosse risco medido | ✅ corrigido |
| C7 | Anexo dizia "confiança média das 25 leituras" mas excluía as dimensões com erro do cálculo | Número certo com legenda errada, na página do cliente | ✅ corrigido |

## Onda "A máquina confessa" (2026-08-26) — o que fechou

A tese: **o maior risco da máquina nunca foi errar, foi não conseguir avisar que errou.** Em mock esse tipo de falha é estruturalmente invisível (mock nunca trunca, nunca falha, nunca varia), então ela só apareceria no primeiro run com chave real, que custa dinheiro e credibilidade. Fechados nesta onda, do registro P1 abaixo: **1, 2, 5, 6, 7** (e a metade visível do 4).

| Item | Estado | O que passa a acontecer |
|---|---|---|
| P1.1 JSON truncado reparado em silêncio | ✅ fechado | O run confessa o reparo, com o sinal autoritativo (`stop_reason`) dos três providers, e paga **um** retry a 1,5x o teto de tokens. O relatório diz que os totais são **um piso, não uma estimativa central** |
| P1.2 Pass 2 falhando em silêncio | ✅ fechado | `pass2=FALHOU` em vez de `pass2=0` |
| P1.4 Vínculo leak↔build por índice | 🟡 metade | O lote perdido agora é REGISTRADO (nomeia os vazamentos que ficaram sem build). Exigir `leakId` explícito continua aberto, agora com evidência para dimensionar |
| P1.5 Dois vocabulários de arquétipo | ✅ fechado | Registro único; palavra fora do vocabulário vira perda declarada, nunca relabelada. **⚠️ mudou o prompt da espinha `loops`** |
| P1.6 Ranking irreproduzível | ✅ fechado | Ordem congelada no fim do run. **Consequência de negócio: `abba outcome` não reordena mais um plano já entregue** — o aprendizado serve o PRÓXIMO run. `abba report --refresh-ranking` re-tira, preservando a ordem anterior |
| P1.7 Logs fora do `forget` | ✅ fechado | Varridos e no certificado; um log sobrevivente **reprova** a atestação de resíduo zero |
| (novo) Cliente não sabia que a leitura era parcial | ✅ fechado | Uma linha de nota de escopo no one-pager, no anexo visual e no deck, logo abaixo do cabeçalho, dizendo a DIREÇÃO do erro |
| (novo) `abba validate` certificava sem olhar as falhas | ✅ fechado | Quatro travas que bloqueiam, três que avisam |

Duas coisas que valem ser ditas em voz alta para o Pedro e para qualquer cliente que pergunte:

1. **Nós preferimos declarar um limite a apresentar um número redondo.** Um run degradado passa a dizer, na primeira página que o cliente lê, que os números são um piso. Isso custa uma linha de desconforto e compra a credibilidade inteira.
2. **Degradação periférica não dispara alarme.** Declarar limite é honestidade; alarmar por ruído é ansiedade, e uma ressalva que aparece sempre é uma ressalva que ninguém lê.

Ficaram abertos, do P1: 3 (receita órfã), 8 (share-link), 9 (sinais de nível de run), 10 (enums vs dinheiro), 11 (shipped sem valor medido), 12 (autoridade do consultor no score). Os quatro últimos mexem em ranking: exigem decisão de método antes de código.

## Registro de Pontos Fracos — P1 (próxima onda: integridade e aprendizado)

1. **JSON truncado é "reparado" em silêncio**: resposta cortada pelo limite de tokens tem os colchetes fechados e parseia com sucesso — os últimos itens de listas (vazamentos, evidências, intervenções) somem sem sinal nenhum. É a perda mais consequente do motor. *Fechar: marcar reparo como warning persistido + retry com maxTokens maior.*
2. **Pass 2 de leaks e de receita falham em silêncio** (catch local, sem log, sem stage_failure): "pass2=0" indistinguível de "nada encontrado". *Fechar: recordStageFailure + aviso.*
3. **Receita é órfã**: o registro de oportunidades de receita não entra em nenhum prompt downstream (o formatador existe e ninguém o chama), e o detector nunca recebe os arquétipos prioritários do setor. *Fechar: injetar contexto de receita no recomendador + passar priorityArchetypes.*
4. **Vínculo leak↔build por índice**: quando um lote do recomendador falha ou devolve menos itens, os vínculos "resolve o vazamento X" dos builds seguintes deslocam. *Fechar: exigir leakId explícito, nunca alinhar por posição.*
5. **`solution_archetype` é texto livre com dois vocabulários** — e é a CHAVE do aprendizado por outcomes. Arquétipos de espinhas diferentes nunca agregam. *Fechar: validar contra vocabulário único.*
6. **O ranking apresentado a um cliente é irreproduzível depois**: o Breach Score nunca é persistido e seus insumos (calibração, trajetória) mudam com o tempo. *Fechar: persistir score+componentes por run.*
7. **Logs por run (com nomes de vazamentos) ficam fora do `abba forget`** e do certificado de eliminação. É o mesmo padrão do bug dos uploads já corrigido. *Fechar: incluir `~/.abba/logs/<runId>.log` na varredura e no certificado.*
8. **Share-link não é anonimizado** (expõe nomes de cliente, vazamentos e valores do one-pager) apesar de a doutrina o chamar de "anonymized". *Fechar: corrigir a doutrina (feito nesta onda) e decidir se o one-pager compartilhável ganha uma variante anonimizada de verdade.*
9. **Sinais de nível de run não conseguem reordenar nada** (multiplicam todas as intervenções igualmente): o organismo, o drag do D21 e o momentum são inertes para a ordem, ao contrário do que a doutrina descreve. *Fechar: decidir se viram fatores POR intervenção ou se a doutrina passa a dizer o que eles realmente fazem.*
10. **Enums movem 12x, dinheiro move 1,75x**: decisão de calibração do método (talvez intencional: estratégia > tamanho), mas hoje não é uma escolha documentada, é um acidente da fórmula. *Fechar: decidir e escrever a intenção; possivelmente amortecer multiplicadores ou desamortecer o prêmio. Mexe em ranking = re-validação real.*
11. **"Shipped" sem valor medido conta como vitória plena** na calibração de outcomes. *Fechar: exigir recovered_usd para win, ou peso menor.*
12. **Overrides do consultor nunca movem o ranking** e o carry entre re-runs quebra com qualquer rename de vazamento. *Fechar: decidir o peso da autoridade humana no score.*

## Registro de Pontos Fracos — P2 (backlog: contexto, caps e observabilidade)

- A cadeia de formatadores descarta silenciosamente: departamentos, fluxos de dados, centros de custo, oportunidades de automação, evidências e confiança dos leaks para o recomendador; a síntese não vê evidências, lacunas nem as respostas às perguntas-chave.
- Loop-mapper corta cada documento a 2500 caracteres sem marcador; contradições injetadas: só as 10 primeiras, cortadas a 100 caracteres.
- ~30 caps sem "quantos ficaram de fora" nas superfícies (top-10 leaks do one-pager, top-8 do deck, top-5 do why-this-ranking...).
- ~15 `JSON.parse` sem guarda no gerador do relatório: um campo corrompido derruba o documento inteiro.
- Contradições duplicam a cada resume; custo de estágio falho some da contabilidade do `--budget`; `analyzed=0` reporta run "completed".
- Prompts enviados não são gravados; `raw_response` é gravado em 7 tabelas e nenhum comando o lê; MCP não sinaliza run parcial ao agente.
- Sínteses lidas com `LIMIT 1` sem `ORDER BY` em 4 superfícies (re-síntese pode divergir entre artefatos).
- Vault: dedupe FTS5 com erro silencioso vira duplicata; anonymizer só conhece o nome do cliente (produtos/cidades/sistemas passam).
- Method Integrity: parte dos checks passa por existência de arquivo, não por atividade no engajamento; capa e contar-o-custo do anexo contam como "vivos" mesmo vazios.
- `measurabilityOk:false` (o veto duro de Goodhart) é código morto; a sonda de readiness de 20 itens nunca entra no score.

## Como usar este registro

Um item sobe de P2 para P1 quando machucar um engajamento real; um P1 vira onda de trabalho quando o custo de fechá-lo couber numa sessão. Itens que mexem em ranking ou em prompt exigem re-validação com chave real (`npm run eval` + runbook). O dossiê técnico traz o file:line de cada item daqui.

---

## Onda de 2026-08-28 — as quatro respostas de sócio

Daniel ratificou as quatro recomendações de uma vez. Todas entregues sob a mesma regra das ondas anteriores: **nenhuma mudança silenciosa na matemática do ranking**, e por isso nenhuma delas dependeu da chave real. Duas *criam* instrumento para o dia em que ela chegar.

### Fecha o P1-10 (enums movem 12x, dinheiro move 1,75x) — decidido: medir, não recalibrar

Não foi canonizado como doutrina nem recalibrado. Canonizar seria transformar em princípio um número que ninguém calibrou; recalibrar agora seria mexer no ranking sem nenhuma evidência e sem forma de saber se melhorou.

Em vez disso: `abba rank whatif <eng> --prize` imprime as duas ordens e o **breakeven** — quanto o dinheiro teria que pesar mais antes de qualquer construção se mover, e antes de o #1 mudar. No engajamento de demonstração dá 2,05x e 2,9x.

- Breakeven **alto** = o amortecimento não é o que decide aquele plano. Não há nada a corrigir.
- Breakeven **baixo** = é, e aí a calibração merece decisão explícita de sócio.

Critério de longo prazo, registrado no `abba pending`: **quantas vezes a confissão do prêmio enterrado apontou uma construção que o consultor acabou promovendo na mão.** Promover na mão repetidamente É a evidência de que o amortecimento está forte demais.

**Argumento que ficou registrado a favor da calibração atual:** uma consultoria não morre por deixar dinheiro na mesa, morre por recomendar algo que o cliente não conseguiu executar. Priorizar viabilidade sobre tamanho é convicção defensável. O que não dava para sustentar era a assimetria na intuição.

### Fecha o P1-8 (share-link não é anonimizado) — decidido: peça fictícia, não versão anonimizada

**A versão anonimizada não será construída, e essa é a decisão.** Anonimizar um relatório real é promessa impossível de cumprir: setor + faixa de faturamento + vazamento principal reidentifica uma empresa de médio porte para qualquer um do mercado, e o mercado brasileiro de médio porte é pequeno. Um teaser que vaza destrói a única coisa que uma consultoria vende.

No lugar: `abba demo` cria a **Nortex Componentes**, empresa fictícia com 25 dimensões, 6 vazamentos quantificados, 6 construções, matriz stop/start/keep e duas oportunidades de receita, renderizada pelos **geradores reais**. Nada no módulo de demonstração escreve documento: escreve linhas, e `abba report` faz o resto. Uma peça montada por renderizador próprio derivaria do produto e acabaria mostrando a um prospect algo que a ferramenta não faz mais.

Regra de uso que continua valendo: **o share-link vai só para o próprio cliente.** É divulgação de nível cliente, não amostra.

Risco que quase passou: a calibração de outcome é **firm-wide por design**, então um resultado inventado na demonstração viraria fator aplicado ao plano de um cliente real. O engajamento é marcado e as duas trilhas do ledger o ignoram.

### Fecha parte do P1-3 (receita órfã) — a decisão está escrita, ligar espera a chave

A suspeita de que faltava encanamento estava errada: o bloco de prioridades por setor **existe dos dois lados**. O que faltava era decidir quais tipos de upside são vivos em cada setor.

Escrito como proposta para **Daniel e Pedro ratificarem**: cinco por setor com o argumento de cada uma, mais o que ficou deliberadamente de fora e por quê. Ler com `abba archetypes --revenue`.

**A pergunta útil na ratificação não é "está certo?".** É: (a) qual dos excluídos deveria voltar, e (b) qual tradução para o setor está errada. Vários rótulos foram escritos pensando em software (`expansion_upsell`, `self_serve`, `speed_to_value`) e a proposta declara como cada indústria os lê.

Duas travas até lá: enquanto não ratificada, toda leitura devolve vazio (nenhum prompt muda nem por engano), e uma varredura de código pega o dia em que alguém alimentar o bloco. **Mesmo ratificada ela espera:** ligar antes do primeiro run real destrói a única linha de base capaz de dizer se o direcionamento ajudou.

### Complemento do congelamento de ranking

Congelar resolveu o problema que importava e criou um silêncio: a firma continua medindo, e nada dizia quando esse aprendizado passou a discordar de um plano já entregue. O relatório do consultor agora traz **"What we would say today"**, nomeando as construções e as posições que teriam hoje.

É a primeira frase da conversa de follow-up, e é **só do consultor**: nenhum one-pager, deck ou anexo recebe uma palavra. A ordem entregue não se move.

### Dois defeitos client-facing que só apareceram porque alguém leu um artefato inteiro

1. O one-pager imprimia **"1 are not visible to your leadership today"**.
2. O anexo visual é PT-BR de ponta a ponta **exceto** que duas páginas imprimiam o título da dimensão em inglês: *"The Knowledge Decay Rate · Power Structure & Politics"* sob um cabeçalho em português, e uma expressão em inglês em cada célula do heatmap.

Ambos corrigidos, o segundo com cobertura travada por teste para que uma dimensão futura não chegue ao cliente em inglês por omissão.

**Lição de processo:** nenhum dos dois era invisível. Ninguém tinha lido um anexo completo de ponta a ponta até a peça de demonstração forçar essa leitura. Vale repetir a leitura integral dos três artefatos depois do primeiro run com chave real.

### Limitação declarada e não maquiada

Os valores da peça de demonstração estão **em dólar**, porque a ferramenta armazena e imprime dólar. Para um prospect brasileiro isso é fraqueza real. Corrigir é funcionalidade de moeda, não truque de demonstração, e por isso está registrado aqui em vez de escondido no fixture. **Novo item P2.**
