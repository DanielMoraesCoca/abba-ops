# Marca — arquivos-fonte

> **DIREÇÃO VIGENTE (v4, confirmada pelo Daniel em 2026-08-11, pendente aval do Pedro): WORDMARK LIMPO** — só a palavra ABBA em Cormorant Garamond SemiBold, espaçamento 0.12em; **sem ponto, sem tagline, sem símbolo pictórico**. Decisão tomada após 3 rodadas de exploração (rotas 1–8, estudos hebraicos, traços fluidos, ponto-fonte). **Todo o material superado foi removido desta pasta em 2026-08-11 a pedido do Daniel — o histórico completo permanece no git** (`git log -- 08-materiais/marca`).

> O kit visual da ABBA. Regras de uso no [manual de marca](manual-de-marca.md); a doutrina de cores/tipografia na [identidade visual](../../00-identidade/identidade-visual.md). Cópias finais pesadas → Drive `05 Marketing/Marca/`.

## Inventário

- **`oficial/` — OS ATIVOS VIGENTES (v4)**: avatar 1080, lockups horizontais claro/escuro, banner LinkedIn empresa (2256×382, editorial branco com a headline), capa LinkedIn pessoal (1584×396), cartão de visita frente/verso (1050×600), timbrado A4 e assinatura de e-mail. `assets-oficiais.html` é a fonte editável; em `nominais/`, os cartões (verso) e assinaturas prontos do Daniel e do Pedro (`nominais.html` é a fonte; a frente do cartão é comum: `cartao-frente.png`).
- `evento/` — kit de produção da logo para brindes: PNGs transparentes nas 3 cores, 6 combinações com fundo, PDF vetorial e `LEIA-ME.txt` com as especificações para o fornecedor.
- `grade-vitrine.html` — os 9 posts de lançamento do Instagram com conteúdo real (16 quadros; fonte editável), na tipografia da marca (v4).
- `templates-posts.html` — os 5 templates de post editáveis (instruções no topo do arquivo), na tipografia da marca e com o wordmark limpo.
- `export/` — os PNGs finais prontos para subir: 5 ativos de marca (cópias de `oficial/`) + as 16 imagens da grade. Regenerar a partir de `oficial/assets-oficiais.html` e `grade-vitrine.html` quando o texto mudar.
- `posts-lancamento.html` + `export/lancamento/` — os 3 primeiros posts (12 quadros), na voz da apresentação institucional. Legendas e estratégia em [`../../03-comercial/posts-lancamento.md`](../../03-comercial/posts-lancamento.md).
- `instagram-preview.html` + `export/instagram/` — **prévia do perfil**: como a grade fica na primeira semana, o ritmo navy/branco corrigido, o recorte 1:1 que o Instagram aplica nas capas 4:5 e um carrossel aberto no feed. As miniaturas puxam os PNGs reais — re-renderizar quando as artes mudarem.
- `fonts/` — Cormorant Garamond e EB Garamond (OFL; licença em `LICENCA.md`).
- **`abba-kit-inicial.pdf` — O DOCUMENTO (v4, 14 páginas)**: marca + regras, cores e tipografia, ativos, papelaria nominal, timbrado e kit de brindes, perfis prontos (LinkedIn empresa/pessoais/Instagram), grade-vitrine, estratégia de conteúdo, briefing para agência, checklist de lançamento e brief para designer. É o que se manda para o Pedro aprovar e o que se entrega à agência. Fonte editável: `kit-inicial-v4.html` (regenerar o PDF via Playwright `page.pdf`, 1240×1754).

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
