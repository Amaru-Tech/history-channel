import os, sys
D = os.environ.get("HC_DIR", os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")
_src = open(f"{D}/build4.py").read().split("# ---------------- render ----------------")[0]
sys_argv_backup = list(sys.argv); sys.argv = [sys.argv[0]]
exec(_src)  # engine, sprites, maps, overlay, compose, music, tts from episode 1
_src5 = open(f"{D}/build5.py").read().split("# ---------------- extra sprites ----------------")[1].split("# ---------------- backgrounds ----------------")[0]
exec(_src5)  # episode 2 sprites: Taino chiefs, sleeper, Caribbean map, fort, canoe, reef
sys.argv = sys_argv_backup
CHECK = "check" in sys.argv
OUT = f"{D}/out_ep03"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep03_return_with_an_army_EN.mp4"

SCENES = [
 ("SEPTEMBER 1493", [
  ("Columbus came back to the New World with an army, and a farm.", "Columbus came back to the New World with an army, and a farm."),
  ("In September fourteen ninety-three, he left Kadeez with seventeen ships and more than twelve hundred men.", "Sept 1493: he left Cádiz with 17 ships and over 1,200 men.")]),
 ("A FLOATING FARM", [
  ("The ships carried horses, wheat and sugarcane.", "The ships carried horses, wheat and sugarcane."),
  ("At La Gomaira, in the Canary Islands, Columbus bought eight pigs.", "At La Gomera, in the Canary Islands, Columbus bought eight pigs.")]),
 ("NOVEMBER 1493", [
  ("On November third, the fleet sighted the island of Domineeka.", "November 3: the fleet sighted the island of Dominica."),
  ("At Hispaniola, bad news waited. The fort he had left there was burned, and its men were dead.", "At Hispaniola, bad news waited. The fort he left there was burned, and its men were dead.")]),
 ("LA ISABELA", [
  ("In January fourteen ninety-four, he founded a town on the north coast, and named it La Eesabella, after the queen.", "January 1494: he founded a town on the north coast, La Isabela, named after the queen."),
  ("It had a church, a plaza, and a stone house for Columbus.", "It had a church, a plaza, and a stone house for Columbus.")]),
 ("HUNGER AND FEVER", [
  ("But food ran short, and disease spread through the camp.", "But food ran short, and disease spread through the camp."),
  ("Hunger and sickness pushed some settlers to mutiny.", "Hunger and sickness pushed some settlers to mutiny.")]),
 ("CUBA IS ASIA?", [
  ("In April fourteen ninety-four, Columbus sailed off to explore Cuba and Jamaica.", "April 1494: Columbus sailed off to explore Cuba and Jamaica."),
  ("He was sure Cuba was part of Asia. On June twelfth, he made his men swear an oath: Cuba was the mainland.", "He was sure Cuba was part of Asia. On June 12 he made his men swear it was the mainland.")]),
 ("HURRICANES", [
  ("Back at La Eesabella, hurricanes struck in fourteen ninety-four and fourteen ninety-five.", "Back at La Isabela, hurricanes struck in 1494 and 1495."),
  ("In June fourteen ninety-five, a storm sank several ships in the harbor.", "In June 1495, a storm sank several ships in the harbor.")]),
 ("THE PIGS STAYED", [
  ("In March fourteen ninety-six, Columbus sailed home. He reached Kadeez in June.", "March 1496: Columbus sailed home. He reached Cádiz in June."),
  ("The pigs stayed behind. They multiplied fast, and were used to stock islands across the Caribbean.", "The pigs stayed. They multiplied fast and were used to stock islands across the Caribbean."),
  ("La Eesabella was soon abandoned. The pigs had come to stay.", "La Isabela was soon abandoned. The pigs had come to stay.")]),
]

_label_orig = label
def label(d, text, cx, y, fg=WHITE, bg=K, font=F16):
    w = d.textlength(text, font=font); cx = min(max(cx, w / 2 + 8), CW - w / 2 - 8)
    _label_orig(d, text, cx, y, fg, bg, font)

# ---------------- extra sprites ----------------
PINK = (232, 160, 150); PINK_D = (190, 112, 106)
def pig(step=0):
    im = Image.new("RGBA", (44, 30)); d = ImageDraw.Draw(im)
    xs = (8, 14, 28, 34) if step == 0 else (6, 16, 26, 36)
    for x in xs: R(d, (x, 20, x + 3, 27), PINK_D)
    d.ellipse((4, 6, 38, 24), fill=PINK); d.ellipse((6, 16, 36, 24), fill=PINK_D)
    R(d, (32, 8, 42, 18), PINK); R(d, (40, 11, 43, 16), PINK_D); R(d, (41, 12, 41, 12), K); R(d, (41, 15, 41, 15), K)
    R(d, (35, 10, 36, 11), K); d.polygon([(32, 8), (34, 2), (37, 8)], fill=PINK_D)
    d.line([(4, 12), (1, 9), (3, 6)], fill=PINK_D, width=2)
    return outline(im)

def friar():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, (120, 84, 50), (90, 60, 34)); R(d, (17, 56, 35, 58), WHITE)
    R(d, (24, 40, 27, 52), WHITE); R(d, (21, 44, 30, 46), WHITE)
    face(d); R(d, (17, 12, 35, 17), (90, 60, 34)); R(d, (16, 16, 19, 30), (90, 60, 34)); R(d, (33, 16, 36, 30), (90, 60, 34))
    return outline(im)

