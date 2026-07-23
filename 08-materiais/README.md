# Materiais — catálogo do que já existe

> Inventário dos materiais reais da ABBA (treinamento, comerciais, estratégia), com onde cada um vive e o que falta produzir. Regra: **modelos genéricos e canônicos → este repo · arquivos finais pesados e instâncias de cliente → Drive** ([estrutura](../07-drive/estrutura-drive.md)).

## 1. ABBA Academy — Materiais Finais de Treinamento (PT-BR)

**O que é:** o pacote FINAL do conteúdo de capacitação (PDF, 23 páginas), pronto para gravar/imprimir/facilitar. **Este é o maior ativo de conteúdo da empresa.**

**Onde vive:** Drive → `03 Modelos/Academy/` (arquivo pesado; não versionado em git). Fonte: gerado em jul/2026.

**Índice (código curricular):**

| Tier | Conteúdo |
|---|---|
| 1A | Roteiros Nível 1, word-for-word (1.1.1–1.4.4) — vídeos de ~5–8 min |
| 1B | Módulo 2.1 — **Método 4D** (2.1.1–2.1.5) |
| 1C | Kit do Facilitador — **Kickoff presencial de meio dia** (Autópsia de Tarefa/Demo Theater, Clínica da Primeira Vitória, Bússola em papel, checklists de logística) |
| 1D | Artefatos impressos: **Card da Bússola · Semáforo de Dados · Esqueleto de Prompt (Papel/Contexto/Tarefa/Formato/Exemplo/Restrições) · Lente de Oportunidade · Solution Canvas · Ficha Primeira Vitória** |
| 1E | Biblioteca de Prompts (40+) |
| 1F | Banco de Desafios (12 desafios da semana, 5 Prompt Golf, 8 drills de discernimento) |
| 2 G–J | Módulos 2.2/2.3, Track G, kits Oficina/Build Day, **lições CrewAI** (role/goal/backstory, tools, crews), rubricas |

**Fundamentos embutidos:** casos reais de alucinação (Mata v. Avianca + precedentes brasileiros TJSC/TST/STJ/OAB Rec. 001/2024) · LGPD/Shadow AI com o Semáforo de Dados como espinha de privacidade · normas de microlearning (1 objetivo/vídeo, gancho em 8s, ação de 60s no FAÇA AGORA).

**Recompensa de conclusão:** certificado ABBA + **licença CrewAI de 12 meses** (consistente com o modelo de serviço).

**⚠️ Atribuição obrigatória (compliance):** o Método 4D é adaptado do *AI Fluency Framework* (Rick Dakan, Joseph Feller e Anthropic), licenciado **CC BY-NC-SA 4.0**. O texto de atribuição está no próprio material e deve aparecer sempre que o 4D aparecer. **A cláusula NC (não-comercial) precisa de validação do advogado para uso em programa pago — incluída na pauta P4.**

**O que falta produzir (do próprio documento):**
1. Gravar os 3 vídeos de maior alavancagem primeiro (1.3.3 "Confie, mas verifique", 1.3.1 Semáforo, 2.1.2 Descrição) + imprimir os 6 cards
2. Gravar o restante do Nível 1 e Módulo 2.1; personalizar slots [PERSONALIZAR] com dados do primeiro cliente
3. Rodar um Kickoff-piloto com turma real usando o kit
4. Métrica que muda o plano: **"horas reinvestidas por pessoa/semana"** + taxa de conclusão dos vídeos
5. Validar com advogado a lição de verificação jurídica (O-JUR) antes de qualquer turma jurídica

## 2. Proposta comercial — modelo canônico (estrutura Galápagos)

**O que é:** a proposta real enviada em jun/2026 (ref ABBA-2026-001) virou o **modelo canônico** de proposta do programa completo.

**Onde vive:**
- **Modelo genericizado (Word):** [`modelos/proposta-comercial-modelo.docx`](modelos/proposta-comercial-modelo.docx) — placeholders `{{NOME_DO_CLIENTE}}`, `{{ANO}}`, `{{NUM}}`, `{{MÊS ANO}}`; identidade visual navy/dourado aplicada
- **Estrutura e conteúdo de referência (markdown):** [`../03-comercial/proposta-programa-completo.md`](../03-comercial/proposta-programa-completo.md) (reescrita sobre esta estrutura)
- **Instância original (com nome do cliente):** Drive → `01 Comercial/Propostas enviadas/` — **nunca em git**

