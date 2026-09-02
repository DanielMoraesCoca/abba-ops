# O Ecossistema ABBA: como um cliente vira parte, e não só compra

> **Camada:** identidade. Responde à pergunta que os sócios levantaram em 2026-08-01: *como criar um ecossistema conosco, de perto, que vista a nossa bandeira e compre o que oferecemos porque é o melhor?*
>
> **O que este documento descobriu e registra:** a infraestrutura do ecossistema **já está construída** no `abba-portal`, e nenhum documento de negócio sabia disso. O trabalho que falta não é de engenharia; é de doutrina, contrato e sequência.
>
> Dono: chapéu Comercial (doutrina) + Tecnologia (ativação). Revisar a cada cliente novo, porque todos os gatilhos são contagem de clientes.

---

## 1. Por que o ecossistema não é enfeite

A ABBA é uma firma de dois sócios. A pesquisa de serviços profissionais é dura com esse tamanho: **firmas de 1 a 10 pessoas perdem em torno de 32% dos clientes por ano; firmas grandes, cerca de 15%.** A causa raramente é insatisfação. É que **o cliente não perde nada ao sair de uma firma pequena.** Não há sistema, não há comunidade, não há histórico que ele não consiga levar embora ou refazer.

O ecossistema é o mecanismo que neutraliza essa penalidade estrutural. Ele funciona por cinco razões, da mais concreta à mais estratégica:

1. **Cria algo que se perde ao sair.** A posição do cliente contra a distribuição dos outros só existe aqui. Sair da ABBA passa a significar *perder a única régua que ele tem*.
2. **A trava é epistêmica, não contratual.** Não existe no Brasil um índice de maturidade de IA para média empresa. **Quem tem os dados define a régua.** O cliente não fica por multa: fica porque é o único lugar onde "eu estou atrasado?" tem resposta com número.
3. **Transforma custo em ativo.** Hoje o dado de cada engajamento morre no tenant do cliente. Com contribuição anonimizada, **cada cliente novo melhora o produto de todos os anteriores**: efeito de rede literal. É o que separa "consultoria com ferramenta" de "consultoria com ativo próprio" ([Visão 2029](visao-2029.md) §3, camada 3).
4. **Dá ao cliente algo para vestir.** Ninguém veste a bandeira de um fornecedor; as pessoas vestem a de um clube onde aparecem bem. O benchmark dá ao patrocinador **material de política interna** ("estamos no primeiro quartil"); a credencial portátil dá ao campeão **material de carreira**. É isso que "vestir a bandeira" significa na prática: não brinde.
5. **Vira o artefato publicável.** Com massa suficiente, a distribuição agregada é um relatório anual de mercado: a peça que gera entrada sem custo marginal, e que **só nós podemos publicar**.

**O custo honesto, dito aqui para não ser esquecido:** nada disso liga com poucos clientes. Os pisos de privacidade são reais e estão no código (≥5 clientes qualificados, ≥5 pessoas por cliente). **Clientes 1 e 2 precisam comprar por outro motivo**: a [escada](../03-comercial/escada-abba.md) e o [protocolo de prova](../04-entrega/protocolo-de-prova.md), que funcionam com um cliente só.

---

## 2. As três camadas

| Camada | Quem veste | O mecanismo | O que o participante ganha |
|---|---|---|---|
| **Empresa** | Patrocinador, diretoria | **Benchmark recíproco**: contribui com medianas anonimizadas → vê o próprio percentil e os quartis | Sabe onde está. Munição interna de orçamento |
| **Pessoa** | Campeão, colaborador | **Credencial verificável portátil** + rede de campeões entre clientes | Carreira. A credencial vale fora da empresa dele |
| **Padrão** | O mercado | **Cofre de padrões anonimizados** → boletim anual | Referência pública de mercado, e a ABBA como quem a publica |

As três se sustentam: a camada Empresa gera o dado, a camada Pessoa gera a lealdade que sobrevive à troca de emprego, e a camada Padrão transforma as duas em posição de mercado.

---

## 3. O que já existe (e estava invisível para o negócio)

Levantado no `abba-portal` em 2026-08-01. **Isto é código real, não plano.**

| Ativo | O que faz | Estado |
|---|---|---|
| `src/lib/fluency-benchmark.ts` | Posiciona a coorte de um cliente contra a distribuição anonimizada de **todos os outros**. Saída = percentil + limiares de quartil + contagem de clientes. **Nunca** nome, contagem exata ou número bruto de outro cliente | Construído e testado. **Renderiza só para equipe ABBA**: o patrocinador vê um cadeado |
| `src/lib/durability-benchmark.ts` | O mesmo para durabilidade de comportamento a 30/60/90 dias: a métrica **não inflacionável**, e o sinal de renovação mais forte | idem |
| migração `20260625_benchmark_contribution.sql` | O opt-in **recíproco**: *"optar por não compartilhar é optar por não ver"*. Coluna `benchmark_contribution` no tenant | Aplicada. **Padrão = `true`**, com a premissa explícita de que *a contribuição anonimizada é divulgada em contrato* |
| Credenciais verificáveis (`/api/credentials/issue`, `/verify`) | O campeão emite uma credencial assinada que ele carrega entre empregos. O token **não** carrega cliente, e-mail nem nota bruta | Funcional |
| `/api/peer-help` | Reconhecimento de ajuda entre pares | Funcional, **escopo por tenant** (dentro do cliente, não entre clientes). O `/feed` ("Mural de conquistas") saiu em 02/09: era placar social, e quem registra a ajuda passou a ser **quem foi ajudado**, nunca quem quer aparecer |
| `docs/operational/CROSS_CLIENT_CHAMPION_NETWORK.md` | Plano de ativação da rede em 3 estágios (WhatsApp → Slack → plataforma) | Escrito, v1.0 |

