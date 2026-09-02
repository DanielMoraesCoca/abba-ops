"""O gate humano — o inegociavel 1, finalmente com mecanismo.

A doutrina da casa e centaura: **a IA rascunha, o humano assina.** Ate o M4a isso
existia no `abba-crews` apenas como frase no rodape do dossie — *"nao vale como
manifestacao enquanto nao for conferido e assinado por Nome do Contador"* — sem que
houvesse caminho algum pelo qual esse contador assinasse. `EstadoDossie.APROVADO` era
enum morto. Este modulo e o caminho.

## Para a frente, e so para a frente

Mesma forma do `decisions` e do `playbooks` do `assessment-brain` (`decided_by`,
`approved_by`, recusa de re-aprovacao):

    RASCUNHO --aprovar--> APROVADO    (terminal)
    RASCUNHO --devolver-> DEVOLVIDO   (terminal)

Nao ha volta e nao ha reabertura. Conferencia nova gera **dossie novo, ao lado**, com
a sua propria impressao — supersessao, nunca deleção. Um documento que pode voltar de
"assinado" para "rascunho" nao prova nada.

## A trava que da valor probatorio

`aprovar()` recalcula o sha256 do rascunho no disco e compara com o que o indice
registrou. Divergiu, **recusa**. Assinar sem conferir que os bytes sao os mesmos que
foram conferidos e assinar em branco — e num dossie fiscal, assinar em branco e assumir
numeros que ninguem leu.

## Nome de gente, sempre

`--por` e obrigatorio e nao aceita vazio. Um gate humano sem nome e automacao com nome
de gate: nao ha quem responda, e responder e o ponto inteiro.
"""

from __future__ import annotations

from decimal import Decimal

from abba_crews.core.arquivo import Arquivo, RegistroDossie, agora, sha256_de
from abba_crews.core.dossie import (
    MARCA_RODAPE_RASCUNHO,
    SUBTITULO,
    Assinatura,
    EstadoDossie,
    bloco_de_assinatura,
)

ZERO = Decimal("0.00")


class GateViolado(RuntimeError):
    """Uma transicao que a maquina de estados nao permite."""


class ConteudoDivergente(RuntimeError):
    """O rascunho no disco nao e mais o que foi indexado. Nao se assina isso."""


def _nome_de_gente(por: str) -> str:
    limpo = (por or "").strip()
    if len(limpo) < 3:
        raise GateViolado(
            "aprovacao exige o nome de quem assina (--por \"Nome Sobrenome\"). "
            "Gate humano sem nome e automacao com nome de gate: nao ha quem responda."
        )
    return limpo


def _exige_rascunho(r: RegistroDossie, acao: str) -> None:
    if r.estado is EstadoDossie.RASCUNHO:
        return
    if r.estado is EstadoDossie.APROVADO:
        raise GateViolado(
            f"nao da para {acao}: o dossie {r.chave} ja foi assinado por "
            f"{r.aprovado_por} em {r.aprovado_em:%d/%m/%Y %H:%M}. Documento assinado "
            f"nao se reabre — rode a conferencia de novo e assine o dossie novo."
        )
    raise GateViolado(
        f"nao da para {acao}: o dossie {r.chave} foi devolvido por {r.devolvido_por} "
        f"({r.motivo}). Devolucao tambem e terminal — a conferencia corrigida gera "
        f"dossie novo, ao lado deste."
    )


def _confere_bytes(arquivo: Arquivo, r: RegistroDossie) -> str:
    markdown = arquivo.markdown(r)
    atual = sha256_de(markdown)
    if atual != r.sha256:
        raise ConteudoDivergente(
            f"o rascunho {r.chave} nao confere com o indice.\n"
            f"  indexado: sha256:{r.sha256}\n"
            f"  no disco: sha256:{atual}\n"
            f"O arquivo mudou depois de guardado. Assinar assim seria assinar em "
            f"branco: rode a conferencia de novo e assine o dossie que ela produzir."
        )
    return markdown


class RodapeAusente(RuntimeError):
    """O rascunho nao tem o marcador que a via assinada substitui."""


def via_assinada(markdown: str, assinatura: Assinatura) -> str:
    """Monta a via assinada **a partir dos bytes conferidos**, nao do modelo.

    Esta e a escolha de desenho que fecha uma fresta minha: a primeira versao
    re-renderizava o dossie a partir do objeto para depois carimbar a assinatura. Isso
    reabria exatamente o buraco que o sha256 existe para tapar — o documento assinado
    poderia divergir do documento conferido, e o hash no rodape passaria a apontar para
    um texto que ninguem leu.

    Aqui o corpo e literalmente o rascunho. Muda so o cabecalho de estado e o paragrafo
    final, que deixa de dizer "falta assinar" e passa a dizer quem assinou.
    """
    linhas = markdown.split("\n")
    if not linhas or not linhas[0].startswith("# "):
        raise RodapeAusente("rascunho sem cabecalho de estado — nao da para assinar")
    linhas[0] = f"# {EstadoDossie.APROVADO.value} — {SUBTITULO}"

    corte = next(
        (i for i, linha in enumerate(linhas) if linha.startswith(MARCA_RODAPE_RASCUNHO)), None
    )
    if corte is None:
        raise RodapeAusente(
            "o rascunho nao traz o paragrafo de RASCUNHO que a via assinada substitui. "
            "Se o rodape de core/dossie.py mudou, MARCA_RODAPE_RASCUNHO tem de mudar junto."
        )
    return "\n".join([*linhas[:corte], *bloco_de_assinatura(assinatura)])


