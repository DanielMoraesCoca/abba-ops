# Instância ABBA — as 4 semanas, dia a dia

> **Camada:** interno (operação). Este é o plano de execução do [runbook da instância ABBA](abba-interna-runbook.md) — o runbook diz O QUE rodar; este documento diz QUANDO, QUEM e COM QUE CRITÉRIO, para as 4 semanas saírem do ⬜ sem fricção. Bloco B do Conselheiro Vertical (V3g), pendência aberta desde 2026-08-04.
>
> **Por que agora:** os dois números que faltam para precificar a recorrência com honestidade — custo/noite e minutos de curadoria/semana (gargalo nº 3 do parecer do conselho) — só nascem desta rodada. E cada semana rodada vira material honesto para as conversas comerciais (inclusive a [palestra de Brasília](../03-comercial/palestra-direito-e-ia.md)): *"nós rodamos o produto em nós mesmos; estes são os números"*.
>
> **Dono:** os dois sócios (curadoria é humana por doutrina). **Entrada:** máquina com assessment-brain + `ABBA_DB_PASSPHRASE` ativa (cerimônia da passphrase feita — kit §2). **Saída:** 4 semanas sem falha + folha de medição preenchida + gaps registrados.

---

## Dia 0 — semeadura (~50 min, os dois sócios juntos)

**1. Criar cliente e engajamento (runbook §1):**

```bash
abba client create "ABBA" --industry "consultoria"
abba engagement create "ABBA" "abba-interna"

abba ingest "abba-interna" <caminho>/abba-ops/00-identidade/mapa-da-abba.md
abba ingest "abba-interna" <caminho>/abba-ops/05-interno/registro-de-riscos.md
abba ingest "abba-interna" <caminho>/abba-ops/00-identidade/plano-de-negocio.md
abba ingest "abba-interna" <caminho>/abba-ops/00-identidade/visao-2029.md
```

**2. As decisões reais pendentes, com gatilho** (cada uma enche a fila da manhã com coisa verdadeira — anotar o `<id>` que cada `add` imprime):

```bash
# P4/P4b — advogado (contrato + Anexo IV) — acionado em 2026-07-25, aguardando
abba decision add "abba-interna" --title "P4/P4b: advogado (contrato + Anexo IV)" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric advogado_contratado --threshold 1 --direction above --review-in 7

# P5 — contador confirma enquadramento — acionado em 2026-07-25, aguardando
abba decision add "abba-interna" --title "P5: contador confirma enquadramento" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric contador_ok --threshold 1 --direction above --review-in 14

# Meta binária do conselho — 8 reuniões em 30 dias (plano de 60 dias, item 5)
abba decision add "abba-interna" --title "Meta binária: 8 reunioes marcadas em 30 dias" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric reunioes_marcadas --threshold 8 --direction above --review-in 30

# R23/R16 — checklist do Pedro (cron do portal · código do assessment web no repositório)
abba decision add "abba-interna" --title "R23+R16: cron verificado e assessment web versionado" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric checklist_pedro_ok --threshold 1 --direction above --review-in 14

# R5 — vídeos de maior alavancagem (1.3.3, 1.3.1, 2.1.2)
abba decision add "abba-interna" --title "R5: 3 videos de maior alavancagem gravados" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric videos_gravados --threshold 3 --direction above --review-in 21

# P10 — overlay jurídico: decidir direção A/B/C antes da palestra
abba decision add "abba-interna" --title "P10: overlay juridico A/B/C antes da palestra" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric overlay_decidido --threshold 1 --direction above --review-in 10
```

**3. Decisões já tomadas entram como tomadas** (dão história ao diário — ex.: V3c prateleira, V2z discurso, faixa de faturamento confirmada no kit §3): `abba decision add ... ` seguido do fluxo `decided --by "Nome"`, com outcome quando o efeito for medível.

**4. Primeira noite, na hora:** `abba brain sleep "abba-interna"` — anotar o custo impresso na folha de medição (linha "semana 0"). Se falhar aqui, é setup, não rotina: resolver antes de declarar a instância iniciada.

## A rotina (semanas 1–4)

