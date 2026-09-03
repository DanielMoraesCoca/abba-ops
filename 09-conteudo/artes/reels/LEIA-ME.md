# Reels — o mesmo sistema visual, agora em vídeo

> **Camada:** ferramenta. Criado em 03/09 (V4k), depois da pergunta do sócio
> sobre que ferramentas dariam qualidade de agência.
>
> **A tese:** não é ferramenta nova de design. É o **mesmo sistema dos
> carrosséis** ([`../feed-lancamento/gen.py`](../feed-lancamento/gen.py))
> traduzido para vídeo com [Remotion](https://www.remotion.dev/), que renderiza
> componentes React quadro a quadro em MP4. Mesma paleta, mesma tipografia,
> mesmo grão, mesma moldura, mesma barra de progresso.

## Por que Remotion, e não CapCut

Em editor de timeline, cada Reels é montado à mão e a consistência depende de
alguém lembrar. Aqui o Reels é **código**: o 15º sai com o mesmo rigor do 1º,
de graça. É a mesma razão pela qual as 97 telas dos carrosséis saem do `gen.py`
em 8 segundos.

**Editor de timeline continua necessário** para o material gravado no celular
(os [doze roteiros](../../roteiros/banco-de-roteiros-curtos.md)). Remotion não
corta vídeo de pessoa falando; ele constrói peça tipográfica e figura de dado.

## Rodar

```bash
npm install
npx remotion studio                       # pré-visualizar e ajustar tempo
npx remotion render src/index.jsx peca-07 out/peca-07.mp4 \
  --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
```

**O `--browser-executable` não é opcional neste ambiente.** O Remotion tenta
baixar o próprio Chromium de `remotion.media`, que a rede aqui bloqueia. O
Chromium do Playwright já está instalado e serve.

**As fontes vêm do disco** (`public/fonts/`, as mesmas do `render.sh`), e
[`src/fontes.jsx`](src/fontes.jsx) segura o render até elas carregarem. Sem
isso, uma queda de rede entregaria 960 quadros desenhados em Georgia sem avisar.

`public/` não vai para o git: as fontes e a marca já vivem em
[`../feed-lancamento/fonts/`](../feed-lancamento/fonts/) e em `08-materiais/marca/`.
Copiar de lá antes de rodar.

## O que o vídeo acrescenta, e é a única coisa que justifica ele existir

**A figura acontece na frente da pessoa.** No carrossel, a distância entre o
medido e o percebido chega pronta. No Reels as duas barras crescem em sentidos
opostos e o vão de 40 pontos abre. É o mesmo dado dizendo a mesma coisa, e
funciona melhor porque a pessoa vê a distância nascer.

Fora isso: **mesmas palavras, mesma ordem, nenhum número fora do cânone.**

## Regra do movimento

**A animação nunca é o assunto.** Um vocabulário só: entra subindo 26px e
aparecendo. Números do cânone contam. Barras crescem. Nada gira, nada pisca,
nada quica. Uma casa que vende registro não faz motion de anúncio de aplicativo.

## Áudio

**Não tem, e isso é decisão em aberto.** O Instagram distribui melhor com áudio.
As opções e a regra de voz sintética estão na conversa de 02/09: voz sintética é
permitida onde a voz é entrega, proibida onde a voz é a prova. Enquanto a regra
não estiver registrada, o Reels sai mudo, que é seguro e legível.

## Ligações

[Sistema visual](../../sistema-visual-social.md) · [Duas pistas](../../duas-pistas.md) ·
[`gen.py`](../feed-lancamento/gen.py) · [Base de evidências](../../../00-identidade/base-de-evidencias.md)
