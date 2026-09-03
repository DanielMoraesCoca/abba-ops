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


# --------------------------------------------------------------------------- #
# Operar uma carteira (M7) — o ponto cego que a engenharia reversa achou
# --------------------------------------------------------------------------- #


def test_agenda_roda_sem_senha_e_diz_que_esta_incompleta() -> None:
    """Sem senha ela responde o que DEVERIA ter sido conferido, e avisa disso."""
    r = roda("agenda", "--hoje", "2027-04-27")
    assert r.exit_code == 0
    assert "agenda de 27/04/2027" in r.stdout
    assert "ABBA_DB_PASSPHRASE" in r.stdout


def test_agenda_mostra_o_que_exige_acao_e_esconde_o_resto(ambiente: Path) -> None:
    r = roda("agenda", "--hoje", "2027-04-27")
    assert "sem_conferencia" in r.stdout
    assert "prazo_perdido" not in r.stdout, "sem --tudo, so o que exige acao"

    completa = roda("agenda", "--hoje", "2027-04-27", "--tudo")
    assert "prazo_perdido" in completa.stdout


def test_agenda_reflete_o_dossie_guardado(ambiente: Path) -> None:
    """A fila tem de saber o que ja foi conferido — senao repete trabalho feito."""
    assert "sem_conferencia" in roda("agenda", "--hoje", "2027-04-27").stdout
    _guarda(ambiente)
    assert "aguardando_assinatura" in roda("agenda", "--hoje", "2027-04-27").stdout


def test_agenda_depois_do_prazo_para_de_pedir_acao(ambiente: Path) -> None:
    r = roda("agenda", "--hoje", "2027-06-10", "--tudo")
    assert "prazo_perdido" in r.stdout
    assert "0 de" in r.stdout


def test_sentinela_sem_cnpj_e_sem_todos_recusa() -> None:
    r = roda("sentinela", "-c", "2027-03", "--mock")
    assert r.exit_code == 1
    assert "--todos" in r.stdout


def test_carteira_roda_todos_os_clientes(ambiente: Path) -> None:
    r = roda("sentinela", "-c", "2027-03", "--hoje", "2027-04-20", "--mock", "--todos", "--guardar")
    assert r.exit_code == 0
    assert "1/1 conferido(s)" in r.stdout
    assert "RASCUNHO" in roda("dossies").stdout


def test_um_cliente_quebrado_nao_derruba_o_lote(
    ambiente: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Duzentos CNPJs em que o 37º aborta a rodada é pior que não ter lote nenhum.

    Os 163 seguintes ficariam sem conferência e ninguém saberia quais.
    """
    from abba_crews.core import clientes as _clientes

    dirc = tmp_path / "clientes"
    dirc.mkdir()
    for cnpj, nome in (("00000000000191", "Empresa A"), ("11444777000161", "Empresa B")):
        (dirc / f"{cnpj}.yaml").write_text(
            f'cnpj: "{cnpj}"\nrazao_social: "{nome}"\ntolerancia_brl: "0.00"\n'
            'aprovacao:\n  responsavel_nome: "Maria Contadora"\n'
            '  responsavel_email: "maria@escritorio.com.br"\n',
            encoding="utf-8",
        )
    (dirc / "11222333000181.yaml").write_text('cnpj: "11222333000181"\n', encoding="utf-8")
    monkeypatch.setattr(_clientes, "DIR_PADRAO", dirc)

    r = roda("sentinela", "-c", "2027-03", "--hoje", "2027-04-20", "--mock", "--todos", "--guardar")
    assert "2/2 conferido(s)" in r.stdout, "os validos tem de rodar apesar do quebrado"
    assert "11222333000181.yaml nao carregou" in r.stdout
    assert r.exit_code == 1, "o lote termina em nao-zero quando algo ficou de fora"
