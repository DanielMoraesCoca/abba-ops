# Estudo — IA na Área Financeira: onde o cliente VÊ o dinheiro

> **Status**: pesquisa concluída (2026-07-31, 3 frentes, ~50 buscas EN+PT). Propostas de oferta ao final são **candidatas — pauta de sócios**. Nada aqui altera a [tabela de preços v1](../03-comercial/tabela-de-precos.md) nem as portas vigentes.
>
> **A tese do sócio que motivou o estudo**: "se conseguirmos criar algo que eles consigam ver o DINHEIRO deixando de ser gasto, aumentando a receita, aumentando o ganho, isso é especial."
>
> A pesquisa confirma a tese com um refinamento crucial: **o diferencial não é achar o dinheiro — dezenas de players fazem isso. É PROVAR o dinheiro de um jeito que o CFO assina.** E a ABBA já construiu, sem saber, a máquina de prova (ver §5).

---

## 1. As 10 famílias de solução — com números documentados

| # | Família | O que a IA faz | Número-âncora (fonte/ano) | Aplicabilidade mid-market BR |
|---|---|---|---|---|
| 1 | **Contas a pagar / NF-e** | OCR+LLM extraem e lançam notas, matching 2/3-vias, detectam duplicidades | Custo/nota US$ 9,40 → US$ 2,78 (−70%, Ardent Partners 2025); duplicatas = 0,1–0,5% do spend; payback BR 6–12 meses | **ALTA** — NF-e estruturada torna o BR ideal para automatizar AP |
| 2 | **Cobrança / inadimplência** | Régua multicanal (WhatsApp), priorização por propensão, agente negociador | DSO −20 a −28% (cases HighRadius 2024-25); Neofin BR: ROI 1.756% em 48 dias; agente IA 2× mais eficaz que chatbot (Moveo 2026) | **ALTA** — dor nº 1 do CFO em 2026 (recorde de inadimplência PJ) |
| 3 | **Conciliação bancos/cartões** | Matching probabilístico extrato×ERP×adquirentes; confere taxas cobradas a maior | 10–15h → <1h por conta/mês; **payback mediano 21 dias** (ProcIndex 2025); Conta Azul: 20–30h/mês | **ALTA** — em varejo/franquia, taxa de adquirente errada é R$ recuperado todo mês |
| 4 | **Previsão de fluxo de caixa** | Forecast 13 semanas sobre AR/AP + histórico; prevê quem atrasa | Precisão 62% → 89% em 2 tri (Stacc 2026); buffers de liquidez −22% | **ALTA** — com Selic alta, R$ 1M de giro liberado vale ~R$ 150–200k/ano em juros; split payment obriga todo CFO a reprojetar caixa |
| 5 | **Análise de gastos / compras** | LLM classifica 100% do spend; detecta maverick spend e price creep | Maverick = até 20% do gasto indireto (GEP); auditoria recupera 2–4% do spend | MÉDIA — exige volume de compras e contratos formalizados |
| 6 | **Fraude / anomalias em pagamentos** | Analisa 100% das transações (vs. amostra de 10–20% manual) | Fraude ocupacional = 5% da receita/ano (ACFE 2024); Toyota/AppZen: US$ 700k capturados | MÉDIA — número probabilístico até o 1º achado; empacotar dentro de AP |
| 7 | **Pricing dinâmico** | Otimiza preço por SKU/canal; detecta desconto excessivo por vendedor | +2–5% receita, +5–10% margem bruta (McKinsey); 1% no preço = +8,7% lucro operacional | MÉDIA — upside enorme, mas 3–6 meses, dados limpos e risco político |
| 8 | **FP&A / fechamento automatizado** | Concilia, lança recorrentes, comenta variações via LLM | Fechamento 10–15 dias → ≤5 (−62% com ≥50% automação, Deloitte 2024) | MÉDIA — métrica clara, mas é tempo (soft), não caixa |
| 9 | **Auditoria de despesas/reembolsos** | Audita 100% dos reembolsos contra política | Cobertura 10–20% → 100% (AppZen) | BAIXA-MÉDIA — T&E pequeno no mid-market; módulo, não produto |
| 10 | **Fiscal/tributário BR** ⭐ | Cruza XML/SPED/NCM para achar tributo pago a maior; simula malha; prontidão IBS/CBS | **95% das empresas pagam errado; ~R$ 100 bi recuperáveis (IBPT)**; cases R$ 1,4M–3,6M por empresa; IA corta 95% do tempo de análise | **ALTA (a maior)** — cheque literal no caixa, êxito elimina risco, reforma cria urgência 2026–2033 |

