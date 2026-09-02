// abba-deck-kickoff — o deck da reuniao de kickoff (12 slides, com {{campos}}).
// Regenerado na V5: as fases do slide 4 viram as 3 fases do Programa com os
// Portoes; SEM travessao; registro formal. Roteiro: 04-entrega/kickoff-roteiro.md.
const t = require("../tema");

function base(pptx, etiqueta, tit, sub) {
  const s = t.novoSlide(pptx);
  t.versalete(s, etiqueta, t.PAG.margem, 0.6);
  s.addText(tit, {
    x: t.PAG.margem, y: 0.98, w: t.PAG.w - 2 * t.PAG.margem, h: 0.85,
    fontFace: t.SERIF, fontSize: 26, bold: true, color: t.NAVY, lineSpacing: 32,
  });
  if (sub) t.corpo(s, sub, t.PAG.margem, 1.9, { w: t.PAG.w - 2 * t.PAG.margem, h: 0.6, size: 12.5, cor: t.SEC, lineSpacing: 18 });
  t.rodape(s, "ABBA · abbaservices.com.br · Confidencial");
  return s;
}

function linhas3col(s, dados, y0, larguras, alt = 0.62) {
  const W = t.PAG.w - 2 * t.PAG.margem;
  dados.forEach((linha, i) => {
    const y = y0 + i * alt;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    let x = t.PAG.margem;
    linha.forEach((cel, j) => {
      t.corpo(s, cel, x, y + 0.08, { w: larguras[j] * W - 0.15, h: alt - 0.1, size: i === 0 ? 10.5 : 12, cor: i === 0 ? t.OURO : t.TEXTO, bold: i === 0, lineSpacing: 15.5 });
      x += larguras[j] * W;
    });
  });
}

