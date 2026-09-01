# Playbook do Vault: a operação do volante ABBA

> **Para que serve:** o vault (assessment-brain) guarda padrões anonimizados de todos os engajamentos. Cada encerramento alimenta; cada proposta nova colhe. Este playbook é a sequência exata a executar: sem ela, o volante é só discurso. Decisão E3 ([análise estratégica](analise-estrategica-2026-07.md)); regra bloqueante no [estágio 11](../02-jornada-do-cliente/11-renovacao-e-encerramento.md).

## A taxonomia: técnico × negócio

A ferramenta classifica padrões em 9 tipos técnicos. No encerramento, os **mínimos 3 padrões** cobrem as 3 categorias de negócio:

| Categoria de negócio (mín. 1 de cada) | Tipos técnicos correspondentes |
|---|---|
| **O que funcionou** | `intervention` · `ai_intervention` · `finding` (confirmado) |
| **O que travou** | `negative` · `risk` · `gap` · `contradiction` · `immune_system` |
| **Benchmark setorial** | `financial_leak` · `finding` (com número comparável) |

Regra de ouro da anonimização: o padrão descreve **o fenômeno, nunca o cliente** (a ferramenta faz dupla passada de anonimização, mas a primeira barreira é como os sócios escrevem o feedback).

## Sequência de comandos no encerramento (chapéu Entrega, ~30 min)

```bash
# 1. Feedback do engajamento (aceita/rejeita findings; ao final, extrair padrões: y)
abba feedback <engagement>

# 2. Outcome por intervenção construída (o que aconteceu de verdade)
abba outcome <engagement> --intervention "<título>" --status shipped|partial|rejected \
  --recovered <valor> --months-to-value <n> --spec-accuracy built|partial|unbuildable

# 3. Conferir o resultado: os números que a proposta vai citar
abba vault --stats            # leitura humana
abba vault --stats --json     # saída para planilha/proposta
```

O ciclo fecha sozinho: os outcomes reconciliam a confiança empírica de cada padrão (padrões que a realidade desmentiu param de ser usados como prior: piso 0,25). Por isso o passo 2 **não é opcional**: sem outcome, o vault acredita em tudo que extraiu.

## Como preencher {{N_PADROES_SETOR}} na proposta

1. `abba vault --stats` → linha do setor: `legal-services: 7 patterns from 3 engagement(s) (avg confidence 0.84, empirical 0.71)`
2. **N = o número de patterns do setor:** usar APENAS se ≥ 3 e vindo do comando (nunca de memória, nunca inflado). Atenção: o "from M engagement(s)" da saída conta engajamentos do setor NA BASE, não necessariamente todos alimentaram o vault: em material de cliente, citar só o N de padrões
3. A frase padrão (plantada na [proposta](../03-comercial/proposta-avaliacao-prontidao.md) e na [coreografia](../03-comercial/coreografia-da-conversao.md)): *"nosso método já acumulou N padrões validados no seu setor"*
4. Atenção à normalização: "Legal Services" e "legal-services" são o mesmo setor para a ferramenta; setores de cliente devem ser cadastrados com nome consistente ({{setor em inglês padronizado: convenção da ferramenta}})

## Métricas do volante (item 7 da [reunião semanal](comunicacao.md))

| Métrica | Fonte | Meta |
|---|---|---|
| Padrões novos na semana | `abba vault --stats` (delta) | > 0 em semana com encerramento |
| Padrões por setor-alvo | idem, linha do setor | ≥ 3 antes da 2ª proposta no setor |
| Confiança empírica média do setor | idem | acompanhar: queda = revisar o que extraímos |
| Outcomes registrados vs. intervenções entregues | `abba outcome` | 100% |

## O que NUNCA fazer

- Citar N que não veio do comando (quebra a honestidade que sustenta a frase)
- Escrever feedback com nome/dado identificável do cliente (a anonimização automática é a 2ª barreira, não a 1ª)
- Encerrar engajamento sem os 3 padrões (o [estágio 11](../02-jornada-do-cliente/11-renovacao-e-encerramento.md) trava)
- Pular o `abba outcome`: vault sem outcome é opinião acumulada, não conhecimento validado
