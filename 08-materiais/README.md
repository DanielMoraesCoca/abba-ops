# Materiais — catálogo do que já existe

> Inventário dos materiais reais da ABBA (treinamento, comerciais, estratégia), com onde cada um vive e o que falta produzir. Regra: **modelos genéricos e canônicos → este repo · arquivos finais pesados e instâncias de cliente → Drive** ([estrutura](../07-drive/estrutura-drive.md)).

## 0. O padrão editorial (decisão do sócio, 2026-08-05)

**[`modelos/abba-apresentacao.pdf`](modelos/abba-apresentacao.pdf) é o documento-padrão** — todo material novo (e toda revisão de material existente) segue a entonação e os termos dele. Não precisa ser igual; precisa estar na mesma linha:

- **Abre direto na ABBA** — sem parágrafos de contexto de mercado (70/30) antes de dizer quem somos
- **Conta a história em ordem** — a jornada na sequência real, cada etapa em "o quê · por quê · como"
- **Sem preços** em material de primeiro contato — preço é conversa
- **Sem "25 dimensões"** em material de envio — vira "mergulho profundo, do conselho à linha de frente" (em proposta/contrato/relatório de entrega o número é escopo e permanece)
- **Sem "somos uma firma nova"** em material — a honestidade sobre histórico é doutrina de **conversa** ([kit, 3ª objeção](../03-comercial/kit-de-presenca.md))
- **Engenharia, não só agentes** — "arquitetura, integrações e agentes de IA trabalhando em conjunto"
- **Raízes sem nomear árvore** nas seções especiais; **"da primeira conversa"**, nunca "do primeiro café"
- **Sem travessão (—) em material oficial** (decisão do sócio, 2026-09-01) — no lugar: dois-pontos, ponto ou vírgula. Vale para todo material que sai; o separador tipográfico `·` continua permitido
- **Registro formal, palco no palco** (decisão do sócio, 2026-09-01): material escrito segue o registro institucional da apresentação comprovada (o quê · por quê · como, as duas frentes, prometemos/recusamos). Do pitch de palco entram apenas o gancho ("mais de oito não vão conseguir mostrar um número"), a leitura ponta/veia e o Portão em linguagem de diretoria — as demais imagens de palco (mesa de três pés, juro composto, primeira parede) ficam no teleprompt e no kit, nunca em material escrito
- **E-mail externo = contato@abbaservices.com.br** · **logos Microsoft e CrewAI** discretas onde a parceria é citada
- Visual: o sistema editorial do próprio documento (branco, Cambria/Calibri, versaletes dourados, filetes — sem cartões nem decoração)

O [Revisor](../06-ferramentas/regua-do-revisor.md) codifica as regras compatíveis com regex; o resto é julgamento contra o documento-padrão.

## 0b. O gerador (Virada V5, 2026-08-31)

Os materiais de apresentação agora **nascem de código**, não de edição manual: [`gerador/`](gerador/) (Node + pptxgenjs/docx pinados). `tema.js` é a única fonte da identidade (navy/dourado/versaletes/filetes — espelha o §0); `conteudo/precos.json` é validado contra a [régua](../06-ferramentas/regua-do-revisor.json) em todo build; um manifesto de hashes recusa sobrescrever arquivo retocado à mão sem `--force`. Uso: `cd gerador && npm ci && node build.js [--pdf]`. Alvos: `abba-apresentacao`, `abba-um-minuto`, `abba-deck-institucional`, `deck-programa`, `deck-conselheiro`, `termo-do-programa-modelo` (DOCX).

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

**Recompensa de conclusão:** certificado ABBA + **licença CrewAI de 12 meses** (consistente com o modelo de serviço; *condicionada à via de contratação CrewAI ativa — R9: não prometer em proposta antes do setup*).

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
- **Modelo genericizado (Word):** retirado na V5 (era o `proposta-comercial-modelo.docx` do cardápio antigo) — o novo modelo é o **Termo do Programa**, na fila de regeneração; números sempre pela [tabela v3](../03-comercial/tabela-de-precos.md)
- **Estrutura e conteúdo de referência (markdown):** [`../05-interno/arquivo/proposta-programa-completo.md`](../05-interno/arquivo/proposta-programa-completo.md) (reescrita sobre esta estrutura)
- **Instância original (com nome do cliente):** Drive → `01 Comercial/Propostas enviadas/` — **nunca em git**

