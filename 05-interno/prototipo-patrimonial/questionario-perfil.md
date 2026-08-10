# Protótipo Patrimonial — Questionário de Perfil v0

> **Camada:** interno (engenharia de protótipo). Parte do pacote [prototipo-patrimonial](plano-de-construcao.md). Instrumento autoral da ABBA, construído do zero — não deriva de material de terceiros. É o único input do sistema: dele nasce o `PerfilEstruturado` (schema no scaffold), que alimenta o gate de red flags e as crews.
>
> **Quem responde:** o advogado/consultor JUNTO com o cliente (nunca o cliente sozinho num formulário frio — a qualidade da resposta é a qualidade da análise). Tempo-alvo: 45–60 min.
>
> Dono: engenharia (estrutura) + advogado nomeado (validação das perguntas antes do GO/NO-GO).

---

## Desenho geral

- **6 seções, 38 perguntas.** A seção D (passivos e litígios) é a mais importante: alimenta o gate 1 — e é deliberadamente a 4ª, não a 1ª (rapport antes de perguntas duras).
- **Ramificação**: perguntas marcadas `→` só aparecem se a anterior for "sim".
- **Red flags duros (🛑)**: resposta que **encerra a análise automática** — o caso vai direto para "parecer humano primeiro", sem desenho de estrutura. Não é recusa do cliente; é reconhecimento de que o caso começa por regularização/aconselhamento humano.
- **Red flags brandos (⚠️)**: seguem para análise, mas o desenho é obrigado a endereçá-los explicitamente.
- Cada pergunta mapeia para um campo do `PerfilEstruturado` (coluna "Campo").

## Seção A — Identificação e residência fiscal (5 perguntas)

| # | Pergunta | Campo |
|---|---|---|
| A1 | Nome, idade, estado civil e regime de bens do casamento (se houver) | `pessoa.{nome, idade, estado_civil, regime_bens}` |
| A2 | País de residência fiscal atual; passa mais de 183 dias/ano no Brasil? | `pessoa.residencia_fiscal` |
| A3 | Possui outras cidadanias ou vistos de residência? Quais? | `pessoa.cidadanias[]` |
| A4 | É "US person" (cidadania/green card/substantial presence nos EUA)? | `pessoa.us_person` (⚠️ ativa trilha FATCA) |
| A5 | Há planos concretos de mudança de país nos próximos 5 anos? | `pessoa.mudanca_planejada` |

## Seção B — Família e sucessão (8 perguntas)

| # | Pergunta | Campo |
|---|---|---|
| B1 | Filhos: quantos, idades, de quais uniões? Algum menor ou incapaz? | `familia.filhos[]` |
| B2 | Cônjuge/companheiro(a) atual: há união estável formalizada? Pacto antenupcial? | `familia.conjuge` |
| B3 | Ex-cônjuges com pendências patrimoniais (partilha aberta, pensões)? | `familia.ex_conjuges[]` (⚠️) |
| B4 | Pais vivos? Dependentes financeiros além de filhos? | `familia.outros_dependentes[]` |
| B5 | Herdeiros residentes fora do Brasil? Onde? | `familia.herdeiros_exterior[]` (ativa trilha multi-jurisdição) |
| B6 | Existe testamento? Doações em vida já feitas (com ou sem reserva de usufruto)? | `sucessao.instrumentos_existentes[]` |
| B7 | O(a) sr(a). deseja tratar herdeiros de forma DESIGUAL além da parte disponível (50%)? | `sucessao.desejo_desigual` (🛑 se a intenção declarada for suprimir a legítima de herdeiro necessário — a legítima é ordem pública; o desenho pode otimizar a parte disponível, nunca burlar a legítima) |
| B8 | Há conflito familiar relevante (herdeiros brigados, sucessão litigiosa em curso)? | `sucessao.conflito` (⚠️) |

## Seção C — Patrimônio e veículos (9 perguntas)

| # | Pergunta | Campo |
|---|---|---|
| C1 | Inventário de ativos por classe e ordem de grandeza: imóveis BR, imóveis exterior, participações societárias, aplicações BR, aplicações exterior, agro/rural, outros | `patrimonio.ativos[]` |
| C2 | Em quantos CNPJs figura como sócio/administrador? Atividade e porte de cada um | `patrimonio.cnpjs[]` |
| C3 | Já existe holding familiar ou estrutura societária de organização? Qual, desde quando, com que propósito documentado? | `patrimonio.estruturas_br[]` |
| C4 | → Se holding: há bens de uso pessoal (casa, carros) dentro da PJ? | `patrimonio.uso_pessoal_na_pj` (⚠️ risco de confusão patrimonial — CC art. 50) |
| C5 | Possui estruturas no exterior (empresa, trust, fundação, conta)? Quais, onde, desde quando? | `patrimonio.estruturas_ext[]` |
| C6 | → Se sim: estão declaradas no IRPF e na DCBE/Bacen (quando ≥ US$ 1 mi)? | `conformidade.declarado_irpf_dcbe` (🛑 se NÃO — existe ativo no exterior não declarado: o caso é de regularização com advogado/contador ANTES de qualquer desenho; seguir desenhando seria construir sobre um ilícito penal — Lei 7.492, art. 22) |
| C7 | Ativos em nome de terceiros (parentes, "laranjas", interpostas pessoas)? | `patrimonio.em_nome_de_terceiros` (🛑 — regularização primeiro, com advogado; o sistema não desenha sobre interposição) |
| C8 | Bens rurais: há regularização fundiária/ambiental pendente (CAR, geo, ITR)? | `patrimonio.rural_pendencias` (⚠️) |
| C9 | Expectativa de liquidez relevante nos próximos 3 anos (venda de empresa, exportação, contrato grande)? | `patrimonio.evento_liquidez` |

