# Artefatos impressos: texto final para design (6 cards)

> **Origem:** Tier 1D do pacote "Academy Materiais Finais" (jul/2026),
> portado em 20/08/2026 **com as correções canônicas**: a 3ª pergunta da
> Bússola é **SÓ EU** (não "Continuar"), e a pontuação por rubrica usa os
> **quatro movimentos da Rubrica ABBA** (não o 4D licenciado). Este é o
> texto que vai para a arte final e a gráfica (pendência da fila de
> produção). Regra de produção física: [guia](guia-producao-fisica.md).

## 1. Card da Bússola das Três Perguntas

**PARAR:** O que posso parar de fazer porque a IA faz agora?
*Sub: O que faço no automático? O que é repetitivo e de baixo risco? O que eu adiaria sem culpa?*

**COMEÇAR:** O que posso começar a fazer porque a IA agora permite?
*Sub: O que eu não tenho tempo de fazer? Que análise eu evito por dar trabalho? Que ideia morre por falta de mãos?*

**SÓ EU** (O que só eu faço) e devo fazer ainda melhor?
*Sub: Onde está o meu julgamento? O que exige confiança humana e responsabilidade? O que perde valor se eu delegar?*

Rastreamento de versão: [ ] v0 (Kickoff) [ ] v1 (fim da aplicação no trabalho) [ ] v2 (pré-graduação) [ ] v3 (graduação, revisada com o gestor). Assinatura do gestor: ______

> ⚠️ O card legado dizia "CONTINUAR" na 3ª pergunta e "My Week With AI" na versão em inglês: **não imprimir o legado**.

## 2. Card Semáforo de Dados

**VERDE: pode usar em ferramenta homologada:** conteúdo público; dúvida conceitual; rascunho genérico; texto de site público; dado já divulgado pela empresa; material de marketing público; pergunta de estudo; template sem dados reais.

**AMARELO: só em ferramenta homologada:** rascunho de proposta; processo interno; ata interna; planilha sem dados pessoais; apresentação interna; código interno; plano de projeto; e-mail interno.

**VERMELHO, nunca em não homologada; homologada só com autorização:** CPF/RG; dados de saúde; dados bancários; salários; avaliações de desempenho; dados de clientes identificáveis; contrato sigiloso; segredo de negócio.

**Regra na dúvida:** se você não tem certeza da cor, é VERMELHO. Pergunte ao gestor ou ao encarregado de dados antes de colar.

## 3. Card do Esqueleto de Prompt ABBA

**Papel + Contexto + Tarefa + Formato + Exemplo + Restrições**

*Exemplo preenchido:* "Você é um analista de atendimento [Papel]. Recebemos as 3 reclamações abaixo de clientes de um plano B2B [Contexto]. Classifique por urgência e escreva um rascunho de resposta empática para cada [Tarefa]. Formato: tabela com colunas Reclamação, Urgência (Alta/Média/Baixa), Rascunho [Formato]. Como este exemplo: 'Cobrança duplicada | Alta | Olá, sinto muito...' [Exemplo]. Máx. 80 palavras por resposta; não prometa reembolso; se faltar dado, escreva [CONFIRMAR] [Restrições]."

## 4. Card da Lente de Oportunidade (com pontuação)

Quatro perguntas, marque Sim (1) / Não (0): **Frequente?** | **Estruturada?** | **Verificável?** | **Baixo risco?**

Pontuação: 4 = ótima candidata a automação · 2–3 = boa para trabalhar em parceria com a IA (com verificação) · 0–1 = provavelmente insubstituivelmente humana (**Pergunta SÓ EU da Bússola**).

## 5. Solution Canvas (A3)

**Bloco 1: Problema e dono:** Qual dor? Quem é o responsável? *Ex.: "Resumo de reuniões consome 5h/semana da equipe comercial. Dono: coordenador comercial."*
**Bloco 2: Dados e acessos:** Que dados? Qual cor no Semáforo? Que acessos? *Ex.: "Transcrições de reunião (amarelo). Ferramenta homologada [PERSONALIZAR]."*
**Bloco 3: Desenho da solução com gates humanos:** Passos + onde entra o humano? *Ex.: "IA gera resumo → coordenador revisa e aprova antes de enviar (gate humano obrigatório)."*
**Bloco 4: Riscos e verificação:** O que pode dar errado? Como checar? *Ex.: "Risco: resumo omitir decisão. Verificação: coordenador confere contra a pauta."*
**Bloco 5: Métrica de sucesso:** Como saber que funcionou? *Ex.: "Horas reinvestidas/semana; % de resumos aprovados sem edição."*

## 6. Ficha do Desafio Primeira Vitória

Campos: Nome | Área | Tarefa transformada | ANTES (tempo/passos) | DEPOIS (tempo/passos) | Prompt usado | Como verifiquei | Horas reinvestidas/semana | Cor do dado (Semáforo)

*Exemplo:* "Ana | Financeiro | Organizar despesas em tabela | ANTES: 40 min manual | DEPOIS: 5 min (revisão) | [prompt com Esqueleto] | Conferi somas por categoria na calculadora | ~3h/sem | Amarelo (valores anonimizados)."

---

## Rubricas de sala (para os kits de oficina: nos quatro movimentos)

**Rubrica de evidência (casos de uso), âncoras 1–5:**
- **Realidade** (1: hipotético / 3: tarefa real esporádica / 5: tarefa real recorrente com dado real anonimizado)
- **Método** (1: pedido de uma linha / 3: usa parte do Esqueleto / 5: Esqueleto completo + iteração pedido→crítica evidente)
- **Impacto** (1: sem medida / 3: economia estimada / 5: horas reinvestidas medidas e plausíveis)
- **Segurança** (1: ignora o Semáforo / 3: classifica os dados / 5: Semáforo + anonimização + gate humano documentados)

**Rubrica Batalha de Prompts (1–5 cada; vence a maior soma):** Escolha (tarefa adequada à IA) · Pedido (clareza/Esqueleto) · Crítica (verificou a saída) · Entrega (respeitou dados e levou ao resultado).

**Rubrica de demo do Build Day (4 critérios, 1–5):** funciona de verdade · gate humano bem desenhado · impacto plausível · reusabilidade.

**Rubrica teach-back do campeão:** clareza da explicação · fidelidade ao método da casa (movimentos + Bússola) · engajamento da turma · qualidade do feedback dado · correção técnica: 1 a 5 cada.
