# Corpus jurídico (curado por advogado)

Este diretório é o **corpus compartilhado** que o RAG consulta. Ele está **vazio
de propósito** — só entra fonte primária/oficial **curada e datada por um
advogado nomeado**. Enquanto vazio, o sistema recusa casos sujos (gate
determinístico) mas se **abstém** de desenhar os limpos (citação-ou-abstenção).

## Como popular
Ver o briefing no abba-ops: `05-interno/prototipo-patrimonial/briefing-corpus-hector.md`.

- `manifest.json` — a lista de documentos, cada um com a ficha `FrescorDoc`
  (`doc_id`, `tipo`, `valid_from`/`valid_to`/`superseded_by`, `last_verified`,
  `ttl_dias`, `fonte_url`).
- `chunks/<doc_id>.jsonl` — o texto, uma linha por chunk:
  `{"chunk_id": "lei-14754#art-10::1", "artigo": "art-10", "texto": "...", "tipo": "lei"}`.
  **Leis quebram por artigo**, preservando `#art-N` no `chunk_id` (é o que vira a
  citação clicável na minuta).

## Regras inegociáveis
- **Só fonte pública/oficial** entra como autoridade (lei, IN, consulta, FAQ
  oficial, jurisprudência). Doutrina entra rotulada `tipo: doutrina`, peso menor.
- **Dados de cliente JAMAIS entram aqui** — o caso do cliente vive no estado do
  Flow, segregado e apagável.
- **Vigência importa**: a recuperação filtra por `as_of` (data do caso) — lei
  revogada não aparece como atual.
