"""Runner do golden set — camada DETERMINÍSTICA (sem LLM-judge).

Camadas de avaliação (avaliacao-e-metrica.md):
1. DETERMINÍSTICA (esta): gate 1 contra gabarito (bloqueado + flags exatos),
   zero citações órfãs, obrigações mínimas, seções da minuta.
2. ESPECIALISTA: advogado nomeado pontua desenho (rubrica 0-2).
3. LLM-judge (só qualidade textual).

Esta camada roda em CI a cada mudança de prompt/corpus — **zero chamada de LLM**.
Prova o gate de conformidade contra as 12 personas do golden set.
"""

from __future__ import annotations

import json
import pathlib

from patrimonio_flow.gates import triagem_red_flags
from patrimonio_flow.schemas import (
    Conformidade, Familia, Objetivos, Passivos, Patrimonio, PerfilEstruturado,
    Pessoa, Sucessao,
)

GOLDEN = pathlib.Path(__file__).parent / "golden_personas.json"


def carregar_personas() -> list[dict]:
    return json.loads(GOLDEN.read_text(encoding="utf-8"))["personas"]


def _perfil_base() -> PerfilEstruturado:
    """Perfil-base CONFORME (defaults limpos). campos_chave introduzem o problema
    de cada persona. `aceite_transparencia=True` de propósito: o cliente-padrão
    aceita transparência — só a persona de recusa (P05) o define False. Sem isto,
    o default False dispararia RF6 em todas (o produto força esse aceite no intake)."""
    return PerfilEstruturado(
        pessoa=Pessoa(idade=50, estado_civil="casado"),
        familia=Familia(), sucessao=Sucessao(), patrimonio=Patrimonio(),
        passivos=Passivos(), objetivos=Objetivos(),
        conformidade=Conformidade(aceite_transparencia=True))


def montar_perfil(campos_chave: dict) -> PerfilEstruturado:
    """Aplica os campos_chave (dot-paths) sobre o perfil base. Best-effort: o
    gate 1 só lê campos bem-tipados (bool/float/list), que mapeiam limpo; campos
    ilustrativos (ex.: descrição de ativos em string) não afetam o gate 1."""
    perfil = _perfil_base()
    for caminho, valor in campos_chave.items():
        partes = caminho.split(".")
        alvo = perfil
        for p in partes[:-1]:
            alvo = getattr(alvo, p)
        setattr(alvo, partes[-1], valor)  # validate_assignment off: sem coerção — ok p/ gate1
    return perfil


def avaliar_gate1() -> dict:
    """Camada 1: red flags contra gabarito para as 12 personas.
    Compara `bloqueado` e o CONJUNTO de códigos de flag."""
    resultados = {"total": 0, "ok": 0, "falhas": []}
    for persona in carregar_personas():
        resultados["total"] += 1
        perfil = montar_perfil(persona.get("campos_chave", {}))
        report = triagem_red_flags(perfil)
        gab = persona.get("gabarito", {})
        esperado_bloqueado = bool(gab.get("bloqueado", False))
        esperados = set(gab.get("flags_esperados", []))
        obtidos = {f.codigo for f in report.flags}
        ok = (report.bloqueado == esperado_bloqueado) and (obtidos == esperados)
        if ok:
            resultados["ok"] += 1
        else:
            resultados["falhas"].append({
                "id": persona["id"],
                "bloqueado_esperado": esperado_bloqueado, "bloqueado_obtido": report.bloqueado,
                "flags_esperados": sorted(esperados), "flags_obtidos": sorted(obtidos),
            })
    return resultados


if __name__ == "__main__":
    print(json.dumps(avaliar_gate1(), indent=2, ensure_ascii=False))
