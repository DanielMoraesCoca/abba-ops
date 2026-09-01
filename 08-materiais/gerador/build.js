// build.js — orquestrador do gerador de materiais ABBA.
// Uso: node build.js [alvo...]   (sem args = todos)
// Emite PPTX em ../modelos/. PDF: node build.js --pdf (requer soffice + fontes crosextra).
// Protege edição manual: se o hash em manifesto-de-saida.json divergir do arquivo
// em modelos/, recusa sobrescrever sem --force.
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { execSync } = require("child_process");
const PptxGenJS = require("pptxgenjs");
const tema = require("./tema");

const MODELOS = path.join(__dirname, "..", "modelos");
const ASSETS = path.join(__dirname, "..", "assets");
const MANIFESTO = path.join(__dirname, "manifesto-de-saida.json");

const assets = {
  logoMicrosoft: path.join(ASSETS, "marca", "logo-microsoft.png"),
  logoCrewai: path.join(ASSETS, "marca", "logo-crewai.png"),
  logoAbba: path.join(ASSETS, "..", "marca", "abba-logo.png"),
  fotos: (nome) => path.join(ASSETS, "fotos", nome),
};

const ALVOS = {
  "abba-apresentacao": require("./decks/apresentacao"),
  "abba-um-minuto": require("./decks/um-minuto"),
  "abba-deck-institucional": require("./decks/institucional"),
  "deck-programa": require("./decks/programa"),
  "deck-conselheiro": require("./decks/conselheiro"),
};

function sha256(f) { return crypto.createHash("sha256").update(fs.readFileSync(f)).digest("hex"); }
function lerManifesto() { try { return JSON.parse(fs.readFileSync(MANIFESTO, "utf8")); } catch { return {}; } }

async function main() {
  execSync(`node ${path.join(__dirname, "verifica-precos.js")}`, { stdio: "inherit" });
  const args = process.argv.slice(2);
  const force = args.includes("--force");
  const querPdf = args.includes("--pdf");
  const pedidos = args.filter((a) => !a.startsWith("--"));
  const alvos = pedidos.length ? pedidos : Object.keys(ALVOS);
  const manifesto = lerManifesto();

  for (const alvo of alvos) {
    if (!ALVOS[alvo]) { console.error(`alvo desconhecido: ${alvo}`); process.exit(1); }
    const saida = path.join(MODELOS, `${alvo}.pptx`);
    if (fs.existsSync(saida) && manifesto[alvo] && manifesto[alvo] !== sha256(saida) && !force) {
      console.error(`${alvo}: arquivo em modelos/ foi editado a mao (hash diverge do manifesto). Use --force para sobrescrever.`);
      continue;
    }
    const pptx = new PptxGenJS();
    tema.definirLayout(pptx);
    ALVOS[alvo](pptx, assets);
    await pptx.writeFile({ fileName: saida });
    manifesto[alvo] = sha256(saida);
    console.log(`gerado: ${alvo}.pptx`);
    if (querPdf) {
      execSync(`soffice --headless -env:UserInstallation=file:///tmp/lo-profile --convert-to pdf --outdir "${MODELOS}" "${saida}"`, { stdio: "pipe" });
      console.log(`gerado: ${alvo}.pdf`);
    }
  }
  fs.writeFileSync(MANIFESTO, JSON.stringify(manifesto, null, 2));
}

main().catch((e) => { console.error(e); process.exit(1); });
