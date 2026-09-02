# abba-crews — a Camada de Caixa da reforma tributária

Biblioteca de crews da ABBA para a **apuração assistida** de IBS/CBS. Sete produtos,
um núcleo determinístico e um caminho de deploy que é conectar o repositório, não portar.

> **Este projeto está em staging dentro de `abba-ops/09-crews/`.** Ele nasceu aqui porque
> o app do GitHub desta sessão não tem permissão para criar repositórios. Ver
> [`STAGING.md`](STAGING.md) para extrair para o repositório definitivo.

---

## O que ele faz

Em 2027 o Fisco passa a entregar a apuração de IBS/CBS **pré-preenchida**. A proposta
fica disponível até o **dia 15** (dia 20 para quem entrega DeRE) — essa é a data em que
ela *aparece*, não o prazo. A manifestação vai até o **último dia útil do mês seguinte**;
não havendo resposta, os valores propostos prevalecem e o crédito tributário é
constituído automaticamente — o que **equivale a confissão de dívida** (art. 348, §1º da
LC 214/2025; §4º do art. 125 do ADCT). Silêncio é aceite.

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
uv run abba-crews cobertura                 # quanto a REGRA resolve sem modelo
uv run abba-crews janela -c 2027-03         # disponibilização x prazo final
uv run abba-crews golden                    # o placar do golden set
```

## O gate humano — a IA rascunha, o humano assina

O dossiê nasce `RASCUNHO` e **só sai daí por assinatura de gente com nome**:

```bash
export ABBA_DB_PASSPHRASE=...               # sem ela, o sistema recusa gravar
export ABBA_CREWS_DOSSIES=~/.abba-crews/dossies

uv run abba-crews sentinela ... --guardar   # grava o rascunho, cifrado
uv run abba-crews dossies                   # o estado real de cada um
uv run abba-crews ver      --chave <ref>
uv run abba-crews aprovar  --chave <ref> --por "Maria Contadora"
uv run abba-crews devolver --chave <ref> --por "Maria" --motivo "faltou a nota 42"
```

Quatro regras que são o desenho, não validação decorativa:

- **Nome obrigatório.** Gate humano sem nome é automação com nome de gate: não há quem
  responda, e responder é o ponto inteiro.
- **Os bytes têm de conferir.** `aprovar` recalcula o sha256 do rascunho e compara com o
  índice. Divergiu, recusa — assinar sem isso é assinar em branco. A via assinada é
  derivada dos **bytes conferidos**, nunca re-renderizada do modelo.
- **Não volta atrás.** `APROVADO` e `DEVOLVIDO` são terminais. Conferência nova gera
  dossiê novo **ao lado**, sem apagar o anterior — supersessão, como no cérebro.
- **Aprovar não é transmitir.** A via assinada diz isso no próprio corpo. A manifestação
  ao Fisco continua sendo ato do contribuinte; não existe ferramenta de transmissão aqui.

### Onde o dado fica, e por quê

Dossiê carrega dado fiscal de cliente. Ele é gravado **fora da árvore do repositório** e
**cifrado** no envelope `ABBA-ENC-1` — o mesmo formato do
[`assessment-brain`](../../assessment-brain/src/core/report-crypto.js), de propósito: um
arquivo escrito aqui é legível lá, e a senha é a mesma (`ABBA_DB_PASSPHRASE`). Um teste
chama o `node` de verdade para provar essa interoperabilidade — sem ele, mexer nos
parâmetros do scrypt manteria o round-trip local verde e mataria a interoperação em
silêncio.

Duas recusas, ambas deliberadas: **sem senha não grava** (nada de degradar para texto
claro) e **dentro de árvore git não grava** (dado de cliente a um `git add -A` de
distância é acidente esperando acontecer). A retenção e o caminho de apagamento estão em
aberto — `docs/PENDENCIAS.md`, **P6**.

## Creditabilidade: o que entra no dossiê e o que fica de fora

O reconciliador acha divergência **estrutural** — o que falta na proposta, o que diverge
em valor. Isso não responde à pergunta que o contador faz primeiro: *este crédito é
legítimo?* `core/creditabilidade.py` responde, **por regra e sem LLM**, lendo o par
(`CST`, `cClassTrib`) contra uma tabela versionada com fonte citada por linha.

A regra de segurança que desenha o módulo: **código desconhecido é `DUVIDOSO` — nunca
creditável, nunca vedado.** Presumir creditabilidade de um par que não conhecemos é o
falso positivo fiscal que manda o cliente pleitear o que não é dele.

A tabela (`core/dados/vedacoes.json`) nasce quase vazia, e de propósito: nenhuma linha
foi conferida no Informe Técnico 2025.002 oficial, e direito tributário não se deduz.
Com ela assim, todo crédito vai a `DUVIDOSO` — o estado real do nosso conhecimento.
Preenchê-la é trabalho com um contador (`docs/PENDENCIAS.md`, P2), e `abba-crews
cobertura` mede o avanço.

Por isso a classificação é **opcional e vem desligada**: ligada hoje, mandaria todo
crédito à rota de julgamento, e a crew que julga só chega no M3b.

## As duas regras que estruturam o código

**1. Determinístico onde há dinheiro e prazo; agêntico só onde há julgamento.**
Aritmética fiscal vive em `core/`, em Python testado. Nenhum número nasce em LLM.
A crew entrará para derrubar achados duvidosos e redigir — hoje ela não existe, e o
produto inteiro roda sem uma chamada de modelo.

**2. `core/` não importa `crewai` — e a CI prova.**
O núcleo (reconciliador, tabela de vedações, calendário fiscal) é o ativo que vale
dinheiro e o que menos muda. A CrewAI é um framework jovem que já trocou de scaffold.
`scripts/audita_fronteira.py` reprova o build se alguém quebrar a fronteira.

## Layout

```
src/abba_crews/
  core/            # ZERO crewai. Pydantic, reconciliação, creditabilidade,
    produtos/      # calendário, cofre, arquivo, aprovação, registro dos 7 produtos
  flows/           # orquestração determinística (importa crewai)
  crews/           # VAZIO — a primeira crew é a de julgamento, no M3b
  tools/           # VAZIO — BaseTool finos por cima de core/, quando houver crew
  main.py          # kickoff/plot/run_with_trigger — convenção da CrewAI
  cli.py           # CLI de operação dos sócios
