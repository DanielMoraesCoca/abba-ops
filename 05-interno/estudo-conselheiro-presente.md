# Estudo: O Conselheiro presente: como ele se senta, escuta, acessa e responde

> **Camada:** interno (pesquisa + plano de produto). Origem: pedido do sócio (2026-08-04): *"como seria a comunicação da empresa com esse conselheiro? Como ele estaria integrado e acessaria tudo o que permitirem com segurança? Como ele se assentaria com os diretores? Onde eles o acessariam? Seria interessante se ele fosse como um Jarvis para se assentar na mesa de reuniões... uma entidade que pudesse estar presente em todos os lugares da empresa, sabendo de tudo o que está acontecendo."*
>
> **O que este documento é:** a pesquisa diligente que responde à pergunta, mais as perguntas que não foram feitas e mudam a resposta, mais um plano em ondas com gatilhos. **Nada aqui está construído**: é desenho, não capacidade. Nenhuma linha deste estudo pode virar promessa comercial antes dos gates nomeados na §9.
>
> Dono: chapéu Tecnologia (arquitetura) + Entrega (protocolo) + Comercial (o que pode ser dito). Revisar quando o PL 2338 for sancionado.

---

## 1. A pergunta, reformulada com honestidade

A visão é boa e o instinto está certo: **um conselheiro que só aparece no trimestre não conhece a empresa; um que conhece a empresa vale dez vezes mais.** A pesquisa confirma o valor. Mas ela também mostra que a forma imaginada (*estar em todo lugar, ouvir tudo*) é, em 2026, simultaneamente **a mais frágil tecnicamente, a mais perigosa juridicamente e a que destrói o próprio dado que quer capturar**.

A reformulação que este estudo defende, e que preserva 100% da ambição:

> **Onipresença não é ouvir tudo. É lembrar de tudo o que importa, ligar os pontos entre as salas e chegar antes.**

Um Conselheiro que registra cada decisão que a diretoria tomou, com o número que ela deveria mover e o resultado medido depois, e que às 7h da manhã diz *"três coisas mudaram desde ontem e uma delas contradiz o que vocês decidiram em março"*: é mais poderoso, mais defensável e mais vendável que um microfone ligado no corredor. E a ABBA **já tem 80% da engenharia disso construída**.

---

## 2. Os cinco achados que mudam o desenho

### Achado 1: A arquitetura do "bot que entra na reunião" está sendo fechada pelas plataformas

