// abba-deck-institucional — o deck de apresentacao AO VIVO (15 slides).
// Registro FORMAL (plateia: diretoria) — feedback do socio 2026-09-01:
// a base e a apresentacao antiga comprovada (o que · por que · como, as
// duas frentes, prometemos/recusamos); do pitch ficam apenas o gancho,
// a leitura ponta/veia e o Portao (reescrito formal). SEM precos, SEM
// travessao, sem frases de efeito no fecho.
// Regua: RAND >80% com fonte; METR; DORA; nunca "garantia", nunca
// "auditoria" (Exame Anual), nunca acuracia prometida.
const t = require("../tema");

function slideSecao(pptx, etiqueta, tit, sub, subW) {
  const s = t.novoSlide(pptx);
  t.versalete(s, etiqueta, t.PAG.margem, 0.6);
  s.addText(tit, {
    x: t.PAG.margem, y: 0.98, w: t.PAG.w - 2 * t.PAG.margem, h: 0.95,
    fontFace: t.SERIF, fontSize: 27, bold: true, color: t.NAVY, lineSpacing: 33,
  });
  if (sub) t.corpo(s, sub, t.PAG.margem, 1.98, { w: subW || t.PAG.w - 2 * t.PAG.margem, h: 0.7, size: 12.5, cor: t.SEC, lineSpacing: 18.5 });
  t.rodape(s);
  return s;
}

// bloco "N · servico" com O QUE / POR QUE / COMO condensados
function blocoServico(s, x, y, w, titulo, linhas) {
  t.filete(s, x, y, w, t.OURO, 1.2);
  t.versalete(s, titulo, x, y + 0.13, { w, size: 10.5 });
  let yy = y + 0.5;
  linhas.forEach(([rot, txt, altura]) => {
    s.addText(rot, { x, y: yy, w: 1.05, h: 0.28, fontFace: t.SANS, fontSize: 8.5, bold: true, color: t.OURO, charSpacing: 2 });
    t.corpo(s, txt, x + 1.1, yy - 0.02, { w: w - 1.1, h: altura, size: 10.5, lineSpacing: 14.5 });
    yy += altura + 0.12;
  });
  return yy;
}

