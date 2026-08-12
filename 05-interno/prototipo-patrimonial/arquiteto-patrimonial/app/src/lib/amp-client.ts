// Cliente do CrewAI AMP — SÓ roda no backend (BFF). O Bearer token nunca vai ao browser.
// A AMP expõe o Flow como API REST: /kickoff, /status/{id}, /resume.

const AMP_BASE = process.env.AMP_BASE_URL!;      // https://<flow>.crewai.com
const AMP_TOKEN = process.env.AMP_BEARER_TOKEN!; // org/user bearer — SÓ no servidor

type KickoffResult = { taskId: string };
type StatusResult = {
  status: "running" | "pending_human_input" | "completed" | "failed";
  result?: unknown;      // preenchido quando completed
  humanTask?: unknown;   // payload do gate humano quando pending_human_input
};

async function amp(path: string, init?: RequestInit) {
  const res = await fetch(`${AMP_BASE}${path}`, {
    ...init,
    headers: {
      Authorization: `Bearer ${AMP_TOKEN}`,
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
  });
  if (!res.ok) throw new Error(`AMP ${path} -> ${res.status}`);
  return res.json();
}

// Inicia um caso. Propaga SEMPRE tenant_id/profissional_id (isolamento) e o teto de custo.
// A webhookUrl é onde a AMP avisa quando o Flow pausa no gate humano.
export async function kickoffCaso(inputs: {
  caso_id: string;
  tenant_id: string;
  profissional_id: string;
  teto_usd_caso: number;
  perfil?: unknown; // do wizard OU do extractor de upload
}, webhookUrl: string): Promise<KickoffResult> {
  const data = await amp("/kickoff", {
    method: "POST",
    body: JSON.stringify({ inputs, meta: { webhookUrl } }),
  });
  return { taskId: data.task_id ?? data.kickoff_id };
}

export async function statusCaso(taskId: string): Promise<StatusResult> {
  return amp(`/status/${taskId}`);
}

// Retoma após a decisão do advogado. ATENÇÃO (pegadinha documentada da AMP):
// a webhookUrl NÃO é carregada do kickoff — precisa ser reenviada aqui.
export async function resumeCaso(params: {
  executionId: string;
  taskId: string;
  humanFeedback: string;
  isApprove: boolean;
  webhookUrl: string;
}): Promise<void> {
  await amp("/resume", {
    method: "POST",
    body: JSON.stringify({
      execution_id: params.executionId,
      task_id: params.taskId,
      human_feedback: params.humanFeedback,
      is_approve: params.isApprove,
      meta: { webhookUrl: params.webhookUrl },
    }),
  });
}
