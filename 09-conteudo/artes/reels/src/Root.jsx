import React from 'react';
import { Composition } from 'remotion';
import { Peca07 } from './Peca07';
import { W, H } from './sistema';

export const RemotionRoot = () => (
  <>
    <Composition
      id="peca-07"
      component={Peca07}
      durationInFrames={960}   // 32s a 30fps
      fps={30}
      width={W}
      height={H}
    />
  </>
);
