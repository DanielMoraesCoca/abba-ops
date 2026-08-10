# Protótipo Patrimonial — Plano de Construção (o documento-mestre)

> **Camada:** interno (estratégia + engenharia de protótipo). Origem: conversa de 2026-08-10 com advogado especialista em estruturas patrimoniais (rede morna), que apresentou a ideia; decisão do sócio: estruturar do zero, sem material de terceiros, como propriedade ABBA. Pesquisa de mercado e regulatória + pesquisa técnica CrewAI executadas antes deste plano (fontes ao longo do pacote).
>
> **O pacote completo:** este documento (o quê e por quê) · [especificação de agentes](especificacao-agentes.md) (como) · [questionário](questionario-perfil.md) (o input) · [corpus](corpus-conhecimento.md) (o que pode ser citado) · [avaliação e métrica](avaliacao-e-metrica.md) (a prova) · [`scaffold/`](scaffold/README.md) (o código-esqueleto).
>
> Dono: sócio de engenharia. Gate comercial: nenhum contrato/sociedade antes do advogado próprio (P4) — regra do conselho.

---

## 1. O produto em uma frase

**Um sistema de apoio que transforma o perfil completo de uma família/empresário em minutas de planejamento patrimonial internacional — 100% declarado e tributado, com fonte citada em cada afirmação e red flags automáticos — para um advogado nomeado revisar, editar e assinar.**

Não é "IA que faz planejamento patrimonial". É a ferramenta que faz o especialista produzir em 1 hora, com mais consistência, o que hoje leva semanas — e que recusa, por desenho, o caso que nenhum especialista sério deveria aceitar.

## 2. Por que agora (a tese, com fatos verificados)

1. **A categoria existe e está capitalizada nos EUA**: Wealth.com (US$ 65M Série B, abr/2026, fundada por brasileiros; líder entre advisors), Vanilla (~US$ 85M), Luminary, FP Alpha. Todas vendem para o PROFISSIONAL, nunca substituindo-o — o único posicionamento defensável, e o que adotamos.
2. **Não há equivalente brasileiro**: o desenho de estruturas internacionais para brasileiros é artesanal (escritórios + provedores fiduciários). Gap real.
3. **A regulação criou o mercado**: a Lei 14.754/2023 acabou com diferimento e sigilo (15% anual, trusts transparentes, CRS com 100+ jurisdições, DCBE) — o que matou o produto antigo ("não aparecer") e criou demanda por um novo: **planejamento declarado, complexo e recorrente**. ITCMD progressivo (EC 132) + PLP 108 são o segundo gatilho, em curso.
4. **Demanda mensurável**: ~386 mil milionários no Brasil; investimento de PF no exterior mais que dobrou em 2024; mercado de grandes fortunas > R$ 3 tri.

## 3. Princípios de desenho (invioláveis)

1. **Conformidade-primeiro** — o sistema otimiza o melhor caminho LEGAL; red flags duros bloqueiam o desenho (fraude a credores, não-declaração, interposta pessoa, supressão de legítima, KYC falho, recusa de transparência). Comercialmente, isso é o diferencial de confiança, não uma limitação.
2. **Centauro/EOAB** — saída é minuta para advogado nomeado; desenho jurídico é ato privativo de advocacia.
3. **Citação ou abstenção** — corpus versionado; claim sem fonte não sai; `nao_coberto` é resposta honesta que vira a seção "limites".
4. **Determinístico onde é regra, agêntico onde é julgamento** — gates, obrigações e cálculos são código; análise, desenho e crítica são agentes.
5. **LGPD por desenho** — memória adaptativa OFF; caso vive no estado tipado (apagável); PII não vai ao provedor; trilha de auditoria completa por minuta.

## 4. Arquitetura (resumo; detalhe na [especificação](especificacao-agentes.md))

CrewAI 1.x, doutrina oficial **Flow-first**: `Flow[EstadoCaso]` com `@persist` orquestrando 3 crews e 2 gates — intake determinístico → **gate 1** red flags (código) → **Crew Análise** (tributário BR, sucessório, jurisdições; RAG-como-tool com proveniência + guardrail anti-citação-órfã) → **Crew Desenho** (arquiteto de alternativas + crítico adversarial que descarta desenhos fatais) → obrigações e cenários (código — o diferencial pós-2024) → **gate 2** humano (`@human_feedback`, advogado, com trilha) → **Crew Redação** (minuta) → render com trilha de auditoria. Custo-alvo: ≤ US$ 5/caso.

