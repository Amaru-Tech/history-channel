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
  ("But worms ate through his ships. In fifteen oh three, he ran them aground in Jamaica.", "But worms ate through his ships. In 1503, he ran them aground in Jamaica."),
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
SEVILLE_P = (-6, 36); CV = (-24, 15); PARIA = (-63, 10.7); STODOM = (-69.9, 18.45)
TRINIDAD = [(-61.9, 10.85), (-60.9, 10.85), (-61.0, 10.1), (-61.9, 10.05)]
# detailed Gulf of Mexico / Central America / northern South America coast (lon, lat)
AMER_D = [(-97.5, 24), (-97.2, 21), (-96, 19), (-94.5, 18.2), (-92, 18.6), (-91, 18.8), (-90.5, 19.8), (-90.4, 21.1), (-88, 21.5), (-87, 21.5),
          (-86.8, 20.8), (-87.5, 19.5), (-87.8, 18.4), (-88.3, 17.3), (-88.3, 16.5), (-88.7, 15.8), (-87.8, 15.8), (-86.5, 15.8), (-85, 16),
          (-84, 15.8), (-83.2, 15.0), (-83.5, 14), (-83.6, 12.5), (-83.8, 11), (-83, 10), (-82.3, 9.3), (-82.2, 9.0), (-81, 8.9), (-79.9, 9.35),
          (-78.5, 9.4), (-77.4, 8.6), (-76.8, 8.6), (-76, 9.5), (-75.5, 10.5), (-74.8, 11), (-73.5, 11.3), (-72, 12.3), (-71.3, 11.0),
          (-70.4, 11.6), (-70.2, 12.1), (-69.8, 11.4), (-68.2, 10.5), (-66.5, 10.6), (-64.5, 10.3), (-63.5, 10.6), (-63, 10.7), (-62, 10.7),
          (-62.2, 10.1), (-61.6, 9.8), (-61, 9.0), (-60, 8.5), (-58, 6.8), (-55, 5.8), (-52, 5), (-50, 0), (-80, 0), (-80, 1), (-78.8, 1.5),
          (-77.5, 4), (-77.5, 6.5), (-78.2, 8.0), (-79.5, 8.95), (-80.4, 7.3), (-81.2, 7.6), (-82.9, 8.1), (-83.7, 8.6), (-85.7, 9.9),
          (-85.8, 11.2), (-87.6, 13.0), (-91.4, 13.9), (-92.3, 14.6), (-94, 16), (-96, 15.7), (-100, 17), (-100, 24)]

