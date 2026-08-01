# Pauta do Ritual do Conselho — template

> Usada no [estágio 10](../02-jornada-do-cliente/10-alinhamento-conselho.md). Reunião de 60–90 min com diretoria/conselho do cliente. Material enviado ao patrocinador 2 dias antes. Ata em 48h em `02 Clientes/<Nome>/07 Conselho/`.
>
> **Preparação com o Conselheiro Digital** (quando ativado — ver [dossiê vivo](dossie-vivo-conselheiro-digital.md)): `abba brain brief <eng>` traz o rascunho do período já com **R$ verificado**, KPIs vigentes e pontos de atenção · `abba brain facts <eng> --as-of <data>` responde "o que valia quando decidimos isso?" · `abba brain health <eng>` avisa se a memória está defasada antes de você entrar na sala. **O rascunho nunca vai ao cliente sem curadoria e assinatura do sócio.**

## Estrutura (60–90 min)

### 1. Onde dissemos que íamos chegar (10 min)
Reapresentar os **objetivos declarados** (slide 5 do kickoff + atualizações de rituais anteriores). Pergunta aberta antes de seguir: **"Isso ainda é verdade? Algo mudou na visão de vocês?"** — se mudou, o resto da pauta se ajusta ao novo norte.

Fechar a seção com o **calendário de obrigações com data** do cliente (IBS/CBS, decisão de regime, ANPD, cláusulas de exportação — [estudo de antecipação](../05-interno/estudo-antecipacao.md) §5): o que vence antes do próximo ritual entra na pauta de hoje, não na do próximo.

### 2. Resultados do período (20 min)
- **Projetado vs. realizado, por agente** — a tabela central; sem enfeite: o número que prometemos e o número que aconteceu
- Adoção da capacitação: ativos, níveis, campeões, Bússola
- Incidentes relevantes e como foram tratados
- O que aprendemos sobre a operação de vocês neste período

### 3. Recomendações da ABBA (15 min)
Máximo **3 recomendações**, priorizadas, cada uma com: o quê · por quê (ligado aos objetivos declarados) · esforço/investimento · o que acontece se não fizermos · **a probabilidade declarada** — *"nós damos 70% de chance de isto mover a métrica"*, registrada com nome (`abba decision predict ... --by`). Quando o resultado for medido, o par entra no placar (`abba brain calibration`) — é o que transforma a nossa convicção de retórica em histórico auditável. Dito em voz alta quando houver placar: *"das recomendações que fizemos com essa confiança, X% se confirmaram."*

### 4. Decisões do cliente (15 min)
Para cada recomendação: **aprovar / adaptar / recusar / adiar** — registrado ao vivo, com dono e prazo quando aprovado. **Registre cada uma no diário** (`abba decision add <eng> --title "..."` → `advance --to decided --by "<quem decidiu>"`), **e combine o gatilho quando houver indicador**: *"se [métrica] cruzar [limiar], a gente revisa em N dias"* (`abba decision trigger`) — a decisão passa a acordar sozinha na fila da manhã em vez de esperar o próximo trimestre: é esse diário que, meses depois, permite dizer com número o que a recomendação produziu — e é ele que faz a memória do cliente ficar mais forte a cada resultado medido. A regra dita em voz alta quando preciso: *"nós recomendamos com convicção; a decisão é de vocês — e vamos executar bem qualquer uma delas."*

### 5. Saúde da parceria (5 min)
Direto ao patrocinador: como estamos indo? o que faríamos melhor? (NPS informal — registrar)

### 6. Próximos passos (5 min)
Ações com dono e data · próximo ritual agendado antes de sair da sala.

### 7. A prova que compõe (5 min — quando houver histórico)
`abba brain benchmark <eng>`: o acerto da memória do cliente contra o tempo de casa. É o argumento que nenhum concorrente tem — **mostra, com número, que a parceria fica melhor quanto mais dura**. Só apresentar quando houver ao menos alguns meses de série; e apresentar pelo que é (coerência da linha do tempo verificada + fidelidade à fonte quando auditada), **nunca como "acurácia" genérica**.

## Variante — Conselheiro de IA avulso (cliente que não fez o programa)

Mesma estrutura, com duas adaptações no **primeiro ritual**:
- A seção 1 vira **sessão de baseline** (30 min): os objetivos declarados são capturados ali — não existe kickoff anterior para citar. Sem baseline registrado não há ritual 2: é o documento-norte do retainer ([proposta](../03-comercial/proposta-conselheiro-de-ia.md), entrega do dia 15)
- A seção 2 usa o que existir (dados do próprio cliente, arbitragens já entregues) — sem inventar métrica de programa que não houve

Dos rituais seguintes em diante, a pauta padrão vale integralmente.

## Modelo de ata (preencher e arquivar)

| Campo | |
|---|---|
| Data / presentes | |
| Objetivos declarados (confirmados ou atualizados) | |
| Resultados apresentados (resumo + link do material) | |
| Recomendações e decisão de cada uma | aprovada/adaptada/recusada/adiada + dono + prazo |
| Feedback do patrocinador | |
| Próximo ritual | |