def divergencia_de_assinante(r: RegistroDossie, nome: str) -> str | None:
    """Quem assinou nao e quem a configuracao dizia que assinaria. Aviso, nao bloqueio.

    O indice ja guardava `responsavel` e `aprovado_por` em campos separados, e portanto
    ja **registrava** a divergencia — sem nunca mostra-la. Um dossie dirigido a "Nome do
    Contador" e assinado por outra pessoa passava sem uma palavra.

    Nao bloqueia de proposito: quem opera hoje sao os socios, o substituto legitimo
    existe (ferias, troca de escritorio), e a CLI nao autentica ninguem — isto e um
    **livro-razao de quem assumiu**, nao um controle de acesso. Autenticacao de verdade
    e assunto do M4c, quando o dossie sair daqui. Ate la, o minimo honesto e a
    divergencia aparecer.
    """
    if _normaliza(nome) == _normaliza(r.responsavel):
        return None
    return (
        f"quem assina ({nome}) nao e o responsavel declarado na configuracao "
        f"({r.responsavel}). A assinatura vale e fica registrada com o nome de quem "
        f"assinou; se o responsavel mudou, atualize o YAML do cliente."
    )


def _normaliza(nome: str) -> str:
    return " ".join(nome.strip().casefold().split())


def aprovar(
    arquivo: Arquivo, referencia: str, *, por: str, efeito_liquido_do: Decimal | None = None
) -> RegistroDossie:
    """Assina um dossie. Exige nome de gente e os bytes conferindo.

    Grava a **via assinada** ao lado do rascunho: o mesmo conteudo, mais quem assumiu,
    quando, e o hash exato do que foi conferido. O rascunho nunca e alterado.

    `efeito_liquido_do` entra so na descricao da decisao registrada no cerebro; o indice
    nao guarda valor, por ser lido em claro.
    """
    nome = _nome_de_gente(por)
    r = arquivo.localizar(referencia)
    _exige_rascunho(r, "aprovar")
    markdown = _confere_bytes(arquivo, r)
    efeito_liquido = efeito_liquido_do or ZERO

    quando = agora()
    assinado = r.model_copy(
        update={"estado": EstadoDossie.APROVADO, "aprovado_por": nome, "aprovado_em": quando}
    )
    arquivo.gravar_via_assinada(
        assinado, via_assinada(markdown, Assinatura(por=nome, em=quando, sha256=r.sha256))
    )
    _registrar_no_outbox(arquivo, assinado, efeito_liquido=efeito_liquido)
    return arquivo.atualizar(assinado)


def _registrar_no_outbox(
    arquivo: Arquivo, r: RegistroDossie, *, efeito_liquido: Decimal
) -> None:
    """Enfileira a decisao para o cerebro. Nao escreve nele — ver `core/outbox`.

    Silencioso quando o cliente nao tem `engagement_id`: nem todo CNPJ conferido
    pertence a um trabalho registrado no cerebro, e inventar um seria pior que nao
    registrar. Falha no outbox **nao** desfaz a assinatura: o documento assinado ja
    existe no disco, e a intencao pode ser reenfileirada; perder a assinatura por causa
    do registro seria trocar o que importa pelo que acompanha.
    """
    if not r.engagement_id or r.aprovado_por is None:
        return
    from abba_crews.core.outbox import Outbox, da_assinatura

    Outbox(arquivo).registrar(
        da_assinatura(
            engagement_id=r.engagement_id,
            cnpj=r.cnpj,
            competencia=r.competencia,
            impressao=r.impressao,
            por=r.aprovado_por,
            sha256=r.sha256,
            efeito_liquido=efeito_liquido,
        )
    )


def devolver(
    arquivo: Arquivo, referencia: str, *, por: str, motivo: str
) -> RegistroDossie:
    """Recusa um dossie, com nome e motivo. Motivo vazio nao passa.

    Devolucao sem motivo nao ensina nada a competencia seguinte — e o motivo e o unico
    sinal que temos de onde a conferencia erra.
    """
    nome = _nome_de_gente(por)
    razao = (motivo or "").strip()
    if not razao:
        raise GateViolado(
            "devolucao exige --motivo. Sem ele nao se sabe o que corrigir, e a "
            "competencia seguinte repete o mesmo erro."
        )
    r = arquivo.localizar(referencia)
    _exige_rascunho(r, "devolver")

    devolvido = r.model_copy(
        update={
            "estado": EstadoDossie.DEVOLVIDO,
            "devolvido_por": nome,
            "devolvido_em": agora(),
            "motivo": razao,
        }
    )
    return arquivo.atualizar(devolvido)
