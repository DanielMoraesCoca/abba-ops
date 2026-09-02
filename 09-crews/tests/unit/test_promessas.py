"""A trava contra a classe de defeito que ja mordeu cinco vezes neste projeto.

## Por que este arquivo existe

"Promessa sem mecanismo" e o defeito recorrente do `abba-crews`. Cinco ocorrencias:

1. **M3a** — `TipoDivergencia.CLASSIFICACAO_DUVIDOSA` declarada, nada a construia: a
   rota `julgamento` do Flow era inalcancavel.
2. **M3a** — `cst`/`c_class_trib` carregados, validados, lidos por ninguem.
3. **M4a** — `EstadoDossie.APROVADO` declarado, nada o produzia.
4. **M4a** — a docstring do Flow prometia o passo `submeter_a_humano`, que nao existia.
5. **M4b (este)** — **a correcao do item 4 reintroduziu o defeito**: o metodo nasceu
   como `_submeter_a_humano`, privado e **sem decorador**, portanto nao e um passo do
   Flow; e a mesma docstring seguia prometendo `reconciliar` e `montar_dossie`, que
   nunca existiram sob esses nomes.

O item 5 e a razao deste arquivo. Quatro marcos achando o mesmo defeito e o quinto
reintroduzindo-o ao corrigi-lo significa que **disciplina nao resolve** — a docstring e
o codigo derivam um do outro em revisao, e ninguem confere par a par. Isto confere.

## O que se trava

O bloco de pipeline na docstring de um Flow (as linhas `nome -> descricao` antes da
primeira linha em branco depois delas) e um **contrato**: todo nome ali tem de existir
como atributo da classe e ser de fato um passo do Flow.
"""

from __future__ import annotations

import inspect
import re

import pytest

from abba_crews.flows.sentinela_flow import SentinelaFlow

FLOWS = [SentinelaFlow]

# `nome -> alguma coisa`, indentado, no bloco de pipeline da docstring.
LINHA_DE_PASSO = re.compile(r"^\s{4}([a-z_][a-z0-9_]*)\s+->\s+\S")

MARCA_CREWAI = "__flow_method_definition__"
"""O atributo que `@start`/`@listen`/`@router` deixam no metodo (CrewAI 1.15)."""


def passos_prometidos(cls: type) -> list[str]:
    doc = inspect.getdoc(cls.__mro__[0]) or ""
    modulo = inspect.getdoc(inspect.getmodule(cls)) or ""
    nomes: list[str] = []
    for texto in (modulo, doc):
        for linha in texto.split("\n"):
            m = LINHA_DE_PASSO.match(linha)
            if m:
                nomes.append(m.group(1))
    return nomes


def e_passo_do_flow(cls: type, nome: str) -> bool:
    """Um passo e um metodo com decorador da CrewAI (`@start`/`@listen`/`@router`).

    Metodo comum nao conta: foi exatamente assim que `_submeter_a_humano` passou por
    passo do Flow sendo uma chamada sincrona dentro de outro metodo.
    """
    metodo = getattr(cls, nome, None)
    if metodo is None:
        return False
    # A CrewAI 1.15 marca todo metodo decorado com `__flow_method_definition__`; um
    # metodo comum nao tem nada. Conferido lendo a biblioteca instalada, nao de memoria
    # — e `test_a_marca_da_crewai_ainda_existe` reprova se a marca sumir num upgrade.
    return hasattr(metodo, MARCA_CREWAI)


@pytest.mark.parametrize("cls", FLOWS, ids=lambda c: c.__name__)
def test_ha_bloco_de_pipeline_para_conferir(cls: type) -> None:
    """Sem isto o teste passaria por vacuo se alguem apagasse o bloco da docstring."""
    assert passos_prometidos(cls), (
        f"{cls.__name__} nao tem bloco de pipeline na docstring do modulo. "
        f"Ou o bloco voltou, ou este teste deixou de proteger alguma coisa."
    )


@pytest.mark.parametrize("cls", FLOWS, ids=lambda c: c.__name__)
def test_todo_passo_prometido_existe(cls: type) -> None:
    ausentes = [n for n in passos_prometidos(cls) if not hasattr(cls, n)]
    assert not ausentes, (
        f"{cls.__name__}: a docstring promete passos que nao existem: {ausentes}. "
        f"Metodos reais: {sorted(m for m in dir(cls) if e_passo_do_flow(cls, m))}"
    )


@pytest.mark.parametrize("cls", FLOWS, ids=lambda c: c.__name__)
def test_todo_passo_prometido_e_de_fato_um_passo(cls: type) -> None:
    """Existir nao basta: tem de ser passo do Flow, nao funcao chamada por dentro."""
    nao_sao = [
        n for n in passos_prometidos(cls) if hasattr(cls, n) and not e_passo_do_flow(cls, n)
    ]
    assert not nao_sao, (
        f"{cls.__name__}: {nao_sao} aparecem no pipeline da docstring mas nao tem "
        f"decorador da CrewAI. Foi assim que `_submeter_a_humano` passou por passo do "
        f"Flow sendo uma chamada sincrona dentro de `_montar`."
    )


@pytest.mark.parametrize("cls", FLOWS, ids=lambda c: c.__name__)
def test_todo_passo_real_esta_documentado(cls: type) -> None:
    """A outra direcao: passo que existe e nao aparece no bloco e passo invisivel.

    So os passos **proprios** da classe: a `Flow` da CrewAI traz os seus
    (`converse_turn`, `route_conversation`...) e nao e a nossa docstring que os descreve.
    """
    reais = {m for m in vars(cls) if not m.startswith("__") and e_passo_do_flow(cls, m)}
    prometidos = set(passos_prometidos(cls))
    assert reais <= prometidos, (
        f"{cls.__name__}: passos do Flow ausentes da docstring: "
        f"{sorted(reais - prometidos)}"
    )


def test_a_marca_da_crewai_ainda_existe() -> None:
    """Se a CrewAI renomear o atributo, esta trava vira teste vazio em silencio.

    Mesma defesa do `test_telemetria`: uma trava que depende de detalhe de outra
    biblioteca tem de falhar alto quando o detalhe muda, nao passar por vacuo.
    """
    decorados = [m for m in dir(SentinelaFlow) if hasattr(getattr(SentinelaFlow, m), MARCA_CREWAI)]
    assert decorados, (
        f"nenhum metodo do SentinelaFlow tem {MARCA_CREWAI}. A CrewAI provavelmente "
        f"renomeou a marca do decorador — procure em crewai/flow/ e atualize MARCA_CREWAI, "
        f"senao esta trava passa sem conferir nada."
    )


def test_a_trava_dispara_quando_a_promessa_e_falsa() -> None:
    """Planta a violacao — mesma disciplina do test_fronteira e do golden set."""

    class FlowMentiroso:
        """Cabecalho.

        pipeline:
            existe_de_verdade  -> faz algo
            nunca_existiu      -> promessa vazia
        """

    assert "nunca_existiu" in passos_prometidos(FlowMentiroso)
    assert not e_passo_do_flow(FlowMentiroso, "nunca_existiu")
