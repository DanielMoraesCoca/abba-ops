# Calculadora de Construção — porte, preço e prazo sem improviso

> **Camada:** ferramenta (comercial + entrega). Criada na v2 da [tabela de preços](../03-comercial/tabela-de-precos.md) (V3t, 2026-08-06, sugestão do sócio). Uso: **toda proposta de construção sai daqui** — o comercial pontua com o que o [Assessment](../03-comercial/roteiro-descoberta-prototipo.md) e a descoberta revelaram, Pedro (chapéu Tecnologia) confere a pontuação técnica, e o resultado (porte + posição na faixa + semanas) vai **anexado à proposta** como transparência de escopo.
>
> É deterministico de propósito: duas pessoas pontuando a mesma empresa devem chegar ao mesmo porte. Divergência de pontuação = conversa antes da proposta, nunca depois.

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

## A régua

| Total (0–14) | Porte | Faixa de preço | Prazo típico | Manutenção de partida (Evolução) |
|---|---|---|---|---|
| **0–4** | **P** | **R$ 60–90 mil** | 6–8 semanas | R$ 9.500/mês (até 2 soluções) |
| **5–9** | **M** | **R$ 120–200 mil** | 10–16 semanas | R$ 9.500–14.500/mês conforme nº de soluções |
| **10–14** | **G** | **R$ 220–400 mil** | 18–28 semanas · por marcos | R$ 15.000+/mês (avaliar camada Estratégia) |

**Posição dentro da faixa:** interpolar pelo total. Ex.: M com 5 pontos → início da faixa (~R$ 120–140 mil); M com 9 pontos → topo (~R$ 180–200 mil). Arredondar para múltiplos de R$ 5 mil. Pagamento sempre **30/30/40 por marco** com critérios de aceite ([relatório de implantação](../08-materiais/modelos/relatorio-deployment-modelo.docx)).

**Gatilhos de exceção (fora da régua — proposta sob medida, sócios juntos):**
- Total 13–14 **e** fator 4 = 2 (missão crítica) → tratar como programa por marcos com hypercare estendido
- Fator 5 = 2 (on-premise) soma **+R$ 15–30 mil** de setup de ambiente à proposta, dito em linha própria
- Cliente exige exclusividade setorial ou SLA fora do padrão → precificar a exceção, nunca absorver

## Exemplo preenchido

Empresa M do assessment Brasal-like: 2 soluções (1) · integração com ERP + planilhas (1) · dados digitais mas bagunçados (1) · erro caro com aprovação desenhada (1) · nuvem do cliente (1) · 2 áreas (1) · fluxo muda em parte (1) = **7 pontos → M, meio da faixa → R$ 160 mil, ~13 semanas**, manutenção de partida R$ 9.500/mês. Confere com o cheque de sanidade da tabela (hora implícita ~R$ 420).

## Ligações

[Tabela de preços v2](../03-comercial/tabela-de-precos.md) · [Roteiro de descoberta](../03-comercial/roteiro-descoberta-prototipo.md) (os blocos 1–5 alimentam os fatores) · [Ficha da ferramenta de agentes](ferramenta-agentes.md) · [SLA](../04-entrega/sla-manutencao.md)
