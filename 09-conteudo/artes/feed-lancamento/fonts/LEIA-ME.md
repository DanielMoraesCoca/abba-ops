# Fontes servidas do disco

As três famílias do sistema (Newsreader · Source Serif 4 · IBM Plex Mono) estão
aqui em `.woff2`, com o `local.css` que as declara.

**Por que vendorizar.** O `render.sh` roda um Chromium sem interface para virar
artboard em PNG. Enquanto ele buscava as fontes no Google, cada render dependia
da rede: quando ela caía, o Chromium esperava o tempo todo e depois desenhava em
Georgia, ou seja, entregava um PNG **errado sem avisar**. Com as fontes no disco,
14 telas saem em 8 segundos e o resultado é sempre o mesmo.

**Licença.** As três são de licença aberta (SIL Open Font License), que permite
redistribuir.

**Os `.dc.html` não usam este diretório.** Eles continuam apontando para o Google
Fonts, porque precisam funcionar dentro do canvas do Claude Design. Quem troca a
referência é o `render.sh`, na cópia temporária, na hora de renderizar.

Para atualizar: baixar o CSS do Google, trocar as URLs por caminhos relativos e
baixar os `.woff2` referenciados.
