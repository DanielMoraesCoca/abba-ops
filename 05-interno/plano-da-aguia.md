# Plano da Águia — da visão auditada à casa vista por inteiro

> **Camada:** interno / execução. Este é o plano que transforma a [Visão da Águia](../00-identidade/visao-da-aguia.md) em realidade completa — fase a fase, cada uma com portão de entrada, dono e critério de "pronto". Ele existe porque a visão já foi escrita (2026-08-31) e já foi **auditada contra o código** (2026-09-01): sabemos exatamente o que a águia já enxerga e o que ainda falta. Este documento sequencia o que falta.
>
> Dono: Sócios (decisões) · Claude (construção). Muda com decisão registrada no [log](registro-de-decisoes.md).

---

## A tese do plano

**A águia já tem os olhos. O que ela ainda não fez foi voar.**

A auditoria de 2026-09-01 confirmou que quase toda a metáfora já é produto: quem está na casa (D06, D18), como funciona na prática (D02, D13, loops), a rotina (D17, D20), o que entra e sai (D04, D12, vazamentos, receita), o que o dono não vê (motor de contradições, agora bilíngue), as relações entre pessoas (fronteiras entre níveis), a casa como organismo. E a mesma auditoria provou o método do plano: a afirmação mais central era a menos testada no idioma do mercado, e só a MEDIÇÃO revelou isso.

Por isso a ordem das fases não é negociável e cada uma é portão da seguinte:

```
VOAR  →  CALIBRAR  →  DESENHAR  →  MORAR  →  APROFUNDAR
(1º run    (julgar os     (o Mapa       (o Conselheiro   (raio-x
 real)      pendentes      da Casa)      no poleiro)      operacional)
            com luz real)
```

Desenhar a casa antes de voar seria desenhar sobre dados de mock (entidades placeholder). Aprofundar antes de morar seria ler ERP de um cliente que ainda não confia. Cada fase gera a evidência que a próxima precisa.

---

## Fase 0 — O primeiro voo (portão de TUDO)

**O que é:** o primeiro run com chave real, ponta a ponta, seguindo o [runbook do primeiro run real](../06-ferramentas/runbook-primeiro-run-real.md) à risca — incluindo a **regra zero: o primeiro run real NÃO é um cliente pagante.**

**Por que é o portão:** nenhum modelo jamais leu uma empresa real por este pipeline. Tudo o que está travado em teste (704 testes verdes nos 2 modos) prova que a máquina não regride — não prova que o raio-x enxerga. A prova é o voo.

**O que sai dele:**
- A linha de base real do eval (hoje só existe a de mock).
- O veredito do `abba validate` — e **vermelho no dia 1 é o sistema funcionando**: `roi.reconciled` e `recommender.coverage` estão declarados no registro (`abba pending`) como portões que DEVEM bloquear no primeiro run.
- As leituras que só a luz real dá: taxas de truncamento por propósito, custo real por dimensão, comportamento do retry de 429.

**Custo e prazo:** ~1 tarde, US$ 10–30 de API. Dono: Daniel (chave + empresa-cobaia) com o runbook aberto.

**Critério de pronto:** run completo, `abba validate` executado, checklist humano respondido ("você assinaria seu nome embaixo disso?"), leituras registradas.

## Fase 1 — Calibração com luz real

**O que é:** julgar, um a um, os itens do registro de pendências (`abba pending`), na ordem da Etapa 5 do runbook. Cada item já carrega o `judge` — o critério de decisão — escrito em código:

1. **A cerca de fontes** (mudou 6 prompts e está LIGADA — o item que um registro mais esquece): revalidar com `npm run eval` real.
2. **Cache de prompt** (economia de ~25x no corpus): ligar só depois do eval real, porque ligar é mudança de prompt.
3. **Espinha loop-native** ("como a casa decide" vira a unidade do plano — o aprofundamento nº 1 da tabela da águia): rodar o check do runbook, comparar com a espinha provada, decidir.
4. **Prioridades de receita por setor**: ratificação Daniel + Pedro (`abba archetypes --revenue`), e só então ligar.
5. **Leituras dos simuladores** (`abba rank whatif` integração e prêmio): com números reais, decidir se o débito de integração vira cobrança por build e se o peso do prêmio muda.

**Critério de pronto:** cada item do `abba pending` com veredito registrado (ligado, adiado com razão, ou descartado). Nenhum "ligar porque parece bom" — só com a medição da Fase 0 na mão.

## Fase 2 — O Mapa da Casa (a página que É a metáfora)

**O que é:** o aprofundamento que falta construir — hoje a ferramenta DETECTA as peças mas não DESENHA a casa. Uma página única, navegável, no padrão do anexo visual (HTML autocontido + SVG inline, zero dependência externa):

