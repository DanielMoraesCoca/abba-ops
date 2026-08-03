# Estudo — Por que a ABBA sobrevive ao diretor de IA interno (e como parar de ouvir essa objeção)

> **Camada:** interno. Origem: pedido do sócio (2026-08-03) — *"ver dentro do nosso negócio o que nós podemos [usar para] destruir o argumento deles baseado no que nós genuinamente temos... e pesquisar como melhorar o que já temos para que esse tipo de discurso não venha mais na nossa frente"*.
>
> **Este documento não é discurso** — o discurso de mesa está na [objeção: diretor de IA](../03-comercial/objecao-diretor-de-ia.md). Este é o entendimento por baixo dele: o inventário honesto do que temos que um diretor interno **estruturalmente não consegue ter**, o inventário igualmente honesto de onde morreríamos, e as mudanças que tiram a ABBA da rota de colisão com o CAIO — pesquisadas, com fonte.
>
> Regra do repo vale aqui: número sem fonte não sobe para material de cliente; itens {{A VERIFICAR}} não viram slide.

---

## 1. O que a pesquisa diligente encontrou (com as fontes)

| Achado | Número | Fonte | O que significa para nós |
|---|---|---|---|
| Pilotos internos de IA generativa com **zero impacto mensurável no resultado** | 95% (MIT Projeto NANDA, jul/2025) · 80,3% sem valor mensurável (RAND) | [MIT/Yahoo Finance](https://finance.yahoo.com/news/mit-report-95-generative-ai-105412686.html) · [Pertama Partners](https://www.pertamapartners.com/insights/ai-project-failure-statistics-2026) | A falha dominante não é modelo — é **ausência de métrica definida antes, dono claro e integração de fluxo**. É literalmente o que o [protocolo de prova](../04-entrega/protocolo-de-prova.md) instala |
| **Comprar de parceiro especializado dá certo ~67% das vezes; construção puramente interna, ~1/3 disso** | 2× a favor do externo | mesmo estudo MIT NANDA ([análise](https://www.thedataexperts.us/writing/enterprise-ai-failure-crisis-95-percent-failure-rate.html)) | O dado que desmonta "fazemos por dentro" **sem atacar ninguém**. É o número mais importante deste estudo |
| Patrocínio executivo **evapora em 6 meses** em 56% dos casos de falha | 56% | [Institute PM](https://www.institutepm.com/knowledge-hub/why-enterprise-ai-pilots-fail) {{A VERIFICAR fonte primária}} | O diretor de IA sozinho não segura o patrocínio — cadência externa com número (nosso ritual) segura |
| **CAIOs saem em ~18 meses**; o cargo frequentemente se dissolve em 2 anos — o descompasso expectativa×realidade é a causa nº 1 | 18 meses | [Forbes/Bernard Marr](https://www.forbes.com/sites/bernardmarr/2025/03/06/the-ai-leadership-crisis-why-chief-ai-officers-are-failing-and-how-to-fix-it/) | O diretor de IA médio **vai embora antes das fundações darem fruto — e leva o contexto na cabeça**. Nossa memória institucional é o contra-ativo exato |
| Empresas **com** CAIO reportam ~10% mais ROI em IA (IBM, 2.300 orgs) | 26% têm CAIO (2025), 2,4× em 2 anos | [Jeff Winter Insights](https://www.jeffwinterinsights.com/insights/the-chief-ai-officer-role) | Confirma a doutrina da [objeção](../03-comercial/objecao-diretor-de-ia.md): o CAIO é **bom para nós** — empresa com ele mede mais, compra melhor. Nunca vender contra |
| **ISO/IEC 42001** (gestão de IA): certificação exige **organismo certificador externo acreditado** — e já aparece como exigência em contratos B2B e compras públicas; ABNT NBR publicada em 2024 | — | [Vanzolini](https://vanzolini.org.br/noticias/iso-42001/) · [IBGIA](https://ibgia.org/en/blog/iso-42001-eu-ai-act-certificacao-governanca-ia-vantagem-competitiva-2026) · [BSI](https://www.bsigroup.com/pt-BR/products-and-services/standards/iso-42001-ai-management-system/) | **Um diretor interno não pode se autocertificar.** A verificação externa é exigência estrutural crescente — não uma opinião nossa |
| **PL 2338** (Marco Legal da IA): aprovado no Senado, votação final na Câmara em 2026; modelo por risco; sanções de até **R$ 50 mi** por infração | — | [Senado](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233) · [Câmara](https://www.camara.leg.br/noticias/1159193-projeto-que-regulamenta-uso-da-inteligencia-artificial-no-brasil) · [Entercast](https://www.entercastconsulting.com.br/blog/marco-legal-ia-brasil-votacao-camara-maio-2026) | Sistemas de alto risco terão obrigação de governança/avaliação — **demanda por avaliação independente que existe independentemente do organograma do cliente**. Já está no nosso [calendário de obrigações](estudo-antecipacao.md) §5 |

**Síntese da pesquisa em uma frase:** o mundo está indo na direção em que **ter um diretor de IA e contratar verificação externa não são alternativas — são complementos obrigatórios**, exatamente como ter contador interno nunca dispensou auditoria externa.

---

## 2. O arsenal genuíno — o que temos que ele não consegue ter

Classificado com honestidade: **[ESTRUTURAL]** = impossível para um interno por definição, não por competência · **[CONSTRUÍDO]** = existe em código/processo hoje, verificável · **[POSIÇÃO]** = estruturalmente nosso, mas vazio até termos clientes.

### (a) [ESTRUTURAL + CONSTRUÍDO] A independência com trava de engenharia — o argumento mais forte que temos

Um diretor de IA **não pode auditar a si mesmo**. Quando ele apresenta o resultado da própria iniciativa ao conselho, ele está defendendo o próprio orçamento — todo conselho sabe disso. É a razão pela qual empresa com CFO contrata auditoria externa e empresa com jurídico interno contrata parecer independente.

O nosso diferencial não é dizer isso — é que **o nosso sistema é fisicamente construído contra a autoavaliação complacente**, e dá para mostrar na tela:

- Probabilidade declarada em recomendação é **imutável** (`PREDICTION_ALREADY_DECLARED`): ninguém reescreve um 60% para 95% quando o rollout vai bem. Prever depois de medir é bloqueado (`PREDICTION_TOO_LATE`).
- Resultado só entra **medido e assinado por humano nomeado** — não existe "deu certo" sem número e sem nome.
- Resultado ruim **não é apagável**: supersessão nunca deleta; a linha do tempo inteira fica auditável (bitemporal).
- A auditoria noturna sonda a **coerência** da própria memória e o resultado é uma leitura, não uma nota que a gente se dá.

Nenhum time interno tem — nem tem incentivo para construir — um sistema que o impeça de maquiar o próprio placar. 429 testes e 7 rodadas adversariais atrás disso ([dossiê](../04-entrega/dossie-vivo-conselheiro-digital.md)). **Este é o núcleo da categoria em que devemos nos posicionar (ver §4.1).**

### (b) [ESTRUTURAL] A posição transversal — ele vê N=1 para sempre

O melhor diretor de IA do Brasil, dentro de uma empresa, vê **uma** empresa. A pergunta que ele nunca vai responder sozinho: *"estamos bem comparados a quem?"*. Benchmark recíproco, cofre de padrões e playbooks de vitórias medidas são [POSIÇÃO]: a mecânica está construída e é lícita por desenho (anonimizado + Anexo IV), mas **está vazia hoje** — piso de 5 clientes para a régua, 3 para padrões úteis. Não é argumento de venda presente; é a razão estrutural pela qual essa objeção **enfraquece a cada cliente nosso** em vez de fortalecer.

### (c) [CONSTRUÍDO] A memória que não pede demissão — casada com o dado dos 18 meses

O CAIO médio sai em ~18 meses — antes das fundações darem fruto — e o contexto vai na cabeça dele. O que fica na empresa quando o nosso conselheiro está lá: fatos com origem e vigência, diário decisão→resultado, dossiê compilado — **ativo da empresa, exportável em formato aberto**. A frase honesta: *"o seu diretor de IA é excelente e o mercado sabe disso — em dólar. O que a gente instala é o que fica quando qualquer pessoa sai."* Isso soma com o diretor, não compete.

### (d) [CONSTRUÍDO] A disciplina que os 95% não tiveram

As causas de falha do MIT/RAND — métrica ausente antes de começar, dono indefinido, patrocínio que evapora — são, ponto a ponto, o que o [protocolo de prova](../04-entrega/protocolo-de-prova.md), o kickoff com pré-mortem e o [ritual semanal](../04-entrega/ritual-semanal.md) tratam. E o dado dos **67% externo vs. ~22% interno** é a resposta de uma linha para "fazemos por dentro". Um diretor de IA que conhece esses números (os bons conhecem) **quer** um parceiro de execução — é assim que ele não vira estatística dos 18 meses.

### (e) [CONSTRUÍDO] Ferramentas prontas contra o funil de contratação dele

No dia 1 chegamos com avaliação instrumentada (25 dimensões), portal de capacitação e esteira de construção. O caminho dele: 6+ meses contratando num mercado onde 98% relatam escassez, pagando prêmio, competindo com vaga remota em dólar.

### O mapa do confronto, em uma tabela

| O argumento deles | O contra-ativo genuíno | Classe |
|---|---|---|
| "Já temos quem cuide de IA" | Cuidar ≠ verificar. Autoavaliação não passa em conselho, banco, certificadora nem no PL 2338 | ESTRUTURAL |
| "Ele define nossa estratégia de IA" | Ótimo — estratégia é dele. Execução em escala (67% vs 1/3) e prova independente são o que ele não fabrica sozinho | CONSTRUÍDO |
| "Ele conhece nossa empresa melhor que vocês" | Verdade — e em ~18 meses esse conhecimento historicamente vai embora com ele. O nosso fica em ativo exportável | CONSTRUÍDO |
| "Contratar vocês é admitir que ele falhou" | Inverso: empresa com CAIO tem ~10% mais ROI justamente porque compra melhor. Nós somos o que ele compra para não virar estatística | ESTRUTURAL |
| "Vocês nunca fizeram isso" (a mesa vira) | **Aqui não temos resposta boa hoje.** Ver §3 | — |

---

## 3. Onde morreríamos — sem anestesia

1. **"Me mostra um caso."** Zero clientes, método validado em sintético, cérebro sem noite real de produção. Contra um diretor de IA cético, o discurso inteiro desmonta aqui. Único remédio: o Cliente Zero completo com LLM real, publicado com acertos E erros (melhoria nº 8 do [parecer do conselho](parecer-conselho-2026-08.md) — as 7 lentes concordaram).
2. **O diretor de verdade, com equipe e métrica.** Existe (raro no nosso porte) o CAIO que já mede, já tem braços e já tem governança. Para ele, hoje, temos pouco: benchmark vazio e construção que ele talvez não precise. Resposta honesta: **não é alvo hoje** — cai nos critérios de recusa do [alvo](../00-identidade/alvo.md) como cliente sem dor compatível. Perder essa mesa rápido e bem é vitória.
3. **Nossas próprias incoerências na frente de um leitor técnico.** Um diretor de IA lê a proposta com lupa: a seção 8 ("5 papéis") cai na primeira pergunta; benchmark prometido sem coorte cai na segunda. As correções já estão ranqueadas pelo conselho — executá-las é pré-requisito para sentar nessa mesa.
4. **Prometer contra ele em vez de para ele.** Se qualquer material nosso soar "você não precisa de um diretor de IA", perdemos as duas pontas: quem tem um (ofendido) e quem quer ter um (assustado). A [objeção](../03-comercial/objecao-diretor-de-ia.md) §6 já proíbe; vale auditar materiais futuros por isso.

---

## 4. As melhorias para essa objeção parar de aparecer (ranqueadas)

A objeção aparece porque hoje entramos na mesa como **"consultoria de IA"** — mesma prateleira do diretor. A saída não é discurso: é **mudar de prateleira**.

| # | Melhoria | O que muda | Esforço | Gate |
|---|---|---|---|---|
| 1 | **Reposicionar a categoria: camada independente de prova + músculo de execução** — nunca "sua estratégia de IA". Auditar posicionamento/kit/deck para que a primeira frase nunca dispute a cadeira do CAIO; a analogia-mestre é auditoria externa: ninguém diz "temos CFO, não precisamos de auditor". ✅ **EXECUTADA 2026-08-03 (V3c)**: [posicionamento](../00-identidade/posicionamento.md) ganhou a seção "A prateleira" (com a regra da palavra "auditoria" — analogia sim, categoria não — e o encaixe da capacitação), headline/15s/45s/Sobre reescritos, kit 30s/3min/roteiro do deck atualizados, diferencial 6 no plano de negócio | A objeção deixa de fazer sentido semanticamente | Baixo (texto; eu executo mediante aprovação) | — |
| 2 | **Mapear as 25 dimensões → ABNT NBR ISO/IEC 42001 + PL 2338** — a avaliação passa a entregar, de brinde, o gap-assessment do padrão que contratos B2B começam a exigir e da lei que vem aí. **Nunca prometer certificação** (não somos organismo acreditado) — preparamos para ela. ✅ **EXECUTADA 2026-08-03**: [mapa](../06-ferramentas/mapa-avaliacao-iso42001-pl2338.md) (dimensão a dimensão + 10 perguntas suplementares + entregável de 1 página) | A avaliação vira algo que o próprio diretor de IA **pede** — ele precisa desse mapa para o conselho | Médio (doc de mapeamento) | Restam: adquirir o texto ABNT p/ conferência fina · revisão quando o PL sancionar |
| 3 | **Batizar e vender o placar de calibração como produto da independência**: "toda recomendação nossa carrega probabilidade declarada que não pode ser reescrita" — mostrado na tela, com as travas | O único fornecedor cujo sistema o impede de maquiar o próprio placar | Baixo (já construído; falta a narrativa no kit) | Honestidade: placar consolidado só com massa (10+ clientes) — vender a **trava**, não o histórico |
| 4 | **Linha de oferta "o sucesso do seu diretor de IA"**: variante do programa onde os entregáveis nascem dentro da estrutura DELE (ele é o campeão formal, dossiê no nome da área dele, capacitação da equipe dele) | Transforma o dono da objeção em comprador nomeado | Baixo-médio (variante de proposta) | Decisão de sócios |
| 5 | **Portabilidade como cláusula padrão** (exportação em formato aberto na saída, sem custo) — o CTO do conselho apontou: ninguém oferece | Mata "ficar refém" e "interno retém conhecimento" numa cláusula | Baixo (contrato — junto do advogado P4) | P4 |
| 6 | **Cliente Zero publicado** (reforço — já é a melhoria nº 8 do conselho) | A única resposta real para "me mostra um caso" | Alto | Já planejado |

**O que NÃO fazer (pesquisado e decidido):** não viramos organismo certificador (acreditação é outro negócio); não viramos CAIO fracionário genérico disputando com a Chiefs.Group por hora-homem — nosso Conselheiro se diferencia pela memória instrumentada e pelo placar com trava, não pelo currículo de uma pessoa; e não usamos os números deste estudo em material de cliente sem a fonte junto (doutrina do repo).

---

## Ligações

[Objeção: diretor de IA](../03-comercial/objecao-diretor-de-ia.md) — o lado de mesa deste estudo · [Parecer do conselho](parecer-conselho-2026-08.md) — as correções pré-requisito (§3.3) · [Protocolo de prova](../04-entrega/protocolo-de-prova.md) · [Dossiê do Conselheiro](../04-entrega/dossie-vivo-conselheiro-digital.md) — as travas citadas no §2a · [Estudo de antecipação](estudo-antecipacao.md) §5 — o calendário regulatório · [Alvo](../00-identidade/alvo.md) — quando a resposta certa é recusar