**Estrutura (11 seções):** Sumário Executivo (com stat-cards) → Contexto e Desafios (situação/complicação/desafios/resolução) → Transformação AI Native em 3 Níveis (estratégia/workflows/pessoas + as 3 perguntas) → A Jornada ABBA (modular: Assessment 4–5 sem → Protótipo 6–8 sem → Deployment → Portal → Serviços Gerenciados com presença semanal → Conselheiro de IA) → Portal de Capacitação (4 fases com desbloqueio de ferramentas) → Metodologia (5 fases com gates) → Cronograma (16 semanas, critérios de aceite) → Equipe e Governança → Arquitetura e Ecossistema → Termos e SLAs → Por Que a ABBA.

**Numeração de referência:** `ABBA-AAAA-NNN` sequencial (próxima: ABBA-2026-002). Registrar cada emissão na pasta do lead.

## 3. Plano de Transformação v3 (estratégia, histórico)

**O que é:** o plano estratégico "From AI Academy to Capability Installation Program" v3.0 (abr/2026). Superseded pelo v3.2 (no abba-portal, marcado histórico) e por este repo, mas contém detalhes ainda úteis: gates de validação mensuráveis, disciplina de descoberta de preço, análise de beachhead jurídico/FRP, dual-branding.

**Onde vive:** Drive → `04 Interno/Estrategia historica/`. Decisões dele que seguem vigentes já estão absorvidas neste repo; o resto é histórico.

## 4. Modelos de entregáveis (Drive legado — inventariados em 2026-07-23)

