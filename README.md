# ABBA Ops — Sistema Operacional do Negócio

> **Este repositório é a FONTE DA VERDADE do negócio ABBA Consultoria de IA.**
> Tudo que define como a ABBA funciona como empresa — identidade, setores, jornada do cliente, templates comerciais, precificação, processos internos — vive aqui, versionado em git.
> Os repositórios de código (`assessment-brain`, `abba-portal`) são ferramentas que servem a este negócio; o repo `ABBA` original é o legado/origem da empresa. Os documentos de negócio que existem neles são histórico ou material de engenharia.

---

## 🗺️ Mapa do repositório

| Diretório | O que contém | Quando consultar |
|---|---|---|
| [`00-identidade/`](00-identidade/) | Plano de negócio, posicionamento, modelo de serviço, marca, apostas futuras | Antes de qualquer material externo novo; dúvida sobre "o que a ABBA é" |
| [`01-setores/`](01-setores/README.md) | Os 5 setores da empresa como "chapéus" com dono e checklist | Divisão de responsabilidades; entrada de novo sócio/funcionário |
| [`02-jornada-do-cliente/`](02-jornada-do-cliente/README.md) | O funil completo em 11 estágios, um doc por estágio | Sempre que um cliente muda de estágio; onboarding de quem vai atender cliente |
| [`03-comercial/`](03-comercial/) | Propostas prontas, contrato-esqueleto, precificação, pautas, e-mails | Da primeira conversa até a assinatura |
| [`04-entrega/`](04-entrega/) | Kickoff, relatório de avaliação, plano de capacitação, SLA, pauta do conselho | Da assinatura até a renovação |
| [`05-interno/`](05-interno/) | Decisões, riscos, finanças, comunicação, societário | Reunião semanal de sócios; qualquer decisão relevante |
| [`06-ferramentas/`](06-ferramentas/mapa-jornada-ferramentas.md) | Mapa jornada × ferramenta (qual ferramenta serve qual estágio) | Planejamento técnico; avaliação de lacunas |
| [`07-drive/`](07-drive/estrutura-drive.md) | Especificação da estrutura no Google Drive | Criação de pastas de cliente; organização de arquivos vivos |

## 📐 Regra de ouro: git vs. Drive

- **git (este repo)** = o que é **canônico e reutilizável**: templates, processos, decisões, metodologia. Versionado, revisável, nunca contém dados de cliente.
- **Google Drive** = o que é **vivo e específico de cliente**: a proposta preenchida da empresa X, o contrato assinado, apresentações, atas. Estrutura espelhada definida em [`07-drive/estrutura-drive.md`](07-drive/estrutura-drive.md).
- **Nunca**: dado de cliente em git; template canônico só no Drive.

## ✍️ Convenções

- Conteúdo em **português brasileiro**; nomes de arquivo em português, **kebab-case, ASCII sem acento** (`precificacao.md`), para evitar problemas de encoding entre sistemas.
- Estágios da jornada têm prefixo numérico (`03-proposta.md`) para a listagem ler como o funil.
- Docs de processo têm formato fixo: **Dono · Entrada · Checklist · Saída · Ferramentas · Templates · Prazo-alvo** — 1 página, executável por 1 pessoa em 1 sentada.
- Placeholders que só os sócios podem preencher aparecem como `{{ASSIM}}`.
- Toda decisão relevante vai para [`05-interno/registro-de-decisoes.md`](05-interno/registro-de-decisoes.md) — decisão não registrada não vale.

## 🚦 Comece por aqui

1. **Pendências dos sócios (P1–P6):** [`05-interno/registro-de-decisoes.md`](05-interno/registro-de-decisoes.md) — domínio/Workspace e planilha de precificação vêm primeiro.
2. **Um cliente apareceu?** [`02-jornada-do-cliente/README.md`](02-jornada-do-cliente/README.md) — siga o funil estágio a estágio.
3. **O que a ABBA é, em uma leitura:** [`00-identidade/modelo-de-servico.md`](00-identidade/modelo-de-servico.md).
