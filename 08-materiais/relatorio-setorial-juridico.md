# IA na Advocacia Brasileira — Relatório Setorial ABBA

> **Camada:** modelo (fonte de conteúdo). Este markdown é a fonte do futuro DOCX/PDF no padrão visual da casa (capa "Preparado para: {{ESCRITÓRIO}}", `Ref: ABBA-2026-{{NNN}}`, sumário, rodapé padrão). Supersede o rascunho em inglês de abril/2026 (`abba-portal/docs/industry/legal-professional-services/INDUSTRY_AI_ADOPTION_REPORT.md`) — dados verificados em agosto/2026, com fonte em cada afirmação de mercado.
>
> **Regras aplicadas:** sem preços (preço é conversa) · sem contagem de dimensões ("mergulho profundo, do conselho à linha de frente") · vocabulário do posicionamento · toda afirmação de mercado com fonte na seção 9.
>
> Versão: 2.0 · 2026-08 · Revisão de sócio pendente antes da primeira entrega externa.

---

**A ABBA é uma consultoria de transformação em IA para empresas brasileiras.** Fazemos o que não dá para fazer de dentro de uma organização: construção de capacidade de IA em escala e prova independente de resultado — o número combinado antes, medido depois, validado por gente do cliente. Este relatório reúne o que o mercado, a regulação e a prática já mostram sobre IA na advocacia brasileira — para que a próxima conversa do seu comitê tenha algo melhor que slides de fornecedor para se apoiar.

## Sumário

1. O panorama de 2026 — a onda deixou de ser promessa
2. O problema invisível — adoção sem governança
3. O que a regulação já pede
4. Oito padrões de uso — onde o valor aparece, e onde trava
5. A economia da banca — a conta da hora faturada
6. Por que programas de adoção fracassam em escritórios
7. O que um caminho estruturado tem
8. Três primeiros passos que não dependem de nós
9. Fontes e método

---

## 1. O panorama de 2026 — a onda deixou de ser promessa

Quatro fatos, todos públicos, nenhum de fornecedor:

- **O primeiro unicórnio de IA da América Latina é uma legaltech brasileira.** A Enter — fundada em 2023 por Mateus Costa-Ribeiro, advogado formado pela UnB, com passagem por Harvard — captou R$ 500 milhões em maio de 2026, em rodada liderada pelo Founders Fund, atingindo avaliação de US$ 1,2 bilhão. A plataforma processa mais de 300 mil processos/ano em contencioso de alto volume para clientes como Bradesco, Nubank e Mercado Livre. [F1]
- **O detalhe estratégico:** a Enter atende as **empresas**, não os escritórios. O contencioso de massa está sendo automatizado por fora da advocacia tradicional, com escritórios parceiros no papel de revisores. Para o escritório de médio e grande porte, a consequência não é "comprar uma ferramenta parecida" — é decidir o que a banca se torna quando o volume deixa de sustentar a pirâmide.
- **O Judiciário institucionalizou.** O STF opera desde dezembro/2024 a MARIA, ferramenta de IA generativa para minutas, relatórios e triagem — sempre com supervisão humana declarada. [F2]
- **A adoção individual é massiva.** 77% dos advogados brasileiros afirmam usar IA no trabalho (estudo OAB, 2025/26); nas pesquisas da FGV Direito SP (CEPI), cerca de 8 em cada 10 profissionais do Direito usam IA com frequência, mais da metade diariamente; levantamento OAB-SP/Jusbrasil/ITS com 1.500+ respondentes encontrou 55,1% de uso diário de IA generativa. [F3][F4][F5]

O mercado de ferramentas também amadureceu: pesquisa jurídica com fonte (Jus IA/Jusbrasil), jurimetria (Turivius), gestão e cálculos (Jusfy — Series A com participação da Thomson Reuters em 2026), geração de peças, CLM de contratos. [F6] São ferramentas de **tarefa** — boas no que fazem, e mudas sobre a pergunta que importa: como a organização inteira trabalha com elas sem violar o que não pode ser violado.

## 2. O problema invisível — adoção sem governança

O contraste que define o momento: a adoção correu na frente da governança. Enquanto a maioria dos advogados já usa IA, a minoria das bancas tem política de IA que a equipe trate como vinculante — nas pesquisas setoriais disponíveis, menos de um quarto. [F3][F7]

