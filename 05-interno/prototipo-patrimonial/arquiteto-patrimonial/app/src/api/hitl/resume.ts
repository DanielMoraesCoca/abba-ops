// BFF — o advogado decidiu (aprovar/rejeitar/revisar) na fila. Retoma o Flow na AMP.
import { resumeCaso } from "../../lib/amp-client";
// import { db, setTenant } from "../../lib/db";

export async function POST(req: Request) {
  const { tenantId, itemId, decisao, feedback, profissionalId } = await req.json();
  // await setTenant(tenantId);
  // const item = await db.fila_revisao.get(itemId);
  const item = { executionId: "", taskId: "" }; // placeholder até o db entrar

  // ATENÇÃO: a webhookUrl PRECISA ser reenviada no resume (a AMP não a carrega do kickoff)
  const webhookUrl = `${process.env.APP_BASE_URL}/api/hitl/webhook`;

  await resumeCaso({
    executionId: item.executionId,
    taskId: item.taskId,
    humanFeedback: feedback ?? "",
    isApprove: decisao === "aprovado",
    webhookUrl,
  });

  // await db.fila_revisao.update({ id: itemId, decisao, feedback, decididoPor: profissionalId, decididoEm: now() });
  return Response.json({ ok: true });
}