def sack(col=(214, 190, 130)):
    im = Image.new("RGBA", (30, 34)); d = ImageDraw.Draw(im)
    d.ellipse((2, 8, 28, 33), fill=col); R(d, (10, 2, 20, 10), col); R(d, (9, 8, 21, 10), BROWN_D)
    for k in range(3): R(d, (8 + k * 6, 0, 9 + k * 6, 2), (200, 170, 60))
    return outline(im)

def cane():
    im = Image.new("RGBA", (40, 80)); d = ImageDraw.Draw(im)
    for k, x in enumerate(range(6, 34, 6)):
        R(d, (x, 12 + k % 2 * 4, x + 3, 78), (110, 160, 70))
        for y in range(20, 78, 12): R(d, (x, y, x + 3, y + 1), (70, 110, 40))
        d.polygon([(x + 1, 14 + k % 2 * 4), (x - 6, 0), (x + 4, 10)], fill=(80, 150, 60))
    R(d, (4, 50, 36, 54), BROWN)
    return outline(im)

SP.update({"pig0": pig(0), "pig1": pig(1), "friar": friar(), "sack": sack(), "cane": cane(), "horse": horse()})

LA_ISABELA = (-71.08, 19.9)
CADIZ = (-6.3, 36.5); GOMERA = (-17.2, 28.1); DOMINICA = (-61.35, 15.4)

