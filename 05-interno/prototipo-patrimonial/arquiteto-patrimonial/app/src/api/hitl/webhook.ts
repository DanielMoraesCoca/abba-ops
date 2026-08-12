// BFF — recebe o webhook da AMP quando o Flow PAUSA no gate humano do advogado.
// Cria um item na fila de revisão do tenant. Autenticação do webhook via bearer/basic.
// import { db, setTenant } from "../../lib/db";

export async function POST(req: Request) {
  // TODO(produção): validar o header de auth do webhook antes de confiar no corpo
  const evento = await req.json();
  const { tenantId, casoId, executionId, taskId, payload } = evento;

  // await setTenant(tenantId);
  // await db.fila_revisao.insert({ casoId, tenantId, executionId, taskId, payload });
  // await db.casos.update({ id: casoId, status: "aguardando_revisao" });

  // notificar o profissional (e-mail/in-app) que há um caso para revisar
  return Response.json({ ok: true });
}
