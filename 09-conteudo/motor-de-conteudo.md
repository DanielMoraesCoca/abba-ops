# O Motor de Conteúdo — como sai peça todo dia

> **Camada:** processo. Formato fixo da casa: Dono · Entrada · Checklist ·
> Saída · Ferramentas · Prazo-alvo. Executável por **uma pessoa em uma
> sentada**, que é a única forma de sobreviver ao terceiro mês.
>
> **A tese deste documento:** empresa nova não morre de falta de ideia de post.
> Morre de fricção — o dia em que produzir custa 40 minutos de decisão é o dia
> em que não se publica, e a partir daí a conta esfria. O motor existe para que
> o custo de publicar seja **aprovar, não criar**.
>
> Dono: chapéu Comercial (aprovação) · Assistente de IA (produção).

---

## A divisão de trabalho, em uma linha

**A IA produz; o sócio aprova e publica; o cliente nunca vê rascunho.** É o
[modelo centauro](../00-identidade/manifesto.md) aplicado ao próprio marketing —
seria incoerente vender "a IA gera, o humano assina" e publicar texto que
ninguém assinou.

| Etapa | Quem | Custo por peça |
|---|---|---|
| Pauta, pesquisa, redação, arte, roteiro | Assistente | 0 min de sócio |
| Conferência na régua + aprovação | Sócio | **~4 min** |
| Publicação + primeira hora de comentários | Sócio | ~15 min |
| Gravação (só peças P5) | Sócio | ~10 min/semana |

Se um dia qualquer custar mais que isso, o motor está quebrado e é isso que se
conserta na revisão de segunda — não a criatividade.

---

## As duas trilhas

### Trilha A — Sem rosto (4 peças/semana)