## 5. Fases (4 sprints; construção só começa com a métrica combinada — já está: [avaliação](avaliacao-e-metrica.md))

| Sprint | Entrega | Critério de saída |
|---|---|---|
| **S1 — Corpus + fundação** | Corpus v0 ingerido (chunk por artigo, embedder explícito), `RagCorpusTool` real, hook de PII, projeto rodando | Busca devolve chunks certos para 20 consultas de teste; PII não sai |
| **S2 — Análise + gates** | Crews Análise e Desenho vivas; `run_eval.py` completo (perfis inteiros por persona); aritmética de cenários | Camada determinística do eval verde: gate 1 = 100%, zero citação órfã |
| **S3 — HITL + minuta** | `@human_feedback` (console → provider async), Crew Redação, render final (markdown → DOCX padrão visual) | Um caso completo ponta a ponta com revisão humana real |
| **S4 — Prova** | Rodada completa do golden set com o advogado especialista; relatório GO/NO-GO | Os 7 critérios da métrica, medidos e assinados |

Estimativa honesta: 6–8 semanas de calendário com 1 engenheiro (Mateus/CrewAI como implementador natural) + horas do advogado no S4. Custos diretos: API (dezenas de US$ no desenvolvimento; ≤ US$ 5/caso em operação) + embeddings (centavos) + plataforma AMP (tier a confirmar com o parceiro — preços públicos não verificáveis).

## 6. Papéis

- **ABBA**: dona do produto, do método e do eval; engenharia via parceria CrewAI (Mateus).
- **Advogado especialista nomeado**: valida gabaritos do golden set (S1), revisa casos (S3) e assina o veredito (S4). Candidatos naturais existem na rede (o especialista da conversa de origem, o escritório da palestra, o contato de LGPD) — **o plano não depende de nenhum deles**; qualquer especialista de estruturas patrimoniais serve.
- **Conversa "produto vs. empresa"**: só DEPOIS do GO, com os números na mesa — e qualquer sociedade passa pelo gate do advogado próprio (P4).

## 7. Riscos e mitigações

| Risco | Mitigação |
|---|---|
| Instabilidade legislativa (PLP 108/ITCMD internacional) | Corpus com status datado; agentes obrigados a marcar área instável como risco, nunca certeza; revisão trimestral do corpus |
| Alucinação jurídica | 4 camadas: RAG com proveniência → schema → guardrail anti-citação-órfã → crítico adversarial → gate humano |
| Uso indevido (cliente querendo ocultação) | Red flags duros + guardrail de linguagem + aceite de transparência como pré-condição de entrada |
| Dependência de um especialista único | Golden set com gabarito escrito e congelado; qualquer especialista qualificado pode re-validar |
| Custo de especialista no S4 | Rubrica enxuta (7 personas de desenho × 5 eixos × ~20 min) |
| Sequência da empresa (foco) | Isto é um protótipo de degrau 2 no pipeline comercial normal — não uma segunda empresa; a decisão maior espera o GO e os gates da casa |

## 8. Relação com a estratégia ABBA

- É um **protótipo de caso de uso (degrau 2)** do pipeline — com a diferença de que a ABBA o desenvolve como ativo próprio reutilizável (a decisão de com quem operá-lo comercialmente vem depois do GO).
- Alimenta a tese jurídica em curso (palestra Brasília, relatório setorial): mais uma prova de que a camada de método + prova + governança é o nosso lugar no mercado jurídico.
- Nada aqui toca cérebro/portal — a moratória de engenharia segue respeitada; o scaffold é material comercial novo, autorizado pelo sócio (registro V3w).

## Ligações

[Especificação](especificacao-agentes.md) · [Questionário](questionario-perfil.md) · [Corpus](corpus-conhecimento.md) · [Avaliação](avaliacao-e-metrica.md) · [Scaffold](scaffold/README.md) · [Registro de decisões](../registro-de-decisoes.md) · [Escada ABBA](../../03-comercial/escada-abba.md) (degrau 2) · [Protocolo de prova](../../04-entrega/protocolo-de-prova.md)
