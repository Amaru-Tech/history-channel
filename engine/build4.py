import os, sys, wave, math, random, subprocess, textwrap
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

D = os.environ.get("HC_DIR", os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")
src = open(f"{D}/build3.py").read().split("# ---------------- animation per scene")[0]
exec(src)  # engine: constants, sprites, helpers, map, backgrounds from episode 1
OUT = f"{D}/out4"; os.makedirs(OUT, exist_ok=True)
VOICE = f"{D}/voice_en/en-us-ryan-high.onnx"
CHECK = "check" in sys.argv
EXT_AUDIO = os.environ.get("NARRATION")  # optional: externally produced narration chunks dir

# (title, [(spoken, caption), ...])
SCENES = [
 ("1492", [
  ("In fourteen ninety-two, Christopher Columbus reached a brand-new continent.", "In 1492, Christopher Columbus reached a brand-new continent."),
  ("The strange part? He never knew it.", "The strange part? He never knew it.")]),
 ("THE PLAN", [
  ("Columbus wanted to reach Asia by sailing west.", "Columbus wanted to reach Asia by sailing west."),
  ("He thought Japan was about four thousand kilometers away.", "He thought Japan was about 4,000 km away."),
  ("The real distance was closer to twenty thousand.", "The real distance was closer to 20,000 km."),
  ("Royal experts in Portugal and Spain said his math was wrong. They were right.", "Royal experts in Portugal and Spain said his math was wrong. They were right.")]),
 ("THREE SHIPS", [
  ("Still, Queen Isabella of Castile backed him.", "Still, Queen Isabella of Castile backed him."),
  ("Three ships: the Neenya, the Pinta and the Santa Maria. About ninety men.", "Three ships: the Niña, the Pinta and the Santa María. About 90 men."),
  ("Five weeks of open ocean.", "Five weeks of open ocean.")]),
 ("LAND!", [
  ("On October twelfth, a sailor named Rodrigo de Triana shouted: Land!", "October 12: sailor Rodrigo de Triana shouts: LAND!"),
  ("The crown had promised a lifetime pension to the first man to see it.", "The crown had promised a lifetime pension to the first man to see it."),
  ("Columbus kept it for himself. He said he had seen a light the night before.", "Columbus kept it for himself. He said he saw a light the night before.")]),
 ("THE INDIES?", [
  ("He landed in the Bahamas, met the Tyeeno people, and called them Indians.", "He landed in the Bahamas, met the Taíno people, and called them 'Indians'."),
  ("He was sure he was in Asia. He died in fifteen oh six still believing it.", "He was sure he was in Asia. He died in 1506 still believing it.")]),
 ("THE POPE'S LINE", [
  ("Back in Europe, Spain and Portugal raced to claim the new lands.", "Back in Europe, Spain and Portugal raced to claim the new lands."),
  ("In fourteen ninety-three, Pope Alexander the Sixth, a Spaniard, drew a line down the Atlantic.", "1493: Pope Alexander VI, a Spaniard, drew a line down the Atlantic."),
  ("West for Spain. East for Portugal.", "West for Spain. East for Portugal.")]),
 ("TORDESILLAS 1494", [
  ("Portugal pushed back. In fourteen ninety-four, the Treaty of Tordeseeyas moved the line further west.", "Portugal pushed back. In 1494, the Treaty of Tordesillas moved the line west."),
  ("That small shift is why Brazil speaks Portuguese today.", "That small shift is why Brazil speaks Portuguese today.")]),
 ("A NEW WORLD", [
  ("So was it Asia? An Italian explorer, Amerigo Vespoochee, said no. He called it a New World.", "So was it Asia? Explorer Amerigo Vespucci said no. He called it a New World."),
  ("In fifteen oh seven, a German mapmaker wrote a new name on his map: America.", "In 1507, a German mapmaker wrote a new name on his map: AMERICA.")]),
 ("WHO GOT THE NAME?", [
  ("Columbus found it. Amerigo got the name.", "Columbus found it. Amerigo got the name."),
  ("One wrong guess, and the map of the world changed forever.", "One wrong guess, and the map of the world changed forever.")]),
]

# ---------------- new sprites ----------------
SKIN_T = (172, 108, 68); SKIN_TD = (140, 84, 50)

def face(d, skin=SKIN_E, shade=(200, 150, 116)):
    R(d, (19, 18, 33, 34), skin); R(d, (30, 18, 33, 34), shade)
    R(d, (22, 24, 23, 25), K); R(d, (28, 24, 29, 25), K); R(d, (25, 27, 26, 29), shade); R(d, (23, 31, 28, 31), shade)

def robe_body(d, robe, robe_d, skin=SKIN_E, wide=False):
    R(d, (19, 77, 24, 81), K); R(d, (28, 77, 33, 81), K)
    b = 42 if wide else 39; a = 10 if wide else 13
    d.polygon([(16, 36), (36, 36), (b, 78), (a, 78)], fill=robe)
    d.polygon([(30, 36), (36, 36), (b, 78), (33, 78)], fill=robe_d)
    R(d, (11, 37, 16, 56), robe); R(d, (36, 37, 41, 56), robe_d)
    R(d, (11, 56, 15, 59), skin); R(d, (37, 56, 41, 59), skin)

def columbus():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, (52, 44, 92), (34, 28, 64))
    R(d, (16, 36, 36, 39), WHITE); d.line([(18, 40), (26, 50), (34, 40)], fill=GOLD, width=2)
    face(d); HW = (226, 222, 214)
    R(d, (17, 14, 35, 19), HW); R(d, (16, 19, 19, 38), HW); R(d, (33, 19, 36, 38), HW)
    R(d, (16, 9, 36, 15), (150, 30, 34)); R(d, (19, 6, 33, 9), (150, 30, 34)); R(d, (16, 13, 36, 15), (110, 20, 24))
    return outline(im)

