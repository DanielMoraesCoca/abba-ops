# Estudo. Conselheiro Digital (o "JARVIS por cliente")

> **Status: ESTUDO CUMPRIDO (atualizado 2026-08-01)**: a aposta 5 foi construída (Fases 0–2 + Ondas 1–3). O inventário e o faseamento abaixo viraram **registro histórico de como decidimos**; o estado atual está no [plano](plano-implementacao-conselheiro.md). Banner original: *"estudo + aposta futura 5: nenhuma construção antes do gatilho"*. Ideia do sócio (2026-07-27): um assessor de IA por cliente que entende tudo da empresa, de nós e de si mesmo; aprende com os resultados reais ao longo do tempo; identifica melhorias proativamente; disponível ao cliente e à ABBA. Pesquisa diligente executada; veredito e faseamento abaixo. Registrado em [apostas-futuras](../00-identidade/apostas-futuras.md) (aposta 5) e no [registro de decisões](registro-de-decisoes.md).

## Veredito

**A ideia é boa, o mercado corre para ela (YC listou "Company Brain" nos pedidos de 2026) e a ABBA já tem ~60% construído.** Mas o formato viável: comercial, jurídica e psicologicamente, é o **modelo centauro**: o JARVIS serve o Tony Stark, não o substitui. A IA gera; o Conselheiro humano cura e assina; a diretoria decide. Nunca "IA aconselhando o board diretamente".

## Por que o formato centauro é obrigatório (3 razões)

1. **Regulatória:** o PL 2338 (lei de IA do Brasil, em tramitação) prevê responsabilidade civil objetiva e solidária para IA de alto risco, e sistemas que influenciam decisões empresariais flertam com essa classificação (multas até R$ 50 mi / 2% do faturamento). A exigência central é revisão humana de resultados relevantes: que já é o nosso princípio: *nós recomendamos, eles decidem*.
2. **Confiança:** um número alucinado num board deck não queima a ferramenta: queima a ABBA (casos reais: bot da Air Canada, jurisprudência inventada). RAG com fonte citada + curadoria + "não sei" honesto são inegociáveis.
3. **Técnica:** LLM não "aprende sozinho": o aprendizado real vem da arquitetura: **RAG** (base viva do cliente) + **memória estruturada** (dados mensais, decisões) + **loop de outcomes**. E o loop de outcomes **a ABBA já construiu**: o vault reconcilia confiança empírica por resultado real e aposenta padrões desmentidos (piso 0,25). É o núcleo que o mercado ainda está inventando.

## Inventário: o que já existe vs. o que falta

| Componente | Estado |
|---|---|
| Fotografia inicial completa da empresa | ✅ = a Avaliação de 25 dimensões |
| Conhecimento sobre a ABBA e sobre o próprio sistema | ✅ abba-ops + specs dos agentes |
| Dados reais contínuos | ⚠️ existem (relatório mensal projetado×realizado, telemetria CrewAI, adoção no portal) · falta unificar no **Dossiê Vivo** por cliente (base RAG) |
| Aprendizado com resultados | ✅ loop de outcomes do vault · falta a versão por-cliente |
| Interface de consulta para o cliente | ⚠️ embrião = **Iris** (já tem contexto por tenant no portal) |
| Identificação proativa de melhorias | ✅ **ENTREGUE** (2026-08-01): o ciclo noturno compara, consolida e rascunha o brief; playbooks nascem de vitórias medidas |
| Canal para a diretoria | ✅ o ritual do conselho (máx. 3 recomendações) · a IA abastece, nunca substitui |

## O ciclo em operação (desenho-alvo)

Dossiê Vivo (assessment + plano diretor + atas + relatórios + telemetria) → rotina mensal de análise gera candidatos a insight → **Conselheiro humano cura** → 3 recomendações no ritual → decisões e resultados voltam ao Dossiê → destilado **anonimizado e consentido** vai ao vault (o volante ganha segundo motor). Iris evolui para responder sobre a operação, com fonte citada.

