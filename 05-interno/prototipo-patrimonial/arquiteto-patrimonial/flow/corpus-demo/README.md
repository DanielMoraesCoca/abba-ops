# Corpus de DEMONSTRAÇÃO — ⚠️ NÃO É AUTORIDADE JURÍDICA

Este diretório contém **leis fictícias**, escritas só para **testar o pipeline
completo** (análise → desenho → minuta) sem depender da curadoria do advogado.

**JAMAIS use para um cliente real.** Todo trecho começa com o aviso "DEMO —
FICTÍCIO". O corpus real e autoritativo vive em `flow/corpus/` e é curado por um
advogado nomeado (ver `briefing-corpus-hector.md` no abba-ops).

## Como usar (só teste interno)
Aponte o Flow para este corpus com a variável de ambiente:
```
CORPUS_DIR=corpus-demo
```
Sem essa variável, o sistema usa o corpus real (`corpus/`, hoje vazio → o
sistema se abstém, que é o comportamento correto em produção).

Quando o corpus real do advogado existir, **remova o `CORPUS_DIR`** e o sistema
passa a citar apenas fonte oficial.
