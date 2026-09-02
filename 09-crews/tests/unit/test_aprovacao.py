"""O gate humano — o inegociavel 1, agora com mecanismo.

Ate o M4a `EstadoDossie.APROVADO` era **enum morto**: existia na declaracao e nada o
produzia. O rodape de todo dossie prometia *"nao vale como manifestacao enquanto nao for
conferido e assinado por Nome do Contador"* e nao havia caminho algum pelo qual esse
contador assinasse. Pior: o Flow montava o markdown na memoria e jogava fora — nao havia
sequer o que assinar.

Estes testes travam as quatro coisas que fazem o gate valer alguma coisa:

1. **exige nome de gente** — gate sem nome e automacao com nome de gate;
2. **os bytes tem de conferir** — assinar sem isso e assinar em branco;
3. **nao volta atras** — documento que pode voltar de assinado para rascunho nao prova nada;
4. **sem senha nao grava** — dado fiscal de cliente nao vai para o disco em claro.

Cada recusa e provada plantando a violacao, como no `test_fronteira` e no golden set.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest

from abba_crews.core.aprovacao import (
    ConteudoDivergente,
    GateViolado,
    aprovar,
    devolver,
)
from abba_crews.core.arquivo import (
    Arquivo,
    DossieNaoEncontrado,
    RaizInsegura,
    ReferenciaAmbigua,
    sha256_de,
)
from abba_crews.core.calendario import JanelaManifestacao
from abba_crews.core.clientes import carregar_por_cnpj
from abba_crews.core.cofre import MAGIC, SenhaAusente, decifrar
from abba_crews.core.dossie import Dossie, EstadoDossie, montar, renderizar
from abba_crews.core.reconciliacao import reconciliar
from abba_crews.core.sinteticos import CNPJ_EMPRESA, COMPETENCIA, golden_set

SENHA = "senha-de-teste"
HOJE = date(2027, 4, 20)


@pytest.fixture(autouse=True)
def _senha(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ABBA_DB_PASSPHRASE", SENHA)


@pytest.fixture
def arquivo(tmp_path: Path) -> Arquivo:
    return Arquivo(tmp_path / "dossies")


def _dossie(caso_id: str = "positivo-credito-omitido") -> tuple[Dossie, str]:
    caso = next(c for c in golden_set() if c.id == caso_id)
    resultado = reconciliar(caso.documentos, caso.apuracao)
    d = montar(
        config=carregar_por_cnpj(CNPJ_EMPRESA),
        janela=JanelaManifestacao.para(COMPETENCIA),
        resultado=resultado,
        hoje=HOJE,
    )
    return d, renderizar(d)


def _guarda(arq: Arquivo, caso_id: str = "positivo-credito-omitido", impressao: str = "aaaa1111"):  # type: ignore[no-untyped-def]
    d, md = _dossie(caso_id)
    return arq.guardar(d, md, impressao=impressao, origem="teste"), d, md


# --------------------------------------------------------------------------- #
# 1. Nome de gente
# --------------------------------------------------------------------------- #


def test_aprovar_sem_nome_recusa(arquivo: Arquivo) -> None:
    r, _, _ = _guarda(arquivo)
    for nome in ("", "   ", "ok"):
        with pytest.raises(GateViolado, match="nome"):
            aprovar(arquivo, r.chave, por=nome)


def test_aprovar_com_nome_grava_quem_e_quando(arquivo: Arquivo) -> None:
    r, d, _ = _guarda(arquivo)
    assinado = aprovar(arquivo, r.chave, por="  Maria Contadora  ")
    assert assinado.estado is EstadoDossie.APROVADO
    assert assinado.aprovado_por == "Maria Contadora"
    assert assinado.aprovado_em is not None
    assert arquivo.localizar(r.impressao).assinado


def test_devolver_exige_motivo(arquivo: Arquivo) -> None:
    """Devolucao sem motivo nao ensina nada a competencia seguinte."""
    r, _, _ = _guarda(arquivo)
    with pytest.raises(GateViolado, match="motivo"):
        devolver(arquivo, r.chave, por="Maria Contadora", motivo="   ")


# --------------------------------------------------------------------------- #
# 2. Os bytes tem de conferir
# --------------------------------------------------------------------------- #


def test_dossie_adulterado_no_disco_nao_pode_ser_assinado(arquivo: Arquivo) -> None:
    """A trava que da valor probatorio ao documento — provada com a adulteracao plantada.

    Sem ela, "aprovado por Maria" seria uma afirmacao sobre um texto que ninguem sabe
    qual era: bastaria trocar o arquivo depois de guardado.
    """
    from abba_crews.core.cofre import cifrar

    r, _, _ = _guarda(arquivo)
    arquivo.caminho_markdown(r).write_text(
        cifrar("# outro documento inteiramente", SENHA), encoding="utf-8"
    )

    with pytest.raises(ConteudoDivergente, match="sha256"):
        aprovar(arquivo, r.chave, por="Maria Contadora")
    assert arquivo.localizar(r.impressao).estado is EstadoDossie.RASCUNHO


def test_sha256_indexado_e_o_do_markdown(arquivo: Arquivo) -> None:
    r, _, md = _guarda(arquivo)
    assert r.sha256 == sha256_de(md)
    assert arquivo.markdown(r) == md


# --------------------------------------------------------------------------- #
# 3. Para a frente e so para a frente
# --------------------------------------------------------------------------- #


def test_nao_se_assina_duas_vezes(arquivo: Arquivo) -> None:
    r, d, _ = _guarda(arquivo)
    aprovar(arquivo, r.chave, por="Maria Contadora")
    with pytest.raises(GateViolado, match="ja foi assinado"):
        aprovar(arquivo, r.chave, por="Outro Nome")


def test_assinado_nao_volta_a_rascunho(arquivo: Arquivo) -> None:
    r, d, _ = _guarda(arquivo)
    aprovar(arquivo, r.chave, por="Maria Contadora")
    with pytest.raises(GateViolado, match="ja foi assinado"):
        devolver(arquivo, r.chave, por="Maria Contadora", motivo="mudei de ideia")


def test_devolvido_tambem_e_terminal(arquivo: Arquivo) -> None:
    r, d, _ = _guarda(arquivo)
    devolver(arquivo, r.chave, por="Maria Contadora", motivo="faltou a nota 42")
    with pytest.raises(GateViolado, match="devolvido"):
        aprovar(arquivo, r.chave, por="Maria Contadora")


def test_reexecutar_nao_reescreve_o_que_foi_assinado(arquivo: Arquivo) -> None:
    """Supersessao, nunca deleção: o registro assinado nao pode ser rebaixado por um rerun."""
    r, d, md = _guarda(arquivo)
    aprovar(arquivo, r.chave, por="Maria Contadora")
    de_novo = arquivo.guardar(d, md, impressao=r.impressao, origem="teste")
    assert de_novo.estado is EstadoDossie.APROVADO
    assert de_novo.aprovado_por == "Maria Contadora"


def test_entradas_diferentes_geram_registro_ao_lado(arquivo: Arquivo) -> None:
    _guarda(arquivo, impressao="aaaa1111")
    _guarda(arquivo, caso_id="positivo-debito-omitido-desfavoravel", impressao="bbbb2222")
    assert len(arquivo.listar()) == 2


# --------------------------------------------------------------------------- #
# 4. A via assinada
# --------------------------------------------------------------------------- #


def test_via_assinada_diz_quem_quando_e_sobre_o_que(arquivo: Arquivo) -> None:
    r, d, _ = _guarda(arquivo)
    assinado = aprovar(arquivo, r.chave, por="Maria Contadora")
    via = arquivo.markdown(assinado, assinado=True)
    assert "# APROVADO" in via
    assert "Maria Contadora" in via
    assert f"sha256:{r.sha256}" in via


def test_via_assinada_deixa_claro_que_aprovar_nao_e_transmitir(arquivo: Arquivo) -> None:
    """Sem esta frase, APROVADO pode ser lido como 'enviado ao Fisco'.

    Num produto fiscal a confusao custa a janela inteira: o contribuinte acharia que a
    manifestacao foi feita, o prazo passaria, e o silencio consolidaria a proposta.
    """
    r, d, _ = _guarda(arquivo)
    assinado = aprovar(arquivo, r.chave, por="Maria Contadora")
    via = arquivo.markdown(assinado, assinado=True)
    assert "Aprovar nao e transmitir" in via
    assert "ato do contribuinte" in via


def test_o_rascunho_nao_muda_quando_a_via_assinada_nasce(arquivo: Arquivo) -> None:
    r, d, md = _guarda(arquivo)
    assinado = aprovar(arquivo, r.chave, por="Maria Contadora")
    assert arquivo.markdown(assinado) == md, "o rascunho conferido e imutavel"


# --------------------------------------------------------------------------- #
# 5. O disco
# --------------------------------------------------------------------------- #


def test_sem_senha_recusa_gravar_em_vez_de_gravar_em_claro(
    arquivo: Arquivo, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A decisao do socio, travada: nada de degradacao silenciosa para texto claro."""
    monkeypatch.delenv("ABBA_DB_PASSPHRASE", raising=False)
    d, md = _dossie()
    with pytest.raises(SenhaAusente, match="ABBA_DB_PASSPHRASE"):
        arquivo.guardar(d, md, impressao="cccc3333")
    assert arquivo.listar() == (), "nao pode ter sobrado arquivo nenhum"


