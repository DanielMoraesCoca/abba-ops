# Identidade Visual — padrão único de materiais

> **Objetivo:** tudo que a ABBA produz — proposta, deck, relatório, certificado, card, portal — parece vir da mesma casa. Este padrão foi extraído do material real mais maduro (a proposta comercial canônica) e passa a valer para TODO material novo. Arquivos-fonte da marca: Drive → `05 Marketing/Marca/`.

## Paleta

Valores **extraídos dos arquivos dos decks** em 20/08/2026 (o XML de
`abba-deck-institucional.pptx` e `abba-apresentacao.pptx` — as duas peças
usam exatamente a mesma paleta). Antes desta data a tabela trazia um
dourado (`#C2A35B`) que não era o dos materiais reais; ficou valendo o
que os arquivos usam.

| Papel | Cor | Hex | Uso |
|---|---|---|---|
| **Primária** | Azul-marinho profundo | `#1B2A4A` | Títulos, marca, botão primário, fundos de capa |
| **Tinta** | Grafite | `#232B3A` | Texto forte sobre fundo claro |
| **Acento** | Dourado/latão | `#B8985A` | Etiquetas em caixa alta, réguas, números de destaque, links — a cor mais usada do deck, e ainda assim usada com parcimônia |
| **Neutro escuro** | Cinza-ardósia | `#5A6472` | Texto secundário, legendas, rodapés |
| **Areia** | Bege claro | `#D9D2C4` | Réguas finas, divisores, superfície de apoio |
| **Fundo** | Creme | `#F7F4EE` | Fundo de página |
| Base | Branco | `#FFFFFF` | Cartões, tabelas |

Regra: **navy + dourado sobre creme = a cara da ABBA** (sóbrio, premium,
confiável). Nunca introduzir cor nova sem registrar aqui.

**Cores funcionais** (só para estado, nunca para decorar): verde
`#2F7A5A` (deu certo) · âmbar `#B8862A` (atenção — é também o amarelo do
Semáforo de Dados) · vermelho `#A33A32` (pare). Se uma cor não está
dizendo "certo", "cuidado" ou "errado", ela deveria ser navy, dourada ou
areia.

### No portal

O portal implementa esta paleta desde 20/08/2026 (decisão DESIGN-01 no
registro do produto). Os tokens vivem em `abba-portal/src/app/globals.css`
sob `@theme`, e `npm run audit:hex` reprova cor nova escrita direto no
componente. Antes disso o portal era escuro, com acentos azul, teal,
laranja, rosa e roxo — que não existiam em nenhum material impresso.

## Tipografia

- **Documentos Office:** Aptos (corpo) e Aptos Display (títulos) — padrão dos materiais atuais. Fallback universal: Calibri / Arial.
- **Portal/web:** serifada nos títulos e sans no corpo, espelhando o par Cambria/Calibri dos decks — na web, Source Serif 4 e Inter. Os hex acima valem para lá, e agora estão implementados.
- Corpo 11pt · legendas 9pt · títulos de seção numerados (`1. `, `1.1 `).

## Anatomia dos documentos

| Elemento | Padrão |
|---|---|
| **Capa** | Logo/nome ABBA + subtítulo da linha de serviço · título do documento · "Preparado para: {{CLIENTE}}" · mês/ano · `Ref: ABBA-AAAA-NNN` |
| **Cabeçalho** | Discreto, com "Confidencial" em cinza 9pt quando aplicável |
| **Rodapé** | ABBA · abbaservices.com.br · página N |
| **Sumário** | Obrigatório em docs de 6+ páginas (TOC com pontilhado) |
| **Tabelas** | Cabeçalho navy com texto branco; linhas alternadas branco/cinza-gelo |
| **Stat-cards** | Números grandes em navy + rótulo em cinza (padrão do sumário executivo da proposta: "12–16 semanas · 3 frentes · 24/7") |
| **Assinatura de e-mail** | Padrão definido em [`../03-comercial/emails-follow-up.md`](../03-comercial/emails-follow-up.md), sempre `@abbaservices.com.br` |

## Referência e numeração

- Documentos comerciais: `Ref: ABBA-AAAA-NNN` (sequencial por ano; registrar emissão na pasta do lead no Drive)
- Versões de modelo: sufixo `v1`, `v2` no nome do arquivo; modelo vigente sem sufixo no Drive `03 Modelos/`
- Idioma: pt-BR; datas por extenso em material de cliente

## Modelos-mestres (a família completa)

O modelo-mestre de proposta já existe: [`../08-materiais/modelos/proposta-comercial-modelo.docx`](../08-materiais/modelos/proposta-comercial-modelo.docx). A fila dos demais está no [catálogo de materiais](../08-materiais/README.md#4-o-que-ainda-não-existe-fila-de-produção-de-materiais) — **todo novo modelo deriva do mestre de proposta** (mesma capa, paleta, tabelas), nunca nasce do zero.

## Regras de ouro

1. Material novo **sempre** parte de um modelo-mestre — se o modelo não existe, criar o modelo primeiro, depois a instância.
2. Nome externo ≠ nome interno ([nomenclatura](marca-e-nomenclatura.md)); URLs só `abbaservices.com.br`.
3. Um documento por versão enviada, congelado em PDF no Drive.
4. Logo: a marca-símbolo (grafo dourado) está versionada em [`../08-materiais/marca/abba-logo.png`](../08-materiais/marca/abba-logo.png) — usada nos decks e certificados. Cópia no Drive `05 Marketing/Marca/`. Evolução profissional da marca pode vir depois.
