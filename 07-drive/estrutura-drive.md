# Estrutura do Google Drive — ABBA

> O Drive guarda **instâncias** (documentos vivos, específicos de cliente); o git guarda **templates e processos canônicos**. Ver regra de ouro no [`../README.md`](../README.md).

## Árvore oficial (Drive compartilhado "ABBA")

```
ABBA (Drive compartilhado)
├── 01 Comercial/
│   ├── Leads/                        ← 1 subpasta por prospect: "AAAA-MM NomeEmpresa"
│   │   └── 2026-08 ExemploCorp/      (brief do scout, anotações da 1ª call, rascunhos)
│   └── Propostas enviadas/           ← PDF congelado de CADA proposta enviada (imutável)
│
├── 02 Clientes/                      ← pasta criada no estágio 04-contrato, nunca antes
│   └── NomeCliente/
│       ├── 01 Contrato/              (contrato assinado, aditivos, NF-e emitidas)
│       ├── 02 Onboarding/            (kickoff, acessos, lista de participantes)
│       ├── 03 Avaliacao/             (relatório de avaliação, one-pager, briefing)
│       ├── 04 Construcao/            (specs dos agentes, atas de aprovação)
│       ├── 05 Capacitacao/           (plano de capacitação, presença presencial, certificados)
│       ├── 06 Manutencao/            (relatórios mensais, incidentes)
│       └── 07 Conselho/              (atas do ritual trimestral, metas declaradas)
│
├── 03 Modelos/                       ← exports DOCX/PPTX dos templates do git — SOMENTE LEITURA
│   ├── Academy/                      (PDF dos materiais finais de treinamento + artes dos cards)
│   └── (cada arquivo com sufixo "(v1 — fonte: git)")
│
├── 04 Interno/
│   ├── Societario/                   (contrato social, CNPJ, atas de sócios)
│   ├── Financeiro/                   (fluxo de caixa, contratos de fornecedores, impostos)
│   ├── Estrategia historica/         (planos v1–v3 e docs superados — só consulta)
│   └── Reunioes de socios/           (pautas e registros — decisões vão pro git!)
│
└── 05 Marketing/
    ├── Marca/                        (logo, cores, fontes)
    ├── Decks publicos/               (apresentação institucional, deck de vendas)
    └── Site/                         (conteúdo e assets do site de marketing)
```

## Convenções de nome

- **Arquivos datados:** `AAAA-MM-DD Documento — Cliente` (ex.: `2026-08-14 Proposta Avaliação — ExemploCorp.pdf`)
- **Pasta de cliente:** nome curto oficial da empresa, sem razão social completa
- **Pasta de lead:** `AAAA-MM NomeEmpresa` (mês do primeiro contato)
- No Drive pode haver acento e espaço (o git não tem)

## Regras de operação

1. **Modelos nunca são editados no Drive.** Mudou o template? Muda no git primeiro, re-exporta para `03 Modelos/`.
2. **Proposta enviada é congelada** em `01 Comercial/Propostas enviadas/` como PDF no dia do envio — é o registro do que foi prometido.
3. **Lead virou cliente?** A subpasta sai de `Leads/` e o conteúdo migra para `02 Clientes/NomeCliente/` no estágio [04-contrato](../02-jornada-do-cliente/04-contrato.md).
4. **Encerrou o contrato?** A pasta do cliente permanece por 24 meses (prazo de retenção prometido em proposta), depois é eliminada — o processo de eliminação segue [11-renovacao-e-encerramento](../02-jornada-do-cliente/11-renovacao-e-encerramento.md).
5. **Compartilhamento externo:** só arquivos individuais, nunca pastas inteiras; sempre com prazo de expiração quando o Drive permitir.

## Migração do Drive antigo (fazer junto com o setup)

