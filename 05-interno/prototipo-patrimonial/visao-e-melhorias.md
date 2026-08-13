# Arquiteto Patrimonial — Visão do Produto e Roadmap de Melhorias

> **Camada:** interno (produto + engenharia). Companheiro do [`produtizacao.md`](produtizacao.md) (plano de negócio) e do [`plano-de-construcao.md`](plano-de-construcao.md) (o mestre). Este documento responde três perguntas: **o que a ferramenta é**, **onde ela pode chegar**, e **o que falta para ela chegar lá** — com fontes. Escrito em 2026-08-13, depois do deploy vivo no CrewAI AMP.
>
> Origem: pedido do sócio — "explique como se eu não soubesse de nada o que essa ferramenta faz, o potencial, quem usa; e pesquise as brechas de melhoria, para o usuário e para nós, já que estamos fazendo dentro da CrewAI".

---

## Parte 1 — O que é (do zero)

### A dor
Uma família rica ou um empresário com patrimônio dentro e fora do Brasil (imóveis, empresas, aplicações no exterior, herdeiros em países diferentes) tem duas perguntas que tiram o sono: **(1)** como organizar isso para pagar o imposto certo — não mais que o devido — e passar aos filhos sem guerra e sem perder metade em imposto de herança; **(2)** como fazer tudo **100% na lei**, agora que o Brasil fechou o cerco (Lei 14.754/2023, CRS com 100+ países, DCBE). Hoje quem resolve isso são escritórios caros e artesanais: leva **semanas**, e a qualidade depende de qual advogado pegou o caso.

### A frase de uma linha
**Um sistema de apoio que transforma o perfil completo de uma família em minutas de planejamento patrimonial internacional — 100% declaradas e tributadas, com a fonte (a lei exata) citada em cada afirmação e os riscos já atacados — para um advogado nomeado revisar, editar e assinar.** Faz em ~1 hora, com mais consistência, o que hoje leva semanas — e **recusa, por desenho, o caso que nenhum especialista sério deveria aceitar**.

Não é "IA que faz planejamento patrimonial". É a ferramenta do profissional. **A IA propõe; o advogado assina.** Desenho jurídico é ato privativo de advogado (EOAB) — o produto nunca dá conselho ao leigo. Chamamos isso de *modelo centauro*.

### O pipeline (as 7 estações — o que foi projetado)
1. **Intake** — o profissional preenche o perfil (ou sobe documentos do cliente).
2. **🚦 Gate de conformidade** — filtro automático de red flags. Caso podre (dinheiro não declarado, interposta pessoa, fraude a credores, supressão de legítima, KYC falho, recusa de transparência) → **para e diz NÃO**, com o motivo e a lei. Não desenha sobre caso sujo.
3. **Análise** — três analistas de IA (tributário BR, sucessório, jurisdições) leem o corpus e produzem os fatos **com a fonte citada**.
4. **Desenho** — um arquiteto propõe 2–3 estruturas; um **crítico adversarial** ataca cada uma e descarta as de falha fatal.
5. **Obrigações e cenários** — cálculo determinístico (15% controlada, DCBE, ITCMD, custo em 5/10 anos).
6. **🧑‍⚖️ Gate humano** — o advogado revisa, edita, aprova ou rejeita. Nada sai sem ele.
7. **Minuta** — documento final + trilha de auditoria (versão do corpus, fontes, quem aprovou).

### O que faz HOJE vs. o que foi projetado (a honestidade)
**Vivo e provado ao vivo no AMP (2026-08-12):**
- ✅ Todo o esqueleto/orquestração (o Flow) deployado e Online.
- ✅ O **🚦 gate de conformidade** — a estação 2 — provado ao vivo, determinístico, **custo zero de LLM** (`usage_metrics:null`). É o coração da confiança do produto.
- ✅ Cálculo de obrigações/cenários (estação 5) implementado; proteções (anti-citação-inventada, anti-linguagem-de-ocultação, mascaramento de PII) no código.

**Construído, mas INERTE — esperando uma peça:**
- ⏸️ Estações 3, 4 e 7 (análise, desenho, minuta) estão cabeadas e prontas, mas **paralisadas** porque falta o **corpus jurídico ingerido**. Um caso *limpo* rodaria até ali e pararia. O corpus é curadoria de advogado — o gargalo humano.
- ⏸️ O app (tela do profissional, contas, fila de revisão) é esqueleto.

**Tradução:** hoje temos uma máquina que **já sabe recusar o caso errado, ao vivo**, e todo o resto montado esperando a única peça que só um humano destrava — **um advogado curando o corpus**.

