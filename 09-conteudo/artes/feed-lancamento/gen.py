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

    .mark { display:block; width:190px; height:auto; opacity:.96; }
    .wordmark { font-family:"Newsreader", Georgia, serif; font-weight:400;
                font-size:52px; letter-spacing:.24em; color:#FFFFFF; }
    .paper .wordmark { color:#1B2A4A; }
  </style>
'''
HEAD = ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
        '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>'
        + STYLE + '</helmet>\n')
TAIL = '</x-dc>\n</body>\n</html>\n'

def page(i, n, ref, folio_r, body, paper=False):
    """i = indice 0-based da tela; n = total. Constroi a moldura com as duas
    tecnicas de transicao: barra de progresso e marca de continuidade."""
    cls = "p paper" if paper else "p"
    span = W - 2*M
    # 1. barra de progresso: fiada cheia + segmento dourado proporcional
    prog = round(span * (i+1) / n)
    # 2. marca de continuidade: sai pela direita em y_i, entra pela esquerda em y_{i-1}
    def ty(k): return round(300 + k * (760 / max(n-1, 1)))
    out_y, in_y = ty(i), ty(i-1) if i > 0 else None
    f = ['<div class="frame">',
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
            f'<div class="stage">{body}</div>'
            f'<span class="ref">{ref}</span>'
            f'<span class="refr">abbaservices.com.br</span>'
            '</div>\n' + TAIL)

def note(mk, txt):
    return f'<div class="note"><span class="mk">{mk}</span><p>{txt}</p></div>'

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
<h1>Tornamos a sua empresa <i>AI native.</i></h1>
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
<h1 class="sm">Uma conversa de 45 minutos, e a sua <i>análise gratuita</i> feita na hora.</h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 02 · A JORNADA ═══════════
JORNADA = [
 ("1","A primeira conversa","45 min · análise gratuita feita na hora"),
 ("2","Assessment","o mergulho profundo · portfólio ranqueado"),
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
<h1>A jornada,<br>em <i>sete passos.</i></h1>
<div class="rule"></div>
<p class="lede">Da primeira conversa à cadeira de estrategista na sua diretoria. Cada etapa entrega algo inteiro sozinha e produz o insumo da próxima.</p>
''', False),
 ("O DESENHO", espinha(), False),
 ("ETAPAS 1 E 2", '''
<p class="label">Antes de qualquer investimento</p>
<div class="steps">
  <div class="step"><span class="n">1</span><div><h3>A primeira conversa</h3><p>45 minutos, e nós já chegamos com uma análise da sua empresa feita com informação pública, incluindo uma estimativa em reais do que pode estar vazando na operação. Fica pronta em menos de cinco minutos, durante a própria conversa.</p></div></div>
  <div class="step"><span class="n">2</span><div><h3>Assessment: o mergulho profundo</h3><p>Do conselho à linha de frente: como o trabalho realmente flui, onde quebra, onde vaza valor. Você sai com um portfólio de oportunidades ranqueado e quantificado, não com uma lista de ideias.</p></div></div>
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
<h1>O que prometemos,<br>e o que <i>recusamos.</i></h1>
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

# ═══════════ PEÇA 04 · A ANÁLISE GRATUITA ═══════════
peca("peca-04", "04 · A análise gratuita", "Analise", 4, [
 ("PEÇA 04", '''
<p class="label">O primeiro passo · gratuito</p>
<h1>Dezenas de páginas sobre a sua empresa, em menos de <i>cinco minutos.</i></h1>
<div class="rule"></div>
<p class="lede">Feita com informação pública. A primeira página traz uma estimativa em reais do que pode estar vazando na operação.</p>
''', False),
 ("POR QUE UM NÚMERO", '''
<p class="label mute">Por que um número, e não três hipóteses</p>
<h1 class="xs">Três hipóteses fazem o leitor pensar. <i>Um número faz o leitor reagir.</i></h1>
<p class="lede">Concordando, discordando ou corrigindo. Qualquer uma das três é uma conversa. A ausência de reação é um PDF arquivado.</p>
''', True),
 ("A CONVERSA", '''
<p class="label">45 minutos · cinco perguntas</p>
<div class="steps">
  <div class="step"><span class="n">1</span><div><h3>O caminho de uma nota fiscal aí dentro,</h3><p>do pedido ao pagamento: quem toca, em que sistema.</p></div></div>
  <div class="step"><span class="n">2</span><div><h3>O que mais atrasa o fechamento do mês,</h3><p>e quanto tempo ele leva hoje.</p></div></div>
  <div class="step"><span class="n">3</span><div><h3>Que número em reais dói hoje</h3><p>e já é medido.</p></div></div>
  <div class="step"><span class="n">4</span><div><h3>Quando vocês descobrem que perderam dinheiro:</h3><p>no mês, no trimestre, ou no ano seguinte.</p></div></div>
  <div class="step"><span class="n">5</span><div><h3>Se esse número melhorasse 20%, quem comemoraria.</h3><p>Quase nunca é quem marcou a reunião.</p></div></div>
</div>
''', False),
 ("AS REGRAS", '''
<p class="label">As regras de honestidade</p>
<table>
<tr><td class="k">I</td><td><b>Faixa, nunca número exato.</b> Um valor exato calculado de fora é uma mentira com aparência de precisão, e o primeiro CFO competente desmonta.</td></tr>
<tr><td class="k">II</td><td><b>Premissa sem fonte não entra.</b> Se não há referência pública citável, o item sai da análise.</td></tr>
<tr><td class="k">III</td><td><b>A faixa pode ser pequena.</b> Se a estimativa honesta for baixa, ela vai baixa. Análise inflada vende uma reunião e perde a relação.</td></tr>
</table>
''', False),
 ("O QUE ELA NÃO É", '''
<p class="label mute">O limite, dito por nós</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">A análise aponta onde o dinheiro parece estar vazando. Ela <i>não prova a causa,</i> porque foi calculada de fora.</h1>
  <div class="margnote">E nunca prometemos capturar a faixa inteira. A captura é uma fração dela, e isso a gente diz em voz alta.</div>
</div>
''', True),
 ("O QUE VOCÊ RECEBE", '''
<p class="label">O que fica com você</p>
<table>
<tr><td class="k">01</td><td><b>A faixa em reais,</b> em ordem de grandeza anual, e o vetor principal: por onde o dinheiro sai.</td></tr>
<tr><td class="k">02</td><td><b>As premissas numeradas, com a fonte citada,</b> incluindo o que assumimos e ainda não sabemos.</td></tr>
<tr><td class="k">03</td><td><b>As perguntas que só você pode responder,</b> e que mudariam a estimativa nos dois sentidos.</td></tr>
</table>
''' + note("·", "Entre 32 e 60 páginas, conforme o modelo de profundidade. Sem custo, sem compromisso, e sem nenhum dado seu no documento."), False),
 ("SOBRE O TAMANHO", '''
<p class="label mute">Uma ressalva que fazemos questão de dar</p>
<h1 class="xs">Sessenta páginas não são o argumento. <i>A primeira é.</i></h1>
<p class="lede">A análise é longa porque <b>cada premissa vem com a fonte</b>, e você precisa poder conferir de onde saiu o número. Se a primeira página não trouxer uma faixa em reais que faça você reagir, o resto não salva.</p>
''', True),
 ("O PRÓXIMO PASSO", '''
<img class="mark" src="abba-logo.png" alt="ABBA">
<p class="label" style="margin-top:34px">O próximo passo</p>
<h1 class="sm">Tem algum número em reais aí dentro que <i>dói hoje,</i> e que vocês já medem?</h1>
''' + note("→", "contato@abbaservices.com.br"), False),
])

# ═══════════ PEÇA 05 · PARCEIROS OFICIAIS ═══════════
peca("peca-05", "05 · Parceiros oficiais", "Parceiro", 5, [
 ("PEÇA 05", '''
<p class="label">Parceiros oficiais</p>
<h1>A sua equipe constrói com as <i>mesmas ferramentas</i> que nós.</h1>
<div class="rule"></div>
<p class="lede">Durante a capacitação, o time de vocês usa ferramentas dos nossos parceiros para construir as próprias soluções.</p>
''', False),
 ("MICROSOFT", '''
<p class="label mute">Parceiro oficial</p>
<div style="margin-top:auto;margin-bottom:auto">
  <span class="wordmark">MICROSOFT</span>
  <p class="lede" style="margin-top:40px">A camada corporativa: identidade, nuvem e as ferramentas de produtividade onde o trabalho da sua empresa já acontece.</p>
</div>
''', True),
 ("CREWAI", '''
<p class="label mute">Parceiro oficial</p>
<div style="margin-top:auto;margin-bottom:auto">
  <span class="wordmark">CREWAI</span>
  <p class="lede" style="margin-top:40px">A camada de agentes: onde os fluxos com aprovação humana são construídos e colocados em produção.</p>
</div>
''', True),
 ("O QUE MUDA", '''
<p class="label">O que isso muda na prática</p>
<table>
<tr><td class="k">01</td><td><b>Ninguém sai refém.</b> As soluções são construídas em tecnologia de mercado, com a documentação pública que qualquer time consegue ler depois.</td></tr>
<tr><td class="k">02</td><td><b>A capacidade fica com vocês.</b> Quem constrói durante a capacitação é o time de vocês, não a gente.</td></tr>
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
<h1>Se você fundasse a sua empresa hoje, <i>ela não seria assim.</i></h1>
<div class="rule"></div>
<p class="lede">Com IA disponível desde o primeiro dia, você desenharia cada processo de outro jeito. Provavelmente nem existiriam alguns deles.</p>
''', False),
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
''' + note("·", "É a próxima conversa."), False),
])

# ═══════════ PEÇA 07 · O NÚMERO DESCONFORTÁVEL (abre o Ato II) ═══════════
# Herda de: peça 03. Gancho para trás: "recusamos prometer acurácia que não
# medimos". Gancho para frente: se nem quem usa sabe, como a diretoria saberia.
peca("peca-07", "07 · O número desconfortável", "Prova", 7, [
 ("PEÇA 07", '''
<p class="label">O estudo mais desconfortável do ano</p>
<h1>19% mais lentos.<br>E convencidos de que estavam <i>20% mais rápidos.</i></h1>
<div class="rule"></div>
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
<p class="label mute">Depois da medição, a pergunta</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Cada um relatou ter ficado cerca de <i>20% mais rápido.</i></h1>
  <div class="margnote">A distância entre o que aconteceu e o que eles sentiram passou de 40 pontos.</div>
</div>
''', True),
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
''' + note("·", "Fontes: METR (jul/2025) · Cui et al., Management Science."), False),
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
