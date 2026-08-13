"""Render DOCX da minuta — documento profissional. Determinístico, zero LLM."""

from __future__ import annotations

from docx import Document

from patrimonio_flow.render import minuta_para_docx, trilha_de_auditoria
from patrimonio_flow.schemas import MinutaFinal


def _minuta():
    return MinutaFinal(
        sumario_executivo="Estrutura sucessória com holding e conta declarada no exterior.",
        corpo_markdown="## Estrutura proposta\nHolding familiar no Brasil.\n## Obrigações\n- DCBE anual",
        fontes_doc_ids=["demo-lei-exterior#art-1::1", "demo-cc-sucessao#art-1::1"],
        limites_da_analise=["PLP 108 em tramitação — área instável"])


def test_gera_docx_com_conteudo(tmp_path):
    caminho = str(tmp_path / "caso1.docx")
    trilha = trilha_de_auditoria("corpus-demo", 3, 0.42)
    saida = minuta_para_docx(_minuta(), caminho, trilha=trilha,
                             preparado_para="Família Exemplo (advogado: Fulano, OAB/XX 000)")
    assert saida == caminho

    doc = Document(caminho)
    texto = "\n".join(p.text for p in doc.paragraphs)
    assert "Sumário executivo" in texto
    assert "Estrutura proposta" in texto
    assert "Preparado para: Família Exemplo" in texto
    # rodapé obrigatório do advogado sempre presente
    assert "Revisão e assinatura" in texto
    # trilha de auditoria presente
    assert "corpus-demo" in texto
    # fontes listadas
    assert "demo-lei-exterior#art-1::1" in texto


def test_trilha_formato():
    t = trilha_de_auditoria("corpus-v0", 5, 1.234)
    assert "corpus-v0" in t and "5 chunks" in t and "US$ 1.23" in t
