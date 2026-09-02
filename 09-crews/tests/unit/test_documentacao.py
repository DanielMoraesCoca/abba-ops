"""Travas na documentacao — porque os dois piores erros deste projeto voltaram por ela.

Codigo corrigido e documento nao corrigido e o mesmo erro, agora mais dificil de achar:
ninguem reabre o modulo, todo mundo le o README.

Os dois casos reais, ambos encontrados no README **depois** de corrigidos no codigo:

1. **O prazo.** O dia 15 (20 com DeRE) e a data de DISPONIBILIZACAO da proposta. O prazo
   de manifestacao vai ate o ultimo dia util do mes seguinte. O README ainda dizia "se a
   empresa nao se manifestar ate o dia 15" — alarmaria na data errada e daria por perdido
   o que ainda dava para manifestar.
2. **A variavel de telemetria.** `CREWAI_TELEMETRY_OPT_OUT` nao existe na biblioteca. O
   `.env.example` foi corrigido no M0 e o nome inventado sobreviveu no README, prometendo
   uma trava de privacidade que a CrewAI ignora — sobre dado fiscal de cliente.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[2]
IGNORADOS = {".venv", ".pytest_cache", ".git", ".ruff_cache", ".mypy_cache", "dist", "build"}


def _markdowns_do_projeto() -> list[Path]:
    return [p for p in RAIZ.rglob("*.md") if not (IGNORADOS & set(p.parts))]


# Documentos do `abba-ops` que falam DESTE produto. Entram na varredura porque o erro do
# prazo (P3b) tinha sobrevivido justamente neles depois de corrigido no codigo — e la a
# correcao dependia de eu lembrar. O caminho e relativo a raiz do repo, e a lista e
# explicita: varrer o abba-ops inteiro traria documento de outra frente.
DOCS_DO_PRODUTO_NO_OPS = (
    "05-interno/plano-camada-de-caixa-2027.md",
    "06-ferramentas/blueprint-crews-camada-de-caixa.md",
)


def _markdowns_do_ops() -> list[Path]:
    ops = RAIZ.parent
    return [c for nome in DOCS_DO_PRODUTO_NO_OPS if (c := ops / nome).exists()]


MARKDOWNS = sorted(_markdowns_do_projeto() + _markdowns_do_ops())
"""Todo markdown deste projeto, mais os documentos do abba-ops que falam dele."""


def test_ha_markdown_para_conferir() -> None:
    assert MARKDOWNS, "nenhum .md encontrado — o teste estaria passando por vacuo"


def test_os_documentos_do_ops_estao_na_varredura() -> None:
    """O erro do prazo sobreviveu no `abba-ops` depois de corrigido aqui.

    Se o staging sair de dentro do abba-ops (`STAGING.md`), estes caminhos deixam de
    existir e este teste avisa — em vez de a varredura encolher em silencio.
    """
    achados = _markdowns_do_ops()
    assert len(achados) == len(DOCS_DO_PRODUTO_NO_OPS), (
        f"documentos do produto no abba-ops nao encontrados: "
        f"{set(DOCS_DO_PRODUTO_NO_OPS) - {p.name for p in achados}}. "
        f"Se o projeto foi extraido para o repo proprio, remova-os desta lista "
        f"deliberadamente — nao deixe a varredura encolher sozinha."
    )


@pytest.mark.parametrize("doc", MARKDOWNS, ids=lambda p: p.name)
def test_quem_fala_do_dia_15_tem_de_falar_do_prazo_real(doc: Path) -> None:
    """Citar a disponibilizacao sem citar o prazo e como o erro se parecia."""
    texto = doc.read_text(encoding="utf-8")
    if not re.search(r"dia\s+15", texto):
        return
    assert re.search(r"[uú]ltimo dia [uú]til", texto), (
        f"{doc.relative_to(RAIZ)} menciona o dia 15 e nao menciona o prazo real. "
        f"O dia 15 e quando a proposta APARECE; a manifestacao vai ate o ultimo dia "
        f"util do mes seguinte. Ver docs/PENDENCIAS.md, P3b."
    )


@pytest.mark.parametrize("doc", MARKDOWNS, ids=lambda p: p.name)
def test_nenhum_documento_cita_variavel_crewai_inexistente(doc: Path) -> None:
    """Mesma trava do `.env.example`, agora sobre o que as pessoas realmente leem."""
    import crewai

    citadas = set(re.findall(r"CREWAI_[A-Z_]+", doc.read_text(encoding="utf-8")))
    if not citadas:
        return
    fontes = [
        f.read_text(encoding="utf-8", errors="ignore")
        for f in Path(crewai.__file__).parent.rglob("*.py")
    ]
    inventadas = sorted(v for v in citadas if not any(v in t for t in fontes))
    assert not inventadas, (
        f"{doc.relative_to(RAIZ)} documenta variaveis que a CrewAI nao le: {inventadas}. "
        f"Trava de privacidade documentada e nao aplicada e pior que trava nenhuma."
    )
