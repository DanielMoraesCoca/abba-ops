// Contratos de domínio do app (espelham os schemas Pydantic do Flow onde se tocam).
// Regra de ouro: PII do cliente vive aqui/no Postgres do app, NUNCA no estado do Flow
// (que trafega pseudonimizado por caso_id) nem no provedor de LLM.

export type Tenant = {
  id: string;              // tenant_id — a firma/profissional
  nome: string;
  criadoEm: string;
};

export type Profissional = {
  id: string;
  tenantId: string;
  nome: string;
  oab?: string;            // registro OAB/UF — vira o "assinado por" da minuta
  email: string;
};

export type CasoStatus =
  | "intake"               // preenchendo perfil (wizard) ou extraindo (upload)
  | "processando"          // Flow rodando
  | "bloqueado"            // gate de red flags reprovou — vai ao profissional, sem desenho
  | "aguardando_revisao"   // Flow pausou no gate humano (HITL)
  | "concluido"            // minuta assinada
  | "arquivado";

export type Caso = {
  id: string;              // caso_id (pseudônimo)
  tenantId: string;
  profissionalId: string;
  clienteNome: string;     // PII — só no app, criptografado; nunca no Flow
  status: CasoStatus;
  taskId?: string;         // execução na AMP
  versaoCorpus?: string;
  tetoUsdCaso: number;
  custoUsd: number;        // acumulado (do Langfuse por tenant/caso)
  criadoEm: string;
  expiraEm: string;        // TTL LGPD — job de deleção apaga estado do Flow + memórias
};

// Item da FILA DE REVISÃO do profissional — o coração do modelo centauro (HITL).
export type ItemRevisao = {
  id: string;
  casoId: string;
  tenantId: string;
  executionId: string;     // para o /resume
  taskId: string;
  payload: unknown;        // análise + desenhos + obrigações vindos do webhook da AMP
  decisao?: "aprovado" | "rejeitado" | "revisar";
  feedback?: string;
  decididoPor?: string;    // profissional_id — quem assina
  decididoEm?: string;
};
