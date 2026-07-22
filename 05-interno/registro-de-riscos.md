# Registro de Riscos — ABBA

> Riscos **gerenciados**, revisados mensalmente na reunião de sócios. Formato: risco · impacto · mitigação/gatilho de ação · dono (chapéu). **Nota:** os itens técnicos vêm do [mapa jornada × ferramentas](../06-ferramentas/mapa-jornada-ferramentas.md) e são riscos a gerenciar, não backlog de código deste repositório.

| # | Risco | Impacto | Mitigação / gatilho de ação | Dono |
|---|---|---|---|---|
| R1 | **Método validado só em dados sintéticos** — a avaliação em 25 dimensões nunca rodou com cliente real | Relatório abaixo do prometido no engajamento mais importante (o primeiro) | 1º cliente em modalidade **charter com escopo apertado** (1 departamento, 1 caso de uso, desconto formal por contrapartidas); rodada com modelo de nível cliente + edição pesada dos sócios; expectativa honesta no contrato | Entrega |
| R2 | **Contrato sem revisão jurídica** | Cláusula LGPD/PI/responsabilidade frágil em disputa | **Nenhuma assinatura sem revisão de advogado** (P4); alçada definida na [planilha](../03-comercial/precificacao-planilha.md) | Fin-Admin |
| R3 | **Autenticação interina do portal** (cookie não assinado) | Bloqueia procurement enterprise; risco de acesso indevido | Não prometer SSO/segurança corporativa até o cutover; charter ciente; cutover antes de cliente com procurement formal | Tecnologia |
| R4 | **Sem site / topo de funil manual** | Aquisição depende 100% de esforço ativo dos sócios | Meta semanal de prospecção ativa ([estágio 01](../02-jornada-do-cliente/01-visitante-e-lead.md)); site entra após 1º charter (kit de reconstrução existe) | Comercial |
| R5 | **Vídeos da capacitação pendentes** (8 lições Foundation com marcador) | Trilha do 1º cliente incompleta na plataforma | Priorizar SOMENTE a trilha do departamento do 1º cliente; presencial cobre lacuna no início; revisão pt-BR nativa antes de uso real | Capacitação |
| R6 | **Bus factor = 2** — tudo depende de 2 pessoas | Férias/doença param a empresa | Suplente definido por chapéu; processos deste repo mantidos executáveis por qualquer um dos dois; gatilhos de contratação no [README de setores](../01-setores/README.md) | Sócios |
| R7 | **Sem domínio/e-mail profissional** | Percepção amadora no primeiro contato | P2 imediata (domínio + Workspace) — **bloqueia envio de proposta** | Fin-Admin |
| R8 | **Sem tabela de preços v1** | Proposta improvisada, margem corroída | P1: planilha preenchida antes de qualquer proposta; disciplina de descoberta de preço | Comercial |
| R9 | **Conta/infra CrewAI não contratada** (via indefinida: Enterprise vs. self-host) | Estágio 07 não executa de ponta a ponta hoje; custo da via escolhida afeta a precificação | Decidir a via e configurar **antes de assinar escopo com construção**; até lá, vender construção com prazo que acomode o setup; refletir o custo na [planilha](../03-comercial/precificacao-planilha.md) | Tecnologia |
| R10 | **Custo de API despercebido** | Margem corroída silenciosamente em avaliações/Iris | Custo por engajamento monitorado no checklist semanal de Tecnologia; alimenta a planilha de precificação | Tecnologia |
| R11 | **Dependência de suboperadores** (LLM, nuvem) | Mudança de preço/termos dos provedores afeta margem e LGPD | Anexo II do contrato mantido atualizado; revisão semestral de alternativas | Tecnologia |
| R12 | **Promessas históricas nos docs antigos** (preços, "29 semanas", URLs) circulando | Prospect encontra material desatualizado/contraditório | Banners de HISTÓRICO aplicados nos repos; todo material novo nasce deste repo | Comercial |

## Processo
- Novo risco → linha nova com número sequencial.
- Risco materializado → vira ação imediata + retrospectiva na reunião seguinte.
- Risco encerrado → riscar (~~texto~~) com data e motivo — nunca apagar.
