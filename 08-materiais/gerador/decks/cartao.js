// cartao-descoberta-prototipo — cartao de mesa A4, 2 paginas: os 7 blocos da
// descoberta tecnica do prototipo. Regenerado na V5 (a integracao real e a
// fase 2 do Programa), SEM travessao. Fonte do processo:
// 03-comercial/roteiro-descoberta-prototipo.md.
const t = require("../tema");

const A4 = { w: 8.27, h: 11.69, margem: 0.55 };
const LARG = A4.w - 2 * A4.margem;

function pagina(pptx, num) {
  const s = pptx.addSlide();
  s.background = { color: t.PAPEL };
  s.addText(`ABBA · CARTÃO DE REUNIÃO · DESCOBERTA DO PROTÓTIPO · PÁGINA ${num} DE 2`, {
    x: A4.margem, y: A4.h - 0.42, w: LARG, h: 0.25, align: "center",
    fontFace: t.SANS, fontSize: 8, color: t.SEC, charSpacing: 1.5,
  });
  return s;
}

// bloco numerado: titulo + tempo + perguntas [fala, nota]
function bloco(s, y, num, titulo, tempo, itens) {
  t.filete(s, A4.margem, y, LARG, t.OURO, 1.2);
  s.addText(String(num), { x: A4.margem, y: y + 0.06, w: 0.36, h: 0.34, fontFace: t.SERIF, fontSize: 17, bold: true, color: t.OURO });
  s.addText(titulo, { x: A4.margem + 0.4, y: y + 0.09, w: LARG - 2.2, h: 0.3, fontFace: t.SANS, fontSize: 11, bold: true, color: t.NAVY, charSpacing: 1.5 });
  s.addText(tempo, { x: A4.w - A4.margem - 1.9, y: y + 0.1, w: 1.9, h: 0.28, align: "right", fontFace: t.SERIF, fontSize: 9.5, italic: true, color: t.SEC });
  let yy = y + 0.42;
  itens.forEach(([fala, nota]) => {
    s.addText("·", { x: A4.margem + 0.05, y: yy - 0.02, w: 0.2, h: 0.22, fontFace: t.SANS, fontSize: 11, bold: true, color: t.OURO });
    const temNota = !!nota;
    s.addText(fala, { x: A4.margem + 0.28, y: yy, w: temNota ? LARG - 2.75 : LARG - 0.3, h: 0.38, fontFace: t.SERIF, fontSize: 8.7, italic: true, color: t.TEXTO, lineSpacing: 10.5 });
    if (temNota) s.addText(nota, { x: A4.w - A4.margem - 2.42, y: yy, w: 2.42, h: 0.38, align: "right", fontFace: t.SANS, fontSize: 7.3, color: t.SEC, lineSpacing: 9 });
    yy += 0.36;
  });
  return yy + 0.06;
}

