# Protocolo de Prova: como a ABBA prova que funcionou

> **Camada:** entrega (processo). É o contrato metodológico que atravessa todo engajamento: **nenhuma decisão de IA entra sem métrica de sucesso acordada antes; toda decisão vira resultado medido depois; o cliente vê o registro inteiro.**
>
> **Por que existe:** até 2026-08-01 a ABBA tinha o mecanismo em código (o diário de decisões do [Conselheiro Digital](dossie-vivo-conselheiro-digital.md)) e **nenhum documento que o vendesse como promessa**. Prova era algo que a gente esperava ter depois do primeiro cliente; este documento a transforma em algo que a gente promete desde o primeiro dia.
>
> Dono: chapéu Entrega. Assinado pelos dois sócios em toda proposta que inclua os degraus 2+ da [escada](../03-comercial/escada-abba.md).

---

## 1. A promessa

Três frases, e elas cabem numa proposta:

1. **Nada entra sem métrica.** Toda recomendação da ABBA nasce com o número que vai dizer se ela deu certo, o valor de partida desse número, e o prazo de medição. **acordados com o cliente antes da execução começar**.
2. **Tudo sai medido.** Terminado o prazo, o número é remedido e o veredito é registrado: melhor, pior, neutro ou inconclusivo. **"Inconclusivo" é um resultado legítimo e aparece no registro**: o que não existe é decisão sem desfecho.
3. **O cliente vê o registro inteiro.** Não uma seleção. O diário completo, incluindo o que deu errado.

### Por que essa promessa vale mais do que parece

O padrão dominante nas falhas de projeto de IA não é técnico: é a **ausência de definição acordada de sucesso antes do início**. Projetos que definem métrica quantificada na largada têm taxa de sucesso substancialmente maior que a média do mercado.

A conclusão prática é incômoda para o resto do setor e ótima para nós: **o ato de registrar a decisão com métrica antes de começar já é a intervenção.** Não é papelada em cima do serviço, é uma das partes do serviço que mais move o resultado. E é a única que a ABBA pode prometer com honestidade **no cliente número um**, porque não depende de histórico.

> **Fonte a citar no material externo:** a estatística acima vem da pesquisa de mercado consolidada em 2026-08-01. Antes de usar o número exato numa peça pública, colar a fonte primária aqui. Enquanto isso, usar a formulação qualitativa ("a maioria dos projetos que falham não tinha métrica acordada antes"), que é seguramente sustentada.

---

## 2. Como funciona na prática

O ciclo é o mesmo em qualquer degrau, e é executado pelas ferramentas que já existem.

| Momento | O que acontece | Comando |
|---|---|---|
| **Recomendação** | A ABBA registra a decisão proposta, com métrica, linha de base e prazo | `abba decision add <eng> --title "..." --recommended-by consultant` |
| **Decisão** | O cliente decide. **Gate de humano nomeado** · sem nome, não avança | `abba decision advance <eng> <id> --to decided --by "Nome"` |
| **Implantação** | Executado | `abba decision advance <eng> <id> --to implemented` |
| **Medição** | O número é remedido contra a linha de base e recebe veredito | `abba decision outcome <eng> <id> --metric ... --value ... --baseline ... --verdict better\|worse\|neutral\|unclear` |
| **Aprendizado** | Um resultado **medido** reforça os fatos que informaram aquela decisão; um resultado ruim **não rebaixa nada em silêncio** · enfileira o fato para reconfirmação humana | `abba brain reconfirm <eng>` |
| **Revisão** | O ciclo inteiro entra na pauta do conselho | [pauta do conselho](pauta-conselho.md) |

O registro é **forward-only**: não se reescreve status para trás e nada é apagado. A memória é bitemporal: supersessão nunca deleta ([dossiê vivo](dossie-vivo-conselheiro-digital.md)).

**Regra do centauro, inegociável:** a IA rascunha, o humano cura e assina, a diretoria decide. Nenhum artefato chega ao cliente sem assinatura humana ([Visão 2029](../00-identidade/visao-2029.md) §6, inegociável 1).

---

## 3. O que medimos, e o que nos recusamos a chamar de medição

Esta seção existe para nos proteger de nós mesmos. É fácil, sob pressão comercial, transformar um número frouxo em promessa.

