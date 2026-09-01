"""Creditabilidade: o item da nota da direito a credito, ou nao?

Ate o M2 o produto achava divergencia **estrutural** — o que falta na proposta do
Fisco, o que diverge em valor. Nada disso responde a pergunta que o contador faz
primeiro: *este credito e legitimo?* `cst` e `c_class_trib` viviam no modelo,
validados como nao-vazios, e nenhuma linha de codigo os lia. Este modulo os le.

## Por regra, sem modelo

A classificacao aqui e **deterministica e auditavel**: uma tabela versionada, com
fonte citada por linha, e nada mais. Modelo de linguagem so entra no residuo — no
que a tabela nao resolve — e isso e o M3b. A ordem importa: regra primeiro, modelo
depois, nunca o contrario. Cada linha que o contador acrescenta a tabela tira um
item da rota cara.

## A regra de seguranca que desenha o modulo

**Codigo desconhecido e `DUVIDOSO`. Nunca creditavel, nunca vedado.**

Presumir creditabilidade de um par que nao conhecemos e exatamente o falso positivo
fiscal que manda o cliente pleitear o que nao e dele — o erro que o golden set
persegue desde o v0. Presumir vedacao e o espelho: some com credito legitimo sem
ninguem ver. As duas presuncoes sao mentira com aparencia de precisao; a duvida
declarada e verdade.

Corolario pratico: **com a tabela vazia, tudo vira `DUVIDOSO`**. Nao e defeito, e o
estado real do nosso conhecimento — e e por isso que `abba-crews cobertura` existe,
para medir esse estado em vez de escondê-lo.

## O que este modulo nao faz

Nao emite parecer. Uma linha de tabela nao e uma opiniao tributaria: e a citacao de
um dispositivo, para que o profissional que assina possa conferir a citacao. Ver
`docs/PENDENCIAS.md`, P2 — a tabela oficial e o Informe Tecnico 2025.002 (RFB), e
ela se preenche **com um contador**, nunca de dentro do codigo.
"""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import Protocol

from pydantic import BaseModel, Field, field_validator, model_validator

CURINGA = "*"
"""`c_class_trib: "*"` vale para qualquer cClassTrib sob aquele CST.

Regra exata sempre vence a curinga — do contrario uma generalizacao ampla
apagaria uma excecao conferida item a item.
"""

TABELA_PADRAO = Path(__file__).parent / "dados" / "vedacoes.json"


class Veredito(str, Enum):  # noqa: UP042
    """O que a tabela diz sobre o direito a credito de um item."""

    CREDITAVEL = "creditavel"
    """A tabela reconhece o direito a credito. Segue para o dossie."""

    VEDADO = "vedado"
    """A tabela nega o direito a credito. Vira descarte com o dispositivo citado."""

    DUVIDOSO = "duvidoso"
    """A tabela nao resolve. **Unica porta para julgamento por modelo (M3b).**"""


class Regra(BaseModel):
    """Uma linha da tabela: um par (CST, cClassTrib) e o que se sabe sobre ele."""

    model_config = {"frozen": True}

    cst: str
    c_class_trib: str = Field(description=f'cClassTrib exato, ou "{CURINGA}" para todo o CST')
    veredito: Veredito
    razao: str = Field(min_length=1, description="Em linguagem de contador, nao de programador")
    doc: str = Field(min_length=1, description="A fonte. Linha sem fonte nao entra na tabela.")
    a_confirmar: bool = Field(
        default=False,
        description=(
            "Levantado, ainda nao conferido na fonte primaria. Rebaixa o veredito a "
            "DUVIDOSO em execucao — a linha fica registrada, mas nao decide nada."
        ),
    )

    @field_validator("cst", "c_class_trib")
    @classmethod
    def _limpo(cls, v: str) -> str:
        limpo = v.strip()
        if not limpo:
            raise ValueError("cst e c_class_trib nao podem ser vazios")
        return limpo

    @model_validator(mode="after")
    def _duvidoso_nao_e_regra(self) -> Regra:
        if self.veredito is Veredito.DUVIDOSO:
            raise ValueError(
                "regra com veredito DUVIDOSO nao faz sentido: a duvida e o que sobra "
                "quando a tabela nao resolve. Para registrar uma linha ainda nao "
                "conferida, declare o veredito real e marque a_confirmar=true."
            )
        return self

    @property
    def curinga(self) -> bool:
        return self.c_class_trib == CURINGA

    @property
    def decide(self) -> bool:
        """Uma linha `a_confirmar` esta na tabela mas nao decide nada."""
        return not self.a_confirmar


