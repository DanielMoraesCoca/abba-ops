"""Mascaramento de PII ANTES do LLM (guardrail de produção — LGPD por desenho).

CONTRATO. A redaction nativa do CrewAI AMP cobre apenas os TRACES; NÃO sanitiza o
prompt enviado ao provedor. Este módulo é o mascaramento real pré-LLM: o caso
trafega pseudonimizado (caso_id + placeholders), e o de-para fica SÓ no backend,
nunca no provedor de modelo.

Implementação de produção (próximo gatilho): Presidio (detecção) + LiteLLM guardrail
(ou gateway Portkey) na frente do modelo. Aqui fica o contrato + um mascarador
determinístico de referência (regex) para teste sem dependência externa.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# Padrões brasileiros comuns. Presidio cobre muito mais em produção (nomes, endereços).
_PADROES = {
    "CPF": re.compile(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"),
    "CNPJ": re.compile(r"\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b"),
    "EMAIL": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
    "TELEFONE": re.compile(r"(?<!\d)(?:\+?55\s?)?\(?\d{2}\)?\s?9?\d{4}-?\d{4}(?!\d)"),
    "RG": re.compile(r"\b\d{1,2}\.?\d{3}\.?\d{3}-?[\dxX]\b"),
}


@dataclass
class MascaraPII:
    """Resultado do mascaramento: texto seguro + o de-para (que NUNCA vai ao LLM)."""
    texto_mascarado: str
    de_para: dict[str, str] = field(default_factory=dict)  # placeholder -> valor original

    def restaurar(self, texto: str) -> str:
        """Re-hidrata a saída do LLM com os valores originais, no backend."""
        for placeholder, original in self.de_para.items():
            texto = texto.replace(placeholder, original)
        return texto


def mascarar(texto: str) -> MascaraPII:
    """Substitui PII por placeholders estáveis (<CPF_1>, <EMAIL_1>...). Determinístico."""
    de_para: dict[str, str] = {}
    contadores: dict[str, int] = {}
    resultado = texto
    for tipo, padrao in _PADROES.items():
        for match in padrao.findall(resultado):
            valor = match if isinstance(match, str) else match[0]
            if valor in de_para.values():
                continue
            contadores[tipo] = contadores.get(tipo, 0) + 1
            placeholder = f"<{tipo}_{contadores[tipo]}>"
            de_para[placeholder] = valor
            resultado = resultado.replace(valor, placeholder)
    return MascaraPII(texto_mascarado=resultado, de_para=de_para)


def before_llm_call_hook(mensagens: list[dict]) -> tuple[list[dict], MascaraPII]:
    """Hook a plugar no @before_llm_call do CrewAI: mascara todo conteúdo antes do envio.
    Retorna as mensagens seguras + a máscara (guardada no backend para re-hidratar a saída).
    TODO(produção): trocar o mascarador regex por Presidio; validar CPF por dígito verificador."""
    mascara_agregada = MascaraPII(texto_mascarado="")
    seguras = []
    for m in mensagens:
        conteudo = m.get("content", "")
        r = mascarar(conteudo)
        mascara_agregada.de_para.update(r.de_para)
        seguras.append({**m, "content": r.texto_mascarado})
    return seguras, mascara_agregada