> **A implicação mais urgente:** o padrão da coluna é `true` **porque a premissa é que o contrato divulga a contribuição anonimizada**. Hoje o [contrato-esqueleto](../03-comercial/contrato-sow-esqueleto.md) não divulga. Ou o contrato passa a divulgar (Anexo IV), ou o padrão é indefensável perante um DPO. **É a única pendência deste documento que não pode esperar.**

### As barreiras de privacidade, para dizer em voz alta ao guardião

1. Piso de **≥5 clientes** na distribuição: abaixo disso a mediana de um único cliente seria dedutível, e a função devolve "indisponível".
2. Piso de **≥5 pessoas pontuadas** para um cliente entrar na distribuição.
3. A saída carrega **percentil + limiares + contagem**, nunca nome, contagem exata ou valor bruto de outro cliente.
4. Reciprocidade: quem opta por sair, some da distribuição **e** perde a comparação.
5. Segregação entre clientes é [inegociável nº 2](visao-2029.md): só o agregado anonimizado cruza.

---

## 4. A sequência: o que acende com quantos clientes

Hoje temos **zero clientes reais** e todos os gatilhos são de 3 a 5. Fingir o contrário seria o erro mais caro deste documento.

| Marco | O que acende | O que precisa estar feito antes |
|---|---|---|
| **Cliente 1** | Nada de rede. Vende-se a régua **interna**: o [diário de decisões](../04-entrega/protocolo-de-prova.md) e a escada | **Anexo de contribuição/opt-in assinado no contrato** (P4) · consentimento de caso publicável |
| **Cliente 2** | idem | Um caso publicável em construção ([modelo](../05-interno/caso-publicavel-modelo.md)) |
| **Cliente 3** | **Rede de campeões entre clientes**: grupo de WhatsApp facilitado pela ABBA (Estágio 1 do plano do portal). Gatilho da [aposta 4](apostas-futuras.md) | Opt-in de rede na graduação dos campeões |
| **Cliente 5** | **Benchmark deixa de ser interno**: o patrocinador passa a ver percentil e quartis. Migração para Slack | Tirar o gate de equipe ABBA e desenhar a tela (trabalho pequeno de portal); ≥5 pessoas pontuadas por cliente |
| **Cliente 8** | **Primeiro boletim público de mercado** a partir do cofre agregado | Cofre com padrões reais; contrato de redação aplicado ([protocolo §5](../04-entrega/protocolo-de-prova.md)) |

**Regra:** nenhuma camada é prometida a cliente antes do seu marco. O que se pode dizer desde o cliente 1 é o que é verdade: *"isso existe, está construído, e liga quando houver massa suficiente para ser anônimo de verdade, inclusive para proteger você."* Essa frase vende melhor que a promessa, porque explica a barreira de privacidade em vez de escondê-la.

---

## 5. O que a ABBA precisa fazer, e não é código

1. **Anexo IV do [contrato](../03-comercial/contrato-sow-esqueleto.md):** contribuição anonimizada + opt-in de rede + direito de retirada. **Pendência P4 (advogado): é o caminho crítico irreversível.** Consentimento não se retroage: um cliente assinado sem a cláusula está fora do ecossistema para sempre, ou obriga uma renegociação constrangedora.
2. **Opt-in do campeão na graduação:** três opções (entrar, adiar, recusar), registradas. Entra no [plano de capacitação](../04-entrega/plano-de-capacitacao.md).
3. **Contar a régua na pauta do conselho:** a posição no benchmark é item fixo da [pauta](../04-entrega/pauta-conselho.md) a partir do cliente 5.
4. **Manter este documento honesto:** a tabela §3 é fácil de deixar apodrecer. Ela existe justamente porque a versão anterior desse desalinhamento durou meses.

---

## 6. O que este ecossistema **não** é

- **Não é comunidade de marketing.** Se virar canal de divulgação, morre: os participantes saem no terceiro post promocional.
- **Não é compartilhamento de dado entre clientes.** Configurações, métricas e dossiê de cada cliente ficam no tenant dele, sempre. Só o agregado anonimizado cruza.
- **Não é programa de indicação.** Indicações aparecem como consequência; se virarem o objetivo, o clube perde a razão de existir.
- **Não é substituto da relação individual.** O ritual do conselho com cada cliente continua sendo o vínculo primário.

---

## Ligações

[Visão 2029](visao-2029.md): o fosso e o relógio de 24–36 meses · [Apostas futuras](apostas-futuras.md): apostas 3 e 4 · [Alvo](alvo.md), quem entra · [Escada](../03-comercial/escada-abba.md): o que se compra antes disso · [Protocolo de prova](../04-entrega/protocolo-de-prova.md): a régua interna, que vale desde o cliente 1
