# Briefing de Curadoria do Corpus — para o advogado nomeado

> **Camada:** interno (engenharia + jurídico). Deriva de [`corpus-conhecimento.md`](corpus-conhecimento.md) (a especificação) e serve o [`plano-de-construcao.md`](plano-de-construcao.md). Destinatário: o **advogado nomeado** (candidato: Héctor) — o profissional de referência que cura o corpus, valida os gabaritos e assina o veredito de GO/NO-GO.
>
> **Gate:** o papel do advogado (remuneração, parceria, sociedade) é decisão de sócios (P10) e passa pelo advogado próprio da ABBA (P4). Este briefing é **técnico** — o que curar e em que formato — e não pressupõe o vínculo comercial resolvido.

---

## 1. Por que o corpus é o gargalo (e por que é o seu trabalho)
O sistema já está deployado e o filtro de conformidade (o "dizer não ao caso errado") já funciona ao vivo. Mas a regra inegociável do produto é **citação ou abstenção**: nenhuma afirmação jurídica sai sem uma fonte no corpus. Hoje o corpus está **vazio** — então o sistema recusa casos sujos, mas ainda não desenha os limpos. **É o corpus que destrava a metade "desenhar e fundamentar".**

O corpus é o que separa este produto das boutiques que vendem no "confia em mim": aqui, cada frase da minuta aponta para a lei exata. Isso só tem valor se as fontes forem **curadas por um advogado** — não pode ser raspagem automática nem texto de IA. Daí o seu papel.

## 2. O que precisamos de você (o entregável)
Para cada documento da lista (§4), entregar um item com:
1. **O texto-fonte** — o texto oficial/primário (lei, IN, solução de consulta, FAQ oficial, julgado). Copiado da fonte pública oficial, **não parafraseado**.
2. **A ficha de metadados** (§3) — preenchida.
3. **Uma validação de vigência** — você confirma que está vigente **nesta data** e sinaliza pontos instáveis (ex.: PLP 108).

Não precisamos que você escreva análise nem opinião — só **curar e datar as fontes** que o sistema poderá citar. A análise é o que os agentes fazem *a partir* do que você curou.

## 3. O formato de cada documento (a ficha)
Cada documento entra com esta ficha (é o que o "corpus vivo" precisa para nunca citar lei revogada como atual):

| Campo | O que é | Exemplo |
|---|---|---|
| `doc_id` | Identificador curto e estável | `lei-14754` |
| `titulo` | Nome oficial | Lei nº 14.754/2023 |
| `tipo` | `lei` \| `regulamento` \| `consulta` \| `oficial` \| `jurisprudencia` \| `doutrina` \| `ficha_jurisdicao` | `lei` |
| `fonte_url` | URL oficial de origem | planalto.gov.br/... |
| `valid_from` | Data em que passou a vigorar (ISO) | `2024-01-01` |
| `valid_to` | Data em que deixou de vigorar (vazio = vigente) | *(vazio)* |
| `superseded_by` | `doc_id` da norma que a revogou/substituiu, se houver | *(vazio)* |
| `last_verified` | **A data em que VOCÊ conferiu a vigência** (ISO) | `2026-08-13` |
| `ttl_dias` | Janela até precisar reconferir: **30** para área instável/regulatória, **180** para estável | `180` |
| `resumo` | 2 linhas: o que a norma diz e por que importa | — |

**A data que só você pode dar é `last_verified`.** É ela que faz o sistema imprimir "corpus reconferido em ___" na trilha de auditoria — e que dispara o alerta de obsolescência quando vence.

## 4. Os documentos do corpus v0 (a lista)

### 4a. Núcleo tributário e de reporte (BR)
| doc_id | Documento | Por que entra |
|---|---|---|
| `lei-14754` | Lei nº 14.754/2023 | O coração do regime pós-2024: 15% anual, transparência de trusts, fim do diferimento |
| `in-2180` | IN RFB nº 2.180/2024 | Regulamentação operacional da 14.754 |
| `faq-offshore` | Perguntas e Respostas oficiais (Fazenda) | Interpretações oficiais operacionais |
| `cosit-75-2025` | Solução de Consulta COSIT nº 75/2025 (trusts) | Posição vinculante da RFB sobre trust |
| `dcbe-bacen` | Normas da DCBE/CBE (Bacen) | Obrigação de reporte; limiares e multas na própria norma |
| `crs-in-2298` | IN RFB nº 2.298/2025 (CRS, vigência 01/01/2026) + material OCDE | Troca automática com 100+ jurisdições |
| `fatca` | Acordo Brasil–EUA (FATCA, Dec. 8.506/2015) | Contas de US persons |