def test_o_que_esta_no_disco_esta_cifrado(arquivo: Arquivo) -> None:
    r, _, _ = _guarda(arquivo)
    bruto = arquivo.caminho_markdown(r).read_text(encoding="utf-8")
    assert bruto.startswith(MAGIC)
    assert CNPJ_EMPRESA not in bruto
    assert decifrar(bruto, SENHA).startswith("# RASCUNHO")


def test_o_indice_nao_carrega_valor_nem_chave_de_acesso(arquivo: Arquivo) -> None:
    """O meta.json fica em claro; entao ele so pode ter o que ja se sabe de fora."""
    r, _, _ = _guarda(arquivo)
    meta = json.loads(
        (arquivo.raiz / r.cnpj / r.competencia / f"{r.impressao}.meta.json").read_text(
            encoding="utf-8"
        )
    )
    texto = json.dumps(meta)
    assert "R$" not in texto
    assert "0" * 44 not in texto, "chave de acesso de documento nao entra no indice"
    assert set(meta) >= {"chave", "sha256", "estado", "responsavel"}


def test_raiz_dentro_de_arvore_git_e_recusada(tmp_path: Path) -> None:
    """Dado de cliente a um `git add -A` de distancia e acidente esperando acontecer."""
    (tmp_path / ".git").mkdir()
    with pytest.raises(RaizInsegura, match="git"):
        Arquivo(tmp_path / "dossies")


