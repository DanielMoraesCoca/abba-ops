# Finanças Básicas — rotina mínima

> A rotina financeira de uma consultoria de 2 sócios: simples, mas sem furo. Dono: chapéu [Fin-Admin](../01-setores/financeiro-admin.md). Instâncias (planilha de caixa, NFs, contratos) vivem em `04 Interno/Financeiro/` no Drive.

## Setup inicial (uma vez — a maioria depende do contador, P5)

- [ ] CNPJ ativo com CNAEs de consultoria/treinamento/desenvolvimento ({{verificar com contador}})
- [ ] **Regime tributário definido com o contador**: Simples Nacional (Anexo III vs. V — fator R decide; consultoria com pró-labore alto tende ao III, ~15,5% inicial) vs. Lucro Presumido. Registrar a decisão
- [ ] Conta PJ aberta (banco digital PJ resolve: {{Inter/Cora/Itaú...}})
- [ ] Emissor de NFS-e configurado (prefeitura ou emissor do contador)
- [ ] Pró-labore dos sócios definido (valor + dia do mês) — alinhado com a [planilha de precificação](../03-comercial/precificacao-planilha.md) (renda-alvo)
- [ ] Planilha de fluxo de caixa criada no Drive (modelo simples: entradas previstas/realizadas, saídas fixas/variáveis, saldo, runway)

## Rotina por evento

**Contrato assinado** ([estágio 04](../02-jornada-do-cliente/04-contrato.md)): lançar as parcelas previstas no fluxo de caixa · emitir NF da 1ª parcela · enviar cobrança com dados de pagamento.

**Marco atingido** (2ª/3ª parcela, mensalidade): emitir NF · cobrar · baixar no fluxo quando cair.

**Pagamento atrasado**: D+3 lembrete cordial por e-mail · D+10 cobrança formal citando a cláusula de mora (1% a.m. + IPCA) · D+30 pausar conforme contrato/SLA e tratar na reunião de sócios.

## Rotina fixa

| Ritmo | Ação |
|---|---|
| Semanal (reunião de sócios) | Caixa e runway em voz alta · a receber vencido? · a pagar em 15 dias? |
| Mensal | Fechar o mês na planilha · conferir NFs × recebimentos · guias de imposto pagas (contador) · métricas do setor (receita, despesa, % recorrente) |
| Trimestral | Revisar assinaturas de ferramentas (algo pago sem uso?) · runway vs. metas do [plano de negócio](../00-identidade/plano-de-negocio.md) |
| Anual | Reajuste IPCA dos recorrentes no aniversário · revisão da tabela de preços · planejamento tributário com o contador |

## Regras

1. **NF para tudo, sempre.** Sem exceção, sem "combina depois".
2. Despesa nova recorrente > R$ {{LIMITE}}/mês → decisão dos dois sócios, registrada.
3. Runway < {{6}} meses → modo alerta: pauta prioritária da reunião semanal até resolver.
4. Dinheiro da empresa ≠ dinheiro dos sócios: pró-labore no dia definido, retirada extra só por decisão registrada.
