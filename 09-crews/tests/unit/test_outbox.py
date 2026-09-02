"""O outbox — como este projeto fala com o cerebro sem escrever nele.

O `assessment-brain` e o sistema de registro da ABBA. Duas memorias concorrentes
significam duas verdades, e a que ficasse fora do cerebro nao seria auditavel nem
apagavel pelo `abba forget`. Entao aqui nao se escreve no cerebro: registra-se intencao,
e o `abba crews sync` (lado Node) aplica pelas funcoes sancionadas.

O que estes testes travam:

1. **origem `tool_output`, nunca `human_stated`** — nada que um programa afirme pode
   sobrepor o que uma pessoa afirmou;
2. **a assinatura vira decisao, nao fato** — ato humano nomeado tem lugar proprio no
   cerebro, e nao e a porta de autoridade maxima;
3. **id estavel** — aplicar duas vezes tem de ser inofensivo;
4. **cifrado como o resto** — a intencao carrega CNPJ, competencia e valores.
"""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import pytest

from abba_crews.core.arquivo import Arquivo
from abba_crews.core.cofre import MAGIC, decifrar
from abba_crews.core.outbox import (
    ORIGEM_DESTE_PROJETO,
    Outbox,
    TipoIntencao,
    da_assinatura,
    da_conferencia,
)

SENHA = "senha-de-teste"
ENG = "eng_teste"
CNPJ = "00000000000191"
COMP = "2027-03"


