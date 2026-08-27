# Banco de Pautas — 60 peças que já existem dentro de casa

> **Camada:** ferramenta. Combustível do [motor](motor-de-conteudo.md). Cada
> pauta aponta para o documento do repositório que a sustenta — **nenhuma
> depende de pesquisa nova**, e é por isso que a ABBA consegue publicar todo dia
> útil desde a primeira semana.
>
> **Como se usa:** a coluna Prioridade ordena a fila. `A` = das primeiras seis
> semanas (maior contraste com o mercado, menor risco). `B` = reserva madura.
> `C` = destrava com evento externo ou com o caso medido.
>
> Ao publicar, marcar a linha com a data. Pauta usada não volta — vira
> reciclagem, que é outra coisa.
>
> Dono: chapéu Comercial.

---

## P1 · A Prova (16 pautas)

| # | Pauta | Molde | Fonte | Pri | Publicado |
|---|---|---|---|---|---|
| 1 | Os devs ficaram 19% mais lentos com IA — e saíram convencidos de que estavam 20% mais rápidos | F1 | [base](../00-identidade/base-de-evidencias.md) METR | **A** | |
| 2 | Por que a gente proibiu, por escrito, o número mais compartilhado do LinkedIn sobre IA | F2 | [índice proibido](../00-identidade/base-de-evidencias.md) | **A** | |
| 3 | Mais de 80% dos projetos de IA falham. A causa nº 1 não é técnica | F1 | RAND | **A** | |
| 4 | "IA amplifica o que já existe": o relatório que explica por que o time bagunçado piora mais rápido | F1 | DORA | **A** | |
| 5 | 72% dos líderes dizem medir o retorno de IA. Metade mede "qualidade de dados" | F1 | Wharton | **A** | |
| 6 | Só 1 em 20 empresas transformou IA em resultado financeiro de verdade | F1 | BCG | B | |
| 7 | A Gartner projeta que 4 em 10 projetos de agentes serão cancelados até 2027 | F1 | Gartner | B | |
| 8 | "Agent washing": de milhares de fornecedores de agentes, cerca de 130 são reais | F2 | Gartner | B | |
| 9 | 47% das empresas brasileiras já treinam IA. A pergunta é o que sobrou 90 dias depois | F1 | KPMG | **A** | |
| 10 | Como saber se um número sobre IA é folclore: as quatro perguntas que a gente faz antes de citar | F3 | [base](../00-identidade/base-de-evidencias.md) §4 | **A** | |
| 11 | O 70/30 é a nossa tese, não um estudo — e por que a gente diz isso em voz alta | F2 | [estatuto do 70/30](../00-identidade/base-de-evidencias.md) | **A** | |
| 12 | No topo do mercado, um quarto da receita da McKinsey já é atrelada a resultado. No médio porte brasileiro, ninguém oferece isso | F1 | McKinsey | B | |
| 13 | Apps "vibe-coded" em produção: o custo que só aparece depois | F1 | Escape.tech | B | |
| 14 | O que "medir de fora" quer dizer na prática — e por que autorrelato não serve | F3 | [protocolo](../04-entrega/protocolo-de-prova.md) | **A** | |
| 15 | Quanto custa uma reunião de IA que começa sem métrica combinada | F1 | RAND + [manifesto](../00-identidade/manifesto.md) | B | |
| 16 | O primeiro caso medido da ABBA, inteiro — incluindo o que não funcionou | F8 | [caso publicável](../05-interno/caso-publicavel-modelo.md) | **C** | |

## P2 · O Bastidor (12 pautas)

