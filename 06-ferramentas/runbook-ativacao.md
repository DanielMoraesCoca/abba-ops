# Runbook de Ativação — ligar o Conselheiro Digital em produção

> **Camada:** ferramenta/infraestrutura. Cobre o que o [dossiê vivo](../04-entrega/dossie-vivo-conselheiro-digital.md) não cobre: o dossiê ensina a **operar** o cérebro; este ensina a **ligá-lo e a não perdê-lo**.
>
> **Por que existe:** o cérebro está construído e testado (429/429), mas até 2026-08-01 não havia nada escrito sobre cron, custódia de chave, backup ou contingência de API — e o próprio dossiê chamava o agendamento de *"cron do sono (1 linha)"*, o que é uma subestimativa perigosa. Um cron ingênuo roda **sem chave nenhuma e contra um segundo banco vazio**, sem erro visível.
>
> Dono: Tecnologia (Pedro). Revisar a cada ativação de cliente novo.

---

## Regra zero — a que não tem volta

> **Se a `ABBA_DB_PASSPHRASE` for perdida, o banco E todos os relatórios e briefs em disco ficam ilegíveis para sempre.** Não existe recuperação, não existe suporte, não existe backdoor. Com [bus factor 2](../05-interno/registro-de-riscos.md), a chave viver só no computador de um sócio é risco de perder a empresa inteira.

**Custódia obrigatória, antes de qualquer dado de cliente entrar:**

1. A passphrase é gerada uma vez, com no mínimo 24 caracteres aleatórios.
2. Ela vive em **dois lugares independentes**: (a) o gerenciador de senhas de cada sócio — os **dois** sócios, não um; (b) um envelope selado físico, guardado fora do escritório.
3. **Nunca** em e-mail, WhatsApp, commit, print ou anotação de reunião.
4. A mesma disciplina vale para a `ABBA_BACKUP_PASSPHRASE` — se não for definida, o comando **gera uma e imprime uma única vez no terminal**; perder aquela linha transforma o backup num tijolo.
5. Rotação: só com plano. Trocar a chave do banco exige rechavear o banco **e** aceitar que os `.md` cifrados com a chave antiga ficam ilegíveis (ver §5).

---

## 1. Preparar a máquina (uma vez)

```bash
cd /caminho/para/assessment-brain
npm install
cp .env.example .env && chmod 600 .env
```

Preencher no `.env`, no mínimo:

| Variável | Por quê |
|---|---|
| `ANTHROPIC_API_KEY` | O ciclo noturno não roda sem ela |
| `ABBA_DATA_DIR` | **Caminho absoluto.** Relativo + cron com diretório errado = segundo banco vazio, em silêncio |
| `ABBA_DB_PASSPHRASE` | Cifra o banco e todo entregável em disco (ver regra zero) |
| `ABBA_BRAIN_MAX_USD` | Teto por cliente por noite (padrão 1,00) |
| `ABBA_BACKUP_PASSPHRASE` | Para o backup não gerar uma senha efêmera |

Conferir:

```bash
node bin/abba.js doctor          # ambiente: chave presente, banco abre, permissões, deps
node bin/abba.js doctor --live   # e a chave FUNCIONA de verdade (~1 token)
```

> `doctor` sozinho confere que a variável existe. Uma chave **revogada ou sem saldo passa em todo teste offline** — só o `--live` denuncia. Rodar o `--live` antes de cada ativação e depois de qualquer mexida em faturamento no provedor.

**Banco já existente sem criptografia?**

```bash
node bin/abba.js db migrate-to-encrypted     # cria a cópia cifrada e verifica linha a linha
# depois de conferir que a cópia abre com a passphrase:
shred -u <caminho-do-banco-antigo>.db        # ou rm -P no macOS
```

O comando **não apaga o banco claro** — apagar é passo manual, e esquecê-lo deixa uma cópia sem criptografia do dado do cliente no disco.

---

## 2. Ligar o ciclo noturno

O wrapper `scripts/nightly.sh` existe porque um `abba brain sleep` direto no crontab falha de quatro formas silenciosas: sem `cd`, o `.env` não é lido; sem `ABBA_DATA_DIR` absoluto, nasce um segundo banco; sem `ABBA_DB_PASSPHRASE` explícita, o keychain está trancado numa sessão headless; e sem log e sem código de saída, a noite pode falhar trinta vezes sem ninguém saber.

```bash
crontab -e
```

```cron
MAILTO=comercial@abbaservices.com.br
0 3 * * *  /caminho/para/assessment-brain/scripts/nightly.sh
```

O wrapper: fixa o diretório · roda o `doctor` · chama `abba brain sleep --all` (todos os engajamentos ativos, um preflight de LLM antes de gastar) · grava em `~/.abba/logs/nightly-AAAA-MM-DD.log` com rotação de 30 dias · sai com código ≠ 0 quando algo falha, para o cron mandar o e-mail.

Alerta em canal próprio (opcional): `export ABBA_ALERT_CMD='/usr/local/bin/notifica-slack'`.

**Conferir na manhã seguinte à primeira noite:**

```bash
tail -40 ~/.abba/logs/nightly-$(date +%F).log
node bin/abba.js brain health <eng>       # 9 componentes, 0–100
node bin/abba.js brain facts <eng> --contested   # alguém tentou envenenar a memória?
```

---

## 3. Backup — o que salvar e como provar que voltou

```bash
node bin/abba.js backup            # banco cifrado + arquivo dos entregáveis + sidecar SHA-256
node bin/abba.js restore <arquivo> # verifica o checksum ANTES de tocar o banco vivo
```

