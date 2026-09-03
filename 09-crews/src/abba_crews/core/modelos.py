"""Modelos do dominio fiscal. Puro Pydantic — nenhuma dependencia de framework.

Duas decisoes que atravessam o arquivo inteiro:

**Dinheiro e `Decimal`, nunca `float`.** `0.1 + 0.2 != 0.3` em ponto flutuante, e num
reconciliador fiscal isso vira divergencia fantasma ou, pior, divergencia real que
some no arredondamento. Todo valor monetario entra por `dinheiro()`, que quantiza
em 2 casas com ROUND_HALF_UP (a regra do fisco brasileiro).

**Campo ausente nao vira zero.** Um `vCBS` que nao veio no XML e diferente de um
`vCBS` que veio zerado: o primeiro e falha de leitura, o segundo e fato. Zero
silencioso num campo de credito e credito perdido sem ninguem perceber.

Estrutura do grupo IBS/CBS conforme a NT 2025.002 (grupo UB):

    gIBSCBS
      vBC      -> vbc
      gIBSUF   -> vIBSUF  (v_ibs_uf)
      gIBSMun  -> vIBSMun (v_ibs_mun)
      gCBS     -> vCBS    (v_cbs)

**So os valores, nao as aliquotas.** `pIBSUF`, `pIBSMun` e `pCBS` existem no XML e
**nao** estao no modelo: a conferencia compara valor contra valor, e guardar aliquota
sem usar seria mais superficie declarada sem dono. Entram quando algo precisar delas.

Item carrega `CST` (CST-IBS/CBS) e `cClassTrib` — o par que amarra o item a um
dispositivo especifico da LC 214/2025.

> **Pendencia de validacao (gate do M6):** os nomes de campo acima vieram de fontes
> secundarias. Antes de tocar em XML real, conferir contra o XSD oficial no Portal
> Nacional da NF-e. Ver `docs/PENDENCIAS.md`.
"""

from __future__ import annotations

from datetime import date
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator

from abba_crews.core.cnpj import exigir

CENTAVO = Decimal("0.01")


def dinheiro(valor: Any) -> Decimal:
    """Converte para Decimal quantizado em centavos, com ROUND_HALF_UP.

    Aceita str, int, Decimal. **Rejeita float** — se um float chegou aqui, alguem
    fez aritmetica de dinheiro em ponto flutuante antes, e o erro ja aconteceu.
    """
    if isinstance(valor, float):
        raise TypeError(
            f"valor monetario recebido como float ({valor!r}). Use str ou Decimal: "
            "ponto flutuante perde centavos e o erro so aparece na conferencia."
        )
    try:
        d = Decimal(valor)
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError(f"valor monetario invalido: {valor!r}") from e

    # `Decimal("nan")` nao levanta: devolve NaN, e `NaN.quantize(...)` devolve NaN.
    # A defesa real vinha de fora — o Pydantic recusa nao-finito no campo, e comparacao
    # de ordem com NaN levanta InvalidOperation. Ou seja: o guarda declarado do dinheiro
    # se apoiava em terceiros sem saber, e quem chamasse `dinheiro()` fora de um modelo
    # levava uma excecao crua em vez da ValueError que esta docstring promete.
    if not d.is_finite():
        raise ValueError(
            f"valor monetario nao finito: {valor!r}. NaN e infinito nao sao dinheiro — "
            f"comparados com qualquer limiar eles nao dao nem verdadeiro nem falso, e "
            f"uma divergencia fiscal desapareceria sem ninguem ver."
        )
    return d.quantize(CENTAVO, rounding=ROUND_HALF_UP)


class Papel(str, Enum):  # noqa: UP042
    """De que lado a empresa esta na operacao."""

    ENTRADA = "entrada"
    """A empresa e a adquirente — e daqui que vem credito."""

    SAIDA = "saida"
    """A empresa e a emitente — e daqui que vem debito."""


class ItemDocumento(BaseModel):
    """Um item de documento fiscal, na parte que interessa a IBS/CBS."""

    model_config = {"frozen": True}

    numero: int = Field(ge=1, description="nItem")
    descricao: str = ""

    cst: str = Field(description="CST-IBS/CBS")
    c_class_trib: str = Field(description="cClassTrib — amarra o item a LC 214/2025")

    vbc: Decimal = Field(description="Base de calculo do grupo gIBSCBS")
    v_ibs_uf: Decimal = Field(description="vIBSUF")
    v_ibs_mun: Decimal = Field(description="vIBSMun")
    v_cbs: Decimal = Field(description="vCBS")

    @field_validator("vbc", "v_ibs_uf", "v_ibs_mun", "v_cbs", mode="before")
    @classmethod
    def _quantiza(cls, v: Any) -> Decimal:
        return dinheiro(v)

    @field_validator("cst", "c_class_trib")
    @classmethod
    def _nao_vazio(cls, v: str, info: Any) -> str:
        if not v or not v.strip():
            raise ValueError(f"{info.field_name} vazio — sem ele nao da para classificar o item")
        return v.strip()

    @property
    def v_ibs(self) -> Decimal:
        """vIBS = vIBSUF + vIBSMun. Invariante que a propria SEFAZ valida (rejeicao 1085)."""
        return self.v_ibs_uf + self.v_ibs_mun

    @property
    def tributo_total(self) -> Decimal:
        return self.v_ibs + self.v_cbs


