# Pesquisa: como o mercado faz e entrega assessments de IA

> Pesquisa de 2026-08-19 (Claude, buscas na web com fontes citáveis), feita a pedido do Daniel após a reunião com o Rafael (Brasal, 18/08). Alimentou o plano "Assessment v2" e as decisões de produto no assessment-brain. Regra da casa vale aqui também: **número só com premissa.**

## 1. As estatísticas de falha (o argumento de venda com fonte)

| Número | Premissa exata | Fonte |
|---|---|---|
| **~80% dos projetos de IA falham** | O dobro da taxa de falha de projetos de TI que não envolvem IA; causas dominantes são problema mal definido, dados insuficientes e foco em tecnologia em vez do problema | RAND Corporation, 2024 ("The Root Causes of Failure for Artificial Intelligence Projects") |
| **95% dos pilotos de GenAI sem retorno mensurável** | Pilotos corporativos de GenAI que não chegaram a impacto mensurável em P&L; a causa apontada é "learning gap" organizacional, não a tecnologia | MIT NANDA, 2025 ("The GenAI Divide: State of AI in Business") |
| **60% dos projetos abandonados até 2026 sem dados AI-ready** | Projeção: organizações sem dados prontos para IA abandonarão 60% dos projetos | Gartner, 2024 |
| **~2,6× mais chance de sucesso com avaliação formal de prontidão** | Organizações que fazem readiness assessment estruturado antes de implementar têm ~2,6x mais probabilidade de sucesso | Estudos de mercado citados em literatura de AI readiness (usar com o multiplicador aproximado, nunca como número exato) |

**A tese do Rafael (Brasal) confirmada pela pesquisa:** empresas querem IA embutida no negócio, mas a maioria dos projetos morre por falta de estruturação ANTES de começar. Fundação antes da obra. Isso virou produto: o **Veredito de Fundação de Dados** no relatório e no anexo visual.

## 2. O que os assessments do mercado entregam (e o cliente passou a esperar)

Padrões recorrentes em Gartner, McKinsey (QuantumBlack), Deloitte, BCG (GAMMA), Accenture e boutiques:

1. **Maturidade por pilar, em níveis nomeados** — tipicamente 5 a 6 pilares (estratégia, dados, tecnologia, talento/pessoas, governança, operação) × 5 níveis com nome (ex.: Awareness → Active → Operational → Systemic → Transformational, no modelo Gartner). Entregue como **radar**.
2. **Heatmap** das dimensões avaliadas — visão de uma página, cor por estado.
3. **Matriz valor × esforço** das iniciativas — o "low hanging fruit" que o Pedro já desenha à mão em reunião.
4. **Roadmap em 3 horizontes** (agora / 6 meses / 12+ meses) com donos nomeados.
5. **Business case por iniciativa** — custo, retorno, payback. (Quase ninguém mostra custo de operação/manutenção antes da assinatura — é a lacuna que a nossa seção "Contar o custo" ataca.)
6. **Problemas mais valiosos primeiro** — priorização explícita, não lista exaustiva.

**Diagnóstico honesto de onde a ABBA estava:** o assessment-brain já produzia substância que o mercado não tem (organismo, loops de decisão, contradições entre níveis hierárquicos, Breach Score, red-team, calibração ambição×prontidão). A lacuna NUNCA foi inteligência — era **tradução executiva e visual**. Relatório markdown denso ≠ o que um dono compra. Fechamos com: camada de maturidade (6 pilares ABBA × 5 níveis nomeados: Improvisado · Consciente · Estruturado · Instalado · Composto), veredito de fundação, reordenação narrativa (veredito em 60 segundos primeiro, riqueza como sustentação) e o **anexo visual de 7 páginas** (`abba report <eng> --visual`).

## 3. Sophy Works (sophyworks.ai) — o concorrente que impressionou a Brasal

Buscas na web + **primeira mão do Rafael na [reunião de 18/08](reuniao-rafael-brasal-2026-08-18.md)** (Brasal tem licença):

- Posiciona-se como **"Innovation OS"** — sistema operacional de inovação, não consultoria pontual. Fundador brasileiro, ex-Serpro, exits anteriores.
- **Modelo e preço:** SaaS **US$49/mês**, com opções on-premise e VPS (dedicado ou compartilhado). Site e produto **todos em inglês, preço em dólar** — decisão deliberada de posicionamento.
- Estrutura em **4 camadas: contexto → hipóteses → validação → entrega**, com rastreabilidade de decisão ponta a ponta ("você propôs X, mas o contexto de 2 anos atrás diz que impacta") e memória persistente de contexto.
- Foco real (segundo o Rafael): **gestão de produto** — discovery, planejamento, mapeamento de processos, arquitetura de projeto; no fim, o output vai para Claude Code/CrewAI construir.
- Vende avaliar hipóteses **"antes de ficarem caras"** (jobs-to-be-done, riscos, roadmap).
- **Lição principal:** o cliente compra um SISTEMA legível — soluções, estrada, maturidade, problemas mais valiosos primeiro — não um documento. A resposta da ABBA não é copiar o formato deles, é entregar a nossa substância (que é maior) com legibilidade equivalente.
- **Fronteira honesta:** a Sophy estrutura o problema por metodologia; o assessment ABBA entra com **dados reais da empresa** (entrevistas multi-nível + documentos) e sai com número, premissa e veredito de fundação. E o hand-off para construção que eles vendem, a ABBA já tem: `abba export --target crewai`. Tornar isso visível na venda.

