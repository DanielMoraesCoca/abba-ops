# Mapa de Entrevistas — Avaliação de Prontidão

Quem ouvir, quantas vezes, por quanto tempo, com que roteiro — e como cada conversa entra na ferramenta. O agendamento é do ponto focal do cliente ([protocolo, Fase 1](protocolo-de-imersao.md)); este mapa é o que entregamos a ele em D-7 para fechar a agenda antes do kickoff.

**O princípio que organiza o mapa:** perguntar a mesma coisa a 3 níveis hierárquicos. Os gaps entre as respostas SÃO o diagnóstico — o detector de contradições da ferramenta compara automaticamente o que o CEO disse com o que a linha de frente vive, e a severidade cresce com a distância hierárquica. Por isso os metadados de ingestão não são burocracia: sem `--level`, a conversa fica fora dessa comparação.

---

## O mapa

| Nível | Quem | Quantas | Duração | Fase da ferramenta | Flag de ingestão |
|---|---|---|---|---|---|
| Conselho / CEO | CEO; presidente do conselho se houver | 1–2 | 60 min | 1 (Surface) | `--level ceo_board --phase 1` |
| C-suite | CFO, COO, CTO/TI, Comercial | 3–4 | 60 min | 1–2 (Surface → Organism) | `--level c_suite --phase 2` |
| Gestores | Donos das áreas no escopo (willing-area primeiro) | 4–6 | 45 min | 2–3 (Organism → Anatomy) | `--level dept_head --phase 2` ou `--phase 3` |
| Linha de frente | Quem executa os processos críticos | 4–8 | 30 min | 3 (Anatomy) | `--level front_line --phase 3` |
| Governança | Jurídico + Compliance + TI, juntos | 1 | 90 min | 3 | `--level dept_head --phase 3` |
| Externos (se aplicável) | Cliente do cliente, parceiro, fornecedor crítico | 0–2 | 30 min | 0 | `--level external --phase 0` |

Total típico: **13 a 21 conversas em 2 semanas** (2–3 por dia; nunca mais de 4 — a qualidade da escuta cai antes da agenda acabar).

**Ordem:** de cima para baixo (CEO → C-suite → gestores → linha de frente). A visão declarada do topo vira hipótese a verificar embaixo — nunca o contrário, para não contaminar a diretoria com achados ainda crus. A sessão de calibração final ([protocolo, wrapper humano](protocolo-de-imersao.md#o-wrapper-humano-o-que-separa-consultoria-de-produto)) fecha o ciclo com `--level consultant --phase 4`.

---

## Roteiro-base por nível

Cada entrevista tem duas metades: as **aberturas fixas** abaixo (sempre as mesmas, para as respostas serem comparáveis entre níveis) e o **guia dirigido por lacunas** que a ferramenta imprime (`abba questions <eng> --phase <n> --output guia.md`) — na primeira rodada ele traz as perguntas-chave do método por dimensão; da segunda rodada em diante, traz o que ficou fraco ou contraditório no que já foi ouvido.

Toda entrevista começa com o aviso de consentimento e gravação ([protocolo, Fase 3](protocolo-de-imersao.md#fase-3--campo-semanas-12)).

### Conselho / CEO (60 min)
1. "Como esta empresa ganha dinheiro, na sua descrição?" (a resposta vira régua para todos os níveis abaixo)
2. "O que precisa ser verdade daqui a 3 anos para você considerar que deu certo?"
3. "Onde a operação te surpreende negativamente com mais frequência?"
4. "O que vocês já tentaram com IA ou automação, e o que aconteceu?"
5. "Que número, em reais, mais te incomoda hoje e já é medido?"
6. + guia da ferramenta (visão, competição, escala, ética)

### C-suite (60 min)
1. "Descreve o caminho de um pedido/cliente do início ao fim, na sua área."
2. "Onde o dado que você usa para decidir nasce, e quanto você confia nele?"
3. "Qual decisão sua demora mais do que deveria, e o que a segura?"
4. "Se a sua equipe dobrasse de produtividade amanhã, o que você faria com a folga?"
5. "O que a linha de frente faz manualmente que você suspeita, mas não tem certeza?"
6. + guia da ferramenta (operações, decisões, pessoas, conhecimento, política)

### Gestores (45 min)
1. "Me mostra como o trabalho de verdade acontece aqui — vale abrir a tela." (o processo real, não o desenhado)
2. "Quais são as 5 tarefas que mais consomem a semana do teu time?"
3. "Onde vocês mantêm planilha paralela ao sistema oficial, e por quê?"
4. "O que quebra quando alguém do time sai de férias?"
5. "Se você pudesse parar de fazer uma coisa amanhã, qual seria?"
6. + guia da ferramenta (exceções, coordenação, dados, cliente)

### Linha de frente (30 min)
1. "Me conta o teu dia de ontem, do primeiro ao último sistema que você abriu."
2. "O que você redigita de um lugar para outro?"
3. "Quando aparece um caso fora do padrão, o que você faz?"
4. "Que ferramenta você usa que o teu chefe talvez não saiba?" (sem tom de auditoria — é onde mora a inovação escondida)
5. "O que você faria com uma hora a mais por dia?"
6. + guia da ferramenta (realidade operacional, confiança, medição)

### Governança (90 min, Jurídico + Compliance + TI juntos)
1. Postura de dados: onde vivem, quem acessa, o que já vazou ou quase
2. LGPD: papéis definidos? DPO? inventário de tratamento? apontamentos abertos de auditoria?
3. Política de uso de IA: existe? cobre o que a linha de frente JÁ usa?
4. Contratos com fornecedores de tecnologia: cláusulas de dados, aprisionamento, saída
5. O que impediria, hoje, um sistema de IA de entrar em produção aqui?

### Externos (30 min, quando o patrocinador abrir a porta)
1. "Como é ser cliente/parceiro desta empresa, no dia a dia?"
2. "Onde eles são mais lentos do que deveriam?"
3. "O que você mudaria primeiro?"

---

## Regras de condução

- **Ingestão no mesmo dia**, com os quatro metadados (`--level`, `--phase`, `--attribution "Nome, Cargo"`, `--date`). Transcrição de áudio direta pela ferramenta (`abba ingest gravacao.m4a ...`) ou transcript em texto.
- **Uma pessoa por vez** nos níveis gestor e linha de frente — em grupo, a hierarquia edita as respostas. A exceção deliberada é a entrevista de governança (o cruzamento Jurídico×TI ao vivo é parte do dado).
- **Contradição vira follow-up, nunca acareação.** "O time comercial nos contou X; como isso se encaixa com o que você descreveu?" — sem citar quem disse.
- **Meio do campo:** rodar `abba questions --output` de novo. As perguntas da segunda rodada devem ser mais específicas que as da primeira; se não forem, a primeira rodada foi rasa.
- **Nada de promessa em campo.** Entrevistador que promete solução contamina a análise e a venda. A resposta padrão: "boa — isso vai para a análise".
