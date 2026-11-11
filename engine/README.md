# History Channel video engine

Retro 16-bit pixel-art history Shorts (1080x1920, 30 fps, English narration, chiptune music, captions).

## Files
- build3.py: core engine (sprites for Incas/conquistadors, South America map, pixel font, text labels, backgrounds helpers).
- build4.py: episode 1 (Columbus). Adds Columbus, Isabella, Pope, Taino, Vespucci, diplomats, sailor, caravel sprites, Atlantic world map, sea/palm backgrounds, bubbles, caption overlay, compose(), Spanish-renaissance chiptune music(), piper tts(), wavdur().
- build5.py: episode 2 (La Navidad). TEMPLATE for new episodes: it execs build4.py up to the render marker, then defines SCENES, extra sprites, make_bg(i, li), draw_scene(...) and the render loop.
- ps2p.woff: Press Start 2P pixel font.

## Setup in a fresh container
    pip install --break-system-packages piper-tts
    mkdir -p voice_en && cd voice_en && curl -sL -o v.tgz https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-en-us-ryan-high.tar.gz && tar xzf v.tgz && rm v.tgz && cd ..
    export HC_DIR=$PWD

## New episode
1. Copy build5.py to buildN.py. Change OUT (outN) and FINAL (epNN_slug_EN.mp4).
2. Rewrite SCENES: 7-9 scenes, each (TITLE IN CAPS, [(spoken, caption), ...]). Spoken text spells numbers and hard names phonetically (Taino -> Tyeeno, Nina -> Neenya, 1492 -> fourteen ninety-two). Captions use digits and real spelling.
3. Write make_bg and draw_scene for the new story. Reuse sprites in SP; add new ones with the same 52x84 outline() style. Every character and place gets a name label. Use maps for geography.
4. python3 buildN.py check  -> out*/check*.png, inspect a contact sheet, fix overlaps.
5. python3 buildN.py        -> final mp4. Keep total 70-115 s. Audio peak must stay below -1 dB.
