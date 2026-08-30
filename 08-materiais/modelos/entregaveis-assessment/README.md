# Entregáveis do assessment — os três modelos canônicos

> **O que são:** os três documentos que um assessment ABBA produz, gerados pela ferramenta real sobre uma empresa fictícia. Não são maquete, não são mock-up de designer: saíram dos mesmos geradores que vão produzir o entregável de um cliente pagante.
>
> **Regra da casa:** estes arquivos são um **retrato datado**. A fonte da verdade é o comando `abba demo` no `assessment-brain`. Quando o produto mudar, estes arquivos ficam velhos, e o jeito certo de atualizá-los é rodar o comando de novo, nunca editá-los à mão.

---

## A empresa não existe

**Nortex Componentes** é uma fabricante fictícia de componentes usinados: 380 pessoas, duas plantas no Sul, R$ 180 milhões de faturamento. Foi inventada.

Isso é uma decisão, não uma limitação. O one-pager de um cliente real carrega o nome dele, os nomes dos vazamentos e as cifras. Anonimizar aquilo é promessa impossível de cumprir: setor + faixa de faturamento + vazamento principal reidentifica uma empresa de médio porte para qualquer um do mercado, e o mercado brasileiro é pequeno. Um teaser que vaza destrói a única coisa que uma consultoria vende.

O rótulo *(empresa fictícia)* viaja dentro de todos os três documentos, em todo lugar onde o nome aparece. **Nunca remova o rótulo.** Um material que precisa de e-mail de acompanhamento para explicar o que é vai acabar sendo enviado sem ele.

---

## Os três documentos e para quem cada um serve

### 1. `anexo-visual-modelo.pdf` — 8 páginas, PT-BR, é o que você mostra

O documento de reunião. Radar de maturidade, heatmap das 25 dimensões, matriz valor × esforço, roteiro, TCO. Autocontido: fontes embutidas, gráficos em SVG, abre em qualquer lugar.

**Usa quando:** primeira reunião com um CEO que nunca viu um assessment de IA; anexo da proposta; reunião de apresentação de resultados.

### 2. `one-pager-cliente-modelo.md` — o que sobrevive à reunião

Onde o dinheiro está vazando, o que a IA destrava, o que muda para cada papel, a sequência recomendada. É o documento que o cliente circula internamente para aprovar orçamento, e por isso é o que mais precisa ser lido sozinho, sem você na sala.

**Usa quando:** o cliente pede "me manda alguma coisa que eu possa mostrar para o meu sócio".

### 3. `relatorio-consultor-modelo.md` — nunca sai da ABBA

O relatório interno inteiro (cerca de 40 KB), com o apêndice de evidências: as 25 dimensões uma a uma, o organismo, a densidade de evidência, os loops de decisão, a auditoria de confiança da própria análise, a integridade do método e a declaração de completude do run.

**Usa quando:** é seu cérebro durante o engajamento, e é a prova de rigor se alguém desafiar um número. Também serve para mostrar a um sócio, a um futuro contratado ou a um parceiro **o que existe por trás** das 8 páginas bonitas.

---

## O que este material prova, e o que ele NÃO prova

**Prova:** que existe uma máquina, que ela produz três documentos coerentes entre si, que os números viajam com premissa, que o ranking é auditável e que a ferramenta declara os próprios limites.

**NÃO prova:** que a análise é boa. Os textos da Nortex foram escritos à mão. Nenhum modelo leu uma empresa real e produziu isto.

**Por isso a frase certa é:** *"este é o formato do que você recebe"*. A frase errada, que não pode ser dita nunca, é *"foi isto que a nossa IA achou nesta empresa"*.

A própria ferramenta protege essa fronteira: `abba validate` sobre o engajamento de demonstração reprova de propósito e imprime **NOT VALIDATED, AND NEVER CAN BE**. É o único engajamento que nenhuma chave de API pode certificar.

---

## Como responder às duas perguntas difíceis

**"Me mostra um relatório de um cliente real."**

> Não mostro, e o motivo é exatamente o que protege você. O relatório do cliente carrega o nome dele, os vazamentos dele e os números dele. Se eu circulasse isso, você teria que se perguntar o que eu circulo do seu. Este documento tem a mesma estrutura, a mesma profundidade e o mesmo rigor, sobre uma empresa que eu inventei justamente para poder mostrar.

Essa resposta é mais forte que o material que ela recusa a mostrar.

**"Esses números são reais?"**

> São de uma empresa fictícia, e estão escritos assim na capa. O que é real é o método que produz cada número: toda cifra aqui vem com a premissa que a gerou, e você pode discordar da premissa. É exatamente o que vai acontecer com os seus.

---

## Moeda

**Os valores estão em reais**, e não por conversão: a empresa é brasileira, os documentos que ela "entregou" estão em reais, e portanto a aritmética que produziu cada cifra já estava em reais. O engajamento declara a moeda (`abba engagement create --currency BRL`) e a ferramenta imprime o que foi declarado. Nada é convertido em lugar nenhum, porque uma conversão inventaria uma taxa e uma data.

Até 2026-08-30 estes documentos saíam com cifrão. Não era escolha de formatação: era um número certo com o símbolo errado, e errado na direção que nos favorecia, fazendo um vazamento ler cerca de cinco vezes maior do que é.

Duas coisas para você saber ao usar a peça:

- **O custo da análise continua em dólar** ("Cost: $3.18"), e está certo: é o que a Anthropic cobrou. Se um cliente perguntar, essa é a resposta.
- **As premissas são checáveis, e é para serem.** R$ 112/h de engenheiro sênior carregado, R$ 180 milhões de faturamento para 380 pessoas, 1.400 cotações com 22% de taxa de ganho. O CSV que a empresa fictícia "enviou" bate com o registro de vazamentos, e todo payback confere com custo dividido por recuperação mensal. Se um diretor industrial conferir, vai fechar. É o único teste que importa neste documento.

## Como regenerar

```bash
cd /caminho/para/assessment-brain
export USE_MOCK_LLM=true
export ABBA_DATA_DIR=/caminho/absoluto/para/dados-demo

node bin/abba.js demo --force
node bin/abba.js report "Demonstração do método ABBA"
node bin/abba.js report "Demonstração do método ABBA" --client
node bin/abba.js report "Demonstração do método ABBA" --visual
```

Os arquivos saem em `$ABBA_DATA_DIR/<cliente>/<engajamento>/reports/`. Copie por cima destes três e commite, dizendo no commit o que mudou no produto.

O engajamento de demonstração é marcado no banco (`is_demo`), e por causa disso o aprendizado entre clientes **ignora** ele: um resultado inventado nunca vira fator no ranking de um cliente real. `abba demo --remove` tira a demonstração e não toca em mais nada.
