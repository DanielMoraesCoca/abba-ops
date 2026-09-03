"""A fila da manha da Camada de Caixa — o que vence, e o que ninguem olhou.

## O ponto cego que este modulo fecha

A tese inteira deste produto e um **prazo**: nao havendo manifestacao ate o ultimo dia
util do mes seguinte, a apuracao do Fisco e presumida correta e o credito tributario e
constituido — o que equivale a confissao de divida.

E ate 2026-09-03 a ferramenta **nao sabia dizer quais prazos estavam perto**. `janela`
recebia uma competencia e nao olhava cliente nenhum; `dossies` listava o que ja fora
conferido, mas nada respondia "quais dos meus CNPJs preciso resolver hoje?". Com um
cliente ninguem sente; com duzentos, o contador teria de cruzar duas listagens na mao,
justamente no mes em que o silencio custa dinheiro.

O buraco nao aparecia em teste nenhum porque **todo teste roda com um cliente**. Foi
preciso partir de janeiro de 2027, com um escritorio contabil de verdade, e andar para
tras.

## A doutrina vem do cerebro, e nao se negocia

O `assessment-brain` ja resolveu isto em `src/brain/anticipation.js`, e a regra de la
vale aqui inteira: **uma visao deterministica, zero LLM, ordenada por PRAZO, nunca por
importancia.** Nas palavras do proprio modulo, *"importancia e julgamento humano, e uma
fila que ranqueia por relevancia vira a fila que o humano para de ler"*.

Por isso esta agenda **nao ordena por R$**. Seria tentador — "olhe primeiro o de maior
valor" — e seria trocar o criterio que a lei impoe (a data) por um que nos escolhemos.
O R$ aparece na linha, para informar; nunca decide a ordem.

## O que ela nao faz

Nao confere, nao assina, nao transmite e nao decide nada. Le a configuracao dos clientes,
o calendario e o que ja esta guardado, e diz o estado. Zero LLM, zero rede, zero escrita.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field

from abba_crews.core.arquivo import Arquivo, RegistroDossie
from abba_crews.core.calendario import JanelaManifestacao, Situacao
from abba_crews.core.clientes import ConfigInvalida, listar_com_problemas
from abba_crews.core.dossie import EstadoDossie

COMPETENCIAS_VIVAS = 3
"""Quantas competencias para tras a agenda olha.

