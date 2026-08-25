# Protocolo de Imersão — do contrato assinado ao primeiro dia de campo

> "O serviço é o processo de imersão." — Rafael (Brasal, 2026-08-18). O cliente não compra um relatório: compra a segurança de que já entramos em empresas bagunçadas e saímos com um caminho. Este protocolo é esse processo, escrito.

**Dono:** chapéu Entrega (Daniel conduz; Pedro é suplente) · **Vale para:** Avaliação de Prontidão standalone e primeira etapa do programa · **Par na ferramenta:** `abba kickoff <engajamento>` gera o Pacote de Imersão (checklist de documentos + mapa de entrevistas + status de cobertura) a partir do mesmo conteúdo deste protocolo.

A regra que organiza tudo: **a checklist de documentos chega ao cliente ANTES do kickoff, nunca durante.** Cliente que recebe a lista com uma semana de antecedência chega preparado; cliente surpreendido com 15 pedidos na primeira reunião trava o cronograma inteiro — e o prazo de 2–3 semanas prometido na proposta depende da agenda DELE, não da nossa.

---

## Visão geral — 3 fases

| Fase | Janela | O que acontece | Artefatos |
|---|---|---|---|
| **1. Pré-kickoff** | D-7 a D0 | Checklist de documentos enviada, participantes confirmados, entrevistas agendadas, engajamento provisionado | [checklist](checklist-documentos-assessment.md) · [e-mails 1–2](emails-imersao.md) · `abba kickoff` |
| **2. Kickoff** | D0 (Semana 0 da proposta) | Reunião de 60–90 min pelo [roteiro](kickoff-roteiro.md); pré-trabalho disparado | deck de kickoff · convites de pré-trabalho |
| **3. Campo** | Semanas 1–2 | Entrevistas por nível (fases 1→4 da ferramenta), documentos ingeridos, contradições viram follow-up | [mapa de entrevistas](mapa-de-entrevistas.md) · `abba questions --output` · `abba requests` |

O fechamento (síntese, relatório, workshop, validação, debrief) segue o [estágio 06](../02-jornada-do-cliente/06-avaliacao-profunda.md) — este protocolo termina onde a análise começa.

---

## Fase 1 — Pré-kickoff (D-7 a D0)

Tudo aqui roda em paralelo com o [estágio 05 — Onboarding](../02-jornada-do-cliente/05-onboarding.md); este protocolo detalha o que o estágio lista.

