# -*- coding: utf-8 -*-
import json, os, html as H
os.chdir('/home/user/abba-feed')

W, HT = 1080, 1350

STYLE = '''
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300;1,6..72,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
  <style>
    body { margin:0; }
    a { color:#C2A35B; } a:hover { color:#D9BA72; }

    .p { width:1080px; height:1350px; box-sizing:border-box; position:relative;
         overflow:hidden; background:#1B2A4A; color:#FFFFFF;
         font-family:"Source Serif 4", Georgia, serif; }
    .p.paper { background:#F2F4F7; color:#1B2A4A; }

    /* --- moldura do documento: folio, referencia, fiadas --- */
    .frame { position:absolute; inset:0; pointer-events:none; }
    .hair { position:absolute; background:#33456A; }
    .paper .hair { background:#CBD3DF; }
    .hair.gold { background:#C2A35B; }
    .folio { position:absolute; top:96px; font-family:"IBM Plex Mono", monospace;
             font-size:19px; letter-spacing:.2em; color:#5D6E92; }
    .paper .folio { color:#8C97AA; }
    .folio.l { left:104px; } .folio.r { right:104px; text-align:right; }
    .ref { position:absolute; bottom:92px; left:104px; font-family:"IBM Plex Mono", monospace;
           font-size:19px; letter-spacing:.2em; color:#5D6E92; }
    .paper .ref { color:#8C97AA; }
    .refr { position:absolute; bottom:92px; right:104px; font-family:"IBM Plex Mono", monospace;
            font-size:19px; letter-spacing:.2em; color:#C2A35B; }

    /* --- area util: dentro do recorte 1:1 da grade --- */
    .stage { position:absolute; left:104px; right:104px; top:196px; bottom:168px;
             display:flex; flex-direction:column; }

    .label { font-family:"IBM Plex Mono", monospace; font-size:20px; letter-spacing:.22em;
             text-transform:uppercase; color:#C2A35B; margin:0 0 30px; }
    .label.mute { color:#5D6E92; } .paper .label.mute { color:#8C97AA; }

    h1 { font-family:"Newsreader", Georgia, serif; font-weight:400; margin:0;
         font-size:80px; line-height:1.12; letter-spacing:-.014em; color:#FFFFFF;
         text-wrap:balance; }
    .paper h1 { color:#1B2A4A; }
    h1.sm { font-size:70px; } h1.xs { font-size:58px; line-height:1.16; }
    h1 i { font-style:italic; color:#D8BE7C; font-weight:300; }
    .paper h1 i { color:#8A6E28; }

    .lede { font-family:"Source Serif 4", Georgia, serif; font-size:36px; line-height:1.5;
            color:#C3CAD8; margin:34px 0 0; max-width:840px; }
    .paper .lede { color:#4E5A70; }
    .lede b { color:#FFFFFF; font-weight:600; } .paper .lede b { color:#1B2A4A; }

    .rule { height:1px; background:#C2A35B; width:96px; margin:44px 0 0; flex:none; }

    /* --- numero grande (arquetipo dado) --- */
    .fig { font-family:"Newsreader", Georgia, serif; font-weight:300;
           font-size:236px; line-height:.9; letter-spacing:-.03em;
           font-variant-numeric:tabular-nums; color:#1B2A4A; margin:0; }
    .p:not(.paper) .fig { color:#FFFFFF; }
    .fig sup { font-size:.38em; vertical-align:super; color:#C2A35B; font-weight:400;
               letter-spacing:0; margin-left:.06em; }
    .figcap { font-family:"IBM Plex Mono", monospace; font-size:22px; letter-spacing:.16em;
              text-transform:uppercase; color:#8A6E28; margin:22px 0 0; }
    .p:not(.paper) .figcap { color:#C2A35B; }

    /* --- nota de rodape: a doutrina da fonte, feita visual --- */
    .note { margin-top:auto; display:flex; gap:20px; align-items:flex-start;
            padding-top:26px; border-top:1px solid #33456A; }
    .paper .note { border-top-color:#CBD3DF; }
    .note .mk { font-family:"IBM Plex Mono", monospace; font-size:19px; color:#C2A35B;
                flex:none; line-height:1.6; }
    .note p { font-family:"Source Serif 4", serif; font-size:22px; line-height:1.55;
              color:#7C88A2; margin:0; } .paper .note p { color:#78839A; }

    /* --- tabela / razao --- */
    table { border-collapse:collapse; width:100%; margin-top:8px; }
    td, th { text-align:left; vertical-align:top; padding:24px 22px 24px 0;
             border-bottom:1px solid #33456A; }
    .paper td, .paper th { border-bottom-color:#CBD3DF; }
    th { font-family:"IBM Plex Mono", monospace; font-size:19px; letter-spacing:.2em;
         text-transform:uppercase; color:#C2A35B; font-weight:400; padding-bottom:16px; }
    td { font-family:"Source Serif 4", serif; font-size:30px; line-height:1.42; color:#C3CAD8; }
    .paper td { color:#4E5A70; }
    td.k { font-family:"IBM Plex Mono", monospace; font-size:21px; color:#5D6E92;
           width:74px; letter-spacing:.08em; padding-top:28px; }
    .paper td.k { color:#9AA4B6; }
    td b { color:#FFFFFF; font-weight:600; } .paper td b { color:#1B2A4A; }

    /* --- lista de etapa --- */
    .steps { display:flex; flex-direction:column; gap:0; margin-top:6px; }
    .step { display:grid; grid-template-columns:96px 1fr; gap:30px;
            padding:26px 0; border-bottom:1px solid #33456A; align-items:baseline; }
    .paper .step { border-bottom-color:#CBD3DF; }
    .step:last-child { border-bottom:none; }
    .step .n { font-family:"IBM Plex Mono", monospace; font-size:24px; color:#C2A35B;
               letter-spacing:.1em; font-variant-numeric:tabular-nums; }
    .step h3 { font-family:"Newsreader", Georgia, serif; font-weight:400; font-size:38px;
               line-height:1.2; margin:0 0 8px; color:#FFFFFF; }
    .paper .step h3 { color:#1B2A4A; }
    .step p { font-family:"Source Serif 4", serif; font-size:26px; line-height:1.44;
              color:#8E9AB4; margin:0; } .paper .step p { color:#6B778E; }

    /* --- margem anotada --- */
    .marg { display:grid; grid-template-columns:1fr 268px; gap:52px; align-items:start; }
    .margnote { font-family:"IBM Plex Mono", monospace; font-size:21px; line-height:1.65;
                color:#7C88A2; border-left:1px solid #C2A35B; padding-left:24px; }
    .paper .margnote { color:#78839A; }
  </style>
'''

