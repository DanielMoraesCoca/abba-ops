# Protótipo Patrimonial — Especificação de Arquitetura e Agentes (CrewAI 1.x)

> **Camada:** interno (engenharia de protótipo). Parte do pacote [prototipo-patrimonial](plano-de-construcao.md). Especificação pronta-para-implementar; o código correspondente está em [`scaffold/`](scaffold/README.md). Baseada na doutrina oficial CrewAI atual (v1.15.x, ago/2026): **Flow-first** — "para produção, comece com um Flow e use Crews como unidades de trabalho" (docs.crewai.com, *Production Architecture*), e na tese do João Moura: *backbone determinístico, inteligência onde importa* — código puro para tudo que é regra; agente só onde há julgamento.
>
> Dono: engenharia. Modelo de LLM por etapa é sugestão inicial — calibrar no eval.

---

## 1. A espinha (um Flow, três Crews, dois gates)

```
Flow[EstadoCaso]  (Pydantic + @persist — SQLite; retomada e trilha auditável)
│
├─ @start  intake()                     [determinístico] questionário → PerfilEstruturado
├─ @listen gate1_red_flags()            [determinístico] tabela de 6 flags duros + brandos
│     └─ @router:  "bloqueado" → relatorio_bloqueio()  [determinístico → advogado]
│                  "liberado"  → crew_analise()
├─ @listen crew_analise()               [Crew A — 3 agentes] fatos jurídicos citados
├─ @listen crew_desenho()               [Crew B — 2 agentes] 2–3 arquiteturas + crítica adversarial
├─ @listen obrigacoes_e_cenarios()      [determinístico] pacote de obrigações + simulação
├─ @human_feedback gate2_advogado()     [HUMANO] aprova | rejeita | revisar (self-loop via or_())
├─ @listen crew_redacao()               [Crew C — 1 agente] minuta ao advogado
└─ @listen render_final()               [determinístico] DOCX/MD + trilha de auditoria + versão do corpus
```

**Por que assim** (decisões amarradas à pesquisa):
- **Flow, não Crew hierárquica**: o caso exige etapas obrigatórias, gates e branching — a matriz oficial "alta complexidade + alta precisão = Flows orquestrando Crews". Processo hierárquico está na lista oficial de erros comuns ("uso prematuro").
- **Gates em código puro**: red flags e obrigações são REGRA, não julgamento. Um agente pode ser convencido; um `if` não.
- **`@persist` + estado tipado**: dados do caso vivem SÓ no estado do Flow (Pydantic) — auditável, retomável, apagável. **Memória CrewAI: OFF** (a nota de privacidade oficial avisa que todo conteúdo memorizado é enviado ao LLM/embedder de análise — inaceitável para dado de cliente por padrão).
- **`@human_feedback` como gate 2**: mecanismo nativo (v1.8+) com outcomes tipados (`emit`), self-loop de revisão (`or_()`), provider assíncrono para produção (e-mail/Slack) e `human_feedback_history` como trilha de auditoria pronta. No protótipo, console; no piloto, provider async. `learn=False` sempre (não gravar correções em memória adaptativa).

## 2. Estado do Flow (`EstadoCaso` — schema completo no scaffold)

`caso_id` · `versao_corpus` · `perfil: PerfilEstruturado` · `red_flags: RedFlagReport` · `analise: AnaliseJuridica` (claims citadas por domínio) · `desenhos: list[DesenhoEstrutura]` (com crítica adversarial anexada) · `obrigacoes: list[PacoteObrigacoes]` (1:1 com desenhos) · `cenarios: list[CenarioProjetado]` · `feedback_advogado: list` · `minuta: MinutaFinal | None` · `chunks_recuperados: list[str]` (IDs — preenchido por event listener; insumo do guardrail).

## 3. As três Crews (processo sequencial, tasks focadas — regra 80/20 dos docs)

### Crew A — Análise (produz FATOS jurídicos citados, não opinião)

| Agente | Role/Goal (essência) | Task | Output |
|---|---|---|---|
| **Analista Tributário BR** | Especialista em Lei 14.754/2023, IN 2.180 e tributação internacional de PF residente. Goal: mapear o enquadramento tributário do perfil, com artigo citado em cada afirmação | "Dado o `PerfilEstruturado`, liste os fatos tributários aplicáveis (regime de controladas, transparência de trust, DCBE, ITCMD por UF do perfil). NÃO proponha estrutura." | `AnaliseTributaria(claims=[ClaimCitada])` |
| **Analista Sucessório** | Especialista em direito de família e sucessões (CC 1.845–1.857, regimes de bens). Goal: mapear a situação sucessória — legítima, parte disponível, exposições por regime de casamento e herdeiros no exterior | "Mapeie a situação sucessória do perfil. Sinalize toda restrição de ordem pública. NÃO proponha estrutura." | `AnaliseSucessoria(claims=[ClaimCitada])` |
| **Analista de Jurisdições** | Especialista em estruturas internacionais e reporte (CRS/FATCA). Goal: para as jurisdições candidatas do corpus, levantar o que o perfil implica em cada uma | "Com base nas fichas de jurisdição do corpus, avalie aderência de cada jurisdição ao perfil. Toda afirmação com `source_id` de ficha." | `AnaliseJurisdicoes(claims=[ClaimCitada])` |

- Cada task: `tools=[rag_corpus]` (a tool devolve chunks com `chunk_id` — proveniência estruturada; motivo de NÃO usar o Knowledge nativo, que não devolve provenance no output) · `output_pydantic` · `guardrails=[valida_schema, anti_citacao_orfa]` (função; retry automático ≤ 3) · `temperature=0` · modelo sugerido: classe Sonnet.
- **Abstenção**: o prompt de cada agente termina com a regra da casa — *"se o corpus não sustenta a afirmação, escreva `nao_coberto` no claim, com o que faltou"*. `nao_coberto` não é falha: vira seção "limites desta análise" da minuta.

