"""Contratos de dados do Flow (fonte: questionario-perfil.md e especificacao-agentes.md).

Todo dado de caso trafega por estes schemas — tipado, auditável, apagável.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------- perfil

class RegimeBens(str, Enum):
    COMUNHAO_PARCIAL = "comunhao_parcial"
    COMUNHAO_UNIVERSAL = "comunhao_universal"
    SEPARACAO_TOTAL = "separacao_total"
    PARTICIPACAO_FINAL = "participacao_final"
    NAO_APLICAVEL = "nao_aplicavel"


class Pessoa(BaseModel):
    # PII direta (nome/CPF) NÃO entra aqui — o caso trafega pseudonimizado (caso_id).
    idade: int
    estado_civil: str
    regime_bens: RegimeBens = RegimeBens.NAO_APLICAVEL
    residencia_fiscal: str = "BR"
    dias_no_brasil_ano: Optional[int] = None
    cidadanias: list[str] = Field(default_factory=list)
    us_person: bool = False
    mudanca_planejada: Optional[str] = None


class Filho(BaseModel):
    idade: int
    uniao: str  # de qual união
    menor_ou_incapaz: bool = False
    residencia: str = "BR"


class Familia(BaseModel):
    filhos: list[Filho] = Field(default_factory=list)
    conjuge_uniao_formalizada: Optional[bool] = None
    pacto_antenupcial: bool = False
    ex_conjuges_pendencias: list[str] = Field(default_factory=list)
    outros_dependentes: list[str] = Field(default_factory=list)
    herdeiros_exterior: list[str] = Field(default_factory=list)  # jurisdições


class Sucessao(BaseModel):
    instrumentos_existentes: list[str] = Field(default_factory=list)  # testamento, doações...
    desejo_desigual: bool = False
    intencao_suprimir_legitima: bool = False  # red flag duro 4 (B7)
    conflito: bool = False


class AtivoClasse(str, Enum):
    IMOVEL_BR = "imovel_br"
    IMOVEL_EXTERIOR = "imovel_exterior"
    PARTICIPACAO_SOCIETARIA = "participacao_societaria"
    APLICACOES_BR = "aplicacoes_br"
    APLICACOES_EXTERIOR = "aplicacoes_exterior"
    RURAL = "rural"
    OUTROS = "outros"


class Ativo(BaseModel):
    classe: AtivoClasse
    descricao: str
    ordem_grandeza_brl: float  # faixa média declarada
    jurisdicao: str = "BR"


class Patrimonio(BaseModel):
    ativos: list[Ativo] = Field(default_factory=list)
    cnpjs: list[str] = Field(default_factory=list)  # descrições, sem razão social real
    estruturas_br: list[str] = Field(default_factory=list)
    uso_pessoal_na_pj: bool = False  # ⚠️ CC art. 50
    estruturas_ext: list[str] = Field(default_factory=list)
    exterior_declarado_irpf_dcbe: Optional[bool] = None  # red flag duro 1 (C6) se False
    em_nome_de_terceiros: bool = False  # red flag duro 2 (C7)
    rural_pendencias: bool = False
    evento_liquidez: Optional[str] = None


class Passivos(BaseModel):
    dividas: list[str] = Field(default_factory=list)
    processos_reu_valor_brl: float = 0.0
    motivacao_inclui_blindagem_contra_passivo_atual: bool = False  # red flag duro 3 (D2)
    fiscal_em_aberto: bool = False
    historico_desconsideracao: bool = False
    exposicao_setorial: Optional[str] = None
    avais: list[str] = Field(default_factory=list)
    seguros: list[str] = Field(default_factory=list)


class Objetivos(BaseModel):
    prioridades: list[str] = Field(default_factory=list)
    visao_sucessoria: str = ""
    horizonte: str = "anos"  # "meses" | "anos"
    apetite_custo: str = "medio"
    preferencias: Optional[str] = None


class Conformidade(BaseModel):
    irpf_em_dia: Optional[bool] = None
    regime_14754: Optional[str] = None
    origem_recursos_documentavel: bool = True  # red flag duro 5 (F3) se False
    aceite_transparencia: bool = False  # red flag duro 6 (F4) se False


class PerfilEstruturado(BaseModel):
    pessoa: Pessoa
    familia: Familia
    sucessao: Sucessao
    patrimonio: Patrimonio
    passivos: Passivos
    objetivos: Objetivos
    conformidade: Conformidade


# ---------------------------------------------------------------- gate 1

class Severidade(str, Enum):
    DURO = "duro"
    BRANDO = "brando"


class RedFlag(BaseModel):
    codigo: str  # ex.: "RF1_exterior_nao_declarado"
    severidade: Severidade
    fundamento_doc_id: str  # ex.: "lei-7492#art-22"
    explicacao: str
    proximo_passo_humano: str


class RedFlagReport(BaseModel):
    flags: list[RedFlag] = Field(default_factory=list)

    @property
    def bloqueado(self) -> bool:
        return any(f.severidade == Severidade.DURO for f in self.flags)


# ---------------------------------------------------------------- análise (crews)

class ClaimCitada(BaseModel):
    text: str
    source_ids: list[str] = Field(default_factory=list)  # chunk_ids do corpus
    nao_coberto: bool = False  # abstenção honesta: corpus não sustenta
    lacuna: Optional[str] = None  # o que faltou, se nao_coberto


class AnaliseTributaria(BaseModel):
    claims: list[ClaimCitada]


class AnaliseSucessoria(BaseModel):
    claims: list[ClaimCitada]


class AnaliseJurisdicoes(BaseModel):
    claims: list[ClaimCitada]


class AnaliseJuridica(BaseModel):
    tributaria: AnaliseTributaria
    sucessoria: AnaliseSucessoria
    jurisdicoes: AnaliseJurisdicoes


# ---------------------------------------------------------------- desenho

class ElementoEstrutura(BaseModel):
    veiculo: str  # ex.: "trust declarado", "holding BR", "PPLI"
    jurisdicao: str
    proposito: str
    source_ids: list[str] = Field(default_factory=list)


class GravidadeAtaque(str, Enum):
    FATAL = "fatal"
    MITIGAVEL = "mitigavel"
    MENOR = "menor"


class AtaqueAdversarial(BaseModel):
    descricao: str
    gravidade: GravidadeAtaque
    base_source_ids: list[str] = Field(default_factory=list)
    mitigacao: Optional[str] = None


class CriticaAdversarial(BaseModel):
    ataques: list[AtaqueAdversarial]


class DesenhoEstrutura(BaseModel):
    nome: str
    elementos: list[ElementoEstrutura]
    sequencia_implantacao: list[str]
    custo_manutencao_anual_estimado_brl: float
    trade_offs: str
    red_flags_brandos_enderecados: list[str] = Field(default_factory=list)
    critica: Optional[CriticaAdversarial] = None

    @property
    def descartado(self) -> bool:
        if self.critica is None:
            return False
        return any(a.gravidade == GravidadeAtaque.FATAL for a in self.critica.ataques)


class ListaDesenhos(BaseModel):
    desenhos: list[DesenhoEstrutura]


class ListaCriticas(BaseModel):
    criticas: list[CriticaAdversarial]  # na mesma ordem dos desenhos


# ---------------------------------------------------------------- obrigações e cenários (determinístico)

class ObrigacaoItem(BaseModel):
    obrigacao: str  # ex.: "DCBE anual (Bacen)"
    fundamento_doc_id: str
    prazo: str
    recorrencia: str  # "anual" | "trimestral" | "unica" | "por_evento"


class PacoteObrigacoes(BaseModel):
    desenho_nome: str
    itens: list[ObrigacaoItem]


class CenarioProjetado(BaseModel):
    desenho_nome: str
    horizonte_anos: int
    custo_tributario_estimado_brl: float
    custo_sucessorio_estimado_brl: float
    premissas: list[str]


# ---------------------------------------------------------------- saída

class MinutaFinal(BaseModel):
    sumario_executivo: str
    corpo_markdown: str  # estrutura fixa (ver especificacao §3, Crew C)
    fontes_doc_ids: list[str]
    limites_da_analise: list[str]
    rodape_obrigatorio: str = (
        "Minuta gerada por sistema de apoio; não constitui parecer jurídico. "
        "Revisão e assinatura: [advogado nomeado, OAB]."
    )


# ---------------------------------------------------------------- estado do Flow

class EstadoCaso(BaseModel):
    caso_id: str = ""  # pseudônimo; nunca nome/CPF
    # --- campos de PRODUTO (multi-tenant) — isolamento por tenant é reforçado por RLS no Postgres
    tenant_id: str = ""        # o profissional/firma dono do caso; propagado em todo kickoff
    profissional_id: str = ""  # quem opera e assina (OAB/registro no app)
    teto_usd_caso: float = 5.0 # guarda de orçamento por caso (Flow aborta ao estourar)
    data_caso: str = ""        # ISO — data-de-referência do caso; filtra o corpus por vigência (as_of)
    gate_humano_ok: bool = False  # marcado no gate2; render_final exige True (gate não-burlável)
    versao_corpus: str = ""
    documento_texto: str = ""   # intake por upload: texto bruto do doc do cliente (extraído p/ perfil)
    perfil: Optional[PerfilEstruturado] = None
    red_flags: Optional[RedFlagReport] = None
    analise: Optional[AnaliseJuridica] = None
    desenhos: list[DesenhoEstrutura] = Field(default_factory=list)
    obrigacoes: list[PacoteObrigacoes] = Field(default_factory=list)
    cenarios: list[CenarioProjetado] = Field(default_factory=list)
    feedback_advogado: list[str] = Field(default_factory=list)
    minuta: Optional[MinutaFinal] = None
    chunks_recuperados: list[str] = Field(default_factory=list)  # preenchido por event listener
    custo_acumulado_usd: float = 0.0
    ciclos_redesenho: int = 0
