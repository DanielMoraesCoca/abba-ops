# Auditoria profunda do Assessment v2 — 2026-08-20

> Reanálise de tudo que foi construído nas ondas v2 (maturidade, anexo visual, princípios executáveis, semeadura de decisões), a pedido do Daniel: "tenha a certeza de que não há nenhuma oportunidade de melhoria". Método: revisão adversarial do código novo + pesquisa de mercado com fontes + execuções ponta a ponta com dados degenerados. **Resultado honesto: havia sim oportunidades, e várias eram graves.** O que era defeito foi corrigido e travado com teste; o que é decisão de produto está na segunda metade deste documento.

## Parte 1 — Defeitos encontrados e corrigidos (commit `f163852`)

### Confidencialidade e LGPD (os dois críticos)

| # | O que estava errado | Por que importava | Correção |
|---|---|---|---|
| 1 | O **anexo visual era o único entregável que ignorava a criptografia em repouso**: gravava a análise inteira do cliente (nome, veredito, vazamentos em dólar, TCO) em HTML puro, ao lado do relatório cifrado | Notebook roubado: o relatório vira ruído, o anexo abre no navegador | Segue a mesma regra 1B dos outros: cifrado no local padrão, cópia legível só com `--output` explícito. O PDF vai no mesmo envelope |
| 2 | **`abba forget` não conseguia apagar o anexo**: dos dois arquivos gravados, só um entrava na tabela `reports` — e a certidão de exclusão ainda atestava "ZERO RESIDUE" | Uma atestação de apagamento comprovadamente falsa é pior que nenhuma | Todo arquivo escrito é registrado; o teste novo falha se um deles ficar órfão |

### Honestidade do número que o cliente vê

3. **Maturidade fabricada do nada:** com zero pilares pontuáveis, o cálculo devolvia nível 1 "Improvisado" (o divisor `|| 1` transformava ausência de evidência no pior veredito possível) — inclusive no one-pager que vai por link compartilhado. Agora fica "sem leitura", e o título informa em quantos dos 6 pilares ele se apoia.
4. **Radar desenhava pilar sem leitura no centro**, sugerindo um nível zero que não existe na escala, ao lado de um título calculado só com os pilares que pontuaram. Eixos sem leitura agora são omitidos.
5. **"Maior vazamento" estava errado em dois eixos:** lia uma coluna inexistente (imprimia o enum cru, tipo `knowledge_concentration`) e pegava o mais *severo*, não o maior — contradizendo o selo ao lado na mesma página. Agora usa o nome e o mesmo valor com desconto de sobreposição dos totais.

### A doutrina estava se auto-enganando

6. **Três princípios checavam a seção errada** (`interventions`, que é "Broader Strategic Moves", em vez de `ai-interventions`, o plano de IA). A tabela Method Integrity negava princípios que o relatório carregava e carimbava ✓ em princípios ausentes.
7. **O teste da "garantia" era auto-referencial:** usava um fixture escrito à mão, então apagar uma seção do gerador não quebrava o CI (verificado: passava). Agora existe `test/integration/assessment-v2.test.js`, que roda o pipeline real e confere os princípios contra a lista de seções realmente emitida. **Sabotagem testada: apagar `sections.push('data-foundation')` derruba o CI.**

### Arco narrativo (a Fase 3 estava pela metade)

8. O apêndice dimensão a dimensão (~40% do relatório) ficava **entre** o plano de intervenções e as seções que dizem como executar — o plano de adoção e o willing-area gate do Rafael ficavam encalhados depois de 330 linhas de apêndice. Agora existe `# Appendix: The Full Evidence`, depois das seções de ação.
9. O **willing-area gate sumia** em rodadas com intervenções mas sem riscos políticos/S-S-K/HITL, porque estava preso à guarda de outro bloco.

### Robustez e operação

10. Payback não-finito imprimia literalmente **"NaN m"** no anexo do cliente. 11. Heatmap gerava `viewBox` negativo (não renderiza nada) quando todas as dimensões falhavam; **cortava a última linha e mentia no título fixo "As 25 dimensões"** no framework v2; engolia a primeira palavra de títulos longos. 12. `--output foo.html` gravava um `foo.pdf` silencioso; `--output report.md` virava `report.md.html`. 13. **`abba decision seed` duplicava decisões a cada reassessment** (ids de intervenção são por rodada), poluindo a fila da manhã e o denominador do Brier — agora casa por vínculo OU título. 14. `abba doctor` passou a dizer se o PDF do anexo vai renderizar (antes só se descobria na reunião).

