# Auditoria de Prontidão — 2026-08-18

> **O que é:** varredura completa dos 4 repositórios (abba-ops, assessment-brain, abba-portal, ABBA-legado) feita a pedido do Daniel, com uma pergunta-guia: *estamos preparados para receber clientes — e para receber MUITOS clientes?* Diferente do [parecer do conselho](parecer-conselho-2026-08.md) (análise de negócio, 01/08), esta auditoria **verificou as afirmações em código**: rodei as suítes de teste hoje, conferi cada risco do [registro](registro-de-riscos.md) contra o estado real dos repos e medi o que andou desde o parecer.
>
> Dono: sócios. Revisar na próxima reunião semanal, junto com o [plano de ação](plano-de-acao.md).

---

## 1. O veredito em três frases

1. **A empresa está mais bem documentada do que a maioria das consultorias de 50 pessoas — e continua sem ter percorrido o próprio caminho uma vez.** As duas caixas que faltavam no critério "pronto para receber um cliente" em 01/08 (Cliente Zero + Conselheiro ativado) são as mesmas que faltam hoje.
2. **Nos 17 dias desde o parecer do conselho, nenhum dos 10 itens das semanas 1–2 dele se moveu no repositório.** O esforço foi todo para marca e marketing (v4 completa, posts, kit — lacuna real, e agora fechada). Mas o caminho crítico congelou: portal sem commit há 22 dias, cérebro há 17.
3. **Para a pergunta "e quando vierem muitos clientes?": o gargalo não é o que vocês temem.** A estrutura de recorrência aguenta 6–8 clientes por desenho. O que não existe é o modelo de capacidade preenchido que diria QUANDO contratar — e o risco real de "muitos clientes" hoje é aceitar 2 programas completos simultâneos, que a matemática documentada diz ser impossível para 2 pessoas.

---

## 2. O que eu verifiquei em código hoje (não é opinião)

| Verificação | Resultado | Implicação |
|---|---|---|
| Suíte do assessment-brain (`USE_MOCK_LLM=true npm test`) | **429/429 verdes** em 10,5s | O código está saudável — e 100% em mock, como o R17 afirma. A pasta `eval/baselines/` tem **um único fixture mock**. O [VALIDATION-RUNBOOK](../../assessment-brain/eval/VALIDATION-RUNBOOK.md) do próprio repo diz: o mock "não pode julgar a qualidade em empresa real" |
| Suíte do abba-portal (`vitest run`) | **801/801 verdes** em 14s | O portal está são; a dívida é de configuração e deploy, não de código |
| R23 (cron contraditório) | **AINDA VIVO.** `vercel.json` agenda `compass-cadence` diariamente às 14:00 UTC; o próprio arquivo da rota diz "commented out in vercel.json until the founder is ready" | Ninguém sabe se o nudge automático roda em produção. 5 minutos do Pedro resolvem |
| R3 (auth do portal) | **Parcial.** Magic-link Supabase semi-ligado ("Move 5a"), mas o cookie `abba_session` segue **transicional e não assinado** por padrão | Continua bloqueando procurement enterprise; charter ciente segue sendo a resposta |
| R19 (backup) | **Mitigação declarada ≠ mitigação existente.** O registro cita `backup-roundtrip.test.js`; o que existe é `backup-integrity.test.js` (veredictos de checksum). Não há evidência do ensaio trimestral de restore em pasta descartável | Backup verificado por checksum ≠ restore ensaiado. Corrigir a linha do registro e agendar o primeiro ensaio |
| R16 (site público fora do repo) | **Sem mudança detectável** — o `web/` do assessment-brain segue sendo o console interno | O site que gera relatórios de 42 páginas continua existindo só no deploy do Pedro |
| R12 (materiais históricos) | **Parcial no portal:** `abba-portal/materials/` guarda 14 documentos da era v1 (oferta, produtos, playbook charter) **sem banner de histórico** | Qualquer pessoa com acesso ao repo pode citar preço/promessa antiga como vigente |
| [Planilha de precificação](../03-comercial/precificacao-planilha.md) | **100% em `{{ }}`** — nenhuma célula preenchida: horas por pacote, piso/hora, utilização, custo | A tabela v1 tem preços; ninguém calculou **margem nem capacidade**. É o buraco central da pergunta "muitos clientes" |
| Metas do ano 1 + runway ([plano de negócio](../00-identidade/plano-de-negocio.md) §7, [finanças](financas-basicas.md)) | **Ainda em `{{VALOR}}`/`{{DATA}}`/`{{N}}`** | Item 3 da semana 1 do conselho, custo ~1h, parado desde julho |
| Contrato ([esqueleto](../03-comercial/contrato-sow-esqueleto.md)) | Cláusula 9.7 **ainda duplicada**; benchmark ainda "contribui salvo recusa" (pendente advogado) | Itens 1–2 da semana 1 do conselho, sem movimento |
| Loop-native do recomendador | `ABBA_RECOMMENDER_SPINE=loops` segue **OFF por default**, "until real-LLM validated" | Coerente — mas é mais uma peça esperando a mesma validação real que nunca aconteceu |

