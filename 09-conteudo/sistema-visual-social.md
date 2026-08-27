# Sistema Visual do Social — o documento de registro

> **Camada:** ferramenta. Estende a [identidade visual](../00-identidade/identidade-visual.md)
> para o formato quadrado/vertical das redes, que os modelos-mestres de Office
> não cobrem. Criado por decisão do sócio (2026-08-27): *"posts com cara de que
> uma agência profissional de marketing fez"*, com o feed anterior arquivado.
>
> **Fonte executável:** [`artes/feed-lancamento/gen.py`](artes/feed-lancamento/gen.py) —
> o CSS e os arquétipos moram lá. Peça nova nasce dele, nunca do zero.
>
> Dono: chapéu Comercial.

---

## 1. O diagnóstico do que estava errado

O feed anterior não era feio — era **repetitivo de um jeito que denuncia
automação**. Um único molde ("olho em caixa alta · frase grande em serifa com
uma palavra dourada · fiada · parágrafo curto") repetido em todos os cards. Esse
molde é o padrão de fábrica das ferramentas de card, e o leitor de LinkedIn e
Instagram já aprendeu a reconhecê-lo — ele lê como *conteúdo gerado*, não como
*material de empresa*.

O que separa peça de agência de peça de template não é a fonte nem a cor. São
três coisas:

1. **Variedade de arquétipos** — uma peça de verdade tem capa, tabela, diagrama,
   nota de margem, fecho. Não seis cópias do mesmo card.
2. **Estrutura que significa alguma coisa** — número de folio, referência de
   seção, nota de rodapé com fonte. Devem *codificar* informação, não decorar.
3. **Contenção do acento** — dourado em fiada, marca e no máximo uma palavra por
   tela. Dourado em tudo vira Canva.

## 2. A direção: documento de registro

A ABBA vende **prova**: registro, métrica combinada antes, trilha auditável,
"a gente anota tudo e prova". O mundo visual autêntico disso não é o cartaz
motivacional — é o **documento de registro**: o dossiê técnico, o extrato, o
parecer.

Daí vêm os elementos, e cada um deles é uma afirmação sobre a empresa:

| Elemento | O que ele diz |
|---|---|
| **Folio** (`ABBA` · `PEÇA 02`) no topo | Isto é um documento numerado, não um story |
| **Referência de seção** (`§2 · 04/09`) no pé | Existe uma ordem, e ela é rastreável |
| **Fiadas de 1px** delimitando a mancha | Rigor de composição, não moldura decorativa |
| **Rótulos em monoespaçada** com entreletra | Nome de campo de formulário — o vocabulário do registro |
| **Nota de rodapé com marca** (`—`, `→`) | A doutrina da fonte na frase, virada em objeto gráfico |
| **Numerais tabulares** | Número que se alinha em coluna é número que se confere |

A monoespaçada não é enfeite de startup: ela é a face dos **rótulos e dos
números**, e existe porque a doutrina desta casa literalmente roda como código
(`abba revise`). Ela nunca aparece em texto corrido.

## 3. Os seis arquétipos

Nenhuma peça usa o mesmo dois cards seguidos — é essa alternância que faz o
carrossel parecer editado por gente.

| # | Arquétipo | Para quê | Onde ver |
|---|---|---|---|
| **A** | **Capa** — olho, título grande, fiada curta, entrada | Abrir a peça | Peça 01, tela 1 |
| **B** | **Razão** — tabela com chave romana e corpo | Enumerar sem virar lista de bullet | Peça 03, telas 2–4 |
| **C** | **Etapas** — número, título, descritor | Sequência com ordem que importa | Peça 04, tela 3 |
| **D** | **Marginália** — texto principal com nota na margem, sobre papel | Declarar o limite, a ressalva, o contraponto | Peça 04, tela 5 |
| **E** | **Diagrama** — SVG de fiada fina | Mostrar mecanismo, não afirmar mecanismo | Peça 02, tela 2 |
| **F** | **Fecho** — pergunta + nota com o contato | Terminar com próximo passo, nunca com isca | todas, última tela |

**O arquétipo D é o mais importante da casa.** É onde o material declara o
próprio limite — a marca visível do [manifesto](../00-identidade/manifesto.md).
Nenhum concorrente publica a ressalva no meio do próprio carrossel.

## 4. Tipografia e cor

| Papel | Face | Uso |
|---|---|---|
| Títulos | **Newsreader** | Só título. Itálico dourado para a palavra de ênfase — no máximo uma por tela |
| Corpo | **Source Serif 4** | Já em uso nos materiais HTML da casa. Continuidade |
| Rótulos, folio, números | **IBM Plex Mono** | Nome de campo, referência, numeral. Nunca texto corrido |

Substitutas de sistema declaradas em todas as pilhas — a exportação em PNG não
embute fonte de servidor externo, então a substituta tem que ter métrica
próxima.

**Cor:** navy `#1B2A4A` e dourado `#C2A35B` da
[identidade visual](../00-identidade/identidade-visual.md), sem alteração.

> **As duas cores derivadas foram registradas** na
> [identidade visual](../00-identidade/identidade-visual.md) em 2026-08-27
> (decisão V4b), com uso **restrito ao social**: papel `#F2F4F7` (fundo claro
> alternado) e ardósia clara `#C3CAD8` (corpo sobre navy). Ambas são tiradas do
> próprio navy, não são cores novas de fato. O papel é azulado de propósito: o
> creme quente é o clichê visual do momento e denuncia peça gerada.

## 4b. Transição: as três técnicas

O que separa um carrossel montado de um carrossel **editado** é o que acontece
entre as telas. Um leitor arrasta o dedo e o material tem que responder ao gesto.

| # | Técnica | Como funciona | O que ela resolve |
|---|---|---|---|
| **1** | **Barra de progresso** | A fiada do topo carrega um segmento dourado que avança proporcionalmente a cada tela: 1/7, 2/7, 3/7 | O leitor sabe onde está e quanto falta. Carrossel sem isso é abandonado no meio |
| **2** | **Marca de continuidade** | Um traço dourado de 56px sai pela **borda direita** de uma tela e reaparece na **mesma altura** na borda esquerda da tela seguinte, descendo a cada passo | No arraste, o traço parece atravessar entre as telas. É o truque clássico de continuidade entre painéis, e é o que faz a peça parecer desenhada como conjunto |
| **3** | **Ritmo de fundo** | Navy e papel alternam num compasso **escolhido**, não aleatório. O papel marca sempre a tela de pausa, de ressalva ou de limite declarado | Sete telas do mesmo fundo cansam. E a alternância passa a significar alguma coisa em vez de decorar |

A técnica 2 é a que mais muda a percepção e é invisível quando bem-feita: ninguém
comenta, mas a peça deixa de parecer um monte de cards soltos.

**Regra:** a barra e a marca são desenhadas pela função `page(i, n, ...)` do
gerador, a partir da posição da tela. Nunca posicionar à mão, porque uma tela
fora de compasso quebra as três técnicas de uma vez.

## 4c. O texto: sem travessão

Nenhuma peça usa travessão (`—` ou `–`). Vírgula, dois-pontos ou ponto; em lista,
ponto médio `·`. É decisão do sócio (V3v, reafirmada e estendida a todo material
externo em V4a-b), e a régua
[v1.5.0](../06-ferramentas/regua-do-revisor.md) bloqueia. Motivo: lê como texto
gerado por máquina.

O gerador tem uma trava no fim que falha se sobrar travessão em qualquer tela.

## 4d. A marca

O logo real entra na **última tela de toda peça**, a 190px. O arquivo
[`abba-logo.png`](../08-materiais/marca/abba-logo.png) tem 614×674, o que o
mantém nítido até cerca de 300px numa tela de 1080. **Acima disso ele fica
macio**, então o sistema foi desenhado para caber no que o ativo aguenta em vez
de pedir um ativo novo. Se um dia existir a marca em vetor, a mesma tela aceita
sem mudança.

## 5. Margem de segurança (a regra que o feed antigo quebrava)

Formato **1080×1350**. Toda mancha de texto vive entre **y=196 e y=1182** e
entre **x=104 e x=976** — ou seja, **dentro do recorte 1:1** que o Instagram
aplica na miniatura da grade do perfil.

Consequência prática: a primeira tela de todo carrossel continua legível quando
alguém abre o perfil e vê só o quadrado. É onde a maior parte das pessoas vê o
post pela primeira vez, e é onde o feed anterior perdia a primeira letra do olho.

## 6. Como produzir a próxima peça

1. Escolher a pauta no [banco](banco-de-pautas.md) e o molde em [formatos](formatos.md).
2. Escrever a peça em [`posts/`](posts/) — texto, legenda, regras de publicação.
3. Acrescentar as telas em [`artes/feed-lancamento/gen.py`](artes/feed-lancamento/gen.py),
   escolhendo entre os seis arquétipos. **Não criar arquétipo novo sem registrar aqui.**
4. Rodar a régua no arquivo da peça e o checklist humano do [motor](motor-de-conteudo.md).
5. Exportar as telas em PNG e publicar.

---

## Ligações

[Identidade visual](../00-identidade/identidade-visual.md) ·
[Formatos](formatos.md) · [Motor](motor-de-conteudo.md) ·
[Estratégia](estrategia-de-conteudo.md) ·
[Kit de presença](../03-comercial/kit-de-presenca.md) — a fonte das falas
