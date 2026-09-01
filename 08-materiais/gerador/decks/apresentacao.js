// abba-apresentacao — o documento-padrao de envio (3 paginas, 16:9).
// Padrao editorial: abre direto na ABBA, historia em ordem, SEM precos,
// SEM travessao (regra do socio, 2026-09-01), a voz do pitch do palco:
// IA na ponta vs. na veia, numero combinado antes e medido depois,
// prova e nao impressao, a primeira parede paga a fundacao.
const t = require("../tema");

module.exports = function gerar(pptx, assets) {
  const W = t.PAG.w - 2 * t.PAG.margem;

  // ---------- PAGINA 1 — capa + o gancho + raizes ----------
  let s = t.novoSlide(pptx);
  t.versalete(s, "ABBA · Consultoria de IA", t.PAG.margem, 0.7);
  s.addText("Tornamos a sua empresa AI native.", {
    x: t.PAG.margem, y: 1.1, w: W, h: 1.1,
    fontFace: t.SERIF, fontSize: 40, bold: true, color: t.NAVY,
  });
  t.filete(s, t.PAG.margem, 2.32, 2.2, t.OURO, 1.5);

  t.corpo(s,
    "De cada dez empresas que decidiram usar IA este ano, mais de oito não vão conseguir " +
    "mostrar um número no fim. E não é por falta de tecnologia: é porque a IA entrou pelo " +
    "lugar errado. Quando entra pela ponta, uma pessoa pede e recebe, e o ganho fica com ela. " +
    "Se ela sai amanhã, o ganho sai junto pela porta. Quando entra pela veia, dentro do " +
    "processo, o organismo passa a funcionar diferente. E o ganho fica na empresa.",
    t.PAG.margem, 2.6, { w: W, h: 1.45, size: 15, lineSpacing: 23 });

  t.corpo(s,
    "A pesquisa mais séria que existe sobre isso, da RAND, mediu: mais de 80% dos projetos de " +
    "IA falham, o dobro dos projetos comuns de tecnologia. A causa número um não foi a qualidade " +
    "do modelo. Foi começar sem ninguém combinar o que seria dar certo. É exatamente aí que " +
    "trabalhamos: escolhemos um processo que dói, fazemos a IA rodar dentro dele até virar parte " +
    "da operação, formamos as pessoas que vivem nesse processo e provamos, de fora, o que mudou. " +
    "Número combinado antes, medido depois. No fim, a diretoria tem prova, não impressão.",
    t.PAG.margem, 4.15, { w: W, h: 1.35, size: 13.5, cor: t.SEC, lineSpacing: 20 });

  t.filete(s, t.PAG.margem, 5.6, W, t.FILETE_CLARO, 0.75);
  t.versalete(s, "As nossas raízes", t.PAG.margem, 5.78);
  t.corpo(s,
    "Trabalhamos com raízes: verdade dita mesmo quando custa, número antes de opinião, e o " +
    "compromisso de terminar com a sua empresa mais capaz, não mais dependente. O que instalamos " +
    "fica com você: os sistemas, as pessoas formadas e o registro de tudo o que foi decidido e medido.",
    t.PAG.margem, 6.14, { w: W, h: 0.85, size: 13, serif: true, italic: true, lineSpacing: 19.5 });
  t.rodape(s);

  // ---------- PAGINA 2 — o Programa em 3 fases, com o que compoe cada uma ----------
  s = t.novoSlide(pptx);
  t.versalete(s, "O caminho", t.PAG.margem, 0.6);
  s.addText("Da primeira conversa à capacidade instalada: um programa, um ano.", {
    x: t.PAG.margem, y: 0.95, w: W, h: 0.8,
    fontFace: t.SERIF, fontSize: 25, bold: true, color: t.NAVY,
  });
  t.corpo(s,
    "Tudo começa com um mapa do que estimamos estar vazando, feito de fora e sem custo. Ninguém " +
    "espera o terreno ficar perfeito para começar a obra: escolhemos juntos a primeira parede, e é " +
    "ela que paga a fundação do resto. Cada fase termina numa porta de saída limpa.",
    t.PAG.margem, 1.78, { w: W, h: 0.72, size: 12.5, cor: t.SEC, lineSpacing: 18.5 });

  const colW = (W - 0.8) / 3;
  const fases = [
    {
      rot: "Fase 1 · A Prova", tempo: "seis semanas",
      oque: "Um caso construído com os seus dados, rodando e medido contra a métrica combinada por escrito na primeira semana.",
      dentro: "Dentro dela: a avaliação profunda, do conselho à linha de frente · o protótipo em uso real · o retrato completo de oportunidades, ranqueado por retorno e esforço.",
      porque: "Porque promessa não decide investimento. Número decide.",
    },
    {
      rot: "Fase 2 · A Construção", tempo: "meses dois a seis",
      oque: "Os casos aprovados entram em produção e a sua equipe aprende a operar e a criar junto.",
      dentro: "Dentro dela: arquitetura, integrações e agentes com aprovação humana nos pontos certos · a turma da sua equipe no nosso portal, com fluência medida em 30, 60 e 90 dias.",
      porque: "Porque sistema novo com a empresa pensando do jeito antigo não transforma nada.",
    },
    {
      rot: "Fase 3 · A Durabilidade", tempo: "meses sete a doze",
      oque: "A capacidade rodando no dia a dia, com a nossa mão cada vez mais leve, de propósito.",
      dentro: "Dentro dela: operação sob SLA com presença semanal · relatório mensal de projetado versus realizado · o ritual com a diretoria e o registro de cada decisão.",
      porque: "Porque a única prova que importa é funcionar sem consultor no meio.",
    },
  ];
  fases.forEach((f, i) => {
    const x = t.PAG.margem + i * (colW + 0.4);
    t.filete(s, x, 2.62, colW, t.OURO, 1.2);
    t.versalete(s, f.rot, x, 2.76, { w: colW, size: 10.5 });
    s.addText(f.tempo, { x, y: 3.06, w: colW, h: 0.28, fontFace: t.SERIF, fontSize: 11.5, italic: true, color: t.SEC });
    t.corpo(s, f.oque, x, 3.38, { w: colW, h: 1.1, size: 11.5, lineSpacing: 16 });
    t.corpo(s, f.dentro, x, 4.52, { w: colW, h: 1.55, size: 10.5, cor: t.SEC, lineSpacing: 15 });
    t.corpo(s, f.porque, x, 6.1, { w: colW, h: 0.62, size: 10.5, cor: t.NAVY, italic: true, lineSpacing: 15 });
  });

  s.addText(
    "O Portão da Prova: ao fim da fase 1 a decisão volta para a sua mão. Se o número não apareceu, " +
    "ou se você simplesmente mudar de ideia, você sai levando tudo o que foi produzido. Sem multa e sem constrangimento.",
    { x: t.PAG.margem, y: 6.68, w: W, h: 0.42,
      fontFace: t.SERIF, fontSize: 11, italic: true, color: t.NAVY, align: "center", lineSpacing: 14 });

  // ---------- PAGINA 3 — a relacao que continua + Conselheiro + parceiros + CTA ----------
  s = t.novoSlide(pptx);
  t.versalete(s, "Depois do primeiro ano", t.PAG.margem, 0.6);
  s.addText("A relação não termina: ela passa a ser medida todo ano.", {
    x: t.PAG.margem, y: 0.95, w: W, h: 0.75,
    fontFace: t.SERIF, fontSize: 25, bold: true, color: t.NAVY,
  });
  t.corpo(s,
    "Do segundo ano em diante a empresa opera sozinha, e nós ficamos com o que não dá para fazer " +
    "de dentro: a operação acompanhada, o conselho trimestral e o Exame Anual de IA, a re-medição " +
    "completa da maturidade, comparada ano contra ano. A série histórica que nasce daí só existe " +
    "aqui, vale mais a cada ano, e é dela que sai a fila de oportunidades do ano seguinte.",
    t.PAG.margem, 1.75, { w: W, h: 1.15, size: 13, lineSpacing: 19.5 });

  t.filete(s, t.PAG.margem, 3.05, W, t.FILETE_CLARO, 0.75);
  t.versalete(s, "Já tem IA rodando? O Conselheiro de IA", t.PAG.margem, 3.22);
  t.corpo(s,
    "Para quem já construiu, a oferta é outra: a cadeira de direção de IA do seu lado da mesa, em " +
    "fração. Funciona em quatro movimentos: presença recorrente na diretoria · o roadmap vivo, " +
    "re-ranqueado conforme os números chegam · parecer por escrito sobre cada fornecedor que " +
    "aparece · e a memória de decisão, com a expectativa declarada antes e o resultado medido " +
    "depois, que nunca se apaga. Nenhum time interno pode ser a própria prova. É por isso que " +
    "empresa com um ótimo CFO ainda contrata quem verifique as contas de fora.",
    t.PAG.margem, 3.58, { w: W, h: 1.35, size: 12.5, lineSpacing: 18.5 });

  t.filete(s, t.PAG.margem, 5.05, W, t.FILETE_CLARO, 0.75);
  t.versalete(s, "Parceiros oficiais", t.PAG.margem, 5.22);
  if (assets.logoMicrosoft) {
    s.addImage({ path: assets.logoMicrosoft, x: t.PAG.margem, y: 5.6, h: 0.34, w: 1.57 });
  }
  if (assets.logoCrewai) {
    s.addImage({ path: assets.logoCrewai, x: t.PAG.margem + 2.0, y: 5.54, h: 0.44, w: 1.45 });
  }
  t.corpo(s,
    "Durante a capacitação, a sua equipe usa ferramentas dos nossos parceiros para construir " +
    "as próprias soluções.",
    t.PAG.margem + 4.0, 5.52, { w: W - 4.0, h: 0.5, size: 11.5, cor: t.SEC, lineSpacing: 16 });

  s.addText("O próximo passo não custa nada e cabe em 45 minutos: o Mapa de Vazamento da sua operação.", {
    x: t.PAG.margem, y: 6.35, w: W, h: 0.55,
    fontFace: t.SERIF, fontSize: 15, bold: true, color: t.NAVY, align: "center",
  });
  t.rodape(s);
};
