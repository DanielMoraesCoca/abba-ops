"""Tool de RAG sobre o corpus jurídico (corpus-conhecimento.md).

DECISÃO DE ARQUITETURA: RAG é tool explícita (não Knowledge nativo do CrewAI)
porque o guardrail anti-citação-órfã exige proveniência estruturada — cada chunk
volta com chunk_id (ex.: "lei-14754#art-10::c2") e o Flow registra o conjunto
recuperado no estado (EstadoCaso.chunks_recuperados).

CORPUS VIVO + BITEMPORAL: cada documento carrega vigência (valid_from/valid_to/
superseded_by) e frescor (last_verified/ttl_dias). A recuperação filtra por
`as_of` (a data do caso) — lei revogada só aparece com incluir_historico=True.
É a mesma disciplina bitemporal do cérebro (uma-verdade-ativa).

MULTI-TENANT: o corpus jurídico é COMPARTILHADO (só-leitura, versionado). Os
documentos do CLIENTE são por-tenant e NÃO vivem aqui — vivem no estado do Flow,
segregados e apagáveis (jamais no corpus). O `tenant_id` é propagado para o dia
em que o vector store real separar namespaces (corpus compartilhado × docs do
cliente); ver produtizacao.md §3.

BUSCA: v0 é um índice determinístico por arquivo (sobreposição de termos, sem
embeddings) sobre um corpus curado por advogado. O corpus real é ingerido pelo
advogado nomeado (briefing-corpus-hector.md); enquanto vazio, a busca devolve
nada e o desenho se abstém (citação-ou-abstenção). Sprint futuro: busca híbrida
(denso + BM25) com embedder explícito.
"""

from __future__ import annotations

import json
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Callable, Optional

from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Diretório default do corpus curado (relativo ao pacote flow/). Sobrescrevível
# por env CORPUS_DIR no deploy. Vazio até o advogado curar (briefing-corpus-hector.md).
_CORPUS_DIR_DEFAULT = Path(__file__).resolve().parents[3] / "corpus"


def _parse_iso(s: Optional[str]) -> Optional[date]:
    if not s:
        return None
    try:
        return date.fromisoformat(s[:10])
    except ValueError:
        return None


class FrescorDoc(BaseModel):
    """Metadados de CORPUS VIVO + BITEMPORAL — o RAG precisa saber quão fresco e
    quão vigente é cada documento. Um RAG jurídico que não detecta obsolescência
    responde com lei revogada."""
    doc_id: str
    versao: str = "1"                      # timeline de versões
    is_current: bool = True                # exatamente UMA versão é 'current' em produção
    # --- vigência (bitemporal) ---
    valid_from: Optional[str] = None       # ISO — quando a norma passou a vigorar
    valid_to: Optional[str] = None         # ISO — quando deixou de vigorar (None = vigente)
    supersedes: Optional[str] = None       # doc_id anterior que ESTE revoga/atualiza
    superseded_by: Optional[str] = None    # doc_id que revoga/substitui ESTE
    # --- frescor (curadoria) ---
    last_verified: Optional[str] = None    # ISO — quando um humano confirmou a vigência
    ttl_dias: int = 90                     # regulatório ~30; estável ~180. Vencido → alerta
    embedding_model: Optional[str] = None  # trocar de modelo exige re-index — rastrear
    fonte_url: Optional[str] = None

    def desatualizado(self, hoje_iso: Optional[str] = None) -> bool:
        """True se o frescor venceu: sem last_verified → sempre stale; senão
        last_verified + ttl_dias < hoje. Aritmética de data real, determinística
        (o `hoje` vem por parâmetro nos testes; None → relógio)."""
        lv = _parse_iso(self.last_verified)
        if lv is None:
            return True
        hoje = _parse_iso(hoje_iso) or date.today()
        return (lv + timedelta(days=self.ttl_dias)) < hoje

    def vigente_em(self, as_of_iso: Optional[str] = None) -> bool:
        """True se a norma está vigente na data do caso (as_of). superseded_by
        preenchido ou valid_to no passado → não vigente."""
        if self.superseded_by:
            return False
        as_of = _parse_iso(as_of_iso) or date.today()
        vf, vt = _parse_iso(self.valid_from), _parse_iso(self.valid_to)
        if vf and as_of < vf:
            return False
        if vt and as_of > vt:
            return False
        return True


class ChunkRecuperado(BaseModel):
    chunk_id: str      # "<doc_id>#<artigo>::<n>"
    doc_id: str
    artigo: Optional[str] = None
    texto: str
    score: float
    tipo: str          # lei | regulamento | consulta | oficial | jurisprudencia | doutrina | ficha_jurisdicao
    frescor: Optional[FrescorDoc] = None   # corpus vivo: cada chunk carrega o frescor do seu doc


# ---------------------------------------------------------------- índice por arquivo

def _tokens(texto: str) -> list[str]:
    return [t for t in re.split(r"[^0-9a-zà-ú]+", texto.lower()) if len(t) > 2]


