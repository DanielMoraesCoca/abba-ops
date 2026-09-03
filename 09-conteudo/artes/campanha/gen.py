# -*- coding: utf-8 -*-
# CAMPANHA · registro alto
#
# Prova de conceito de um SEGUNDO registro visual para a ABBA. O sistema do feed
# continua existindo e continua certo para peca de argumento. Este existe para o
# que ele nao faz: parar o dedo.
#
# O que NAO muda: paleta (navy, papel, ouro), as tres familias, o grao, o
# contato, e a regra de nao usar numero fora do canone.
#
# O que muda: a escala (tipo sangrando para fora da margem), a camada (coisas
# por cima de coisas), a textura (carimbo com tinta irregular) e o tom (deadpan,
# sarcastico, primeira pessoa).
#
# O DISPOSITIVO: o carimbo do proprio Revisor. A casa tem uma ferramenta cujo
# trabalho e reprovar o material dela. Nenhum concorrente pode copiar isso sem
# antes construir uma, e nenhum vai construir uma que o reprove. E a unica
# imagem de marca que e ao mesmo tempo verdadeira, engracada e nao imitavel.

import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

W, HT = 1080, 1350

STYLE = '''
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,300;1,6..72,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
  <style>
    body { margin:0; }
    /* <x-dc> e um elemento customizado, e elemento customizado nasce inline.
       Inline dentro do body cria caixa de linha com altura propria, e era isso
       que deixava uma faixa de alguns pixels sobrando embaixo do cartao em todo
       PNG. Vale para o gerador do feed tambem. */
    x-dc { display:block; } helmet { display:none; }
    .p { width:1080px; height:1350px; box-sizing:border-box; position:relative;
         overflow:hidden; background:#F2F4F7; color:#1B2A4A;
         font-family:"Source Serif 4", Georgia, serif; }
    .p.navy { background:#1B2A4A; color:#FFFFFF; }

    /* Grao pesado. Aqui ele e assunto, nao acabamento: e o que faz a peca ler
       como papel carimbado em vez de tela. */
    .grao { position:absolute; top:0; left:0; width:1080px; height:1350px;
            pointer-events:none;
            background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E");
            background-size:240px 240px; opacity:.5; mix-blend-mode:multiply; }
    .navy .grao { opacity:.09; mix-blend-mode:overlay; }

    .cab { position:absolute; top:70px; left:96px; right:96px;
           display:flex; justify-content:space-between;
           font-family:"IBM Plex Mono", monospace; font-size:19px;
           letter-spacing:.2em; color:#8C97AA; text-transform:uppercase; }
    .navy .cab { color:#5D6E92; }
    .fio { position:absolute; left:96px; right:96px; height:1px; background:#CBD3DF; }
    .navy .fio { background:#33456A; }

    /* Faixa de altura fixa, nao caixa que se mede pelo conteudo: como flex
       sem altura declarada ele colapsava para 3px e o texto sumia do PNG. */
    .pe { position:absolute; top:1186px; left:96px; right:96px;
          display:flex; justify-content:space-between;
          font-family:"IBM Plex Mono", monospace; font-size:21px; line-height:1.5;
          letter-spacing:.16em; color:#4E5A70; }
    .navy .pe { color:#8E9AB4; }
    .pe .ouro { color:#8A6E28; } .navy .pe .ouro { color:#C2A35B; }

    /* A FALA DO MERCADO. Sangra para fora da margem direita de proposito: e o
       gesto que tira a peca do registro de slide e coloca no de cartaz. */
    .fala { position:absolute; left:96px; right:-52px;
            font-family:"Newsreader", Georgia, serif; font-weight:400;
            font-size:126px; line-height:1.0; letter-spacing:-.028em;
            color:#1B2A4A; }
    .navy .fala { color:#FFFFFF; }
    .fala .m { color:#AEB8C8; } .navy .fala .m { color:#4A5B80; }
    .fala .g { color:#8A6E28; font-style:italic; }
    .navy .fala .g { color:#D8BE7C; font-style:italic; }

    /* A TARJA. Feita com text-decoration em vez de barra posicionada a mao:
       o navegador acerta a altura por linha, inclusive quando a frase muda de
       tamanho. Posicao calculada a mao erra sempre um pouco, e em tamanho de
       cartaz o erro aparece. */
    .fala.tarjada { text-decoration:line-through; text-decoration-thickness:13px;
                    text-decoration-color:#1B2A4A; text-decoration-skip-ink:none; }
    .navy .fala.tarjada { text-decoration-color:#C2A35B; }

    /* O CARIMBO. Caixa dupla, mono pesado, girado, com tinta irregular. O
       filtro de deslocamento e o que impede de parecer clip-art. */
    .carimbo { position:absolute; border:5px solid #1B2A4A;
               padding:20px 40px 16px; text-align:center;
               font-family:"IBM Plex Mono", monospace; font-weight:600;
               font-size:74px; letter-spacing:.14em; color:#1B2A4A;
               line-height:1; background:transparent;
               box-shadow:inset 0 0 0 5px #F2F4F7, inset 0 0 0 10px #1B2A4A;
               filter:url(#tinta); opacity:.9; }
    .carimbo .sob { display:block; font-size:18px; font-weight:500;
                    letter-spacing:.3em; margin-top:16px; }

    .bloco { position:absolute; left:96px; right:96px; }
    .rot { font-family:"IBM Plex Mono", monospace; font-size:21px;
           letter-spacing:.24em; text-transform:uppercase; color:#8A6E28;
           margin:0 0 20px; }
    .navy .rot { color:#C2A35B; }
    .cor { font-size:32px; line-height:1.48; color:#4E5A70; margin:0; max-width:860px; }
    .navy .cor { color:#C3CAD8; }
    .cor b { color:#1B2A4A; font-weight:600; } .navy .cor b { color:#FFFFFF; }
    .cor i { font-style:italic; color:#8A6E28; } .navy .cor i { color:#D8BE7C; }

    .mono { font-family:"IBM Plex Mono", monospace; font-size:23px;
            line-height:1.75; letter-spacing:.05em; color:#6B778E; margin:0; }
    .navy .mono { color:#7C88A2; }
    .mono b { color:#1B2A4A; font-weight:600; } .navy .mono b { color:#FFFFFF; }

    .marca { display:block; width:148px; height:auto; }
  </style>
'''

