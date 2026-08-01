# Dossiê Vivo / Conselheiro Digital — operação do cérebro por cliente

> **Camada:** processo de entrega. **Status: CONSTRUÍDO (2026-07-30) + Ondas 1–3 de memória entregues (2026-08-01); ativação gateada no 1º cliente em manutenção.** O código vive no assessment-brain (`src/brain/`); arquitetura em [`../05-interno/arquitetura-cerebro-conselheiro.md`](../05-interno/arquitetura-cerebro-conselheiro.md); plano e fases em [`../05-interno/plano-implementacao-conselheiro.md`](../05-interno/plano-implementacao-conselheiro.md). Este doc é o manual de operação para o Conselheiro humano. Nome comercial do produto = decisão de sócios (Fase 4); até lá, internamente: **Dossiê Vivo**.

## O que é (em uma frase para o sócio; não é material de cliente)

Um cérebro de IA POR CLIENTE, segregado, que ingere tudo do engajamento, **dorme toda noite** (consolida com teto de gasto), acorda com um brief rascunhado para a sua curadoria, **nunca esquece** (memória bitemporal: responde "o que era verdade em março?") e **melhora com resultado medido** (cada rejeição sua vira uma melhoria proposta; cada melhoria aprovada tem uplift comparado).

## O ciclo diário do Conselheiro humano (o ritual centauro)

| Momento | Ação | Comando |
|---|---|---|
| Durante o dia | Ingerir o que chegou do cliente (atas, KPIs, docs) — a ingestão re-renderiza o brief do mês sozinha | `abba ingest <eng> <arquivos>` |
| Noite (cron ou manual) | O cérebro dorme: extrai fatos, resolve contradições, expira KPIs vencidos, pontua runs, recompila o dossiê, rascunha o brief — tudo com teto de gasto (US$ 1 default) | `abba brain sleep <eng> [--max-usd]` |
| Manhã | Ler o brief rascunhado (SEMPRE marcado RASCUNHO até você aprovar) | `abba brain brief <eng>` |
| Manhã (30s) | **Reconfirmar o que vai vencer**: verdades perto do TTL ou contrariadas por um resultado medido. Perguntar ao cliente e reafirmar — é isso que mantém a memória viva | `abba brain reconfirm <eng>` |
| Mensal (opcional, custa) | Auditoria de fidelidade: compara os fatos com o texto-fonte de onde saíram. A auditoria de coerência já roda grátis toda noite | `abba brain audit <eng> --max-usd 0.10` |
| Ao medir um resultado | Registrar o outcome MEDIDO — é o que renova o TTL e sobe a confiança dos fatos que informaram a decisão, e o que gera playbook | `abba decision outcome <eng> <dec> --metric ... --baseline ... --value ... --verdict better` |
| Manhã (30s) | Revisar claims CONTESTADOS: documento contradisse verdade mais forte — o sleep avisa quando houver. Aceitar = afirmar você mesmo o valor; ignorar = claim fica inerte | `abba brain facts <eng> --contested` · aceitar: `abba brain fact <eng> --subject ... --predicate ... --object ... --by "Nome"` |
| Curadoria | Aprovar com nome (congela o mês; snapshot imutável `*-aprovado.md`) — OU corrigir | `abba brain brief <eng> --approve --by "Nome"` |
| Correção (o cérebro aprende) | Rejeitar uma saída com motivo → vira rascunho de melhoria + caso de regressão | `abba learn feedback <eng> --verdict reject --reason "..." --purpose dimension --by "Nome"` |
| Ativar a lição | Aprovar a melhoria proposta (gate humano nomeado; vale a partir do próximo run) | `abba addenda approve <pad_id> --by "Nome"` |
| Medir | Conferir se a melhoria melhorou de verdade | `abba learn uplift <eng> <pad_id>` |

## O ritual do conselho (mensal/trimestral)

1. Registrar cada recomendação levada à diretoria: `abba decision add <eng> --title "..."` → avançar conforme a vida real: `decided` (exige nome — a diretoria decidiu) → `implemented` → **outcome medido** (`abba decision outcome ... --metric --value --verdict`). O diário recomendado→decidido→implementado→medido é O ativo que compõe — nenhum concorrente tem.
2. Consultas na preparação: `abba brain facts <eng>` (verdades vigentes, com validade) · `--as-of 2026-03-01` (o que valia então) · `abba brain profile <eng>` (dossiê compilado) · `abba brain health <eng>` (9 componentes, 0–100 — abaixo de 70, olhar o detalhe antes do ritual) · `abba brain playbook <eng>` (métodos que já funcionaram neste cliente).
3. **Prova para a diretoria**: `abba brain benchmark <eng>` — o acerto da memória contra o tempo de casa. É o gráfico que mostra que o cérebro melhora com a convivência, e o único do mercado.
4. Identidade por cliente: `abba learn soul <cliente> --set '<json>'` (valores/voz/limites que moldam a narrativa do brief; sanitizado anti-injeção).

## Regras invioláveis (as mesmas do estudo, agora executáveis)

- **Um cérebro por cliente, segregado** — nunca cruzar dados; só o vault anonimizado cruza padrões
- **Toda saída ao cliente passa por curadoria e assinatura** — o brief nasce RASCUNHO e o approve é real (banner + congelamento do mês)
- **Nada se deleta fora do `abba forget`** — episódios são append-only; fatos supersedem, nunca somem
- **Todo job autônomo tem teto de gasto** (`--max-usd` / `ABBA_BRAIN_MAX_USD`) e deixa linha auditável (`brain_runs`)
- **O avaliador é intocável** — golden sets e gates ficam fora do alcance de qualquer loop de melhoria
- Consentimento de transcrição/ingestão segue o [guia LGPD](../08-materiais/guia-oculos-hud.md) e o contrato
- **A auditoria não se auto-elogia** — as sondas grátis medem COERÊNCIA da linha do tempo, não acurácia; só a sonda paga (contra o texto-fonte) mede fidelidade. Nunca apresentar uma como a outra
- **Resultado ruim não rebaixa verdade em silêncio** — abre dúvida para o humano decidir (`abba brain reconfirm`)

## O que falta para ligar em produção (gatilho: 1º cliente em manutenção)

1. Dados reais entrando (a disciplina de ingestão desde o kickoff) · 2. Calibração do golden set (20–50 saídas notadas pelos sócios) · 3. Cron do sono (1 linha) · 4. Decisões de sócios pendentes: nome comercial e se/como o cérebro entra no discurso comercial (hoje: diferencial interno da cadeira de Conselheiro, nunca prometido como produto avulso).