### O potencial
1. **Existe uma camada vazia no mercado.** De um lado, boutiques que vendem no "confia em mim"; do outro, executores fiduciários que só implementam. **No meio — o desenho fundamentado e verificável — não há ninguém no Brasil.** É onde o produto vive: onde os outros pedem confiança, ele entrega **prova** ("show me", não "trust me").
2. **A regulação criou a demanda.** A Lei 14.754/2023 matou o produto antigo ("não aparecer") e criou um novo: planejamento **declarado, complexo e recorrente**.
3. **A categoria vale bilhões nos EUA** (Wealth.com US$65M, fundada por brasileiros; Vanilla ~US$85M) — **todas B2B**. Sem equivalente brasileiro.
4. **Mercado mensurável:** ~386 mil milionários no Brasil, investimento PF no exterior dobrou em 2024, grandes fortunas > R$3 tri.

### Quem usa e como ajuda
- **Usuário direto = o profissional** (advogado/contador/planejador). Produz em 1h o que levava semanas, com consistência; **retém e cresce a carteira**. Cada saída sai com o nome e a OAB dele — mais forte, não substituído.
- **Cliente final (indireto)** = a família. Plano legal, mais rápido, mais barato, filtrado contra ilegalidade.
- **ABBA** = dona do método, do corpus e da métrica de prova. B2B SaaS; ativo que prova a tese "nosso lugar é a camada de método + prova + governança".

---

## Parte 2 — Brechas e melhorias (dentro da CrewAI)

> Pesquisa externa concluída (CrewAI, legal-RAG, comparáveis) — fontes ao final. Descoberta-âncora: **a fundação já está no padrão certo**. As melhorias são amadurecimento, não conserto.

### O que já acertamos (verificado contra o estado da arte)
- ✅ **Guardrail anti-citação-inventada já é nativo** (roda como `guardrail` de task com output tipado) — apontado pelos estudos de legal-RAG como *o* controle mais importante (sistemas ainda inventam 13–21% das citações mesmo com RAG).
- ✅ **Memória adaptativa DESLIGADA** — confirmado como a decisão certa de LGPD; o estado do caso (`@persist`) é a memória certa (escopada, apagável via `abba forget`).
- ✅ **Gate humano obrigatório + centauro** — o controle exato contra exercício ilegal (a ABA cataloga 150+ casos de IA alucinando em petições; o gatilho é sempre "confiou sem revisão").
- ✅ Determinístico onde é regra, agêntico onde é julgamento · `@router` · saídas tipadas entre crews.

### Brechas para o USUÁRIO FINAL (o profissional)
1. **[P1] Upload de documento → extração por IA → perfil pronto.** Todos os comparáveis (Wealth.com/Ester, Vanilla, Luminary, FP Alpha) lideram com isto — o "aha" de adoção. Hoje temos o RAG do corpus, não a extração dos documentos do cliente. É a maior brecha de produto e a que mais converte.
2. **[P1] "Clique na afirmação → veja a fonte".** O que faz um advogado assinar. Temos o `chunk_id` do lado do corpus; falta levar a mesma UX para a tela.
3. **[ganho rápido] Velocidade como vitrine.** A Vanilla vende "em minutos". Medir e mostrar o tempo por caso.
4. **[P1 — o fosso] Monitoramento de mudança de lei / evento de vida.** Minuta única é transação; monitoramento é assinatura. Quando uma norma do corpus é revogada (`superseded_by`), listar todos os casos que a citaram → "precisa de revisão". Reusa a disciplina bitemporal que a ABBA já tem no cérebro. Provavelmente nenhum concorrente BR tem.
5. **[depois] Visualização da estrutura** (diagrama que o advogado mostra ao cliente) — Luminary retém advisors assim.

### Brechas para NÓS (quem constrói e opera)
1. **[P1] Gate humano assíncrono.** Hoje o `@human_feedback` é síncrono/console; num produto REST, o advogado fechar a aba mataria a execução. Padrão certo: pausa → persiste → `Flow.from_pending(flow_id).resume()`. Já anotado como TODO no nosso código.
2. **[P1] Corpus bitemporal com filtro "na data do caso".** A falha nº1 de legal-RAG é lei válida no passado apresentada como atual. Já desenhamos `FrescorDoc`; falta ligar o filtro por data (chunk vencido só com flag "histórico"). Destrava segurança contra lei velha **e** o motor de retenção.
3. **[P1] Citação a nível de trecho.** Hoje verificamos que o `chunk_id` foi recuperado; o próximo nível é verificar que o texto citado **está contido** no chunk (existe alucinação "com cara de citação").
4. **[P1] Abstenção estrutural.** Corpus não cobre → o sistema é *obrigado* (guardrail) a marcar "não coberto — requer autoridade do profissional", em vez de inventar. Abster-se não é falha; é a devolução ao humano.
5. **[P1] GO/NO-GO como teste contínuo (CI).** Já temos o golden set de 12 personas e os 7 critérios. Rodar como portão de CI (DeepEval), julgando com **modelo de família diferente** do que gera (anti-auto-favorecimento).
6. **[ganho rápido → P1] Guarda de custo no Flow + observabilidade.** `step_callback` que soma tokens e aborta ao estourar `teto_usd_caso` (mesmo padrão do `--max-usd` do cérebro) + Langfuse desde o dia 1.
7. **[P1] Isolamento multi-tenant no vetor.** Corpus de leis = compartilhado (só-leitura, versionado); documentos do cliente = por-tenant (isolados). **Não misturar no mesmo índice** (qualidade de busca + LGPD). Auditar que o vetor entra na cascata do `abba forget`.
8. **[P1 — controle anti-UPL] Gate humano impossível de pular no grafo.** Garantir que nenhum caminho chega à saída final sem passar pelo nó de aprovação.

