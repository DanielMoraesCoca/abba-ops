"""A telemetria da CrewAI tem de ficar desligada — e o nome da variavel tem de existir.

Por que este teste existe: no M0 o `.env.example` documentava
`CREWAI_TELEMETRY_OPT_OUT=true`, que **nao existe na biblioteca**. O efeito e o pior
possivel numa trava de privacidade — a documentacao diz que esta desligado, e nao esta.

Este projeto toca dado fiscal de cliente. A defesa contra o erro se repetir e ler o
codigo instalado da CrewAI e falhar se o nome que documentamos sumir de la.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[2]
ENV_EXEMPLO = RAIZ / ".env.example"

# Nomes que o `.env.example` promete e que a biblioteca precisa reconhecer.
VARIAVEIS_PROMETIDAS = ("CREWAI_DISABLE_TELEMETRY", "CREWAI_TRACING_ENABLED")


def _fontes_da_crewai() -> list[Path]:
    try:
        import crewai
    except ImportError:  # pragma: no cover — ambiente sem crewai
        pytest.skip("crewai nao instalado neste ambiente")
    return list(Path(crewai.__file__).parent.rglob("*.py"))


@pytest.mark.parametrize("variavel", VARIAVEIS_PROMETIDAS)
def test_variavel_documentada_existe_na_crewai(variavel: str) -> None:
    """Se a CrewAI renomear a variavel, o nosso `.env.example` vira mentira silenciosa."""
    fontes = _fontes_da_crewai()
    achou = any(variavel in f.read_text(encoding="utf-8", errors="ignore") for f in fontes)
    assert achou, (
        f"{variavel} nao aparece mais no codigo da CrewAI instalada. "
        f"O .env.example promete uma variavel que a biblioteca ignora — "
        f"a telemetria pode estar LIGADA sobre dado fiscal de cliente. "
        f"Procure o nome novo em crewai/telemetry/ e atualize .env.example e este teste."
    )


@pytest.mark.parametrize("variavel", VARIAVEIS_PROMETIDAS)
def test_env_exemplo_desliga_a_variavel(variavel: str) -> None:
    """O valor tambem importa: `CREWAI_DISABLE_TELEMETRY=false` desliga nada."""
    conteudo = ENV_EXEMPLO.read_text(encoding="utf-8")
    esperado = {"CREWAI_DISABLE_TELEMETRY": "true", "CREWAI_TRACING_ENABLED": "false"}[variavel]
    padrao = rf"^{variavel}={esperado}$"
    assert re.search(padrao, conteudo, re.MULTILINE), (
        f".env.example precisa conter exatamente `{variavel}={esperado}`"
    )


def test_nenhuma_variavel_inventada_no_env_exemplo() -> None:
    """Toda `CREWAI_*` que documentamos tem de ser reconhecida pela biblioteca."""
    conteudo = ENV_EXEMPLO.read_text(encoding="utf-8")
    documentadas = set(re.findall(r"^(CREWAI_[A-Z_]+)=", conteudo, re.MULTILINE))
    fontes = _fontes_da_crewai()
    textos = [f.read_text(encoding="utf-8", errors="ignore") for f in fontes]

    inventadas = [v for v in sorted(documentadas) if not any(v in t for t in textos)]
    assert not inventadas, (
        f"variaveis documentadas que a CrewAI nao le: {inventadas}. "
        f"Variavel inventada da a sensacao de configuracao sem efeito nenhum."
    )
