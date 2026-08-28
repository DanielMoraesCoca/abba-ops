# Especificação — o Flow de conteúdo com agentes

> **Camada:** ferramenta (especificação, não implementação). Criada por decisão
> do sócio (2026-08-27, V4g): **especificar agora, construir depois.**
>
> **A tese:** o [motor](motor-de-conteudo.md) já descreve o processo inteiro em
> português. Esta spec o traduz para o padrão de Flow que **já existe e roda**
> no `arquiteto-patrimonial`, para que ele deixe de depender de uma conversa e
> passe a ser um sistema.
>
> **O que NÃO se automatiza está no §5, e é a parte mais importante deste
> documento.**
>
> Dono: chapéu Tecnologia (construção) + Comercial (doutrina).

---

## 1. O que já existe e é reusado sem reinventar

O `arquiteto-patrimonial/flow/` já implementa exatamente a arquitetura de que
este Flow precisa. **Nada aqui é novo padrão; é o mesmo padrão, com outro
domínio.**

| Peça existente | Onde | O que resolve aqui |
|---|---|---|
| `Flow` com `@persist()` e estado tipado | `main.py` | A peça atravessa etapas sem perder contexto, e pode pausar |
| **Gate determinístico em código** | `gates.py` (`triagem_red_flags`) | O análogo direto da [régua do revisor](../06-ferramentas/regua-do-revisor.md): trava em código, não em prompt |
| **Teto de gasto que aborta** | `main.py` (`TETO_USD_POR_CASO`, `_cobrar_custo`) | Teto por peça. O mesmo desenho do `--max-usd` do cérebro |
| **Gate humano assíncrono** | `hitl.py` (`montar_item_revisao`, `aplicar_decisao`, `from_pending().resume()`) | O sócio aprova quando puder, sem segurar a execução |
| **Trilha do que foi entregue ao agente** | `main.py` (`chunks_recuperados`) | Torna verificável que toda afirmação da peça veio de fonte real |
| Crews separadas por tarefa | `crews/` | Análise, desenho e redação como unidades distintas |
| Memória desligada em tudo | doutrina do Flow | Cada peça é independente; o contexto entra explícito |

**Regra de construção:** se algo aqui exigir um padrão que o
`arquiteto-patrimonial` não demonstra hoje, isso é sinal de que a spec
extrapolou, e a spec muda antes do código.

---

## 2. A espinha

```
combustível do sócio (§5, humano)
      ↓
[1] Escuta ........... propõe pautas          (crew, barato)
      ↓
[2] Curador de arco .. casa com a linha editorial   (crew, barato)
      ↓
[3] Redator .......... escreve a peça          (crew, médio)
      ↓
[4] RÉGUA ............ gate determinístico     (código, custo zero)
      ↓ (bloqueio volta para [3], no máximo 2 ciclos)
[5] Arte ............. gera as telas           (código, custo zero)
      ↓
[6] GATE DO SÓCIO .... aprovação nominal       (humano, assíncrono)
      ↓
   fila de publicação
```

Determinístico onde dá, LLM só onde precisa. **Dois dos seis passos custam
zero**, e são justamente os dois que protegem a casa.

---

## 3. Os agentes

### [1] Escuta
**Entrada:** o calendário de obrigações do [estudo de antecipação](../05-interno/estudo-antecipacao.md) §5 · notícias do setor · perguntas que clientes fizeram na semana
**Saída:** de 3 a 5 pautas candidatas, cada uma com o gancho de atualidade e a fonte
**Ferramenta:** o mesmo provedor de busca do `abba scout`
**Regra:** nunca inventa acontecimento. Pauta sem fonte datada é descartada no gate.

### [2] Curador de arco
**Entrada:** as pautas candidatas + [`linha-editorial.md`](linha-editorial.md) + [`banco-de-pautas.md`](banco-de-pautas.md)
**Saída:** uma pauta escolhida, com **ato, peça da qual herda, gancho para trás com a palavra exata, e gancho para frente**
**Regra:** se a pauta não couber no ato corrente, ela volta para o banco em vez de furar o arco. **É este agente que impede o feed de virar fila.**

### [3] Redator
**Entrada:** a pauta curada + [`formatos.md`](formatos.md) + o léxico travado + o razão de continuidade
**Saída:** a peça no molde, com legenda, primeiro comentário e notas de operação
**Regra:** só cita número que esteja na [base de evidências](../00-identidade/base-de-evidencias.md), e sempre com a fonte na frase.