| Classe | Exemplo | Como tratamos |
|---|---|---|
| **Dinheiro duro** | Custo que deixou de sair do caixa, receita recuperada, multa evitada | Vai para o resultado com valor em R$. É a classe que o CFO aceita |
| **Dinheiro mole** | Horas economizadas, tempo de ciclo | Vai para o registro **em horas ou dias, nunca convertido em R$ sem o cliente concordar com a taxa de conversão por escrito** |
| **Capacidade** | Campeões formados, adoção, autonomia | Vai para o registro como contagem. **Nunca somado a dinheiro** |
| **Coerência da memória** | Sondas de consistência bitemporal da auditoria noturna | Nunca chamado de "acurácia". Mede se a linha do tempo é coerente, **não** se ela é verdadeira ([inegociável 5](../00-identidade/visao-2029.md)) |
| **Fidelidade à fonte** | Sondas pagas de *grounding* | Só quando efetivamente compradas (`--audit-grounding-usd`). Sem elas, não afirmamos fidelidade |

**Nunca somar classes diferentes num total único.** Um total que mistura reais com horas é uma mentira aritmética com aparência de rigor.

---

## 4. O que hoje provamos, e o que ainda não

Honestidade obrigatória, e este quadro precisa ser atualizado, não apagado, à medida que os clientes chegam.

| Afirmação | Estado em 2026-08-01 |
|---|---|
| "Temos um método de registro decisão → resultado, em produção, auditável" | ✅ **Verdade.** Construído, testado (429/429 nos dois modos), seis rodadas de revisão adversarial |
| "A avaliação em 25 dimensões captura o que promete" | ⚠️ **Validado em dados sintéticos.** A validação com LLM real ainda não foi rodada ([R1](../05-interno/registro-de-riscos.md), [runbook §6](../06-ferramentas/runbook-ativacao.md)) |
| "Temos padrões acumulados entre clientes que aceleram o próximo diagnóstico" | ❌ **Ainda não.** A mecânica do cofre existe; o cofre está **vazio** · nenhum engajamento real ainda |
| "Temos casos com resultado medido" | ❌ **Ainda não.** O molde do primeiro está pronto ([caso publicável](../05-interno/caso-publicavel-modelo.md)); falta o cliente real |
| "Temos benchmark entre clientes" | ❌ **Construído e desligado.** Piso de 5 clientes ([ecossistema](../00-identidade/ecossistema.md)) |

**Como isso se diz na frente do cliente**, sem perder a venda e sem mentir:

> *"O que eu posso te garantir hoje não é uma média de mercado, é o método. Toda decisão que a gente recomendar vai ter um número combinado com vocês antes, e vai ter esse número remedido depois, esteja bom ou ruim. Você vai ver o registro inteiro. Se depois de seis meses o registro mostrar que não valeu a pena, você vai ser a primeira pessoa a saber, por escrito, e por nós."*

Essa frase converte melhor que uma estatística inventada, e é a única que aguenta uma auditoria.

---

## 5. Do registro ao caso publicável

O diário é interno e confidencial. O que sai dele para o mundo passa por um **contrato de redação**: o mesmo padrão já usado no relatório de Shadow AI:

1. **N ≥ 5**: nenhum achado atribuível a um departamento com menos de 5 pessoas.
2. **Duas entradas corroborantes**: nenhum achado publicado a partir de uma única fonte.
3. **Sem identificação indireta**: nada de "a empresa de logística de Goiás com 300 funcionários".
4. **Aprovação nominal do cliente por escrito**, com o texto final à vista, antes de qualquer publicação.
5. **O que deu errado também é publicável**, e é o que dá credibilidade ao resto.

Estrutura do caso: [modelo de caso publicável](../05-interno/caso-publicavel-modelo.md).

---

## 6. Onde este protocolo aparece

- **Proposta** (degraus 2+): uma página anexa com a §1, é o diferencial mais forte que temos hoje
- **[Contrato](../03-comercial/contrato-sow-esqueleto.md):** a promessa vira cláusula; a contribuição anonimizada ao cofre vira anexo
- **[Kickoff](kickoff-roteiro.md):** as métricas dos primeiros itens são acordadas ali, com o patrocinador na sala
- **[Pauta do conselho](pauta-conselho.md):** o diário é lido em voz alta, item a item
- **[Renovação](../02-jornada-do-cliente/11-renovacao-e-encerramento.md):** o registro acumulado é o argumento, não a apresentação