### 4b. Núcleo civil, sucessório e penal (os limites)
| doc_id | Documento | Por que entra |
|---|---|---|
| `cc-sucessao` | CC arts. 1.845–1.857 (legítima, herdeiros necessários, testamento) | A legítima é ordem pública |
| `cc-art50` | CC art. 50 (desconsideração da PJ) | Quando estruturas caem: confusão patrimonial |
| `cc-fraude` | CC arts. 158–165 + CPC art. 792 (fraude contra credores / à execução) | O red flag duro nº 1 |
| `lei-7492` | Lei 7.492/1986, art. 22 (evasão de divisas) | Depósito não declarado no exterior é crime |
| `lei-9613` | Lei 9.613/1998 (lavagem) | Fronteira penal; base do KYC |
| `eoab` | Lei 8.906/1994, arts. 1º e 34 | Desenho jurídico é ato privativo → saída é minuta PARA advogado |
| `itcmd-uf` | Tabela ITCMD por UF (alíquotas vigentes) | Custo sucessório real por estado |
| `ec132-plp108` | EC 132/2023 + status do PLP 108 | Gatilho de urgência — **área INSTÁVEL**: `ttl_dias`=30, marcar como risco, não cravar |
| `stj-selec` | Julgados STJ (desconsideração, fraude à execução, holdings de blindagem) | Jurisprudência que fundamenta os red flags |

### 4c. Fichas de jurisdição (v0: 6)
Uma ficha padronizada por jurisdição, **só de fontes oficiais/OCDE**, com data de captura. Campos fixos: participa do CRS? · veículos típicos (trust/LLC/fundação) · tributação local para não-residentes · convenção com o Brasil (bitributação)? · observações de reputação/listas (GAFI; IN 1.037).

v0: **EUA (Delaware + estate tax federal p/ não-residentes)** · **Cayman** · **BVI** · **Luxemburgo** · **Suíça** · **Uruguai**. (Cobrem os 4 padrões do golden set: common law com trust, imposto sucessório agressivo p/ estrangeiro, private banking europeu, vizinho regional.)

## 5. Como o sistema vai quebrar o texto (chunking) — o que isso pede de você
- **Textos de lei quebram por artigo** — cada chunk é um artigo (± parágrafos), e o identificador preserva o artigo: `lei-14754#art-10`. Por isso, ao entregar uma lei, **mantenha a numeração de artigos intacta** — é o que vira a citação clicável na minuta.
- Demais textos (FAQ, consultas, fichas) quebram em blocos; preserve títulos/seções.
- Cada afirmação que um agente fizer vai carregar o `#art-N` da fonte. Se a numeração vier bagunçada, a citação perde a precisão.

## 6. A fronteira (o que entra e o que nunca entra)
- **Entra como autoridade:** só fonte primária/oficial (lei, IN, solução de consulta, FAQ oficial, jurisprudência).
- **Entra com peso menor, rotulado `doutrina`:** artigos técnicos (Conjur/Migalhas/escritórios), um a um, com URL e data — o agente pode citar como "entendimento", nunca como "a lei diz".
- **Nunca entra:** material comercial de provedores de estrutura, conteúdo que ensine ocultação, "fórmulas" sem fonte legal, dados de cliente (o caso do cliente vive segregado e apagável, jamais no corpus).

## 7. O que "assinado" significa (o gate de qualidade)
Antes do GO/NO-GO, você faz duas coisas que só um advogado pode fazer, e que ficam registradas com o seu nome:
1. **Valida os gabaritos do golden set** (12 personas sintéticas em [`avaliacao-e-metrica.md`](avaliacao-e-metrica.md)) — confirma que "o que um bom especialista faria" está correto. Congelam-se depois disso.
2. **Assina o veredito** — pontua a concordância dos desenhos (rubrica 0–2) e assina o relatório de GO/NO-GO. É o que transforma o produto em "validado por advogado nomeado, com estes números".

## 8. O caminho de menor esforço para começar
Não precisa entregar os ~26 itens de uma vez. A ordem que mais destrava:
1. **`lei-14754` + `in-2180` + `dcbe-bacen`** — com estes três, um caso de estrutura declarada já roda com citação.
2. **`cc-sucessao` + `cc-fraude` + `cc-art50`** — cobrem o núcleo sucessório e os limites.
3. As **6 fichas de jurisdição** — destravam o desenho internacional.
4. O resto (FAQ, COSIT, CRS, FATCA, ITCMD-UF, EC132/PLP108, STJ) completa o v0.

Cada item entregue já entra no sistema (o corpus é incremental). Um lote de 3–6 documentos já faz um caso *limpo* rodar ponta a ponta.

## Ligações
[Corpus (especificação)](corpus-conhecimento.md) · [Plano de construção](plano-de-construcao.md) · [Avaliação e métrica](avaliacao-e-metrica.md) · [Visão e melhorias](visao-e-melhorias.md) · [Registro de decisões](../registro-de-decisoes.md)
