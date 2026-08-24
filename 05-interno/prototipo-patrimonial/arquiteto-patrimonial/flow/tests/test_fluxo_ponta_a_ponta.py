"""Integração ponta-a-ponta do PatrimonioFlow — SEM LLM, SEM rede, SEM segredo.

Prova o ENCANAMENTO do produto (o que uma run paga no AMP exercita), substituindo
apenas as saídas dos agentes por saídas fabricadas VÁLIDAS NO SCHEMA. Cobre o que
o medo legítimo "vai rodar mesmo?" pergunta:

  intake → gate1 (liberado) → crew_analise (monta AnaliseJuridica dos 3 outputs)
  → crew_desenho (zip desenho×crítica, descarta ataque fatal, loop de reexecução,
    guards de None do commit 78231f7) → obrigacoes_e_cenarios (aritmética real)
  → [gate do advogado: aprovação simulada] → crew_redacao → render_final (+ DOCX).

O que ISTO NÃO cobre (e só uma run paga cobre): a adesão do modelo real ao schema
de saída. Mas o único modo de falha visto ao vivo (truncamento de JSON) já tem
correção (max_tokens) e a análise real já respeitou o schema. Aqui provamos que,
DADAS saídas bem-formadas, a máquina roda do começo ao fim e entrega a minuta.
"""

from __future__ import annotations

import os
import types

import pytest

import patrimonio_flow.crews.analise_crew as analise_mod
import patrimonio_flow.crews.desenho_crew as desenho_mod
import patrimonio_flow.crews.redacao_crew as redacao_mod
from patrimonio_flow import schemas as S
from patrimonio_flow.main import PatrimonioFlow


# --------------------------------------------------------------- fakes de crew

class _FakeTaskOut:
    def __init__(self, pydantic):
        self.pydantic = pydantic


class _FakeResult:
    """Imita o CrewOutput: tasks_output[i].pydantic + token_usage."""

    def __init__(self, pydantics, pt=1200, ct=800):
        self.tasks_output = [_FakeTaskOut(p) for p in pydantics]
        self.token_usage = types.SimpleNamespace(prompt_tokens=pt, completion_tokens=ct)


class _FakeCrew:
    def __init__(self, pydantics):
        self._pydantics = pydantics

    def kickoff(self, inputs=None):
        return _FakeResult(self._pydantics)


def _fake_crew_class(pydantics):
    class _Fake:
        def __init__(self, *a, **k):
            pass

        def crew(self):
            return _FakeCrew(pydantics)

    return _Fake


# --------------------------------------------------------------- saídas fabricadas

def _claim(text, sid):
    return S.ClaimCitada(text=text, source_ids=[sid])


def _analise_outputs():
    return [
        S.AnaliseTributaria(claims=[_claim("Regime 14.754 aplica-se ao exterior.", "demo-lei-exterior")]),
        S.AnaliseSucessoria(claims=[_claim("Sucessao segue o CC brasileiro.", "demo-cc-sucessao")]),
        S.AnaliseJurisdicoes(claims=[_claim("Imovel nos EUA sujeito a estate tax.", "demo-ficha-eua")]),
    ]


def _desenho_bom():
    return S.DesenhoEstrutura(
        nome="Holding BR + conta declarada",
        elementos=[S.ElementoEstrutura(veiculo="holding BR", jurisdicao="BR",
                                       proposito="consolidar", source_ids=["demo-cc-sucessao"])],
        sequencia_implantacao=["constituir holding", "declarar exterior"],
        custo_manutencao_anual_estimado_brl=12000.0,
        trade_offs="simples, transparente")


def _desenho_fatal():
    return S.DesenhoEstrutura(
        nome="Estrutura opaca no exterior",
        elementos=[S.ElementoEstrutura(veiculo="offshore", jurisdicao="XX", proposito="ocultar")],
        sequencia_implantacao=["passo"], custo_manutencao_anual_estimado_brl=50000.0,
        trade_offs="opaca")


def _desenho_outputs(com_fatal: bool):
    """1ª task: ListaDesenhos. 2ª task: ListaCriticas (na mesma ordem)."""
    if com_fatal:
        desenhos = [_desenho_bom(), _desenho_bom(), _desenho_fatal()]
        criticas = [
            S.CriticaAdversarial(ataques=[S.AtaqueAdversarial(descricao="ok", gravidade=S.GravidadeAtaque.MENOR)]),
            S.CriticaAdversarial(ataques=[S.AtaqueAdversarial(descricao="ok", gravidade=S.GravidadeAtaque.MENOR)]),
            S.CriticaAdversarial(ataques=[S.AtaqueAdversarial(descricao="ilícito", gravidade=S.GravidadeAtaque.FATAL)]),
        ]
    else:
        desenhos = [_desenho_bom(), _desenho_bom()]
        criticas = [
            S.CriticaAdversarial(ataques=[S.AtaqueAdversarial(descricao="ok", gravidade=S.GravidadeAtaque.MENOR)]),
            S.CriticaAdversarial(ataques=[S.AtaqueAdversarial(descricao="ok", gravidade=S.GravidadeAtaque.MENOR)]),
        ]
    return [S.ListaDesenhos(desenhos=desenhos), S.ListaCriticas(criticas=criticas)]