def test_localizar_por_prefixo_e_por_chave(arquivo: Arquivo) -> None:
    r, _, _ = _guarda(arquivo)
    assert arquivo.localizar(r.chave).chave == r.chave
    assert arquivo.localizar(r.impressao[:4]).chave == r.chave


def test_referencia_desconhecida_e_ambigua_falham_com_mensagem_util(
    arquivo: Arquivo,
) -> None:
    _guarda(arquivo, impressao="aaaa1111")
    with pytest.raises(DossieNaoEncontrado, match="dossies"):
        arquivo.localizar("zzzz")

    _guarda(arquivo, caso_id="positivo-debito-omitido-desfavoravel", impressao="aaaa2222")
    with pytest.raises(ReferenciaAmbigua, match="mais de um"):
        arquivo.localizar("aaaa")


def test_listar_filtra_por_cnpj_competencia_e_estado(arquivo: Arquivo) -> None:
    r, d, _ = _guarda(arquivo, impressao="aaaa1111")
    _guarda(arquivo, caso_id="positivo-debito-omitido-desfavoravel", impressao="bbbb2222")
    aprovar(arquivo, r.chave, por="Maria Contadora")

    assert len(arquivo.listar(estado=EstadoDossie.APROVADO)) == 1
    assert len(arquivo.listar(estado=EstadoDossie.RASCUNHO)) == 1
    assert len(arquivo.listar(cnpj="00.000.000/0001-91")) == 2
    assert arquivo.listar(competencia="2099-01") == ()


