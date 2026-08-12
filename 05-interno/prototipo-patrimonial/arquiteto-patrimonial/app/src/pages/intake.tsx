// Tela de intake (esqueleto). Padrão híbrido da pesquisa: upload OU wizard guiado.
// O formulário monolítico causa abandono — o wizard é progressivo.
// TODO: componentizar; conectar ao /api/cases/kickoff; extração de upload com PII mascarada.

export default function IntakePage() {
  return (
    <main>
      <h1>Novo caso</h1>

      <section aria-label="Upload de documentos">
        <h2>Já tem os documentos do cliente?</h2>
        <p>Faça upload (contrato social, IR, estruturas existentes). A IA extrai o perfil —
           e a PII é mascarada antes de qualquer modelo. O documento é apagado após a extração.</p>
        {/* <UploadDropzone onExtract={perfil => kickoff(perfil)} /> */}
      </section>

      <section aria-label="Wizard guiado">
        <h2>Começar do zero</h2>
        <p>Responda o questionário em etapas (identificação → família → patrimônio →
           passivos → objetivos → conformidade). Cada etapa salva sozinha.</p>
        {/* <PerfilWizard perguntas={QUESTIONARIO_38} onComplete={perfil => kickoff(perfil)} /> */}
      </section>

      <footer>
        <small>Ferramenta de apoio ao profissional. Não constitui parecer jurídico;
        a análise e a assinatura são do advogado responsável.</small>
      </footer>
    </main>
  );
}
