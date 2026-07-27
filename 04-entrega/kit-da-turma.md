# Kit da Turma — operação do formato único da capacitação

> **Decisão E4:** capacitação só existe como **"Turma {{N}} da {{Empresa}}"** — identidade, calendário e graduação; nunca "acesso à plataforma". Executado pelo [estágio 08](../02-jornada-do-cliente/08-capacitacao-e-transformacao.md) conforme o [plano de capacitação](plano-de-capacitacao.md). Suporte em código: tela `/admin/turmas` do portal (branch `claude/abba-consulting-structure-kdyfga`, pendente merge do Pedro).

## Regra de nomeação

`Turma {{N}} da {{Empresa}}` — N sequencial por cliente (Turma 1, Turma 2…). O nome aparece: no portal (criação via `/admin/turmas`), no e-mail de boas-vindas, no kickoff (slide de abertura), nos certificados e no relatório mensal. Nome é identidade: **nunca** renomear turma em andamento.

## Cronograma-modelo (adaptar no plano de capacitação)

| Semana | Marco |
|---|---|
| 0 | **Kickoff presencial** (kit do facilitador da Academy) — a turma nasce com data de graduação anunciada |
| 1–2 | Nível 1 Explorador: trilha + desafios + Bússola preenchida por todos |
| 3–4 | Workshop de marco (presencial ou ao vivo) + início do Nível 2 nos papéis certos |
| 5–7 | Trilhas por papel + desafios aplicados aos agentes reais do cliente |
| 8 | **Graduação** — cerimônia presencial: certificados, campeões apresentam a Primeira Vitória, patrocinador fala |

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

- [ ] Status da turma → `graduated` no portal (`/admin/turmas` — carimba a data oficial)
- [ ] Certificados gerados pelo [modelo](../08-materiais/modelos/certificados-modelo.pptx) (nível alcançado por participante — escala oficial P7)
- [ ] Cerimônia: patrocinador abre · 2–3 campeões apresentam a Ficha Primeira Vitória · entrega dos certificados · foto da turma
- [ ] Pós: foto + números da turma (conclusão, horas reinvestidas) no relatório mensal · depoimento do patrocinador pedido no evento (quente > frio)
- [ ] Graduados Nível 4 (Arquiteto): licença CrewAI de 12 meses ativada (promessa oficial — [ficha](../06-ferramentas/ferramenta-agentes.md))

## Frases

- ✅ "A Turma 1 da {{Empresa}} se forma em {{mês}}" · ❌ "vocês terão acesso à plataforma"
- ✅ "restam {{X}} semanas para a graduação" · ❌ "façam no seu ritmo" (ritmo é da turma)
