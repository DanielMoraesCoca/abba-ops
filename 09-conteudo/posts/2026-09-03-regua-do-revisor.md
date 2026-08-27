# A ferramenta que reprova os nossos próprios materiais

| | |
|---|---|
| **Pilar** | P2 — O Bastidor |
| **Molde** | [F4 · O Bastidor](../formatos.md#f4--o-bastidor) — screencast, sem rosto |
| **Canal** | LinkedIn — perfil do sócio (vídeo 50s + texto) |
| **Quando** | Quinta, 03/09/2026, 9h30 |
| **Cabeça-alvo** | O cético técnico e o guardião (jurídico/DPO/controladoria) |
| **Fonte** | [Régua do revisor](../../06-ferramentas/regua-do-revisor.md) |
| **Aprovado por** | ⬜ |
| **Publicado em** | |

---

## Texto (copiar a partir daqui)

Antes de qualquer material nosso sair, ele passa por uma ferramenta cujo trabalho é tentar reprová-lo.

No vídeo, um comando de terminal rodando contra um documento real.

Ela se chama régua do revisor. É um conjunto de regras que roda contra tudo que vai para fora — proposta, relatório, apresentação, e-mail, post. Inclusive este.

Ela não é inteligente, e isso é de propósito. É determinística: mesma entrada, mesma saída, custo zero por execução. Não é um modelo opinando sobre o texto; é uma trava conferindo fatos.

O que ela bloqueia:

— número que não está na nossa base de evidências
— preço diferente da tabela vigente
— promessa que a nossa infraestrutura ainda não sustenta
— qualquer frase que sugira que a IA decide alguma coisa sozinha

Achado de bloqueio significa que o material não sai. Existe uma opção de forçar. Usá-la é uma decisão com nome, e o nome vai para o registro.

O que ela não faz: dizer se o texto é bom. Isso continua sendo trabalho de gente, e vai continuar sendo.

Construímos isso porque a coisa mais cara de perder num negócio de consultoria não é um contrato — é a credibilidade técnica, que não se recompra. E credibilidade não sobrevive a "a gente confere na hora de mandar".

A pergunta honesta: o que impede, hoje, um número inventado de sair da sua empresa dentro de uma proposta assinada?

---

## Especificação do vídeo (50 segundos, screencast, sem rosto)

Gravação de tela com QuickTime/OBS. **Sem voz** — texto queimado e trilha
discreta. Exportar em 1080×1080 (quadrado ocupa mais altura no feed) e também
9:16 para reel.

| Tempo | O que aparece na tela | Texto sobreposto |
|---|---|---|
| 0–5s | Terminal limpo | "Toda peça nossa passa por isto antes de sair" |
| 5–12s | Digitar o comando de revisão e dar enter | — |
| 12–28s | A saída rolando, com pelo menos **um achado de bloqueio visível** | "Bloqueio = o material não sai" |
| 28–38s | Abrir o documento e corrigir a linha flagrada | "A correção, não a justificativa" |
| 38–46s | Rodar de novo, passando limpo | "Agora sai" |
| 46–50s | Tela final navy com o logo | "Determinística. Custo zero. Roda em post também." |

**Inegociável:** mostrar um bloqueio de verdade, não um passe limpo encenado.
Screencast maquiado é a versão em vídeo do número inflado — e num post sobre
integridade, seria a pior peça possível.

**Se o módulo de revisão não estiver no checkout** ([pendência conhecida](../../06-ferramentas/regua-do-revisor.md)):
gravar o arquivo de regras sendo lido e uma busca do termo bloqueado dentro do
documento. Menos elegante, igualmente verdadeiro. **Nunca simular uma saída de
terminal que não aconteceu.**

## Primeiro comentário

> A régua é um arquivo de regras versionado junto com a doutrina que ela protege — regra nova só entra com o motivo e o link do documento que a origina. É a mesma ideia de um teste automatizado, aplicada a material comercial em vez de código.

## Notas de operação

- Este post fala com o cético técnico, que é a cabeça mais difícil de todas e a
  que mais derruba proposta por dentro. Comentário técnico aqui vale mais que
  dez curtidas.
- **Pergunta provável:** "por que não usar um modelo para revisar?" Resposta
  pronta: *"a gente usa, mas como segunda camada e nunca como bloqueio — a
  pesquisa de 2026 mostra que modelo-juiz pega bem menos de um quarto dos
  defeitos sistemáticos. O que bloqueia é determinístico; o modelo aponta
  contradição e um sócio decide."*
