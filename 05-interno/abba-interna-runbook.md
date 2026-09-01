# Runbook: a instância ABBA do Conselheiro (o Cliente Zero do próprio produto)

> **Camada:** interno (operação). Origem: Conselheiro Vertical (V3g). A ABBA vira o primeiro cliente do próprio Conselheiro: as nossas decisões viram diário, os nossos docs viram memória, o ciclo noturno roda com LLM real sobre nós, e é isso que mede custo (R20), valida a extração com dados reais (ataca R17) e produz o primeiro caso publicável honesto.
>
> É também a **onda 1 do [Assento](estudo-conselheiro-presente.md)**: a Ata Viva das reuniões de sócios alimenta esta instância.
>
> Dono: os dois sócios (a curadoria é humana por doutrina). Sucesso = 4 semanas sem falha + custo/noite medido + minutos de curadoria medidos.

## 1. Semear (uma vez, ~20 min)

```bash
# na máquina que roda o assessment-brain (dados reais → com passphrase!)
abba client create "ABBA" --industry "consultoria"
abba engagement create "ABBA" "abba-interna"

# memória inicial: os docs-mestres (nossos, sem LGPD de terceiros)
abba ingest "abba-interna" caminho/para/abba-ops/00-identidade/mapa-da-abba.md
abba ingest "abba-interna" caminho/para/abba-ops/05-interno/registro-de-riscos.md
abba ingest "abba-interna" caminho/para/abba-ops/00-identidade/plano-de-negocio.md
abba ingest "abba-interna" caminho/para/abba-ops/00-identidade/visao-2029.md
```

## 2. As decisões reais, com gatilho (uma vez, ~30 min)

Cada pendência viva vira uma decisão com data de revisão: é isso que enche a fila da manhã com coisa verdadeira:

```bash
abba decision add "abba-interna" --title "P4/P4b: advogado (contrato + Anexo IV)" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric advogado_contratado --threshold 1 --direction above --review-in 7

abba decision add "abba-interna" --title "P5: contador confirma enquadramento" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric contador_ok --threshold 1 --direction above --review-in 14

abba decision add "abba-interna" --title "Meta binária do conselho: 8 reuniões em 30 dias" --recommended-by consultant
abba decision trigger "abba-interna" <id> --metric reunioes_marcadas --threshold 8 --direction above --review-in 30

# idem para: faixa de faturamento (sócios), R23/R16 (Pedro), gravação dos vídeos (R5)
```

Decisões já tomadas (V3c prateleira, V2z discurso CAIO…) entram como `decided` com `--by` e ganham outcome quando o efeito for medível.

## 3. A rotina (diária, ~10 min; semanal na reunião de sócios)

```bash
abba brain sleep "abba-interna"          # noite: LLM REAL, teto padrão US$1: anotar o custo impresso
abba brain next "abba-interna"           # manhã: a fila: o que vence, o que está parado
abba brain facts "abba-interna" --contested   # semanal: claims disputados p/ resolver com --by
abba brain brief "abba-interna" --render      # mensal: o brief da própria ABBA
```

**Medir e anotar aqui mesmo (ou na planilha de precificação):** custo/noite impresso pelo sleep · minutos de curadoria por semana. Sem esses dois números, o preço da recorrência continua imaginário (gargalo nº 3 do conselho).

## 4. O Revisor na rotina (a voz que confere)

```bash
abba revise material-novo.md --engagement "abba-interna"        # antes de QUALQUER material sair
abba revise proposta.md --engagement "abba-interna" --llm       # + contradições com a nossa memória
```

Régua: [regua-do-revisor](../06-ferramentas/regua-do-revisor.md). Violação `block` = não sai. E quando o Revisor apontar um problema **recorrente de análise**, o circuito de melhoria já existe: `abba learn feedback <eng> --verdict reject --reason "..." --by "Nome"` → vira rascunho de addendum → sócio aprova (`abba addenda approve`) → o próximo assessment já sai melhor. **É assim que o Conselheiro vira conselheiro do nosso próprio assessment**: zero código novo.

## 5. O snapshot do portal (mensal, quando houver turma real)

```bash
# no portal (staff): GET /api/admin/engagement-snapshot?clientCode=<code>  → salvar snapshot.json
abba portal import "abba-interna" snapshot.json   # vira fatos tool_output com TTL de 35 dias
```

TTL mensal é proposital: snapshot esquecido **expira sozinho** e aparece na fila: o sistema cobra o re-sync em vez de exibir dado rançoso.

## 6. O que NÃO fazer nesta instância

- **Não ligar `ABBA_INJECT_FACTS`** antes do eval com flag (plano V3g, bloco E): a injeção de memória na análise está construída e desligada.
- **Não misturar dado de cliente real:** a abba-interna é da ABBA; cliente real tem engajamento próprio, segregado como sempre.
- **Não usar os padrões `market_research` do vault como "nossa experiência"** em material: são pesquisa com fonte, e o material deve dizer isso.
- **Não pular a passphrase** em máquina real (R18 continua valendo).

## Ligações

[Plano do Conselheiro Vertical](plano-implementacao-conselheiro.md) §14 · [Régua do Revisor](../06-ferramentas/regua-do-revisor.md) · [O Assento](estudo-conselheiro-presente.md) · [Dia a dia](estudo-conselheiro-dia-a-dia.md) · [Cliente Zero runbook](cliente-zero-runbook.md): o ensaio comercial, que esta instância alimenta
