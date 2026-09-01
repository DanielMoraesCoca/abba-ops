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

## 4e. Logo de parceiro

Regra criada na [V4i](../05-interno/registro-de-decisoes.md), quando as logos
oficiais Microsoft e CrewAI entraram na peça 05. Vale para qualquer marca de
terceiro que apareça no feed.

**O arquivo é o mesmo do material de envio.** As duas logos foram tiradas do
[`abba-apresentacao.pptx`](../08-materiais/modelos/abba-apresentacao.pptx), onde
já estavam aprovadas desde a [V3o](../05-interno/registro-de-decisoes.md), e
vivem ao lado das artes como `logo-microsoft.png` e `logo-crewai.png`. **Não se
baixa uma versão nova para o social.** Um material só, um arquivo só.

| Regra | Por quê |
|---|---|
| **Campo branco com folga em volta**, a classe `.plate`: caixa de 420×152, fundo `#FFFFFF`, fio de 1px em ardósia clara | É o que a guia de marca de cada parceiro exige, e resolve o fato de a logo da Microsoft não ter fundo transparente. Sem a placa, ela apareceria como um retângulo branco acidental sobre o papel |
| **Sem recorte, sem recolorir, sem distorcer.** Altura fixa, largura automática | Marca de terceiro não é elemento gráfico do nosso sistema. Ela entra como está |
| **As placas de uma mesma peça têm a mesma caixa e a mesma altura na tela** | No swipe a placa fica parada e só a marca troca. É a [terceira técnica de transição](#4b-transição-as-três-técnicas) aplicada a logo, e é o que faz duas telas lerem como um par em vez de dois tratamentos |
| **Só em tela de papel, nunca no navy** | Sobre o fundo escuro a marca perderia contraste, e a única saída seria alterá-la, o que a regra acima proíbe |

**O que a logo não autoriza a dizer.** A presença da marca não muda uma vírgula
do texto: continua valendo a redação da
[V3i](../05-interno/registro-de-decisoes.md), *"sua equipe usa ferramentas dos
nossos parceiros durante a capacitação"*, sem prometer licença
([risco R9](../05-interno/registro-de-riscos.md)).

## 4f. A capa cheia, e por que a regra antiga virou o problema

> Reescrito em 01/09 (V4j), depois de o sócio olhar a grade do perfil com cinco
> peças no ar e dizer que estava sem graça. Ele tinha razão, e a causa era
> técnica.

**O que aconteceu.** O §5 abaixo mandava toda mancha de texto viver dentro do
**recorte 1:1**, entre y=196 e y=1182, porque era assim que o Instagram cortava
a miniatura da grade. **O Instagram mudou.** A grade do perfil hoje mostra a
**altura inteira** do cartão 4:5 e corta cerca de 3% de cada lado.

A consequência é direta: a capa antiga punha tudo no terço de cima e deixava
**mais da metade do cartão vazia**, e essa metade vazia, que antes era cortada,
passou a aparecer em toda miniatura. Cinco peças no ar viraram cinco retângulos
navy com um pouco de texto no topo. Não era falta de ideia, era uma régua velha.

**A capa agora ancora embaixo.** Rótulo no topo, vazio no meio, e a frase grande
fechando o cartão contra o filete de rodapé.

| | Antes | Agora |
|---|---|---|
| Manchete | 80px, fixa | **132 · 112 · 94 · 78px**, escolhida pelo tamanho da frase (`.c1` a `.c4`) |
| Posição | topo | ancorada no rodapé (`.stage.cover`) |
| Mancha ocupada | ~40% da altura | ~70% |

## 4g. Ritmo da grade: a peça não se julga sozinha

A grade mostra **três por linha**. Uma peça pode ser ótima sozinha e a grade
continuar morta, que era o caso. Por isso o fundo passou a ser decidido no nível
da **sequência**, não da peça:

| Peça | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fundo | navy | papel | navy | **ouro** | navy | papel | navy | **ouro** | navy | papel | navy | **ouro** | navy | papel |

O ciclo tem período 4 e a grade tem 3 colunas, então **nenhuma linha sai só de
um valor**, e isso vale de qualquer ponto da sequência, o que importa porque o
Instagram mostra do mais novo para o mais antigo e a ordem de leitura vira ao
contrário.

**Terceiro fundo: campo dourado.** Navy e papel davam só claro e escuro. O
dourado da marca como campo cheio dá o terceiro valor. Tipo em navy sobre ouro
(5,9:1) e **acento por itálico, nunca por cor**, porque nada claro tem contraste
suficiente sobre o dourado.

## 4h. Grão

Fundo chapado lê como slide. Um grão de ruído a 6% sobre o navy e a 42% em
multiplicação sobre o papel faz o cartão ler como impresso. É textura sem
imagem, que é o único jeito de dar matéria a este sistema sem cair na imagem
genérica de IA que a [duas-pistas](duas-pistas.md) proíbe.

## 4i. Número herói

Quando a manchete **é** um número do cânone, o número vira a imagem da capa:
300px, no display, com a fonte na sequência. Vale para as peças 07 (19%),
08 (mais de 80%) e 10 (72%). Quando o cânone diz "mais de", a linha mono
`.heropre` carrega o "mais de", porque **arredondar em favor do impacto seria
inventar um número**.

## 4j. Figura

Onde existe dado real, entra figura, e ela segue a régua de gráfico:

- **a forma vem do trabalho do dado.** A da peça 07 é polaridade (uma perda
  medida contra um ganho percebido), então são duas barras divergindo de uma
  linha de zero, e não duas barras lado a lado
- **as cores saem do sistema** e passam pelo validador antes de entrar. O par
  em uso, `#D8BE7C` medido × `#7C88A2` percebido, dá separação 22,5 em visão
  normal, 20,7 em protanopia e 20,8 em tritanopia, e as duas ficam acima de
  3:1 sobre o navy
- **todo texto usa tinta do sistema, nunca a cor da série**, e cada barra
  carrega o próprio rótulo colado nela: a identidade nunca depende só da cor
- **respiro de superfície** entre marcas adjacentes, senão duas barras que se
  encontram no zero leem como um bloco só

Próximas figuras candidatas, todas com número já no cânone: peça 08 (RAND),
peça 09 (DORA) e peça 10 (Wharton).

## 5. Margem de segurança (a regra que o feed antigo quebrava)

Formato **1080×1350**. Toda mancha de texto vive entre **y=196 e y=1182** e
entre **x=104 e x=976**.

> **Corrigido em 01/09 (V4j).** Esta margem existia porque o Instagram cortava a
> miniatura da grade em **1:1**. Não corta mais: a grade mostra a **altura
> inteira** e tira cerca de **3% de cada lado**. A margem lateral de 104px cobre
> esse corte com folga, então ela fica. **A margem vertical deixou de ser um
> recorte e passou a ser só respiro**, e foi por confundir as duas coisas que as
> capas nasceram com metade do cartão vazia. Ver [4f](#4f-a-capa-cheia-e-por-que-a-regra-antiga-virou-o-problema).

Consequência prática: a primeira tela de todo carrossel é vista quase inteira
quando alguém abre o perfil. É onde a maior parte das pessoas vê o post pela
primeira vez.

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