HEAD = ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
        '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>'
        + STYLE + '</helmet>\n')
TAIL = '</x-dc>\n</body>\n</html>\n'

def page(ref, folio_r, body, paper=False, gold_rule_y=None):
    cls = "p paper" if paper else "p"
    frame = ('<div class="frame">'
             '<div class="hair" style="left:104px;right:104px;top:150px;height:1px"></div>'
             '<div class="hair" style="left:104px;right:104px;bottom:146px;height:1px"></div>'
             '<div class="hair gold" style="left:104px;top:150px;width:52px;height:2px"></div>'
             '</div>')
    return (HEAD + f'<div class="{cls}">{frame}'
            f'<span class="folio l">ABBA</span><span class="folio r">{folio_r}</span>'
            f'<div class="stage">{body}</div>'
            f'<span class="ref">{ref}</span>'
            f'<span class="refr">abbaservices.com.br</span>'
            '</div>\n' + TAIL)

def note(mark, txt):
    return f'<div class="note"><span class="mk">{mark}</span><p>{txt}</p></div>'

F = {}   # nome do arquivo -> html
PAGES = []  # (page_id, nome, [arquivos])

# ============================================================
# PEÇA 01 · A TESE
# ============================================================
p1 = []
p1.append(("Tese01", page("§1 · 01/07", "PEÇA 01", '''
<p class="label">Consultoria de inteligência artificial</p>
<h1>Instalamos capacidade de IA.<br>E provamos, <i>de fora,</i> o que ela mudou.</h1>
<div class="rule"></div>
<p class="lede">Número combinado antes. Medido depois, do mesmo jeito. Assinado por gente que responde por ele.</p>
''')))

