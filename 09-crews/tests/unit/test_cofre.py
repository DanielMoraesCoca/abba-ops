"""A cifra em repouso, e a prova de que ela conversa com o `assessment-brain`.

Este projeto passou a gravar dado fiscal de cliente em disco no M4a. A decisao do socio
(2026-09-02) foi cifrar e, sem senha, **recusar gravar** em vez de degradar para claro.

O teste que mais importa aqui nao e o round-trip — e o de **interoperabilidade**: o
formato foi copiado do `assessment-brain` justamente para que um arquivo escrito aqui
seja legivel la. Se alguem mexer nos parametros do scrypt ou na ordem dos campos do
envelope, o round-trip continua verde e a interoperacao morre em silencio. Por isso o
teste chama o `node` de verdade.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from abba_crews.core.cofre import (
    MAGIC,
    ConteudoAdulterado,
    SenhaAusente,
    cifrar,
    decifrar,
    esta_cifrado,
    ler_possivelmente_cifrado,
    senha_do_ambiente,
    senha_obrigatoria,
)

SENHA = "senha-de-teste"
TEXTO = "dossie — R$ 1.234,56 · CNPJ 00000000000191 · acentuação e ç"
REPORT_CRYPTO = Path("/home/user/assessment-brain/src/core/report-crypto.js")


def test_round_trip() -> None:
    assert decifrar(cifrar(TEXTO, SENHA), SENHA) == TEXTO


def test_envelope_tem_o_formato_da_casa() -> None:
    blob = cifrar(TEXTO, SENHA)
    assert blob.startswith(MAGIC + "\n")
    assert blob.endswith("\n")
    assert esta_cifrado(blob) and not esta_cifrado(TEXTO)


def test_texto_claro_nao_vaza_no_arquivo() -> None:
    blob = cifrar("CNPJ 00000000000191 credito de R$ 100,00", SENHA)
    assert "00000000000191" not in blob
    assert "100,00" not in blob


def test_duas_cifras_do_mesmo_texto_diferem() -> None:
    """Sal e IV aleatorios: dois arquivos iguais nao devem parecer iguais."""
    assert cifrar(TEXTO, SENHA) != cifrar(TEXTO, SENHA)


def test_senha_errada_falha_alto() -> None:
    """GCM autentica. Devolver lixo em silencio seria pior que nao decifrar."""
    with pytest.raises(ConteudoAdulterado):
        decifrar(cifrar(TEXTO, SENHA), "senha-errada")


def test_conteudo_adulterado_falha_alto() -> None:
    """A prova de que a autenticacao serve para alguma coisa: planta a adulteracao."""
    blob = cifrar(TEXTO, SENHA)
    corpo = blob.split("\n")[1]
    virado = ("B" if corpo[-6] != "B" else "C") + corpo[-5:]
    adulterado = f"{MAGIC}\n{corpo[:-6]}{virado}\n"
    assert adulterado != blob
    with pytest.raises(ConteudoAdulterado):
        decifrar(adulterado, SENHA)


def test_cifrar_sem_senha_recusa() -> None:
    with pytest.raises(SenhaAusente):
        cifrar(TEXTO, "")


def test_ler_possivelmente_cifrado_passa_claro_adiante() -> None:
    assert ler_possivelmente_cifrado(TEXTO, None) == TEXTO
    assert ler_possivelmente_cifrado(cifrar(TEXTO, SENHA), SENHA) == TEXTO


def test_senha_obrigatoria_diz_o_que_fazer(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("ABBA_DB_PASSPHRASE", raising=False)
    assert senha_do_ambiente() is None
    with pytest.raises(SenhaAusente, match="ABBA_DB_PASSPHRASE"):
        senha_obrigatoria()

    monkeypatch.setenv("ABBA_DB_PASSPHRASE", "  x  ")
    assert senha_obrigatoria() == "x"


def test_variavel_so_de_espacos_conta_como_ausente(monkeypatch: pytest.MonkeyPatch) -> None:
    """`ABBA_DB_PASSPHRASE=" "` nao pode passar por senha configurada."""
    monkeypatch.setenv("ABBA_DB_PASSPHRASE", "   ")
    assert senha_do_ambiente() is None


# --------------------------------------------------------------------------- #
# Interoperabilidade com o assessment-brain — o teste que justifica o formato
# --------------------------------------------------------------------------- #


def _node() -> str:
    caminho = shutil.which("node")
    if caminho is None or not REPORT_CRYPTO.exists():  # pragma: no cover
        pytest.skip("node ou assessment-brain/report-crypto.js ausente neste ambiente")
    return caminho


def test_o_brain_decifra_o_que_este_projeto_cifra(tmp_path: Path) -> None:
    node = _node()
    arquivo = tmp_path / "dossie.md.enc"
    arquivo.write_text(cifrar(TEXTO, SENHA), encoding="utf-8")

    saida = subprocess.run(
        [
            node,
            "-e",
            f"const c=require({str(REPORT_CRYPTO)!r});"
            f"const fs=require('fs');"
            f"const b=fs.readFileSync({str(arquivo)!r},'utf8');"
            f"process.stdout.write(JSON.stringify({{"
            f"  cifrado: c.isEncryptedReport(b),"
            f"  texto: c.readPossiblyEncrypted(b, {SENHA!r})"
            f"}}));",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    lido = json.loads(saida.stdout)
    assert lido["cifrado"] is True
    assert lido["texto"] == TEXTO, (
        "o assessment-brain nao leu o que este projeto escreveu. Alguem mexeu nos "
        "parametros do scrypt ou na ordem do envelope — o round-trip local continua "
        "verde e a interoperacao morreu."
    )


def test_este_projeto_decifra_o_que_o_brain_cifra(tmp_path: Path) -> None:
    node = _node()
    destino = tmp_path / "do-brain.md.enc"
    subprocess.run(
        [
            node,
            "-e",
            f"const c=require({str(REPORT_CRYPTO)!r});"
            f"const fs=require('fs');"
            f"fs.writeFileSync({str(destino)!r}, c.encryptText({TEXTO!r}, {SENHA!r}));",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert decifrar(destino.read_text(encoding="utf-8"), SENHA) == TEXTO
