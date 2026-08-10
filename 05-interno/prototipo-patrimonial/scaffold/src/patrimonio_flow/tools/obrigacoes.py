"""Etapa determinística: pacote de obrigações + cenários (NUNCA agente — é regra, não julgamento).

Implementa o diferencial pós-2024: cada desenho sai com o checklist completo do
que ele OBRIGA (Lei 14.754, DCBE/Bacen, ITCMD da UF, balanço de controlada).
Valores/limiares verificados em ago/2026 — revisar junto com o corpus.
"""

from __future__ import annotations

from .. import schemas as S

LIMIAR_DCBE_ANUAL_USD = 1_000_000.0
LIMIAR_DCBE_TRIMESTRAL_USD = 100_000_000.0


def montar_pacote_obrigacoes(desenho: S.DesenhoEstrutura, perfil: S.PerfilEstruturado,
                             total_exterior_usd: float) -> S.PacoteObrigacoes:
    itens: list[S.ObrigacaoItem] = []
    tem_exterior = any(e.jurisdicao.upper() != "BR" for e in desenho.elementos)
    tem_trust = any("trust" in e.veiculo.lower() for e in desenho.elementos)
    tem_controlada = any(e.veiculo.lower().startswith(("holding", "empresa", "llc"))
                         and e.jurisdicao.upper() != "BR" for e in desenho.elementos)

    if tem_exterior:
        itens.append(S.ObrigacaoItem(
            obrigacao="Declaração dos ativos no exterior no IRPF (ficha de bens; regime da Lei 14.754)",
            fundamento_doc_id="lei-14754", prazo="DAA anual", recorrencia="anual"))
        if total_exterior_usd >= LIMIAR_DCBE_ANUAL_USD:
            itens.append(S.ObrigacaoItem(
                obrigacao="DCBE anual (Bacen)", fundamento_doc_id="dcbe-bacen",
                prazo="fev-abr do ano seguinte", recorrencia="anual"))
        if total_exterior_usd >= LIMIAR_DCBE_TRIMESTRAL_USD:
            itens.append(S.ObrigacaoItem(
                obrigacao="DCBE trimestral (Bacen)", fundamento_doc_id="dcbe-bacen",
                prazo="por trimestre", recorrencia="trimestral"))
    if tem_controlada:
        itens.append(S.ObrigacaoItem(
            obrigacao="Tributação anual de 15% sobre lucros da controlada (fim do diferimento) + balanço anual da entidade",
            fundamento_doc_id="lei-14754#art-5", prazo="31/12 + DAA", recorrencia="anual"))
        itens.append(S.ObrigacaoItem(
            obrigacao="Avaliar opção pelo regime de transparência fiscal da controlada",
            fundamento_doc_id="in-2180", prazo="na DAA", recorrencia="unica"))
    if tem_trust:
        itens.append(S.ObrigacaoItem(
            obrigacao="Trust: patrimônio permanece na declaração do instituidor; distribuição = doação (ITCMD) ou transmissão causa mortis",
            fundamento_doc_id="lei-14754#art-10", prazo="por evento", recorrencia="por_evento"))
    itens.append(S.ObrigacaoItem(
        obrigacao=f"ITCMD da UF de domicílio ({perfil.pessoa.residencia_fiscal}) em doações/transmissões do plano",
        fundamento_doc_id="itcmd-uf", prazo="por evento", recorrencia="por_evento"))
    return S.PacoteObrigacoes(desenho_nome=desenho.nome, itens=itens)


def projetar_cenarios(desenho: S.DesenhoEstrutura, perfil: S.PerfilEstruturado,
                      total_exterior_usd: float) -> list[S.CenarioProjetado]:
    # TODO(Sprint 2): aritmética real (15% sobre lucro estimado, ITCMD da UF, custo de manutenção)
    # com TODAS as premissas declaradas no campo `premissas`. Stub devolve estrutura vazia válida.
    return [S.CenarioProjetado(
        desenho_nome=desenho.nome, horizonte_anos=h,
        custo_tributario_estimado_brl=0.0, custo_sucessorio_estimado_brl=0.0,
        premissas=["STUB — implementar aritmética no Sprint 2 com premissas declaradas"],
    ) for h in (5, 10)]
