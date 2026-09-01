# Blueprint de Engenharia — Biblioteca de Crews da Camada de Caixa

> **Camada:** ferramentas (spec). É o desenho técnico do que o [plano da Camada de Caixa](../05-interno/plano-camada-de-caixa-2027.md) decidiu construir. Mesmo formato da [spec do assessment web](spec-alinhamento-assessment-web.md): especificação para engenharia, não backlog deste repositório.
>
> **Status:** spec **candidata — não construir antes do gate do Mês 2** (executor dedicado definido) e da resposta a **C2** (superfície de integração da apuração assistida). Dono: chapéu [Tecnologia](../01-setores/tecnologia.md).
>
> **Nota de versão:** a API da CrewAI muda rápido. Todo trecho de código aqui é **desenho, não cópia** — confirmar contra a documentação da versão fixada no `pyproject.toml` antes de implementar.

---

## 1. O princípio que governa todo o resto

> **Determinístico onde há dinheiro e prazo. Agêntico só onde há julgamento.**

Este produto conta dinheiro e cumpre prazo legal. Um LLM que soma errado é um passivo, não um recurso. A evidência interna é explícita: o MAST ([estudo de antecipação](../05-interno/estudo-antecipacao.md) §4) mede que **41,8% das falhas multiagente são de especificação/desenho e 36,9% de coordenação** — *"robustez exige melhor orquestração, não modelos maiores"*. Portanto:

| Camada | Implementação | Por quê |
|---|---|---|
| **Orquestração, prazo, estado** | **CrewAI Flow** (`@start`, `@listen`, `@router`, estado tipado, `@persist`) | Determinístico, reexecutável, auditável. É o esqueleto |
| **Aritmética fiscal e de caixa** | **Python puro, em ferramenta, com teste unitário** | Nenhum número nasce em LLM. Nunca |
| **Extração de documento estruturado** (XML de NF-e, SPED) | **Parser determinístico** | XML é estruturado. Usar LLM aqui é queimar dinheiro e introduzir erro |
| **Classificação ambígua, leitura de exceção, redação** | **Crew de agentes** | É onde julgamento existe e onde o LLM ganha |
| **Decisão de agir** | **Humano nomeado** | Inegociável 1. A crew rascunha; o contador assina |

**Consequência de custo, que é o que torna o produto viável em escala:** num escritório com 300 CNPJs, a Sentinela roda 300 vezes por mês. Se cada execução mandasse todos os documentos para um LLM, o produto não fecharia conta. No desenho acima, **a maioria das execuções não chama LLM nenhum** — o cruzamento determinístico resolve, e o modelo só entra nas divergências que sobraram. Ver §9.

---

## 2. Estrutura do projeto

Repositório novo, Python. Não mora no `assessment-brain` (que é Node/CLI de avaliação) nem no `abba-portal` (Next.js). Nome de trabalho: `abba-crews`.

```
abba-crews/
├── pyproject.toml                 # crewai pinado em versão exata
├── src/abba_crews/
│   ├── flows/
│   │   ├── sentinela_flow.py      # o esqueleto mensal (Flow)
│   │   ├── diagnostico_flow.py
│   │   └── rad_flow.py
│   ├── crews/
│   │   ├── sentinela/
│   │   │   ├── config/agents.yaml
│   │   │   ├── config/tasks.yaml
│   │   │   └── crew.py            # @CrewBase
│   │   ├── aceleracao_credito/
│   │   ├── rad/
│   │   └── diagnostico/
│   ├── tools/                     # ferramentas determinísticas, testadas
│   │   ├── nfe_reader.py
│   │   ├── apuracao_parser.py
│   │   ├── reconciliador.py       # o coração — Python puro
│   │   ├── simulador_caixa.py
│   │   ├── calendario_fiscal.py
│   │   └── ledger_abba.py         # ponte para o assessment-brain
│   ├── models/                    # Pydantic: TODO output é tipado
│   ├── knowledge/                 # base consultável, versionada
│   └── config/clientes/           # UM YAML por cliente. É o "ajuste"
└── tests/
    ├── unit/                      # aritmética: cobertura alta, obrigatória
    └── golden/                    # o conjunto de avaliação (§10)
```

