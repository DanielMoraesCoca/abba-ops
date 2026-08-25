# Estágio 08 — Capacitação e Transformação (híbrida)

**Dono:** chapéu Capacitação · **Prazo-alvo:** contínuo durante o engajamento; plano fechado até 1 semana após o kickoff

## Entrada
Onboarding concluído; participantes com conta na plataforma; [plano de capacitação](../04-entrega/plano-de-capacitacao.md) preenchido para o cliente.

## O modelo híbrido

| Trilho | O quê |
|---|---|
| **Plataforma (assíncrono)** | Trilhas por nível (Explorador → Praticante → Especialista → Arquiteto), aulas próprias em pt-BR (vídeos ABBA em gravação por lotes — [ficha](../06-ferramentas/ferramenta-portal.md)), desafios práticos avaliados pela Rubrica ABBA, Bússola (**Parar / Começar / Só eu** — redação canônica 19/08), Iris disponível o tempo todo — e a **academia diária** (Currículo v3, 23/08): Prática de Hoje na home, Boletim semanal, Biblioteca de Pedidos, cenários de decisão, Minhas Ferramentas — o portal entre as aulas e depois delas |
| **Presencial (síncrono)** | Sessão de abertura (lançamento do programa com o patrocinador) · workshops nos marcos (por nível ou por departamento) · sessão de encerramento/graduação |
| **Topo da progressão** | Participantes nível Arquiteto ganham acesso a ferramentas de criação de agentes (CrewAI) para construir soluções dos próprios fluxos — com curadoria da ABBA |

## Checklist

**Lançamento**
- [ ] Plano de capacitação aprovado pelo patrocinador (trilhas × papéis, cadência, datas presenciais)
- [ ] **`turma:preflight` rodado no ambiente da turma** → 0 bloqueadores (o script audita currículo E operação: migrações, segredo de sessão, provedor de e-mail, estoque do Boletim)
- [ ] **Turma criada com nome próprio** — "Turma {{N}} da {{Empresa}}" (formato único, decisão E4) em `/admin/turmas`: início e fim declarados, graduação agendada desde o dia 1
- [ ] **Roster importado** em `/admin/roster` (lista nominal do cliente), pessoas vinculadas à turma, **convites disparados** — conferir na tela que o e-mail saiu, não só o sino
- [ ] Catálogo do tenant publicado (as trilhas contratadas visíveis à turma)
- [ ] **[Ficha de Linha de Base](../08-materiais/ficha-linha-de-base.md) aplicada no kickoff** (bloco de 30 min) — sem dia 0 não há relatório d90, e o d90 é o que assinamos
- [ ] Sessão presencial de abertura realizada (patrocinador abre; ABBA conduz; Bússola preenchida ao vivo por todos)

**Ritmo (semanal)**
- [ ] Adoção monitorada no admin do portal: % ativos, progresso por nível, desafios, Bússola
- [ ] Departamento travado (<{{PCT}}% ativos por 2 semanas) → diagnóstico com o gestor + intervenção (sessão extra, ajuste de trilha, conversa do patrocinador)
- [ ] Nudges no canal do cliente (logística por WhatsApp/Slack conforme [política](../05-interno/comunicacao.md))

**Marcos**
- [ ] Workshops presenciais dos marcos realizados (presença + feedback arquivados)
- [ ] Promoções de nível celebradas no canal (visibilidade importa)
- [ ] Campeões identificados e desenvolvidos (candidatos: primeiros Especialistas)
- [ ] Graduação em `/admin/graduacao`: o portão (Fundação 8/8 + ≥6/8 drills) conferido NA TELA, pessoa a pessoa, e as credenciais verificáveis emitidas **em lote** na cerimônia (idempotente — re-clicar não duplica; exceções são decisão humana, fora do lote)

**Depois da graduação (o estágio não acaba aqui — correção 24/08: a versão anterior terminava na cerimônia e deixava a nossa maior promessa sem dono)**
- [ ] A academia diária segue como rotina da turma (Prática de Hoje, Boletim de segunda — a régua "não é curso que acaba; é academia que a pessoa frequenta")
- [ ] Marcos de durabilidade **d30 · d60 · d90**: o portal cobra evidência dos compromissos; gestor corrobora no painel
- [ ] Reaplicação da Ficha de Linha de Base no d90 (mesma redação, agendada com o patrocinador)
- [ ] **[Relatório de Durabilidade de 90 dias](../04-entrega/relatorio-d90-modelo.md) preparado, assinado e entregue em reunião** — é o fecho do serviço 5 e a ponte comercial para protótipos/construção

## Saída
Equipe operando no dia a dia + campeões formados + **relatório d90 assinado na mesa da diretoria** → alimenta [09-manutencao](09-manutencao.md), a venda da Turma 2 e o [pacote de handover do estágio 11](11-renovacao-e-encerramento.md).

## Ferramentas e templates
Portal ABBA (trilhas, admin, Iris, Bússola) · [plano de capacitação](../04-entrega/plano-de-capacitacao.md) · Drive `05 Capacitacao/`
