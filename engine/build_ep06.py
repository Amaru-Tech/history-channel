import os, sys
D = os.environ.get("HC_DIR", os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")
_src = open(f"{D}/build4.py").read().split("# ---------------- render ----------------")[0]
sys_argv_backup = list(sys.argv); sys.argv = [sys.argv[0]]
exec(_src)  # engine, sprites, maps, overlay, compose, music, tts from episode 1
_src5 = open(f"{D}/build5.py").read().split("# ---------------- extra sprites ----------------")[1].split("# ---------------- backgrounds ----------------")[0]
exec(_src5)  # episode 2 sprites: Taino chiefs, sleeper, Caribbean map, fort, canoe, reef
_src6 = open(f"{D}/build_ep03.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- backgrounds ----------------")[0]
exec(_src6)  # episode 3 sprites: pig, friar, sack, sugarcane, huts, church, stone house, rain
_src7 = open(f"{D}/build_ep04.py").read().split("# ---------------- extra sprites: crops and animals ----------------")[1].split("# ---------------- backgrounds ----------------")[0]
exec(_src7)  # episode 4 sprites: crop icons (c_*), cow, chicken, farmers
_src8 = open(f"{D}/build_ep05.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- backgrounds ----------------")[0]
exec(_src8)  # episode 5: Bobadilla, Ferdinand, Ovando, settlers, baskets, region_map, props (torch, clouds, gulls, town, dock...)
sys.argv = sys_argv_backup
CHECK = "check" in sys.argv
OUT = f"{D}/out_ep06"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep06_words_from_the_taino_EN.mp4"

SCENES = [
 ("WORDS THEY GAVE US", [
  ("Hurricane. Canoe. Hammock. Barbecue.", "Hurricane. Canoe. Hammock. Barbecue."),
  ("All four words come from the Tyeeno, the people Columbus met in fourteen ninety-two.", "All four words come from the Taíno, the people Columbus met in 1492.")]),
 ("THE TAÍNO", [
  ("The Tyeeno lived across the Bahamas, Cuba, Hispaniola, Puerto Rico and Jamaica.", "The Taíno lived across the Bahamas, Cuba, Hispaniola, Puerto Rico and Jamaica."),
  ("Their villages were led by chiefs called kah-seeks, both men and women.", "Their villages were led by chiefs called caciques, both men and women."),
  ("They grew cassava, played a sacred ball game called bah-tay, and honored spirits called seh-mees.", "They grew cassava, played a sacred ball game called batey, and honored spirits called zemís.")]),
 ("BOATS AND BEDS", [
  ("Columbus saw their dugout boats, called canoa. English made it canoe.", "Columbus saw their dugout boats, called canoa. English made it canoe."),
  ("Their hanging net beds, hamaca, became the hammock.", "Their hanging net beds, hamaca, became the hammock.")]),
 ("STORMS AND SMOKE", [
  ("Hoo-rah-kahn, their word for the great storms, became hurricane.", "Hurakán, their word for the great storms, became hurricane."),
  ("Barbacoa was a raised wooden frame for cooking or storing food. It gave us barbecue.", "Barbacoa was a raised wooden frame for cooking or storing food. It gave us barbecue."),
  ("And tabaco, possibly their name for a smoking pipe, became tobacco.", "And tabaco, possibly their name for a smoking pipe, became tobacco.")]),
 ("THE ENCOMIENDA", [
  ("In fifteen oh two, Governor Ovando set up the encomienda on Hispaniola.", "In 1502, Governor Ovando set up the encomienda on Hispaniola."),
  ("Spanish settlers received Tyeeno workers. In return, they had to teach them the Christian faith.", "Spanish settlers received Taíno workers. In return, they had to teach them the Christian faith."),
  ("In practice, it was forced labor.", "In practice, it was forced labor.")]),
 ("THE COLLAPSE", [
  ("In fifteen oh eight, a Spanish count found about sixty thousand Tyeeno on Hispaniola.", "In 1508, a Spanish count found about 60,000 Taíno on Hispaniola."),
  ("By fifteen fourteen, about twenty-six thousand. Then smallpox struck in fifteen eighteen.", "By 1514, about 26,000. Then smallpox struck in 1518."),
  ("By fifteen forty-two, only about two thousand were left.", "By 1542, only about 2,000 were left.")]),
 ("STILL HERE", [
  ("But the Tyeeno did not fully vanish. In twenty eighteen, scientists read DNA from an ancient tooth found in the Bahamas.", "But the Taíno did not fully vanish. In 2018, scientists read DNA from an ancient tooth found in the Bahamas."),
  ("The Native ancestry of modern Puerto Ricans matched her people more closely than any other.", "The Native ancestry of modern Puerto Ricans matched her people more closely than any other.")]),
 ("THEIR WORDS LIVE ON", [
  ("Their world was shattered. But every hurricane still carries their word.", "Their world was shattered. But every hurricane still carries their word.")]),
]

_label_orig = label
def label(d, text, cx, y, fg=WHITE, bg=K, font=F16):
    w = d.textlength(text, font=font); cx = min(max(cx, w / 2 + 8), CW - w / 2 - 8)
    _label_orig(d, text, cx, y, fg, bg, font)

# ---------------- extra sprites ----------------
def cacica():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    for x0, x1 in [(20, 23), (29, 32)]: R(d, (x0, 66, x1, 81), SKIN_T)
    R(d, (17, 36, 35, 58), SKIN_T); R(d, (31, 36, 35, 58), SKIN_TD)
    R(d, (15, 56, 37, 68), WHITE); R(d, (15, 60, 37, 61), (200, 50, 30))  # nagua skirt
    R(d, (12, 37, 16, 56), SKIN_T); R(d, (36, 37, 40, 56), SKIN_TD)
    for x in range(18, 35, 4): R(d, (x, 37, x + 2, 39), GOLD)
    d.ellipse((22, 41, 30, 49), fill=GOLD); d.ellipse((24, 43, 28, 47), fill=GOLD_D)
    face(d, SKIN_T, SKIN_TD); R(d, (16, 12, 36, 20), HAIR); R(d, (15, 20, 19, 46), HAIR); R(d, (33, 20, 37, 46), HAIR)
    R(d, (17, 12, 35, 15), GOLD)
    for k, x in enumerate(range(19, 34, 5)): R(d, (x, 4, x + 2, 12), [(40, 140, 90), WHITE, (200, 50, 30)][k % 3])
    return outline(im)

def modern(shirt=(60, 130, 200), skin=(190, 140, 100), hair=(40, 28, 20), long_hair=False):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    for x0, x1 in [(20, 23), (29, 32)]: R(d, (x0, 62, x1, 78), (50, 70, 120)); R(d, (x0 - 1, 77, x1 + 1, 81), WHITE)
    R(d, (16, 36, 36, 62), shirt); R(d, (16, 58, 36, 64), (50, 70, 120))
    R(d, (11, 37, 16, 46), shirt); R(d, (36, 37, 41, 46), shirt); R(d, (11, 46, 15, 54), skin); R(d, (37, 46, 41, 54), skin)
    face(d, skin, tuple(int(v * 0.8) for v in skin)); R(d, (17, 12, 35, 18), hair)
    if long_hair: R(d, (16, 18, 19, 40), hair); R(d, (33, 18, 36, 40), hair)
    return outline(im)

def zemi():
    im = Image.new("RGBA", (56, 40)); d = ImageDraw.Draw(im)
    d.polygon([(2, 36), (14, 20), (28, 2), (42, 20), (54, 36)], fill=(150, 140, 120))
    d.polygon([(10, 36), (20, 22), (28, 10), (36, 22), (46, 36)], fill=(170, 160, 140))
    d.ellipse((6, 24, 16, 34), fill=(130, 120, 100)); R(d, (9, 27, 11, 29), K)  # face on the front point
    R(d, (24, 20, 26, 22), K); R(d, (30, 20, 32, 22), K); R(d, (25, 27, 31, 28), K)
    return outline(im)

def tooth():
    im = Image.new("RGBA", (40, 50)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((4, 2, 36, 26), 8, fill=(240, 236, 214))
    d.polygon([(6, 20), (34, 20), (30, 46), (24, 46), (20, 30), (16, 46), (10, 46)], fill=(240, 236, 214))
    R(d, (10, 6, 14, 12), WHITE)
    return outline(im)

SP.update({"cacica": cacica(), "zemi": zemi(), "tooth": tooth(),
           "pr1": modern((200, 50, 60)), "pr2": modern((60, 130, 200), (170, 120, 84), long_hair=True), "pr3": modern((240, 190, 50), (150, 104, 70))})

def lying_taino():
    return SP["tai2"].rotate(90, resample=Image.NEAREST, expand=True)
SP["lie"] = lying_taino()

# ---------------- props ----------------
def word_card(d, old, new, cx, y, show=1.0):
    label(d, old, cx, y, K, YEL, F16)
    if show > 0.35:
        d.text((cx, y + 34), "↓", font=F16, fill=WHITE, anchor="mm"); R(d, (cx - 1, y + 22, cx + 1, y + 28), WHITE)
        label(d, new, cx, y + 48, WHITE, RED_D, F16)

def swirl(d, cx, cy, r, f, col=(230, 234, 240), w=4):
    for k in range(3):
        a0 = f * 6 + k * 120
        d.arc((cx - r, cy - r, cx + r, cy + r), a0, a0 + 80, fill=col, width=w)
        d.arc((cx - r * 0.6, cy - r * 0.6, cx + r * 0.6, cy + r * 0.6), a0 + 40, a0 + 110, fill=col, width=w)
    d.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), fill=col)

