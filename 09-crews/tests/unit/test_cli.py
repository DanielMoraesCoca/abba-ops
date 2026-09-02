"""A CLI — a superficie que os socios operam, e que ate 2026-09-02 nao tinha teste nenhum.

Nenhum arquivo de teste importava `abba_crews.cli`. Nove comandos, dois ajudantes e
todos os caminhos de recusa rodavam sem rede de protecao — e foi por isso que passaram
despercebidos um ramo morto (`if prontos:` em `produtos`, que nunca executa) e duas
excecoes que chegavam ao usuario como traceback cru apesar de `cofre.py` descrever a
falha alta como comportamento de projeto.

O que se trava aqui e o que o operador ve: a mensagem certa e o codigo de saida certo.
Recusa que sai como traceback e recusa que parece defeito.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from abba_crews.cli import app

runner = CliRunner()
CNPJ = "00000000000191"


@pytest.fixture
def ambiente(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    raiz = tmp_path / "dossies"
    monkeypatch.setenv("ABBA_DB_PASSPHRASE", "senha-de-teste")
    monkeypatch.setenv("ABBA_CREWS_DOSSIES", str(raiz))
    return raiz


def roda(*args: str) -> object:
    return runner.invoke(app, list(args))


# ------------------------------ leitura ------------------------------ #


def test_produtos_diz_a_verdade_sobre_o_que_e_vendavel() -> None:
    r = roda("produtos")
    assert r.exit_code == 0
    assert "Vendavel hoje: NENHUM" in r.stdout, (
        "a trava de honestidade do projeto. Se isto mudar, foi porque um produto "
        "chegou a PRODUCAO — e ai o gate declarado no registry tem de estar cumprido."
    )


def test_golden_roda_e_aprova() -> None:
    r = roda("golden")
    assert r.exit_code == 0
    assert "golden set v0 aprovado" in r.stdout


def test_cobertura_reporta_a_tabela_vazia() -> None:
    r = roda("cobertura")
    assert r.exit_code == 0
    assert "COBERTURA" in r.stdout
    assert "a confirmar" in r.stdout


def test_janela_separa_disponibilizacao_de_prazo() -> None:
    r = roda("janela", "-c", "2027-03", "--hoje", "2027-04-20")
    assert r.exit_code == 0
    assert "disponibilizacao   15/04/2027" in r.stdout
    assert "prazo final        30/04/2027" in r.stdout


def test_janela_com_dere_atrasa_a_proposta_e_nao_o_prazo() -> None:
    r = roda("janela", "-c", "2027-03", "--dere", "--hoje", "2027-04-20")
    assert "disponibilizacao   20/04/2027" in r.stdout
    assert "prazo final        30/04/2027" in r.stdout


# ------------------------------ o ciclo do gate ------------------------------ #


def _guarda(ambiente: Path) -> str:
    r = roda("sentinela", "--cnpj", CNPJ, "-c", "2027-03", "--hoje", "2027-04-20",
             "--mock", "--guardar")
    assert r.exit_code == 0, r.stdout
    linha = next(x for x in r.stdout.splitlines() if "guardado" in x)
    return linha.split(":")[-1].strip()


def test_ciclo_completo_guardar_listar_assinar(ambiente: Path) -> None:
    ref = _guarda(ambiente)

    listagem = roda("dossies")
    assert "RASCUNHO" in listagem.stdout

    assinatura = roda("aprovar", "--chave", ref, "--por", "Nome do Contador")
    assert assinatura.exit_code == 0
    assert "ASSINADO" in assinatura.stdout
    assert "Assinar nao e transmitir" in assinatura.stdout

    assert "APROVADO" in roda("dossies").stdout
    assert "# APROVADO" in roda("ver", "--chave", ref, "--assinado").stdout


def test_assinar_com_nome_diferente_do_responsavel_avisa(ambiente: Path) -> None:
    """A divergencia ja era registrada no indice e nunca aparecia."""
    ref = _guarda(ambiente)
    r = roda("aprovar", "--chave", ref, "--por", "Outra Pessoa")
    assert r.exit_code == 0
    assert "ATENCAO" in r.stdout
    assert "Nome do Contador" in r.stdout


def test_assinar_duas_vezes_recusa_com_mensagem(ambiente: Path) -> None:
    ref = _guarda(ambiente)
    roda("aprovar", "--chave", ref, "--por", "Nome do Contador")
    r = roda("aprovar", "--chave", ref, "--por", "Nome do Contador")
    assert r.exit_code == 1
    assert "RECUSADO" in r.stdout and "ja foi assinado" in r.stdout


def test_devolver_exige_motivo_e_aparece_na_listagem(ambiente: Path) -> None:
    ref = _guarda(ambiente)
    r = roda("devolver", "--chave", ref, "--por", "Nome do Contador",
             "--motivo", "faltou a nota 42")
    assert r.exit_code == 0
    assert "DEVOLVIDO" in roda("dossies").stdout


# ------------------------------ as recusas ------------------------------ #


def test_sem_senha_recusa_e_nao_grava_nada(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A decisao do socio, no caminho que o operador realmente usa."""
    raiz = tmp_path / "dossies"
    monkeypatch.delenv("ABBA_DB_PASSPHRASE", raising=False)
    monkeypatch.setenv("ABBA_CREWS_DOSSIES", str(raiz))
    r = roda("sentinela", "--cnpj", CNPJ, "-c", "2027-03", "--mock", "--guardar")
    assert r.exit_code == 1
    assert "ABBA_DB_PASSPHRASE" in r.stdout
    assert not raiz.exists() or not list(raiz.rglob("*.enc"))