## Regras de desenho (invioláveis)

- **Um cérebro por cliente, segregado**, nunca cruzar dados entre clientes; só o vault anonimizado cruza padrões
- On-premises disponível para quem exigir · nunca treinar modelos com dados do cliente (RAG consulta, não treina)
- Toda saída para a diretoria passa por curadoria e assinatura ABBA (blindagem PL 2338 + marca)
- Consentimento contratual explícito para a destilação anonimizada ao vault (pauta P4/advogado quando ativar)

## Faseamento (gatilhos, não datas)

| Fase | Gatilho | O que ativa |
|---|---|---|
| 0 (agora) | · | ~~Nada a construir~~ → **antecipado**: Fases 0–2 + Ondas 1–3 construídas em jul-ago/2026 por decisão do sócio. A disciplina segue valendo: estruturar todo dado de engajamento pensando no Dossiê |
| 1 | 1º cliente em manutenção | Dossiê Vivo interno + brief mensal gerado por IA, curado pelo sócio (uso interno; custo ~centenas de R$/mês) |
| 2 | 1º cliente na camada Estratégia | Insights proativos formais no ritual, co-assinados |
| 3 | 3+ clientes | Interface Iris-Empresa no portal, por tenant, com guardrails |
| 4 | 10+ clientes | Produto nomeado (candidato ao coração da tabela v3); naming = decisão de sócios |

**Custo real:** infra modesta; o trabalho é o encanamento de dados (~80%). **Retorno:** justifica a camada Estratégia, cria lock-in legítimo (o cérebro acumulado), diferencia de qualquer CAIO humano-só, e realiza tecnicamente a frase 18 da Visão 2029.

## Adendo (2026-07-27): investigação profunda do Meta-ANN do repo legado

Pergunta do sócio: usar o Meta-ANN (a rede meta-agêntica do repo ABBA) como o cérebro por cliente, no lugar do desenho acima? **Investigação completa executada** (varredura do master + 3 branches, ~200k linhas na área meta-ann/enterprise/ann/cognitive).

**Veredito: NÃO usar o Meta-ANN como plataforma. SIM para absorver 3 peças comprovadas dele no desenho do Conselheiro Digital.**

O que a investigação encontrou (verificado no código, não nos docs):
- **O loop de aprendizado nunca fecha:** `autoApply: false`; as funções de aplicar melhorias existem mas nunca são chamadas; o aplicador de feedback (559 linhas) não é importado por arquivo nenhum. Gera críticas; não aprende.
- **A memória MIRIX é write-only:** grava no Postgres mas NÃO tem caminho de leitura/hidratação: ao reiniciar, esquece tudo (as tabelas viram trilha de auditoria que o próprio sistema nunca relê).
- **Validação-teatro:** o validador da rede "mede" com `Math.random()` (taxa de sucesso hardcoded 0,996). O próprio repo criou o teste `no-theater` que PROÍBE o servidor real de importar esses módulos: o time quarentenou o Meta-ANN.
- **Nunca rodou em produção:** o deploy real sobe outro servidor, sem nenhuma rota Meta-ANN; a rota principal de geração nem existe como endpoint; K8s por cliente é template com imagem nunca construída; multi-tenancy instanciada só no próprio teste (e com API de MongoDB num codebase Postgres).
- **A decisão de 2026-07-22 (construção = CrewAI direto; ABBA = legado) fica CONFIRMADA pela evidência.**

