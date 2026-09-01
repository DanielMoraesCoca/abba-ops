# Pendências — o que precisa ser conferido antes de tocar em dado real

> Cada item aqui é um gate declarado. Nenhum deles bloqueia o desenvolvimento em
> dado sintético; todos bloqueiam o uso com cliente.

## P1 — Layout do XML contra o XSD oficial

Os nomes de campo do grupo IBS/CBS (`gIBSCBS`, `vBC`, `gIBSUF`/`pIBSUF`/`vIBSUF`,
`gIBSMun`/`pIBSMun`/`vIBSMun`, `gCBS`/`pCBS`/`vCBS`, `CST`, `cClassTrib`) foram
levantados de **fontes secundárias** — documentação de fornecedores e material
técnico sobre a NT 2025.002. Não foi possível abrir o Portal Nacional da NF-e
neste ambiente.

**Antes do M6:** baixar os XML Schemas oficiais (Portal Nacional NF-e → Documentos
→ Schemas XML) e conferir campo a campo. Um nome errado não quebra ruidosamente:
o parser lê ausente, o valor vira ausente, e o produto deixa de achar crédito sem
avisar. Por isso `core/modelos.py` recusa transformar campo ausente em zero.

**Dono:** chapéu Tecnologia. **Gate:** M6.

## P2 — Tabela de vedações da LC 214/2025

O par (`CST`, `cClassTrib`) amarra cada item a um dispositivo específico da lei —
é a base da classificação determinística de creditabilidade. A tabela oficial é o
**Informe Técnico 2025.002 — Tabelas de Classificação do IBS e da CBS** (RFB).

**Estado desde o M3a (2026-09-01):** o mecanismo existe e a tabela está vazia — de
propósito.

`core/creditabilidade.py` classifica cada crédito em `CREDITAVEL`, `VEDADO` ou
`DUVIDOSO`; `core/dados/vedacoes.json` é a tabela versionada, com **fonte citada por
linha**. Ela nasce com uma única linha, marcada `a_confirmar: true` — nenhuma foi
conferida no Informe Técnico oficial, e direito tributário não se deduz. Enquanto for
assim, todo crédito cai em `DUVIDOSO`, que é o comportamento seguro: presumir
creditabilidade de código desconhecido é o falso positivo fiscal que manda o cliente
pleitear o que não é dele.

**O trabalho concreto que fecha esta pendência:** sentar com o contador e preencher
`vedacoes.json`, uma linha por dispositivo, cada uma com `doc` apontando o item do IT
2025.002. Trocar `a_confirmar: true` por `false` **só junto com a citação conferida** —
`tests/unit/test_creditabilidade.py` reprova quem apagar a marca deixando a fonte
dizendo "A CONFERIR".

**Como medir o avanço:** `abba-crews cobertura` imprime a fração de itens resolvida sem
julgamento por modelo. Cada linha conferida move o número e tira custo de LLM do produto.

**Dono:** Tecnologia + contador do cliente. **Gate:** M3b (a crew de julgamento só faz
sentido sobre o resíduo que esta tabela não resolver) e promoção a PRODUCAO.

## P3 — Golden set com um contador

O golden set v0 (`core/sinteticos.py`) cobre o comportamento **estrutural** do
reconciliador e nada além disso. Ele não prova nada sobre direito a crédito.

O golden set que promove a Sentinela a `PRODUCAO` é outro: competências reais
anonimizadas, montado **com um contador**, com as vedações do P2, e com o limiar
de precisão nos negativos acordado por escrito — número que ninguém define sozinho
de dentro da ABBA.

**Dono:** Entrega. **Gate:** promoção a PRODUCAO.

## P3b — O calendário, conferido na fonte primária

**Corrigido em 2026-08-30, e vale registrar como o erro se parecia.** Até esta data o
projeto tratava o dia 15 (dia 20 com DeRE) como a data-limite de manifestação. É a data
de **disponibilização** da proposta. O prazo de manifestação vai até o **último dia útil
do mês seguinte**.

O erro era do tipo mais perigoso: plausível, repetido em vários documentos, e no fato
que sustenta o produto inteiro. Um calendário errado no código faria a Sentinela alarmar
na data errada — ou pior, dar por perdido o que ainda dava para manifestar.

Base legal do silêncio, a conferir junto: **art. 348, §1º da LC 214/2025** e **§4º do
art. 125 do ADCT** — a falta de manifestação equivale a **confissão de dívida**.

`core/calendario.py` nasce no M2 com estes prazos e **com a fonte citada por regra**.
Nenhuma data fica escrita em prompt.

**Dono:** Tecnologia. **Gate:** M2 para o código; fonte primária antes de peça comercial.

## P4 — Credencial da Plataforma RTC

O caminho crítico do produto não é código. É entrar no **piloto RTC-CBS**, ou obter
procuração digital de um cliente, para gerar credencial no serviço "Gerar Credencial
para API". Sem isso não há apuração assistida para conferir.

**Dono:** Comercial. **Gate:** M6. **É a semana 1 do plano de 90 dias.**

## P5 — Fronteira profissional revisada por advogado

Texto padrão "diagnosticamos, evidenciamos e organizamos; a decisão e a transmissão
são do cliente" em proposta e contrato, antes da primeira venda. Junto da P4 do
registro de decisões do `abba-ops`.

Inclui a decisão sobre **manifestação do destinatário** na Distribuição DF-e: sem
ela o web service devolve só o resumo, não o XML completo — mas manifestar é
transmitir à SEFAZ, e a doutrina do produto é não transmitir.

**Dono:** Fin-Admin. **Gate:** primeira venda.
