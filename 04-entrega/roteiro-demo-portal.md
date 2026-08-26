# Roteiro de demo do portal — ~20 minutos, na ordem da venda

> **Para que serve:** conduzir a demonstração ao vivo do portal numa
> reunião comercial (primeiro uso: Brasal, semana de 24/08/2026).
> Substitui o roteiro de abril (`_PHASE1_DEMO_SCRIPT.md` do abba-portal),
> que descrevia outro produto — em inglês, com blocos e níveis que não
> existem mais. As falas de mesa são as de
> [falas-treinamento](../03-comercial/falas-treinamento.md); aqui é o
> percurso de telas que as prova. **Regra do roteiro: cada tela existe
> para provar UMA fala. Se a fala já pousou, avance.**

## Antes de abrir a sala (checklist, na véspera)

- [ ] `npm run turma:preflight` no ambiente da demo → 0 bloqueadores
      (audita o DADO: currículo, migrações, segredos, provedor de e-mail)
- [ ] **`npm run demo:rehearsal`** no ambiente da demo → 0 quebras
      (audita a TELA: abre as 17 telas deste roteiro num navegador de
      verdade e acusa crash, inglês na cara do aluno, elemento da fala
      que não apareceu. Contra o ambiente real:
      `npm run demo:rehearsal -- --base-url=https://… --cookie="<abba_session da persona>"`
      — o cookie sai do navegador depois de entrar como ela. As
      capturas ficam em `.demo-rehearsal/`: dá para conferir cada
      tela sem reabrir o portal)
- [ ] Semear a demo: `POST /api/admin/seed-demo-client` (sessão de staff;
      só opera em tenant `demo-*`) — confere que `maria@ridgeline.com`
      abre com progresso rico
- [ ] `/boletim` mostra o número da semana (segunda-feira publica sozinho
      — na semana da reunião o nº 2 está no ar; conferir mesmo assim)
- [ ] `ALLOW_EMAIL_ONLY_SIGNIN=true` no ambiente da demo (entrada por
      e-mail é chave de DEMO; em produção de cliente fica desligada —
      não comentar na mesa, apenas garantir que o login flui)
- [ ] Iris viva: abrir uma aula e mandar um "oi" (chave da API + teto de
      custo diário podem estar esgotados — melhor descobrir na véspera)
- [ ] Navegador: perfil limpo, pt-BR, zoom 110–125%, notificações OFF
- [ ] Abas abertas na ordem dos blocos abaixo; a primeira é `/signin`

### Mapa de contas da demo (tenant demo-ridgeline)

| Conta | Papel | Usar para |
|---|---|---|
| `pedro@ridgeline.com` | participante, Fundação | a jornada do aluno começando (home, aula, desafios) |
| `maria@ridgeline.com` | campeã, Especialista | progresso rico: /me, cadência, ferramentas |
| `carla@ridgeline.com` | gestora | painel do gestor + atestado |
| `helena@ridgeline.com` | patrocinadora | painel de adoção do patrocinador |

Trocar de conta: sair (menu) → `/signin` → e-mail da persona.

## O percurso (8 blocos, ~20 min)

### 0 · Abertura — SEM tela (1 min)

A fala, antes de qualquer clique: *"O que vocês vão ver não é um curso
que acaba — é uma academia que a pessoa frequenta. Todo dia o portal
propõe uma prática de dois a cinco minutos no trabalho real dela. E no
fim, o que a gente assina não é presença: é o relatório de durabilidade
de 90 dias."* (Os três diferenciais — durabilidade, patrocínio do
gestor, credencial verificável — TÊM de ser ditos até o fim da demo;
esta abertura planta o primeiro.)

### 1 · Home do aluno — entrar como Pedro (3 min)

`/signin` → `pedro@ridgeline.com`. Mostrar, nesta ordem:

1. **Prática de Hoje** no topo — *"isto muda todo dia: um erro plausível
   para caçar, um pedido para testar na tarefa de hoje, a pergunta da
   semana. Dois a cinco minutos, no trabalho real."*
2. O CTA **Continuar** — *"o caminho principal continua de onde parou"*.
3. O cartão do **Boletim** — *"toda segunda sai um estudo curto na voz
   da casa. O de hoje entrou no ar sozinho, de manhã"* (é verdade na
   semana da reunião — cadência viva, não promessa).

### 2 · A aula — abrir a Aula 1 da Fundação (4 min)

Pelo Continuar ou pelo catálogo. Mostrar o desenho, não ler o conteúdo:

- Os blocos na sequência: **Gancho → Leitura → Faça Você → Reflexão**.
- No Faça Você, abrir a **Iris** do lado e rodar o pedido da aula.
  *"Ninguém aprende assistindo vídeo — essa frase está na nossa
  apresentação institucional. A aula é um gancho e uma leitura curta;
  o aprendizado acontece AQUI, fazendo na própria tarefa com a guia do
  lado."*
- Na Reflexão, apontar a **Bússola** (as três perguntas). *"Cada aula
  termina com um compromisso if-então. É isso que a gente mede depois
  — não a conclusão da aula."* (segundo plantio da durabilidade)

### 3 · Minhas Ferramentas (2 min) — ⚠️ ver ressalva

