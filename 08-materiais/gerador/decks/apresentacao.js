// abba-apresentacao — o documento-padrao de envio (3 paginas, 16:9).
// Padrao editorial: abre direto na ABBA, historia em ordem, SEM precos,
// "da primeira conversa", engenharia (nao so agentes), raizes sem nomear arvore.
const t = require("../tema");

module.exports = function gerar(pptx, assets) {
  // ---------- PAGINA 1 — capa + quem somos + raizes ----------
  let s = t.novoSlide(pptx);
  t.versalete(s, "ABBA · Consultoria de IA", t.PAG.margem, 0.75);
  s.addText("Tornamos a sua empresa AI native.", {
    x: t.PAG.margem, y: 1.15, w: t.PAG.w - 2 * t.PAG.margem, h: 1.15,
    fontFace: t.SERIF, fontSize: 40, bold: true, color: t.NAVY,
  });
  t.filete(s, t.PAG.margem, 2.42, 2.2, t.OURO, 1.5);

  t.corpo(s,
    "A ABBA faz duas coisas que não dá para fazer de dentro de uma empresa: " +
    "constrói capacidade de IA em escala, com arquitetura, integrações e agentes " +
    "trabalhando em conjunto e um time inteiro formado, e prova, como terceiro, o " +
    "que mudou: cada decisão com o número que ela precisa mover, combinado antes, " +
    "medido depois, assinado por gente. No fim, a diretoria tem prova, não impressão.",
    t.PAG.margem, 2.7, { w: t.PAG.w - 2 * t.PAG.margem, h: 1.5, size: 15.5, lineSpacing: 24 });

  t.corpo(s,
    "A maioria dos projetos de IA não falha na tecnologia. A pesquisa mais séria que " +
    "existe, da RAND, mediu: mais de 80% falham, o dobro dos projetos comuns de " +
    "tecnologia, e a causa número um é começar sem combinar o que seria dar certo. " +
    "É exatamente aí que trabalhamos.",
    t.PAG.margem, 4.15, { w: t.PAG.w - 2 * t.PAG.margem, h: 1.1, size: 13.5, cor: t.SEC, lineSpacing: 21 });

  // A seção dourada das raízes
  t.filete(s, t.PAG.margem, 5.35, t.PAG.w - 2 * t.PAG.margem, t.FILETE_CLARO, 0.75);
  t.versalete(s, "As nossas raízes", t.PAG.margem, 5.55);
  t.corpo(s,
    "Trabalhamos com raízes: verdade dita mesmo quando custa, número antes de opinião, " +
    "e o compromisso de nos tornarmos desnecessários no operacional. O que instalamos " +
    "fica com você — os sistemas, as pessoas formadas e o registro de tudo o que foi " +
    "decidido e medido.",
    t.PAG.margem, 5.95, { w: t.PAG.w - 2 * t.PAG.margem, h: 1.0, size: 13.5, serif: true, italic: true, lineSpacing: 21 });
  t.rodape(s);

  // ---------- PAGINA 2 — o Programa em 3 fases ----------
  s = t.novoSlide(pptx);
  t.versalete(s, "O caminho", t.PAG.margem, 0.65);
  s.addText("Da primeira conversa à capacidade instalada: um programa, um ano.", {
    x: t.PAG.margem, y: 1.0, w: t.PAG.w - 2 * t.PAG.margem, h: 0.85,
    fontFace: t.SERIF, fontSize: 26, bold: true, color: t.NAVY,
  });
  t.corpo(s,
    "Tudo começa com um mapa do que estimamos estar vazando, feito de fora e sem custo. " +
    "Se fizer sentido, o programa percorre três fases — e você tem uma porta de saída " +
    "limpa em cada uma delas.",
    t.PAG.margem, 1.9, { w: t.PAG.w - 2 * t.PAG.margem, h: 0.7, size: 13, cor: t.SEC, lineSpacing: 20 });

  const colW = (t.PAG.w - 2 * t.PAG.margem - 0.8) / 3;
  const fases = [
    {
      rot: "Fase 1 · A Prova", tempo: "seis semanas",
      oque: "Mergulho nos processos onde o dinheiro vaza e um caso construído com os seus dados, rodando e medido contra a métrica combinada por escrito na primeira semana — mais o portfólio completo de oportunidades, ranqueado.",
      porque: "Porque promessa não decide investimento; número decide. Você delibera sobre o ano inteiro com um caso provado na mesa.",
    },
    {
      rot: "Fase 2 · A Construção", tempo: "meses dois a seis",
      oque: "Os casos aprovados entram em produção, com arquitetura, integrações e agentes de IA com pontos de aprovação humana — e a sua equipe é formada em turma própria, com fluência medida em 30, 60 e 90 dias.",
      porque: "Porque sistemas novos com a empresa pensando do jeito antigo não transformam nada. Pessoas e sistemas andam juntos.",
    },
    {
      rot: "Fase 3 · A Durabilidade", tempo: "meses sete a doze",
      oque: "Operação acompanhada, presença semanal, relatório mensal de projetado versus realizado e o registro de cada decisão contra o resultado medido.",
      porque: "Porque a única prova que importa para a sua diretoria é a capacidade funcionando sem consultor no meio — e isso só o tempo mostra.",
    },
  ];
  fases.forEach((f, i) => {
    const x = t.PAG.margem + i * (colW + 0.4);
    t.filete(s, x, 2.75, colW, t.OURO, 1.2);
    t.versalete(s, f.rot, x, 2.9, { w: colW, size: 10.5 });
    s.addText(f.tempo, { x, y: 3.2, w: colW, h: 0.3, fontFace: t.SERIF, fontSize: 12, italic: true, color: t.SEC });
    t.corpo(s, f.oque, x, 3.55, { w: colW, h: 1.9, size: 11.5, lineSpacing: 16.5 });
    t.corpo(s, f.porque, x, 5.5, { w: colW, h: 1.2, size: 10.5, cor: t.SEC, italic: true, lineSpacing: 15.5 });
  });

  s.addText(
    "O Portão da Prova: ao fim da fase 1, a decisão volta para a sua mão. Se o número não " +
    "apareceu, ou se você simplesmente mudar de ideia, sai levando tudo o que foi produzido — sem multa e sem constrangimento.",
    { x: t.PAG.margem, y: 6.62, w: t.PAG.w - 2 * t.PAG.margem, h: 0.62,
      fontFace: t.SERIF, fontSize: 12.5, italic: true, color: t.NAVY, align: "center", lineSpacing: 17 });
  t.rodape(s);

  // ---------- PAGINA 3 — a relacao que continua + parceiros + CTA ----------
  s = t.novoSlide(pptx);
  t.versalete(s, "Depois do primeiro ano", t.PAG.margem, 0.65);
  s.addText("A relação não termina: ela passa a ser medida todo ano.", {
    x: t.PAG.margem, y: 1.0, w: t.PAG.w - 2 * t.PAG.margem, h: 0.8,
    fontFace: t.SERIF, fontSize: 26, bold: true, color: t.NAVY,
  });
  t.corpo(s,
    "Do segundo ano em diante, a empresa opera sozinha e nós ficamos com o que não dá para " +
    "fazer de dentro: a operação acompanhada, o conselho trimestral e o Exame Anual de IA — a " +
    "re-medição completa da maturidade da empresa, comparada ano contra ano. A série histórica " +
    "que nasce daí só existe aqui, vale mais a cada ano, e é dela que sai a fila de " +
    "oportunidades do ano seguinte.",
    t.PAG.margem, 1.85, { w: t.PAG.w - 2 * t.PAG.margem, h: 1.3, size: 13.5, lineSpacing: 21 });

  t.filete(s, t.PAG.margem, 3.35, t.PAG.w - 2 * t.PAG.margem, t.FILETE_CLARO, 0.75);
  t.versalete(s, "Já tem IA rodando?", t.PAG.margem, 3.55);
  t.corpo(s,
    "Para quem já construiu, a oferta é outra: o Conselheiro de IA — a cadeira de direção " +
    "estratégica, fracionária, do seu lado da mesa, com parecer por escrito sobre cada " +
    "fornecedor e a memória do que foi decidido e medido.",
    t.PAG.margem, 3.9, { w: t.PAG.w - 2 * t.PAG.margem, h: 0.85, size: 13, lineSpacing: 20 });

  t.filete(s, t.PAG.margem, 4.95, t.PAG.w - 2 * t.PAG.margem, t.FILETE_CLARO, 0.75);
  t.versalete(s, "Parceiros oficiais", t.PAG.margem, 5.12);
  if (assets.logoMicrosoft) {
    s.addImage({ path: assets.logoMicrosoft, x: t.PAG.margem, y: 5.5, h: 0.34, w: 1.57 });
  }
  if (assets.logoCrewai) {
    s.addImage({ path: assets.logoCrewai, x: t.PAG.margem + 2.0, y: 5.44, h: 0.44, w: 1.45 });
  }
  t.corpo(s,
    "Durante a capacitação, a sua equipe usa ferramentas dos nossos parceiros para construir " +
    "as próprias soluções.",
    t.PAG.margem + 4.0, 5.42, { w: t.PAG.w - 2 * t.PAG.margem - 4.0, h: 0.5, size: 11.5, cor: t.SEC, lineSpacing: 16 });

  s.addText("O próximo passo não custa nada e cabe em 45 minutos: o Mapa de Vazamento da sua operação.", {
    x: t.PAG.margem, y: 6.25, w: t.PAG.w - 2 * t.PAG.margem, h: 0.55,
    fontFace: t.SERIF, fontSize: 15, bold: true, color: t.NAVY, align: "center",
  });
  t.rodape(s);
};
