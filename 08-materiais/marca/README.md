# Marca — arquivos-fonte

> **DIREÇÃO VIGENTE (v3, 2026-08-09, pendente aval do Pedro): WORDMARK "ponto-fonte"** — ABBA em Cormorant Garamond com um ponto dourado sobre o eixo central do palíndromo; sem símbolo pictórico (padrão das consultorias premium: McKinsey/BCG são só tipografia). Fontes e ativos em [`wordmark/`](wordmark/); o documento consolidado é [`abba-kit-inicial.pdf`](abba-kit-inicial.pdf). Os símbolos anteriores (fonte v2 e cérebro) permanecem arquivados abaixo como histórico de exploração.

> O kit visual da ABBA. Regras de uso no [manual de marca](manual-de-marca.md); a doutrina de cores/tipografia na [identidade visual](../../00-identidade/identidade-visual.md). Cópias finais pesadas → Drive `05 Marketing/Marca/`.

## Inventário

- `abba-logo.png` — o símbolo original, cérebro-grafo (histórico; preservar, não usar em material novo).
- `abba-logo-*.svg` — a família vetorizada v2, símbolo "a fonte": nó-origem na base, jorros que sobem e se ramificam em rede (3 cores, horizontal e empilhado em claro/escuro). Gerada por script determinístico; para variações novas, editar os SVGs diretamente ou refazer o gerador.
- `abba-avatar-1080.svg`, `abba-banner-linkedin-empresa.svg`, `abba-capa-linkedin-pessoal.svg` — ativos de rede social prontos.
- `templates-posts.html` — os 5 templates de post editáveis (instruções no topo do arquivo).
- `grade-vitrine.html` — os 9 posts de lançamento do Instagram com conteúdo real (16 quadros; fonte editável).
- `export/` — os PNGs finais prontos para subir: 6 ativos de marca + as 16 imagens da grade. Regenerar a partir dos SVGs/HTML quando o texto mudar.
- `abba-kit-social.pdf` — kit da era "símbolo fonte" (histórico).
- **`abba-kit-inicial.pdf` — O DOCUMENTO: kit inicial consolidado da ABBA** (marca wordmark + ativos + perfis + grade com legendas + estratégia + checklist + brief para designer + fontes da pesquisa). É o que se manda para o Pedro aprovar e o que se entrega à agência.
- `rotas/` — **estudo de marca em 8 rotas (agência, 2 rodadas)**: monograma A·, nascente geométrica, o selo e "a herança do nome" (selo com o raio da fonte; variante aleph) — cada uma com racional e mockups (avatar, cartão, timbrado, tela). `abba-estudo-marca.pdf` é a apresentação de 11 páginas para os sócios decidirem; 3 finalistas registrados: Rota 4 "o raio", Rota 6 "o abraço", Rota 7 "o manancial"; aleph como variação de colecionador. Rodada 3: `hebraico.html` + `heb-pai.png`/`heb-fonte.png` — estudo tipográfico das palavras hebraicas ligadas ao nome (אבא e מקור), 10 tratamentos cada, para avaliar uma marca de herança caligráfica. Pendente: escolha dos sócios.
- `wordmark/` — a marca vigente: `wm_assets.html` (ativos), `wordmarks.html` (5 estudos), `fonts/` (OFL) e `export/` com os PNGs (avatar, lockups, banner, capa, estudos).
- `variante-cerebro/` — o MESMO kit inteiro com o símbolo cérebro: **vetorização fiel do abba-logo.png original** (68 nós e 112 conexões extraídos por análise de imagem; desvio médio de posição 0,1%), com as correções de um parecer de design independente: aresta perdida restaurada, linhas em dourado a 50% de opacidade (recuam; nós lideram — a hierarquia do original), traço engrossado para sobreviver em 48px, marca a 65% do canvas no avatar. SVGs, grade, `export/` com os 22 PNGs e `abba-kit-social-cerebro.pdf`. Existe para os sócios compararem e decidirem o símbolo definitivo; a decisão deve ser registrada aqui quando tomada.

## Como exportar PNG

**Sem ferramenta:** abrir o SVG/HTML no navegador em zoom 100% e capturar (print do quadro). Suficiente para avatar e posts.

**Com Node + Playwright (pixel-perfect):**

```js
// export.js — node export.js arquivo.svg saida.png
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [svgPath, out] = process.argv.slice(2);
  const svg = fs.readFileSync(svgPath, 'utf8');
  const [, w, h] = svg.match(/width="(\d+)" height="(\d+)"/).map(Number);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  await page.setContent(`<body style="margin:0">${svg}</body>`);
  await page.screenshot({ path: out });
  await browser.close();
})();
```

Para os templates de post: abrir `templates-posts.html` com Playwright e usar `page.locator('#t1-capa').screenshot(...)` (ids `t1-capa` … `t5-numero`).

## Regras rápidas

1. Nunca recolorir fora de dourado/branco/navy; nunca gradiente; nunca esticar.
2. Avatar e capas de rede: usar os arquivos prontos — não recompor à mão.
3. O nome do arquivo diz o fundo: `-claro` = usar sobre branco/gelo; `-escuro` = já traz o navy.
