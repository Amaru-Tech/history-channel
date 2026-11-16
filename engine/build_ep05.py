import os, sys
D = os.environ.get("HC_DIR", os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")
_src = open(f"{D}/build4.py").read().split("# ---------------- render ----------------")[0]
sys_argv_backup = list(sys.argv); sys.argv = [sys.argv[0]]
exec(_src)  # engine, sprites, maps, overlay, compose, music, tts from episode 1
_src5 = open(f"{D}/build5.py").read().split("# ---------------- extra sprites ----------------")[1].split("# ---------------- backgrounds ----------------")[0]
exec(_src5)  # episode 2 sprites: Taino chiefs, sleeper, Caribbean map, fort, canoe, reef
_src6 = open(f"{D}/build_ep03.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- backgrounds ----------------")[0]
exec(_src6)  # episode 3 sprites: pig, friar, sack, sugarcane, huts, church, stone house, rain
sys.argv = sys_argv_backup
CHECK = "check" in sys.argv
OUT = f"{D}/out_ep05"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep05_columbus_in_chains_EN.mp4"

SCENES = [
 ("IN CHAINS", [
  ("In fifteen hundred, the man who reached the New World sailed home in chains.", "In 1500, the man who reached the New World sailed home in chains."),
  ("Christopher Columbus had been arrested by a judge sent by his own king and queen.", "Christopher Columbus had been arrested by a judge sent by his own king and queen.")]),
 ("THE THIRD VOYAGE", [
  ("In fourteen ninety-eight, on his third voyage, he reached the coast of South America.", "In 1498, on his third voyage, he reached the coast of South America."),
  ("Then he returned to Hispaniola, where he ruled as governor.", "Then he returned to Hispaniola, where he ruled as governor.")]),
 ("THE JUDGE", [
  ("Settlers sent complaints to Spain about his rule.", "Settlers sent complaints to Spain about his rule."),
  ("So the crown sent a judge, Francisco de Bobadeeya. He landed in August fifteen hundred.", "So the crown sent a judge, Francisco de Bobadilla. He landed in August 1500.")]),
 ("SENT HOME", [
  ("Bobadeeya arrested Columbus and shipped him back to Spain in chains.", "Bobadilla arrested Columbus and shipped him back to Spain in chains."),
  ("Ferdinand and Isabella set him free. But he never governed Hispaniola again.", "Ferdinand and Isabella set him free. But he never governed Hispaniola again.")]),
 ("THE LAST VOYAGE", [
  ("In fifteen oh two, he sailed one last time, with four ships.", "In 1502, he sailed one last time, with four ships."),
  ("At Santo Domingo, he warned that a hurricane was coming. The new governor ignored him.", "At Santo Domingo, he warned that a hurricane was coming. The new governor ignored him."),
  ("The storm sank about twenty ships of the fleet. Bobadeeya went down with them.", "The storm sank about 20 ships of the fleet. Bobadilla went down with them.")]),
 ("CASTAWAYS", [
  ("Columbus explored Central America, from Honduras to Panama.", "Columbus explored Central America, from Honduras to Panama."),
  ("But worms ate through his ships. In fifteen oh three, he beached them in Jamaica.", "But worms ate through his ships. In 1503, he beached them in Jamaica."),
  ("Two of his men crossed the open sea by canoe, to find help.", "Two of his men crossed the open sea by canoe, to find help.")]),
 ("THE ECLIPSE", [
  ("Months passed, and the local Tyeeno stopped bringing food.", "Months passed, and the local Taino stopped bringing food."),
  ("But Columbus had an almanac. It predicted a lunar eclipse on February twenty-ninth, fifteen oh four.", "But Columbus had an almanac. It predicted a lunar eclipse on February 29, 1504."),
  ("He warned that God would hide the moon. When it darkened, the food came back.", "He warned that God would hide the moon. When it darkened, the food came back.")]),
 ("THE END", [
  ("Rescue came in June fifteen oh four, a year after the shipwreck.", "Rescue came in June 1504, a year after the shipwreck."),
  ("Columbus died in Vah-yah-doh-leed in fifteen oh six. He never got his power back.", "Columbus died in Valladolid in 1506. He never got his power back.")]),
]

_label_orig = label
def label(d, text, cx, y, fg=WHITE, bg=K, font=F16):
    w = d.textlength(text, font=font); cx = min(max(cx, w / 2 + 8), CW - w / 2 - 8)
    _label_orig(d, text, cx, y, fg, bg, font)

# ---------------- extra sprites ----------------
CHAIN = (150, 156, 168)
def chains(im):
    im = im.copy(); d = ImageDraw.Draw(im)
    for x in range(12, 41, 4): R(d, (x, 56, x + 2, 58), CHAIN); R(d, (x + 1, 57, x + 1, 57), K)
    for y in range(58, 80, 4): R(d, (25, y, 27, y + 2), CHAIN)
    for x in range(14, 39, 4): R(d, (x, 77, x + 2, 79), CHAIN)
    R(d, (10, 54, 16, 60), STEEL_D); R(d, (36, 54, 42, 60), STEEL_D)
    return im

def bobadilla():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    R(d, (44, 14, 45, 79), BROWN); R(d, (43, 12, 46, 16), GOLD)
    robe_body(d, (34, 32, 40), (20, 18, 24))
    R(d, (16, 36, 36, 40), WHITE); R(d, (24, 40, 28, 56), (60, 56, 70))
    face(d); R(d, (19, 28, 33, 35), (70, 50, 40)); R(d, (24, 31, 28, 31), (150, 80, 70))
    R(d, (16, 10, 36, 16), K); R(d, (20, 4, 32, 10), K)
    return outline(im)

def ferdinand():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, (40, 60, 140), (26, 40, 100))
    for y in (52, 66): R(d, (14, y, 38, y + 1), GOLD)
    R(d, (16, 36, 36, 39), (240, 236, 220))
    face(d); R(d, (17, 15, 35, 20), (90, 60, 30)); R(d, (17, 20, 19, 32), (90, 60, 30)); R(d, (33, 20, 35, 32), (90, 60, 30))
    R(d, (18, 10, 34, 15), GOLD); R(d, (18, 6, 20, 10), GOLD); R(d, (25, 4, 27, 10), GOLD); R(d, (32, 6, 34, 10), GOLD)
    R(d, (21, 11, 23, 13), RED)
    return outline(im)

