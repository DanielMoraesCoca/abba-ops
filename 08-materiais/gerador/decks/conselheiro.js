// deck-conselheiro — o Conselheiro de IA em 6 slides (substitui o
// servico-7-conselheiro-deck retirado na V5). SEM precos, SEM travessao.
// Com o parecer de arbitragem real (empresa preservada). So para quem JA
// tem IA rodando.
const t = require("../tema");

function base(pptx, etiqueta, tit, sub) {
  const s = t.novoSlide(pptx);
  t.versalete(s, etiqueta, t.PAG.margem, 0.65);
  s.addText(tit, {
    x: t.PAG.margem, y: 1.05, w: t.PAG.w - 2 * t.PAG.margem, h: 1.0,
    fontFace: t.SERIF, fontSize: 27, bold: true, color: t.NAVY, lineSpacing: 33,
  });
  if (sub) t.corpo(s, sub, t.PAG.margem, 2.1, { w: t.PAG.w - 2 * t.PAG.margem, h: 0.75, size: 13, cor: t.SEC, lineSpacing: 20 });
  t.rodape(s);
  return s;
}

module.exports = function gerar(pptx, assets) {
  const W = t.PAG.w - 2 * t.PAG.margem;

  // 1 — capa
  t.capaNavy(pptx, {
    etiqueta: "ABBA · Conselheiro de IA",
    tituloTexto: "A cadeira de IA do seu\nlado da mesa.",
    sub: "Direção estratégica fracionária para quem já tem IA rodando. Sem o custo, nem o conflito, de mais um diretor em folha.",
  });

  // 2 — para quem
  let s = base(pptx, "Para quem é", "Você já construiu. A pergunta agora é outra.",
    "O Conselheiro é para a empresa que já tem IA em produção, e por isso enfrenta as perguntas que ferramenta nenhuma responde:");
  const pergs = [
    "O que priorizar no próximo trimestre, e o que recusar?",
    "Este fornecedor entrega o que promete? A que preço isso se compara?",
    "O que já rodou de fato mudou algum número, ou só virou demonstração?",
    "Quem, da diretoria, sustenta essas respostas com registro, não com memória?",
  ];
  pergs.forEach((p, i) => {
    const y = 2.95 + i * 0.85;
    t.filete(s, t.PAG.margem, y, 0.5, t.OURO, 1.2);
    t.corpo(s, p, t.PAG.margem + 0.75, y - 0.12, { w: W - 0.75, h: 0.7, size: 14.5, serif: true, lineSpacing: 20 });
  });

  // 3 — o que e
  s = base(pptx, "O que é", "Presença de direção, em fração. Com tudo por escrito.");
  const itens = [
    ["Na diretoria", "presença recorrente nas reuniões de direção: a pauta de IA preparada, defendida e registrada."],
    ["Roadmap vivo", "a fila de oportunidades mantida e re-ranqueada conforme os números chegam. Nunca um PDF parado."],
    ["Arbitragem de fornecedores", "parecer por escrito sobre cada proposta que chega à mesa: o que é real, o que é caro, o que é risco."],
    ["Memória de decisão", "cada decisão registrada com a expectativa declarada antes e o resultado medido depois. Imutável por construção."],
  ];
  itens.forEach((it, i) => {
    const y = 2.3 + i * 1.1;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, it[0], t.PAG.margem, y + 0.12, { w: 3.1, size: 10.5 });
    t.corpo(s, it[1], t.PAG.margem + 3.3, y + 0.1, { w: W - 3.3, h: 0.9, size: 13, lineSpacing: 19 });
  });

  // 4 — o parecer real
  s = base(pptx, "Como se parece", "Um parecer de arbitragem de verdade.",
    "Página real de um parecer entregue (empresa preservada): a proposta do fornecedor decomposta, o preço comparado, a recomendação assinada.");
  s.addImage({ path: assets.fotos("conselheiro--parecer-arbitragem.jpg"), x: t.PAG.w / 2 - 1.38, y: 2.9, w: 2.76, h: 3.9 });

  // 5 — por que terceiro
  s = base(pptx, "Por que um terceiro", "Nenhum time interno pode ser a própria prova.");
  t.corpo(s,
    "Quem executa não pode atestar o próprio resultado. É a razão pela qual empresas com um ótimo CFO " +
    "ainda contratam quem verifique as contas de fora. O Conselheiro traz exatamente isso para a IA: " +
    "a expectativa declarada antes e imutável, o resultado medido e assinado por uma pessoa nomeada da " +
    "sua empresa, o histórico que nunca se apaga.\n\n" +
    "Um diretor de IA contratado amanhã não substitui esse registro. Ele o herda, e trabalha melhor por causa dele.",
    t.PAG.margem, 2.35, { w: W, h: 2.6, size: 15, lineSpacing: 24 });
  t.filete(s, t.PAG.margem, 5.3, W, t.FILETE_CLARO, 0.75);
  t.corpo(s,
    "Sem exclusividade forçada, sem contrato que prende: a memória é sua e é exportável. A permanência se paga em valor, ou não se paga.",
    t.PAG.margem, 5.55, { w: W, h: 0.8, size: 13.5, serif: true, italic: true, cor: t.NAVY, lineSpacing: 21 });

  // 6 — CTA
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  t.versalete(s, "O próximo passo", t.PAG.margem, 2.3, { size: 12 });
  s.addText("Uma conversa de 45 minutos sobre a sua pauta de IA. E um parecer de exemplo sobre um fornecedor que já esteja na sua mesa.", {
    x: t.PAG.margem, y: 2.85, w: W, h: 1.9,
    fontFace: t.SERIF, fontSize: 26, bold: true, color: "FFFFFF", lineSpacing: 38,
  });
  t.filete(s, t.PAG.margem, 5.05, 2.2, t.OURO, 1.5);
  s.addText("ABBA Consultoria de IA · contato@abbaservices.com.br", {
    x: t.PAG.margem, y: 5.35, w: W, h: 0.4,
    fontFace: t.SANS, fontSize: 12, color: "D8DCE8", charSpacing: 1,
  });
};
