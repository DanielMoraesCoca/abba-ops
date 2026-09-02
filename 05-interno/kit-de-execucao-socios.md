# Kit de Execução: as tarefas dos sócios, prontas para fazer

> **Camada:** interno. Cada seção abaixo é uma tarefa da lista de ativação transformada em coisa **executável hoje**: texto pronto para enviar, passo a passo com comandos, pauta pronta para reunião. Marcar a caixa quando feito e registrar a data.
>
> Ordem de execução: 1 e 2 hoje (independentes, ~40 min somados) · 3 esta semana (90 min de reunião) · 4 em paralelo (Pedro) · 5 depois de 1–4 · 6 depois de 5.

---

## 1. O e-mail para o advogado (P4 + P4b + R15): enviar HOJE

**Anexar:** o [contrato-esqueleto completo](../03-comercial/contrato-sow-esqueleto.md) (exportar em PDF ou Word: inclui os Anexos I–IV) e [uma cópia da licença CC BY-NC-SA do Método 4D].

**Texto pronto (ajustar o nome):**

> Assunto: Revisão jurídica: contrato de consultoria + 3 pontos específicos (prazo: temos primeira assinatura prevista para as próximas semanas)
>
> Dr(a). {{NOME}},
>
> Conforme conversamos, segue o contrato-mãe de prestação de serviços da ABBA com seus quatro anexos, para revisão. Três pontos pedem atenção específica além da revisão geral (LGPD, PI, limitação de responsabilidade):
>
> **1. Anexo IV. Contribuição Anonimizada e Rede (o mais urgente).** Nossa plataforma opera um comparativo estatístico entre clientes cuja premissa é que a contribuição anonimizada é divulgada em contrato. A minuta do anexo já traz as garantias técnicas (piso de 5 organizações, agregação irreversível, reciprocidade). Precisamos do seu parecer sobre: (a) se o legítimo interesse (Art. 7º, IX) basta para a cláusula IV.1 ou se convém consentimento expresso; (b) se o padrão "contribui, salvo recusa" é sustentável ou deve ser adesão ativa; (c) a redação de IV.5 sobre o que é irreversível após agregação; (d) a compatibilidade da adesão individual de colaboradores (IV.4) com políticas de RH do cliente. **Este anexo precisa estar válido no primeiro contrato que assinarmos**: consentimento não se retroage.
>
> **2. Licença do material pedagógico.** Parte do nosso material de capacitação deriva do "Método 4D", licenciado sob Creative Commons BY-NC-SA (cláusula não-comercial). Usamos em programa pago, com atribuição. Precisamos saber: isso configura uso comercial vedado? Se sim, quais as alternativas (licença direta com o autor, substituição do material, transformação suficiente)?
>
> **3. Cláusula de estudo de caso (Anexo III)**: confirmar se a redação de aprovação prévia + direito de retirada é suficiente.
>
> Prazo ideal: retorno em até {{7}} dias úteis, mesmo que parcial (o Anexo IV pode vir antes do resto). Qualquer dúvida, temos documentação técnica detalhada de cada garantia mencionada.
>
> Obrigado, {{Daniel}}

- [ ] Enviado em: ____ · Retorno recebido em: ____

**E a cobrança do contador (P5), no mesmo dia: mensagem curta:**

> {{Nome}}, tudo bem? Seguimos aguardando a confirmação do enquadramento (Simples Anexo III via Fator R) que conversamos em julho. Temos primeira nota fiscal prevista para as próximas semanas: consegue nos confirmar até {{data, 5 dias úteis}}? Se faltar algum documento nosso, me diz que envio hoje.

- [ ] Cobrança enviada: ____ · Enquadramento confirmado: ____

---

## 2. A cerimônia da passphrase: 30 minutos, os dois sócios juntos

Pré-requisito de QUALQUER dado de cliente. Fazer numa chamada ou presencial, os dois:

1. **Gerar** (no terminal de quem hospeda o assessment-brain):
   ```bash
   openssl rand -base64 30        # gera a ABBA_DB_PASSPHRASE (~40 caracteres)
   openssl rand -base64 30        # gera a ABBA_BACKUP_PASSPHRASE (DIFERENTE da primeira)
   ```
