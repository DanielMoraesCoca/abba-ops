"""Configuracao por cliente — o "esqueleto pronto, a gente faz os ajustes".

Esta e a peca que torna a biblioteca um produto em vez de um reconciliador. A crew,
o flow e o nucleo sao os mesmos para toda empresa; o que muda e um YAML.

**Nenhum segredo aqui.** Certificado digital e credencial da Plataforma RTC vivem em
gerenciador de segredos e chegam por variavel de ambiente. O `.gitignore` bloqueia
`*.p12`/`*.pem`/`*.key` e a CI reprova se algum for rastreado.
"""

from __future__ import annotations

from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field, ValidationError, field_validator

from abba_crews.core.modelos import dinheiro

DIR_PADRAO = Path(__file__).resolve().parents[1] / "config" / "clientes"


class Regime(str, Enum):  # noqa: UP042
    REGULAR = "regular"
    SIMPLES = "simples"


class Aprovacao(BaseModel):
    """Quem assina o dossie. Sem nome, nao ha gate humano — so automacao."""

    model_config = {"frozen": True}

    responsavel_nome: str = Field(min_length=3)
    responsavel_email: str
    papel: str = Field(default="contador")

    @field_validator("responsavel_email")
    @classmethod
    def _parece_email(cls, v: str) -> str:
        if "@" not in v or "." not in v.split("@")[-1]:
            raise ValueError(f"e-mail invalido: {v!r}")
        return v.strip().lower()


class ConfigCliente(BaseModel):
    """Tudo o que muda de uma empresa para outra."""

    model_config = {"frozen": True}

    cnpj: str
    razao_social: str = Field(min_length=2)
    regime: Regime = Regime.REGULAR
    entrega_dere: bool = Field(
        default=False,
        description="Decide a data de disponibilizacao: dia 20 com DeRE, dia 15 sem.",
    )
    engagement_id: str | None = Field(
        default=None, description="Liga ao cerebro do assessment-brain. Opcional ate o M5."
    )
    tolerancia_brl: Decimal = Field(
        default=Decimal("0.00"),
        description="Diferenca ignorada por arredondamento. Tolerancia alta esconde "
        "divergencia real — o padrao e zero e quem quiser folga assume.",
    )
    aprovacao: Aprovacao
    produtos_ativos: tuple[str, ...] = ("sentinela",)

    @field_validator("cnpj")
    @classmethod
    def _cnpj(cls, v: str) -> str:
        limpo = "".join(c for c in str(v) if c.isdigit())
        if len(limpo) != 14:
            raise ValueError(f"CNPJ deve ter 14 digitos, veio {len(limpo)}: {v!r}")
        return limpo

    @field_validator("tolerancia_brl", mode="before")
    @classmethod
    def _tolerancia(cls, v: Any) -> Decimal:
        d = dinheiro(v)
        if d < 0:
            raise ValueError("tolerancia nao pode ser negativa")
        return d


def carregar(caminho: Path) -> ConfigCliente:
    """Le e valida um YAML de cliente. Falha alto, dizendo qual campo e por que."""
    try:
        bruto = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise FileNotFoundError(f"configuracao de cliente nao encontrada: {caminho}") from None
    except yaml.YAMLError as e:
        raise ValueError(f"{caminho.name}: YAML invalido — {e}") from e

    if not isinstance(bruto, dict):
        raise ValueError(f"{caminho.name}: esperava um mapa de campos no topo do arquivo")

    try:
        config = ConfigCliente(**bruto)
    except ValidationError as e:
        problemas = "; ".join(
            f"{'.'.join(str(p) for p in err['loc'])}: {err['msg']}" for err in e.errors()
        )
        raise ValueError(f"{caminho.name}: configuracao invalida — {problemas}") from e

    esperado = caminho.stem
    if esperado.isdigit() and esperado != config.cnpj:
        raise ValueError(
            f"{caminho.name}: o nome do arquivo diz CNPJ {esperado} e o conteudo diz "
            f"{config.cnpj}. Um dos dois esta errado, e conferir a apuracao do CNPJ "
            f"errado e o pior erro possivel deste produto."
        )
    return config


def carregar_por_cnpj(cnpj: str, diretorio: Path | None = None) -> ConfigCliente:
    """Busca `<cnpj>.yaml` no diretorio de configuracoes."""
    limpo = "".join(c for c in cnpj if c.isdigit())
    base = diretorio or DIR_PADRAO
    caminho = base / f"{limpo}.yaml"
    if not caminho.exists():
        disponiveis = sorted(p.stem for p in base.glob("*.yaml")) if base.is_dir() else []
        raise FileNotFoundError(
            f"sem configuracao para o CNPJ {limpo} em {base}. "
            f"Disponiveis: {', '.join(disponiveis) or 'nenhuma'}"
        )
    return carregar(caminho)
