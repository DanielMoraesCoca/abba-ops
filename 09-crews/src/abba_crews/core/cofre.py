"""Cifra em repouso — o mesmo formato que o `assessment-brain` ja usa.

Este marco e a primeira vez que o `abba-crews` grava dado fiscal de cliente em disco:
CNPJ, chaves de acesso de 44 digitos, valores. A decisao do socio (2026-09-02) foi
gravar **fora da arvore do repositorio e cifrado**, e sem senha **recusar gravar** em
vez de degradar para texto claro. A falha alta e o desenho, nao efeito colateral.

## Por que reproduzir o formato do brain em vez de inventar um

O `assessment-brain` ja cifra relatorios em repouso (`src/core/report-crypto.js`). Usar
o mesmo envelope tem tres ganhos concretos e nenhum custo:

- um arquivo escrito aqui e **legivel la**, e vice-versa — uma casa, um formato;
- a mesma variavel de ambiente (`ABBA_DB_PASSPHRASE`) — uma senha, nao duas;
- o dia em que o `abba forget` precisar alcancar os dossies, ele ja sabe ler.

O `readPossiblyEncrypted` do lado JS **nao** tem equivalente aqui, e isso e deliberado:
ele existe no brain porque o brain tem relatorio antigo em claro. Este projeto **nunca
grava em claro** — sem senha ele recusa —, entao espelhar a funcao so pela simetria
seria superficie declarada sem dono.

    "ABBA-ENC-1\\n" + base64( salt[16] | iv[12] | tag[16] | ciphertext ) + "\\n"
    AES-256-GCM · chave scrypt (N=16384, r=8, p=1, dklen=32)

Os parametros do scrypt sao os padroes do `crypto.scryptSync` do Node — e por isso que
os dois lados se entendem byte a byte. Mudar qualquer um deles quebra a interoperacao;
`tests/unit/test_cofre.py` prova a compatibilidade chamando o `node` de verdade.

## GCM autentica, e isso importa mais aqui do que a cifra

Senha errada ou arquivo adulterado **falham alto**. Num dossie fiscal isso vale mais que
o sigilo: decifrar em silencio um arquivo modificado significaria um contador assinando
numeros que nao sao os que ele conferiu.
"""

from __future__ import annotations

import base64
import hashlib
import os
import secrets

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MAGIC = "ABBA-ENC-1"
"""Primeira linha do arquivo cifrado. Igual a do `assessment-brain`."""

VARIAVEL_SENHA = "ABBA_DB_PASSPHRASE"
"""A mesma do brain. Uma casa, uma senha."""

_SAL = 16
_IV = 12
_TAG = 16
# Padroes do crypto.scryptSync do Node. Mudar aqui quebra a leitura no lado JS.
_N, _R, _P, _DK = 16384, 8, 1, 32
_MAXMEM = 64 * 1024 * 1024


class SenhaAusente(RuntimeError):
    """Nao ha senha para cifrar. O caminho certo e recusar, nunca gravar em claro."""


class ConteudoAdulterado(ValueError):
    """A autenticacao do GCM falhou: senha errada ou bytes alterados."""


def _chave(senha: str, sal: bytes) -> bytes:
    return hashlib.scrypt(
        senha.encode("utf-8"), salt=sal, n=_N, r=_R, p=_P, dklen=_DK, maxmem=_MAXMEM
    )


def esta_cifrado(conteudo: str) -> bool:
    return isinstance(conteudo, str) and conteudo.startswith(MAGIC)


def cifrar(texto: str, senha: str) -> str:
    """Cifra um texto no envelope ABBA-ENC-1."""
    if not senha:
        raise SenhaAusente("senha vazia: cifrar com senha vazia e nao cifrar")
    sal = secrets.token_bytes(_SAL)
    iv = secrets.token_bytes(_IV)
    selado = AESGCM(_chave(senha, sal)).encrypt(iv, texto.encode("utf-8"), None)
    # O AESGCM do `cryptography` devolve ciphertext||tag; o Node guarda tag antes do
    # ciphertext. Reordenar aqui e o que faz os dois lados lerem o mesmo arquivo.
    corpo, tag = selado[:-_TAG], selado[-_TAG:]
    return MAGIC + "\n" + base64.b64encode(sal + iv + tag + corpo).decode("ascii") + "\n"


def decifrar(blob: str, senha: str) -> str:
    """Decifra um envelope ABBA-ENC-1. Falha alto se a senha ou os bytes nao baterem."""
    if not esta_cifrado(blob):
        raise ValueError("conteudo nao esta no envelope ABBA-ENC-1")
    if not senha:
        raise SenhaAusente(
            f"sem senha para decifrar. Defina {VARIAVEL_SENHA} com a mesma senha usada "
            f"para gravar."
        )
    try:
        bruto = base64.b64decode(blob[len(MAGIC) :].strip(), validate=True)
    except Exception as e:
        raise ConteudoAdulterado(f"envelope ABBA-ENC-1 ilegivel: {e}") from e
    if len(bruto) < _SAL + _IV + _TAG:
        raise ConteudoAdulterado("envelope ABBA-ENC-1 truncado")

    sal = bruto[:_SAL]
    iv = bruto[_SAL : _SAL + _IV]
    tag = bruto[_SAL + _IV : _SAL + _IV + _TAG]
    corpo = bruto[_SAL + _IV + _TAG :]
    try:
        aberto = AESGCM(_chave(senha, sal)).decrypt(iv, corpo + tag, None)
    except Exception as e:
        raise ConteudoAdulterado(
            "falha ao autenticar o conteudo: senha errada ou arquivo alterado. "
            "Nao ha degradacao silenciosa aqui de proposito — decifrar em silencio um "
            "dossie modificado seria entregar a um contador numeros que ele nao conferiu."
        ) from e
    return aberto.decode("utf-8")


def senha_do_ambiente() -> str | None:
    """A senha configurada, ou `None`. Quem decide o que fazer sem ela e o chamador."""
    senha = os.environ.get(VARIAVEL_SENHA, "").strip()
    return senha or None


def senha_obrigatoria() -> str:
    """A senha, ou uma recusa explicando o que fazer."""
    senha = senha_do_ambiente()
    if not senha:
        raise SenhaAusente(
            f"{VARIAVEL_SENHA} nao esta definida e este projeto nao grava dado fiscal "
            f"de cliente em claro. Defina a variavel com a mesma senha do "
            f"assessment-brain — os dois lados leem o mesmo envelope."
        )
    return senha
