"""O golden set e o avaliador — e o avaliador e intocavel.

Inegociavel 4 da casa: golden sets e limiares ficam fora do alcance de qualquer
loop de melhoria automatica. Um sistema que pode mexer na propria regua otimiza a
nota, nao o resultado.

Estes testes travam duas coisas: que o conjunto passa, e que o **avaliador reprova
de verdade** quando o produto erra. Avaliador que nunca falha nao mede nada.
"""

from __future__ import annotations

from abba_crews.core.reconciliacao import TipoDivergencia
from abba_crews.core.sinteticos import CasoGolden, Familia, golden_set, rodar


def test_golden_set_v0_passa() -> None:
    placar = rodar()
    assert placar.aprovado, "\n".join(placar.falhas)
    assert placar.recall == 1.0
    assert placar.precisao_nos_negativos == 1.0


def test_o_conjunto_cobre_as_tres_familias() -> None:
    familias = {c.familia for c in golden_set()}
    assert familias == {Familia.POSITIVO, Familia.NEGATIVO, Familia.LIMPO}


def test_todo_tipo_estrutural_tem_caso() -> None:
    """Tipo de divergencia sem caso no golden set e comportamento nao medido."""
    cobertos = {t for c in golden_set() for t in c.tipos_esperados}
    estruturais = set(TipoDivergencia) - {TipoDivergencia.CLASSIFICACAO_DUVIDOSA}
    faltando = estruturais - cobertos
    assert not faltando, f"sem caso no golden set: {sorted(t.value for t in faltando)}"


def test_ids_unicos_e_descricoes_preenchidas() -> None:
    casos = golden_set()
    ids = [c.id for c in casos]
    assert len(ids) == len(set(ids))
    for c in casos:
        assert c.descricao.strip(), f"{c.id} sem descricao — caso sem razao e caso esquecido"


def test_avaliador_reprova_falso_positivo() -> None:
    """Prova que o avaliador pega o erro que mais importa.

    Pegamos um caso que DEVE ficar limpo e mentimos no gabarito, dizendo que ele
    nao espera achado quando na verdade ha divergencia. Se o avaliador aprovasse,
    ele nao estaria medindo precisao nenhuma.
    """
    positivo = next(c for c in golden_set() if c.familia is Familia.POSITIVO)
    disfarcado = CasoGolden(
        id="plantado-falso-positivo",
        familia=Familia.NEGATIVO,
        descricao="Caso com divergencia real, marcado como se devesse ficar limpo.",
        documentos=positivo.documentos,
        apuracao=positivo.apuracao,
        tipos_esperados=(),
    )

    placar = rodar((disfarcado,))

    assert not placar.aprovado
    assert placar.precisao_nos_negativos == 0.0
    assert any("FALSO POSITIVO" in f for f in placar.falhas)


def test_avaliador_reprova_falso_negativo() -> None:
    """E pega tambem o achado que o produto deixou passar."""
    limpo = next(c for c in golden_set() if c.familia is Familia.LIMPO)
    disfarcado = CasoGolden(
        id="plantado-falso-negativo",
        familia=Familia.POSITIVO,
        descricao="Caso limpo, marcado como se tivesse credito omitido.",
        documentos=limpo.documentos,
        apuracao=limpo.apuracao,
        tipos_esperados=(TipoDivergencia.CREDITO_OMITIDO,),
    )

    placar = rodar((disfarcado,))

    assert not placar.aprovado
    assert placar.recall == 0.0