@pytest.fixture(autouse=True)
def _senha(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ABBA_DB_PASSPHRASE", SENHA)


@pytest.fixture
def outbox(tmp_path: Path) -> Outbox:
    return Outbox(Arquivo(tmp_path / "dossies"))


def _conferencia(impressao: str = "aaaa1111"):  # type: ignore[no-untyped-def]
    return da_conferencia(
        engagement_id=ENG, cnpj=CNPJ, competencia=COMP, impressao=impressao,
        favoravel=Decimal("100.00"), desfavoravel=Decimal("0.00"),
        descartado=Decimal("0.00"), itens=1,
    )


def _assinatura(impressao: str = "aaaa1111", por: str = "Maria Contadora"):  # type: ignore[no-untyped-def]
    return da_assinatura(
        engagement_id=ENG, cnpj=CNPJ, competencia=COMP, impressao=impressao,
        por=por, sha256="a" * 64, efeito_liquido=Decimal("100.00"),
    )


# --------------------------------------------------------------------------- #
# 1. Autoridade de origem
# --------------------------------------------------------------------------- #


def test_fato_sai_como_tool_output() -> None:
    """Autoridade 2. Nunca sobrepoe `human_stated` (3), que e so por `--by "Nome"`."""
    assert ORIGEM_DESTE_PROJETO == "tool_output"
    assert _conferencia().dados["origin"] == "tool_output"


def test_nenhuma_intencao_pede_human_stated() -> None:
    """A trava do inegociavel: um programa nao entra pela porta de autoridade maxima."""
    for intencao in (_conferencia(), _assinatura()):
        assert "human_stated" not in str(intencao.dados.values())


def test_a_assinatura_vira_decisao_e_nao_fato() -> None:
    """Ato humano nomeado tem lugar proprio no cerebro: decisao com `decided_by`."""
    i = _assinatura(por="Maria Contadora")
    assert i.tipo is TipoIntencao.DECISAO_MANIFESTACAO
    assert i.dados["decided_by"] == "Maria Contadora"
    assert "origin" not in i.dados


def test_a_decisao_diz_que_assinar_nao_e_transmitir() -> None:
    """A frase acompanha o registro, nao so o documento."""
    assert "nao e transmitir" in _assinatura().dados["description"]


# --------------------------------------------------------------------------- #
# 2. Idempotencia
# --------------------------------------------------------------------------- #


def test_mesma_afirmacao_mesmo_id() -> None:
    assert _conferencia().id == _conferencia().id
    assert _assinatura().id == _assinatura().id


def test_conferencias_de_impressoes_diferentes_sao_intencoes_diferentes() -> None:
    """Conferir de novo com documentos novos e outra afirmacao — o cerebro e que decide
    a supersessao, pela regra bitemporal dele. Nao cabe a nos resolver aqui."""
    assert _conferencia("aaaa1111").id != _conferencia("bbbb2222").id


def test_fato_e_decisao_da_mesma_competencia_nao_colidem() -> None:
    assert _conferencia().id != _assinatura().id


def test_registrar_duas_vezes_nao_duplica(outbox: Outbox) -> None:
    outbox.registrar(_conferencia())
    outbox.registrar(_conferencia())
    assert len(outbox.listar()) == 1


# --------------------------------------------------------------------------- #
# 3. Disco
# --------------------------------------------------------------------------- #


def test_a_intencao_fica_cifrada(outbox: Outbox) -> None:
    i = outbox.registrar(_conferencia())
    bruto = (outbox.raiz / f"{i.id}.json.enc").read_text(encoding="utf-8")
    assert bruto.startswith(MAGIC)
    assert CNPJ not in bruto
    assert CNPJ in decifrar(bruto, SENHA)


def test_marcar_aplicada_tira_da_fila_sem_apagar_a_carga(outbox: Outbox) -> None:
    """Nada e apagado: aplicada vira registro do que foi ao cerebro e quando."""
    i = outbox.registrar(_conferencia())
    assert len(outbox.listar(pendentes=True)) == 1
    outbox.marcar_aplicada(i.id, por="teste")
    assert outbox.listar(pendentes=True) == ()
    assert len(outbox.listar()) == 1
    assert (outbox.raiz / f"{i.id}.json.enc").exists()


def test_sem_senha_nao_enfileira(outbox: Outbox, monkeypatch: pytest.MonkeyPatch) -> None:
    from abba_crews.core.cofre import SenhaAusente

    monkeypatch.delenv("ABBA_DB_PASSPHRASE", raising=False)
    with pytest.raises(SenhaAusente):
        outbox.registrar(_conferencia())


# --------------------------------------------------------------------------- #
# 4. Integracao com o produto
# --------------------------------------------------------------------------- #


def test_cliente_sem_engagement_nao_gera_intencao(tmp_path: Path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """`engagement_id` nulo = cliente fora do cerebro. Inventar um seria pior."""
    from abba_crews.core.sinteticos import golden_set
    from abba_crews.flows.sentinela_flow import Fonte, SentinelaFlow

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", SENHA)
    arq = Arquivo(tmp_path / "dossies")
    caso = next(c for c in golden_set() if c.id == "positivo-credito-omitido")
    f = SentinelaFlow(
        fonte=Fonte(documentos=caso.documentos, apuracao=caso.apuracao), arquivo=arq
    )
    f.kickoff(
        {"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": "2027-04-20"}}
    )
    assert f.state.registro is not None
    assert f.state.registro.engagement_id is None
    assert Outbox(arq).listar() == ()


def test_ciclo_completo_produz_as_duas_intencoes(tmp_path: Path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """Conferir e assinar enfileira fato + decisao. E o caminho que o `sync` drena.

    O caso negativo acima prova que sem engagement nada e registrado; este prova o
    outro lado — senao a metade que importa passaria sem teste.
    """
    from abba_crews.core.aprovacao import aprovar
    from abba_crews.core.sinteticos import golden_set
    from abba_crews.flows.sentinela_flow import Fonte, SentinelaFlow

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", SENHA)
    clientes = tmp_path / "clientes"
    clientes.mkdir()
    (clientes / f"{CNPJ}.yaml").write_text(
        f'cnpj: "{CNPJ}"\n'
        'razao_social: "Empresa com Engagement"\n'
        'regime: regular\n'
        'entrega_dere: false\n'
        f'engagement_id: "{ENG}"\n'
        'tolerancia_brl: "0.00"\n'
        "aprovacao:\n"
        '  responsavel_nome: "Maria Contadora"\n'
        '  responsavel_email: "maria@escritorio.com.br"\n',
        encoding="utf-8",
    )

    arq = Arquivo(tmp_path / "dossies")
    caso = next(c for c in golden_set() if c.id == "positivo-credito-omitido")
    f = SentinelaFlow(
        fonte=Fonte(documentos=caso.documentos, apuracao=caso.apuracao),
        arquivo=arq,
        dir_clientes=clientes,
    )
    f.kickoff(
        {"crewai_trigger_payload": {"cnpj": CNPJ, "competencia": COMP, "hoje": "2027-04-20"}}
    )

    caixa = Outbox(arq)
    assert [i.tipo for i in caixa.listar()] == [TipoIntencao.FATO_COMPETENCIA_CONFERIDA]

    assert f.state.registro is not None
    aprovar(arq, f.state.registro.chave, por="Maria Contadora")

    tipos = {i.tipo for i in caixa.listar()}
    assert tipos == {TipoIntencao.FATO_COMPETENCIA_CONFERIDA, TipoIntencao.DECISAO_MANIFESTACAO}
    decisao = next(i for i in caixa.listar() if i.tipo is TipoIntencao.DECISAO_MANIFESTACAO)
    assert decisao.dados["decided_by"] == "Maria Contadora"
    assert decisao.engagement_id == ENG