### Legal-RAG — práticas que reforçam a confiança
- **Cite a fonte exata** (o nosso `chunk_id`-só-se-recuperado é estado da arte) — reforçar com contenção a nível de trecho.
- **Detecte lei revogada** (corpus vivo com `valid_from`/`valid_to`/`superseded_by`; filtro por data-do-caso).
- **Abstenha-se estruturalmente** quando o corpus não cobre — não por instrução de prompt, por guardrail.
- **Recuperação híbrida/por jurisdição** [depois] — estruturas internacionais cruzam jurisdições; jurisdição como filtro duro de metadado já ajuda.

### Como os comparáveis retêm (mecânica transferível)
| Produto | Mecânica de confiança/retenção |
|---|---|
| Wealth.com / Ester | Lê e extrai de documentos → insights estruturados revisáveis; vendido embutido no desktop do advisor |
| Vanilla (V/AI) | Resumo do espólio "em minutos"; import auto-propaga campos extraídos |
| Luminary | Modelagem de cenários + visualização — o que o advisor mostra ao cliente |
| FP Alpha | Estate Lab projeta crescimento + imposto sucessório |
| Estateably | Formulários atualizados em tempo real quando a regulação muda (retenção via "corpus vivo") |

**Prioridades de retenção:** upload→extração→perfil (a porta), source-linking na UI, velocidade como headline, e **monitoramento de mudança de lei** (o motor de assinatura).

### Riscos e mitigações (dentro do Flow)
| Risco | Mitigação no Flow |
|---|---|
| Alucinação de citação | Guardrail anti-órfã com retry + contenção a nível de trecho |
| Lei revogada | Corpus bitemporal + filtro por data-do-caso; varredura de obsolescência |
| Sobre-alcance além do corpus | Abstenção estrutural (guardrail), não prompt |
| Propagação de erro entre agentes | Saídas tipadas por etapa + passe cético antes do gate humano |
| UPL / EOAB | Centauro + gate humano **não-burlável no grafo**; "assinado pelo profissional, nunca conselho ao leigo" |
| Estouro de custo | `step_callback` com teto por caso + `max_rpm`/`max_iter` + retries limitados |
| LGPD | Memória OFF; namespaces por tenant; vetor na cascata do `forget` |
| Viés de LLM-juiz | Juiz de família diferente no CI; métricas segmentadas, nunca um número agregado |

### A única sequência que importa
Quase tudo acima é Fase 1 — mas **todas essas melhorias vivem atrás do corpus real**. Sem o corpus curado pelo advogado nomeado (Héctor), o RAG não recupera nada, e não há o que citar, verificar, datar ou monitorar.

> **O corpus não é uma tarefa a mais na lista. É o gargalo que libera a lista inteira.** Próximo passo real: o [briefing de curadoria do corpus](briefing-corpus-hector.md).

---

## Fontes da pesquisa
CrewAI: human-feedback-in-flows; async HITL (crewAI #2051); Knowledge + bug de metadados (#1757); Tasks/guardrails; Testing (test exige OpenAI, #2067); Memory; Agents v1.15.2; AMP intro. Avaliação/observabilidade: DeepEval (integração CrewAI, LLM-as-judge); Langfuse (integração CrewAI); mem0. Legal-RAG: LegalCiteBench; Citation Grounding; Mojar legal-RAG guide; Vaquill. Falhas/UPL: LegalHalluLens; QuisLex (5 modos de falha); ABA UPL; human-on-the-loop. Comparáveis: Wealth.com/Ester; Vanilla V/AI; Luminary; FP Alpha; Estateably.

*(URLs completas no registro da sessão; docs.crewai.com/deepeval.com estavam bloqueados por egresso e foram corroborados por GitHub/comunidade/tutoriais — verificar assinaturas de método contra a versão instalada antes de codar.)*

## Ligações
[Produtização](produtizacao.md) · [Plano de construção](plano-de-construcao.md) · [Corpus](corpus-conhecimento.md) · [Briefing do corpus (Héctor)](briefing-corpus-hector.md) · [Avaliação e métrica](avaliacao-e-metrica.md) · [Registro de decisões](../registro-de-decisoes.md)
