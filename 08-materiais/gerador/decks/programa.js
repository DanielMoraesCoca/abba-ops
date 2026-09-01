// deck-programa — o mergulho no Programa "AI Native · Ano 1" (substitui os
// 7 decks de servico do cardapio antigo). SEM precos, SEM travessao.
// A voz do pitch: primeira parede paga a fundacao, numero combinado antes,
// prova e nao impressao. Com as fotos reais dos entregaveis (empresa
// preservada) e o slide informativo "o que compoe cada fase".
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
function fotoDireita(s, assets, nome, legenda, altura = 4.2) {
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
    sub: "A decisão do ano é tomada uma vez. O risco, nunca: cada fase termina num portão onde a decisão volta para a sua mão.",
  });

  // 2 — antes do programa: o mapa
  let s = base(pptx, "Antes de qualquer contrato", "Tudo começa com o Mapa de Vazamento. Grátis.",
    "Feito de fora, com um número em reais dentro: onde estimamos que a operação está vazando, quanto por mês, e o que faríamos primeiro.", SUB_COM_FOTO);
  {
    const limite = fotoDireita(s, assets, "mapa-de-vazamento--pagina-real.jpg", "Página real de um Mapa entregue (empresa preservada).");
    t.corpo(s,
      "O Mapa é a porta única da ABBA. Ele existe para uma decisão: vale ou não vale abrir o Programa? " +
      "Se o número não convencer, a conversa termina ali. Sem custo e sem compromisso.\n\n" +
      "Se convencer, o Termo do Programa é assinado uma vez, com as três fases dentro: a fase 1 firme, " +
      "e as fases 2 e 3 já precificadas como opção sua, condicionada ao Portão da Prova. Provar valor " +
      "em semanas, com dinheiro pequeno, antes de comprometer dinheiro grande.",
      t.PAG.margem, 2.85, { w: limite - t.PAG.margem, h: 3.6, size: 13.5, lineSpacing: 21 });
  }

  // 3 — o que compoe cada fase (a vitrine virou informacao)
  s = base(pptx, "O sistema por dentro", "O que acontece em cada fase, e por quê.",
    "Cada capacidade que a ABBA opera tem lugar e hora dentro do Programa. Nada é vendido em separado: é assim que o sistema funciona.");
  const linhas = [
    ["Avaliação profunda", "Fase 1", "O mergulho do conselho à linha de frente: onde o dinheiro vaza, o que a empresa tem de base, quem vive cada processo. Sai o retrato completo de oportunidades, ranqueado por retorno e esforço."],
    ["Protótipo medido", "Fase 1", "O caso escolhido construído com os seus dados e posto em uso real, contra a métrica combinada por escrito na primeira semana. É a prova antes do investimento: a diretoria decide GO ou NO-GO com números na mesa."],
    ["Construção", "Fase 2", "Os casos aprovados em produção: arquitetura, integrações com os seus sistemas e agentes com aprovação humana nos pontos certos. Erro caro passa por gente antes de acontecer."],
    ["Capacitação", "Fase 2", "A turma da sua equipe no nosso portal, uma prática por dia no trabalho real, com fluência medida em 30, 60 e 90 dias. Sistema novo e gente formada andam juntos."],
    ["Operação assistida", "Fase 3", "SLA, presença semanal e relatório mensal de projetado versus realizado, com a nossa mão cada vez mais leve, de propósito."],
    ["Ritual com a diretoria", "Fase 3 em diante", "O registro de cada decisão contra o resultado medido, apresentado a quem decide. É o que vira o Exame Anual do ano 2."],
  ];
  linhas.forEach((l, i) => {
    const y = 2.72 + i * 0.73;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, l[0], t.PAG.margem, y + 0.08, { w: 2.55, size: 9.5 });
    s.addText(l[1], { x: t.PAG.margem + 2.65, y: y + 0.06, w: 1.5, h: 0.3, fontFace: t.SERIF, fontSize: 10.5, italic: true, color: t.SEC });
    t.corpo(s, l[2], t.PAG.margem + 4.25, y + 0.05, { w: W - 4.25, h: 0.66, size: 10, lineSpacing: 13 });
  });

  // 4 — fase 1
  s = base(pptx, "Fase 1 · A Prova · seis semanas", "Um caso construído, rodando e medido. E o retrato inteiro.",
    "A métrica é combinada por escrito na primeira semana. Ao fim, o número está na mesa. E a decisão é sua.", SUB_COM_FOTO);
  {
    const limite = fotoDireita(s, assets, "prototipo--relatorio-gono-go.jpg", "Relatório GO/NO-GO real de um protótipo (empresa preservada).");
    t.corpo(s,
      "O que a fase 1 entrega:\n" +
      "· o caso escolhido construído com os seus dados, em uso real;\n" +
      "· a medição de terceiro contra a métrica combinada: projetado versus realizado, assinado por uma pessoa nomeada da sua empresa;\n" +
      "· a avaliação profunda de maturidade;\n" +
      "· o retrato completo de oportunidades, ranqueado por retorno e esforço.\n\n" +
      "O retrato é seu, fique ou não: o portão retém execução, nunca informação.",
      t.PAG.margem, 2.85, { w: limite - t.PAG.margem, h: 3.9, size: 12.5, lineSpacing: 19 });
  }

  // 5 — como se combina um numero (exemplo real, empresa preservada)
  s = base(pptx, "Como se combina um número", "Palavra por palavra, antes de começar. Como numa proposta real.",
    "De uma proposta emitida em agosto de 2026 (empresa preservada, setor de eventos): o piloto já nasce com a meta travada por escrito na reunião técnica, e o fechamento mede contra ela.");
  const metas = [
    ["Meta combinada 1", "Zero encaminhamento manual: a lista inteira de convidados processada sem o dono tocar no telefone."],
    ["Meta combinada 2", "Taxa de confirmação igual ou melhor que a do último evento comparável, com o esforço de horas caindo a quase zero."],
    ["Meta combinada 3", "Todo contato com resposta registrada: quem confirmou, quem recusou, quem ficou no encerramento."],
    ["A medição", "O relatório de fechamento do piloto compara os números do evento contra a meta combinada antes. É esse papel que decide a conversa seguinte: não a nossa opinião."],
  ];
  metas.forEach((m, i) => {
    const y = 2.95 + i * 0.9;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, m[0], t.PAG.margem, y + 0.1, { w: 2.6, size: 10 });
    t.corpo(s, m[1], t.PAG.margem + 2.8, y + 0.08, { w: W - 2.8, h: 0.75, size: 12, lineSpacing: 16 });
  });
  t.corpo(s,
    "É assim em todo caso da ABBA, do piloto de seis semanas ao ano inteiro: sucesso combinado antes, medido depois.",
    t.PAG.margem, 6.62, { w: W, h: 0.35, size: 11.5, serif: true, italic: true, cor: t.NAVY, align: "center" });

  // 6 — o portao
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  t.versalete(s, "O Portão da Prova · semana 6", t.PAG.margem, 1.9, { size: 12 });
  s.addText("Ao término da fase 1, a decisão de continuar é integralmente sua. Se o resultado medido não confirmar o critério combinado, o Programa se encerra ali: sem multa, e com os entregáveis em suas mãos.", {
    x: t.PAG.margem, y: 2.35, w: W, h: 2.2,
    fontFace: t.SERIF, fontSize: 21, bold: true, color: "FFFFFF", lineSpacing: 30,
  });
  t.filete(s, t.PAG.margem, 4.7, 2.2, t.OURO, 1.5);
  s.addText(
    "Os portões se repetem no mês seis e no mês doze. Nenhuma fase se inicia sem que a anterior tenha " +
    "comprovado o seu resultado: o risco de continuidade é nosso, não seu.",
    { x: t.PAG.margem, y: 4.95, w: W, h: 0.9, fontFace: t.SERIF, fontSize: 15, italic: true, color: "D8DCE8", lineSpacing: 23 });

  // 7 — fase 2
  s = base(pptx, "Fase 2 · A Construção · meses 2 a 6", "Sistemas em produção. Pessoas formadas. Juntos.",
    "Os casos que você aprovou no retrato entram em produção, e a sua equipe é formada em turma própria, em paralelo.");
  t.corpo(s,
    "Engenharia de verdade: arquitetura, integrações com os seus sistemas e agentes de IA com pontos de " +
    "aprovação humana desenhados. Erro caro passa por gente antes de acontecer. E capacitação medida: " +
    "uma prática por dia, no trabalho real, com fluência medida em 30, 60 e 90 dias. Porque sistema novo " +
    "com a empresa pensando do jeito antigo não transforma nada.",
    t.PAG.margem, 2.9, { w: W, h: 1.15, size: 12.5, lineSpacing: 18 });
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("portal--inicio-atual.png"), x: t.PAG.margem, y: 3.95, w: 4.87, h: 2.75 });
    s.addImage({ path: assets.fotos("construcao--relatorio-deployment.jpg"), x: t.PAG.margem + 5.35, y: 3.95, w: 1.94, h: 2.75 });
    t.corpo(s, "O portal da turma, como o seu time vê hoje.",
      t.PAG.margem, 6.74, { w: 4.87, h: 0.25, size: 9.5, cor: t.SEC, italic: true });
    t.corpo(s, "Relatório de implantação real (empresa preservada).",
      t.PAG.margem + 5.35, 6.74, { w: 3.2, h: 0.25, size: 9.5, cor: t.SEC, italic: true });
  }

  // 8 — fase 3
  s = base(pptx, "Fase 3 · A Durabilidade · meses 7 a 12", "A única prova que importa: funcionar sem nós no meio.",
    "A operação acompanhada de perto. E a mão cada vez mais leve, de propósito.", SUB_COM_FOTO);
  {
    const limite = fotoDireita(s, assets, "gerenciados--relatorio-mensal.jpg", "Relatório mensal real de operação (empresa preservada).");
    t.corpo(s,
      "Presença semanal, SLA, relatório mensal de projetado versus realizado e o registro de cada decisão " +
      "contra o resultado medido.\n\n" +
      "No mês 12, a diretoria não recebe uma impressão: recebe a série do ano inteiro. O que foi prometido, " +
      "o que foi medido, o que ficou instalado e quem, da sua equipe, opera cada peça.",
      t.PAG.margem, 2.85, { w: limite - t.PAG.margem, h: 3.5, size: 13, lineSpacing: 20 });
  }

  // 9 — depois do ano
  s = base(pptx, "E depois do ano?", "A relação vira medição anual.",
    "Do segundo ano em diante: operação sob SLA, conselho trimestral e o Exame Anual de IA, a maturidade re-medida e comparada ano contra ano.");
  t.corpo(s,
    "A série histórica que nasce daí só existe aqui e vale mais a cada ano. É dela que sai a fila de " +
    "oportunidades do ano seguinte: melhorias que só aparecem depois que o fluxo novo existe. Expansões " +
    "entram como mini-ciclos dentro da assinatura, cada um com a mesma regra de sempre: métrica combinada " +
    "antes, medida depois.",
    t.PAG.margem, 3.0, { w: W, h: 1.5, size: 14, lineSpacing: 22 });
  t.filete(s, t.PAG.margem, 4.8, W, t.FILETE_CLARO, 0.75);
  t.corpo(s,
    "Retemos clientes do único jeito que aceitamos: composição de valor, nunca dependência. Tudo o que " +
    "construímos é seu, o dado é exportável, e a saída é limpa em qualquer aniversário.",
    t.PAG.margem, 5.05, { w: W, h: 0.9, size: 13.5, serif: true, italic: true, cor: t.NAVY, lineSpacing: 21 });

  // 10 — o que fica com voce
  s = base(pptx, "No fim", "O que fica com você");
  const itens = [
    ["Os sistemas", "em produção, documentados, com aprovação humana nos pontos certos. Propriedade sua."],
    ["As pessoas", "formadas em turma própria, com fluência medida. E um dono interno para cada peça."],
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