A forma concreta desse vão tem nome: **Shadow AI**. O associado que, às 23h, cola um trecho de contrato ou de caso num chatbot gratuito para "ganhar tempo" está — sem que ninguém tenha decidido isso — combinando três exposições no mesmo clique:

1. **Sigilo profissional** (Código de Ética e Disciplina da OAB, arts. 25–27): confidencialidade absoluta sobre os assuntos do cliente. Dado identificável de cliente em ferramenta externa não contratada é violação independentemente da intenção.
2. **LGPD**: dado pessoal — muitas vezes sensível (matéria criminal, trabalhista, de saúde) — processado fora de base legal clara, em ferramenta cuja retenção e reuso a banca não controla, com direitos do titular (acesso, deleção) que a banca não consegue mais garantir.
3. **Risco de resultado**: jurisprudência inventada por ferramenta genérica já produziu casos públicos de peças com citações falsas — e uma peça errada protocolada não queima a ferramenta; queima o advogado que assinou.

A resposta reflexa — proibir — costuma piorar: empurra o uso para o celular pessoal, onde nem visibilidade existe. O que funciona é o caminho oposto: mapear o uso real (com anistia), decidir o que é permitido com quais salvaguardas, e dar à equipe um caminho oficial melhor do que o improvisado.

## 3. O que a regulação já pede

Não é preciso esperar lei nova para saber o que fazer — o calendário já existe:

| Marco | O que pede, na prática |
|---|---|
| **Recomendação OAB nº 001/2024** (Conselho Federal, nov/2024) [F8] | Uso ético de IA generativa na advocacia: confidencialidade e privacidade, independência técnica do advogado, **dever de revisão humana** do que a IA produz, transparência com o cliente sobre o uso |
| **Resolução CNJ nº 615/2025** (mar/2025) [F9] | Marco da IA no Judiciário: classificação de risco, governança, supervisão humana obrigatória, transparência — o padrão de referência que tribunais aplicarão e que contrapartes citarão |
| **LGPD** (em vigor) | Base legal para cada tratamento, atenção especial a dado sensível (art. 11), direitos do titular exercíveis (art. 18), medidas de segurança (art. 46+), comunicação de incidente à ANPD |
| **PL de IA em tramitação** | Direção clara: responsabilidade sobre sistemas de risco, revisão humana de decisões relevantes — quem já opera assim não precisará correr |

A leitura executiva: **as obrigações centrais já valem hoje** — sigilo e LGPD não esperam regulamento de IA. O escritório que se organiza agora faz planejamento; o que espera, fará resposta a incidente.

## 4. Oito padrões de uso — onde o valor aparece, e onde trava

Síntese de padrões observados no mercado brasileiro e na literatura setorial. Em todos, a mesma lei: **a IA que funciona está dentro do fluxo de quem trabalha, com revisão humana no ponto certo; a que fracassa é uma plataforma separada que alguém deveria visitar.**

| # | Padrão | Onde trava | Onde funciona |
|---|---|---|---|
| 1 | **Triagem e revisão de contratos** | Chatbot genérico erra sutilmente cláusulas brasileiras (indexação, foro, arbitragem); um erro constrangedor e o uso vira clandestino | Agente treinado nos modelos e no histórico DA banca, com humano no ponto de desvio |
| 2 | **Pesquisa de jurisprudência** | Ferramenta genérica inventa julgados com aparência plausível | Busca com recuperação sobre bases licenciadas, **fonte citada em toda resposta**, verificação obrigatória antes de protocolar |
| 3 | **Due diligence documental** | Plataforma comprada, usada num deal, abandonada (custo de treinar a equipe a cada uso supera o ganho percebido) | Integração ao fluxo e ao repositório que a equipe já usa — a arquitetura de adoção importa mais que a capacidade da IA |
| 4 | **Minutas de peças** | O piso de qualidade da IA é alto o bastante para o associado preguiçoso protocolar sem revisar — até a citação falsa aparecer e a banca reagir com proibição geral | IA como **assistente de pesquisa de quem escreve** (precedentes, cruzamento de citações), não como redator |
| 5 | **Comunicação com cliente e relatórios** | Cada um tem seu improviso; a qualidade varia por pessoa; ninguém vê o agregado | Modelos da casa + personalização assistida + revisão — o ROI mais rápido e o risco mais baixo da lista |
| 6 | **Mapeamento de conformidade / LGPD** | IA enumera obrigações bem e erra materialidade — completa e errada onde mais importa | Primeira passada estruturada pela IA + julgamento do advogado sênior por cima |
| 7 | **Triagem trabalhista / tributária de volume** | Especificidade de TRT/TRF e súmulas: a ferramenta genérica erra o detalhe que muda a triagem | Modelo ajustado ao acervo da própria banca, com aprovação de sênior — investimento que só se justifica quando a matéria é fatia relevante da receita |
| 8 | **Memória da banca** (precedentes internos, pareceres, quem sabe o quê) | O conhecimento vive em e-mails e pastas pessoais — não há o que a IA recuperar | Estruturar o acervo ANTES da ferramenta: a IA é os últimos 10% do projeto; a arquitetura de conhecimento é os 90 |

