// Peça 07 · O número desconfortável — versão Reels (1080×1920, 32s a 30fps).
//
// Mesmo argumento do carrossel, mesma ordem, mesmas palavras. O que o vídeo
// acrescenta é uma coisa só, e é a que justifica ele existir: **a figura da
// distância entre o medido e o percebido acontece na frente da pessoa** em vez
// de aparecer pronta. As barras crescem em sentidos opostos e o vão de 40
// pontos abre. Isso não dá para fazer em carrossel.
//
// Nenhum número fora do cânone da base de evidências. Nenhuma frase nova.

import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import {
  Moldura, Cena, Rotulo, Manchete, Grifo, Lede, Filete, Marca, Item, Forte,
  Contador, useEntrada, C, F,
} from './sistema';
import { useFontes } from './fontes';

// ── cronograma, em frames a 30fps ─────────────────────────────────────────
const T = {
  hook:       [0,   130],
  percepcao:  [130, 270],
  experimento:[270, 430],
  figura:     [430, 640],
  ressalva:   [640, 800],   // única cena de papel: papel marca a ressalva
  conclusao:  [800, 910],
  cta:        [910, 960],
};

// ── a figura, agora em movimento ──────────────────────────────────────────
const FiguraDistancia = ({ aos }) => {
  const frame = useCurrentFrame();
  const Z = 400, U = 10, X = 0, BW = 300, R = 6, G = 3;

  // as duas barras crescem, a de cima primeiro: primeiro o que eles sentiram,
  // depois o que o cronômetro registrou. A ordem importa, é a ordem do estudo.
  const cresce = (atraso, dur = 34) =>
    interpolate(frame - aos - atraso, [0, dur], [0, 1], {
      extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
      easing: (t) => 1 - Math.pow(1 - t, 3),
    });

  const hB = Math.round(20 * U * cresce(0));
  const hA = Math.round(19 * U * cresce(26));
  const colchete = interpolate(frame - aos - 62, [0, 22], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });

  const barra = (h, baixo, cor) => {
    if (h < R + G) return null;
    const y0 = baixo ? Z + G : Z - G;
    const y1 = baixo ? Z + h : Z - h;
    const sy = baixo ? -R : R;
    return (
      <path
        d={`M${X},${y0} L${X},${y1 + sy} Q${X},${y1} ${X + R},${y1} L${X + BW - R},${y1} Q${X + BW},${y1} ${X + BW},${y1 + sy} L${X + BW},${y0} Z`}
        fill={cor}
      />
    );
  };

  const bx = X + BW + 54;
  return (
    <svg viewBox="0 0 872 800" width="100%" style={{ overflow: 'visible' }}>
      <text x={X} y={Z - 20 * U - 76} fill={C.nota} fontFamily={F.mono}
            fontSize="22" letterSpacing="4" opacity={cresce(0)}>RELATADO POR ELES</text>
      <text x={X} y={Z - 20 * U - 20} fill={C.branco} fontFamily={F.display}
            fontSize="60" opacity={cresce(0)}>20% mais rápidos</text>

      {barra(hB, false, C.serie2)}
      {barra(hA, true, C.ouroClaro)}
      <line x1={-104} y1={Z} x2={X + BW + 20} y2={Z} stroke={C.nota} strokeWidth="1" />

      <text x={X} y={Z + 19 * U + 90} fill={C.branco} fontFamily={F.display}
            fontSize="60" opacity={cresce(26)}>19% mais lentos</text>
      <text x={X} y={Z + 19 * U + 140} fill={C.nota} fontFamily={F.mono}
            fontSize="22" letterSpacing="4" opacity={cresce(26)}>MEDIDO NO CRONÔMETRO</text>

      <g opacity={colchete}>
        <path d={`M${bx},${Z - 20 * U} L${bx + 18},${Z - 20 * U} L${bx + 18},${Z + 19 * U} L${bx},${Z + 19 * U}`}
              fill="none" stroke={C.ouro} strokeWidth="1" />
        <text x={bx + 44} y={Z - 6} fill={C.ouro} fontFamily={F.mono} fontSize="23" letterSpacing="3">40 PONTOS</text>
        <text x={bx + 44} y={Z + 30} fill={C.ouro} fontFamily={F.mono} fontSize="23" letterSpacing="3">DE DISTÂNCIA</text>
      </g>
    </svg>
  );
};

