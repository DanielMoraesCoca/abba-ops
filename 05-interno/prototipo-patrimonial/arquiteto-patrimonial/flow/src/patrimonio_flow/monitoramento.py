"""Monitoramento de corpus vivo — o motor de retenção (o "fosso").

Uma minuta única é uma transação; o monitoramento é uma assinatura. Quando uma
norma do corpus é revogada, superada ou vence o frescor, este módulo (a) lista o
que precisa de revisão e (b) aponta quais CASOS PASSADOS citaram aquela norma —
o gancho de reengajamento que os comparáveis (Estateably, FP Alpha) usam para
reter o profissional. Tudo determinístico, zero LLM.

Nada dispara sozinho: estas funções alimentam um alerta que um humano lê — a
mesma disciplina da camada de antecipação do cérebro (TTL/aritmética, não
'previsão').
"""

from __future__ import annotations

from typing import Iterable, Optional

from patrimonio_flow.tools.rag_corpus import FrescorDoc, carregar_fichas


def docs_para_revisar(
    corpus_dir: Optional[str] = None,
    hoje_iso: Optional[str] = None,
    fichas: Optional[dict] = None,
) -> list[dict]:
    """Documentos do corpus que pedem atenção de um advogado, com o motivo:
    - 'revogado'      → superseded_by preenchido ou valid_to no passado
    - 'frescor_vencido' → last_verified + ttl_dias < hoje (ou sem last_verified)
    `fichas` pode ser injetado (testes); senão carrega do manifest."""
    docs = fichas if fichas is not None else carregar_fichas(corpus_dir)
    pendentes: list[dict] = []
    for doc_id, f in docs.items():
        motivos: list[str] = []
        if f.superseded_by:
            motivos.append(f"revogado por {f.superseded_by}")
        elif not f.vigente_em(hoje_iso):
            motivos.append("fora de vigência (valid_to no passado)")
        if f.desatualizado(hoje_iso):
            motivos.append(f"frescor vencido (ttl {f.ttl_dias}d desde {f.last_verified or 'nunca verificado'})")
        if motivos:
            pendentes.append({"doc_id": doc_id, "motivos": motivos})
    return sorted(pendentes, key=lambda d: d["doc_id"])


def _doc_id_do_chunk(chunk_id: str) -> str:
    """'lei-14754#art-10::1' -> 'lei-14754'."""
    return chunk_id.split("#", 1)[0].split("::", 1)[0]


def casos_afetados_por(doc_ids: Iterable[str], casos: Iterable[dict]) -> list[dict]:
    """Dado um conjunto de doc_ids que mudaram (ex.: recém-revogados) e uma lista
    de casos {caso_id, chunks} (os chunk_ids que aquele caso citou), retorna os
    casos que dependem desses docs — 'estas minutas podem ter sido afetadas pela
    norma X; revisar'. É o loop de reengajamento de alto valor."""
    alvo = set(doc_ids)
    afetados: list[dict] = []
    for caso in casos:
        docs_citados = {_doc_id_do_chunk(c) for c in caso.get("chunks", [])}
        tocados = sorted(docs_citados & alvo)
        if tocados:
            afetados.append({"caso_id": caso.get("caso_id", ""), "docs_afetados": tocados})
    return afetados
