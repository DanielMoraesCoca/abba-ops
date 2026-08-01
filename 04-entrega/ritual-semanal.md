# Ritual Semanal — 20 minutos que seguram o cliente

> **Camada:** entrega (processo). O pulso dos degraus **3 e 4** da [escada](../03-comercial/escada-abba.md) (Manutenção e Conselheiro/Estratégia). Decisão dos sócios em 2026-08-01, fundamentada no [estudo de antecipação](../05-interno/estudo-antecipacao.md) §3: contato humano recorrente muda comportamento (meta-análise só de RCTs, g = 0,59); cutucão automatizado não (d = 0,004 corrigido viés). **A ligação é o produto; a IA prepara a pauta.**
>
> Dono: o sócio Conselheiro daquele cliente. **20 minutos, cronometrados.** O relatório mensal e o conselho trimestral continuam — isto é pulso, não substituição.

---

## Quando começa e quando não se aplica

- **Começa** quando o cliente entra no degrau 3 (primeiro mês de manutenção) — nunca antes: sem sistema vivo e sem diário, a semanal vira conversa vazia e mata a percepção de valor.
- **Não se aplica** a Workshop, Avaliação e Sprint LGPD (têm começo, meio e fim).
- **Durante o Programa** (16 semanas) vale a reunião de projeto, que é outra coisa e mais longa. A semanal assume quando o programa termina — e é exatamente a ponte que impede o "acabou, obrigado".

## Preparação (5 min, antes de ligar)

```bash
node bin/abba.js brain next <eng>       # a fila: o que venceu, gatilho, decisão parada, contestado
node bin/abba.js decision list <eng>    # estado do diário
```

A fila é ordenada por prazo. **Escolher no máximo 4 itens** — o que não couber espera ou vira pauta do conselho. Se `brain health` estiver abaixo de 70, resolver a memória antes da ligação, não durante.

## O roteiro — 4 itens fixos, sempre na mesma ordem

| # | Item | Tempo | O que se diz |
|---|---|---|---|
| 1 | **O que venceu** | 5' | *"Três verdades da memória de vocês estão vencendo: o churn ainda é 4%? O prazo do fornecedor mudou?"* — reconfirmar ou corrigir ali (`abba brain fact ... --by`) |
| 2 | **Qual gatilho disparou** | 5' | *"Combinamos revisar se o DSO passasse de 45. Passou?"* — conferência do indicador é humana; se disparou, a revisão entra na agenda com data |
| 3 | **O que decidimos** | 5' | Decisão nova ou destravada → diário na hora, com nome (`abba decision add` / `advance --by`). Decisão parada há 30+ dias → implementar, medir ou abandonar com motivo — **em voz alta** |
| 4 | **O que vamos medir** | 5' | Toda decisão do item 3 sai com métrica, linha de base e data de medição — **antes** de executar ([protocolo de prova](protocolo-de-prova.md) §1) |

## O que NÃO entra (e como cortar sem grosseria)

- **Suporte técnico** → *"isso é chamado de SLA — abro agora e te retorno hoje"* ([SLA](sla-manutencao.md))
- **Escopo novo** → *"quero fazer direito: levo para o conselho / te mando proposta de mini-ciclo"*
- **Estratégia aberta** → é pauta do [conselho](pauta-conselho.md), onde há tempo e a diretoria presente
- Estourou 20 minutos duas semanas seguidas → o formato está errado ou o cliente precisa de outra camada; discutir na reunião de sócios, não esticar em silêncio

## Registro (2 linhas, no máximo)

Na pasta do cliente, após cada ligação: `data · itens tocados · decisões novas (ids) · próximo gatilho`. O diário e os episódios já guardam o resto — o registro é só o índice.

## Custo e capacidade

~20 min de ligação + ~10 min de preparo/registro = **~30 min/sócio/cliente/semana**. Em 6–8 clientes de recorrência: 3–4h/semana por sócio. **É o teto confortável** — acima de 10 clientes de recorrência, ou entra gente ou a cadência cai para quinzenal nos de menor camada (decisão de sócios, não deriva silenciosa).

## Por que isso segura o cliente (a mecânica, para não virar cerimônia)

1. A cada semana o cliente **reconfirma ou corrige a própria memória** — o dossiê fica mais dele, e sair da ABBA passa a significar perder um sistema vivo, não cancelar uma reunião.
2. O item 4 alimenta o [protocolo de prova](protocolo-de-prova.md) — sem a semanal, a métrica "combinada antes" atrasa até virar métrica reconstruída depois, que não vale nada.
3. É a diferença estrutural contra a agência de automação: ela entrega e some; nós aparecemos toda semana com a fila na mão. **O concorrente pode copiar o software; não pode copiar a cadência sem pagar o custo dela.**

## Ligações

[Estudo de antecipação](../05-interno/estudo-antecipacao.md) — a evidência · [Escada](../03-comercial/escada-abba.md) — onde o ritual mora · [Dossiê vivo](dossie-vivo-conselheiro-digital.md) — o ciclo diário do Conselheiro · [Pauta do conselho](pauta-conselho.md) — o ritual maior · [SLA](sla-manutencao.md)