## 5. A economia da banca — a conta da hora faturada

A conversa que os fornecedores de ferramenta evitam: **para quem fatura por hora, produtividade mal desenhada é queda de receita.** Se a IA reduz um terço do tempo de uma tarefa faturada por hora e nada mais muda, o resultado é faturar menos.

Onde o ganho é real — e são decisões de desenho do modelo, não de software:

- **Amplitude de revisão do sócio.** O ganho mensurável não é o associado mais rápido; é o sócio revisando mais trabalhos por mês, com qualidade de primeira passada melhor. É a alavanca que torna o investimento racional numa banca de pirâmide.
- **Trabalho a preço fechado e por êxito** vira expansão direta de margem — e a IA torna mais matérias precificáveis assim, com risco controlado.
- **Retenção e percepção de cliente.** Cliente bem informado, com relatórios pontuais e status sob medida, renova — e o custo de produzir isso despenca (padrão 5 da tabela acima).
- **A pergunta de portfólio** que o unicórnio impõe (§1): quanto da receita atual depende de volume que tende a ser automatizado por fora — e o que ocupa esse espaço na banca daqui a 3 anos?

## 6. Por que programas de adoção fracassam em escritórios

Os modos de fracasso, na ordem em que aparecem:

1. **Opt-out silencioso de sócio sênior.** O comitê aprova; dois sócios de peso ignoram; os associados percebem e concluem que é opcional. Em seis meses o programa para — e a conta é debitada da "tecnologia", quando a falha foi de patrocínio.
2. **A armadilha do piloto.** Testa-se um produto num grupo, sem métrica combinada antes. Seja qual for o resultado, ninguém sabe o que ele provou — renova-se (por simpatia) ou cancela-se (por um episódio ruim), e a organização não construiu capacidade nenhuma.
3. **Governança de teatro.** A política existe, foi enviada por e-mail e é ignorada. Sem mecanismo vivo — treinamento específico, auditoria possível, exemplos visíveis de cima — papel não muda comportamento.
4. **Confundir capacitação com evento.** Seminários e palestras informam; não mudam como o trabalho é feito na terça-feira. Mudança de comportamento exige prática no fluxo real, acompanhamento e cobrança — o que distingue instalação de capacidade de um calendário de eventos.
5. **Estratégia terceirizada ao fornecedor.** O vendedor de legaltech apresenta o produto como "a transformação"; a banca compra a narrativa; dois trimestres depois o uso é baixo e a culpa é do fornecedor. Nenhum fornecedor consegue instalar uma capacidade que a organização não desenhou para receber.

O fio comum: **a maior parte do valor vive em pessoas, processos e cultura — e essa é exatamente a parte que não vem na caixa.**

## 7. O que um caminho estruturado tem

O jeito ABBA de percorrer isso, em seis etapas — cada uma entrega valor sozinha e produz o insumo da seguinte:

1. **Análise por informação pública** (gratuita) — uma amostra real do método, feita de fora, apresentada em 45 minutos: onde o dinheiro está vazando e as perguntas que só a banca pode responder. *"Foi feito de fora — imagine com os dados de dentro."*
2. **Avaliação profunda** — o mergulho do conselho à linha de frente: entrevistas em todos os níveis, revisão documental, quantificação. Sai um portfólio de oportunidades ranqueado e quantificado, com dado por trás de cada afirmação — e as decisões de governança (OAB, LGPD) registradas antes de qualquer construção.
3. **Prova em protótipo** — o caso escolhido, construído com dados reais e validado com usuários-chave; a diretoria decide continuar ou parar **com números combinados antes**. É o oposto do piloto solto.
4. **Construção e implantação** — os agentes aprovados, sob medida, com pontos de revisão humana, integrados aos sistemas da banca — na infraestrutura de vocês ou em nuvem gerenciada.
5. **Capacitação de todos os níveis** — plataforma própria com trilhas progressivas + sessões presenciais nos marcos; e a pergunta da Bússola instalada em cada pessoa: *o que posso parar de fazer? o que posso começar? o que ainda preciso fazer?*
6. **Presença contínua** — operação sob acordo de nível de serviço, ritual quinzenal curto, relatório mensal de impacto — e o registro decisão → resultado medido que permite à banca **provar** o que mudou, não achar.