def draw_route(d, seg, prog, head=True):
    lens = [math.dist(seg[k], seg[k + 1]) for k in range(len(seg) - 1)]; want = sum(lens) * prog; acc = 0; hp = seg[0]
    for k, L in enumerate(lens):
        if L == 0: continue
        n = int(L // 6) + 1
        for s in range(n):
            pos = acc + min(L, s * 6)
            if pos > want: break
            a, b = seg[k], seg[k + 1]; tt = min(1, s * 6 / L); x, y = a[0] + (b[0] - a[0]) * tt, a[1] + (b[1] - a[1]) * tt
            R(d, (x - 1, y - 1, x + 1, y + 1), WHITE); hp = (x, y)
        acc += L
    if prog >= 1: hp = seg[-1]; R(d, (hp[0] - 1, hp[1] - 1, hp[0] + 1, hp[1] + 1), WHITE)
    if head and prog < 1:
        x, y = hp; d.polygon([(x - 6, y + 3), (x + 6, y + 3), (x + 4, y + 7), (x - 4, y + 7)], fill=BROWN); d.polygon([(x, y - 8), (x, y + 2), (x + 6, y + 1)], fill=WHITE)

def region_map(f, box, w=490, h=380, labels=(), route=None, title=None, dots=(), extra=None):
    lon0, lon1, lat0, lat1 = box
    m = Image.new("RGBA", (w, h)); d = ImageDraw.Draw(m); d.fontmode = "1"
    P = lambda lon, lat: (6 + (lon - lon0) / (lon1 - lon0) * (w - 12), 6 + (lat1 - lat) / (lat1 - lat0) * (h - 12))
    R(d, (0, 0, w - 1, h - 1), (58, 98, 150))
    for lon in range(-100, -40, 5):
        x = P(lon, 0)[0]
        if 0 < x < w: d.line([(x, 0), (x, h)], fill=(52, 88, 136))
    for lat in range(0, 30, 5):
        y = P(0, lat)[1]
        if 0 < y < h: d.line([(0, y), (w, y)], fill=(52, 88, 136))
    for poly in (AMER_D, FLA, CUBA2, HISP2, JAM, PR, TRINIDAD): d.polygon([P(*p) for p in poly], fill=(118, 150, 84), outline=(52, 74, 38))
    for lon, lat, r in BAH:
        x, y = P(lon, lat); rr = r * (w - 12) / (lon1 - lon0); d.ellipse((x - rr, y - rr / 2, x + rr, y + rr / 2), fill=(118, 150, 84))
    rnd = random.Random(2)
    for _ in range(26):  # jungle dots on the mainland
        lon, lat = rnd.uniform(lon0, lon1), rnd.uniform(lat0, lat1); x, y = P(lon, lat)
        if 0 < x < w and 0 < y < h and m.getpixel((int(x), int(y)))[:3] == (118, 150, 84): R(d, (x, y, x + 3, y + 2), (90, 126, 64))
    if route:
        pts, prog = route; draw_route(d, [P(*p) for p in pts], prog)
    for lon, lat in dots:
        x, y = P(lon, lat); on = (f // 10) % 2 == 0
        R(d, (x - 4, y - 4, x + 4, y + 4), RED if on else WHITE); d.rectangle((x - 4, y - 4, x + 4, y + 4), outline=K)
    for text, lon, lat, fg, bg in labels:
        x, y = P(lon, lat); tw = d.textlength(text, font=F16); x = min(max(x, tw / 2 + 8), w - tw / 2 - 8)
        R(d, (x - tw / 2 - 4, y - 10, x + tw / 2 + 3, y + 9), bg); d.text((x - tw / 2, y - 8), text, font=F16, fill=fg)
    if title:
        tw = d.textlength(title, font=F16); R(d, (w / 2 - tw / 2 - 5, 8, w / 2 + tw / 2 + 4, 30), K); d.text((w / 2 - tw / 2, 11), title, font=F16, fill=GOLD)
    # compass rose
    cx, cy = w - 30, h - 34; d.polygon([(cx, cy - 16), (cx + 4, cy), (cx, cy + 16), (cx - 4, cy)], fill=WHITE); d.polygon([(cx - 16, cy), (cx, cy - 4), (cx + 16, cy), (cx, cy + 4)], fill=(200, 200, 190))
    R(d, (cx - 3, cy - 26, cx + 3, cy - 20), K); d.text((cx, cy - 23), "N", font=F8, fill=WHITE, anchor="mm")
    d.rectangle((0, 0, w - 1, h - 1), outline=(240, 220, 170), width=3)
    return outline(m)

def world_route(f, prog, labels):
    m = world_map(f, labels=labels, title="THIRD VOYAGE, 1498"); d = ImageDraw.Draw(m); w, h = m.size
    P = lambda lon, lat: (6 + (lon + 100) / 125 * (w - 12), 6 + (64 - lat) / 104 * (h - 12))
    draw_route(d, [P(*p) for p in (SEVILLE_P, CV, (-45, 9), PARIA)], prog)
    return m

# ---------------- props ----------------
def torch(d, x, base, f):
    R(d, (x, base - 70, x + 4, base), BROWN_D); R(d, (x - 3, base - 76, x + 7, base - 68), (80, 60, 40))
    fl = (f // 3) % 3
    d.polygon([(x - 4, base - 76), (x + 2, base - 96 - fl * 3), (x + 8, base - 76)], fill=(240, 120, 30))
    d.polygon([(x - 1, base - 76), (x + 2, base - 88 - fl * 2), (x + 5, base - 76)], fill=(255, 220, 90))

def barrel(d, x, base):
    d.ellipse((x, base - 34, x + 26, base), fill=(130, 84, 44)); R(d, (x + 2, base - 26, x + 24, base - 24), (70, 70, 76)); R(d, (x + 2, base - 10, x + 24, base - 8), (70, 70, 76))
    d.ellipse((x, base - 34, x + 26, base), outline=K)

def crate(d, x, base, s=30):
    R(d, (x, base - s, x + s, base), (170, 120, 60)); d.rectangle((x, base - s, x + s, base), outline=K, width=2)
    d.line([(x, base - s), (x + s, base)], fill=(120, 80, 40), width=2)

def gulls(d, f, n=4, y0=200, col=WHITE):
    for k in range(n):
        pr = random.Random(k + 40); x = (pr.randint(0, CW) + f * pr.choice((1, 2))) % (CW + 40) - 20; y = y0 + pr.randint(0, 120) + int(math.sin(f * 0.1 + k) * 6)
        wing = 4 if (f // 5 + k) % 2 else 1
        d.line([(x - 8, y - wing), (x, y), (x + 8, y - wing)], fill=col, width=2)

def clouds(d, f, y0=150, col=(250, 250, 250), n=4, speed=0.3, seed=1):
    for k in range(n):
        pr = random.Random(seed * 10 + k); x = (pr.randint(0, CW) + f * speed) % (CW + 160) - 80; y = y0 + pr.randint(0, 140)
        for dx, dy, r in ((0, 0, 18), (20, -8, 22), (42, 0, 16)): d.ellipse((x + dx - r, y + dy - r, x + dx + r, y + dy + r), fill=col)

def stars(d, n=60, ymax=500, seed=4):
    rnd = random.Random(seed)
    for _ in range(n): x, y = rnd.randint(0, CW), rnd.randint(0, ymax); R(d, (x, y, x, y), WHITE)

def town(d, base, x0=0, x1=CW, dark=False):
    rnd = random.Random(12); x = x0
    while x < x1:
        w = rnd.randint(40, 70); h = rnd.randint(40, 90); col = (60, 56, 66) if dark else (200, 186, 160)
        R(d, (x, base - h, x + w, base), col)
        if not dark:
            d.polygon([(x - 3, base - h), (x + w // 2, base - h - 14), (x + w + 3, base - h)], fill=(176, 90, 60))
            for wx in range(x + 8, x + w - 8, 16): R(d, (wx, base - h + 14, wx + 6, base - h + 24), (60, 50, 50))
        else:
            for wx in range(x + 8, x + w - 8, 16):
                if rnd.random() < 0.5: R(d, (wx, base - h + 14, wx + 5, base - h + 22), (240, 200, 90))
        x += w + rnd.randint(2, 10)

def skyline_cadiz(d, base):
    R(d, (0, base - 30, 300, base), (220, 210, 190))
    for k, (x, h) in enumerate(((10, 70), (60, 50), (110, 90), (170, 60), (230, 80))):
        R(d, (x, base - h, x + 36, base), (230, 220, 200)); R(d, (x + 6, base - h + 10, x + 12, base - h + 20), (90, 80, 70))
    d.ellipse((126, base - 130, 170, base - 86), fill=(214, 180, 90)); R(d, (146, base - 140, 150, base - 128), GOLD_D)
    for x in range(0, 300, 14): R(d, (x, base - 36, x + 8, base - 30), (200, 190, 170))

def dock(d, x1=330, y=690):
    R(d, (0, y, x1, CH), (120, 80, 46))
    for x in range(0, x1, 24): R(d, (x, y, x + 1, CH), (90, 58, 30))
    R(d, (0, y, x1, y + 4), (150, 104, 60))
    for x in range(10, x1, 80): R(d, (x, y + 4, x + 8, CH), (80, 50, 26))
    R(d, (x1 - 8, y - 20, x1, y + 40), (90, 58, 30))

def letter(d, x, y):
    R(d, (x, y, x + 20, y + 14), WHITE); d.rectangle((x, y, x + 20, y + 14), outline=K); d.line([(x, y), (x + 10, y + 8), (x + 20, y)], fill=K); R(d, (x + 8, y + 7, x + 12, y + 11), RED)

def scroll(d, x, y):
    R(d, (x, y, x + 60, y + 44), (240, 226, 180)); R(d, (x - 4, y - 4, x + 64, y + 2), (200, 170, 110)); R(d, (x - 4, y + 42, x + 64, y + 48), (200, 170, 110))
    for k in range(4): R(d, (x + 8, y + 8 + k * 8, x + 52, y + 9 + k * 8), (140, 120, 90))
    d.ellipse((x + 40, y + 30, x + 54, y + 44), fill=RED_D)

def rowboat(c, d, x, y, f, who="col"):
    d.polygon([(x, y), (x + 90, y), (x + 80, y + 14), (x + 10, y + 14)], fill=(120, 74, 38)); R(d, (x + 2, y, x + 88, y + 2), (150, 100, 56))
    put(c, who, x + 44, y + 4, crop=56); put(c, "sailor", x + 4, y + 4, crop=46)
    a = math.sin(f * 0.25) * 8; d.line([(x + 30, y - 10), (x + 22 + a, y + 22)], fill=BROWN_D, width=2)

def lightning(d, f, x0=300):
    if f % 40 < 3:
        pts = [(x0, 0)]; rnd = random.Random(f // 40)
        for k in range(6): pts.append((pts[-1][0] + rnd.randint(-30, 30), pts[-1][1] + 70))
        d.line(pts, fill=(255, 250, 200), width=4)
        return True
    return False

def big_waves(d, f, y0, col, col2):
    for x in range(-40, CW + 40, 60):
        xx = x + (f * 2) % 60; yy = y0 + int(math.sin((x + f * 4) * 0.03) * 10)
        d.polygon([(xx - 40, yy + 30), (xx, yy), (xx + 30, yy + 30)], fill=col); R(d, (xx - 6, yy, xx + 4, yy + 3), col2)

def chest(d, x, y):
    R(d, (x, y, x + 26, y + 18), (130, 80, 40)); R(d, (x, y + 6, x + 26, y + 8), GOLD); R(d, (x + 11, y + 6, x + 15, y + 12), GOLD); d.rectangle((x, y, x + 26, y + 18), outline=K)

def shallow(c, y0, y1, x0=0, x1=CW, col=(60, 180, 200)):
    lay = Image.new("RGBA", (x1 - x0, y1 - y0), col + (150,)); c.alpha_composite(lay, (x0, y0))

def foam(d, f, y, x0=0, x1=CW):
    for x in range(x0, x1, 22):
        xx = x + int(math.sin(f * 0.15 + x) * 4); R(d, (xx, y, xx + 12, y + 2), WHITE)

def thatched_wreck(flip=False):
    s = SP["wreck"].copy(); d = ImageDraw.Draw(s)
    d.polygon([(40, 92), (80, 70), (120, 92)], fill=(200, 170, 90)); R(d, (46, 92, 114, 100), (150, 110, 60))
    s = outline(s)
    return s.transpose(Image.FLIP_LEFT_RIGHT) if flip else s
SP["hutwreck"] = thatched_wreck(); SP["hutwreck2"] = thatched_wreck(True)

def candle(d, x, base, f):
    R(d, (x, base - 24, x + 8, base), (240, 230, 200)); fl = (f // 4) % 2
    d.polygon([(x + 1, base - 24), (x + 4, base - 36 - fl * 3), (x + 7, base - 24)], fill=(255, 200, 60)); R(d, (x - 4, base - 2, x + 12, base), GOLD_D)

def window(d, x, y, w, h, night=True, f=0, moon_shade=0.0):
    R(d, (x - 6, y - 6, x + w + 6, y + h + 6), (90, 58, 30))
    if night:
        R(d, (x, y, x + w, y + h), (16, 20, 50)); rnd = random.Random(3)
        for k in range(10): px, py = x + (k * 37) % (w - 6) + 3, y + (k * 23) % (h - 6) + 3; R(d, (px, py, px, py), WHITE)
    else:
        R(d, (x, y, x + w, y + h), (150, 200, 240)); town(d, y + h, x, x + w)
    R(d, (x + w // 2 - 2, y, x + w // 2 + 2, y + h), (90, 58, 30)); R(d, (x, y + h // 2 - 2, x + w, y + h // 2 + 2), (90, 58, 30))

def castile_banner(d, x, y):
    R(d, (x, y, x + 50, y + 80), (190, 30, 40)); R(d, (x + 14, y + 26, x + 36, y + 52), GOLD); R(d, (x + 12, y + 20, x + 38, y + 26), GOLD)
    for k in range(3): R(d, (x + 12 + k * 10, y + 14, x + 18 + k * 10, y + 20), GOLD)
    R(d, (x + 22, y + 40, x + 28, y + 52), (120, 70, 20)); R(d, (x - 4, y - 4, x + 54, y), GOLD_D)

def aragon_banner(d, x, y):
    R(d, (x, y, x + 50, y + 80), GOLD)
    for k in range(4): R(d, (x + 4 + k * 12, y, x + 9 + k * 12, y + 80), (190, 30, 40))
    R(d, (x - 4, y - 4, x + 54, y), GOLD_D)

def bonfire(d, x, base, f):
    for k in range(3): R(d, (x - 20 + k * 12, base - 6, x - 6 + k * 12, base), BROWN_D)
    fl = (f // 3) % 3
    d.polygon([(x - 18, base - 6), (x - 2, base - 50 - fl * 4), (x + 18, base - 6)], fill=(230, 90, 30))
    d.polygon([(x - 9, base - 6), (x, base - 34 - fl * 3), (x + 9, base - 6)], fill=(255, 210, 80))

def bed(c, d, x, base):
    R(d, (x, base - 50, x + 220, base - 26), (120, 74, 38)); R(d, (x, base - 26, x + 8, base), (90, 58, 30)); R(d, (x + 212, base - 26, x + 220, base), (90, 58, 30))
    R(d, (x, base - 100, x + 12, base - 26), (90, 58, 30)); R(d, (x + 4, base - 64, x + 216, base - 50), (236, 230, 214))
    R(d, (x + 14, base - 72, x + 50, base - 58), WHITE)
    lying = SP["col"].rotate(90, resample=Image.NEAREST, expand=True); c.alpha_composite(lying, (x + 12, base - 100))
    R(d, (x + 60, base - 74, x + 216, base - 52), (150, 40, 50)); d.rectangle((x + 60, base - 74, x + 216, base - 52), outline=K)

def hunger_crew(c, x0, base, n=3):
    for k in range(n): put(c, "sailor", x0 + k * 46, base)

# ---------------- backgrounds ----------------
def night_sea(d, horizon=600):
    sea(d, (10, 14, 40), (60, 70, 120), horizon, (20, 30, 70), (80, 100, 160)); stars(d)

def day_sea(d, horizon=600):
    sea(d, (80, 160, 230), (200, 225, 250), horizon, (40, 110, 170), (200, 230, 250))

def court(d):
    grad(d, (60, 20, 24), (110, 40, 40), 0, GY, 12)
    for x in range(30, CW, 120): R(d, (x, 120, x + 24, GY), (140, 110, 80)); R(d, (x - 4, 116, x + 28, 128), (170, 140, 100))
    R(d, (0, GY, CW, CH), (120, 30, 36)); R(d, (150, GY, 390, CH), (170, 40, 46))
    for x in range(0, CW, 40): R(d, (x, GY, x + 1, CH), (90, 20, 26))

def jamaica_bay(d, sky=None):
    if sky == "sunset": sea(d, (250, 150, 90), (250, 210, 150), 560, (40, 110, 170), (240, 200, 160))
    elif sky == "night": sea(d, (10, 14, 40), (50, 60, 100), 560, (20, 40, 70), (80, 100, 150)); stars(d, 40, 480)
    else: sea(d, (80, 170, 240), (200, 230, 250), 560, (40, 150, 190), (200, 240, 240))
    night = sky == "night"
    d.polygon([(380, 560), (440, 520), (500, 530), (CW, 545), (CW, 560)], fill=(30, 50, 40) if night else (80, 130, 80))
    sand = (120, 108, 76) if night else (236, 214, 150)
    d.polygon([(250, 690), (CW, 640), (CW, CH), (0, CH), (0, 760)], fill=sand)
    rnd = random.Random(8)
    for _ in range(70):
        x, y = rnd.randint(0, CW), rnd.randint(700, CH)
        if y > 690 - (x - 250) * 50 / 290: R(d, (x, y, x + 1, y), (100, 90, 60) if night else (210, 186, 124))
    palm(d, 480, 660, 210, -1); palm(d, 400, 668, 150, 1)

def cabin(d):
    grad(d, (70, 44, 24), (110, 72, 40), 0, CH, 10)
    for y in range(0, CH, 32): R(d, (0, y, CW, y + 1), (60, 36, 18))
    R(d, (0, GY, CW, CH), (90, 58, 30))
    for x in range(0, CW, 40): R(d, (x, GY, x + 1, CH), (60, 36, 18))

def village(d):
    sea(d, (80, 170, 240), (200, 230, 250), 560, (40, 150, 190), (200, 240, 240))
    R(d, (0, 620, CW, CH), (150, 170, 90))
    rnd = random.Random(6)
    for _ in range(80): x, y = rnd.randint(0, CW), rnd.randint(624, CH); R(d, (x, y, x + 2, y), (120, 146, 70))
    palm(d, 500, 630, 200, -1)

def room(d):
    grad(d, (120, 112, 100), (160, 150, 136), 0, GY, 10)
    for y in range(0, GY, 28):
        for x in range((y // 28 % 2) * 30, CW, 60): R(d, (x, y, x, y + 27), (110, 102, 92))
        R(d, (0, y, CW, y), (110, 102, 92))
    R(d, (0, GY, CW, CH), (110, 80, 50))
    for x in range(0, CW, 36): R(d, (x, GY, x + 1, CH), (80, 56, 34))

def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0 or (i == 3 and li == 0):
        night_sea(d); d.ellipse((420, 120, 466, 166), fill=(236, 236, 214)); town(d, 600, 0, 260, dark=True); dock(d)
    elif i == 1:
        grad(d, (24, 44, 70), (60, 90, 120), 0, 560, 12)
        if li == 0: day_sea(d, 560)
        else:
            R(d, (0, 560, CW, CH), (196, 176, 120)); town(d, 610, 0, CW)
            rnd = random.Random(8)
            for _ in range(60): x, y = rnd.randint(0, CW), rnd.randint(612, CH); R(d, (x, y, x + 1, y), (170, 150, 100))
    elif i == 2:
        day_sea(d, 600); town(d, 600, 0, 300); R(d, (0, 600, 300, 690), (196, 176, 120)); dock(d)
    elif i == 3:
        court(d)
    elif i == 4:
        if li == 0: day_sea(d, 600); skyline_cadiz(d, 600)
        elif li == 1:
            day_sea(d, 600); town(d, 600, 0, 200); dock(d, 200)
        else: sea(d, (20, 22, 30), (60, 64, 76), 600, (24, 40, 50), (110, 120, 130))
    elif i == 5:
        if li == 0: grad(d, (24, 44, 70), (60, 90, 120), 0, 560, 12); day_sea(d, 560)
        elif li == 1: jamaica_bay(d)
        else: day_sea(d, 600)
    elif i == 6:
        if li == 0: village(d)
        elif li == 1: cabin(d)
        else: jamaica_bay(d, "night")
    elif i == 7:
        if li == 0: jamaica_bay(d, "sunset")
        else: room(d)
    return c

# ---------------- scenes ----------------
def guards(c, xs, f, flip=False):
    for k, x in enumerate(xs): put(c, f"esp{st(f, k, 12)}", x, FEET, sc=2, flip=flip)

def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        waves(d, f, 600, (80, 100, 160))
        put(c, "ship", 350, 700 + bob(f, 3, 0.1), k=0.85)
        for k in range(2): put(c, "sailor", 372 + k * 70, 650 + bob(f, 3, 0.1), crop=50)
        torch(d, 6, 690, f); torch(d, 316, 690, f); barrel(d, 290, 700); crate(d, 30, 700)
        if li == 0:
            put(c, "esp0", -20, FEET, sc=2); put(c, "colc", 96, FEET, sc=2); put(c, "esp1", 206, FEET, sc=2, flip=True)
            label(d, "COLUMBUS", 148, 500, GOLD); label(d, "GUARD", 40, 545, WHITE, K); label(d, "GUARD", 262, 545, WHITE, K)
            label(d, "HISPANIOLA, 1500", 270, 250, K, YEL, F16); label(d, "SHIP", 430, 520, GOLD)
        else:
            put(c, "bob", -10, FEET, sc=2); put(c, "colc", 96, FEET, sc=2); put(c, "esp1", 206, FEET, sc=2, flip=True)
            label(d, "BOBADILLA", 42, 545, GOLD); label(d, "COLUMBUS", 148, 500, GOLD)
            scroll(d, 60, 380 + bob(f, 3, 0.08)); label(d, "ROYAL ORDER", 90, 350, WHITE, RED_D)
            label(d, "ARRESTED", 380, 250, WHITE, RED, F16); label(d, "BY ROYAL ORDER", 380, 290, K, YEL, F16)
    elif i == 1:
        if li == 0:
            c.alpha_composite(world_route(f, min(1, prog * 1.3), [("SPAIN", -4, 42, K, YEL), ("AFRICA", 15, 5, K, YEL), ("SOUTH AMERICA", -60, -12, K, YEL)]), (25, 110))
            waves(d, f, 560, (200, 230, 250)); gulls(d, f, 3, 560, WHITE)
            put(c, "ship", 40 + prog * 220, 720 + bob(f, 3, 0.1)); label(d, "COLUMBUS'S SHIP", 120 + prog * 220, 570, GOLD)
            if prog > 0.75: label(d, "SOUTH AMERICAN MAINLAND!", 270, 535, WHITE, RED_D, F16)
        else:
            c.alpha_composite(region_map(f, (-80, -58, 8, 22), h=380, route=([PARIA, (-64, 11.6), (-68, 15), STODOM], min(1, prog * 1.4)),
                labels=[("HISPANIOLA", -71, 20.4, K, YEL), ("SANTO DOMINGO", -66, 17.6, WHITE, K), ("PARIA", -63.5, 9.5, K, YEL), ("JAMAICA", -77.2, 16.9, WHITE, K)],
                dots=[STODOM], title="BACK TO HISPANIOLA"), (25, 110))
            put(c, "col", 200, FEET, sc=2); label(d, "GOVERNOR COLUMBUS", 252, 545, GOLD)
            put(c, "esp0", 330, FEET); put(c, "esp1", 380, FEET); label(d, "SOLDIERS", 380, 620, WHITE, K)
            put(c, "set1", 20, FEET); put(c, "set2", 80, FEET, flip=True); label(d, "SETTLERS", 76, 620, WHITE, K)
            R(d, (470, 520, 473, FEET), BROWN_D); castile_banner(d, 474, 524)
    elif i == 2:
        waves(d, f, 600, (200, 230, 250)); gulls(d, f, 3, 180)
        if li == 0:
            put(c, "ship", 360, 700 + bob(f, 3, 0.1)); label(d, "TO SPAIN", 440, 520, GOLD)
            pos = [(-10, "set1", False), (70, "set2", True), (150, "set1", True)]
            for x, key, fl in pos: put(c, key, x, FEET, sc=2, flip=fl)
            label(d, "SETTLERS", 120, 545, GOLD)
            bubble(d, "UNFAIR!", 60, 470); bubble(d, "TOO HARSH!", 210, 430) if prog > 0.25 else None
            for k in range(3):
                ph = (prog * 1.5 + k * 0.33) % 1; x = 160 + ph * 260; y = 520 - math.sin(ph * math.pi) * 160
                letter(d, x, y)
            label(d, "COMPLAINTS TO SPAIN", 270, 250, K, YEL, F16)
        else:
            x = 520 - min(1, prog * 2) * 170; put(c, "ship", x, 700 + bob(f, 3, 0.1)); put(c, "sailor", x + 30, 650, crop=50)
            put(c, "bob", 120, FEET, sc=2); label(d, "BOBADILLA", 172, 545, GOLD)
            guards(c, [10], f)
            put(c, "esp1", 230, FEET, sc=2, flip=True); label(d, "SOLDIERS", 60, 500, WHITE, K)
            scroll(d, 240, 400) if prog > 0.5 else None
            label(d, "ROYAL JUDGE", 330, 250, K, YEL, F16); label(d, "AUGUST 1500", 330, 290, WHITE, K, F16)
    elif i == 3:
        if li == 0:
            waves(d, f, 600, (80, 100, 160))
            sy = bob(f, 3, 0.1); put(c, "ship", 350, 700 + sy, k=0.85)
            d.polygon([(310, 690), (360, 652 + sy), (366, 658 + sy), (316, 696)], fill=(150, 104, 60))
            torch(d, 6, 690, f); torch(d, 316, 690, f)
            put(c, "bob", -10, FEET, sc=2); label(d, "BOBADILLA", 42, 545, GOLD)
            x = 90 + prog * 150; put(c, "colc", x, FEET, sc=2); label(d, "COLUMBUS", x + 52, 500, GOLD)
            label(d, "OCTOBER 1500", 330, 250, K, YEL, F16); label(d, "BACK TO SPAIN", 330, 290, WHITE, RED, F16)
        else:
            castile_banner(d, 60, 150); aragon_banner(d, 430, 150)
            R(d, (20, 640, 280, 700), (170, 140, 100)); R(d, (20, 636, 280, 642), GOLD_D)
            for x in (40, 150):
                R(d, (x, 520, x + 90, 640), (150, 30, 40)); R(d, (x - 4, 510, x + 94, 524), GOLD)
            put(c, "ferd", 50, 680, sc=2); put(c, "isa", 160, 680, sc=2)
            label(d, "FERDINAND", 102, 460, GOLD); label(d, "ISABELLA", 212, 420, GOLD)
            freed = prog > 0.35
            put(c, "col" if freed else "colc", 380, FEET, sc=2, flip=True); label(d, "COLUMBUS", 432, 545, GOLD)
            if freed:
                for k in range(6): R(d, (390 + k * 14, FEET - 4, 398 + k * 14, FEET), CHAIN)
                label(d, "FREE", 432, 300, K, YEL, F16)
            if prog > 0.6: label(d, "NO LONGER GOVERNOR", 300, 340, WHITE, RED, F16)
    elif i == 4:
        if li == 0:
            clouds(d, f, 140); gulls(d, f, 4, 300, (40, 40, 40))
            waves(d, f, 600, (200, 230, 250))
            for k in range(4):
                put(c, "ship" if k == 0 else tint(SP["ship"], 0.85), 120 + k * 105 - t * 3, 680 + (k % 2) * 30 + bob(f, 3, 0.1, k))
            label(d, "CÁDIZ", 150, 420, GOLD)
            label(d, "MAY 1502: FOUR SHIPS", 270, 250, K, YEL, F16)
        elif li == 1:
            dark = min(1, prog * 1.5)
            for k in range(5):
                pr = random.Random(k); cx = 540 - dark * 200 + k * 60; cy = 120 + pr.randint(0, 80)
                for dx, dy, r in ((0, 0, 30), (34, -10, 36), (70, 0, 28)): d.ellipse((cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r), fill=(70, 74, 86))
            for k in range(8): put(c, tint(SP["ship"], 0.6).resize((80, 65), Image.NEAREST), 210 + k * 40, 612 + (k % 2) * 6)
            label(d, "TREASURE FLEET", 380, 530, WHITE, K)
            waves(d, f, 600, (200, 230, 250))
            put(c, "ovando", 20, FEET, sc=2); label(d, "GOVERNOR OVANDO", 120, 545, GOLD); put(c, "esp0", 130, FEET)
            rowboat(c, d, 300, 730 + bob(f, 3, 0.1), f); label(d, "COLUMBUS", 360, 640, GOLD)
            bubble(d, "HURRICANE COMING!", 370, 460)
            if prog > 0.5: bubble(d, "NONSENSE.", 90, 400)
            label(d, "SANTO DOMINGO", 270, 250, K, YEL, F16)
        else:
            flash = lightning(d, f, 120 + (f // 40) * 97 % 300)
            rain(d, f)
            for k in range(5):
                sink = 0.65 * min(1, max(0, prog * 1.6 - k * 0.15)); x = -10 + k * 110
                im = SP["ship"].rotate(-14 + 28 * (k % 2) + int(math.sin(f * 0.2 + k) * 6), resample=Image.NEAREST, expand=True)
                im = im.crop((0, 0, im.width, max(1, int(im.height * (1 - sink * 0.85)))))
                put(c, tint(im, 0.6), x, 680 + int(sink * 50) + bob(f, 6, 0.2, k))
            big_waves(d, f, 640, (30, 50, 64), (180, 190, 200))
            for k in range(3): chest(d, 80 + k * 150 + int(math.sin(f * 0.1 + k) * 10), 700 + bob(f, 5, 0.15, k))
            label(d, "BOBADILLA'S SHIP", 120, 470, GOLD)
            label(d, "~20 SHIPS LOST", 270, 250, WHITE, RED, F16); label(d, "~500 DEAD", 270, 290, WHITE, K, F16)
            if flash: R(d, (0, 0, CW, 6), WHITE)
    elif i == 5:
        if li == 0:
            route = [STODOM, (-73, 17.4), (-77, 17.3), (-85.9, 16.5), (-84, 16.2), (-82.9, 15.1), (-83.2, 12.5), (-83.3, 11), (-82.6, 10.1),
                     (-82.0, 9.3), (-80, 9.6), (-79.0, 9.6), (-77.5, 13), (-75.9, 17.9), (-76.4, 18.55), (-77.2, 18.42)]
            c.alpha_composite(region_map(f, (-90, -66, 7, 22), h=400, route=(route, min(1, prog * 1.15)),
                labels=[("HONDURAS", -87.5, 14.4, K, YEL), ("COSTA RICA", -86.5, 9.3, K, YEL), ("PANAMA", -79.5, 7.9, K, YEL), ("JAMAICA", -81.5, 18.2, WHITE, K), ("HISPANIOLA", -71, 17.3, K, YEL)],
                title="FOURTH VOYAGE, 1502-03"), (25, 110))
            waves(d, f, 560, (200, 230, 250))
            for k in range(6): palm(d, 20 + k * 90, 600, 40 + (k % 3) * 10, 1 if k % 2 else -1)
            R(d, (0, 590, CW, 604), (90, 130, 70))
            put(c, "ship", 200 + math.sin(t * 0.3) * 20, 720 + bob(f, 3, 0.1)); label(d, "CENTRAL AMERICAN COAST", 270, 640, WHITE, K)
        elif li == 1:
            for x, key in ((-10, "hutwreck"), (150, "hutwreck2")): put(c, key, x, 726 - (x > 0) * 6)
            shallow(c, 700, 760, 0, 330); foam(d, f, 700, 0, 300); foam(d, f + 30, 744, 0, 260)
            for k in range(3): put(c, "sailor", 300 + k * 40, FEET - 20 + k * 6)
            put(c, "col", 440, FEET - 4); label(d, "COLUMBUS", 466, 600, GOLD); label(d, "CREW", 340, 580, WHITE, K)
            label(d, "JAMAICA, 1503", 270, 250, K, YEL, F16); label(d, "RUN AGROUND", 270, 290, WHITE, RED, F16)
            label(d, "SHIPWORMS!", 140, 440, WHITE, K)
            for k in range(5): R(d, (40 + k * 50 + (f // 6 + k) % 6, 640 + (k % 2) * 16, 46 + k * 50 + (f // 6 + k) % 6, 642 + (k % 2) * 16), (230, 220, 200))
        else:
            waves(d, f, 600, (200, 240, 240)); gulls(d, f, 2, 520)
            c.alpha_composite(region_map(f, (-79, -68, 16.5, 20.5), w=490, h=250, route=([(-76.2, 18.0), (-75.3, 18.1), (-74.45, 18.4)], min(1, prog * 1.2)),
                labels=[("JAMAICA", -77.3, 17.2, K, YEL), ("HISPANIOLA", -71.5, 19.9, K, YEL)], title="ABOUT 450 MILES BY CANOE"), (25, 110))
            x = 30 + prog * 230; y = 690 + bob(f, 4, 0.12)
            for j in range(2):
                put(c, "sailor", x + 20 + j * 90, y + 8, sc=2, crop=46); a = math.sin(f * 0.25 + j) * 14
                d.line([(x + 90 + j * 90, y - 40), (x + 80 + j * 90 + a, y + 36)], fill=BROWN_D, width=4)
            d.polygon([(x, y), (x + 220, y), (x + 196, y + 28), (x + 24, y + 28)], fill=(120, 74, 38)); R(d, (x + 4, y, x + 216, y + 4), (150, 100, 56))
            label(d, "MÉNDEZ", x + 72, y - 120, GOLD); label(d, "FIESCHI", x + 162, y - 150, GOLD)
    elif i == 6:
        if li == 0:
            for k in range(3): hut(d, 250 + k * 90, 640, 60)
            put(c, "col", 10, FEET, sc=2); label(d, "COLUMBUS", 62, 545, GOLD)
            hunger_crew(c, 110, FEET, 2); label(d, "HUNGRY CREW", 156, 600, WHITE, K)
            for k in range(3):
                x = 250 + k * 80 + prog * 60; put(c, f"tai{st(f, k, 7)}", x, FEET, flip=False)
                put(c, "bask0", x + 10, FEET - 50, crop=26)
            label(d, "TAINO", 360, 610, GOLD); label(d, "NO MORE FOOD", 270, 250, WHITE, RED, F16)
        elif li == 1:
            window(d, 330, 160, 150, 120); draw_moon(c, 405, 210, 22, 0)
            R(d, (120, 560, 420, 580), (130, 84, 44)); R(d, (140, 580, 156, FEET), (100, 64, 30)); R(d, (384, 580, 400, FEET), (100, 64, 30))
            almanac(d, 170, 430); candle(d, 390, 560, f)
            label(d, "ALMANAC", 270, 400, GOLD)
            put(c, "col", 10, FEET, sc=2); label(d, "COLUMBUS", 62, 545, GOLD)
            label(d, "ECLIPSE: FEB 29, 1504", 270, 330, K, YEL, F16)
        else:
            shade = min(1, prog * 1.6); draw_moon(c, 270, 220, 56, shade)
            bonfire(d, 270, FEET, f)
            put(c, "col", -10, FEET, sc=2); label(d, "COLUMBUS", 42, 545, GOLD)
            for k in range(3): put(c, f"tai{k % 2}", 330 + k * 60, FEET - (k % 2) * 8, flip=True)
            label(d, "TAINO", 420, 620, GOLD)
            if prog > 0.7:
                for k in range(3): put(c, "bask", 120 + k * 36, FEET - (k % 2) * 6)
                label(d, "FOOD IS BACK", 270, 420, K, YEL, F16)
            else: label(d, "THE MOON DARKENS", 270, 420, WHITE, RED_D, F16)
    elif i == 7:
        if li == 0:
            put(c, "hutwreck", -10, 724, k=0.8); shallow(c, 700, 760, 0, 330); foam(d, f, 700, 0, 300)
            x = 520 - min(1, prog * 1.6) * 200; put(c, "ship", x, 615 + bob(f, 3, 0.1)); label(d, "RESCUE SHIP", x + 80, 460, GOLD)
            gulls(d, f, 3, 300, (60, 40, 40))
            for k in range(3):
                put(c, "sailor", 280 + k * 46, FEET + (k % 2) * 6 - (6 if (f // 8 + k) % 2 else 0))
            put(c, "col", 440, FEET); label(d, "COLUMBUS", 466, 600, GOLD); label(d, "SURVIVORS", 340, 570, WHITE, K)
            label(d, "RESCUED: JUNE 1504", 270, 250, K, YEL, F16)
        else:
            window(d, 360, 200, 130, 140, night=False)
            R(d, (80, 160, 84, 230), BROWN_D); R(d, (66, 176, 98, 180), BROWN_D)
            bed(c, d, 60, FEET); candle(d, 300, FEET - 60, f); R(d, (290, FEET - 60, 330, FEET), (110, 70, 34))
            label(d, "COLUMBUS", 170, 600, GOLD)
            label(d, "VALLADOLID, 1506", 190, 260, K, YEL, F16)
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