**A biblioteca é de prateleira; o que muda por cliente é `config/clientes/<cnpj>.yaml`** — regime, perfil de operação, plano de contas, tolerâncias, quem aprova, quem recebe. É isso que responde ao pedido do sócio: *"o esqueleto pronto, a gente faz os ajustes"*.

---

## 3. Crew 1 — Sentinela da Apuração (a primeira a construir)

**Missão:** entre o dia em que a apuração pré-preenchida fica **disponível** (dia 15, ou 20 para quem entrega DeRE) e o **último dia útil do mês seguinte** — que é o prazo real de manifestação —, garantir que **nenhum crédito legítimo da empresa seja perdido pelo silêncio**.

### 3.1 O Flow (o esqueleto determinístico)

```python
class EstadoSentinela(BaseModel):
    cnpj: str
    competencia: str                  # "2027-03"
    prazo_limite: date                # calculado, não digitado
    apuracao_fisco: ApuracaoFisco | None = None
    documentos_empresa: list[DocumentoFiscal] = []
    divergencias: list[Divergencia] = []
    dossie_id: str | None = None
    aprovado_por: str | None = None

class SentinelaFlow(Flow[EstadoSentinela]):

    @start()
    def abrir_competencia(self):
        # calendario_fiscal: calcula o prazo real e quantos dias restam.
        # Se restam < N dias, o estado nasce marcado como urgente.

    @listen(abrir_competencia)
    def coletar(self):
        # apuracao_parser + nfe_reader. Zero LLM.

    @listen(coletar)
    def reconciliar(self):
        # reconciliador.py — Python puro. Produz divergências
        # já classificadas nos tipos conhecidos e quantificadas em R$.

    @router(reconciliar)
    def decidir_rota(self):
        if not self.state.divergencias:
            return "sem_divergencia"          # encerra: registra e avisa. Sem LLM.
        if todas_de_tipo_conhecido(self.state.divergencias):
            return "rotina"                   # dossiê por template. Sem LLM.
        return "julgamento"                   # aqui, e só aqui, a crew entra.

    @listen("julgamento")
    def analisar(self):
        # SentinelaCrew().kickoff(inputs=...) — os 4 agentes do §3.2

    @listen(or_("rotina", "analisar"))
    def submeter_a_humano(self):
        # Grava dossiê PENDENTE_APROVACAO no ledger. NÃO transmite.
        # NÃO conclui. O turno acaba aqui.
```

**Três propriedades desse desenho, e cada uma é uma regra da casa:**

1. **O Flow nunca transmite nada ao Fisco.** Não existe ferramenta de transmissão no projeto. A confirmação da apuração é ato do contribuinte ([plano](../05-interno/plano-camada-de-caixa-2027.md) §6).
2. **O turno termina em aprovação pendente**, nunca em "feito". Inegociável 1 — a saída nasce rascunho.
3. **O caminho feliz é barato.** Sem divergência ou só divergência conhecida = nenhum token gasto.

### 3.2 Os agentes (só na rota de julgamento)

| Agente | `role` / `goal` | Ferramentas | Saída tipada |
|---|---|---|---|
| **`conferente`** | Confrontar a apuração do Fisco contra os documentos da empresa e **nomear** cada divergência: o que difere, em qual documento, em quanto | `nfe_reader`, `apuracao_parser`, `reconciliador` | `list[Divergencia]` |
| **`caçador_de_credito`** | Achar crédito presente nos documentos da empresa e **ausente** da proposta do Fisco — e apontar o documento que o comprova | `nfe_reader`, `classificador_creditabilidade`, base de conhecimento | `list[CreditoOmitido]` |
| **`cetico`** | Tentar **derrubar** cada achado do caçador: existe hipótese de vedação, uso e consumo pessoal, documento inidôneo, competência errada? | base de conhecimento, `reconciliador` | `list[Veredito]` |
| **`redator_do_dossie`** | Montar o dossiê de manifestação em linguagem de contador, com evidência apontada item a item e o R$ em risco no topo | — | `DossieManifestacao` |

