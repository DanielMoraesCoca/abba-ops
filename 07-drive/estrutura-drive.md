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

## Setup inicial (fazer uma vez, ~30 min)

- [ ] Criar Drive compartilhado "ABBA" no Google Workspace (ver decisão pendente P2 do [registro de decisões](../05-interno/registro-de-decisoes.md) — requer o Workspace)
- [ ] Criar a árvore acima (vazia)
- [ ] Exportar os templates de [`../03-comercial/`](../03-comercial/) e [`../04-entrega/`](../04-entrega/) para DOCX em `03 Modelos/`
- [ ] Definir permissões: ambos os sócios como administradores; ninguém mais até haver funcionários
