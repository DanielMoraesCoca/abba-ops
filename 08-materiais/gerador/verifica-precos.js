// verifica-precos.js — falha o build se conteudo/precos.json divergir da
// regra precos-travados da regua do revisor. O espelho mecanico do Revisor.
const fs = require("fs");
const path = require("path");

const precos = JSON.parse(fs.readFileSync(path.join(__dirname, "conteudo/precos.json"), "utf8"));
const regua = JSON.parse(fs.readFileSync(path.join(__dirname, "../../06-ferramentas/regua-do-revisor.json"), "utf8"));
const regra = regua.rules.find((r) => r.id === "precos-travados");
const travados = Object.fromEntries(regra.products.map((p) => [p.name, p.priceBRL]));

const esperado = {
  "fase-1-programa": precos.programa.fase1,
  "programa-porte-p": precos.programa.portes.P.ano1,
  "programa-porte-m": precos.programa.portes.M.ano1,
  "programa-porte-g": precos.programa.portes.G.ano1,
  "trimestre-p": precos.programa.portes.P.trimestre,
  "trimestre-m": precos.programa.portes.M.trimestre,
  "trimestre-g": precos.programa.portes.G.trimestre,
  "assinatura-p": precos.programa.portes.P.assinatura_mensal,
  "assinatura-m": precos.programa.portes.M.assinatura_mensal,
  "assinatura-g": precos.programa.portes.G.assinatura_mensal,
  "diagnostico-standalone": precos.diagnostico_standalone,
  "mini-ciclo": precos.mini_ciclo,
  "conselheiro-mensal": precos.conselheiro.mensal,
  "conselheiro-trimestral": precos.conselheiro.trimestral,
  "instalacao-memoria": precos.conselheiro.instalacao_memoria,
};

let erros = 0;
for (const [nome, valor] of Object.entries(esperado)) {
  if (travados[nome] === undefined) { console.error(`FALTA na regua: ${nome}`); erros++; }
  else if (travados[nome] !== valor) { console.error(`DIVERGE ${nome}: regua=${travados[nome]} precos.json=${valor}`); erros++; }
}
for (const nome of Object.keys(travados)) {
  if (esperado[nome] === undefined) { console.error(`FALTA no precos.json: ${nome}`); erros++; }
}
if (erros) { console.error(`\n${erros} divergencia(s). Build recusado.`); process.exit(1); }
console.log("precos.json == regua-do-revisor (precos-travados). OK.");
