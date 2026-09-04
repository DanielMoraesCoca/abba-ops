# Crônica da Construção: o estado de tudo

> **O que é isto:** a memória destilada das sessões de construção da ABBA (sócios + Claude, jul a set/2026). Um documento só que responde "o que existe, por que existe, e o que falta". Escrito para dois leitores: os sócios, e o Jarvis (o agente pessoal, que carrega este arquivo no contexto).
>
> **Regra de manutenção:** atualizar ao fim de cada rodada grande de construção. Detalhe fino mora nos documentos-fonte linkados; aqui vive o mapa.

Última atualização: 2026-09-04.

## 1. A máquina hoje: quatro repositórios e um acervo

**abba-ops** (este repositório): a fonte da verdade do negócio. Identidade e doutrina (`00-identidade/`), setores (`01-setores/`), jornada do cliente (`02-jornada-do-cliente/`), comercial vigente (`03-comercial/`), entrega (`04-entrega/`), interno e estudos (`05-interno/`), fichas de ferramenta (`06-ferramentas/`), materiais (`08-materiais/`) com um **gerador determinístico** (Node + pptxgenjs/docx) que produz todos os decks e DOCX a partir de código, com validador de preços contra a régua em todo build e manifesto anti-sobrescrita.

**assessment-brain**: a ferramenta interna de assessment. CLI Node que analisa empresas nas **25 dimensões proprietárias** (prompts validados a 25/25 de captura, 0,91 de confiança média), com ingestão de documentos, síntese, relatórios, knowledge vault de padrões anonimizados e revisor de materiais (régua v2.0.0 embarcada, sincronizada com a deste repo). Dentro dele vive o **cérebro do Conselheiro (Fase 1)**: fatos bitemporais que nunca são apagados, autoridade por origem (humano > documento > inferência), decisões com portão humano nomeado, ciclo noturno com teto de gasto, consolidação de memória em camadas, fila da manhã de antecipação e calibração de previsões (Brier). Perto de 300 testes automatizados; deleção de PII só pelo caminho sancionado (`abba forget`).

**abba-portal**: o portal de treinamento (Next.js) usado no programa. As telas atuais estão capturadas como fotos nos materiais.

**ABBA** (repo de origem, legado): o runtime CrewAI histórico. Hoje abriga o **Jarvis** (`jarvis/`): o chefe de gabinete pessoal no Telegram, em produção desde 2026-09-04 (ver §5).

**Acervo Claude**: os estudos estratégicos publicados como artifacts (Um Produto Só v2, A Máquina que Constrói a Máquina, estudos do Conselheiro). O conteúdo decisório deles está sempre refletido nos .md deste repo; o artifact é a versão navegável.

## 2. O modelo comercial vigente (V5, resumo executivo)

Três caminhos, nada mais (detalhe: [`../03-comercial/tabela-de-precos.md`](../03-comercial/tabela-de-precos.md)):

1. **Mapa de Vazamento** (gratuito): a porta de entrada.
2. **Programa "AI Native · Ano 1"**: 12 meses, 3 fases, 3 portões de saída sem multa (semana 6, mês 6, mês 12). Fase 1 firme a R$ 26.000; fases 2 e 3 são opção exercida no Portão da Prova. Portes: P R$ 218k · M R$ 278k · G R$ 378k (26 + 4 trimestres de 48/63/88k).
3. **Conselheiro de IA** avulso: R$ 12k mensal ou R$ 7,5k/mês no trimestral; com memória (cérebro) R$ 15k.

Ano 2+: **Assinatura da Capacidade** (11/15/21k por mês conforme porte) ancorada no **Exame Anual de IA** (re-medição das 25 dimensões; nunca chamar de "auditoria"). Expansão por mini-ciclos (R$ 42k). Diagnóstico standalone R$ 45k. **Tudo marcado "proposta V5, Pedro valida os preços".** Alternativa mensal do programa: +8% sobre o equivalente trimestral.

## 3. A história em capítulos (linha do tempo)