**Estrutura (11 seções):** Sumário Executivo (com stat-cards) → Contexto e Desafios (situação/complicação/desafios/resolução) → Transformação AI Native em 3 Níveis (estratégia/workflows/pessoas + as 3 perguntas) → A Jornada ABBA (modular: Assessment 4–5 sem → Protótipo 6–8 sem → Deployment → Portal → Serviços Gerenciados) → Portal de Capacitação (4 fases com desbloqueio de ferramentas) → Metodologia (5 fases com gates) → Cronograma (16 semanas, critérios de aceite) → Equipe e Governança → Arquitetura e Ecossistema → Termos/SLAs/Garantias → Por Que a ABBA.

**Numeração de referência:** `ABBA-AAAA-NNN` sequencial (próxima: ABBA-2026-002). Registrar cada emissão na pasta do lead.

## 3. Plano de Transformação v3 (estratégia, histórico)

**O que é:** o plano estratégico "From AI Academy to Capability Installation Program" v3.0 (abr/2026). Superseded pelo v3.2 (no abba-portal, marcado histórico) e por este repo, mas contém detalhes ainda úteis: gates de validação mensuráveis, disciplina de descoberta de preço, análise de beachhead jurídico/FRP, dual-branding.

**Onde vive:** Drive → `04 Interno/Estrategia historica/`. Decisões dele que seguem vigentes já estão absorvidas neste repo; o resto é histórico.

## 4. Modelos de entregáveis (Drive legado — inventariados em 2026-07-23)

A pasta antiga do Drive contém **os modelos dos entregáveis que a proposta promete**, todos com dados de exemplo (nunca enviar como estão). Mapa completo de migração: [estrutura-drive](../07-drive/estrutura-drive.md#mapa-de-migração-arquivo-a-arquivo-inventário-de-2026-07-23). Destaques:

- **Termo de Aceite** → já transcrito: [`../04-entrega/termo-de-aceite.md`](../04-entrega/termo-de-aceite.md)
- **Relatório de Maturidade** (6 dimensões, escala 1–5 Exploratório→Transformacional) · **Mapa de Casos de Uso** (matriz de priorização + ROI) · **Plano Diretor** (24 meses) — os três entregáveis do Assessment
- **Relatório de Protótipo** (sprints, métricas, decisão GO/NO-GO) e **Relatório de Deployment** (testes de aceite, SLAs, rollback, handover, hypercare)
- **Relatório Mensal de Operação** (serviços gerenciados)
- Proposta anterior **com os preços reais emitidos** (R$ 150K — registrado na [planilha de precificação](../03-comercial/precificacao-planilha.md))

Nota de nomenclatura: os docs legados usam "ABBA Intelligence" / "AI Consulting & Platform" / "ABBA Consulting" — o nome comercial vigente é **ABBA Consultoria de IA** ([marca](../00-identidade/marca-e-nomenclatura.md)); padronizar na migração.

## 5. O que ainda NÃO existe (fila de produção de materiais)

Prioridade no [plano de ação](../05-interno/plano-de-acao.md). Tudo nasce do [padrão visual](../00-identidade/identidade-visual.md):

| Material | Uso | Status |
|---|---|---|
| Deck institucional (PPTX, 12 slides) | 1ª reunião / apresentação da ABBA | ✅ [`modelos/abba-deck-institucional.pptx`](modelos/abba-deck-institucional.pptx) |
| Modelo de deck de kickoff (PPTX) | [roteiro já existe](../04-entrega/kickoff-roteiro.md) | a criar |
| Modelo da Análise ABBA (degustação, DOCX → PDF) | estágio 02 | ✅ [`modelos/analise-abba-modelo.docx`](modelos/analise-abba-modelo.docx) |
| Modelos DOCX das 3 propostas de entrada | derivar do modelo canônico | a criar |
| Modelo do Relatório de Avaliação (capa/estilo) | estágio 06 | base existe (Relatório de Maturidade no Drive legado) — padronizar |
| Certificados (participante e campeão) | graduação | a criar |
| Vídeos do Nível 1 + Módulo 2.1 | portal | roteiros prontos; gravar |
| Cards impressos (6 artefatos do Tier 1D) | kickoff presencial | arte final + gráfica |
| Papel timbrado / modelo de documento geral | tudo | a criar |