As 3 peças reais que valem ser portadas (para o runtime CrewAI, nos gatilhos das fases):
1. **Loop de versão de prompt com aprovação humana e uplift medido** (`src/core/learning-*`: real, testado ponta a ponta): é exatamente o mecanismo de "aprimoramento" honesto e compatível com PL 2338 para a Fase 2 do Conselheiro Digital: propor → sócio aprova → medir.
2. **Pesos hebbianos de roteamento** (loop fechado real: recompensa → força de conexão → roteamento 70/30): padrão útil quando houver múltiplos agentes por cliente em produção (Fase 3+).
3. **A taxonomia de memória em 6 tipos do MIRIX** (migração 117: schema de nível de produção): informa o desenho do Dossiê Vivo (com a lição: persistência SÓ com caminho de leitura implementado e testado).

Pendências operacionais derivadas: (a) cherry-pick do doc `ABBA_COMPLETE_ASSESSMENT_FRAMEWORK.md` (1.469 linhas, só existe na branch `claude/meta-agentic-networks-vMbKU`, commit `4fa6814f`): preservar o IP; (b) avisar Pedro: o master do ABBA carrega `/api/backprop` quebrado e MIRIX sem hidratação montados no servidor legado (não deployado: risco baixo, mas decidir consertar ou desmontar).

## Adendo 2 (2026-07-29): a arquitetura completa do cérebro

Pergunta seguinte do sócio: os 4 quebrados podem ser reconstruídos certos? o que mais o Conselheiro precisa para ser o mais disruptivo possível. "um cérebro constantemente alimentado, aprendendo e descansando, num ciclo sem fim"? Três frentes de pesquisa profunda executadas (memória/sleep-time compute, auto-melhoria segura, mercado/moat). **Resposta consolidada em [`arquitetura-cerebro-conselheiro.md`](arquitetura-cerebro-conselheiro.md)**: o desenho-alvo do ciclo dia/noite (com base científica: sleep-time compute, ~5× mais barato e +13–18% de acurácia), a escada de melhoria em 4 degraus com 5 salvaguardas, os 7 stores de memória em Postgres, o custo (~US$ 10–40/mês por cérebro) e o veredito honesto de mercado ("ninguém tem" é falso como dito; a interseção operador-responsável + diário de resultados + assinatura humana + preço de cadeira de conselheiro está desocupada no mid-market BR). O faseamento por gatilho deste estudo permanece o mesmo.

**Sequência (2026-07-29):** o [plano de implementação](plano-implementacao-conselheiro.md) foi escrito e a Fase 0 entregue em código; o [estudo de engenharia das big techs](arquivo/estudo-big-techs-company-brain.md) foi consolidado e mergeado no plano (4 marcadores resolvidos, 8 adições, 3 rejeições conscientes).

## Fontes

- [Y Combinator/Company Brain: a camada de dados decide tudo](https://colrows.com/blogs/company-brain-for-enterprise-ai/) · [Enterprise AI 2026. TechRadar](https://www.techradar.com/pro/2026-the-year-enterprise-ai-finally-gets-to-work) · [Previsões CIO 2026. InformationWeek](https://www.informationweek.com/machine-learning-ai/2026-enterprise-ai-predictions-fragmentation-commodification-and-the-agent-push-facing-cios)
- [RAG vs fine-tuning. Databricks](https://www.databricks.com/blog/rag-vs-fine-tuning) · [AI Memory vs RAG vs Knowledge Graph. Atlan](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/) · [RAG vs memória de agentes. Mem0](https://mem0.ai/blog/rag-vs-ai-memory)
- [PL 2338: visão geral](https://regulations.ai/regulations/RAI-BR-NA-SUMMARY-2026) · [PL 2338: análise MAIEI](https://montrealethics.ai/ai-policy-corner-how-brazil-plans-to-govern-ai-reviewing-pl-2338-2023/) · [Regulação de IA no Brasil. CMS](https://cms.law/en/int/expert-guides/ai-regulation-scanner/brazil)
- [Alucinações de IA em negócios. IntuitionLabs](https://intuitionlabs.ai/articles/ai-hallucinations-business-causes-prevention) · [Ceticismo e confiança em AI advisors: arXiv](https://arxiv.org/pdf/2606.23491)