p1.append(("Tese02", page("§1 · 02/07", "QUEM SOMOS", '''
<p class="label mute">Quem somos</p>
<h1 class="sm">Entramos na sua empresa para <i>entendê-la a fundo.</i></h1>
<p class="lede">Construímos as soluções certas para o seu fluxo de trabalho, validamos cada uma com <b>dados reais</b> antes de qualquer investimento pesado, formamos as suas pessoas — e ficamos ao seu lado acompanhando, mês a mês, <b>o que mudou.</b></p>
''')))

p1.append(("Tese03", page("§1 · 03/07", "AS DUAS FRENTES", '''
<p class="label">O trabalho acontece em duas frentes ao mesmo tempo</p>
<table>
<tr><td class="k">01</td><td><b>Nos processos.</b><br>Projetamos e implantamos sistemas inteligentes — arquitetura, integrações e agentes de IA trabalhando em conjunto — que tornam a operação mais eficiente, mais rápida e mais poderosa.</td></tr>
<tr><td class="k">02</td><td><b>Nas pessoas.</b><br>Formamos cada nível da equipe para trabalhar com IA e enxergar o próprio trabalho de um jeito novo — do conselho à linha de frente.</td></tr>
</table>
''' + note("—", "De nada adiantam sistemas novos com a empresa pensando do jeito antigo. Por isso as duas frentes andam juntas."))))

p1.append(("Tese04", page("§1 · 04/07", "O PROCESSO", '''
<p class="label mute">O nosso processo</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Começa na diretoria e se estende, <i>como raízes,</i> por toda a empresa — até alcançar cada pessoa, em cada processo, todos os dias.</h1>
  <div class="margnote">Uma empresa não muda por uma ponta só.</div>
</div>
''', paper=True)))

p1.append(("Tese05", page("§1 · 05/07", "AS TRÊS PERGUNTAS", '''
<p class="label">A mentalidade que instalamos em cada pessoa</p>
<div class="steps">
  <div class="step"><span class="n">I</span><div><h3>O que eu posso parar de fazer</h3><p>porque a IA agora faz.</p></div></div>
  <div class="step"><span class="n">II</span><div><h3>O que eu posso começar a fazer</h3><p>porque a IA agora permite.</p></div></div>
  <div class="step"><span class="n">III</span><div><h3>O que só eu faço</h3><p>e devo fazer ainda melhor.</p></div></div>
</div>
''' + note("—", "Não é treinamento de ferramenta. Quando a organização inteira pensa assim, a mudança deixa de depender de consultor."))))

p1.append(("Tese06", page("§1 · 06/07", "COMO TRABALHAMOS", '''
<p class="label mute">Como trabalhamos</p>
<h1 class="sm">A IA rascunha.<br>Um humano <i>assina.</i><br>A diretoria decide.</h1>
<p class="lede">Toda decisão entra num registro: métrica combinada antes, resultado medido depois — e vocês veem o registro inteiro, <b>incluindo o que não funcionou.</b></p>
''', paper=True)))

p1.append(("Tese07", page("§1 · 07/07", "O PRÓXIMO PASSO", '''
<p class="label">O próximo passo</p>
<h1 class="sm">Uma conversa de 45 minutos — e o seu <i>Mapa de Vazamento,</i> gratuito.</h1>
<p class="lede">Uma estimativa em reais do que pode estar vazando na sua operação, feita com informação pública. Sem custo e sem compromisso.</p>
''' + note("→", "contato@abbaservices.com.br"))))

F.update(dict(p1)); PAGES.append(("peca-01","01 · A tese",[n for n,_ in p1]))

