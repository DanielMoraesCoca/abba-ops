#!/bin/sh
# checar-texto.sh — a checagem de texto da casa, antes de congelar PDF.
#
#   sh scripts/checar-texto.sh
#
# Não instala nada e não depende de node nem de python: só sh e awk, que
# já existem no Mac e no Linux. Roda em segundos sobre todos os .md.
#
# O que BLOQUEIA hoje:
#
#   1. TRAVESSÃO (—) no texto. Decisão do sócio de 01/09/2026, olhando os
#      prints do portal: travessão não entra em texto da ABBA. É a
#      assinatura mais reconhecível de texto escrito por IA, e o que a
#      gente vende é justamente saber usar IA sem parecer que a IA
#      escreveu. A troca não é mecânica: cada caso vira dois-pontos,
#      vírgula, ponto-e-vírgula, ponto ou parênteses conforme o que o
#      travessão estava fazendo na frase. Por isso aqui BLOQUEIA em vez
#      de avisar: um travessão novo pede decisão de redação.
#
#   2. CÉLULA DE TABELA QUEBRADA (`|:` ou `| — |`). Foi o defeito que a
#      conversão de 01/09 criou três vezes: o traço que marcava "nada
#      aqui" virou dois-pontos solto e quebrou a linha da tabela.
#
#   3. TRAVESSÃO ÓRFÃO (`—,`). A metade que fecha um par cujo abre já
#      virou outra coisa. Deixa a frase sem sentido.
#
# Bloco cercado (``` … ```) fica FORA da checagem de travessão: lá dentro
# é código, comando ou desenho, onde alinhamento e sintaxe importam mais
# que a pontuação da casa. Os diagramas que são texto lido (Mermaid, os
# fluxos em ASCII) já foram convertidos à mão em 01/09.

cd "$(dirname "$0")/.." || exit 1
FALHAS=0

reportar() {
  # $1 = título  $2 = arquivo com os achados  $3 = o que fazer
  n=$(wc -l < "$2" | tr -d ' ')
  if [ "$n" -gt 0 ]; then
    printf '\n✗ BLOQUEIA · %s (%s)\n' "$1" "$n"
    head -8 "$2" | sed 's/^/      /'
    [ "$n" -gt 8 ] && printf '      … e mais %s\n' "$((n - 8))"
    printf '   → %s\n' "$3"
    FALHAS=$((FALHAS + 1))
  else
    printf '✓ %s\n' "$1"
  fi
}

TMP=$(mktemp -d) || exit 1
trap 'rm -rf "$TMP"' EXIT

# 1 · travessão fora de bloco cercado
find . -name '*.md' -not -path './.git/*' | sort | while read -r f; do
  awk -v arq="$f" '
    /^[ \t]*(```|~~~)/ { dentro = !dentro; next }
    !dentro && /—/    { printf "%s:%d: %s\n", arq, NR, substr($0, 1, 110) }
  ' "$f"
done > "$TMP/travessao"
reportar "nenhum travessão no texto" "$TMP/travessao" \
  "troque por dois-pontos, vírgula, ponto-e-vírgula, ponto ou parênteses conforme o caso."

# 2 · célula de tabela quebrada
grep -rn --include='*.md' -e '|[ \t]*:' -e '|[ \t]*—[ \t]*|' . 2>/dev/null \
  | cut -c1-120 > "$TMP/celula"
reportar "nenhuma célula de tabela quebrada" "$TMP/celula" \
  "célula que marcava \"nada aqui\" fica VAZIA; não deixe dois-pontos solto."

# 3 · travessão órfão
grep -rn --include='*.md' -e '—[ \t]*,' . 2>/dev/null \
  | cut -c1-120 > "$TMP/orfao"
reportar "nenhum travessão órfão" "$TMP/orfao" \
  "é a metade que fecha um par: feche com parênteses ou vírgula."

printf '\n'
if [ "$FALHAS" -gt 0 ]; then
  printf '%s checagem(ns) reprovada(s). NÃO congele PDF assim.\n' "$FALHAS"
  exit 1
fi
printf 'Texto da casa em ordem.\n'
