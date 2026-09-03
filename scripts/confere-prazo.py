#!/usr/bin/env python3
"""O dia 15 nao e o prazo — e esta trava existe porque o erro voltou por documento.

## Por que isto mora no `abba-ops`

Ate 2026-09-03 esta regra era um teste do `abba-crews`
(`tests/unit/test_documentacao.py`), e ele alcancava dois documentos DESTE repositorio
lendo `RAIZ.parent` — o projeto estava em staging dentro de `09-crews/`.

Com a extracao para `abba-solucao-tributaria`, aquele teste deixou de alcancar estes
arquivos, e nem deveria: teste que le arquivo fora do proprio repositorio passa conforme
o que estiver no disco de quem roda, nao conforme o que esta versionado.

Mas a protecao nao podia simplesmente sumir. **O erro do prazo sobreviveu justamente
nestes dois documentos depois de corrigido no codigo** — a versao errada dizia que a
empresa tinha de se manifestar "ate o dia 15". Quem lesse isso alarmaria na data errada e
daria por perdido o que ainda dava para manifestar. Entao a regra mudou de casa em vez de
morrer: extrair o projeto e levar a trava embora seria apagar uma protecao em silencio.

## A regra

O dia 15 (20 para quem entrega DeRE) e a data em que a apuracao pre-preenchida
**aparece**. O prazo de manifestacao vai ate o **ultimo dia util do mes seguinte**; nao
havendo manifestacao, os valores propostos prevalecem e o credito tributario e constituido
— o que equivale a confissao de divida (art. 348, §1º da LC 214/2025).

Logo: documento que cita o dia 15 tem de citar tambem o prazo real. Nao e questao de
estilo — as duas datas levam a acoes diferentes em meses diferentes.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

DOCUMENTOS = (
    "05-interno/plano-camada-de-caixa-2027.md",
    "06-ferramentas/blueprint-crews-camada-de-caixa.md",
)
"""Os documentos deste repositorio que falam do produto.

Lista explicita, e nao varredura do repositorio inteiro: aqui ha documento de outras
frentes que cita "dia 15" por motivo que nada tem a ver com a reforma tributaria.
"""

DIA_15 = re.compile(r"dia\s+15")
PRAZO_REAL = re.compile(r"[uú]ltimo dia [uú]til")


def main() -> int:
    faltando = [nome for nome in DOCUMENTOS if not (RAIZ / nome).exists()]
    if faltando:
        # Documento renomeado ou movido nao encolhe a varredura em silencio. Foi assim que
        # a trava original quase se perdeu na extracao: ela dependia de alguem lembrar.
        print(f"::error::documento do produto nao encontrado: {faltando}")
        print("Se foi renomeado, atualize DOCUMENTOS deliberadamente.")
        return 1

    problemas = []
    for nome in DOCUMENTOS:
        texto = (RAIZ / nome).read_text(encoding="utf-8")
        if DIA_15.search(texto) and not PRAZO_REAL.search(texto):
            problemas.append(nome)

    for nome in problemas:
        print(f"::error file={nome}::cita o dia 15 e nao cita o prazo real")
        print(
            f"  {nome}: o dia 15 e quando a proposta APARECE. A manifestacao vai ate o "
            f"ultimo dia util do mes seguinte, e o silencio equivale a confissao de "
            f"divida (LC 214/2025, art. 348 §1º)."
        )
    if problemas:
        return 1

    print(f"ok — {len(DOCUMENTOS)} documento(s) do produto, prazo citado corretamente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