**D-7 (ou no dia da assinatura, o que vier primeiro):**
- [ ] E-mail 1 ([convocação](emails-imersao.md#e-mail-1)) ao patrocinador: pede (a) o ponto focal do cliente (quem agenda salas e cobra pendências internas), (b) a lista de participantes por nível, (c) confirmação das janelas de entrevista.
- [ ] E-mail 2 ([pedido de documentos](emails-imersao.md#e-mail-2)) com a [checklist de documentos](checklist-documentos-assessment.md) anexada, **separando "obrigatório antes do campo" de "desejável em até 30 dias"**. O campo não começa sem os obrigatórios; os desejáveis não seguram o cronograma.
- [ ] Engajamento provisionado na ferramenta: `abba client create` + `abba engagement create --profile <perfil-do-setor>` (o perfil ajusta as perguntas e os arquétipos de vazamento prioritários) — setup completo em [ferramenta-avaliacao.md](../06-ferramentas/ferramenta-avaliacao.md).
- [ ] `abba kickoff <engajamento> --output` rodado → Pacote de Imersão impresso para levar ao kickoff (é a versão viva da checklist, já filtrada pelo perfil do setor).
- [ ] Se o cliente veio do assessment gratuito: relatório público ingerido como ponto de partida (`abba ingest <relatorio> --level external --phase 0`) — ver [contrato de fronteira](../06-ferramentas/contrato-fronteira-gratuito-pago.md). Senão: `abba scout` com provedor de busca real.

**D-5 a D-2:**
- [ ] Ponto focal agenda as entrevistas conforme o [mapa de entrevistas](mapa-de-entrevistas.md) (quem agenda é o cliente, nas salas dele; nós damos o mapa e as janelas). Meta: agenda fechada ANTES do kickoff.
- [ ] Willing-area confirmada: qual área entra primeiro e qual NÃO entra (aval do diretor da área + equipe avisada — critério do Anexo I, ver [SOW](../03-comercial/contrato-sow-esqueleto.md)). Sem aval do diretor da área, aquela área sai do escopo — não se força imersão em território hostil.
- [ ] E-mail 3 ([lembrete D-3](emails-imersao.md#e-mail-3)) se os documentos obrigatórios ainda não chegaram.

**D0 (kickoff):** segue o [roteiro](kickoff-roteiro.md). Deste protocolo, entram no kickoff: o Pacote de Imersão impresso (checklist + mapa + agenda), a escalada de pendências (abaixo) e a regra de consentimento das entrevistas.

### Plano B — pré-trabalho e documentos não entregues

O pré-trabalho vale **/40 da pontuação** ([proposta §3](../03-comercial/proposta-avaliacao-prontidao.md)). Cliente que não entrega não recebe nota fabricada — recebe a nota real, com a lacuna nomeada.

1. **D-3:** lembrete ao ponto focal (e-mail 3).
2. **D0 (kickoff):** pendências apresentadas ao patrocinador ao vivo, sem constrangimento e sem drama: "estes itens seguram o início do campo".
3. **Campo:** não começa sem os itens **obrigatórios** da checklist. Se o patrocinador decidir começar assim mesmo, a decisão é dele, por escrito, e o relatório declara o que faltou (todo número tem premissa citada; premissa ausente é dita como ausente).
4. **Persistindo:** a pontuação de pré-trabalho é registrada como incompleta, com o motivo, por humano nomeado (`abba objective add --by` para o registro; nunca nota inventada). A cláusula de dependências da proposta cobre o replanejamento de prazo.

---

## Fase 2 — Kickoff (D0)

Já coberto pelo [roteiro de kickoff](kickoff-roteiro.md) (objetivos declarados ao vivo no slide 5, pré-mortem no 6b). O que este protocolo acrescenta:

- Objetivos declarados pela diretoria entram na ferramenta no mesmo dia: `abba objective add <eng> "<objetivo nas palavras deles>" --by "<quem declarou>"` — a cobertura objetivo↔build no relatório final depende disso.
- Convites de pré-trabalho disparados até D+1 (e-mail 4 do [pacote](emails-imersao.md#e-mail-4)).

---

## Fase 3 — Campo (Semanas 1–2)

O mapa completo (quem, quantas, quanto tempo, roteiro por nível) está em [mapa-de-entrevistas.md](mapa-de-entrevistas.md). As regras de condução:

**Consentimento e gravação.** Toda entrevista começa com o mesmo aviso, verbal e simples: quem somos, para que serve a conversa, que ela será gravada e transcrita para análise, que trechos podem aparecer no relatório de forma não nominal, e que a pessoa pode pedir para algo ficar de fora. Se a pessoa recusar gravação, a entrevista acontece com anotação manual — nunca se grava sem avisar.

**Ingestão no mesmo dia.** Toda entrevista e todo documento entram na ferramenta no dia em que chegam, com os quatro metadados:

```
abba ingest <eng> <arquivo> --level <nivel> --phase <fase> --attribution "Nome, Cargo" --date <AAAA-MM-DD>
```

Sem `--level`, a fonte fica **invisível ao detector de contradições** — e a contradição entre níveis É o assessment ("pergunte a mesma coisa a 3 níveis; os gaps são o diagnóstico"). Ingestão sem metadado é trabalho jogado fora.

**Meio do campo:** `abba questions <eng> --output` gera o guia da segunda rodada, dirigido pelas lacunas do que já foi ouvido. `abba requests list <eng>` mostra o funil de documentos pedidos e recebidos.

**Contradições viram follow-up, não constrangimento.** Quando o C-level diz "flui bem" e a linha de frente descreve a planilha paralela, isso vira pergunta de clarificação na próxima entrevista — nunca acareação.

### O wrapper humano (o que separa consultoria de produto)

Três momentos humanos que a ferramenta não substitui, e que fecham a lacuna nº 3 da [auditoria v2](../05-interno/auditoria-assessment-v2-2026-08-20.md):

1. **Protocolo de entrevistas entregue impresso** — o cliente vê método, não improviso (este documento + o mapa + o guia do `abba questions`).
2. **Workshop de briefing estratégico (3h)** — já no [estágio 06](../02-jornada-do-cliente/06-avaliacao-profunda.md).
3. **Sessão de validação de achados (90 min, antes do relatório final)** — os sócios apresentam as contradições detectadas e os achados preliminares ao patrocinador + 2–3 lideranças e pedem reação: "isto que ouvimos está certo? O que falta?" O que o cliente corrige entra como fonte (`--level c_suite --phase 4`); o que confirma vira evidência com dupla checagem. O relatório nunca é a primeira vez que o cliente vê os achados.

---

## LGPD em uma tela (o mínimo que todo condutor precisa saber)

Detalhe completo por tipo de documento na [checklist](checklist-documentos-assessment.md). O resumo:

- **Papel:** a ABBA atua como **Operadora** — trata dados sob instrução do cliente (Controlador), para a finalidade do contrato ([proposta §11](../03-comercial/proposta-avaliacao-prontidao.md)). Base legal do tratamento: execução de contrato; para dados de contato de participantes, legítimo interesse com transparência.
- **Minimização:** pedimos o agregado, não o nominal. Organograma com cargos serve; folha com salários individuais não. Ver a seção "não pedir / não receber" da checklist.
- **Rede de segurança não é licença:** a ferramenta redige CPF/CNPJ/e-mails automaticamente na ingestão, mas isso não autoriza receber o que não devíamos pedir.
- **Retenção e eliminação:** o prazo de retenção é o do contrato (registrado no engajamento); ao término, `abba forget` elimina e emite certificado com contagem de resíduo zero — que pode ser entregue ao cliente como prova.

---

## Encaixe na jornada

[04-contrato](../02-jornada-do-cliente/04-contrato.md) → **este protocolo (Fase 1)** → [05-onboarding](../02-jornada-do-cliente/05-onboarding.md) + [kickoff](kickoff-roteiro.md) (**Fase 2**) → **campo (Fase 3)** → [06-avaliacao-profunda](../02-jornada-do-cliente/06-avaliacao-profunda.md) (análise, workshop, validação, debrief).