module.exports = function gerar(pptx) {
  const W = t.PAG.w - 2 * t.PAG.margem;

  // 1 — capa
  t.capaNavy(pptx, {
    etiqueta: "Kickoff",
    tituloTexto: "{{NOME_DO_CLIENTE}}  ×  ABBA",
    sub: "{{DATA}}   ·   Ref: ABBA-{{ANO}}-{{NUM}}   ·   Confidencial",
  });

  // 2 — quem esta na sala
  let s = base(pptx, "Kickoff · {{CLIENTE}}", "Quem está na sala");
  const col2 = (W - 0.6) / 2;
  t.versalete(s, "{{CLIENTE}}", t.PAG.margem, 2.3, { w: col2 });
  t.corpo(s, "{{Patrocinador, nome e cargo}}  ★\n{{Participante 2}}\n{{Participante 3}}\n{{Participante 4}}", t.PAG.margem, 2.72, { w: col2, h: 2.6, size: 14, lineSpacing: 26 });
  t.versalete(s, "ABBA", t.PAG.margem + col2 + 0.6, 2.3, { w: col2 });
  t.corpo(s, "{{Sócio A}} · Engagement Lead\n{{Sócio B}} · {{papel}}", t.PAG.margem + col2 + 0.6, 2.72, { w: col2, h: 1.4, size: 14, lineSpacing: 26 });

  // 3 — ponto de partida
  s = base(pptx, "O ponto de partida", "Por que estamos aqui");
  t.corpo(s, "Nas palavras de vocês (da descoberta e da proposta):", t.PAG.margem, 2.2, { w: W, h: 0.4, size: 13, cor: t.SEC });
  s.addText("“{{A DOR/OPORTUNIDADE, transcrita nas palavras do cliente}}”", {
    x: t.PAG.margem, y: 2.7, w: W, h: 1.6, fontFace: t.SERIF, fontSize: 20, italic: true, color: t.NAVY, lineSpacing: 30,
  });
  t.filete(s, t.PAG.margem, 4.6, W, t.FILETE_CLARO, 0.75);
  t.versalete(s, "O que contratamos juntos", t.PAG.margem, 4.8);
  t.corpo(s, "{{escopo do Termo do Programa em uma frase: a fase 1 firme e as fases 2 e 3 como opção do Portão da Prova}}", t.PAG.margem, 5.18, { w: W, h: 0.8, size: 14, lineSpacing: 21 });

  // 4 — o programa (V5: as 3 fases)
  s = base(pptx, "O Programa", "O caminho que vamos percorrer");
  const fases = [
    ["Fase", "Período", "O que acontece", "O portão"],
    ["Fase 1 · A Prova", "semanas 1 a 6", "Avaliação profunda + o caso escolhido construído e medido contra a métrica combinada na semana 1", "Portão da Prova: a decisão de continuar volta para vocês"],
    ["Fase 2 · A Construção", "meses 2 a 6", "Casos do portfólio em produção + a turma no portal, com fluência medida", "Portão 2: revisão formal com a diretoria"],
    ["Fase 3 · A Durabilidade", "meses 7 a 12", "Operação assistida, ritual semanal e relatório de projetado versus realizado", "Portão 3: renovação pela Assinatura da Capacidade"],
  ];
  linhas3col(s, fases, 2.25, [0.2, 0.13, 0.37, 0.3], 0.95);
  t.corpo(s, "Cada fase fecha com um Termo de Aceite formal: critérios acordados hoje, validados na entrega. Sem surpresa, sem fase seguinte sem aceite.",
    t.PAG.margem, 6.3, { w: W, h: 0.6, size: 12.5, serif: true, italic: true, cor: t.NAVY, align: "center", lineSpacing: 17 });

  // 5 — a pergunta mais importante
  s = t.novoSlide(pptx);
  t.versalete(s, "A pergunta mais importante de hoje", t.PAG.margem, 0.9);
  s.addText("Onde vocês querem que a empresa esteja em 12 meses, e como IA serve a isso?", {
    x: t.PAG.margem, y: 1.45, w: W, h: 1.5, fontFace: t.SERIF, fontSize: 27, bold: true, color: t.NAVY, lineSpacing: 38,
  });
  ["1.  {{OBJETIVO DECLARADO, escrito AO VIVO, nesta reunião}}",
   "2.  {{OBJETIVO DECLARADO, escrito AO VIVO, nesta reunião}}",
   "3.  {{OBJETIVO DECLARADO, escrito AO VIVO, nesta reunião}}"].forEach((o, i) => {
    t.filete(s, t.PAG.margem, 3.25 + i * 0.85, W, t.FILETE_CLARO, 0.75);
    t.corpo(s, o, t.PAG.margem, 3.38 + i * 0.85, { w: W, h: 0.6, size: 15, lineSpacing: 21 });
  });
  t.corpo(s, "Estes objetivos viram o baseline de TODOS os rituais de alinhamento: cada trimestre, medimos contra eles.",
    t.PAG.margem, 6.1, { w: W, h: 0.5, size: 12.5, serif: true, italic: true, cor: t.NAVY, align: "center" });
  t.rodape(s, "ABBA · abbaservices.com.br · Confidencial");

  // 6 — criterios de sucesso
  s = base(pptx, "Critérios de sucesso", "Como saberemos que deu certo");
  const met = [
    ["Métrica", "Baseline hoje", "Alvo", "Como mediremos"],
    ["{{ex.: horas reinvestidas por pessoa/semana}}", "{{ }}", "{{ }}", "{{ }}"],
    ["{{ }}", "{{ }}", "{{ }}", "{{ }}"],
    ["{{ }}", "{{ }}", "{{ }}", "{{ }}"],
  ];
  linhas3col(s, met, 2.3, [0.4, 0.2, 0.15, 0.25], 0.75);
  t.corpo(s, "Projetado versus realizado em todo relatório: é a nossa promessa central. Resultado verificado, sem enfeite.",
    t.PAG.margem, 5.6, { w: W, h: 0.5, size: 12.5, serif: true, italic: true, cor: t.NAVY, align: "center" });

  // 7 — cronograma
  s = base(pptx, "Quando", "Cronograma e marcos");
  const cron = [
    ["Semana", "Marco", "Critério de aceite"],
    ["{{1}}", "Kickoff (hoje)", "Objetivos, critérios e cronograma aprovados nesta sala"],
    ["{{6}}", "Portão da Prova", "Caso medido contra a métrica combinada + retrato de oportunidades entregue"],
    ["{{ }}", "{{marco da fase 2}}", "{{ }}"],
    ["{{ }}", "{{marco final}}", "{{ }}"],
  ];
  linhas3col(s, cron, 2.25, [0.12, 0.33, 0.55], 0.68);
  t.corpo(s, "Sessões presenciais: {{Kickoff Academy · workshops de marco · graduação}}",
    t.PAG.margem, 5.9, { w: W, h: 0.4, size: 12, cor: t.SEC, align: "center" });

  // 8 — papeis e compromissos
  s = base(pptx, "Honestidade primeiro", "Papéis e compromissos, dos dois lados");
  t.versalete(s, "O que a ABBA entrega", t.PAG.margem, 2.25, { w: col2 });
  t.corpo(s, "Condução de todas as fases, com os fundadores\nEntregáveis formais com critério de aceite\nReunião semanal de 30 min com o patrocinador\nResposta em até 1 dia útil",
    t.PAG.margem, 2.68, { w: col2, h: 2.6, size: 13, lineSpacing: 24 });
  t.versalete(s, "O que precisamos de vocês", t.PAG.margem + col2 + 0.6, 2.25, { w: col2 });
  t.corpo(s, "Patrocinador com autoridade para mobilizar\nParticipação da equipe no pré-trabalho e sessões\nAcessos e integrações acordados: {{lista}}\nDecisões nos portões: vocês decidem, nós executamos",
    t.PAG.margem + col2 + 0.6, 2.68, { w: col2, h: 2.6, size: 13, lineSpacing: 24 });

  // 9 — comunicacao
  s = base(pptx, "Comunicação", "Como vamos nos falar");
  const com = [
    ["Canal", "Uso"],
    ["Canal do projeto", "{{Slack/Teams do cliente, canal dedicado}}: dia a dia e logística"],
    ["E-mail", "Decisões, escopo, entregáveis. A trilha formal ({{nome}}@abbaservices.com.br)"],
    ["Reunião semanal", "{{dia/hora}} · 30 min · patrocinador + ABBA: progresso, bloqueios, próximos 7 dias"],
    ["Ritual da diretoria", "Ao fim de cada fase e trimestralmente: resultados contra os objetivos declarados"],
  ];
  linhas3col(s, com, 2.25, [0.22, 0.78], 0.72);

  // 10 — lgpd
  s = base(pptx, "LGPD e confidencialidade", "Seus dados, com respeito");
  const lgpd = [
    ["Papéis", "Vocês: Controlador · ABBA: Operadora. Tratamos dados sob suas instruções documentadas"],
    ["Segurança", "Ambiente segregado por cliente, criptografia, trilha de auditoria"],
    ["Decisões automatizadas", "Todo agente tem ponto de aprovação humana e inventário mapeado ao Art. 20"],
    ["O que NUNCA fazemos", "Treinar modelos com dados de vocês · dado de cliente fora do ambiente do projeto"],
  ];
  lgpd.forEach((l, i) => {
    const y = 2.35 + i * 1.05;
    t.filete(s, t.PAG.margem, y, W, t.FILETE_CLARO, 0.75);
    t.versalete(s, l[0], t.PAG.margem, y + 0.12, { w: 3.3, size: 10.5 });
    t.corpo(s, l[1], t.PAG.margem + 3.5, y + 0.1, { w: W - 3.5, h: 0.85, size: 12.5, lineSpacing: 18 });
  });

  // 11 — proximos 7 dias
  s = base(pptx, "Ação imediata", "Os próximos 7 dias");
  const acoes = [
    ["Ação", "Dono", "Até"],
    ["{{Pré-trabalho disparado aos participantes}}", "ABBA", "{{data}}"],
    ["{{Acessos e integrações liberados}}", "{{Cliente}}", "{{data}}"],
    ["{{Primeira entrevista agendada}}", "Ambos", "{{data}}"],
    ["Ata deste kickoff no e-mail de vocês", "ABBA", "24h"],
  ];
  linhas3col(s, acoes, 2.3, [0.6, 0.2, 0.2], 0.68);

  // 12 — fecho
  s = t.novoSlide(pptx, { fundo: t.NAVY });
  s.addText("Obrigado. Agora é execução.", {
    x: t.PAG.margem, y: 2.5, w: W, h: 0.9, fontFace: t.SERIF, fontSize: 34, bold: true, color: "FFFFFF",
  });
  t.filete(s, t.PAG.margem, 3.55, 2.2, t.OURO, 1.5);
  s.addText("Nós recomendamos com convicção. Vocês decidem. E medimos tudo: projetado versus realizado, do primeiro dia à graduação.", {
    x: t.PAG.margem, y: 3.85, w: W, h: 1.0, fontFace: t.SERIF, fontSize: 17, italic: true, color: "D8DCE8", lineSpacing: 26,
  });
  s.addText("{{nome}}@abbaservices.com.br · abbaservices.com.br", {
    x: t.PAG.margem, y: 5.1, w: W, h: 0.4, fontFace: t.SANS, fontSize: 12, color: "D8DCE8", charSpacing: 1,
  });
};
