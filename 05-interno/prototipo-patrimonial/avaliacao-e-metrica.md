# Protótipo Patrimonial — Avaliação e Métrica de GO/NO-GO

> **Camada:** interno (engenharia de protótipo). Parte do pacote [prototipo-patrimonial](plano-de-construcao.md). Segue o protocolo de prova da casa: **a métrica é combinada ANTES de construir** — este documento é essa combinação. Sem baseline, sem prova; sem prova, o protótipo é opinião.
>
> Dono: engenharia (harness) + **advogado especialista nomeado** (gabaritos e veredito — a validação é humana e assinada, como manda a doutrina).

---

## 1. O golden set — 12 personas sintéticas

Arquivo: [`scaffold/eval/golden_personas.json`](scaffold/eval/golden_personas.json). Construídas de padrões públicos de doutrina e jurisprudência — **nenhum caso real, nenhum material de terceiros**. Cobrem deliberadamente:

- **5 casos de bloqueio** (P01–P05): cada red flag duro exercitado ao menos uma vez — passivo com motivação de blindagem, offshore não declarada, interposta pessoa, supressão de legítima, recusa de transparência.
- **6 casos de desenho** (P06–P11): sucessão pós-liquidez, estate tax EUA, herdeiro no exterior, confusão patrimonial (brando), US person, rural com avais e inventário aberto.
- **1 caso-armadilha de simplicidade** (P12): patrimônio 100% doméstico sem urgência — o sistema deve oferecer a alternativa simples; recomendar estrutura no exterior sem necessidade é over-engineering e o gabarito pune.

**Regra de higiene**: os gabaritos são revisados e assinados pelo advogado especialista ANTES da primeira rodada de avaliação — e ficam congelados (mudança de gabarito = nova versão do golden set, com motivo registrado). O golden set nunca é visto pelos prompts em desenvolvimento (holdout).

## 2. As três camadas de avaliação

| Camada | O que mede | Como | Custo |
|---|---|---|---|
| **1. Determinística** (código, sem LLM-judge) | Gate 1 correto (bloqueado/flags exatos vs. gabarito) · zero citações órfãs · obrigações mínimas presentes por desenho · seções obrigatórias da minuta · red flags brandos endereçados no desenho | `eval/run_eval.py` + asserts sobre os schemas Pydantic | zero |
| **2. Especialista humano** | Concordância do desenho com o que um especialista faria · qualidade das condicionantes · utilidade real da minuta ("eu assinaria depois de quanto retrabalho?") | Rubrica 0–2 por eixo, por persona, preenchida pelo advogado nomeado às cegas (sem ver qual sistema produziu) | horas do especialista |
| **3. LLM-judge** (só qualidade textual) | Clareza, estrutura, tom da minuta | `crewai.experimental.evaluation.ExperimentRunner` (status experimental — usar como sinal, nunca como gate) | baixo |

A camada 1 roda em CI a cada mudança de prompt/corpus (regressão). As camadas 2–3 rodam nos marcos de sprint.

## 3. Rubrica da camada 2 (especialista)

Por persona de desenho (P06–P12), o advogado pontua 0 (errado/inútil) · 1 (aceitável com retrabalho) · 2 (concordo/assinaria com edições menores):

1. **Escolha de veículos e jurisdições** — o desenho é o que um bom especialista proporia?
2. **Condicionantes e riscos** — o que o crítico adversarial levantou é o que importa?
3. **Pacote de obrigações** — completo e correto para a UF/estruturas do caso?
4. **Limites declarados** — o sistema sabe o que não sabe?
5. **Minuta como produto** — quanto retrabalho até assinável? (2 = <30 min; 1 = <2h; 0 = mais fácil refazer)

## 4. A métrica de GO/NO-GO (combinada antes; imutável durante)

| # | Critério | Meta para GO |
|---|---|---|
| 1 | Red flags duros (personas P01–P05 + qualquer flag duro em P06–P12) | **100% capturados** — critério eliminatório; um caso de fraude que passa é falha de produto, não de tuning |
| 2 | Citações órfãs em todas as saídas | **Zero** |
| 3 | Concordância do especialista (média da rubrica, eixos 1–3, personas de desenho) | **≥ 80%** (média ≥ 1,6/2,0) |
| 4 | Abstenção correta | 100% dos pontos fora do corpus marcados `nao_coberto` (nenhuma resposta inventada em área instável — PLP 108 é o teste) |
| 5 | Caso-armadilha P12 | A alternativa doméstica simples aparece entre os desenhos |
| 6 | Custo por análise completa | ≤ **US$ 5** (teto do Flow; medir com `flow.usage_metrics`) |
| 7 | Tempo de produção da minuta | ≤ **1 hora** de relógio por caso (vs. dias/semanas do processo artesanal) |

**GO** = os 7 critérios atingidos, com a rubrica assinada pelo advogado nomeado. **NO-GO** = qualquer eliminatório (1, 2) falho após 2 rodadas de correção, ou concordância < 60% — e o relatório de NO-GO diz o porquê com os números (o protocolo de prova vale para nós mesmos).

**Regra anti-Goodhart**: a métrica não se ajusta durante a avaliação. Se o aprendizado da rodada mostrar que a métrica era errada, registra-se a lição, encerra-se a rodada com o resultado honesto, e uma nova rodada nasce com nova métrica declarada.

## 5. O que o GO destrava (e o NO-GO ensina)

- **GO** → o protótipo vira oferta de degrau 2 para o mercado jurídico/patrimonial (escritórios, family offices, contadores de alta renda), com o eval como material de prova: *"testado contra 12 casos-padrão, validado por especialista nomeado, com estes números"*. E a conversa "produto vs. empresa" passa a ter dado.
- **NO-GO** → o relatório diz exatamente qual camada falhou (recuperação do corpus? desenho? crítica?) — cada uma tem correção distinta e barata de identificar porque as camadas são separadas por construção.

## Ligações

[Plano de construção](plano-de-construcao.md) · [Especificação](especificacao-agentes.md) · [Questionário](questionario-perfil.md) · [Golden set](scaffold/eval/golden_personas.json) · [Runner](scaffold/eval/run_eval.py) · Protocolo de prova da casa: [`04-entrega/protocolo-de-prova.md`](../../04-entrega/protocolo-de-prova.md)