# ============================================================
# PEÇA 02 · A JORNADA EM SETE PASSOS
# ============================================================
JORNADA = [
 ("1","A primeira conversa","45 min · Mapa de Vazamento · gratuito"),
 ("2","Assessment","o mergulho profundo · portfólio ranqueado"),
 ("3","Protótipo de caso de uso","dados reais · GO ou NO-GO com números"),
 ("4","Construção e implantação","engenharia sob medida · em produção"),
 ("5","Treinamento + ABBA Portal","todos os níveis · campeões internos"),
 ("6","Sistemas gerenciados","ritual semanal · o registro do que mudou"),
 ("7","Conselheiro de IA","a cadeira de estrategista, do seu lado"),
]

def espinha():
    x, y0, dy = 46, 26, 108
    parts = [f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0+dy*6}" stroke="#33456A" stroke-width="1"/>']
    for i,(n,t,s) in enumerate(JORNADA):
        y = y0 + dy*i
        parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#C2A35B"/>')
        parts.append(f'<text x="{x-22}" y="{y+7}" text-anchor="end" font-family="IBM Plex Mono, monospace" font-size="21" fill="#5D6E92" letter-spacing="1">{n}</text>')
        parts.append(f'<text x="{x+34}" y="{y-2}" font-family="Newsreader, Georgia, serif" font-size="35" fill="#FFFFFF">{t}</text>')
        parts.append(f'<text x="{x+34}" y="{y+30}" font-family="IBM Plex Mono, monospace" font-size="18" fill="#7C88A2" letter-spacing="1.2">{s}</text>')
    yb = y0 + dy*6
    for dx in (-120, -46, 46, 120):
        parts.append(f'<path d="M{x} {yb+14} C {x} {yb+70}, {x+dx} {yb+62}, {x+dx} {yb+128}" fill="none" stroke="#33456A" stroke-width="1"/>')
    parts.append(f'<text x="{x-4}" y="{yb+176}" font-family="IBM Plex Mono, monospace" font-size="19" fill="#5D6E92" letter-spacing="3.4" text-anchor="middle">ATÉ CADA PESSOA, EM CADA PROCESSO</text>')
    return f'<svg viewBox="0 0 872 {yb+210}" width="100%" style="margin-top:auto;margin-bottom:auto" aria-hidden="true">{"".join(parts)}</svg>'

p2 = []
p2.append(("Jornada01", page("§2 · 01/09", "PEÇA 02", '''
<p class="label">O caminho completo</p>
<h1>A jornada,<br>em <i>sete passos.</i></h1>
<div class="rule"></div>
<p class="lede">Da primeira conversa à cadeira de estrategista na sua diretoria. Cada etapa entrega algo inteiro sozinha — e produz o insumo da próxima.</p>
''')))

p2.append(("Jornada02", page("§2 · 02/09", "O DESENHO", espinha())))

p2.append(("Jornada03", page("§2 · 03/09", "ETAPAS 1 E 2", '''
<p class="label">Antes de qualquer investimento</p>
<div class="steps">
  <div class="step"><span class="n">1</span><div><h3>A primeira conversa</h3><p>45 minutos — e nós já chegamos com uma análise da sua empresa feita, com informação pública, incluindo uma estimativa em reais do que pode estar vazando na operação. Gratuito.</p></div></div>
  <div class="step"><span class="n">2</span><div><h3>Assessment — o mergulho profundo</h3><p>Do conselho à linha de frente: como o trabalho realmente flui, onde quebra, onde vaza valor. Você sai com um portfólio de oportunidades ranqueado e quantificado — não uma lista de ideias.</p></div></div>
</div>
''' + note("—", "Ninguém deveria pagar para descobrir se faz sentido."))))

p2.append(("Jornada04", page("§2 · 04/09", "ETAPA 3", '''
<p class="label mute">Etapa 3 · a prova antes do investimento</p>
<h1 class="xs">O caso mais promissor, construído com <i>os seus dados reais.</i></h1>
<p class="lede">A sua diretoria decide GO ou NO-GO com números na mesa.</p>
<p class="lede"><b>NO-GO também é resultado:</b> custou pouco e evitou um investimento errado.</p>
''', paper=True)))

