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

**O M4a deu a esta pendência um texto concreto para revisar.** A via assinada
(`abba-crews aprovar`) carrega, no corpo do documento, a frase que separa assinar de
transmitir:

> **Aprovar não é transmitir.** Esta assinatura registra que o profissional conferiu o
> conteúdo acima e o assume. A manifestação ao Fisco continua sendo ato do contribuinte,
> feita no sistema do próprio Fisco, dentro da janela. A ABBA não transmite.

É esse parágrafo — e não uma descrição nossa dele — que vai ao advogado. Ele é o que um
contador lê no dia em que assina, e o que sobra num processo cinco anos depois.

**Dono:** Fin-Admin. **Gate:** primeira venda.

## P6 — Retenção e apagamento dos dossiês

**Aberta no M4a (2026-09-02), junto com a primeira gravação em disco.**

O `abba-crews` passou a guardar dossiês em `~/.abba-crews/dossies/` (ou onde
`ABBA_CREWS_DOSSIES` apontar), cifrados no envelope **ABBA-ENC-1** — o mesmo do
`assessment-brain`, deliberadamente, para que os dois lados leiam o mesmo arquivo.

Duas perguntas ficam em aberto e **nenhuma delas é técnica**:

1. **Por quanto tempo se guarda** o dossiê de um cliente? A resposta tem componente
   legal (prazo decadencial tributário) e componente contratual (o que se promete ao
   cliente sobre os dados dele).
2. **Qual é o caminho de apagamento?** No `assessment-brain` a única via sancionada é
   `abba forget --client|--engagement|--expired`, que expurga arquivo em disco,
   cascateia e escreve tombstone. Hoje o `abba forget` **não alcança** o diretório de
   dossiês do `abba-crews`. Enquanto não alcançar, existe dado de cliente fora do único
   caminho de deleção que a casa reconhece — o que contraria a doutrina de PII do
   `assessment-brain`.

O formato compartilhado é o que torna isso resolvível sem migração: o `forget` já sabe
ler o envelope, falta ensiná-lo o diretório.

**Estado desde 2026-09-02 (P6 parcialmente fechada):** o **caminho de apagamento existe**.
`abba forget --engagement|--client` no `assessment-brain` passa a purgar também os dossiês
e o outbox do `abba-crews`, contando-os no tombstone. Ele acha o que é de quem pelo
`engagement_id` gravado no índice em claro de cada dossiê — que é justamente por isso que
esse campo fica fora da cifra.

Duas honestidades no desenho: quando o outbox não pode ser lido (senha ausente ou
diferente da usada para gravar), o comando **avisa em vez de dizer que apagou** —
deleção parcial anunciada como completa é pior que deleção nenhuma, porque a pessoa para
de procurar. E o diretório nomeado pelo CNPJ some junto: o nome dele é a carteira de
clientes em texto claro.

**O que continua aberto nesta pendência:** por quanto tempo se guarda. Isso tem componente
legal (prazo decadencial tributário) e contratual (o que se promete ao cliente), e não é
decisão de engenharia. Enquanto não houver resposta, os dossiês ficam indefinidamente —
o que é o padrão conservador, mas não é uma política.

**Dono:** Fin-Admin (retenção) + Tecnologia (feito). **Gate:** primeira venda, para a
política de retenção entrar no contrato.

## P7 — Feriado estadual e municipal no cálculo do prazo

**Aberta no M4b (2026-09-02).** `core/calendario.py` cobre feriados nacionais e pontos
facultativos federais — e declara em código que **não** cobre estadual nem municipal.

Isso importa porque o prazo de manifestação é o **último dia útil do mês seguinte**. Uma
empresa em município cujo feriado local caia no último dia útil tem prazo diferente do
que o produto calcula, e o erro é na direção ruim: o produto diria que ainda há prazo.

A mitigação atual é o dossiê sempre mostrar **a data**, nunca só "você tem N dias" — o
contador reconhece o feriado da cidade dele. A correção de verdade é a configuração por
cliente aceitar uma lista de feriados locais, junto do município.

**Correção relacionada, já feita:** faltava o **20 de novembro** (Consciência Negra,
feriado nacional pela Lei 14.759/2023). O produto contava um dia útil a mais em novembro
sempre que a data caía em dia de semana.

**Dono:** Tecnologia + o contador do cliente. **Gate:** primeiro cliente fora de um
município sem feriado relevante — na prática, o primeiro cliente real.

## P8 — CNPJ alfanumérico

**Aberta no M7 (2026-09-03).** `core/cnpj.py` valida o dígito verificador do CNPJ
**numérico** — o que fecha o buraco em que `00000000000192` e `11111111111111` eram
aceitos como clientes válidos.

A Receita passou a emitir **CNPJ com letras**, e a regra de dígito do formato novo
**não pôde ser conferida deste ambiente** (gov.br bloqueado, como no P1 e no P3b).
Implementar regra fiscal que não dá para verificar é exatamente o defeito que este
projeto vem combatendo marco após marco — então ela não foi implementada.

**Efeito hoje:** um CNPJ alfanumérico é recusado por tamanho, porque `normalizar()`
descarta as letras. Falha alto, que é o desfecho seguro — mas por sorte, não por
desenho, e a mensagem de erro aponta para esta pendência.

**O que fecha:** a regra oficial do dígito verificador para o formato alfanumérico, na
fonte primária, mais a decisão sobre a partir de quando um cliente pode aparecer com um.

**Dono:** Tecnologia. **Gate:** primeiro cliente com CNPJ alfanumérico — que pode ser o
primeiro cliente, dependendo de quando a emissão começou a valer para empresas novas.

## P9 — Persistência no destino do deploy (antes de subir para a CrewAI)

**Aberta no M8 (2026-09-03), ao responder "e quando transferirmos para a CrewAI?".**

O armazém de dossiês (`core/arquivo.py`) assume **disco durável**: `~/.abba-crews/dossies`
guarda o rascunho cifrado, a via assinada, o índice e o outbox do ledger. Todo o M4a, o
M4b e o M5 dependem disso.

O gate humano depende de disco durável por desenho, não por acaso: o contador assina
**depois**, no tempo dele. Um dossiê que existe só durante a execução que o gerou não pode
ser assinado por ninguém — e o outbox que espera o `abba crews sync` também se perde.

**Não afirmo o modelo de runtime da plataforma da CrewAI: não consigo verificá-lo deste
ambiente.** Por isso é pendência declarada, não correção. Mas a pergunta precisa de
resposta **antes** do primeiro `crewai deploy push`, porque é decisão de arquitetura:

- se o contêiner for efêmero, o armazém precisa de destino durável (volume, objeto
  remoto, ou o próprio `assessment-brain` como guarda) — e aí a cifra em repouso e o
  alcance do `abba forget` (P6) precisam acompanhar o destino novo;
- se houver disco persistente por deployment, resta decidir onde ele mora em relação ao
  `ABBA_CREWS_DOSSIES` e como a senha chega lá.

**Ressalva de valor:** hoje um deploy não faria nada útil de qualquer forma. `main.py`
monta o Flow sem `Fonte`, e a coleta real só chega no M6 (P4, credencial RTC) — subir
agora produz um Flow que sempre levanta `NotImplementedError`. Honesto, e sem valor.

**Dono:** Tecnologia. **Gate:** antes do primeiro `crewai deploy push`.
