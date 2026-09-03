// termo-do-programa-modelo.docx — o documento comercial ÚNICO da V5:
// a proposta que vira contrato. Fase 1 firme + fases 2 e 3 como opcao
// exercivel no Portao da Prova. Precos SEMPRE de conteudo/precos.json
// (validado contra a regua no build). Placeholders {{ }} como no modelo
// antigo. Registro formal, SEM travessao. Integra-se ao contrato-mae
// (03-comercial/contrato-sow-esqueleto.md) e seus Anexos.
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, HeadingLevel, PageBreak,
  Header, Footer, TabStopType,
} = require("docx");
const precos = require("../conteudo/precos.json");

const NAVY = "1B2A4A";
const OURO = "C2A35B";
const TEXTO = "33394A";
const SEC = "6E6858";
const SERIF = "Cambria";
const SANS = "Calibri";

const fmt = (n) => "R$ " + n.toLocaleString("pt-BR");
const P = precos.programa.portes;

// ---- helpers -------------------------------------------------------------
function corpo(texto, opts = {}) {
  return new Paragraph({
    spacing: { after: opts.after ?? 160, line: 276 },
    alignment: opts.align,
    children: [new TextRun({
      text: texto, font: SANS, size: opts.size ?? 21,
      color: opts.cor ?? TEXTO, italics: opts.italico ?? false,
      bold: opts.negrito ?? false,
    })],
  });
}

function h1(texto) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 200 },
    children: [new TextRun({ text: texto, font: SERIF, size: 30, bold: true, color: NAVY })],
  });
}

function h2(texto) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 240, after: 140 },
    children: [new TextRun({ text: texto, font: SERIF, size: 24, bold: true, color: OURO })],
  });
}

function versalete(texto) {
  return new Paragraph({
    spacing: { before: 60, after: 100 },
    children: [new TextRun({
      text: texto.toUpperCase(), font: SANS, size: 17, bold: true,
      color: OURO, characterSpacing: 40,
    })],
  });
}

const SEM_BORDA = {
  top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
  left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
};
const FILETE = {
  top: { style: BorderStyle.SINGLE, size: 4, color: "E5E0D4" },
  bottom: { style: BorderStyle.SINGLE, size: 4, color: "E5E0D4" },
  left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
};

function celula(texto, opts = {}) {
  return new TableCell({
    borders: opts.filete ? FILETE : SEM_BORDA,
    margins: { top: 90, bottom: 90, left: 100, right: 100 },
    width: opts.w ? { size: opts.w, type: WidthType.PERCENTAGE } : undefined,
    children: [new Paragraph({
      spacing: { after: 0, line: 252 },
      children: [new TextRun({
        text: texto, font: opts.serif ? SERIF : SANS,
        size: opts.size ?? 20, bold: opts.negrito ?? false,
        color: opts.cor ?? TEXTO, italics: opts.italico ?? false,
      })],
    })],
  });
}

function tabela(linhas) {
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: SEM_BORDA,
    rows: linhas,
  });
}

