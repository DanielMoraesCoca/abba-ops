# Kit de prompts — imagem e vídeo gerados

> **Camada:** ferramenta. Criado em 04/09 (V4p), a pedido do sócio: posts com
> foto e vídeo gerados por IA, em vez de só tipografia sobre campo chapado.
>
> **A divisão de trabalho, que é o que faz isso funcionar:** o sócio gera a
> imagem numa ferramenta de imagem; eu componho a peça em cima dela. Eu não
> gero foto nem vídeo, e nunca gerei: o que eu faço é código, layout e render.
>
> Dono: chapéu Comercial.

---

## 1. A regra que separa isto do banco de imagens

**A foto nunca é o post.** Ela é o campo sobre o qual a tipografia da casa
deita. A marca continua sendo o tipo, o filete, o folio e o rodapé; a imagem
só troca o fundo. É isso que impede a peça de virar aquela foto de sala de
reunião com sobreposição azul que toda consultoria tem.

E daí sai a decisão de arte mais importante deste kit:

> ### Objeto, nunca cena. Natureza-morta, nunca escritório.

Um cronômetro sobre fundo infinito é ABBA. Uma equipe sorrindo apontando para
um monitor é qualquer empresa do mundo. Objeto único, luz dura, sombra funda,
paleta da casa: isso tem cara de catálogo de museu, e catálogo de museu é primo
do documento de registro que vocês já são.

**Duas regras de composição:** a foto **sangra** até as bordas, porque foto
dentro de moldura lê como slide; e entra um **véu escuro** do meio para baixo,
senão o texto compete com a imagem e os dois perdem.

---

## 2. O bloco de estilo da casa

**Cola isto no fim de todo prompt, sempre igual.** É o que faz oito imagens
geradas em dias diferentes parecerem a mesma campanha.

```
editorial still life photograph, single object, seamless deep navy background,
one hard directional light from upper left, long soft shadow, restrained palette
of deep navy blue, warm brass gold and bone white only, medium format camera,
100mm macro lens, f/8, fine film grain, museum catalogue aesthetic, generous
empty space in the upper half, muted and desaturated, no text
```

**E o bloco de recusa, também sempre igual:**

```
--no people, hands, faces, robots, circuit boards, glowing neon, holograms,
blue tech overlay, HUD, futuristic interface, brain imagery, lens flare, text,
letters, logos, watermark, 3d render look, plastic shine, stock photo smile
```

---

## 3. Os oito objetos, um por peça

Cada objeto sai da doutrina de vocês. Nenhum é decoração.

| Peça | Objeto | O prompt (antes do bloco de estilo) |
|---|---|---|
| **07** METR | cronômetro | `a vintage mechanical stopwatch lying on its side, second hand caught mid sweep in slight motion blur, brass casing, glass slightly scratched` |
| **08** RAND | pastas caídas | `a stack of manila project folders, most of them toppled over and spilling, one still standing upright` |
| **09** DORA | amplificador | `a single brass amplifier knob turned all the way up, macro, worn metal, scale markings engraved` |
| **10** Wharton | mostrador zerado | `an analogue pressure gauge, glass face, needle resting exactly at zero, brass bezel, dust on the glass` |
| **03** recusas | caneta e papel | `a fountain pen resting on a printed document, ink still wet on a signature line, one corner of the page lifted` |
| **11** régua | carimbo | `a wooden rubber stamp lying beside an open ink pad, a stamped sheet of paper underneath, ink slightly smudged` |
| **14** Conselheiro | cadeira vazia | `a single empty wooden chair at the head of a long bare table, other chairs out of focus behind it` |
| **04** assessment | documento marcado | `a thick bound report, many paper tabs sticking out of the pages, one page held half open` |

**Formato:** peça `--ar 4:5` para o feed e `--ar 9:16` para o Reels. Gere as
duas proporções do mesmo objeto, senão o corte estraga o enquadramento.

---

## 4. O que reprovar, e é para reprovar sem dó

Gerar é barato. **Aceitar imagem mediana é o que faz o feed parecer amador.**

1. **Tem pessoa, mão ou rosto?** Reprova. Gente gerada por IA é o sinal mais
   rápido de "isso foi feito por máquina", e é o que mata a credibilidade de
   uma casa que vende prova.
2. **Tem letra em qualquer lugar?** Reprova. A tipografia é minha, e letra
   gerada sai torta.
3. **Tem brilho azul, holograma, circuito ou cérebro?** Reprova. É o clichê que
   o [sistema visual](sistema-visual-social.md) existe para evitar.
4. **A metade de cima está ocupada?** Reprova. Ali entra o folio e o respiro.
5. **A cor fugiu da paleta?** Reprova ou corrija na ferramenta. Verde, roxo e
   ciano não existem nesta casa.
6. **Parece render 3D, com aquele brilho de plástico?** Reprova. Tem que
   parecer fotografado, com poeira, arranhão e desgaste.

**Gere quatro de cada e me mande as quatro.** A que você descartaria costuma
ser a que compõe melhor com o texto, porque a foto boa sozinha compete com a
manchete.

---

## 5. Vídeo

Mesmos objetos, mesma paleta, movimento mínimo. **Nada de câmera voando.**

```
slow push in on [o objeto], almost imperceptible camera movement, shallow depth
of field, one hard light from upper left, dust floating in the beam, 5 seconds,
locked off tripod feel
```

O corte, a tipografia e a trilha entram no Remotion, que já está montado em
[`artes/reels/`](artes/reels/LEIA-ME.md). O vídeo gerado vira **camada de
fundo**, nunca o Reels inteiro.

---

## 6. Como isso chega até mim

1. Você gera na ferramenta que preferir. Para foto de objeto, hoje as mais
   fortes são Nano Banana Pro, Midjourney e Seedream.
2. **Me manda os arquivos crus, sem selecionar e sem editar.**
3. Eu componho: recorto no formato, aplico o véu, deito a tipografia, rodo a
   régua e devolvo o PNG pronto de postar.

**O molde já existe** em `artes/foto/`, com a área da foto, o véu e a mancha de
texto no lugar certo.

---

## Ligações

[Sistema visual](sistema-visual-social.md) · [Registro alto](campanha-registro-alto.md) ·
[Plataforma de marca](plataforma-de-marca.md) · [Reels](artes/reels/LEIA-ME.md)
