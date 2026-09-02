# Mapa: as 25 dimensões × ISO/IEC 42001 × PL 2338

> **Camada:** ferramenta (negócio). Origem: melhoria nº 2 do [estudo de imunidade](../05-interno/estudo-imunidade-diretor-de-ia.md) (2026-08-03): a avaliação passa a entregar, junto do portfólio de oportunidades, uma **leitura de prontidão regulatória**: onde a empresa está em relação ao sistema de gestão de IA da ISO/IEC 42001 (ABNT NBR publicada em 2024) e às obrigações que o PL 2338 (Marco Legal da IA) vai criar.
>
> **Três travas de honestidade, antes de qualquer uso comercial:**
> 1. **Não somos organismo certificador.** Este mapa produz *gap assessment* (prontidão), nunca certificação: certificar exige organismo acreditado e auditoria de terceira parte. A frase permitida: *"preparamos para a certificação"*; a proibida: *"certificamos"*.
> 2. **O PL 2338 ainda não é lei.** Aprovado no Senado, em votação final na Câmara (2026). As obrigações citadas aqui vêm do texto aprovado no Senado e **{{A VERIFICAR contra o texto final sancionado antes de qualquer material de cliente}}**.
> 3. **Este mapa é uma camada SOBRE o framework, não uma mudança nele.** O `framework.js` é IP travado: nada aqui altera dimensão, pergunta ou prompt. Se um dia o mapeamento entrar na ferramenta (relatório automático), é feature do assessment-brain com decisão própria.
>
> Dono: chapéu Entrega (aplicação) + Tecnologia (se virar feature). Revisar quando o PL 2338 for sancionado.

---

## 1. Por que este mapa existe (a lógica comercial)

- A ISO 42001 já aparece como **exigência em contratos B2B e compras públicas**; a certificação exige verificação externa: um diretor de IA interno não se autocertifica. O PL 2338 prevê classificação de risco, avaliação de impacto algorítmico e sanções de até R$ 50 mi.
- A avaliação de 25 dimensões **já coleta a maior parte da evidência** que um gap assessment desses padrões pede. Hoje jogamos essa sobreposição fora; com este mapa, o mesmo trabalho de campo produz dois entregáveis.
- É o entregável que o **próprio diretor de IA do cliente pede**: ele precisa desse mapa para o conselho, e não pode produzi-lo sozinho (autoavaliação não convence conselho nem certificadora). É a materialização da mudança de prateleira: camada independente de prova.

**Como usar na prática (hoje, sem tocar em código):** ao final da avaliação profunda, o consultor preenche a tabela do §4 com o que as entrevistas já revelaram + as 10 perguntas suplementares do §3, e o relatório ganha uma seção "Prontidão regulatória" com semáforo por área.

---

## 2. O mapeamento: dimensão por dimensão

Estrutura da ISO/IEC 42001 usada como referência: cláusulas 4–10 (contexto, liderança, planejamento, apoio, operação, avaliação de desempenho, melhoria) + Anexo A (controles A.2 políticas · A.3 organização interna · A.4 recursos · A.5 avaliação de impactos · A.6 ciclo de vida do sistema de IA · A.7 dados · A.8 informação às partes interessadas · A.9 uso responsável · A.10 terceiros). **{{A VERIFICAR: conferir numeração fina contra o texto ABNT adquirido antes de citar cláusula em documento de cliente}}**

### Cobertura forte: a avaliação já coleta a evidência

