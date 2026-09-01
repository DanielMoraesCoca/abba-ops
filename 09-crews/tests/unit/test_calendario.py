"""O calendario e a alma da tese — e foi onde o projeto errou feio.

Ate 2026-08-30 o produto tratava o dia 15 como data-limite de manifestacao. E a data
de DISPONIBILIZACAO; o prazo vai ate o ultimo dia util do mes seguinte. Estes testes
travam a distincao, para que ela nao se perca de novo num refactor.
"""

from __future__ import annotations

from datetime import date

import pytest

from abba_crews.core.calendario import (
    JanelaManifestacao,
    Situacao,
    dias_uteis_entre,
    e_dia_util,
    feriados_nacionais,
    ultimo_dia_util,
)


@pytest.mark.parametrize(
    ("ano", "pascoa"),
    [(2024, date(2024, 3, 31)), (2026, date(2026, 4, 5)), (2027, date(2027, 3, 28))],
)
def test_pascoa_confere_com_datas_conhecidas(ano: int, pascoa: date) -> None:
    """Feriado movel errado = dia util errado = prazo errado."""
    from abba_crews.core.calendario import _pascoa

    assert _pascoa(ano) == pascoa


def test_sexta_santa_e_corpus_christi_sao_feriado() -> None:
    f = feriados_nacionais(2027)
    assert date(2027, 3, 26) in f, "Sexta-feira Santa de 2027"
    assert date(2027, 5, 27) in f, "Corpus Christi de 2027"
    assert date(2027, 9, 7) in f, "Independencia"


def test_fim_de_semana_e_feriado_nao_sao_dia_util() -> None:
    assert not e_dia_util(date(2027, 5, 1))  # sabado E feriado
    assert not e_dia_util(date(2027, 5, 2))  # domingo
    assert e_dia_util(date(2027, 5, 3))  # segunda comum


def test_ultimo_dia_util_recua_de_fim_de_semana() -> None:
    """Outubro/2027 termina num domingo: o prazo tem de recuar para sexta."""
    assert date(2027, 10, 31).weekday() == 6
    assert ultimo_dia_util(2027, 10) == date(2027, 10, 29)


def test_dias_uteis_entre_e_simetrico_e_sinalizado() -> None:
    a, b = date(2027, 4, 26), date(2027, 4, 30)
    assert dias_uteis_entre(a, b) == 4
    assert dias_uteis_entre(b, a) == -4
    assert dias_uteis_entre(a, a) == 0


# --------------------------------------------------------------------------- #
# A distincao que o projeto errou
# --------------------------------------------------------------------------- #


def test_dia_15_e_disponibilizacao_nao_prazo() -> None:
    j = JanelaManifestacao.para("2027-03")
    assert j.disponibilizacao == date(2027, 4, 15)
    assert j.prazo_final == date(2027, 4, 30)
    assert j.prazo_final > j.disponibilizacao, (
        "o dia 15 e quando a proposta APARECE; o prazo e o ultimo dia util do mes"
    )


def test_dere_muda_a_disponibilizacao_e_nao_o_prazo() -> None:
    sem = JanelaManifestacao.para("2027-03")
    com = JanelaManifestacao.para("2027-03", entrega_dere=True)
    assert com.disponibilizacao == date(2027, 4, 20)
    assert com.prazo_final == sem.prazo_final, "DeRE nao estende o prazo, so atrasa a proposta"


def test_virada_de_ano() -> None:
    j = JanelaManifestacao.para("2027-12")
    assert j.disponibilizacao == date(2028, 1, 15)
    assert j.prazo_final == ultimo_dia_util(2028, 1)


@pytest.mark.parametrize(
    ("hoje", "esperada"),
    [
        (date(2027, 4, 1), Situacao.AGUARDANDO),
        (date(2027, 4, 15), Situacao.ABERTA),
        (date(2027, 4, 27), Situacao.ULTIMOS_DIAS),
        (date(2027, 4, 30), Situacao.ULTIMOS_DIAS),
        (date(2027, 5, 3), Situacao.ENCERRADA),
    ],
)
def test_situacao_ao_longo_da_janela(hoje: date, esperada: Situacao) -> None:
    assert JanelaManifestacao.para("2027-03").situacao(hoje) is esperada


def test_so_a_janela_aberta_permite_manifestar() -> None:
    assert Situacao.ABERTA.permite_manifestar
    assert Situacao.ULTIMOS_DIAS.permite_manifestar
    assert not Situacao.AGUARDANDO.permite_manifestar
    assert not Situacao.ENCERRADA.permite_manifestar


def test_dias_restantes_fica_negativo_depois_do_prazo() -> None:
    j = JanelaManifestacao.para("2027-03")
    assert j.dias_uteis_restantes(date(2027, 4, 30)) == 0
    assert j.dias_uteis_restantes(date(2027, 5, 3)) < 0


def test_resumo_encerrado_nao_promete_manifestacao() -> None:
    """Fora do prazo o texto muda: nao se manifesta, registra-se a perda."""
    j = JanelaManifestacao.para("2027-03")
    assert "ENCERRADO" in j.resumo(date(2027, 5, 3))
    assert "Faltam" in j.resumo(date(2027, 4, 20))