def isabella():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    d.polygon([(16, 36), (36, 36), (44, 81), (8, 81)], fill=(176, 30, 40))
    d.polygon([(30, 36), (36, 36), (44, 81), (32, 81)], fill=(130, 18, 30))
    for y in (50, 62, 74): R(d, (12, y, 40, y + 1), GOLD)
    R(d, (20, 36, 32, 46), GOLD_D); R(d, (22, 37, 30, 45), (220, 200, 120))
    R(d, (11, 37, 16, 54), (176, 30, 40)); R(d, (36, 37, 41, 54), (130, 18, 30))
    R(d, (11, 54, 15, 57), SKIN_E); R(d, (37, 54, 41, 57), SKIN_E)
    face(d); HA = (176, 92, 40)
    R(d, (17, 15, 35, 20), HA); R(d, (17, 20, 19, 36), HA); R(d, (33, 20, 35, 36), HA)
    R(d, (18, 10, 34, 15), GOLD); R(d, (18, 6, 20, 10), GOLD); R(d, (25, 4, 27, 10), GOLD); R(d, (32, 6, 34, 10), GOLD)
    R(d, (21, 11, 23, 13), RED); R(d, (29, 11, 31, 13), (40, 110, 200))
    return outline(im)

def pope():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    R(d, (44, 18, 45, 79), GOLD_D); R(d, (40, 22, 49, 24), GOLD); R(d, (43, 16, 46, 26), GOLD)
    robe_body(d, (240, 238, 228), (196, 194, 186), wide=True)
    d.polygon([(13, 36), (39, 36), (37, 48), (15, 48)], fill=(190, 24, 34)); R(d, (25, 40, 27, 46), GOLD)
    R(d, (11, 37, 16, 46), (190, 24, 34)); R(d, (36, 37, 41, 46), (150, 18, 26))
    face(d, SKIN, SKIN_D); R(d, (19, 18, 33, 21), (60, 50, 50))
    d.polygon([(19, 19), (33, 19), (31, 2), (21, 2)], fill=WHITE)
    for y in (16, 11, 6): R(d, (20, y, 32, y + 1), GOLD)
    R(d, (25, 0, 27, 3), GOLD)
    return outline(im)

def taino(step=0, feather=True):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    xs = [(20, 23), (29, 32)] if step == 0 else [(17, 20), (32, 35)]
    for x0, x1 in xs: R(d, (x0, 64, x1, 81), SKIN_T)
    R(d, (17, 36, 35, 62), SKIN_T); R(d, (31, 36, 35, 62), SKIN_TD)
    for y in (42, 48): R(d, (19, y, 33, y + 1), (200, 50, 30))
    R(d, (17, 58, 35, 67), WHITE); R(d, (23, 67, 29, 72), WHITE)
    R(d, (12, 37, 16, 56), SKIN_T); R(d, (36, 37, 40, 56), SKIN_TD)
    face(d, SKIN_T, SKIN_TD); R(d, (17, 13, 35, 21), HAIR); R(d, (16, 21, 19, 40), HAIR); R(d, (33, 21, 36, 40), HAIR)
    R(d, (17, 18, 35, 19), (200, 50, 30)); R(d, (24, 28, 27, 29), GOLD)
    if feather: R(d, (32, 4, 34, 18), WHITE); R(d, (32, 4, 34, 7), (200, 50, 30))
    return outline(im)

def vespucci():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, (120, 30, 40), (86, 20, 28))
    R(d, (16, 36, 36, 38), WHITE)
    R(d, (38, 46, 46, 60), (236, 222, 180)); R(d, (38, 46, 46, 47), BROWN); R(d, (38, 59, 46, 60), BROWN)
    face(d); R(d, (18, 15, 34, 20), (60, 40, 30)); R(d, (17, 20, 19, 30), (60, 40, 30)); R(d, (33, 20, 35, 30), (60, 40, 30))
    R(d, (15, 9, 37, 15), K); R(d, (17, 7, 33, 9), K)
    return outline(im)

def diplomat(robe, robe_d, hat):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, robe, robe_d); R(d, (16, 36, 36, 39), WHITE)
    face(d); R(d, (19, 27, 33, 35), (90, 60, 40)); R(d, (24, 30, 28, 30), (150, 80, 70))
    R(d, (16, 10, 36, 17), hat); R(d, (19, 7, 33, 10), hat)
    return outline(im)

def sailor():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    for x0, x1 in [(20, 23), (29, 32)]: R(d, (x0, 62, x1, 78), (110, 80, 50)); R(d, (x0 - 1, 77, x1 + 1, 81), K)
    R(d, (16, 36, 36, 63), (230, 226, 210)); R(d, (16, 58, 36, 60), BROWN)
    R(d, (11, 37, 16, 50), (230, 226, 210)); R(d, (36, 22, 40, 40), (230, 226, 210)); R(d, (36, 18, 40, 22), SKIN_E)
    face(d); R(d, (18, 12, 34, 18), RED); R(d, (30, 8, 36, 13), RED)
    return outline(im)

