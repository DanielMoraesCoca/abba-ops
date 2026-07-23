# Planilha de Precificação — preencher pelos sócios

> Preencher **numa sentada, juntos**. Seguir a [metodologia](precificacao-metodologia.md). Ao final: transcrever para [`tabela-de-precos.md`](tabela-de-precos.md), registrar no [registro de decisões](../05-interno/registro-de-decisoes.md) (pendência P1). Campos `{{ }}` = só os sócios podem responder.

## 1. Base de custo

| Campo | Valor | Nota |
|---|---|---|
| Renda-alvo anual Sócio A (pró-labore) | R$ {{ }} | O que você PRECISA ganhar/ano para esta empresa fazer sentido |
| Renda-alvo anual Sócio B | R$ {{ }} | idem |
| **Overhead anual** | soma abaixo ↓ | |
| · API Anthropic/Claude (avaliações + Iris) | R$ {{ }} | ref.: ~R$ 5/avaliação em Haiku, ~R$ 130 em Sonnet; estimar nº de engajamentos/ano |
| · Vercel + Supabase + Render | R$ {{ }} | ref.: US$ 40–100/mês somados nos planos pagos iniciais |
| · CrewAI | R$ {{ }} | ref.: Enterprise ~US$ 60–120 mil/ano OU self-host ≈ R$ 0 + ops. **Decisão embutida: qual via?** |
| · Google Workspace + domínio | R$ {{ }} | ref.: ~R$ 40/usuário/mês × 2 |
| · Contador | R$ {{ }} | ref.: R$ 400–1.200/mês para serviços |
| · Advogado (pacote LGPD + contrato, ano 1) | R$ {{ }} | ref.: R$ 10–30 mil no ano 1 (do checklist do fundador) |
| · Marketing (site, LinkedIn, eventos) | R$ {{ }} | |
| · Outros (seguro, viagens não repassadas...) | R$ {{ }} | |
| Impostos (% sobre receita) | {{ }}% | simulação inicial: 15,5% (Simples Anexo III) — confirmar com contador (P5) |
| Semanas úteis/ano por sócio | {{ 46 }} | 52 − férias − feriados − doença |
| Horas/semana dedicadas à ABBA por sócio | {{ }} | honestidade > otimismo |
| Utilização faturável | {{ }}% | sugerido 50–60% |

**Cálculo:**

```
HORAS_FATURAVEIS = 2 × semanas × horas/semana × utilização% = {{ }}
CUSTO_ANUAL      = rendas + overhead                        = R$ {{ }}
PISO_HORA        = CUSTO_ANUAL ÷ (1 − impostos%) ÷ HORAS_FATURAVEIS = R$ {{ }}
PISO_DIA         = PISO_HORA × 8                            = R$ {{ }}
```

## 2. Esforço e custo por pacote

Estimar horas TOTAIS dos dois sócios por entrega (usar os escopos das propostas em `03-comercial/` como referência de atividades):

| Pacote | Horas estimadas | Custo (h × piso) | Preço mínimo (×2,5) |
|---|---|---|---|
| Workshop Shadow AI (prep + sessão 90min + relatório 48h + follow-up) | {{ }} | R$ {{ }} | R$ {{ }} |
| Avaliação de Prontidão (2 semanas: kickoff, pré-trabalho, entrevista, briefing, relatório) | {{ }} | R$ {{ }} | R$ {{ }} |
| Sprint LGPD + IA (2–3 semanas) | {{ }} | R$ {{ }} | R$ {{ }} |
| Programa completo (avaliação + construção de 1–3 agentes + capacitação híbrida + 30d operação) | {{ }} | R$ {{ }} | R$ {{ }} |
| Manutenção mensal (monitoramento + ajustes + relatório) | {{ }}/mês | R$ {{ }}/mês | R$ {{ }}/mês |
| Mini-ciclo por caso de uso adicional | {{ }} | R$ {{ }} | R$ {{ }} |

## 3. Teto de mercado (pesquisa — mín. 3 comparáveis por linha)

| Pacote | Comparável 1 | Comparável 2 | Comparável 3 | Teto adotado |
|---|---|---|---|---|
| Workshop | {{ }} | {{ }} | {{ }} | R$ {{ }} |
| Avaliação | {{ }} | {{ }} | {{ }} | R$ {{ }} |
| Sprint LGPD | {{ }} | {{ }} | {{ }} | R$ {{ }} |
| Programa | {{ }} | {{ }} | {{ }} | R$ {{ }} |
| Manutenção | {{ }} | {{ }} | {{ }} | R$ {{ }}/mês |

## 4. Preço-alvo final (entre mínimo e teto)

| Pacote | Preço-alvo | Faixa publicada (± ajustes de porte) |
|---|---|---|
| Workshop Shadow AI | R$ {{ }} | R$ {{ }} – {{ }} |
| Avaliação de Prontidão | R$ {{ }} | R$ {{ }} – {{ }} |
| Sprint LGPD + IA | R$ {{ }} | R$ {{ }} – {{ }} |
| Programa completo | R$ {{ }} | R$ {{ }} – {{ }} |
| Manutenção (mensal) | R$ {{ }} | R$ {{ }} – {{ }} |
| Mini-ciclo | R$ {{ }} | R$ {{ }} – {{ }} |

## 5. Políticas

| Política | Decisão |
|---|---|
| Desconto charter máximo (com contrapartidas da Cl. 5.3) | {{ }}% |
| Desconto por pagamento anual antecipado (recorrentes) | {{ }}% |
| Crédito do produto de entrada no programa (prazo) | 100% em até {{ 90 }} dias |
| Alçada: acima de R$ {{ }} exige revisão de advogado antes de assinar | (pendência P4) |

## 6. Descoberta de preço (preencher após cada conversa real)

| Data | Prospect | Pacote | Preço dito | Reação (susto / neutro / fácil demais) | Ajuste? |
|---|---|---|---|---|---|
| 2026-06 | Galápagos Capital (ref ABBA-2026-001) | Assessment R$ 45K + Protótipo R$ 65K + Deployment R$ 40K = **R$ 150K** (30/30/30/10) | R$ 150.000 | {{REGISTRAR: qual foi a resposta?}} | — |

> ⚠️ Único dado real de mercado até agora: a proposta emitida em jun/2026 a **R$ 150K** pelo engajamento de 12–16 semanas. Registrar a reação do prospect acima — é o primeiro teste da disciplina de descoberta de preço.
