// tema.js — a ÚNICA fonte da identidade visual dos materiais ABBA.
// Espelha o padrão editorial (08-materiais/README.md §0): branco, navy,
// versaletes dourados, filetes, serifa para títulos, sem cartões nem decoração.

const NAVY = "1B2A4A";
const OURO = "C2A35B";
const TEXTO = "33394A";
const SEC = "6E6858";
const PAPEL = "FFFFFF";
const FILETE_CLARO = "E5E0D4";

const SERIF = "Cambria";
const SANS = "Calibri";

// Página 16:9 em polegadas (PptxGenJS LAYOUT_WIDE: 13.33 x 7.5)
const PAG = { w: 13.33, h: 7.5, margem: 0.9 };

function definirLayout(pptx) {
  pptx.defineLayout({ name: "ABBA_WIDE", width: PAG.w, height: PAG.h });
  pptx.layout = "ABBA_WIDE";
  pptx.author = "ABBA Consultoria de IA";
  pptx.company = "ABBA";
}

// Versalete dourado: etiqueta em caixa alta, espaçada, dourada
function versalete(slide, texto, x, y, opts = {}) {
  slide.addText(texto.toUpperCase(), {
    x, y, w: opts.w || 6, h: 0.32,
    fontFace: SANS, fontSize: opts.size || 11, bold: true,
    color: OURO, charSpacing: 3, align: opts.align || "left",
  });
}

// Filete: linha fina horizontal
function filete(slide, x, y, w, cor = OURO, esp = 0.75) {
  slide.addShape("line", { x, y, w, h: 0, line: { color: cor, width: esp } });
}

// Título serifado
function titulo(slide, texto, x, y, opts = {}) {
  slide.addText(texto, {
    x, y, w: opts.w || PAG.w - 2 * PAG.margem, h: opts.h || 1.0,
    fontFace: SERIF, fontSize: opts.size || 30, bold: opts.bold !== false,
    color: opts.cor || NAVY, align: opts.align || "left",
    lineSpacing: opts.lineSpacing,
  });
}

// Corpo de texto
function corpo(slide, texto, x, y, opts = {}) {
  slide.addText(texto, {
    x, y, w: opts.w || PAG.w - 2 * PAG.margem, h: opts.h || 1.0,
    fontFace: opts.serif ? SERIF : SANS, fontSize: opts.size || 14,
    color: opts.cor || TEXTO, align: opts.align || "left",
    italic: opts.italic || false, lineSpacing: opts.lineSpacing || 20,
    bold: opts.bold || false,
  });
}

// Slide branco padrão com número de página discreto
function novoSlide(pptx, opts = {}) {
  const slide = pptx.addSlide();
  slide.background = { color: opts.fundo || PAPEL };
  return slide;
}

// Rodapé institucional
function rodape(slide, texto = "ABBA Consultoria de IA · contato@abbaservices.com.br") {
  slide.addText(texto, {
    x: PAG.margem, y: PAG.h - 0.5, w: PAG.w - 2 * PAG.margem, h: 0.3,
    fontFace: SANS, fontSize: 9, color: SEC, align: "center", charSpacing: 1,
  });
}

// Slide de capa navy
function capaNavy(pptx, { etiqueta, tituloTexto, sub }) {
  const slide = novoSlide(pptx, { fundo: NAVY });
  if (etiqueta) {
    slide.addText(etiqueta.toUpperCase(), {
      x: PAG.margem, y: 2.1, w: PAG.w - 2 * PAG.margem, h: 0.35,
      fontFace: SANS, fontSize: 12, bold: true, color: OURO, charSpacing: 4,
    });
  }
  slide.addText(tituloTexto, {
    x: PAG.margem, y: 2.6, w: PAG.w - 2 * PAG.margem, h: 1.8,
    fontFace: SERIF, fontSize: 44, bold: true, color: "FFFFFF",
  });
  filete(slide, PAG.margem, 4.55, 2.2, OURO, 1.5);
  if (sub) {
    slide.addText(sub, {
      x: PAG.margem, y: 4.8, w: PAG.w - 2 * PAG.margem - 2, h: 1.2,
      fontFace: SERIF, fontSize: 17, italic: true, color: "D8DCE8",
      lineSpacing: 26,
    });
  }
  return slide;
}

module.exports = {
  NAVY, OURO, TEXTO, SEC, PAPEL, FILETE_CLARO, SERIF, SANS, PAG,
  definirLayout, versalete, filete, titulo, corpo, novoSlide, rodape, capaNavy,
};