def test_devolvido_continua_visivel_na_listagem(arquivo: Arquivo) -> None:
    """Esconder o recusado seria perder o unico sinal de onde a conferencia erra."""
    r, _, _ = _guarda(arquivo)
    devolver(arquivo, r.chave, por="Maria Contadora", motivo="faltou a nota 42")
    devolvidos = arquivo.listar(estado=EstadoDossie.DEVOLVIDO)
    assert len(devolvidos) == 1
    assert "faltou a nota 42" in devolvidos[0].resumo()


# --------------------------------------------------------------------------- #
# 6. A via assinada vem dos BYTES conferidos — nao de um re-render
# --------------------------------------------------------------------------- #


def test_o_corpo_assinado_e_literalmente_o_rascunho(arquivo: Arquivo) -> None:
    """A trava contra a fresta que este marco quase deixou aberta.

    A primeira versao re-renderizava o dossie a partir do objeto e so entao carimbava a
    assinatura. Isso reabria o buraco que o sha256 existe para tapar: o documento
    assinado poderia divergir do conferido, e o hash apontaria para um texto que
    ninguem leu. Aqui o corpo tem de ser byte a byte o rascunho.
    """
    from abba_crews.core.dossie import MARCA_RODAPE_RASCUNHO

    r, _, md = _guarda(arquivo)
    assinado = aprovar(arquivo, r.chave, por="Maria Contadora")
    via = arquivo.markdown(assinado, assinado=True)

    corpo_rascunho = md.split("\n")[1 : md.split("\n").index(
        next(x for x in md.split("\n") if x.startswith(MARCA_RODAPE_RASCUNHO))
    )]
    assert via.split("\n")[1 : 1 + len(corpo_rascunho)] == corpo_rascunho


def test_a_via_assinada_nao_fala_mais_em_rascunho(arquivo: Arquivo) -> None:
    from abba_crews.core.dossie import MARCA_RODAPE_RASCUNHO

    r, _, _ = _guarda(arquivo)
    assinado = aprovar(arquivo, r.chave, por="Maria Contadora")
    via = arquivo.markdown(assinado, assinado=True)
    assert MARCA_RODAPE_RASCUNHO not in via
    assert via.startswith("# APROVADO")


def test_rascunho_sem_o_marcador_recusa_virar_via_assinada() -> None:
    """Se o rodape de core/dossie.py mudar, isto quebra — que e o objetivo."""
    from datetime import UTC, datetime

    from abba_crews.core.aprovacao import RodapeAusente, via_assinada
    from abba_crews.core.dossie import Assinatura

    a = Assinatura(por="Maria", em=datetime.now(UTC), sha256="a" * 64)
    with pytest.raises(RodapeAusente, match="MARCA_RODAPE_RASCUNHO"):
        via_assinada("# RASCUNHO — algo\n\ncorpo sem rodape\n", a)
    with pytest.raises(RodapeAusente, match="cabecalho"):
        via_assinada("sem cabecalho nenhum", a)


# --------------------------------------------------------------------------- #
# 7. Achados do review de 2026-09-02
# --------------------------------------------------------------------------- #


def test_o_disco_fica_so_para_o_dono(arquivo: Arquivo) -> None:
    """Cifrar e deixar legivel por qualquer usuario protege o conteudo e entrega o resto.

    A doutrina do `assessment-brain` e "perms + encryption" (cabecalho do
    `report-crypto.js`; o `config.js` avisa sobre arquivo group/other-readable). Ate
    2026-09-02 tinhamos feito so a cifra, e o disco saia `0644`/`0755` — os diretorios,
    nomeados por CNPJ, eram a carteira de clientes em texto claro.
    """
    r, _, _ = _guarda(arquivo)
    for caminho in (arquivo.caminho_markdown(r), arquivo.raiz / r.cnpj):
        modo = caminho.stat().st_mode & 0o777
        assert not modo & 0o077, f"{caminho} esta acessivel a outros: {modo:o}"


def test_o_indice_em_claro_nao_diz_que_o_cliente_perdeu_o_prazo(arquivo: Arquivo) -> None:
    """`natureza: registro_de_perda` em claro e a frase "este cliente perdeu o prazo"."""
    r, _, _ = _guarda(arquivo)
    bruto = (arquivo.raiz / r.cnpj / r.competencia / f"{r.impressao}.meta.json").read_text(
        encoding="utf-8"
    )
    assert "natureza" not in bruto
    assert "registro_de_perda" not in bruto
