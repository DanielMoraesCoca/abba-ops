# Protótipo Patrimonial — Corpus de Conhecimento (a base do RAG)

> **Camada:** interno (engenharia de protótipo). Parte do pacote [prototipo-patrimonial](plano-de-construcao.md). Este documento define O QUE o sistema pode citar — e portanto o que ele pode afirmar. Regra do produto: **citação ou abstenção** — afirmação legal sem fonte neste corpus não sai.
>
> Dono: engenharia (montagem) + advogado nomeado (curadoria de conteúdo antes do GO/NO-GO). Verificado em ago/2026.

---

## 1. Princípios do corpus

1. **Só fonte primária ou oficial entra como autoridade** (lei, IN, solução de consulta, FAQ oficial, jurisprudência). Doutrina/artigos entram com metadado `tipo: doutrina` e peso menor — o agente pode citá-los apenas como "entendimento", nunca como "a lei diz".
2. **Todo documento tem ficha**: `doc_id`, título, tipo (lei | regulamento | consulta | oficial | jurisprudencia | doutrina | ficha_jurisdicao), data, URL de origem, data de captura, resumo de 2 linhas.
3. **Chunking com metadado jurídico**: chunk carrega `doc_id` + artigo/seção (ex.: `lei-14754#art-10`). É esse ID que aparece nas `claims` dos agentes e que o guardrail anti-citação-órfã confere.
4. **Versionamento**: o corpus é um diretório versionado; toda atualização é um commit com data. A minuta final registra a versão do corpus usada (trilha de auditoria).
5. **Política de atualização**: revisão trimestral obrigatória + gatilho por evento (nova IN, julgamento do PLP 108, mudança de ITCMD estadual). Corpus com mais de 6 meses sem revisão → o sistema imprime aviso na capa de toda minuta.

## 2. O corpus v0 — núcleo tributário e de reporte (BR)

| doc_id | Documento | Por que entra | Fonte |
|---|---|---|---|
| `lei-14754` | Lei nº 14.754/2023 (tributação de aplicações no exterior, offshores e trusts) | O coração do regime pós-2024: fim do diferimento, 15% anual, transparência de trusts, regime opcional | planalto.gov.br (texto compilado) |
| `in-2180` | IN RFB nº 2.180/2024 | Regulamentação operacional da 14.754 (como declarar, regimes, balanço) | gov.br/receitafederal |
| `faq-offshore` | Perguntas e Respostas oficiais — Fazenda (Lei 14.754 e IN 2.180) | Interpretações oficiais em linguagem operacional | gov.br/fazenda (PDF 29/04/2024) |
| `cosit-75-2025` | Solução de Consulta COSIT nº 75/2025 (trusts) | Posição vinculante da RFB sobre tratamento de trust | normas RFB |
| `dcbe-bacen` | Normas da Declaração de Capitais Brasileiros no Exterior (CBE/Bacen) | Obrigação de reporte nos limiares anual e trimestral da norma; multas administrativas relevantes por omissão (valores na própria norma, que integra o corpus) | bcb.gov.br (Res. 4.841 e manual CBE) |
| `crs-in-2298` | IN RFB nº 2.298/2025 (CRS atualizado, vigência 01/01/2026) + material OCDE | Fundamento do "não existe mais sigilo": troca automática com 100+ jurisdições | gov.br/receitafederal · oecd.org (AEOI) |
| `fatca` | Acordo Brasil–EUA (FATCA, Decreto 8.506/2015) | Contas de US persons; segunda perna da transparência | planalto.gov.br |

## 3. Núcleo civil, sucessório e penal (os limites)

