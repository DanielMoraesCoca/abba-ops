# Ferramenta: Agentes — ficha de negócio

> **Nome externo:** "Agentes ABBA" / serviços gerenciados · **stack interna:** CrewAI + roteamento de LLMs. Serve os estágios [07](../02-jornada-do-cliente/07-construcao-e-implantacao.md) e [09](../02-jornada-do-cliente/09-manutencao.md). (O repo ABBA original é legado/origem — nada aqui depende dele.)

## O que podemos prometer hoje

| ✅ Prometer | ⚠️ Com cuidado | ❌ Não prometer (ainda) |
|---|---|---|
| Agentes sob medida com **pontos de aprovação humana** e limites de custo, integrados aos sistemas do cliente | Prazo de construção: só após a conta/via CrewAI ativa (R9) — até lá, cronograma com folga de setup explícita | **24/7 / 99,5% / resposta em 4h** — congelado até a P9 definir o SLA sustentável |
| Deploy em nuvem gerenciada OU on-premise (a escolha é do cliente) | "Orquestramos o ecossistema (CrewAI, principais LLMs)" = uso de stack, verdadeiro | "Parceria formal com Microsoft/AWS/CrewAI" — congelado até a P8 confirmar o que existe assinado |
| Inventário de decisões automatizadas mapeado ao Art. 20 LGPD | Operação assistida de 30 dias pós go-live | Garantias de resultado — o que prometemos é medição honesta (projetado vs. realizado) |
| Manifesto de handoff: da avaliação sai o scaffold dos agentes (demonstrável) | | |

## Setup de cliente

- [ ] **Pré-requisito de venda:** via CrewAI decidida e conta ativa ANTES de assinar escopo com construção (R9)
- [ ] Workspace/projeto por cliente, segregado
- [ ] Integrações acordadas no kickoff (sistemas, credenciais DO CLIENTE, janelas de acesso)
- [ ] Pontos de aprovação humana definidos POR agente com o dono do processo
- [ ] Limites de custo configurados por agente
- [ ] Inventário Art. 20 iniciado no primeiro deploy · monitoramento ligado no go-live

## Custo por uso

| Operação | Custo de referência | |
|---|---|---|
| Execução de agente (LLM + infra) | {{MEDIR no protótipo do 1º cliente}} | → planilha e SLA (margem da manutenção) |
| Assinatura/infra CrewAI | {{DECIDIR via: Enterprise ~US$ 60–120k/ano vs. self-host ≈ custo de ops}} | → planilha, linha overhead |

## Dono e lacunas

**Operação:** chapéu [Entrega](../01-setores/entrega.md) · **Stack:** [Tecnologia](../01-setores/tecnologia.md). Lacunas ativas: R9 (conta CrewAI), R13 (SLA vs. capacidade — P9), R14 (parcerias — P8). Status no [mapa](mapa-jornada-ferramentas.md).