2. **Guardar nos dois gerenciadores de senha**: cada sócio salva AS DUAS no seu (1Password/Bitwarden/etc.), título "ABBA DB passphrase" e "ABBA backup passphrase". Nunca em nota de celular, WhatsApp ou e-mail.
3. **Envelope físico:** imprimir (ou escrever à mão) as duas, selar em envelope, os dois assinam sobre o lacre, guardar **fora do escritório** (casa de um dos dois, cofre, gaveta dos pais). Anotar onde: ____
4. **Configurar a máquina de produção:**
   ```bash
   cd /caminho/assessment-brain
   cp .env.example .env && chmod 600 .env
   # editar .env: ANTHROPIC_API_KEY, ABBA_DATA_DIR (caminho ABSOLUTO),
   # ABBA_DB_PASSPHRASE, ABBA_BACKUP_PASSPHRASE, ABBA_BRAIN_MAX_USD=1
   node bin/abba.js doctor          # tudo verde?
   node bin/abba.js doctor --live   # a chave FUNCIONA (gasta ~1 token)
   ```
5. **Apagar** qualquer lugar temporário onde as senhas passaram (terminal com histórico: `history -c`; arquivo rascunho: apagar).

- [ ] Feito em: ____ · Envelope está em: ____

---

## 3. A reunião de sócios: pauta pronta (90 min, decidir as 5)

Regras: toda decisão sai com registro no [log](registro-de-decisoes.md) na hora; o que não se decidir sai com DATA de decisão, não com "depois".