A pasta antiga do Drive contém **os modelos dos entregáveis que a proposta promete**, todos com dados de exemplo (nunca enviar como estão). Mapa completo de migração: [estrutura-drive](../07-drive/estrutura-drive.md#mapa-de-migração-arquivo-a-arquivo-inventário-de-2026-07-23). Destaques:

- **Termo de Aceite** → já transcrito: [`../04-entrega/termo-de-aceite.md`](../04-entrega/termo-de-aceite.md)
- **Relatório de Maturidade** (6 dimensões, escala 1–5 Exploratório→Transformacional — **este é o arquivo legado do Drive, não o modelo vigente**; o modelo regenerado em `modelos/` já diz 25 dimensões, conferido no DOCX em 2026-08-01) · **Mapa de Casos de Uso** (matriz de priorização + ROI) · **Plano Diretor** (24 meses) — os três entregáveis do Assessment
- **Relatório de Protótipo** (sprints, métricas, decisão GO/NO-GO) e **Relatório de Deployment** (testes de aceite, SLAs, rollback, handover, hypercare)
- **Relatório Mensal de Operação** (serviços gerenciados)
- Proposta anterior **com os preços reais emitidos** (R$ 150K — registrado na [planilha de precificação](../03-comercial/precificacao-planilha.md))

Nota de nomenclatura: os docs legados usam "ABBA Intelligence" / "AI Consulting & Platform" / "ABBA Consulting" — o nome comercial vigente é **ABBA Consultoria de IA** ([marca](../00-identidade/marca-e-nomenclatura.md)); padronizar na migração.

## 5. Família de modelos regularizada (2026-07-23)

Os modelos legados foram **regenerados do zero** no padrão vigente — mesma identidade visual, discurso alinhado (modelo de 6 etapas, nomes oficiais, sem promessas pendentes de P8/P9), `{{PLACEHOLDERS}}` no lugar de dados de exemplo. Em [`modelos/`](modelos/):

| Modelo | Estágio da jornada |
|---|---|
| `relatorio-maturidade-modelo.docx` | 06 — Avaliação (**25 dimensões** do método vigente, escala 1–5 — o modelo já diz 25; a escala de 6 era do legado) |
| `mapa-de-oportunidades-modelo.docx` | 06 — Avaliação (matriz de priorização + ROI rastreável) |
| `plano-diretor-modelo.docx` | 06 — Avaliação (roadmap com gates e governança) |
| `relatorio-prototipo-modelo.docx` | 07 — Construção (GO/NO-GO com números medidos) |
| `relatorio-deployment-modelo.docx` | 07 — Implantação (aceite, SLA, handover, hypercare) |
| `relatorio-mensal-modelo.docx` | 09 — Manutenção (projetado vs. realizado sempre) |
| `termo-de-aceite-modelo.docx` | gates — fecha fase e libera fatura de marco |
| `plano-capacitacao-modelo.docx` | 08 — Capacitação (4 fases, Bússola, kickoff meio dia) |

**Regra:** os DOCX legados do Drive viram ARQUIVO após a migração — quem vale são estes. Os markdown correspondentes em `04-entrega/` são a documentação do processo; os DOCX são o que o cliente vê.

## 6. Inventário de materiais e fila restante (2 pendências reais: vídeos e cards — o resto ✅)

Prioridade no [plano de ação](../05-interno/plano-de-acao.md). Tudo nasce do [padrão visual](../00-identidade/identidade-visual.md):

| Material | Uso | Status |
|---|---|---|
| Deck institucional (PPTX+PDF, **15 slides — refeito na V5, registro formal (2026-09-01)**: capa navy, quem somos, o gancho, as duas frentes + ponta/veia, as 3 medições, o Mapa, o Programa em 3 fases, um slide "por dentro" para cada fase (serviços em o quê · por quê · como, com fotos), o Portão formal, depois do ano 1, Conselheiro especificado, prometemos/recusamos + próximo passo — **sem preços, sem travessão**) | 2ª reunião em diante — apresentação ao vivo | ✅ [`modelos/abba-deck-institucional.pptx`](modelos/abba-deck-institucional.pptx) |
| Deck de kickoff (PPTX, 12–13 slides com o pré-mortem 6b, com logo) | [roteiro](../04-entrega/kickoff-roteiro.md) | ✅ [`modelos/abba-deck-kickoff.pptx`](modelos/abba-deck-kickoff.pptx) |
| Modelo da Análise ABBA (degustação, DOCX → PDF) | estágio 02 | ✅ [`modelos/analise-abba-modelo.docx`](modelos/analise-abba-modelo.docx) |
| 3 propostas de entrada (DOCX) | workshop · avaliação · sprint LGPD | 🔴 retiradas na V5 — as ofertas saíram da vitrine ([tabela v3](../03-comercial/tabela-de-precos.md)); processos arquivados em [`../05-interno/arquivo/`](../05-interno/arquivo/README.md) |
| Modelo do Relatório de Avaliação (capa/estilo) | estágio 06 | ✅ regularizado (`modelos/relatorio-maturidade-modelo.docx` + oportunidades + plano diretor) |
| Certificados (participante e campeão, PPTX com logo) | graduação | ✅ [`modelos/certificados-modelo.pptx`](modelos/certificados-modelo.pptx) |
| Vídeos do Nível 1 + Módulo 2.1 | portal | roteiros prontos; gravar |
| Cards impressos (6 artefatos do Tier 1D) | kickoff presencial | arte final + gráfica |
| Card da Bússola do portal em pt-BR | o card existente ("My Week With AI") está em inglês — não pode aparecer em material pt-BR | pendência de tradução (Pedro/portal) |
| **Modelo Word do Termo do Programa** (DOCX — o documento de proposta único da V5: capa, sumário executivo, o que ouvimos, as 3 fases com os portões, investimento por porte (preços puxados de `gerador/conteudo/precos.json`, validados contra a régua no build), Assinatura ano 2+, como trabalhamos, aceite; placeholders `{{ }}`; **sem travessão**) | toda proposta de Programa — preencher, congelar PDF no Drive, registrar a ref `ABBA-AAAA-NNN` | ✅ [`modelos/termo-do-programa-modelo.docx`](modelos/termo-do-programa-modelo.docx) (gerador, alvo `termo-do-programa-modelo`) |
| Papel timbrado (DOCX) | correspondência | ✅ [`modelos/papel-timbrado-modelo.docx`](modelos/papel-timbrado-modelo.docx) |
| One-pager do Conselheiro de IA (DOCX) | [produto E1](../03-comercial/conselheiro-de-ia.md) — estágio 10 / venda direta | ✅ [`modelos/conselheiro-de-ia-onepager-modelo.docx`](modelos/conselheiro-de-ia-onepager-modelo.docx) |
| Proposta do Conselheiro de IA (DOCX) | [processo](../03-comercial/proposta-conselheiro-de-ia.md) | ✅ [`modelos/proposta-conselheiro-modelo.docx`](modelos/proposta-conselheiro-modelo.docx) |
| **Apresentação enviável** (PDF 16:9, 3 págs — **o documento-padrão, §0, refeito na V5 pelo gerador**: quem somos + raízes, o Programa em 3 fases com o Portão da Prova, a relação que continua (Assinatura + Exame Anual) + Conselheiro + logos + CTA do Mapa; **sem preços**; **é o que se manda quando o prospect pede "conteúdo antes da reunião"**; versão-relâmpago de 1 pág para WhatsApp: `abba-um-minuto.pdf`, também refeita) | pós-ligação / pré-reunião — [ordem de envio no kit](../03-comercial/kit-de-presenca.md) | ✅ [`modelos/abba-apresentacao.pdf`](modelos/abba-apresentacao.pdf) (fonte: `.pptx` ao lado) |
| **Os 7 decks de serviço** (PPTX+PDF, 6 slides cada, padrão editorial §0 — um mergulho por serviço: capa com a essência → o quê → por quê → como → o que fica com você → o encaixe na jornada; **com as fotos reais dos entregáveis embutidas**: página de análise real com radar de maturidade (empresa preservada), relatório de maturidade, relatório do protótipo, relatório de implantação, relatório mensal e parecer de arbitragem; **sem preços**) | aprofundamento por serviço: apresentar ao vivo na conversa daquele serviço, ou enviar DEPOIS dela — nunca como primeiro contato (primeiro contato = a apresentação) | 🔴 **retirados na V5 (2026-08-31)** — o cardápio de 7 serviços foi descontinuado ([tabela v3](../03-comercial/tabela-de-precos.md)); substituídos pelo deck único do Programa + deck do Conselheiro, em regeneração pelo gerador |
| **Deck do Programa** (PPTX+PDF, 10 slides, padrão §0 — capa navy, o Mapa, fase 1, o Portão da Prova, fases 2–3, depois do ano, o que fica com você; **com as fotos reais dos entregáveis** (empresa preservada); **sem preços**) | aprofundamento do Programa: ao vivo na conversa, ou enviar DEPOIS dela — nunca como primeiro contato | ✅ [`modelos/deck-programa.pptx`](modelos/deck-programa.pptx) (gerador, V5) |
| **Deck do Conselheiro** (PPTX+PDF, 7 slides, padrão §0 — para quem já tem IA rodando; com o parecer de arbitragem real; **sem preços**) | conversa do Conselheiro — substitui o `servico-7-conselheiro-deck` | ✅ [`modelos/deck-conselheiro.pptx`](modelos/deck-conselheiro.pptx) (gerador, V5) |
| Parecer de Arbitragem de Fornecedores (DOCX) | [processo](../04-entrega/arbitragem-de-fornecedores.md) — entregável do Conselheiro | ✅ [`modelos/arbitragem-fornecedores-modelo.docx`](modelos/arbitragem-fornecedores-modelo.docx) |
| Proposta de Continuidade (DOCX) | [processo](../05-interno/arquivo/proposta-continuidade.md) — renovação em 3 camadas, estágio 11 | 🔴 retirado na V5 — a continuidade virou a Assinatura da Capacidade ([tabela v3](../03-comercial/tabela-de-precos.md)) |
