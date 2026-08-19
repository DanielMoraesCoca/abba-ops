# Ferramenta: Avaliação — ficha de negócio

> **Nome externo:** "Análise ABBA" (degustação) e "Avaliação em 25 dimensões" · **interno:** assessment-brain. Serve os estágios [02](../02-jornada-do-cliente/02-diagnostico-gratuito.md) e [06](../02-jornada-do-cliente/06-avaliacao-profunda.md). Engenharia vive no repo da ferramenta — aqui é só o negócio. Linhas `{{CONFIRMAR}}` precisam de validação dos sócios.

## O que podemos prometer hoje

| ✅ Prometer | ⚠️ Com cuidado | ❌ Não prometer (ainda) |
|---|---|---|
| Análise por informação pública (scout) apresentada em 5 dias úteis | Prazo da avaliação profunda: 2–3 semanas (depende da agenda de entrevistas DO CLIENTE — deixar explícito) | Benchmarks entre clientes (exige 3+ clientes no vault) |
| Avaliação em 25 dimensões com entrevistas do conselho à linha de frente | Primeira execução com dados reais — enquadrar como charter: método validado, primeira aplicação real com escopo controlado (risco R1) | "Método certificado em clientes reais" — ainda não é verdade |
| Relatórios editados pelos sócios + one-pager + quantificação rastreável | Assessment web (no ar em URL própria, **ainda não aberto ao público** — ver abaixo): alinhamento visual/CTA/gating entra ANTES do lançamento | |
| Compartilhamento seguro: só o one-pager anonimizado, link com expiração | | |
| **Maturidade em IA por pilar** (6 pilares × 5 níveis nomeados: Improvisado·Consciente·Estruturado·Instalado·Composto) + **Veredito de Fundação de Dados** (FRÁGIL/PARCIAL/PRONTA) — derivados DESTA análise, nunca vendidos como benchmark de mercado | **Anexo visual de 7 páginas** (`abba report <eng> --visual`: capa-veredito, radar, heatmap 25D, matriz valor×esforço, roadmap 3 horizontes, Contar o Custo, limite honesto) — construído e testado em mock; **apresentar a cliente só após o gate real do Cliente Zero** | |

## Assessment v2 (2026-08-19) — a camada que o cliente vê

Melhoria estruturada a partir da reunião Rafael/Brasal + [pesquisa de mercado](../05-interno/pesquisa-assessment-mercado.md) + [princípios do método](../00-identidade/principios-do-assessment.md). O que mudou na ferramenta (tudo agregação pós-análise; prompts travados intocados; 456 testes verdes):

- **Relatório reordenado para a narrativa que vende:** Veredito em 60 segundos → Sumário → Maturidade por pilar → Fundação de Dados → achados → plano → apêndices profundos.
- **`abba report <eng> --visual`** gera o anexo visual (PDF via Chromium; sem Chromium, HTML imprimível). One-pager ganhou a miniatura de maturidade (continua anonimizado, seguro para share-link).
- **Fase M (motor: 4 análises LLM novas)** aprovada mas sequenciada DEPOIS do gate real — flag `ABBA_ASSESSMENT_V2`, default off. Nada disso vai a cliente antes da Etapa 1 do [Cliente Zero](../05-interno/cliente-zero-execucao.md).

## Prontidão regulatória (ISO/IEC 42001 + PL 2338)

A avaliação pode entregar, sem campo adicional, uma seção de **prontidão regulatória**: o [mapa 25 dimensões × ISO 42001 × PL 2338](mapa-avaliacao-iso42001-pl2338.md) mostra qual evidência as entrevistas já coletam e as 10 perguntas suplementares que fecham o resto. Travas: é leitura de prontidão, **nunca certificação** (não somos organismo acreditado); PL 2338 ainda em tramitação — conferir o mapa antes de prometer.

## Superfície web (assessment.abbaservices.com.br)

