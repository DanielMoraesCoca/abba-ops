// As fontes vêm do disco, não da rede.
//
// Mesmo motivo do `render.sh` dos carrosséis: quando a rede caía, o Chromium
// desistia e desenhava em Georgia SEM AVISAR, entregando arquivo errado. Num
// vídeo de 960 quadros isso seria descoberto tarde e caro. Aqui o render espera
// as fontes carregarem antes de desenhar o primeiro quadro.

import { staticFile, delayRender, continueRender } from 'remotion';
import { useState, useEffect } from 'react';

let injetado = false;

export const useFontes = () => {
  const [handle] = useState(() => delayRender('carregando as fontes da casa'));
  const [pronto, setPronto] = useState(false);

  useEffect(() => {
    if (!injetado) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = staticFile('fonts/local.css');
      document.head.appendChild(link);
      injetado = true;
    }
    // as três famílias precisam estar carregadas, não só declaradas
    Promise.all([
      document.fonts.load('400 100px "Newsreader"'),
      document.fonts.load('300 100px "Newsreader"'),
      document.fonts.load('italic 300 100px "Newsreader"'),
      document.fonts.load('400 40px "Source Serif 4"'),
      document.fonts.load('600 40px "Source Serif 4"'),
      document.fonts.load('400 24px "IBM Plex Mono"'),
    ])
      .then(() => document.fonts.ready)
      .then(() => { setPronto(true); continueRender(handle); })
      .catch(() => { setPronto(true); continueRender(handle); });
  }, [handle]);

  return pronto;
};