| Quando | Quem | O quê | Tempo |
|---|---|---|---|
| Toda manhã (dia útil) | Sócio do dia (alternar por semana) | `abba brain next "abba-interna"` — ler a fila; o que venceu, decidir ou re-armar; anotar minutos gastos | ~10 min |
| Toda noite (cron ou manual) | — | `abba brain sleep "abba-interna"` — anotar custo impresso | 0 min (roda só) |
| Reunião semanal de sócios | Os dois | `abba brain facts "abba-interna" --contested` — resolver claims disputados com `--by` · atualizar métricas dos gatilhos que mudaram (`--checked`) · preencher a linha da semana na folha | ~15 min do encontro |
| Material novo da semana | Quem escreveu | `abba revise <arquivo.md> --engagement "abba-interna"` — o Revisor entra na rotina; `block` = não sai | ~2 min/arquivo |
| Fim da semana 4 | Os dois | `abba brain brief "abba-interna" --render` — o primeiro brief da própria ABBA; retrospectiva de 30 min: o que a fila acertou, o que ignorou, o que os números dizem | 45 min |

## Folha de medição (preencher aqui mesmo, toda semana)

| Semana | Noites rodadas | Custo total (US$) | Custo médio/noite | Min. de curadoria (soma) | Itens na fila resolvidos | Falhas/observações |
|---|---|---|---|---|---|---|
| 0 (dia 0) | | | | | | |
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

**Os dois números que esta folha existe para produzir:** custo médio/noite (validação do teto de US$ 1 e do custo-alvo por cérebro) e minutos de curadoria/semana (a hora de sócio que o preço da recorrência precisa cobrir). Ao final: transferir para a [planilha de precificação](../03-comercial/precificacao-planilha.md).

## Critérios

**Sucesso (o ⬜ vira ✅):** 4 semanas consecutivas sem falha de ciclo · folha completa · ≥ 1 brief mensal renderizado e curado · claims contestados zerados nas reuniões semanais.

**Alertas e ação:**

| Sinal | Ação |
|---|---|
| Custo/noite estourando o teto (`--max-usd`, padrão US$ 1) | Não subir o teto no reflexo: ver O QUE encareceu (volume ingerido? grounding ligado?) e decidir na reunião semanal |
| Fila da manhã ignorada 3+ dias corridos | O problema não é a ferramenta, é o ritual: reduzir para 3× por semana OFICIALMENTE em vez de falhar em silêncio — e registrar a mudança |
| Claims `--contested` acumulando sem resolução | Sinal de ingestão indiscriminada: revisar o que está sendo ingerido (o classificador da porta existe por isso — só entra o que merece memória) |
| Qualquer perda de dado | Parar, `abba backup`, investigar antes de seguir — e o teste de restore da Semana do Cliente Zero (kit §5) sobe de prioridade |

## Encadeamento com a Semana do Cliente Zero

Esta instância roda ANTES e DURANTE a [Semana do Cliente Zero](cliente-zero-runbook.md) (kit §5) e a alimenta: o cron do sono já estará ligado e medido, o ritual `next → decision → trigger → outcome` já estará ensaiado com pendências reais, e o teste de restore encontra um banco com conteúdo de verdade. A fricção da tabela v1 no runbook do Cliente Zero foi corrigida (referência atualizada para a v2 vigente).

## O que NÃO fazer (runbook §6 — vale a releitura antes do dia 0)

Não ligar `ABBA_INJECT_FACTS` (construído e desligado até eval com flag) · não misturar dado de cliente real (a abba-interna é da ABBA; cliente real tem engajamento segregado) · não citar padrões `market_research` do vault como "nossa experiência" em material · não pular a passphrase em máquina real (R18).

## Ligações

[Runbook da instância](abba-interna-runbook.md) · [Kit de execução dos sócios](kit-de-execucao-socios.md) · [Cliente Zero runbook](cliente-zero-runbook.md) · [Régua do Revisor](../06-ferramentas/regua-do-revisor.md) · [Plano do Conselheiro](plano-implementacao-conselheiro.md) §14 · [Parecer do conselho](parecer-conselho-2026-08.md) (gargalo nº 3 e plano de 60 dias)
