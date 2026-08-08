# Marca — arquivos-fonte

> O kit visual da ABBA. Regras de uso no [manual de marca](manual-de-marca.md); a doutrina de cores/tipografia na [identidade visual](../../00-identidade/identidade-visual.md). Cópias finais pesadas → Drive `05 Marketing/Marca/`.

## Inventário

- `abba-logo.png` — o símbolo original (histórico; preservar).
- `abba-logo-*.svg` — a família vetorizada v1 (símbolo em 3 cores, horizontal e empilhado em claro/escuro). Gerada por script determinístico; a fonte do gerador está no histórico da sessão de criação — para variações novas, editar os SVGs diretamente ou refazer o gerador.
- `abba-avatar-1080.svg`, `abba-banner-linkedin-empresa.svg`, `abba-capa-linkedin-pessoal.svg` — ativos de rede social prontos.
- `templates-posts.html` — os 5 templates de post editáveis (instruções no topo do arquivo).

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
