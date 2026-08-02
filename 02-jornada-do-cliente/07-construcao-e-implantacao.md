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

**Protótipo de validação (o marco que destrava o GO/NO-GO e a parcela de 30%)**
- [ ] Protótipo do caso de uso prioritário construído: agente funcional em produção limitada, **com dados reais**, validado com usuários-chave
- [ ] Métricas do protótipo medidas contra o critério de sucesso combinado no kickoff (nunca "impressão" — número)
- [ ] [Relatório de Protótipo](../08-materiais/modelos/relatorio-prototipo-modelo.docx) emitido com a recomendação GO/NO-GO
- [ ] **Decisão GO/NO-GO da diretoria registrada** (`abba decision advance ... --by`) + [Termo de Aceite](../04-entrega/termo-de-aceite.md) do marco → **faturar a parcela do protótipo validado** — avisar Fin-Admin
- [ ] NO-GO não é fracasso: é o método funcionando — registrar o porquê e re-priorizar com o portfólio da avaliação

**Construção (após o GO)**
- [ ] Agente construído **diretamente com CrewAI** (conta/via contratada no setup — risco R9: não assinar cronograma de construção antes disso), sob medida, com pontos de aprovação humana e limites de custo configurados
- [ ] Teste com dados de homologação (**nunca** dados reais em teste)
- [ ] Demonstração ao dono do processo → ajustes → aceite registrado por escrito

**Implantação**
- [ ] Go-live com acompanhamento diário na primeira semana
- [ ] Inventário de decisões automatizadas atualizado (Art. 20 LGPD — checkpoint humano identificado por decisão)
- [ ] Medição baseline capturada (para o projetado vs. realizado)
- [ ] Relatório de deployment emitido + [Termo de Aceite](../04-entrega/termo-de-aceite.md) assinado → **faturar a parcela do marco** — avisar Fin-Admin

## Saída
Agente(s) em produção com critério de sucesso medindo → [08-capacitacao](08-capacitacao-e-transformacao.md) (roda em paralelo) e [09-manutencao](09-manutencao.md) (após período de operação assistida).

## Ferramentas e templates
assessment-brain (export handoff → manifesto CrewAI) · CrewAI · [relatório de protótipo](../08-materiais/modelos/relatorio-prototipo-modelo.docx) e [de deployment](../08-materiais/modelos/relatorio-deployment-modelo.docx) · [termo de aceite](../04-entrega/termo-de-aceite.md) · Drive `04 Construcao/`
