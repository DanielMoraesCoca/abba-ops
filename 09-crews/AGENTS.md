# Regras da casa — `abba-crews`

Leia antes de escrever código aqui. São poucas e todas têm consequência.

## 1. `core/` não importa `crewai`

`core/` guarda o reconciliador, a tabela de vedações e o calendário fiscal — o que vale
dinheiro e o que menos muda. A CrewAI é um framework jovem que já trocou de scaffold uma vez.

Se precisar de lógica nova numa crew: escreva em `core/` (Python puro, testado) e exponha
por uma `BaseTool` fina em `tools/`. `scripts/audita_fronteira.py` reprova o build se
alguém quebrar isso — e há um teste que planta uma violação para provar que a trava funciona.

## 2. Nenhum número nasce em LLM

Aritmética fiscal e de caixa é código determinístico com teste unitário. O modelo classifica
o que é ambíguo e redige o que é texto; ele nunca soma, nunca calcula imposto, nunca decide
valor. Um LLM que soma errado é passivo, não recurso.

## 3. O produto nunca transmite ao Fisco

Não existe ferramenta de transmissão neste projeto, e não deve passar a existir. A crew
evidencia; o contador do cliente conclui, assina e transmite. Isso inclui a manifestação
do destinatário na Distribuição DF-e — é ato do contribuinte.

Corolário: nada de linguagem de parecer no texto gerado ("é devido", "faz jus a").

## 4. A maturidade do produto é declarada, não presumida

`core/produtos/registry.py` diz o que existe e em que estado. Para promover um produto,
cumpra o `gate` declarado e mude o registry **no mesmo commit** que entrega o gate.
Os testes reprovam promoção sem os campos que a promoção exige.

Se você está prestes a demonstrar algo a um cliente, rode `abba-crews produtos` primeiro.

## 5. Segredo nunca entra no repositório

Certificado digital A1, credencial da Plataforma RTC, chave de API. `.gitignore` bloqueia
as extensões e a CI reprova se alguma for rastreada. Se um segredo vazar num commit, o
caminho é rotacionar a credencial, não só remover o arquivo.

## 6. Comentário explica *por quê*, não *o quê*

O código já diz o que faz. Comentário bom registra a decisão, a restrição legal ou o bug
que a linha evita — como os que já estão em `audita_fronteira.py` e no registry.

## 7. Português no domínio, inglês onde a ferramenta exige

Nomes de domínio (`Divergencia`, `competencia`, `creditabilidade`) em português: é a língua
em que o contador pensa e em que a lei está escrita. O que a CrewAI exige (`kickoff`,
`agents.yaml`, `role`/`goal`/`backstory`) fica como ela espera. Sem acento em identificador.

## Verificação antes de qualquer commit

```bash
uv run python scripts/audita_fronteira.py && uv run ruff check . && uv run mypy && uv run pytest -q
```
