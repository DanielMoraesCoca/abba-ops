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

**Mostra tambem o que ficou de fora.** A secao "Descartados e por que" lista o credito
que a empresa tem documentado e que a classificacao de creditabilidade nao deixou
entrar, com o dispositivo citado. Um documento que so mostra o que entra pede fe; um
que mostra o que ficou de fora, e sob qual regra, pode ser conferido.

O rodape declara a fronteira: a ABBA evidencia; concluir, decidir e transmitir e do
cliente. Nenhuma linha deste modulo produz linguagem de parecer.
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field

from abba_crews.core.calendario import JanelaManifestacao
from abba_crews.core.clientes import ConfigCliente
from abba_crews.core.reconciliacao import (
    Divergencia,
    ItemDescartado,
    ResultadoReconciliacao,
    Sentido,
)

ZERO = Decimal("0.00")

SUBTITULO = "Conferencia da apuracao assistida"
MARCA_RODAPE_RASCUNHO = "Este documento esta em **RASCUNHO**"
"""O paragrafo que a via assinada substitui.

Definido aqui, e nao repetido em `aprovacao.py`, para que mudar o rodape quebre um
teste em vez de quebrar em silencio a montagem da via assinada.
"""


class EstadoDossie(str, Enum):  # noqa: UP042
    """Estado do documento. Anda para a frente e so para a frente.

    Ate o M4a `APROVADO` era **enum morto**: existia na declaracao e nada o produzia.
    O rodape de todo dossie prometia uma assinatura que o sistema nao sabia receber.
    """

    RASCUNHO = "RASCUNHO"
    """Nasce assim e so sai daqui por aprovacao nomeada."""

    APROVADO = "APROVADO"
    """Congelado, com nome e horario de quem assinou. Terminal."""

    DEVOLVIDO = "DEVOLVIDO"
    """O humano recusou, com motivo. Tambem terminal: nao se reabre um documento —
    conferencia nova gera dossie novo, ao lado, sem apagar este."""

    @property
    def terminal(self) -> bool:
        return self is not EstadoDossie.RASCUNHO


class Assinatura(BaseModel):
    """Quem assinou, quando, e sobre quais bytes.

    O `sha256` e o que da valor probatorio ao documento: sem ele, "aprovado por Maria"
    e uma afirmacao sobre um texto que ninguem sabe qual era.
    """

    model_config = {"frozen": True}

    por: str = Field(min_length=1)
    em: datetime
    sha256: str = Field(min_length=64, max_length=64)


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
    def total_descartado(self) -> Decimal:
        """O que a classificacao tirou do dossie — mostrado, nunca omitido."""
        return self.resultado.total_descartado

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
    # `permite_manifestar` em vez de `is ENCERRADA`: a pergunta aqui e "da para
    # manifestar?", nao "qual e o rotulo da situacao". Se um estado novo entrar em
    # `Situacao`, esta linha continua certa sozinha.
    if not janela.situacao(hoje).permite_manifestar:
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


def _secao_descartados(descartados: tuple[ItemDescartado, ...], total: Decimal) -> list[str]:
    """O que a empresa tem documentado e nao vai pleitear, com a regra que o barrou."""
    if not descartados:
        return []
    linhas = [
        f"### Descartados e por que — {_brl(total)}",
        "",
        "Creditos documentados pela empresa que a conferencia de creditabilidade **nao** "
        "levou ao pleito. Estao aqui para serem conferidos, nao para serem esquecidos: "
        "discordando da regra citada, o profissional que assina decide diferente.",
        "",
    ]
    for d in descartados:
        linhas.append(f"- **{_brl(d.valor_brl)}** · CST {d.cst} / cClassTrib {d.c_class_trib}")
        linhas.append(f"  - documento `{d.chave}`, item {d.item}")
        linhas.append(f"  - {d.razao}")
        linhas.append(f"  - fonte: {d.fonte}")
    linhas.append("")
    return linhas


