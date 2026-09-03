# Staging — como extrair para o repositório `abba-crews`

## Por que este projeto está dentro de `abba-ops`

O plano previa um repositório próprio desde o commit #1, porque o **CrewAI AMP conecta
um repositório GitHub por projeto** e espera `pyproject.toml` com `[tool.crewai]` e
`uv.lock` **na raiz**. A criação do repositório foi tentada e recusada:

```
POST https://api.github.com/user/repos: 403 Resource not accessible by integration
```

O app do GitHub desta sessão pode ler e escrever nos repositórios existentes, mas não
pode criar novos. Então o projeto nasceu aqui, íntegro e completo, para não se perder —
e sai daqui com um comando.

**Tentado de novo no M8 (2026-09-03): o mesmo 403.** Não é permissão que se conquiste
insistindo — a criação do repositório é ato manual de quem tem a conta, e é o passo 1
abaixo.

**Nada no código depende deste caminho.** Não há import relativo para fora de `09-crews/`,
nem caminho absoluto. O único arquivo que menciona o staging é este e o `README.md`.

## A extração, em três passos

### 1. Criar o repositório vazio

No GitHub, criar `DanielMoraesCoca/abba-crews` — **privado**, **sem** README, `.gitignore`
ou licença (o conteúdo já existe aqui e um commit inicial atrapalha).

### 2. Extrair preservando o histórico

```bash
cd /caminho/para/abba-ops
git subtree split --prefix=09-crews -b extrai-abba-crews

mkdir ../abba-crews && cd ../abba-crews
git init -b main
git pull ../abba-ops extrai-abba-crews
git remote add origin git@github.com:DanielMoraesCoca/abba-crews.git
git push -u origin main
```

`git subtree split` reescreve o histórico de `09-crews/` como se ele sempre tivesse sido
a raiz — os commits e as mensagens sobrevivem. Uma cópia simples de arquivos perderia isso.

### 3. Limpar o staging

```bash
cd ../abba-ops
git rm -r 09-crews
git commit -m "Camada de Caixa: codigo migrado para o repositorio abba-crews"
```

Depois disso, atualizar o ponteiro em
[`../06-ferramentas/blueprint-crews-camada-de-caixa.md`](../06-ferramentas/blueprint-crews-camada-de-caixa.md).

## O que passa a valer sozinho depois da extração

- **A CI sai do `abba-ops` e vira a CI deste repositório.** Hoje ela mora em
  `../.github/workflows/abba-crews.yml` — na raiz do `abba-ops`, porque o GitHub só lê
  workflows na raiz do repositório — e roda com um filtro de `paths` para `09-crews/**`.
  Depois da extração ela volta para `.github/workflows/` daqui e **o filtro de `paths`
  sai junto**, porque o repositório inteiro passa a ser o projeto.

  > Este parágrafo dizia, até o M8, que "enquanto o projeto estiver aqui, a CI **não
  > roda**". Era verdade quando foi escrito e deixou de ser no M4b (achado G3), que moveu
  > o workflow para a raiz. Ficou falso por quatro marcos e ninguém percebeu, porque
  > nenhuma trava do projeto lê este arquivo.
- **`crewai deploy`** — o AMP conecta o repositório e lê `pyproject.toml` e `uv.lock` da raiz.

## Checklist de transferência para o CrewAI AMP

Conferido pela CI desde o M8 — o passo `crewai deploy validate` roda a cada push e
**confere a saída**, porque ele sai com código 0 mesmo quando avisa. Hoje: *Pre-deploy
validation passed.*

Já verdadeiro neste commit — conferir se continua depois da extração:

- [x] `pyproject.toml` com `[tool.crewai] type = "flow"`
- [x] `uv.lock` commitado (**não** no `.gitignore`)
- [x] `crewai[tools]>=1.15.18,<2.0.0`; Python `>=3.11,<3.14` (o piso real — ver V4l)
- [x] Entrypoints `kickoff` / `plot` / `run_with_trigger` em `[project.scripts]`
- [x] `crewai_trigger_payload` aceito no `@start()` — é como o AMP passa CNPJ e competência
- [x] Configuração toda por variável de ambiente; nenhum caminho local
- [x] Nenhuma chamada a CLI Node no código das crews (é a razão do outbox)
- [x] Segredos fora do repositório; certificado digital por gerenciador
- [x] Crews importáveis sem efeito colateral no import
- [ ] `Dockerfile` para paridade com o auto-hospedado — **não entregue.** Esta linha
      prometia "chega no M2"; o M2 passou (e o M3a, o M4a, o M4b, o M5, o M7 e o M8) e
      ele não existe. Não é bloqueio para o AMP, que constrói a partir do repositório;
      só vale para auto-hospedar. A promessa com prazo fica **sem prazo** até alguém
      tomar a decisão de auto-hospedar — que é o que a **P9** vai forçar.

## Antes de rodar `crewai deploy push`

A extração acima resolve o **encanamento**. Ela não torna o deploy útil, e duas coisas
precisam de resposta antes:

- **P9 — onde os dossiês moram.** `core/arquivo.py` assume disco durável, e o gate humano
  depende disso por desenho: o contador assina **depois**, no tempo dele. Num contêiner
  efêmero o dossiê e o outbox do ledger somem com a execução. Não afirmo o modelo de
  runtime da plataforma — não consigo verificá-lo daqui —, e por isso é decisão de
  arquitetura a tomar antes, não configuração a ajustar depois.
- **M6 — a coleta real.** `main.py` monta o Flow sem `Fonte`, e a coleta chega no M6, que
  depende da credencial da Plataforma RTC (**P4**). Subir hoje produz um Flow que só sabe
  levantar `NotImplementedError`. Honesto, e sem valor nenhum — vale dizer isso antes de
  alguém tentar.