| # | Pauta | Molde | Fonte | Pri | Publicado |
|---|---|---|---|---|---|
| 17 | Uma ferramenta que confere os nossos próprios materiais e barra o que não pode sair | F4 | [régua do revisor](../06-ferramentas/regua-do-revisor.md) | **A** | |
| 18 | O gate de red flags roda antes do modelo, em código — não em prompt | F4 | arquiteto-patrimonial | **A** | |
| 19 | Um Flow CrewAI de ponta a ponta, com o gate humano no meio | F4 | arquiteto-patrimonial `flow/` | **A** | |
| 20 | PII nunca chega crua ao modelo: como a gente faz isso antes da chamada | F4 | arquiteto-patrimonial | **A** | |
| 21 | O que o nosso sistema faz às 3 da manhã enquanto ninguém está olhando | F4 | assessment-brain `brain/` | B | |
| 22 | Um fato novo não apaga o antigo — ele o supersede, com data. Por que isso importa numa auditoria | F4 | assessment-brain bitemporal | B | |
| 23 | A gente bloqueou por código a chance de melhorar a própria nota depois do resultado | F4 | assessment-brain anti-cheat | **A** | |
| 24 | Como a gente apaga dado de cliente — e emite certificado de que apagou | F4 | assessment-brain `forget.js` | **A** | |
| 25 | O que quebrou essa semana no protótipo, e o que a gente mudou | F4 | qualquer repo | B | |
| 26 | Por que toda função que toca banco é assíncrona num sistema que ainda usa SQLite | F4 | assessment-brain | C | |
| 27 | Teto de gasto por noite: o sistema para sozinho antes de estourar | F4 | assessment-brain `--max-usd` | B | |
| 28 | Um agente rodando dentro do fluxo de um cliente, do começo ao fim | F4 | CrewAI + portal | **C** | |

## P3 · O Método (14 pautas)

| # | Pauta | Molde | Fonte | Pri | Publicado |
|---|---|---|---|---|---|
| 29 | O Mapa de Vazamento: como estimar o dinheiro que some, de fora, sem acesso a nada | F3 | [mapa](../03-comercial/mapa-de-vazamento.md) | **A** | |
| 30 | As 5 perguntas de 45 minutos que valem mais que um diagnóstico de 3 semanas | F3 | [mapa](../03-comercial/mapa-de-vazamento.md) | **A** | |
| 31 | Faixa, nunca número exato: a regra que faz o CFO confiar no que a gente entrega | F7 | [mapa](../03-comercial/mapa-de-vazamento.md) | **A** | |
| 32 | A escada: o que exatamente se compra, degrau a degrau, e o que se perde ao parar em cada um | F3 | [escada](../03-comercial/escada-abba.md) | **A** | |
| 33 | O teste de 6 perguntas para saber se uma empresa está pronta para IA | F3 | [alvo](../00-identidade/alvo.md) | **A** | |
| 34 | Toda proposta nossa tem uma seção do que a gente **não** vai fazer | F7 | [manifesto](../00-identidade/manifesto.md) | **A** | |
| 35 | Manutenção como cartório, não como seguro | F3 | [escada](../03-comercial/escada-abba.md) | B | |
| 36 | A pergunta que a gente instala em cada funcionário: o que posso parar, começar, e ainda preciso fazer | F5 | [posicionamento](../00-identidade/posicionamento.md) | **A** | |
| 37 | O "passo atrás" é produto, não atraso | F7 | DORA + [base](../00-identidade/base-de-evidencias.md) Verdade 2 | **A** | |
| 38 | Por que a métrica é combinada **antes** — e quem do lado do cliente assina | F3 | [protocolo](../04-entrega/protocolo-de-prova.md) | **A** | |
| 39 | Como a gente escolhe cliente: utilidade menos a melhor alternativa dele, vezes gente afetada | F3 | [base](../00-identidade/base-de-evidencias.md) Verdade 3 | B | |
| 40 | Ligação de 20 minutos por semana: o ritual que substitui o relatório mensal que ninguém lê | F3 | [ritual](../04-entrega/ritual-semanal.md) | B | |
| 41 | Dinheiro duro, dinheiro mole e capacidade: por que a gente nunca soma os três | F3 | [protocolo](../04-entrega/protocolo-de-prova.md) §3 | **A** | |
| 42 | O que fica com o cliente quando a gente vai embora | F3 | [escada](../03-comercial/escada-abba.md) | B | |

## P4 · O Brasil Real (10 pautas)