FILTRO = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
          '<filter id="tinta" x="-14%" y="-14%" width="128%" height="128%">'
          '<feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="4" seed="7" result="r"/>'
          '<feDisplacementMap in="SourceGraphic" in2="r" scale="8" '
          'xChannelSelector="R" yChannelSelector="G"/></filter></defs></svg>')

def cabeca():
    """Montado na hora, e nao uma vez no import: STYLE cresce ao longo do
    arquivo (o css da bula entra depois), e HEAD congelado deixava as regras
    novas de fora sem nenhum erro aparecer."""
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>'
            + STYLE + '</helmet>\n')
TAIL = '</x-dc>\n</body>\n</html>\n'

F, PAGES = {}, []

def pagina(nome, corpo, navy=False, cab_dir='', pe_esq=''):
    cls = 'p navy' if navy else 'p'
    F[nome] = (cabeca() + f'<div class="{cls}">' + FILTRO +
               '<div class="grao"></div>'
               f'<div class="cab"><span>ABBA</span><span>{cab_dir}</span></div>'
               '<div class="fio" style="top:116px"></div>'
               '<div class="fio" style="top:1140px"></div>'
               + corpo +
               f'<div class="pe"><span>{pe_esq}</span>'
               '<span class="ouro">abbaservices.com.br</span></div>'
               '</div>\n' + TAIL)


