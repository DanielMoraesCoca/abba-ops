# Ferramenta: Portal — ficha de negócio

> **Nome externo:** "Plataforma ABBA" · **interno:** abba-portal. Serve o estágio [08](../02-jornada-do-cliente/08-capacitacao-e-transformacao.md) (+ pré-trabalho do [06](../02-jornada-do-cliente/06-avaliacao-profunda.md)). Conteúdo didático: [materiais da Academy](../08-materiais/README.md).

## O que podemos prometer hoje

| ✅ Prometer | ⚠️ Com cuidado | ❌ Não prometer (ainda) |
|---|---|---|
| Trilhas em pt-BR com desafios avaliados pela Rubrica ABBA, Bússola e Iris (guia em português) — **27 aulas escritas e no portal: Fundação (8), Operacional (6), Gestor (5) e Especialista/formação de campeão (8, escrita 24/08 — visível-e-travada até o nível)** | **Vídeos: são NOSSOS (decisão CONTENT-13, 19/08/2026 — revoga o modelo de licenciar terceiros).** Roteiros word-for-word das 8 aulas prontos; gravação pelos fundadores em lotes (aulas 3, 4 e 1 primeiro). Até gravar, a aula roda em 4 blocos — **prometer "aulas com prática avaliada"; NUNCA prometer biblioteca de vídeo com data** | SSO corporativo / requisitos de procurement enterprise (autenticação interina — R3) |
| Acesso individual por colaborador, progresso e adoção visíveis ao patrocinador | Fases 2–4: estrutura pronta, conteúdo produzido sob demanda do 1º cliente — prometer "trilha do seu departamento", não "catálogo completo" | Fórum aberto entre clientes **antes do 3º cliente** — a rede existe em plano e o mecanismo está construído, mas não se promete data ([ecossistema](../00-identidade/ecossistema.md)) |
| Pré-trabalho da avaliação (reflexões, mapas de fluxo, Bússola) | Níveis oficiais (P7 ✅): Explorador → Praticante → Especialista → Arquiteto — Academy e proposta seguem esta escala; portal já implementa | Marketplace de agentes |
| Fluxos LGPD do titular (acesso, exportação, eliminação) | | CrewAI embutido no portal — integração simples, prevista para os próximos dias (Pedro é o dono da conta/parceria CrewAI; confirmado 2026-07-24). Migra para ✅ quando estiver no ar E testada; até lá, a promessa segura é a licença CrewAI de 12 meses ao graduar |
| **O portal entre as aulas — a academia diária (Currículo v3, 23/08/2026, CONTENT-16 no portal):** Prática de Hoje na home (uma ação de 2–5 min/dia), Biblioteca de Pedidos (40 pedidos por área, todo cartão termina em conferência), academia curta (drills de caça ao erro, Prompt Golf, cenários de decisão em texto) e Boletim semanal (estudo curto na voz da casa; **8 números escritos e agendados até 05/10** — rotina editorial: um número novo por semana, dono: sócios; o `turma:preflight` avisa quando não há número futuro no estoque). **Fala pronta: "não é curso que acaba — é academia que a pessoa frequenta: todo dia o portal propõe uma prática de dois a cinco minutos no trabalho real dela".** Nada disso depende de vídeo — completo por desenho | **Minhas Ferramentas** (o método escrito da pessoa, guardado e editável em `/ferramentas` + "Guardar como ferramenta" nas aulas O2–O6): construído e testado, mas **liga quando a migração `20260823_user_artifacts.sql` rodar no Supabase** — até lá, mostrar na demo sem gravar, não prometer como ativo | |

### O que está construído e **desligado** (não prometer data, mas saber que existe)

Levantado em 2026-08-01 — o portal tem três capacidades de ecossistema prontas em código e sem exposição comercial ([ecossistema](../00-identidade/ecossistema.md)):

| Capacidade | Estado | Quando liga |
|---|---|---|
| **Benchmark de fluência e de durabilidade entre clientes** (`src/lib/fluency-benchmark.ts`, `durability-benchmark.ts`) | Construído e testado; renderiza **só para equipe ABBA** | Piso de privacidade de **5 clientes** qualificados (≥5 pessoas pontuadas cada) |
| **Credencial verificável portátil** do colaborador (`/api/credentials/issue`, `/verify`) | Funcional. O token não identifica o cliente | Pode ser combinada já no 1º cliente, na graduação |
| **Opt-in recíproco de contribuição** (coluna `benchmark_contribution`, padrão `true`) | Aplicado em banco | **Depende do Anexo IV do [contrato](../03-comercial/contrato-sow-esqueleto.md)** — sem ele, o padrão é indefensável perante um DPO |

**Como falar disso com cliente:** "existe, está construído, e liga quando houver massa suficiente para o anonimato ser real — inclusive para proteger vocês". Nunca prometer data.

## Setup de cliente

- [ ] Turma criada em `/admin/turmas` como **"Turma {{N}} da {{Empresa}}"** com datas de início e graduação (formato único E4 — [kit da turma](../04-entrega/kit-da-turma.md))
- [ ] Roster importado em `/admin/roster` (vincula à turma) e **convites disparados** — a tela diz se o e-mail saiu ou se ficou só no sino (exige `RESEND_API_KEY` no ambiente)
- [ ] Handoff da avaliação importado (quando estágio 06 concluído)
- [ ] Trilha do departamento configurada conforme o [plano de capacitação](../04-entrega/plano-de-capacitacao.md)
- [ ] Slots [PERSONALIZAR] do conteúdo preenchidos com dados do cliente
- [ ] Patrocinador com acesso ao painel de adoção

## Custo por uso

| Operação | Custo de referência | |
|---|---|---|
| Iris (conversas dos participantes) | {{MEDIR: custo/participante/mês na 1ª turma}} | → planilha |
| Hospedagem/infra | fixo mensal (overhead) | → planilha |

## Dono e lacunas

**Operação:** chapéu [Capacitação](../01-setores/capacitacao.md) · **Saúde:** [Tecnologia](../01-setores/tecnologia.md). Lacunas ativas: R3 (auth interina) · R5 (vídeos — roteiros prontos em `abba-portal/docs/platform/content/roteiros/`, gravação em lotes pelos fundadores). P7: ✅ resolvida 2026-07-23. Status no [mapa](mapa-jornada-ferramentas.md).
