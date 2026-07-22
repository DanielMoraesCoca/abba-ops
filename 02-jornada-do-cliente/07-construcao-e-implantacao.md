# Estágio 07 — Construção e Implantação

**Dono:** chapéu Entrega · **Prazo-alvo:** conforme cronograma do Anexo I (referência: 2–4 semanas por agente)

## Entrada
Plano aprovado pela diretoria ([06](06-avaliacao-profunda.md) + sessão de alinhamento): quais agentes, em que ordem, com que critério de sucesso.

## Checklist

**Especificação (por agente)**
- [ ] Exportar o manifesto de handoff do assessment-brain (specs das intervenções ranqueadas → scaffold CrewAI)
- [ ] Spec revisada com o dono do processo no cliente: entradas, saídas, **pontos de aprovação humana**, sistemas integrados, critério de sucesso mensurável
- [ ] Decisão de hospedagem registrada: on-premises do cliente OU nuvem gerenciada ABBA (Anexo II atualizado se muda suboperador)
- [ ] Spec arquivada em `02 Clientes/<Nome>/04 Construcao/`

**Construção**
- [ ] Agente construído **diretamente com CrewAI**, sob medida, com pontos de aprovação humana e limites de custo configurados
- [ ] Teste com dados de homologação (**nunca** dados reais em teste)
- [ ] Demonstração ao dono do processo → ajustes → aceite registrado por escrito

**Implantação**
- [ ] Go-live com acompanhamento diário na primeira semana
- [ ] Inventário de decisões automatizadas atualizado (Art. 20 LGPD — checkpoint humano identificado por decisão)
- [ ] Medição baseline capturada (para o projetado vs. realizado)
- [ ] Marco de implantação atingido → **faturar 2ª parcela** (30%) — avisar Fin-Admin

## Saída
Agente(s) em produção com critério de sucesso medindo → [08-capacitacao](08-capacitacao-e-transformacao.md) (roda em paralelo) e [09-manutencao](09-manutencao.md) (após período de operação assistida).

## Ferramentas e templates
assessment-brain (export handoff → manifesto CrewAI) · CrewAI · sistemas do cliente · Drive `04 Construcao/`
