# Metodologia de Precificação — ABBA

> **Status:** os preços antigos (R$ 280–450K programa; R$ 8–35K produtos de entrada) foram **descartados por decisão dos sócios** (ver [registro de decisões](../05-interno/registro-de-decisoes.md)) e sobrevivem apenas como referência histórica no anexo da [tabela de preços](tabela-de-precos.md). Esta metodologia reconstrói a precificação do zero. O preenchimento é feito na [planilha de precificação](precificacao-planilha.md).

## Princípio

Preço tem **piso** (o que custa entregar, com margem), **teto** (o que o mercado aceita) e **âncora de valor** (o que o cliente ganha). O preço certo fica entre piso×margem e teto, comunicado sempre pela âncora de valor — nunca por custo.

---

## Passo 1 — Piso de custo (o que uma hora dos sócios precisa render)

Fórmula:

```
CUSTO_ANUAL = RENDA_ALVO_SOCIO_A + RENDA_ALVO_SOCIO_B + OVERHEAD_ANUAL
PISO_HORA   = CUSTO_ANUAL ÷ (1 − IMPOSTOS_%) ÷ HORAS_FATURAVEIS_ANO
PISO_DIA    = PISO_HORA × 8
```

- `RENDA_ALVO_*`: pró-labore anual desejado por sócio. **Só os sócios podem definir.**
- `OVERHEAD_ANUAL`: soma das linhas de ferramenta/serviço (lista completa com estimativas de referência na planilha — API Claude, Vercel, Supabase, CrewAI, Workspace, contador, advogado, marketing).
- `IMPOSTOS_%`: depende do regime tributário — **pendência P5** (contador). Para simulação inicial, usar 15,5% (Simples Nacional Anexo III, faixa inicial) e refazer quando o contador definir.
- `HORAS_FATURAVEIS_ANO`: 2 sócios × 46 semanas úteis × 40h × utilização-alvo. **Utilização sugerida: 50–60%** — o resto do tempo é venda, administração e desenvolvimento das ferramentas. Empresa de consultoria nova raramente passa de 50%.

## Passo 2 — Custo por pacote

Para cada produto, estimar horas de entrega na tabela de esforço da planilha (horas por atividade, por sócio) e calcular:

```
CUSTO_PACOTE = HORAS_ESTIMADAS × PISO_HORA
PRECO_MINIMO = CUSTO_PACOTE × 2,5    ← margem mínima de consultoria
```

O multiplicador 2,5× cobre: retrabalho, venda não convertida, risco de escopo e formação de caixa. Abaixo disso, é melhor não vender.

## Passo 3 — Teto de mercado (pesquisa que os sócios executam)

Para cada pacote, levantar 3–5 comparáveis brasileiros e registrar na planilha:

| Onde pesquisar | O que perguntar/observar |
|---|---|
| Consultorias boutique de IA/dados (BR) | Preço de diagnóstico/assessment; day rate |
| Big-4 e consultorias médias | Day rate de consultor sênior (referência pública: R$ 3–8 mil/dia) |
| Plataformas de treinamento corporativo | Preço por colaborador/ano de programas de capacitação |
| Rede de contatos que já contratou consultoria | "Quanto pagou? Achou caro?" |
| Editais e licitações públicas de IA | Valores homologados (públicos) |

## Passo 4 — Âncora de valor por pacote

A proposta nunca justifica preço por custo — justifica por valor. Âncora padrão por produto:

| Produto | Âncora de valor |
|---|---|
| Workshop Shadow AI | Risco evitado: um incidente LGPD custa a partir de R$ 50 mil em multa + reputação |
| Avaliação de Prontidão | Decisão informada: erro de priorização em IA custa 6–12 meses e o orçamento do piloto |
| Sprint LGPD + IA | Multa LGPD: até 2% do faturamento (teto R$ 50 milhões) por infração |
| Programa completo | Horas economizadas/semana × custo médio do colaborador × 52 semanas |
| Manutenção | Custo de um agente parado × dias de indisponibilidade evitados |

## Passo 5 — Arquitetura de pacotes (mantida da estratégia anterior)

```
3 produtos de entrada (baixo atrito, convertem para o programa)
   → Programa completo (herói — engajamento de transformação)
      → Recorrentes (manutenção + continuidade do portal + mini-ciclos por caso de uso)
```

- Produto de entrada **credita 100%** no programa completo se o cliente converter em até 90 dias (regra herdada e mantida — remove objeção de "pagar duas vezes").
- Exceção: o Sprint LGPD **não credita** (produto genuinamente distinto, comprador distinto).

## Passo 6 — Condições de pagamento (padrão)

| Situação | Condição |
|---|---|
| Produtos de entrada | 50% na assinatura, 50% em até 10 dias úteis após entrega final |
| Programa completo | 30% assinatura / 30% no marco de implantação / 40% no encerramento — ou mensalizado |
| Recorrentes | Mensal ou anual antecipado com desconto a definir na planilha |
| Reajuste | IPCA anual em contratos recorrentes |
| Mora | 1% a.m. + correção IPCA (mesmo padrão do contrato-esqueleto) |
| Desconto charter | Só com contrapartidas formais (depoimento, métricas, logo, referências — Cláusula 5.3 do [contrato](contrato-sow-esqueleto.md)); desconto máximo definido na planilha |

## Passo 7 — Disciplina de descoberta de preço

Preço não se valida internamente — se valida em conversa:

1. Apresentar o preço-alvo nas **3 primeiras conversas reais** sem hesitar.
2. **2 reações de susto** ("sticker shock") → preço está alto demais OU âncora de valor mal comunicada — revisar a comunicação antes de baixar o preço.
3. **2 reações de "razoável" imediato** → preço está baixo — subir 20–30% na próxima conversa.
4. Registrar cada reação na planilha (aba de descoberta) e a decisão final no [registro de decisões](../05-interno/registro-de-decisoes.md).

## Saída

Planilha preenchida → [`tabela-de-precos.md`](tabela-de-precos.md) v1 fixada → decisão registrada. As propostas em `03-comercial/` referenciam a tabela por placeholder (`{{PRECO_*}}`) e só podem ser enviadas depois da tabela v1 existir.