p2.append(("Jornada05", page("§2 · 05/09", "ETAPA 4", '''
<p class="label">Etapa 4 · a engenharia da solução</p>
<table>
<tr><th>O quê</th></tr>
<tr><td>Projetamos a arquitetura — dados, integrações, lógica de decisão — e construímos sistemas sob medida, com <b>agentes de IA inseridos onde fazem diferença</b>, em produção no fluxo real da sua equipe.</td></tr>
<tr><th>Como</th></tr>
<tr><td>Com a tecnologia dos nossos parceiros e <b>pontos de aprovação humana em tudo que é crítico:</b> a IA executa, gente da sua confiança valida.</td></tr>
</table>
''' + note("—", "Relatório na gaveta não muda empresa. Sistema rodando muda."))))

p2.append(("Jornada06", page("§2 · 06/09", "ETAPA 5", '''
<p class="label">Etapa 5 · as pessoas</p>
<h1 class="xs">Formamos todos os níveis — plataforma própria e <i>sessões presenciais.</i></h1>
<p class="lede">O objetivo não é ensinar ferramenta. É instalar, em cada pessoa, três perguntas que mudam o jeito de olhar o próprio trabalho.</p>
''' + note("—", "Campeões internos carregam a transformação depois que saímos da sala — e a capacidade fica com vocês."))))

p2.append(("Jornada07", page("§2 · 07/09", "ETAPAS 6 E 7", '''
<p class="label">Depois que está rodando</p>
<div class="steps">
  <div class="step"><span class="n">6</span><div><h3>Sistemas gerenciados</h3><p>Operamos o que construímos: monitoramento, evolução contínua e um ritual semanal de 20 minutos com quem decide. Toda decisão entra num registro — métrica combinada antes, resultado medido depois.</p></div></div>
  <div class="step"><span class="n">7</span><div><h3>Conselheiro de IA</h3><p>Um estrategista de IA presente na sua diretoria: roadmap vivo, governança e análise independente de qualquer proposta de fornecedor que chegar.</p></div></div>
</div>
''')))

p2.append(("Jornada08", page("§2 · 08/09", "A CADEIRA", '''
<p class="label mute">Por que a etapa 7 existe</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">Todo fornecedor de IA tem um vendedor. A sua mesa merece <i>alguém do seu lado</i> quando a fatura chega.</h1>
  <div class="margnote">Também para quem já tem IA rodando: não precisa do programa para ter a cadeira.</div>
</div>
''', paper=True)))

p2.append(("Jornada09", page("§2 · 09/09", "O PRÓXIMO PASSO", '''
<p class="label">Onde vocês estão nesse caminho hoje?</p>
<h1 class="sm">A história começa com uma conversa de <i>45 minutos.</i></h1>
<p class="lede">E com o seu Mapa de Vazamento, gratuito.</p>
''' + note("→", "contato@abbaservices.com.br"))))

F.update(dict(p2)); PAGES.append(("peca-02","02 · A jornada",[n for n,_ in p2]))

# ============================================================
# PEÇA 03 · PROMETEMOS × RECUSAMOS
# ============================================================
p3 = []
p3.append(("Recusa01", page("§3 · 01/06", "PEÇA 03", '''
<p class="label">O documento que define uma consultoria</p>
<h1>O que prometemos<br>— e o que <i>recusamos.</i></h1>
<div class="rule"></div>
<p class="lede">Escopo sem limite é escopo sem preço. Toda proposta nossa tem uma seção do que não vamos fazer.</p>
''')))

p3.append(("Recusa02", page("§3 · 02/06", "PROMETEMOS", '''
<p class="label">Prometemos</p>
<table>
<tr><td class="k">I</td><td><b>O método.</b> Métrica combinada antes, medida depois, num registro que vocês veem inteiro.</td></tr>
<tr><td class="k">II</td><td><b>Presença recorrente de quem decide</b> — não um relatório na gaveta.</td></tr>
<tr><td class="k">III</td><td><b>Honestidade sobre escopo:</b> o que fazemos, nomeado — e o que fica de fora.</td></tr>
</table>
''')))

p3.append(("Recusa03", page("§3 · 03/06", "RECUSAMOS", '''
<p class="label">Recusamos</p>
<table>
<tr><td class="k">I</td><td><b>Prometer acurácia que não medimos.</b> Um número que não temos destruiria a única coisa que não se recompra: credibilidade técnica.</td></tr>
<tr><td class="k">II</td><td><b>Prever o imprevisível.</b> Não vendemos oráculo.</td></tr>
</table>
''', paper=True)))

