# Precificação — Proposta do Especialista (pesquisa + modelo + tabela-rascunho)

> Elaborada em 2026-07-23 com pesquisa de mercado e tributária citada. **Falta apenas 2 insumos dos sócios** (renda-alvo e horas/semana) para travar a tabela v1 — as tabelas de cenários abaixo permitem se localizar imediatamente. Complementa a [metodologia](precificacao-metodologia.md) e alimenta a [planilha](precificacao-planilha.md).

## 1. Tributos — o número real para Brasília/DF (pesquisado)

**Regime recomendado: Simples Nacional, Anexo III via Fator R.** A jogada fiscal inteira:

| Fato pesquisado | Número | O que significa para a ABBA |
|---|---|---|
| Fator R ≥ 28% (folha+pró-labore ÷ receita 12m) → **Anexo III** | alíquota inicial **6%** | Manter pró-labore total dos sócios ≥ 28% da receita → tributação começa em 6% (vs. 15,5% no Anexo V) |
| Anexo III, faixa até R$ 180 mil/ano | 6% efetivo | Cenário do 1º ano |
| Anexo III, R$ 180–360 mil/ano | ~7,3–8,2% efetivo | Cenário ano 1–2 |
| Anexo III, R$ 360–720 mil/ano | ~9,5–10,7% efetivo | Cenário de crescimento |
| Fator R < 28% → Anexo V | 15,5%+ | Evitar: custa ~2× mais |
| ISS Brasília/DF para TI (CNAE 62, incl. 6204-0 consultoria em TI) | **2%** (LC 963/2020; geral é 5%) | Dentro do DAS no Simples; relevante se um dia migrar para Lucro Presumido |
| INSS sobre pró-labore (sócio) | 11% (sem patronal no Simples III) | Custo do pró-labore |
| IRPF 2026: pró-labore até R$ 5.000/mês | **isento** (reforma 2026) | Pró-labore ótimo: R$ 5.000/sócio (isento de IR) + distribuição de lucros (isenta) |
| Lucro Presumido (comparação) | ~13,33% federal + 2% ISS + 20% INSS patronal | Só compensa muito acima do teto do Simples — ignorar por anos |

**Provisão recomendada sobre a receita: 12%** (DAS ~7–9% nas faixas do ano 1–2 + margem de segurança). Conservador: 15%.
**Estrutura de retirada recomendada:** pró-labore de R$ 5.000/sócio/mês (satisfaz o Fator R até ~R$ 430 mil/ano de receita, IRPF zero, INSS R$ 550/sócio) + o restante como distribuição de lucros isenta. ⚠️ Validar com o contador (P5) — esta é a tese; ele confirma o CNAE e o enquadramento.

## 2. Mercado — onde a ABBA pode se posicionar (pesquisado)

| Referência | Faixa |
|---|---|
| Valor-hora consultoria no Brasil (geral) | R$ 70 – R$ 1.000+ |
| **Consultor sênior/especialista TI (faixa mais comum)** | **R$ 200 – R$ 450/h** |
| Consultoria estratégica / premium (Big-4 no topo) | > R$ 500/h |
| Workshops de IA in-company | mercado ativo (KPMG, boutiques); preços sob consulta — sinal de categoria premium |

**Leitura:** com método proprietário + ferramentas próprias + entrega de sistemas (não slides), a ABBA se posiciona legitimamente em **R$ 300–400/h implícitos** — meio-alto da faixa sênior, abaixo do premium Big-4 (coerente com "custamos uma fração").

## 3. Esforço estimado por pacote (base: escopos das propostas)

| Pacote | Horas estimadas (2 sócios somados) | Racional |
|---|---|---|
| Workshop Shadow AI | ~35h | prep 12h + kickoff/logística 6h + sessão 2×2h + relatório 48h ~10h + follow-up 3h |
| Avaliação de Prontidão (2 sem) | ~70h | kickoff 4h + entrevistas 16h + ingestão/análise 12h + edição dos 3 relatórios 24h + briefing+debrief 8h + coord. 6h |
| Sprint LGPD (2–3 sem) | ~60h | kickoff 4h + inventário/mapeamento 20h + framework+pacote 24h + revisões/entrega 12h |
| Programa completo (16 sem) | ~450h | avaliação 70h + protótipo 120h + deployment 100h + capacitação 100h + gestão/rituais 60h |
| Manutenção mensal | ~20h/mês | monitoramento 8h + ajustes 6h + relatório 3h + ritual amortizado 3h |

## 4. Piso da hora — cenários (localizem-se e escolham)

`PISO = (renda anual dos 2 sócios + overhead R$ 36k/ano estimado) ÷ (1 − 12% tributos) ÷ horas faturáveis`
`Horas faturáveis = 2 sócios × 46 sem × horas/sem dedicadas × 55% de utilização`