def ovando():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, (230, 226, 214), (190, 186, 176))
    R(d, (24, 42, 28, 56), (40, 120, 60)); R(d, (19, 47, 33, 51), (40, 120, 60))
    face(d); R(d, (19, 28, 33, 35), (110, 100, 96))
    R(d, (16, 10, 36, 16), K); R(d, (19, 7, 33, 10), K)
    return outline(im)

def settler(shirt):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    for x0, x1 in [(20, 23), (29, 32)]: R(d, (x0, 62, x1, 78), (90, 70, 50)); R(d, (x0 - 1, 77, x1 + 1, 81), K)
    R(d, (16, 36, 36, 63), shirt); R(d, (16, 58, 36, 60), BROWN)
    R(d, (11, 37, 16, 52), shirt); R(d, (36, 20, 40, 40), shirt); R(d, (36, 16, 40, 20), SKIN_E)
    face(d); R(d, (17, 13, 35, 19), (70, 50, 30))
    return outline(im)

def basket(full=True):
    im = Image.new("RGBA", (34, 26)); d = ImageDraw.Draw(im)
    if full:
        for x, y, col in ((6, 2, (240, 200, 50)), (14, 0, (214, 40, 30)), (21, 3, (176, 130, 76)), (10, 5, (90, 150, 60))): d.ellipse((x, y, x + 9, y + 9), fill=col)
    d.polygon([(1, 10), (33, 10), (29, 25), (5, 25)], fill=(190, 150, 80))
    for y in (14, 19): R(d, (4, y, 30, y), (150, 110, 50))
    return outline(im)

SP.update({"colc": chains(SP["col"]), "bob": bobadilla(), "ferd": ferdinand(), "ovando": ovando(),
           "set1": settler((170, 60, 50)), "set2": settler((60, 100, 150)), "bask": basket(True), "bask0": basket(False)})

def wreck():
    s = SP["ship"].rotate(-11, resample=Image.NEAREST, expand=True); d = ImageDraw.Draw(s)
    rnd = random.Random(7)
    for _ in range(14):
        x, y = rnd.randint(30, 140), rnd.randint(100, 135)
        if s.getpixel((x, y))[3] > 0: R(d, (x, y, x + 3, y + 2), K)
    return s
SP["wreck"] = wreck()