**Estado final:** 470/470 testes verdes (com e sem `ABBA_DB_PASSPHRASE`), eval mock OK, `prompts.js` e `framework.js` intocados.

## Parte 2 — Oportunidades que são decisão dos sócios (não corrigi por conta própria)

Ranqueadas por quanto custam com o **primeiro comprador enterprise**. Fontes na [pesquisa de mercado](pesquisa-assessment-mercado.md).

| # | Lacuna | Situação hoje | Decisão necessária |
|---|---|---|---|
| **1** | **Conteúdo regulatório** | A [ficha comercial](../06-ferramentas/ferramenta-avaliacao.md) **promete** "seção de prontidão regulatória", mas a ferramenta não a produz. O framework (D09) cita GDPR/HIPAA/SOX, **não** cita LGPD, AI Act nem ISO 42001 | Ou construir a seção (camada de agregação, sem tocar prompts travados), ou tirar a promessa da ficha. Hoje há descasamento entre o que se vende e o que sai |
| **2** | **Idioma dos artefatos do cliente** | O anexo visual é PT-BR; **o one-pager e o deck, que são os artefatos que vão para o cliente (inclusive por link), estão em inglês** | Escolher um padrão. Nota: o Daniel já disse na reunião que o inglês foi decisão consciente um dia, e a Sophy usa inglês+dólar de propósito. Mas hoje está inconsistente entre dois artefatos do mesmo cliente |
| **3** | **Sem "wrapper" humano no entregável** | Documentos entram, relatório sai. O mercado entrega protocolo de entrevistas, workshop executivo e sessão de validação dos achados | É método, não código: o mais barato de fechar e o que mais separa "produto" de "consultoria" |
| **4** | **Evals e observabilidade por construção** | Cada intervenção tem "measurement plan"; o mercado de 2026 espera golden dataset, harness de eval, LLM-as-judge calibrado e portão de CI | Define credibilidade técnica diante do time de tecnologia do cliente |
| **5** | **Modelo de ameaças por recomendação** | Nada mapeia OWASP LLM/Agentic Top 10, tiering de autonomia, injeção de prompt, kill-switch | Recomendação agêntica sem isso não passa em revisão de segurança |
| **6** | **Business case que o CFO assina** | Custo/payback existem; falta baseline formal, indicadores de 6 meses e **um instrumento de acompanhamento entregue ao cliente** | A maquinaria já existe no cérebro (decisões, triggers, outcomes, Brier) — é reempacotar, não construir |
| **7** | **Artefatos de governança** | Saem julgamentos, não saem política de IA, inventário, risk register, RACI, charter de CoE | Compradores ISO 42001 pedem ~20-25 artefatos |
| **8** | **Build/buy/partner e TCO de 3 anos** | O plano assume "construir"; não classifica comprar/parceirizar nem lista fornecedores | |
| **9** | **Âncora externa da maturidade** | A escala é honesta ("não é benchmark de mercado"), mas o comprador pergunta "comparado a quem?" | Ancorar em dados públicos (Stanford AI Index, Census BTOS) ou no vault com o n impresso |

## Parte 3 — O que NÃO foi verificado (honestidade sobre os limites desta auditoria)

- **Status do PL 2338/2023 é incerto.** Havia votação prevista na Câmara para 27/05/2026, mas não achei fonte confirmando que ocorreu nem o resultado; uma fonte aponta dezembro, e há projetos concorrentes (PL 2.688/2025, PL 762/2026, PL 704/2026). **Não afirmar em material de cliente que o Brasil "já tem lei de IA" antes de conferir na tramitação oficial.**
- **Correção regulatória relevante:** o Digital Omnibus da UE (em vigor 27/07/2026) **adiou** as obrigações de alto risco do Anexo III para 02/12/2027. Mas o **Artigo 50 (transparência) está valendo desde 02/08/2026**, com multa de até €15M ou 3% do faturamento, e o Artigo 4 (letramento em IA) segue operante. Se algum material nosso disser "vale a partir de agosto de 2026" de forma genérica, precisa ser ajustado.
- **sophyworks.ai continua bloqueado** pelo proxy do ambiente: tudo o que sabemos vem de trechos de busca e do relato do Rafael. Preço em dólar, fundador e a alegação de ">90% das iniciativas entregues" não puderam ser confirmados de forma independente.
- **A terceira frente da auditoria (varredura ampla do repositório: features meio-ligadas, cobertura de testes de risco, consistência entre os quatro artefatos, custo de API) não terminou** — o agente morreu por limite de sessão. Fica como próxima passada.
