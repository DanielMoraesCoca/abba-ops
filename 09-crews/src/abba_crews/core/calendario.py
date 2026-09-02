"""O calendario da apuracao assistida — o prazo, que e a tese do produto.

Ate 2026-08-30 este modulo nao existia, e a ausencia dele foi o que deixou passar o
erro mais grave do projeto: tratar o dia 15 como data-limite de manifestacao. Nao e.

    dia 15 (ou 20, com DeRE)  ->  DISPONIBILIZACAO da proposta do Fisco
    ultimo dia util do mes    ->  PRAZO de manifestacao (ajustes + e -)

O silencio ate o prazo nao e omissao inofensiva: a apuracao do Fisco e presumida
correta e o credito tributario e constituido, **o que equivale a confissao de divida**
(art. 348, §1o da LC 214/2025; §4o do art. 125 do ADCT).

Consequencia de produto: **o valor de um achado e funcao do tempo.** Dentro da janela
e dinheiro; fora dela e registro de perda. Nenhum outro modulo deve calcular datas.

> **Fonte secundaria.** Como todo fato legal deste projeto, os prazos vieram de imprensa
> especializada e escritorios. Reconferir na fonte primaria antes de peca comercial —
> pendencia P3b em `docs/PENDENCIAS.md`. Cada regra abaixo carrega o seu `fonte`.
"""

from __future__ import annotations

import calendar
from datetime import date, timedelta
from enum import Enum

from pydantic import BaseModel, Field

DIA_DISPONIBILIZACAO_PADRAO = 15
"""Contribuinte em geral. Fonte: regulamentos da apuracao assistida (RCBS/RIBS)."""

DIA_DISPONIBILIZACAO_DERE = 20
"""Quem entrega a Declaracao de Regimes Especificos. Mesma fonte."""

LIMIAR_ULTIMOS_DIAS = 3
"""Dias uteis a partir dos quais a janela entra em alerta. Escolha operacional, nao legal."""


class Situacao(str, Enum):  # noqa: UP042
    """Onde a competencia esta, em relacao a janela de manifestacao."""

    AGUARDANDO = "aguardando"
    """A proposta do Fisco ainda nao foi disponibilizada. Nada a conferir."""

    ABERTA = "aberta"
    """Da para conferir e manifestar com folga."""

    ULTIMOS_DIAS = "ultimos_dias"
    """A janela fecha em poucos dias uteis. E aqui que o dossie precisa sair."""

    ENCERRADA = "encerrada"
    """O prazo passou. O que nao foi manifestado virou confissao de divida."""

    @property
    def permite_manifestar(self) -> bool:
        return self in (Situacao.ABERTA, Situacao.ULTIMOS_DIAS)


def _pascoa(ano: int) -> date:
    """Domingo de Pascoa pelo algoritmo de Meeus/Jones/Butcher (calendario gregoriano)."""
    a, b, c = ano % 19, ano // 100, ano % 100
    d, e = b // 4, b % 4
    f, g = (b + 8) // 25, 0
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    m = (32 + 2 * e + 2 * i - h - k) % 7
    n = (a + 11 * h + 22 * m) // 451
    mes = (h + m - 7 * n + 114) // 31
    dia = ((h + m - 7 * n + 114) % 31) + 1
    return date(ano, mes, dia)


def feriados_nacionais(ano: int) -> frozenset[date]:
    """Feriados nacionais e pontos facultativos federais que fecham banco e Fisco.

    Fixos (Lei 662/1949, com as alteracoes ate a Lei 14.759/2023) e moveis
    derivados da Pascoa.

    **Limitacao declarada:** nao cobre feriado estadual nem municipal. Uma empresa em
    municipio com feriado local no ultimo dia util tem prazo diferente do calculado
    aqui. Ate a configuracao por cliente aceitar feriados locais, o produto pode
    superestimar o prazo em um dia — e por isso o dossie sempre mostra a data, nunca
    so "voce tem N dias".
    """
    p = _pascoa(ano)
    return frozenset(
        {
            date(ano, 1, 1),  # Confraternizacao Universal
            p - timedelta(days=48),  # Carnaval (segunda)
            p - timedelta(days=47),  # Carnaval (terca)
            p - timedelta(days=2),  # Sexta-feira Santa
            date(ano, 4, 21),  # Tiradentes
            date(ano, 5, 1),  # Dia do Trabalho
            p + timedelta(days=60),  # Corpus Christi
            date(ano, 9, 7),  # Independencia
            date(ano, 10, 12),  # Nossa Senhora Aparecida
            date(ano, 11, 2),  # Finados
            date(ano, 11, 15),  # Proclamacao da Republica
            # Consciencia Negra — feriado NACIONAL pela Lei 14.759/2023, a partir de
            # 2024. Faltava aqui ate 2026-09-02, e o erro era na direcao perigosa: o
            # produto contava um dia util a mais em novembro (2026, 2028, 2029...),
            # fazendo o contador achar que tinha mais tempo do que tem.
            date(ano, 11, 20),  # Dia Nacional de Zumbi e da Consciencia Negra
            date(ano, 12, 25),  # Natal
        }
    )


