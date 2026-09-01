"""Configuracao por cliente e o dossie — o "esqueleto + ajustes" e o que a pessoa le."""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from abba_crews.core.calendario import JanelaManifestacao
from abba_crews.core.clientes import ConfigCliente, carregar, carregar_por_cnpj
from abba_crews.core.dossie import EstadoDossie, Natureza, montar, renderizar
from abba_crews.core.modelos import Papel
from abba_crews.core.reconciliacao import apuracao_a_partir_de, reconciliar
from abba_crews.core.sinteticos import CNPJ_EMPRESA, COMPETENCIA, _doc, _vazia

BASE = Path(__file__).resolve().parents[2] / "src" / "abba_crews" / "config" / "clientes"

YAML_OK = """
cnpj: "00000000000191"
razao_social: "Empresa Teste Ltda"
regime: regular
entrega_dere: false
tolerancia_brl: "0.00"
aprovacao:
  responsavel_nome: "Maria Contadora"
  responsavel_email: "maria@escritorio.com.br"
  papel: contador
"""


def escreve(tmp_path: Path, nome: str, texto: str) -> Path:
    p = tmp_path / nome
    p.write_text(texto, encoding="utf-8")
    return p


# ------------------------------ configuracao ------------------------------ #


def test_exemplo_versionado_carrega() -> None:
    """O exemplo e documentacao viva: se ele quebrar, a doc mentiu."""
    assert carregar(BASE / "exemplo.yaml").razao_social


def test_carrega_por_cnpj() -> None:
    c = carregar_por_cnpj("00.000.000/0001-91", BASE)
    assert c.cnpj == "00000000000191"
    assert c.aprovacao.responsavel_nome


def test_cnpj_do_arquivo_tem_de_bater_com_o_conteudo(tmp_path: Path) -> None:
    """Conferir a apuracao do CNPJ errado e o pior erro possivel deste produto."""
    p = escreve(tmp_path, "11444777000161.yaml", YAML_OK)
    with pytest.raises(ValueError, match="nome do arquivo"):
        carregar(p)


def test_yaml_invalido_falha_dizendo_o_campo(tmp_path: Path) -> None:
    p = escreve(tmp_path, "00000000000191.yaml", YAML_OK.replace("Maria Contadora", "M"))
    with pytest.raises(ValueError, match="responsavel_nome"):
        carregar(p)


def test_email_invalido_e_recusado(tmp_path: Path) -> None:
    p = escreve(
        tmp_path, "00000000000191.yaml", YAML_OK.replace("maria@escritorio.com.br", "maria")
    )
    with pytest.raises(ValueError, match="aprovacao.responsavel_email"):
        carregar(p)


def test_tolerancia_negativa_e_recusada(tmp_path: Path) -> None:
    p = escreve(tmp_path, "00000000000191.yaml", YAML_OK.replace('"0.00"', '"-1.00"'))
    with pytest.raises(ValueError, match="tolerancia"):
        carregar(p)


def test_cnpj_inexistente_lista_os_disponiveis(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="Disponiveis"):
        carregar_por_cnpj("99999999999999", tmp_path)


# --------------------------------- dossie --------------------------------- #


def config() -> ConfigCliente:
    return carregar(BASE / "exemplo.yaml")


def dossie_de(hoje: date, *, conforme: bool):
    entrada = _doc(1, Papel.ENTRADA)
    apuracao = (
        apuracao_a_partir_de((entrada,), CNPJ_EMPRESA, COMPETENCIA) if conforme else _vazia()
    )
    r = reconciliar((entrada,), apuracao)
    j = JanelaManifestacao.para(COMPETENCIA)
    return montar(config=config(), janela=j, resultado=r, hoje=hoje)


def test_dossie_nasce_rascunho() -> None:
    d = dossie_de(date(2027, 4, 20), conforme=False)
    assert d.estado is EstadoDossie.RASCUNHO
    assert "RASCUNHO" in renderizar(d)


def test_dentro_da_janela_com_divergencia_e_manifestacao() -> None:
    d = dossie_de(date(2027, 4, 20), conforme=False)
    assert d.natureza is Natureza.MANIFESTACAO
    assert d.total_favoravel > Decimal("0")


