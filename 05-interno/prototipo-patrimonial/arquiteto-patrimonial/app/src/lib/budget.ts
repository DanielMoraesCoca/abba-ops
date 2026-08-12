// Guarda de orçamento por caso/tenant. A AMP não tem hard-cap nativo confiável,
// então o teto é aplicado aqui (BFF) somando o custo real via Langfuse por tenant_id.
export async function checarOrcamento(params: {
  tenantId: string;
  casoId: string;
  tetoUsdCaso: number;
}): Promise<boolean> {
  // TODO(produção): consultar o custo acumulado do caso no Langfuse (por session/user id)
  // e retornar false se >= tetoUsdCaso. Stub permite (retorna true) até o Langfuse entrar.
  const custoAtual = 0.0;
  return custoAtual < params.tetoUsdCaso;
}
