# Cliente Zero — log de execução

> Registro vivo da execução do [runbook](cliente-zero-runbook.md). O que já rodou, com data e evidência; o que falta, com o comando exato. Dono: os dois sócios + Claude.

## Etapa 0 · Ensaio mecânico (2026-08-19) — ✅ FEITO

Rodado por Claude em ambiente descartável (mock, banco não cifrado, dados sintéticos MediFlow — nenhum dado real envolvido). Objetivo: provar que a **coreografia de comandos** funciona de ponta a ponta antes de gastar um centavo de API.

| Passo | Comando | Resultado |
|---|---|---|
| Saúde do ambiente | `abba doctor` | ✅ (Node 22, deps opcionais ok) |
| Gate de regressão | `USE_MOCK_LLM=true npm run eval` | ✅ OK no fixture MediFlow |
| Cliente + engajamento | `client create` / `engagement create <cliente> <nome>` | ✅ (atenção: o nome é posicional, não `--name`) |
| Ingestão | `ingest <eng> test/fixtures/sample-company/ --level ceo_board --phase 1` | ✅ 8 docs, 0 erros; o sistema **avisa corretamente** os níveis/fases que faltam |
| Análise completa | `assess <eng>` | ✅ relatório 25/25 dimensões gerado |
| Brief pré-reunião | `brief <eng>` | ✅ gerado |
| Fato no cérebro | `brain fact <eng> --subject <s> --text ... --by "Nome"` | ✅ (atenção: `--subject` é obrigatório) |
| Noite do cérebro | `brain sleep <eng> --max-usd 1` | ✅ health 100/100, 4/4 probes, brief noturno gerado, custo $0 |
| Fila da manhã | `brain next <eng>` | ✅ responde com a antecipação (vazia, como esperado com 1 fato) |

**O que este ensaio prova:** a mecânica inteira (comandos, arquivos, fluxo) funciona. **O que ele NÃO prova:** a qualidade do conteúdo — todo texto veio como `[MOCK]`. A validação de verdade é a Etapa 1.

## Etapa 1 · Validação com LLM real — ⏳ BLOQUEADA EM 1 VARIÁVEL

O ambiente remoto do Claude **não tem** `ANTHROPIC_API_KEY` (o proxy da sessão não autentica ferramentas de terceiros — verificado em 19/08 com `doctor --live`, resposta 401).

**Para destravar (Pedro ou Daniel, ~5 min):** adicionar `ANTHROPIC_API_KEY` como variável de ambiente do ambiente Claude Code (claude.ai/code → configurações do ambiente → environment variables). **Nunca colar a chave no chat.** Custo estimado da etapa: ~US$ 0,70 (smoke test) + a rodada real (~15 min de pipeline).

Com a variável presente, a sequência (do [VALIDATION-RUNBOOK](../../assessment-brain/eval/VALIDATION-RUNBOOK.md)):

```bash
node bin/abba.js doctor --live      # a chave FUNCIONA de verdade
npm run eval                        # passo 1: pipeline real no MediFlow
                                    # esperar: captureRate ≥ 0.85, leakRecall ≥ 0.6, RMSE ≤ 0.2
# passo 2: engajamento real anonimizado (alvo já sugerido no pipeline:
# Brasal / ABC DataSaúde / Grupo Santa — análises de teste já existem)
node bin/abba.js scout "<Alvo>" --industry <slug> --create
node bin/abba.js ingest ... && node bin/abba.js assess ... && node bin/abba.js report ...
# passo 3: congelar como fixture de regressão (--update-baseline)
```

O julgamento humano do passo 2 (loops reais? Breach-Score faz sentido? plano de adoção são?) é **dos sócios** — o runbook é explícito: "your thumbs-up/down here IS the validation".

## Etapa 2 · Ensaios humanos (T1/T2, objeções, cronômetro) — ⏳ AGENDA DOS SÓCIOS

Dias 1 e 3 do [runbook](cliente-zero-runbook.md): não dependem de chave nem de Claude — dependem de 2×45 min na agenda dos dois. O material de apoio está pronto (pautas, coreografia, kit de presença).

## Descobertas do ensaio mecânico (corrigir na próxima passada)

1. `engagement create` usa nome **posicional** (`<cliente> <nome>`), não `--name` — o runbook do Cliente Zero não menciona; anotado aqui para ninguém travar nisso.
2. `brain fact` exige `--subject` — idem.
3. O relatório em mock imprime confiança 0.50 e custo $0.0000 — bom sinal de honestidade do sistema (não inventa números quando não há modelo real).
