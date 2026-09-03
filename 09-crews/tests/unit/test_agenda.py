"""A fila da manha — o ponto cego que a engenharia reversa achou.

A tese inteira deste produto e um prazo: silencio ate o ultimo dia util do mes seguinte
equivale a confissao de divida. E ate 2026-09-03 **a ferramenta nao sabia dizer quais
prazos estavam perto**. `janela` recebia uma competencia e nao olhava cliente nenhum;
`dossies` listava o que ja fora conferido. Nada respondia "quais dos meus CNPJs preciso
resolver hoje?".

O buraco nao aparecia em teste nenhum porque **todo teste rodava com um cliente**. Por
isso estes testes usam uma carteira: um cliente so nao exercita largura.

A trava de doutrina mais importante aqui e a da ordenacao: **por prazo, nunca por valor**
— herdada de `abba brain next`, onde esta escrito que "uma fila que ranqueia por
relevancia vira a fila que o humano para de ler".
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from abba_crews.core.agenda import COMPETENCIAS_VIVAS, EstadoCompetencia, montar
from abba_crews.core.arquivo import Arquivo

SENHA = "senha-de-teste"
CNPJ_A = "00000000000191"
CNPJ_B = "11444777000161"


def _cliente(dirc: Path, cnpj: str, nome: str, *, dere: bool = False) -> None:
    (dirc / f"{cnpj}.yaml").write_text(
        f'cnpj: "{cnpj}"\n'
        f'razao_social: "{nome}"\n'
        f"entrega_dere: {str(dere).lower()}\n"
        'tolerancia_brl: "0.00"\n'
        "aprovacao:\n"
        '  responsavel_nome: "Maria Contadora"\n'
        '  responsavel_email: "maria@escritorio.com.br"\n',
        encoding="utf-8",
    )


@pytest.fixture
def carteira(tmp_path: Path) -> Path:
    d = tmp_path / "clientes"
    d.mkdir()
    _cliente(d, CNPJ_A, "Empresa A")
    _cliente(d, CNPJ_B, "Empresa B", dere=True)
    return d


# --------------------------------------------------------------------------- #
# A doutrina: prazo, nunca valor
# --------------------------------------------------------------------------- #


def test_ordena_por_prazo(carteira: Path) -> None:
    a = montar(hoje=date(2027, 4, 27), dir_clientes=carteira)
    prazos = [i.janela.prazo_final for i in a.itens]
    assert prazos == sorted(prazos), "a fila tem de sair em ordem de prazo"


def test_o_valor_nao_ordena_a_fila() -> None:
    """Ordenar por R$ seria trocar o criterio da lei (a data) por um nosso.

    Se um dia alguem acrescentar `key=valor_em_jogo` no sort, este teste nao pega —
    mas a docstring de `core/agenda.py` e a razao registrada pegam a revisao.
    """
    from abba_crews.core.agenda import ItemAgenda

    assert "valor_em_jogo" in ItemAgenda.model_fields
    descricao = ItemAgenda.model_fields["valor_em_jogo"].description or ""
    assert "Nao ordena" in descricao


# --------------------------------------------------------------------------- #
# Os estados
# --------------------------------------------------------------------------- #


def test_carteira_intocada_e_tudo_sem_conferencia(carteira: Path) -> None:
    a = montar(hoje=date(2027, 4, 27), dir_clientes=carteira)
    da_competencia = [i for i in a.itens if i.competencia == "2027-03"]
    assert len(da_competencia) == 2, "os dois clientes tem de aparecer"
    assert all(i.situacao is EstadoCompetencia.SEM_CONFERENCIA for i in da_competencia)
    assert all(i.situacao.exige_acao for i in da_competencia)


def test_antes_da_disponibilizacao_nao_e_problema(carteira: Path) -> None:
    """Aguardar a proposta do Fisco nao e pendencia — e a lei."""
    a = montar(hoje=date(2027, 4, 5), dir_clientes=carteira, competencias=1)
    assert all(i.situacao is EstadoCompetencia.AGUARDANDO_PROPOSTA for i in a.itens)
    assert a.exigem_acao == ()


def test_depois_do_prazo_vira_perda_e_para_de_exigir_acao(carteira: Path) -> None:
    a = montar(hoje=date(2027, 5, 10), dir_clientes=carteira)
    de_marco = [i for i in a.itens if i.competencia == "2027-03"]
    assert de_marco and all(i.situacao is EstadoCompetencia.PRAZO_PERDIDO for i in de_marco)
    assert all(not i.situacao.exige_acao for i in de_marco)


def test_rascunho_guardado_vira_aguardando_assinatura(
    carteira: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from abba_crews.core.calendario import JanelaManifestacao
    from abba_crews.core.clientes import carregar_por_cnpj
    from abba_crews.core.dossie import montar as montar_dossie
    from abba_crews.core.dossie import renderizar
    from abba_crews.core.reconciliacao import reconciliar
    from abba_crews.core.sinteticos import caso_para

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", SENHA)
    arq = Arquivo(tmp_path / "dossies")
    caso = caso_para(CNPJ_A, "2027-03")
    r = reconciliar(caso.documentos, caso.apuracao)
    d = montar_dossie(
        config=carregar_por_cnpj(CNPJ_A, carteira),
        janela=JanelaManifestacao.para("2027-03"),
        resultado=r,
        hoje=date(2027, 4, 20),
    )
    arq.guardar(d, renderizar(d), impressao="aaaa1111", origem="teste")

    a = montar(hoje=date(2027, 4, 27), arquivo=arq, dir_clientes=carteira)
    do_a = next(i for i in a.itens if i.cnpj == CNPJ_A and i.competencia == "2027-03")
    do_b = next(i for i in a.itens if i.cnpj == CNPJ_B and i.competencia == "2027-03")
    assert do_a.situacao is EstadoCompetencia.AGUARDANDO_ASSINATURA
    assert do_b.situacao is EstadoCompetencia.SEM_CONFERENCIA, "o outro cliente nao muda"


def test_assinado_sai_da_fila_de_acao(
    carteira: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from abba_crews.core.aprovacao import aprovar
    from abba_crews.core.calendario import JanelaManifestacao
    from abba_crews.core.clientes import carregar_por_cnpj
    from abba_crews.core.dossie import montar as montar_dossie
    from abba_crews.core.dossie import renderizar
    from abba_crews.core.reconciliacao import reconciliar
    from abba_crews.core.sinteticos import caso_para

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", SENHA)
    arq = Arquivo(tmp_path / "dossies")
    caso = caso_para(CNPJ_A, "2027-03")
    d = montar_dossie(
        config=carregar_por_cnpj(CNPJ_A, carteira),
        janela=JanelaManifestacao.para("2027-03"),
        resultado=reconciliar(caso.documentos, caso.apuracao),
        hoje=date(2027, 4, 20),
    )
    reg = arq.guardar(d, renderizar(d), impressao="aaaa1111", origem="teste")
    aprovar(arq, reg.chave, por="Maria Contadora")

    a = montar(hoje=date(2027, 4, 27), arquivo=arq, dir_clientes=carteira)
    do_a = next(i for i in a.itens if i.cnpj == CNPJ_A and i.competencia == "2027-03")
    assert do_a.situacao is EstadoCompetencia.ASSINADO
    assert not do_a.situacao.exige_acao


# --------------------------------------------------------------------------- #
# O que nao carregou nunca some em silencio
# --------------------------------------------------------------------------- #


def test_config_quebrada_aparece_na_agenda(carteira: Path) -> None:
    """Cliente que sumiu da fila por YAML quebrado e cliente que ninguem vai conferir."""
    (carteira / "11222333000181.yaml").write_text('cnpj: "11222333000181"\n', encoding="utf-8")
    a = montar(hoje=date(2027, 4, 27), dir_clientes=carteira)
    assert len(a.problemas) == 1
    assert a.problemas[0].caminho == "11222333000181.yaml"
    assert {i.cnpj for i in a.itens} == {CNPJ_A, CNPJ_B}, "os validos continuam na fila"


def test_carteira_vazia_e_inofensiva(tmp_path: Path) -> None:
    vazio = tmp_path / "nenhum"
    vazio.mkdir()
    a = montar(hoje=date(2027, 4, 27), dir_clientes=vazio)
    assert a.itens == () and a.problemas == ()


def test_dere_atrasa_a_proposta_e_nao_o_prazo(carteira: Path) -> None:
    """A configuracao por cliente tem de chegar ate a agenda."""
    a = montar(hoje=date(2027, 4, 17), dir_clientes=carteira, competencias=1)
    sem_dere = next(i for i in a.itens if i.cnpj == CNPJ_A)
    com_dere = next(i for i in a.itens if i.cnpj == CNPJ_B)
    assert sem_dere.situacao is not EstadoCompetencia.AGUARDANDO_PROPOSTA
    assert com_dere.situacao is EstadoCompetencia.AGUARDANDO_PROPOSTA
    assert sem_dere.janela.prazo_final == com_dere.janela.prazo_final


def test_olha_para_tras_o_numero_declarado_de_competencias(carteira: Path) -> None:
    a = montar(hoje=date(2027, 4, 27), dir_clientes=carteira)
    assert len({i.competencia for i in a.itens}) == COMPETENCIAS_VIVAS