def test_sem_divergencia_e_nada_a_fazer() -> None:
    d = dossie_de(date(2027, 4, 20), conforme=True)
    assert d.natureza is Natureza.NADA_A_FAZER
    assert "Nada a manifestar" in renderizar(d)


def test_fora_do_prazo_vira_registro_de_perda() -> None:
    """Nao se manifesta fora da janela — e o texto tem de dizer isso."""
    d = dossie_de(date(2027, 5, 10), conforme=False)
    assert d.natureza is Natureza.REGISTRO_DE_PERDA
    texto = renderizar(d)
    assert "Registro de perda" in texto
    assert "ENCERRADO" in texto


def test_dossie_abre_com_prazo_e_valor() -> None:
    """O contador tem janela curta: prazo e R$ vem antes de qualquer detalhe."""
    texto = renderizar(dossie_de(date(2027, 4, 27), conforme=False))
    cabecalho = texto.split("### ")[0]
    assert "Prazo de manifestacao" in cabecalho
    assert "R$" in cabecalho


def test_os_dois_lados_aparecem_separados() -> None:
    saida = _doc(2, Papel.SAIDA)
    entrada = _doc(1, Papel.ENTRADA)
    r = reconciliar((entrada, saida), _vazia())
    d = montar(
        config=config(),
        janela=JanelaManifestacao.para(COMPETENCIA),
        resultado=r,
        hoje=date(2027, 4, 20),
    )
    texto = renderizar(d)
    assert "A favor do contribuinte" in texto
    assert "Contra o contribuinte" in texto
    assert d.total_desfavoravel > Decimal("0")


def test_rodape_declara_a_fronteira_e_nao_conclui() -> None:
    texto = renderizar(dossie_de(date(2027, 4, 20), conforme=False))
    assert "nao transmite nada ao Fisco" in texto
    assert "Nao emite parecer tributario" in texto
    for proibido in ("e devido", "faz jus a", "recomendamos pleitear"):
        assert proibido not in texto.lower()


def test_render_e_deterministico() -> None:
    a = renderizar(dossie_de(date(2027, 4, 20), conforme=False))
    b = renderizar(dossie_de(date(2027, 4, 20), conforme=False))
    assert a == b


# --------------------------- descartados e por que --------------------------- #


def _dossie_com_descarte(caso_id: str):  # type: ignore[no-untyped-def]
    from abba_crews.core.sinteticos import TABELA_ENSAIO, golden_set

    caso = next(c for c in golden_set() if c.id == caso_id)
    resultado = reconciliar(caso.documentos, caso.apuracao, classificador=TABELA_ENSAIO)
    return montar(
        config=carregar_por_cnpj(CNPJ_EMPRESA),
        janela=JanelaManifestacao.para(COMPETENCIA),
        resultado=resultado,
        hoje=date(2027, 4, 20),
    )


def test_dossie_mostra_o_que_foi_descartado_com_a_fonte() -> None:
    """Um documento que so mostra o que entra pede fe; este pode ser conferido."""
    md = renderizar(_dossie_com_descarte("negativo-cst-vedado"))
    assert "Descartados e por que" in md
    assert "R$ 100,00" in md
    assert "CST 999" in md
    assert "fonte:" in md


def test_nada_a_manifestar_com_descarte_nao_diz_que_a_proposta_confere() -> None:
    """Sem esta ressalva o texto mentiria.

    A proposta NAO conferiu com os documentos: houve credito ausente dela, que nao foi
    pleiteado por decisao de creditabilidade. "Nenhuma divergencia encontrada" ali
    esconderia justamente a decisao que o contador precisa conferir.
    """
    d = _dossie_com_descarte("negativo-cst-vedado")
    assert d.natureza is Natureza.NADA_A_FAZER
    md = renderizar(d)
    assert "Nenhuma divergencia encontrada" not in md
    assert "nao entrou" in md or "nao entraram" in md
    assert d.total_descartado == Decimal("100.00")


def test_dossie_sem_descarte_nao_ganha_a_secao() -> None:
    docs = (_doc(1, Papel.ENTRADA),)
    r = reconciliar(docs, _vazia())
    d = montar(
        config=carregar_por_cnpj(CNPJ_EMPRESA),
        janela=JanelaManifestacao.para(COMPETENCIA),
        resultado=r,
        hoje=date(2027, 4, 20),
    )
    assert "Descartados" not in renderizar(d)