p3.append(("Recusa04", page("§3 · 04/06", "RECUSAMOS", '''
<p class="label">Recusamos</p>
<table>
<tr><td class="k">III</td><td><b>Piloto sem métrica.</b> É a receita documentada do fracasso — aceitar seria vender uma derrota com nota fiscal.</td></tr>
<tr><td class="k">IV</td><td><b>IA decidindo sozinha.</b> A IA rascunha, um humano assina, a diretoria decide.</td></tr>
</table>
''', paper=True)))

p3.append(("Recusa05", page("§3 · 05/06", "POR QUE PUBLICAR", '''
<p class="label mute">Por que isto é público</p>
<h1 class="xs">Uma recusa escrita é a única promessa que <i>custa alguma coisa</i> para quem a faz.</h1>
<p class="lede">Todo mundo consegue prometer. Poucos conseguem publicar o que se recusam a vender — porque copiar esta lista exigiria parar de vender o que se vende hoje.</p>
''')))

p3.append(("Recusa06", page("§3 · 06/06", "O PRÓXIMO PASSO", '''
<p class="label">O próximo passo</p>
<h1 class="sm">Qual métrica a sua empresa mediria <i>antes</i> de começar?</h1>
<p class="lede">É a primeira pergunta que a gente faz. E é de graça.</p>
''' + note("→", "contato@abbaservices.com.br"))))

F.update(dict(p3)); PAGES.append(("peca-03","03 · Prometemos × Recusamos",[n for n,_ in p3]))

# ============================================================
# PEÇA 04 · O MAPA DE VAZAMENTO
# ============================================================
p4 = []
p4.append(("Mapa01", page("§4 · 01/07", "PEÇA 04", '''
<p class="label">Degrau zero · gratuito</p>
<h1>O Mapa<br>de <i>Vazamento.</i></h1>
<div class="rule"></div>
<p class="lede">Uma estimativa em reais do que pode estar saindo da sua operação — calculada de fora, antes de você contratar qualquer coisa.</p>
''')))

p4.append(("Mapa02", page("§4 · 02/07", "POR QUE UM NÚMERO", '''
<p class="label mute">Por que um número, e não três hipóteses</p>
<h1 class="xs">Três hipóteses fazem o leitor pensar. <i>Um número faz o leitor reagir.</i></h1>
<p class="lede">Concordando, discordando ou corrigindo. Qualquer uma das três é uma conversa — a ausência de reação é um PDF arquivado.</p>
''', paper=True)))

p4.append(("Mapa03", page("§4 · 03/07", "A CONVERSA", '''
<p class="label">45 minutos · cinco perguntas</p>
<div class="steps">
  <div class="step"><span class="n">1</span><div><h3>O caminho de uma nota fiscal aí dentro</h3><p>do pedido ao pagamento — quem toca, em que sistema.</p></div></div>
  <div class="step"><span class="n">2</span><div><h3>O que mais atrasa o fechamento do mês</h3><p>e quanto tempo ele leva hoje.</p></div></div>
  <div class="step"><span class="n">3</span><div><h3>Que número em reais dói hoje</h3><p>e já é medido.</p></div></div>
  <div class="step"><span class="n">4</span><div><h3>Quando vocês descobrem que perderam dinheiro</h3><p>no mês, no trimestre, ou no ano seguinte.</p></div></div>
  <div class="step"><span class="n">5</span><div><h3>Se esse número melhorasse 20%, quem comemoraria</h3><p>— quase nunca é quem marcou a reunião.</p></div></div>
</div>
''')))

p4.append(("Mapa04", page("§4 · 04/07", "AS REGRAS", '''
<p class="label">As regras de honestidade</p>
<table>
<tr><td class="k">I</td><td><b>Faixa, nunca número exato.</b> Um número exato calculado de fora é uma mentira com aparência de precisão — e o primeiro CFO competente desmonta.</td></tr>
<tr><td class="k">II</td><td><b>Premissa sem fonte não entra.</b> Se não há referência pública citável, o item sai do mapa.</td></tr>
<tr><td class="k">III</td><td><b>A faixa pode ser pequena.</b> Se a estimativa honesta for baixa, ela vai baixa. Mapa inflado vende uma reunião e perde a relação.</td></tr>
</table>
''')))

