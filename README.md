# ABBA Ops: Sistema Operacional do Negócio

> **Este repositório é a FONTE DA VERDADE do negócio ABBA Consultoria de IA.**
> Tudo que define como a ABBA funciona como empresa (identidade, setores, jornada do cliente, templates comerciais, precificação, processos internos) vive aqui, versionado em git.
> Os repositórios de código (`assessment-brain`, `abba-portal`) são ferramentas que servem a este negócio; o repo `ABBA` original é o legado/origem da empresa. Os documentos de negócio que existem neles são histórico ou material de engenharia.

---

## 🗺️ Mapa do repositório

| Diretório | O que contém | Quando consultar |
|---|---|---|
| [`00-identidade/`](00-identidade/) | Plano de negócio, posicionamento, **manifesto**, **alvo**, **ecossistema**, modelo de serviço, marca, apostas futuras, Visão 2029 | Antes de qualquer material externo novo; dúvida sobre "o que a ABBA é" ou "para quem é" |
| [`01-setores/`](01-setores/README.md) | Os 5 setores da empresa como "chapéus" com dono e checklist | Divisão de responsabilidades; entrada de novo sócio/funcionário |
| [`02-jornada-do-cliente/`](02-jornada-do-cliente/README.md) | O funil completo em 11 estágios, um doc por estágio | Sempre que um cliente muda de estágio; onboarding de quem vai atender cliente |
| [`03-comercial/`](03-comercial/) | **Escada**, **kit de presença**, **Mapa de Vazamento**, propostas prontas, contrato-esqueleto, precificação, pautas, e-mails | Da primeira conversa até a assinatura |
| [`04-entrega/`](04-entrega/) | Kickoff, relatório de avaliação, plano de capacitação, SLA, pauta do conselho | Da assinatura até a renovação |
| [`05-interno/`](05-interno/) | Decisões, riscos, finanças, comunicação, societário | Reunião semanal de sócios; qualquer decisão relevante |
| [`06-ferramentas/`](06-ferramentas/mapa-jornada-ferramentas.md) | Mapa jornada × ferramenta + fichas de negócio (o que prometer, setup, custo, dono) | Antes de prometer qualquer coisa técnica; setup de cliente novo |
| [`07-drive/`](07-drive/estrutura-drive.md) | Especificação da estrutura no Google Drive | Criação de pastas de cliente; organização de arquivos vivos |
| [`08-materiais/`](08-materiais/README.md) | Catálogo dos materiais reais (Academy, propostas, modelos-mestres) + fila de produção | Antes de criar qualquer material novo; onboarding de conteúdo |

## 📐 Arquitetura de documentos: as três camadas

Todo documento da ABBA vive em exatamente UMA destas camadas: é isso que impede duplicação e desalinhamento:

| Camada | O que é | Onde vive | Exemplo |
|---|---|---|---|
| **1. Processo** (interno: o COMO) | Checklists, regras, jornada. O que os sócios seguem | Markdown neste repo (`02-jornada/`, `04-entrega/*.md`…) | [processo do termo de aceite](04-entrega/termo-de-aceite.md) |
| **2. Modelo** (externo: o QUE o cliente vê) | DOCX/PPTX no padrão visual, com `{{PLACEHOLDERS}}` | [`08-materiais/modelos/`](08-materiais/README.md) neste repo | [`termo-de-aceite-modelo.docx`](08-materiais/modelos/termo-de-aceite-modelo.docx) |
| **3. Instância** (por cliente) | O modelo preenchido para a empresa X, congelado em PDF | Google Drive ([estrutura](07-drive/estrutura-drive.md)) | `2026-08-14 Termo de Aceite - ExemploCorp.pdf` |

Regras que decorrem disso:
- Conteúdo de entregável mora **só no modelo**: o processo aponta para ele, nunca o duplica.
- Mudou o que o cliente recebe? Muda o **modelo** (camada 2) e registra no [log de decisões](05-interno/registro-de-decisoes.md). Mudou como trabalhamos? Muda o **processo** (camada 1).
- **Nunca**: dado de cliente em git; modelo canônico só no Drive; instância editada depois de enviada (nova versão datada).

## ✍️ Convenções

