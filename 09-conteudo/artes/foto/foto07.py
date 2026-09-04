# -*- coding: utf-8 -*-
# Peca 07 com foto. A composicao RESPONDE a imagem, nao o contrario.
#
# Nesta foto o objeto esta embaixo e a metade de cima e campo vazio, entao a
# mancha de texto sobe. O molde generico punha o texto embaixo; obedecer o
# molde aqui cobriria o cronometro. Molde e ponto de partida, nao lei.
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

STYLE = '''
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=IBM+Plex+Mono:wght@400;500&display=swap">
  <style>
    body { margin:0; } x-dc { display:block; } helmet { display:none; }
    .p { width:1080px; height:1350px; position:relative; overflow:hidden;
         background:#16233E; color:#FFFFFF;
         font-family:"Source Serif 4", Georgia, serif; }

    .foto { position:absolute; top:0; left:0; width:1080px; height:1350px;
            background:url("cronometro.jpg") center/cover no-repeat; }

    /* Veu leve em cima, para a tipografia branca ganhar do azul, e veu forte
       so na faixa do rodape. No miolo a foto fica limpa: e ela que trabalha. */
    .veu { position:absolute; top:0; left:0; width:1080px; height:1350px;
           background:linear-gradient(180deg,
             rgba(9,16,30,.58) 0%, rgba(9,16,30,.44) 34%,
             rgba(9,16,30,.06) 52%, rgba(9,16,30,0) 68%,
             rgba(9,16,30,.30) 88%, rgba(9,16,30,.72) 100%); }

    .grao { position:absolute; top:0; left:0; width:1080px; height:1350px;
            background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E");
            background-size:240px 240px; opacity:.11; mix-blend-mode:overlay; }

    .cab { position:absolute; top:70px; left:96px; right:96px; display:flex;
           justify-content:space-between; font-family:"IBM Plex Mono", monospace;
           font-size:19px; letter-spacing:.2em; color:#C3CAD8; }
    .fio { position:absolute; left:96px; height:1px; width:888px;
           background:rgba(255,255,255,.26); }

    .rot { position:absolute; left:96px; top:206px; margin:0;
           font-family:"IBM Plex Mono", monospace; font-size:21px;
           letter-spacing:.24em; text-transform:uppercase; color:#D8BE7C; }
    h1 { position:absolute; left:96px; right:-40px; top:262px; margin:0;
         font-family:"Newsreader", Georgia, serif; font-weight:400;
         font-size:106px; line-height:1.03; letter-spacing:-.024em;
         text-shadow:0 2px 30px rgba(9,16,30,.5); }
    h1 i { font-style:italic; font-weight:300; color:#D8BE7C; }
    .lede { position:absolute; left:96px; top:512px; width:800px; margin:0;
            font-size:31px; line-height:1.46; color:#DCE2EC;
            text-shadow:0 2px 24px rgba(9,16,30,.6); }
    .pe { position:absolute; top:1186px; left:96px; right:96px; display:flex;
          justify-content:space-between; font-family:"IBM Plex Mono", monospace;
          font-size:21px; letter-spacing:.16em; color:#AEB8C8; }
    .pe .ouro { color:#C2A35B; }
  </style>
'''

open('Foto07.dc.html','w',encoding='utf-8').write(
 '<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
 '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>' + STYLE + '</helmet>\n'
 '<div class="p">'
 '<div class="foto"></div><div class="veu"></div><div class="grao"></div>'
 '<div class="cab"><span>ABBA</span><span>PEÇA 07</span></div>'
 '<div class="fio" style="top:116px"></div>'
 '<div class="fio" style="top:1140px"></div>'
 '<p class="rot">O estudo mais desconfortável do ano</p>'
 '<h1>O cronômetro <i>discordou.</i></h1>'
 '<p class="lede">Desenvolvedores experientes se sentiram 20% mais rápidos usando IA. '
 'A medição registrou 19% mais lentos.</p>'
 '<div class="pe"><span>METR, jul/2025</span>'
 '<span class="ouro">abbaservices.com.br</span></div>'
 '</div>\n</x-dc>\n</body>\n</html>\n')
print('composto')
