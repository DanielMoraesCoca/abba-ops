# Calculadora de Porte — o tamanho do Programa e da Assinatura, sem improviso

> **Camada:** ferramenta (comercial + entrega). Criada na v2 da tabela (V3t) como calculadora de construção; **na Virada V5 muda de função: deixa de precificar construção avulsa e passa a dimensionar o porte do [Programa](../00-identidade/modelo-de-servico.md) e da Assinatura da Capacidade** ([tabela v3](../03-comercial/tabela-de-precos.md) — proposta, Pedro valida). Uso: **toda proposta de Programa anexa o resultado desta calculadora** (transparência do porte) — o comercial pontua com o que a descoberta revelou, Pedro (chapéu Tecnologia) confere a pontuação técnica.
>
> É determinístico de propósito: duas pessoas pontuando a mesma empresa devem chegar ao mesmo porte. Divergência de pontuação = conversa antes da proposta, nunca depois.

## Os 7 fatores (pontuar 0 · 1 · 2 cada)

| # | Fator | 0 pontos | 1 ponto | 2 pontos |
|---|---|---|---|---|
| 1 | **Nº de soluções** a construir | 1 | 2–3 | 4+ |
| 2 | **Integrações** | nenhuma ou exportação manual (arquivo) | 1–2 sistemas com integração direta | 3+ sistemas, ou sistema sem interface de integração (automação de tela/desenvolvimento sob medida) |
| 3 | **Dados** | digitais e padronizados, prontos | precisam de limpeza/estruturação | escaneados/foto/áudio, espalhados ou de baixa qualidade |
| 4 | **Criticidade e aprovações** | erro tolerável, revisão simples | erro caro — aprovação humana desenhada em pontos-chave | missão crítica/regulado — aprovação em tudo, trilha de auditoria, inventário Art. 20 extenso |
| 5 | **Ambiente** | nossa nuvem gerenciada | nuvem do cliente (contas e políticas deles) | on-premise (infraestrutura do cliente, janelas de acesso) |
| 6 | **Usuários e áreas** | 1 equipe, ≤10 usuários | 2–3 áreas, ≤50 usuários | empresa toda ou 50+ usuários |
| 7 | **Mudança de processo** | a solução encaixa no fluxo atual | o fluxo muda em parte (retreinar hábitos) | o processo é redesenhado junto com a solução |

## A régua (V5)

| Total (0–14) | Porte | Programa — Ano 1 | Estrutura de pagamento | Assinatura — Ano 2+ |
|---|---|---|---|---|
| **0–4** | **P** | **R$ 218.000** | 26.000 (fase 1, na assinatura do Termo) + 4 × 48.000 (trimestres antecipados) | **R$ 11.000/mês** |
| **5–9** | **M** | **R$ 278.000** | 26.000 + 4 × 63.000 | **R$ 15.000/mês** |
| **10–14** | **G** | **R$ 378.000** | 26.000 + 4 × 88.000 | **R$ 21.000/mês** |

**O preço do Programa é fixo por porte** — a tabela v3 não tem faixa a interpolar. A posição do total dentro do porte serve ao **planejamento interno**: um M com 7 pontos estima esforço de fase 2 no meio da antiga faixa (~13 semanas de construção); um M com 9, no topo. Uso interno de equipe e prazo, nunca dito ao cliente como variação de preço.

> **Nota de histórico:** as faixas antigas de construção avulsa (P R$ 60–90 mil · M R$ 120–200 mil · G R$ 220–400 mil, 6–28 semanas) **não são mais preço** — ficam como memória de cálculo interna do esforço da fase 2, nunca expostas a cliente.

**Sinalizações internas (não mudam o preço — acendem conversa entre os sócios antes da proposta):**
- Total 13–14 **e** fator 4 = 2 (missão crítica) → prever hypercare estendido na fase 3 e marcos de aceite mais finos
- Fator 5 = 2 (on-premise) → esforço extra de setup de ambiente dentro da fase 2 (memória de cálculo do porte G)
- Cliente exige exclusividade setorial ou SLA fora do padrão → fora da régua; sócios decidem caso a caso, nunca absorver em silêncio

## Exemplo preenchido

Empresa M do assessment Brasal-like: 2 soluções (1) · integração com ERP + planilhas (1) · dados digitais mas bagunçados (1) · erro caro com aprovação desenhada (1) · nuvem do cliente (1) · 2 áreas (1) · fluxo muda em parte (1) = **7 pontos → porte M → Programa R$ 278.000** (26.000 + 4 × 63.000) · **Assinatura ano 2+ R$ 15.000/mês**. Esforço interno de fase 2 equivalente ao meio da antiga faixa M (~13 semanas — memória de cálculo, não preço).

## Ligações

[Tabela de preços v3](../03-comercial/tabela-de-precos.md) · [Modelo de serviço V5](../00-identidade/modelo-de-servico.md) · [Roteiro de descoberta](../03-comercial/roteiro-descoberta-prototipo.md) (os blocos 1–5 alimentam os fatores) · [Ficha da ferramenta de agentes](ferramenta-agentes.md) · [SLA](../04-entrega/sla-manutencao.md)
