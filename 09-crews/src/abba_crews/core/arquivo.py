"""O armazem de dossies — a primeira vez que este projeto grava um byte.

Ate o M4a o Flow montava o markdown na memoria e **jogava fora**. Nao havia registro do
que foi conferido, nao havia artefato para o contador olhar, e nao havia o que aprovar.
A docstring do Flow prometia `submeter_a_humano -> grava e ENCERRA` e o metodo nunca
existiu. Este modulo e a metade que faltava.

## Onde as coisas caem, e por que ai

Raiz por `ABBA_CREWS_DOSSIES`, padrao `~/.abba-crews/dossies/`:

    <raiz>/<cnpj>/<competencia>/<impressao>.md.enc           rascunho, cifrado
    <raiz>/<cnpj>/<competencia>/<impressao>.aprovado.md.enc  via assinada, congelada
    <raiz>/<cnpj>/<competencia>/<impressao>.meta.json        estado, sha256, quem, quando

O nome do arquivo e a **impressao das entradas** — o mesmo hash que ja da idempotencia
ao Flow. Entradas iguais, mesmo arquivo; entradas diferentes, arquivo novo **ao lado**.
Nada e sobrescrito e nada e apagado: e a supersessao do cerebro, aplicada a documento.

## Duas recusas que sao o desenho

**Sem senha, nao grava.** Decisao do socio (2026-09-02): dado fiscal de cliente nao vai
para o disco em claro. Sem `ABBA_DB_PASSPHRASE`, o comando falha alto.

**Dentro de arvore git, nao grava.** Se qualquer ancestral do destino tiver `.git`, a
raiz e recusada. Dado de cliente a um `git add -A` de distancia e acidente esperando
acontecer — e a defesa contra ele nao pode ser a memoria de quem digita.

**Permissao restrita.** `0700` nos diretorios, `0600` nos arquivos. A doutrina do
`assessment-brain` e "perms + encryption" (cabecalho do `report-crypto.js`; o
`config.js` avisa sobre arquivo group/other-readable) e ate 2026-09-02 tinhamos feito so
a cifra: `0644`/`0755`. Cifrar e deixar legivel por qualquer usuario da maquina protege
o conteudo e entrega o resto — os diretorios, nomeados por CNPJ, sao a carteira de
clientes em texto claro.

O `meta.json` fica em claro porque e o indice, e por isso guarda o **minimo**: chave,
hash, estado, quem assinou e quando. Nao guarda valor, nem chave de acesso, nem detalhe
de divergencia — e desde 2026-09-02 tambem nao guarda a `natureza`, porque
`registro_de_perda` em claro e a frase "este cliente perdeu o prazo".
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
from datetime import UTC, datetime
from pathlib import Path

from pydantic import BaseModel, Field

from abba_crews.core.cofre import (
    decifrar,
    senha_do_ambiente,
    senha_obrigatoria,
)
from abba_crews.core.dossie import Dossie, EstadoDossie

VARIAVEL_RAIZ = "ABBA_CREWS_DOSSIES"
RAIZ_PADRAO = Path.home() / ".abba-crews" / "dossies"


class RaizInsegura(RuntimeError):
    """A raiz escolhida esta dentro de uma arvore git. Recusado."""


class DossieNaoEncontrado(KeyError):
    pass


class ReferenciaAmbigua(KeyError):
    pass


def agora() -> datetime:
    """UTC, sempre. Prazo fiscal com fuso implicito e prazo errado esperando acontecer."""
    return datetime.now(UTC)


def sha256_de(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


class RegistroDossie(BaseModel):
    """O indice de um dossie guardado. Nao carrega valor nem chave de acesso."""

    model_config = {"frozen": True}

    chave: str = Field(description="cnpj:competencia:impressao — a chave de execucao")
    cnpj: str
    competencia: str
    impressao: str = Field(description="hash das entradas; e o nome do arquivo")
    sha256: str = Field(min_length=64, max_length=64, description="hash do markdown")
    estado: EstadoDossie = EstadoDossie.RASCUNHO
    responsavel: str = Field(description="quem deveria assinar, segundo a config")
    origem: str = "desconhecida"
    guardado_em: datetime

    aprovado_por: str | None = None
    aprovado_em: datetime | None = None
    devolvido_por: str | None = None
    devolvido_em: datetime | None = None
    motivo: str | None = None

    @property
    def assinado(self) -> bool:
        return self.estado is EstadoDossie.APROVADO

    def resumo(self) -> str:
        if self.estado is EstadoDossie.APROVADO and self.aprovado_em:
            quem = f"assinado por {self.aprovado_por} em {self.aprovado_em:%d/%m/%Y %H:%M}"
        elif self.estado is EstadoDossie.DEVOLVIDO and self.devolvido_em:
            quem = f"devolvido por {self.devolvido_por}: {self.motivo}"
        else:
            quem = f"aguardando {self.responsavel}"
        return f"{self.estado.value:<9} {self.chave}  ({quem})"


def _dentro_de_arvore_git(caminho: Path) -> Path | None:
    """Devolve o diretorio com `.git` que contem o caminho, se houver."""
    for pai in [caminho, *caminho.parents]:
        if (pai / ".git").exists():
            return pai
    return None


MODO_DIR = 0o700
MODO_ARQ = 0o600


class Arquivo:
    """O armazem. Instanciar ja valida a raiz — falhar tarde aqui seria falhar no disco."""

    def __init__(self, raiz: Path | None = None) -> None:
        self.raiz = Path(raiz) if raiz is not None else raiz_padrao()
        repo = _dentro_de_arvore_git(self.raiz.expanduser())
        if repo is not None:
            raise RaizInsegura(
                f"{self.raiz} esta dentro da arvore git em {repo}. Este projeto nao "
                f"grava dossie de cliente onde um `git add -A` alcanca. Aponte "
                f"{VARIAVEL_RAIZ} para fora do repositorio."
            )
        self.raiz = self.raiz.expanduser()

    # ------------------------------------------------------------------ caminhos
    def _pasta(self, cnpj: str, competencia: str) -> Path:
        return self.raiz / cnpj / competencia

    def _meta(self, r: RegistroDossie) -> Path:
        return self._pasta(r.cnpj, r.competencia) / f"{r.impressao}.meta.json"

    def caminho_markdown(self, r: RegistroDossie) -> Path:
        return self._pasta(r.cnpj, r.competencia) / f"{r.impressao}.md.enc"

    def caminho_assinado(self, r: RegistroDossie) -> Path:
        return self._pasta(r.cnpj, r.competencia) / f"{r.impressao}.aprovado.md.enc"

    # ------------------------------------------------------------------ escrita
    def guardar(
        self, dossie: Dossie, markdown: str, *, impressao: str, origem: str = "desconhecida"
    ) -> RegistroDossie:
        """Grava o rascunho cifrado e o seu indice. Sem senha, recusa."""
        from abba_crews.core.cofre import cifrar

        senha = senha_obrigatoria()
        registro = RegistroDossie(
            chave=f"{dossie.cnpj}:{dossie.competencia}:{impressao}",
            cnpj=dossie.cnpj,
            competencia=dossie.competencia,
            impressao=impressao,
            sha256=sha256_de(markdown),
            estado=EstadoDossie.RASCUNHO,
            responsavel=dossie.responsavel,
            origem=origem,
            guardado_em=agora(),
        )

        existente = self._ler_meta_se_houver(registro)
        if existente is not None and existente.estado.terminal:
            # Mesmas entradas, dossie ja julgado: nao se reescreve o que foi assinado.
            return existente

        self._preparar(registro)
        self._escrever(self.caminho_markdown(registro), cifrar(markdown, senha))
        self._gravar_meta(registro)
        return registro

    def _preparar(self, r: RegistroDossie) -> None:
        """Cria a arvore com `0700`, incluindo os niveis intermediarios."""
        pasta = self._pasta(r.cnpj, r.competencia)
        pasta.mkdir(parents=True, exist_ok=True, mode=MODO_DIR)
        # `mkdir(parents=True)` nao aplica o modo aos pais ja existentes nem, em algumas
        # plataformas, aos criados — entao reforcamos nivel a nivel.
        for nivel in (self.raiz, pasta.parent, pasta):
            with contextlib.suppress(OSError):
                nivel.chmod(MODO_DIR)

    @staticmethod
    def _escrever(destino: Path, conteudo: str) -> None:
        """Grava com `0600` **antes** de escrever — nada de janela world-readable."""
        fd = os.open(destino, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, MODO_ARQ)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(conteudo)
        with contextlib.suppress(OSError):
            destino.chmod(MODO_ARQ)

    def _gravar_meta(self, r: RegistroDossie) -> None:
        self._preparar(r)
        self._escrever(
            self._meta(r),
            json.dumps(r.model_dump(mode="json"), ensure_ascii=False, indent=2) + "\n",
        )

    def atualizar(self, r: RegistroDossie) -> RegistroDossie:
        """Regrava o indice. O markdown do rascunho nunca muda — so o estado muda."""
        self._gravar_meta(r)
        return r

    def gravar_via_assinada(self, r: RegistroDossie, markdown: str) -> Path:
        from abba_crews.core.cofre import cifrar

        destino = self.caminho_assinado(r)
        self._preparar(r)
        self._escrever(destino, cifrar(markdown, senha_obrigatoria()))
        return destino

    # ------------------------------------------------------------------ leitura
    def _ler_meta_se_houver(self, r: RegistroDossie) -> RegistroDossie | None:
        caminho = self._meta(r)
        if not caminho.exists():
            return None
        return RegistroDossie.model_validate_json(caminho.read_text(encoding="utf-8"))

    def listar(
        self,
        *,
        cnpj: str | None = None,
        competencia: str | None = None,
        estado: EstadoDossie | None = None,
    ) -> tuple[RegistroDossie, ...]:
        """Todos os registros, mais recentes primeiro. Nada e escondido — nem o devolvido."""
        if not self.raiz.exists():
            return ()
        achados = []
        for meta in sorted(self.raiz.glob("*/*/*.meta.json")):
            r = RegistroDossie.model_validate_json(meta.read_text(encoding="utf-8"))
            if cnpj and r.cnpj != "".join(c for c in cnpj if c.isdigit()):
                continue
            if competencia and r.competencia != competencia:
                continue
            if estado and r.estado is not estado:
                continue
            achados.append(r)
        return tuple(sorted(achados, key=lambda r: r.guardado_em, reverse=True))

    def localizar(self, referencia: str) -> RegistroDossie:
        """Acha por chave inteira ou por prefixo da impressao — a CLI e digitada por gente."""
        ref = referencia.strip()
        candidatos = [
            r for r in self.listar() if r.chave == ref or r.impressao.startswith(ref)
        ]
        if not candidatos:
            raise DossieNaoEncontrado(
                f"nenhum dossie para {ref!r} em {self.raiz}. "
                f"Use `abba-crews dossies` para ver o que existe."
            )
        if len(candidatos) > 1:
            chaves = "\n  ".join(r.chave for r in candidatos)
            raise ReferenciaAmbigua(f"{ref!r} casa com mais de um dossie:\n  {chaves}")
        return candidatos[0]

    def markdown(self, r: RegistroDossie, *, assinado: bool = False) -> str:
        """Le e decifra. Senha errada falha alto — nunca devolve lixo."""
        caminho = self.caminho_assinado(r) if assinado else self.caminho_markdown(r)
        if not caminho.exists():
            raise DossieNaoEncontrado(f"arquivo ausente: {caminho}")
        return decifrar(caminho.read_text(encoding="utf-8"), senha_do_ambiente() or "")


def raiz_padrao() -> Path:
    bruto = os.environ.get(VARIAVEL_RAIZ, "").strip()
    return Path(bruto) if bruto else RAIZ_PADRAO