Existe um Drive ABBA anterior com testes e rascunhos: [pasta "ABBA"](https://drive.google.com/drive/folders/1baqSSorcHRxRJKgtAOOrLGCjT8WBxJes) na conta pessoal `pedrohdmoura@gmail.com` (criada em mar/2026). Regras da migração:

1. **Não construir nada novo lá.** A pasta antiga é legado até a migração.
2. Motivo estrutural: material da empresa em conta pessoal de sócio é risco (acesso, saída, LGPD). O Drive oficial vive no Workspace da empresa (`abbaservices.com.br`), com os dois sócios como administradores.
3. Renomear a pasta antiga para `_ARQUIVO ABBA (não usar)` ao final, backup por 90 dias.

### Mapa de migração arquivo a arquivo (inventário de 2026-07-23)

⚠️ **Todos os documentos abaixo contêm DADOS DE EXEMPLO** (empresas fictícias, métricas ilustrativas — algumas com erros, ex.: "acurácia 101%"). São **modelos**, nunca enviáveis como estão: na migração, trocar exemplos por `{{PLACEHOLDERS}}`.

| Arquivo na pasta antiga | O que é | Destino no Drive oficial |
|---|---|---|
| `ABBA_Proposta_Comercial.docx` | Versão anterior da proposta Galápagos **com preços (R$ 150K total)** | `04 Interno/Estrategia historica/` — superada pelo [modelo canônico](../08-materiais/modelos/proposta-comercial-modelo.docx); preços registrados na [planilha de precificação](../03-comercial/precificacao-planilha.md) |
| `ABBA_Proposta_Comercial.pptx` | Deck da proposta | `03 Modelos/Comercial/` — revisar contra o modelo canônico antes de reusar |
| `ABBA_Institucional [Autosaved].pptx` | Deck institucional (tentativa anterior) | `04 Interno/Estrategia historica/` — superado pelo [novo deck](../08-materiais/modelos/abba-deck-institucional.pptx); garimpar slides bons antes de arquivar |
| `ABBA_Termo_Aceite.docx` | **Termo de aceite formal de entregáveis** | `03 Modelos/Entrega/` — vivo! Transcrito para o repo: [`04-entrega/termo-de-aceite.md`](../04-entrega/termo-de-aceite.md) |
| `ABBA_Assessment_Maturidade_IA.docx` | Modelo do Relatório de Maturidade (6 dimensões, escala 1–5) | `03 Modelos/Entrega/` — base do relatório do estágio 06 |
| `ABBA_Mapeamento_Casos_Uso.docx` | Modelo do Mapa de Oportunidades (matriz de priorização, ROI) | `03 Modelos/Entrega/` |
| `ABBA_Plano_Diretor_Tecnologia.docx` | Modelo do Plano Diretor de IA (24 meses) | `03 Modelos/Entrega/` |
| `ABBA_Relatorio_Prototipo.docx` | Modelo do relatório de protótipo (sprints, métricas, GO/NO-GO) | `03 Modelos/Entrega/` — estágio 07 |
| `ABBA_Relatorio_Deployment.docx` | Modelo do relatório de go-live (testes, SLAs, rollback, handover, hypercare) | `03 Modelos/Entrega/` — estágio 07 |
| `ABBA_Relatorio_Mensal_Operacao.docx` | Modelo do relatório mensal de serviços gerenciados | `03 Modelos/Entrega/` — alinhar com o [SLA](../04-entrega/sla-manutencao.md) (estágio 09) |
| `ABBA_Plano_Capacitacao_IA.docx` | Plano de capacitação anterior (4 trilhas por papel, 8 semanas) | `04 Interno/Estrategia historica/` — superado pelo modelo Academy; a divisão por papel pode inspirar o [plano por cliente](../04-entrega/plano-de-capacitacao.md) |
| `ABBA_Estrategia_Implementacao.docx` | Exemplo de Estratégia de Implementação (programa enterprise R$ 4,2M) | `03 Modelos/Entrega/` — modelo para engajamentos grandes |
| `ABBA_Training_Operational_Playbook.docx` | Playbook operacional de treinamento | `03 Modelos/Academy/` — conciliar com os [materiais finais](../08-materiais/README.md) |

## Setup inicial (fazer uma vez, ~30 min)

- [ ] Criar Drive compartilhado "ABBA" no Google Workspace (ver decisão pendente P2 do [registro de decisões](../05-interno/registro-de-decisoes.md) — requer o Workspace)
- [ ] Criar a árvore acima (vazia)
- [ ] Exportar os templates de [`../03-comercial/`](../03-comercial/) e [`../04-entrega/`](../04-entrega/) para DOCX em `03 Modelos/`
- [ ] Definir permissões: ambos os sócios como administradores; ninguém mais até haver funcionários
