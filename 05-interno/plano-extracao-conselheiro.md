# Plano de extração dormente — o Conselheiro Digital em repositório próprio

> **Camada:** interno (desenho de engenharia, DORMENTE). Origem: decisão de sócios 2026-08-10 ([registro](registro-de-decisoes.md)) — a ideia do repo próprio foi acolhida na direção e negada no timing. Este documento existe para que, quando o gatilho acender, a extração seja um recorte planejado e não uma discussão do zero.
>
> **Gatilho de ativação: Fase 3 do [plano do Conselheiro](plano-implementacao-conselheiro.md) — 3+ clientes**, quando a Iris-Empresa (portal) passar a ler o cérebro e nascer a necessidade real de uma fronteira de serviço. Antes disso: **nenhuma linha deste plano vira código** (moratória de engenharia do [parecer do conselho](parecer-conselho-2026-08.md)).
>
> Dono: sócio de engenharia. Revisão: no gatilho, contra o estado real do código na época.

---

## O que SAI (vira o repo do cérebro)

- `assessment-brain/src/brain/` inteiro (facts bitemporais, decisions/outcomes, profile_blocks, ciclo noturno, reforço, consolidação, auditoria, playbooks, calibração, antecipação, prompts do brain)
- As migrações do cérebro (029–048: episodes, prompt_addenda, facts, decisions, consolidations, audit_runs…) — com a história preservada
- O CLI `abba brain *`, `abba episodes`, `abba addenda`, `abba learn`
- Os testes do cérebro, INCLUINDO as travas de regressão das re-análises (review-regressions, review4-regressions) — as travas viajam com o órgão que protegem

## O que FICA (assessment-brain continua sendo o motor de diagnóstico)

- Pipeline de análise (25 dimensões, síntese, inteligência financeira, calibração de análise) e os prompts canônicos travados (byte-equality)
- Ingestão, relatórios, knowledge vault (a "memória da espécie" é da ABBA, não de um cérebro de cliente — a troca vault↔cérebro atravessa a fronteira por contrato)
- `abba scout`, share-links, o assessment web

## A costura (a parte que decide se a extração é recorte ou reescrita)

1. **Contrato versionado** entre os dois lados, nos moldes do `assessment-handoff` (o precedente que já liga assessment-brain ↔ abba-portal): schema Zod/JSON com versão, validado nos dois lados. Superfícies mínimas: emissão de episódios (host → cérebro) · consulta de fatos/brief (cérebro → host) · troca com o vault (padrão anonimizado sobe, prior de setor desce) · **cascade do `abba forget`** atravessando a fronteira com certificado de deleção único.
2. **O `forget` é o teste de aceitação nº 1:** um `abba forget --engagement X` disparado no host tem que purgar o cérebro do outro lado e devolver UM certificado consolidado. Se isso não funcionar, a extração não acontece — LGPD não vira responsabilidade distribuída.
3. **Banco:** a decisão SQLite→Postgres (já prevista no plano do Conselheiro, `connection.js` preparado) é tomada JUNTO com a extração — um cérebro-serviço multi-cliente nasce em Postgres com RLS, na infra que o portal já usa.

## Critérios de pronto (nenhum negociável)

Suíte verde nos dois repos · teste de restart (o cérebro reidrata `profile_blocks` do zero) · teste do `forget` ponta a ponta com certificado · byte-equality dos prompts canônicos intocada no host · zero queda nos pisos do benchmark · um cliente piloto operando 2 semanas na fronteira nova antes de migrar os demais.

## As tentações a recusar até (e durante) o gatilho

| Tentação | Por que recusar |
|---|---|
| Extrair "já que estamos mexendo" antes de 3 clientes | Encanamento a serviço de zero consumidores; o fosso é o diário acumulando, não a arquitetura |
| Dar nome/marca ao produto na extração | Naming é decisão de sócios gateada na Fase 4 (10+ clientes) |
| API pública/aberta do cérebro | A superfície é o contrato interno; exposição externa é outra decisão, com outra segurança |
| Reescrever "da maneira certa" durante a mudança | A extração move órgãos testados; melhoria é outro PR, depois, com as travas de sempre |
| Multi-tenancy nova no meio do caminho | Usar a que existe (portal, RLS staged) — não inventar uma terceira |

## Ligações

[Plano do Conselheiro](plano-implementacao-conselheiro.md) (fases e gatilhos) · [Arquitetura do cérebro](arquitetura-cerebro-conselheiro.md) · [Estudo Conselheiro Digital](estudo-conselheiro-digital.md) · [Registro de decisões](registro-de-decisoes.md) (entrada 2026-08-10)