scripts/           # audita_fronteira.py
tests/             # unit + golden
```

`crews/` e `tools/` estão vazios de propósito e o layout diz isso: **não existe nenhuma
crew neste projeto ainda.** A Sentinela roda ponta a ponta sem LLM nenhum; a primeira
crew é a de julgamento do resíduo, e ela depende da tabela de vedações (P2).

## Fronteira — onde o produto para

- **Nenhuma crew transmite ao Fisco.** Não existe ferramenta de transmissão no projeto.
- **Nenhum parecer tributário gerado por LLM.** A crew evidencia; o contador conclui e assina.
- **Sem 100% por resultado.**
- **Este projeto ainda não escreve nada no cérebro** (`assessment-brain`). Quando
  escrever, no M5, será com origem `tool_output` — que nunca sobrepõe o que um humano
  afirmou. `engagement_id` já existe na configuração e é a metade que espera a outra.

## Segredos

Certificado digital A1 e credenciais da Plataforma RTC **nunca** entram no repositório.
`.gitignore` bloqueia `*.p12`, `*.pfx`, `*.pem`, `*.key`; a CI reprova se algum for rastreado.
Ver `.env.example` para os nomes das variáveis.

Telemetria da CrewAI vem desligada por padrão — este projeto toca dado fiscal de
cliente. A trava é aplicada **em execução**, em `abba_crews/__init__.py`, antes de
qualquer import de `crewai`: `CREWAI_DISABLE_TELEMETRY=true`, `CREWAI_TRACING_ENABLED=false`
e `OTEL_SDK_DISABLED=true`. `tests/unit/test_telemetria.py` lê o código instalado da
CrewAI e reprova se algum desses nomes deixar de existir lá — documentação que promete
uma variável ignorada pela biblioteca é o pior defeito possível numa trava de privacidade.