def carregar_corpus(corpus_dir: Optional[str] = None) -> list[ChunkRecuperado]:
    """Lê o corpus curado do disco: manifest.json (fichas FrescorDoc por doc) +
    chunks/<doc_id>.jsonl (uma linha por chunk: {chunk_id, artigo, texto, tipo}).
    Corpus vazio → lista vazia → o sistema se abstém. Sem cache global de
    propósito: o corpus é pequeno e o determinismo dos testes vem primeiro."""
    base = Path(corpus_dir) if corpus_dir else _CORPUS_DIR_DEFAULT
    manifest = base / "manifest.json"
    if not manifest.exists():
        return []
    dados = json.loads(manifest.read_text(encoding="utf-8"))
    fichas: dict[str, FrescorDoc] = {}
    for d in dados.get("docs", []):
        f = FrescorDoc(**d)
        fichas[f.doc_id] = f
    chunks: list[ChunkRecuperado] = []
    chunks_dir = base / "chunks"
    for doc_id, ficha in fichas.items():
        arq = chunks_dir / f"{doc_id}.jsonl"
        if not arq.exists():
            continue
        for linha in arq.read_text(encoding="utf-8").splitlines():
            linha = linha.strip()
            if not linha:
                continue
            c = json.loads(linha)
            chunks.append(ChunkRecuperado(
                chunk_id=c["chunk_id"], doc_id=doc_id, artigo=c.get("artigo"),
                texto=c["texto"], score=0.0,
                tipo=c.get("tipo", "lei"), frescor=ficha))
    return chunks


def buscar_no_corpus(
    query: str,
    *,
    filtro_tipo: str = "",
    top_k: int = 5,
    as_of: Optional[str] = None,
    incluir_historico: bool = False,
    corpus_dir: Optional[str] = None,
    corpus: Optional[list[ChunkRecuperado]] = None,
) -> list[ChunkRecuperado]:
    """Busca determinística por sobreposição de termos, com filtro bitemporal.
    `corpus` pode ser injetado (testes); senão carrega do disco. Chunk cujo doc
    não está vigente em `as_of` só entra se incluir_historico=True."""
    itens = corpus if corpus is not None else carregar_corpus(corpus_dir)
    q = set(_tokens(query))
    if not q:
        return []
    tipos = {t.strip() for t in filtro_tipo.split(",") if t.strip()}
    ranked: list[ChunkRecuperado] = []
    for c in itens:
        if tipos and c.tipo not in tipos:
            continue
        if not incluir_historico and c.frescor is not None and not c.frescor.vigente_em(as_of):
            continue
        toks = _tokens(c.texto)
        if not toks:
            continue
        presentes = q.intersection(toks)
        if not presentes:
            continue
        # score = cobertura de termos da query + densidade (determinístico)
        cobertura = len(presentes) / len(q)
        densidade = sum(toks.count(t) for t in presentes) / len(toks)
        c.score = round(cobertura + 0.1 * densidade, 4)
        ranked.append(c)
    # ordenação estável: score desc, depois chunk_id asc (determinismo)
    ranked.sort(key=lambda c: (-c.score, c.chunk_id))
    return ranked[:top_k]


class RagCorpusTool(BaseTool):
    name: str = "consulta_corpus_juridico"
    description: str = (
        "Busca no corpus jurídico versionado da ABBA (leis, INs, consultas, fichas de jurisdição). "
        "Retorna chunks com chunk_id — cite APENAS chunk_ids retornados por esta tool. "
        "Se nada relevante voltar, declare nao_coberto=true na claim."
    )
    # callback para o Flow registrar os chunks entregues (alimenta o guardrail)
    on_retrieve: Optional[Callable[[list[str]], None]] = Field(default=None, exclude=True)
    # texto dos chunks entregues nesta execução (chunk_id -> texto): alimenta o
    # guardrail de sustentação a nível de trecho. Referência viva por caso.
    textos_entregues: dict = Field(default_factory=dict, exclude=True)
    # contexto do caso — setado por caso em main.py, NÃO manipulável pelo agente:
    as_of: Optional[str] = None            # data do caso (filtro bitemporal)
    tenant_id: str = ""                    # namespace do tenant (corpus compartilhado × docs cliente)
    corpus_dir: Optional[str] = None       # override do diretório do corpus
    incluir_historico: bool = False        # normas revogadas só sob demanda explícita

    def _run(self, query: str, filtro_tipo: str = "", top_k: int = 5) -> str:
        chunks = self._buscar(query, filtro_tipo, top_k)
        for c in chunks:
            self.textos_entregues[c.chunk_id] = c.texto
        if self.on_retrieve is not None:
            self.on_retrieve([c.chunk_id for c in chunks])
        if not chunks:
            return "NENHUM_RESULTADO — declare nao_coberto=true e descreva a lacuna."
        return "\n\n".join(
            f"[{c.chunk_id}] ({c.tipo}, score={c.score:.2f})\n{c.texto}" for c in chunks
        )

    def _buscar(self, query: str, filtro_tipo: str, top_k: int) -> list[ChunkRecuperado]:
        return buscar_no_corpus(
            query, filtro_tipo=filtro_tipo, top_k=top_k,
            as_of=self.as_of, incluir_historico=self.incluir_historico,
            corpus_dir=self.corpus_dir)