| Dimensão | ISO/IEC 42001 | PL 2338 | O que a evidência da dimensão responde |
|---|---|---|---|
| **D09** Risco & Compliance | 6.1 (riscos/oportunidades) · 8.2 (avaliação de risco de IA) · A.5 | Classificação de risco; avaliação preliminar; **avaliação de impacto algorítmico** (alto risco) | A pergunta-matadora ("que decisões exigem humano por lei?") é literalmente o insumo da classificação de risco |
| **D19** Modos de Falha | A.6 (verificação & validação) · A.8 (comunicação de incidente) | Comunicação de **incidente grave** à autoridade; medidas de segurança | Raio de dano + limiar de confiança + fallback = o dossiê de segurança que a AIA pede |
| **D14** Arquitetura de Confiança | A.9 (uso responsável) | **Supervisão humana efetiva** | O nível real de autonomia que a empresa aguenta · pré-requisito da supervisão humana exigida |
| **D05** Mapa de Decisões | A.9 · A.6 (requisitos) | Direito à **revisão humana** de decisão automatizada | A taxonomia (automatizar/aumentar/consertar dado) marca onde revisão humana é obrigatória, não opcional |
| **D23** Dimensão Ética | A.5 (impactos em indivíduos/grupos/sociedade) | **Não-discriminação; correção de vieses** | O teste do jornalista é uma avaliação de impacto social em miniatura |
| **D08** Dados Ocultos + **D12** Topologia da Informação | A.7 (gestão, qualidade, proveniência de dados) | Qualidade/governança de dados usados por IA (interface com LGPD) | Onde o dado mora, quem toca, qual a qualidade · o inventário que a A.7 exige |
| **D03** Paisagem Tecnológica (shadow IT) | 4.1 (contexto) · A.4 (recursos) | Responsabilidade do **aplicador** por sistemas em uso | O shadow AI descoberto aqui é exatamente o "sistema de IA em uso sem governança" que os dois marcos punem · ligação direta com o [Workshop Shadow AI](../05-interno/arquivo/proposta-workshop-shadow-ai.md) (arquivado na V5 · hoje capacidade da fase 1 do Programa) |
| **D25** Baseline de Medição | 9.1 (monitoramento e medição) | Prestação de contas/documentação | O [protocolo de prova](../04-entrega/protocolo-de-prova.md) É a cláusula 9 em operação: métrica antes, medição depois, registro assinado |
| **D18** Poder & Política | 5 (liderança) · A.3 (papéis e responsabilidades) | Definição de responsável interno pelos sistemas | "Quem mata o projeto no corredor" e "quem responde pelo sistema" são a mesma pergunta com sinais trocados |
| **D06** Realidade das Pessoas + **D15** Decaimento de Conhecimento | 7.2–7.3 (competência e conscientização) · A.4 (recursos humanos) | Capacitação/letramento (dever de governança) | Composição de tarefas + conhecimento tácito = o diagnóstico de competência que a cláusula 7 pede |
| **D07** Experiência do Cliente | A.8 (informação a usuários; transparência) | Direito à **informação** (saber que interage com IA) | Os pontos de contato mapeados são onde o aviso de IA precisa aparecer |
| **D01/D10/D11** DNA, Lacuna de Visão, Inteligência Competitiva | 4.1–4.2 (contexto e partes interessadas) · 6.2 (objetivos) | · | O "porquê agora" e as partes interessadas · abertura obrigatória de qualquer SGIA |
| **D24** Construir Hoje vs. Amanhã + **D22** Penhasco de Escala | 6.1 · 8.1 (planejamento operacional) | · | Roadmap com gates = o plano de tratamento de risco da cláusula 6 |
| **D02/D13/D16/D17/D20/D21** Operação real | A.6 (operação, monitoramento, logs) | Registros/documentação dos sistemas | Fluxo real + exceções + latência = onde logging e monitoramento precisam existir |

### Sem correspondência direta, e está certo assim

**D04 (Mapa do Dinheiro)** é dimensão de negócio puro: nenhum marco regulatório pede mapa de vazamento financeiro. Registrar a ausência é parte da honestidade do mapa, não inflar cobertura.

---

## 3. O que as 25 dimensões NÃO cobrem: as 10 perguntas suplementares

O gap honesto: o framework avalia a **empresa para receber IA**; os marcos avaliam a **gestão da IA que já existe**. As 10 perguntas que fecham a diferença (aplicar na mesma rodada de entrevistas, ~20 min com o guardião):

