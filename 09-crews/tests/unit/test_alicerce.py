"""O alicerce do projeto — a configuracao que decide o que roda em producao.

## Por que este arquivo existe

Em 2026-09-02 o commit `7ec9613`, intitulado **"CI: matriz de versoes e o piso de Python
honesto"**, alterou oito linhas do `pyproject.toml` — **todas de comentario**. O
`requires-python` continuou `>=3.10`. O `target-version` do ruff continuou `py310`. O
commit, o registro V4h e o relato ao socio afirmaram uma correcao que nao aconteceu.

Causa mecanica: o script de edicao fazia tres substituicoes e so entao gravava o arquivo.
A terceira levantou `AssertionError`, o `write_text` nunca rodou, e os checks seguintes
ficaram verdes porque **nada estava errado no que sobrou** — so faltava o que nao entrou.

E a classe "promessa sem mecanismo" na forma mais pura: o registro afirma, o mecanismo
nao existe. As travas deste projeto olhavam para o codigo (`test_promessas`), para a
documentacao (`test_documentacao`) e para os produtos (`test_registry`). **Nenhuma olhava
para a configuracao**, que e onde essa passou.

## As tres invariantes

1. **os pisos concordam entre si** — `requires-python`, `ruff.target-version` e
   `mypy.python_version` tem de apontar para a mesma versao;
2. **o piso e instalavel** — declarar uma versao em que o projeto nao instala e promessa
   que ele nao pode cumprir;
3. **o codigo nao usa simbolo acima do piso** — a regra que o ruff nao tem: ele sugere
   idioma novo quando o alvo e alto, mas nao reprova o uso de um simbolo mais novo que o
   proprio alvo.
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[2]
PYPROJECT = RAIZ / "pyproject.toml"


def _config() -> dict:  # type: ignore[type-arg]
    return tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))


def _piso_declarado() -> tuple[int, int]:
    """O `>=X.Y` de `requires-python`, como tupla."""
    bruto = _config()["project"]["requires-python"]
    m = re.search(r">=\s*(\d+)\.(\d+)", bruto)
    assert m, f"requires-python sem piso legivel: {bruto!r}"
    return int(m.group(1)), int(m.group(2))


# --------------------------------------------------------------------------- #
# 1. Os pisos concordam
# --------------------------------------------------------------------------- #


def test_ruff_mira_o_piso_declarado() -> None:
    """Lint que mira diferente do que o pacote suporta nao avisa: ele introduz o bug.

    Foi assim que `timezone.utc` virou `datetime.UTC` (3.11+) num pacote que dizia
    suportar 3.10 — e depois o alvo foi baixado para `py310` para "casar", deixando o
    `datetime.UTC` no codigo.
    """
    maior, menor = _piso_declarado()
    alvo = _config()["tool"]["ruff"]["target-version"]
    assert alvo == f"py{maior}{menor}", (
        f"ruff mira {alvo} e o pacote declara piso {maior}.{menor}. "
        f"Os dois tem de dizer a mesma coisa."
    )


def test_mypy_confere_contra_o_piso_declarado() -> None:
    maior, menor = _piso_declarado()
    versao = _config()["tool"]["mypy"]["python_version"]
    assert versao == f"{maior}.{menor}", (
        f"mypy confere contra {versao} e o pacote declara piso {maior}.{menor}."
    )


# --------------------------------------------------------------------------- #
# 2. O piso e real
# --------------------------------------------------------------------------- #


def test_o_piso_declarado_nao_e_menor_que_o_das_dependencias() -> None:
    """`onnxruntime`, via `crewai[tools]`, nao publica wheel para cp310.

    Declarar `>=3.10` era uma promessa que o projeto **nao consegue cumprir**: `uv sync`
    em 3.10 falha na instalacao, antes de qualquer linha nossa rodar.
    """
    maior, menor = _piso_declarado()
    assert (maior, menor) >= (3, 11), (
        "o piso nao pode ser menor que 3.11: onnxruntime (dependencia transitiva da "
        "crewai) so publica wheels cp311+. Conferido rodando `uv sync --python 3.10`."
    )


def test_o_interpretador_do_desenvolvimento_respeita_o_piso() -> None:
    assert sys.version_info[:2] >= _piso_declarado()


# --------------------------------------------------------------------------- #
# 3. O codigo nao usa simbolo acima do piso
# --------------------------------------------------------------------------- #

SIMBOLOS_POR_VERSAO = {
    (3, 11): ("datetime.UTC", "from datetime import UTC", "typing.Self", "StrEnum"),
    (3, 12): ("itertools.batched", "typing.override"),
}
"""Simbolos que so existem a partir da versao dada. Cresce quando aparecer caso novo."""


def _fontes() -> list[Path]:
    return sorted((RAIZ / "src").rglob("*.py"))


@pytest.mark.parametrize("versao", sorted(SIMBOLOS_POR_VERSAO))
def test_nenhum_simbolo_acima_do_piso(versao: tuple[int, int]) -> None:
    """A regra que o ruff nao tem.

    Ele sugere idiomas novos quando o alvo e alto, mas nao reprova o **uso** de um
    simbolo mais novo que o alvo. Com piso 3.10 e `datetime.UTC` no codigo, `ruff check`
    passava — e o import teria quebrado em 3.10.
    """
    if _piso_declarado() >= versao:
        pytest.skip(f"o piso ja e {versao[0]}.{versao[1]} ou maior")

    achados = []
    for f in _fontes():
        texto = f.read_text(encoding="utf-8")
        for simbolo in SIMBOLOS_POR_VERSAO[versao]:
            if simbolo in texto:
                achados.append(f"{f.relative_to(RAIZ)}: {simbolo}")
    assert not achados, (
        f"simbolos de {versao[0]}.{versao[1]}+ usados com piso menor: {achados}"
    )


def test_a_lista_de_simbolos_nao_esta_vazia() -> None:
    """Sem isto o teste acima passaria por vacuo se alguem esvaziasse a tabela."""
    assert all(SIMBOLOS_POR_VERSAO.values())
