#!/bin/bash
# Renderiza artboards .dc.html em PNG, com as fontes servidas do disco.
# A rede do ambiente cai com frequencia; fonts/local.css remove essa dependencia
# e faz o render virar deterministico.
set -e
OUT="${OUT:-/tmp/render}"; SCALE="${SCALE:-2}"
mkdir -p "$OUT" "$OUT/fonts"
cp -n fonts/*.woff2 fonts/local.css "$OUT/fonts/" 2>/dev/null || true
cp -n abba-logo.png logo-microsoft.png logo-crewai.png "$OUT/" 2>/dev/null || true
for f in "$@"; do
  g=$(grep -o 'class="p[^"]*"' "$f.dc.html" | head -1)
  case "$g" in *gold*) BG="#C2A35B";; *paper*) BG="#F2F4F7";; *) BG="#1B2A4A";; esac
  sed -e "s|<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com[^\"]*\">|<link rel=\"stylesheet\" href=\"fonts/local.css\">|" \
      -e "s|body { margin:0; }|body { margin:0; background:$BG; } html,body{height:1350px;overflow:hidden}|" "$f.dc.html" > "$OUT/$f.html"
  /opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox \
    --hide-scrollbars --force-device-scale-factor=$SCALE --window-size=1080,1350 \
    --default-background-color=${BG#\#}ff \
    --virtual-time-budget=2500 --screenshot="$OUT/$f.png" "file://$OUT/$f.html" 2>/dev/null
done