p4.append(("Mapa05", page("§4 · 05/07", "O QUE ELE NÃO É", '''
<p class="label mute">O limite, dito por nós</p>
<div class="marg" style="margin-top:auto;margin-bottom:auto">
  <h1 class="sm">O Mapa aponta onde o dinheiro parece estar vazando. Ele <i>não prova a causa</i> — foi calculado de fora.</h1>
  <div class="margnote">E nunca prometemos capturar a faixa inteira. A captura é uma fração dela, e isso a gente diz em voz alta.</div>
</div>
''', paper=True)))

p4.append(("Mapa06", page("§4 · 06/07", "O QUE VOCÊ RECEBE", '''
<p class="label">O que fica com você</p>
<table>
<tr><td class="k">01</td><td><b>A faixa em reais</b>, em ordem de grandeza anual, e o vetor principal: por onde o dinheiro sai.</td></tr>
<tr><td class="k">02</td><td><b>Três premissas numeradas, com a fonte citada</b> — incluindo o que assumimos e ainda não sabemos.</td></tr>
<tr><td class="k">03</td><td><b>As perguntas que só você pode responder</b> — e que mudariam a estimativa nos dois sentidos.</td></tr>
</table>
''' + note("—", "Duas páginas. Sem custo, sem compromisso, sem dado seu no documento."))))

p4.append(("Mapa07", page("§4 · 07/07", "O PRÓXIMO PASSO", '''
<p class="label">O próximo passo</p>
<h1 class="sm">Tem algum número em reais aí dentro que <i>dói hoje</i> — e que vocês já medem?</h1>
<p class="lede">Essa é a conversa. Quarenta e cinco minutos.</p>
''' + note("→", "contato@abbaservices.com.br"))))

F.update(dict(p4)); PAGES.append(("peca-04","04 · O Mapa de Vazamento",[n for n,_ in p4]))

# ============================================================
# escrita + canvas
# ============================================================
order = []
for pid, nome, arqs in PAGES:
    order.extend(arqs)

ren = {}
first = order[0]
for name in order:
    fn = "Main.dc.html" if name == first else name + ".dc.html"
    ren[name] = fn
    open(fn, "w", encoding="utf-8").write(F[name])

boards = []
for pid, nome, arqs in PAGES:
    for i, a in enumerate(arqs):
        col = i % 5; row = i // 5
        boards.append({"file": ren[a], "x": col*1260, "y": row*1620,
                       "w": W, "h": HT, "page": pid})

canvas = {
  "pages": [{"id": pid, "name": nome} for pid, nome, _ in PAGES],
  "artboards": boards,
  "annotations": [
    {"id":"nota-sistema","x":0,"y":-260,"w":620,"page":"peca-01",
     "text":"SISTEMA · documento de registro.\nNewsreader (títulos) · Source Serif 4 (corpo) · IBM Plex Mono (rótulos, folios e números).\nNavy #1B2A4A e papel #F2F4F7 alternando; dourado #C2A35B só em fiada, marca e uma palavra por tela.\nTodo texto dentro do recorte 1:1 da grade do perfil."},
    {"id":"nota-arquetipos","x":700,"y":-260,"w":540,"page":"peca-01",
     "text":"SEIS ARQUÉTIPOS DE CARD, não um template repetido:\ncapa · razão (tabela) · etapas · marginália · diagrama · fecho.\nÉ a variedade que faz o feed parecer feito por gente."}
  ],
  "launch": {"view": "canvas", "page": "peca-01"}
}
open("canvas.json","w",encoding="utf-8").write(json.dumps(canvas,ensure_ascii=False,indent=2))
print("arquivos:", len(order), "| paginas:", len(PAGES))
for pid,nome,arqs in PAGES: print(" ", nome, "->", len(arqs), "telas")
