# Mapa Jornada × Ferramentas

> Qual ferramenta serve cada estágio da [jornada](../02-jornada-do-cliente/README.md), o estado real de cada uma, e a lacuna — **como risco gerenciado, não como backlog** (as lacunas relevantes têm entrada no [registro de riscos](../05-interno/registro-de-riscos.md)). Dono da manutenção deste mapa: chapéu [Tecnologia](../01-setores/tecnologia.md). Revisar mensalmente.

| Estágio | Ferramenta | Estado (2026-07) | Lacuna / observação |
|---|---|---|---|
| 01 Visitante e lead | Site de marketing | **Inexistente** (kit de reconstrução arquivado no abba-portal) | Topo de funil é 100% ativo (LinkedIn, indicação, e-mail frio); URLs antigas `*.vercel.app` não devem ir a prospect |
| 02 Degustação | assessment-brain (`abba scout`) | Funcional via CLI, uso interno | Não é público — degustação é gerada pelos sócios e apresentada ao vivo (decisão registrada em [apostas futuras](../00-identidade/apostas-futuras.md), aposta 2); exige provedor de busca real configurado |
| 03–04 Proposta e contrato | Templates deste repo + Drive + assinatura eletrônica | Templates prontos | Tabela de preços v1 pendente (P1) · advogado pendente (P4) · plataforma de assinatura a escolher |
| 05 Onboarding | Portal (tenant, contas) + assessment-brain (engajamento) | Funcional | Autenticação do portal é interina (cookie não assinado) — suficiente para charter, **não prometer SSO corporativo/procurement** até o cutover |
| 06 Avaliação profunda | assessment-brain (pipeline 25 dimensões, relatórios, one-pager, share-links) | Funcional; ~312 testes verdes | **Validado apenas em dados sintéticos** — o 1º cliente real é também a 1ª validação real (mitigação: escopo charter apertado); certificação com modelo de nível cliente pendente |
| 06→07 handoff | Export assessment-brain → portal (`/import`) | Funcional, validado no fixture sintético com teste de regressão | Nunca exercitado com engajamento real |
| 07 Construção | **CrewAI (direto)** — agentes sob medida com pontos de aprovação humana | Stack definida; conta pendente | Via de contratação a decidir (Enterprise vs. self-host) e configurar **antes** de assinar escopo com construção (risco R9) |
| 08 Capacitação | Portal (trilhas, desafios, Bússola, Iris, admin) + presencial | Conteúdo FINAL; produção pendente | Materiais completos ([catálogo](../08-materiais/README.md)): roteiros, kit de Kickoff, cards, prompts, desafios, lições CrewAI · falta: gravar vídeos, imprimir cards, carregar no portal · unificar nomes de nível (P7) |
| 09 Manutenção | CrewAI/infra própria (monitoramento) + portal | Parcial | Processo definido no [SLA](../04-entrega/sla-manutencao.md); tooling de alerta a montar no 1º contrato de manutenção |
| 10 Conselho | Relatórios/dashboards das ferramentas | Funcional | Material do ritual é montado manualmente a partir dos relatórios — ok para o porte atual |
| 11 Encerramento | Pacote de handover + vault (`abba outcome`) | Funcional | — |

## Leitura executiva

**Pronto para o primeiro cliente charter:** estágios 02–06 e 10–11 funcionam hoje com processo manual onde falta automação; o estágio 07 (construção) fica pronto com a contratação/setup do CrewAI — fazer **antes** de assinar escopo que inclua construção.
**As três lacunas que mais importam:** (1) validação com dados reais — resolvida PELO primeiro engajamento; (2) conta CrewAI — decisão Enterprise vs. self-host pendente; (3) produção da capacitação — roteiros e kit prontos; gravar os 3 vídeos de maior alavancagem primeiro. (O site importa para escalar aquisição, não para atender o 1º cliente.)

## Nota sobre o repo ABBA (legado)

O repo `ABBA` — a "plataforma de agentes" da fase produto da empresa — é **legado/origem**: guarda ativos reutilizáveis (padrões de aprovação humana, integrações, aprendizados) e a história de onde a ABBA veio. **Não é ferramenta de entrega atual** e não entra em promessa comercial. A construção de agentes é feita diretamente com CrewAI.