def bent_palm(d, x, base, h, f, wind=1.0):
    lean = 1 + int(wind * (2 + math.sin(f * 0.3)))
    palm(d, x, base, h, lean)

def hammock(c, d, x0, x1, y, f, who=True):
    sag = 34 + bob(f, 3, 0.1)
    pts = [(x0 + (x1 - x0) * k / 16, y + sag * math.sin(math.pi * k / 16)) for k in range(17)]
    for off, col in ((0, (200, 60, 50)), (5, (240, 200, 80)), (10, (60, 120, 170))):
        d.line([(px, py + off) for px, py in pts], fill=col, width=5)
    for k in range(0, 17, 2):
        px, py = pts[k]; d.line([(px, py), (px, py + 12)], fill=(150, 110, 60), width=1)
    d.line([(x0 - 14, y - 10), (x0, y)], fill=(150, 110, 60), width=2); d.line([(x1 + 14, y - 10), (x1, y)], fill=(150, 110, 60), width=2)
    if who: c.alpha_composite(SP["lie"], (int((x0 + x1) / 2 - 42), int(y + sag - 40)))

def barbacoa(d, x, base, f, meat=True):
    for px in (x, x + 140):
        R(d, (px, base - 90, px + 6, base), BROWN_D)
    for k in range(9): R(d, (x - 4, base - 92 + (k % 2), x + 150, base - 90 + (k % 2)), BROWN) if k == 0 else R(d, (x + k * 16, base - 94, x + k * 16 + 3, base - 86), (150, 104, 60))
    R(d, (x - 4, base - 90, x + 150, base - 86), BROWN)
    if meat:
        for k in range(4):
            d.ellipse((x + 12 + k * 32, base - 106, x + 36 + k * 32, base - 92), fill=(170, 80, 50)); R(d, (x + 18 + k * 32, base - 102, x + 26 + k * 32, base - 100), (210, 120, 80))
    bonfire(d, x + 74, base, f)
    for k in range(4):
        ph = ((f * 0.8 + k * 25) % 100) / 100; r = int(5 + ph * 14)
        d.ellipse((x + 70 - r + int(math.sin(ph * 6 + k) * 10), base - 110 - ph * 140 - r, x + 70 + r + int(math.sin(ph * 6 + k) * 10), base - 110 - ph * 140 + r), fill=(200, 200, 204))

