// BFF — inicia um caso. Roda no servidor (token da AMP nunca vai ao browser).
// Guarda de orçamento: recusa se o teto do caso/tenant já estourou.
import { kickoffCaso } from "../../lib/amp-client";
import { checarOrcamento } from "../../lib/budget";
// import { db, setTenant } from "../../lib/db"; // Postgres com RLS (próximo gatilho)

export async function POST(req: Request) {
  const { tenantId, profissionalId, casoId, perfil, tetoUsdCaso } = await req.json();

  // 1) isolamento: toda query roda sob o tenant do usuário autenticado (RLS)
  // await setTenant(tenantId);

  // 2) guarda de custo (Langfuse soma o gasto do tenant/caso)
  const ok = await checarOrcamento({ tenantId, casoId, tetoUsdCaso });
  if (!ok) return Response.json({ erro: "Teto de orçamento do caso atingido" }, { status: 402 });

  // 3) webhook onde a AMP avisa quando o Flow pausar no gate humano do advogado
  const webhookUrl = `${process.env.APP_BASE_URL}/api/hitl/webhook`;

  const { taskId } = await kickoffCaso(
    { caso_id: casoId, tenant_id: tenantId, profissional_id: profissionalId, teto_usd_caso: tetoUsdCaso, perfil },
    webhookUrl,
  );

  // await db.casos.update({ id: casoId, taskId, status: "processando" });
  return Response.json({ taskId });
}
