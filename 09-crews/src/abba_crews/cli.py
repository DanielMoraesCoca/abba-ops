"""CLI de operacao do abba-crews.

Separada da entrada `kickoff` que a CrewAI espera (`main.py`): esta e a
ferramenta dos socios; aquela e o que o AMP executa.
"""

from __future__ import annotations

import typer

from abba_crews.core.calendario import JanelaManifestacao
from abba_crews.core.produtos import Maturidade, listar, vendaveis
from abba_crews.core.sinteticos import Familia, golden_set, rodar

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




@app.command("golden")
def golden(
    detalhe: bool = typer.Option(False, "--detalhe", "-d", help="Lista caso a caso."),
) -> None:
    """Roda o golden set da Sentinela e imprime o placar.

    A metrica que manda e a precisao nos negativos: falso positivo fiscal manda o
    cliente pleitear o que nao e dele.
    """
    casos = golden_set()
    placar = rodar(casos)

    if detalhe:
        typer.echo("")
        for c in casos:
            marca = {Familia.POSITIVO: "+", Familia.NEGATIVO: "-", Familia.LIMPO: "o"}[c.familia]
            typer.echo(f"  [{marca}] {c.id}")
            typer.echo(f"      {c.descricao}")

    typer.echo(f"\n  casos              {len(casos)}")
    typer.echo(f"  recall             {placar.recall:.0%}  "
               f"({placar.positivos_achados}/{placar.positivos} com divergencia)")
    typer.echo(f"  precisao negativos {placar.precisao_nos_negativos:.0%}  "
               f"({placar.negativos_sem_falso_positivo}/{placar.negativos_e_limpos} limpos) "
               f"<- a metrica que manda")

    if placar.falhas:
        typer.echo("\n  FALHAS:")
        for f in placar.falhas:
            typer.echo(f"    {f}")
        raise typer.Exit(code=1)

    typer.echo("\n  golden set v0 aprovado.")
    typer.echo("  Nao promove a Sentinela a PRODUCAO: isso exige golden set montado")
    typer.echo("  com um contador, sobre competencias reais anonimizadas.\n")


@app.command("janela")
def janela(
    competencia: str = typer.Option(..., "--competencia", "-c", help="AAAA-MM"),
    dere: bool = typer.Option(False, "--dere", help="Empresa entrega DeRE."),
    hoje: str = typer.Option("", "--hoje", help="Data de referencia (AAAA-MM-DD)."),
) -> None:
    """Mostra a janela de manifestacao de uma competencia.

    O dia 15 (ou 20, com DeRE) e a DISPONIBILIZACAO da proposta. O prazo de
    manifestacao vai ate o ultimo dia util do mes seguinte.
    """
    from datetime import date as _date

    ref = _date.fromisoformat(hoje) if hoje else _date.today()
    j = JanelaManifestacao.para(competencia, entrega_dere=dere)
    typer.echo("")
    typer.echo(f"  competencia        {j.competencia}{'  (DeRE)' if dere else ''}")
    typer.echo(f"  disponibilizacao   {j.disponibilizacao.strftime('%d/%m/%Y')}")
    typer.echo(f"  prazo final        {j.prazo_final.strftime('%d/%m/%Y')}")
    typer.echo(f"  situacao em {ref.strftime('%d/%m/%Y')}  {j.situacao(ref).value}")
    typer.echo(f"  dias uteis restantes  {j.dias_uteis_restantes(ref)}")
    typer.echo("")
    typer.echo(f"  {j.resumo(ref)}")
    typer.echo("")


@app.command("sentinela")
def sentinela(
    cnpj: str = typer.Option(..., "--cnpj"),
    competencia: str = typer.Option(..., "--competencia", "-c", help="AAAA-MM"),
    hoje: str = typer.Option("", "--hoje", help="Data de referencia (AAAA-MM-DD)."),
    mock: bool = typer.Option(False, "--mock", help="Usa fonte sintetica."),
    caso: str = typer.Option("positivo-credito-omitido", "--caso", help="Caso do golden set."),
) -> None:
    """Roda a Sentinela e imprime o dossie.

    Sem `--mock` a coleta real ainda nao existe: ela chega no M6 e depende da
    credencial do piloto RTC-CBS.
    """
    from datetime import date as _date

    from abba_crews.flows.sentinela_flow import Fonte, SentinelaFlow

    fonte = None
    if mock:
        casos = {c.id: c for c in golden_set()}
        if caso not in casos:
            typer.echo(f"caso desconhecido: {caso}\nValidos: {', '.join(sorted(casos))}")
            raise typer.Exit(code=1)
        c = casos[caso]
        fonte = Fonte(documentos=c.documentos, apuracao=c.apuracao, origem=f"golden:{caso}")

    payload: dict[str, object] = {"cnpj": cnpj, "competencia": competencia}
    if hoje:
        payload["hoje"] = hoje

    flow = SentinelaFlow(fonte=fonte)
    flow.kickoff({"crewai_trigger_payload": payload})

    if not flow.state.markdown:
        typer.echo("o fluxo terminou sem produzir dossie")
        raise typer.Exit(code=1)
    typer.echo("")
    typer.echo(flow.state.markdown)
    typer.echo(f"<!-- chave de execucao: {flow.state.chave_execucao} -->")
    _ = _date


if __name__ == "__main__":
    app()
