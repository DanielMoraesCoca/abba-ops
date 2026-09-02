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


@app.command("cobertura")
def cobertura(
    tabela: str = typer.Option("", "--tabela", help="Caminho de outra tabela de vedacoes."),
) -> None:
    """Mede quanto da conferencia a REGRA resolve sozinha, sem julgamento por modelo.

    E a resposta direta a pergunta de custo do plano de negocio: que fracao dos itens
    cai na rota cara? Cada linha conferida que o contador acrescenta a tabela move
    este numero para cima. Com a tabela como nasce, ele e zero — e o zero e honesto.
    """
    from pathlib import Path

    from abba_crews.core.creditabilidade import carregar
    from abba_crews.core.reconciliacao import reconciliar

    t = carregar(Path(tabela) if tabela else None)

    typer.echo("")
    typer.echo(f"  tabela             {t.versao}")
    typer.echo(f"  fonte              {t.fonte}")
    typer.echo(f"  regras             {len(t.regras)}  "
               f"({len(t.ativas)} decidem, {len(t.pendentes)} a confirmar)")

    from decimal import Decimal

    conferidos = julgamento = descartados = 0
    brl_julgamento = Decimal("0.00")
    for caso in golden_set():
        r = reconciliar(caso.documentos, caso.apuracao, classificador=t)
        conferidos += r.itens_conferidos
        julgamento += r.itens_em_julgamento
        descartados += len(r.descartados)
        brl_julgamento += sum(
            (d.valor_brl for d in r.divergencias if d.requer_julgamento), Decimal("0.00")
        )

    pct = (conferidos - julgamento) / conferidos if conferidos else 1.0
    typer.echo("")
    typer.echo(f"  itens conferidos   {conferidos}   (corpus: golden set v0)")
    typer.echo(f"  em julgamento      {julgamento}   (R$ {brl_julgamento})")
    typer.echo(f"  descartados        {descartados}")
    typer.echo(f"  COBERTURA          {pct:.0%}  <- resolvido sem modelo")
    typer.echo("")
    typer.echo("  O denominador e TODO item conferido, nao so os que passam pela tabela:")
    typer.echo("  saida e item ja reconhecido pela proposta nunca precisam de")
    typer.echo("  creditabilidade. A cobertura mede custo — que fracao cai na rota cara.")
    typer.echo("")

    if t.pendentes:
        typer.echo(f"  {len(t.pendentes)} linha(s) marcada(s) a_confirmar NAO decidem nada:")
        for r_ in t.pendentes:
            typer.echo(f"    CST {r_.cst} / cClassTrib {r_.c_class_trib} -> {r_.doc}")
        typer.echo("")
    if t.nota:
        typer.echo(f"  {t.nota}")
        typer.echo("")


# --------------------------------------------------------------------------- #
# O gate humano
# --------------------------------------------------------------------------- #


def _abre_arquivo() -> Arquivo:  # type: ignore[name-defined] # noqa: F821
    """Abre o armazem, traduzindo as recusas em mensagem de terminal.

    As duas recusas sao deliberadas (ver core/arquivo.py): sem senha nao grava, e
    dentro de arvore git nao grava. Aqui elas viram texto que diz o que fazer.
    """
    from abba_crews.core.arquivo import Arquivo, RaizInsegura
    from abba_crews.core.cofre import SenhaAusente, senha_obrigatoria

    try:
        arquivo = Arquivo()
        # Confere a senha AQUI, nao la na hora de gravar. Mesma disciplina do
        # `abrir_competencia` do Flow: validar antes de qualquer custo. Descobrir a
        # falta de senha depois da conferencia rodada gastaria o trabalho e devolveria
        # um traceback em vez de uma instrucao.
        senha_obrigatoria()
        return arquivo
    except (RaizInsegura, SenhaAusente) as e:
        typer.echo(f"\n  {e}\n")
        raise typer.Exit(code=1) from e


@app.command("dossies")
def dossies(
    cnpj: str = typer.Option("", "--cnpj"),
    competencia: str = typer.Option("", "--competencia", "-c", help="AAAA-MM"),
    estado: str = typer.Option("", "--estado", help="RASCUNHO | APROVADO | DEVOLVIDO"),
) -> None:
    """Lista os dossies guardados e o estado real de cada um.

    Mostra tambem os devolvidos: esconder o que foi recusado seria perder o unico
    sinal que temos de onde a conferencia erra.
    """
    from abba_crews.core.dossie import EstadoDossie

    filtro = None
    if estado:
        try:
            filtro = EstadoDossie(estado.strip().upper())
        except ValueError:
            validos = ", ".join(e.value for e in EstadoDossie)
            typer.echo(f"estado desconhecido: {estado}. Validos: {validos}")
            raise typer.Exit(code=1) from None

    registros = _abre_arquivo().listar(
        cnpj=cnpj or None, competencia=competencia or None, estado=filtro
    )
    typer.echo("")
    if not registros:
        typer.echo("  nenhum dossie guardado.")
        typer.echo("  Rode `abba-crews sentinela ... --guardar` para produzir um.\n")
        return
    for r in registros:
        typer.echo(f"  {r.resumo()}")
    typer.echo(f"\n  {len(registros)} dossie(s).\n")