def pipe(d, x, y):
    d.line([(x, y + 40), (x + 18, y + 8)], fill=(150, 104, 60), width=4); d.line([(x + 36, y + 40), (x + 18, y + 8)], fill=(150, 104, 60), width=4)
    d.line([(x + 18, y + 8), (x + 18, y - 10)], fill=(150, 104, 60), width=4)
    for k in range(3): d.ellipse((x + 12 + k * 6 - 4, y - 18 - k * 14 - 4, x + 12 + k * 6 + 4 + k * 2, y - 18 - k * 14 + 4 + k * 2), fill=(210, 210, 214))

def conuco(d, x, base, n=3):
    for k in range(n):
        cx = x + k * 54
        d.ellipse((cx, base - 22, cx + 46, base + 6), fill=(130, 90, 50))
        for j in (-10, 0, 10):
            R(d, (cx + 22 + j // 3, base - 46, cx + 24 + j // 3, base - 16), (120, 90, 50))
            for a in (-40, 0, 40):
                ex = cx + 23 + j + int(math.sin(math.radians(a)) * 12); d.line([(cx + 23 + j // 3, base - 44), (ex, base - 56)], fill=(70, 150, 60), width=3)

def batey(d, c, x, y, f):
    R(d, (x, y, x + 230, y + 70), (214, 190, 140))
    for k in range(0, 230, 18): R(d, (x + k, y - 8, x + k + 12, y), (150, 146, 136)); R(d, (x + k, y + 70, x + k + 12, y + 78), (150, 146, 136))
    put(c, f"tai{st(f, 0, 7)}", x + 6, y + 64); put(c, f"tai{st(f, 1, 7)}", x + 176, y + 64, flip=True)
    ph = (f % 40) / 40; bx = x + 50 + (130 * ph if (f // 40) % 2 == 0 else 130 * (1 - ph)); by = y + 10 - math.sin(ph * math.pi) * 60
    d.ellipse((bx - 7, by - 7, bx + 7, by + 7), fill=K); d.ellipse((bx - 4, by - 5, bx, by - 1), fill=(90, 90, 90))

def bars(d, x, y, vals, shown, prog, maxv=60000):
    R(d, (x, y, x + 460, y + 330), (236, 222, 180)); d.rectangle((x, y, x + 460, y + 330), outline=BROWN_D, width=4)
    R(d, (x + 30, y + 280, x + 440, y + 283), K)
    for k, (yr, v, txt) in enumerate(vals):
        if k >= shown: break
        grow = 1.0 if k < shown - 1 else min(1, prog * 2.2)
        hgt = max(4, int(220 * v / maxv * grow)); bx = x + 50 + k * 135
        R(d, (bx, y + 280 - hgt, bx + 90, y + 280), RED if k else (160, 60, 50)); d.rectangle((bx, y + 280 - hgt, bx + 90, y + 280), outline=K, width=2)
        d.text((bx + 45, y + 302), yr, font=F16, fill=K, anchor="mm")
        if grow >= 1: d.text((bx + 45, y + 280 - hgt - 16), txt, font=F16, fill=K, anchor="mm")

def helix(d, cx, y0, h, f, cols=((200, 60, 60), (60, 120, 200))):
    for k in range(0, h, 8):
        ph = k * 0.07 + f * 0.12; dx = math.sin(ph) * 34
        R(d, (cx + dx - 4, y0 + k, cx + dx + 4, y0 + k + 4), cols[0]); R(d, (cx - dx - 4, y0 + k, cx - dx + 4, y0 + k + 4), cols[1])
        if k % 16 == 0: d.line([(cx + dx, y0 + k + 2), (cx - dx, y0 + k + 2)], fill=(220, 220, 220), width=1)

def cave(d, x, base):
    d.polygon([(x, base), (x + 20, base - 170), (x + 120, base - 210), (x + 240, base - 160), (x + 270, base)], fill=(120, 110, 100))
    d.polygon([(x + 70, base), (x + 90, base - 100), (x + 140, base - 120), (x + 190, base - 90), (x + 200, base)], fill=(40, 34, 32))

# ---------------- maps ----------------
ELEUTHERA = (-76.2, 25.0); PR_PT = (-66.4, 18.2)
TAINO_BOX = (-85, -62, 16, 27.5)

# ---------------- backgrounds ----------------
def day_sea(d, horizon=600):
    sea(d, (80, 160, 230), (200, 225, 250), horizon, (40, 110, 170), (200, 230, 250))

def beach(d, sky="day", horizon=560):
    if sky == "sunset": sea(d, (250, 150, 90), (250, 210, 150), horizon, (40, 110, 170), (240, 200, 160))
    elif sky == "storm": sea(d, (30, 34, 44), (70, 76, 90), horizon, (30, 50, 64), (110, 120, 130))
    else: sea(d, (80, 170, 240), (200, 230, 250), horizon, (40, 150, 190), (200, 240, 240))
    sand = (150, 140, 110) if sky == "storm" else (236, 214, 150)
    d.polygon([(0, 690), (CW, 650), (CW, CH), (0, CH)], fill=sand)
    rnd = random.Random(8)
    for _ in range(60):
        x, y = rnd.randint(0, CW), rnd.randint(700, CH); R(d, (x, y, x + 1, y), (210, 186, 124) if sky != "storm" else (120, 110, 90))

def jungle_village(d, dusk=False):
    if dusk: grad(d, (40, 30, 60), (200, 110, 80), 0, 620, 12)
    else: grad(d, (80, 170, 240), (200, 230, 250), 0, 620, 12)
    for k in range(9):
        x = k * 66 - 20; d.ellipse((x, 470, x + 110, 640), fill=(40, 110, 60) if not dusk else (30, 60, 40))
    R(d, (0, 620, CW, CH), (170, 150, 96) if not dusk else (110, 96, 70))
    rnd = random.Random(6)
    for _ in range(80): x, y = rnd.randint(0, CW), rnd.randint(624, CH); R(d, (x, y, x + 2, y), (140, 120, 70))

def colony(d):
    grad(d, (80, 160, 230), (200, 225, 250), 0, 600, 12)
    R(d, (0, 600, CW, CH), (196, 176, 120)); town(d, 600, 0, CW)
    rnd = random.Random(8)
    for _ in range(60): x, y = rnd.randint(0, CW), rnd.randint(612, CH); R(d, (x, y, x + 1, y), (170, 150, 100))

def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0:
        if li == 0: beach(d); palm(d, 470, 660, 200, -1); palm(d, 30, 690, 170, 1)
        else: beach(d); palm(d, 500, 650, 190, -1)
    elif i == 1:
        if li == 0: day_sea(d, 600)
        else: jungle_village(d, dusk=(li == 1))
    elif i == 2:
        if li == 0: beach(d)
        else: beach(d, "sunset"); palm(d, 40, 690, 260, 1); palm(d, 470, 655, 260, -1)
    elif i == 3:
        if li == 0: beach(d, "storm")
        elif li == 1: jungle_village(d, dusk=True)
        else: jungle_village(d)
    elif i == 4:
        if li == 2:
            jungle_village(d); R(d, (0, 690, CW, 720), (60, 140, 190))
        else: colony(d)
    elif i == 5:
        jungle_village(d, dusk=True)
    elif i == 6:
        if li == 0: day_sea(d, 600); R(d, (0, 690, CW, CH), (236, 214, 150))
        else: day_sea(d, 600); R(d, (0, 690, CW, CH), (200, 190, 170))
    elif i == 7:
        beach(d, "sunset"); palm(d, 470, 655, 210, -1); palm(d, 20, 690, 160, 1)
    return c

# ---------------- scenes ----------------
def taino_map(f, labels, title, dots=(), route=None, h=380):
    return region_map(f, TAINO_BOX, h=h, labels=labels, title=title, dots=dots, route=route)

def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        if li == 0:
            clouds(d, f, 130); gulls(d, f, 3, 320)
            waves(d, f, 560, (200, 240, 240)); canoe(c, d, 60 + prog * 200, 640 + bob(f, 3, 0.1), f)
            words = [("HURRICANE", 140, 250), ("CANOE", 400, 250), ("HAMMOCK", 140, 400), ("BARBECUE", 400, 400)]
            for k, (w, x, y) in enumerate(words):
                if prog > k * 0.2: label(d, w, x, y, K, YEL, F16)
            if prog > 0.0: swirl(d, 140, 320, 26, f, (90, 110, 150))
            if prog > 0.2:
                d.polygon([(350, 316), (450, 316), (440, 330), (360, 330)], fill=(120, 74, 38))
            if prog > 0.4: d.arc((90, 420, 190, 480), 10, 170, fill=(200, 60, 50), width=6)
            if prog > 0.6:
                R(d, (350, 470, 450, 474), BROWN); R(d, (354, 474, 358, 500), BROWN_D); R(d, (442, 474, 446, 500), BROWN_D)
                bonfire(d, 400, 500, f)
            label(d, "CANOE", 160 + prog * 200, 590, GOLD)
        else:
            clouds(d, f, 140, seed=3); waves(d, f, 560, (200, 240, 240))
            put(c, "ship", 330, 600 + bob(f, 3, 0.1), k=0.9); label(d, "COLUMBUS'S SHIP", 400, 450, WHITE, K)
            for k in range(3): hut(d, 10 + k * 80, 690, 54)
            put(c, "guaca", 20, FEET, sc=2); put(c, "cacica", 130, FEET, sc=2)
            put(c, "tai0", 260, FEET); put(c, "tai1", 310, FEET, flip=True); put(c, "tai2", 360, FEET)
            label(d, "TAÍNO", 182, 545, GOLD); label(d, "TAÍNO", 330, 630, GOLD)
            label(d, "1492", 270, 250, K, YEL, F16)
    elif i == 1:
        if li == 0:
            c.alpha_composite(taino_map(f, [("BAHAMAS", -79.5, 25.8, K, YEL), ("CUBA", -80, 22.0, K, YEL), ("HISPANIOLA", -71.5, 17.2, K, YEL),
                                            ("PUERTO RICO", -64.5, 20.6, K, YEL), ("JAMAICA", -81.5, 18.6, K, YEL)],
                                        "TAÍNO HOMELANDS", dots=[(-71, 19), (-80, 22.4), (-77.2, 18.2), (-66.4, 18.2), (-77.5, 24.6)]), (25, 110))
            waves(d, f, 600, (200, 230, 250)); gulls(d, f, 3, 520)
            canoe(c, d, 40 + prog * 180, 690 + bob(f, 3, 0.1), f); label(d, "TAÍNO CANOE", 100 + prog * 180, 600, GOLD)
            for k in range(3): palm(d, 380 + k * 50, 720, 60 + k * 10, -1)
            R(d, (360, 710, CW, CH), (236, 214, 150))
        elif li == 1:
            for k in range(4): hut(d, 20 + k * 130, 640, 70)
            bonfire(d, 270, 720, f)
            put(c, "guaca", 40, FEET, sc=2); label(d, "CACIQUE", 92, 545, GOLD)
            put(c, "cacica", 380, FEET, sc=2, flip=True); label(d, "CACICA", 432, 545, GOLD)
            for k in range(3): put(c, f"tai{st(f, k, 9)}", 180 + k * 40, FEET - 10 + (k % 2) * 8)
            label(d, "TAÍNO VILLAGE", 270, 250, K, YEL, F16)
            label(d, "MEN AND WOMEN RULED", 270, 290, WHITE, K, F16)
        else:
            conuco(d, 10, 700, 3); put(c, f"tai{st(f, 0, 10)}", 60, FEET); label(d, "CASSAVA", 90, 560, GOLD)
            batey(d, c, 290, 370, f); label(d, "BATEY", 405, 330, GOLD)
            R(d, (60, 400, 140, 470), (120, 100, 80)); put(c, "zemi", 72, 402); label(d, "ZEMÍ", 100, 320, GOLD)
            hut(d, 440, 650, 70); put(c, "cacica", 300, FEET, flip=True)
            for k in range(3): put(c, "c_maize" if k == 1 else "c_tobacco", 200 + k * 30, 640)
    elif i == 2:
        if li == 0:
            clouds(d, f, 140); gulls(d, f, 3, 300)
            waves(d, f, 560, (200, 240, 240))
            put(c, "ship", 340, 600 + bob(f, 3, 0.1), k=0.85)
            rowboat(c, d, 360, 640 + bob(f, 3, 0.1), f); label(d, "COLUMBUS", 410, 560, GOLD)
            for k in range(2): canoe(c, d, 20 + k * 30 + prog * 80, 640 + k * 50 + bob(f, 3, 0.1, k), f, k)
            label(d, "DUGOUT CANOES", 120, 530, WHITE, K)
            word_card(d, "CANOA", "CANOE", 270, 240, prog * 1.5)
        else:
            hammock(c, d, 100, 440, 520, f)
            label(d, "TAÍNO", 270, 640, GOLD); label(d, "HAMMOCK", 270, 460, WHITE, K)
            word_card(d, "HAMACA", "HAMMOCK", 270, 240, prog * 1.5)
            gulls(d, f, 2, 380, (80, 50, 50))
    elif i == 3:
        if li == 0:
            flash = lightning(d, f, 400); rain(d, f)
            swirl(d, 270, 420, 90, f); swirl(d, 270, 420, 50, -f, (190, 196, 210), 3)
            for k, x in enumerate((20, 140, 420)): bent_palm(d, x, 690 + k * 6, 120 + k * 20, f)
            big_waves(d, f, 600, (30, 50, 64), (180, 190, 200))
            put(c, "tai0", 280, FEET); put(c, "tai1", 330, FEET); hut(d, 380, 730, 60)
            word_card(d, "HURAKÁN", "HURRICANE", 270, 240, prog * 1.5)
            if flash: R(d, (0, 0, CW, 6), WHITE)
        elif li == 1:
            barbacoa(d, 200, 720, f); label(d, "BARBACOA", 274, 560, GOLD)
            put(c, "tai0", 40, FEET, sc=2); label(d, "TAÍNO COOK", 92, 545, WHITE, K)
            for k in range(2): hut(d, 360 + k * 90, 640, 54)
            word_card(d, "BARBACOA", "BARBECUE", 270, 240, prog * 1.5)
        else:
            for k in range(6): put(c, SP["c_tobacco"].resize((56, 56), Image.NEAREST), 280 + (k % 3) * 70, 690 + (k // 3) * 40)
            label(d, "TOBACCO PLANTS", 390, 600, WHITE, K)
            put(c, "guaca", 40, FEET, sc=2); pipe(d, 150, 560); label(d, "PIPE", 168, 610, GOLD)
            label(d, "CACIQUE", 92, 545, GOLD)
            word_card(d, "TABACO", "TOBACCO", 270, 240, prog * 1.5)
    elif i == 4:
        if li == 0:
            clouds(d, f, 130); torch(d, 270, 720, f); barrel(d, 300, 730); crate(d, 340, 730)
            R(d, (470, 520, 473, FEET), BROWN_D); castile_banner(d, 474, 524)
            put(c, "ovando", 30, FEET, sc=2); label(d, "GOVERNOR OVANDO", 120, 545, GOLD)
            put(c, "esp0", 160, FEET); put(c, "esp1", 210, FEET); label(d, "SOLDIERS", 210, 630, WHITE, K)
            scroll(d, 290, 380 + bob(f, 3, 0.08)); label(d, "ENCOMIENDA", 320, 345, WHITE, RED_D)
            label(d, "HISPANIOLA, 1502", 270, 250, K, YEL, F16)
        elif li == 1:
            church(d, 420, 640)
            put(c, "set1", 10, FEET, sc=2); label(d, "SETTLER", 62, 545, GOLD)
            put(c, "friar", 130, FEET, sc=2); label(d, "FRIAR", 182, 500, GOLD)
            for k in range(4): put(c, f"tai{k % 2}" if k < 3 else "cacica", 270 + k * 48, FEET - (k % 2) * 8, flip=True)
            label(d, "TAÍNO WORKERS", 380, 630, WHITE, K)
            label(d, "LABOR FOR SETTLERS", 270, 250, K, YEL, F16)
            if prog > 0.45: label(d, "DUTY: TEACH THE FAITH", 270, 290, WHITE, K, F16)
        else:
            conuco(d, 300, 680, 4); clouds(d, f, 140, seed=5); gulls(d, f, 2, 360, (60, 40, 40))
            for k in range(4):
                x = 40 + k * 70 + (f * 1.2 + k * 30) % 30; put(c, f"tai{st(f, k, 6)}", x, FEET - 30 + (k % 2) * 10)
                put(c, "sack", x + 10, FEET - 80 - 30 + (k % 2) * 10)
            put(c, "set2", 420, FEET, sc=2, flip=True); label(d, "OVERSEER", 472, 545, GOLD)
            for k in range(5): R(d, (30 + k * 90 + (f // 4 + k) % 8, 702, 36 + k * 90 + (f // 4 + k) % 8, 704), GOLD)
            label(d, "RIVER GOLD", 140, 640, K, YEL)
            label(d, "FORCED LABOR", 270, 250, WHITE, RED, F16)
    elif i == 5:
        vals = [("1508", 60000, "60,000"), ("1514", 26334, "26,000"), ("1542", 2000, "2,000")]
        bars(d, 40, 140, vals, li + 1, prog)
        label(d, "TAÍNO ON HISPANIOLA", 270, 110, K, YEL, F16)
        n = [10, 5, 1][li]
        for k in range(10):
            x = 20 + k * 50; a = 1.0 if k < n else (0.25 if li == 0 else 0.0)
            if a > 0: put(c, f"tai{k % 2}", x, FEET - (k % 2) * 6, alpha=a)
        for k in range(2): hut(d, 40 + k * 380, 640, 54, burned=(li == 2))
        if li >= 1 and prog > 0.4 or li == 2:
            for k in range(5):
                pr = random.Random(k); x = 60 + pr.randint(0, 420); y = 520 + pr.randint(0, 80) + bob(f, 6, 0.1, k)
                put(c, SP["c_germ"], x, y)
            label(d, "SMALLPOX, 1518", 270, 490, WHITE, RED_D, F16)
    elif i == 6:
        if li == 0:
            c.alpha_composite(taino_map(f, [("BAHAMAS", -79.5, 25.8, K, YEL), ("ELEUTHERA", -73.2, 24.9, WHITE, K), ("CUBA", -80, 22.0, K, YEL)],
                                        "ANCIENT GENOME, 2018", dots=[ELEUTHERA], h=320), (25, 110))
            cave(d, 260, 700); put(c, "tooth", 360, 690 + bob(f, 3, 0.1)); label(d, "ANCIENT TOOTH", 380, 600, GOLD)
            put(c, "pr2", 30, FEET); put(c, "pr1", 90, FEET, flip=True); label(d, "SCIENTISTS", 90, 630, WHITE, K)
            label(d, "CAVE ON ELEUTHERA", 270, 460, K, YEL, F16)
            label(d, "WOMAN, 700s-900s", 270, 500, WHITE, K, F16)
        else:
            c.alpha_composite(taino_map(f, [("ELEUTHERA", -79.8, 24.4, WHITE, K), ("PUERTO RICO", -64.5, 20.6, K, YEL), ("HISPANIOLA", -71.5, 17.0, K, YEL)],
                                        "DNA MATCH", dots=[ELEUTHERA, PR_PT], route=([ELEUTHERA, (-71, 22.5), (-66.6, 18.6), PR_PT], min(1, prog * 1.4)), h=320), (25, 110))
            helix(d, 270, 478, 150, f)
            put(c, "tai2", 60, FEET, sc=2); label(d, "TAÍNO", 112, 545, GOLD)
            for k, key in enumerate(("pr1", "pr2", "pr3")): put(c, key, 330 + k * 60, FEET - (k % 2) * 8, flip=True)
            label(d, "PUERTO RICANS TODAY", 400, 630, WHITE, K)
            if prog > 0.4: label(d, "CLOSEST MATCH", 270, 446, K, YEL, F16)
    elif i == 7:
        waves(d, f, 560, (240, 200, 160)); gulls(d, f, 3, 300, (80, 50, 50))
        swirl(d, 120, 230, 40, f, (250, 230, 210))
        canoe(c, d, 150 + prog * 60, 640 + bob(f, 3, 0.1), f)
        hammock(c, d, 300, 500, 560, f, who=False)
        put(c, "cacica", 30, FEET, sc=2); label(d, "TAÍNO", 82, 545, GOLD)
        label(d, "HURRICANE · CANOE", 330, 250, K, YEL, F16); label(d, "HAMMOCK · BARBECUE", 330, 290, K, YEL, F16)
        if prog > 0.45: label(d, "FOLLOW FOR MORE HISTORY", 270, 420, WHITE, RED, F16)

# ---------------- render ----------------
if CHECK:
    for i, (head, lines) in enumerate(SCENES):
        for li in range(len(lines)):
            compose(i, li, 40, 2.0, 2.6, 3.0, 8.0, make_bg(i, li), overlay(head, lines[li][1])).save(f"{OUT}/check{i}_{li}.png")
    sys.exit()

audios, clips, total = [], [], 0.0
for i, (head, lines) in enumerate(SCENES):
    ldurs = []
    for li, (spoken, cap) in enumerate(lines):
        raw = f"{OUT}/a{i}_{li}.wav"; pad = f"{OUT}/p{i}_{li}.wav"
        tts(spoken, raw)
        gap = 0.55 if li == len(lines) - 1 else 0.3
        if i == len(SCENES) - 1: gap = 2.2  # hold the final frame with FOLLOW FOR MORE HISTORY
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
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{OUT}/video.mp4", "-i", f"{OUT}/voice.wav", "-i", f"{OUT}/music.wav",
                "-filter_complex", "[1:a]volume=-3dB[v];[2:a]volume=0.12[m];[v][m]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.89:level=disabled[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", FINAL], check=True)
print("total", round(total, 1))
