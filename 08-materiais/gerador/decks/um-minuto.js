// abba-um-minuto — 1 pagina: a ABBA explicada num minuto. SEM precos.
// Uso: anexo leve de primeiro contato, quando a apresentacao de 3 paginas e muito.
const t = require("../tema");

module.exports = function gerar(pptx) {
  const s = t.novoSlide(pptx);
  const W = t.PAG.w - 2 * t.PAG.margem;

  t.versalete(s, "ABBA · Consultoria de IA · num minuto", t.PAG.margem, 0.6);
  s.addText("Tornamos a sua empresa AI native — e provamos, com número.", {
    x: t.PAG.margem, y: 1.0, w: W, h: 1.0,
    fontFace: t.SERIF, fontSize: 30, bold: true, color: t.NAVY, lineSpacing: 36,
  });
  t.filete(s, t.PAG.margem, 2.1, 2.2, t.OURO, 1.5);

  t.corpo(s,
    "Mais de 80% dos projetos de IA falham — o dobro dos projetos comuns de tecnologia — e a " +
    "causa número um é começar sem combinar o que seria dar certo (RAND). Nós trabalhamos " +
    "exatamente aí: cada caso nasce com a métrica combinada por escrito, é medido por " +
    "terceiro e assinado por gente da sua empresa.",
    t.PAG.margem, 2.35, { w: W, h: 1.05, size: 13.5, lineSpacing: 20 });

  // Os 3 caminhos
  const colW = (W - 0.8) / 3;
  const caminhos = [
    {
      rot: "1 · O Mapa de Vazamento",
      texto: "Grátis, feito de fora, com um número em reais dentro: onde estimamos que a sua operação está vazando dinheiro. É por aqui que toda conversa começa.",
    },
    {
      rot: "2 · O Programa — um ano",
      texto: "Três fases: a Prova (um caso construído e medido em seis semanas), a Construção (sistemas em produção + a sua equipe formada) e a Durabilidade (a capacidade rodando sem consultor no meio). Porta de saída limpa em cada fase.",
    },
    {
      rot: "3 · Depois do primeiro ano",
      texto: "A relação vira medição anual: operação acompanhada, conselho trimestral e o Exame Anual de IA — a maturidade re-medida e comparada ano contra ano. Quem já tem IA rodando entra pelo Conselheiro de IA.",
    },
  ];
  caminhos.forEach((c, i) => {
    const x = t.PAG.margem + i * (colW + 0.4);
    t.filete(s, x, 3.6, colW, t.OURO, 1.2);
    t.versalete(s, c.rot, x, 3.75, { w: colW, size: 10.5 });
    t.corpo(s, c.texto, x, 4.12, { w: colW, h: 1.9, size: 11.5, lineSpacing: 16.5 });
  });

  t.filete(s, t.PAG.margem, 6.15, W, t.FILETE_CLARO, 0.75);
  s.addText(
    "O que instalamos fica com você: os sistemas, as pessoas formadas e o registro do que foi decidido e medido.",
    { x: t.PAG.margem, y: 6.32, w: W, h: 0.5,
      fontFace: t.SERIF, fontSize: 13.5, italic: true, color: t.NAVY, align: "center" });
  t.rodape(s);
};
