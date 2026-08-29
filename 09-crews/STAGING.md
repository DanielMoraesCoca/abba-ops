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

- **`.github/workflows/ci.yml`** — o GitHub só lê workflows na raiz do repositório.
  Enquanto o projeto estiver aqui, a CI **não roda**; os mesmos comandos estão no
  `README.md` para rodar na mão.
- **`crewai deploy`** — o AMP conecta o repositório e lê `pyproject.toml` e `uv.lock` da raiz.

## Checklist de transferência para o CrewAI AMP

Já verdadeiro neste commit — conferir se continua depois da extração:

- [x] `pyproject.toml` com `[tool.crewai] type = "flow"`
- [x] `uv.lock` commitado (**não** no `.gitignore`)
- [x] `crewai[tools]>=1.15.18,<2.0.0`; Python `>=3.10,<3.14`
- [x] Entrypoints `kickoff` / `plot` / `run_with_trigger` em `[project.scripts]`
- [x] `crewai_trigger_payload` aceito no `@start()` — é como o AMP passa CNPJ e competência
- [x] Configuração toda por variável de ambiente; nenhum caminho local
- [x] Nenhuma chamada a CLI Node no código das crews (é a razão do outbox)
- [x] Segredos fora do repositório; certificado digital por gerenciador
- [x] Crews importáveis sem efeito colateral no import
- [ ] `Dockerfile` para paridade com o auto-hospedado — **pendente, chega no M2**