def _minuta_output():
    return [S.MinutaFinal(
        sumario_executivo="Estrutura recomendada: holding BR + conta declarada.",
        corpo_markdown="# Minuta\n\n## Análise\n...\n## Estrutura\n...\n## Obrigações\n...",
        fontes_doc_ids=["demo-lei-exterior", "demo-cc-sucessao", "demo-ficha-eua"],
        limites_da_analise=["Sujeito a revisão do advogado nomeado."])]


# --------------------------------------------------------------- perfil liberado

def _perfil_liberado() -> S.PerfilEstruturado:
    return S.PerfilEstruturado(
        pessoa=S.Pessoa(idade=64, estado_civil="viuvo", residencia_fiscal="BR", us_person=False),
        familia=S.Familia(), sucessao=S.Sucessao(),
        patrimonio=S.Patrimonio(
            ativos=[
                S.Ativo(classe=S.AtivoClasse.IMOVEL_EXTERIOR, descricao="Apto Miami",
                        ordem_grandeza_brl=8_000_000.0, jurisdicao="US"),
                S.Ativo(classe=S.AtivoClasse.IMOVEL_BR, descricao="Imovel SP",
                        ordem_grandeza_brl=3_000_000.0, jurisdicao="BR"),
            ],
            exterior_declarado_irpf_dcbe=True),
        passivos=S.Passivos(),
        objetivos=S.Objetivos(prioridades=["organizar_sucessao"]),
        conformidade=S.Conformidade(irpf_em_dia=True, origem_recursos_documentavel=True,
                                    aceite_transparencia=True))


def _flow_liberado(monkeypatch, com_fatal: bool) -> PatrimonioFlow:
    monkeypatch.setattr(analise_mod, "AnaliseCrew", _fake_crew_class(_analise_outputs()))
    monkeypatch.setattr(desenho_mod, "DesenhoCrew", _fake_crew_class(_desenho_outputs(com_fatal)))
    monkeypatch.setattr(redacao_mod, "RedacaoCrew", _fake_crew_class(_minuta_output()))
    flow = PatrimonioFlow()
    flow.state.perfil = _perfil_liberado()
    flow.state.caso_id = "caso-teste"
    flow.state.teto_usd_caso = 100.0  # sem estourar teto neste teste de encanamento
    return flow


# =============================================================== os testes

def test_spine_ate_obrigacoes_roda_ponta_a_ponta(monkeypatch):
    """intake → gate1 → análise → desenho → obrigações, tudo encadeado."""
    flow = _flow_liberado(monkeypatch, com_fatal=False)

    flow.intake()
    assert flow.state.perfil is not None

    rota = flow.gate1_red_flags()
    assert rota == "liberado", "P07 é caso liberado — não pode bloquear"

    analise = flow.crew_analise()
    assert isinstance(analise, S.AnaliseJuridica)
    assert analise.tributaria.claims[0].source_ids == ["demo-lei-exterior"]

    desenhos = flow.crew_desenho()
    assert len(desenhos) == 2, "2 desenhos bons sobrevivem"
    assert all(d.critica is not None for d in desenhos), "cada desenho recebeu sua crítica (zip)"

    obrig = flow.obrigacoes_e_cenarios()
    assert len(obrig) == 2, "um pacote de obrigações por desenho"
    assert flow.state.cenarios, "cenários projetados"


def test_desenho_descarta_ataque_fatal(monkeypatch):
    """O 3º desenho tem ataque FATAL → é descartado; sobram os 2 bons."""
    flow = _flow_liberado(monkeypatch, com_fatal=True)
    flow.intake()
    flow.gate1_red_flags()
    flow.crew_analise()
    desenhos = flow.crew_desenho()
    nomes = {d.nome for d in desenhos}
    assert "Estrutura opaca no exterior" not in nomes, "desenho com ataque fatal deve ser descartado"
    assert len(desenhos) == 2


def test_aprovacao_gera_minuta_e_docx(monkeypatch, tmp_path):
    """Pós-gate: aprovação → redação → render_final entrega markdown + DOCX no disco."""
    flow = _flow_liberado(monkeypatch, com_fatal=False)
    flow.intake()
    flow.gate1_red_flags()
    flow.crew_analise()
    flow.crew_desenho()
    flow.obrigacoes_e_cenarios()

    # gate do advogado: aprovação (o gate real é @human_feedback; aqui simulamos a
    # decisão humana — a lógica do gate já é testada em test_hitl.py).
    from patrimonio_flow.hitl import aplicar_decisao
    aplicar_decisao(flow.state, "aprovado", feedback="ok")
    assert flow.state.gate_humano_ok is True

    minuta = flow.crew_redacao()
    assert isinstance(minuta, S.MinutaFinal)

    os.environ["MINUTA_DIR"] = str(tmp_path)
    try:
        saida = flow.render_final()
    finally:
        os.environ.pop("MINUTA_DIR", None)

    assert "Minuta" in saida
    assert flow.state.minuta.rodape_obrigatorio in saida, "rodapé obrigatório presente"
    docx = tmp_path / "caso-teste.docx"
    assert docx.exists() and docx.stat().st_size > 0, "DOCX entregue no disco"


def test_render_sem_gate_humano_e_bloqueado(monkeypatch):
    """Trava não-burlável: render_final sem gate humano levanta AssertionError."""
    flow = _flow_liberado(monkeypatch, com_fatal=False)
    flow.intake()
    flow.gate1_red_flags()
    flow.crew_analise()
    flow.crew_desenho()
    flow.obrigacoes_e_cenarios()
    flow.crew_redacao()
    assert flow.state.gate_humano_ok is False
    with pytest.raises(AssertionError):
        flow.render_final()