Dois arquivos são gerados, e os **dois** são necessários:

| Arquivo | Contém | Se faltar |
|---|---|---|
| `abba-backup-<data>.db` | Banco: memória, decisões, resultados, auditoria | Perde o cérebro |
| `abba-backup-<data>-deliverables.tar.gz` | Relatórios, one-pagers, briefs em disco | **Perde o que o cliente efetivamente recebeu** — e é exatamente o que ele pediria de volta |

**Onde guardar:** o padrão grava em `data/backups`, ou seja, **no mesmo disco que o backup deveria proteger**. Copiar semanalmente para destino externo (Drive da empresa ou disco físico). Sugestão de cron:

```cron
0 4 * * 0  cd /caminho/assessment-brain && node bin/abba.js backup && rsync -a data/backups/ /destino/externo/
```

**Testar o restore a cada trimestre, em pasta descartável.** Um backup nunca restaurado não é um backup — é uma esperança. (Este comando passou meses quebrado sem que ninguém notasse, porque só o cálculo do checksum era testado; hoje há teste de round-trip real em `test/integration/backup-roundtrip.test.js`.)

> **Armadilha do restore em máquina nova:** o banco volta com a chave nova, mas os `.md` cifrados no arquivo de entregáveis foram cifrados com a chave **antiga**. Restaurar num ambiente com passphrase diferente devolve o banco e deixa os relatórios ilegíveis para sempre. **Restaurar sempre com a mesma `ABBA_DB_PASSPHRASE` de origem** — outro motivo para a regra zero.

---

## 4. Contingência de chave de API no meio de uma entrega

| Sintoma | O que fazer |
|---|---|
| `doctor --live` acusa `credit` | Saldo esgotado. Recarregar no console do provedor. **O ciclo noturno não começa** (o preflight barra antes de gastar) — nada foi perdido |
| `doctor --live` acusa `auth` | Chave revogada/errada. Gerar nova, atualizar `.env`, `chmod 600` de novo |
| Sono abortou por orçamento (`budget_aborted`) | Comportamento normal e seguro: o progresso da noite está gravado e a próxima noite **retoma de onde parou, sem repagar**. Se acontecer sempre, subir `ABBA_BRAIN_MAX_USD` |
| Falha no meio, sem ser orçamento | Os episódios que falharam são **reprocessados na noite seguinte** automaticamente. Conferir `brain health` e o log |

---

## 5. Retenção e o direito de ser esquecido

`abba forget --client|--engagement|--expired` é o **único** caminho sancionado de deleção: purga os arquivos em disco, cascateia no banco e grava um tombstone com **certificado de resíduo zero** — que re-conta toda tabela ligada ao titular e atesta que nada sobrou. É o artefato para uma solicitação de titular sob a LGPD.

**O que ainda depende de decisão dos sócios** (nada disso está automatizado hoje):

- [ ] Definir a política de retenção por engajamento (quantos meses após o encerramento) e refleti-la no contrato
- [ ] Setar `retention_until` no encerramento de cada engajamento — hoje **nenhum código faz isso**
- [ ] Agendar a varredura: `0 5 1 * *  cd /caminho && node bin/abba.js forget --expired`

---

## 6. O gate que separa "ligado" de "confiável"

Ligar o cérebro é infraestrutura (as seções acima). **Confiar nele com um cliente pagando é outra coisa**, e exige crédito de API e tempo de sócio sênior:

| # | O quê | Onde | Custo |
|---|---|---|---|
| 1 | **Validação com LLM real** — passos 1 a 4 do runbook de validação | `eval/VALIDATION-RUNBOOK.md` no assessment-brain | ~US$ 1 no eval + 1 engajamento anonimizado julgado a olho |
| 2 | **Golden set de 20–50 casos** aprovados pelos sócios | especificado no [plano §6](../05-interno/plano-implementacao-conselheiro.md), **ainda não implementado** | tempo de sócio |
| 3 | **Ensaio no Cliente Zero** — ciclo noturno real, ritual diário completo | [runbook do Cliente Zero](../05-interno/cliente-zero-runbook.md) + [dossiê vivo](../04-entrega/dossie-vivo-conselheiro-digital.md) | 1 semana |
| 4 | **Check loop-native** antes de `ABBA_RECOMMENDER_SPINE=loops` | seção Wave 2 do mesmo runbook | 2 assessments Sonnet (~US$ 6) + julgamento sênior |

**Enquanto os quatro não estiverem feitos:** o método está validado apenas em dados sintéticos ([R1](../05-interno/registro-de-riscos.md)), o recomendador loop-native fica **desligado** e o framework v2 (D26–D28) **não vai a cliente**.

---

## Checklist de ativação (imprimir e marcar)

**Infraestrutura**
- [ ] `.env` preenchido e `chmod 600`
- [ ] Passphrase do banco em custódia dupla (dois gerenciadores + envelope físico)
- [ ] Passphrase de backup definida e guardada
- [ ] `doctor` e `doctor --live` verdes
- [ ] Banco cifrado (e o `.db` claro destruído, se houve migração)
- [ ] Cron do sono instalado com `MAILTO`
- [ ] Primeira noite conferida no log da manhã seguinte
- [ ] Cron de backup semanal + cópia externa
- [ ] Restore testado em pasta descartável

**Confiança**
- [ ] Validação com LLM real (passos 1–4)
- [ ] Golden set calibrado pelos sócios
- [ ] Cliente Zero percorrido com o ciclo noturno ligado
- [ ] Política de retenção decidida e `retention_until` sendo setado

**Só com as duas listas fechadas o cérebro atende um cliente pagante.**
