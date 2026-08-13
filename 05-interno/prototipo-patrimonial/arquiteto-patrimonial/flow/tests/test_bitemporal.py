"""Corpus vivo/bitemporal — vigência por data-do-caso + frescor. Zero LLM.

Fixtures SINTÉTICAS (não são autoridade jurídica — só exercitam a máquina de
recuperação). O corpus real é curado por advogado (briefing-corpus-hector.md).
"""

from __future__ import annotations

from patrimonio_flow.tools.rag_corpus import (
    ChunkRecuperado, FrescorDoc, buscar_no_corpus,
)


def _chunk(chunk_id, texto, frescor, tipo="lei"):
    return ChunkRecuperado(chunk_id=chunk_id, doc_id=frescor.doc_id, texto=texto,
                           score=0.0, tipo=tipo, frescor=frescor)


def test_vigente_em_janela():
    f = FrescorDoc(doc_id="x", valid_from="2024-01-01", valid_to="2025-12-31")
    assert f.vigente_em("2024-06-01") is True
    assert f.vigente_em("2023-12-31") is False   # antes de vigorar
    assert f.vigente_em("2026-01-01") is False   # depois de revogada


def test_superseded_nao_vigente():
    f = FrescorDoc(doc_id="x", superseded_by="y")
    assert f.vigente_em("2024-06-01") is False


def test_desatualizado_por_ttl():
    f = FrescorDoc(doc_id="x", last_verified="2026-01-01", ttl_dias=30)
    assert f.desatualizado("2026-01-15") is False   # dentro do TTL
    assert f.desatualizado("2026-03-01") is True    # TTL vencido
    assert FrescorDoc(doc_id="x").desatualizado("2026-01-01") is True  # sem last_verified → stale


def test_busca_filtra_por_as_of():
    vigente = FrescorDoc(doc_id="lei-nova", valid_from="2024-01-01")
    revogada = FrescorDoc(doc_id="lei-velha", valid_from="2015-01-01", valid_to="2023-12-31")
    corpus = [
        _chunk("lei-nova#art-1::1", "aliquota de quinze por cento sobre lucros", vigente),
        _chunk("lei-velha#art-1::1", "aliquota de quinze por cento sobre lucros", revogada),
    ]
    # como caso de 2026: só a vigente aparece
    r = buscar_no_corpus("aliquota quinze por cento lucros", as_of="2026-08-13", corpus=corpus)
    ids = [c.chunk_id for c in r]
    assert "lei-nova#art-1::1" in ids
    assert "lei-velha#art-1::1" not in ids
    # com incluir_historico, a revogada volta (marcada)
    r2 = buscar_no_corpus("aliquota quinze por cento lucros", as_of="2026-08-13",
                          incluir_historico=True, corpus=corpus)
    assert len(r2) == 2


def test_busca_vazia_quando_corpus_vazio():
    assert buscar_no_corpus("qualquer coisa", corpus=[]) == []


def test_busca_sem_termo_em_comum():
    f = FrescorDoc(doc_id="d", valid_from="2020-01-01")
    corpus = [_chunk("d#1::1", "texto sobre sucessao e legitima", f)]
    assert buscar_no_corpus("bitcoin ethereum blockchain", as_of="2026-01-01", corpus=corpus) == []
