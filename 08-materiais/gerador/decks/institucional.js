// abba-deck-institucional — o deck de apresentacao AO VIVO (~12 slides).
// Narrativa V5 com a voz do pitch do palco: ponta vs. veia, mesa de tres
// pes, a primeira parede paga a fundacao, prova e nao impressao, juro
// composto na moeda errada. SEM precos, SEM travessao.
// Regua: RAND >80% com fonte; METR ~40 pontos; DORA amplifica; nunca
// "garantia", nunca "auditoria" (Exame Anual), nunca acuracia prometida.
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
    sub: "Capacidade de IA construída em escala. E provada, como terceiro: número combinado antes, medido depois.",
  });

  // 2 — o gancho do palco
  let s = t.novoSlide(pptx);
  t.versalete(s, "Uma coisa que ninguém fala em voz alta", t.PAG.margem, 0.9);
  s.addText(
    "De cada dez empresas que decidiram usar IA este ano, mais de oito não vão conseguir mostrar um número no fim.",
    { x: t.PAG.margem, y: 1.5, w: W, h: 1.8, fontFace: t.SERIF, fontSize: 29, bold: true, color: t.NAVY, lineSpacing: 40 });
  t.filete(s, t.PAG.margem, 3.5, 2.2, t.OURO, 1.5);
  t.corpo(s,
    "E não é por falta de tecnologia. Se entrarmos em dez empresas hoje e perguntarmos se usam " +
    "inteligência artificial, dez dizem que sim. E estão falando a verdade: tem licença, tem gente " +
    "usando, tem gente feliz. Só que quando se olha o resultado da empresa, não mudou nada.",
    t.PAG.margem, 3.8, { w: W, h: 1.2, size: 15, lineSpacing: 23 });
  t.corpo(s,
    "Não é porque a IA não funciona. É porque ela entrou pelo lugar errado.",
    t.PAG.margem, 5.2, { w: W, h: 0.6, size: 16, serif: true, italic: true, cor: t.NAVY, lineSpacing: 24 });
  t.rodape(s);

  // 3 — ponta vs. veia
  s = slideSecao(pptx, "Por onde a IA entra", "Na ponta, ou na veia?");
  const duas = [
    ["IA na ponta", "Uma pessoa pega uma tarefa, pede para a ferramenta, recebe o resultado. Começo, meio e fim na mão dela. O ganho fica com a pessoa: se ela sai amanhã, o ganho sai junto pela porta. É remédio que a pessoa toma."],
    ["IA na veia", "A IA roda dentro do processo, com integrações, aprovações humanas nos pontos certos e um número acompanhando. O organismo funciona diferente. O ganho fica na empresa, mesmo quando as pessoas mudam."],
  ];
  const colW2 = (W - 0.6) / 2;
  duas.forEach((d, i) => {
    const x = t.PAG.margem + i * (colW2 + 0.6);
    t.filete(s, x, 2.5, colW2, t.OURO, 1.2);
    t.versalete(s, d[0], x, 2.66, { w: colW2, size: 11 });
    t.corpo(s, d[1], x, 3.05, { w: colW2, h: 2.3, size: 13.5, lineSpacing: 20 });
  });
  s.addText(
    "A pergunta que separa quem colhe de quem não colhe não é qual ferramenta comprar. É por onde a IA está entrando na sua empresa.",
    { x: t.PAG.margem, y: 5.75, w: W, h: 0.85,
      fontFace: t.SERIF, fontSize: 15, italic: true, color: t.NAVY, align: "center", lineSpacing: 22 });

  // 4 — a prova (as 3 fontes)
  s = slideSecao(pptx, "Não é impressão nossa", "Três medições independentes, dizendo a mesma coisa.");
  const provas = [
    ["RAND", "Mais de 80% dos projetos de IA falham. O dobro dos projetos comuns de tecnologia. E a causa número um não foi a qualidade do modelo: foi começar sem ninguém combinar o que seria dar certo."],
    ["METR", "Programadores experientes ficaram 19% mais lentos usando IA, e saíram convencidos de que tinham ficado 20% mais rápidos. Ninguém sabe o próprio ganho sem medir de fora."],
    ["DORA", "A IA amplifica o que já existe: time com base arrumada acelera, base bagunçada piora mais rápido. Arrumar a base não é atraso. É a condição do ganho."],
  ];
  provas.forEach((p, i) => {
    const y = 2.35 + i * 1.45;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, p[0], t.PAG.margem, y + 0.12, { w: 1.6 });
    t.corpo(s, p[1], t.PAG.margem + 1.8, y + 0.1, { w: W - 1.8, h: 1.2, size: 13, lineSpacing: 19 });
  });

  // 5 — a mesa de tres pes
  s = slideSecao(pptx, "A nossa tese", "Isto é uma mesa de três pés.");
  t.corpo(s,
    "Tecnologia, processo e gente. Se um pé fica mais curto que os outros, o problema não é o pé: " +
    "é a mesa inteira. E aí a empresa passa o resto da vida enfiando papelzinho embaixo. Papelzinho " +
    "não é solução. É convivência com o defeito.",
    t.PAG.margem, 2.3, { w: W, h: 1.3, size: 15.5, lineSpacing: 24 });
  t.corpo(s,
    "O mercado vende um pé de cada vez: licença para todo mundo, software de prateleira, curso que " +
    "vira aplauso e segunda-feira igual. Nenhum desses caminhos é burro. Todos foram escolhidos por " +
    "gente inteligente. Eles só não seguram a mesa.",
    t.PAG.margem, 3.75, { w: W, h: 1.15, size: 13.5, cor: t.SEC, lineSpacing: 20 });
  t.filete(s, t.PAG.margem, 5.1, W, t.FILETE_CLARO, 0.75);
  t.corpo(s,
    "Por isso não vendemos ferramenta, nem piloto, nem curso: instalamos os três pés juntos, num " +
    "caminho de um ano com porta de saída limpa em cada fase. E provamos que a mesa parou de balançar.",
    t.PAG.margem, 5.35, { w: W, h: 0.95, size: 14.5, serif: true, italic: true, cor: t.NAVY, lineSpacing: 22 });

  // 6 — o mapa (porta unica)
  s = slideSecao(pptx, "Como toda conversa começa", "O Mapa de Vazamento: grátis, feito de fora, com um número dentro.",
    "Antes de qualquer contrato, entregamos um mapa do que estimamos estar vazando na sua operação: onde, quanto por mês, e o que faríamos primeiro. Se o número não convencer, a conversa termina ali. Sem custo e sem compromisso.");
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("mapa-de-vazamento--pagina-real.jpg"), x: t.PAG.w / 2 - 1.75, y: 3.1, w: 3.5, h: 3.85 });
  }

  // 7 — o programa (visao geral, com o que compoe cada fase)
  s = slideSecao(pptx, "O caminho", "Um programa, um ano, três fases. E três portas de saída.",
    "Ninguém espera o terreno ficar perfeito para começar a obra: escolhemos juntos a primeira parede, e é ela que paga a fundação do resto.");
  const fases = [
    ["Fase 1 · A Prova", "seis semanas", "Um caso construído com os seus dados, rodando e medido contra a métrica combinada por escrito na primeira semana. Dentro dela: a avaliação profunda, o protótipo em uso real e o retrato completo de oportunidades, ranqueado."],
    ["Fase 2 · A Construção", "meses 2 a 6", "Os casos aprovados em produção. Dentro dela: arquitetura, integrações e agentes com aprovação humana nos pontos certos, e a turma da sua equipe no nosso portal, com fluência medida em 30, 60 e 90 dias."],
    ["Fase 3 · A Durabilidade", "meses 7 a 12", "A capacidade rodando sem consultor no meio. Dentro dela: operação sob SLA com presença semanal, relatório de projetado versus realizado e o ritual com a diretoria."],
  ];
  const colW = (W - 0.8) / 3;
  fases.forEach((f, i) => {
    const x = t.PAG.margem + i * (colW + 0.4);
    t.filete(s, x, 3.05, colW, t.OURO, 1.2);
    t.versalete(s, f[0], x, 3.2, { w: colW, size: 10.5 });
    s.addText(f[1], { x, y: 3.5, w: colW, h: 0.3, fontFace: t.SERIF, fontSize: 12, italic: true, color: t.SEC });
    t.corpo(s, f[2], x, 3.85, { w: colW, h: 2.6, size: 11.5, lineSpacing: 16.5 });
  });

  // 8 — o portao da prova
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  t.versalete(s, "O Portão da Prova", t.PAG.margem, 2.0, { size: 12 });
  s.addText("Se em seis semanas o número combinado não apareceu, ou se você simplesmente mudar de ideia, você sai levando tudo o que foi produzido. Sem multa. Sem constrangimento.", {
    x: t.PAG.margem, y: 2.5, w: W, h: 2.2,
    fontFace: t.SERIF, fontSize: 24, bold: true, color: "FFFFFF", lineSpacing: 34,
  });
  t.filete(s, t.PAG.margem, 4.9, 2.2, t.OURO, 1.5);
  s.addText("Se a gente não bater o número, a gente não segue para a próxima fase. O portão retém execução, nunca informação: o retrato de oportunidades é seu, fique ou não.", {
    x: t.PAG.margem, y: 5.15, w: W, h: 0.9,
    fontFace: t.SERIF, fontSize: 15, italic: true, color: "D8DCE8", lineSpacing: 22,
  });

  // 9 — dentro da construcao (portal atual)
  s = slideSecao(pptx, "Dentro da construção", "Engenharia de verdade. E gente formada de verdade.",
    "Arquitetura, integrações com os seus sistemas e agentes com aprovação humana nos pontos certos: erro caro passa por gente antes de acontecer. Em paralelo, a sua equipe estuda em turma própria no nosso portal, uma prática por dia, no trabalho real.");
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("portal--inicio-atual.png"), x: t.PAG.margem + 0.55, y: 3.2, w: 5.9, h: 3.33 });
    s.addImage({ path: assets.fotos("portal--aula-atual.png"), x: t.PAG.margem + 6.75, y: 3.2, w: 5.9, h: 3.33 });
    t.corpo(s, "O portal da turma, como o seu time vê: o início com a prática do dia e uma aula real da formação.",
      t.PAG.margem + 0.55, 6.6, { w: W - 1.1, h: 0.3, size: 10, cor: t.SEC, italic: true, align: "center" });
  }

  // 10 — depois do primeiro ano
  s = slideSecao(pptx, "Depois do primeiro ano", "A relação não termina: ela passa a ser medida todo ano.",
    "Do segundo ano em diante, a empresa opera sozinha e nós ficamos com o que não dá para fazer de dentro:");
  const camadas = [
    ["Operação acompanhada", "SLA, presença semanal e relatório mensal de projetado versus realizado."],
    ["Conselho trimestral", "A pauta de IA da diretoria, preparada e defendida por quem mediu o ano inteiro."],
    ["O Exame Anual de IA", "A re-medição completa da maturidade, comparada ano contra ano: a série histórica que só existe aqui e vale mais a cada ano."],
  ];
  camadas.forEach((c, i) => {
    const y = 2.9 + i * 1.25;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, c[0], t.PAG.margem, y + 0.12, { w: 3.4, size: 10.5 });
    t.corpo(s, c[1], t.PAG.margem + 3.6, y + 0.1, { w: W - 3.6, h: 1.0, size: 13, lineSpacing: 19 });
  });
  t.corpo(s, "É do Exame que sai a fila de oportunidades do ano seguinte: melhorias que só aparecem depois que o fluxo novo existe.",
    t.PAG.margem, 6.6, { w: W, h: 0.5, size: 12.5, serif: true, italic: true, cor: t.NAVY, align: "center" });

  // 11 — conselheiro (o mecanismo + o parecer real)
  s = slideSecao(pptx, "Já tem IA rodando?", "O Conselheiro de IA: a cadeira do seu lado da mesa.",
    "Para quem já construiu: direção de IA em fração, sem o custo nem o conflito de mais um diretor em folha. Funciona em quatro movimentos:");
  const movs = [
    ["Presença", "na diretoria, com a pauta de IA preparada e defendida."],
    ["Roadmap vivo", "re-ranqueado conforme os números chegam. Nunca um PDF parado."],
    ["Arbitragem", "parecer por escrito sobre cada fornecedor que chega à mesa: o que é real, o que é caro, o que é risco."],
    ["Memória", "cada decisão registrada com a expectativa declarada antes e o resultado medido depois. Imutável por construção."],
  ];
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("conselheiro--parecer-arbitragem.jpg"), x: t.PAG.w - t.PAG.margem - 2.62, y: 2.95, w: 2.62, h: 3.7 });
    t.corpo(s, "Um parecer de arbitragem real (empresa preservada).",
      t.PAG.w - t.PAG.margem - 2.62, 6.68, { w: 2.62, h: 0.3, size: 9.5, cor: t.SEC, italic: true, lineSpacing: 13 });
  }
  movs.forEach((m, i) => {
    const y = 3.0 + i * 0.95;
    t.filete(s, t.PAG.margem, y, W - 3.3, t.FILETE_CLARO, 0.75);
    t.versalete(s, m[0], t.PAG.margem, y + 0.1, { w: 2.2, size: 10.5 });
    t.corpo(s, m[1], t.PAG.margem + 2.4, y + 0.08, { w: W - 3.3 - 2.4, h: 0.8, size: 12.5, lineSpacing: 17.5 });
  });
  t.corpo(s,
    "Nenhum time interno pode ser a própria prova: por isso empresa com um ótimo CFO ainda contrata verificação de fora.",
    t.PAG.margem, 6.82, { w: W - 3.3, h: 0.3, size: 10.5, serif: true, italic: true, cor: t.NAVY, lineSpacing: 13 });

  // 12 — raizes + CTA
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  t.versalete(s, "As nossas raízes · o próximo passo", t.PAG.margem, 1.35, { size: 12 });
  s.addText("Verdade dita mesmo quando custa.\nNúmero antes de opinião.\nTerminar com a sua empresa mais capaz, não mais dependente.", {
    x: t.PAG.margem, y: 1.85, w: W, h: 2.3,
    fontFace: t.SERIF, fontSize: 24, bold: true, color: "FFFFFF", lineSpacing: 38,
  });
  t.filete(s, t.PAG.margem, 4.35, 2.2, t.OURO, 1.5);
  s.addText(
    "Adiar isso não é ficar parado: é pagar juro composto na moeda errada. O próximo passo não custa " +
    "nada e cabe em 45 minutos: o Mapa de Vazamento da sua operação.",
    { x: t.PAG.margem, y: 4.65, w: W, h: 1.1, fontFace: t.SERIF, fontSize: 16, italic: true, color: "D8DCE8", lineSpacing: 25 });
  s.addText("ABBA Consultoria de IA · contato@abbaservices.com.br", {
    x: t.PAG.margem, y: 5.95, w: W, h: 0.4,
    fontFace: t.SANS, fontSize: 12, color: "D8DCE8", charSpacing: 1,
  });
};