**Leitura honesta do conjunto:** os problemas não são novos — são os mesmos de 01/08, agora com 17 dias a mais de idade. A novidade positiva é que a lacuna "a empresa não tem cara" (marca, materiais, presença) foi de fato fechada neste intervalo. A negativa é que ela foi fechada **em vez** do caminho crítico, não em paralelo.

---

## 3. O placar do plano de 60 dias do conselho (dia 17 de 60)

| Item (semanas 1–2, "tudo esforço baixo") | Estado em 18/08 |
|---|---|
| 1. Advogado + contador acionados com minuta corrigida (9.7, DPO, prazo de incidente) | 🔴 Acionados em 25/07, sem retorno registrado; minuta não corrigida |
| 2. Seção 8 reescrita (sócios nomeados) + benchmark opt-in | 🔴 Sem evidência no repo |
| 3. Metas do ano 1 + runway preenchidos | 🔴 Placeholders intactos |
| 4. Moratória de engenharia declarada | 🟡 Cumprida de fato (zero commit de feature) — mas por omissão, não por decisão registrada |
| 5. 20 alvos nomeados + 2 apresentações mornas/semana (meta: 8 reuniões em 30 dias) | ⚪ Não auditável por mim (tracker vive no Drive) — **é A pergunta para a reunião de sócios** |
| 7. Cliente Zero com LLM real + cérebro ligado | 🔴 Não iniciado (nenhuma evidência de execução do runbook) |
| 8. Medir custo noturno, decidir via CrewAI, site para o repo | 🔴 R9/R16/R20 sem mudança |

O único movimento estrutural do período foi meu, na frente de materiais: marca v4, kit inicial, posts, papelaria nominal, prévia do Instagram. Isso destravou parte da Frente B/D — mas **a publicação está bloqueada no aval do Pedro**, e as pendências humanas (fotos, bios, handle) continuam paradas.

---

## 4. A pergunta central: "e quando vierem muitos clientes?"

A matemática que o próprio repo documenta, consolidada num lugar só:

**Recorrência (manutenção + Conselheiro):**
- [Ritual semanal](../04-entrega/ritual-semanal.md): ~30 min/sócio/cliente/semana → **6–8 clientes = teto confortável; 10 = teto absoluto** antes de contratar ou cair para quinzenal.
- Custo noturno do cérebro: ~R$ 150/mês/cliente **estimado, nunca medido** (R20) — e fora da planilha de preço.
- Cada ativação de cliente novo é **manual**: [runbook de ativação](../06-ferramentas/runbook-ativacao.md) (cérebro por cliente) + seed do portal + turma + kickoff. Para 1–3 clientes, ok. A partir do 4º, o custo de onboarding precisa estar no preço e no calendário.

**Programas completos:**
- ~450h de sócios por programa de 16 semanas (estimativa do parecer, seção 5.3) contra ~167h faturáveis/mês da firma inteira no cenário C → **1 programa consome ~65% da firma. 2 programas simultâneos não cabem em 2 pessoas.** Este é o único cenário de "muitos clientes" que quebra a ABBA no curto prazo — e a defesa é uma frase no comercial: programa entra em fila, com data de início contratual, nunca dois kickoffs no mesmo mês.
- Os [gatilhos de contratação](../01-setores/README.md) existem e estão certos ("2+ engajamentos simultâneos com entrega apertada → contratar perfil de entrega"). O que falta para eles funcionarem é o **placar**: sem a planilha de capacidade preenchida e sem o log semanal rodando, o gatilho dispara tarde.

**Funil (se o marketing der certo):**
- O tracker de pipeline é uma tabela markdown copiada para o Drive — dimensionado para 20 alvos, correto para agora; acima de ~50 leads/mês vira gargalo (sem lembretes, sem histórico automático). Não é problema de hoje; registrar como gatilho: *pipeline > 30 linhas ativas → CRM de verdade*.
- Toda análise aceita promete **documento em 48h e apresentação em ≤5 dias**. Isso nunca foi cronometrado (é o Dia 2 do Cliente Zero). Se 5 análises chegarem na mesma semana, hoje ninguém sabe se a promessa se sustenta — o dry-run cronometrado responde isso.
- **WhatsApp continua sendo a maior lacuna de canal** (reconhecida no plano de redes §5): o parecer é explícito que a venda mid-market acontece lá, e não existe playbook.