class DocumentoFiscal(BaseModel):
    """Um documento fiscal eletronico, do ponto de vista de uma empresa."""

    model_config = {"frozen": True}

    chave: str = Field(min_length=44, max_length=44)
    papel: Papel
    emitente_cnpj: str
    destinatario_cnpj: str
    data_emissao: date
    itens: tuple[ItemDocumento, ...]

    @field_validator("chave")
    @classmethod
    def _chave_numerica(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("chave de acesso tem de ter 44 digitos numericos")
        return v

    @field_validator("emitente_cnpj", "destinatario_cnpj")
    @classmethod
    def _cnpj_valido(cls, v: str, info: Any) -> str:
        return exigir(v, campo=info.field_name)

    @model_validator(mode="after")
    def _tem_item(self) -> DocumentoFiscal:
        if not self.itens:
            raise ValueError(f"documento {self.chave} sem itens")
        numeros = [i.numero for i in self.itens]
        if len(numeros) != len(set(numeros)):
            raise ValueError(f"documento {self.chave} tem nItem repetido")
        return self

    @property
    def competencia(self) -> str:
        """AAAA-MM da emissao. E por ela que o documento entra numa apuracao."""
        return f"{self.data_emissao.year:04d}-{self.data_emissao.month:02d}"

    @property
    def total_ibs(self) -> Decimal:
        """Reservado para o Diagnostico de Impacto de Caixa (produto `diagnostico`).

        Sem chamador hoje. Fica declarado porque a projecao de caixa por tributo e o
        proximo uso previsto, e removida se ela nao vier — a regra da casa desde o
        review de 2026-09-02 e que nada fica declarado sem dono.
        """
        return sum((i.v_ibs for i in self.itens), Decimal("0.00"))

    @property
    def total_cbs(self) -> Decimal:
        """Reservado para o Diagnostico de Impacto de Caixa. Ver `total_ibs`."""
        return sum((i.v_cbs for i in self.itens), Decimal("0.00"))


class LinhaApuracao(BaseModel):
    """Uma linha da apuracao pre-preenchida que o Fisco propoe.

    O Fisco monta a proposta a partir dos documentos eletronicos que ele recebeu.
    A conferencia consiste em achar onde essa proposta diverge dos documentos que a
    empresa tem — e, sobretudo, o que ela **nao** trouxe.
    """

    model_config = {"frozen": True}

    chave: str = Field(min_length=44, max_length=44)
    item: int = Field(ge=1)
    papel: Papel
    v_ibs: Decimal
    v_cbs: Decimal

    @field_validator("v_ibs", "v_cbs", mode="before")
    @classmethod
    def _quantiza(cls, v: Any) -> Decimal:
        return dinheiro(v)

    @property
    def chave_item(self) -> tuple[str, int]:
        return (self.chave, self.item)

    @property
    def tributo_total(self) -> Decimal:
        return self.v_ibs + self.v_cbs


class ApuracaoFisco(BaseModel):
    """A apuracao assistida pre-preenchida, para um CNPJ e uma competencia.

    Silencio do contribuinte ate o prazo = aceite: os valores propostos prevalecem
    e o credito tributario e constituido automaticamente. Dai a Sentinela existir.
    """

    model_config = {"frozen": True}

    cnpj: str
    competencia: str = Field(pattern=r"^\d{4}-\d{2}$")
    linhas: tuple[LinhaApuracao, ...]

    @field_validator("cnpj")
    @classmethod
    def _cnpj_valido(cls, v: str) -> str:
        return exigir(v, campo="cnpj")

    @property
    def total_debito(self) -> Decimal:
        """Usada por `saldo`. Ver a nota la sobre por que a cadeia existe."""
        return sum(
            (linha.tributo_total for linha in self.linhas if linha.papel is Papel.SAIDA),
            Decimal("0.00"),
        )

    @property
    def total_credito(self) -> Decimal:
        return sum(
            (linha.tributo_total for linha in self.linhas if linha.papel is Papel.ENTRADA),
            Decimal("0.00"),
        )

    @property
    def saldo(self) -> Decimal:
        """Positivo = a pagar. Negativo = credito acumulado.

        Reservado para o Diagnostico: o efeito de caixa da competencia e esta conta.
        Sem chamador hoje — declarado com dono, nao por inercia.
        """
        return self.total_debito - self.total_credito

    def por_chave_item(self) -> dict[tuple[str, int], LinhaApuracao]:
        return {linha.chave_item: linha for linha in self.linhas}
