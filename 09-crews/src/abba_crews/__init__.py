"""abba-crews — a Camada de Caixa da reforma tributaria.

**Trava de privacidade aplicada no import.** Este projeto toca dado fiscal de cliente.
O `.env.example` documenta as variaveis que desligam telemetria e tracing da CrewAI,
mas documentacao nao desliga nada: ate 2026-09-01 o processo ainda tentava exportar
spans para `telemetry.crewai.com`, observado em execucao.

Aqui os defaults sao aplicados **antes** de qualquer import de crewai. Quem quiser
ligar de volta define a variavel no ambiente — respeitamos a escolha explicita do
operador, e so a dela.
"""

from __future__ import annotations

import os

__version__ = "0.1.0"

_PADROES_PRIVACIDADE = {
    "CREWAI_DISABLE_TELEMETRY": "true",
    "CREWAI_TRACING_ENABLED": "false",
    "OTEL_SDK_DISABLED": "true",
}

for _nome, _valor in _PADROES_PRIVACIDADE.items():
    os.environ.setdefault(_nome, _valor)
