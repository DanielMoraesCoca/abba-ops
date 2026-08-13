"""Corpus de DEMONSTRAÇÃO — prova que o pipeline PODE recuperar de um corpus real
(fictício, marcado DEMO) e que o override por env CORPUS_DIR funciona. Zero LLM.
"""

from __future__ import annotations

import os

from patrimonio_flow.tools.rag_corpus import buscar_no_corpus, carregar_fichas


def test_demo_carrega_fichas():
    fichas = carregar_fichas("corpus-demo")
    assert "demo-lei-exterior" in fichas
    assert len(fichas) == 6


def test_demo_recupera_sobre_exterior():
    r = buscar_no_corpus("aliquota quinze lucros controlada exterior",
                         corpus_dir="corpus-demo", as_of="2026-08-13")
    assert r, "esperava recuperar chunk do corpus-demo"
    assert any(c.doc_id == "demo-lei-exterior" for c in r)
    # todo chunk demo é marcado (nunca confundível com autoridade real)
    assert all("DEMO" in c.texto for c in r)


def test_demo_recupera_sobre_legitima():
    r = buscar_no_corpus("legitima herdeiro necessario testamento parte disponivel",
                         corpus_dir="corpus-demo", as_of="2026-08-13")
    assert any(c.doc_id == "demo-cc-sucessao" for c in r)


def test_env_corpus_dir_override():
    os.environ["CORPUS_DIR"] = "corpus-demo"
    try:
        r = buscar_no_corpus("estate tax nao-residente eua", as_of="2026-08-13")
        assert any(c.doc_id == "demo-ficha-eua" for c in r)
    finally:
        del os.environ["CORPUS_DIR"]


def test_sem_env_usa_corpus_real_vazio():
    # sem CORPUS_DIR e sem arg, cai no corpus real (corpus/, vazio) → abstenção
    assert "CORPUS_DIR" not in os.environ
    assert buscar_no_corpus("qualquer lei", as_of="2026-08-13") == []