**O agente `cetico` não é enfeite.** É a resposta de desenho ao risco **C5** (a crew "acha" crédito que não existe). Um achado que não sobrevive à contestação **não entra no dossiê** — sai numa lista separada, "descartados e por quê", que é o que dá ao contador confiança para assinar o resto.

**Todos os agentes com `allow_delegation=False`.** Delegação livre é a origem das falhas de coordenação do MAST. A coordenação mora no Flow, não na conversa entre agentes.

### 3.3 Guardrails (validação de tarefa, antes de seguir adiante)

Cada `Task` carrega um `guardrail` — função determinística que devolve `(ok, valor|erro)` e faz a tarefa repetir se falhar:

| Guardrail | O que trava |
|---|---|
| `toda_divergencia_tem_documento` | Achado sem chave de documento fiscal apontada **não passa**. Sem exceção |
| `soma_confere` | O total do dossiê tem de bater com a soma dos itens. Aritmética conferida em código |
| `sem_valor_inventado` | Todo valor em R$ do dossiê tem de existir num documento coletado. Comparação literal |
| `dentro_do_prazo` | Se o prazo já passou, o dossiê muda de natureza (vira registro de perda) e o texto muda junto |
| `sem_conclusao_juridica` | Bloqueia linguagem de parecer ("é devido", "faz jus a") no texto. A crew evidencia; quem conclui é o contador (§6 do plano) |

### 3.4 Aprovação humana — por que não `human_input=True`

A CrewAI oferece `human_input=True` na task, que pausa e pede confirmação **no console**. Isso serve para desenvolvimento e não serve para produção: o contador não vive num terminal, e o prazo é de dias, não de segundos.

**Desenho correto:** o Flow grava o dossiê como `PENDENTE_APROVACAO` no ledger e **encerra**. O contador aprova, edita ou rejeita **no portal**, no tempo dele. A aprovação registra **nome, horário e o que foi alterado**. Um segundo Flow, disparado pela aprovação, produz o pacote final.

Isso não é preciosismo: é o mesmo gate de humano nomeado que o [protocolo de prova](../04-entrega/protocolo-de-prova.md) já exige, e é o que torna o registro defensável depois.

---

## 4. As outras quatro crews (spec resumida)

Construir só depois que a Sentinela tiver um mês real rodando.

### Crew 2 — Diagnóstico de Impacto de Caixa
Roda **uma vez** por cliente; é a porta comercial.
- **Núcleo determinístico:** `simulador_caixa` projeta, mês a mês, o líquido em conta sob três cenários — **sem RAD** · **com RAD** · **com split payment** (cenário marcado como *hipotético, sem data*).
- **Agentes:** `perfilador` (classifica o perfil de operação a partir do histórico de NF-e: prazo médio, mix de crédito, concentração de fornecedores) → `narrador` (escreve a comparação em linguagem de diretoria).
- **Regra de honestidade, herdada do [Mapa de Vazamento](../03-comercial/mapa-de-vazamento.md):** o resultado sai como **faixa, nunca ponto**, com as premissas numeradas e a fonte citada. Número exato calculado por fora é mentira com aparência de precisão.

### Crew 3 — Aceleração de Crédito
- `rastreador` (quais notas de entrada esperadas não chegaram ou não foram escrituradas — cruzando pedidos, pagamentos e documentos recebidos) → `classificador` (creditável? com que vedação?) → `priorizador` (determinístico: ordena por R$ × dias até o prazo) → `redator_de_cobranca` (rascunha o e-mail ao fornecedor; **quem envia é gente**).
- **Métrica:** dias entre emissão e escrituração, e crédito que entrou na competência certa. **Não** "retenção evitada" — ver [plano](../05-interno/plano-camada-de-caixa-2027.md) §8.

### Crew 4 — Conselho de Adesão ao RAD
- Roda **por contraparte**, com `kickoff_for_each`.
- `analista_de_contraparte` (volume, prazo, histórico) → `simulador_rad` (determinístico: efeito de caixa dos dois lados) → `redator_da_recomendacao`.
- **Saída obrigatória:** recomendação **com probabilidade declarada** e métrica de revisão — que entra no diário de decisões do Conselheiro como `decision` com `predicted_probability` e gatilho armado. É a única crew que já nasce alimentando o placar de calibração.

