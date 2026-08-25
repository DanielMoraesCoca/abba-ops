# Checklist de Documentos — Avaliação de Prontidão

O que pedir ao cliente, quando, com que base legal, e o que **nunca** aceitar. Enviada com o [e-mail 2](emails-imersao.md#e-mail-2) em D-7, antes do kickoff.

> **A lista viva é a da ferramenta.** `abba kickoff <engajamento> --output` imprime esta checklist já filtrada pelo perfil do setor do engajamento (os arquétipos de vazamento prioritários mudam o que pedir primeiro). Este documento é a moldura humana e jurídica: o que a lista significa, por que pedimos, e os limites que a ferramenta não decide por nós.

**Regra de duas colunas:** todo pedido é **obrigatório antes do campo** ou **desejável em até 30 dias**. Obrigatório segura o início do campo; desejável nunca segura nada — chega quando chegar e afina a análise ([plano B no protocolo](protocolo-de-imersao.md#plano-b--pré-trabalho-e-documentos-não-entregues)).

**Como cada documento entra na ferramenta:** `abba ingest <eng> <arquivo> --level internal_data --phase 0 --date <data-do-documento>`. Formatos aceitos: PDF, DOCX, XLSX/CSV, MD/TXT, imagens (OCR) e áudio (transcrição). PPTX ainda não: pedir exportação em PDF.

---

## 1. Financeiro

Base legal: dados de pessoa jurídica não são dados pessoais; tratamento coberto pela execução do contrato. Cuidado apenas com planilhas que tragam nomes + salários (ver seção "não pedir").

| Documento | Prioridade | Quem entrega | Por que pedimos |
|---|---|---|---|
| DRE gerencial dos últimos 12 meses | Obrigatório | CFO / Controladoria | Ancora toda quantificação de vazamento em números reais, não em estimativa |
| Margem bruta por linha de produto/serviço | Obrigatório | CFO | Detecta erosão de margem que a empresa não internalizou |
| Orçamento e gasto real de TI/SaaS (por ferramenta) | Obrigatório | CFO / Procurement | Shadow IT, licenças duplicadas, renovações automáticas |
| Calendário de renovação de contratos SaaS | Desejável | Procurement | Sequencia as decisões de corte |
| Métricas de utilização por assento das 20 maiores ferramentas | Desejável | TI / Procurement | Assentos pagos e não usados |
| CAC e mix de receita nova por produto (8 trimestres) | Desejável | CFO / Comercial | Deslocamento de mix não internalizado |

## 2. Processos e operação

| Documento | Prioridade | Quem entrega | Por que pedimos |
|---|---|---|---|
| Mapa ou descrição dos 5 processos mais críticos (mesmo informal) | Obrigatório | COO / Gestores | O processo real, não o desenhado, é o objeto da análise |
| Exportação de tickets/chamados dos últimos 6 meses (contagens e categorias bastam) | Obrigatório | TI / Operações | Retrabalho, exceções, triagem repetida |
| Atas ou minutas do comitê de direção dos últimos 6 meses | Obrigatório | Patrocinador | Decisões que atrasam e o custo do atraso |
| Exportação de agenda: reuniões recorrentes + participantes (metadados, sem conteúdo) | Desejável | TI / Assistente executiva | Custo de coordenação: gente × duração × frequência |
| Registros de apontamento de horas (agregados por área) | Desejável | RH / Operações | Trabalho manual que ninguém custeou |
| Postmortems de incidentes por integração | Desejável | TI / Engenharia | Fragilidade de integrações |
| Logs de erro e taxas de falha de QA por processo | Desejável | TI / Qualidade | Custo de retrabalho e exceção |

## 3. Sistemas e dados

| Documento | Prioridade | Quem entrega | Por que pedimos |
|---|---|---|---|
| Inventário de sistemas (nome, função, dono, integrações) | Obrigatório | TI | O mapa do organismo; sem ele toda dimensão técnica é chute |
| Lista de fornecedores de tecnologia com contratos vigentes | Obrigatório | TI / Procurement | Dependências e aprisionamento |
| Diagrama ou descrição de fluxo de dados entre sistemas (mesmo rabisco) | Desejável | TI | Onde o dado é redigitado é onde o processo quebrou |
| Painéis/dashboards em uso pela diretoria (prints servem) | Desejável | Patrocinador | O que a empresa de fato mede |
| Relatórios de auditoria interna/externa mais recentes + status dos apontamentos | Desejável | Compliance / Jurídico | Bombas-relógio regulatórias com consequência em reais |
| Inventário de acordos de tratamento de dados (DPAs) com status | Desejável | Jurídico / DPO | Prontidão LGPD do próprio cliente |

## 4. Pessoas e organização

Aqui mora o maior risco LGPD. A regra: **o agregado serve, o nominal não.**

| Documento | Prioridade | Quem entrega | Por que pedimos |
|---|---|---|---|
| Organograma com cargos e áreas (nomes de lideranças apenas) | Obrigatório | RH / Patrocinador | Mapa de entrevistas e de influência |
| Headcount e massa salarial POR ÁREA (agregado, sem nomes) | Obrigatório | RH / CFO | Custo carregado das horas manuais |
| Lista de participantes do assessment (nome, cargo, e-mail, área) | Obrigatório | Ponto focal | Agendamento e pré-trabalho; base legal: execução do contrato + transparência |
| Cobertura de documentação por área (% de processos com runbook) | Desejável | Operações | Concentração de conhecimento em pessoas únicas |
| Profundidade de escala de plantão por sistema | Desejável | TI | Ponto único de falha humano |
| Indicadores agregados de rotatividade por área (últimos 12 meses) | Desejável | RH | Risco de evasão de conhecimento |

---

## NÃO PEDIR / NÃO RECEBER

Nunca pedimos — e se chegar, não ingerimos:

| Nunca | Por quê |
|---|---|
| Folha de pagamento nominal (nome + salário individual) | Dado pessoal desnecessário à finalidade; o agregado por área responde a mesma pergunta |
| Dados de saúde, prontuários, atestados, dados de plano de saúde | Dado sensível (LGPD art. 5º, II); saúde está explicitamente fora do escopo da ferramenta |
| Dados de menores de idade | Regime especial (art. 14); nenhuma finalidade do assessment os justifica |
| Dados bancários, cartões ou credenciais de pessoas físicas | Desnecessários e de alto risco; finanças que importam são as da PJ |
| Biometria, fotos de documentos, dados de geolocalização individual | Sensíveis ou de alto risco, sem finalidade no assessment |
| Conteúdo de e-mails/mensagens individuais de colaboradores | Expectativa de privacidade; pedimos metadados agregados (volumes, categorias), nunca conteúdo pessoal |
| Dados de clientes finais do cliente (bases de CRM nominais) | Somos Operadora do NOSSO cliente; a base de clientes dele tem outra finalidade. Amostras anonimizadas ou agregados resolvem |

**Se chegar mesmo assim** (cliente manda a folha nominal inteira, por exemplo):
1. **Não ingerir** o arquivo na ferramenta.
2. Avisar o ponto focal no mesmo dia: "recebemos X; não precisamos e não vamos usar; segue o que serve no lugar" (modelo no [e-mail 5](emails-imersao.md#e-mail-5)).
3. Apagar o arquivo recebido dos nossos sistemas e registrar o episódio na pasta do cliente (data, o que era, o que foi feito).
4. Pedir a versão agregada/anonimizada da coluna "por que pedimos".

**Rede de segurança não é licença.** A ferramenta redige CPF, CNPJ, e-mails e nomes automaticamente na ingestão — isso protege contra o acidente residual, não autoriza receber o que esta seção proíbe.

---

## Papel da ABBA e ciclo de vida do dado

- **Operadora:** tratamos os dados sob instrução do cliente (Controlador), exclusivamente para a finalidade do contrato ([proposta §11](../03-comercial/proposta-avaliacao-prontidao.md)). Suboperadores (provedores de LLM e nuvem) listados no Anexo II do [contrato](../03-comercial/contrato-sow-esqueleto.md).
- **Minimização e transparência:** só entra o que tem linha nesta checklist; pedido fora dela exige justificativa nova, por escrito.
- **Retenção:** o prazo é o do contrato e fica registrado no engajamento da ferramenta; sem cláusula específica, aplica-se o padrão de 18 meses após o arquivamento.
- **Eliminação com prova:** ao término (ou a pedido), `abba forget` elimina relatórios, fontes e derivados em cascata e emite **certificado de eliminação com contagem de resíduo zero** — entregável ao cliente como evidência de atendimento LGPD.
- **O que nunca sai daqui:** dados de um cliente jamais aparecem para outro. O acervo entre clientes guarda apenas padrões anonimizados por construção (empresa vira "[Company]", pessoa vira "[Role]", valores viram faixas).
