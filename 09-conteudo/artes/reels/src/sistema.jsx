// Sistema visual da ABBA em movimento.
//
// Isto NÃO é um sistema novo. É o mesmo `gen.py` dos carrosséis traduzido para
// vídeo: mesma paleta, mesma tipografia, mesmo grão, mesma moldura, mesma barra
// de progresso. O que muda é o formato (1080×1920 em vez de 1080×1350) e o fato
// de o tempo existir.
//
// Regra do movimento: **a animação nunca é o assunto.** Ela dirige o olho e
// marca a passagem de um argumento para o outro. Nada gira, nada pisca, nada
// quica. Uma casa que vende registro não faz motion de anúncio de aplicativo.
//
// Tudo aqui trabalha em FRAME ABSOLUTO, sem <Sequence>. É de propósito: a barra
// de progresso precisa atravessar o vídeo inteiro sem reiniciar, e é mais fácil
// garantir isso com um relógio só do que sincronizando vários.

import React from 'react';
import {
  AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate,
  spring, staticFile, Img,
} from 'remotion';

// ── paleta, idêntica à dos carrosséis ──────────────────────────────────────
export const C = {
  navy: '#1B2A4A', papel: '#F2F4F7',
  ouro: '#C2A35B', ouroClaro: '#D8BE7C', ouroEscuro: '#8A6E28',
  branco: '#FFFFFF',
  fio: '#33456A', fioPapel: '#CBD3DF',
  mudo: '#5D6E92', mudoPapel: '#8C97AA',
  lede: '#C3CAD8', ledePapel: '#4E5A70',
  nota: '#7C88A2', notaPapel: '#78839A',
  serie2: '#7C88A2',                       // o "percebido" da figura
};

export const F = {
  display: '"Newsreader", Georgia, serif',
  texto: '"Source Serif 4", Georgia, serif',
  mono: '"IBM Plex Mono", monospace',
};

export const W = 1080, H = 1920, M = 104;

const GRAO =
  "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E" +
  "%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' " +
  "stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E";

// ── entrada padrão: sobe 26px e aparece ────────────────────────────────────
// Uma única entrada usada em tudo. Vocabulário curto é o que faz a peça
// parecer dirigida em vez de montada.
export const useEntrada = (aos = 0) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({
    frame: frame - aos, fps,
    config: { damping: 200, stiffness: 90, mass: 0.7 },
  });
  return {
    opacity: interpolate(s, [0, 1], [0, 1]),
    transform: `translateY(${interpolate(s, [0, 1], [26, 0])}px)`,
  };
};

// ── cena: recorte de tempo em frame absoluto ───────────────────────────────
export const Cena = ({ de, ate, children }) => {
  const frame = useCurrentFrame();
  if (frame < de || frame >= ate) return null;
  return <>{children}</>;
};

// ── número que conta. Só para número que está no cânone. ───────────────────
export const Contador = ({ ate, aos = 0, dur = 32, sufixo = '%' }) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame - aos, [0, dur], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const eased = 1 - Math.pow(1 - t, 3);   // assenta em vez de parar seco
  return (
    <>
      {Math.round(ate * eased)}
      <span style={{ fontSize: '0.42em', verticalAlign: '0.52em', letterSpacing: '-0.01em' }}>
        {sufixo}
      </span>
    </>
  );
};

