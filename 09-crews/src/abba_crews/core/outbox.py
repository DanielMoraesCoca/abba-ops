"""O outbox do ledger — como este projeto fala com o cerebro sem escrever nele.

O sistema de registro da ABBA e o cerebro do `assessment-brain`: bitemporal, com
supersessao que nunca deleta, autoridade de origem e cobertura pelo `abba forget`. Duas
memorias concorrentes significam duas verdades, e a que ficasse fora do cerebro nao
seria auditavel nem apagavel pelo caminho sancionado.

Este modulo **nao escreve no cerebro**. Ele registra *intencoes* em disco; o lado Node
(`abba crews sync`) as le e aplica pelas funcoes sancionadas — `assertFact`,
`addDecision`, `advanceDecision`. A razao de nao escrever direto e simples: as regras que
protegem a verdade (autoridade de origem, supersessao, o gate do `human_stated`) moram
naquelas funcoes. Reimplementa-las em Python seria manter duas copias de uma logica cuja
divergencia ninguem perceberia ate ser tarde.

## Origem: `tool_output`, nunca `human_stated`

Todo fato que sai daqui carrega `origin='tool_output'` — autoridade 2, mesma de
`client_doc`, abaixo de `human_stated` (3). Ou seja: **nada que este projeto afirme
sobrepoe o que uma pessoa afirmou.** A unica via de `human_stated` continua sendo
`abba brain fact ... --by "Nome"`, na mao.

A assinatura do contador nao e excecao a isso. Ela nao vira fato `human_stated`; vira
uma **decisao** com `decided_by` — que e onde o cerebro guarda ato humano nomeado.

## Cifrado, como o resto

A intencao carrega CNPJ, competencia e valores. Mesmo envelope ABBA-ENC-1 dos dossies,
mesma senha. **E aqui que a interoperabilidade do M4a paga**: o lado Node le com o
`readPossiblyEncrypted` que ja existe la, sem formato novo e sem segunda senha.

## Idempotencia

Cada intencao tem `id` estavel, derivado do que ela afirma. Aplicar duas vezes tem de
ser inofensivo: o `sync` marca a aplicacao num arquivo ao lado e pula o que ja foi. Nada
e apagado — intencao aplicada vira registro do que foi para o cerebro e quando.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from decimal import Decimal
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field

from abba_crews.core.arquivo import MODO_DIR, Arquivo, agora
from abba_crews.core.cofre import cifrar, decifrar, senha_do_ambiente, senha_obrigatoria

ORIGEM_DESTE_PROJETO = "tool_output"
"""Autoridade 2 no cerebro. Nunca sobrepoe `human_stated`. Nao mudar sem V-record."""


class TipoIntencao(str, Enum):  # noqa: UP042
    """O que se quer registrar no cerebro. Fechado de proposito."""

    FATO_COMPETENCIA_CONFERIDA = "fato.competencia_conferida"
    """Uma competencia foi conferida, com o que foi achado. Vira `assertFact`."""

    DECISAO_MANIFESTACAO = "decisao.manifestacao"
    """Um humano nomeado assinou o dossie. Vira `addDecision` + `advanceDecision`."""


class Intencao(BaseModel):
    """Uma escrita pedida ao cerebro, ainda nao aplicada.

    Deliberadamente **nao** e a chamada da API do cerebro: e o que se quer dizer. Como
    isso vira `assertFact` ou `addDecision` e decisao do lado que conhece o cerebro.
    """

    model_config = {"frozen": True}

    id: str = Field(min_length=16, max_length=16)
    tipo: TipoIntencao
    engagement_id: str = Field(min_length=1)
    cnpj: str
    competencia: str
    criada_em: datetime
    dados: dict[str, str] = Field(
        description="Carga em texto. Valores monetarios ja formatados — o cerebro nao "
        "faz aritmetica fiscal, so guarda o que foi conferido."
    )

    def resumo(self) -> str:
        return f"{self.tipo.value:<32} {self.cnpj} {self.competencia}  ({self.id})"


def _identidade(tipo: TipoIntencao, engagement_id: str, cnpj: str, competencia: str,
                marca: str) -> str:
    """Id estavel: mesma afirmacao, mesmo id. E o que torna o `sync` idempotente."""
    crua = f"{tipo.value}|{engagement_id}|{cnpj}|{competencia}|{marca}"
    return hashlib.sha256(crua.encode("utf-8")).hexdigest()[:16]


def _brl(v: Decimal) -> str:
    return f"{v:.2f}"


class Outbox:
    """As intencoes em disco, ao lado dos dossies e sob a mesma senha."""

    def __init__(self, arquivo: Arquivo) -> None:
        self.raiz = arquivo.raiz / "outbox"

    # ------------------------------------------------------------------ caminhos
    def _carga(self, id_: str) -> Path:
        return self.raiz / f"{id_}.json.enc"

    def _marca(self, id_: str) -> Path:
        """Sidecar em claro dizendo se e quando foi aplicada. Sem dado de cliente."""
        return self.raiz / f"{id_}.aplicada.json"

    # ------------------------------------------------------------------ escrita
    def registrar(self, intencao: Intencao) -> Intencao:
        """Grava a intencao. Repetir a mesma afirmacao nao cria uma segunda."""
        senha = senha_obrigatoria()
        self.raiz.mkdir(parents=True, exist_ok=True, mode=MODO_DIR)
        destino = self._carga(intencao.id)
        if destino.exists():
            return intencao
        Arquivo._escrever(
            destino,
            cifrar(json.dumps(intencao.model_dump(mode="json"), ensure_ascii=False), senha),
        )
        return intencao

    def marcar_aplicada(self, id_: str, *, por: str) -> None:
        """Chamado pelo lado que aplicou. Nao apaga a carga — registra o que foi."""
        Arquivo._escrever(
            self._marca(id_),
            json.dumps({"aplicada_em": agora().isoformat(), "por": por}, ensure_ascii=False)
            + "\n",
        )

    # ------------------------------------------------------------------ leitura
    def aplicada(self, id_: str) -> bool:
        return self._marca(id_).exists()

    def listar(self, *, pendentes: bool = False) -> tuple[Intencao, ...]:
        if not self.raiz.exists():
            return ()
        senha = senha_do_ambiente() or ""
        achadas = []
        for carga in sorted(self.raiz.glob("*.json.enc")):
            id_ = carga.name.removesuffix(".json.enc")
            if pendentes and self.aplicada(id_):
                continue
            achadas.append(
                Intencao.model_validate_json(decifrar(carga.read_text(encoding="utf-8"), senha))
            )
        return tuple(sorted(achadas, key=lambda i: i.criada_em))


# --------------------------------------------------------------------------- #
# Os construtores — o unico lugar que sabe traduzir o produto em intencao
# --------------------------------------------------------------------------- #


def da_conferencia(
    *, engagement_id: str, cnpj: str, competencia: str, impressao: str,
    favoravel: Decimal, desfavoravel: Decimal, descartado: Decimal, itens: int,
) -> Intencao:
    """O que a conferencia de uma competencia achou. Vira fato `tool_output`.

    A `impressao` entra na identidade: conferencias diferentes da mesma competencia
    (dias diferentes, documentos novos) sao afirmacoes diferentes, e o cerebro resolve
    a supersessao pela sua propria regra bitemporal — nao cabe a nos decidir aqui.
    """
    return Intencao(
        id=_identidade(
            TipoIntencao.FATO_COMPETENCIA_CONFERIDA, engagement_id, cnpj, competencia, impressao
        ),
        tipo=TipoIntencao.FATO_COMPETENCIA_CONFERIDA,
        engagement_id=engagement_id,
        cnpj=cnpj,
        competencia=competencia,
        criada_em=agora(),
        dados={
            "subject": f"cnpj:{cnpj}",
            "predicate": f"apuracao_conferida:{competencia}",
            "object": (
                f"favoravel={_brl(favoravel)}; desfavoravel={_brl(desfavoravel)}; "
                f"descartado={_brl(descartado)}; itens={itens}"
            ),
            "origin": ORIGEM_DESTE_PROJETO,
            "impressao": impressao,
        },
    )


def da_assinatura(
    *, engagement_id: str, cnpj: str, competencia: str, impressao: str,
    por: str, sha256: str, efeito_liquido: Decimal,
) -> Intencao:
    """O contador assinou. Vira **decisao** com `decided_by`, nao fato `human_stated`.

    A distincao importa: `human_stated` e a autoridade maxima do cerebro e a sua unica
    porta e uma pessoa digitando `abba brain fact --by "Nome"`. Uma assinatura relatada
    por um programa nao pode entrar por ali — mas e exatamente o que o cerebro chama de
    decisao tomada por humano nomeado, e e la que ela pertence.
    """
    return Intencao(
        id=_identidade(
            TipoIntencao.DECISAO_MANIFESTACAO, engagement_id, cnpj, competencia, impressao
        ),
        tipo=TipoIntencao.DECISAO_MANIFESTACAO,
        engagement_id=engagement_id,
        cnpj=cnpj,
        competencia=competencia,
        criada_em=agora(),
        dados={
            "title": f"Manifestacao da apuracao {competencia} — CNPJ {cnpj}",
            "description": (
                f"Dossie conferido e assinado por {por}. Efeito liquido apurado: "
                f"R$ {_brl(efeito_liquido)}. Documento identificado por sha256:{sha256}. "
                f"Assinar nao e transmitir: a manifestacao ao Fisco e ato do contribuinte."
            ),
            "decided_by": por,
            "sha256": sha256,
            "impressao": impressao,
        },
    )
