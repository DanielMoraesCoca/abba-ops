# Verificador de Contraparte (KYB anti-fraude) — Plano de Construção

> **Camada:** interno (estratégia + engenharia de protótipo). Origem: 2026-08-12, pedido do contato de domínio por uma ferramenta que "pesquise em fontes públicas os funcionários/empresas de uma contraparte para que ela não minta". A leitura dos documentos que ele enviou revelou tipologia de fraude de instrumento financeiro ([alerta](alerta-indicadores-fraude.md)) — o que torna o caso de uso, na verdade, **verificação de contraparte / KYB anti-fraude**, uma categoria real e legal.
>
> **Leia primeiro:** [fronteira ética e legal](fronteira-etica-legal.md) — neste produto, a fronteira é o produto.
>
> Gate comercial: nenhum contrato/sociedade antes do advogado próprio (P4). Isto é um protótipo (degrau 2), não uma empresa nova.

---

## 1. O produto em uma frase

**Um sistema que, a partir dos documentos que uma contraparte envia, extrai as entidades e pessoas, cruza cada uma com fontes públicas e oficiais, e produz um relatório de risco com fonte citada — para um humano nomeado decidir se confia.** Detecta e expõe; nunca aprova, nunca facilita, nunca transaciona.

## 2. Por que faz sentido (e por que agora)

- **Categoria real:** KYB/EDD (Know Your Business / Enhanced Due Diligence) é um mercado estabelecido (Moody's Orbis/Grid, LexisNexis, Dun & Bradstreet, ComplyAdvantage, Sayari). Exigência regulatória no sistema financeiro.
- **O caso que originou é a prova:** os documentos recebidos são um exemplo-livro de fraude prime-bank/PPP. A ferramenta que os teria pego é exatamente esta.
- **Encaixe com a doutrina ABBA:** conformidade-primeiro nativo; mesma espinha do [protótipo patrimonial](../plano-de-construcao.md) (Flow determinístico + gate + citação-ou-abstenção + humano assina). Reaproveita ~80% da arquitetura — muda o corpus (tipologias de fraude + registros públicos em vez de lei tributária) e o gate (indicadores de fraude em vez de red flags patrimoniais).
- **Uso interno imediato:** a própria ABBA passa a verificar contrapartes antes de qualquer parceria — inclusive é o que sustenta a prudência com o próprio contato de domínio.

## 3. Princípios de desenho

Os 5 do protótipo patrimonial + as 4 travas da [fronteira](fronteira-etica-legal.md): conformidade-primeiro · centauro (humano assina) · **risco, nunca aprovação** · determinístico onde é regra (os indicadores de fraude são código) · só fonte pública · LGPD por desenho (dado de caso só no estado do Flow, apagável; nada de dossiê além da finalidade).

## 4. Arquitetura (resumo; detalhe na [especificação](especificacao-verificador.md))

CrewAI 1.x, Flow-first — mesma espinha do patrimonial:

```
intake (upload dos documentos da contraparte)
  → extração determinística de entidades (empresas, pessoas, bancos, e-mails, telefones, IBAN/SWIFT, endereços, registros)
  → GATE de indicadores de fraude (código puro — a tabela do alerta: MT760/RWA/PPP; e-mail gratuito de "bank officer"; "IP/IP"/"CIS"; somas absurdas; country-code divergente; entidades ligadas por e-mail/telefone/endereço; formato SWIFT/BIC inválido)
  → crew de verificação (agentes + tools de fonte PÚBLICA: registro empresarial · sanções OFAC/UE/ONU · diretório SWIFT · WHOIS · mídia adversa) — cada achado com fonte
  → análise de vínculos (entidades "independentes" que se cruzam)
  → relatório de RISCO (não "aprovado") com nível, cada afirmação citada, e o que NÃO foi possível verificar
  → gate humano (advogado/analista assina)
```

## 5. Fases (mesma cadência do patrimonial; construção só com métrica combinada antes)

| Sprint | Entrega | Saída |
|---|---|---|
| **S1** | Extração de entidades de PDF + gate de indicadores de fraude (código, testável sem LLM) | Gate pega os 2 documentos-exemplo como alto risco |
| **S2** | Tools de fonte pública (registro, sanções, SWIFT, WHOIS) + crew de verificação | Relatório com fonte para 10 casos de teste |
| **S3** | Análise de vínculos + relatório final + gate humano | Um caso ponta a ponta |
| **S4** | Golden set (documentos de fraude conhecidos + contrapartes legítimas) + métrica de GO/NO-GO | Assinado por especialista |

## 6. Métrica de GO/NO-GO (combinada antes)

100% de captura dos indicadores duros nos documentos-fraude do golden set (eliminatório) · zero "aprovado" emitido (eliminatório — a ferramenta só dá risco/inconclusivo) · zero citação órfã · abstenção correta onde a fonte não cobre (o rigor do relatório de pesquisa: "confirmado por regulador" ≠ "sem fonte que valide") · custo por verificação ≤ teto.

## 7. Riscos e mitigações

| Risco | Mitigação |
|---|---|
| Virar carimbo de credibilidade | Trava 2 (nunca "aprovado") + teste de finalidade da [fronteira](fronteira-etica-legal.md) |
| Falso positivo difamando empresa real (ex.: WAFUNIF é real) | Distinção obrigatória "confirmado" vs "sem fonte que valide"; linguagem "invocação indevida de nome", não "X é fraude" |
| Uso para dossiê indevido de pessoas | LGPD por desenho: só finalidade de prevenção à fraude, dado apagável, sem dado sensível fora da hipótese |
| Fontes bloqueadas/pagas (PEP não tem base oficial única) | Declarar alcance e lacunas no relatório; PEP como camada assumidamente parcial |
| Facilitar sem querer | Trava 1 + gate humano; ABBA nunca na transação |

## 8. Relação com o resto

- Protótipo de degrau 2, ativo próprio da ABBA. Decisão "produto vs. empresa" só depois do GO, com número.
- **Não altera a postura com o contato de domínio:** parceria segue pausada (registro 2026-08-12); a ferramenta é, inclusive, o teste — apontada aos documentos que ele enviou, a reação dele ao veredito é dado.
- Reaproveita a arquitetura e o scaffold do [protótipo patrimonial](../plano-de-construcao.md).

## Ligações

[Alerta de indicadores](alerta-indicadores-fraude.md) · [Fronteira ética e legal](fronteira-etica-legal.md) · [Especificação](especificacao-verificador.md) · [Protótipo patrimonial](../plano-de-construcao.md) · [Registro de decisões](../../registro-de-decisoes.md)
