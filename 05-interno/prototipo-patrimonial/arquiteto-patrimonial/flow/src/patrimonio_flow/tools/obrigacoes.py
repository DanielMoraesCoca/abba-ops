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


# Premissas de cálculo — VERSÃO DE PRODUTO v0. Toda premissa é declarada no
# cenário e revisável pelo advogado. Valores/alíquotas verificados em ago/2026;
# revisar junto com o corpus (o corpus vivo dispara alerta quando a lei muda).
ALIQUOTA_CONTROLADA = 0.15          # Lei 14.754/2023, art. 5 — 15% anual sobre lucro
RENDIMENTO_ANUAL_ESTIMADO = 0.06    # premissa conservadora de rendimento do exterior
CAMBIO_USD_BRL = 5.0                # premissa declarada; no produto vem de fonte de câmbio datada

# ITCMD por UF — faixa de topo indicativa (a EC 132 tornou a progressividade obrigatória;
# valores reais dependem da lei estadual vigente — o corpus é a fonte, isto é premissa de projeção).
ITCMD_UF = {"DF": 0.06, "SP": 0.08, "RJ": 0.08, "MG": 0.08, "GO": 0.08}
ITCMD_PADRAO = 0.08


def _custo_manutencao_anual(desenho: S.DesenhoEstrutura) -> float:
    """Extrai um ponto médio da faixa textual de manutenção do desenho (ex.: 'R$ 120–250 mil/ano')."""
    import re
    txt = desenho.custo_manutencao_anual_estimado_brl if isinstance(
        getattr(desenho, "custo_manutencao_anual_estimado_brl", None), (int, float)) else None
    if isinstance(txt, (int, float)):
        return float(txt)
    # o schema declara float; se vier 0/ausente, projeta 0 e a premissa registra isso
    return float(getattr(desenho, "custo_manutencao_anual_estimado_brl", 0.0) or 0.0)


def projetar_cenarios(desenho: S.DesenhoEstrutura, perfil: S.PerfilEstruturado,
                      total_exterior_usd: float) -> list[S.CenarioProjetado]:
    """Aritmética determinística e AUDITÁVEL — cada número acompanha suas premissas.
    Não é aconselhamento: é projeção de ordem de grandeza para a revisão do advogado."""
    total_exterior_brl = total_exterior_usd * CAMBIO_USD_BRL
    lucro_anual = total_exterior_brl * RENDIMENTO_ANUAL_ESTIMADO
    tem_controlada = any(
        e.veiculo.lower().startswith(("holding", "empresa", "llc")) and e.jurisdicao.upper() != "BR"
        for e in desenho.elementos)
    manutencao = _custo_manutencao_anual(desenho)
    aliquota_itcmd = ITCMD_UF.get(perfil.pessoa.residencia_fiscal.upper(), ITCMD_PADRAO)
    patrimonio_total_brl = sum(a.ordem_grandeza_brl for a in perfil.patrimonio.ativos) * 1_000_000 \
        if perfil.patrimonio.ativos and perfil.patrimonio.ativos[0].ordem_grandeza_brl < 10_000 \
        else sum(a.ordem_grandeza_brl for a in perfil.patrimonio.ativos)

    cenarios: list[S.CenarioProjetado] = []
    for h in (5, 10):
        custo_trib = (lucro_anual * ALIQUOTA_CONTROLADA + manutencao) * h if tem_controlada \
            else manutencao * h
        # custo sucessório: ITCMD incide na transmissão (evento único no horizonte, não anual)
        custo_suc = patrimonio_total_brl * aliquota_itcmd
        premissas = [
            f"câmbio USD/BRL = {CAMBIO_USD_BRL} (premissa declarada; no produto, fonte datada)",
            f"rendimento anual estimado do exterior = {RENDIMENTO_ANUAL_ESTIMADO:.0%} (conservador)",
            f"tributação de controlada = {ALIQUOTA_CONTROLADA:.0%}/ano sobre lucro (Lei 14.754, art. 5)"
            if tem_controlada else "sem controlada no exterior neste desenho",
            f"ITCMD de {perfil.pessoa.residencia_fiscal} = {aliquota_itcmd:.0%} na transmissão "
            f"(faixa de topo indicativa; progressividade EC 132 — valor real pela lei estadual)",
            f"custo de manutenção anual do desenho = R$ {manutencao:,.0f}",
            "projeção de ORDEM DE GRANDEZA para revisão do advogado — não é cálculo definitivo",
        ]
        cenarios.append(S.CenarioProjetado(
            desenho_nome=desenho.nome, horizonte_anos=h,
            custo_tributario_estimado_brl=round(custo_trib, 2),
            custo_sucessorio_estimado_brl=round(custo_suc, 2),
            premissas=premissas,
        ))
    return cenarios