module.exports = function gerar(pptx, assets) {
  const W = t.PAG.w - 2 * t.PAG.margem;

  // 1 — capa
  t.capaNavy(pptx, {
    etiqueta: "ABBA · Consultoria de Inteligência Artificial",
    tituloTexto: "Tornamos a sua empresa AI native.",
    sub: "Capacidade de IA construída em escala. E provada, como terceiro: número combinado antes, medido depois.",
  });

  // 2 — quem somos (a abertura antiga, comprovada)
  let s = slideSecao(pptx, "Quem somos", "Uma consultoria de inteligência artificial.");
  t.corpo(s,
    "Entramos na sua empresa para entendê-la a fundo, construímos as soluções certas para o seu " +
    "fluxo de trabalho, validamos cada uma com dados reais antes de qualquer investimento pesado, " +
    "formamos as suas pessoas e ficamos ao seu lado acompanhando, mês a mês, o que mudou.",
    t.PAG.margem, 2.25, { w: W, h: 1.3, size: 15.5, lineSpacing: 24 });
  t.filete(s, t.PAG.margem, 3.85, W, t.FILETE_CLARO, 0.75);
  t.corpo(s,
    "Nos próximos minutos, o caminho completo, da primeira conversa à cadeira de estrategista na " +
    "sua diretoria: o que fazemos em cada etapa, por quê, e como.",
    t.PAG.margem, 4.1, { w: W, h: 0.85, size: 13.5, cor: t.SEC, lineSpacing: 20 });
  t.corpo(s,
    "O nosso processo começa com quem decide e só termina quando chega a quem executa. Uma empresa não muda por uma ponta só.",
    t.PAG.margem, 5.3, { w: W, h: 0.8, size: 14, serif: true, italic: true, cor: t.NAVY, lineSpacing: 21 });

  // 3 — o gancho (aprovado)
  s = t.novoSlide(pptx);
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

  // 4 — as duas frentes + a leitura ponta/veia
  s = slideSecao(pptx, "Onde o trabalho acontece", "Duas frentes, ao mesmo tempo.",
    "Implantamos as nossas soluções dentro do fluxo de trabalho e dos processos da empresa, e nas pessoas que os vivem. As duas frentes andam juntas por desenho.");
  const duasFrentes = [
    ["Nos processos", "Projetamos e implantamos sistemas inteligentes: arquitetura, integrações e agentes de IA trabalhando em conjunto, que tornam a operação mais eficiente, mais rápida e mais poderosa."],
    ["Nas pessoas", "Formamos cada nível da equipe para trabalhar com IA e enxergar o próprio trabalho de um jeito novo, do conselho à linha de frente."],
  ];
  const colW2 = (W - 0.6) / 2;
  duasFrentes.forEach((d, i) => {
    const x = t.PAG.margem + i * (colW2 + 0.6);
    t.filete(s, x, 2.85, colW2, t.OURO, 1.2);
    t.versalete(s, d[0], x, 3.0, { w: colW2, size: 11 });
    t.corpo(s, d[1], x, 3.4, { w: colW2, h: 1.7, size: 13, lineSpacing: 19.5 });
  });
  t.filete(s, t.PAG.margem, 5.3, W, t.FILETE_CLARO, 0.75);
  t.corpo(s,
    "É a diferença entre a IA na ponta e a IA na veia: na ponta, uma pessoa pede e recebe, e o ganho " +
    "vai embora com ela. Na veia, dentro do processo e das pessoas, o ganho fica na empresa, mesmo " +
    "quando as pessoas mudam. De nada adiantam sistemas novos com a empresa pensando do jeito antigo.",
    t.PAG.margem, 5.55, { w: W, h: 1.1, size: 13.5, serif: true, italic: true, cor: t.NAVY, lineSpacing: 20 });

  // 5 — as tres medicoes (aprovado)
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

  // 6 — o mapa (porta unica)
  s = slideSecao(pptx, "Como toda conversa começa", "O Mapa de Vazamento: gratuito, feito de fora, com um número dentro.",
    "Antes de qualquer contrato, entregamos um mapa do que estimamos estar vazando na sua operação: onde, quanto por mês, e o que faríamos primeiro. Ninguém deveria pagar para descobrir se faz sentido. Se o número não convencer, a conversa termina ali, sem custo e sem compromisso.");
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("mapa-de-vazamento--pagina-real.jpg"), x: t.PAG.w / 2 - 1.7, y: 3.15, w: 3.4, h: 3.74 });
  }

  // 7 — o programa (visao geral)
  s = slideSecao(pptx, "O caminho", "Um programa, um ano, três fases. E três portas de saída.",
    "Cada etapa entrega algo inteiro sozinha e produz o insumo da próxima. A decisão do ano é tomada uma vez; o risco, fase a fase: cada uma termina num portão onde a decisão volta para a sua mão.");
  const fasesResumo = [
    ["Fase 1 · A Prova", "seis semanas", "O Assessment: o mergulho profundo, do conselho à linha de frente. E o protótipo do caso mais promissor, construído com os seus dados reais e medido contra o critério combinado por escrito."],
    ["Fase 2 · A Construção", "meses 2 a 6", "A engenharia da solução: sistemas sob medida em produção, com aprovação humana no que é crítico. E o treinamento de todos os níveis, na nossa plataforma própria e em sessões presenciais."],
    ["Fase 3 · A Durabilidade", "meses 7 a 12", "A operação com presença: monitoramento, evolução contínua, ritual semanal com quem decide e o relatório mensal de projetado versus realizado."],
  ];
  const colW = (W - 0.8) / 3;
  fasesResumo.forEach((f, i) => {
    const x = t.PAG.margem + i * (colW + 0.4);
    t.filete(s, x, 3.05, colW, t.OURO, 1.2);
    t.versalete(s, f[0], x, 3.2, { w: colW, size: 10.5 });
    s.addText(f[1], { x, y: 3.5, w: colW, h: 0.3, fontFace: t.SERIF, fontSize: 12, italic: true, color: t.SEC });
    t.corpo(s, f[2], x, 3.85, { w: colW, h: 2.4, size: 11.5, lineSpacing: 16.5 });
  });
  t.corpo(s, "Os três slides seguintes abrem cada fase: o que cada serviço faz, por quê, e o que fica com você.",
    t.PAG.margem, 6.55, { w: W, h: 0.4, size: 11.5, cor: t.SEC, italic: true, align: "center" });

  // 8 — FASE 1 por dentro: assessment + prototipo
  s = slideSecao(pptx, "Fase 1 · A Prova · por dentro", "O mergulho que revela, e a prova antes do investimento.", null);
  {
    const fw = 2.35, fx = t.PAG.w - t.PAG.margem - fw;
    if (assets && assets.fotos) {
      s.addImage({ path: assets.fotos("assessment--relatorio-interno.jpg"), x: fx, y: 2.15, w: fw, h: 3.32 });
      t.corpo(s, "Página do relatório de maturidade (modelo).", fx, 5.5, { w: fw, h: 0.4, size: 9, cor: t.SEC, italic: true, lineSpacing: 12 });
    }
    const tw = fx - 0.5 - t.PAG.margem;
    let y = blocoServico(s, t.PAG.margem, 2.15, tw, "O Assessment · o mergulho profundo", [
      ["O QUÊ", "Entramos na empresa e entendemos, do conselho à linha de frente, como o trabalho realmente flui: onde quebra, onde vaza valor, quem decide o quê. Entrevistas em todos os níveis, analisadas com a nossa ferramenta própria.", 0.72],
      ["POR QUÊ", "Solução genérica falha. O que separa o investimento certo do desperdício é entender onde, no seu fluxo, existe valor preso. O Assessment transforma opinião em portfólio priorizado, com número.", 0.66],
      ["O QUE FICA", "O relatório de maturidade, o portfólio de oportunidades ranqueado e quantificado, e o plano diretor: o que fazer, em que ordem, e por quê. Não uma lista de ideias.", 0.62],
    ]);
    blocoServico(s, t.PAG.margem, y + 0.15, tw, "O Protótipo de caso de uso · a prova", [
      ["O QUÊ", "O caso mais promissor do portfólio, construído com os seus dados reais e testado pelas pessoas que vão usá-lo, contra critérios de sucesso combinados por escrito antes da primeira linha de código.", 0.68],
      ["POR QUÊ", "Ninguém investe no escuro: o investimento grande só acontece depois que o caso provou, com números, que merece. A diretoria decide GO ou NO-GO com números na mesa. E NO-GO também é resultado: custou pouco e evitou um investimento errado.", 0.8],
    ]);
  }

  // 9 — FASE 2 por dentro: construcao + treinamento
  s = slideSecao(pptx, "Fase 2 · A Construção · por dentro", "A engenharia da solução, e a mentalidade nova.", null);
  {
    let y = blocoServico(s, t.PAG.margem, 2.15, W, "Construção e implantação · a engenharia da solução", [
      ["O QUÊ", "Projetamos a arquitetura: dados, integrações e lógica de decisão. E construímos sistemas inteligentes sob medida, com agentes de IA inseridos onde fazem diferença, em produção no fluxo real da sua equipe.", 0.52],
      ["POR QUÊ", "Relatório na gaveta não muda empresa. Sistema rodando muda. E engenharia importa: solução montada às pressas quebra no primeiro mês; a nossa é projetada para conviver com os seus sistemas e crescer com a operação.", 0.52],
      ["COMO", "Arquitetura primeiro; aprovação humana em tudo que é crítico (a IA executa, gente da sua confiança valida); na sua infraestrutura ou em nuvem; testes de aceite antes de o sistema assumir o trabalho real.", 0.5],
    ]);
    y = blocoServico(s, t.PAG.margem, y + 0.1, W, "Treinamento + ABBA Portal · a mentalidade nova", [
      ["O QUÊ", "Todos os níveis da equipe, na nossa plataforma própria e em sessões presenciais: trilhas por papel, desafios aplicados no trabalho real, fluência medida em 30, 60 e 90 dias, campeões internos formados.", 0.5],
      ["POR QUÊ", "O objetivo não é ensinar ferramenta: é instalar em cada pessoa as três perguntas que mudam o olhar sobre o próprio trabalho. O que posso parar de fazer? O que posso começar a fazer? O que só eu faço, e devo fazer ainda melhor?", 0.52],
    ]);
  }

  // 10 — FASE 2: o portal ao vivo (fotos atuais)
  s = slideSecao(pptx, "Fase 2 · a plataforma própria", "O portal da turma, como o seu time vê.",
    "Uma prática por dia, no trabalho real: o início com a prática do dia, e as aulas da formação. O avanço na trilha desbloqueia ferramentas novas, e a fluência é medida semanas depois: se o comportamento mudou de verdade, não se o vídeo foi assistido.");
  if (assets && assets.fotos) {
    s.addImage({ path: assets.fotos("portal--inicio-atual.png"), x: t.PAG.margem + 0.55, y: 3.15, w: 5.9, h: 3.33 });
    s.addImage({ path: assets.fotos("portal--aula-atual.png"), x: t.PAG.margem + 6.75, y: 3.15, w: 5.9, h: 3.33 });
  }

  // 11 — FASE 3 por dentro: sistemas gerenciados
  s = slideSecao(pptx, "Fase 3 · A Durabilidade · por dentro", "A operação com presença.", null);
  {
    const fw = 2.35, fx = t.PAG.w - t.PAG.margem - fw;
    if (assets && assets.fotos) {
      s.addImage({ path: assets.fotos("gerenciados--relatorio-mensal.jpg"), x: fx, y: 2.15, w: fw, h: 3.32 });
      t.corpo(s, "Relatório mensal real de operação (empresa preservada).", fx, 5.5, { w: fw, h: 0.4, size: 9, cor: t.SEC, italic: true, lineSpacing: 12 });
    }
    const tw = fx - 0.5 - t.PAG.margem;
    blocoServico(s, t.PAG.margem, 2.15, tw, "Sistemas gerenciados · a operação com presença", [
      ["O QUÊ", "Operamos o que construímos: monitoramento contínuo, correção e evolução dos sistemas em produção, e um ritual semanal de 20 minutos com quem decide.", 0.55],
      ["POR QUÊ", "Sistema sem dono definha. E a diretoria precisa ver o retorno, não sentir que ele existe: a maioria das empresas que investe em IA não consegue dizer o que mudou, porque ninguém combinou antes o que seria mudança, nem mediu depois.", 0.78],
      ["COMO", "Alertas de máquina o tempo todo, com prazos de resposta por severidade. Evolução dentro do combinado; o que exceder é cotado antes, nunca fatura-surpresa. E o relatório mensal: projetado versus realizado, sempre.", 0.72],
      ["O QUE FICA", "O diário de decisões: métrica combinada antes, resultado medido depois, assinado por gente. Incluindo o que não funcionou. É o registro que transforma a conversa de renovação em leitura de resultados, não em ato de fé.", 0.75],
    ]);
  }

  // 12 — o portao da prova (formal)
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  t.versalete(s, "O Portão da Prova", t.PAG.margem, 1.85, { size: 12 });
  s.addText("Ao término da fase 1, a decisão de continuar é integralmente sua.", {
    x: t.PAG.margem, y: 2.35, w: W, h: 1.1,
    fontFace: t.SERIF, fontSize: 26, bold: true, color: "FFFFFF", lineSpacing: 36,
  });
  t.filete(s, t.PAG.margem, 3.7, 2.2, t.OURO, 1.5);
  s.addText(
    "Se o resultado medido não confirmar o critério combinado em contrato, o Programa se encerra " +
    "ali: sem multa, sem renegociação, e com todos os entregáveis da fase em suas mãos. Os portões " +
    "se repetem no mês seis e no mês doze. Nenhuma fase se inicia sem que a anterior tenha " +
    "comprovado o seu resultado.",
    { x: t.PAG.margem, y: 4.0, w: W, h: 1.5, fontFace: t.SERIF, fontSize: 15.5, color: "D8DCE8", lineSpacing: 25 });

  // 13 — depois do primeiro ano (aprovado)
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

  // 14 — conselheiro (especificado como os demais servicos)
  s = slideSecao(pptx, "Já tem IA rodando?", "O Conselheiro de IA: do seu lado da mesa.", null);
  {
    const fw = 2.3, fx = t.PAG.w - t.PAG.margem - fw;
    if (assets && assets.fotos) {
      s.addImage({ path: assets.fotos("conselheiro--parecer-arbitragem.jpg"), x: fx, y: 2.15, w: fw, h: 3.25 });
      t.corpo(s, "Um parecer de arbitragem real (empresa preservada).", fx, 5.43, { w: fw, h: 0.4, size: 9, cor: t.SEC, italic: true, lineSpacing: 12 });
    }
    const tw = fx - 0.5 - t.PAG.margem;
    blocoServico(s, t.PAG.margem, 2.15, tw, "A cadeira de estrategista de IA da sua empresa", [
      ["O QUÊ", "Um estrategista presente na sua diretoria, em regime recorrente: o roadmap de IA vivo e revisado a cada ciclo, a governança vigiada, e análise independente de qualquer proposta de fornecedor que chegar à sua mesa.", 0.72],
      ["POR QUÊ", "Todo fornecedor de IA tem um vendedor. A sua mesa merece alguém do seu lado quando a fatura chega: isso é real? é para nós? qual o preço justo? Por escrito e sem conflito de interesse.", 0.68],
      ["COMO", "Presença estruturada, com no máximo três recomendações priorizadas por encontro. Cada recomendação entra no registro com o número que dirá, depois, se deu certo. Cada parecer de fornecedor sai em até cinco dias úteis.", 0.72],
      ["AS PORTAS", "A porta natural: ao fim do Programa, a cadeira dá continuidade ao que foi construído. A porta direta: para quem já tem IA rodando e não tem quem dirija. Não precisa do Programa para ter a cadeira.", 0.68],
    ]);
  }

  // 15 — como trabalhamos + prometemos e recusamos + proximo passo
  s = slideSecao(pptx, "Como trabalhamos", "Prova, não impressão.",
    "Toda decisão entra num diário: métrica combinada antes, resultado medido depois. E vocês veem o registro inteiro, incluindo o que não funcionou. A IA rascunha, um humano assina, a diretoria decide.");
  const cols = [
    ["Prometemos", "O método: métrica combinada antes, medida depois, num registro que vocês veem inteiro. · Presença recorrente de quem decide, não um relatório na gaveta. · Honestidade sobre escopo: o que fazemos, nomeado, e o que fica de fora."],
    ["Recusamos", "Prometer acurácia que não medimos. · Prever o imprevisível: não vendemos oráculo. · Piloto sem métrica: é a receita documentada do fracasso. · IA decidindo sozinha: a IA rascunha, um humano assina, a diretoria decide."],
  ];
  cols.forEach((c, i) => {
    const x = t.PAG.margem + i * (colW2 + 0.6);
    t.filete(s, x, 3.15, colW2, t.OURO, 1.2);
    t.versalete(s, c[0], x, 3.3, { w: colW2, size: 11 });
    t.corpo(s, c[1], x, 3.7, { w: colW2, h: 1.9, size: 11.5, lineSpacing: 17 });
  });
  t.filete(s, t.PAG.margem, 5.8, W, t.FILETE_CLARO, 0.75);
  if (assets) {
    if (assets.logoMicrosoft) s.addImage({ path: assets.logoMicrosoft, x: t.PAG.margem, y: 6.0, h: 0.3, w: 1.39 });
    if (assets.logoCrewai) s.addImage({ path: assets.logoCrewai, x: t.PAG.margem + 1.8, y: 5.95, h: 0.4, w: 1.32 });
  }
  t.corpo(s,
    "A história começa com uma conversa de 45 minutos, e com o seu Mapa de Vazamento, gratuito. contato@abbaservices.com.br",
    t.PAG.margem + 3.6, 5.98, { w: W - 3.6, h: 0.55, size: 12.5, serif: true, cor: t.NAVY, lineSpacing: 18 });
};