| # | Pauta | Molde | Fonte | Pri | Publicado |
|---|---|---|---|---|---|
| 43 | O calendário de obrigações com data que transforma "um dia" em "agora" | F6 | [antecipação](../05-interno/estudo-antecipacao.md) §5 | **A** | |
| 44 | PL 2338 e ISO 42001: o que muda para uma empresa de médio porte, em português | F6 | [mapa ISO](../06-ferramentas/mapa-avaliacao-iso42001-pl2338.md) | **A** | |
| 45 | IA-sombra: seus funcionários já usam, e o jurídico não sabe quais | F6 | [workshop](../03-comercial/proposta-workshop-shadow-ai.md) | **A** | |
| 46 | LGPD e IA: as três perguntas que o DPO vai fazer e que ninguém prepara | F6 | [sprint LGPD](../03-comercial/proposta-sprint-lgpd.md) | **A** | |
| 47 | Reforma tributária: por que ela é um evento de dado antes de ser um evento fiscal | F6 | [antecipação](../05-interno/estudo-antecipacao.md) | **A** | |
| 48 | NF-e, SPED, EFD: a lei brasileira padronizou o dado, e quase ninguém usa isso a favor | F1 | [mapa](../03-comercial/mapa-de-vazamento.md) | B | |
| 49 | As pesquisas apontam que 98% das empresas brasileiras não acham profissional de IA qualificado | F1 | [base](../00-identidade/base-de-evidencias.md) | **A** | |
| 50 | A cadeira de IA virou padrão — e no médio porte ela nasce fracionária | F1 | Gartner + [conselheiro](../03-comercial/conselheiro-de-ia.md) | B | |
| 51 | Residência de dado no Brasil: a pergunta de compras que derruba fornecedor | F6 | CrewAI/LGPD | B | |
| 52 | Médio porte do DF: o que a gente vê nas empresas daqui que não vê em relatório nenhum | F5 | observação do sócio | **C** | |

## P5 · A Fronteira (8 pautas — as com rosto)

| # | Pauta | Molde | Fonte | Pri | Publicado |
|---|---|---|---|---|---|
| 53 | O que a gente se recusa a prever — e por que publicar o limite é o que torna o resto crível | F5 | [manifesto](../00-identidade/manifesto.md) recusa 8 | **A** | |
| 54 | "Vocês querem tomar o lugar do meu diretor de IA?" Não. E aqui está o porquê | F5/F7 | [objeção](../03-comercial/objecao-diretor-de-ia.md) | **A** | |
| 55 | Nosso sucesso é você precisar menos da gente. Isso destrói o nosso próprio contrato? | F5 | [manifesto](../00-identidade/manifesto.md) crença 6 | **A** | |
| 56 | Ninguém aqui fala "a IA decidiu". A IA rascunhou; alguém assinou | F5 | [manifesto](../00-identidade/manifesto.md) crença 3 | **A** | |
| 57 | O que eu ouvi de um head de TI e que mudou a nossa forma de vender | F5 | insumo do sócio | **A** | |
| 58 | Por que a gente recusa cliente — e como se recusa sem queimar a relação | F5 | [alvo](../00-identidade/alvo.md) | B | |
| 59 | Empresa nova vendendo prova: como se ganha credibilidade sem ter caso ainda | F5 | postura | B | |
| 60 | O que eu vi hoje dentro de uma empresa aqui de Brasília | F5 | visita presencial | **C** | |

---

## Como o banco se renova

Sessenta pautas cobrem ~15 semanas na cadência de 4/semana. A renovação vem de
três lugares, nesta ordem de qualidade:

1. **O combustível de segunda** ([motor](motor-de-conteudo.md)) — reunião,
   objeção, número novo, visita. **Sempre a melhor pauta da semana**, porque é
   a única que nenhum concorrente tem.
2. **Comentário que virou pergunta boa** — a resposta vira a peça da semana
   seguinte, e quem perguntou é notificado. Conteúdo e relacionamento no mesmo
   ato.
3. **Documento novo no repositório** — todo doc de estratégia que entra em
   `abba-ops` carrega pelo menos uma pauta pública dentro dele.

**O que nunca vira pauta:** número fora do cânone · dado de cliente sem
aprovação nominal por escrito · promessa do portal antes do portal
· caso de sucesso antes do [caso medido](../05-interno/caso-publicavel-modelo.md).

---

## Ligações

[Motor](motor-de-conteudo.md) · [Formatos](formatos.md) ·
[Estratégia](estrategia-de-conteudo.md) · [Plano de 90 dias](plano-90-dias.md)