O assessment no ar gera relatórios profundos por informação pública (fontes citadas com nível de confiança, formato Situação/Complicação/Resolução). **Consistência verificada em 3 execuções** (Brasal/deep 42p · Grupo Santa/quick 30p · ABC DataSaúde/quick 31p): mesma estrutura e qualidade, com consciência regulatória por setor.

**Confirmado pelos sócios (2026-07-24):**
- **Motor:** assessment-brain — **porém o site público NÃO está no repositório** (inspeção 2026-07-25: sem página de visitante, sem captura; o `web/` do repo é o console interno) → risco [R16](../05-interno/registro-de-riscos.md): Pedro commita o site inteiro antes de qualquer evolução. Guia pronto no próprio repo: `docs/ALINHAMENTO-WEB.md`
- **Ainda não aberto ao público** — vantagem estratégica: captura de e-mail, gating e visual entram ANTES do lançamento, sem retrofit
- **Captura de e-mail antes do resultado:** indefinida no fluxo atual → requisito obrigatório da [spec de alinhamento](spec-alinhamento-assessment-web.md) (seção 4)
- **Custo por execução:** não medido — {{MEDIR na próxima execução e registrar na planilha}}

Pendências de alinhamento no [Caminho Crítico](../05-interno/plano-de-acao.md): visual (navy/dourado) · nomes (tabela oficial) · CTA final · gating. Achados adicionais das 3 amostras:
- **Nunca enviar PDFs gerados na versão de preview** — o rodapé de execuções antigas traz URL de staging (`amber-summit-taak.here.now`) em todas as páginas; só circular PDFs com `assessment.abbaservices.com.br` no rodapé
- Modo *quick* ocasionalmente puxa fonte irrelevante ("Rede Santa Catarina" num assessment do Grupo Santa, confiança baixa) — revisão humana de fontes antes de qualquer uso comercial do PDF
- Mesmo o modo *quick* entrega ~30 páginas — reforça a decisão de gating (teaser público, completo na apresentação)

## Setup de cliente (executar no [estágio 05](../02-jornada-do-cliente/05-onboarding.md))

- [ ] Criar cliente + engajamento na ferramenta
- [ ] Provedor de busca real configurado para o scout ({{PEDRO VERIFICAR: qual provedor está ativo — sócios não souberam responder em 2026-07-24}}) — **nunca** enviar brief marcado como pesquisa sintética
- [ ] Convenção de ingestão acordada entre os sócios: níveis (conselho → linha de frente) e fases desde a 1ª entrevista
- [ ] Modelo de nível cliente selecionado para o entregável (nunca o modelo barato)
- [ ] Ao encerrar: feedback/outcome + **mín. 3 padrões anonimizados** registrados no vault (E3 — bloqueante no [estágio 11](../02-jornada-do-cliente/11-renovacao-e-encerramento.md)) e ciclo de retenção de dados iniciado. Métrica viva: nº de padrões por setor via `abba vault --stats --json` — citável em proposta quando ≥ 3 ([playbook](../05-interno/playbook-vault.md))

## Custo por uso (alimenta a [planilha de precificação](../03-comercial/precificacao-planilha.md))

| Operação | Custo de referência | Registrar onde |
|---|---|---|
| Scout (degustação) | {{MEDIR na 1ª execução real}} | Planilha, linha overhead API |
| Avaliação completa (modelo econômico, uso interno) | ~R$ 5 (referência da ferramenta) | idem |
| Avaliação completa (modelo de nível cliente) | ~R$ 130 (referência) — {{MEDIR na 1ª execução}} | idem |

Regra: anotar o custo real de CADA engajamento — é o número que protege a margem.

## Dono e lacunas

**Operação:** chapéu [Entrega](../01-setores/entrega.md) · **Saúde/infra:** [Tecnologia](../01-setores/tecnologia.md). Lacunas ativas: R1 (validação em dados reais — resolvida PELO primeiro charter). Status geral no [mapa](mapa-jornada-ferramentas.md).
