# abba-crews — a Camada de Caixa da reforma tributária

Biblioteca de crews da ABBA para a **apuração assistida** de IBS/CBS. Sete produtos,
um núcleo determinístico e um caminho de deploy que é conectar o repositório, não portar.

> **Este projeto está em staging dentro de `abba-ops/09-crews/`.** Ele nasceu aqui porque
> o app do GitHub desta sessão não tem permissão para criar repositórios. Ver
> [`STAGING.md`](STAGING.md) para extrair para o repositório definitivo.

---

## O que ele faz

Em 2027 o Fisco passa a entregar a apuração de IBS/CBS **pré-preenchida**. Se a empresa
não se manifestar até o dia 15 (dia 20 para quem entrega DeRE), **os valores propostos
prevalecem e o crédito tributário é constituído automaticamente**. Silêncio é aceite.

A Sentinela da Apuração confere a proposta do Fisco contra os documentos da própria
empresa, acha crédito legítimo omitido, e monta o dossiê de manifestação para o
**contador do cliente assinar**. Ela nunca transmite nada ao Fisco.

Estratégia completa: [`../05-interno/plano-camada-de-caixa-2027.md`](../05-interno/plano-camada-de-caixa-2027.md).

## Estado real dos produtos

```bash
uv run abba-crews produtos --detalhe
```

Nenhum produto está em `PRODUCAO` hoje. O comando acima diz a verdade sobre cada um,
e os testes impedem que alguém promova um produto sem cumprir o gate declarado.

## Como rodar

```bash
uv sync --extra dev
uv run pytest -q                            # testes
uv run ruff check .                         # lint
uv run mypy                                 # tipos, estrito em core/
uv run python scripts/audita_fronteira.py   # a trava de portabilidade
uv run abba-crews produtos                  # o estado honesto
```

## As duas regras que estruturam o código

**1. Determinístico onde há dinheiro e prazo; agêntico só onde há julgamento.**
Aritmética fiscal vive em `core/`, em Python testado. Nenhum número nasce em LLM.
A crew só entra para derrubar achados duvidosos e redigir o dossiê.

**2. `core/` não importa `crewai` — e a CI prova.**
O núcleo (reconciliador, tabela de vedações, calendário fiscal) é o ativo que vale
dinheiro e o que menos muda. A CrewAI é um framework jovem que já trocou de scaffold.
`scripts/audita_fronteira.py` reprova o build se alguém quebrar a fronteira.

## Layout

```
src/abba_crews/
  core/            # ZERO crewai. Pydantic, parsers, reconciliação, régua.
    produtos/      # o registro dos 7 produtos e suas maturidades
  crews/           # crews CrewAI (convenção de projeto Flow)
  flows/           # orquestração determinística
  tools/           # BaseTool finos por cima de core/ — sem lógica
  main.py          # kickoff/plot/run_with_trigger — convenção da CrewAI
  cli.py           # CLI de operação dos sócios
scripts/           # auditoria de fronteira, geradores
tests/             # unit + golden
```

## Fronteira — onde o produto para

- **Nenhuma crew transmite ao Fisco.** Não existe ferramenta de transmissão no projeto.
- **Nenhum parecer tributário gerado por LLM.** A crew evidencia; o contador conclui e assina.
- **Sem 100% por resultado.**
- Tudo que este projeto escreve no cérebro tem origem `tool_output` — nunca sobrepõe
  o que um humano afirmou.

## Segredos

Certificado digital A1 e credenciais da Plataforma RTC **nunca** entram no repositório.
`.gitignore` bloqueia `*.p12`, `*.pfx`, `*.pem`, `*.key`; a CI reprova se algum for rastreado.
Ver `.env.example` para os nomes das variáveis.

Telemetria da CrewAI vem desligada por padrão (`CREWAI_TELEMETRY_OPT_OUT=true`) — este
projeto toca dado fiscal de cliente.
