# Manual de Marca — ABBA (v1, uso digital)

> **O que é:** as regras mínimas para qualquer pessoa (sócio, freelancer ou agência) produzir uma peça digital que pareça da ABBA. Complementa a [identidade visual](../../00-identidade/identidade-visual.md) (documentos impressos/Office) — este manual cobre o **digital**: redes sociais, avatares, banners. Em conflito, a identidade visual manda.
>
> Dono: chapéu Comercial (Daniel). Evolução profissional da marca (naming de estúdio, ajuste óptico do símbolo) pode vir depois — estes arquivos são a **v1 utilizável**, e já substituem o PNG único.

## O símbolo

O cérebro-grafo: dois hemisférios de nós conectados, em dourado. É a marca-símbolo desde o início ([abba-logo.png](abba-logo.png), preservado como original). Agora existe **vetorizado**, em variações:

| Arquivo | Uso |
|---|---|
| `abba-logo-simbolo.svg` | Símbolo dourado, fundo transparente — sobre branco ou navy |
| `abba-logo-simbolo-branco.svg` | Monocromático branco — sobre foto escura ou navy quando o dourado competir |
| `abba-logo-simbolo-navy.svg` | Monocromático navy — impressão 1 cor, fundos claros |
| `abba-logo-horizontal-claro.svg` | Símbolo + ABBA + "Consultoria de IA" — cabeçalhos sobre fundo claro |
| `abba-logo-horizontal-escuro.svg` | Idem, sobre navy — rodapé de slide escuro, assinatura de vídeo |
| `abba-logo-empilhado-claro.svg` / `-escuro.svg` | Capa de documento, certificado, encerramento de deck |
| `abba-avatar-1080.svg` | Avatar 1:1 — LinkedIn, Instagram, WhatsApp Business (o símbolo centrado com margem para recorte circular) |
| `abba-banner-linkedin-empresa.svg` | Capa da página LinkedIn (2256×382 = 1128×191 @2x), com a headline canônica |
| `abba-capa-linkedin-pessoal.svg` | Capa de perfil pessoal dos sócios (1584×396), sem headline — o perfil fala por si |

Regras do símbolo:
1. Nunca recolorir fora das três versões (dourado, branco, navy). Nunca gradiente.
2. Margem de respiro mínima: a altura de um nó grande em volta de todo o logo.
3. Sobre foto: só a versão branca, e só se a foto for escura e calma.
4. O wordmark "ABBA" sem símbolo é permitido em contexto onde o símbolo já apareceu (rodapé de carrossel).

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
- **Digital/social (este manual):** serifada **Cambria → Georgia → Times New Roman** (pilha com fallback universal; Cambria é a serifada do padrão editorial). Para web futura: **Source Serif 4** (livre, Google Fonts) é a equivalente aprovada — já é a serifada do design system do portal.
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