| # | Decisão (tempo) | Opções | Recomendação preparada |
|---|---|---|---|
| 1 | **Faixa de faturamento do alvo** (10') | (a) confirmar R$ 50–500 mi · (b) ajustar | **(a)** · coerente com a tabela de preços e com o ticket de conforto (R$ 30–150k/fase). Ajustar depois com dado real é barato |
| 2 | **Preço v2 e o ritual semanal** (30') | (a) manter v1 vigente; semanal incluída nas camadas Evolução+ ao preço atual durante o charter; revisar após as 3 primeiras reações reais de preço (a regra que já existe) · (b) ativar v2 já | **(a)** · não mudar preço sem reação de mercado; a semanal vira argumento de valor do charter, não linha de preço. Decidir também: o Conselheiro **Trimestral** fica SEM semanal (cadência é a do produto) · confirmar |
| 3 | **P3 · nome do programa** (10') | (a) decidir agora · (b) fixar critérios e decidir com o site | **(b)** · mas sair da reunião com 3 candidatos anotados e o critério: nome em português, sem "IA" genérico, que caiba na frase do manifesto |
| 4 | **Caça ao Dinheiro + Resgate** (20') | (a) aprovar preparação dos one-pagers agora, lançamento pós-Cliente Zero · (b) adiar tudo | **(a)** · os estudos estão completos com to-dos prontos; preparar não é lançar, e a porta do CFO é a mais quente do mercado ([estudo](estudo-ia-financeira.md) §4) |
| 5 | **As 5 tensões da Visão 2029** (20') | Não são para resolver · são para cada sócio declarar posição | Ler [visao-2029.md §8](../00-identidade/visao-2029.md) ANTES da reunião. Na mesa: cada um diz, por tensão, para que lado pende e por quê. Registrar as divergências · elas são o mapa das brigas futuras, melhor tê-las mapeadas |

- [ ] Reunião feita em: ____ · Decisões registradas: V____

---

## 4. Checklist do Pedro (paralelo a tudo: ~2h somadas)

1. **R23: cron do portal** (15'): no painel da Vercel, ver se `/api/cron/compass-cadence` executou nas últimas 24h (aba Crons/Logs). Se roda: apagar o comentário obsoleto no cabeçalho do arquivo. Se não roda: remover a entrada do `vercel.json` ou ligar de verdade. **um dos dois lados tem que ceder**. Registrar o achado no [registro de riscos](registro-de-riscos.md).
2. **R16: código do assessment web** (o mais importante): commitar no repositório o código que está rodando em produção (`assessment.abbaservices.com.br`). Regra permanente dali em diante: produção só roda código versionado.
3. **Provedor de busca do scout** (15'): conferir no ambiente de produção qual chave existe (`EXA_API_KEY`? `BRAVE_API_KEY`?) e rodar `node bin/abba.js scout "Empresa Teste" --industry varejo`: o brief NÃO pode sair carimbado "SYNTHETIC DESK RESEARCH". Registrar qual é e o custo por execução no [mapa de ferramentas](../06-ferramentas/mapa-jornada-ferramentas.md).
4. **CrewAI (R9)** (decisão com o Daniel): Enterprise vs. self-host. Critério simples: se o 1º cliente com construção assina em <60 dias, Enterprise (rápido, caro); senão, self-host com tempo de maturar. Refletir o custo na [planilha de precificação](../03-comercial/precificacao-planilha.md).

- [ ] R23: ____ · R16: ____ · Busca: ____ · CrewAI: ____

---

## 5. A semana do Cliente Zero: agendar 5 dias seguidos

**Pré-requisitos (não começar sem):** seções 1–4 feitas · `doctor --live` verde · vídeos: pelo menos os 3 de maior alavancagem gravados (1.3.3, 1.3.1, 2.1.2: roteiros prontos em [materiais](../08-materiais/README.md)).

**O roteiro dia a dia já existe:** [cliente-zero-runbook.md](cliente-zero-runbook.md). O que esta rodada acrescentou ao ensaio:

- **Ligar o cron do sono de verdade** na semana ([runbook de ativação §2](../06-ferramentas/runbook-ativacao.md)): `crontab -e` com `MAILTO` + conferir o log na manhã seguinte.
- **Ensaiar o ritual semanal** uma vez com cliente fictício: `abba brain next <eng>` → os 4 itens → registrar decisão com gatilho (`decision add` → `decision trigger`) → declarar probabilidade (`decision predict`) → medir (`decision outcome`) → conferir que o gatilho conferido sai da fila (`decision trigger --checked`).
- **Testar o restore**: `abba backup` → apagar em pasta descartável → `abba restore` → conferir que banco E entregáveis voltam.
- **Critério de saída** (do runbook): jornada completa sem improviso. Cada travada = gap corrigido em ambiente seguro.

- [ ] Semana agendada: ____ a ____ · Critério de saída atingido: ____

---

## 6. A rua, só depois do 5

1. **Lista de 20 alvos nomeados** no [pipeline](../03-comercial/pipeline-modelo.md), da rede real de vocês. Para cada um: o placar 0–6 do [teste do alvo](../00-identidade/alvo.md) (as 3 primeiras perguntas dá para estimar antes mesmo da conversa) e a **obrigação com data** dele (pergunta 6): quem tem prazo compra primeiro, e a validação IBS/CBS está em produção AGORA.
2. **Cadência:** 10 contatos novos/semana · degustação aceita = Mapa de Vazamento entregue em 5 dias úteis · [coreografia](../03-comercial/coreografia-da-conversao.md) em cada passo · retrospectiva de 10 min após cada conversa real.
3. **O material da mesa:** [kit de presença](../03-comercial/kit-de-presenca.md) (30s/3min/1página, com as 3 objeções respondidas: inclusive "quantas empresas vocês já atenderam?") · [escada](../03-comercial/escada-abba.md) · [protocolo de prova](../04-entrega/protocolo-de-prova.md).
4. **Meta do trimestre: 1 cliente charter.** Ele resolve de uma vez: R1 (validação real), cofre vazio, primeiro caso publicável, primeiro ponto da curva de tenure.

- [ ] Lista de 20 fechada: ____ · Primeiro contato: ____ · Charter assinado: ____

---

## O placar deste kit

| Seção | Estado |
|---|---|
| 1. E-mail ao advogado | ⬜ |
| 2. Cerimônia da passphrase | ⬜ |
| 3. Reunião das 5 decisões | ⬜ |
| 4. Checklist do Pedro | ⬜ |
| 5. Semana do Cliente Zero | ⬜ |
| 6. A rua | ⬜ |

Quando as 6 estiverem ✅, a ABBA deixou de ser um sistema pronto e virou uma empresa operando. O [mapa](../00-identidade/mapa-da-abba.md) é atualizado a cada uma que fechar.