`/ferramentas` (como Maria, se quiser exemplos; como Pedro mostra o
estado vazio que ensina o caminho). *"O que a pessoa constrói nas aulas
— o padrão da entrega dela, os pontos de conferência dela, o pedido que
funcionou — fica guardado com o nome dela, editável, pronto para o dia
de trabalho. O método deixa de morar na cabeça."*

**Ressalva operacional:** gravar ferramenta nova depende da migração
`20260823_user_artifacts.sql` aplicada no Supabase do ambiente
([ficha do portal](../06-ferramentas/ferramenta-portal.md)). Sem ela:
mostrar a tela e o botão "Guardar como ferramenta" **sem gravar** — não
prometer como ativo. Com ela aplicada: gravar ao vivo, é o momento mais
forte do bloco.

### 4 · Academia curta — /challenges + um cenário (3 min)

`/challenges`: apontar os três formatos (**drill de caça ao erro**,
**prompt golf**, **cenário de decisão**) e a honestidade da página — o
que conta para subir de nível e o que é prática livre.

Abrir o **cenário da estatística** e jogar as duas primeiras decisões ao
vivo: escolha → consequência → **a leitura da casa**. *"A gente treina
DECISÃO, não decoreba: a pessoa erra aqui dentro, onde errar é barato, e
lê o porquê na hora."*

### 5 · Biblioteca de Pedidos (2 min)

`/biblioteca`: buscar algo do mundo do cliente ("tabela", "e-mail").
*"Quarenta pedidos por área, e TODO cartão termina em conferência — o
que verificar antes de confiar. A gente nunca entrega o atalho sem o
freio."* Se a Prática de Hoje do dia for um pedido, mostrar o deep link
com o cartão do dia destacado.

### 6 · O gestor e o patrocinador — trocar de conta (3 min)

- Como **Carla** (`/manager`): o time dela, o que cada pessoa aplicou,
  o **atestado do gestor**. *"O gestor não assiste: ele corrobora o que
  o time aplicou. É o único diferencial que aparece em todo estudo sério
  de adoção."* (segundo diferencial dito)
- Como **Helena** (`/sponsor`): adoção do programa inteiro. *"É a visão
  que sustenta a conversa de vocês com a diretoria."*

### 7 · Credencial verificável + fecho (2 min)

**Preparo (véspera):** `/verify` SEM token mostra o cartão "não
válida" — emita uma credencial da persona de demo antes
(`/me/credential` → Emitir; a de Fundação exige as 8 aulas concluídas
no seed) e guarde o LINK COMPLETO com `?token=…` num favorito. A
página é pública e em pt-BR (25/08), com o selo "Fundação em IA".

`/verify`: *"A credencial é da pessoa e verifica-se por link — sem
depender de planilha nossa nem da memória de vocês. Vocês já desenharam
o processo certo: licença para quem concluiu. Isto é o critério
auditável que faltava nele."* (terceiro diferencial dito — e encaixa no
funil que o Rafa descreveu em 18/08)

Fecho, sem tela: *"A Turma 1 de vocês é a primeira a ser medida assim:
tamanho combinado antes, linha de base no dia 0, comparação no d90 — e
o relatório de 90 dias é o que a gente assina."*

## Se algo falhar (fallbacks)

| Sintoma | O que fazer na hora |
|---|---|
| Iris não responde (chave/teto de custo) | *"A guia responde em segundos — hoje estamos no ambiente de demonstração"* e seguir para a tela seguinte; NUNCA reenviar três vezes na frente do cliente |
| "Guardar como ferramenta" dá erro | é a ressalva do bloco 3 (migração): mostrar sem gravar e seguir |
| Tela sem dados (seed não rodou) | `/signin?demo=true` entra como a persona semeada padrão; se seguir vazio, pular para o bloco 5 (biblioteca e boletim não dependem de banco) |
| Boletim de número futuro dá 404 | é desenho (agenda não vaza); mostrar a lista, não o link futuro |
| Qualquer tela quebrar | F5 uma vez; se persistir, dizer o que a tela mostra e seguir — o roteiro tem 8 blocos justamente para nenhum ser insubstituível |

## O que NÃO fazer na demo

- Não prometer o que a mesa não decidiu: calendário de vídeo, CrewAI
  além do que o [kit da turma](kit-da-turma.md) registra, trilhas "em
  produção" como se prontas ([falas](../03-comercial/falas-treinamento.md)).
- Não abrir `/admin/*` na frente do cliente (cozinha, não vitrine).
- Não digitar dado real do cliente na Iris durante a demo.
- Não corrigir defeito ao vivo. Anotar e seguir o bloco.

## Histórico

| Versão | Data | Mudança |
|---|---|---|
| v1 | 2026-08-24 | Criado para a reunião da Brasal. Substitui o `_PHASE1_DEMO_SCRIPT.md` (abril, inglês, produto antigo); percurso alinhado ao Currículo v3 (academia diária) e às falas v2 |
| v1.1 | 2026-08-26 | Primeiro ENSAIO real (as 17 telas abertas num navegador, `npm run demo:rehearsal`, agora na véspera): 0 quebras. Dois defeitos consertados antes de virarem cena — a concordância de "credencial" (era masculina na barra lateral de todas as telas) e a home que, sem conseguir ler a escada, afirmava "as aulas estão feitas". Bloco 7 ganhou o preparo do token do /verify |
