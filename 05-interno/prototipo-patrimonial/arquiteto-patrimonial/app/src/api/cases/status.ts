// BFF — o front faz polling disto (~5-10s) até completed OU pending_human_input.
import { statusCaso } from "../../lib/amp-client";

export async function GET(req: Request) {
  const taskId = new URL(req.url).searchParams.get("taskId");
  if (!taskId) return Response.json({ erro: "taskId obrigatório" }, { status: 400 });
  const s = await statusCaso(taskId);
  // mapeia o status da AMP para o status de domínio (ver schemas/domain.ts)
  return Response.json(s);
}