**Top 5 por "dinheiro visível × viabilidade"**: (1º) fiscal/tributário, (2º) cobrança, (3º) contas a pagar, (4º) conciliação, (5º) previsão de caixa.

**Achado transversal**: as famílias 1+3+4+10 compartilham os MESMOS dados — ERP + extratos + XML fiscal/SPED. E os dados fiscais a empresa é **obrigada por lei a ter** — mata a objeção "nossos dados não estão prontos". Um único pipeline de ingestão habilita quatro ofertas.

---

## 2. Como o CFO VÊ o dinheiro — a mecânica da prova

### 2.1 Hard vs. soft savings (a taxonomia que decide a venda)

- **Nível 1 — Hard (o CFO assina)**: caixa recuperado (crédito tributário, duplicata, cobrança), despesa eliminada (linha de orçamento menor), preço reduzido (fatura antiga vs. nova), **capital de giro liberado** (dias de DSO × faturamento diário × custo de capital), receita incremental com grupo de controle.
- **Nível 2 — Semi-duro (aceito com metodologia)**: custo evitado com baseline acordado ANTES; custo unitário de processo (custo/nota, custo/cobrança).
- **Nível 3 — Soft (o CFO desconta 50–100%)**: "horas economizadas × custo da hora" — a métrica favorita dos vendors de IA e a MAIS desacreditada ("4h/semana economizadas não é business case, é descrição de atividade" — CFO Dive 2026; Workday: ~40% das horas 'ganhas' são gastas corrigindo a IA). Horas só viram dinheiro quando viram vaga cancelada, hora extra zerada ou custo unitário caindo.

**Regra ABBA**: prometer só Nível 1 e 2. Horas entram como bônus, em linha separada, rotulada.

### 2.2 Os 5 mecanismos de prova que funcionam

1. **Baseline contratual assinado ANTES** (o "MASC" da HighRadius): métrica, valor medido, fórmula, janela, variáveis de ajuste, executivo nomeado do cliente que assina o atingimento. Baseline definido depois é justificativa, não prova (savings sem baseline prévio são superestimados em 30–50%).
2. **Ancorar em métrica de caixa que o CFO já usa**: DSO, custo/nota, % touchless, % recuperado — nunca "produtividade".
3. **Achar dinheiro do PASSADO primeiro**: diagnóstico sobre dados históricos → "encontramos R$ X que já são seus" vence "vamos economizar R$ Y". O passado é auditável; a projeção, não. (Modelo PRGX: 20–35% do recuperado, zero se não recupera.)
4. **Medição & verificação por protocolo** (padrão IPMVP das ESCOs): janela definida, ajuste por volume/inflação, contrafactual onde couber (carteira piloto vs. controle), e **quem valida é o financeiro do cliente**, não o vendor.
5. **Dashboard "R$ economizado até hoje"** que reconcilia com o razão — o ROI vira interface; renovação se vende sozinha.

### 2.3 Modelos comerciais (faixas reais)

| Modelo | Faixa | Quando |
|---|---|---|
| Êxito puro | Recuperação tributária BR: 10–30%; recovery audit: 20–35%; cobrança BR: 10–20% escalonado pelo atraso | Dinheiro do passado, auditável |
| **Fixo + êxito (recomendado ABBA)** | Fixo cobre operação + 10–20% da economia verificada, com teto e prazo | Projetos com implementação + resultado incerto no timing |
| Gain-share futuro | ~15–20% da economia por 12–36 meses, baseline contratual | Custo recorrente (compras, telecom) |
| Outcome-based (HighRadius 2026) | $0 setup + $0 assinatura até go-live; % do saving | Quando há base estatística própria |
| Piloto pago com baseline | 60–90 dias, baseline na semana 1, preço do rollout já tabelado | Cliente cético, 1ª vez |

**Brasil**: o script cultural do êxito JÁ existe (recuperação tributária, cobrança, ESCOs) — o CFO conhece e aceita. **O gargalo não é o modelo, é a credibilidade da medição.** ~79% das decisões passam pelo CFO; ciclo 45–90 dias; ticket de conforto R$ 30–150k por fase com prova em 60–90 dias.

### 2.4 Anti-padrões (a munição do cético)

- MIT 2025: **95% dos pilotos de GenAI sem impacto mensurável no P&L** — todo CFO cita isso. (E é o pitch do nosso Resgate de IA.)
- 84% dos CFOs não viram retorno de IA em finanças (Deloitte); só 29% conseguem medir ROI com confiança (IBM). **O gap percepção→medição é exatamente o espaço da consultoria que prova.**
- Deloitte: retorno típico leva 2–4 anos vs. expectativa de 7–12 meses. Prometer payback de 6 meses sem base = desmoralização.
- Por que claims morrem na auditoria: baseline a posteriori; horas sem realocação real; misturar cost avoidance com hard saving; ignorar volume/inflação; vendor medindo o próprio resultado; não descontar custo total.