// ---- documento -----------------------------------------------------------
module.exports = async function gerar() {
  const filhos = [];

  // CAPA
  filhos.push(
    new Paragraph({ spacing: { before: 2400, after: 60 }, children: [
      new TextRun({ text: "ABBA", font: SERIF, size: 52, bold: true, color: NAVY, characterSpacing: 80 }),
    ]}),
    new Paragraph({ spacing: { after: 1200 }, children: [
      new TextRun({ text: "CONSULTORIA DE INTELIGÊNCIA ARTIFICIAL", font: SANS, size: 17, bold: true, color: OURO, characterSpacing: 50 }),
    ]}),
    new Paragraph({ spacing: { after: 200 }, children: [
      new TextRun({ text: "Termo do Programa", font: SERIF, size: 56, bold: true, color: NAVY }),
    ]}),
    new Paragraph({ spacing: { after: 1600 }, children: [
      new TextRun({ text: "AI Native · Ano 1", font: SERIF, size: 32, italics: true, color: SEC }),
    ]}),
    corpo("Preparado para: {{NOME_DO_CLIENTE}}", { size: 24, negrito: true }),
    corpo("{{MÊS ANO}}   ·   Ref: ABBA-{{ANO}}-{{NUM}}   ·   Validade: 15 dias", { cor: SEC }),
    corpo("Confidencial. Este documento integra-se ao Contrato de Prestação de Serviços da ABBA e a seus Anexos.", { cor: SEC, size: 18 }),
    new Paragraph({ children: [new PageBreak()] }),
  );

  // 1. SUMARIO EXECUTIVO
  filhos.push(
    h1("1.  Sumário Executivo"),
    corpo(
      "A ABBA propõe ao {{NOME_DO_CLIENTE}} o Programa \"AI Native · Ano 1\": doze meses, três fases, " +
      "três portas de saída. A decisão do ano é tomada uma única vez, neste Termo; o risco, nunca: " +
      "apenas a fase 1 é firme na assinatura, e as fases 2 e 3 já entram precificadas como uma opção " +
      "sua, exercível no Portão da Prova, ao fim da sexta semana."),
    corpo(
      "Em seis semanas, a fase 1 entrega um caso construído com os seus dados reais, rodando e medido " +
      "contra a métrica combinada por escrito na primeira semana, além do retrato completo de " +
      "oportunidades da empresa, ranqueado e quantificado. Com esse resultado na mesa, a sua diretoria " +
      "decide, com números, se o ano continua."),
    corpo(
      "Diferentemente de consultorias que entregam relatórios, a ABBA entrega sistemas funcionando e " +
      "pessoas capacitadas, e prova, como terceiro, o que mudou: número combinado antes, medido depois, " +
      "assinado por uma pessoa nomeada da sua empresa."),
    versalete("O programa em uma linha"),
    tabela([
      new TableRow({ children: [
        celula("1 ano", { negrito: true, serif: true, size: 24, cor: NAVY, w: 25 }),
        celula("3 fases", { negrito: true, serif: true, size: 24, cor: NAVY, w: 25 }),
        celula("3 portas de saída", { negrito: true, serif: true, size: 24, cor: NAVY, w: 25 }),
        celula("1 decisão", { negrito: true, serif: true, size: 24, cor: NAVY, w: 25 }),
      ]}),
      new TableRow({ children: [
        celula("do Termo ao Exame", { cor: SEC, size: 18 }),
        celula("Prova · Construção · Durabilidade", { cor: SEC, size: 18 }),
        celula("semana 6 · mês 6 · mês 12, sem multa", { cor: SEC, size: 18 }),
        celula("fase 1 firme; fases 2 e 3 são opção sua", { cor: SEC, size: 18 }),
      ]}),
    ]),
  );

  // 2. O QUE OUVIMOS
  filhos.push(
    h1("2.  O que ouvimos de vocês"),
    corpo("{{ACHADO_1: citação ou constatação da conversa/Mapa de Vazamento}}", { italico: true, cor: SEC }),
    corpo("{{ACHADO_2}}", { italico: true, cor: SEC }),
    corpo("{{ACHADO_3}}", { italico: true, cor: SEC }),
    corpo(
      "O Mapa de Vazamento entregue em {{DATA_DO_MAPA}} estimou {{FAIXA_ESTIMADA_EM_R$}} por mês em " +
      "valor preso na operação. Este Termo existe para transformar essa estimativa em resultado " +
      "medido, começando pelo caso de maior retorno."),
  );

  // 3. AS TRES FASES
  filhos.push(
    h1("3.  O caminho: três fases, três portões"),
    corpo("Cada fase entrega algo inteiro sozinha e produz o insumo da próxima. Nenhuma fase se inicia sem que a anterior tenha comprovado o seu resultado."),

    h2("3.1  Fase 1 · A Prova (semanas 1 a 6) · firme na assinatura"),
    corpo(
      "O QUÊ: o mergulho diagnóstico focado (processos, dados, pessoas e governança, do conselho à " +
      "linha de frente) e a construção do caso escolhido, {{CASO_DA_FASE_1}}, com os seus dados reais, " +
      "posto em uso e medido."),
    corpo(
      "A MEDIÇÃO: a métrica de sucesso é combinada por escrito na primeira semana, com a métrica proxy " +
      "definida, e assinada por {{PATROCINADOR, cargo}}. Ao fim da semana 6, o relatório apresenta " +
      "projetado versus realizado."),
    corpo(
      "O QUE FICA: o caso rodando, o relatório de medição, o relatório de maturidade e o portfólio " +
      "completo de oportunidades, ranqueado por retorno e esforço. O portfólio é seu integralmente, " +
      "independente da decisão no Portão: o portão retém execução, nunca informação."),

    h2("3.2  O Portão da Prova (semana 6)"),
    corpo(
      "Ao término da fase 1, a decisão de continuar é integralmente sua. Se o resultado medido não " +
      "confirmar o critério combinado, ou se a decisão for simplesmente não seguir, o Programa se " +
      "encerra ali: sem multa, sem renegociação, e com todos os entregáveis da fase em suas mãos. " +
      "Exercida a opção, as fases 2 e 3 iniciam nas condições já fixadas na seção 4."),

    h2("3.3  Fase 2 · A Construção (meses 2 a 6)"),
    corpo(
      "O QUÊ: os casos aprovados do portfólio entram em produção. Projetamos a arquitetura (dados, " +
      "integrações e lógica de decisão) e construímos sistemas sob medida, com agentes de IA e pontos " +
      "de aprovação humana desenhados em tudo que é crítico: a IA executa, gente da sua confiança valida."),
    corpo(
      "EM PARALELO: a capacitação de todos os níveis, na plataforma própria da ABBA e em sessões " +
      "presenciais, com fluência medida em 30, 60 e 90 dias e campeões internos formados. Sistemas e " +
      "pessoas se transformam ao mesmo tempo, por desenho."),
    corpo(
      "ENTREGÁVEL NOMEADO EM TODOS OS MESES: cada mês do Programa tem um entregável definido no plano " +
      "de fase, com critério de aceite. O Portão 2, no mês 6, é a revisão formal com a diretoria, com " +
      "saída mediante aviso, sem multa."),

    h2("3.4  Fase 3 · A Durabilidade (meses 7 a 12)"),
    corpo(
      "O QUÊ: operamos o que construímos, com presença decrescente de propósito: monitoramento, " +
      "evolução contínua, ritual semanal de 20 minutos com quem decide e relatório mensal de projetado " +
      "versus realizado. Toda decisão entra num diário: métrica combinada antes, resultado medido depois."),
    corpo(
      "NO MÊS 12: a diretoria recebe a série do ano inteiro (o que foi prometido, o que foi medido, o " +
      "que ficou instalado e quem, da sua equipe, opera cada peça) e decide, no terceiro portão, sobre " +
      "a continuidade pela Assinatura da Capacidade (seção 5)."),
  );

  // 4. INVESTIMENTO
  const porteLinha = (sigla, nome) => new TableRow({ children: [
    celula(`Porte ${sigla} (${nome})`, { negrito: true, filete: true, w: 34 }),
    celula(`${fmt(precos.programa.fase1)} + 4 × ${fmt(P[sigla].trimestre)}`, { filete: true, w: 36 }),
    celula(`${fmt(P[sigla].ano1)} no ano`, { negrito: true, filete: true, cor: NAVY, w: 30 }),
  ]});
  filhos.push(
    h1("4.  O investimento"),
    corpo(
      "O porte do Programa é determinado pela calculadora de porte da ABBA (anexa a este Termo), " +
      "preenchida com o que a descoberta revelou. Para o {{NOME_DO_CLIENTE}}, o porte apurado é " +
      "{{PORTE}} ({{PONTUAÇÃO}} pontos)."),
    tabela([
      new TableRow({ children: [
        celula("Estrutura", { negrito: true, cor: OURO, size: 18, filete: true, w: 34 }),
        celula("Pagamento", { negrito: true, cor: OURO, size: 18, filete: true, w: 36 }),
        celula("Total do ano 1", { negrito: true, cor: OURO, size: 18, filete: true, w: 30 }),
      ]}),
      new TableRow({ children: [
        celula("Fase 1 · A Prova", { negrito: true, filete: true }),
        celula(`${fmt(precos.programa.fase1)}, na assinatura deste Termo`, { filete: true }),
        celula("firme", { cor: SEC, filete: true }),
      ]}),
      porteLinha("P", "0 a 4 pontos"),
      porteLinha("M", "5 a 9 pontos"),
      porteLinha("G", "10 a 14 pontos"),
    ]),
    corpo(
      "Os trimestres das fases 2 e 3 são pagos antecipadamente, no início de cada trimestre. Pagamento " +
      "mensal disponível com acréscimo de 8% sobre o equivalente. Reajuste anual pelo IPCA. Condições " +
      "charter, quando aplicáveis, constam do Anexo III do Contrato.", { cor: SEC }),
    corpo(
      "Não exercida a opção no Portão da Prova, nada além da fase 1 é devido.", { negrito: true }),
  );

  // 5. DEPOIS DO ANO 1
  filhos.push(
    h1("5.  Depois do primeiro ano: a Assinatura da Capacidade"),
    corpo(
      "Do segundo ano em diante, a relação passa a ser medida anualmente: operação sob SLA, ritual " +
      "semanal, conselho trimestral e o Exame Anual de IA, a re-medição completa da maturidade da " +
      "empresa, comparada ano contra ano. Valor mensal por porte: " +
      `${fmt(P.P.assinatura_mensal)} (P) · ${fmt(P.M.assinatura_mensal)} (M) · ${fmt(P.G.assinatura_mensal)} (G), ` +
      "com renovação automática a partir do ano 2 e aviso de saída de 60 dias. Casos de uso novos " +
      `entram como mini-ciclos de ${fmt(precos.mini_ciclo)} dentro da assinatura. Condições completas no Anexo I-B do Contrato.`),
    corpo(
      "A saída é limpa em qualquer aniversário: tudo o que construímos é seu, o dado é exportável, e a " +
      "transição é assistida por 30 dias.", { italico: true }),
  );

  // 6. COMO TRABALHAMOS
  filhos.push(
    h1("6.  Como trabalhamos"),
    corpo(
      "Prova, não impressão: toda decisão entra num diário com a métrica combinada antes e o resultado " +
      "medido depois, e vocês veem o registro inteiro, incluindo o que não funcionou. A IA rascunha, um " +
      "humano assina, a diretoria decide. Recomendamos com convicção; quem decide são vocês."),
    corpo(
      "O que recusamos, por método: prometer acurácia que não medimos; prever o imprevisível; piloto " +
      "sem métrica; IA decidindo sozinha. Honestidade sobre escopo: o que fazemos está nomeado neste " +
      "Termo, e o que fica de fora, também."),
  );

  // 7. CONDICOES GERAIS + ACEITE
  filhos.push(
    h1("7.  Condições gerais e aceite"),
    corpo(
      "Este Termo integra o Contrato de Prestação de Serviços da ABBA, que rege confidencialidade, " +
      "proteção de dados (LGPD), propriedade intelectual, suboperadores (Anexo II), contribuição " +
      "anonimizada (Anexo IV) e demais condições. Em caso de conflito, prevalece o disposto neste " +
      "Termo quanto a escopo, preço e portões."),
    corpo("Vigência: 12 meses a partir da assinatura. Validade desta proposta: 15 dias. Foro: {{CIDADE/UF}}."),
    corpo(""),
    corpo("{{CIDADE}}, {{DATA}}.", { after: 480 }),
    tabela([
      new TableRow({ children: [
        celula("_________________________________", { w: 50 }),
        celula("_________________________________", { w: 50 }),
      ]}),
      new TableRow({ children: [
        celula("ABBA · {{REPRESENTANTE_ABBA}}", { negrito: true }),
        celula("{{NOME_DO_CLIENTE}} · {{REPRESENTANTE_CLIENTE}}", { negrito: true }),
      ]}),
    ]),
  );

  const doc = new Document({
    creator: "ABBA Consultoria de IA",
    title: "Termo do Programa · AI Native · Ano 1",
    styles: { default: { document: { run: { font: SANS, size: 21, color: TEXTO } } } },
    sections: [{
      properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
      headers: { default: new Header({ children: [new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
        children: [
          new TextRun({ text: "ABBA · CONSULTORIA DE INTELIGÊNCIA ARTIFICIAL", font: SANS, size: 14, color: SEC, characterSpacing: 30 }),
          new TextRun({ text: "\tCONFIDENCIAL", font: SANS, size: 14, color: SEC, characterSpacing: 30 }),
        ]})] }) },
      footers: { default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "contato@abbaservices.com.br · abbaservices.com.br", font: SANS, size: 14, color: SEC })],
      })] }) },
      children: filhos,
    }],
  });

  return Packer.toBuffer(doc);
};
