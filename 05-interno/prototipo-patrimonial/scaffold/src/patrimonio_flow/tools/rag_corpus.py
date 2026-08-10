"""Tool de RAG sobre o corpus jurídico (corpus-conhecimento.md).

DECISÃO DE ARQUITETURA: RAG é tool explícita (não Knowledge nativo do CrewAI)
porque o guardrail anti-citação-órfã exige proveniência estruturada — cada chunk
volta com chunk_id (ex.: "lei-14754#art-10::c2") e o Flow registra o conjunto
recuperado no estado (EstadoCaso.chunks_recuperados).

STUB: a busca real (embedder explícito + vector store em CREWAI_STORAGE_DIR)
é implementação do Sprint 1. O contrato abaixo é o que importa.
"""

from __future__ import annotations

from typing import Callable, Optional

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class ChunkRecuperado(BaseModel):
    chunk_id: str      # "<doc_id>#<artigo>::<n>"
    doc_id: str
    artigo: Optional[str] = None
    texto: str
    score: float
    tipo: str          # lei | regulamento | consulta | oficial | jurisprudencia | doutrina | ficha_jurisdicao


class RagCorpusTool(BaseTool):
    name: str = "consulta_corpus_juridico"
    description: str = (
        "Busca no corpus jurídico versionado da ABBA (leis, INs, consultas, fichas de jurisdição). "
        "Retorna chunks com chunk_id — cite APENAS chunk_ids retornados por esta tool. "
        "Se nada relevante voltar, declare nao_coberto=true na claim."
    )
    # callback para o Flow registrar os chunks entregues (alimenta o guardrail)
    on_retrieve: Optional[Callable[[list[str]], None]] = Field(default=None, exclude=True)

    def _run(self, query: str, filtro_tipo: str = "", top_k: int = 5) -> str:
        chunks = self._buscar(query, filtro_tipo, top_k)
        if self.on_retrieve is not None:
            self.on_retrieve([c.chunk_id for c in chunks])
        if not chunks:
            return "NENHUM_RESULTADO — declare nao_coberto=true e descreva a lacuna."
        return "\n\n".join(
            f"[{c.chunk_id}] ({c.tipo}, score={c.score:.2f})\n{c.texto}" for c in chunks
        )

    def _buscar(self, query: str, filtro_tipo: str, top_k: int) -> list[ChunkRecuperado]:
        # TODO(Sprint 1): busca híbrida (denso + BM25) sobre o corpus chunkeado
        # por artigo (leis) / 4000-200 (demais), embedder EXPLÍCITO na config.
        raise NotImplementedError("Implementar no Sprint 1 — ver corpus-conhecimento.md §6")