class Classificacao(BaseModel):
    """O que se concluiu sobre um item — sempre com a razao e a fonte junto.

    Nao existe classificacao sem razao: o contador que assina precisa poder
    conferir a citacao, e um veredito sem dispositivo e opiniao disfarcada de fato.
    """

    model_config = {"frozen": True}

    veredito: Veredito
    razao: str
    fonte: str

    @property
    def requer_julgamento(self) -> bool:
        return self.veredito is Veredito.DUVIDOSO


class Classificador(Protocol):
    """O que `reconciliar()` precisa saber sobre quem classifica.

    Protocolo, e nao classe base, para que o teste possa injetar um classificador de
    tres linhas sem carregar tabela nenhuma.
    """

    def classificar(self, cst: str, c_class_trib: str) -> Classificacao: ...


class TabelaCreditabilidade(BaseModel):
    """A tabela versionada de creditabilidade. Implementa `Classificador`."""

    model_config = {"frozen": True}

    versao: str
    fonte: str
    nota: str = Field(
        default="",
        description="Por que a tabela esta no estado em que esta. Lido por `abba-crews cobertura`.",
    )
    regras: tuple[Regra, ...] = ()

    @model_validator(mode="after")
    def _sem_par_repetido(self) -> TabelaCreditabilidade:
        vistos: set[tuple[str, str]] = set()
        for r in self.regras:
            par = (r.cst, r.c_class_trib)
            if par in vistos:
                raise ValueError(
                    f"par repetido na tabela: CST {r.cst}, cClassTrib {r.c_class_trib}. "
                    f"Tabela contraditoria e pior que tabela vazia — a vazia declara "
                    f"duvida, a contraditoria decide por ordem de arquivo."
                )
            vistos.add(par)
        return self

    def classificar(self, cst: str, c_class_trib: str) -> Classificacao:
        """Classifica um par. Desconhecido -> DUVIDOSO, sempre."""
        cst, c_class_trib = cst.strip(), c_class_trib.strip()

        exata = next(
            (r for r in self.regras if r.cst == cst and r.c_class_trib == c_class_trib), None
        )
        curinga = next((r for r in self.regras if r.cst == cst and r.curinga), None)
        regra = exata or curinga

        if regra is None:
            return Classificacao(
                veredito=Veredito.DUVIDOSO,
                razao=(
                    f"par (CST {cst}, cClassTrib {c_class_trib}) ausente da tabela "
                    f"{self.versao}. Nao se presume creditabilidade de codigo "
                    f"desconhecido: vai a conferencia humana."
                ),
                fonte=self.fonte,
            )

        if not regra.decide:
            return Classificacao(
                veredito=Veredito.DUVIDOSO,
                razao=(
                    f"a tabela registra '{regra.veredito.value}' para este par, mas a "
                    f"linha esta marcada a_confirmar — levantada e ainda nao conferida "
                    f"na fonte primaria. Vale como indicio, nao como decisao. "
                    f"Motivo registrado: {regra.razao}"
                ),
                fonte=regra.doc,
            )

        return Classificacao(veredito=regra.veredito, razao=regra.razao, fonte=regra.doc)

    @property
    def ativas(self) -> tuple[Regra, ...]:
        """Linhas que decidem. As `a_confirmar` ficam de fora."""
        return tuple(r for r in self.regras if r.decide)

    @property
    def pendentes(self) -> tuple[Regra, ...]:
        return tuple(r for r in self.regras if not r.decide)


def carregar(caminho: Path | None = None) -> TabelaCreditabilidade:
    """Le a tabela do disco. Arquivo malformado falha alto — nunca degrada em silencio."""
    alvo = caminho or TABELA_PADRAO
    try:
        bruto = json.loads(alvo.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise FileNotFoundError(
            f"tabela de creditabilidade ausente em {alvo}. Ela e versionada junto do "
            f"codigo; se sumiu, algo quebrou no empacotamento."
        ) from None
    except json.JSONDecodeError as e:
        raise ValueError(f"tabela de creditabilidade malformada em {alvo}: {e}") from e
    return TabelaCreditabilidade.model_validate(bruto)
