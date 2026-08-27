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
| preço divergente da tabela v2 (45k·26k/65k·15k/35k·6k/9,5k/15k·12k/7,5k·260k · portas 14k/24k/42k — construção via calculadora, sem valor único; **28k e 185k da v1 bloqueiam**) | block | V3t — tabela v2 por serviço |
| "5 papéis" | block | parecer do conselho, melhoria nº 1 |
| SSO prometido | block | R3 — autenticação interina |
| "a IA decide"/"IA autônoma" | block | centauro inegociável |
| "presente em todos os lugares"/"ouve tudo"/"monitora o time" | block | 8 recusas do Assento |
| prever regime/futuro | block | recusa 8 do manifesto |
| "primeiro café" (a forma aprovada é "da primeira conversa") | block | V3n — veto do sócio |
| **"95% dos pilotos/projetos falham" · "GenAI Divide" · "MIT NANDA"** (substituto: RAND >80%) | block | V4a — [base de evidências](../00-identidade/base-de-evidencias.md), índice proibido |
| **"parceiro externo dobra o acerto" · "67% vs 33%"** (substituto: RAND+METR+DORA) | block | V4a — mesmo relatório MIT aposentado |
| **"ROI de 3x a 8x" · "payback 5,1 meses" · "73% preferem" · "90% falham em treinamento"** (substituto: payback com número DO cliente) | block | V4a — folclore de vendor sem fonte primária |
| **travessão** (— ou –) em qualquer material que sai | block | v1.5.0 — V3v + V4a-b; vírgula, dois-pontos ou ponto |
| **proporção por extenso** ("nove de cada dez", "um em cada cinco") | warn | v1.4.0 — proporção é estatística; confira cânone + fonte na frase |
| **porcentagem banida por extenso** ("noventa e cinco por cento dos pilotos falham") | block | v1.4.0 — índice proibido, agora também em letra |
| "benchmark" (conferir tempo verbal) · "acurácia" (fora da recusa) | warn | ecossistema §3 · manifesto |
| "firma nova" (é doutrina de conversa, não texto de material) | warn | V3o — padrão editorial |
| "25 dimensões" (ok em proposta/contrato/entrega; não em material de envio) | warn | V3l — [padrão editorial §0](../08-materiais/README.md) |

**Exceções embutidas no motor:** frase proibida **citada entre aspas em tabela** (as tabelas "o que nunca dizemos") não flagra; contexto de **rascunho/âncora/anualização** não flagra preço; valor **sancionado da tabela** nunca flagra.

## Como a régua evolui

1. Doutrina nova (decisão V-registrada) que proíba ou trave algo → regra nova no JSON, com `reason` e `doc` apontando o documento.
2. Falso positivo em material que sai → ajustar `unless`/exceção **no mesmo commit** que o registra.
3. A versão (`version`) sobe a cada mudança; o episódio `revisor.reviewed` grava com qual versão o material foi conferido.

**v1.5.0 (2026-08-27)** — regra `travessao` (block). O sócio já tinha mandado
tirar os travessões dos enviáveis em 11/08 (V3v), mas **aquela decisão nunca foi
registrada**, então não valia para material novo e o social nasceu cheio deles.
Registrada retroativamente como V3v e estendida a todo material externo como
V4a-b. Substituto: vírgula, dois-pontos ou ponto; em lista, ponto médio.

**v1.4.0 (2026-08-27)** — duas regras novas contra número **por extenso**, que
burlava todos os padrões numéricos existentes: `proporcao-por-extenso` (warn —
"nove de cada dez" é 90%; não bloqueia porque o cânone tem proporção
sancionada, "1 em 20 empresas" da BCG, então quem confere é o humano) e
`porcentagem-por-extenso-banida` (block — "noventa e cinco por cento dos
pilotos falham" e afins). **Origem:** um card publicado no Instagram da ABBA em
agosto/2026 abria com *"nove de cada dez empresas que adotaram IA não vão
mostrar um número no fim"* — número sem fonte, numericamente colado no "90% das
organizações falham em treinamento" que o índice proibido bane. Passou por
`mit-95`, `roi-magico` e todo o resto porque nenhum deles olhava letra. A régua
só protege o que ela sabe ler.

**v1.3.0 (2026-08-23)** — três regras novas do índice proibido da [base de evidências](../00-identidade/base-de-evidencias.md) (V4a): `mit-95`, `parceiro-dobra-acerto`, `roi-magico`. Todos os números do MIT NANDA e o folclore de vendor agora bloqueiam; a exceção `unless` (aposentad/banid/proibid/❌) deixa a própria base e as notas de correção citarem os números banidos sem flagrar. Padrões estreitos de propósito — "0,95" de confiança e "95% de cobertura" não disparam. **Pendência:** sincronizar a cópia embarcada no assessment-brain quando o módulo revisor estiver no checkout (não existe em `src/` hoje).

**v1.2.1 (2026-08-10)** — falso positivo corrigido: a negação `não somos auditoria` — que é a própria doutrina sendo afirmada — bloqueava. A exceção exige a negação **colada** ao termo (`não\s+somos\s+(a\s+)?auditor`), para que "não somos apenas X, somos auditoria" continue bloqueando.

## Ligações

[Posicionamento](../00-identidade/posicionamento.md) · [Manifesto](../00-identidade/manifesto.md) · [Tabela de preços](../03-comercial/tabela-de-precos.md) · [Registro de riscos](../05-interno/registro-de-riscos.md) · [Runbook da instância ABBA](../05-interno/abba-interna-runbook.md) — onde o Revisor vira rotina
