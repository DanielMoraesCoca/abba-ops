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

O `meta.json` fica em claro de proposito: ele guarda so o que ja se sabe de fora (CNPJ,
competencia, estado, quem assinou) e nenhum valor, nenhuma chave de acesso, nenhum
detalhe de divergencia. E o indice; o conteudo vive cifrado, sempre.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
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
    return datetime.now(timezone.utc)  # noqa: UP017


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
    natureza: str
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
            natureza=dossie.natureza.value,
            responsavel=dossie.responsavel,
            origem=origem,
            guardado_em=agora(),
        )

        existente = self._ler_meta_se_houver(registro)
        if existente is not None and existente.estado.terminal:
            # Mesmas entradas, dossie ja julgado: nao se reescreve o que foi assinado.
            return existente

        self._pasta(registro.cnpj, registro.competencia).mkdir(parents=True, exist_ok=True)
        self.caminho_markdown(registro).write_text(cifrar(markdown, senha), encoding="utf-8")
        self._gravar_meta(registro)
        return registro

    def _gravar_meta(self, r: RegistroDossie) -> None:
        self._pasta(r.cnpj, r.competencia).mkdir(parents=True, exist_ok=True)
        self._meta(r).write_text(
            json.dumps(r.model_dump(mode="json"), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def atualizar(self, r: RegistroDossie) -> RegistroDossie:
        """Regrava o indice. O markdown do rascunho nunca muda — so o estado muda."""
        self._gravar_meta(r)
        return r

    def gravar_via_assinada(self, r: RegistroDossie, markdown: str) -> Path:
        from abba_crews.core.cofre import cifrar

        destino = self.caminho_assinado(r)
        destino.write_text(cifrar(markdown, senha_obrigatoria()), encoding="utf-8")
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