def moon(d, cx, cy, r, shade):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(236, 236, 214))
    if shade > 0:
        col = tuple(int(a + (b - a) * shade) for a, b in zip((236, 236, 214), (120, 40, 30)))
        off = int(2 * r * (1 - shade))
        lay = Image.new("L", (2 * r + 1, 2 * r + 1), 0); ld = ImageDraw.Draw(lay); ld.ellipse((0, 0, 2 * r, 2 * r), fill=255)
        sh = Image.new("L", (2 * r + 1, 2 * r + 1), 0); sd = ImageDraw.Draw(sh); sd.ellipse((-off, 0, 2 * r - off, 2 * r), fill=255)
        mask = ImageChops.multiply(lay, sh)
        return col, mask
    return None, None

def draw_moon(c, cx, cy, r, shade):
    d = ImageDraw.Draw(c); col, mask = moon(d, cx, cy, r, shade)
    if mask is not None:
        c.paste(Image.new("RGBA", mask.size, col + (255,)), (cx - r, cy - r), mask)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=K, width=2)

def almanac(d, x, y, open_prog=1.0):
    R(d, (x, y, x + 200, y + 130), (110, 60, 30)); R(d, (x + 8, y + 6, x + 96, y + 124), (236, 222, 180)); R(d, (x + 104, y + 6, x + 192, y + 124), (236, 222, 180))
    R(d, (x + 98, y, x + 102, y + 130), (80, 40, 20))
    for k in range(8): R(d, (x + 16, y + 16 + k * 12, x + 86, y + 17 + k * 12), (150, 130, 100))
    for k in range(3):
        cx, cy = x + 130 + k * 26, y + 40; d.ellipse((cx - 9, cy - 9, cx + 9, cy + 9), fill=(236, 236, 214), outline=K)
        d.ellipse((cx - 9 + (3 - k) * 6, cy - 9, cx + 9 + (3 - k) * 6, cy + 9), fill=(236, 222, 180)) if k < 2 else d.ellipse((cx - 9, cy - 9, cx + 9, cy + 9), fill=(140, 40, 30), outline=K)
    for k in range(4): R(d, (x + 112, y + 70 + k * 12, x + 184, y + 71 + k * 12), (150, 130, 100))

# ---------------- maps ----------------
SEVILLE_P = (-6.3, 36.8); CV = (-24, 16); TRIN = (-61.5, 10.3); STODOM = (-69.9, 18.5)
TRINIDAD = [(-61.9, 10.85), (-60.9, 10.85), (-61.0, 10.1), (-61.9, 10.05)]

