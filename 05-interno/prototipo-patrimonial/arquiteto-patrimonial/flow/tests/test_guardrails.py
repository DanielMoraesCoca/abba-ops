"""Guardrails de citação e ocultação — determinísticos, zero LLM.

Cobre as três camadas: abstenção estrutural, anti-órfã, e sustentação a nível
de trecho (o ID é real mas o chunk não ampara a afirmação).
"""

from __future__ import annotations

from types import SimpleNamespace

from patrimonio_flow.guardrails import (
    make_anti_citacao_orfa, minuta_tem_secoes_obrigatorias, sem_linguagem_de_ocultacao,
)
from patrimonio_flow.schemas import AnaliseTributaria, ClaimCitada, MinutaFinal


def _out(model, raw=""):
    return SimpleNamespace(pydantic=model, raw=raw)


def _analise(*claims):
    return _out(AnaliseTributaria(claims=list(claims)))


CHUNK = "lei-14754#art-10::1"
TEXTO = "a lei fixa aliquota de quinze por cento sobre os lucros da controlada no exterior"


def test_abstencao_estrutural_claim_sem_fonte():
    g = make_anti_citacao_orfa([CHUNK], {CHUNK: TEXTO})
    ok, _ = g(_analise(ClaimCitada(text="algo sem fonte nenhuma", source_ids=[])))
    assert ok is False


def test_abstencao_honesta_passa():
    g = make_anti_citacao_orfa([CHUNK], {CHUNK: TEXTO})
    ok, _ = g(_analise(ClaimCitada(text="area instavel, sem cobertura", source_ids=[], nao_coberto=True)))
    assert ok is True


def test_anti_orfa_source_nao_recuperado():
    g = make_anti_citacao_orfa([CHUNK], {CHUNK: TEXTO})
    ok, _ = g(_analise(ClaimCitada(text="aliquota de quinze por cento", source_ids=["inventado#art-99::9"])))
    assert ok is False


def test_sustentacao_claim_amparada_passa():
    g = make_anti_citacao_orfa([CHUNK], {CHUNK: TEXTO})
    ok, _ = g(_analise(ClaimCitada(text="aliquota de quinze por cento sobre lucros", source_ids=[CHUNK])))
    assert ok is True


def test_sustentacao_claim_nao_amparada_falha():
    # ID real e recuperado, mas o texto do chunk não sustenta a afirmação
    g = make_anti_citacao_orfa([CHUNK], {CHUNK: TEXTO})
    ok, _ = g(_analise(ClaimCitada(
        text="o trust internacional fica totalmente isento de tributacao brasileira",
        source_ids=[CHUNK])))
    assert ok is False


def test_sem_textos_mantem_comportamento_id():
    # sem o mapa de textos, só checa órfã/abstenção (retrocompatível)
    g = make_anti_citacao_orfa([CHUNK])
    ok, _ = g(_analise(ClaimCitada(text="qualquer coisa", source_ids=[CHUNK])))
    assert ok is True


def test_linguagem_de_ocultacao_bloqueia():
    ok, _ = sem_linguagem_de_ocultacao(_out(None, raw="usar laranja para nao aparecer ao fisco"))
    assert ok is False
    ok2, _ = sem_linguagem_de_ocultacao(_out(None, raw="estrutura declarada e tributada"))
    assert ok2 is True


def test_minuta_exige_secoes():
    boa = MinutaFinal(sumario_executivo="s",
                      corpo_markdown="## Limites\n## Fontes\n## Obrigacoes\ntexto",
                      fontes_doc_ids=["lei-14754"], limites_da_analise=["x"])
    ok, _ = minuta_tem_secoes_obrigatorias(_out(boa))
    assert ok is True
    ruim = MinutaFinal(sumario_executivo="s", corpo_markdown="sem secoes",
                       fontes_doc_ids=[], limites_da_analise=[])
    ok2, _ = minuta_tem_secoes_obrigatorias(_out(ruim))
    assert ok2 is False