def test_raiz_dentro_de_git_recusa(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    (tmp_path / ".git").mkdir()
    monkeypatch.setenv("ABBA_DB_PASSPHRASE", "x")
    monkeypatch.setenv("ABBA_CREWS_DOSSIES", str(tmp_path / "dossies"))
    r = roda("dossies")
    assert r.exit_code == 1
    assert "git" in r.stdout


def test_ver_dossie_adulterado_recusa_sem_traceback(ambiente: Path) -> None:
    """`cofre.py` descreve a falha alta como desenho; entrega-la como traceback e susto."""
    ref = _guarda(ambiente)
    alvo = next(ambiente.rglob("*.md.enc"))
    alvo.write_text("ABBA-ENC-1\nQUFB\n", encoding="utf-8")
    r = roda("ver", "--chave", ref)
    assert r.exit_code == 1
    assert "Traceback" not in r.stdout
    assert "autenticar" in r.stdout or "ilegivel" in r.stdout or "truncado" in r.stdout


def test_chave_desconhecida_recusa_com_mensagem_util(ambiente: Path) -> None:
    _guarda(ambiente)
    r = roda("ver", "--chave", "zzzzzzzz")
    assert r.exit_code == 1
    assert "nenhum dossie" in r.stdout


def test_estado_invalido_lista_os_validos(ambiente: Path) -> None:
    r = roda("dossies", "--estado", "INVENTADO")
    assert r.exit_code == 1
    assert "RASCUNHO" in r.stdout and "APROVADO" in r.stdout


def test_caso_desconhecido_no_mock_lista_os_validos() -> None:
    r = roda("sentinela", "--cnpj", CNPJ, "-c", "2027-03", "--mock", "--caso", "nao-existe")
    assert r.exit_code == 1
    assert "caso desconhecido" in r.stdout


def test_sem_mock_recusa_citando_o_gate_do_m6() -> None:
    """Recusa honesta: coleta real depende da credencial da Plataforma RTC."""
    r = roda("sentinela", "--cnpj", CNPJ, "-c", "2027-03")
    assert r.exit_code != 0
    assert isinstance(r.exception, NotImplementedError)
    assert "M6" in str(r.exception)