- **Andares** = os níveis hierárquicos ouvidos (conselho → diretoria → chefias → linha de frente).
- **Cômodos** = as entidades e áreas do mapa de entidades.
- **Setas** = os fluxos reais de informação e material (D12 + loops de decisão): por onde o dado REALMENTE viaja — planilha, WhatsApp, memória.
- **Marcas vermelhas** = os vazamentos, no cômodo onde sangram, com o valor na moeda do engajamento.
- **Calor nas fronteiras** = a densidade de contradições por par de níveis (a agregação que a auditoria construiu) — onde a informação quebra entre andares.
- **Porta de entrada e saída** = receita que poderia entrar e não entra; dinheiro que sai pelo ralo.

**Por que dá para construir sem risco:** todo dado já está no banco ao fim de um run. Zero chamada de LLM, zero mudança de prompt, renderizador determinístico — a mesma classe de construção do anexo visual e da agregação de fronteiras. A doutrina viaja junto: fronteiras nomeadas como processo, nunca dossiê de pessoa.

**Por que está gateada na Fase 0:** desenhada sobre mock, a página nasceria bonita e mentirosa (entidades placeholder, fluxos inventados). O primeiro desenho deve ser da primeira casa real — é também o teste de que o desenho serve.

**Critério de pronto:** o mapa renderiza do run real da Fase 0, um consultor olha e reconhece a empresa, e a página entra no relatório do consultor (client-facing só depois de decisão registrada).

## Fase 3 — A águia que fica (o Conselheiro no poleiro)

**O que é:** ativar o cérebro por cliente no primeiro cliente em manutenção — o gatilho já registrado desde julho, aqui reafirmado na linguagem da águia: **a visão de hoje não pode virar retrato amarelado em seis meses.** Fatos com validade no tempo, decisões com resultado medido, o brief que se atualiza, o ciclo noturno com teto de gasto. Tudo construído e travado por teste; falta o cliente.

**Critério de pronto:** primeiro contrato de manutenção assinado → [runbook de ativação](../06-ferramentas/runbook-ativacao.md) executado → primeiro brief mensal aprovado por humano nomeado.

## Fase 4 — O raio-x operacional (Aposta 7)

**O que é:** ler o escapamento operacional direto (extratos de ERP, logs de processo) em vez de só documentos e entrevistas. A fronteira real da profundidade — e a mais delicada. Fica exatamente como registrada em [apostas futuras](../00-identidade/apostas-futuras.md) (aposta 7): gatilhos e salvaguardas definidos, **nenhuma construção antes dos gatilhos**, e a regra da águia mantida — fluxos e processos, agregados e nomeáveis; **a águia sobrevoa, não instala câmera no quarto.**

---

## O que fica FORA do plano, e por quê (decisões já dormidas)

- **Anonimizar relatório real** — recusado (2026-08-28): setor + faixa + vazamento reidentifica; a peça de prospect é a demo fictícia.
- **Converter moeda** — recusado (2026-08-30): rótulo, nunca conversão; converter inventa taxa e data.
- **Dossiê de pessoa** — recusado por doutrina (a fronteira da águia): eficácia, LGPD, adoção.
- **Dashboard web multiusuário** — espera enquanto a operação é local; o item aberto (login real) está registrado.
- **Verticalizar por setor** — decidido (2026-08-01): o eixo é forma, não indústria.

## Decisões que o plano precisa dos sócios

| Decisão | Fase | Quem |
|---|---|---|
| Empresa-cobaia do primeiro voo (a própria ABBA, a Brasal da degustação, ou parceiro que tope) | 0 | Daniel |
| Ratificar prioridades de receita por setor | 1 | Daniel + Pedro |
| Espinha loop-native: ligar ou manter | 1 | Sócios, com a leitura do check |
| Mapa da Casa: consultor-only ou client-facing | 2 | Sócios |
| Gatilhos da Aposta 7 (revisar quando a Fase 3 estiver viva) | 4 | Sócios |

## Regras de execução (as mesmas que trouxeram até aqui)

1. **Nenhuma mudança silenciosa no ranking.** Simulador antes de doutrina; breakeven antes de peso.
2. **Toda trava é provada por sabotagem.** Um teste que não falha quando o comportamento é removido não é trava.
3. **Medir em vez de acreditar.** Todo defeito client-facing desta casa foi achado LENDO um artefato inteiro, nunca por teste. A auditoria da águia achou o raio-x cego em português do mesmo jeito.
4. **A IP é travada.** `prompts.js` e `framework.js` não mudam sem re-validação com evidência; mudança de prompt espera a linha de base real.
5. **Nada é apagado.** Supersessão, aposentadoria com razão, tombstone — nunca delete.

---

## Referências

- [A Visão da Águia](../00-identidade/visao-da-aguia.md) — o porquê de tudo isto
- [Runbook do primeiro run real](../06-ferramentas/runbook-primeiro-run-real.md) — a Fase 0, passo a passo
- [Apostas futuras](../00-identidade/apostas-futuras.md) — aposta 7 (Fase 4)
- [Registro de decisões](registro-de-decisoes.md) · [Caminho Crítico](plano-de-acao.md) — este plano é a trilha "ferramenta"; o Caminho Crítico segue sendo a trilha "negócio"