def reprovado(nome, fala_html, motivo, no_lugar, carimbo_top=402,
              carimbo_esq=486, giro=-7, sob='REGRA 4.2 · BASE DE EVIDENCIAS',
              cab='Régua do Revisor · v1.5.0', pe='Bloqueio 001'):
    """Uma fala do mercado, tarjada, com o carimbo do nosso proprio revisor.

    O carimbo cai POR CIMA do fim da frase, nunca ao lado. Carimbo que nao
    encosta no que reprovou lê como adesivo; encostando, lê como documento
    carimbado, que e o que esta casa e.
    """
    corpo = (
        f'<div class="fala tarjada" style="top:206px">{fala_html}</div>'
        f'<div class="carimbo" style="top:{carimbo_top}px;left:{carimbo_esq}px;'
        f'transform:rotate({giro}deg)">BLOQUEADO<span class="sob">{sob}</span></div>'
        f'<div class="bloco" style="top:646px">'
        f'<p class="rot">O que a nossa régua diz</p>'
        f'<p class="mono">{motivo}</p></div>'
        f'<div class="bloco" style="top:986px">'
        f'<p class="cor">{no_lugar}</p></div>'
    )
    pagina(nome, corpo, navy=False, cab_dir=cab, pe_esq=pe)


# ══════════ 01 · os 95% ══════════
reprovado(
    'Bloq01',
    '<span class="m">“</span>95% dos pilotos<br>de IA <span>falham.</span><span class="m">”</span>',
    motivo='MOTIVO&nbsp;&nbsp;número fora da base de evidências<br>'
           'FONTE&nbsp;&nbsp;&nbsp;MIT NANDA, não revisado por pares,<br>'
           '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;critério de sucesso estreitíssimo, e os<br>'
           '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;autores vendem o framework que o<br>'
           '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;relatório recomenda',
    no_lugar='No lugar dele a gente usa a RAND, que entrevistou 65 engenheiros de '
             'machine learning sêniores: <b>mais de 80% dos projetos de IA falham</b>, '
             'o dobro dos projetos de TI comuns. <i>Menos viral. Sustenta uma reunião.</i>',
    pe='Bloqueio 001 · 2026',
)

# ══════════ 02 · o agente que decide ══════════
reprovado(
    'Bloq02',
    '<span class="m">“</span>Nosso agente<br>decide <span>sozinho.</span><span class="m">”</span>',
    motivo='MOTIVO&nbsp;&nbsp;frase proibida em material desta casa<br>'
           'REGRA&nbsp;&nbsp;&nbsp;a IA rascunha · um humano assina ·<br>'
           '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a diretoria decide<br>'
           'NOTA&nbsp;&nbsp;&nbsp;&nbsp;a ordem não muda em nenhum cliente',
    no_lugar='Quem responde pela empresa é gente. E gente não terceiriza assinatura. '
             '<i>Se o seu fornecedor promete o contrário, pergunte quem assina quando der errado.</i>',
    sob='RECUSA 4 · PROMESSAS × RECUSAS',
    pe='Bloqueio 002 · 2026',
)

# ══════════ 03 · a peca que explica o carimbo ══════════
pagina(
    'Bloq03',
    '<div class="bloco" style="top:236px">'
    '<p class="rot">Por que a gente publica os próprios bloqueios</p>'
    '<div class="fala" style="position:relative;left:0;right:-52px;top:26px;font-size:96px">'
    'A ferramenta existe para <span class="m">reprovar a gente.</span></div>'
    '</div>'
    '<div class="bloco" style="top:730px">'
    '<p class="mono">'
    'Antes de qualquer material nosso sair, ele passa por uma régua que tenta '
    'reprovar ele. Ela bloqueia número que não está na nossa base de evidências, '
    'preço fora da tabela, promessa que a infraestrutura não sustenta e qualquer '
    'frase que diga que a IA decide sozinha.<br><br>'
    '<b>Bloqueio significa que o material não sai.</b> Existe uma opção de forçar, '
    'e usar ela é uma decisão com nome em cima.'
    '</p></div>'
    '<div class="bloco" style="top:1108px">'
    '<p class="cor">O que impede, hoje, um número inventado de sair da sua empresa '
    '<i>dentro de uma proposta assinada?</i></p></div>',
    navy=True, cab_dir='Régua do Revisor · v1.5.0', pe_esq='contato@abbaservices.com.br',
)