def e_dia_util(d: date, feriados: frozenset[date] | None = None) -> bool:
    """Dia util = nao e sabado, nao e domingo, nao e feriado."""
    if d.weekday() >= 5:
        return False
    return d not in (feriados if feriados is not None else feriados_nacionais(d.year))


def ultimo_dia_util(ano: int, mes: int) -> date:
    """O ultimo dia util do mes. E o prazo de manifestacao."""
    d = date(ano, mes, calendar.monthrange(ano, mes)[1])
    feriados = feriados_nacionais(ano)
    while not e_dia_util(d, feriados):
        d -= timedelta(days=1)
    return d


def dias_uteis_entre(inicio: date, fim: date) -> int:
    """Dias uteis de `inicio` (exclusive) ate `fim` (inclusive). Negativo se ja passou."""
    if fim < inicio:
        return -dias_uteis_entre(fim, inicio)
    total, d = 0, inicio
    feriados_por_ano: dict[int, frozenset[date]] = {}
    while d < fim:
        d += timedelta(days=1)
        fer = feriados_por_ano.setdefault(d.year, feriados_nacionais(d.year))
        if e_dia_util(d, fer):
            total += 1
    return total


def _mes_seguinte(competencia: str) -> tuple[int, int]:
    ano, mes = (int(p) for p in competencia.split("-"))
    return (ano + 1, 1) if mes == 12 else (ano, mes + 1)


class JanelaManifestacao(BaseModel):
    """A janela de uma competencia, para um contribuinte."""

    model_config = {"frozen": True}

    competencia: str = Field(pattern=r"^\d{4}-\d{2}$")
    entrega_dere: bool
    disponibilizacao: date
    prazo_final: date

    @classmethod
    def para(cls, competencia: str, *, entrega_dere: bool = False) -> JanelaManifestacao:
        """Calcula a janela. Unico caminho sancionado — nenhuma data em outro modulo."""
        ano, mes = _mes_seguinte(competencia)
        dia = DIA_DISPONIBILIZACAO_DERE if entrega_dere else DIA_DISPONIBILIZACAO_PADRAO
        return cls(
            competencia=competencia,
            entrega_dere=entrega_dere,
            disponibilizacao=date(ano, mes, dia),
            prazo_final=ultimo_dia_util(ano, mes),
        )

    def dias_uteis_restantes(self, hoje: date) -> int:
        """Dias uteis ate o prazo. Zero no ultimo dia; negativo depois dele."""
        return dias_uteis_entre(hoje, self.prazo_final)

    def situacao(self, hoje: date) -> Situacao:
        if hoje > self.prazo_final:
            return Situacao.ENCERRADA
        if hoje < self.disponibilizacao:
            return Situacao.AGUARDANDO
        return (
            Situacao.ULTIMOS_DIAS
            if self.dias_uteis_restantes(hoje) <= LIMIAR_ULTIMOS_DIAS
            else Situacao.ABERTA
        )

    def resumo(self, hoje: date) -> str:
        """Uma linha para o topo do dossie. O contador le isto primeiro."""
        s = self.situacao(hoje)
        prazo = self.prazo_final.strftime("%d/%m/%Y")
        if s is Situacao.ENCERRADA:
            return (
                f"Prazo ENCERRADO em {prazo}. O que nao foi manifestado foi consolidado "
                f"pela proposta do Fisco."
            )
        if s is Situacao.AGUARDANDO:
            disp = self.disponibilizacao.strftime("%d/%m/%Y")
            return f"Proposta prevista para {disp}. Prazo de manifestacao ate {prazo}."
        dias = self.dias_uteis_restantes(hoje)
        urgencia = " — ULTIMOS DIAS" if s is Situacao.ULTIMOS_DIAS else ""
        return f"Prazo de manifestacao: {prazo}. Faltam {dias} dia(s) util(eis){urgencia}."