def caravel():
    im = Image.new("RGBA", (160, 130)); d = ImageDraw.Draw(im)
    for x, top in ((60, 6), (102, 22), (28, 40)): R(d, (x, top, x + 3, 96), BROWN_D)
    S = (244, 240, 226); SD = (210, 204, 186)
    d.polygon([(38, 18), (86, 18), (90, 42), (84, 68), (40, 68), (34, 42)], fill=S); d.polygon([(70, 18), (86, 18), (90, 42), (84, 68), (72, 68)], fill=SD)
    R(d, (58, 26, 65, 60), RED); R(d, (46, 39, 78, 46), RED)
    d.polygon([(86, 32), (118, 32), (120, 48), (116, 66), (88, 66)], fill=S); R(d, (100, 38, 105, 60), RED); R(d, (92, 46, 114, 51), RED)
    d.polygon([(30, 38), (14, 74), (40, 74)], fill=SD)
    d.polygon([(118, 92), (150, 80), (150, 84), (120, 96)], fill=BROWN_D)
    R(d, (60, 0, 72, 6), RED); R(d, (60, 3, 72, 4), GOLD)
    d.polygon([(6, 92), (146, 92), (132, 122), (22, 122)], fill=(140, 88, 46))
    R(d, (6, 72, 44, 94), (120, 74, 38)); R(d, (112, 80, 146, 94), (120, 74, 38))
    for y in (100, 110): R(d, (14, y, 140, y + 2), BROWN_D)
    R(d, (6, 92, 146, 94), GOLD_D); R(d, (12, 78, 16, 82), (240, 200, 90)); R(d, (22, 78, 26, 82), (240, 200, 90))
    return outline(im)

SP.update({"col": columbus(), "isa": isabella(), "pope": pope(), "tai0": taino(0), "tai1": taino(1), "tai2": taino(0, False),
           "vesp": vespucci(), "dES": diplomat((196, 40, 40), (150, 26, 30), K), "dPT": diplomat((40, 120, 70), (26, 86, 50), K),
           "sailor": sailor(), "ship": caravel()})

# ---------------- world map ----------------
NA_E = [(-100, 64), (-80, 64), (-65, 60), (-58, 54), (-56, 48), (-66, 45), (-70, 42), (-74, 40), (-76, 35), (-81, 31), (-80, 26),
        (-81.5, 25), (-82.5, 28), (-84, 30), (-90, 30), (-97, 27.5), (-97, 22), (-91, 18.5), (-87, 21.5), (-88, 16), (-84, 15),
        (-83, 10.5), (-79.5, 9)]
CA_W = [(-80, 7.5), (-86, 11.5), (-92, 15), (-100, 17)]
AMER = NA_E + SA + CA_W
EURAF = [(25, 64), (10, 60), (8, 57), (8, 54), (5, 53), (2, 51), (-1, 49.5), (-4.5, 48.5), (-1.5, 46.5), (-1.5, 43.5), (-9, 43),
         (-9, 37), (-6, 36), (-10, 32), (-13, 28), (-17, 21), (-17, 15), (-15, 11), (-8, 4.5), (0, 5.5), (9, 4), (9, -1),
         (12, -6), (13, -12), (12, -18), (15, -27), (18, -34), (25, -36)]
MED = [(-5.5, 36), (0, 38.5), (3, 43), (10, 44), (15, 40.5), (25, 39), (25, 31.5), (10, 33), (0, 35.5)]
GB = [(-5.5, 50), (1.5, 51), (0.5, 53), (-2, 56), (-2, 58.6), (-5, 58.6), (-6, 56), (-3, 54.5), (-4.5, 52)]
IE = [(-10, 51.6), (-6, 52), (-6, 55), (-8, 55.4), (-10, 54)]
CUBA = [(-85, 22), (-80, 23.2), (-74.2, 20.2), (-77, 19.9), (-80, 21.5), (-85, 21.6)]
HISP = [(-74.5, 19.8), (-69, 19.7), (-68.4, 18.5), (-72, 18), (-74.5, 18.4)]
AZORES = (-28, 38.5); CAPEVERDE = (-24, 16); CANARY = (-15.5, 28); PALOS = (-6.9, 37.2); BAHAMAS = (-74.5, 24.1)