---

## 3. O mercado brasileiro — dores e janela

### 3.1 As dores com número

- **Inadimplência PJ recorde**: 8,9 mi de CNPJs negativados, R$ 213 bi (Serasa dez/2025); recuperação B2B despenca após 20 dias de atraso.
- **Custo tributário pior do mundo**: 1.483–1.501 h/ano por empresa só para apurar e pagar (Banco Mundial); 95% pagam errado; Custo Brasil = R$ 1,7 tri/ano (MBC/MDIC 2025).
- **Fechamento lento**: 10–15 dias úteis no mid-market vs. ≤5 nos maduros.
- **Visibilidade de caixa precária**: fragmentação de sistemas é o entrave nº 1 (Grant Thornton 2025).
- **Fraude**: R$ 25,5 bi perdidos no Pix em 12 meses; 1,87 mi tentativas/tri.

### 3.2 A reforma tributária é a janela de urgência (2026–2033)

- 2026 = ano-teste (CBS 0,9% + IBS 0,1%, campos novos na NF-e); 2027 = CBS integral, PIS/Cofins extintos; 2029–2032 = **dois sistemas tributários em paralelo por 4 anos**; 2033 = modelo pleno.
- **Split payment**: o imposto será retido na liquidação — o bruto que hoje financia 30–60 dias de capital de giro **desaparece**; conciliação e projeção de caixa mudam de natureza.
- **72% das médias/grandes não estão prontas** (CRCSP); só 9,5% se dizem prontas; 47,9% têm processos fiscais pouco estruturados. Big 4 pega as grandes; o contador não dá conta do mid-market. **É deadline regulatória, não discricionária — o CFO não pode adiar.**
- Urgência adicional: inventário de créditos do sistema antigo até 31/12/2026.

### 3.3 Mapa competitivo (5 clusters e o gap de cada um)

| Cluster | Players | O que NÃO fazem (o gap) |
|---|---|---|
| ERPs com IA | TOTVS, Sankhya, Omie, Conta Azul | A IA só enxerga o próprio ERP; não orquestram banco+adquirente+planilhas; automatizam o processo ruim existente |
| Tesouraria/caixa | F360, Kamino, Celero, Dattos | Verticais/funcionais; não transformam visibilidade em decisão (pricing, política de prazo, giro) |
| Cobrança digital | Monest, Global, Acordo Certo | Atuam DEPOIS do estouro; não fazem prevenção (crédito na venda, régua preventiva, política comercial) |
| Taxtechs | Tributo Justo, Revizia, Tax Group | Caça ao tesouro pontual e retroativa; não corrigem o processo que gera o erro nem preparam para IBS/CBS |
| BPO financeiro | mercado de R$ 26,8 bi (+11,7% a.a.) | Executam com gente, sem engenharia; substituem o time em vez de elevá-lo |

### 3.4 Os 5 whitespaces de consultoria (sem competir com SaaS)

- **W1 — Orquestrador do stack financeiro**: ligar ERP↔bancos↔fiscal↔BI com agentes + redesenho de processo. Cada stack é único = serviço por natureza.
- **W2 — Prontidão IBS/CBS + split payment para mid-market**: diagnóstico de impacto → adequação de ERP/cadastros → simulação de caixa → automação da apuração dual. Urgência embutida; nenhum SaaS faz o redesenho, todos precisam dele.
- **W3 — Order-to-cash preventivo**: score de crédito próprio + régua preventiva ERP/CRM/WhatsApp + política comercial. ROI imediato, cobrável parte em êxito.
- **W4 — Fechamento "5 dias" com IA**: agentes de conciliação/classificação sobre o ERP existente (sem trocar de sistema) + antifraude de favorecidos/Pix.
- **W5 — FP&A as a service para empresa de dono**: forecast por driver, cenários de preço/margem sob IBS/CBS, relatório de gestão automatizado. Receita recorrente.

---

## 4. Síntese: a Porta Financeira da ABBA (proposta candidata — pauta de sócios)

### 4.1 O insight central

A pesquisa das 3 frentes converge num único desenho: **entrar pelo dinheiro do passado, ficar pela prova contínua.**

**"Caça ao Dinheiro"** (nome de trabalho) — variante financeira da Avaliação de Prontidão:

1. **Diagnóstico (2–3 semanas, preço fixo)** sobre dados que a empresa é obrigada a ter (XML/SPED/ERP/extratos/adquirentes/aging de títulos): duplicatas pagas, taxas de adquirente cobradas a maior, tributo pago a maior (com parceiro taxtech ou tese simples), carteira de inadimplência recuperável, giro preso em DSO. Entregável: **"Encontramos R$ X"** — mapa de vazamentos com base legal/documental, priorizado.
2. **Builds de estancamento (fixo + êxito 10–20% verificado)**: cobrança preventiva com IA, conciliação+conferência de taxas, automação de AP com trava de duplicidade, forecast de caixa — cada build ancorado num vazamento do diagnóstico, com **baseline assinado antes** (modelo MASC).
3. **Prova contínua (recorrência)**: ritual mensal de "savings sign-off" com o financeiro do cliente validando o número + dashboard "R$ economizado até hoje" que reconcilia com o razão. **Quem apresenta o número ao conselho é o CFO — como número dele.**

### 4.2 Por que a ABBA já tem a máquina (ninguém no mercado tem as 3 juntas)

| Peça necessária (pesquisa) | O que já existe no assessment-brain |
|---|---|
| Achar o dinheiro (diagnóstico) | Dimensão 25 do framework é literalmente "onde o dinheiro vaza e como provar ROI antes/durante/depois"; `financial_leaks` com custo anual + fator de sobreposição; um build por vazamento (solution-mapper) |
| Número que sobrevive a auditor | **`roi-reconcile.js`**: top-down × bottom-up com trava de divergência — número inflado nunca chega ao cliente sem flag. É exatamente a "credibilidade da medição" que a pesquisa aponta como O gargalo do mercado brasileiro |
| Medição & verificação contínua | **O Conselheiro é o motor de M&V**: `decisions` → `decision_outcomes` com `baseline_value`, `measured_value`, `verdict` e gate humano nomeado — o ledger de savings verificados já está construído. O brief mensal é o relatório de verificação |

Ou seja: taxtech acha dinheiro mas não corrige processo; SaaS corrige função mas não prova no razão; BPO executa mas não mede. **A ABBA pode ser a única que acha → estanca → prova, com o Conselheiro como órgão de prova.** E cada engajamento alimenta o cérebro (episódios + facts de vazamento por setor → padrões anonimizados no vault).

### 4.3 Encaixe nas regras vigentes (nada quebra)

- **Mesma espinha**: 25 dimensões → build → run → advise → brain. A Caça ao Dinheiro é um FRAME da Avaliação (como o Resgate é o frame "por que falhou"), não um produto novo de engenharia.
- **Máx. 3 portas visíveis**: candidatas a vitrine — Avaliação | Resgate | Caça ao Dinheiro (a definir pelos sócios; o estudo de mercado já apontava a "porta do CFO corte-de-custos" como situação de comprador nº 2).
- **Recorrência como centro**: o savings sign-off mensal É a manutenção/Conselheiro re-ancorados em R$.
- **Cuidado E6**: garantia "achamos ≥3× ou devolvemos" continua PORTA DE 1 VIA — êxito por build é reversível e substitui a necessidade dela por ora.
- **Anti-patterns respeitados**: não prometemos payback de 6 meses genérico; não vendemos horas; não viramos taxtech (tributário via parceiro/tese simples — advocacia de êxito exige OAB).

### 4.4 To-dos se aprovada (não executar sem decisão dos sócios)

- [ ] One-pager comercial "Caça ao Dinheiro" em `03-comercial/` (âncoras: R$ 213 bi inadimplência, 95% pagam tributo errado, split payment).
- [ ] Roteiro do diagnóstico financeiro mapeado sobre as dimensões (subconjunto financeiro das 25 + checklist XML/SPED/adquirentes/aging).
- [ ] Modelo de "termo de baseline" (MASC ABBA, 1–2 páginas): métrica, valor, fórmula, janela, ajustes, assinatura nomeada — vira anexo padrão de proposta.
- [ ] Preço na proposta v2 (fixo do diagnóstico + faixas de êxito por família, escalonado pela dificuldade).
- [ ] Avaliar parceiro taxtech (white-label ou indicação com fee) para a tese tributária.
- [ ] Conselheiro: brief mensal ganha seção "R$ verificado no período" (consulta em `decision_outcomes` — só engenharia de relatório, o dado já existe).
- [ ] Prontidão IBS/CBS (W2) como oferta-satélite ou capítulo do diagnóstico — decidir escopo.

---

*Fontes completas nos três relatórios de pesquisa que originaram este estudo (Ardent Partners 2025, HighRadius 2024–26, Serasa 2025–26, Banco Mundial, Deloitte CFO Survey 2025, ACFE 2024, McKinsey, MIT 2025, CRCSP, IBPT, entre outras — links preservados no histórico da sessão).*