### Crew 5 — Conciliação Nota × Pagamento
Só depois de base instalada. Exige integração com o meio de pagamento; até lá, lote diário sobre extrato exportado.

---

## 5. Catálogo de ferramentas

Toda ferramenta é `BaseTool` com `args_schema` Pydantic, `_run()` determinístico e teste unitário. **Nenhuma faz chamada de rede sem timeout e sem registro.**

| Ferramenta | Entrada | Saída | Nota |
|---|---|---|---|
| `nfe_reader` | XML de NF-e/NFC-e/CT-e | `DocumentoFiscal` tipado | Parser, não LLM. Cobrir os campos de IBS/CBS obrigatórios desde 03/08/2026 |
| `apuracao_parser` | Apuração pré-preenchida | `ApuracaoFisco` | **Depende de C2.** Enquanto não houver API, entrada é arquivo exportado pelo contador |
| `reconciliador` | Documentos + apuração | `list[Divergencia]` | **O coração.** Python puro, cobertura alta, casos negativos no teste |
| `classificador_creditabilidade` | Item de documento | creditável / vedado / duvidoso + razão | Regra primeiro; LLM só no "duvidoso" |
| `simulador_caixa` | Perfil + cenário | Série mensal | Determinístico. Nenhum LLM toca a série |
| `calendario_fiscal` | Competência + perfil | Prazos e dias restantes | Fonte única dos prazos. Nunca data em prompt |
| `ledger_abba` | Fato, decisão, desfecho | Registro no `assessment-brain` | Ponte para o cérebro. Ver §6 |

**Base de conhecimento** (`knowledge/`), versionada em git e citável: LC 214/2025 (arts. 27, 47, 48 e o capítulo de creditamento), Decreto 12.955/2026, Resolução CGIBS 6/2026, tabelas de classificação, e o **caderno de exceções por cliente** que sai da descoberta. Regra: **todo item da base tem fonte e data**; item sem fonte não entra — a mesma regra da [base de evidências](../00-identidade/base-de-evidencias.md).

---

## 6. Integração com o que a ABBA já construiu

Esta é a diferença entre "mais uma ferramenta fiscal" e um produto ABBA.

| Ativo existente | Como entra |
|---|---|
| **Diário de decisões** (`decisions` → `decision_outcomes`, gate de humano nomeado) | Cada manifestação de apuração e cada adesão ao RAD é uma **decisão registrada** com métrica, baseline e prazo. O desfecho é medido e recebe veredito. É daí que sai a prova, e é daí que sai a cobrança variável |
| **Fatos bitemporais com autoridade de origem** | O que o contador confirma nasce `human_stated` e **não pode ser rebaixado** por inferência de LLM depois. É exatamente a trava que um produto fiscal precisa |
| **`roi-reconcile`** (top-down × bottom-up com trava de divergência) | O R$ recuperado do mês passa por ele antes de virar número de cobrança. Número inflado não chega ao cliente |
| **`abba forget`** | Único caminho de deleção. Dado fiscal entra no ciclo de vida declarado desde o primeiro dia |
| **`abba brain next`** | O prazo de manifestação de cada CNPJ (último dia útil do mês seguinte) entra na fila de antecipação, com a disponibilização do dia 15/20 como marco de início. O ritual da manhã já existe |
| **`crewai-export.js`** (`abba.crewai-export/v1`) | **Continua servindo o caminho sob medida** — o assessment gera crews por cliente. Esta biblioteca é o caminho de prateleira. **Os dois convivem**; não substituir um pelo outro |

### A doutrina de memória — e é uma decisão, não um detalhe

A CrewAI tem memória própria (curta, longa, entidades). **Desligar a memória de longo prazo da CrewAI.**