Pilares [P1 Prova · P2 Bastidor · P3 Método · P4 Brasil](estrategia-de-conteudo.md#4-os-cinco-pilares).
**Entregues prontas para copiar e colar.** O sócio não escreve nada.

Cada peça chega como um arquivo em [`posts/`](posts/) contendo: o texto final,
a especificação da arte (ou o HTML do carrossel), o destino, o horário-alvo, a
fonte no repo e a linha de aprovação.

### Trilha B — Com rosto (1 peça/semana)

Pilar [P5 Fronteira](estrategia-de-conteudo.md#4-os-cinco-pilares). O sócio
grava; a IA entrega **roteiro cronometrado, plano de captação e legenda** em
[`roteiros/`](roteiros/). Nunca "grave algo sobre X" — sempre falas
cronometradas, porque roteiro vago é o que faz o vídeo não ser gravado.

**Regra de acúmulo:** grava-se em bloco. Uma sessão de 30 minutos por semana
produz 3–4 vídeos; a semana ruim consome o estoque em vez de furar a
consistência. **Estoque mínimo: 2 vídeos.** Abaixo disso, a gravação vira
pendência de sócio na reunião de segunda.

---

## A semana

| Dia | LinkedIn (perfil do sócio) | Instagram | Pilar |
|---|---|---|---|
| **Seg** | — (só comentários) | Story: bastidor da semana | — |
| **Ter** | Peça 1 · 9h30 | Carrossel reciclado da peça da semana anterior | P1 Prova |
| **Qua** | Peça 2 · 9h30 | Story | P3 Método |
| **Qui** | Peça 3 · 9h30 | Reel (recorte do vídeo P5) | P2 Bastidor |
| **Sex** | Peça 4 · 8h30 | Story | P4 Brasil |
| **Sáb/Dom** | — | — | — |
| **1x/semana** (encaixa em qualquer dia) | Vídeo P5 | Reel completo | P5 Fronteira |

**Por que 4–5 e não 7.** As medições públicas de 2026 convergem: de 2 a 5
publicações por semana é a faixa de melhor retorno por peça, e acima de 5 o
engajamento por peça cai de forma mensurável. Mais decisivo: contas que
publicam 3x por semana **com resposta ativa nos comentários** superam contas
que publicam diariamente sem isso, por uma margem larga. **O diário deste plano
é a atividade, não a publicação** — e a atividade que faltava não era postar,
era conversar.

> **Se o sócio quiser 7 dias:** é defensável e o banco de pautas comporta, mas
> só depois de 6 semanas com 4/semana entregues sem falha. Consistência primeiro,
> volume depois. Furar 7 na terceira semana custa mais do que 4 nunca furados.

### O ritual diário do sócio (25 min, sempre no mesmo horário)

1. **Abrir o arquivo do dia** em `posts/`, ler, conferir a régua, publicar. *(5 min)*
2. **Comentar em 5 posts** de gente do alvo ou do ecossistema — comentário com
   substância, que acrescenta um dado ou discorda com educação. Nunca "ótimo
   post!". *(10 min)*
3. **Responder todo comentário no post da véspera**, um por um, com pergunta de
   volta. Conversa que continua é o que o algoritmo lê como relevância — e é
   onde a reunião nasce. *(10 min)*

O passo 2 é o mais negligenciado e o de maior retorno para uma conta sem
público: comentário bom em post alheio é o único jeito de aparecer para a
audiência de outra pessoa **sem prospecção fria** — o que mantém a doutrina do
[plano de ataque](../03-comercial/plano-de-ataque.md) §6 intacta.

---

## O ciclo semanal (a conversa deste chat)

| Quando | O quê | Saída |
|---|---|---|
| **Segunda, na reunião de sócios** | Revisão de 10 min: o que publicou, o que pegou, o placar, o estoque de vídeo | Decisões registradas |
| **Segunda, neste chat** | O sócio traz o combustível da semana (ver abaixo). A IA devolve **as 5 peças da semana prontas** | 4 arquivos em `posts/` + 1 em `roteiros/` |
| **Durante a semana** | Ajustes, pautas reativas (notícia, visita, reunião), reciclagem do que pegou | Peças extras |
| **Sexta** | Números da semana no placar | Linha no histórico |

### O combustível — o que o sócio traz toda segunda

A qualidade da semana é decidida aqui, e custa 5 minutos. Sem isso, a IA
produz do repositório (o que funciona, mas se repete no terceiro mês). Com
isso, o conteúdo é insubstituível porque ninguém mais tem esses fatos.

- **Uma coisa que aconteceu** — reunião, visita, objeção que ouviu, pergunta
  que um cliente fez, algo que quebrou num protótipo
- **Um número novo** que apareceu (do cliente, de um teste, de uma medição)
- **Uma opinião** que ele defendeu em voz alta essa semana e daria uma boa briga
- **Onde ele vai estar** — visita, evento, viagem (vira peça presencial)

> Uma frase dita numa reunião real vale mais que dez pautas tiradas de
> tendência. **"O head de TI da Brasal disse que procura quem já pegou empresa
> bagunçada e saiu com caso de sucesso"** é um post inteiro, e nenhum
> concorrente tem essa frase.

---

## O gate de publicação — a régua roda no post

Nenhuma peça sai sem passar. O escopo da
[régua do revisor](../06-ferramentas/regua-do-revisor.md) **já inclui posts**;
não é regra nova, é a regra da casa aplicada onde ela ainda não estava rodando.

```bash
abba revise 09-conteudo/posts/AAAA-MM-DD-slug.md
```

Achado `block` = a peça não sai. Publicar com `--force` é uma decisão com nome,
e vai para o [registro de decisões](../05-interno/registro-de-decisoes.md).

**Checklist humano de 5 minutos** (o que a régua determinística não pega):

- [ ] **De qual peça esta herda?** Tem gancho para trás com a palavra exata já
      usada, e gancho para frente? Contradiz alguma linha do razão de
      continuidade? ([linha editorial](linha-editorial.md) §5 e §8)
- [ ] **Mira uma das quatro cabeças?** Se não mira nenhuma, é decorativa — não sai
- [ ] **Todo número tem a fonte na frase** e está no cânone da [base de evidências](../00-identidade/base-de-evidencias.md)?
- [ ] **A primeira frase diz o que não dá para fazer de dentro**, ou pelo menos não disputa a cadeira do diretor de IA? ([posicionamento](../00-identidade/posicionamento.md) regra 1)
- [ ] **Tem número, prazo ou nome** — em vez de adjetivo? ([tom](../00-identidade/manifesto.md#o-tom))
- [ ] **Declara o próprio limite** onde couber? (é a marca visível da casa)
- [ ] **Nenhum dado de cliente** sem aprovação nominal por escrito?
- [ ] **Link fora do corpo** (vai no primeiro comentário)?
- [ ] O sócio **assinaria isso em voz alta numa sala com um cético técnico**?

O último item é o gate real. Se a resposta hesitar, a peça volta.

---

## Reciclagem — uma peça, cinco vidas

Nada é produzido uma vez só. É assim que 4 peças/semana viram presença em dois
canais sem dobrar o trabalho.

| Origem | Vira | Onde | Quando |
|---|---|---|---|
| Post de texto que pegou (>3x a mediana) | Carrossel de 8 telas | LinkedIn + Instagram | 2 semanas depois |
| Vídeo P5 | 2 reels de 45s + 3 stories | Instagram | Mesma semana |
| Carrossel | PDF de 1 página | Anexo de e-mail de follow-up | Sob demanda |
| 4 peças de um pilar | Seção de newsletter | LinkedIn (a partir do mês 3) | Mensal |
| Peça que gerou pergunta boa nos comentários | Post novo respondendo a pergunta | LinkedIn | Semana seguinte |

**A regra da mediana:** toda peça que passar de 3x a mediana de visualizações
do perfil entra automaticamente na fila de reciclagem. Não se discute — o
mercado já votou.

---

## Onde os arquivos moram

```
09-conteudo/
  estrategia-de-conteudo.md    # por que e para quem
  motor-de-conteudo.md         # este arquivo — como
  formatos.md                  # os moldes
  banco-de-pautas.md           # o combustível (60 pautas ranqueadas)
  plano-90-dias.md             # o calendário e as fases
  posts/AAAA-MM-DD-slug.md     # peça pronta, uma por arquivo
  roteiros/AAAA-MM-DD-slug.md  # roteiro de vídeo cronometrado
```

**Convenção:** ASCII sem acento, kebab-case, data na frente para a listagem ler
como calendário — igual ao resto do repositório. Toda peça publicada ganha a
linha `Publicado em:` com data e o número de 48h, para o placar sair do git e
não da memória.

---

## Prazo-alvo

| Item | Prazo |
|---|---|
| Peças da semana entregues | Segunda até 12h |
| Aprovação do sócio | Segunda até 18h |
| Peça reativa (notícia, visita) | 4h do pedido |
| Números no placar | Sexta |

---

## Ligações

[Estratégia](estrategia-de-conteudo.md) · [Formatos](formatos.md) ·
[Banco de pautas](banco-de-pautas.md) · [Plano de 90 dias](plano-90-dias.md) ·
[Régua do revisor](../06-ferramentas/regua-do-revisor.md) ·
[Ritual semanal](../04-entrega/ritual-semanal.md)
