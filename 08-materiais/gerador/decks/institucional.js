// abba-deck-institucional — o deck de apresentacao AO VIVO (~12 slides).
// Narrativa V5: um programa, tres fases, a relacao que continua. SEM precos.
// Regua: RAND >80% com fonte; METR ~40 pontos; DORA amplifica; nunca "garantia",
// nunca "auditoria" (Exame Anual), nunca acuracia prometida.
const t = require("../tema");

function slideSecao(pptx, etiqueta, tit, sub) {
  const s = t.novoSlide(pptx);
  t.versalete(s, etiqueta, t.PAG.margem, 0.65);
  s.addText(tit, {
    x: t.PAG.margem, y: 1.05, w: t.PAG.w - 2 * t.PAG.margem, h: 1.0,
    fontFace: t.SERIF, fontSize: 28, bold: true, color: t.NAVY, lineSpacing: 34,
  });
  if (sub) t.corpo(s, sub, t.PAG.margem, 2.1, { w: t.PAG.w - 2 * t.PAG.margem, h: 0.7, size: 13, cor: t.SEC, lineSpacing: 20 });
  t.rodape(s);
  return s;
}

module.exports = function gerar(pptx, assets) {
  const W = t.PAG.w - 2 * t.PAG.margem;

  // 1 — capa
  t.capaNavy(pptx, {
    etiqueta: "ABBA · Consultoria de IA",
    tituloTexto: "Tornamos a sua empresa AI native.",
    sub: "Capacidade de IA construída em escala — e provada, como terceiro, com o número combinado antes e medido depois.",
  });

  // 2 — o problema
  let s = slideSecao(pptx, "O problema", "A maioria dos projetos de IA não falha na tecnologia.");
  const provas = [
    ["RAND", "Mais de 80% dos projetos de IA falham — o dobro dos projetos comuns de TI. A causa número um: começar sem combinar o que seria dar certo."],
    ["METR", "Desenvolvedores experientes com IA ficaram 19% mais lentos — convencidos de que estavam 20% mais rápidos. Autoavaliação erra por ~40 pontos: sem medição externa, ninguém sabe o que tem."],
    ["DORA", "IA amplifica o que já existe: base organizada rende; base bagunçada piora mais rápido. Arrumar a base não é atraso — é a condição do ganho."],
  ];
  provas.forEach((p, i) => {
    const y = 2.35 + i * 1.45;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, p[0], t.PAG.margem, y + 0.12, { w: 1.6 });
    t.corpo(s, p[1], t.PAG.margem + 1.8, y + 0.1, { w: W - 1.8, h: 1.2, size: 13, lineSpacing: 19 });
  });

  // 3 — a tese
  s = slideSecao(pptx, "A nossa tese", "O valor está 70% em pessoas, processos e governança.",
    "O mercado vende os outros 30% — ferramentas, pilotos sem métrica, cursos soltos. Nós instalamos os 70%: o critério de sucesso, a base arrumada, as pessoas formadas e a medição de terceiro que sustenta cada decisão.");
  t.filete(s, t.PAG.margem, 3.3, W, t.FILETE_CLARO, 0.75);
  t.corpo(s,
    "Por isso não vendemos ferramenta, nem piloto, nem curso: vendemos um caminho de um ano com " +
    "porta de saída limpa em cada fase — e a prova, medida, de que ele funcionou.",
    t.PAG.margem, 3.6, { w: W, h: 0.9, size: 14.5, serif: true, italic: true, lineSpacing: 22 });

  // 4 — o mapa (porta única)
  s = slideSecao(pptx, "Como toda conversa começa", "O Mapa de Vazamento — grátis, feito de fora, com um número dentro.",
    "Antes de qualquer contrato, entregamos um mapa do que estimamos estar vazando na sua operação: onde, quanto por mês, e o que faríamos primeiro. Se o número não convencer, a conversa termina ali — sem custo e sem compromisso.");
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("mapa-de-vazamento--pagina-real.jpg"), x: t.PAG.w / 2 - 1.75, y: 3.1, w: 3.5, h: 3.85 });
  }

  // 5 — o programa (visao geral)
  s = slideSecao(pptx, "O caminho", "Um programa, um ano, três fases — e três portas de saída.",
    "A decisão do ano é tomada uma vez, mas o risco não: cada fase termina num portão onde a decisão volta para a sua mão.");
  const fases = [
    ["Fase 1 · A Prova", "seis semanas", "Um caso construído com os seus dados, rodando e medido contra a métrica combinada por escrito na primeira semana — mais o portfólio completo de oportunidades, ranqueado."],
    ["Fase 2 · A Construção", "meses 2–6", "Os casos aprovados em produção, com integrações e pontos de aprovação humana — e a sua equipe formada em turma própria, com fluência medida em 30, 60 e 90 dias."],
    ["Fase 3 · A Durabilidade", "meses 7–12", "Operação acompanhada, presença semanal, relatório de projetado versus realizado — a capacidade funcionando sem consultor no meio."],
  ];
  const colW = (W - 0.8) / 3;
  fases.forEach((f, i) => {
    const x = t.PAG.margem + i * (colW + 0.4);
    t.filete(s, x, 3.05, colW, t.OURO, 1.2);
    t.versalete(s, f[0], x, 3.2, { w: colW, size: 10.5 });
    s.addText(f[1], { x, y: 3.5, w: colW, h: 0.3, fontFace: t.SERIF, fontSize: 12, italic: true, color: t.SEC });
    t.corpo(s, f[2], x, 3.85, { w: colW, h: 2.2, size: 11.5, lineSpacing: 16.5 });
  });

  // 6 — o portao da prova
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  t.versalete(s, "O Portão da Prova", t.PAG.margem, 2.0, { size: 12 });
  s.addText("Se em seis semanas o número combinado não apareceu — ou se você simplesmente mudar de ideia — você sai levando tudo o que foi produzido. Sem multa. Sem constrangimento.", {
    x: t.PAG.margem, y: 2.5, w: W, h: 2.2,
    fontFace: t.SERIF, fontSize: 24, bold: true, color: "FFFFFF", lineSpacing: 34,
  });
  t.filete(s, t.PAG.margem, 4.9, 2.2, t.OURO, 1.5);
  s.addText("O portão retém execução, nunca informação: o portfólio ranqueado da fase 1 é seu, fique ou não.", {
    x: t.PAG.margem, y: 5.15, w: W, h: 0.7,
    fontFace: t.SERIF, fontSize: 15, italic: true, color: "D8DCE8", lineSpacing: 22,
  });

  // 7 — como a fase 2 constroi
  s = slideSecao(pptx, "Dentro da construção", "Engenharia de verdade, não demo de feira.",
    "Arquitetura, integrações com os seus sistemas, agentes de IA com pontos de aprovação humana desenhados — e cada entrega com dono, prazo e critério de aceite.");
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("construcao--relatorio-deployment.jpg"), x: t.PAG.margem + 0.4, y: 3.1, w: 2.65, h: 3.75 });
    s.addImage({ path: assets.fotos("portal--painel-real.jpg"), x: t.PAG.margem + 3.7, y: 3.35, w: 5.65, h: 3.19 });
    t.corpo(s, "Relatório de implantação real (empresa preservada) e o portal da turma.",
      t.PAG.margem + 3.7, 6.58, { w: 5.65, h: 0.3, size: 10, cor: t.SEC, italic: true });
  }

  // 8 — depois do primeiro ano
  s = slideSecao(pptx, "Depois do primeiro ano", "A relação não termina: ela passa a ser medida todo ano.",
    "Do segundo ano em diante, a empresa opera sozinha e nós ficamos com o que não dá para fazer de dentro:");
  const camadas = [
    ["Operação acompanhada", "SLA, presença semanal e relatório mensal de projetado versus realizado."],
    ["Conselho trimestral", "A pauta de IA da diretoria, preparada e defendida por quem mediu o ano inteiro."],
    ["O Exame Anual de IA", "A re-medição completa da maturidade, comparada ano contra ano — a série histórica que só existe aqui e vale mais a cada ano."],
  ];
  camadas.forEach((c, i) => {
    const y = 2.9 + i * 1.25;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, c[0], t.PAG.margem, y + 0.12, { w: 3.4, size: 10.5 });
    t.corpo(s, c[1], t.PAG.margem + 3.6, y + 0.1, { w: W - 3.6, h: 1.0, size: 13, lineSpacing: 19 });
  });
  t.corpo(s, "É do Exame que sai a fila de oportunidades do ano seguinte — melhorias que só aparecem depois que o fluxo novo existe.",
    t.PAG.margem, 6.6, { w: W, h: 0.5, size: 12.5, serif: true, italic: true, cor: t.NAVY, align: "center" });

  // 9 — conselheiro
  s = slideSecao(pptx, "Já tem IA rodando?", "O Conselheiro de IA — a cadeira do seu lado da mesa.",
    "Para quem já construiu: presença fracionária na diretoria, roadmap vivo, parecer por escrito sobre cada fornecedor e a memória do que foi decidido e medido — sem custo de um diretor em folha.");
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("conselheiro--parecer-arbitragem.jpg"), x: t.PAG.w / 2 - 1.4, y: 3.15, w: 2.8, h: 3.96 });
  }

  // 10 — por que nao da para fazer de dentro
  s = slideSecao(pptx, "Por que um terceiro", "Nenhum time interno pode ser a própria prova.");
  t.corpo(s,
    "É a razão pela qual empresas com um ótimo CFO ainda contratam quem verifique as contas de fora: " +
    "quem executa não pode atestar o próprio resultado. Na ABBA, a prova é de terceiro por construção — " +
    "a expectativa é declarada antes e fica imutável, o resultado só entra medido e assinado por uma pessoa " +
    "nomeada da sua empresa, e o histórico nunca se apaga. O melhor diretor de IA do mundo não substitui isso; " +
    "ele usa isso.",
    t.PAG.margem, 2.3, { w: W, h: 2.0, size: 15, lineSpacing: 24 });
  t.filete(s, t.PAG.margem, 4.6, W, t.FILETE_CLARO, 0.75);
  t.versalete(s, "Ferramentas próprias e parceiros", t.PAG.margem, 4.8);
  t.corpo(s,
    "A avaliação roda sobre tecnologia construída por nós; a capacitação, sobre plataforma própria. " +
    "Na construção, a sua equipe usa ferramentas dos nossos parceiros para construir as próprias soluções.",
    t.PAG.margem, 5.15, { w: W, h: 0.75, size: 12.5, lineSpacing: 18 });
  if (assets) {
    if (assets.logoMicrosoft) s.addImage({ path: assets.logoMicrosoft, x: t.PAG.margem, y: 6.1, h: 0.34, w: 1.57 });
    if (assets.logoCrewai) s.addImage({ path: assets.logoCrewai, x: t.PAG.margem + 2.0, y: 6.04, h: 0.44, w: 1.45 });
  }

  // 11 — raizes
  s = t.novoSlide(pptx);
  t.versalete(s, "As nossas raízes", t.PAG.margem, 0.75);
  s.addText("Verdade dita mesmo quando custa.\nNúmero antes de opinião.\nTornar-nos desnecessários no operacional.", {
    x: t.PAG.margem, y: 1.5, w: W, h: 3.0,
    fontFace: t.SERIF, fontSize: 27, bold: true, color: t.NAVY, lineSpacing: 46,
  });
  t.filete(s, t.PAG.margem, 4.75, 2.2, t.OURO, 1.5);
  t.corpo(s,
    "O que instalamos fica com você: os sistemas, as pessoas formadas e o registro de tudo o que foi decidido e medido.",
    t.PAG.margem, 5.0, { w: W, h: 0.8, size: 15, serif: true, italic: true, lineSpacing: 23 });
  t.rodape(s);

  // 12 — CTA
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  t.versalete(s, "O próximo passo", t.PAG.margem, 2.3, { size: 12 });
  s.addText("Não custa nada e cabe em 45 minutos:\no Mapa de Vazamento da sua operação.", {
    x: t.PAG.margem, y: 2.85, w: W, h: 1.9,
    fontFace: t.SERIF, fontSize: 30, bold: true, color: "FFFFFF", lineSpacing: 42,
  });
  t.filete(s, t.PAG.margem, 4.95, 2.2, t.OURO, 1.5);
  s.addText("ABBA Consultoria de IA · contato@abbaservices.com.br", {
    x: t.PAG.margem, y: 5.25, w: W, h: 0.4,
    fontFace: t.SANS, fontSize: 12, color: "D8DCE8", charSpacing: 1,
  });
};
