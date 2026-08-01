# Apostas Futuras — registradas, não ativas

> Ideias estratégicas boas demais para perder, mas que **não são a identidade atual** (decisão de 2026-07-22: consulting-first). Cada aposta tem gatilho de reavaliação — quando o gatilho acender, vira pauta de reunião de sócios.

## Aposta 1 — Plataforma como produto SaaS standalone

**O que é:** a visão documentada em `abba-portal/docs/platform/01_VISION.md` (histórico): o portal de capacitação vendido como produto por assento (SaaS por níveis), com a consultoria como um dos canais de venda; marketplace de agentes; parcerias de conteúdo.

**Por que não agora:** exige conteúdo completo nos 4 níveis, autenticação corporativa madura, billing, suporte self-serve e marca — tudo enquanto o negócio de consultoria ainda não tem o primeiro cliente. Vender consultoria financia e valida a plataforma; o inverso não.

**Gatilhos de reavaliação:**
- [ ] 5+ clientes de consultoria usando a plataforma com adoção comprovada
- [ ] Pedido espontâneo de 2+ empresas para "só a plataforma"
- [ ] Conteúdo dos níveis Praticante+ completo e revisado

## Aposta 2 — Degustação como widget público self-service ✅ REALIZADA (2026-07)

**Virou realidade antes do previsto:** existe um assessment ao vivo em `assessment.abbaservices.com.br`, gerando relatórios profundos por informação pública (ex.: Brasal, 42 págs, jul/2026). A aposta sai daqui e vira operação: alinhamento de marca/nomes/CTA e estratégia de gating no [Caminho Crítico](../05-interno/plano-de-acao.md) e no [estágio 02](../02-jornada-do-cliente/02-diagnostico-gratuito.md).

## Aposta 3 — Verticalização por setor

**O que é:** pacotes por vertical (jurídico, saúde, financeiro) com material, benchmarks e agentes de prateleira por setor. Material de jurídico/serviços profissionais já existe (histórico em `abba-portal/docs/industry/`).

**Decisão dos sócios (2026-08-01): não verticalizar agora.** O eixo de densidade escolhido é **forma, não indústria** — maturidade de adoção + moldura regulatória brasileira, que é o que os benchmarks do portal já calculam sem olhar setor e o que a lei fiscal padroniza em qualquer ramo ([alvo](alvo.md)). O custo dessa escolha fica registrado no próprio [alvo](alvo.md): sem densidade setorial, o cofre demora mais a virar produto de setor.

**Gatilhos (mantidos):** 3+ clientes no mesmo setor · padrões repetidos no vault do assessment-brain. Se acenderem por acaso, a decisão é reavaliada com dado.

## Aposta 4 — Ecossistema entre clientes (rede + benchmark) — **infraestrutura CONSTRUÍDA, ativação gateada**

**O que é:** as três camadas do [ecossistema](ecossistema.md) — benchmark recíproco entre empresas, rede de campeões e credencial portátil entre pessoas, cofre de padrões virando boletim de mercado.

**Status (2026-08-01): deixou de ser aposta de papel.** O levantamento do `abba-portal` mostrou que o mecanismo está em código e apenas invisível: benchmarks de fluência e durabilidade entre clientes (com pisos de privacidade de 5 clientes/5 pessoas), opt-in **recíproco** de contribuição em banco, credenciais verificáveis portáteis e um plano de ativação da rede em três estágios. O benchmark hoje renderiza **só para a equipe ABBA**. O que falta não é engenharia — é contrato, doutrina e clientes.

**Gatilhos:**
- [ ] **Anexo IV do [contrato](../03-comercial/contrato-sow-esqueleto.md)** validado pelo advogado (P4) — **caminho crítico irreversível**: consentimento não se retroage
- [ ] 3+ clientes com campeões graduados → rede de campeões (Estágio 1: grupo facilitado)
- [ ] 5+ clientes qualificados → benchmark deixa de ser interno e aparece ao patrocinador
- [ ] 8+ clientes → primeiro boletim público de mercado

## Aposta 5 — Conselheiro Digital (o "JARVIS por cliente")

**O que é:** um cérebro de IA por cliente — Dossiê Vivo (assessment + plano diretor + relatórios + telemetria) + análise proativa mensal + interface de consulta (evolução da Iris) — que abastece o Conselheiro de IA humano e aprende com os resultados reais via loop de outcomes. **Modelo centauro obrigatório:** a IA gera, o Conselheiro cura e assina, a diretoria decide. Estudo completo com pesquisa, riscos (PL 2338, alucinação, LGPD) e arquitetura: [estudo](../05-interno/estudo-conselheiro-digital.md).

**Status (2026-08-01): CONSTRUÍDO ANTECIPADAMENTE por decisão do sócio — esta aposta deixou de ser aposta.** Fases 0–2 **+ Ondas 1–3 de memória** entregues em código no assessment-brain: memória bitemporal com autoridade de origem, ciclo noturno com teto de gasto, diário de decisões, loop de aprendizado com gate humano, reforço por resultado medido, consolidação em tiers, auditoria noturna da própria memória, playbooks procedurais e benchmark longitudinal. **Cinco rodadas de revisão adversarial independente (50 defeitos corrigidos), suíte 414/414 nos dois modos, migrações 029–045.** Operação em [`../04-entrega/dossie-vivo-conselheiro-digital.md`](../04-entrega/dossie-vivo-conselheiro-digital.md); estratégia de longo prazo em [`visao-2029.md`](visao-2029.md).

**Gatilhos de reavaliação:**
- [x] ~~Fase 1: 1º cliente em manutenção~~ → **construída antes do gatilho** (Dossiê Vivo + brief mensal curado)
- [x] ~~Fase 2: 1º cliente na camada Estratégia~~ → **construída antes do gatilho** (loop de aprendizado + soul por cliente)
- [ ] Fase 3: 3+ clientes → interface Iris-Empresa no portal (**parcialmente antecipada**: tier procedural e benchmark entregues na Onda 3; a interface segue gateada)
- [ ] Cláusula de consentimento para destilação anonimizada ao vault na pauta do advogado (P4) antes da ativação
- [ ] **ATIVAÇÃO com dados reais** — o que de fato falta: validação com LLM real, golden set calibrado pelos sócios e cron do sono ligado ([runbook](../06-ferramentas/runbook-ativacao.md))

## Aposta 6 — O Radar (varredura regulatória e de sinal fraco por cliente)

**O que é:** varredura mensal por cliente — mudança regulatória com data (reforma tributária, ANPD, cláusulas de exportação), movimento de concorrente e sinal fraco setorial — entrando como seção do brief mensal, com curadoria humana. A fase de varredura ficou barata com LLM; a curadoria continua sendo o serviço. Especificado no [estudo de antecipação](../05-interno/estudo-antecipacao.md) §6.

**Por que não agora:** custo de API recorrente por cliente antes de existir cliente; risco de virar ruído sem calibração; e depende de resolver qual provedor de busca está ativo em produção (pendência do Pedro, [mapa de ferramentas](../06-ferramentas/mapa-jornada-ferramentas.md)).

**Gatilhos:**
- [ ] 1º cliente pagante em manutenção (degrau 3)
- [ ] Provedor de busca do scout confirmado e configurado
- [ ] Custo estimado por cliente/mês medido em ensaio interno

## Regra

Aposta futura não recebe investimento de tempo além de: (a) manter este registro atualizado; (b) não tomar decisões hoje que **impossibilitem** a aposta amanhã (ex.: contratos que proíbam comunidade entre clientes sem necessidade).