// ── o número herói do hook ────────────────────────────────────────────────
const Heroi = ({ aos }) => {
  const e = useEntrada(aos);
  return (
    <div style={{
      fontFamily: F.display, fontWeight: 300, fontSize: 340, lineHeight: 0.84,
      letterSpacing: '-0.045em', color: C.ouroClaro,
      fontVariantNumeric: 'tabular-nums', margin: '0 0 30px', ...e,
    }}>
      <Contador ate={19} aos={aos + 6} dur={30} />
    </div>
  );
};

export const Peca07 = () => {
  useFontes();
  const frame = useCurrentFrame();
  const papel = frame >= T.ressalva[0] && frame < T.ressalva[1];

  const folio =
    frame < T.experimento[0] ? 'PEÇA 07' :
    frame < T.figura[0] ? 'O EXPERIMENTO' :
    frame < T.ressalva[0] ? 'A PERCEPÇÃO' :
    frame < T.conclusao[0] ? 'O LIMITE' :
    frame < T.cta[0] ? 'A CONCLUSÃO' : 'O PRÓXIMO PASSO';

  return (
    <Moldura papel={papel} folio={folio} referencia="§7 · METR, jul/2025">

      <Cena de={T.hook[0]} ate={T.hook[1]}>
        <Rotulo aos={0}>O estudo mais desconfortável do ano</Rotulo>
        <Heroi aos={10} />
        <Manchete tamanho={92} aos={48}>mais lentos.</Manchete>
        <Lede aos={62}>Desenvolvedores experientes usando IA, medidos por fora.</Lede>
      </Cena>

      <Cena de={T.percepcao[0]} ate={T.percepcao[1]}>
        <Rotulo aos={T.percepcao[0]}>Depois da medição, a pergunta</Rotulo>
        <Manchete tamanho={96} aos={T.percepcao[0] + 10}>
          E eles saíram convencidos de que estavam <Grifo>20% mais rápidos.</Grifo>
        </Manchete>
      </Cena>

      <Cena de={T.experimento[0]} ate={T.experimento[1]}>
        <Rotulo aos={T.experimento[0]}>Não foi enquete</Rotulo>
        <Item n="01" aos={T.experimento[0] + 12}>
          <Forte>16 desenvolvedores experientes, 246 tarefas reais</Forte>, no código que eles mesmos dominavam. Metade com IA, metade sem.
        </Item>
        <Item n="02" aos={T.experimento[0] + 30}>
          <Forte>O tempo foi cronometrado</Forte>, não perguntado.
        </Item>
      </Cena>

      <Cena de={T.figura[0]} ate={T.figura[1]}>
        <Rotulo aos={T.figura[0]}>A distância</Rotulo>
        <FiguraDistancia aos={T.figura[0] + 14} />
      </Cena>

      <Cena de={T.ressalva[0]} ate={T.ressalva[1]}>
        <Rotulo aos={T.ressalva[0]} papel>O que este número não prova</Rotulo>
        <Manchete tamanho={80} aos={T.ressalva[0] + 10} papel>
          Isso não é argumento contra IA, e a gente faz questão <Grifo papel>de dizer.</Grifo>
        </Manchete>
        <Lede aos={T.ressalva[0] + 26} papel tamanho={34}>
          A amostra é pequena. O maior experimento já publicado, com 4.867 desenvolvedores, encontrou 26% mais tarefas concluídas.
        </Lede>
      </Cena>

      <Cena de={T.conclusao[0]} ate={T.conclusao[1]}>
        <Rotulo aos={T.conclusao[0]}>O que os dois estudos dizem juntos</Rotulo>
        <Manchete tamanho={98} aos={T.conclusao[0] + 10}>
          Ninguém sabe se a ferramenta ajudou <Grifo>sem medir de fora.</Grifo>
        </Manchete>
      </Cena>

      <Cena de={T.cta[0]} ate={T.cta[1]}>
        <Marca aos={T.cta[0]} />
        <Filete aos={T.cta[0] + 8} />
        <Manchete tamanho={72} aos={T.cta[0] + 12}>
          Se nem quem usa sabe, <Grifo>como a diretoria saberia?</Grifo>
        </Manchete>
        <Lede aos={T.cta[0] + 24} tamanho={32}>contato@abbaservices.com.br</Lede>
      </Cena>

    </Moldura>
  );
};