Razão: o sistema de registro da ABBA é o cérebro do `assessment-brain` — bitemporal, com supersessão que nunca deleta, autoridade de origem e cobertura pelo `abba forget`. Duas memórias concorrentes significam duas verdades, e a que a CrewAI guarda **não** é auditável nem apagável pelo caminho sancionado — o que quebra os inegociáveis 2 e 3 de uma vez. A memória de curto prazo dentro de uma execução pode ficar; o que atravessa execuções passa pelo `ledger_abba`.

---

## 7. Modelos e roteamento

| Etapa | Modelo | Razão |
|---|---|---|
| Extração e classificação de rotina | **Nenhum** (código) | XML é estruturado |
| Classificação do "duvidoso" | Modelo pequeno e barato | Volume alto, tarefa estreita, saída tipada |
| Ceticismo e síntese do dossiê | Modelo forte | É onde o julgamento vive e onde errar custa caro |
| Redação para o cliente | Modelo forte | Rascunho que um humano vai assinar |

Roteamento por agente (`llm=` no `Agent`), com **teto de custo por execução** e por cliente/mês — a mesma disciplina do `abba brain sleep` (`--max-usd`). Teto estourado **interrompe e avisa**; nunca degrada em silêncio.

**Ambiente:** o cliente escolhe, como em toda construção ABBA — nuvem gerenciada ou on-premise. Para dado fiscal, esperar que uma parte dos clientes exija `sa-east-1` ou dentro de casa. A biblioteca não pode assumir nuvem.

---

## 8. A questão CrewAI Enterprise — e o que fazer hoje

O [risco R9](../05-interno/registro-de-riscos.md) está aberto: conta e infraestrutura não contratadas, via indefinida, e o e-mail de contato (`abba-portal/materials/abba-crewai-outreach-and-runbook-v1.md`) nunca foi enviado. **Não existe parceria formal com a CrewAI** — existe escolha de stack (regra P8, 2026-07-23).

**Recomendação:** construir sobre **CrewAI open-source, auto-hospedado**. Não exige contrato, não bloqueia o cronograma, e é a via que preserva on-premise. Enterprise/AMP Factory volta à mesa como **decisão de operação** quando houver clientes pagantes e volume medido — aí a conversa com eles tem número, que é uma conversa melhor.

**Ação de 30 dias:** enviar o e-mail que já está escrito e registrar a resposta. Não para destravar este produto — para fechar R9.

---

## 9. Custo — a conta que decide a viabilidade

Modelo de referência, a **medir no protótipo** (todo número abaixo é hipótese a validar, não promessa):

```
Execução mensal por CNPJ:
  caminho sem divergência        →  R$ 0 de LLM   (esperado: a maioria)
  caminho de divergência conhecida →  R$ 0 de LLM   (template)
  caminho de julgamento          →  única chamada real
```

**A pergunta que o protótipo tem de responder na primeira competência real:** que fração dos CNPJs cai na rota de julgamento? Se for baixa, o produto escala para escritório com centenas de clientes e a assinatura por CNPJ fecha. Se for alta, o preço muda ou o reconciliador precisa ficar mais esperto — **e essa é uma decisão de engenharia, não de desconto**.

Registrar o custo medido na [ficha da ferramenta de agentes](ferramenta-agentes.md), que hoje tem `{{MEDIR no protótipo do 1º cliente}}` em aberto.

---

## 10. Avaliação — e a trava que a protege

**Golden set:** competências reais e anonimizadas, com o gabarito do que **deveria** ter sido manifestado, montado com um contador. Mínimo para a primeira construção: **20 a 50 casos** — a mesma amostra que o [roteiro de descoberta](../03-comercial/roteiro-descoberta-prototipo.md) pergunta no Bloco 5, item 25.

O conjunto precisa conter, obrigatoriamente:

- **Casos positivos** — crédito legítimo omitido pelo Fisco. O produto tem de achar.
- **Casos negativos** — crédito que **parece** devido e não é (vedação, uso e consumo pessoal, documento inidôneo, competência errada). O produto tem de **não** achar. Falso positivo aqui é pior que falso negativo: manda o cliente pleitear o que não é dele.
- **Casos limpos** — nada a fazer. O produto tem de dizer "nada a fazer" sem inventar trabalho.

