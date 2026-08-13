"""Põe `src/` (pacote patrimonio_flow) e `eval/` (run_eval) no sys.path para os
testes rodarem sem instalar o pacote. `pytest` a partir de flow/."""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]  # flow/
for _p in (ROOT / "src", ROOT / "eval"):
    _s = str(_p)
    if _s not in sys.path:
        sys.path.insert(0, _s)
