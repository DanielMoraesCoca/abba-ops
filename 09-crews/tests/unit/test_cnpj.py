"""O digito verificador do CNPJ — a defesa contra o pior erro possivel deste produto.

Ate 2026-09-03 os tres validadores de CNPJ do projeto so **contavam** catorze digitos.
`00000000000192` (um digito trocado) e `11111111111111` passavam.

Com um cliente isso falha alto: a guarda do M4b rejeita todo documento como de terceiro
e alguem percebe. **Com uma carteira, o typo que cai sobre outro CNPJ valido confere a
empresa errada em silencio** — e `core/clientes.py` chama exatamente esse cenario de "o
pior erro possivel deste produto".
"""

from __future__ import annotations

import pytest

from abba_crews.core.cnpj import exigir, normalizar, valido

VALIDOS = ("00000000000191", "11444777000161", "11222333000181")
"""Os CNPJs que o projeto ja usava. Todos passam — a trava entrou sem churn."""


@pytest.mark.parametrize("cnpj", VALIDOS)
def test_os_cnpjs_do_projeto_sao_validos(cnpj: str) -> None:
    assert valido(cnpj)


def test_typo_de_um_digito_e_recusado() -> None:
    """O erro mais comum de digitacao, e o que a validacao existe para pegar."""
    assert valido("00000000000191")
    assert not valido("00000000000192")


def test_transposicao_de_digitos_e_recusada() -> None:
    """O segundo erro mais comum: trocar dois digitos de lugar."""
    assert not valido("00000000000119")


def test_sequencia_repetida_e_recusada() -> None:
    """Passa na aritmetica do modulo 11 e nao existe na vida real."""
    for d in "0123456789":
        assert not valido(d * 14), f"{d * 14} nao pode ser aceito"


def test_formatacao_nao_atrapalha() -> None:
    assert valido("00.000.000/0001-91")
    assert normalizar("00.000.000/0001-91") == "00000000000191"


def test_tamanho_errado_e_recusado() -> None:
    assert not valido("123")
    assert not valido("000000000001911")


def test_exigir_separa_os_dois_erros() -> None:
    """Tamanho e digito mandam a pessoa olhar coisas diferentes do que ela digitou."""
    with pytest.raises(ValueError, match="14 digitos"):
        exigir("123", campo="cnpj")
    with pytest.raises(ValueError, match="digito verificador"):
        exigir("00000000000192", campo="cnpj")


def test_exigir_devolve_normalizado() -> None:
    assert exigir("00.000.000/0001-91") == "00000000000191"


def test_alfanumerico_e_recusado_e_a_mensagem_aponta_a_pendencia() -> None:
    """A Receita passou a emitir CNPJ com letras e a regra nova nao pode ser conferida
    deste ambiente. Recusar e o desfecho seguro; a mensagem diz onde esta a pendencia."""
    with pytest.raises(ValueError, match="P8"):
        exigir("12ABC34501DE35", campo="cnpj")


# --------------------------------------------------------------------------- #
# Onde a trava tem de valer
# --------------------------------------------------------------------------- #


def test_config_de_cliente_recusa_cnpj_invalido() -> None:
    """O YAML e digitado a mao — e onde o typo nasce."""
    from abba_crews.core.clientes import Aprovacao, ConfigCliente

    ap = Aprovacao(responsavel_nome="Fulano de Tal", responsavel_email="a@b.com")
    with pytest.raises(ValueError, match="digito verificador"):
        ConfigCliente(cnpj="00000000000192", razao_social="Empresa", aprovacao=ap)


def test_documento_fiscal_recusa_cnpj_invalido() -> None:
    from datetime import date

    from abba_crews.core.modelos import DocumentoFiscal, ItemDocumento, Papel

    item = ItemDocumento(
        numero=1, cst="000", c_class_trib="000001", vbc="1000.00",
        v_ibs_uf="5.00", v_ibs_mun="5.00", v_cbs="90.00",
    )
    with pytest.raises(ValueError, match="digito verificador"):
        DocumentoFiscal(
            chave="9" * 44, papel=Papel.ENTRADA,
            emitente_cnpj="11444777000162",  # digito trocado
            destinatario_cnpj="00000000000191",
            data_emissao=date(2027, 3, 15), itens=(item,),
        )


def test_apuracao_recusa_cnpj_invalido() -> None:
    from abba_crews.core.modelos import ApuracaoFisco

    with pytest.raises(ValueError, match="digito verificador"):
        ApuracaoFisco(cnpj="00000000000192", competencia="2027-03", linhas=())
