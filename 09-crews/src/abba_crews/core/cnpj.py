"""CNPJ — normalizacao e digito verificador, num lugar so.

Ate 2026-09-03 havia **tres** validadores de CNPJ copiados pelo projeto
(`clientes.ConfigCliente`, `modelos.DocumentoFiscal`, `modelos.ApuracaoFisco`) e os tres
faziam a mesma coisa incompleta: contavam catorze digitos. Isso aceitava
`00000000000192` (um digito trocado), `11111111111111` (sequencia repetida) e qualquer
numero que alguem digitasse errado com o tamanho certo.

## Por que isso importa mais numa carteira do que num cliente

A configuracao de cliente e um YAML **digitado a mao**. Com um cliente, um typo falha
alto: a guarda do M4b rejeita todo documento como sendo de terceiro, e alguem percebe.
Com duzentos clientes, o typo e questao de *quando*, nao de *se* — e o typo que cai
sobre **outro CNPJ valido** nao falha: confere a empresa errada em silencio.

`core/clientes.py` chama exatamente esse cenario de "o pior erro possivel deste produto".
O digito verificador e a defesa barata contra ele: pega todo erro de um digito e toda
transposicao de dois adjacentes, que sao os dois jeitos de errar ao digitar.

## O que este modulo NAO resolve

**CNPJ alfanumerico.** A Receita passou a emitir CNPJ com letras, e a regra de digito do
formato novo nao pode ser conferida deste ambiente (gov.br bloqueado). Implementar regra
fiscal que nao da para verificar e o defeito que este projeto vem combatendo marco apos
marco — entao aqui vale o numerico, e o alfanumerico e a pendencia **P8**, para entrar
com fonte primaria na mao.

Efeito pratico hoje: um CNPJ alfanumerico e recusado por tamanho depois da limpeza
(`normalizar` descarta as letras). Falha alto, que e o desfecho seguro — mas por sorte,
nao por desenho, e a pendencia existe para dizer isso.
"""

from __future__ import annotations

TAMANHO = 14

_PESOS_1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
_PESOS_2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def normalizar(bruto: object) -> str:
    """So os digitos. `00.000.000/0001-91` vira `00000000000191`."""
    return "".join(c for c in str(bruto) if c.isdigit())


def _digito(base: str, pesos: tuple[int, ...]) -> str:
    soma = sum(int(d) * p for d, p in zip(base, pesos, strict=True))
    resto = soma % 11
    return "0" if resto < 2 else str(11 - resto)


def valido(bruto: object) -> bool:
    """`True` se o CNPJ tem 14 digitos e os dois verificadores conferem."""
    limpo = normalizar(bruto)
    if len(limpo) != TAMANHO:
        return False
    # Sequencia repetida passa na aritmetica do modulo 11 e nao existe na vida real.
    # `11111111111111` seria aceito sem esta linha.
    if len(set(limpo)) == 1:
        return False
    d1 = _digito(limpo[:12], _PESOS_1)
    return limpo[12:] == d1 + _digito(limpo[:12] + d1, _PESOS_2)


def exigir(bruto: object, *, campo: str = "CNPJ") -> str:
    """Devolve o CNPJ normalizado ou levanta `ValueError` dizendo o que houve.

    A mensagem separa os dois casos de propósito: "tamanho errado" e "digito nao confere"
    mandam a pessoa olhar coisas diferentes do que ela digitou.
    """
    limpo = normalizar(bruto)
    if len(limpo) != TAMANHO:
        raise ValueError(
            f"{campo} deve ter {TAMANHO} digitos, veio {len(limpo)}: {bruto!r}. "
            f"(CNPJ alfanumerico ainda nao e suportado — ver docs/PENDENCIAS.md, P8.)"
        )
    if not valido(limpo):
        raise ValueError(
            f"{campo} {limpo} tem 14 digitos mas o digito verificador nao confere — "
            f"provavelmente um erro de digitacao. Conferir a apuracao do CNPJ errado e o "
            f"pior erro possivel deste produto, entao ele nao passa daqui."
        )
    return limpo
