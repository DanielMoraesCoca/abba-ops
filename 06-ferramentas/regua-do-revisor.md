# A Régua do Revisor — a doutrina que confere sozinha

> **Camada:** ferramenta. Origem: Conselheiro Vertical (decisão do sócio, 2026-08-04, V3g). O Revisor é a voz interna do Conselheiro sobre os NOSSOS entregáveis: antes de um material sair, ele confere contra esta régua — determinística, com custo zero — e, opcionalmente, contra a memória do engajamento (pass de LLM, consultivo).
>
> **Fonte da verdade:** este `.md` explica; o [`regua-do-revisor.json`](regua-do-revisor.json) ao lado é a régua executável. **Ao mudar doutrina aqui, sincronizar o JSON e a cópia embarcada** em `assessment-brain/src/revisor/regua.json` (o motor lê a cópia; `ABBA_REVISOR_RULES` aponta para outra).
>
> **Escopo: material que SAI.** Propostas, relatórios, kit, deck, e-mails, posts. Docs internos de estratégia citam temas gateados por natureza (curva de tenure na visão, rascunho v2 na precificação) e disparam bloqueios esperados — não são o alvo.

## Como usar

```bash
abba revise <arquivo.md>                       # gate determinístico (custo zero)
abba revise <arquivo> --engagement <eng>       # + grava o episódio revisor.reviewed
abba revise <arquivo> --engagement <eng> --llm # + coerência com a memória (pago, consultivo)
abba report <eng> --revise                     # o relatório só grava se passar
```

**Regra de bloqueio:** achado `block` = o material não sai (exit 1; `--force` existe, e usar `--force` é uma decisão com nome). Achado `warn` = humano confere o tempo verbal/contexto. **O pass de LLM nunca bloqueia sozinho** — pesquisa de 2026 mostra que LLM-juiz pega bem menos de um quarto dos defeitos sistemáticos; ele aponta contradições ("isto contradiz a decisão X de março") e um sócio decide.

## As regras (resumo humano — o JSON é o executável)

| Regra | Severidade | Doutrina |
|---|---|---|
| "garantia" (substantivo, fora de "garantimos o método") | block | E6 não ativada |
| "24/7" (fora de "monitoramento 24/7") | block | P9 — SLA honesto |
| "somos a auditoria"/"auditamos" (analogia "funciona como" pode) | block | V3c — a prateleira |
| "certificado/validado em clientes reais" | block | R1 — só sintético |
| "curva de tenure" | block | gateada + anglicismo |
| preço divergente da tabela v1 (14k·28k·24k·185k·9,5k·42k) | block | P1 travada |
| "5 papéis" | block | parecer do conselho, melhoria nº 1 |
| SSO prometido | block | R3 — autenticação interina |
| "a IA decide"/"IA autônoma" | block | centauro inegociável |
| "presente em todos os lugares"/"ouve tudo"/"monitora o time" | block | 8 recusas do Assento |
| prever regime/futuro | block | recusa 8 do manifesto |
| "primeiro café" (a forma aprovada é "da primeira conversa") | block | V3n — veto do sócio |
| "benchmark" (conferir tempo verbal) · "acurácia" (fora da recusa) | warn | ecossistema §3 · manifesto |
| "firma nova" (é doutrina de conversa, não texto de material) | warn | V3o — padrão editorial |
| "25 dimensões" (ok em proposta/contrato/entrega; não em material de envio) | warn | V3l — [padrão editorial §0](../08-materiais/README.md) |

**Exceções embutidas no motor:** frase proibida **citada entre aspas em tabela** (as tabelas "o que nunca dizemos") não flagra; contexto de **rascunho/âncora/anualização** não flagra preço; valor **sancionado da tabela** nunca flagra.

## Como a régua evolui

1. Doutrina nova (decisão V-registrada) que proíba ou trave algo → regra nova no JSON, com `reason` e `doc` apontando o documento.
2. Falso positivo em material que sai → ajustar `unless`/exceção **no mesmo commit** que o registra.
3. A versão (`version`) sobe a cada mudança; o episódio `revisor.reviewed` grava com qual versão o material foi conferido.

## Ligações

[Posicionamento](../00-identidade/posicionamento.md) · [Manifesto](../00-identidade/manifesto.md) · [Tabela de preços](../03-comercial/tabela-de-precos.md) · [Registro de riscos](../05-interno/registro-de-riscos.md) · [Runbook da instância ABBA](../05-interno/abba-interna-runbook.md) — onde o Revisor vira rotina