**Métricas:** recall nos positivos · **precisão nos negativos (a métrica que manda)** · R$ correto no total · taxa de dossiê aprovado pelo contador sem edição material.

> **O avaliador é intocável** (inegociável 4). O golden set e os limiares ficam fora do alcance de qualquer loop de melhoria automática. Um sistema que pode mexer na própria régua otimiza a nota, não o resultado.

**E a regra de vocabulário que vale aqui como em todo o resto:** medimos **concordância com o gabarito**, e é isso que se diz. Não se chama isso de "acurácia fiscal" nem se promete percentual de acerto em contrato (inegociável 5).

---

## 11. Segurança e LGPD

| Item | Regra |
|---|---|
| Segregação | **Um ambiente e um cérebro por cliente.** Escritório contábil = cada CNPJ atendido é um tenant, não uma linha numa tabela comum |
| Credenciais | Sempre **do cliente**, com janela de acesso acordada. A ABBA não guarda certificado digital sem contrato explícito e prazo |
| Retenção | Declarada em contrato, por tipo de dado. Deleção só por `abba forget`, com tombstone |
| Trilha | Toda execução registra entradas, saída, modelo, custo e quem aprovou. É o que se mostra numa fiscalização |
| Inventário Art. 20 LGPD | Iniciado no primeiro deploy, como em toda construção ABBA |
| Segredo | Certificado digital, chave de API e credencial de portal **nunca** em git, nunca em prompt, nunca em log |

---

## 12. Sequência de construção — com os gates

| # | Entrega | Gate para começar |
|---|---|---|
| 0 | `reconciliador` + `nfe_reader` + testes, **sem nenhum agente** | Nenhum. Vale por si: já acha divergência |
| 1 | Golden set com um contador | Escritório parceiro definido |
| 2 | `SentinelaFlow` completo, rota de julgamento incluída | Passo 0 verde no golden set + **C2 respondida** |
| 3 | Aprovação no portal + `ledger_abba` | Um dossiê real aprovado à mão primeiro |
| 4 | Uma competência real, um escritório, poucos CNPJs | Contrato assinado com baseline (MASC) |
| 5 | Diagnóstico de Impacto de Caixa | Sentinela com dois meses rodando |
| 6 | Aceleração de Crédito · Conselho de RAD | Demanda puxada por cliente pagante |

**O passo 0 é o mais importante e o mais fácil de pular.** Um reconciliador determinístico e bem testado, sozinho, já entrega valor e já responde à pergunta de custo do §9. Começar pelos agentes é a forma mais rápida de construir um demo bonito que não fecha conta.

---

## 13. O que **não** construir

Lista curta, porque cada item aqui é uma tentação real:

- ❌ **Transmissão automática ao Fisco.** Nunca. Nem com aprovação. Não é o nosso papel e não é a nossa responsabilidade legal.
- ❌ **Parecer tributário gerado por LLM.** A crew evidencia; o contador conclui.
- ❌ **Agente que decide sozinho aderir ao RAD.** É decisão do cliente, com nome no registro.
- ❌ **Memória própria da CrewAI atravessando execuções.** §6.
- ❌ **Framework/orquestrador próprio.** O [estudo de antecipação](../05-interno/estudo-antecipacao.md) §4 proíbe explicitamente: será grátis ou desmentido em ~18 meses.
- ❌ **Produto que só funciona se o split payment sair.** Foi adiado sem data em 12/08/2026. Nada no caminho crítico pode depender dele.

---

## Ligações

[Plano da Camada de Caixa](../05-interno/plano-camada-de-caixa-2027.md) (a decisão de produto) · [Ficha da ferramenta de agentes](ferramenta-agentes.md) (o que se pode prometer hoje) · [Roteiro de descoberta](../03-comercial/roteiro-descoberta-prototipo.md) (a entrevista que alimenta o desenho) · [Protocolo de prova](../04-entrega/protocolo-de-prova.md) (o gate humano e a medição) · [Estudo da porta financeira](../05-interno/estudo-ia-financeira.md) §4 (de onde a linha nasce)
