"""O dossie de manifestacao — a unica saida que uma pessoa le.

Tres regras que vem da doutrina da casa e nao se negociam:

**Nasce RASCUNHO.** Espelha o brief do Conselheiro (`abba brain brief`), que so deixa
de ser rascunho com aprovacao nomeada. Enquanto nao houver assinatura humana, o
cabecalho diz isso em letra grande.

**Abre com o R$ e com o prazo.** O contador tem dezenas de CNPJs e uma janela curta.
Se a primeira linha nao disser quanto esta em jogo e quantos dias faltam, o documento
perdeu a sua funcao.

**Mostra os dois lados.** Favoravel e desfavoravel em secoes separadas e somadas.
Conferir a apuracao e calar sobre o que pesa contra o cliente e divulgacao seletiva —
e um dossie assim nao e assinavel por um profissional.

O rodape declara a fronteira: a ABBA evidencia; concluir, decidir e transmitir e do
cliente. Nenhuma linha deste modulo produz linguagem de parecer.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field

from abba_crews.core.calendario import JanelaManifestacao, Situacao
from abba_crews.core.clientes import ConfigCliente
from abba_crews.core.reconciliacao import Divergencia, ResultadoReconciliacao, Sentido

ZERO = Decimal("0.00")


class EstadoDossie(str, Enum):  # noqa: UP042
    RASCUNHO = "RASCUNHO"
    """Nasce assim e so sai daqui por aprovacao nomeada (M4)."""

    APROVADO = "APROVADO"
    """Congelado, com nome e horario de quem assinou."""


class Natureza(str, Enum):  # noqa: UP042
    MANIFESTACAO = "manifestacao"
    """Ha janela aberta: o dossie serve para agir."""

    NADA_A_FAZER = "nada_a_fazer"
    """A proposta do Fisco bate com os documentos."""

    REGISTRO_DE_PERDA = "registro_de_perda"
    """O prazo passou. Nao se manifesta fora da janela — registra-se o que se perdeu."""


class Dossie(BaseModel):
    """O que a Sentinela entrega ao humano que assina."""

    model_config = {"frozen": True}

    cnpj: str
    razao_social: str
    competencia: str
    gerado_em: date
    estado: EstadoDossie = EstadoDossie.RASCUNHO
    natureza: Natureza
    janela: JanelaManifestacao
    resultado: ResultadoReconciliacao
    responsavel: str = Field(description="Quem deve assinar. Sem nome nao ha gate humano.")

    @property
    def total_favoravel(self) -> Decimal:
        return self.resultado.total_favoravel

    @property
    def total_desfavoravel(self) -> Decimal:
        return self.resultado.total_desfavoravel

    @property
    def efeito_liquido(self) -> Decimal:
        """Positivo = a manifestacao tende a favorecer o contribuinte."""
        return self.total_favoravel - self.total_desfavoravel


def montar(
    *,
    config: ConfigCliente,
    janela: JanelaManifestacao,
    resultado: ResultadoReconciliacao,
    hoje: date,
) -> Dossie:
    """Monta o dossie. Deterministico: mesmas entradas, mesmo documento."""
    situacao = janela.situacao(hoje)
    if situacao is Situacao.ENCERRADA:
        natureza = Natureza.REGISTRO_DE_PERDA
    elif resultado.conforme:
        natureza = Natureza.NADA_A_FAZER
    else:
        natureza = Natureza.MANIFESTACAO

    return Dossie(
        cnpj=config.cnpj,
        razao_social=config.razao_social,
        competencia=resultado.competencia,
        gerado_em=hoje,
        natureza=natureza,
        janela=janela,
        resultado=resultado,
        responsavel=config.aprovacao.responsavel_nome,
    )


def _brl(v: Decimal) -> str:
    inteiro, _, centavos = f"{v:.2f}".partition(".")
    negativo = inteiro.startswith("-")
    digitos = inteiro.lstrip("-")
    grupos: list[str] = []
    while len(digitos) > 3:
        grupos.insert(0, digitos[-3:])
        digitos = digitos[:-3]
    grupos.insert(0, digitos)
    return f"{'-' if negativo else ''}R$ {'.'.join(grupos)},{centavos}"


def _secao(
    titulo: str, divergencias: tuple[Divergencia, ...], total: Decimal
) -> list[str]:
    if not divergencias:
        return []
    linhas = [f"### {titulo} — {_brl(total)}", ""]
    for d in divergencias:
        linhas.append(f"- **{_brl(d.valor_brl)}** · {d.tipo.value.replace('_', ' ')}")
        linhas.append(f"  - documento `{d.chave}`, item {d.item}")
        linhas.append(f"  - {d.detalhe}")
    linhas.append("")
    return linhas


def renderizar(dossie: Dossie) -> str:
    """O dossie em Markdown, para leitura humana."""
    d = dossie
    hoje = d.gerado_em
    favoraveis = tuple(x for x in d.resultado.divergencias if x.sentido is Sentido.FAVORAVEL)
    desfavoraveis = tuple(
        x for x in d.resultado.divergencias if x.sentido is Sentido.DESFAVORAVEL
    )
    indeterminadas = tuple(
        x for x in d.resultado.divergencias
        if x.sentido not in (Sentido.FAVORAVEL, Sentido.DESFAVORAVEL)
    )

    L: list[str] = [
        f"# {d.estado.value} — Conferencia da apuracao assistida",
        "",
        f"**{d.razao_social}** · CNPJ {d.cnpj} · competencia **{d.competencia}**",
        f"Gerado em {hoje.strftime('%d/%m/%Y')}. Para conferencia e assinatura de "
        f"**{d.responsavel}**.",
        "",
        "---",
        "",
        f"> {d.janela.resumo(hoje)}",
        "",
    ]

    if d.natureza is Natureza.NADA_A_FAZER:
        L += [
            "## Nada a manifestar",
            "",
            f"A proposta do Fisco confere com os {d.resultado.itens_conferidos} item(ns) "
            f"documentado(s) na competencia. Nenhuma divergencia encontrada.",
            "",
        ]
    else:
        if d.natureza is Natureza.REGISTRO_DE_PERDA:
            L += [
                "## Registro de perda — fora do prazo",
                "",
                "O prazo de manifestacao ja passou. Este documento **nao** e uma "
                "manifestacao: registra o que a conferencia encontrou depois da janela, "
                "para que a competencia seguinte nao repita o mesmo padrao.",
                "",
            ]
        else:
            L += [
                "## O que esta em jogo",
                "",
                f"- A favor do contribuinte: **{_brl(d.total_favoravel)}**",
                f"- Contra o contribuinte: **{_brl(d.total_desfavoravel)}**",
                f"- Efeito liquido da manifestacao: **{_brl(d.efeito_liquido)}**",
                "",
                f"{len(d.resultado.divergencias)} divergencia(s) em "
                f"{d.resultado.itens_conferidos} item(ns) conferido(s).",
                "",
            ]

        L += _secao("A favor do contribuinte", favoraveis, d.total_favoravel)
        L += _secao("Contra o contribuinte", desfavoraveis, d.total_desfavoravel)
        if indeterminadas:
            L += _secao(
                "Sentido indeterminado — exigem conferencia antes de qualquer decisao",
                indeterminadas,
                sum((x.valor_brl for x in indeterminadas), ZERO),
            )

    L += [
        "---",
        "",
        "## Por que este documento existe",
        "",
        "Nao havendo manifestacao no prazo, a apuracao proposta pelo Fisco e presumida "
        "correta e o credito tributario e constituido automaticamente — o que equivale "
        "a confissao de divida (art. 348, §1o da LC 214/2025; §4o do art. 125 do ADCT).",
        "",
        "## O que a ABBA faz e o que nao faz",
        "",
        "A ABBA confere, evidencia e organiza. **Nao emite parecer tributario, nao "
        "decide e nao transmite nada ao Fisco.** Cada item acima aponta o documento "
        "que o sustenta; a conclusao, a decisao e a manifestacao sao do contribuinte "
        "e do profissional que o assessora.",
        "",
        f"Este documento esta em **{d.estado.value}** e nao vale como manifestacao "
        f"enquanto nao for conferido e assinado por {d.responsavel}.",
        "",
    ]
    return "\n".join(L)