Escolha operacional, nao legal: a janela de uma competencia fecha no ultimo dia util do
mes seguinte, entao duas ja bastariam para cobrir todo prazo aberto. A terceira existe
para o que foi **perdido** continuar visivel por um ciclo — perda que some da tela nao
ensina nada a competencia seguinte.
"""


class EstadoCompetencia(str, Enum):  # noqa: UP042
    """O estado de uma competencia de um cliente, do ponto de vista de quem opera.

    Nome proprio, e nao `Situacao`, porque `calendario.Situacao` ja existe e responde
    outra pergunta: aquela diz onde a **janela** esta; esta diz onde o **trabalho** esta.
    """

    SEM_CONFERENCIA = "sem_conferencia"
    """Janela aberta e nenhum dossie. Ninguem olhou este CNPJ nesta competencia."""

    AGUARDANDO_ASSINATURA = "aguardando_assinatura"
    """Ha rascunho guardado e ninguem assinou. O prazo corre e o dossie nao vale nada."""

    DEVOLVIDO_SEM_NOVA_CONFERENCIA = "devolvido_sem_nova_conferencia"
    """O humano recusou com motivo e nada foi refeito desde entao."""

    ASSINADO = "assinado"
    """Conferido e assinado por gente com nome. Resolvido do nosso lado."""

    PRAZO_PERDIDO = "prazo_perdido"
    """Fora da janela. Nao se manifesta mais — registra-se a perda."""

    AGUARDANDO_PROPOSTA = "aguardando_proposta"
    """O Fisco ainda nao disponibilizou a apuracao. Nada a fazer, e nao e problema."""

    @property
    def exige_acao(self) -> bool:
        """Se o humano precisa fazer alguma coisa antes do prazo."""
        return self in (
            EstadoCompetencia.SEM_CONFERENCIA,
            EstadoCompetencia.AGUARDANDO_ASSINATURA,
            EstadoCompetencia.DEVOLVIDO_SEM_NOVA_CONFERENCIA,
        )


class ItemAgenda(BaseModel):
    """Uma linha da fila: um CNPJ, uma competencia, um prazo."""

    model_config = {"frozen": True}

    cnpj: str
    razao_social: str
    competencia: str
    situacao: EstadoCompetencia
    janela: JanelaManifestacao
    dias_uteis_restantes: int
    registro: RegistroDossie | None = None
    valor_em_jogo: Decimal | None = Field(
        default=None,
        description=(
            "R$ do dossie guardado, quando ha um. **Nao ordena a fila** — informa. O "
            "criterio de ordem e a data, que e o que a lei impoe; ordenar por valor "
            "seria trocar o criterio da lei por um nosso."
        ),
    )

    def resumo(self) -> str:
        dias = self.dias_uteis_restantes
        prazo = self.janela.prazo_final.strftime("%d/%m/%Y")
        if self.situacao is EstadoCompetencia.PRAZO_PERDIDO:
            quando = f"prazo era {prazo}"
        elif self.situacao is EstadoCompetencia.AGUARDANDO_PROPOSTA:
            quando = f"proposta em {self.janela.disponibilizacao.strftime('%d/%m/%Y')}"
        else:
            quando = f"{prazo} — {dias} dia(s) util(eis)"
        marca = "!" if self.situacao.exige_acao else " "
        return (
            f"{marca} {self.competencia}  {self.cnpj}  "
            f"{self.situacao.value:<30} {quando}  {self.razao_social}"
        )


class Agenda(BaseModel):
    """A fila inteira, mais o que nao carregou."""

    model_config = {"frozen": True}

    hoje: date
    itens: tuple[ItemAgenda, ...]
    problemas: tuple[ConfigInvalida, ...] = ()
    """Configuracao que nao carregou. Nunca some em silencio: um cliente que sumiu da
    fila por causa de um YAML quebrado e um cliente que ninguem vai conferir."""

    @property
    def exigem_acao(self) -> tuple[ItemAgenda, ...]:
        return tuple(i for i in self.itens if i.situacao.exige_acao)


def _competencias(hoje: date, quantas: int = COMPETENCIAS_VIVAS) -> list[str]:
    """As `quantas` competencias anteriores a de hoje, da mais antiga para a mais nova."""
    ano, mes = hoje.year, hoje.month
    saida = []
    for _ in range(quantas):
        mes -= 1
        if mes == 0:
            ano, mes = ano - 1, 12
        saida.append(f"{ano:04d}-{mes:02d}")
    return sorted(saida)


def _situacao_de(
    janela: JanelaManifestacao, hoje: date, registros: tuple[RegistroDossie, ...]
) -> tuple[EstadoCompetencia, RegistroDossie | None]:
    """Cruza o calendario com o que esta guardado. Deterministico e sem rede."""
    situacao_janela = janela.situacao(hoje)

    assinado = next((r for r in registros if r.estado is EstadoDossie.APROVADO), None)
    if assinado is not None:
        return EstadoCompetencia.ASSINADO, assinado

    if situacao_janela is Situacao.AGUARDANDO:
        return EstadoCompetencia.AGUARDANDO_PROPOSTA, None

    rascunho = next((r for r in registros if r.estado is EstadoDossie.RASCUNHO), None)
    devolvido = next((r for r in registros if r.estado is EstadoDossie.DEVOLVIDO), None)

    if situacao_janela is Situacao.ENCERRADA:
        return EstadoCompetencia.PRAZO_PERDIDO, rascunho or devolvido
    if rascunho is not None:
        return EstadoCompetencia.AGUARDANDO_ASSINATURA, rascunho
    if devolvido is not None:
        return EstadoCompetencia.DEVOLVIDO_SEM_NOVA_CONFERENCIA, devolvido
    return EstadoCompetencia.SEM_CONFERENCIA, None


def montar(
    *,
    hoje: date,
    arquivo: Arquivo | None = None,
    dir_clientes: Path | None = None,
    competencias: int = COMPETENCIAS_VIVAS,
) -> Agenda:
    """A fila da manha, ordenada por prazo.

    `arquivo` opcional: sem ele a agenda ainda responde o que **deveria** ter sido
    conferido (calendario + carteira), so nao sabe o que ja foi. Util para ver a fila sem
    a senha em maos.
    """
    clientes, problemas = listar_com_problemas(dir_clientes)
    itens: list[ItemAgenda] = []

    for config in clientes:
        guardados = arquivo.listar(cnpj=config.cnpj) if arquivo is not None else ()
        for competencia in _competencias(hoje, competencias):
            janela = JanelaManifestacao.para(competencia, entrega_dere=config.entrega_dere)
            desta = tuple(r for r in guardados if r.competencia == competencia)
            situacao, registro = _situacao_de(janela, hoje, desta)
            itens.append(
                ItemAgenda(
                    cnpj=config.cnpj,
                    razao_social=config.razao_social,
                    competencia=competencia,
                    situacao=situacao,
                    janela=janela,
                    dias_uteis_restantes=janela.dias_uteis_restantes(hoje),
                    registro=registro,
                )
            )

    # Por PRAZO, sempre. Desempate por CNPJ e competencia so para a saida ser estavel —
    # nunca por valor, nunca por "gravidade".
    itens.sort(key=lambda i: (i.janela.prazo_final, i.cnpj, i.competencia))
    return Agenda(hoje=hoje, itens=tuple(itens), problemas=problemas)
