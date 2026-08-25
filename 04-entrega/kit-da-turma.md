# Kit da Turma — operação do formato único da capacitação

> **Decisão E4:** capacitação só existe como **"Turma {{N}} da {{Empresa}}"** — identidade, calendário e graduação; nunca "acesso à plataforma". Executado pelo [estágio 08](../02-jornada-do-cliente/08-capacitacao-e-transformacao.md) conforme o [plano de capacitação](plano-de-capacitacao.md). Suporte em código, **no ar** (correção 24/08 — a nota antiga "pendente merge / vínculo é evolução futura" estava defasada): tela `/admin/turmas` cria a turma com datas; o importador `/admin/roster` carrega a lista, **vincula cada pessoa à turma** e dispara os convites de acesso (e-mail quando o provedor está configurado; sempre no sino do portal).

## Regra de nomeação

`Turma {{N}} da {{Empresa}}` — N sequencial por cliente (Turma 1, Turma 2…). O nome aparece: no portal (criação via `/admin/turmas`), no e-mail de boas-vindas, no kickoff (slide de abertura), nos certificados e no relatório mensal. Nome é identidade: **nunca** renomear turma em andamento.

## Cronograma-modelo (adaptar no plano de capacitação)

| Semana | Marco |
|---|---|
| 0 | **Kickoff da Academy** ([kit do facilitador](kit-do-facilitador.md)) — a turma nasce com data de graduação anunciada e **linha de base medida** |
| 1–2 | Nível Explorador: trilha da Fundação + desafios + Bússola preenchida por todos |
| 3 | **Marco 1 — "o caso de vocês"** (presencial): os casos reais da empresa viram os desafios do resto do programa |
| 3–5 | Trilhas por papel + desafios no fluxo real de cada um |
| 6 | **Peneira + Marco 2 — formação de campeões** (presencial, só os selecionados): critério é comportamento observado — concluiu + aplicou + ajudou |
| 6–7 | Campeões em formação · demais consolidam, praticando em duplas |
| 8 | **Graduação** — cerimônia presencial: comparação com a linha de base, campeões apresentam a Primeira Vitória, certificados e credencial, patrocinador fala |
| d30 · d60 · d90 | **Checkpoints de durabilidade + relatório d90.** A entrega termina aqui, não na formatura |

Regras do formato (evidência cohort — [análise](../05-interno/analise-estrategica-2026-07.md), seção 5): início e fim **declarados no dia 0** · desafios com componente coletivo · graduação é evento, não e-mail.

## E-mail de boas-vindas (copy pronta — enviar pelo comercial@/facilitador)

> **Assunto:** Bem-vindo(a) à Turma {{N}} da {{Empresa}} — começamos {{DATA_KICKOFF}}
>
> Olá, {{NOME}} —
>
> Você faz parte da **Turma {{N}} da {{Empresa}}**: {{QTD}} colegas, {{SEMANAS}} semanas, começando no kickoff presencial de {{DATA_KICKOFF}} e terminando na graduação de {{DATA_GRADUACAO}} — com certificado e apresentação das primeiras vitórias.
>
> O que fazer antes do kickoff (15 min): acesse a Plataforma ABBA com o link abaixo, complete seu perfil e responda a primeira reflexão da Bússola. A Iris (sua guia de IA, em português) te acompanha em tudo.
>
> {{LINK_DE_ACESSO}}
>
> Até o dia {{DATA_KICKOFF}} — ABBA Consultoria de IA

## Checklist de graduação (chapéu Capacitação, semana final)

- [ ] **Cerimônia em `/admin/graduacao`** (B2.3, 25/08): o portão (Fundação 8/8 + ≥6/8 drills) conferido NA TELA, pessoa a pessoa, e as **credenciais verificáveis de Fundação emitidas em lote** — o clique da cerimônia também carimba a turma `graduated` (a data oficial). Sem planilha paralela; re-clicar não duplica; exceções são decisão humana, fora do lote
- [ ] Certificados IMPRESSOS gerados pelo [modelo](../08-materiais/modelos/certificados-modelo.pptx) (nível alcançado por participante — escala oficial P7; complementam a credencial digital, não a substituem)
- [ ] Cerimônia: patrocinador abre · 2–3 campeões apresentam a Ficha Primeira Vitória · entrega dos certificados · foto da turma
- [ ] Pós: foto + números da turma (conclusão, horas reinvestidas) no relatório mensal · depoimento do patrocinador pedido no evento (quente > frio)
- [ ] Graduados Nível 4 (Arquiteto): licença CrewAI de 12 meses ativada (promessa oficial — [ficha](../06-ferramentas/ferramenta-agentes.md))

## Frases

- ✅ "A Turma 1 da {{Empresa}} se forma em {{mês}}" · ❌ "vocês terão acesso à plataforma"
- ✅ "restam {{X}} semanas para a graduação" · ❌ "façam no seu ritmo" (ritmo é da turma)
- ✅ "o nosso treinamento acaba no relatório de durabilidade de 90 dias" · ❌ "acabou na formatura"
- ✅ "campeão é quem aplicou e ajudou alguém" · ❌ "campeão é quem tirou as melhores notas"