def _secao_tolerancia(r: ResultadoReconciliacao) -> list[str]:
    """A folga aplicada, e o que ela engoliu. So aparece quando ha folga.

    Um dossie que diz "nada a manifestar" depois de uma tolerancia ter apagado
    divergencia real esta pedindo uma assinatura sob informacao incompleta. Se houve
    folga, ela e declarada — mesmo que nada tenha sido suprimido, porque saber que a
    conferencia rodou com folga muda como o contador le o resto.
    """
    if r.tolerancia_brl <= ZERO:
        return []
    linhas = [
        f"### Tolerancia aplicada — {_brl(r.tolerancia_brl)} por item",
        "",
        f"Esta conferencia ignorou diferencas de ate {_brl(r.tolerancia_brl)} por item, "
        f"conforme a configuracao deste cliente.",
        "",
    ]
    if r.suprimidos_por_tolerancia:
        linhas += [
            f"**{r.suprimidos_por_tolerancia} item(ns) divergiam e nao foram reportados**, "
            f"somando {_brl(r.valor_suprimido_brl)}. Se essa folga nao reflete o que foi "
            f"combinado, a conferencia precisa rodar de novo com a tolerancia certa "
            f"antes de este documento ser assinado.",
            "",
        ]
    else:
        linhas += ["Nenhuma divergencia caiu dentro dessa folga nesta competencia.", ""]
    return linhas


def renderizar(dossie: Dossie) -> str:
    """O dossie em Markdown, para leitura humana. Sempre o rascunho.

    A **via assinada nao se renderiza daqui** — ela e derivada dos bytes que o humano
    conferiu (`core/aprovacao.via_assinada`). Re-renderizar do modelo abriria a fresta
    exata que o sha256 existe para fechar: o assinado poderia divergir do conferido.
    """
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
        f"# {d.estado.value} — {SUBTITULO}",
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
        L += ["## Nada a manifestar", ""]
        if d.resultado.descartados:
            # Sem esta ressalva o texto mentiria: a proposta NAO conferiu com os
            # documentos — houve credito ausente dela, e ele nao foi pleiteado por
            # decisao de creditabilidade. Dizer "nenhuma divergencia" aqui esconderia
            # justamente a decisao que o contador precisa conferir.
            barrados = len(d.resultado.descartados)
            restante = d.resultado.itens_conferidos - barrados
            frase = (
                f"Nada a pleitear nesta competencia. Dos "
                f"{d.resultado.itens_conferidos} item(ns) conferido(s), {barrados} "
                f"nao entrou no pleito por creditabilidade — {_brl(d.total_descartado)} "
                f"listado(s) abaixo, com a regra que os barrou."
            )
            # So afirmar sobre o restante quando ele existe: "o restante confere" com
            # zero itens restantes e frase vazia com cara de conclusao.
            if restante > 0:
                frase += f" Os outros {restante} item(ns) conferem com a proposta do Fisco."
            L += [frase, ""]
        else:
            L += [
                f"A proposta do Fisco confere com os {d.resultado.itens_conferidos} "
                f"item(ns) documentado(s) na competencia. Nenhuma divergencia encontrada.",
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

    # Fora do if: quando TUDO foi descartado nao ha divergencia, a natureza vira
    # "nada a fazer" — e e justamente ai que omitir os descartes seria pior.
    L += _secao_descartados(d.resultado.descartados, d.total_descartado)
    L += _secao_tolerancia(d.resultado)

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
        f"{MARCA_RODAPE_RASCUNHO} e nao vale como manifestacao "
        f"enquanto nao for conferido e assinado por {d.responsavel}.",
        "",
    ]
    return "\n".join(L)


def bloco_de_assinatura(a: Assinatura) -> list[str]:
    """A via assinada — e a frase que impede que ela seja lida como envio.

    Sem esta secao, "APROVADO" no cabecalho pode ser lido como "transmitido ao Fisco".
    Num produto fiscal essa confusao custa caro: o contribuinte acharia que a
    manifestacao foi feita, perderia a janela, e o silencio consolidaria a proposta.
    """
    return [
        "## Conferido e assinado",
        "",
        f"- **{a.por}**",
        f"- em {a.em.strftime('%d/%m/%Y as %H:%M')} (UTC)",
        f"- sobre o rascunho `sha256:{a.sha256}`",
        "",
        "> **Aprovar nao e transmitir.** Esta assinatura registra que o profissional "
        "conferiu o conteudo acima e o assume. **A manifestacao ao Fisco continua "
        "sendo ato do contribuinte**, feita no sistema do proprio Fisco, dentro da "
        "janela. A ABBA nao transmite — nao existe ferramenta de transmissao neste "
        "produto.",
        "",
        "O hash acima identifica exatamente os bytes conferidos. Qualquer versao deste "
        "documento que nao produza esse hash **nao e a que foi assinada**.",
        "",
    ]