### Crew B — Desenho (produz ALTERNATIVAS, cada uma atacada antes de sair)

| Agente | Role/Goal | Task | Output |
|---|---|---|---|
| **Arquiteto de Estruturas** | Planejador patrimonial sênior; goal: desenhar 2–3 arquiteturas ALTERNATIVAS aderentes à análise, todas 100% declaradas e tributadas, com trade-offs explícitos | "Com a `AnaliseJuridica` como contexto, proponha 2–3 desenhos (veículos, jurisdições, sequência de implantação, custo estimado de manutenção). Cada elemento com `source_ids`. Enderece explicitamente cada red flag brando." | `list[DesenhoEstrutura]` |
| **Crítico Adversarial** | Advogado de contraparte/fiscal da Receita em simulação; goal: DERRUBAR cada desenho — desconsideração, fraude, recaracterização, custo oculto, instabilidade legislativa (PLP 108) | "Para cada desenho, produza os 3 ataques mais fortes e classifique: `fatal` (desenho descartado), `mitigavel` (vira condicionante), `menor`. Cite a base do ataque." | `CriticaAdversarial` por desenho |

- Desenho com ataque `fatal` não segue — o Flow (código) descarta e, se restarem <2 desenhos, reexecuta a task do Arquiteto com a crítica no contexto (máx. 2 ciclos).
- Modelo sugerido: classe Sonnet/Opus no Crítico (é o que mais paga inteligência).

### Crew C — Redação (produz a MINUTA, nunca o conselho final)

| Agente | Role/Goal | Task | Output |
|---|---|---|---|
| **Redator Jurídico** | Redator técnico de pareceres; goal: consolidar análise + desenhos sobreviventes + obrigações + cenários + feedback do advogado numa minuta clara, com todas as fontes citadas e os limites declarados | "Redija a minuta em pt-BR para revisão do advogado responsável. Estrutura fixa: sumário executivo · perfil · red flags e condicionantes · alternativas com trade-offs · pacote de obrigações · cenários · limites da análise · fontes." | `MinutaFinal` |

- Guardrails: schema + anti-citação-órfã + presença obrigatória das seções "limites" e do rodapé fixo: *"Minuta gerada por sistema de apoio; não constitui parecer jurídico. Revisão e assinatura: [advogado nomeado, OAB]."*

## 4. Guardrails (funções — determinísticos; código no scaffold)

1. **`valida_schema`** — `output_pydantic` já valida; a função confere regras extras (mín. de claims, campos não vazios).
2. **`anti_citacao_orfa`** — todo `source_id` citado ∈ `estado.chunks_recuperados` (preenchido por event listener de retrieval). Citação inventada → `(False, "source_id X não foi recuperado; refaça citando apenas chunks fornecidos")` → retry automático.
3. **`sem_linguagem_de_ocultacao`** — lista de padrões proibidos no output (ex.: "sem aparecer", "fora do radar", "não declarar", "em nome de terceiro") → bloqueia e reorienta. Complemento Enterprise opcional: `HallucinationGuardrail` (faithfulness) como 2ª camada.
4. **Hook `@before_llm_call`** — redação de PII direta (CPF, RG) antes de qualquer chamada ao provedor; o caso trafega com pseudônimo (`caso_id`).

## 5. Etapas determinísticas (código, nunca agente)

- **`gate1_red_flags`**: a tabela do [questionário](questionario-perfil.md) implementada em `gates.py`. Duro → rota "bloqueado" com relatório do porquê + próximo passo humano. Brando → segue anotado (o Arquiteto é obrigado a endereçar).
- **`obrigacoes_e_cenarios`**: por desenho, gera o checklist de obrigações (IRPF/regime 14.754, DCBE anual/trimestral, balanço de controlada, ITCMD da UF, prazos) por REGRAS — e projeta cenários (custo tributário e sucessório em 5/10 anos) com aritmética simples e premissas declaradas. É o diferencial pós-2024 e é 100% verificável — por isso não é LLM.
- **`render_final`**: markdown → DOCX (padrão visual ABBA), anexando trilha: versão do corpus, chunks usados, histórico de feedback humano, timestamps.

## 6. Observabilidade, custo e operação

- Tracing AMP ligado desde o dia 1 (`tracing=True`); custo por análise via `flow.usage_metrics` (agrega todas as crews — não usar o token_usage da última crew).
- Teto de gasto por caso (guarda no Flow: aborta com estado persistido se estourar) — mesmo princípio do `--max-usd` da casa.
- `CREWAI_STORAGE_DIR` fixo do projeto; embedder explícito.
- Avaliação: asserts determinísticos + `ExperimentRunner` (experimental) — detalhe em [avaliacao-e-metrica.md](avaliacao-e-metrica.md).

## 7. O que fica explicitamente FORA do protótipo

Execução de abertura de estruturas · aconselhamento direto ao cliente final · qualquer funcionalidade de ocultação/anonimato · memória adaptativa entre casos · fine-tuning · integrações bancárias. (Fase 2, se GO: provider async de HITL, DOCX timbrado, multi-caso, fichas de jurisdição expandidas.)

## Ligações

[Plano de construção](plano-de-construcao.md) · [Questionário](questionario-perfil.md) · [Corpus](corpus-conhecimento.md) · [Avaliação](avaliacao-e-metrica.md) · [Scaffold](scaffold/README.md)