- Conteúdo em **português brasileiro**; nomes de arquivo em português, **kebab-case, ASCII sem acento** (`precificacao.md`), para evitar problemas de encoding entre sistemas.
- Estágios da jornada têm prefixo numérico (`03-proposta.md`) para a listagem ler como o funil.
- Docs de processo têm formato fixo: **Dono · Entrada · Checklist · Saída · Ferramentas · Templates · Prazo-alvo**: 1 página, executável por 1 pessoa em 1 sentada.
- Placeholders que só os sócios podem preencher aparecem como `{{ASSIM}}`.
- Toda decisão relevante vai para [`05-interno/registro-de-decisoes.md`](05-interno/registro-de-decisoes.md): decisão não registrada não vale.
- **Travessão (o traço longo) não entra em texto da ABBA** (decisão do sócio, 01/09/2026).
  É a assinatura mais reconhecível de texto escrito por IA, e o que a gente
  vende é justamente saber usar IA sem parecer que a IA escreveu. A troca não
  é mecânica: cada caso vira dois-pontos, vírgula, ponto-e-vírgula, ponto ou
  parênteses conforme o que o travessão estava fazendo na frase.
  **Antes de congelar qualquer PDF, rode `sh scripts/checar-texto.sh`**: não
  instala nada, roda em segundos e reprova travessão, célula de tabela
  quebrada e travessão órfão. A própria regra é escrita sem usar o
  caractere: o guarda vale para o README também.

## 🚦 Comece por aqui

1. **Pendências dos sócios, prontas para executar:** [`05-interno/kit-de-execucao-socios.md`](05-interno/kit-de-execucao-socios.md), e-mail do advogado pronto, cerimônia da passphrase, pauta da reunião das 5 decisões, checklist do Pedro, semana do Cliente Zero, a rua. Registro completo: [`05-interno/registro-de-decisoes.md`](05-interno/registro-de-decisoes.md).
1b. **O que 7 lentes externas acham de tudo isso:** [`05-interno/parecer-conselho-2026-08.md`](05-interno/parecer-conselho-2026-08.md): o parecer do conselho consultivo (dono, CFO, CTO, concorrente, investidor, DPO, vendedor): placar, gargalos ranqueados e o plano de 60 dias. Leitura obrigatória antes da próxima reunião de sócios.
2. **Um cliente apareceu?** [`02-jornada-do-cliente/README.md`](02-jornada-do-cliente/README.md). Siga o funil estágio a estágio.
3. **A empresa inteira em uma página (estado real de cada peça):** [`00-identidade/mapa-da-abba.md`](00-identidade/mapa-da-abba.md). O modelo de entrega em detalhe: [`00-identidade/modelo-de-servico.md`](00-identidade/modelo-de-servico.md).
4. **Antes de qualquer decisão grande:** [`00-identidade/visao-2029.md`](00-identidade/visao-2029.md): a paisagem competitiva, o fosso, os inegociáveis e as tensões que não têm resposta pronta.
5. **Vai falar com um prospect?** Três documentos, nesta ordem, e você conduz a reunião inteira: [`00-identidade/alvo.md`](00-identidade/alvo.md) (qualificar e quando recusar) → [`03-comercial/escada-abba.md`](03-comercial/escada-abba.md) (o que exatamente se compra) → [`04-entrega/protocolo-de-prova.md`](04-entrega/protocolo-de-prova.md) (como a gente prova). Falas prontas em [`03-comercial/kit-de-presenca.md`](03-comercial/kit-de-presenca.md); postura em [`00-identidade/manifesto.md`](00-identidade/manifesto.md).
6. **Como o cliente vira parte, e não só compra:** [`00-identidade/ecossistema.md`](00-identidade/ecossistema.md): as 3 camadas, o que já está construído e desligado, e a cláusula de contrato que não pode esperar.
7. **Por que a ABBA prevê algumas coisas e se recusa a prever outras:** [`05-interno/estudo-antecipacao.md`](05-interno/estudo-antecipacao.md): a evidência, a fronteira honesta e o calendário de obrigações com data. O pulso operacional disso é o [`ritual semanal`](04-entrega/ritual-semanal.md).
8. **O Conselheiro Digital** (o maior ativo de engenharia da empresa): o que é e como operar em [`04-entrega/dossie-vivo-conselheiro-digital.md`](04-entrega/dossie-vivo-conselheiro-digital.md) · como ligar em produção em [`06-ferramentas/runbook-ativacao.md`](06-ferramentas/runbook-ativacao.md) · o plano por fases em [`05-interno/plano-implementacao-conselheiro.md`](05-interno/plano-implementacao-conselheiro.md).
