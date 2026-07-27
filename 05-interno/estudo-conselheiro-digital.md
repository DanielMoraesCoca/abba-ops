# Estudo — Conselheiro Digital (o "JARVIS por cliente")

> **Status: ESTUDO + APOSTA FUTURA 5 — nenhuma construção antes do gatilho.** Ideia do sócio (2026-07-27): um assessor de IA por cliente que entende tudo da empresa, de nós e de si mesmo; aprende com os resultados reais ao longo do tempo; identifica melhorias proativamente; disponível ao cliente e à ABBA. Pesquisa diligente executada; veredito e faseamento abaixo. Registrado em [apostas-futuras](../00-identidade/apostas-futuras.md) (aposta 5) e no [registro de decisões](registro-de-decisoes.md).

## Veredito

**A ideia é boa, o mercado corre para ela (YC listou "Company Brain" nos pedidos de 2026) e a ABBA já tem ~60% construído.** Mas o formato viável — comercial, jurídica e psicologicamente — é o **modelo centauro**: o JARVIS serve o Tony Stark, não o substitui. A IA gera; o Conselheiro humano cura e assina; a diretoria decide. Nunca "IA aconselhando o board diretamente".

## Por que o formato centauro é obrigatório (3 razões)

1. **Regulatória:** o PL 2338 (lei de IA do Brasil, em tramitação) prevê responsabilidade civil objetiva e solidária para IA de alto risco — e sistemas que influenciam decisões empresariais flertam com essa classificação (multas até R$ 50 mi / 2% do faturamento). A exigência central é revisão humana de resultados relevantes — que já é o nosso princípio: *nós recomendamos, eles decidem*.
2. **Confiança:** um número alucinado num board deck não queima a ferramenta — queima a ABBA (casos reais: bot da Air Canada, jurisprudência inventada). RAG com fonte citada + curadoria + "não sei" honesto são inegociáveis.
3. **Técnica:** LLM não "aprende sozinho" — o aprendizado real vem da arquitetura: **RAG** (base viva do cliente) + **memória estruturada** (dados mensais, decisões) + **loop de outcomes**. E o loop de outcomes **a ABBA já construiu**: o vault reconcilia confiança empírica por resultado real e aposenta padrões desmentidos (piso 0,25). É o núcleo que o mercado ainda está inventando.

## Inventário: o que já existe vs. o que falta

| Componente | Estado |
|---|---|
| Fotografia inicial completa da empresa | ✅ = a Avaliação de 25 dimensões |
| Conhecimento sobre a ABBA e sobre o próprio sistema | ✅ abba-ops + specs dos agentes |
| Dados reais contínuos | ⚠️ existem (relatório mensal projetado×realizado, telemetria CrewAI, adoção no portal) — falta unificar no **Dossiê Vivo** por cliente (base RAG) |
| Aprendizado com resultados | ✅ loop de outcomes do vault — falta a versão por-cliente |
| Interface de consulta para o cliente | ⚠️ embrião = **Iris** (já tem contexto por tenant no portal) |
| Identificação proativa de melhorias | ❌ construir: rotina periódica que compara metas×realizado e rascunha candidatos a insight |
| Canal para a diretoria | ✅ o ritual do conselho (máx. 3 recomendações) — a IA abastece, nunca substitui |

## O ciclo em operação (desenho-alvo)

Dossiê Vivo (assessment + plano diretor + atas + relatórios + telemetria) → rotina mensal de análise gera candidatos a insight → **Conselheiro humano cura** → 3 recomendações no ritual → decisões e resultados voltam ao Dossiê → destilado **anonimizado e consentido** vai ao vault (o volante ganha segundo motor). Iris evolui para responder sobre a operação, com fonte citada.

## Regras de desenho (invioláveis)

- **Um cérebro por cliente, segregado** — nunca cruzar dados entre clientes; só o vault anonimizado cruza padrões
- On-premises disponível para quem exigir · nunca treinar modelos com dados do cliente (RAG consulta, não treina)
- Toda saída para a diretoria passa por curadoria e assinatura ABBA (blindagem PL 2338 + marca)
- Consentimento contratual explícito para a destilação anonimizada ao vault (pauta P4/advogado quando ativar)

## Faseamento (gatilhos, não datas)

| Fase | Gatilho | O que ativa |
|---|---|---|
| 0 (agora) | — | Nada a construir; disciplina: estruturar todo dado de engajamento desde o 1º cliente pensando no Dossiê |
| 1 | 1º cliente em manutenção | Dossiê Vivo interno + brief mensal gerado por IA, curado pelo sócio (uso interno; custo ~centenas de R$/mês) |
| 2 | 1º cliente na camada Estratégia | Insights proativos formais no ritual, co-assinados |
| 3 | 3+ clientes | Interface Iris-Empresa no portal, por tenant, com guardrails |
| 4 | 10+ clientes | Produto nomeado (candidato ao coração da tabela v3); naming = decisão de sócios |

**Custo real:** infra modesta; o trabalho é o encanamento de dados (~80%). **Retorno:** justifica a camada Estratégia, cria lock-in legítimo (o cérebro acumulado), diferencia de qualquer CAIO humano-só, e realiza tecnicamente a frase 18 da Visão 2029.

## Fontes

- [Y Combinator/Company Brain — a camada de dados decide tudo](https://colrows.com/blogs/company-brain-for-enterprise-ai/) · [Enterprise AI 2026 — TechRadar](https://www.techradar.com/pro/2026-the-year-enterprise-ai-finally-gets-to-work) · [Previsões CIO 2026 — InformationWeek](https://www.informationweek.com/machine-learning-ai/2026-enterprise-ai-predictions-fragmentation-commodification-and-the-agent-push-facing-cios)
- [RAG vs fine-tuning — Databricks](https://www.databricks.com/blog/rag-vs-fine-tuning) · [AI Memory vs RAG vs Knowledge Graph — Atlan](https://atlan.com/know/ai-memory-vs-rag-vs-knowledge-graph/) · [RAG vs memória de agentes — Mem0](https://mem0.ai/blog/rag-vs-ai-memory)
- [PL 2338 — visão geral](https://regulations.ai/regulations/RAI-BR-NA-SUMMARY-2026) · [PL 2338 — análise MAIEI](https://montrealethics.ai/ai-policy-corner-how-brazil-plans-to-govern-ai-reviewing-pl-2338-2023/) · [Regulação de IA no Brasil — CMS](https://cms.law/en/int/expert-guides/ai-regulation-scanner/brazil)
- [Alucinações de IA em negócios — IntuitionLabs](https://intuitionlabs.ai/articles/ai-hallucinations-business-causes-prevention) · [Ceticismo e confiança em AI advisors — arXiv](https://arxiv.org/pdf/2606.23491)