def world_map(f, w=490, h=410, parch=False, americas=1.0, line=None, oldline=None, tint=False, route=None, japan=None,
              labels=(), america_text=False, title=None):
    m = Image.new("RGBA", (w, h)); d = ImageDraw.Draw(m); d.fontmode = "1"
    P = lambda lon, lat: (6 + (lon + 100) / 125 * (w - 12), 6 + (64 - lat) / 104 * (h - 12))
    sea = (226, 208, 164) if parch else (58, 98, 150); land = (196, 160, 104) if parch else (118, 150, 84)
    edge = (110, 74, 36) if parch else (52, 74, 38)
    R(d, (0, 0, w - 1, h - 1), sea)
    for lon in range(-90, 21, 30): x = P(lon, 0)[0]; d.line([(x, 0), (x, h)], fill=tint_c(sea, 0.9))
    for lat in range(60, -41, -30): y = P(0, lat)[1]; d.line([(0, y), (w, y)], fill=tint_c(sea, 0.9))
    eu = Image.new("L", (w, h), 0); ed = ImageDraw.Draw(eu)
    for poly in (EURAF, GB, IE): ed.polygon([P(*p) for p in poly], fill=255)
    ed.polygon([P(*p) for p in MED], fill=0)
    am = Image.new("L", (w, h), 0); ad = ImageDraw.Draw(am)
    for poly in (AMER, CUBA, HISP): ad.polygon([P(*p) for p in poly], fill=int(255 * americas))
    mask = ImageChops.lighter(eu, am)
    col = Image.new("RGBA", (w, h), land + (255,))
    if tint and line is not None:
        cd = ImageDraw.Draw(col); lx = P(line[0], 0)[0]
        R(cd, (0, 0, lx, h), (214, 70, 54)); R(cd, (lx, 0, w, h), (54, 150, 84))
    m.paste(col, (0, 0), mask)
    for poly in (EURAF, GB, IE) + ((AMER, CUBA, HISP) if americas > 0.6 else ()):
        d.polygon([P(*p) for p in poly], outline=edge)
    if americas < 0.6 and japan is None:
        pass
    if route:
        pts, prog = route; seg = [P(*p) for p in pts]
        lens = [math.dist(seg[k], seg[k + 1]) for k in range(len(seg) - 1)]; tot = sum(lens); want = tot * prog; acc = 0
        head = seg[0]
        for k, L in enumerate(lens):
            n = int(L // 6)
            for s in range(n):
                pos = acc + s * 6
                if pos > want: break
                a = seg[k]; b = seg[k + 1]; tt = s * 6 / L
                x, y = a[0] + (b[0] - a[0]) * tt, a[1] + (b[1] - a[1]) * tt; R(d, (x - 1, y - 1, x + 1, y + 1), WHITE); head = (x, y)
            acc += L
        x, y = head; d.polygon([(x - 6, y + 3), (x + 6, y + 3), (x + 4, y + 7), (x - 4, y + 7)], fill=BROWN); d.polygon([(x, y - 8), (x, y + 2), (x + 6, y + 1)], fill=WHITE)
    if japan:
        jx, jy = P(*japan); ph = (f // 4) % 2
        for k in range(0, 360, 30):
            a = math.radians(k + ph * 15); R(d, (jx + 16 * math.cos(a) - 1, jy + 9 * math.sin(a) - 1, jx + 16 * math.cos(a) + 1, jy + 9 * math.sin(a) + 1), YEL)
    if oldline is not None:
        x = P(oldline, 0)[0]
        for y in range(0, h, 10): R(d, (x - 1, y, x + 1, y + 5), (200, 200, 200))
    if line is not None:
        x = P(line[0], 0)[0]; yend = h * line[1]
        R(d, (x - 2, 0, x + 2, yend), YEL); R(d, (x - 1, 0, x - 1, yend), WHITE)
    if america_text:
        tx, ty = P(-63, -14)
        d.text((tx, ty), "AMERICA", font=ImageFont.truetype(FONT, 24), fill=(120, 40, 20), anchor="mm")
    for text, lon, lat, fg, bg in labels:
        x, y = P(lon, lat); tw = d.textlength(text, font=F16); x = min(max(x, tw / 2 + 8), w - tw / 2 - 8)
        R(d, (x - tw / 2 - 4, y - 10, x + tw / 2 + 3, y + 9), bg); d.text((x - tw / 2, y - 8), text, font=F16, fill=fg)
    if title:
        tw = d.textlength(title, font=F16); R(d, (w / 2 - tw / 2 - 5, 8, w / 2 + tw / 2 + 4, 30), K); d.text((w / 2 - tw / 2, 11), title, font=F16, fill=GOLD)
    d.rectangle((0, 0, w - 1, h - 1), outline=(240, 220, 170) if not parch else (110, 74, 36), width=3)
    return outline(m)

# ---------------- backgrounds ----------------
def sea(d, top, bot, y0, col1, col2):
    grad(d, top, bot, 0, y0, 10); R(d, (0, y0, CW, CH), col1)
    rnd = random.Random(5)
    for _ in range(120): x, y = rnd.randint(0, CW), rnd.randint(y0 + 6, CH); R(d, (x, y, x + rnd.choice((6, 10, 14)), y + 1), col2)

def palm(d, x, base, h, lean=1):
    for k in range(h // 6):
        R(d, (x + lean * k * k // 12, base - k * 6 - 6, x + lean * k * k // 12 + 7, base - k * 6), (130, 90, 50) if k % 2 else (110, 74, 40))
    tx = x + lean * (h // 6) ** 2 // 12 + 3; ty = base - h
    for ang in (-160, -120, -60, -20, 20, 200):
        a = math.radians(ang); ex, ey = tx + 44 * math.cos(a), ty + 22 * math.sin(a) + 14
        d.polygon([(tx, ty), (ex, ey), ((tx + ex) / 2, (ty + ey) / 2 + 8)], fill=(46, 130, 60))

def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0:
        sea(d, (60, 30, 90), (250, 150, 70), 600, (40, 70, 120), (240, 160, 100)); d.ellipse((330, 540, 430, 640), fill=(255, 200, 90))
        sea_line = Image.new("RGBA", (CW, CH)); R(d, (0, 600, CW, CH), (40, 70, 120))
        rnd = random.Random(2)
        for _ in range(80): x, y = rnd.randint(0, CW), rnd.randint(606, CH); R(d, (x, y, x + 12, y + 1), (240, 160, 100))
        R(d, (0, 690, 250, CH), (120, 80, 46))
        for x in range(0, 250, 24): R(d, (x, 690, x + 1, CH), (90, 58, 30))
        R(d, (0, 690, 250, 694), (150, 104, 60))
    elif i in (1, 5, 6, 7):
        grad(d, (40, 30, 26), (90, 64, 44), 0, CH, 12)
        R(d, (0, GY, CW, CH), (70, 48, 30))
        for x in range(0, CW, 30): R(d, (x, GY, x + 1, CH), (54, 36, 22))
    elif i == 2 and li == 0:
        inca_wall(d, 0, 0, CW, GY, (150, 134, 110), (110, 96, 76), doors=())
        for bx in (60, 400):
            R(d, (bx, 120, bx + 80, 330), (190, 30, 40)); d.polygon([(bx, 330), (bx + 40, 360), (bx + 80, 330)], fill=(190, 30, 40))
            R(d, (bx + 24, 190, bx + 56, 250), GOLD); R(d, (bx + 20, 180, bx + 60, 190), GOLD)
            for k in range(4): R(d, (bx + 20 + k * 11, 172, bx + 26 + k * 11, 180), GOLD)
            R(d, (bx + 34, 226, bx + 46, 250), (120, 70, 20))
        R(d, (0, GY, CW, CH), (150, 30, 40)); R(d, (180, GY, 360, CH), (200, 40, 50))
        R(d, (330, 520, 470, GY), GOLD_D); R(d, (340, 470, 460, 530), (176, 30, 40)); R(d, (330, 460, 470, 474), GOLD)
    elif i == 2:
        sea(d, (70, 140, 230), (190, 220, 248), 560, (40, 96, 170), (190, 220, 250))
        for cx, cy in ((100, 200), (380, 140)):
            for dx, dy, r in ((0, 0, 22), (22, -8, 26), (46, 0, 20)): d.ellipse((cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r), fill=WHITE)
    elif i == 3:
        sea(d, (10, 14, 40), (60, 70, 120), 600, (20, 30, 70), (80, 100, 160))
        rnd = random.Random(4)
        for _ in range(60): x, y = rnd.randint(0, CW), rnd.randint(0, 500); R(d, (x, y, x, y), WHITE)
        d.ellipse((420, 120, 466, 166), fill=(236, 236, 214))
        d.polygon([(0, 600), (40, 584), (110, 578), (170, 590), (200, 600)], fill=(16, 22, 30))
    elif i == 4:
        sea(d, (80, 170, 240), (200, 230, 250), 560, (40, 170, 190), (200, 240, 240))
        R(d, (0, 640, CW, CH), (236, 214, 150)); d.polygon([(0, 640), (CW, 620), (CW, 640)], fill=(236, 214, 150))
        rnd = random.Random(8)
        for _ in range(90): x, y = rnd.randint(0, CW), rnd.randint(644, CH); R(d, (x, y, x + 1, y), (210, 186, 124))
        palm(d, 470, 650, 210, -1); palm(d, 20, 650, 170, 1)
    elif i == 8:
        grad(d, (20, 16, 50), (90, 50, 110), 0, CH, 12)
        rnd = random.Random(9)
        for _ in range(70): x, y = rnd.randint(0, CW), rnd.randint(0, 600); R(d, (x, y, x, y), WHITE)
        R(d, (0, GY, CW, CH), (50, 40, 70))
    return c

def waves(d, f, y0, col):
    for k in range(40):
        pr = random.Random(k); x = (pr.randint(0, CW) + f * pr.choice((1, 2))) % (CW + 20) - 10; y = pr.randint(y0 + 6, CH)
        R(d, (x, y, x + 8, y + 1), col)

def bob(f, amp=4, sp=0.12, ph=0): return int(amp * math.sin(f * sp + ph))

def bubble(d, text, cx, y, font=None):
    font = font or F16; w = d.textlength(text, font=font); h = 16 if font is F16 else 8
    R(d, (cx - w / 2 - 8, y - 8, cx + w / 2 + 7, y + h + 7), WHITE); d.rectangle((cx - w / 2 - 8, y - 8, cx + w / 2 + 7, y + h + 7), outline=K, width=2)
    d.polygon([(cx - 6, y + h + 7), (cx + 6, y + h + 7), (cx - 2, y + h + 18)], fill=WHITE)
    d.text((cx - w / 2, y), text, font=font, fill=K)

# ---------------- scenes ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        waves(d, f, 600, (240, 170, 110))
        for k, (x, y) in enumerate(((260, 640), (330, 610), (400, 625))):
            put(c, "ship" if k == 0 else tint(SP["ship"], 0.75), x - 60 + t * 3, y + bob(f, 3, 0.1, k), k=None)
        put(c, "col", 40, FEET, sc=2); label(d, "COLUMBUS", 92, 540, GOLD)
        if li == 1: bubble(d, "WELCOME TO... INDIA?", 190, 470)
    elif i == 1:
        am = 0.0 if li < 2 else min(1.0, lt / 0.8) if li == 2 else 1.0
        labs = [("SPAIN", -3, 44, WHITE, K), ("CANARIES", CANARY[0] + 4, CANARY[1] - 5, WHITE, K)]
        jp = None
        if li >= 1:
            jp = (-68, 31); labs.append(("JAPAN? (HIS GUESS)", -68, 39, K, YEL)); labs.append(("4,000 KM", -50, 24, WHITE, K))
        if li >= 2:
            labs.append(("UNKNOWN LAND", -58, 2, WHITE, RED_D)); labs.append(("REAL JAPAN: 20,000 KM", -55, 57, K, YEL))
        m = world_map(f, americas=am, japan=jp, labels=labs, route=((PALOS, CANARY, (-68, 31)), 1.0) if li >= 1 else None)
        c.alpha_composite(m, (25, 110))
        if li >= 2:
            R(d, (30, 140, 34, 150), YEL); d.polygon([(26, 160), (40, 160), (33, 172)], fill=YEL) if False else None
        put(c, "col", 218, FEET, sc=2)
        if li == 3:
            put(c, "dPT", 50, FEET, sc=2); put(c, "dES", 386, FEET, sc=2, flip=True)
            bubble(d, "WRONG MATH!", 112, 540); bubble(d, "WRONG MATH!", 430, 540)
    elif i == 2:
        if li == 0:
            put(c, "isa", 348, 690, sc=2); label(d, "QUEEN ISABELLA", 400, 500, GOLD)
            put(c, "col", 60, FEET, sc=2); label(d, "COLUMBUS", 112, 540, GOLD)
        else:
            waves(d, f, 560, (190, 220, 250))
            names = ["NIÑA", "PINTA", "SANTA MARÍA"]
            for k, (x, y) in enumerate(((30, 650), (190, 700), (330, 668))):
                xx = x + (t * 8) % 40 - 20 if li == 2 else x
                put(c, "ship", xx, y + bob(f, 4, 0.1, k * 2)); label(d, names[k], xx + 80, y - 150, GOLD)
            if li == 2:
                day = 1 + int(35 * prog); label(d, f"DAY {day}", 270, 230, WHITE, K, F16)
    elif i == 3:
        waves(d, f, 600, (80, 100, 160))
        sx, sy = 200, 760 + bob(f, 3, 0.08)
        big = put(c, "ship", sx, sy, sc=2)
        put(c, "sailor", sx + 104, sy - 238, crop=60)
        if (f // 15) % 2 and li >= 0: R(d, (88, 574, 92, 578), (255, 240, 160))
        if li == 0: bubble(d, "LAND!", sx + 150, sy - 300); label(d, "RODRIGO DE TRIANA", sx + 130, sy - 330 - 20, GOLD)
        if li >= 1:
            label(d, "REWARD: LIFETIME PENSION", 270, 210, K, GOLD)
        if li == 2:
            put(c, "col", sx + 60, sy - 70); bubble(d, "I SAW A LIGHT FIRST!", 270, 300)
            label(d, "PENSION -> COLUMBUS", 270, 250, WHITE, RED)
    elif i == 4:
        waves(d, f, 560, (200, 240, 240))
        put(c, "ship", 300, 610 + bob(f, 3, 0.1), k=0.85)
        R(d, (148, 520, 150, 740), BROWN_D); R(d, (150, 520, 200, 556), WHITE); R(d, (166, 524, 172, 552), (30, 110, 60)); R(d, (156, 535, 194, 541), (30, 110, 60))
        put(c, "col", 80, FEET + 4); put(c, "esp0", 30, FEET - 10, k=0.85)
        label(d, "COLUMBUS", 106, 640, GOLD)
        for k, x in enumerate((320, 380, 440)): put(c, f"tai{(k + (f // 20)) % 2 if k < 2 else 2}", x, FEET + (k % 2) * 6, flip=True)
        label(d, "TAÍNO PEOPLE", 410, 640, GOLD)
        if li == 0: bubble(d, "HELLO, INDIANS!", 140, 560)
        else:
            bubble(d, "THIS IS ASIA.", 130, 560)
            if prog > 0.5: label(d, "DIED 1506, STILL SURE", 270, 230, WHITE, RED_D)
    elif i == 5:
        labs = [("SPAIN", 6, 41, WHITE, K), ("PORTUGAL", -14, 50, WHITE, K)]
        line = None; tint_on = False
        if li == 1: line = (-38, prog)
        if li == 2: line = (-38, 1.0); tint_on = True; labs += [("SPAIN", -62, -12, WHITE, RED_D), ("PORTUGAL", 12, -10, WHITE, (26, 86, 50))]
        if li >= 1: labs.append(("1493 LINE", -38, 50, K, YEL))
        m = world_map(f, line=line, tint=tint_on, labels=labs, title="BULL INTER CAETERA, 1493" if li >= 1 else None)
        c.alpha_composite(m, (25, 110))
        if li == 0:
            put(c, "dES", 100, FEET, sc=2); put(c, "dPT", 336, FEET, sc=2, flip=True)
            label(d, "SPAIN", 152, 540, WHITE, RED_D); label(d, "PORTUGAL", 388, 540, WHITE, (26, 86, 50))
        else:
            put(c, "pope", 218, FEET, sc=2)
            label(d, "POPE ALEXANDER VI", 270, 540, GOLD)
    elif i == 6:
        lon = -38 + (-46.5 + 38) * (min(1, prog * 1.4) if li == 0 else 1)
        labs = [("1494 LINE", lon, 50, K, YEL)]
        if li == 1: labs.append(("BRAZIL", -44, -8, WHITE, (26, 86, 50)))
        m = world_map(f, line=(lon, 1.0), oldline=-38, tint=True, labels=labs, title="TREATY OF TORDESILLAS, 1494")
        c.alpha_composite(m, (25, 110))
        put(c, "dES", 90, FEET, sc=2); put(c, "dPT", 346, FEET, sc=2, flip=True)
        R(d, (206, 640, 334, 680), (240, 226, 180)); d.rectangle((206, 640, 334, 680), outline=BROWN_D, width=2)
        d.text((270, 660), "TREATY", font=F8, fill=K, anchor="mm")
        label(d, "SPAIN", 142, 540, WHITE, RED_D); label(d, "PORTUGAL", 398, 540, WHITE, (26, 86, 50))
    elif i == 7:
        m = world_map(f, parch=True, america_text=(li == 1 and (prog > 0.45)), labels=[("MUNDUS NOVUS", -60, 35, WHITE, BROWN)] if li == 0 else [],
                      title="WALDSEEMÜLLER MAP, 1507" if li == 1 else None)
        c.alpha_composite(m, (25, 110))
        put(c, "vesp", 40, FEET, sc=2); label(d, "AMERIGO VESPUCCI", 150, 538, GOLD)
        if li == 0: bubble(d, "A NEW WORLD!", 360, 580)
    elif i == 8:
        if li == 0:
            put(c, "col", 40, FEET, sc=2); put(c, "vesp", 396, FEET, sc=2)
            label(d, "COLUMBUS", 92, 530, GOLD); label(d, "AMERIGO", 448, 530, GOLD)
            label(d, "FOUND IT", 92, 300, K, YEL, F16); label(d, "GOT THE NAME", 430, 300, K, YEL, F16)
        else:
            c.alpha_composite(world_map(f, parch=True, america_text=True, title="THE NEW MAP OF THE WORLD"), (25, 110))
            put(c, "col", 40, FEET, sc=2); put(c, "vesp", 396, FEET, sc=2)
            label(d, "COLUMBUS", 92, 540, GOLD); label(d, "AMERIGO", 448, 540, GOLD)
            if prog > 0.4: label(d, "FOLLOW FOR MORE HISTORY", 270, 620, WHITE, RED, F16)

def overlay(head, cap):
    o = Image.new("RGBA", (FW, FH)); d = ImageDraw.Draw(o)
    for size in (64, 56, 48, 40):
        fh = ImageFont.truetype(FONT, size)
        if d.textlength(head, font=fh) <= FW - 80: break
    d.text((FW // 2 + 8, 168), head, font=fh, fill=K, anchor="mm"); d.text((FW // 2, 160), head, font=fh, fill=GOLD, anchor="mm")
    d.rectangle([40, 1500, 1040, 1860], fill=(0, 0, 0)); d.rectangle([40, 1500, 1040, 1860], outline=WHITE, width=8)
    d.rectangle([56, 1516, 1024, 1844], outline=(120, 120, 120), width=4)
    fc = ImageFont.truetype(FONT, 38); lines = textwrap.wrap(cap, 23); y = 1680 - (len(lines) - 1) * 29
    for ln in lines: d.text((FW // 2, y), ln, font=fc, fill=WHITE, anchor="mm"); y += 58
    return o

def compose(i, li, f, t, lt, ldur, sdur, bg, ov):
    c = bg.copy(); d = ImageDraw.Draw(c)
    draw_scene(i, c, d, f, t, li, lt, ldur, sdur)
    big = c.resize((FW, FH), Image.NEAREST); big.alpha_composite(ov); return big.convert("RGB")

# ---------------- music: Spanish renaissance chiptune (3/4, D minor) ----------------
def music(total, path, sr=44100):
    N = {"A4": 440, "Bb4": 466.16, "C#5": 554.37, "D5": 587.33, "E5": 659.25, "F5": 698.46, "G5": 783.99, "A5": 880, "G4": 392, "F4": 349.23}
    pA = [("D5", 2), ("E5", 1), ("F5", 1.5), ("E5", .5), ("D5", 1), ("C#5", 2), ("A4", 1), ("D5", 3),
          ("F5", 2), ("G5", 1), ("A5", 1.5), ("G5", .5), ("F5", 1), ("E5", 2), ("C#5", 1), ("D5", 3)]
    pB = [("A5", 2), ("G5", 1), ("F5", 2), ("E5", 1), ("D5", 2), ("Bb4", 1), ("A4", 3),
          ("Bb4", 2), ("C#5", 1), ("D5", 1.5), ("E5", .5), ("F5", 1), ("E5", 2), ("C#5", 1), ("D5", 3)]
    q = 60 / 104; n = int(total * sr); out = np.zeros(n); pos = 0.0; ph = 0
    while pos < total:
        for nm, ln in (pA if ph % 2 == 0 else pB):
            dur = ln * q; s0, s1 = int(pos * sr), min(n, int((pos + dur) * sr))
            if s0 >= n: break
            tt = np.arange(s1 - s0) / sr; fr = N[nm] * (1 + 0.004 * np.sin(2 * np.pi * 5.5 * tt))
            sq = np.where((np.cumsum(fr) / sr) % 1 < 0.25, 1.0, -1.0) * np.minimum(1, tt * 60) * np.exp(-tt * 1.6)
            out[s0:s1] += 0.2 * sq; pos += dur
        ph += 1
    roots = [146.83, 110, 146.83, 110, 116.54, 130.81, 110, 146.83]
    bar = 0; pos = 0.0
    while pos < total:
        r = roots[bar % 8]
        for b in range(3):
            s0, s1 = int(pos * sr), min(n, int((pos + q) * sr))
            if s0 >= n: break
            tt = np.arange(s1 - s0) / sr
            fr = r if b == 0 else r * 1.5
            out[s0:s1] += (0.3 if b == 0 else 0.16) * (2 * np.abs(2 * ((tt * fr) % 1) - 1) - 1) * np.exp(-tt * 2.5)
            if b == 0: out[s0:s1] += 0.35 * np.sin(2 * np.pi * 58 * tt) * np.exp(-tt * 22)
            else: out[s0:s1] += 0.07 * np.random.default_rng(bar * 3 + b).uniform(-1, 1, s1 - s0) * np.exp(-tt * 40)
            pos += q
        bar += 1
    fade = int(2.5 * sr); out[-fade:] *= np.linspace(1, 0, fade); out[:int(0.5 * sr)] *= np.linspace(0, 1, int(0.5 * sr))
    out = (out / np.max(np.abs(out)) * 0.8 * 32767).astype(np.int16)
    with wave.open(path, "w") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(out.tobytes())

def wavdur(p):
    with wave.open(p) as w: return w.getnframes() / w.getframerate()

def tts(text, path):
    subprocess.run(["python3", "-m", "piper", "-m", VOICE, "-f", path, "--length_scale", "0.88", "--sentence_silence", "0.15"],
                   input=text.encode(), check=True, capture_output=True)

# ---------------- render ----------------
if CHECK:
    for i, (head, lines) in enumerate(SCENES):
        for li in range(len(lines)):
            compose(i, li, 40, 2.0, 2.4, 3.0, 8.0, make_bg(i, li), overlay(head, lines[li][1])).save(f"{OUT}/check{i}_{li}.png")
    sys.exit()

audios, clips, total = [], [], 0.0
for i, (head, lines) in enumerate(SCENES):
    ldurs = []
    for li, (spoken, cap) in enumerate(lines):
        raw = f"{OUT}/a{i}_{li}.wav"; pad = f"{OUT}/p{i}_{li}.wav"
        if EXT_AUDIO: raw = f"{EXT_AUDIO}/{i}_{li}.wav"
        else: tts(spoken, raw)
        gap = 0.55 if li == len(lines) - 1 else 0.3
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", raw, "-af", f"aresample=44100,apad=pad_dur={gap}", "-ac", "1", pad], check=True)
        dur = round(wavdur(pad) * FPS) / FPS
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", pad, "-t", f"{dur:.4f}", "-af", f"apad=whole_dur={dur:.4f}", f"{pad}.fit.wav"], check=True)
        audios.append(f"{pad}.fit.wav"); ldurs.append(dur)
    sdur = sum(ldurs); total += sdur
    bgs = [make_bg(i, li) for li in range(len(lines))]; ovs = [overlay(head, cap) for _, cap in lines]
    tmp, fin = f"{OUT}/s{i}.tmp.mp4", f"{OUT}/s{i}.mp4"
    if os.path.exists(fin) and not os.environ.get("REDO"): clips.append(fin); continue
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{FW}x{FH}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
    for f in range(int(round(sdur * FPS))):
        t = f / FPS; li, acc = 0, 0.0
        while li < len(ldurs) - 1 and t >= acc + ldurs[li]: acc += ldurs[li]; li += 1
        img = compose(i, li, f, t, t - acc, ldurs[li], sdur, bgs[li], ovs[li])
        if t < 0.25: img = Image.blend(Image.new("RGB", (FW, FH)), img, t / 0.25)
        p.stdin.write(img.tobytes())
    p.stdin.close(); assert p.wait() == 0; os.rename(tmp, fin); clips.append(fin); print("scene", i, round(sdur, 1), flush=True)

open(f"{OUT}/v.txt", "w").write("".join(f"file '{c}'\n" for c in clips))
open(f"{OUT}/a.txt", "w").write("".join(f"file '{a}'\n" for a in audios))
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/v.txt", "-c", "copy", f"{OUT}/video.mp4"], check=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/a.txt", "-c:a", "pcm_s16le", f"{OUT}/voice.wav"], check=True)
music(total, f"{OUT}/music.wav")
final = f"{D}/ep02_columbus_EN.mp4"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{OUT}/video.mp4", "-i", f"{OUT}/voice.wav", "-i", f"{OUT}/music.wav",
                "-filter_complex", "[1:a]volume=-3dB[v];[2:a]volume=0.12[m];[v][m]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.89:level=disabled[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", final], check=True)
print("total", round(total, 1))