- **Jul/2026 · Fundação.** O abba-ops nasce como fonte única da verdade; decisões P1 a P9 resolvem preço v1, e-mail, níveis, SLA honesto. A identidade visual é fixada (navy #1B2A4A, dourado #C2A35B). O assessment web é descoberto no ar.
- **Ago/2026 · Profundidade.** Estudos grandes: utility delta, conselheiro presente, análise estratégica, parecer do conselho. O cérebro do Conselheiro é construído no assessment-brain (ondas 1 a 3 + camada de antecipação). Tabela v2 (jornada R$ 260k).
- **2026-08-31 a 09-01 · A Virada V5.** O cardápio de ~15 caminhos colapsa nos 3 caminhos acima, com foco declarado em retenção perpétua. Seis frentes de pesquisa + red-team derrubam as peças fracas (multa de saída, retenção de portfólio). Reescrita completa dos documentos-base e da apresentação institucional.
- **09-01 a 09-02 · Forma e voz.** Duas rodadas de feedback do sócio moldam os materiais: registro formal de diretoria (base na apresentação antiga comprovada), palco só no palco, um slide por fase com os serviços em "o quê · por quê · como", Conselheiro pelo mecanismo, exemplo real de metas combinadas (empresa preservada). Regra editorial: **sem travessão** em documento oficial e interno. Termo do Programa vira DOCX do gerador; régua embarcada sincronizada.
- **09-02 · O conselho.** Estudo "A Máquina que Constrói a Máquina": a tese de que a ABBA tem hoje uma máquina de entrega madura (centenas de testes) e zero clientes; a lição do Model 3 é dominar o processo à mão antes de automatizar; o gargalo não é ferramenta, é agenda.
- **09-04 · O Jarvis.** Agente pessoal do sócio entra em produção no Telegram (fase 1). Em paralelo, o sócio inicia por conta própria a reescrita do assessment em Python/CrewAI; proposto um teste de paridade (golden set Node vs. Python) antes de qualquer troca.

## 4. Doutrinas inegociáveis (o digest que não muda)

1. **Nunca mensagem fria.** Caminho: contexto público, introdução quente, canal corporativo.
2. **Prova, não impressão.** Número combinado antes, medido depois; nenhum time interno pode ser a própria prova.
3. **Nome de cliente nunca em material público ou em git de material.** O vault guarda só padrões anonimizados.
4. **Preço público só sai a cliente com validação do Pedro.**
5. **Garantia é porta de 1 via não ativada**: o portão é direito de saída, nunca "garantia de resultado".
6. **Retenção por composição de valor, nunca por dependência.**
7. **Sem travessão** em documento oficial e interno (vigente desde 2026-09-02; históricos preservados).
8. **LGPD como produto**: a ABBA vende governança; as ferramentas da casa usam só fontes públicas e são exemplares nisso.
9. **Decisão relevante só vale registrada** no [`registro-de-decisoes.md`](registro-de-decisoes.md) (append-only, portas de 1 e 2 vias).

## 5. O Jarvis (o leitor deste arquivo)

Chefe de gabinete pessoal do sócio, no Telegram (`ABBA/jarvis/`). CrewAI, 1 agente, acesso restrito por id. Fase 1 em produção: consulta CNPJ (BrasilAPI), busca web de decisores (Serper, opcional), busca em todo este repositório, notas de trabalho, rascunhos (nunca envia em nome do sócio). Fases seguintes: 2 agenda + rascunhos de e-mail · 3 trocar o dossiê estático pelo `abba brain` da engagement abba-interna · 4 WhatsApp pela API oficial da Meta. Fronteira deliberada: **não garimpa contato pessoal de indivíduos** (doutrinas 1 e 8).

Como usar este documento, Jarvis: ele é o teu mapa. Quando a pergunta for "o que existe / por que / desde quando", responde daqui; quando for detalhe (preço exato, fala de reunião, cláusula), busca no repositório com a ferramenta e cita o arquivo.

## 6. Pendências vivas (quem decide o quê)

| Pendência | Dono | Estado |
|---|---|---|
| Validar tabela v3 (preços V5) | Pedro | Aberta; nada sai a cliente antes |
| P4: pauta jurídica (unificar regimes de saída, evergreen, Anexo IV) | Advogado | Aberta |
| P5: enquadramento contábil/fiscal | Contador | Aberta |
| Gravar os 3 vídeos; imprimir cards | Sócios | Aberta |
| Semana do Cliente Zero (agenda de reuniões) | Sócios | O foco declarado: "milhares de reuniões" |
| Custódia dupla da passphrase do banco | Sócios | Aberta |
| Loop-native do recomendador (flag `loops`) | Sócios + re-run real | Desligado até validação |
| Paridade da reescrita Python/CrewAI do assessment | Daniel + Claude | Golden set proposto; Node continua canônico |