### [4] Régua *(código, custo zero)*
**Entrada:** o arquivo da peça
**Saída:** `pass` ou lista de achados
Roda `abba revise` mais as conferências que a régua determinística não cobre:

- todo número citado existe no cânone
- nenhuma linha contradiz o [razão de continuidade](linha-editorial.md) §5
- os dois ganchos existem e a palavra do gancho para trás bate literalmente
- para a [Pista B](duas-pistas.md): nenhuma isca, nenhuma promessa de Pista A

**Bloqueio devolve para [3], no máximo 2 ciclos.** Terceiro bloqueio vira item
para humano, nunca nova tentativa. É o `MAX_CICLOS_REDESENHO` do Flow existente.

### [5] Arte *(código, custo zero)*
Chama o [`gen.py`](artes/feed-lancamento/gen.py) que já existe, escolhendo entre
os seis arquétipos. Não gera arquétipo novo: molde novo é decisão humana,
registrada no [sistema visual](sistema-visual-social.md).

### [6] Gate do sócio *(humano, assíncrono)*
Padrão idêntico ao `hitl.py`: o Flow pausa e persiste, o item entra numa fila, o
sócio aprova, edita ou rejeita, e o Flow retoma.

**O item mostra:** a peça pronta · a pauta e por que ela foi escolhida · o
resultado da régua · o custo gasto · **e o que o Flow não conseguiu confirmar.**

---

## 4. Guarda-corpos, herdados do Flow que existe

| Guarda | Como |
|---|---|
| **Teto de gasto** | Por peça e por semana. Estourou, aborta. Não degrada em silêncio |
| **Nada publica sozinho** | O Flow entrega na fila. **Publicar é sempre ato humano.** Sem exceção e sem modo automático |
| **Trilha de fonte** | Toda afirmação da peça carrega a fonte que a originou, no padrão do `chunks_recuperados` |
| **Sem dado de cliente** | Nenhum agente recebe nome de cliente. O molde [F8](formatos.md) segue bloqueado até existir caso medido com aprovação nominal |
| **Memória desligada** | Cada peça é independente. O arco entra como contexto explícito, lido dos arquivos, nunca como memória acumulada |
| **Régua nunca é LLM** | Quem bloqueia é código. O LLM pode apontar contradição; **quem decide é sócio** |

---

## 5. O que não se automatiza, e por quê

Esta é a seção que mais importa, e ela existe para ser lida antes de qualquer
linha de código.

**O combustível de segunda não tem substituto.** O
[motor](motor-de-conteudo.md) pede quatro coisas ao sócio toda semana: uma coisa
que aconteceu, um número novo, uma opinião defendida em voz alta, e onde ele vai
estar. **Nenhum agente tem acesso a nada disso.**

E é exatamente esse material que faz o conteúdo ser insubstituível. A frase que o
head de TI da Brasal disse é conteúdo que nenhum concorrente tem, e ela não está
em nenhuma base que um agente possa varrer.

**A consequência de desenho:** um sistema que gera pauta sozinho, sem
combustível humano, produz conteúdo correto, coerente com o arco, aprovado pela
régua, e **genérico**. Ou seja: exatamente o que este projeto inteiro existe
para evitar.

Por isso a espinha começa com o combustível humano, e não com o agente de
Escuta. **A Escuta enriquece o combustível; ela não o substitui.**

**Também não se automatiza:** a decisão de publicar · a escolha de arquétipo
visual novo · a aprovação de número novo para o cânone · qualquer peça que
mencione cliente.

---

## 6. Gatilhos para construir

Não construir antes destes três, porque antes deles a automação otimiza um
processo que ainda não provou que roda:

1. **8 semanas de publicação sem furo** na Pista A
2. **O provedor de busca do scout resolvido** (pendência conhecida no [mapa jornada × ferramenta](../06-ferramentas/mapa-jornada-ferramentas.md))
3. **O custo por peça medido** na operação manual, para haver contra o que comparar

**Ordem sugerida quando começar:** [4] Régua e [5] Arte primeiro, porque custam
zero, são determinísticos e já economizam trabalho sozinhos. Os agentes de LLM
depois.

---

## Ligações

[Motor](motor-de-conteudo.md) · [Duas pistas](duas-pistas.md) ·
[Linha editorial](linha-editorial.md) · [Formatos](formatos.md) ·
[Régua do revisor](../06-ferramentas/regua-do-revisor.md) ·
`arquiteto-patrimonial/flow/` (o padrão de referência)
