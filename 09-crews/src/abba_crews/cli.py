"""CLI de operacao do abba-crews.

Separada da entrada `kickoff` que a CrewAI espera (`main.py`): esta e a
ferramenta dos socios; aquela e o que o AMP executa.
"""

from __future__ import annotations

import typer

from abba_crews.core.produtos import Maturidade, listar, vendaveis

app = typer.Typer(
    help="Camada de Caixa da reforma tributaria — operacao.",
    no_args_is_help=True,
    add_completion=False,
)

_ROTULO: dict[Maturidade, str] = {
    Maturidade.PRODUCAO: "PRODUCAO    ",
    Maturidade.EXECUTAVEL: "executavel  ",
    Maturidade.ESPECIFICADO: "especificado",
    Maturidade.ESTACIONADO: "ESTACIONADO ",
}


@app.callback()
def principal() -> None:
    """Sem este callback o Typer colapsa um app de comando unico e `produtos`
    deixaria de ser subcomando. Ele existe para a CLI crescer sem quebrar."""


@app.command("produtos")
def produtos(
    detalhe: bool = typer.Option(
        False, "--detalhe", "-d", help="Mostra metrica, gate e ressalvas."
    ),
) -> None:
    """Lista os produtos da Camada de Caixa e o estado real de cada um.

    Esta tabela e a defesa contra vender como pronto o que nao esta.
    """
    itens = listar()
    typer.echo(f"\n{len(itens)} produtos na Camada de Caixa\n")

    for p in itens:
        vaz = f"vaz.{p.vazamento}" if p.vazamento is not None else "novo "
        typer.echo(f"  [{_ROTULO[p.maturidade]}] {vaz}  {p.nome}")
        if detalhe:
            typer.echo(f"       {p.resumo}")
            typer.echo(f"       metrica: {p.metrica}")
            typer.echo(f"       gate:    {p.gate}")
            if p.base_legal:
                typer.echo(f"       base:    {p.base_legal}")
            if p.observacao:
                typer.echo(f"       nota:    {p.observacao}")
            typer.echo("")

    prontos = vendaveis()
    typer.echo("")
    if prontos:
        nomes = ", ".join(p.nome for p in prontos)
        typer.echo(f"Vendavel hoje: {nomes}")
    else:
        typer.echo(
            "Vendavel hoje: NENHUM. Nenhum produto atingiu PRODUCAO — e o estado real.\n"
            "Nao prometer a cliente o que esta em 'especificado' ou 'executavel'."
        )
    typer.echo("")


if __name__ == "__main__":
    app()
