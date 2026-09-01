// deck-programa — o mergulho no Programa "AI Native · Ano 1" (substitui os
// 7 decks de servico do cardapio antigo). SEM precos — preco so na proposta,
// pela tabela vigente. Com as fotos reais dos entregaveis (empresa preservada).
const t = require("../tema");

function base(pptx, etiqueta, tit, sub, subW) {
  const s = t.novoSlide(pptx);
  t.versalete(s, etiqueta, t.PAG.margem, 0.65);
  s.addText(tit, {
    x: t.PAG.margem, y: 1.05, w: t.PAG.w - 2 * t.PAG.margem, h: 1.0,
    fontFace: t.SERIF, fontSize: 27, bold: true, color: t.NAVY, lineSpacing: 33,
  });
  if (sub) t.corpo(s, sub, t.PAG.margem, 2.1, { w: subW || t.PAG.w - 2 * t.PAG.margem, h: 0.9, size: 13, cor: t.SEC, lineSpacing: 20 });
  t.rodape(s);
  return s;
}

// largura de subtitulo que nao invade a foto-retrato da direita
const SUB_COM_FOTO = t.PAG.w - 2 * t.PAG.margem - 3.6;

// bloco texto-esquerda + foto-retrato-direita (910x1287 → prop. 0.707)
function fotoDireita(s, assets, nome, legenda, altura = 4.3) {
  const w = altura * 0.707;
  const x = t.PAG.w - t.PAG.margem - w;
  s.addImage({ path: assets.fotos(nome), x, y: 2.55, w, h: altura });
  if (legenda) t.corpo(s, legenda, x, 2.6 + altura, { w, h: 0.45, size: 9.5, cor: t.SEC, italic: true, lineSpacing: 13 });
  return x - 0.5; // limite direito para o texto
}

