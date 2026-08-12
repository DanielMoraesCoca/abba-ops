// Fila de revisão do advogado (esqueleto) — o coração do modelo centauro (HITL).
// O Flow pausou; o profissional lê análise+desenhos+obrigações e decide.
// TODO: buscar itens de /api/hitl (por tenant, via RLS); conectar decisão ao /api/hitl/resume.

export default function ReviewPage() {
  return (
    <main>
      <h1>Casos aguardando sua revisão</h1>

      {/* itens.map(item => ( */}
      <article aria-label="Item de revisão">
        <h2>Caso <code>{/* item.casoId */}</code></h2>

        <section>
          <h3>Análise (cada afirmação com fonte)</h3>
          {/* <ClaimsComFonte claims={item.payload.analise} /> — link para o artigo do corpus */}
        </section>

        <section>
          <h3>Alternativas de estrutura</h3>
          {/* <Desenhos desenhos={item.payload.desenhos} criticaAdversarial /> */}
        </section>

        <section>
          <h3>Obrigações e cenários</h3>
          {/* <Obrigacoes pacotes={item.payload.obrigacoes} cenarios={item.payload.cenarios} /> */}
        </section>

        <div role="group" aria-label="Decisão">
          {/* onClick -> POST /api/hitl/resume com decisao */}
          <button>Aprovar e gerar minuta</button>
          <button>Pedir revisão</button>
          <button>Rejeitar</button>
        </div>
        <small>Ao aprovar, a minuta sai com “revisão e assinatura: [você, OAB]”.</small>
      </article>
      {/* )) */}
    </main>
  );
}