**Conclusão desta seção:** a ABBA está *desenhada* para escalar até ~8 clientes de recorrência + 1 programa por vez, com gatilhos de contratação prontos. O que não está pronto é (a) o preenchimento dos números que fazem os gatilhos dispararem a tempo, e (b) qualquer coisa ter sido cronometrada na vida real. **O risco de escala não é "não aguentar muitos clientes" — é dizer sim ao segundo programa.**

---

## 5. As falhas, ranqueadas (o que mudaria o jogo, em ordem)

1. **Executar, não escrever.** (Sem custo, decisão pura.) O repo já diz tudo; os 3 bloqueios do critério final são humanos: aval do Pedro (marca/headline/posts), advogado/contador (cobrança de retorno — 24 dias sem resposta registrada), Cliente Zero na agenda. Uma semana de execução vale mais que qualquer documento novo — inclusive este.
2. **Cliente Zero com LLM real + cérebro ligado uma noite de verdade** (frente C / conselho item 7–8). Converte R1+R17 no primeiro caso publicável. Sem isso, cada material de marketing novo aumenta a promessa não exercitada.
3. **Preencher em 1 hora: metas do ano 1, runway, e as 6 células de capacidade da planilha** (horas/semana honestas, utilização, horas por pacote nos 3 produtos de entrada). Sem isso não há placar, e sem placar os gatilhos de contratação e o "quando dizer não" não funcionam.
4. **Higiene técnica de meio dia do Pedro:** R23 (cron: decidir e alinhar código × vercel.json), R16 (site público para o repo), R18 (custódia dupla da passphrase — regra zero, anterior a QUALQUER dado de cliente), R19 (um restore ensaiado + corrigir a linha do registro), banner de HISTÓRICO nos 14 arquivos de `abba-portal/materials/`.
5. **Fila contratual de programas** — uma cláusula/frase de proposta: kickoff de programa completo agendado com exclusividade de janela; segundo programa entra em fila com data. É a defesa contra o único cenário de escala que quebra a firma.
6. **Playbook de WhatsApp (v1 de uma página)** — primeira mensagem via indicação, áudio de 40s, cadência pós-proposta. É o canal onde a venda acontece e o único sem processo.
7. **Medir os dois custos cegos:** uma noite real do cérebro (R20) e uma execução do scout (custo por análise) — os dois números entram na planilha e fecham R9/R10/R20 junto com a decisão da via CrewAI.

## 6. O que está genuinamente bom (para não consertar o que funciona)

- **As duas suítes verdes** (429 + 801) — a base de código é sólida e testada nos dois repos vivos.
- **A doutrina comercial é rara**: coreografia, objeções, escada, protocolo de prova, jornada em 11 estágios com dono e checklist — a maioria das firmas de 10 anos não tem isso.
- **Honestidade estrutural**: zero clientes inventados, SLA realista, riscos com dono. É defensável em qualquer due diligence.
- **A marca agora existe e é coerente** (v4 em tudo: kit, posts, papelaria, perfis) — a lacuna "empresa sem cara" está fechada; falta apenas publicar.
- **Os gatilhos de contratação e o teto de recorrência já estão pensados** — o desenho de escala existe; falta o placar que o alimenta.

---

## 7. Proposta de 14 dias (cabe na agenda de 2 sócios)

| Dia | Ação | Dono | Custo |
|---|---|---|---|
| 1 | Aval do Pedro em bloco: marca v4 + headline + posts + menção CrewAI/João | Pedro | 1h de leitura do kit |
| 1 | ✅ **ASSUMIDO PELOS SÓCIOS (2026-08-19):** advogado e contador serão resolvidos por fora | Daniel + Pedro | — |
| 2 | ✅ **ASSUMIDO PELOS SÓCIOS (2026-08-19):** metas ano 1 + runway + células de capacidade serão preenchidos por fora | Daniel + Pedro | — |
| 2 | Custódia dupla da passphrase (regra zero) | Os dois | 30 min |
| 3 | Higiene técnica: R23 + banner nos materials/ + 1 restore ensaiado | Pedro | meio dia |
| 3 | Publicar: perfis + 3 posts (sequência curta) + fotos agendadas | Daniel | 2h |
| 4–8 | **Cliente Zero completo** ([runbook](cliente-zero-runbook.md)), com LLM real e uma noite do cérebro | Os dois | a semana |
| 9–10 | Corrigir o que o Cliente Zero quebrar; medir os 2 custos cegos; cronometrar a análise | Os dois | 1 dia |
| 11–14 | 20 alvos nomeados no Drive + primeiras 4 apresentações mornas pedidas via WhatsApp | Daniel | 2h + cadência |

No dia 14, o critério final do [plano de ação](plano-de-acao.md) fica com todas as caixas marcadas menos, no máximo, a jurídica — que não depende de vocês, só de cobrança.