Em março de 2026 o Google Meet passou a **marcar bots de anotação de terceiros como "risco potencial" e a negar a entrada por padrão**; a Microsoft passou a **detectar bots externos no Teams, rotulá-los no lobby e exigir aprovação do organizador**; e em julho de 2026 o Teams ganhou um **interruptor que desliga Copilot/recap no meio da reunião**. Organizações já publicam listas de assistentes de terceiros **não autorizados**. ([Basil AI](https://basilai.app/articles/2026-06-13-bot-vs-bot-free-ai-notetaker-google-meet-teams-2026.html) · [Nudge Security](https://www.nudgesecurity.com/post/shadow-ai-is-taking-notes-the-growing-risk-of-ai-meeting-assistants) · [Windows Latest](https://www.windowslatest.com/2026/07/05/microsoft-caves-after-teams-ai-backlash-will-let-you-turn-off-copilot-facilitator-and-recap-mid-meeting/))

**Consequência de desenho:** construir o diferencial da ABBA sobre um bot que entra na reunião do cliente é construir sobre areia, e sobre uma superfície que o TI do cliente tem ordens para bloquear. **O caminho durável é o oposto: a plataforma do cliente grava com a licença dele, e o Conselheiro recebe o resultado.** Nós nunca somos o bot estranho no lobby.

### Achado 2: A presença de um gravador degrada exatamente o dado que se quer capturar

Levantamentos de 2026 relatam que **84% das pessoas mudam de comportamento ou deixam de dizer coisas quando um bot de IA entra na chamada.** ([Nudge Security](https://www.nudgesecurity.com/post/shadow-ai-is-taking-notes-the-growing-risk-of-ai-meeting-assistants))

**Consequência de desenho:** a reunião de diretoria é justamente onde se diz o que não se escreve. Um ouvido permanente transforma a sala honesta em teatro, e a ABBA passa a registrar a versão performada da empresa. **O silêncio induzido é um custo invisível que nenhum fornecedor menciona.** Presença anunciada e episódica preserva a franqueza; presença permanente a mata.

### Achado 3: No Brasil, monitorar sem aviso prévio e expresso é passivo trabalhista, não risco teórico

A jurisprudência do TST é consistente: o poder diretivo do empregador **não é absoluto**: é limitado pela Constituição, por acordos coletivos e pela boa-fé; o monitoramento de ferramentas corporativas só é lícito **com ciência prévia e expressa** do empregado; e **monitoramento excessivo ou invasivo gera dano moral indenizável**. ([Chohfi](https://chohfiadvogados.com.br/monitoramento-por-cameras-no-ambiente-de-trabalho-limites-fixados-pelo-tst/) · [Guersoni Rezende & Simões](https://grsimoesadvogados.com.br/monitoramento-no-trabalho-limites-legais-tst-lgpd/) · [TST: Coordenadoria de Documentação](https://www.tst.jus.br/documents/1295387/1309397/Privacidade+e+direito+a+intimidade+no+ambiente+de+trabalho))

Na LGPD, gravação de reunião exige **informar sempre**, de preferência com consentimento por escrito; o legítimo interesse é possível mas exige teste de balanceamento documentado (LIA) e **não sobrevive a expectativa legítima frustrada**; e a boa prática é declarar **onde fica armazenado, quem acessa e por quanto tempo**. ([TI Rio](https://www.ti.rio/gravar-uma-reuniao-sem-avisar-lgpd-e-direito-de-imagem/) · [Maluf Geraigire](https://www.mgadv.com.br/gravacao-de-imagens-e-a-lgpd-os-individuos-sob-a-otica-da-privacidade-e-protecao-de-dados/) · [Data Privacy Brasil: o legítimo interesse](https://www.dataprivacybr.org/wp-content/uploads/2021/10/O-legitimo-interesse-na-LGPD.pdf))

E o PL 2338, em votação final na Câmara, adota o modelo de risco com **avaliação de impacto algorítmico obrigatória** para alto risco, **supervisão humana efetiva** e sanções de até **R$ 50 milhões por infração**: com monitoramento de trabalhadores entre os usos sensíveis. ([Senado](https://legis.senado.leg.br/sdleg-getter/documento?disposition=inline&dm=9347622) · [Exame](https://exame.com/inteligencia-artificial/marco-legal-da-inteligencia-artificial-pl-2338-o-que-muda-para-empresas-com-a-nova-lei/))

**Consequência de desenho:** qualquer captura ambiente exige política escrita, aviso prévio, base legal documentada, retenção declarada e caminho de contestação: **antes** do primeiro áudio. Isso não é burocracia: para uma firma que vende governança, é o produto.

### Achado 4: "Quem disse o quê" erra o suficiente para ser perigoso numa sala de diretoria

A separação de falantes (diarização) tem erro de **5–10% em áudio limpo com 2–3 pessoas, subindo para 20–30% em salas ruidosas com muitos falantes**; os melhores modelos abertos ficam em 11–19% em benchmarks padrão. A literatura é explícita: **diarização não é verificação de identidade.** ([AssemblyAI](https://www.assemblyai.com/blog/what-is-speaker-diarization-and-how-does-it-work) · [comparativo 2026](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis))

**Consequência de desenho:** atribuir a um diretor uma frase que ele não disse, num registro que a empresa trata como cartório, é o tipo de erro que encerra um contrato. **Regra inviolável: atribuição de fala nunca vira fato registrado sem confirmação humana nomeada.** Isso já é a doutrina de autoridade de origem que a ABBA implementou em código (`human_stated` > `llm_inference`): aqui ela vira salva-vidas.

### Achado 5: Memória total é também exposição total (e ninguém vende isso junto)

Tribunais em 2026 já recusaram estender sigilo profissional a material preparado em ferramenta de IA de consumo (*United States v. Heppner*), e a análise de proteção considera **retenção e compartilhamento com terceiros pelo fornecedor**. ([Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk) · [Smith Anderson](https://www.smithlaw.com/newsroom/publications/the-silent-guest-in-your-meetings-legal-risks-of-ai-note-takers))

**Consequência de desenho, e esta é a que ninguém diz ao cliente:** hoje a memória de uma empresa é fragmentada, e essa fragmentação é, na prática, uma proteção. Um arquivo completo e pesquisável de tudo o que foi dito vira **prova disponível** em qualquer disputa trabalhista, tributária ou societária. **Retenção deixa de ser detalhe de configuração e passa a ser a decisão de arquitetura mais importante do produto.** A resposta certa não é guardar tudo para sempre: é guardar **a decisão e o número**, e descartar o áudio bruto por padrão.

---

## 3. As doze perguntas que não foram feitas, e que decidem o produto

| # | A pergunta | Por que ela decide o desenho | Resposta proposta |
|---|---|---|---|
| 1 | **A quem o Conselheiro responde?** Se o CEO e um diretor perguntam a mesma coisa, recebem a mesma resposta? | Uma entidade que sabe tudo vira arma política interna no dia em que responde diferente para pessoas diferentes | **Uma só verdade, escopo declarado.** O Conselheiro responde sobre a *empresa*, nunca sobre *pessoas*. Perfis de acesso definidos em contrato, e o cliente vê a lista de quem pergunta o quê |
| 2 | **E quando a pauta é gente?** (demissão, desempenho, saúde, sindicato) | LGPD art. 11 (dado sensível) e risco trabalhista direto | **Zona sem registro, por padrão.** Protocolo com botão de encerrar captura e regra escrita: pauta de pessoas não entra na memória |
| 3 | **Quem é controlador e quem é operador?** | Define quem responde perante a ANPD | Cliente = **controlador**; ABBA = **operador**, com instruções documentadas. Já é a estrutura do nosso contrato: a captura de reunião exige anexo próprio |
| 4 | **Terceiros na sala** (clientes, fornecedores, advogado), quem os informa? | Eles não são empregados; não há poder diretivo sobre eles | **Aviso no convite + no início**, e regra de que reunião com terceiro só é capturada com anuência explícita registrada |
| 5 | **Por quanto tempo fica, e o que exatamente fica?** | É a decisão que cria (ou evita) a exposição do Achado 5 | **Áudio: descartado após a extração** (padrão). **Transcrição: prazo curto e declarado.** **Permanente: só decisão, métrica, resultado e fato confirmado por humano** |
| 6 | **O que acontece quando ele erra na frente do conselho?** | Credibilidade é o produto | Modelo centauro já vigente: recomendação nasce com **probabilidade declarada e imutável**; erro entra no registro em vez de sumir |
| 7 | **O campeão interno vai sentir isso como vigilância?** | O campeão é a peça que faz a adoção acontecer: os 70% que vendemos | Só a **camada de diretoria** é capturada; nunca a operação. E o campeão recebe o resumo, não é objeto dele |
| 8 | **Quem alimenta a memória?** | Doutrina vigente: ingestão é **curada por humano**; saturação nunca bloqueia escrita | Uma torrente ambiente quebraria isso. **A curadoria continua humana: o Conselheiro propõe, um sócio aprova** |
| 9 | **Isso não nos torna a IA-sombra que combatemos?** | Vendemos um Workshop de Shadow AI. Entrar com bot não sancionado no Teams do cliente é virar o problema | **Nunca entramos com ferramenta não aprovada.** Se o TI não homologou, não existe |
| 10 | **Quanto custa por cliente/mês?** | A margem da recorrência já é o risco nº 10 do conselho | Estimado na §8, com os itens não medidos marcados |
| 11 | **O que a Microsoft já dá de graça na licença que o cliente paga?** | Se o nosso diferencial for transcrição, perdemos | Recap nativo exige licença Copilot/Teams Premium ([MS](https://mc.merill.net/message/MC1261588)). **O nosso diferencial nunca é transcrever: é ligar reuniões diferentes ao longo de meses e provar o resultado** |
| 12 | **Reunião presencial**: a maioria no médio porte brasileiro | O desenho "bot no Meet" não cobre a sala real | Padrão do **operador humano**: alguém abre, anuncia, encerra. Nunca aparelho ligado sozinho |

---

## 4. O desenho: "O Assento": cinco camadas, da mais segura à mais sensível

O nome nasce do produto que já existe (a *cadeira*). O Conselheiro **toma assento**: por convite, anunciado, com hora para entrar e sair. Nunca está "no ar".

### Camada 0: O que já funciona hoje (nada a construir)
Ritual semanal de 20 min, conselho trimestral, diário decisão→resultado, brief mensal, fila da manhã. **Esta camada sozinha já entrega presença**, e é a única que está construída e testada.

### Camada 1: A Ata Viva (o assento nas nossas próprias reuniões)
O Conselheiro "senta" nas reuniões que **a ABBA já conduz**: o ritual semanal e o conselho trimestral. Um sócio opera: anuncia, captura, encerra. A saída não é transcrição: é **decisão + métrica + fato**, revisada pelo sócio antes de entrar na memória.
*Exige:* protocolo escrito, anexo de consentimento, botão de encerrar. *Risco:* baixo (é a nossa reunião, com nossa pauta). *Prazo:* semanas.

### Camada 2: A Voz (onde os diretores o acessam)
Duas superfícies, com uma regra de separação que a nossa própria política já impõe:
- **WhatsApp:** a porta que o diretor brasileiro realmente usa: pergunta rápida, alerta da fila da manhã, aviso de gatilho vencendo. Custo por mensagem baixo e previsível ([tabela 2026](https://www.socialhub.pro/blog/preco-whatsapp-api-2026-brasil/)). **Nunca leva conteúdo sensível**: leva o aviso e o link.
- **Portal (área do conselho):** onde a resposta com conteúdo vive: dossiê, decisões, gatilhos, brief. Autenticado, auditado, por perfil.

*Exige:* superfície nova no portal + integração WhatsApp Business API. *Risco:* baixo-médio (autenticação do portal é R3). *Prazo:* meses.

### Camada 3: Os Olhos (integração com os sistemas, só leitura)
Conexões **somente leitura** a ERP/fiscal/CRM pelo padrão MCP, com escopo por usuário, propósito declarado e log de cada chamada (identidade, ferramenta, recurso, agente, propósito, resultado, hora), e com o alerta que a própria literatura faz: **agente não pode herdar credencial de serviço genérica**, e log tem que registrar *autoridade*, não só ação. ([Atlan](https://atlan.com/know/ai-agent/how-to-build-mcp-servers-for-enterprise-data/) · [MCP: auth gerenciada](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) · [Synapt](https://www.synapt.ai/layered-by-synapt/mcp-governance-enterprise-ai/))
*Exige:* homologação do TI do cliente, mapa de fontes × autoridade, DPO no circuito. *Risco:* médio. *Prazo:* por cliente.

### Camada 4: O Ouvido Ampliado (as reuniões do cliente)
**Nunca com bot nosso.** O cliente grava com a licença que já paga (Teams/Meet), e **o cliente compartilha** o resultado com o Conselheiro. Nós somos destinatário, não intruso: o que sobrevive à política de bloqueio das plataformas e ao TI do cliente.
*Exige:* política de IA do cliente, aviso a empregados, base legal documentada, retenção declarada, terceiros informados. *Risco:* alto. *Gate:* advogado + DPO do cliente.

### Camada 5: A Sala Física (presencial)
Kit de sala com **operador humano**: alguém abre, a placa na mesa avisa, encerra-se ao fim. Sem gravação contínua, sem dispositivo autônomo, sem exceção.
*Exige:* tudo da camada 4 + protocolo presencial + registro de anuência dos presentes. *Risco:* alto. *Gate:* último a ser ativado, se for.

---

## 5. A anti-camada: o que recusamos por escrito

Estas recusas são produto, não limitação. Vão para o material do guardião:

1. **Nunca captura ambiente permanente.** O Conselheiro não fica ligado; ele é convidado.
2. **Nunca gravação sem aviso**, em nenhuma hipótese, para ninguém.
3. **Nunca análise de desempenho, sentimento ou "engajamento" de indivíduos.** Não medimos pessoas.
4. **Nunca resposta sobre uma pessoa:** o Conselheiro fala de decisões, números e processos.
5. **Nunca entramos com ferramenta que o TI do cliente não homologou.**
6. **Nunca atribuímos uma fala sem confirmação humana.**
7. **Nunca guardamos áudio por padrão:** extrai-se a decisão, descarta-se o bruto.
8. **Nunca somos o certificador da nossa própria captura:** a auditoria de conformidade é do DPO do cliente.

---

## 6. Como isso se apoia no que já está construído

A boa notícia: **a espinha existe e foi testada.** O que falta é superfície, não cérebro.

| Peça do "Assento" | O que já existe no código | O que falta |
|---|---|---|
| Memória com verdade datada | `facts` bitemporais, supersessão que nunca apaga |  |
| Quem pode afirmar o quê | **autoridade de origem** (`human_stated` > `client_doc`/`tool_output` > `llm_inference`) | mapear "fala em reunião" como origem de **baixa** autoridade até confirmação |
| Cartório de decisões | `decisions` + `decision_outcomes` com gate de humano nomeado |  |
| Chegar antes | fila da manhã (`brain next`), gatilhos por decisão, obsolescência projetada | entrega da fila no WhatsApp/portal |
| Honestidade da recomendação | probabilidade declarada **imutável** + placar de calibração |  |
| Esquecer sob comando | `abba forget` + certificado de deleção | estender ao áudio/transcrição |
| Ciclo noturno | `abba brain sleep` com teto de gasto |  |
| **Ingestão de reunião** |  | **peça nova** (transcrição → proposta de fatos/decisões → revisão humana) |
| **Superfície de pergunta** |  | **peça nova** (portal + WhatsApp) |
| **Conectores de leitura** |  | **peça nova** (MCP read-only + log de autoridade) |

---

## 7. O dossiê do guardião deste produto (o que o DPO vai perguntar)

Uma página que precisa existir **antes** da primeira demonstração: base legal por camada (e a LIA escrita quando for legítimo interesse) · quem é controlador e operador · o que é capturado e o que não é · onde o dado mora e por quanto tempo · quem acessa e como se audita · como se contesta e como se apaga (com certificado) · o que acontece no fim do contrato (portabilidade em formato aberto) · e a lista de recusas da §5. Encaixa direto no [mapa ISO 42001 / PL 2338](../06-ferramentas/mapa-avaliacao-iso42001-pl2338.md) e no [Sprint LGPD](../03-comercial/proposta-sprint-lgpd.md).

---

## 8. Custo e preço (estrutura fechada, números a medir)

| Item | Ordem de grandeza | Estado |
|---|---|---|
| Transcrição + diarização por hora de áudio | centavos a poucos reais/hora | **{{MEDIR}}** na primeira execução real |
| LLM da extração (fatos/decisões por reunião) | cabe no teto atual do ciclo noturno | **{{MEDIR}}** |
| Ciclo noturno por cliente | ~R$ 150/mês (estimativa já registrada, R20) | **{{MEDIR}}** |
| WhatsApp | ~R$ 0,035 por mensagem de utilidade; respostas dentro da janela passam a ser cobradas a partir de out/2026 ([fonte](https://www.aleguimas.com.br/blog/whatsapp-business-api-o-que-muda/)) | verificado |
| **Hora de sócio na curadoria** | **o item dominante**, e o que o conselho já apontou como subestimado | **decidir teto por cliente** |

**Regra de precificação:** o Assento é **camada da manutenção/Conselheiro**, nunca produto avulso, e nenhuma camada entra em tabela antes do custo unitário medido. A camada 4 (reuniões do cliente) precisa de teto de horas explícito, senão ela come a margem inteira.

---

## 9. O plano em quatro ondas, com gatilho de cada uma

| Onda | O que se faz | Gatilho para começar | Gate para terminar |
|---|---|---|---|
| **1: Cliente Zero interno** (30 dias) | A ABBA usa o Assento **em si mesma**: as reuniões de sócios viram Ata Viva; a fila da manhã roda de verdade; medimos custo e tempo de curadoria | Nenhum: é interno e não toca dado de cliente | Custo medido + protocolo escrito + 4 semanas sem falha |
| **2: Ata Viva no 1º cliente** (camadas 1+2) | O assento nas reuniões que já conduzimos + a voz (portal, e WhatsApp só para avisos) | 1º cliente em manutenção **e** onda 1 concluída | Anexo de consentimento revisado pelo advogado (junto de P4) |
| **3: Os Olhos** (camada 3) | Conectores só-leitura ao ERP/fiscal, com log de autoridade e homologação do TI | Cliente pede, TI homologa, DPO aprova | Teste de menor privilégio: chamada fora de escopo tem que ser recusada |
| **4: O Ouvido Ampliado** (camadas 4/5) | Reuniões do próprio cliente, sempre via licença dele; presencial com operador humano | Política de IA do cliente publicada + aviso a empregados + LIA escrita | Avaliação de impacto algorítmico se o PL 2338 estiver sancionado |

**Regra que atravessa as quatro:** nenhuma onda começa sem a anterior fechada, e **nenhuma delas vira frase de venda antes de existir**. Hoje, o que se pode dizer a um cliente é a camada 0, que já é mais do que qualquer concorrente entrega.

---

## 10. O que fazer nos próximos 30 dias (e não custa nada)

1. **Escrever o protocolo da Ata Viva** (uma página: como se anuncia, o que se captura, o que se descarta, quem revisa, como se encerra).
2. **Rodar em nós mesmos:** a reunião semanal de sócios vira o primeiro assento. É o Cliente Zero do produto, dentro do Cliente Zero que já está planejado.
3. **Medir**: custo por hora de reunião processada e minutos de curadoria por reunião. Sem esses dois números, não há preço.
4. **Levar ao advogado junto de P4/P4b**: o anexo de captura de reunião (controlador/operador, base legal, retenção, terceiros, revogação).
5. **Uma página do guardião** (§7), que serve também para a venda.

Nada disso depende de código novo, e tudo isso é pré-requisito do que depende.

---

## 11. Como isso muda o discurso comercial

**O que passa a ser dito (verdadeiro hoje):** *"O Conselheiro não é uma cabeça que aparece no trimestre: ele senta nas reuniões que conduzimos, registra cada decisão com a métrica combinada antes, e às segundas-feiras diz o que mudou e o que vence. A memória fica com vocês, exportável."*

**O que só pode ser dito depois do gate:** qualquer menção a ouvir reuniões do cliente, a integração com sistemas, a assistente no WhatsApp ou a "sabe tudo o que acontece na empresa".

**O que nunca será dito:** "está presente em todos os lugares", "ouve tudo", "acompanha o time". Não porque não seja vendável, mas porque é exatamente a frase que faz o DPO do cliente encerrar a reunião, e porque é a promessa que a pesquisa mostra que se volta contra quem a faz.

---

## Ligações

[Conselheiro de IA](../03-comercial/conselheiro-de-ia.md): o produto que este estudo aprofunda · [Dossiê vivo](../04-entrega/dossie-vivo-conselheiro-digital.md): o cérebro que já existe · [Ritual semanal](../04-entrega/ritual-semanal.md): a camada 0 em operação · [Estudo de imunidade](estudo-imunidade-diretor-de-ia.md): por que a independência é o ativo · [Mapa ISO 42001 / PL 2338](../06-ferramentas/mapa-avaliacao-iso42001-pl2338.md) · [Registro de riscos](registro-de-riscos.md): R3 (autenticação), R20 (custo do ciclo)