module.exports = function gerar(pptx, assets) {
  const W = t.PAG.w - 2 * t.PAG.margem;

  // 1 — capa
  t.capaNavy(pptx, {
    etiqueta: "O Programa · AI Native · Ano 1",
    tituloTexto: "Um ano. Três fases.\nTrês portas de saída.",
    sub: "A decisão do ano é tomada uma vez — o risco, nunca: cada fase termina num portão onde a decisão volta para a sua mão.",
  });

  // 2 — antes do programa: o mapa
  let s = base(pptx, "Antes de qualquer contrato", "Tudo começa com o Mapa de Vazamento — grátis.",
    "Feito de fora, com um número em reais dentro: onde estimamos que a operação está vazando, quanto por mês, e o que faríamos primeiro.", SUB_COM_FOTO);
  {
    const limite = fotoDireita(s, assets, "mapa-de-vazamento--pagina-real.jpg", "Página real de um Mapa entregue (empresa preservada).", 4.2);
    t.corpo(s,
      "O Mapa é a porta única da ABBA. Ele existe para uma decisão: vale ou não vale abrir o Programa? " +
      "Se o número não convencer, a conversa termina ali — sem custo e sem compromisso.\n\n" +
      "Se convencer, o Termo do Programa é assinado uma vez, com as três fases dentro: a fase 1 firme, " +
      "e as fases 2 e 3 já precificadas como opção sua — condicionada ao Portão da Prova.",
      t.PAG.margem, 2.85, { w: limite - t.PAG.margem, h: 3.6, size: 13.5, lineSpacing: 21 });
  }

  // 3 — fase 1
  s = base(pptx, "Fase 1 · A Prova — seis semanas", "Um caso construído, rodando e medido. E o retrato inteiro.",
    "A métrica é combinada por escrito na primeira semana. Ao fim, o número está na mesa — e a decisão é sua.", SUB_COM_FOTO);
  {
    const limite = fotoDireita(s, assets, "prototipo--relatorio-gono-go.jpg", "Relatório GO/NO-GO real de um protótipo (empresa preservada).", 4.2);
    t.corpo(s,
      "O que a fase 1 entrega:\n" +
      "· o caso escolhido construído com os seus dados, em uso real;\n" +
      "· a medição de terceiro contra a métrica combinada — projetado versus realizado, assinado por uma pessoa nomeada da sua empresa;\n" +
      "· a avaliação de maturidade em 25 dimensões;\n" +
      "· o portfólio completo de oportunidades, ranqueado por retorno e esforço.\n\n" +
      "O portfólio é seu, fique ou não: o portão retém execução, nunca informação.",
      t.PAG.margem, 2.85, { w: limite - t.PAG.margem, h: 3.9, size: 12.5, lineSpacing: 19 });
  }

  // 4 — o portao
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  t.versalete(s, "O Portão da Prova · semana 6", t.PAG.margem, 1.9, { size: 12 });
  s.addText("Se o número combinado não apareceu — ou se você simplesmente mudar de ideia — você sai levando tudo. Sem multa.", {
    x: t.PAG.margem, y: 2.45, w: W, h: 2.0,
    fontFace: t.SERIF, fontSize: 25, bold: true, color: "FFFFFF", lineSpacing: 35,
  });
  t.filete(s, t.PAG.margem, 4.7, 2.2, t.OURO, 1.5);
  s.addText(
    "Há mais dois portões como este: no mês 6 e no mês 12. Nenhuma fase começa sem a anterior ter provado — " +
    "é o nosso risco, não o seu.",
    { x: t.PAG.margem, y: 4.95, w: W, h: 0.9, fontFace: t.SERIF, fontSize: 15, italic: true, color: "D8DCE8", lineSpacing: 23 });

  // 5 — fase 2
  s = base(pptx, "Fase 2 · A Construção — meses 2 a 6", "Sistemas em produção. Pessoas formadas. Juntos.",
    "Os casos que você aprovou no portfólio entram em produção — e a sua equipe é formada em turma própria, em paralelo.", SUB_COM_FOTO);
  {
    const limite = fotoDireita(s, assets, "construcao--relatorio-deployment.jpg", "Relatório de implantação real (empresa preservada).", 4.2);
    t.corpo(s,
      "Engenharia de verdade: arquitetura, integrações com os seus sistemas e agentes de IA com pontos de " +
      "aprovação humana desenhados — erro caro passa por gente antes de acontecer.\n\n" +
      "Capacitação medida: turma própria na nossa plataforma, com trilhas por papel e fluência medida em " +
      "30, 60 e 90 dias — porque sistema novo com a empresa pensando do jeito antigo não transforma nada.",
      t.PAG.margem, 2.85, { w: limite - t.PAG.margem, h: 3.7, size: 13, lineSpacing: 20 });
  }

  // 6 — fase 3
  s = base(pptx, "Fase 3 · A Durabilidade — meses 7 a 12", "A única prova que importa: funcionar sem nós no meio.",
    "A operação acompanhada de perto — e a mão cada vez mais leve, de propósito.", SUB_COM_FOTO);
  {
    const limite = fotoDireita(s, assets, "gerenciados--relatorio-mensal.jpg", "Relatório mensal real de operação (empresa preservada).", 4.2);
    t.corpo(s,
      "Presença semanal, SLA, relatório mensal de projetado versus realizado e o registro de cada decisão " +
      "contra o resultado medido.\n\n" +
      "No mês 12, a diretoria não recebe uma impressão: recebe a série do ano inteiro — o que foi prometido, " +
      "o que foi medido, o que ficou instalado e quem, da sua equipe, opera cada peça.",
      t.PAG.margem, 2.85, { w: limite - t.PAG.margem, h: 3.5, size: 13, lineSpacing: 20 });
  }

  // 7 — depois do ano
  s = base(pptx, "E depois do ano?", "A relação vira medição anual.",
    "Do segundo ano em diante: operação sob SLA, conselho trimestral e o Exame Anual de IA — a maturidade re-medida e comparada ano contra ano.");
  t.corpo(s,
    "A série histórica que nasce daí só existe aqui e vale mais a cada ano — e é dela que sai a fila de " +
    "oportunidades do ano seguinte: melhorias que só aparecem depois que o fluxo novo existe. Expansões " +
    "entram como mini-ciclos dentro da assinatura, cada um com a mesma regra de sempre: métrica combinada " +
    "antes, medida depois.",
    t.PAG.margem, 3.0, { w: W, h: 1.5, size: 14, lineSpacing: 22 });
  t.filete(s, t.PAG.margem, 4.8, W, t.FILETE_CLARO, 0.75);
  t.corpo(s,
    "Retemos clientes do único jeito que aceitamos: composição de valor, nunca dependência. Tudo o que " +
    "construímos é seu, o dado é exportável, e a saída é limpa em qualquer aniversário.",
    t.PAG.margem, 5.05, { w: W, h: 0.9, size: 13.5, serif: true, italic: true, cor: t.NAVY, lineSpacing: 21 });

  // 8 — o que fica com voce
  s = base(pptx, "No fim", "O que fica com você");
  const itens = [
    ["Os sistemas", "em produção, documentados, com aprovação humana nos pontos certos — propriedade sua."],
    ["As pessoas", "formadas em turma própria, com fluência medida — e um dono interno para cada peça."],
    ["O registro", "cada decisão com o número combinado antes e o resultado medido depois, assinado por gente sua."],
    ["A prova", "não a nossa palavra: a série de projetado versus realizado do ano inteiro, pronta para a diretoria."],
  ];
  itens.forEach((it, i) => {
    const y = 2.25 + i * 1.08;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, it[0], t.PAG.margem, y + 0.12, { w: 2.6, size: 10.5 });
    t.corpo(s, it[1], t.PAG.margem + 2.8, y + 0.1, { w: W - 2.8, h: 0.85, size: 13, lineSpacing: 19 });
  });
  s.addText("O próximo passo não custa nada: o Mapa de Vazamento da sua operação.", {
    x: t.PAG.margem, y: 6.6, w: W, h: 0.5,
    fontFace: t.SERIF, fontSize: 15, bold: true, color: t.NAVY, align: "center",
  });
};
