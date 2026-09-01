# -*- coding: utf-8 -*-
# Sistema visual do social da ABBA. Documento de registro.
# Sem travessao em texto de peca (decisao do socio V3v, 2026-08-11, reafirmada 2026-08-27).
import json, os
os.chdir('/home/user/abba-feed')
W, HT = 1080, 1350
M = 104                      # margem lateral
TOP, BOT = 196, 168          # mancha dentro do recorte 1:1 da grade

STYLE = '''
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300;1,6..72,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
  <style>
    body { margin:0; }
    a { color:#C2A35B; } a:hover { color:#D9BA72; }
    .p { width:1080px; height:1350px; box-sizing:border-box; position:relative;
         overflow:hidden; background:#1B2A4A; color:#FFFFFF;
         font-family:"Source Serif 4", Georgia, serif; }
    .p.paper { background:#F2F4F7; color:#1B2A4A; }

    .frame { position:absolute; inset:0; pointer-events:none; }
    .hair { position:absolute; background:#33456A; }
    .paper .hair { background:#CBD3DF; }
    .gold { position:absolute; background:#C2A35B; }

    .folio { position:absolute; top:96px; font-family:"IBM Plex Mono", monospace;
             font-size:19px; letter-spacing:.2em; color:#5D6E92; }
    .paper .folio { color:#8C97AA; }
    .folio.l { left:104px; } .folio.r { right:104px; text-align:right; }
    .ref { position:absolute; bottom:92px; left:104px; font-family:"IBM Plex Mono", monospace;
           font-size:19px; letter-spacing:.2em; color:#5D6E92; }
    .paper .ref { color:#8C97AA; }
    .refr { position:absolute; bottom:92px; right:104px; font-family:"IBM Plex Mono", monospace;
            font-size:19px; letter-spacing:.2em; color:#C2A35B; }

    .stage { position:absolute; left:104px; right:104px; top:196px; bottom:168px;
             display:flex; flex-direction:column; }

    .label { font-family:"IBM Plex Mono", monospace; font-size:20px; letter-spacing:.22em;
             text-transform:uppercase; color:#C2A35B; margin:0 0 30px; }
    .label.mute { color:#5D6E92; } .paper .label.mute { color:#8C97AA; }

    h1 { font-family:"Newsreader", Georgia, serif; font-weight:400; margin:0;
         font-size:80px; line-height:1.12; letter-spacing:-.014em; color:#FFFFFF;
         text-wrap:balance; }
    .paper h1 { color:#1B2A4A; }
    h1.sm { font-size:68px; } h1.xs { font-size:56px; line-height:1.18; }
    h1 i { font-style:italic; color:#D8BE7C; font-weight:300; }
    .paper h1 i { color:#8A6E28; }

    .lede { font-size:36px; line-height:1.5; color:#C3CAD8; margin:34px 0 0; max-width:840px; }
    .paper .lede { color:#4E5A70; }
    .lede b { color:#FFFFFF; font-weight:600; } .paper .lede b { color:#1B2A4A; }
    .rule { height:1px; background:#C2A35B; width:96px; margin:44px 0 0; flex:none; }

    table { border-collapse:collapse; width:100%; margin-top:8px; }
    td, th { text-align:left; vertical-align:top; padding:24px 22px 24px 0;
             border-bottom:1px solid #33456A; }
    .paper td, .paper th { border-bottom-color:#CBD3DF; }
    th { font-family:"IBM Plex Mono", monospace; font-size:19px; letter-spacing:.2em;
         text-transform:uppercase; color:#C2A35B; font-weight:400; padding-bottom:16px; }
    td { font-size:30px; line-height:1.42; color:#C3CAD8; }
    .paper td { color:#4E5A70; }
    td.k { font-family:"IBM Plex Mono", monospace; font-size:21px; color:#5D6E92;
           width:74px; letter-spacing:.08em; padding-top:28px; }
    .paper td.k { color:#9AA4B6; }
    td b { color:#FFFFFF; font-weight:600; } .paper td b { color:#1B2A4A; }

    .steps { display:flex; flex-direction:column; margin-top:6px; }
    .step { display:grid; grid-template-columns:96px 1fr; gap:30px;
            padding:26px 0; border-bottom:1px solid #33456A; align-items:baseline; }
    .paper .step { border-bottom-color:#CBD3DF; }
    .step:last-child { border-bottom:none; }
    .step .n { font-family:"IBM Plex Mono", monospace; font-size:24px; color:#C2A35B;
               letter-spacing:.1em; font-variant-numeric:tabular-nums; }
    .step h3 { font-family:"Newsreader", Georgia, serif; font-weight:400; font-size:38px;
               line-height:1.2; margin:0 0 8px; color:#FFFFFF; }
    .paper .step h3 { color:#1B2A4A; }
    .step p { font-size:26px; line-height:1.44; color:#8E9AB4; margin:0; }
    .paper .step p { color:#6B778E; }

    .marg { display:grid; grid-template-columns:1fr 268px; gap:52px; align-items:start; }
    .margnote { font-family:"IBM Plex Mono", monospace; font-size:21px; line-height:1.65;
                color:#7C88A2; border-left:1px solid #C2A35B; padding-left:24px; }
    .paper .margnote { color:#78839A; }

    .note { margin-top:auto; display:flex; gap:20px; align-items:flex-start;
            padding-top:26px; border-top:1px solid #33456A; }
    .paper .note { border-top-color:#CBD3DF; }
    .note .mk { font-family:"IBM Plex Mono", monospace; font-size:19px; color:#C2A35B;
                flex:none; line-height:1.7; }
    .note p { font-size:22px; line-height:1.55; color:#7C88A2; margin:0; }
    .paper .note p { color:#78839A; }


    /* ── Grao. O fundo chapado lia como slide; com grao le como impresso.
       E o unico jeito honesto de dar textura sem imagem generica de IA. ── */
    .grain { position:absolute; inset:0; pointer-events:none;
             background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E"); background-size:240px 240px;
             opacity:.06; mix-blend-mode:overlay; }
    .paper .grain { opacity:.42; mix-blend-mode:multiply; }
    .gold .grain  { opacity:.30; mix-blend-mode:multiply; }

    /* ── Terceiro fundo: campo dourado. Existe para dar contraste de valor
       na grade do perfil, onde tudo era navy. Acento por italico, nunca por
       cor, porque nada claro tem contraste suficiente sobre o dourado. ── */
    .p.gold { background:#C2A35B; color:#1B2A4A; }
    .gold .hair { background:#A98D48; }
    /* colisao de nome: a barra de progresso e a marca de continuidade usam a
       classe .gold, que sobre o cartao dourado ficava dourado sobre dourado.
       No campo dourado elas viram bronze escuro. */
    .p.gold .gold { background:#3E3210; }
    .gold .folio, .gold .ref { color:#6F5A22; }
    .gold .refr { color:#3E3210; }
    .gold .label { color:#5C4A18; }
    .gold .label.mute { color:#6F5A22; }
    .gold h1, .gold h1 i { color:#1B2A4A; }
    .gold .lede { color:#4A3D18; }
    .gold .lede b { color:#1B2A4A; }
    .gold .rule { background:#3E3210; }
    .gold .note { border-top-color:#A98D48; }
    .gold .note p { color:#5C4A18; }
    .gold .note .mk { color:#3E3210; }
    .gold td, .gold th { border-bottom-color:#A98D48; }
    .gold td { color:#4A3D18; } .gold td b { color:#1B2A4A; }
    .gold td.k { color:#6F5A22; }

    /* ── Capa cheia. A grade do perfil deixou de recortar em 1:1 e passou a
       mostrar quase o cartao inteiro, entao a capa antiga, que usava so o
       terco de cima, aparecia com metade vazia em toda miniatura. A capa
       agora ancora embaixo: o rotulo fica no topo, o vazio no meio, e a
       frase grande fecha o cartao. ── */
    .stage.cover .label { margin-bottom:auto; }
    .cover h1.c1 { font-size:132px; line-height:1.04; letter-spacing:-.022em; }
    .cover h1.c2 { font-size:112px; line-height:1.06; letter-spacing:-.02em; }
    .cover h1.c3 { font-size:94px;  line-height:1.08; letter-spacing:-.018em; }
    .cover h1.c4 { font-size:78px;  line-height:1.12; letter-spacing:-.014em; }
    .cover .rule { margin-top:38px; }
    .cover .lede { font-size:31px; margin-top:30px; max-width:800px; }

    /* ── Numero heroi. Quando a manchete E um numero do canone, o numero
       vira a imagem da capa. E o unico "interrompe o scroll" que esta casa
       pode usar sem inventar nada. ── */
    .hero { font-family:"Newsreader", Georgia, serif; font-weight:300;
            font-size:300px; line-height:.84; letter-spacing:-.045em;
            color:#D8BE7C; margin:0 0 26px; font-variant-numeric:tabular-nums; }
    .paper .hero { color:#8A6E28; } .gold .hero { color:#1B2A4A; }
    .hero .u { font-size:.42em; letter-spacing:-.01em; vertical-align:.52em; }
    .heropre { font-family:"IBM Plex Mono", monospace; font-size:24px;
               letter-spacing:.22em; text-transform:uppercase; color:#8E9AB4;
               margin:0 0 14px; }
    .paper .heropre { color:#78839A; } .gold .heropre { color:#5C4A18; }
    .cover h1.sub { font-size:62px; line-height:1.14; letter-spacing:-.01em; }

    /* ── Figura. Duas cores so, tiradas do proprio sistema: #D8BE7C para o
       que foi medido e #7C88A2 para o que foi sentido. Separacao conferida
       no validador (normal 22,5 · protan 20,7 · tritan 20,8; contraste
       acima de 3:1 sobre o navy). Cada barra tem rotulo proprio, entao a
       identidade nunca depende so da cor. ── */
    .fig { margin-top:auto; margin-bottom:auto; }
    .fig .v { font-family:"Newsreader", Georgia, serif; font-size:54px; fill:#FFFFFF; }
    .fig .k { font-family:"IBM Plex Mono", monospace; font-size:20px;
              letter-spacing:.2em; fill:#8E9AB4; }
    .fig .g { font-family:"IBM Plex Mono", monospace; font-size:20px;
              letter-spacing:.2em; fill:#C2A35B; }
    .paper .fig .v { fill:#1B2A4A; } .paper .fig .k { fill:#6B778E; }

    .mark { display:block; width:190px; height:auto; opacity:.96; }
    /* Placa de parceiro. A marca oficial vai sobre campo branco, com folga em
       volta, sem recorte e sem recolorir (V3o e guia de marca de cada parceiro).
       As duas placas tem a mesma caixa de propósito: lidas em sequencia, elas
       formam um par, e nao dois tratamentos diferentes. Por isso a placa so
       aparece em tela de papel: no navy a marca perderia contraste e a unica
       saida seria altera-la. */
    .plate { width:420px; height:152px; box-sizing:border-box; background:#FFFFFF;
             border:1px solid #CBD3DF; display:flex; align-items:center;
             justify-content:center; }
    .plogo { display:block; width:auto; }
    .plogo.ms { height:62px; }
    .plogo.crew { height:70px; }
  </style>
'''
HEAD = ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
        '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>'
        + STYLE + '</helmet>\n')