| Cenário | Renda-alvo/sócio/mês | Horas/sem dedicadas (cada) | Horas faturáveis/ano | **Piso/h** |
|---|---|---|---|---|
| A — começo conservador | R$ 8.000 | 20h | 1.012 | **R$ 256** |
| B — dedicação séria | R$ 12.000 | 25h | 1.265 | **R$ 291** |
| C — full na ABBA | R$ 20.000 | 35h | 1.771 | **R$ 331** |

Todos os cenários caem DENTRO da faixa de mercado sênior (R$ 200–450/h) → **o negócio fecha em qualquer cenário razoável.** Nota de método: o piso já embute renda+overhead+tributos na utilização assumida — preço ≥ piso é sustentável; o multiplicador da metodologia vira **colchão de 1,3–1,5×** (protege contra utilização abaixo do previsto), não 2,5× sobre o piso cheio.

## 5. TABELA-RASCUNHO (cenário B, hora-alvo R$ 350 — meio da banda de posicionamento)

| Produto | Custo (h × piso B) | **Preço-alvo recomendado** | Faixa publicada | Validação de mercado |
|---|---|---|---|---|
| Workshop Shadow AI | R$ 10.185 | **R$ 12.500** | R$ 10–15 mil | hora implícita R$ 357 ✓ |
| Avaliação de Prontidão | R$ 20.370 | **R$ 25.000** | R$ 20–32 mil | R$ 357/h ✓ · era o produto de R$ 45k na proposta Galápagos como "Assessment" de 4-5 sem — coerente |
| Sprint LGPD + IA | R$ 17.460 | **R$ 22.000** | R$ 18–30 mil | R$ 367/h ✓ |
| **Programa completo (16 sem)** | R$ 130.950 | **R$ 160.000** | R$ 140–220 mil (por porte/escopo) | **R$ 356/h ✓ — e valida os R$ 150K emitidos à Galápagos (estavam bem calibrados!)** |
| Manutenção mensal | R$ 5.820/mês | **R$ 8.500/mês** | R$ 7–12 mil/mês | inclui infra + margem de risco de plantão |
| Mini-ciclo (caso de uso adicional) | ~R$ 35.000 | **R$ 45.000** | R$ 35–60 mil | ~100h |

Políticas (mantidas da metodologia): entrada credita 100% no programa em 90 dias (exceto Sprint LGPD) · 50/50 nas entradas, 30/30/40 no programa · IPCA anual nos recorrentes · desconto charter máx. **20%** só com Anexo III do contrato · alçada advogado: contratos > R$ 50 mil.

## 6. O que falta para virar tabela v1 (registrar no log ao travar)

1. Sócios escolhem o cenário (A/B/C) ou dão os números reais → recalculo em minutos
2. Resposta da Galápagos aos R$ 150K (dado de descoberta nº 1)
3. Confirmação do contador: CNAE + Anexo III + estratégia de pró-labore (P5)

## Fontes da pesquisa

- Fator R / Anexos III e V: [Contabilizei](https://www.contabilizei.com.br/contabilidade-online/anexo-3-simples-nacional/) · [Contabilidade.com](https://contabilidade.com/blog/fator-r-no-simples-nacional-2026-como-calcular-exemplos-praticos-e-quando-servicos-migram-do-anexo-v-para-o-iii/) · [e-Auditoria](https://www.e-auditoria.com.br/blog/anexo-iii-ou-anexo-v-simples-nacional/) · [Agilize](https://artigos.agilize.com.br/tabela-simples-nacional-servicos-2026/)
- ISS DF 2% para TI (LC 963/2020): [licitacaoecontrato.com.br](https://www.licitacaoecontrato.com.br/noticia/reducao-aliquota-iss-servicos-tecnologia-informacao31012020.php) · [Meu Escritório Virtual](https://meuescritoriovirtual.com.br/blog/iss-brasilia/)
- Pró-labore/INSS/IRPF 2026: [ContaJá](https://contaja.com.br/blog/inss-pro-labore/) · [Contabilizei](https://www.contabilizei.com.br/contabilidade-online/inss-pro-labore/) · [Trivium](https://triviumcontabil.com.br/pro-labore/)
- Valor-hora mercado: [RDD10+ (estudo 2024-25)](https://www.robertodiasduarte.com.br/analise-do-valor-hora-em-consultorias-no-brasil-2024-2025-2/) · [BID Consultoria](https://bidconsultoria.com/valor-hora-consultoria-empresarial/) · [Expansion](https://expansioncontabilidade.com.br/valor-de-consultoria-no-brasil-saiba-quanto-custa/)
- Workshops IA in-company (categoria): [KPMG Business School](https://kbs.kpmg.com.br/workshopinteligenciaartificial/p) · [HiveAgent](https://hiveagent.com.br/servicos/workshop)