# ══════════ escrita ══════════



# ══════════════════════════════════════════════════════════════════════════
# CAMPANHA "BOMBA" — a metafora e do socio (03/09): "transformar a empresa,
# potencializa-la, faze-la tomar bomba, mas que nao faz mal a longo prazo".
#
# Por que ela e boa, e nao e so engracada:
#
#   · TODO MUNDO ENTENDE NA HORA. Nao precisa explicar o que e bomba, e
#     ninguem usa essa metafora em B2B. Custa zero e nao tem dono.
#   · ELA JA E A DOUTRINA DA CASA, so que em outra lingua. O DORA diz que a IA
#     AMPLIFICA o que ja existe: bomba amplifica. Base ruim, carga pesada,
#     lesao. O METR diz que os caras se sentiram 20% mais rapidos e estavam
#     19% mais lentos: e exatamente quem se olha no espelho e se acha maior.
#     A recusa de prometer acuracia que nao se mede e a bula.
#   · E O CAMINHO MAIS CURTO ATE "AI NATIVE". Empresa AI native nao esta
#     dopada, esta treinada. Nao e dose, e fisiologia.
#
# A regra do guardiao continua valendo: a piada e sobre a pratica, nunca sobre
# pessoa nem empresa com nome, e toda peca fecha num numero do canone.
# ══════════════════════════════════════════════════════════════════════════

BULA_CSS = '''
  <style>
    .secao { display:grid; grid-template-columns:250px 1fr; gap:34px;
             padding:30px 0; border-top:1px solid #CBD3DF; }
    .navy .secao { border-top-color:#33456A; }
    .secao:last-of-type { border-bottom:1px solid #CBD3DF; }
    .navy .secao:last-of-type { border-bottom-color:#33456A; }
    .secao .k { font-family:"IBM Plex Mono", monospace; font-size:19px;
                letter-spacing:.18em; text-transform:uppercase; color:#8A6E28;
                line-height:1.5; }
    .navy .secao .k { color:#C2A35B; }
    .secao .v { font-family:"IBM Plex Mono", monospace; font-size:26px;
                line-height:1.62; color:#4E5A70; }
    .navy .secao .v { color:#C3CAD8; }
    .secao .v b { color:#1B2A4A; font-weight:600; }
    .navy .secao .v b { color:#FFFFFF; }
    .selo { position:absolute; font-family:"IBM Plex Mono", monospace;
            font-weight:600; font-size:20px; letter-spacing:.3em;
            border:3px solid #8A6E28; color:#8A6E28; padding:12px 22px;
            filter:url(#tinta); }
  </style>
'''
STYLE = STYLE + BULA_CSS

# ── 04 · a capa da campanha ───────────────────────────────────────────────
pagina(
    'Bomba01',
    '<div class="bloco" style="top:250px">'
    '<p class="rot">Sobre atalho</p></div>'
    '<div class="fala" style="top:330px;font-size:130px">'
    'Tem empresa tomando <span class="g">bomba</span> de IA.</div>'
    '<div class="bloco" style="top:900px">'
    '<p class="cor">Cresce rápido. Fica bem na foto do trimestre. '
    'E <b>quebra na primeira carga real.</b></p></div>'
    '<div class="bloco" style="top:990px">'
    '<p class="mono">Mais de 80% dos projetos de IA falham, o dobro da taxa dos '
    'projetos de TI comuns.<br>RAND, 65 engenheiros de machine learning sêniores.</p>'
    '</div>',
    navy=False, cab_dir='Campanha · Bomba 01/05', pe_esq='Prova, não impressão.',
)