TAIL = '</x-dc>\n</body>\n</html>\n'

def page(i, n, ref, folio_r, body, paper=False):
    """i = indice 0-based da tela; n = total. Constroi a moldura com as duas
    tecnicas de transicao: barra de progresso e marca de continuidade.
    `paper` aceita False (navy), True (papel) ou a string 'gold'."""
    ground = {False:"", True:" paper", "gold":" gold", "paper":" paper"}[paper]
    cls = "p" + ground
    span = W - 2*M
    # 1. barra de progresso: fiada cheia + segmento dourado proporcional
    prog = round(span * (i+1) / n)
    # 2. marca de continuidade: sai pela direita em y_i, entra pela esquerda em y_{i-1}
    def ty(k): return round(300 + k * (760 / max(n-1, 1)))
    out_y, in_y = ty(i), ty(i-1) if i > 0 else None
    f = ['<div class="grain"></div>', '<div class="frame">',
         f'<div class="hair" style="left:{M}px;right:{M}px;top:150px;height:1px"></div>',
         f'<div class="gold" style="left:{M}px;top:149px;width:{prog}px;height:3px"></div>',
         f'<div class="hair" style="left:{M}px;right:{M}px;bottom:146px;height:1px"></div>']
    if i < n-1:
        f.append(f'<div class="gold" style="right:0;top:{out_y}px;width:56px;height:2px"></div>')
    if in_y is not None:
        f.append(f'<div class="gold" style="left:0;top:{in_y}px;width:56px;height:2px"></div>')
    f.append('</div>')
    return (HEAD + f'<div class="{cls}">' + "".join(f) +
            f'<span class="folio l">ABBA</span><span class="folio r">{folio_r}</span>'
            f'<div class="stage{" cover" if i == 0 else ""}">{body}</div>'
            f'<span class="ref">{ref}</span>'
            f'<span class="refr">abbaservices.com.br</span>'
            '</div>\n' + TAIL)

def note(mk, txt):
    return f'<div class="note"><span class="mk">{mk}</span><p>{txt}</p></div>'


def fig_distancia():
    """A distancia entre o que foi medido e o que foi sentido (METR).

    FORMA: duas barras divergindo de uma linha de zero. O trabalho do dado e
    POLARIDADE, uma perda real contra um ganho percebido, e nao comparacao de
    magnitude, entao o zero fica no meio e as barras crescem em sentidos
    opostos. E a unica forma que faz a distancia de 40 pontos ser vista em vez
    de lida.

    COR: dourado #D8BE7C no medido, ardosia #7C88A2 no percebido, as duas ja no
    sistema. Conferido no validador de paleta: separacao normal 22,5 · protan
    20,7 · tritan 20,8, e as duas acima de 3:1 sobre o navy.

    TEXTO: tinta do sistema, nunca a cor da serie. Cada barra carrega o proprio
    rotulo, colado nela, entao a identidade nunca depende so da cor.

    Sem camada de hover, de proposito: isto vira PNG de carrossel, nao pagina.
    """
    Z, U, X, BW, R = 330, 9.5, 40, 300, 6   # zero · px/ponto · x · largura · raio
    hA, hB = round(19*U), round(20*U)       # medido p/ baixo · percebido p/ cima
    G = 3                                   # respiro de superficie entre as duas
    def barra(h, baixo, cor):
        y0 = Z + G if baixo else Z - G      # a barra nao encosta na linha do zero:
        y1 = Z + h if baixo else Z - h      # sem o respiro as duas viram um bloco so
        sy = -R if baixo else R
        return (f'<path d="M{X},{y0} L{X},{y1+sy} Q{X},{y1} {X+R},{y1} '
                f'L{X+BW-R},{y1} Q{X+BW},{y1} {X+BW},{y1+sy} L{X+BW},{y0} Z" fill="{cor}"/>')
    bx = X + BW + 46                        # colchete da distancia
    return f'''<div class="fig"><svg viewBox="0 0 928 640" width="928" height="640">
  <text class="k" x="{X}" y="56">RELATADO POR ELES</text>
  <text class="v" x="{X}" y="112">20% mais rápidos</text>
  {barra(hB, False, "#7C88A2")}
  {barra(hA, True,  "#D8BE7C")}
  <line x1="0" y1="{Z}" x2="{X+BW+18}" y2="{Z}" stroke="#7C88A2" stroke-width="1"/>
  <text class="v" x="{X}" y="{Z+hA+82}">19% mais lentos</text>
  <text class="k" x="{X}" y="{Z+hA+124}">MEDIDO NO CRONÔMETRO</text>

  <path d="M{bx},{Z-hB} L{bx+16},{Z-hB} L{bx+16},{Z+hA} L{bx},{Z+hA}"
        fill="none" stroke="#C2A35B" stroke-width="1"/>
  <text class="g" x="{bx+40}" y="{Z-6}">40 PONTOS</text>
  <text class="g" x="{bx+40}" y="{Z+26}">DE DISTÂNCIA</text>
</svg></div>'''


