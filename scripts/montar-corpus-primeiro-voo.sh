#!/bin/sh
# Monta o corpus do PRIMEIRO VOO REAL a partir dos documentos vivos deste repo.
#
# Por que um script e não uma pasta commitada: o corpus é uma VISTA dos
# documentos, não uma cópia deles. Uma cópia envelhece em silêncio e no dia da
# chave a máquina leria uma ABBA que não existe mais. Isto remonta em segundos.
#
# A regra de curadoria, e ela é a decisão mais importante aqui:
#   O CORPUS CARREGA EVIDÊNCIA, NUNCA CONCLUSÃO ALHEIA.
# Ficaram DE FORA, de propósito, o parecer do conselho, a auditoria de prontidão
# e o plano de ação. Os três são análises PRÉVIAS da ABBA. Alimentar a máquina
# com a conclusão de outra pessoa a faria lavar aquela conclusão como achado
# próprio, e o primeiro voo deixaria de medir se ela sabe LER uma empresa. Um
# engajamento real não recebe o relatório do consultor anterior como fonte; se
# receber, entra com --level consultant e sabendo o que isso significa.
#
# Também fora: tudo que descreve a FERRAMENTA em vez da FIRMA (runbooks,
# dossiês técnicos, contrato da máquina). A empresa a ser lida é a ABBA que
# vende e entrega, não o repositório que a atende.
#
# Uso: sh scripts/montar-corpus-primeiro-voo.sh [destino]
set -eu

REPO=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
DEST=${1:-"$REPO/../corpus-abba-primeiro-voo"}

# nível|fase|arquivo   — o nível é o que o método usa para cruzar versões.
# A fase segue o mapa de entrevistas: 1 topo, 2 gestão, 3 operação, 0 dado frio.
LISTA=$(cat <<'EOF'
ceo_board|1|00-identidade/mapa-da-abba.md
ceo_board|1|00-identidade/plano-de-negocio.md
ceo_board|1|00-identidade/modelo-de-servico.md
ceo_board|1|05-interno/acordo-societario.md
c_suite|2|01-setores/README.md
c_suite|2|01-setores/comercial.md
c_suite|2|01-setores/entrega.md
c_suite|2|01-setores/tecnologia.md
c_suite|2|01-setores/financeiro-admin.md
c_suite|2|01-setores/capacitacao.md
dept_head|3|04-entrega/ritual-semanal.md
dept_head|3|04-entrega/sla-manutencao.md
dept_head|3|03-comercial/pipeline-modelo.md
dept_head|3|04-entrega/protocolo-de-imersao.md
internal_data|0|05-interno/registro-de-riscos.md
internal_data|0|05-interno/financas-basicas.md
internal_data|0|03-comercial/precificacao-planilha.md
internal_data|0|06-ferramentas/mapa-jornada-ferramentas.md
external|2|05-interno/reuniao-rafael-brasal-2026-08-18.md
EOF
)

rm -rf "$DEST"
for NIVEL in ceo_board c_suite dept_head internal_data external; do
  mkdir -p "$DEST/$NIVEL"
done

TOTAL=0
N=0
echo "$LISTA" | while IFS='|' read -r NIVEL FASE ARQ; do
  [ -n "$NIVEL" ] || continue
  if [ ! -f "$REPO/$ARQ" ]; then
    echo "FALTANDO: $ARQ" >&2
    exit 1
  fi
  cp "$REPO/$ARQ" "$DEST/$NIVEL/$(basename "$ARQ")"
done

echo "$LISTA" > "$DEST/MANIFESTO.txt"
echo "Corpus montado em: $DEST"
for NIVEL in ceo_board c_suite dept_head internal_data external; do
  N=$(ls "$DEST/$NIVEL" | wc -l)
  B=$(cat "$DEST/$NIVEL"/* | wc -c)
  printf "  %-14s %2d arquivo(s)  %7d bytes\n" "$NIVEL" "$N" "$B"
done
printf "  %-14s %2d arquivo(s)  %7d bytes\n" TOTAL \
  "$(find "$DEST" -name '*.md' | wc -l)" "$(cat $(find "$DEST" -name '*.md') | wc -c)"
