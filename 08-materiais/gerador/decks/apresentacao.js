// abba-apresentacao — o documento-padrao de envio (3 paginas, 16:9).
// Registro formal (feedback do socio 2026-09-01): a base e a apresentacao
// antiga comprovada; do pitch ficam o gancho e a leitura ponta/veia.
// Cada fase nomeia os servicos embutidos, com o que · por que · como.
// SEM precos, SEM travessao, sem frases de efeito.
const t = require("../tema");

// bloco de servico numerado: rotulo dourado + 3 linhas O QUE/POR QUE/COMO
function servico(s, x, y, w, titulo, linhas) {
  t.filete(s, x, y, w, t.OURO, 1.1);
  t.versalete(s, titulo, x, y + 0.11, { w, size: 10 });
  let yy = y + 0.44;
  linhas.forEach(([rot, txt, h]) => {
    s.addText(rot, { x, y: yy, w: 0.95, h: 0.25, fontFace: t.SANS, fontSize: 8, bold: true, color: t.OURO, charSpacing: 2 });
    t.corpo(s, txt, x + 1.0, yy - 0.03, { w: w - 1.0, h, size: 10, lineSpacing: 13.5 });
    yy += h + 0.08;
  });
  return yy;
}

module.exports = function gerar(pptx, assets) {
  const W = t.PAG.w - 2 * t.PAG.margem;

  // ---------- PAGINA 1 — capa + quem somos + o gancho + raizes ----------
  let s = t.novoSlide(pptx);
  t.versalete(s, "ABBA · Consultoria de IA", t.PAG.margem, 0.65);
  s.addText("Tornamos a sua empresa AI native.", {
    x: t.PAG.margem, y: 1.02, w: W, h: 1.05,
    fontFace: t.SERIF, fontSize: 38, bold: true, color: t.NAVY,
  });
  t.filete(s, t.PAG.margem, 2.18, 2.2, t.OURO, 1.5);

  t.corpo(s,
    "A ABBA é uma consultoria de inteligência artificial. Entramos na sua empresa para entendê-la a " +
    "fundo, construímos as soluções certas para o seu fluxo de trabalho, validamos cada uma com dados " +
    "reais antes de qualquer investimento pesado, formamos as suas pessoas e ficamos ao seu lado " +
    "acompanhando, mês a mês, o que mudou. O trabalho acontece em duas frentes ao mesmo tempo: nos " +
    "processos, com sistemas inteligentes implantados dentro do fluxo real, e nas pessoas, formadas " +
    "para enxergar o próprio trabalho de um jeito novo.",
    t.PAG.margem, 2.45, { w: W, h: 1.6, size: 14, lineSpacing: 21.5 });

  t.corpo(s,
    "Por que assim? De cada dez empresas que decidiram usar IA este ano, mais de oito não vão " +
    "conseguir mostrar um número no fim (RAND: mais de 80% dos projetos falham, o dobro dos projetos " +
    "comuns de tecnologia, e a causa número um é começar sem combinar o que seria dar certo). Não é " +
    "falta de tecnologia: é a IA entrando pela ponta, na mão de uma pessoa, em vez de entrar pela " +
    "veia, dentro do processo. Por isso cada caso nosso nasce com a métrica combinada por escrito, " +
    "e termina medido por terceiro. No fim, a diretoria tem prova, não impressão.",
    t.PAG.margem, 4.15, { w: W, h: 1.5, size: 13, cor: t.SEC, lineSpacing: 19.5 });

  t.filete(s, t.PAG.margem, 5.75, W, t.FILETE_CLARO, 0.75);
  t.versalete(s, "As nossas raízes", t.PAG.margem, 5.92);
  t.corpo(s,
    "Verdade dita mesmo quando custa, número antes de opinião, e o compromisso de terminar com a sua " +
    "empresa mais capaz, não mais dependente. O que instalamos fica com você: os sistemas, as pessoas " +
    "formadas e o registro de tudo o que foi decidido e medido.",
    t.PAG.margem, 6.26, { w: W, h: 0.75, size: 12, serif: true, italic: true, lineSpacing: 17.5 });
  t.rodape(s);

  // ---------- PAGINA 2 — fases 1 e 2, com os servicos por dentro ----------
  s = t.novoSlide(pptx);
  t.versalete(s, "O Programa · Ano 1 · primeira parte", t.PAG.margem, 0.55, { w: 9 });
  s.addText("Da primeira conversa aos sistemas rodando.", {
    x: t.PAG.margem, y: 0.9, w: W, h: 0.65,
    fontFace: t.SERIF, fontSize: 23, bold: true, color: t.NAVY,
  });
  t.corpo(s,
    "Tudo começa com o Mapa de Vazamento, gratuito: feito de fora, com uma estimativa em reais do que " +
    "pode estar vazando na operação. Depois dele, o Programa percorre três fases em um ano. Cada etapa " +
    "entrega algo inteiro sozinha e produz o insumo da próxima.",
    t.PAG.margem, 1.6, { w: W, h: 0.62, size: 11.5, cor: t.SEC, lineSpacing: 16.5 });

  const colW2 = (W - 0.6) / 2;
  // coluna fase 1
  t.versalete(s, "Fase 1 · A Prova · seis semanas", t.PAG.margem, 2.35, { w: colW2, size: 11 });
  let y1 = servico(s, t.PAG.margem, 2.72, colW2, "O Assessment · o mergulho profundo", [
    ["O QUÊ", "Do conselho à linha de frente: como o trabalho realmente flui, onde quebra, onde vaza valor, quem decide o quê.", 0.52],
    ["POR QUÊ", "Solução genérica falha. O que funciona nasce de entender o seu negócio.", 0.38],
    ["O QUE FICA", "Portfólio de oportunidades ranqueado e quantificado, relatório de maturidade e plano diretor. Não uma lista de ideias.", 0.52],
  ]);
  servico(s, t.PAG.margem, y1 + 0.12, colW2, "O Protótipo · a prova antes do investimento", [
    ["O QUÊ", "O caso mais promissor, construído com os seus dados reais, contra critérios combinados por escrito antes.", 0.5],
    ["POR QUÊ", "Ninguém investe no escuro. A diretoria decide GO ou NO-GO com números na mesa; NO-GO também é resultado.", 0.52],
  ]);
  // coluna fase 2
  const x2 = t.PAG.margem + colW2 + 0.6;
  t.versalete(s, "Fase 2 · A Construção · meses 2 a 6", x2, 2.35, { w: colW2, size: 11 });
  let y2 = servico(s, x2, 2.72, colW2, "Construção e implantação · a engenharia", [
    ["O QUÊ", "Arquitetura, integrações e agentes de IA sob medida, em produção no fluxo real da sua equipe.", 0.5],
    ["POR QUÊ", "Relatório na gaveta não muda empresa. Sistema rodando muda.", 0.38],
    ["COMO", "Aprovação humana em tudo que é crítico: a IA executa, gente da sua confiança valida. Testes de aceite antes do trabalho real.", 0.52],
  ]);
  servico(s, x2, y2 + 0.12, colW2, "Treinamento + ABBA Portal · a mentalidade nova", [
    ["O QUÊ", "Todos os níveis, em plataforma própria e sessões presenciais, com fluência medida em 30, 60 e 90 dias.", 0.5],
    ["POR QUÊ", "O objetivo não é ensinar ferramenta: é instalar as três perguntas (parar · começar · só eu) em cada pessoa.", 0.52],
  ]);
  s.addText(
    "O Portão da Prova: ao término da fase 1, a decisão de continuar é integralmente sua. Se o resultado medido não confirmar o critério combinado, o Programa se encerra ali, sem multa e com os entregáveis em suas mãos.",
    { x: t.PAG.margem, y: 6.62, w: W, h: 0.45,
      fontFace: t.SERIF, fontSize: 10.5, italic: true, color: t.NAVY, align: "center", lineSpacing: 13.5 });
  t.rodape(s);

  // ---------- PAGINA 3 — fase 3, o ano 2+, o conselheiro, parceiros, proximo passo ----------
  s = t.novoSlide(pptx);
  t.versalete(s, "O Programa · segunda parte", t.PAG.margem, 0.55, { w: 9 });
  s.addText("A operação com presença, e a medição que não para.", {
    x: t.PAG.margem, y: 0.9, w: W, h: 0.65,
    fontFace: t.SERIF, fontSize: 23, bold: true, color: t.NAVY,
  });

  // fase 3
  servico(s, t.PAG.margem, 1.7, colW2, "Fase 3 · Sistemas gerenciados · meses 7 a 12", [
    ["O QUÊ", "Operamos o que construímos: monitoramento, evolução contínua e um ritual semanal de 20 minutos com quem decide.", 0.52],
    ["POR QUÊ", "Sistema sem dono definha. E a diretoria precisa ver o retorno, não sentir que ele existe.", 0.4],
    ["COMO", "Toda decisão entra num diário: métrica combinada antes, resultado medido depois. Relatório mensal de projetado versus realizado, sempre.", 0.52],
  ]);
  // ano 2+
  servico(s, x2, 1.7, colW2, "Ano 2 em diante · a Assinatura da Capacidade", [
    ["O QUÊ", "Operação sob SLA, conselho trimestral e o Exame Anual de IA: a maturidade re-medida e comparada ano contra ano.", 0.52],
    ["POR QUÊ", "A série histórica que nasce daí só existe aqui e vale mais a cada ano. É dela que sai a fila de oportunidades do ano seguinte.", 0.52],
    ["COMO", "Renovação anual com saída limpa: tudo o que construímos é seu, e o dado é exportável.", 0.4],
  ]);

  t.filete(s, t.PAG.margem, 4.35, W, t.FILETE_CLARO, 0.75);
  servico(s, t.PAG.margem, 4.55, W, "Já tem IA rodando? O Conselheiro de IA · do seu lado da mesa", [
    ["O QUÊ", "Um estrategista de IA presente na sua diretoria: roadmap vivo, governança, e análise independente de qualquer proposta de fornecedor que chegar, com parecer por escrito.", 0.38],
    ["POR QUÊ", "Todo fornecedor de IA tem um vendedor. A sua mesa merece alguém do seu lado quando a fatura chega. E cada recomendação entra no registro com o número que dirá, depois, se deu certo.", 0.38],
    ["AS PORTAS", "Ao fim do Programa, a cadeira dá continuidade ao que foi construído. E para quem já tem IA rodando, a porta é direta: não precisa do Programa para ter a cadeira.", 0.38],
  ]);

  t.filete(s, t.PAG.margem, 6.15, W, t.FILETE_CLARO, 0.75);
  t.versalete(s, "Parceiros oficiais", t.PAG.margem, 6.3, { size: 9.5 });
  if (assets.logoMicrosoft) s.addImage({ path: assets.logoMicrosoft, x: t.PAG.margem, y: 6.62, h: 0.26, w: 1.21 });
  if (assets.logoCrewai) s.addImage({ path: assets.logoCrewai, x: t.PAG.margem + 1.6, y: 6.58, h: 0.34, w: 1.12 });
  t.corpo(s,
    "A história começa com uma conversa de 45 minutos, e com o seu Mapa de Vazamento, gratuito.",
    t.PAG.margem + 3.2, 6.58, { w: W - 3.2, h: 0.4, size: 12, serif: true, cor: t.NAVY, lineSpacing: 16 });
  t.rodape(s);
};