// ── a moldura, sempre no topo da árvore e nunca dentro de cena ─────────────
export const Moldura = ({ papel = false, folio, referencia, children }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  const tinta = papel ? C.navy : C.branco;
  const fio = papel ? C.fioPapel : C.fio;
  const mudo = papel ? C.mudoPapel : C.mudo;

  const progresso = interpolate(frame, [0, durationInFrames - 1], [0, W - 2 * M], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{
      backgroundColor: papel ? C.papel : C.navy,
      fontFamily: F.texto, color: tinta,
    }}>
      <AbsoluteFill style={{
        backgroundImage: `url("${GRAO}")`, backgroundSize: '240px 240px',
        opacity: papel ? 0.42 : 0.06,
        mixBlendMode: papel ? 'multiply' : 'overlay',
      }} />

      <div style={{
        position: 'absolute', top: 112, left: M, right: M,
        display: 'flex', justifyContent: 'space-between',
        fontFamily: F.mono, fontSize: 22, letterSpacing: '0.2em', color: mudo,
      }}>
        <span>ABBA</span><span>{folio}</span>
      </div>

      <div style={{ position: 'absolute', top: 176, left: M, right: M, height: 1, background: fio }} />
      <div style={{ position: 'absolute', top: 175, left: M, width: progresso, height: 3, background: C.ouro }} />

      <AbsoluteFill style={{
        left: M, top: 250, width: W - 2 * M, height: H - 250 - 230,
        display: 'flex', flexDirection: 'column', justifyContent: 'center',
      }}>
        {children}
      </AbsoluteFill>

      <div style={{ position: 'absolute', bottom: 172, left: M, right: M, height: 1, background: fio }} />
      <div style={{
        position: 'absolute', bottom: 104, left: M, right: M,
        display: 'flex', justifyContent: 'space-between',
        fontFamily: F.mono, fontSize: 22, letterSpacing: '0.2em',
      }}>
        <span style={{ color: mudo }}>{referencia}</span>
        <span style={{ color: C.ouro }}>abbaservices.com.br</span>
      </div>
    </AbsoluteFill>
  );
};

// ── peças de texto ─────────────────────────────────────────────────────────
export const Rotulo = ({ children, aos = 0, papel = false }) => {
  const e = useEntrada(aos);
  return (
    <p style={{
      fontFamily: F.mono, fontSize: 24, letterSpacing: '0.22em',
      textTransform: 'uppercase', color: papel ? C.ouroEscuro : C.ouro,
      margin: '0 0 44px', ...e,
    }}>{children}</p>
  );
};

export const Manchete = ({ children, tamanho = 104, aos = 0, papel = false }) => {
  const e = useEntrada(aos);
  return (
    <h1 style={{
      fontFamily: F.display, fontWeight: 400, margin: 0,
      fontSize: tamanho, lineHeight: 1.08, letterSpacing: '-0.02em',
      color: papel ? C.navy : C.branco, ...e,
    }}>{children}</h1>
  );
};

export const Grifo = ({ children, papel = false }) => (
  <i style={{ fontStyle: 'italic', fontWeight: 300, color: papel ? C.ouroEscuro : C.ouroClaro }}>
    {children}
  </i>
);

export const Lede = ({ children, aos = 0, papel = false, tamanho = 38 }) => {
  const e = useEntrada(aos);
  return (
    <p style={{
      fontSize: tamanho, lineHeight: 1.5, margin: '44px 0 0', maxWidth: 860,
      color: papel ? C.ledePapel : C.lede, ...e,
    }}>{children}</p>
  );
};

export const Filete = ({ aos = 0 }) => {
  const frame = useCurrentFrame();
  const w = interpolate(frame - aos, [0, 18], [0, 96], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  return <div style={{ height: 1, width: w, background: C.ouro, margin: '48px 0 0', flex: 'none' }} />;
};

export const Marca = ({ aos = 0 }) => {
  const e = useEntrada(aos);
  return <Img src={staticFile('abba-logo.png')}
              style={{ width: 210, height: 'auto', display: 'block', ...e }} />;
};

// ── item numerado, o mesmo `td.k` dos carrosséis ───────────────────────────
export const Item = ({ n, children, aos = 0, papel = false }) => {
  const e = useEntrada(aos);
  return (
    <div style={{
      display: 'grid', gridTemplateColumns: '90px 1fr', gap: 26,
      padding: '30px 0', borderBottom: `1px solid ${papel ? C.fioPapel : C.fio}`,
      ...e,
    }}>
      <span style={{
        fontFamily: F.mono, fontSize: 24, color: papel ? C.mudoPapel : C.mudo,
        letterSpacing: '0.08em', paddingTop: 6,
      }}>{n}</span>
      <div style={{ fontSize: 36, lineHeight: 1.42, color: papel ? C.ledePapel : C.lede }}>
        {children}
      </div>
    </div>
  );
};

export const Forte = ({ children, papel = false }) => (
  <b style={{ color: papel ? C.navy : C.branco, fontWeight: 600 }}>{children}</b>
);