| doc_id | Documento | Por que entra | Fonte |
|---|---|---|---|
| `cc-sucessao` | Código Civil, arts. 1.845–1.857 (herdeiros necessários, legítima, testamento) | A legítima é ordem pública — base dos red flags de sucessão | planalto.gov.br |
| `cc-art50` | Código Civil, art. 50 (desconsideração da personalidade jurídica) | Quando estruturas caem: desvio de finalidade e confusão patrimonial | planalto.gov.br |
| `cc-fraude` | Código Civil, arts. 158–165 (fraude contra credores) + CPC art. 792 (fraude à execução) | O red flag duro nº 1: estrutura montada depois do passivo | planalto.gov.br |
| `lei-7492` | Lei nº 7.492/1986, art. 22 e parágrafo único (evasão de divisas) | Manter depósito não declarado no exterior é crime (2–6 anos, permanente) | planalto.gov.br |
| `lei-9613` | Lei nº 9.613/1998 (lavagem) | Fronteira penal do desenho de estruturas; base do KYC | planalto.gov.br |
| `eoab` | Lei nº 8.906/1994 (Estatuto da Advocacia), arts. 1º e 34 | Desenho jurídico é ato privativo de advogado → a saída do sistema é minuta PARA advogado | planalto.gov.br |
| `itcmd-uf` | Tabela ITCMD por UF (alíquotas e progressividade vigentes) | Custo sucessório real por estado; muda o cenário | sites das Sefaz estaduais (capturar tabela consolidada com data) |
| `ec132-plp108` | EC 132/2023 (ITCMD progressivo) + status do PLP 108 (herança/doação com elemento estrangeiro) | O gatilho de urgência legítimo — e uma área INSTÁVEL: o agente deve declarar a instabilidade, não cravar | planalto.gov.br · congresso (status com data de captura) |
| `stj-selec` | Seleção de julgados STJ sobre desconsideração, fraude à execução e holdings "de blindagem" | Jurisprudência que fundamenta os red flags | stj.jus.br (inteiro teor dos selecionados) |

## 4. Fichas de jurisdição (v0: 6 jurisdições)

Uma ficha padronizada por jurisdição — **só de fontes oficiais/OCDE**, com data de captura. Campos fixos: participa do CRS? · veículos típicos (trust/LLC/fundação) · tributação local relevante para não-residentes · convenção com o Brasil (bitributação)? · observações de reputação/listas (GAFI, paraíso fiscal na IN 1.037).

v0: **EUA (Delaware + estate tax federal para não-residentes)** · **Ilhas Cayman** · **BVI** · **Luxemburgo** · **Suíça** · **Uruguai**. (Expansão pós-protótipo: Singapura, Jersey, Panamá, Liechtenstein, Portugal.)

Por que essas 6: cobrem os quatro padrões que o golden set exercita — common law com trust (Cayman/BVI), imposto sucessório agressivo para estrangeiro (EUA), private banking europeu (Suíça/Luxemburgo) e vizinho regional (Uruguai).

## 5. Doutrina e contexto (peso menor, rotulado)

- Artigos técnicos verificados na pesquisa de mercado (Conjur/Migalhas/escritórios sobre 14.754, trusts, PPLI, ITCMD) — entram como `tipo: doutrina`, um a um, com URL e data.
- **Nunca entram**: material comercial de provedores de estrutura, conteúdo que ensine ocultação, "fórmulas" sem fonte legal.

## 6. Regras de ingestão (implementação no scaffold)

- Chunking: default CrewAI (4000/200) **exceto** textos de lei, que quebram por artigo (chunk = artigo ± parágrafos, preservando o `#art-N` no ID).
- Embedder **explícito** na configuração (nunca o default silencioso); armazenamento em `CREWAI_STORAGE_DIR` fixo do projeto.
- O RAG é **tool explícita** (não Knowledge nativo): retorna `[{chunk_id, doc_id, artigo, texto, score}]` — proveniência estruturada é requisito do guardrail anti-citação-órfã ([especificação](especificacao-agentes.md) §4).
- Dados do CLIENTE jamais entram no corpus — corpus é conhecimento público; caso do cliente vive no estado do Flow, segregado e apagável.

## Ligações

[Plano de construção](plano-de-construcao.md) · [Especificação dos agentes](especificacao-agentes.md) · [Avaliação e métrica](avaliacao-e-metrica.md) · Scaffold: `scaffold/src/patrimonio_flow/tools/rag_corpus.py`