module.exports = function gerar(pptx) {
  pptx.defineLayout({ name: "ABBA_A4", width: A4.w, height: A4.h });
  pptx.layout = "ABBA_A4";

  // -------- pagina 1 --------
  let s = pagina(pptx, 1);
  s.addText("ABBA", { x: A4.margem, y: 0.35, w: 2, h: 0.35, fontFace: t.SERIF, fontSize: 16, bold: true, color: t.NAVY, charSpacing: 3 });
  s.addText("CARTÃO DE REUNIÃO · DESCOBERTA TÉCNICA DO PROTÓTIPO · 7 BLOCOS, ~60 MIN", {
    x: A4.margem, y: 0.72, w: LARG, h: 0.25, fontFace: t.SANS, fontSize: 9, bold: true, color: t.OURO, charSpacing: 2,
  });
  s.addText("Sair daqui com o protótipo desenhável.", {
    x: A4.margem, y: 1.0, w: LARG, h: 0.4, fontFace: t.SERIF, fontSize: 17, bold: true, color: t.NAVY,
  });
  s.addText("“Hoje o meu papel é entender o problema a fundo. Vou fazer bastante pergunta, algumas bem básicas. É de propósito: o nosso time de engenharia desenha o protótipo em cima do que eu levar daqui.”", {
    x: A4.margem, y: 1.45, w: LARG, h: 0.55, fontFace: t.SERIF, fontSize: 9.5, italic: true, color: t.SEC, lineSpacing: 12.5,
  });
  s.addText("Ouro: pedir para MOSTRAREM · anotar todo nome próprio (sistema, tela, campo) · nunca prometer prazo ou arquitetura na hora.", {
    x: A4.margem, y: 2.02, w: LARG, h: 0.3, fontFace: t.SANS, fontSize: 8.5, bold: true, color: t.NAVY, lineSpacing: 11,
  });

  let y = 2.45;
  y = bloco(s, y, 1, "O PROBLEMA E O PROCESSO", "· 12 min", [
    ["“Me contem o processo do início ao fim, como se eu fosse fazer esse trabalho amanhã: o que chega, quem pega, o que faz, para onde vai?”", ""],
    ["“O que DISPARA o processo: e-mail, arquivo, pedido, data do mês?”", "a entrada do fluxo"],
    ["“Resposta na hora, ou pode rodar em lote, de noite?”", "ritmo = arquitetura e custo"],
    ["“Quantos por dia/mês? Quanto tempo cada um? Quantas pessoas tocam?”", ""],
    ["“E quando NÃO segue o padrão? Dois exemplos reais.”", "os casos de teste; onde protótipos morrem"],
    ["“Se só um pudesse ser resolvido este mês, qual tira mais dinheiro/sono?”", "protótipo é UM caso"],
  ]);
  y = bloco(s, y, 2, "O NÚMERO DO SUCESSO E O CUSTO DO ERRO", "· 10 min · O MAIS IMPORTANTE", [
    ["“Qual é o número de hoje: tempo, erro, custo, atraso? Já é medido? Onde?”", "baseline"],
    ["“Que número faria vocês dizerem ‘aprovado, vamos investir’?”", "a meta do GO, combinada ANTES"],
    ["“Que erro seria INACEITÁVEL? E qual é tolerável, se pego na revisão?”", "define onde vai a aprovação humana"],
    ["“Quem bate o martelo de que funcionou?”", ""],
  ]);
  bloco(s, y, 3, "A INTELIGÊNCIA DO TRABALHO", "· 10 min · O QUE DESENHA A SOLUÇÃO", [
    ["“Se eu colocasse aqui amanhã um estagiário brilhante, sem experiência da casa: o que diriam para ele fazer, em que ordem? E o que ele ERRARIA no primeiro mês? Por quê?”", "o que erraria = o conhecimento tácito que vira instrução, exemplo ou revisão"],
    ["“Onde está ESCRITO como fazer certo: manual, política, tabela, catálogo, histórico? E o que só existe na cabeça de alguém?”", "a base de consulta da solução"],
    ["“Quais passos são ‘seguir regra’, e quais têm decisão de verdade?”", ""],
    ["“Como vocês reconhecem um resultado BEM feito? E um que parece certo mas está errado?”", ""],
  ]);

  // -------- pagina 2 --------
  s = pagina(pptx, 2);
  y = 0.35;
  y = bloco(s, y, 4, "OS SISTEMAS E O DESTINO", "· 8 min", [
    ["“Onde o processo mora: que sistemas, planilhas, ferramentas? Nuvem ou servidor de vocês?”", "nome e versão"],
    ["“Como a informação entra e sai: digitação, relatório exportado, integração automática?”", "API = a ‘tomada’ que liga sistemas"],
    ["“O resultado precisa chegar ONDE, em que formato, para quem?”", "o destino define a última etapa"],
    ["“Para a prova, exportação manual serve? Alguém extrai e nos manda?”", "de-risk: tira a TI do caminho crítico; a integração real é a fase 2 do Programa"],
    ["“Quem administra: TI interna, fornecedor, terceirizada?”", "de quem virá o acesso"],
  ]);
  y = bloco(s, y, 5, "OS DADOS E A AMOSTRA", "· 10 min", [
    ["“Que documentos e dados o processo usa e produz?”", "PEDIR PARA VER UM EXEMPLAR NA HORA"],
    ["“PDF escaneado ou digital? Foto? Áudio? Planilha padronizada ou cada um de um jeito?”", "muda o protótipo inteiro"],
    ["“Quantos por mês? Guardado desde quando? Onde? · Tem dado pessoal: nome, CPF, salário?”", "LGPD → anonimização"],
    ["“A empresa permite IA em nuvem sobre esses dados, ou fica tudo dentro de casa?”", "temos as duas vias"],
    ["“Precisamos de 20–50 exemplos reais com a resposta certa de cada um: um gabarito. Quem monta, e até quando?”", "a régua com que o protótipo será medido"],
  ]);
  y = bloco(s, y, 6, "AS PESSOAS", "· 5 min", [
    ["“Quem faz hoje? Quem conhece as exceções de cor?”", "essa 2ª pessoa participa do protótipo"],
    ["“Quantas horas por semana essa pessoa nos dá durante o protótipo?”", "o gargalo real; perguntar SEMPRE"],
    ["“Quem revisa e aprova o que a IA fizer?”", "a IA executa, gente da confiança de vocês valida"],
    ["“Quem é o nosso ponto focal técnico?”", "nome + canal"],
  ]);
  y = bloco(s, y, 7, "RESTRIÇÕES E LOGÍSTICA", "· 5 min", [
    ["“Precisa de NDA antes da amostra? Quem autoriza acessos?”", ""],
    ["“Se bater a meta, quem decide o passo seguinte, e em que fórum?”", ""],
    ["Prazo: não prometer na hora. “Nosso time volta com o desenho, cronograma e critérios por escrito.”", ""],
  ]);

  // fecho: os 12 + sinais de alerta
  t.filete(s, A4.margem, y + 0.02, LARG, t.NAVY, 1.2);
  s.addText("NÃO SAIA DA REUNIÃO SEM · OS 12", { x: A4.margem, y: y + 0.1, w: LARG, h: 0.24, fontFace: t.SANS, fontSize: 9.5, bold: true, color: t.NAVY, charSpacing: 2 });
  const doze = [
    ["1 UM caso escolhido (demais → fila)", "7 Onde está escrito como fazer certo"],
    ["2 Processo + gatilho + ritmo (hora × lote)", "8 Sistemas com nome (nuvem × local)"],
    ["3 Baseline em número + onde é medido", "9 Formato real visto + destino da saída"],
    ["4 A meta que define GO, dita por eles", "10 Amostra c/ gabarito + horas do especialista"],
    ["5 O erro inaceitável, nomeado", "11 Usuário-chave + aprovador + ponto focal"],
    ["6 O que o estagiário erraria (tácito)", "12 Dados podem sair? IA em nuvem ok?"],
  ];
  doze.forEach((par, i) => {
    const yy = y + 0.38 + i * 0.19;
    s.addText(par[0], { x: A4.margem, y: yy, w: LARG / 2 - 0.1, h: 0.2, fontFace: t.SANS, fontSize: 8, color: t.TEXTO });
    s.addText(par[1], { x: A4.margem + LARG / 2, y: yy, w: LARG / 2, h: 0.2, fontFace: t.SANS, fontSize: 8, color: t.TEXTO });
  });
  const ya = y + 0.38 + 6 * 0.19 + 0.06;
  s.addText("SINAIS DE ALERTA · MUDAM A CONVERSA, NÃO MATAM A REUNIÃO", { x: A4.margem, y: ya, w: LARG, h: 0.22, fontFace: t.SANS, fontSize: 8.5, bold: true, color: t.OURO, charSpacing: 1.5 });
  s.addText(
    "Sem dado acessível → protótipo começa capturando o dado · Sem número → 1ª semana mede o hoje · “Automatizar tudo” → “tudo começa por um. Qual?” · " +
    "Conhecimento todo na cabeça de um → sessões de extração antes do desenho · Especialista sem tempo → cronograma é ficção; renegociar · " +
    "Erro inaceitável em tudo → nasce com aprovação humana em tudo, e a autonomia cresce com a confiança medida · Dado preso + sem infra → desenho especial, sem prazo na hora.",
    { x: A4.margem, y: ya + 0.22, w: LARG, h: 0.55, fontFace: t.SANS, fontSize: 7.5, color: t.SEC, lineSpacing: 9.5 });
  s.addText("Mesmo dia: registro dos 7 blocos ao time. O que faltar vira pergunta ao ponto focal, não segunda reunião.",
    { x: A4.margem, y: ya + 0.82, w: LARG, h: 0.22, fontFace: t.SERIF, fontSize: 8.5, italic: true, color: t.NAVY, align: "center" });
};