**Aprofundamento 20/08 (buscas adicionais; site segue bloqueado no ambiente):** o produto se chama **aOS** e o coração é o **Decision Stack** — 4 camadas empilhadas como um sistema operacional (contexto na base → entrega no topo) rodando como **"living system, not a slide deck"**; a pergunta-mestra é **"why does this work exist — and is it still the right bet?"**; máxima de método: **"the first hypothesis is rarely the best one — it's just the fastest"**; ações nas IDEs (Claude Code, Cursor) **retroalimentam o Decision Stack**; transparência de custo até o token; sem tiers ou feature gating. Posicionamento: "clarity problem, not execution problem". Fontes: [sophyworks.ai](https://sophyworks.ai/) (via snippets de busca).

**O que a ABBA absorveu disso (2026-08-20, tudo no assessment-brain):** os 4 princípios de mercado do registro executável (`sistema-vivo-nao-slide`, `primeira-hipotese-mais-rapida`, `por-que-este-trabalho-existe`, `transparencia-de-custo` em `src/report/principles.js`) e o novo **`abba decision seed`** — as intervenções ranqueadas do assessment viram decisões `recommended` no cérebro (com evidência do vazamento como "porquê", trigger de revisão sugerido, outcome e Brier depois). O assessment deixou de morrer como documento: é o Decision Stack da ABBA, com a vantagem de nascer de dados reais.

## 4. O que virou produto (rastreabilidade das decisões)

| Achado da pesquisa | Decisão de produto | Onde vive |
|---|---|---|
| Radar de maturidade é a língua franca | `src/report/maturity.js` (agregação pura, sem LLM novo) + página 2 do anexo | assessment-brain |
| Heatmap de uma página | Página 3 do anexo (25 dimensões, cor por estado, marcador de confiança) | assessment-brain |
| Matriz valor×esforço | Página 4 do anexo (dados do Breach Score existente) | assessment-brain |
| Roadmap 3 horizontes | Página 5 (horizonte derivado de frontier-timing + payback; donos nomeados NA reunião) | assessment-brain |
| Ninguém mostra TCO antes da assinatura | Página 6 "Contar o custo" (payback simples vs. payback honesto) | assessment-brain + [princípios](../00-identidade/principios-do-assessment.md) |
| Fundação antes da obra (Rafael + RAND/Gartner) | Veredito de Fundação de Dados (FRÁGIL/PARCIAL/PRONTA) no relatório, capa do anexo e one-pager | assessment-brain |
| Cliente compra sistema legível | Reordenação narrativa do relatório: veredito em 60s → sumário → maturidade → fundação → achados → plano → apêndices | assessment-brain |

**Guarda-corpos mantidos:** prompts travados (`src/analysis/prompts.js`) intocados; tudo acima é agregação/apresentação pós-análise; toda visualização carrega nota de método ("derivado DESTA análise, não é benchmark de mercado"); nada vai a cliente antes do gate real do [Cliente Zero](cliente-zero-execucao.md).

## 5. O que ainda falta (Fase M — motor, decisão consciente, atrás de gate)

Quatro análises novas com LLM (sonda de fundação, narrativa "o que destrava o próximo nível", TCO assistido, gerador de roadmap) foram aprovadas pelo Daniel em 19/08 **sequenciadas DEPOIS da validação real** — entram em módulo separado (`assessment-v2-prompts.js`) atrás de flag `ABBA_ASSESSMENT_V2`, default off.

**Refino da transcrição Rafael/Brasal (chegou 19/08):** a sonda de fundação deve cobrir **dados E processos** — o padrão de campo é o processo quebrado aparecendo como dado ruim (dois departamentos com duas planilhas dos mesmos números de venda). E o gerador de roadmap deve considerar a **disposição da área para mudar** (aval do diretor + equipe alinhada) como critério de sequência, não só valor×esforço — "o humano no loop ou ajuda ou vira detrator". Insights completos: [reuniao-rafael-brasal-2026-08-18.md](reuniao-rafael-brasal-2026-08-18.md).
