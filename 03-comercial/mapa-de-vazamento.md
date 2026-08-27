# Mapa de Vazamento — a peça de abertura

> **Camada:** comercial (processo). É o **degrau 0** da [escada](escada-abba.md) e a resposta ao diagnóstico dos sócios em 2026-08-01: *"temos acesso a qualquer empresa; falta ter algo apresentável e sólido."*
>
> **O que mudou:** a [degustação](../02-jornada-do-cliente/02-diagnostico-gratuito.md) já existia e era boa — três hipóteses de oportunidade com ordem de grandeza. Faltava **um número em reais na primeira página**. O Mapa de Vazamento é essa primeira página, e o resto da Análise ABBA continua igual.
>
> Dono: chapéu Comercial. Modelo: [`analise-abba-modelo.docx`](../08-materiais/modelos/analise-abba-modelo.docx), seção 1.

---

## Por que um número, e não três hipóteses

Três hipóteses fazem o leitor pensar. **Um número faz o leitor reagir** — concordando, discordando ou corrigindo. Qualquer uma das três reações é uma conversa; a ausência de reação é um PDF arquivado.

O número também escolhe o interlocutor. Hipótese de IA circula na TI. **Faixa de dinheiro vazando circula na diretoria e no financeiro** — que é exatamente onde o [alvo](../00-identidade/alvo.md) diz que a decisão mora.

E é independente de setor por construção: a estimativa se apoia no que a lei brasileira padroniza (NF-e, SPED, EFD, obrigações acessórias) e em referências públicas de mercado — não em conhecimento de indústria que não temos ainda ([estudo da porta financeira](../05-interno/estudo-ia-financeira.md)).

---

## A conversa de 45 minutos

Não é reunião de vendas. É a coleta que torna a estimativa defensável. **Cinco perguntas, nesta ordem** — e as três primeiras são as do [teste do alvo](../00-identidade/alvo.md), então a qualificação acontece de graça, junto.

1. *"Me conta o caminho de uma nota fiscal aí dentro, do pedido até o pagamento — quem toca, em que sistema."*
   → revela retrabalho, quebras entre sistemas e onde o dado mora.
2. *"O que mais atrasa o fechamento do mês? E quanto tempo ele leva hoje?"*
   → o fechamento é o termômetro universal de fricção financeira, em qualquer setor.
3. *"Tem algum número em reais que dói hoje e que vocês já medem?"*
   → a única pergunta cuja resposta negativa muda a oferta (sem métrica, o degrau é a avaliação, não o programa).
4. *"Quando vocês descobrem que perderam dinheiro — no mês, no trimestre, no ano seguinte?"*
   → a latência da descoberta é onde o vazamento vive escondido.
5. *"Se esse número melhorasse 20%, quem na empresa comemoraria?"*
   → identifica o patrocinador real, que quase nunca é quem marcou a reunião.

**Regra:** não apresentar nada nesta conversa. Quem apresenta antes de entender vende o produto errado.

---

## O documento: a abertura da Análise ABBA

**O Mapa de Vazamento é a seção 1** — a primeira página, a que carrega a faixa em
reais. Ele **não é** o documento inteiro: a
[Análise ABBA](../02-jornada-do-cliente/02-diagnostico-gratuito.md) completa tem
hoje **entre 32 e 60 páginas**, conforme o modelo de profundidade escolhido, e é
**gerada em menos de cinco minutos** pelo assessment-brain (fato corrigido em
2026-08-27; o "2 páginas em 48h" que estava aqui descrevia só a seção 1 e o
prazo do fluxo antigo).

**A regra que isso não muda:** a primeira página continua sendo um número, não um
sumário. As outras dezenas existem para o leitor **conferir de onde o número
saiu**. Volume é trilha de auditoria, nunca argumento de venda: uma análise
longa que não abre com uma faixa em reais falhou no que importa.

Estrutura da seção 1:

| Elemento | Regra |
|---|---|
| **A faixa em R$** | Sempre **faixa**, nunca ponto. Em ordem de grandeza anual |
| **O vetor principal** | Uma frase dizendo por onde o dinheiro sai (retrabalho fiscal · juros e tarifas evitáveis · perdas em conciliação · contingências…) |
| **As premissas** | Três, numeradas, **com a fonte citada**. Incluindo obrigatoriamente **o que assumimos e ainda não sabemos** |
| **O aviso de faixa** | Texto fixo: foi calculado de fora; uma resposta do cliente pode mover a faixa nos dois sentidos |
| **As perguntas** | As que só ele pode responder — e que mudariam a estimativa |

### As regras de honestidade (não negociáveis)

1. **Faixa, nunca número exato.** Um número exato calculado de fora é uma mentira com aparência de precisão — e o primeiro CFO competente que ele encontrar vai desmontá-la.
2. **Premissa sem fonte não entra.** Se não há referência pública citável, o item sai do mapa.
3. **A faixa pode ser pequena.** Se a estimativa honesta for baixa, ela vai baixa. Um mapa inflado vende uma reunião e perde a relação.
4. **Nunca prometer que a ABBA captura a faixa inteira.** O mapa estima o vazamento; a captura é uma fração dele, e isso se diz em voz alta na apresentação.
5. **Sem dado do cliente no documento** enquanto não houver contrato — só informação pública e o que ele disse na conversa.

> Estas cinco regras são o mesmo princípio do [protocolo de prova](../04-entrega/protocolo-de-prova.md): não afirmamos precisão que não medimos. É a peça de abertura que já demonstra o método pelo qual queremos ser contratados.

---

## Fluxo operacional

| Quando | O quê |
|---|---|
| Antes | `abba scout "NomeEmpresa" --industry X --create` com provedor de busca real. **A geração leva menos de 5 minutos** |
| Antes | Curadoria dos sócios sobre a faixa: escolher o vetor, escrever as premissas com fonte |
| Antes | Revisão cruzada do outro sócio sobre **a faixa** — **obrigatória**, é onde a faixa inflada é pega |
| D+0 | Conversa de 45 min (as 5 perguntas) · registrar o placar do teste de alvo · apresentar a análise ao vivo |
| D+0 | O PDF vai **depois** da apresentação |

> **A questão operacional que a velocidade abriu** (decisão dos sócios pendente):
> a geração em 5 minutos permite entregar a análise **dentro da própria conversa**,
> e é isso que o [enviável](../08-materiais/modelos/abba-apresentacao.pdf) promete
> desde a [V3v](../05-interno/registro-de-decisoes.md). Mas a **revisão cruzada da
> faixa é inegociável** e não cabe numa conversa ao vivo. A saída que este fluxo
> adota: **o scout roda antes da conversa**, com informação pública, e a conversa
> refina. Se os sócios preferirem gerar ao vivo, então a faixa da primeira página
> só é dita depois da revisão cruzada, nunca na hora.
| D+2 | Registrar reação, objeções e o degrau proposto no [pipeline](pipeline-modelo.md) |

**Custo-alvo:** < {{CUSTO_MAX}} em API + 3h de sócio. Acima disso, só para lead que fez ≥3 pontos no teste de alvo.

---

## Ligações

[Estágio 02 — degustação](../02-jornada-do-cliente/02-diagnostico-gratuito.md) (o processo completo do estágio) · [Alvo](../00-identidade/alvo.md) · [Escada](escada-abba.md) · [Estudo da porta financeira](../05-interno/estudo-ia-financeira.md) · [Modelo DOCX](../08-materiais/modelos/analise-abba-modelo.docx)