E os quatro princípios de arquitetura que traduzem o sigilo profissional em engenharia — utilizáveis como checklist para avaliar qualquer fornecedor, inclusive nós: **memória segregada por cliente · deleção comprovável · fonte citada ou abstenção · um humano nomeado assina**.

## 8. Três primeiros passos que não dependem de nós

1. **Mapeie o uso real antes de escrever política.** Uma sessão de anistia anônima ("o que vocês já usam, para quê?") produz o retrato que nenhum comitê tem — e é pré-requisito de qualquer política que pretenda ser obedecida.
2. **Nomeie um patrocinador com poder e agenda.** Programa de IA que reporta a "inovação" sem um sócio do comitê com horas reais dedicadas fracassa de forma previsível. O patrocinador precisa de mandato para segurar inclusive sócio sênior na regra.
3. **Exija número combinado antes, em qualquer piloto — de qualquer fornecedor.** Qual métrica, medida por quem, em quanto tempo, e o que acontece se não atingir. A pergunta custa zero e evita a armadilha que consome a maioria dos orçamentos de IA.

Se em algum desses passos fizer sentido ter a gente do lado de vocês, a porta de entrada é a análise gratuita da própria banca (item 1 do §7) — contato@abbaservices.com.br.

## 9. Fontes e método

**O que este relatório é:** síntese de dados públicos verificados em agosto/2026, do contexto regulatório primário e da experiência da ABBA em transformação organizacional com IA. **O que não é:** parecer jurídico, endosso de fornecedor específico, ou substituto de avaliação da realidade concreta da sua banca.

- [F1] Forbes Brasil — *"Startup jurídica Enter vira unicórnio de IA com rodada de US$ 100 milhões liderada pelo Founders Fund"* (mai/2026): forbes.com.br/forbes-money/2026/05/startup-juridica-enter-vira-unicornio-de-ia · CNN Brasil: cnnbrasil.com.br/economia/negocios/startup-brasileira-de-ia-juridica-enter-alcanca-us-12-bi-em-valuation · InfoMoney: infomoney.com.br/mercados/startups-quem-e-a-enter-unicornio-brasileiro-de-ia-do-setor-juridico
- [F2] STF — *"Supremo inaugura MARIA, primeira ferramenta do Tribunal com inteligência artificial generativa"* (dez/2024): noticias.stf.jus.br
- [F3] Exame — *"IA já é usada por 77% dos advogados e redefine a prática jurídica, aponta estudo da OAB"*: exame.com/inteligencia-artificial/ia-ja-e-usada-por-77-dos-advogados
- [F4] FGV Direito SP (CEPI) — pesquisa sobre IA generativa no Direito: direitosp.fgv.br (uso frequente ~80%; diário 58%)
- [F5] OAB-SP / Jusbrasil / ITS Rio — pesquisa com 1.500+ profissionais (55,1% uso diário): sobre.jusbrasil.com.br/releases
- [F6] Law.com — *"Brazilian Legal Tech Startup Jusfy Announces $15M Series A Backed by Thomson Reuters"* (jul/2026); sites institucionais Turivius, Jus IA
- [F7] Pesquisas setoriais de adoção × política vinculante (Thomson Reuters Institute; levantamentos legal tech 2024–2025) — faixas citadas de forma conservadora
- [F8] OAB Conselho Federal — *"OAB aprova recomendações para uso de IA na prática jurídica"* (Recomendação nº 001/2024): oab.org.br/noticia/62704
- [F9] CNJ — Resolução nº 615, de 11/03/2025: atos.cnj.jus.br/atos/detalhar/6001

---

*ABBA · abbaservices.com.br · Este documento é entregue em PDF datado; a versão vigente é sempre a de data mais recente.*