def carib_map2(f, labels=(), route=None, title=None, isa=True):
    m = carib_map(f, labels=(), dot=False, route=route, title=title); d = ImageDraw.Draw(m); d.fontmode = "1"
    w, h = m.size; P = lambda lon, lat: (6 + (lon + 86) / 22 * (w - 12), 6 + (28.5 - lat) / 13 * (h - 12))
    if isa:
        x, y = P(*LA_ISABELA); on = (f // 10) % 2 == 0
        R(d, (x - 4, y - 4, x + 4, y + 4), RED if on else WHITE); d.rectangle((x - 4, y - 4, x + 4, y + 4), outline=K)
    for text, lon, lat, fg, bg in labels:
        x, y = P(lon, lat); tw = d.textlength(text, font=F16); x = min(max(x, tw / 2 + 8), w - tw / 2 - 8)
        R(d, (x - tw / 2 - 4, y - 10, x + tw / 2 + 3, y + 9), bg); d.text((x - tw / 2, y - 8), text, font=F16, fill=fg)
    return m

# ---------------- props ----------------
def hut(d, x, base, w=60, burned=False):
    R(d, (x, base - 40, x + w, base), (150, 110, 70)); R(d, (x + w // 2 - 7, base - 24, x + w // 2 + 7, base), (60, 40, 26))
    d.polygon([(x - 8, base - 38), (x + w // 2, base - 76), (x + w + 8, base - 38)], fill=(200, 170, 90))
    for k in range(4): d.line([(x - 4 + k * (w + 8) // 3, base - 40), (x + w // 2, base - 74)], fill=(160, 130, 60))

def church(d, x, base):
    R(d, (x, base - 110, x + 90, base), (210, 200, 180)); d.polygon([(x - 6, base - 108), (x + 45, base - 150), (x + 96, base - 108)], fill=(170, 80, 60))
    R(d, (x + 32, base - 46, x + 58, base), (90, 60, 34)); R(d, (x + 43, base - 186, x + 47, base - 150), K); R(d, (x + 35, base - 176, x + 55, base - 172), K)

def stone_house(d, x, base):
    R(d, (x, base - 100, x + 110, base), (160, 156, 146))
    for y in range(base - 100, base, 14):
        for xx in range(x + (0 if (y // 14) % 2 else 10), x + 110, 22): R(d, (xx, y, xx, y + 13), (120, 116, 108))
        R(d, (x, y, x + 110, y), (120, 116, 108))
    R(d, (x - 4, base - 108, x + 114, base - 100), (130, 126, 118)); R(d, (x + 44, base - 50, x + 66, base), (80, 50, 30))
    R(d, (x + 14, base - 80, x + 30, base - 62), K); R(d, (x + 80, base - 80, x + 96, base - 62), K)

def rain(d, f, col=(170, 190, 220)):
    for k in range(90):
        pr = random.Random(k); x = (pr.randint(0, CW + 200) - f * 6) % (CW + 200) - 100; y = (pr.randint(0, CH) + f * 22) % CH
        d.line([(x, y), (x - 6, y + 18)], fill=col, width=1)

def pigs(c, f, n, x0, y0, dx=50, dy=0, speed=1.5, seed=0):
    for k in range(n):
        x = x0 + k * dx + (f * speed + k * 37) % 40 - 20; put(c, f"pig{st(f, k, 5)}", x, y0 + (k % 3) * dy, flip=(k % 2 == 1))

# ---------------- backgrounds ----------------
def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0:
        sea(d, (250, 170, 90), (250, 220, 170), 600, (40, 90, 150), (240, 200, 160))
        for k, x in enumerate(range(0, CW, 70)): R(d, (x, 520 - (k % 3) * 20, x + 60, 600), (230, 210, 170)); R(d, (x + 20, 560 - (k % 3) * 20, x + 34, 580 - (k % 3) * 20), (120, 90, 60))
        d.polygon([(380, 500), (420, 440), (460, 500)], fill=(200, 180, 140)); R(d, (380, 500, 460, 600), (220, 200, 160))
        R(d, (0, 700, CW, CH), (120, 80, 46))
        for x in range(0, CW, 24): R(d, (x, 700, x + 1, CH), (90, 58, 30))
        R(d, (0, 700, CW, 704), (150, 104, 60))
    elif i == 1 and li == 0:
        grad(d, (40, 30, 26), (90, 64, 44), 0, CH, 12)
        R(d, (0, GY, CW, CH), (110, 72, 40))
        for x in range(0, CW, 30): R(d, (x, GY, x + 1, CH), (80, 50, 26))
        for y in (200, 330): R(d, (0, y, CW, y + 10), (70, 46, 28))
    elif i == 1:
        sea(d, (90, 170, 240), (210, 230, 250), 560, (40, 120, 180), (200, 230, 250))
        d.polygon([(0, 560), (60, 420), (140, 330), (230, 300), (330, 350), (420, 440), (CW, 520), (CW, 560)], fill=(110, 140, 80))
        d.polygon([(140, 330), (230, 300), (330, 350), (260, 360), (200, 345)], fill=(90, 120, 66))
        R(d, (0, 640, CW, CH), (196, 176, 120))
        rnd = random.Random(8)
        for _ in range(90): x, y = rnd.randint(0, CW), rnd.randint(644, CH); R(d, (x, y, x + 1, y), (170, 150, 100))
    elif i == 2 and li == 1:
        sea(d, (90, 80, 100), (170, 150, 150), 600, (40, 70, 110), (140, 140, 160))
        R(d, (0, 680, CW, CH), (200, 182, 130))
    elif i in (2, 3, 5) and not (i == 3 and li == 1) and not (i == 5 and li == 1):
        grad(d, (24, 44, 70), (60, 90, 120), 0, CH, 12)
    elif i in (3, 4) or (i == 7 and li == 2):
        sea(d, (90, 170, 240), (210, 230, 250), 520, (40, 150, 180), (200, 240, 240))
        R(d, (0, 600, CW, CH), (150, 170, 90))
        rnd = random.Random(6)
        for _ in range(90): x, y = rnd.randint(0, CW), rnd.randint(604, CH); R(d, (x, y, x + 2, y), (120, 146, 70))
        palm(d, 490, 610, 190, -1)
        if i == 4: grad(d, (120, 110, 100), (180, 170, 150), 0, 520, 10)
    elif i == 5:
        sea(d, (80, 170, 240), (200, 230, 250), 560, (40, 170, 190), (200, 240, 240))
        R(d, (0, 640, CW, CH), (236, 214, 150)); palm(d, 470, 650, 200, -1)
    elif i == 6:
        sea(d, (30, 34, 44), (70, 76, 90), 560, (30, 50, 60), (120, 130, 140))
        for cx, cy in ((90, 140), (300, 100), (470, 180)):
            for dx, dy, r in ((0, 0, 40), (40, -14, 48), (86, 0, 36)): d.ellipse((cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r), fill=(56, 60, 70))
    elif i == 7:
        sea(d, (250, 150, 90), (250, 210, 150), 600, (40, 90, 150), (240, 200, 160))
        if li == 1: R(d, (0, 640, CW, CH), (150, 170, 90))
    return c

def tilt(key, deg):
    im = SP[key]; return im.rotate(deg, resample=Image.NEAREST, expand=True)

# ---------------- scenes ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        waves(d, f, 600, (240, 200, 160))
        if li == 0:
            put(c, "ship", 260 + t * 4, 680 + bob(f, 3, 0.1))
            put(c, "col", 40, FEET + 4, sc=2); label(d, "COLUMBUS", 92, 548, GOLD)
            put(c, "horse", 330, FEET + 4, sc=2); label(d, "AN ARMY + A FARM", 290, 290, K, YEL, F16)
        else:
            for k in range(6):
                x = 20 + k * 86 + (k % 2) * 20 - t * 3; put(c, "ship", x, 610 + (k % 2) * 60 + bob(f, 3, 0.1, k), k=0.6 + 0.08 * (k % 3))
            label(d, "CÁDIZ", 420, 400, GOLD); label(d, "17 SHIPS", 270, 290, K, YEL, F16)
            for k in range(7): put(c, f"esp{st(f, k, 9)}" if k % 2 else "sailor", 6 + k * 76, FEET + 6)
            label(d, "1,200+ MEN", 270, 330, WHITE, RED_D, F16)
    elif i == 1:
        if li == 0:
            put(c, "horse", 10, FEET, sc=2); label(d, "HORSES", 110, 570, GOLD)
            for k in range(3): put(c, "sack", 220 + k * 30, FEET, sc=2) if k < 2 else None
            put(c, "sack", 250, FEET - 56, sc=2); label(d, "WHEAT", 280, 590, GOLD)
            put(c, "cane", 380, FEET, sc=2); label(d, "SUGARCANE", 440, 560, GOLD)
            label(d, "CARGO", 270, 130, K, YEL, F16)
        else:
            label(d, "LA GOMERA", 230, 260, GOLD)
            pigs(c, f, 8 if prog > 0.3 else 4, 10, 690, dx=62, dy=22)
            label(d, "8 PIGS", 270, 600, K, YEL, F16)
    elif i == 2:
        if li == 0:
            route = ([CADIZ, GOMERA, (-40, 20), DOMINICA], min(1.0, 0.25 + prog))
            c.alpha_composite(world_map(f, route=route, labels=[("CÁDIZ", -6.3, 41, WHITE, K), ("LA GOMERA", -17, 24, WHITE, K), ("DOMINICA", -61, 10.5, K, YEL)], title="SECOND VOYAGE, 1493"), (25, 140))
            label(d, "NOV 3, 1493", 270, 620, WHITE, RED_D, F16)
        else:
            waves(d, f, 600, (140, 140, 160))
            fort(d, 190, 740, 1.0, burned=True, f=f)
            put(c, "col", 20, FEET, sc=2); label(d, "COLUMBUS", 72, 550, GOLD)
            label(d, "LA NAVIDAD", 270, 360, GOLD); label(d, "NO SURVIVORS", 270, 400, WHITE, RED, F16)
    elif i == 3:
        if li == 0:
            c.alpha_composite(carib_map2(f, labels=[("LA ISABELA", -71.1, 21.4, K, YEL), ("HISPANIOLA", -71.0, 17.0, WHITE, K), ("CUBA", -79.5, 23.6, WHITE, K)], title="JANUARY 1494"), (25, 140))
            put(c, "isa", 380, FEET, sc=2); label(d, "QUEEN ISABELLA", 400, 548, GOLD)
        else:
            church(d, 20, 640); label(d, "CHURCH", 65, 440, GOLD)
            stone_house(d, 380, 640); label(d, "COLUMBUS'S HOUSE", 400, 500, GOLD)
            hut(d, 170, 620); hut(d, 260, 610, 50)
            R(d, (120, 650, 420, 700), (200, 190, 150)); label(d, "PLAZA", 270, 668, K, YEL)
            put(c, "friar", 80, 760); label(d, "FRIAR", 106, 770, WHITE)
            put(c, "col", 330, 780); put(c, "esp0", 210, 790)
    elif i == 4:
        hut(d, 30, 610); hut(d, 380, 610)
        if li == 0:
            for k in range(3): c.alpha_composite(SP["sleeper"], (60 + k * 140, 680 + (k % 2) * 40))
            put(c, "sack", 420, 800, k=0.6); put(c, "sack", 450, 806, k=0.6)
            label(d, "FOOD RAN SHORT", 270, 300, WHITE, K, F16); label(d, "FEVER", 270, 340, WHITE, RED_D, F16)
        else:
            for k in range(4): put(c, f"esp{st(f, k, 5)}", 20 + k * 70, FEET + 20)
            put(c, "piz0", 420, FEET + 20, flip=True); label(d, "OFFICER", 446, 650, GOLD)
            bubble(d, "WE ARE STARVING!", 170, 560)
            label(d, "MUTINY", 270, 300, WHITE, RED, F16)
    elif i == 5:
        if li == 0:
            route = ([LA_ISABELA, (-74.2, 20.6), (-77.5, 20.2), (-78.0, 18.8), (-77.3, 19.6), (-80.5, 21.2), (-83, 21.7)], min(1.0, 0.2 + prog))
            c.alpha_composite(carib_map2(f, route=route, labels=[("CUBA", -79.5, 23.6, WHITE, K), ("JAMAICA", -77.3, 16.6, K, YEL), ("LA ISABELA", -71.1, 21.4, WHITE, K)], title="APRIL - SEPT 1494"), (25, 140))
            put(c, "ship", 200, 740 + bob(f, 3, 0.1))
        else:
            waves(d, f, 560, (200, 240, 240))
            put(c, "col", 40, FEET + 20, sc=2); label(d, "COLUMBUS", 92, 540, GOLD)
            for k in range(3): put(c, "sailor" if k != 1 else "esp0", 280 + k * 76, FEET + 20, flip=True)
            bubble(d, "CUBA IS ASIA!", 200, 430)
            if prog > 0.4: label(d, "OATH: JUNE 12, 1494", 270, 250, K, YEL, F16)
            if prog > 0.75: label(d, "(CUBA IS AN ISLAND)", 270, 290, WHITE, K, F16)
    elif i == 6:
        waves(d, f, 560, (120, 130, 140))
        for k in range(3):
            ang = 12 * math.sin(f * 0.12 + k * 1.7) - (30 * prog if (li == 1 and k == 1) else 0)
            sh = tilt("ship", ang); c.alpha_composite(sh, (int(10 + k * 170), int(560 + (k % 2) * 40 - sh.height // 2 + bob(f, 8, 0.15, k) + (prog * 80 if (li == 1 and k == 1) else 0))))
        rain(d, f)
        if (f // 9) % 7 == 0: R(d, (300, 0, 304, 200), (255, 255, 230))
        label(d, "HURRICANE", 270, 300, WHITE, RED, F16)
        if li == 0: label(d, "1494 + 1495", 270, 340, K, YEL, F16)
        else: label(d, "JUNE 1495: SHIPS SUNK", 270, 340, K, YEL, F16)
    elif i == 7:
        waves(d, f, 600, (240, 200, 160))
        if li == 0:
            x = 200 + prog * 220; put(c, "ship", x, 700 + bob(f, 3, 0.1)); label(d, "NIÑA", x + 80, 520, GOLD)
            label(d, "BACK TO CÁDIZ, 1496", 270, 280, WHITE, K, F16)
        elif li == 1:
            n = 8 + int(prog * 16)
            for k in range(n):
                pr = random.Random(k); x = pr.randint(0, CW - 44) + int(math.sin(f * 0.05 + k) * 10); y = 660 + pr.randint(0, 80)
                put(c, f"pig{st(f, k, 5)}", x, y, flip=bool(k % 2))
            label(d, "8 PIGS ...", 140, 300, WHITE, K, F16)
            if prog > 0.3: label(d, "... THOUSANDS", 380, 340, K, YEL, F16)
        else:
            for k in range(6): R(d, (40 + k * 80, 640 - (k % 3) * 12, 90 + k * 80, 650), (140, 136, 126))
            label(d, "LA ISABELA (RUINS)", 270, 470, GOLD)
            pigs(c, f, 6, 20, 700, dx=80, dy=20)
            if prog > 0.3: label(d, "FOLLOW FOR MORE HISTORY", 270, 260, WHITE, RED, F16)

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
