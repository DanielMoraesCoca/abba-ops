# Estudo — Visualizar a ABBA como ecossistema em tempo real ("Mission Control")

> **Status: ESTUDO — nenhuma decisão tomada.** Pedido do sócio (2026-07-27): pesquisar diligentemente a melhor forma de visualizar a empresa inteira e acompanhar tudo em tempo real, para decidir se vale a pena. Recomendação ao final; decisão é dos sócios (investimento de tempo do chapéu Tecnologia → porta de 2 vias, mas com custo de manutenção recorrente — ler o "contra" antes de empolgar).

## 1. O que a pesquisa diz (síntese com fontes)

**Os 3 sinais vitais de uma consultoria** (David A. Fields, referência da indústria): **caixa, saúde do pipeline e capacidade de entrega.** Um painel de consultoria que não responde esses três é decoração.

**A armadilha nº 1: dashboard de vaidade.** A regra de ouro da literatura: para cada número no painel, perguntar *"este número me ajuda a tomar uma decisão?"* — se não, ele não entra. Times pequenos caem no erro de exibir o que é fácil de medir em vez do que muda comportamento.

**A armadilha nº 2: custo de manutenção.** Todo painel é um sistema vivo: fonte de dados quebra, número desatualizado vira mentira institucional (pior que não ter painel). A heurística da literatura: se a manutenção passa de ~2h/semana, a ferramenta está errada para o tamanho do time.

**Tempo real vs. cadência:** observabilidade em tempo real (estilo Grafana) só paga quando existe operação contínua gerando eventos (agentes em produção, site público com leads). Para funil comercial e caixa, **cadência semanal é o padrão correto** — tempo real não muda nenhuma decisão dessas duas áreas.

## 2. As opções mapeadas (para o nosso contexto específico)

| Opção | O que é | Prós | Contras | Custo |
|---|---|---|---|---|
| **A. Mission Control no portal** (`/admin`) | Página nova no admin do abba-portal puxando Supabase (adoção, turmas, tiers) + export do vault (`abba vault --stats --json`) + planilha do pipeline (API do Sheets) | Stack que o Pedro já mantém · identidade visual nossa · o admin do portal JÁ tem um dashboard de operações para estender · vira vitrine (mostrável a cliente como prova de como operamos) | Dev do Pedro (estimativa 2–4 dias para v0) · assessment-brain é SQLite local — tempo real de verdade exigiria hospedar a API dele | R$ 0 de licença |
| **B. Metabase** (BI open-source) | Instância apontada para o Postgres do portal + CSVs | No-code, gráficos rápidos, alertas | Mais um serviço para hospedar/manter · não alcança bem SQLite local nem Sheets · cara genérica | Hospedagem ~US$ 10–20/mês ou self-host |
| **C. Looker Studio sobre o Sheets** | Painel gratuito do Google sobre a planilha de pipeline + números da pauta semanal | Zero infra · 1h de setup · suficiente pré-primeiro-cliente | Não é tempo real das ferramentas · manual · fora da identidade | R$ 0 |
| **D. Notion/Airtable como hub** | Replicar a operação numa ferramenta de workspace | Bonito rápido | **Conflita com a fonte da verdade** (este repo + Drive) — duplicação é o inimigo nº 1 que acabamos de eliminar | descartada |

## 3. O que a ABBA tem HOJE de dado vivo (inventário honesto)

| Fonte | Dado | Tempo real? |
|---|---|---|
| Portal (Supabase) | Adoção, progresso, turmas, tiers, custos da Iris | ✅ já é |
| assessment-brain (SQLite local) | Vault, engajamentos, custo por análise | ❌ local — export manual via `--json` |
| Assessment web | Leads/execuções | ⚠️ nem versionado ainda (R16) — captura de e-mail é pré-requisito |
| Pipeline | 20 alvos, estágios T0–T6 | ❌ planilha manual no Drive |
| Caixa | Fluxo | ❌ planilha manual |
| Log de INPUT | Métricas da semana | ❌ markdown, preenchido na reunião |

**Leitura fria:** hoje, um painel em tempo real mostraria zeros em tempo real. O dado que mais importa nesta fase (funil) é manual por natureza, e a cadência certa dele é semanal — exatamente o que a [pauta](pauta-reuniao-semanal.md) já cobre.

## 4. Recomendação (faseada — o gatilho é cliente, não vontade)

- **Fase 0 (agora):** não construir. O log da pauta semanal É o painel desta fase — 8 números, cadência certa, custo zero. Construir Mission Control antes do 1º cliente é procrastinação com cara de progresso.
- **Fase 1 (ao assinar o 1º cliente):** **Opção A, versão mínima** — 1 página no `/admin` do portal com os 3 sinais vitais (caixa · funil · entrega/adoção da turma) + card do vault. Fontes: Supabase (auto) + colagem semanal do `--json` + Sheets API. Critério de sucesso: os sócios abrem ANTES da reunião semanal e a reunião fica mais curta.
- **Fase 2 (3+ clientes, assessment web público):** tempo real de verdade — API do assessment-brain hospedada, webhook de leads do site, custo de API por engajamento ao vivo, alertas (S1 aberto, hora de evolução a 80%). Reavaliar A vs. B com o volume real.
- **Nunca:** opção D (duplicação da fonte da verdade) e qualquer número no painel que não responda "que decisão isso muda?".

**Por que vale a pena (a visão do sócio está certa, na hora certa):** a partir do 1º cliente, o mesmo painel que dirige a empresa vira **prova viva do posicionamento** — "instalamos capacidade dirigida por dados" fica muito mais crível quando o prospect vê que a própria ABBA opera assim. O erro seria só o timing, não a ideia.

## Fontes

- [David A. Fields — The Perfect Dashboard for Consulting Firms](https://davidafields.com/the-perfect-dashboard-for-consulting-firms/) (3 sinais vitais)
- [ERP/PSA dashboards para professional services](https://sysgenpro.com/erp/professional-services-erp-dashboards-for-executive-oversight-of-pipeline-and-delivery) (pipeline/utilização/margem num painel só)
- [Metabase vs. Grafana 2026](https://www.thebricks.com/resources/metabase-vs-grafana) · [comparativo de ferramentas open-source](https://www.fanruan.com/en/blog/open-source-metrics-dashboard-tools) (BI vs. observabilidade; Metabase = melhor custo/benefício SME)
- [Vanity metrics — o que rastrear no lugar](https://improvado.io/blog/what-is-a-vanity-metric) · [dashboards que dirigem decisão](https://f7i.ai/blog/building-a-maintenance-kpi-dashboard-that-actually-drives-decisions-not-just-data) (a pergunta-filtro e a heurística das 2h/semana)
- [Dashboard leve com Supabase + React + Vercel](https://jiradett.medium.com/how-i-built-a-personal-health-dashboard-with-claude-supabase-react-and-vercel-in-one-evening-c48dcb1f8788) · [Draxlr sobre Supabase](https://www.draxlr.com/blogs/how-to-build-dashboards-from-supabase-data/) (viabilidade da opção A com a stack atual)