F, PAGES = {}, []

def peca(pid, nome, prefixo, sec, telas):
    """telas: lista de (folio, corpo, paper)"""
    n = len(telas)
    nomes = []
    for i, (folio, body, paper) in enumerate(telas):
        nm = f"{prefixo}{i+1:02d}"
        F[nm] = page(i, n, f"§{sec} · {i+1:02d}/{n:02d}", folio, body, paper)
        nomes.append(nm)
    PAGES.append((pid, nome, nomes))

# ═══════════ PEÇA 01 · A TESE ═══════════
peca("peca-01", "01 · A tese", "Tese", 1, [
 ("PEÇA 01", '''
<p class="label">Consultoria de inteligência artificial</p>
<h1 class="c1">Tornamos a sua empresa <i>AI native.</i></h1>
<div class="rule"></div>
<p class="lede">E provamos, de fora, o que isso mudou. Número combinado antes. Medido depois, do mesmo jeito. Assinado por gente que responde por ele.</p>
''', False),
 ("QUEM SOMOS", '''
<p class="label mute">Quem somos</p>
<h1 class="sm">Entramos na sua empresa para <i>entendê-la a fundo.</i></h1>
<p class="lede">Construímos as soluções certas para o seu fluxo de trabalho, validamos cada uma com <b>dados reais</b> antes de qualquer investimento pesado, formamos as suas pessoas e ficamos ao seu lado acompanhando, mês a mês, <b>o que mudou.</b></p>
''', False),
 ("AS DUAS FRENTES", '''
<p class="label">O trabalho acontece em duas frentes ao mesmo tempo</p>
<table>
<tr><td class="k">01</td><td><b>Nos processos.</b> Projetamos e implantamos sistemas inteligentes, com arquitetura, integrações e agentes de IA trabalhando em conjunto, que tornam a operação mais eficiente, mais rápida e mais poderosa.</td></tr>
<tr><td class="k">02</td><td><b>Nas pessoas.</b> Formamos cada nível da equipe para trabalhar com IA e enxergar o próprio trabalho de um jeito novo, do conselho à linha de frente.</td></tr>
</table>
''' + note("·", "De nada adiantam sistemas novos com a empresa pensando do jeito antigo. Por isso as duas frentes andam juntas."), False),
 ("O PROCESSO", '''
<p class="label mute">O nosso processo</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Começa com quem decide e só termina <i>quando chega a quem executa.</i></h1>
  <div class="margnote">Uma empresa não muda por uma ponta só.</div>
</div>
''', True),
 ("AS TRÊS PERGUNTAS", '''
<p class="label">A mentalidade que instalamos em cada pessoa</p>
<div class="steps">
  <div class="step"><span class="n">I</span><div><h3>O que eu posso parar de fazer,</h3><p>porque a IA agora faz?</p></div></div>
  <div class="step"><span class="n">II</span><div><h3>O que eu posso começar a fazer,</h3><p>porque a IA agora permite?</p></div></div>
  <div class="step"><span class="n">III</span><div><h3>O que só eu faço,</h3><p>e devo fazer ainda melhor?</p></div></div>
</div>
''' + note("·", "O objetivo não é ensinar ferramenta. Quando a organização inteira pensa assim, a mudança deixa de depender de consultor."), False),
 ("COMO TRABALHAMOS", '''
<p class="label mute">Como trabalhamos</p>
<h1 class="sm">A IA rascunha.<br>Um humano <i>assina.</i><br>A diretoria decide.</h1>
<p class="lede">Toda decisão entra num registro: métrica combinada antes, resultado medido depois. E vocês veem o registro inteiro, <b>incluindo o que não funcionou.</b></p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">O próximo passo</p>
<h1 class="sm">Uma conversa de 45 minutos, e o seu <i>assessment gratuito</i> da empresa.</h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 02 · A JORNADA ═══════════
JORNADA = [
 ("1","A primeira conversa","45 min · assessment gratuito da empresa"),
 ("2","Avaliação de Prontidão","o mergulho profundo · portfólio ranqueado"),
 ("3","Protótipo de caso de uso","dados reais · GO ou NO-GO com números"),
 ("4","Construção e implantação","engenharia sob medida · em produção"),
 ("5","Treinamento + ABBA Portal","todos os níveis · campeões internos"),
 ("6","Sistemas gerenciados","ritual semanal · o registro do que mudou"),
 ("7","Conselheiro de IA","a cadeira de estrategista, do seu lado"),
]
def espinha():
    x, y0, dy = 46, 26, 108
    q = [f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0+dy*6}" stroke="#33456A" stroke-width="1"/>']
    for i,(n,t,s) in enumerate(JORNADA):
        y = y0 + dy*i
        q += [f'<circle cx="{x}" cy="{y}" r="5" fill="#C2A35B"/>',
              f'<text x="{x-22}" y="{y+7}" text-anchor="end" font-family="IBM Plex Mono, monospace" font-size="21" fill="#5D6E92" letter-spacing="1">{n}</text>',
              f'<text x="{x+34}" y="{y-2}" font-family="Newsreader, Georgia, serif" font-size="35" fill="#FFFFFF">{t}</text>',
              f'<text x="{x+34}" y="{y+30}" font-family="IBM Plex Mono, monospace" font-size="18" fill="#7C88A2" letter-spacing="1.2">{s}</text>']
    yb = y0 + dy*6
    for dx in (-120,-46,46,120):
        q.append(f'<path d="M{x} {yb+14} C {x} {yb+70}, {x+dx} {yb+62}, {x+dx} {yb+128}" fill="none" stroke="#33456A" stroke-width="1"/>')
    q.append(f'<text x="{x-4}" y="{yb+176}" font-family="IBM Plex Mono, monospace" font-size="19" fill="#5D6E92" letter-spacing="3.4" text-anchor="middle">ATÉ CADA PESSOA, EM CADA PROCESSO</text>')
    return f'<svg viewBox="0 0 872 {yb+210}" width="100%" style="margin-top:auto;margin-bottom:auto" aria-hidden="true">{"".join(q)}</svg>'

peca("peca-02", "02 · A jornada", "Jornada", 2, [
 ("PEÇA 02", '''
<p class="label">O caminho completo</p>
<h1 class="c1">A jornada,<br>em <i>sete passos.</i></h1>
<div class="rule"></div>
<p class="lede">Da primeira conversa à cadeira de estrategista na sua diretoria. Cada etapa entrega algo inteiro sozinha e produz o insumo da próxima.</p>
''', True),
 ("O DESENHO", espinha(), False),
 ("ETAPAS 1 E 2", '''
<p class="label">Antes de qualquer investimento</p>
<div class="steps">
  <div class="step"><span class="n">1</span><div><h3>A primeira conversa</h3><p>45 minutos, e nós já chegamos com um assessment da sua empresa feito só com informação pública: nota de maturidade em IA, oportunidades priorizadas e o ledger de todas as fontes que usamos.</p></div></div>
  <div class="step"><span class="n">2</span><div><h3>Avaliação de Prontidão: o mergulho profundo</h3><p>Do conselho à linha de frente: como o trabalho realmente flui, onde quebra, onde vaza valor. Você sai com um portfólio de oportunidades ranqueado e quantificado, não com uma lista de ideias.</p></div></div>
</div>
''' + note("·", "Ninguém deveria pagar para descobrir se faz sentido."), False),
 ("ETAPA 3", '''
<p class="label mute">Etapa 3 · a prova antes do investimento</p>
<h1 class="xs">O caso mais promissor, construído com <i>os seus dados reais.</i></h1>
<p class="lede">A sua diretoria decide GO ou NO-GO com números na mesa.</p>
<p class="lede"><b>NO-GO também é resultado:</b> custou pouco e evitou um investimento errado.</p>
''', True),
 ("ETAPA 4", '''
<p class="label">Etapa 4 · a engenharia da solução</p>
<table>
<tr><th>O quê</th></tr>
<tr><td>Projetamos a arquitetura, com dados, integrações e lógica de decisão, e construímos sistemas sob medida, com <b>agentes de IA inseridos onde fazem diferença</b>, em produção no fluxo real da sua equipe.</td></tr>
<tr><th>Como</th></tr>
<tr><td>Com a tecnologia dos nossos parceiros e <b>pontos de aprovação humana em tudo que é crítico:</b> a IA executa, gente da sua confiança valida.</td></tr>
</table>
''' + note("·", "Relatório na gaveta não muda empresa. Sistema rodando muda."), False),
 ("ETAPA 5", '''
<p class="label">Etapa 5 · as pessoas</p>
<h1 class="xs">Formamos todos os níveis, na plataforma própria e em <i>sessões presenciais.</i></h1>
<p class="lede">O objetivo não é ensinar ferramenta. É instalar, em cada pessoa, três perguntas que mudam o jeito de olhar o próprio trabalho.</p>
''' + note("·", "Campeões internos carregam a transformação depois que saímos da sala, e a capacidade fica com vocês."), False),
 ("ETAPAS 6 E 7", '''
<p class="label">Depois que está rodando</p>
<div class="steps">
  <div class="step"><span class="n">6</span><div><h3>Sistemas gerenciados</h3><p>Operamos o que construímos: monitoramento, evolução contínua e um ritual semanal de 20 minutos com quem decide. Toda decisão entra num registro: métrica combinada antes, resultado medido depois.</p></div></div>
  <div class="step"><span class="n">7</span><div><h3>Conselheiro de IA</h3><p>Um estrategista de IA presente na sua diretoria: roadmap vivo, governança e análise independente de qualquer proposta de fornecedor que chegar.</p></div></div>
</div>
''', False),
 ("A CADEIRA", '''
<p class="label mute">Por que a etapa 7 existe</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Todo fornecedor de IA tem um vendedor. A sua mesa merece <i>alguém do seu lado</i> quando a fatura chega.</h1>
  <div class="margnote">Também para quem já tem IA rodando. Não precisa do programa para ter a cadeira.</div>
</div>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Onde vocês estão nesse caminho hoje?</p>
<h1 class="sm">A história começa com uma conversa de <i>45 minutos.</i></h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 03 · PROMETEMOS × RECUSAMOS ═══════════
peca("peca-03", "03 · Prometemos × Recusamos", "Recusa", 3, [
 ("PEÇA 03", '''
<p class="label">O documento que define uma consultoria</p>
<h1 class="c1">O que prometemos,<br>e o que <i>recusamos.</i></h1>
<div class="rule"></div>
<p class="lede">Escopo sem limite é escopo sem preço. Toda proposta nossa tem uma seção do que não vamos fazer.</p>
''', False),
 ("PROMETEMOS", '''
<p class="label">Prometemos</p>
<table>
<tr><td class="k">I</td><td><b>O método.</b> Métrica combinada antes, medida depois, num registro que vocês veem inteiro.</td></tr>
<tr><td class="k">II</td><td><b>Presença recorrente de quem decide,</b> não um relatório na gaveta.</td></tr>
<tr><td class="k">III</td><td><b>Honestidade sobre escopo:</b> o que fazemos, nomeado, e o que fica de fora.</td></tr>
</table>
''', False),
 ("RECUSAMOS", '''
<p class="label">Recusamos</p>
<table>
<tr><td class="k">I</td><td><b>Prometer acurácia que não medimos.</b> Um número que não temos destruiria a única coisa que não se recompra: credibilidade técnica.</td></tr>
<tr><td class="k">II</td><td><b>Prever o imprevisível.</b> Não vendemos oráculo.</td></tr>
</table>
''', True),
 ("RECUSAMOS", '''
<p class="label">Recusamos</p>
<table>
<tr><td class="k">III</td><td><b>Piloto sem métrica.</b> É a receita documentada do fracasso. Aceitar seria vender uma derrota com nota fiscal.</td></tr>
<tr><td class="k">IV</td><td><b>IA decidindo sozinha.</b> A IA rascunha, um humano assina, a diretoria decide.</td></tr>
</table>
''', True),
 ("POR QUE PUBLICAR", '''
<p class="label mute">Por que isto é público</p>
<h1 class="xs">Uma recusa escrita é a única promessa que <i>custa alguma coisa</i> para quem a faz.</h1>
<p class="lede">Todo mundo consegue prometer. Poucos conseguem publicar o que se recusam a vender, porque copiar esta lista exigiria parar de vender o que se vende hoje.</p>
''', False),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">O próximo passo</p>
<h1 class="sm">Qual métrica a sua empresa mediria <i>antes</i> de começar?</h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 04 · O ASSESSMENT GRATUITO ═══════════
peca("peca-04", "04 · O assessment gratuito", "Assess", 4, [
 ("PEÇA 04", '''
<p class="label">O primeiro passo · gratuito</p>
<h1 class="c3">Um assessment de IA da sua empresa, feito só com <i>informação pública.</i></h1>
<div class="rule"></div>
<p class="lede">Dezenas de páginas, geradas em minutos, sem custo e sem você precisar abrir um dado sequer.</p>
''', 'gold'),
 ("O QUE SAI DELE", '''
<p class="label">O que vem dentro</p>
<table>
<tr><td class="k">01</td><td><b>Uma nota de maturidade em IA</b>, de 0 a 5, em seis dimensões da sua operação.</td></tr>
<tr><td class="k">02</td><td><b>As oportunidades priorizadas</b>, com impacto contra esforço, e uma delas marcada como o ponto de partida.</td></tr>
<tr><td class="k">03</td><td><b>Um roadmap em três horizontes</b>, do que dá ganho em seis meses ao que muda o modelo de negócio.</td></tr>
<tr><td class="k">04</td><td><b>O ledger de todas as fontes</b> que usamos, com a citação literal de cada uma.</td></tr>
</table>
''', False),
 ("A NOTA", '''
<p class="label mute">A parte que costuma incomodar</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Uma nota de maturidade, <i>de fora,</i> sem ninguém pedir licença.</h1>
  <div class="margnote">Estratégia, processos, dados, tecnologia, pessoas e governança. Se a nota estiver baixa, ela vai baixa.</div>
</div>
''', True),
 ("A PRIORIZAÇÃO", '''
<p class="label">Onde começar, e por quê</p>
<h1 class="xs">Não é uma lista de ideias. É uma fila, <i>com um primeiro.</i></h1>
<p class="lede">Cada oportunidade entra numa matriz de impacto contra esforço, recebe um score e um horizonte. Uma delas sai marcada como <b>piloto-farol</b>: por onde a gente recomenda começar, com o motivo escrito.</p>
''', False),
 ("A AUTOCLASSIFICAÇÃO", '''
<p class="label">O detalhe que ninguém mais faz</p>
<table>
<tr><td class="k">·</td><td><b>Cada achado se declara.</b> Se é fato apurado ou hipótese nossa. Se veio da sua empresa ou do seu setor. E com que confiança: alta, média ou baixa.</td></tr>
<tr><td class="k">·</td><td><b>O que não descobrimos fica escrito como desconhecido</b>, nunca preenchido por dedução.</td></tr>
</table>
''' + note("·", "Um documento que se autoclassifica é um documento que você pode conferir. Essa é a ideia."), False),
 ("O LEDGER", '''
<p class="label">A prova de que dá para conferir</p>
<h1 class="xs">Toda fonte que usamos vai no fim, com a <i>citação literal.</i></h1>
<p class="lede">Id, provedor, nível de confiança, o trecho exato que foi lido e o endereço. Se você discordar de uma conclusão, dá para ir na fonte dela em dez segundos.</p>
''', False),
 ("OS DESCONHECIDOS", '''
<p class="label mute">A última seção do documento</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">O que ainda não sabemos não é falha. <i>É a agenda da conversa.</i></h1>
  <div class="margnote">O assessment lista o que a informação pública não alcançou. É por aí que a primeira reunião começa.</div>
</div>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">O próximo passo</p>
<h1 class="sm">Quer ver o que a informação pública já diz <i>sobre a sua empresa?</i></h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 05 · PARCEIROS OFICIAIS ═══════════
peca("peca-05", "05 · Parceiros oficiais", "Parceiro", 5, [
 ("PEÇA 05", '''
<p class="label">Parceiros oficiais</p>
<h1 class="c2">A sua equipe constrói com as <i>mesmas ferramentas</i> que nós.</h1>
<div class="rule"></div>
<p class="lede">Durante a capacitação, o time de vocês usa ferramentas dos nossos parceiros para construir as próprias soluções.</p>
''', False),
 ("MICROSOFT", '''
<p class="label mute">Parceiro oficial</p>
<div style="margin-top:145px;margin-bottom:auto">
  <div class="plate"><img class="plogo ms" src="logo-microsoft.png" alt="Microsoft"></div>
  <div class="rule" style="margin-top:38px"></div>
  <p class="lede" style="margin-top:38px">A camada corporativa: identidade, nuvem e as ferramentas de produtividade onde o trabalho da sua empresa já acontece.</p>
</div>
''', True),
 ("CREWAI", '''
<p class="label mute">Parceiro oficial</p>
<div style="margin-top:145px;margin-bottom:auto">
  <div class="plate"><img class="plogo crew" src="logo-crewai.png" alt="CrewAI"></div>
  <div class="rule" style="margin-top:38px"></div>
  <p class="lede" style="margin-top:38px">A camada de agentes: onde os fluxos com aprovação humana são construídos e colocados em produção.</p>
</div>
''', True),
 ("O QUE MUDA", '''
<p class="label">O que isso muda na prática</p>
<table>
<tr><td class="k">01</td><td><b>Ninguém sai refém.</b> As soluções são construídas em tecnologia de mercado, com a documentação pública que qualquer time consegue ler depois.</td></tr>
<tr><td class="k">02</td><td><b>A capacidade fica com vocês.</b> As primeiras soluções quem constrói somos nós, com o dono do processo do lado. O seu time é formado em paralelo, e no topo da trilha passa a construir os próprios fluxos.</td></tr>
</table>
''' + note("·", "Aprovação humana nos pontos críticos continua valendo em qualquer ferramenta: a IA executa, gente da sua confiança valida."), False),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">O próximo passo</p>
<h1 class="sm">Quem, no seu time, sairia dessa história com <i>mais capacidade?</i></h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])



# ═══════════ PEÇA 06 · O QUE É AI NATIVE (fecha o Ato I) ═══════════
# Herda de: peça 01. Gancho para trás: "Tornamos a sua empresa AI native",
# a capa da peça 01, que nunca foi explicada. Gancho para frente: reconstruir
# processo é fácil de afirmar, como você saberia que melhorou (peça 07).
peca("peca-06", "06 · O que é AI native", "Native", 6, [
 ("PEÇA 06", '''
<p class="label">A definição, sem slogan</p>
<h1 class="c2">Se você fundasse a sua empresa hoje, <i>ela não seria assim.</i></h1>
<div class="rule"></div>
<p class="lede">Com IA disponível desde o primeiro dia, você desenharia cada processo de outro jeito. Provavelmente nem existiriam alguns deles.</p>
''', True),
 ("A NOSSA PRIMEIRA FRASE", '''
<p class="label mute">O que está na capa de tudo que a gente manda</p>
<h1 class="sm">Tornamos a sua empresa <i>AI native.</i></h1>
<p class="lede">É a nossa primeira frase, e ela merece uma definição em vez de virar slogan. Esta peça é a definição.</p>
''', False),
 ("O PROBLEMA", '''
<p class="label">Por que o experimento mental não basta</p>
<h1 class="sm">Ninguém vai refundar <i>a própria empresa.</i></h1>
<p class="lede">A sua já funciona. Tem clientes, contratos, gente boa e processos que deram certo ao longo de anos. Jogar isso fora para começar do zero não é opção, e nem deveria ser.</p>
''', False),
 ("A DEFINIÇÃO", '''
<p class="label mute">AI native</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">É chegar no mesmo lugar <i>sem refundar nada.</i></h1>
  <div class="margnote">A empresa que você teria desenhado hoje, construída a partir da que você já tem.</div>
</div>
''', True),
 ("COMO SE FAZ", '''
<p class="label">Na prática, gargalo por gargalo</p>
<div class="steps">
  <div class="step"><span class="n">1</span><div><h3>Mapear o que já dá certo</h3><p>Não se automatiza o caos. Primeiro se entende como o trabalho realmente flui.</p></div></div>
  <div class="step"><span class="n">2</span><div><h3>Achar o gargalo que tem número</h3><p>Onde o trabalho para, onde o dinheiro vaza, onde a decisão demora.</p></div></div>
  <div class="step"><span class="n">3</span><div><h3>Reconstruir o processo com IA</h3><p>Onde ela faz diferença, e só aí. Solução sob medida, no fluxo real.</p></div></div>
  <div class="step"><span class="n">4</span><div><h3>Medir o que mudou</h3><p>Métrica combinada antes, resultado medido depois.</p></div></div>
</div>
''', False),
 ("O QUE FICA", '''
<p class="label mute">Quando a gente sai</p>
<h1 class="xs">As ferramentas ficam. E as pessoas <i>sabem operá-las.</i></h1>
<p class="lede">Junto com cada solução instalamos a capacidade de usar, mudar e cobrar resultado dela. Sistema sem gente formada vira software abandonado em seis meses, e aí a empresa não ficou AI native: ficou com mais uma assinatura.</p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Fica a pergunta</p>
<h1 class="sm">Reconstruir processo é fácil de afirmar. <i>Como você saberia que melhorou?</i></h1>
''' + note("→", "É a próxima conversa. contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 07 · O NÚMERO DESCONFORTÁVEL (abre o Ato II) ═══════════
# Herda de: peça 03. Gancho para trás: "recusamos prometer acurácia que não
# medimos". Gancho para frente: se nem quem usa sabe, como a diretoria saberia.
peca("peca-07", "07 · O número desconfortável", "Prova", 7, [
 ("PEÇA 07", '''
<p class="label">O estudo mais desconfortável do ano</p>
<div class="hero">19<span class="u">%</span></div>
<h1 class="sub">mais lentos. E convencidos de que estavam <i>20% mais rápidos.</i></h1>
<p class="lede">Desenvolvedores experientes usando IA, medidos por fora e depois perguntados por dentro.</p>
''', False),
 ("A LIGAÇÃO", '''
<p class="label mute">De onde vem esta peça</p>
<h1 class="sm">Recusamos prometer acurácia <i>que não medimos.</i></h1>
<p class="lede">Essa é uma das nossas quatro recusas. Existe um estudo que explica por que ela não é modéstia, e sim a única postura defensável.</p>
''', False),
 ("O EXPERIMENTO", '''
<p class="label">Não foi enquete</p>
<table>
<tr><td class="k">01</td><td><b>16 desenvolvedores experientes, 246 tarefas reais</b>, no código que eles mesmos dominavam. Metade com IA, metade sem.</td></tr>
<tr><td class="k">02</td><td><b>O tempo foi cronometrado</b>, não perguntado. Com IA, levaram 19% mais tempo.</td></tr>
</table>
''' + note("·", "METR, julho de 2025. Experimento controlado."), False),
 ("A PERCEPÇÃO", '''
<p class="label">Depois da medição, a pergunta</p>
''' + fig_distancia() + note("·", "Mesmo experimento, mesmas pessoas. A barra de cima é o que eles sentiram; a de baixo é o que o cronômetro registrou."), False),
 ("O LIMITE DESTE ESTUDO", '''
<p class="label mute">O que este número não prova</p>
<h1 class="xs">Isso não é argumento contra IA, e a gente faz questão <i>de dizer.</i></h1>
<p class="lede">A amostra é pequena e o cenário é específico. O maior experimento já publicado sobre o mesmo tema, com <b>4.867 desenvolvedores</b>, encontrou <b>26% mais tarefas concluídas</b>, e os menos experientes foram os que mais ganharam.</p>
''' + note("·", "Cui et al., Management Science."), True),
 ("A CONCLUSÃO", '''
<p class="label">O que os dois estudos dizem juntos</p>
<h1 class="sm">Ninguém sabe se a ferramenta ajudou <i>sem medir de fora.</i></h1>
<p class="lede">Um achou perda, o outro achou ganho. Nos dois casos, <b>quem estava usando não sabia qual dos dois era o seu caso.</b></p>
''', False),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Fica a pergunta</p>
<h1 class="sm">Se nem quem está usando sabe, <i>como a diretoria saberia?</i></h1>
''' + note("→", "Fontes: METR (jul/2025) · Cui et al., Management Science.<br>contato@abbaservices.com.br"), False),
])


# ═══════════ PEÇA 08 · A CAUSA Nº 1 DO FRACASSO (RAND) ═══════════
# Herda de 07. Trás: "ninguém sabe se a ferramenta ajudou sem medir de fora".
# Frente: e se o erro começa antes, na largada?
peca("peca-08", "08 · A causa nº 1 do fracasso", "Rand", 8, [
 ("PEÇA 08", '''
<p class="label">A pesquisa mais séria sobre o assunto</p>
<p class="heropre">Mais de</p>
<div class="hero">80<span class="u">%</span></div>
<h1 class="sub">dos projetos de IA <i>falham.</i></h1>
<p class="lede">O dobro da taxa dos projetos de TI comuns. E a causa número um não é técnica.</p>
''', 'gold'),
 ("A LIGAÇÃO", '''
<p class="label mute">De onde vem esta peça</p>
<h1 class="sm">Ninguém sabe se a ferramenta ajudou <i>sem medir de fora.</i></h1>
<p class="lede">Esse era o problema de não medir. Existe um problema anterior, e ele acontece antes de qualquer ferramenta entrar na empresa.</p>
''', False),
 ("A PESQUISA", '''
<p class="label">Quem mediu, e como</p>
<table>
<tr><td class="k">01</td><td>A RAND entrevistou <b>65 engenheiros de machine learning sêniores</b> sobre projetos que deram errado.</td></tr>
<tr><td class="k">02</td><td>O resultado: <b>mais de 80% dos projetos de IA falham</b>, o dobro da taxa de projetos de TI comuns.</td></tr>
</table>
''' + note("·", "RAND, The Root Causes of Failure for AI Projects, 2024."), False),
 ("A CAUSA", '''
<p class="label mute">A causa número um</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Começar sem combinar <i>o que seria dar certo.</i></h1>
  <div class="margnote">Não é modelo ruim. Não é dado ruim. É desconexão entre o que o projeto buscava e o que a organização precisava.</div>
</div>
''', True),
 ("O QUE ISSO SIGNIFICA", '''
<p class="label">A leitura</p>
<h1 class="xs">O fracasso é de enquadramento, <i>não de tecnologia.</i></h1>
<p class="lede">Um projeto que começa sem métrica de sucesso acordada <b>não pode dar certo</b>, porque não existe definição do que seria certo. Ele só pode terminar, e alguém decide depois se gostou.</p>
''', False),
 ("O QUE A GENTE FAZ", '''
<p class="label mute">A consequência, aqui dentro</p>
<h1 class="sm">Nenhuma decisão entra sem a métrica <i>combinada antes.</i></h1>
<p class="lede">Registrar a decisão com o número que ela precisa mover, antes de começar, não é burocracia em cima do serviço. <b>É a intervenção que mais move o resultado.</b></p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Fica a pergunta</p>
<h1 class="sm">E se a base da empresa <i>já estiver bagunçada?</i></h1>
''' + note("→", "Fonte: RAND (2024). contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 09 · A IA AMPLIFICA O QUE JÁ EXISTE (DORA) ═══════════
peca("peca-09", "09 · A IA amplifica o que já existe", "Dora", 9, [
 ("PEÇA 09", '''
<p class="label">O relatório que ninguém quer ouvir</p>
<h1 class="c2">A IA não conserta um time. Ela <i>amplifica</i> o que já está lá.</h1>
<div class="rule"></div>
<p class="lede">E amplificar não é sempre uma boa notícia.</p>
''', False),
 ("A LIGAÇÃO", '''
<p class="label mute">De onde vem esta peça</p>
<h1 class="sm">Começar sem combinar <i>o que seria dar certo.</i></h1>
<p class="lede">Essa é a causa número um. Tem um segundo jeito de errar, e ele aparece mesmo em quem combinou tudo direito.</p>
''', False),
 ("O QUE FOI MEDIDO", '''
<p class="label">DORA 2025, cerca de 5.000 respondentes</p>
<table>
<tr><td class="k">01</td><td>Adoção de IA correlaciona <b>positivamente com velocidade</b>. Os times entregam mais rápido.</td></tr>
<tr><td class="k">02</td><td>E correlaciona <b>negativamente com estabilidade</b>. Mais falhas, mais retrabalho.</td></tr>
</table>
''' + note("·", "DORA 2025, Google."), False),
 ("A LEITURA", '''
<p class="label mute">O que isso quer dizer na prática</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Time com a base arrumada acelera. Time com processo bagunçado <i>piora mais rápido.</i></h1>
  <div class="margnote">A ferramenta é a mesma. O que muda é o que ela encontra quando chega.</div>
</div>
''', True),
 ("A CONSEQUÊNCIA", '''
<p class="label">O que a gente faz com isso</p>
<h1 class="xs">Às vezes a primeira entrega é <i>um passo atrás.</i></h1>
<p class="lede">Cliente com dado duplicado e processo sem dono não recebe da gente um agente em cima do caos. Recebe <b>o diagnóstico disso, com número</b>, e a fundação como primeira entrega.</p>
''', False),
 ("A FRASE", '''
<p class="label mute">Dito de outro jeito</p>
<h1 class="sm">Arrumar a base não é atraso. <i>É a condição do ganho.</i></h1>
<p class="lede">Automatizar um cadastro errado não corrige o cadastro. <b>Só faz o erro chegar mais cedo.</b></p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Fica a pergunta</p>
<h1 class="sm">E quem já arrumou a base <i>e já mede?</i></h1>
''' + note("→", "Fonte: DORA 2025, Google. contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 10 · QUASE TODO MUNDO DIZ QUE MEDE (fecha o Ato II) ═══════════
peca("peca-10", "10 · Quase todo mundo diz que mede", "Medir", 10, [
 ("PEÇA 10", '''
<p class="label">A última armadilha</p>
<div class="hero">72<span class="u">%</span></div>
<h1 class="sub">dos líderes dizem acompanhar <i>o retorno de IA.</i></h1>
<p class="lede">Metade deles mede qualidade de dados.</p>
''', True),
 ("A LIGAÇÃO", '''
<p class="label mute">De onde vem esta peça</p>
<h1 class="sm">Arrumar a base não é atraso. <i>É a condição do ganho.</i></h1>
<p class="lede">Suponha que a base esteja arrumada e a métrica combinada. Ainda sobra uma pergunta: medir o quê?</p>
''', False),
 ("A PESQUISA", '''
<p class="label">Wharton, terceiro ano do levantamento</p>
<table>
<tr><td class="k">01</td><td><b>72%</b> dos líderes dizem que acompanham o retorno de IA generativa.</td></tr>
<tr><td class="k">02</td><td><b>Metade</b> usa "qualidade de dados" como a métrica de retorno.</td></tr>
<tr><td class="k">03</td><td>E <b>53%</b> reportam retorno de apenas 1 a 5%.</td></tr>
</table>
''' + note("·", "Wharton GBK, outubro de 2025."), False),
 ("O PROBLEMA", '''
<p class="label mute">Por que isso importa</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Qualidade de dados não é retorno. <i>É pré-requisito.</i></h1>
  <div class="margnote">Medir o pré-requisito e chamar de resultado é como pesar os ingredientes e dizer que o bolo ficou bom.</div>
</div>
''', True),
 ("O QUE É MEDIR", '''
<p class="label">Medição de verdade tem quatro partes</p>
<div class="steps">
  <div class="step"><span class="n">1</span><div><h3>Combinada antes</h3><p>Não escolhida depois, entre as que ficaram boas.</p></div></div>
  <div class="step"><span class="n">2</span><div><h3>Apurada do mesmo jeito nas duas pontas</h3><p>Mesma fonte, mesma regra, mesma periodicidade.</p></div></div>
  <div class="step"><span class="n">3</span><div><h3>Ligada ao resultado da empresa</h3><p>E não a um indicador de uso da ferramenta.</p></div></div>
  <div class="step"><span class="n">4</span><div><h3>Assinada por alguém que responde por ela</h3><p>Com nome, do lado do cliente.</p></div></div>
</div>
''', False),
 ("O FECHO DO ARCO", '''
<p class="label mute">Onde isso nos deixa</p>
<h1 class="xs">Todo mundo diz que mede. Quase ninguém mede <i>de fora.</i></h1>
<p class="lede">É por isso que a gente existe, e é por isso que a nossa primeira frase é a que é: <b>instalamos capacidade de IA, e provamos, de fora, o que ela mudou.</b></p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">O próximo passo</p>
<h1 class="sm">Qual número a sua empresa acompanha hoje, <i>e ele é resultado ou pré-requisito?</i></h1>
''' + note("→", "Fonte: Wharton GBK (out/2025). contato@abbaservices.com.br"), False),
])


# ═══════════ PEÇA 11 · A RÉGUA (abre o Ato III) ═══════════
peca("peca-11", "11 · A régua que nos reprova", "Regua", 11, [
 ("PEÇA 11", '''
<p class="label">O Ato III começa aqui</p>
<h1 class="c2">A ferramenta cujo trabalho é <i>reprovar a gente.</i></h1>
<div class="rule"></div>
<p class="lede">Antes de qualquer material nosso sair, ele passa por ela. Inclusive este post.</p>
''', False),
 ("A LIGAÇÃO", '''
<p class="label mute">De onde vem esta peça</p>
<h1 class="sm">Todo mundo diz que mede. Quase ninguém mede <i>de fora.</i></h1>
<p class="lede">Falar isso é fácil. Nas próximas peças a gente mostra a máquina por dentro, começando pela trava que a gente aponta para nós mesmos.</p>
''', False),
 ("O QUE ELA BLOQUEIA", '''
<p class="label">Quatro coisas nunca passam</p>
<table>
<tr><td class="k">01</td><td>Número que <b>não está na nossa base de evidências</b>.</td></tr>
<tr><td class="k">02</td><td>Preço diferente da tabela vigente.</td></tr>
<tr><td class="k">03</td><td>Promessa que a nossa infraestrutura ainda não sustenta.</td></tr>
<tr><td class="k">04</td><td>Qualquer frase que sugira <b>IA decidindo sozinha</b>, sem assinatura humana.</td></tr>
</table>
''', False),
 ("O BLOQUEIO", '''
<p class="label mute">O que acontece quando ela reprova</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Bloqueio significa que o material <i>não sai.</i></h1>
  <div class="margnote">Existe uma opção de forçar. Usar ela é uma decisão com nome, e o nome vai para o registro.</div>
</div>
''', True),
 ("O QUE ELA NÃO FAZ", '''
<p class="label">O limite dela</p>
<h1 class="xs">Ela não diz se o texto <i>é bom.</i></h1>
<p class="lede">É determinística de propósito: mesma entrada, mesma saída, custo zero por execução. <b>Não é um modelo opinando sobre o texto</b>, é uma trava conferindo fatos. Julgar qualidade continua sendo trabalho de gente.</p>
''', False),
 ("POR QUE EXISTE", '''
<p class="label mute">O motivo</p>
<h1 class="sm">A coisa mais cara de perder numa consultoria não é um contrato. É <i>credibilidade técnica.</i></h1>
<p class="lede">Contrato se recupera. Credibilidade não se recompra. E ela não sobrevive a <b>"a gente confere na hora de mandar"</b>.</p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Fica a pergunta</p>
<h1 class="sm">O que impede, hoje, um número inventado de sair da sua empresa <i>dentro de uma proposta assinada?</i></h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 12 · A DELEÇÃO COM CERTIFICADO ═══════════
peca("peca-12", "12 · Apagar com comprovante", "Forget", 12, [
 ("PEÇA 12", '''
<p class="label">Ato III · a máquina por dentro</p>
<h1 class="c2">Quando um cliente manda apagar, a gente apaga. <i>E comprova.</i></h1>
<div class="rule"></div>
<p class="lede">O comando emite um certificado de deleção. Não é promessa por e-mail.</p>
''', 'gold'),
 ("A LIGAÇÃO", '''
<p class="label mute">De onde vem esta peça</p>
<h1 class="sm">O que impede um número inventado <i>de sair da sua empresa?</i></h1>
<p class="lede">Aquilo era uma trava na saída. Esta é uma trava na deleção, e ela existe pelo mesmo motivo: promessa sem mecanismo é só promessa.</p>
''', False),
 ("O QUE O COMANDO FAZ", '''
<p class="label">Três coisas, numa transação só</p>
<table>
<tr><td class="k">01</td><td><b>Purga os arquivos em disco</b>, incluindo os relatórios já gerados.</td></tr>
<tr><td class="k">02</td><td><b>Apaga os registros em cascata</b>, camada por camada.</td></tr>
<tr><td class="k">03</td><td><b>Grava uma lápide</b>: o registro de que a deleção aconteceu, que sobrevive ao que foi apagado.</td></tr>
</table>
''', False),
 ("O CERTIFICADO", '''
<p class="label mute">O que fica na mão do cliente</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Quantos registros, quantos arquivos, quem pediu, <i>e quando.</i></h1>
  <div class="margnote">É o documento que o DPO leva para uma fiscalização. Sem ele, "a gente apagou" é palavra contra palavra.</div>
</div>
''', True),
 ("A REGRA", '''
<p class="label">O inegociável</p>
<h1 class="xs">Nada se deleta <i>fora desse caminho.</i></h1>
<p class="lede">Não existe apagar na mão, não existe apagar no banco, não existe apagar sem deixar o comprovante. <b>Verdade que some sem registro não era verdade.</b></p>
''', False),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Fica a pergunta</p>
<h1 class="sm">Se o seu jurídico pedisse hoje a prova de que um dado foi apagado, <i>ela existiria?</i></h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 13 · O ANTI-CHEAT ═══════════
peca("peca-13", "13 · Bloqueamos a nossa própria trapaça", "Cheat", 13, [
 ("PEÇA 13", '''
<p class="label">Ato III · a máquina por dentro</p>
<h1 class="c3">A gente bloqueou, em código, a chance de <i>melhorar a própria nota.</i></h1>
<div class="rule"></div>
<p class="lede">Duas travas, e as duas existem contra nós mesmos.</p>
''', False),
 ("COMO FUNCIONA", '''
<p class="label">O desenho</p>
<h1 class="xs">Quem recomenda declara quanto acredita, <i>antes.</i></h1>
<p class="lede">Toda recomendação nossa carrega uma probabilidade declarada, com nome de quem declarou. Depois, o resultado é medido. E existe um placar comparando as duas coisas.</p>
''', False),
 ("A PRIMEIRA TRAVA", '''
<p class="label">Trava 1</p>
<table>
<tr><td class="k">01</td><td><b>Declarar a probabilidade depois de medir o resultado é bloqueado.</b> O sistema recusa, com erro nomeado.</td></tr>
<tr><td class="k">02</td><td>Sem isso, bastaria esperar o número aparecer para "prever" com precisão perfeita.</td></tr>
</table>
''', False),
 ("A SEGUNDA TRAVA", '''
<p class="label mute">Trava 2, a mais importante</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Probabilidade declarada <i>é imutável.</i></h1>
  <div class="margnote">Declarar 60%, ver os números melhorarem e trocar para 95% limparia o placar sem deixar vestígio. O código não deixa.</div>
</div>
''', True),
 ("O QUE ISSO CUSTA", '''
<p class="label">Sendo honesto sobre o preço</p>
<h1 class="xs">Isso deixa <i>os nossos erros</i> registrados para sempre.</h1>
<p class="lede">Uma recomendação em que a gente apostou alto e deu errado fica lá, com nome e data. <b>É desconfortável de propósito:</b> um placar que se pode editar não é um placar.</p>
''', False),
 ("A REGRA GERAL", '''
<p class="label mute">O princípio por trás das duas</p>
<h1 class="sm">Quem vende medição <i>se mede primeiro.</i></h1>
<p class="lede">Não dá para cobrar de um cliente uma métrica combinada antes e, do nosso lado, ajustar o próprio placar depois do jogo.</p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Fica a pergunta</p>
<h1 class="sm">Quem mede <i>o seu fornecedor de IA?</i></h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])


# ═══════════ PEÇA 14 · O CONSELHEIRO DE IA (fecha o Ato III) ═══════════
# Herda de 13. Trás: "Quem mede o seu fornecedor de IA?" Frente: e quem já tem
# IA rodando? Sem curva de tenure, sem placar, sem preço, sem as 5 camadas.
peca("peca-14", "14 · O Conselheiro de IA", "Consel", 14, [
 ("PEÇA 14", '''
<p class="label">A cadeira que quase ninguém tem</p>
<h1 class="c3">Todo fornecedor de IA tem um vendedor. A sua mesa merece <i>alguém do seu lado.</i></h1>
<div class="rule"></div>
<p class="lede">Quando a fatura chega, quando a proposta chega, quando o contrato vence.</p>
''', True),
 ("A LIGAÇÃO", '''
<p class="label mute">De onde vem esta peça</p>
<h1 class="sm">Quem mede <i>o seu fornecedor de IA?</i></h1>
<p class="lede">A gente fechou a peça anterior com essa pergunta. Ela tem um nome, e é a cadeira que está faltando na maioria das diretorias do médio porte.</p>
''', False),
 ("O MERCADO", '''
<p class="label">O cargo que mais cresce</p>
<table>
<tr><td class="k">01</td><td>O executivo de IA passou de <b>26% das organizações em 2025 para 76% em 2026</b>. Virou padrão.</td></tr>
<tr><td class="k">02</td><td>E no médio porte ele nasce <b>fracionário</b>: a Gartner projeta mais de 30% das médias empresas com executivo de IA nesse formato até 2027.</td></tr>
</table>
''' + note("·", "Gartner e levantamentos setoriais."), False),
 ("O PROBLEMA DE CONTRATAR", '''
<p class="label mute">Por que fracionário, e não contratado</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">As pesquisas apontam que 98% das empresas brasileiras <i>não acham</i> profissional de IA qualificado.</h1>
  <div class="margnote">E quem acha costuma ver a pessoa sair em cerca de 18 meses, levando o contexto inteiro na cabeça.</div>
</div>
''', True),
 ("O QUE A CADEIRA ENTREGA", '''
<p class="label">Quatro entregas nomeadas</p>
<table>
<tr><td class="k">01</td><td><b>Presença no conselho.</b> Resultados contra os objetivos declarados, no máximo três recomendações priorizadas, e as decisões registradas.</td></tr>
<tr><td class="k">02</td><td><b>Arbitragem de fornecedores.</b> Análise independente de qualquer proposta de IA que chegar, por escrito: isso é real, é para vocês, e o preço é justo?</td></tr>
<tr><td class="k">03</td><td><b>Roadmap vivo.</b> O plano deixa de ser documento e vira instrumento revisado a cada ciclo.</td></tr>
<tr><td class="k">04</td><td><b>Governança e LGPD de IA.</b> Vigilância contínua: uso novo, risco novo, adequação.</td></tr>
</table>
''', False),
 ("O QUE ELA NÃO É", '''
<p class="label mute">Quatro recusas, para não haver mal-entendido</p>
<h1 class="xs">Não é banco de horas. Não é suporte. Não é parecer jurídico. E não é <i>terceirizar a decisão.</i></h1>
<p class="lede">É senioridade recorrente com pauta própria. A gente recomenda com convicção e assina a recomendação. <b>Quem decide é quem responde pela empresa.</b></p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">Se você já tem IA rodando</p>
<h1 class="sm">A pergunta não é se você precisa de consultoria. É quem senta <i>do seu lado</i> quando o fornecedor apresenta a fatura.</h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ escrita ═══════════
order = [a for _,_,arqs in PAGES for a in arqs]
ren, first = {}, order[0]
for nm in order:
    fn = "Main.dc.html" if nm == first else nm + ".dc.html"
    ren[nm] = fn
    open(fn, "w", encoding="utf-8").write(F[nm])

boards = []
for pid,_,arqs in PAGES:
    for i,a in enumerate(arqs):
        boards.append({"file":ren[a], "x":(i%5)*1260, "y":(i//5)*1620, "w":W, "h":HT, "page":pid})

canvas = {
 "pages":[{"id":p,"name":n} for p,n,_ in PAGES],
 "artboards":boards,
 "annotations":[
  {"id":"nota-transicao","x":0,"y":-300,"w":660,"page":"peca-01",
   "text":"TRANSIÇÃO, três técnicas:\n1. Barra de progresso dourada no topo, que avança a cada tela. O leitor sente onde está.\n2. Marca de continuidade: um traço sai pela borda direita e reaparece na mesma altura na borda esquerda da tela seguinte. No swipe, ele parece atravessar.\n3. Ritmo de fundo: navy e papel alternam num compasso desenhado, e o papel sempre marca a tela de pausa ou de ressalva."},
  {"id":"nota-texto","x":740,"y":-300,"w":560,"page":"peca-01",
   "text":"SEM TRAVESSÃO em nenhuma peça (decisão do sócio V3v, reafirmada em 27/08). Vírgula, dois-pontos ou ponto.\nSem emoji. Sem hashtag genérica.\nA metáfora das raízes saiu, por decisão registrada na mesma V3v.\nTodo texto dentro do recorte 1:1 da grade."}],
 "launch":{"view":"canvas","page":"peca-01"}
}
open("canvas.json","w",encoding="utf-8").write(json.dumps(canvas,ensure_ascii=False,indent=2))

# guarda: nenhum travessao pode sobrar no texto das pecas
bad = [nm for nm,src in F.items() if "—" in src or "–" in src]
print("telas:", len(order), "| peças:", len(PAGES), "| travessões restantes:", bad or "nenhum")