## Seção D — Passivos, litígios e exposição (7 perguntas) — alimenta o gate 1

| # | Pergunta | Campo |
|---|---|---|
| D1 | Dívidas relevantes hoje (bancárias, fiscais, com pessoas físicas)? Em dia? | `passivos.dividas[]` |
| D2 | Processos em curso CONTRA o(a) sr(a). ou suas empresas (cível, trabalhista, fiscal)? Valor estimado somado | `passivos.processos_reu[]` (🛑 se houver passivo relevante exigível ou iminente E a motivação declarada incluir "proteger os bens disso" — transferência nesse cenário é fraude contra credores/à execução; CC arts. 158–165, CPC 792) |
| D3 | Execuções fiscais, dívida ativa, parcelamentos em aberto? | `passivos.fiscal[]` (⚠️/🛑 conforme materialidade) |
| D4 | Já sofreu desconsideração de personalidade jurídica ou bloqueio de bens? | `passivos.historico_desconsideracao` (⚠️ forte) |
| D5 | Atividade com alta litigiosidade inerente (incorporação, saúde, agro com passivo ambiental)? | `passivos.exposicao_setorial` |
| D6 | Avais e fianças pessoais concedidos? Para quem, quanto? | `passivos.avais[]` (⚠️) |
| D7 | Existe seguro (D&O, vida, responsabilidade) contratado? | `passivos.seguros[]` |

## Seção E — Objetivos e horizonte (5 perguntas)

| # | Pergunta | Campo |
|---|---|---|
| E1 | Ordene por importância: sucessão organizada · eficiência tributária LÍCITA · proteção contra litigiosidade FUTURA · internacionalização de investimentos · governança familiar | `objetivos.prioridades[]` |
| E2 | O que o(a) sr(a). quer que aconteça com o patrimônio na sua falta? (resposta livre, capturada verbatim) | `objetivos.visao_sucessoria` |
| E3 | Horizonte: isso é para resolver em meses (evento à vista) ou estruturar em anos? | `objetivos.horizonte` |
| E4 | Apetite por complexidade e custo recorrente de manutenção (estruturas no exterior custam para manter e declarar todo ano) | `objetivos.apetite_custo` |
| E5 | Alguma jurisdição/veículo que o(a) sr(a). já considera ou rejeita? Por quê? | `objetivos.preferencias` |

## Seção F — Conformidade atual (4 perguntas)

| # | Pergunta | Campo |
|---|---|---|
| F1 | IRPF em dia e completo? Quem assessora (contador/advogado tributarista)? | `conformidade.irpf` |
| F2 | Optou por algum regime da Lei 14.754 (transparência de offshore; atualização de bens)? | `conformidade.regime_14754` |
| F3 | Origem do patrimônio principal documentável (venda de empresa, herança, atividade)? | `conformidade.origem_recursos` (🛑 se não documentável — KYC falha; caso não entra) |
| F4 | Disposição declarada: *"toda estrutura desenhada será integralmente declarada ao fisco brasileiro e tributada conforme a lei"* — o cliente confirma? | `conformidade.aceite_transparencia` (🛑 se NÃO — o produto não desenha ocultação; é o aceite que protege o advogado, a ABBA e o próprio cliente) |

## Os 6 red flags duros (resumo do gate 1)

| # | Flag | Origem | Rota |
|---|---|---|---|
| 1 | Ativo no exterior não declarado | C6 | Regularização (advogado/contador) antes de qualquer desenho |
| 2 | Bens em nome de terceiros/interpostas pessoas | C7 | Regularização assistida por advogado |
| 3 | Passivo exigível + motivação de blindagem contra ele | D2/D3 | Parecer humano; desenho vedado (fraude a credores) |
| 4 | Intenção de suprimir legítima de herdeiro necessário | B7 | Reenquadrar objetivo (parte disponível); parecer humano |
| 5 | Origem de recursos não documentável | F3 | Caso não entra (KYC) |
| 6 | Recusa do aceite de transparência | F4 | Caso não entra |

> Os red flags duros não são "burocracia": são o que mantém o produto do lado certo da lei, o advogado protegido, e — comercialmente — são o nosso diferencial de confiança: *"a primeira coisa que o nosso sistema faz é dizer NÃO para o caso errado"*.

## Ligações

[Plano de construção](plano-de-construcao.md) · [Especificação dos agentes](especificacao-agentes.md) (o gate 1 implementa esta tabela) · Scaffold: `scaffold/src/patrimonio_flow/schemas.py` (o `PerfilEstruturado`) e `gates.py` (a triagem)
