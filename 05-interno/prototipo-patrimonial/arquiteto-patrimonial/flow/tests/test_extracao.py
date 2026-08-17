"""Porta de entrada (extração de documento) — a garantia crítica: PII não vaza
para o LLM. Determinístico, zero LLM.
"""

from __future__ import annotations

from patrimonio_flow.pii import mascarar


DOC = (
    "Cliente: João da Silva Andrade, CPF 123.456.789-09, e-mail joao@exemplo.com, "
    "telefone (61) 99999-8888. Vendeu a empresa em 2025 por cerca de R$ 80 milhões. "
    "Mantém conta de investimento nos EUA, declarada. Dois filhos do primeiro casamento."
)


def test_documento_mascara_cpf_email_telefone():
    m = mascarar(DOC)
    # os dados sensíveis SUMIRAM do texto que iria ao LLM
    assert "123.456.789-09" not in m.texto_mascarado
    assert "joao@exemplo.com" not in m.texto_mascarado
    assert "99999-8888" not in m.texto_mascarado
    # e ficaram guardados no de-para (que fica só no backend)
    assert "123.456.789-09" in m.de_para.values()
    assert any(k.startswith("<CPF") for k in m.de_para)
    # o conteúdo NÃO sensível permanece (o LLM ainda entende o caso)
    assert "empresa" in m.texto_mascarado and "EUA" in m.texto_mascarado


def test_restaurar_roundtrip():
    m = mascarar(DOC)
    assert m.restaurar(m.texto_mascarado) == DOC


def test_placeholders_estaveis_por_valor():
    # o mesmo valor repetido ganha um único placeholder
    m = mascarar("CPF 111.111.111-11 e de novo 111.111.111-11")
    assert list(m.de_para.values()).count("111.111.111-11") == 1


def test_extracao_crew_importavel():
    from patrimonio_flow.crews.extracao_crew import ExtracaoCrew
    assert "extracao_agents.yaml" in ExtracaoCrew.agents_config
    assert "extracao_tasks.yaml" in ExtracaoCrew.tasks_config
