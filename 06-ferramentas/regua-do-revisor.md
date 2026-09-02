# A Régua do Revisor: a doutrina que confere sozinha

> **Camada:** ferramenta. Origem: Conselheiro Vertical (decisão do sócio, 2026-08-04, V3g). O Revisor é a voz interna do Conselheiro sobre os NOSSOS entregáveis: antes de um material sair, ele confere contra esta régua: determinística, com custo zero: e, opcionalmente, contra a memória do engajamento (pass de LLM, consultivo).
>
> **Fonte da verdade:** este `.md` explica; o [`regua-do-revisor.json`](regua-do-revisor.json) ao lado é a régua executável. **Ao mudar doutrina aqui, sincronizar o JSON e a cópia embarcada** em `assessment-brain/src/revisor/regua.json` (o motor lê a cópia; `ABBA_REVISOR_RULES` aponta para outra).
>
> **Escopo: material que SAI.** Propostas, relatórios, kit, deck, e-mails, posts. Docs internos de estratégia citam temas gateados por natureza (curva de tenure na visão, rascunho v2 na precificação) e disparam bloqueios esperados, não são o alvo.

## Como usar

```bash
abba revise <arquivo.md>                       # gate determinístico (custo zero)
abba revise <arquivo> --engagement <eng>       # + grava o episódio revisor.reviewed
abba revise <arquivo> --engagement <eng> --llm # + coerência com a memória (pago, consultivo)
abba report <eng> --revise                     # o relatório só grava se passar
```

**Regra de bloqueio:** achado `block` = o material não sai (exit 1; `--force` existe, e usar `--force` é uma decisão com nome). Achado `warn` = humano confere o tempo verbal/contexto. **O pass de LLM nunca bloqueia sozinho**: pesquisa de 2026 mostra que LLM-juiz pega bem menos de um quarto dos defeitos sistemáticos; ele aponta contradições ("isto contradiz a decisão X de março") e um sócio decide.

## As regras (resumo humano: o JSON é o executável)

| Regra | Severidade | Doutrina |
|---|---|---|
| "garantia" (substantivo, fora de "garantimos o método") | block | E6 não ativada |
| "24/7" (fora de "monitoramento 24/7") | block | P9 · SLA honesto |
| "somos a auditoria"/"auditamos" (analogia "funciona como" pode) | block | V3c · a prateleira |
| "certificado/validado em clientes reais" | block | R1 · só sintético |
| "curva de tenure" | block | gateada + anglicismo |
| preço divergente da tabela v3 (Programa 218k/278k/378k · entrada 26k · trimestres 48k/63k/88k · Assinatura 11k/15k/21k/mês · Conselheiro 12k/7,5k + memória 15k · standalone 45k · mini-ciclo 42k) | block | **V5 · tabela v3, um produto só (proposta; Pedro valida)** |
| **oferta aposentada apresentada com preço** (workshop, sprint LGPD, pacote de 3, jornada completa, avaliação de prontidão, treinamento híbrido, camadas vendidas separadas) | block | V5 · o cardápio dos 7 serviços foi descontinuado; contexto histórico/arquivado não flagra |
| "5 papéis" | block | parecer do conselho, melhoria nº 1 |
| SSO prometido | block | R3 · autenticação interina |
| "a IA decide"/"IA autônoma" | block | centauro inegociável |
| "presente em todos os lugares"/"ouve tudo"/"monitora o time" | block | 8 recusas do Assento |
| prever regime/futuro | block | recusa 8 do manifesto |
| "primeiro café" (a forma aprovada é "da primeira conversa") | block | V3n · veto do sócio |
| **"95% dos pilotos/projetos falham" · "GenAI Divide" · "MIT NANDA"** (substituto: RAND >80%) | block | V4a · [base de evidências](../00-identidade/base-de-evidencias.md), índice proibido |
| **"parceiro externo dobra o acerto" · "67% vs 33%"** (substituto: RAND+METR+DORA) | block | V4a · mesmo relatório MIT aposentado |
| **"ROI de 3x a 8x" · "payback 5,1 meses" · "73% preferem" · "90% falham em treinamento"** (substituto: payback com número DO cliente) | block | V4a · folclore de vendor sem fonte primária |
| "benchmark" (conferir tempo verbal) · "acurácia" (fora da recusa) | warn | ecossistema §3 · manifesto |
| "firma nova" (é doutrina de conversa, não texto de material) | warn | V3o · padrão editorial |
| "25 dimensões" (ok em proposta/contrato/entrega; não em material de envio) | warn | V3l · [padrão editorial §0](../08-materiais/README.md) |

**Exceções embutidas no motor:** frase proibida **citada entre aspas em tabela** (as tabelas "o que nunca dizemos") não flagra; contexto de **rascunho/âncora/anualização** não flagra preço; valor **sancionado da tabela** nunca flagra.

## Como a régua evolui

1. Doutrina nova (decisão V-registrada) que proíba ou trave algo → regra nova no JSON, com `reason` e `doc` apontando o documento.
2. Falso positivo em material que sai → ajustar `unless`/exceção **no mesmo commit** que o registra.
3. A versão (`version`) sobe a cada mudança; o episódio `revisor.reviewed` grava com qual versão o material foi conferido.

**v2.0.0 (2026-08-31)**: a Virada V5: a regra `precos-travados` inteira reescrita para a tabela v3 (3 caminhos: Mapa grátis · Programa "AI Native · Ano 1" por porte · Conselheiro; + Assinatura da Capacidade ano 2+). Regra nova `ofertas-aposentadas-v5` (block): oferta do modelo dos 7 serviços apresentada com preço bloqueia: exceções para contexto histórico/arquivado/nota de correção. **Major version porque inverte o sancionado: os preços v2 deixam de passar.** Pendência: sincronizar a cópia embarcada no assessment-brain (`ABBA_REVISOR_RULES` aponta para este JSON como ponte até lá).

**v1.3.0 (2026-08-23)**: três regras novas do índice proibido da [base de evidências](../00-identidade/base-de-evidencias.md) (V4a): `mit-95`, `parceiro-dobra-acerto`, `roi-magico`. Todos os números do MIT NANDA e o folclore de vendor agora bloqueiam; a exceção `unless` (aposentad/banid/proibid/❌) deixa a própria base e as notas de correção citarem os números banidos sem flagrar. Padrões estreitos de propósito. "0,95" de confiança e "95% de cobertura" não disparam. **Pendência:** sincronizar a cópia embarcada no assessment-brain quando o módulo revisor estiver no checkout (não existe em `src/` hoje).

**v1.2.1 (2026-08-10)**: falso positivo corrigido: a negação `não somos auditoria`: que é a própria doutrina sendo afirmada: bloqueava. A exceção exige a negação **colada** ao termo (`não\s+somos\s+(a\s+)?auditor`), para que "não somos apenas X, somos auditoria" continue bloqueando.

## Ligações

[Posicionamento](../00-identidade/posicionamento.md) · [Manifesto](../00-identidade/manifesto.md) · [Tabela de preços](../03-comercial/tabela-de-precos.md) · [Registro de riscos](../05-interno/registro-de-riscos.md) · [Runbook da instância ABBA](../05-interno/abba-interna-runbook.md): onde o Revisor vira rotina