# ── 05 · a bula ───────────────────────────────────────────────────────────
pagina(
    'Bomba02',
    '<div class="bloco" style="top:196px">'
    '<p class="rot">Bula · uso corporativo</p>'
    '<div class="fala" style="position:relative;left:0;right:-52px;top:8px;'
    'font-size:104px">IA sem fundação</div></div>'
    '<div class="bloco" style="top:470px">'
    '<div class="secao"><div class="k">Composição</div><div class="v">'
    'ferramenta comprada · piloto sem métrica combinada · pressa de diretoria'
    '</div></div>'
    '<div class="secao"><div class="k">Contraindicações</div><div class="v">'
    'processo bagunçado · dado que ninguém confia · <b>sucesso não combinado antes</b>'
    '</div></div>'
    '<div class="secao"><div class="k">Efeitos colaterais</div><div class="v">'
    'sistema que uma pessoa só entende · fornecedor que some levando o '
    'conhecimento · a descoberta, dois anos depois, de que trocar custa mais '
    'do que custou o projeto'
    '</div></div>'
    '</div>'
    '<div class="bloco" style="top:1020px">'
    '<p class="mono">A causa número um do fracasso não é técnica.<br>'
    '<b>É começar sem combinar o que seria dar certo.</b> RAND.</p></div>',
    navy=False, cab_dir='Campanha · Bomba 02/05', pe_esq='Prova, não impressão.',
)

# ── 06 · o exame ──────────────────────────────────────────────────────────
pagina(
    'Bomba03',
    '<div class="bloco" style="top:250px"><p class="rot">O espelho mente</p></div>'
    '<div class="fala" style="top:326px;font-size:138px">'
    'No espelho, cresceu.<br><span class="g">No exame, não.</span></div>'
    '<div class="bloco" style="top:730px">'
    '<div class="secao"><div class="k">No espelho</div>'
    '<div class="v"><b>20% mais rápidos</b>, foi o que eles relataram</div></div>'
    '<div class="secao"><div class="k">No cronômetro</div>'
    '<div class="v"><b>19% mais lentos</b>, foi o que a medição registrou</div></div>'
    '</div>'
    '<div class="bloco" style="top:1030px">'
    '<p class="mono">Desenvolvedores experientes, 246 tarefas reais, tempo '
    'cronometrado.<br>METR, julho de 2025.</p></div>',
    navy=False, cab_dir='Campanha · Bomba 03/05', pe_esq='Prova, não impressão.',
)

# ── 07 · a amplificacao ───────────────────────────────────────────────────
pagina(
    'Bomba04',
    '<div class="bloco" style="top:250px"><p class="rot">O que a substância faz</p></div>'
    '<div class="fala" style="top:326px;font-size:122px">'
    'Bomba não conserta técnica ruim. <span class="m">Ela amplifica.</span></div>'
    '<div class="bloco" style="top:900px">'
    '<p class="cor">Time com a base arrumada acelera. Time com processo bagunçado '
    '<b>piora, e piora mais rápido.</b> Automatizar um cadastro errado só faz o '
    'erro chegar mais cedo.</p></div>'
    '<div class="bloco" style="top:1050px">'
    '<p class="mono">A IA amplifica o que já existe. Relatório DORA, Google.</p></div>',
    navy=False, cab_dir='Campanha · Bomba 04/05', pe_esq='Prova, não impressão.',
)

# ── 08 · o fecho: e aqui que "AI native" entra ────────────────────────────
pagina(
    'Bomba05',
    '<div class="bloco" style="top:236px"><p class="rot">O outro caminho</p></div>'
    '<div class="fala" style="top:312px;font-size:138px">'
    'Não é dose.<br><span class="m">É fisiologia.</span></div>'
    '<div class="bloco" style="top:770px">'
    '<p class="cor">Empresa <i>AI native</i> não está dopada. Está treinada. '
    'É a empresa que você teria desenhado hoje, construída a partir da que você '
    'já tem, gargalo por gargalo, com <b>métrica combinada antes e medida depois.</b></p>'
    '</div>'
    '<div class="bloco" style="top:1030px">'
    '<p class="mono">→ &nbsp;contato@abbaservices.com.br</p></div>',
    navy=True, cab_dir='Campanha · Bomba 05/05', pe_esq='Prova, não impressão.',
)

for nome, html in F.items():
    open(nome + '.dc.html', 'w', encoding='utf-8').write(html)
print('campanha bomba:', ' '.join(sorted(n for n in F if n.startswith('Bomba'))))