def westcarib_map(f, w=490, h=360, labels=(), route=None, title=None, dots=()):
    m = Image.new("RGBA", (w, h)); d = ImageDraw.Draw(m); d.fontmode = "1"
    P = lambda lon, lat: (6 + (lon + 90) / 30 * (w - 12), 6 + (24 - lat) / 18 * (h - 12))
    R(d, (0, 0, w - 1, h - 1), (58, 98, 150))
    for poly in (AMER, CUBA2, HISP2, JAM, PR, TRINIDAD): d.polygon([P(*p) for p in poly], fill=(118, 150, 84), outline=(52, 74, 38))
    if route:
        pts, prog = route; seg = [P(*p) for p in pts]
        lens = [math.dist(seg[k], seg[k + 1]) for k in range(len(seg) - 1)]; want = sum(lens) * prog; acc = 0; head = seg[0]
        for k, L in enumerate(lens):
            for s in range(int(L // 6)):
                if acc + s * 6 > want: break
                a, b = seg[k], seg[k + 1]; tt = s * 6 / L; x, y = a[0] + (b[0] - a[0]) * tt, a[1] + (b[1] - a[1]) * tt
                R(d, (x - 1, y - 1, x + 1, y + 1), WHITE); head = (x, y)
            acc += L
        x, y = head; d.polygon([(x - 6, y + 3), (x + 6, y + 3), (x + 4, y + 7), (x - 4, y + 7)], fill=BROWN); d.polygon([(x, y - 8), (x, y + 2), (x + 6, y + 1)], fill=WHITE)
    for lon, lat in dots:
        x, y = P(lon, lat); on = (f // 10) % 2 == 0
        R(d, (x - 4, y - 4, x + 4, y + 4), RED if on else WHITE); d.rectangle((x - 4, y - 4, x + 4, y + 4), outline=K)
    for text, lon, lat, fg, bg in labels:
        x, y = P(lon, lat); tw = d.textlength(text, font=F16); x = min(max(x, tw / 2 + 8), w - tw / 2 - 8)
        R(d, (x - tw / 2 - 4, y - 10, x + tw / 2 + 3, y + 9), bg); d.text((x - tw / 2, y - 8), text, font=F16, fill=fg)
    if title:
        tw = d.textlength(title, font=F16); R(d, (w / 2 - tw / 2 - 5, 8, w / 2 + tw / 2 + 4, 30), K); d.text((w / 2 - tw / 2, 11), title, font=F16, fill=GOLD)
    d.rectangle((0, 0, w - 1, h - 1), outline=(240, 220, 170), width=3)
    return outline(m)

# ---------------- backgrounds ----------------
def night_sea(d):
    sea(d, (10, 14, 40), (60, 70, 120), 600, (20, 30, 70), (80, 100, 160))
    rnd = random.Random(4)
    for _ in range(60): x, y = rnd.randint(0, CW), rnd.randint(0, 500); R(d, (x, y, x, y), WHITE)

def court(d):
    grad(d, (60, 20, 24), (110, 40, 40), 0, GY, 12)
    for x in range(30, CW, 120): R(d, (x, 120, x + 24, GY), (140, 110, 80)); R(d, (x - 4, 116, x + 28, 128), (170, 140, 100))
    R(d, (0, GY, CW, CH), (120, 30, 36)); R(d, (150, GY, 390, CH), (170, 40, 46))
    for x in range(0, CW, 40): R(d, (x, GY, x + 1, CH), (90, 20, 26))

def beach(d, night=False):
    if night: sea(d, (10, 14, 40), (50, 60, 100), 560, (20, 40, 70), (80, 100, 150))
    else: sea(d, (80, 170, 240), (200, 230, 250), 560, (40, 170, 190), (200, 240, 240))
    R(d, (0, 640, CW, CH), (130, 116, 80) if night else (236, 214, 150))
    rnd = random.Random(8)
    for _ in range(90): x, y = rnd.randint(0, CW), rnd.randint(644, CH); R(d, (x, y, x + 1, y), (110, 96, 64) if night else (210, 186, 124))
    palm(d, 490, 650, 200, -1)

def dock(d, x1=250):
    R(d, (0, 690, x1, CH), (120, 80, 46))
    for x in range(0, x1, 24): R(d, (x, 690, x + 1, CH), (90, 58, 30))
    R(d, (0, 690, x1, 694), (150, 104, 60))

def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0 or (i == 3 and li == 0):
        night_sea(d); d.ellipse((420, 120, 466, 166), fill=(236, 236, 214)); dock(d)
    elif i in (1, 7) and not (i == 7 and li == 1) or (i == 5 and li == 0) or (i == 2 and li == 1):
        if i == 7: sea(d, (250, 150, 90), (250, 210, 150), 600, (40, 90, 150), (240, 200, 160)); R(d, (0, 640, CW, CH), (236, 214, 150))
        else: grad(d, (24, 44, 70), (60, 90, 120), 0, CH, 12)
        if i == 2: sea(d, (90, 170, 240), (210, 230, 250), 600, (40, 120, 180), (200, 230, 250)); dock(d)
        if i == 1 and li == 1: R(d, (0, GY, CW, CH), (196, 176, 120))
    elif i == 2 and li == 0:
        sea(d, (90, 170, 240), (210, 230, 250), 560, (40, 120, 180), (200, 230, 250))
        R(d, (0, 640, CW, CH), (196, 176, 120)); stone_house(d, 380, 650); church(d, 30, 650)
    elif i == 3 or (i == 7 and li == 1):
        court(d)
    elif i == 4:
        if li < 2: sea(d, (80, 160, 230), (200, 225, 250), 600, (40, 110, 170), (200, 230, 250))
        else: sea(d, (30, 34, 44), (70, 76, 90), 600, (30, 50, 60), (120, 130, 140))
        if li == 1: R(d, (0, 640, CW, CH), (196, 176, 120))
    elif i == 5:
        beach(d) if li == 1 else sea(d, (80, 170, 240), (200, 230, 250), 600, (40, 110, 170), (200, 240, 240))
    elif i == 6:
        beach(d, night=(li > 0))
    return c

# ---------------- scenes ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        waves(d, f, 600, (80, 100, 160))
        x = 300 + t * 4; put(c, "ship", x, 690 + bob(f, 3, 0.1), k=0.85)
        put(c, "colc", 30, FEET, sc=2); label(d, "COLUMBUS", 82, 540, GOLD)
        if li == 0: label(d, "SPAIN, 1500", 300, 260, K, YEL, F16)
        else:
            put(c, "bob", 140, FEET, sc=2); label(d, "ROYAL JUDGE", 192, 500, GOLD)
            label(d, "ARRESTED", 300, 260, WHITE, RED, F16); label(d, "BY ROYAL ORDER", 300, 300, K, YEL, F16)
    elif i == 1:
        if li == 0:
            c.alpha_composite(world_map(f, route=([SEVILLE_P, CV, TRIN], min(1, prog * 1.4)), labels=[("SPAIN", -4, 41, K, YEL), ("SOUTH AMERICA", -60, -12, K, YEL)], title="THIRD VOYAGE, 1498"), (25, 120))
            if prog > 0.7: label(d, "SOUTH AMERICA REACHED", 270, 570, WHITE, RED_D, F16)
        else:
            c.alpha_composite(westcarib_map(f, labels=[("HISPANIOLA", -71, 21.2, K, YEL), ("SANTO DOMINGO", -71, 16.6, WHITE, K)], dots=[STODOM], title="1498-1500"), (25, 110))
            put(c, "col", 218, FEET, sc=2); label(d, "GOVERNOR COLUMBUS", 270, 545, GOLD)
    elif i == 2:
        if li == 0:
            put(c, "set1", 40, FEET, sc=2); put(c, "set2", 380, FEET, sc=2, flip=True)
            label(d, "SETTLER", 92, 545, GOLD); label(d, "SETTLER", 432, 545, GOLD)
            bubble(d, "UNFAIR!", 110, 470); bubble(d, "HARSH!", 420, 470) if prog > 0.3 else None
            label(d, "COMPLAINTS TO SPAIN", 270, 250, K, YEL, F16)
        else:
            waves(d, f, 600, (80, 100, 160))
            put(c, "ship", 260, 640 + bob(f, 3, 0.1))
            put(c, "bob", 40, FEET, sc=2); label(d, "BOBADILLA", 92, 545, GOLD)
            label(d, "ROYAL JUDGE", 330, 250, K, YEL, F16); label(d, "AUGUST 1500", 330, 290, WHITE, K, F16)
    elif i == 3:
        if li == 0:
            waves(d, f, 600, (80, 100, 160))
            put(c, "ship", 290, 690 + bob(f, 3, 0.1)); put(c, "colc", 140, FEET, sc=2)
            put(c, "bob", 30, FEET, sc=2); label(d, "BOBADILLA", 82, 545, GOLD); label(d, "COLUMBUS", 192, 500, GOLD)
            label(d, "OCTOBER 1500", 330, 250, K, YEL, F16); label(d, "IN CHAINS", 330, 290, WHITE, RED, F16)
        else:
            put(c, "ferd", 30, FEET, sc=2); put(c, "isa", 140, FEET, sc=2)
            label(d, "FERDINAND", 82, 545, GOLD); label(d, "ISABELLA", 192, 500, GOLD)
            put(c, "col" if prog > 0.3 else "colc", 380, FEET, sc=2, flip=True); label(d, "COLUMBUS", 432, 545, GOLD)
            if prog > 0.3: label(d, "FREE", 432, 300, K, YEL, F16)
            if prog > 0.6: label(d, "NOT GOVERNOR", 330, 340, WHITE, RED, F16)
    elif i == 4:
        if li == 0:
            waves(d, f, 600, (200, 230, 250))
            for k in range(4):
                put(c, "ship" if k == 0 else tint(SP["ship"], 0.8), 20 + k * 120 + t * 4, 680 + (k % 2) * 20 + bob(f, 3, 0.1, k))
            label(d, "1502: FOUR SHIPS", 270, 260, K, YEL, F16)
        elif li == 1:
            put(c, "col", 40, FEET, sc=2); label(d, "COLUMBUS", 92, 545, GOLD)
            put(c, "ovando", 380, FEET, sc=2, flip=True); label(d, "GOVERNOR OVANDO", 400, 545, GOLD)
            bubble(d, "HURRICANE!", 130, 460)
            if prog > 0.5: bubble(d, "NONSENSE.", 410, 400)
            label(d, "SANTO DOMINGO", 270, 250, K, YEL, F16)
        else:
            rain(d, f)
            for k in range(5):
                sink = min(1, max(0, prog * 1.6 - k * 0.15)); x = 20 + k * 100
                im = SP["ship"].rotate(-8 + 16 * (k % 2) + int(math.sin(f * 0.2 + k) * 4), resample=Image.NEAREST, expand=True)
                im = im.crop((0, 0, im.width, max(1, int(im.height * (1 - sink * 0.85)))))
                put(c, tint(im, 0.6), x, 690 + int(sink * 40) + bob(f, 6, 0.2, k))
            waves(d, f, 600, (140, 150, 170))
            label(d, "~20 SHIPS LOST", 270, 250, WHITE, RED, F16); label(d, "BOBADILLA DROWNS", 270, 290, WHITE, K, F16)
    elif i == 5:
        if li == 0:
            c.alpha_composite(westcarib_map(f, route=([(-78, 18.6), (-85.5, 16.4), (-83.2, 15.0), (-83.3, 10.8), (-81, 8.8), (-79.6, 9.6)], min(1, prog * 1.3)),
                labels=[("HONDURAS", -86.5, 14.2, K, YEL), ("PANAMA", -80.5, 7.6, K, YEL), ("JAMAICA", -77.2, 19.4, WHITE, K)], title="FOURTH VOYAGE, 1502-03"), (25, 110))
        elif li == 1:
            put(c, "wreck", 60, 720); put(c, "wreck", 250, 730, flip=True)
            label(d, "JAMAICA, 1503", 270, 250, K, YEL, F16); label(d, "SHIPWORM DAMAGE", 270, 290, WHITE, K, F16)
            put(c, "col", 430, FEET); label(d, "COLUMBUS", 456, 600, GOLD)
        else:
            waves(d, f, 600, (200, 240, 240))
            x = -60 + prog * 400
            d.polygon([(x, 700), (x + 120, 700), (x + 108, 714), (x + 12, 714)], fill=(120, 74, 38)); R(d, (x + 4, 700, x + 116, 702), (150, 100, 56))
            for j in range(2):
                put(c, "sailor", x + 20 + j * 50, 704, crop=46); a = math.sin(f * 0.25 + j) * 8
                d.line([(x + 50 + j * 50, 688), (x + 44 + j * 50 + a, 722)], fill=BROWN_D, width=2)
            label(d, "TO HISPANIOLA", 270, 250, K, YEL, F16); label(d, "BY CANOE", 270, 290, WHITE, K, F16)
    elif i == 6:
        if li == 0:
            put(c, "col", 40, FEET, sc=2); label(d, "COLUMBUS", 92, 545, GOLD)
            put(c, "tai0", 380, FEET, sc=2, flip=True); label(d, "TAINO", 432, 545, GOLD)
            put(c, "bask0", 300, FEET); label(d, "NO MORE FOOD", 270, 250, WHITE, RED, F16)
        elif li == 1:
            almanac(d, 170, 420); label(d, "ALMANAC", 270, 380, GOLD)
            label(d, "ECLIPSE: FEB 29, 1504", 270, 250, K, YEL, F16)
            draw_moon(c, 460, 150, 26, 0)
        else:
            shade = min(1, prog * 1.6); draw_moon(c, 270, 300, 60, shade)
            put(c, "col", 40, FEET, sc=2); label(d, "COLUMBUS", 92, 545, GOLD)
            put(c, "tai0", 390, FEET, sc=2, flip=True); label(d, "TAINO", 442, 545, GOLD)
            if prog > 0.7: put(c, "bask", 300, FEET); put(c, "bask", 330, FEET - 4); label(d, "FOOD IS BACK", 270, 420, K, YEL, F16)
    elif i == 7:
        if li == 0:
            waves(d, f, 600, (240, 200, 160))
            put(c, "ship", 340 - prog * 60, 690 + bob(f, 3, 0.1)); put(c, "wreck", 10, 740, k=0.8)
            put(c, "col", 220, FEET - 20); label(d, "COLUMBUS", 246, 580, GOLD)
            label(d, "RESCUED: JUNE 1504", 270, 250, K, YEL, F16)
        else:
            put(c, "colc", 220, FEET, sc=2, alpha=0.35)
            put(c, "col", 220, FEET, sc=2, alpha=max(0.2, 1 - prog)); label(d, "COLUMBUS", 272, 545, GOLD)
            label(d, "VALLADOLID, 1506", 270, 250, K, YEL, F16)
            if prog > 0.5: label(d, "FOLLOW FOR MORE HISTORY", 270, 340, WHITE, RED, F16)

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
