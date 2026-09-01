// abba-um-minuto — 1 pagina: a ABBA explicada num minuto. SEM precos,
// SEM travessao. A voz do pitch: ponta vs. veia, numero combinado antes.
// Uso: anexo leve de primeiro contato, quando a apresentacao de 3 paginas e muito.
const t = require("../tema");

module.exports = function gerar(pptx) {
  const s = t.novoSlide(pptx);
  const W = t.PAG.w - 2 * t.PAG.margem;

  t.versalete(s, "ABBA · Consultoria de IA · num minuto", t.PAG.margem, 0.6);
  s.addText("Tornamos a sua empresa AI native. E provamos, com número.", {
    x: t.PAG.margem, y: 1.0, w: W, h: 1.0,
    fontFace: t.SERIF, fontSize: 30, bold: true, color: t.NAVY, lineSpacing: 36,
  });
  t.filete(s, t.PAG.margem, 2.1, 2.2, t.OURO, 1.5);

  t.corpo(s,
    "De cada dez empresas que decidiram usar IA este ano, mais de oito não vão conseguir mostrar " +
    "um número no fim (RAND: mais de 80% falham, o dobro dos projetos comuns de tecnologia). " +
    "Não é falta de tecnologia: é a IA entrando pela ponta, na mão de uma pessoa, em vez de entrar " +
    "pela veia, dentro do processo. Nós fazemos a IA rodar dentro do processo que dói, com o número " +
    "que define sucesso combinado por escrito antes, medido de fora depois.",
    t.PAG.margem, 2.35, { w: W, h: 1.15, size: 13.5, lineSpacing: 20 });

  // Os 3 caminhos
  const colW = (W - 0.8) / 3;
  const caminhos = [
    {
      rot: "1 · O Mapa de Vazamento",
      texto: "Grátis, feito de fora, com um número em reais dentro: onde estimamos que a sua operação está vazando dinheiro. É por aqui que toda conversa começa.",
    },
    {
      rot: "2 · O Programa · um ano",
      texto: "Três fases: a Prova (um caso construído e medido em seis semanas), a Construção (sistemas em produção e a sua equipe formada) e a Durabilidade (a capacidade rodando sem consultor no meio). Porta de saída limpa em cada fase.",
    },
    {
      rot: "3 · Depois do primeiro ano",
      texto: "A relação vira medição anual: operação acompanhada, conselho trimestral e o Exame Anual de IA, a maturidade re-medida e comparada ano contra ano. Quem já tem IA rodando entra pelo Conselheiro de IA.",
    },
  ];
  caminhos.forEach((c, i) => {
    const x = t.PAG.margem + i * (colW + 0.4);
    t.filete(s, x, 3.65, colW, t.OURO, 1.2);
    t.versalete(s, c.rot, x, 3.8, { w: colW, size: 10.5 });
    t.corpo(s, c.texto, x, 4.17, { w: colW, h: 1.9, size: 11.5, lineSpacing: 16.5 });
  });

  t.filete(s, t.PAG.margem, 6.15, W, t.FILETE_CLARO, 0.75);
  s.addText(
    "O que instalamos fica com você: os sistemas, as pessoas formadas e o registro do que foi decidido e medido.",
    { x: t.PAG.margem, y: 6.32, w: W, h: 0.5,
      fontFace: t.SERIF, fontSize: 13.5, italic: true, color: t.NAVY, align: "center" });
  t.rodape(s);
};
