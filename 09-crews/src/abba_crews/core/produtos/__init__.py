"""Registro dos produtos da Camada de Caixa e suas maturidades."""

from abba_crews.core.produtos.registry import (
    PRODUTOS,
    Maturidade,
    Produto,
    listar,
    por_id,
    vendaveis,
)

__all__ = ["PRODUTOS", "Maturidade", "Produto", "listar", "por_id", "vendaveis"]
