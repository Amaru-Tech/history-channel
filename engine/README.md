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
2. Rewrite SCENES: 7-9 scenes. The FIRST line of scene 1 is always a title line that names the topic and its main figure, e.g. ("The first voyage around the world. Ferdinand Magellan.", "The First Voyage Around the World: Ferdinand Magellan"), drawn as a title card (topic in big yellow labels, main character with name label, a map or key prop). The hook and story start on the next line (Jorge's request, episode 10).
   Scenes, each (TITLE IN CAPS, [(spoken, caption), ...]). Spoken text spells numbers out (1492 -> fourteen ninety-two). Captions use digits and real spelling.
   Spanish and Native names: write them as {Name} in the spoken text and give their IPA in the IPA dict (see build_ep07.py). tts() turns them into piper raw phonemes [[ ... ]], so they sound Spanish instead of robotic. Never use hyphenated phonetic spellings (Mon-teh-see-nos).
   Voice: always piper en-us-ryan-high, length_scale 0.88. Jorge wants the same narrator in every episode (tested Kokoro voices in ep 7, rejected).
3. Write make_bg and draw_scene for the new story. Reuse sprites in SP; add new ones with the same 52x84 outline() style. Every character and place gets a name label. Use maps for geography.
4. python3 buildN.py check  -> out*/check*.png, inspect a contact sheet, fix overlaps.
5. python3 buildN.py        -> final mp4. Keep total 70-115 s. Audio peak must stay below -1 dB.

## Visual quality checklist (from Jorge's review of episode 5)
- Fill every frame: background life (town, dock, clouds, gulls, torches, crowds, props) and some motion in each line. Avoid empty skies and lone characters.
- Ships float in water. Never put a hull on sand or grass; a grounded ship sits in shallow water (use shallow() and foam()).
- Voyage routes on maps start and end exactly on a coastline vertex or a city dot, never in open sea or inland. Use region_map() and AMER_D from build_ep05.py for Caribbean and Central America close-ups.
- Labels never overlap each other, map titles or sprites. Keep scale consistent: main characters sc=2.
