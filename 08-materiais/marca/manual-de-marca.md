# Manual de Marca — ABBA (v2, uso digital)

> **O que é:** as regras mínimas para qualquer pessoa (sócio, freelancer ou agência) produzir uma peça digital que pareça da ABBA. Complementa a [identidade visual](../../00-identidade/identidade-visual.md) (documentos impressos/Office) — este manual cobre o **digital**: redes sociais, avatares, banners. Em conflito, a identidade visual manda.
>
> Dono: chapéu Comercial (Daniel). Refino óptico por designer (kerning fino) pode vir depois — estes arquivos são a **versão utilizável e vigente**.

## A marca

**Wordmark limpo (v4, 2026-08-11 — decisão do Daniel, pendente aval do Pedro):** só a palavra **ABBA** em Cormorant Garamond SemiBold (600), espaçamento de 12% entre letras (0.12em). Sem ponto, sem tagline, sem símbolo pictórico — o padrão das consultorias premium. O nome é um palíndromo; a tipografia carrega a marca sozinha.

Arquivos vigentes (pasta [`oficial/`](oficial/)):

| Arquivo | Uso |
|---|---|
| `oficial/avatar.png` | Avatar 1080×1080 navy — LinkedIn, Instagram, WhatsApp Business |
| `oficial/horiz-claro.png` / `horiz-escuro.png` | Lockup horizontal sobre branco / sobre navy |
| `oficial/banner.png` | Capa da página LinkedIn empresa (2256×382), editorial branco com a headline |
| `oficial/capa.png` | Capa de perfil pessoal dos sócios (1584×396), navy |
| `oficial/cartao-frente.png` + `nominais/cartao-*.png` | Cartão de visita 9×5 (frente comum + verso nominal) |
| `oficial/nominais/ass-*.png` | Assinaturas de e-mail nominais |
| `oficial/timbrado.png` | Papel timbrado A4 |
| `evento/` | Kit de produção para brindes: PNGs transparentes nas 3 cores, combinações e PDF vetorial |

Regras da marca:
1. Nunca recolorir fora das três cores (navy, dourado, branco). Nunca gradiente, sombra ou contorno.
2. Nunca esticar, inclinar ou espelhar.
3. Margem de respiro mínima: metade da altura do A em volta de toda a marca.
4. Sobre foto: só branco ou dourado, e só se a foto for escura e calma.
5. A fonte da marca é Cormorant Garamond 600 com 0.12em — não recompor em outra fonte.

## Paleta (a mesma da identidade visual — nenhuma cor nova)

| Papel | Hex | No digital |
|---|---|---|
| Navy | `#1B2A4A` | Fundo de capa e cards escuros; texto-título sobre claro |
| Dourado | `#C2A35B` | Eyebrows, filetes, números de destaque, o símbolo. **Com parcimônia — nunca corpo de texto** |
| Ardósia | `#5A6472` | Texto secundário sobre claro |
| Gelo | `#E8E8E8` | Divisores, fundos de bloco |
| Petróleo | `#2E8B9A` | Links e elementos interativos (raro) |
| Branco | `#FFFFFF` | Fundo padrão de slide de conteúdo |

Contraste (verificado): navy sobre branco 12,6:1 ✅ · branco sobre navy 12,6:1 ✅ · ardósia sobre branco 5,9:1 ✅ · **dourado sobre branco 2,3:1 e dourado sobre navy 5,4:1** → dourado como TEXTO só sobre navy, e só em eyebrow/destaque grande (≥30px). Sobre branco, dourado é elemento gráfico (filete, número gigante), nunca texto corrido.

## Tipografia

- **Office/impresso:** Aptos / Aptos Display (já definido na identidade visual).
- **Digital/social (este manual):** display e marca em **Cormorant Garamond** (OFL, em [`fonts/`](fonts/)); corpo de texto em **EB Garamond**. Fallback quando as fontes não estiverem instaladas: Georgia. Para web futura: as mesmas, via Google Fonts.
- Sans-serif de apoio (legendas de UI, se precisar): Inter ou a do sistema.
- Versaletes dourados com letter-spacing largo (≥ 0.3em) para eyebrows — a assinatura tipográfica do padrão editorial.

## Templates de post

[`templates-posts.html`](templates-posts.html) — 5 quadros prontos para editar e capturar:

| # | Template | Formato | Uso |
|---|---|---|---|
| 1 | Capa de carrossel | 1080×1350 (4:5) | Primeiro slide — navy, headline com termo-chave em dourado |
| 2 | Slide interno | 1080×1350 | Slides 2..N-1 — branco, uma ideia por slide |
| 3 | Slide-CTA | 1080×1350 | Último slide — fecho + convite único (Mapa de Vazamento) |
| 4 | Card de citação | 1080×1080 | Frase do manifesto ou dos sócios — navy |
| 5 | Card de número | 1080×1080 | Um dado com premissa citada — branco |

Como exportar: abrir no navegador e capturar cada `<div class="frame">` em zoom 100%, ou usar o script de captura descrito no [README](README.md) da pasta.

Regras editoriais dos posts (herdam o [manifesto](../../00-identidade/manifesto.md) e o [padrão editorial](../README.md#0-o-padrão-editorial-decisão-do-sócio-2026-08-05)):
1. **Sem emoji.** Sem "jornada". Sem superlativo sem número. Sem "revolucionário/disruptivo/inovador".
2. Todo número publicado tem premissa ou fonte no próprio card.
3. Rodapé sempre: `ABBA · abbaservices.com.br`.
4. A conclusão vem antes da justificativa — o primeiro slide entrega, os internos sustentam.
5. Sem preços. Sem "25 dimensões" (vira "mergulho profundo, do conselho à linha de frente").
6. Clientes: **nenhum nome real** até existir caso publicável aprovado no [molde](../../05-interno/caso-publicavel-modelo.md).

## Fotografia (quando houver)

Herdada da política do portal: documental/editorial, nunca banco de imagem encenado (aperto de mão, laptop genérico); paleta fria que não brigue com navy+dourado; contexto brasileiro quando natural; sócios em ambiente real de trabalho. Fotos de rosto dos sócios: pendência dos sócios (ver [marketing-redes-sociais](../../03-comercial/marketing-redes-sociais.md)).
