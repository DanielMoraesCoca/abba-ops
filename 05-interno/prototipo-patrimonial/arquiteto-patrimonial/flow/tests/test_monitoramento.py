"""Monitoramento de corpus vivo (o motor de retenção) — determinístico, zero LLM."""

from __future__ import annotations

from patrimonio_flow.monitoramento import casos_afetados_por, docs_para_revisar
from patrimonio_flow.tools.rag_corpus import FrescorDoc


def test_docs_para_revisar_pega_revogado_e_vencido():
    fichas = {
        "lei-ok": FrescorDoc(doc_id="lei-ok", valid_from="2024-01-01",
                             last_verified="2026-08-01", ttl_dias=180),
        "lei-revogada": FrescorDoc(doc_id="lei-revogada", superseded_by="lei-nova",
                                   last_verified="2026-08-01", ttl_dias=180),
        "lei-vencida": FrescorDoc(doc_id="lei-vencida", valid_from="2020-01-01",
                                  last_verified="2026-01-01", ttl_dias=30),
    }
    pend = docs_para_revisar(hoje_iso="2026-08-13", fichas=fichas)
    ids = {d["doc_id"] for d in pend}
    assert "lei-ok" not in ids           # vigente e fresca
    assert "lei-revogada" in ids         # superseded_by
    assert "lei-vencida" in ids          # ttl vencido


def test_docs_para_revisar_corpus_vazio():
    assert docs_para_revisar(fichas={}) == []


def test_casos_afetados_por_doc_mudado():
    casos = [
        {"caso_id": "c1", "chunks": ["lei-14754#art-10::1", "cc-sucessao#art-1846::2"]},
        {"caso_id": "c2", "chunks": ["dcbe-bacen#lim::1"]},
        {"caso_id": "c3", "chunks": []},
    ]
    afetados = casos_afetados_por(["lei-14754"], casos)
    ids = {a["caso_id"] for a in afetados}
    assert ids == {"c1"}
    assert afetados[0]["docs_afetados"] == ["lei-14754"]


def test_casos_afetados_nenhum():
    casos = [{"caso_id": "c1", "chunks": ["lei-14754#art-10::1"]}]
    assert casos_afetados_por(["norma-inexistente"], casos) == []
