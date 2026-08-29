"""Registro dos produtos da Camada de Caixa.

Este modulo e a fonte unica da verdade sobre **o que existe e em que estado**.
Ele e deliberadamente declarativo: nenhum produto pode ser vendido como pronto
sem que a sua maturidade diga isso aqui, e a maturidade so sobe quando o gate
declarado for cumprido.

Regra de fronteira: este arquivo (como todo `core/`) **nao importa crewai**.
As crews sao referenciadas por caminho em texto, nunca importadas — e
`scripts/audita_fronteira.py` reprova o build se alguem quebrar isso.

Doutrina de origem: plano em `abba-ops/05-interno/plano-camada-de-caixa-2027.md`.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


# UP042: `StrEnum` so existe em 3.11+. A CrewAI declara >=3.10,<3.14 e nos ficamos
# na mesma faixa — entao herdar de (str, Enum) e a forma correta aqui.
class Maturidade(str, Enum):  # noqa: UP042
    """O quanto se pode prometer de um produto, hoje.

    A ordem importa: `ordem()` permite comparar e ordenar por prontidao.
    """

    PRODUCAO = "producao"
    """Roda sobre dado real, tem golden set e metrica medida. Vendavel."""

    EXECUTAVEL = "executavel"
    """Roda ponta a ponta em dado sintetico. Demonstravel, NAO vendavel."""

    ESPECIFICADO = "especificado"
    """Contrato, configuracao e teste existem; implementacao nao. Nao demonstravel."""

    ESTACIONADO = "estacionado"
    """Bloqueado por fato externo (lei, cronograma). Nao construir ate o gate abrir."""

    def ordem(self) -> int:
        return _ORDEM[self]

    @property
    def vendavel(self) -> bool:
        return self is Maturidade.PRODUCAO

    @property
    def demonstravel(self) -> bool:
        return self in (Maturidade.PRODUCAO, Maturidade.EXECUTAVEL)


_ORDEM: dict[Maturidade, int] = {
    Maturidade.PRODUCAO: 0,
    Maturidade.EXECUTAVEL: 1,
    Maturidade.ESPECIFICADO: 2,
    Maturidade.ESTACIONADO: 3,
}


class Produto(BaseModel):
    """Um produto da escada da Camada de Caixa."""

    model_config = {"frozen": True}

    id: str
    nome: str
    maturidade: Maturidade
    resumo: str
    entrada: str
    saida: str
    metrica: str = Field(
        description="Como o resultado e medido em R$ ou em dias. Nunca 'horas economizadas'."
    )
    gate: str = Field(description="O que precisa acontecer para a maturidade subir um nivel.")
    vazamento: int | None = Field(
        default=None,
        description="Ponto no mapa de 7 vazamentos do plano de negocio. None = fora do mapa.",
    )
    base_legal: str | None = None
    crew: str | None = Field(
        default=None,
        description="Caminho da crew, em TEXTO. core/ nunca importa crewai.",
    )
    flow: str | None = None
    observacao: str | None = None


PRODUTOS: tuple[Produto, ...] = (
    Produto(
        id="sentinela",
        nome="Sentinela da Apuracao",
        maturidade=Maturidade.ESPECIFICADO,
        vazamento=None,
        resumo=(
            "Confere a apuracao assistida pre-preenchida pelo Fisco contra os documentos "
            "da propria empresa, acha credito legitimo omitido e monta o dossie de "
            "manifestacao antes do prazo. Nunca transmite."
        ),
        entrada="Apuracao pre-preenchida (API RTC) + documentos fiscais da competencia",
        saida="Dossie de manifestacao em estado RASCUNHO, para o contador assinar",
        metrica=(
            "Credito legitimo omitido pela proposta do Fisco e incorporado por "
            "manifestacao dentro do prazo, em R$, no mes"
        ),
        gate="M1 (nucleo deterministico) verde no golden set → EXECUTAVEL",
        base_legal="Decreto 12.955/2026 (RCBS) e Resolucao CGIBS 6/2026 (RIBS)",
        crew="abba_crews.crews.sentinela",
        flow="abba_crews.flows.sentinela_flow",
        observacao=(
            "Silencio do contribuinte = aceite: o credito tributario e constituido "
            "automaticamente. E a unica dor mensal, universal e ja regulamentada."
        ),
    ),
    Produto(
        id="diagnostico",
        nome="Diagnostico de Impacto de Caixa",
        maturidade=Maturidade.ESPECIFICADO,
        vazamento=5,
        resumo=(
            "Projeta, mes a mes, o caixa liquido sob tres cenarios — sem RAD, com RAD "
            "e com split payment (hipotetico, sem data). E a porta comercial."
        ),
        entrada="Historico de NF-e da empresa + perfil de operacao",
        saida="Faixa em R$, nunca ponto, com premissas numeradas e fonte citada",
        metrica="Nao tem — e produto de aquisicao, medido por conversao, nao por R$ recuperado",
        gate="Sentinela com 2 competencias rodadas → EXECUTAVEL",
        crew="abba_crews.crews.diagnostico",
        flow="abba_crews.flows.diagnostico_flow",
        observacao=(
            "Regra de honestidade herdada do Mapa de Vazamento: faixa, nunca numero "
            "exato. Numero exato calculado de fora e mentira com aparencia de precisao."
        ),
    ),
    Produto(
        id="aceleracao",
        nome="Aceleracao de Credito",
        maturidade=Maturidade.ESPECIFICADO,
        vazamento=2,
        resumo=(
            "Rastreia notas de entrada que nao chegaram ou nao foram escrituradas, "
            "classifica creditabilidade e prioriza por R$ x dias ate o prazo."
        ),
        entrada="Distribuicao DF-e (NFeDistribuicaoDFe) + escrituracao da empresa",
        saida="Fila priorizada + rascunho de cobranca ao fornecedor. Quem envia e gente.",
        metrica="Dias entre emissao e escrituracao; credito que entrou na competencia certa",
        gate="Certificado digital de um cliente disponivel → EXECUTAVEL",
        base_legal="LC 214/2025, art. 47",
        crew="abba_crews.crews.aceleracao",
        observacao=(
            "A metrica NAO e 'retencao evitada': sem split payment nao ha retencao a "
            "evitar em 2027, e cobrar por ela viraria disputa com o cliente."
        ),
    ),
    Produto(
        id="rad",
        nome="Conselho de Adesao ao RAD",
        maturidade=Maturidade.ESPECIFICADO,
        vazamento=None,
        resumo=(
            "Simula, por contraparte, o efeito de caixa e o risco de aderir ou nao ao "
            "recolhimento pelo adquirente. Decisao bilateral, com efeito nos dois lados."
        ),
        entrada="Carteira de contrapartes: volume, prazo, perfil de credito",
        saida="Recomendacao por contraparte, com probabilidade declarada e gatilho armado",
        metrica="Brier das probabilidades declaradas contra o verdito medido",
        gate="Demanda puxada por cliente pagante → EXECUTAVEL",
        base_legal="LC 214/2025, art. 27, IV — facultativo em B2B a partir de jan/2027",
        crew="abba_crews.crews.rad",
        flow="abba_crews.flows.rad_flow",
        observacao=(
            "Unico produto que ja nasce alimentando o placar de calibracao do "
            "Conselheiro: toda adesao e uma decision com predicted_probability."
        ),
    ),
    Produto(
        id="conciliacao",
        nome="Conciliacao Nota x Pagamento",
        maturidade=Maturidade.ESPECIFICADO,
        vazamento=3,
        resumo=(
            "Vincula documento fiscal a liquidacao financeira e detecta divergencia "
            "antes de ela virar apuracao errada."
        ),
        entrada="Documentos fiscais + extrato/adquirente",
        saida="Divergencias nota x pagamento, com o R$ em risco",
        metrica="Divergencias corrigidas antes do fechamento, em R$",
        gate="Integracao de meio de pagamento contratada → EXECUTAVEL",
        crew="abba_crews.crews.conciliacao",
        observacao=(
            "Sem split payment a divergencia nao gera retencao incorreta — gera "
            "apuracao incorreta. Menor que o plano de negocio original supunha, mas real."
        ),
    ),
    Produto(
        id="devolucao",
        nome="Recuperacao de Caixa Preso em Devolucao",
        maturidade=Maturidade.ESTACIONADO,
        vazamento=4,
        resumo="Rastreio e recuperacao do valor retido em operacoes canceladas ou devolvidas.",
        entrada="Eventos de cancelamento e devolucao + retencoes efetivadas",
        saida="Fila de recuperacao com honorario sobre exito",
        metrica="Valor efetivamente recuperado, em R$",
        gate="Split payment com data publicada em ato conjunto RFB/CGIBS → ESPECIFICADO",
        base_legal="LC 214/2025, arts. 31 a 35",
        observacao=(
            "ESTACIONADO por fato externo: depende de retencao instantanea, que nao "
            "existe enquanto o split payment estiver adiado (CGIBS, 12/08/2026). "
            "Sem retencao nao ha caixa preso. Nao construir."
        ),
    ),
    Produto(
        id="saude_fornecedor",
        nome="Verificacao de Saude Tributaria do Fornecedor",
        maturidade=Maturidade.ESTACIONADO,
        vazamento=7,
        resumo=(
            "Prova ao comprador que o fornecedor extinguiu o debito — condicao legal "
            "para o comprador se creditar."
        ),
        entrada="Cadeia de fornecedores + status de extincao do debito",
        saida="Atestado por relacao monitorada",
        metrica="Relacoes monitoradas; creditos preservados, em R$",
        gate="Art. 48 deixar de dispensar a exigencia de extincao → ESPECIFICADO",
        base_legal="LC 214/2025, arts. 47 e 48",
        observacao=(
            "ESTACIONADO por fato juridico: o art. 48 DISPENSA a exigencia de extincao "
            "enquanto split payment ou RAD nao estiverem implementados. O plano de "
            "negocio original chamava isto de 'a defesa de longo prazo' — e e, mas nao "
            "em 2027. Nao vender."
        ),
    ),
)


_POR_ID: dict[str, Produto] = {p.id: p for p in PRODUTOS}


def por_id(produto_id: str) -> Produto:
    """Devolve o produto pelo id. Levanta KeyError com a lista valida se nao existir."""
    try:
        return _POR_ID[produto_id]
    except KeyError:
        validos = ", ".join(sorted(_POR_ID))
        raise KeyError(f"produto desconhecido: {produto_id!r}. Validos: {validos}") from None


def listar(maturidade: Maturidade | None = None) -> tuple[Produto, ...]:
    """Lista produtos, opcionalmente filtrando por maturidade, ordenados por prontidao."""
    itens = (
        PRODUTOS
        if maturidade is None
        else tuple(p for p in PRODUTOS if p.maturidade is maturidade)
    )
    return tuple(sorted(itens, key=lambda p: (p.maturidade.ordem(), p.nome)))


def vendaveis() -> tuple[Produto, ...]:
    """Produtos que podem ser vendidos hoje. Se estiver vazio, esta certo — e o estado real."""
    return tuple(p for p in PRODUTOS if p.maturidade.vendavel)
