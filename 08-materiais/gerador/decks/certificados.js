// certificados-modelo — 2 certificados (participante e Campeao), {{campos}}.
// Regenerado na V5: mesmo conteudo consagrado, SEM travessao.
// Nota R9: a licenca CrewAI do Campeao e condicionada a via de contratacao
// ativa; nao prometer em proposta antes do setup (o certificado e emitido
// na graduacao, quando a condicao ja se resolveu).
const t = require("../tema");

function certificado(pptx, { titulo, corpoTexto }) {
  const s = t.novoSlide(pptx);
  const W = t.PAG.w - 2 * t.PAG.margem;
  // moldura dupla discreta
  s.addShape("rect", { x: 0.35, y: 0.35, w: t.PAG.w - 0.7, h: t.PAG.h - 0.7, line: { color: t.OURO, width: 1.5 }, fill: { type: "none" } });
  s.addShape("rect", { x: 0.5, y: 0.5, w: t.PAG.w - 1.0, h: t.PAG.h - 1.0, line: { color: t.FILETE_CLARO, width: 0.75 }, fill: { type: "none" } });

  s.addText("ABBA · Consultoria de IA", {
    x: t.PAG.margem, y: 0.95, w: W, h: 0.35, align: "center",
    fontFace: t.SANS, fontSize: 12, bold: true, color: t.OURO, charSpacing: 4,
  });
  s.addText(titulo, {
    x: t.PAG.margem, y: 1.55, w: W, h: 0.9, align: "center",
    fontFace: t.SERIF, fontSize: 36, bold: true, color: t.NAVY,
  });
  t.filete(s, t.PAG.w / 2 - 1.1, 2.6, 2.2, t.OURO, 1.5);
  s.addText("{{NOME DO PARTICIPANTE}}", {
    x: t.PAG.margem, y: 2.95, w: W, h: 0.75, align: "center",
    fontFace: t.SERIF, fontSize: 30, italic: true, color: t.TEXTO,
  });
  s.addText(corpoTexto, {
    x: t.PAG.margem + 1.2, y: 3.85, w: W - 2.4, h: 1.5, align: "center",
    fontFace: t.SANS, fontSize: 14, color: t.TEXTO, lineSpacing: 22,
  });
  s.addText("{{Cidade}}, {{data}}   ·   Verificação: ABBA-CERT-{{ANO}}-{{NUM}}", {
    x: t.PAG.margem, y: 5.45, w: W, h: 0.35, align: "center",
    fontFace: t.SANS, fontSize: 11, color: t.SEC,
  });
  // assinaturas
  const colW = 3.4;
  [["{{Sócio A}} · ABBA", t.PAG.w / 2 - colW - 0.5], ["{{Sócio B}} · ABBA", t.PAG.w / 2 + 0.5]].forEach(([nome, x]) => {
    t.filete(s, x, 6.35, colW, t.SEC, 0.75);
    s.addText(nome, { x, y: 6.45, w: colW, h: 0.3, align: "center", fontFace: t.SANS, fontSize: 11, color: t.TEXTO });
  });
}

module.exports = function gerar(pptx) {
  certificado(pptx, {
    titulo: "Certificado de Conclusão",
    corpoTexto:
      "concluiu o programa de capacitação em Inteligência Artificial da ABBA ({{fase/trilha}}, na " +
      "{{NOME_DA_EMPRESA}}), demonstrando domínio prático das três perguntas: o que parar, o que " +
      "começar e o que ainda é essencialmente humano.",
  });
  certificado(pptx, {
    titulo: "Certificação de Campeão ABBA",
    corpoTexto:
      "graduou-se Campeão de IA da {{NOME_DA_EMPRESA}}: completou a trilha integral, construiu " +
      "soluções próprias e assume o papel de multiplicador, com licença CrewAI de 12 meses " +
      "concedida pela ABBA.",
  });
};