| # | Pergunta | Cobre |
|---|---|---|
| 1 | Existe uma **política de IA escrita e aprovada** pela diretoria? Quem a assina? | A.2 |
| 2 | Existe um **inventário dos sistemas de IA em uso** (incluindo os embutidos em SaaS)? | 4.1 · aplicador (PL) |
| 3 | Quem é o **responsável nomeado** por cada sistema de IA · e a quem ele reporta? | A.3 · PL |
| 4 | Existe **canal para relatar preocupação** com um sistema de IA (funcionário ou cliente)? | A.3 · A.8 |
| 5 | Para cada sistema: existe **documentação técnica e log de eventos** recuperável? | A.6 |
| 6 | Existe **processo de resposta a incidente de IA** (quem decide desligar, quem comunica, em quanto tempo)? | A.8 · PL (incidente grave) |
| 7 | De onde vêm os **dados de cada sistema** (proveniência) e quem atesta a qualidade? | A.7 |
| 8 | Contratos com **fornecedores de IA** alocam responsabilidade (quem responde se o modelo errar)? | A.10 · cadeia de agentes (PL) |
| 9 | As pessoas afetadas **sabem quando estão interagindo com IA**? Onde está escrito? | A.8 · direito à informação (PL) |
| 10 | Alguma decisão automatizada afeta **direito de pessoa** (crédito, emprego, saúde…)? Existe caminho de **contestação e revisão humana**? | A.5 · alto risco + revisão humana (PL) |

**Regra de aplicação:** respostas viram semáforo (verde/amarelo/vermelho) por área, nunca "nota de conformidade" (nota sugere certificação, que não damos).

---

## 4. O entregável: seção "Prontidão regulatória" no relatório

Formato de uma página, ao final do relatório da avaliação:

| Área | Evidência (dimensões + perguntas) | Estado | O que fecha o gap |
|---|---|---|---|
| Contexto e liderança | D01/D10/D18 + P1, P3 | 🟢/🟡/🔴 | … |
| Risco e impacto | D09/D19/D23 + P10 | | … |
| Dados | D08/D12 + P7 | | … |
| Ciclo de vida e operação | D03/D21/operacionais + P2, P5, P6 | | … |
| Pessoas e competência | D06/D15 | | … |
| Transparência e direitos | D07/D14/D05 + P4, P9, P10 | | … |
| Terceiros | + P8 | | … |
| Medição e melhoria | D25 (protocolo de prova) | | … |

Rodapé obrigatório do entregável: *"Esta é uma leitura de prontidão, não uma auditoria de certificação. Certificação ISO/IEC 42001 exige organismo acreditado. O PL 2338 está em tramitação; obrigações finais dependem do texto sancionado."*

---

## 5. Encaixe comercial

- **Avaliação (R$ 28k):** ganha a seção de prontidão sem custo de campo adicional: as perguntas entram nas entrevistas existentes. Reforça o argumento de preço contra "agência faz por menos".
- **Workshop Shadow AI (R$ 14k):** o inventário (P2) é o que ele já produz: agora com a moldura "primeiro passo da prontidão ISO/PL". Porta lateral fortalecida.
- **Sprint LGPD (R$ 24k):** vizinho natural: mesma mesa (guardião), agora com a ponte IA×dados.
- **Para o diretor de IA do cliente:** este é o entregável que ele leva ao conselho: feito por terceiro, o que é exatamente o que dá valor. Vender **para** ele ([objeção](../03-comercial/objecao-diretor-de-ia.md) §2).
- **Fora do escopo por decisão:** virar consultoria de certificação/implantação ISO full, é outro negócio, com players estabelecidos. Ficamos na leitura de prontidão que nasce de graça do nosso próprio campo.

## Pendências

1. **Adquirir o texto da ABNT NBR ISO/IEC 42001** e conferir a numeração fina das cláusulas/controles citados (§2): antes do primeiro uso em cliente. (Custo: ~centenas de reais na loja ABNT: decisão de sócio pelo valor, não pelo mérito.)
2. **PL 2338 sancionado** → revisar §2 e o rodapé do entregável.
3. Se o uso manual (3 primeiras aplicações) provar valor → decidir se vira seção automática do relatório no assessment-brain (feature própria, fora deste doc).

## Ligações

[Estudo de imunidade](../05-interno/estudo-imunidade-diretor-de-ia.md): a melhoria nº 2 que este mapa executa · [Ferramenta: avaliação](ferramenta-avaliacao.md) · [Protocolo de prova](../04-entrega/protocolo-de-prova.md) · [Objeção: diretor de IA](../03-comercial/objecao-diretor-de-ia.md) · [Estudo de antecipação](../05-interno/estudo-antecipacao.md) §5: o calendário regulatório
