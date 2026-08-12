"""Gate 1 — triagem determinística de red flags (implementa a tabela do questionario-perfil.md).

REGRA DA CASA: isto é código puro de propósito. Um agente pode ser convencido a
relativizar um red flag; um `if` não. Não converter em agente.
"""

from __future__ import annotations

from patrimonio_flow.schemas import PerfilEstruturado, RedFlag, RedFlagReport, Severidade

# Passivo relevante: acima deste valor, D2/D3 com motivação de blindagem = duro.
LIMIAR_PASSIVO_RELEVANTE_BRL = 100_000.0


def triagem_red_flags(perfil: PerfilEstruturado) -> RedFlagReport:
    """Aplica os 6 red flags duros e os brandos. Determinístico e testável."""
    flags: list[RedFlag] = []

    # ---- duros (bloqueiam o desenho) ----
    if perfil.patrimonio.estruturas_ext and perfil.patrimonio.exterior_declarado_irpf_dcbe is False:
        flags.append(RedFlag(
            codigo="RF1_exterior_nao_declarado",
            severidade=Severidade.DURO,
            fundamento_doc_id="lei-7492#art-22",
            explicacao="Ativo no exterior não declarado (IRPF/DCBE): manter depósito não declarado é crime de evasão de divisas.",
            proximo_passo_humano="Regularização com advogado/contador ANTES de qualquer desenho.",
        ))

    if perfil.patrimonio.em_nome_de_terceiros:
        flags.append(RedFlag(
            codigo="RF2_interposta_pessoa",
            severidade=Severidade.DURO,
            fundamento_doc_id="lei-9613",
            explicacao="Bens em nome de terceiros/interpostas pessoas.",
            proximo_passo_humano="Regularização assistida por advogado; o sistema não desenha sobre interposição.",
        ))

    if (perfil.passivos.motivacao_inclui_blindagem_contra_passivo_atual
            and (perfil.passivos.processos_reu_valor_brl >= LIMIAR_PASSIVO_RELEVANTE_BRL
                 or perfil.passivos.fiscal_em_aberto)):
        flags.append(RedFlag(
            codigo="RF3_fraude_a_credores",
            severidade=Severidade.DURO,
            fundamento_doc_id="cc-fraude",
            explicacao="Passivo exigível/iminente com motivação declarada de blindagem contra ele: fraude contra credores/à execução.",
            proximo_passo_humano="Parecer humano; desenho vedado neste cenário.",
        ))

    if perfil.sucessao.intencao_suprimir_legitima:
        flags.append(RedFlag(
            codigo="RF4_legitima",
            severidade=Severidade.DURO,
            fundamento_doc_id="cc-sucessao#art-1846",
            explicacao="Intenção de suprimir a legítima de herdeiro necessário — ordem pública; a otimização lícita se limita à parte disponível.",
            proximo_passo_humano="Reenquadrar o objetivo com o advogado (parte disponível).",
        ))

    if not perfil.conformidade.origem_recursos_documentavel:
        flags.append(RedFlag(
            codigo="RF5_kyc_origem",
            severidade=Severidade.DURO,
            fundamento_doc_id="lei-9613",
            explicacao="Origem do patrimônio principal não documentável (KYC).",
            proximo_passo_humano="Caso não entra.",
        ))

    if not perfil.conformidade.aceite_transparencia:
        flags.append(RedFlag(
            codigo="RF6_recusa_transparencia",
            severidade=Severidade.DURO,
            fundamento_doc_id="lei-14754",
            explicacao="Cliente não confirmou o aceite de transparência (declaração integral ao fisco).",
            proximo_passo_humano="Caso não entra sem o aceite.",
        ))

    # ---- brandos (seguem, mas o desenho é obrigado a endereçar) ----
    if perfil.patrimonio.uso_pessoal_na_pj:
        flags.append(RedFlag(
            codigo="RFB_confusao_patrimonial",
            severidade=Severidade.BRANDO,
            fundamento_doc_id="cc-art50",
            explicacao="Bens de uso pessoal dentro da PJ: risco de confusão patrimonial/desconsideração.",
            proximo_passo_humano="Desenho deve segregar uso pessoal.",
        ))
    if perfil.passivos.historico_desconsideracao:
        flags.append(RedFlag(
            codigo="RFB_historico_desconsideracao",
            severidade=Severidade.BRANDO,
            fundamento_doc_id="cc-art50",
            explicacao="Histórico de desconsideração/bloqueio: escrutínio elevado.",
            proximo_passo_humano="Propósito negocial documentado em cada elemento do desenho.",
        ))
    if perfil.familia.ex_conjuges_pendencias:
        flags.append(RedFlag(
            codigo="RFB_pendencias_conjugais",
            severidade=Severidade.BRANDO,
            fundamento_doc_id="cc-sucessao",
            explicacao="Pendências patrimoniais com ex-cônjuges.",
            proximo_passo_humano="Resolver/mapear partilhas antes da implantação.",
        ))
    if perfil.passivos.avais:
        flags.append(RedFlag(
            codigo="RFB_avais",
            severidade=Severidade.BRANDO,
            fundamento_doc_id="cc-fraude",
            explicacao="Avais/fianças pessoais: passivo contingente relevante.",
            proximo_passo_humano="Dimensionar exposição antes do desenho.",
        ))
    if perfil.pessoa.us_person:
        flags.append(RedFlag(
            codigo="RFB_us_person",
            severidade=Severidade.BRANDO,
            fundamento_doc_id="fatca",
            explicacao="US person: trilha FATCA e tributação americana em paralelo.",
            proximo_passo_humano="Coordenar com assessor fiscal nos EUA.",
        ))

    return RedFlagReport(flags=flags)
