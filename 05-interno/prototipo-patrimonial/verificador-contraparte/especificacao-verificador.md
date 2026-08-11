# Verificador de Contraparte — Especificação e Fontes

> **Camada:** interno (engenharia de protótipo). Detalhe técnico do [plano](plano-verificador.md); herda a arquitetura CrewAI Flow-first do [protótipo patrimonial](../especificacao-agentes.md). Todas as afirmações de indicador de fraude têm fonte no [alerta](alerta-indicadores-fraude.md).

---

## 1. A espinha (Flow + gate de código + crew de verificação + humano)

```
Flow[EstadoVerificacao]  (@persist)
│
├─ @start  intake()                    [determinístico] upload PDF/texto → extração de entidades
├─ @listen gate_indicadores()          [determinístico] a tabela de indicadores de fraude (código)
├─ @router:  "alto_risco_documental"   → relatorio_risco_alto()  [humano primeiro]
│            "prosseguir_verificacao"  → crew_verificacao()
├─ @listen crew_verificacao()          [crew] tools de fonte pública, cada achado citado
├─ @listen analise_vinculos()          [determinístico] entidades ligadas por e-mail/tel/endereço
├─ @human_feedback gate_analista()     [HUMANO] analista/advogado lê e assina
└─ @listen render_relatorio()          [determinístico] relatório de RISCO (nunca "aprovado") + trilha
```

## 2. Extração de entidades (intake — determinístico)

De cada documento: **empresas** (nome, registro, jurisdição, endereço) · **pessoas** (nome, cargo, passaporte, nascimento) · **bancos/instrumentos** (nome, SWIFT/BIC, IBAN, conta, tipo — MT103/MT760/SBLC/RWA) · **contatos** (e-mail, telefone, domínio) · **valores**. Saída: `EntidadesExtraidas` (Pydantic). PII redigida antes de qualquer LLM (hook `@before_llm_call`).

## 3. Gate de indicadores de fraude (código puro — o coração)

Implementa a tabela do [alerta](alerta-indicadores-fraude.md). Cada regra devolve indicador com severidade e fonte:

| Regra (código) | Severidade | Fonte citada |
|---|---|---|
| Presença de MT760/MT103 "trading/swap/monetization" · RWA + POF bilionário · PPP/MTN program · SBLC "leased" | **alto** | FBI/SEC/Tesouro/ICC prime-bank |
| Termos "IP/IP", "server-to-server", "KTT", "screen-to-screen" | **alto** | compliance bancário (KTT/IPIP) |
| Documento não reconhecido ("Certificate of Infrastructure Setup") | **médio** (sem fonte que valide — declarar como tal) | — (ausência de fonte legítima) |
| "Bank officer" com e-mail gratuito (gmail/outlook) ou domínio ≠ do banco | **alto** | FATF/FFIEC/ONU |
| Country-code do telefone ≠ jurisdição declarada | **médio** | ACAMS/FFIEC |
| Soma desproporcional à natureza/porte declarados | **médio** | FATF |
| Mesma pessoa/e-mail/telefone/endereço em entidades "independentes" | **alto** | FATF (partes relacionadas) |
| SWIFT/BIC com formato inválido (regex ISO 9362) ou inexistente no diretório | **alto** | SWIFT |

`≥1 indicador alto` → rota "alto risco documental": o relatório sai com o alerta e **sem** prosseguir para dar aparência de verificação aprofundada a algo já reprovado. (Verificar fontes ainda roda, mas o veredito de risco já está cravado.)

## 4. Crew de verificação (agentes + tools de fonte pública)

Processo sequencial; cada task com `output_pydantic` + guardrail anti-citação-órfã (herdado do patrimonial); temperature 0.

| Agente | Tool (fonte pública) | Produz |
|---|---|---|
| **Verificador societário** | registro empresarial (OpenCorporates como índice → fonte primária: Companies House, SEC EDGAR, e-Justice/BRIS, Receita/CNPJ) | a empresa existe? dirigentes batem? há UBO oculto? |
| **Verificador de sanções** | OFAC SDN · UN Consolidated · EU Consolidated · OpenSanctions (inclui PEP parcial) | entidade/pessoa em lista? |
| **Verificador bancário** | diretório SWIFT/BIC oficial · validação ISO 9362 | o BIC existe e pertence ao banco citado? |
| **Verificador de infraestrutura** | WHOIS (ICANN Lookup) | idade/registro do domínio; e-mail corporativo real ou recém-criado? |
| **Verificador de mídia** | busca web de mídia adversa | notícia de fraude/litígio/insolvência? |

Regra de abstenção herdada: sem fonte que sustente, `nao_coberto=true` — e a distinção **"confirmado por regulador" vs "sem fonte que valide"** é campo obrigatório do achado (foi a disciplina que a pesquisa exigiu: WAFUNIF é real; "CIS" não tem fonte; etc.).

## 5. Relatório de saída (nunca "aprovado")

Schema `RelatorioRisco`: nível geral (`alto` · `médio` · `inconclusivo` · `sem indicadores encontrados nesta data`) — **não existe "aprovado/idôneo"** · lista de indicadores com severidade e fonte · resultado de cada verificação com fonte · o que NÃO foi possível verificar · rodapé fixo: *"Relatório de apoio à decisão; não é atestado de idoneidade nem recomendação de transação. Consultas em fontes públicas na data X. Decisão e assinatura: [analista/advogado nomeado]."*

## 6. Guardrails (código)

Anti-citação-órfã (herdado) · **anti-selo**: bloqueia qualquer saída contendo "aprovado", "idôneo", "garantido", "seguro para transacionar" (a trava 2 vira código) · anti-linguagem-de-facilitação.

## 7. Reuso do scaffold patrimonial

`schemas.py`, `guardrails.py` (anti-citação-órfã), o padrão de Flow + gate + `@human_feedback`, o harness de eval — tudo herdado de `../scaffold/`. Novo: `gate_fraude.py` (a tabela §3), as tools de fonte pública, o schema `RelatorioRisco`. Memória OFF; dado de caso só no estado do Flow.

## Ligações

[Plano](plano-verificador.md) · [Fronteira ética e legal](fronteira-etica-legal.md) · [Alerta de indicadores](alerta-indicadores-fraude.md) · [Especificação patrimonial (arquitetura-mãe)](../especificacao-agentes.md) · [Scaffold reutilizado](../scaffold/README.md)
