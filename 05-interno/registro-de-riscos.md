# Registro de Riscos — ABBA

> Riscos **gerenciados**, revisados mensalmente na reunião de sócios. Formato: risco · impacto · mitigação/gatilho de ação · dono (chapéu). **Nota:** os itens técnicos vêm do [mapa jornada × ferramentas](../06-ferramentas/mapa-jornada-ferramentas.md) e são riscos a gerenciar, não backlog de código deste repositório.

| # | Risco | Impacto | Mitigação / gatilho de ação | Dono |
|---|---|---|---|---|
| R1 | **Método validado só em dados sintéticos** — a avaliação em 25 dimensões nunca rodou com cliente real | Relatório abaixo do prometido no engajamento mais importante (o primeiro) | 1º cliente em modalidade **charter com escopo apertado** (1 departamento, 1 caso de uso, desconto formal por contrapartidas); rodada com modelo de nível cliente + edição pesada dos sócios; expectativa honesta no contrato | Entrega |
| R2 | **Contrato sem revisão jurídica** | Cláusula LGPD/PI/responsabilidade frágil em disputa | **Nenhuma assinatura sem revisão de advogado** (P4); alçada definida na [planilha](../03-comercial/precificacao-planilha.md) | Fin-Admin |
| R3 | **Autenticação interina do portal** (cookie não assinado) | Bloqueia procurement enterprise; risco de acesso indevido | Não prometer SSO/segurança corporativa até o cutover; charter ciente; cutover antes de cliente com procurement formal | Tecnologia |
| R4 | **Topo de funil parcialmente resolvido, desalinhado** — o assessment web (`assessment.abbaservices.com.br`) está NO AR gerando relatórios profundos, mas com visual fora do padrão (teal vs. navy/dourado), nomes fora da tabela oficial ("Assessment", "Discovery de IA") e sem CTA/captura de lead clara | Prospect recebe 42 páginas de graça sem conversa — e vê uma marca diferente da dos documentos | Alinhar marca + nomes + CTA + estratégia de gating (teaser público, relatório completo na apresentação ao vivo); prospecção ativa continua como canal principal | Comercial + Tecnologia |
| R5 | **Vídeos da capacitação não gravados** — os roteiros word-for-word e todo o material estão FINAIS ([catálogo](../08-materiais/README.md)), mas os vídeos não existem e os cards não foram impressos | Trilha do 1º cliente incompleta na plataforma | Seguir a ordem do próprio material: gravar primeiro os 3 vídeos de maior alavancagem (1.3.3, 1.3.1, 2.1.2) + imprimir os 6 cards; Kickoff presencial cobre o início; personalizar slots [PERSONALIZAR] com o 1º cliente | Capacitação |
| R6 | **Bus factor = 2** — tudo depende de 2 pessoas | Férias/doença param a empresa | Suplente definido por chapéu; processos deste repo mantidos executáveis por qualquer um dos dois; gatilhos de contratação no [README de setores](../01-setores/README.md) | Sócios |
| R7 | **Sem domínio/e-mail profissional** | Percepção amadora no primeiro contato | P2 imediata (domínio + Workspace) — **bloqueia envio de proposta** | Fin-Admin |
| R8 | **Sem tabela de preços v1** | Proposta improvisada, margem corroída | P1: planilha preenchida antes de qualquer proposta; disciplina de descoberta de preço | Comercial |
| R9 | **Conta/infra CrewAI não contratada** (via indefinida: Enterprise vs. self-host) | Estágio 07 não executa de ponta a ponta hoje; custo da via escolhida afeta a precificação | Decidir a via e configurar **antes de assinar escopo com construção**; até lá, vender construção com prazo que acomode o setup; refletir o custo na [planilha](../03-comercial/precificacao-planilha.md) | Tecnologia |
| R10 | **Custo de API despercebido** | Margem corroída silenciosamente em avaliações/Iris | Custo por engajamento monitorado no checklist semanal de Tecnologia; alimenta a planilha de precificação | Tecnologia |
| R11 | **Dependência de suboperadores** (LLM, nuvem) | Mudança de preço/termos dos provedores afeta margem e LGPD | Anexo II do contrato mantido atualizado; revisão semestral de alternativas | Tecnologia |
| R12 | **Promessas históricas nos docs antigos** (preços, "29 semanas", URLs) circulando | Prospect encontra material desatualizado/contraditório | Banners de HISTÓRICO aplicados nos repos; todo material novo nasce deste repo | Comercial |

| R13 | **Promessas de SLA acima da capacidade** — proposta emitida promete 24/7, 99,5% uptime e resposta em 4h com uma equipe de 2 pessoas | Quebra de promessa contratual no 1º incidente fora de horário | Pendência P9: definir SLA sustentável (ex.: horário comercial + plantão crítico) e corrigir proposta + SLA antes da próxima emissão | Entrega |
| R14 | **Parcerias citadas em proposta sem confirmação formal** (CrewAI, Microsoft, AWS, plataforma de educação) | Prospect verifica e a credibilidade cai | Pendência P8: mapear o que é contrato assinado vs. uso-de-stack vs. intenção; ajustar o texto ("parceiros tecnológicos" vs. "stack utilizada") | Comercial |
| R15 | **Método 4D sob licença CC BY-NC-SA** (cláusula não-comercial) usado em programa pago | Risco de violação de licença do material pedagógico central | Validação jurídica na pauta do advogado (P4); manter atribuição obrigatória em todo material até lá | Fin-Admin |

## Processo
- Novo risco → linha nova com número sequencial.
- Risco materializado → vira ação imediata + retrospectiva na reunião seguinte.
- Risco encerrado → riscar (~~texto~~) com data e motivo — nunca apagar.