@app.command("ver")
def ver(
    chave: str = typer.Option(..., "--chave", help="Chave ou prefixo da impressao."),
    assinado: bool = typer.Option(False, "--assinado", help="Mostra a via assinada."),
) -> None:
    """Decifra e imprime um dossie guardado."""
    arquivo = _abre_arquivo()
    r = _localiza(arquivo, chave)
    typer.echo("")
    typer.echo(arquivo.markdown(r, assinado=assinado))


def _localiza(arquivo: Arquivo, chave: str):  # type: ignore[name-defined,no-untyped-def] # noqa: F821,E501
    from abba_crews.core.arquivo import DossieNaoEncontrado, ReferenciaAmbigua

    try:
        return arquivo.localizar(chave)
    except (DossieNaoEncontrado, ReferenciaAmbigua) as e:
        typer.echo(f"\n  {e}\n")
        raise typer.Exit(code=1) from e


@app.command("aprovar")
def aprovar(
    chave: str = typer.Option(..., "--chave", help="Chave ou prefixo da impressao."),
    por: str = typer.Option(..., "--por", help='Nome de quem assina. Ex: "Maria Contadora".'),
) -> None:
    """Assina um dossie — o gate humano, com nome.

    Confere que os bytes no disco sao os mesmos que foram indexados antes de assinar.
    Aprovar NAO transmite nada ao Fisco: a manifestacao continua sendo ato do
    contribuinte, no sistema do proprio Fisco.
    """
    from abba_crews.core.aprovacao import ConteudoDivergente, GateViolado
    from abba_crews.core.aprovacao import aprovar as _aprovar

    arquivo = _abre_arquivo()
    r = _localiza(arquivo, chave)
    try:
        assinado = _aprovar(arquivo, r.chave, por=por)
    except (GateViolado, ConteudoDivergente) as e:
        typer.echo(f"\n  RECUSADO: {e}\n")
        raise typer.Exit(code=1) from e

    typer.echo("")
    typer.echo(f"  ASSINADO  {assinado.chave}")
    typer.echo(f"  por       {assinado.aprovado_por}")
    typer.echo(f"  em        {assinado.aprovado_em:%d/%m/%Y %H:%M} UTC")
    typer.echo(f"  sobre     sha256:{assinado.sha256}")
    typer.echo("")
    typer.echo("  Assinar nao e transmitir. A manifestacao ao Fisco continua sendo ato")
    typer.echo("  do contribuinte, no sistema do Fisco, dentro da janela.")
    typer.echo("")


@app.command("devolver")
def devolver(
    chave: str = typer.Option(..., "--chave", help="Chave ou prefixo da impressao."),
    por: str = typer.Option(..., "--por", help="Nome de quem devolve."),
    motivo: str = typer.Option(..., "--motivo", help="O que esta errado. Obrigatorio."),
) -> None:
    """Recusa um dossie, com nome e motivo. O motivo e o que ensina a proxima competencia."""
    from abba_crews.core.aprovacao import GateViolado
    from abba_crews.core.aprovacao import devolver as _devolver

    arquivo = _abre_arquivo()
    r = _localiza(arquivo, chave)
    try:
        d = _devolver(arquivo, r.chave, por=por, motivo=motivo)
    except GateViolado as e:
        typer.echo(f"\n  RECUSADO: {e}\n")
        raise typer.Exit(code=1) from e
    typer.echo(f"\n  DEVOLVIDO {d.chave}\n  por {d.devolvido_por}: {d.motivo}\n")


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
    classificar: bool = typer.Option(
        False,
        "--classificar",
        help="Liga a conferencia de creditabilidade. Com --mock usa a tabela de ENSAIO.",
    ),
    guardar: bool = typer.Option(
        False, "--guardar", help="Grava o dossie cifrado, para aprovacao posterior."
    ),
) -> None:
    """Roda a Sentinela e imprime o dossie.

    Sem `--mock` a coleta real ainda nao existe: ela chega no M6 e depende da
    credencial do piloto RTC-CBS.

    `--classificar` liga a conferencia de creditabilidade. Ela vem desligada porque
    a tabela de vedacoes ainda nao tem linha conferida (P2): ligada sobre a tabela
    real, todo credito vai a julgamento — e a crew que julga so chega no M3b.
    """
    from datetime import date as _date

    from abba_crews.core.creditabilidade import Classificador, carregar
    from abba_crews.core.sinteticos import TABELA_ENSAIO
    from abba_crews.flows.sentinela_flow import Fonte, SentinelaFlow

    classificador: Classificador | None = None
    if classificar:
        classificador = TABELA_ENSAIO if mock else carregar()

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

    arquivo = _abre_arquivo() if guardar else None

    flow = SentinelaFlow(fonte=fonte, classificador=classificador, arquivo=arquivo)
    flow.kickoff({"crewai_trigger_payload": payload})

    if not flow.state.markdown:
        typer.echo("o fluxo terminou sem produzir dossie")
        raise typer.Exit(code=1)
    typer.echo("")
    typer.echo(flow.state.markdown)
    typer.echo(f"<!-- chave de execucao: {flow.state.chave_execucao} -->")

    if flow.state.registro is not None:
        r = flow.state.registro
        typer.echo("")
        typer.echo(f"  guardado  {r.chave}")
        typer.echo(f"  estado    {r.estado.value}  (aguardando {r.responsavel})")
        typer.echo(f"  assinar   abba-crews aprovar --chave {r.impressao} --por \"Nome\"")
        typer.echo("")
    _ = _date


if __name__ == "__main__":
    app()
