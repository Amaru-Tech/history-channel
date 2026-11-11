import os, sys, wave, math, random, subprocess, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

D = os.environ.get("HC_DIR", os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")
A = f"{D}/out2"; OUT = f"{D}/out3"; os.makedirs(OUT, exist_ok=True)
FONT = f"{D}/ps2p.woff"
FW, FH, CW, CH, FPS = 1080, 1920, 540, 960, 30
GY = 700          # horizon of the ground
FEET = 738        # where characters stand
CHECK = "check" in sys.argv

SCENES = [
 ("168 vs 10.000.000", ["168 soldados derrotaron a un imperio de 10 millones de personas.", "¿Cómo fue posible?"]),
 ("TAWANTINSUYU", ["En 1532, el Imperio Inca dominaba más de 4.000 km de Andes, de Ecuador a Chile."]),
 ("LA VIRUELA", ["Pero la viruela llegó antes que los españoles.", "Mató al emperador Huayna Cápac y a gran parte de la población."]),
 ("GUERRA CIVIL", ["Sus hijos, Huáscar y Atahualpa, pelearon una guerra civil brutal.", "Atahualpa acababa de ganarla cuando llegó Pizarro."]),
 ("CAJAMARCA 1532", ["En Cajamarca, Atahualpa entró a la plaza con miles de acompañantes, casi sin armas.", "Los españoles atacaron con caballos, acero y cañones. El emperador fue capturado."]),
 ("EL RESCATE", ["Pagó un cuarto lleno de oro y dos de plata. Aun así, fue ejecutado."]),
 ("ALIADOS", ["Lo que nadie cuenta: miles de andinos se unieron a los españoles."]),
 ("TORMENTA PERFECTA", ["No cayó por 168 hombres. Cayó por una tormenta perfecta.", "¿Qué imperio contamos ahora? Escríbelo en los comentarios."]),
]

# ---------------- colors ----------------
K = (22, 14, 12); SKIN = (196, 128, 84); SKIN_D = (160, 96, 62); SKIN_E = (225, 178, 140)
HAIR = (26, 20, 22); GOLD = (240, 190, 50); GOLD_D = (184, 128, 30); RED = (200, 36, 36); RED_D = (140, 20, 24)
WHITE = (246, 244, 236); STEEL = (176, 182, 194); STEEL_D = (116, 122, 138); STEEL_L = (226, 232, 242)
BROWN = (120, 72, 36); BROWN_D = (78, 46, 24); YEL = (232, 200, 70)

def R(d, b, c): d.rectangle(b, fill=c)

def outline(im, col=K + (255,)):
    a = im.getchannel("A").point(lambda v: 255 if v > 0 else 0)
    o = Image.new("RGBA", im.size, col); o.putalpha(a.filter(ImageFilter.MaxFilter(3)))
    o.alpha_composite(im); return o

def tint(im, k, add=(0, 0, 0)):
    r, g, b, a = im.split()
    ch = [x.point(lambda v, ad=ad: min(255, int(v * k + ad))) for x, ad in zip((r, g, b), add)]
    return Image.merge("RGBA", ch + [a])

# ---------------- sprites (52x84, feet at bottom) ----------------
def legs(d, step, skin=True, col=None, boots=None):
    xs = [(20, 23), (29, 32)] if step == 0 else [(17, 20), (32, 35)]
    for x0, x1 in xs:
        R(d, (x0, 64, x1, 78), SKIN if skin else col)
        R(d, (x0 - 1, 77, x1 + 1, 81) if not boots else (x0 - 1, 73, x1 + 1, 81), BROWN_D if not boots else boots)

def inca_head(d, feathers=True, royal=True, helmet=None):
    R(d, (19, 18, 33, 34), SKIN); R(d, (20, 35, 32, 35), SKIN_D)
    R(d, (30, 18, 33, 34), SKIN_D)
    R(d, (18, 13, 34, 19), HAIR); R(d, (18, 19, 19, 29), HAIR); R(d, (33, 19, 34, 29), HAIR)
    R(d, (22, 25, 23, 26), K); R(d, (28, 25, 29, 26), K); R(d, (21, 23, 23, 23), HAIR); R(d, (28, 23, 30, 23), HAIR)
    R(d, (25, 27, 26, 29), SKIN_D); R(d, (23, 31, 28, 31), SKIN_D)
    if helmet:
        R(d, (17, 11, 35, 18), helmet); R(d, (17, 15, 35, 16), WHITE)
    if royal:
        for x in range(18, 35):   # llauto: braided multicolor band
            d.point((x, 16), [RED, YEL, (40, 110, 60), WHITE][x % 4]); d.point((x, 17), [YEL, RED, WHITE, (40, 110, 60)][x % 4])
        R(d, (21, 18, 31, 23), RED)   # mascaipacha fringe
        for x in range(22, 31, 2): R(d, (x, 18, x, 23), RED_D)
        R(d, (13, 21, 18, 28), GOLD); R(d, (15, 23, 16, 26), GOLD_D)   # ear spools
        R(d, (34, 21, 39, 28), GOLD); R(d, (36, 23, 37, 26), GOLD_D)
    if feathers:
        R(d, (23, 3, 24, 15), WHITE); R(d, (28, 3, 29, 15), WHITE); R(d, (23, 3, 24, 6), K); R(d, (28, 3, 29, 6), K)
        R(d, (25, 9, 27, 15), GOLD)

def noble(tunic, cape, step=0, feathers=True, scepter=True):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    d.polygon([(14, 36), (38, 36), (42, 70), (10, 70)], fill=cape)
    legs(d, step)
    R(d, (16, 36, 36, 66), tunic); R(d, (32, 36, 36, 66), tint_c(tunic, 0.75))
    for k in range(5):
        R(d, (17 + k * 4, 47, 19 + k * 4, 49), [GOLD, K, WHITE, RED, GOLD][k])
        R(d, (17 + k * 4, 51, 19 + k * 4, 53), [K, WHITE, GOLD, K, WHITE][k])
    R(d, (16, 60, 36, 61), GOLD)
    d.polygon([(23, 36), (29, 36), (26, 40)], fill=SKIN)
    R(d, (12, 37, 16, 42), tunic); R(d, (36, 37, 40, 42), tint_c(tunic, 0.75))
    R(d, (12, 43, 15, 54), SKIN); R(d, (37, 43, 40, 54), SKIN_D)
    R(d, (12, 43, 15, 45), GOLD); R(d, (37, 43, 40, 45), GOLD)
    if scepter:
        R(d, (41, 28, 42, 66), GOLD_D); R(d, (39, 24, 44, 29), GOLD); R(d, (41, 22, 42, 23), GOLD)
    inca_head(d, feathers)
    return outline(im)

def tint_c(c, k): return tuple(int(v * k) for v in c)

def warrior(step=0, shield=True, mace=True, tunic_hi=RED):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    legs(d, step)
    for y in range(41, 66, 4):
        for x in range(16, 37, 4):
            R(d, (x, y, min(36, x + 3), min(65, y + 3)), K if ((x // 4 + y // 4) % 2) else WHITE)
    R(d, (16, 36, 36, 41), tunic_hi); d.polygon([(23, 36), (29, 36), (26, 40)], fill=SKIN)
    R(d, (12, 37, 16, 41), tunic_hi); R(d, (36, 37, 40, 41), tunic_hi)
    R(d, (12, 42, 15, 54), SKIN); R(d, (37, 42, 40, 54), SKIN_D)
    inca_head(d, feathers=False, royal=False, helmet=(150, 90, 50))
    if mace:
        R(d, (40, 26, 41, 58), BROWN); R(d, (37, 21, 44, 28), STEEL_D)
        for px, py in ((40, 19), (40, 29), (35, 24), (45, 24)): R(d, (px, py, px + 1, py + 1), STEEL_D)
    if shield:
        R(d, (5, 40, 17, 58), (210, 170, 90)); R(d, (7, 42, 15, 56), RED)
        R(d, (7, 47, 15, 50), GOLD); R(d, (10, 42, 12, 56), GOLD)
    return outline(im)

def conquistador(step=0, leader=False):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    if leader: d.polygon([(14, 37), (38, 37), (42, 72), (10, 72)], fill=RED_D)
    beard = (150, 140, 132) if leader else (92, 58, 34)
    legs(d, step, skin=False, col=(150, 40, 40) if leader else (90, 70, 50), boots=(40, 30, 28))
    for x in range(16, 37, 3): R(d, (x, 54, x + 1, 64), RED if leader else (170, 110, 50))
    for x in range(18, 37, 3): R(d, (x, 54, x, 64), YEL)
    R(d, (16, 36, 36, 55), STEEL); R(d, (31, 36, 36, 55), STEEL_D); R(d, (19, 38, 21, 51), STEEL_L)
    R(d, (26, 37, 26, 53), STEEL_D); R(d, (16, 53, 36, 55), BROWN_D); R(d, (25, 53, 27, 55), GOLD)
    slv = RED if leader else (170, 110, 50)
    R(d, (11, 37, 16, 51), slv); R(d, (36, 37, 41, 51), tint_c(slv, 0.8))
    for y in (40, 45): R(d, (12, y, 15, y + 1), YEL); R(d, (37, y, 40, y + 1), YEL)
    R(d, (11, 52, 15, 55), SKIN_E); R(d, (37, 52, 41, 55), SKIN_E)
    d.line([(42, 54), (48, 80)], fill=STEEL_L, width=2); R(d, (38, 52, 44, 54), GOLD)
    R(d, (19, 18, 33, 34), SKIN_E); R(d, (30, 18, 33, 34), (200, 150, 116))
    R(d, (22, 24, 23, 25), K); R(d, (28, 24, 29, 25), K)
    d.polygon([(18, 27), (34, 27), (32, 37), (26, 41), (20, 37)], fill=beard)
    R(d, (22, 27, 30, 28), beard); R(d, (24, 30, 28, 30), (150, 80, 70))
    d.polygon([(19, 19), (33, 19), (31, 9), (21, 9)], fill=STEEL)   # morion
    d.polygon([(21, 9), (31, 9), (29, 2), (23, 2)], fill=STEEL_D)
    d.polygon([(9, 15), (12, 18), (40, 18), (43, 15), (41, 21), (11, 21)], fill=STEEL)
    R(d, (12, 20, 40, 21), STEEL_D); R(d, (22, 11, 23, 17), STEEL_L)
    if leader:
        d.polygon([(30, 4), (40, 0), (46, 4), (38, 8)], fill=RED); d.polygon([(38, 8), (46, 4), (47, 9)], fill=WHITE)
    return outline(im)

def horse():
    im = Image.new("RGBA", (100, 72)); d = ImageDraw.Draw(im)
    H, Hd = (130, 80, 46), (96, 56, 30)
    d.polygon([(22, 28), (10, 44), (14, 52), (24, 36)], fill=(50, 34, 24))
    for x0 in (26, 36, 66, 76):
        R(d, (x0, 46, x0 + 4, 66), Hd if x0 in (36, 76) else H); R(d, (x0 - 1, 66, x0 + 5, 70), K)
    d.ellipse((20, 22, 84, 52), fill=H); d.ellipse((24, 40, 80, 52), fill=Hd)
    d.polygon([(66, 30), (78, 8), (88, 10), (82, 36)], fill=H)
    d.polygon([(76, 4), (90, 8), (96, 16), (94, 20), (86, 20), (80, 14)], fill=H)
    R(d, (88, 10, 89, 11), K); R(d, (93, 17, 94, 18), K)
    d.polygon([(76, 4), (80, 0), (82, 6)], fill=Hd)
    for k in range(7): R(d, (70 + k, 26 - k * 3, 73 + k, 30 - k * 3), (50, 34, 24))
    R(d, (40, 20, 62, 36), RED); R(d, (40, 34, 62, 36), YEL); R(d, (40, 20, 62, 21), YEL)
    return outline(im)

def rider(leader=True):
    h = horse(); c = conquistador(0, leader).crop((0, 0, 52, 58))
    im = Image.new("RGBA", (100, 110)); im.alpha_composite(c, (24, 4)); im.alpha_composite(h, (0, 38))
    d = ImageDraw.Draw(im); R(d, (44, 60, 49, 76), (150, 40, 40) if leader else (90, 70, 50)); R(d, (43, 72, 50, 80), (40, 30, 28))
    return outline(im)

def cannon():
    im = Image.new("RGBA", (50, 30)); d = ImageDraw.Draw(im)
    R(d, (6, 6, 42, 14), (70, 72, 80)); R(d, (6, 6, 42, 8), (120, 122, 130)); R(d, (40, 4, 44, 16), (70, 72, 80))
    R(d, (4, 8, 7, 12), (60, 60, 66)); R(d, (10, 14, 30, 20), BROWN)
    d.ellipse((12, 16, 26, 29), fill=BROWN_D); d.ellipse((16, 20, 22, 25), fill=BROWN)
    return outline(im)

def llama():
    im = Image.new("RGBA", (50, 60)); d = ImageDraw.Draw(im)
    W, Wd = (236, 226, 206), (200, 186, 160)
    for x0 in (12, 18, 30, 36): R(d, (x0, 38, x0 + 3, 56), Wd); R(d, (x0, 56, x0 + 3, 58), K)
    d.ellipse((8, 24, 44, 44), fill=W); R(d, (34, 6, 41, 30), W); d.polygon([(34, 6), (46, 8), (46, 14), (36, 14)], fill=W)
    R(d, (35, 1, 36, 6), Wd); R(d, (39, 1, 40, 6), Wd); R(d, (40, 9, 41, 10), K); R(d, (6, 26, 10, 30), Wd)
    R(d, (16, 26, 30, 34), RED); R(d, (16, 30, 30, 31), YEL)
    return outline(im)

def build_sprites():
    S = {}
    for s in (0, 1):
        S[f"ata{s}"] = noble((226, 140, 40), RED, s)
        S[f"hua{s}"] = noble((40, 96, 190), (24, 50, 120), s)
        S[f"hc{s}"] = noble((120, 60, 150), (70, 30, 90), s)
        S[f"war{s}"] = warrior(s); S[f"warB{s}"] = warrior(s, tunic_hi=(40, 96, 190)); S[f"warO{s}"] = warrior(s, tunic_hi=(226, 140, 40))
        S[f"run{s}"] = warrior(s, shield=False, mace=False)
        S[f"bear{s}"] = warrior(s, shield=False, mace=False, tunic_hi=GOLD_D)
        S[f"esp{s}"] = conquistador(s); S[f"piz{s}"] = conquistador(s, True)
    S["rider"] = rider(True); S["rider2"] = rider(False); S["cannon"] = cannon(); S["llama"] = llama()
    return S

SP = build_sprites()

def put(c, key, x, feet=FEET, sc=1, flip=False, alpha=1.0, crop=None, k=None):
    im = SP[key] if isinstance(key, str) else key
    if crop: im = im.crop((0, 0, im.width, crop))
    if k: im = tint(im, k)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    if sc != 1: im = im.resize((im.width * sc, im.height * sc), Image.NEAREST)
    if alpha < 1: im.putalpha(im.getchannel("A").point(lambda a: int(a * alpha)))
    c.alpha_composite(im, (int(x), int(feet - im.height)))
    return im

def st(f, ph=0, rate=6): return ((f // rate) + ph) % 2

# ---------------- text helpers ----------------
F8 = ImageFont.truetype(FONT, 8); F16 = ImageFont.truetype(FONT, 16)
def label(d, text, cx, y, fg=WHITE, bg=K, font=F16):
    w = d.textlength(text, font=font); h = 8 if font is F8 else 16
    R(d, (cx - w / 2 - 4, y - 3, cx + w / 2 + 3, y + h + 2), bg)
    d.text((cx - w / 2, y), text, font=font, fill=fg)

# ---------------- map ----------------
SA = [(-77, 8.5), (-72, 12), (-63, 10.7), (-60, 8.5), (-52, 5), (-50, 0), (-44, -2.5), (-35, -5), (-35, -9), (-39, -13),
      (-39, -18), (-41, -22), (-48, -25.5), (-48.5, -28.5), (-53, -33.7), (-57.5, -35), (-57, -38), (-62, -39), (-65, -42),
      (-67.5, -46), (-69, -51), (-68.5, -53), (-71, -54.5), (-74.5, -52), (-75.5, -47), (-73.5, -42), (-73.5, -37),
      (-71.5, -30), (-70.2, -23), (-70.3, -18.3), (-75.5, -15), (-77, -12), (-79.5, -7), (-81, -5), (-80, -2), (-80, 1),
      (-78.8, 1.5), (-77.5, 4), (-77.5, 7)]
EMP = [(-71.6, -35), (-71.5, -30), (-70.3, -23), (-70.3, -18.3), (-75.5, -15), (-77, -12), (-79.5, -7), (-81, -5), (-80, -2),
       (-80, 1), (-78.8, 1.5), (-77, 1.8), (-76.5, -1), (-77, -4), (-76, -7), (-74.5, -10), (-72, -12), (-69, -14), (-67, -17),
       (-65.5, -21), (-65.5, -25), (-67, -29), (-69, -33), (-70, -35.5)]
CITIES = {"QUITO": (-78.5, -0.2), "CAJAMARCA": (-78.5, -7.2), "CUSCO": (-72, -13.5)}

def draw_map(c, x, y, w, h, cities, f, title=None):
    m = Image.new("RGBA", (w, h)); d = ImageDraw.Draw(m); d.fontmode = "1"
    R(d, (0, 0, w - 1, h - 1), (70, 110, 160)); d.rectangle((0, 0, w - 1, h - 1), outline=(240, 220, 170), width=3)
    P = lambda lon, lat: (6 + (lon + 84) / 52 * (w - 12), 6 + (14 - lat) / 70 * (h - 12))
    d.polygon([P(*p) for p in SA], fill=(118, 150, 84), outline=(60, 80, 40))
    d.polygon([P(*p) for p in EMP], fill=GOLD, outline=GOLD_D)
    for name in cities:
        px, py = P(*CITIES[name]); on = (f // 10) % 2 == 0
        R(d, (px - 2, py - 2, px + 2, py + 2), RED if on else WHITE); d.rectangle((px - 2, py - 2, px + 2, py + 2), outline=K)
        tw = d.textlength(name, font=F8); tx = px + 6
        R(d, (tx - 2, py - 5, tx + tw + 1, py + 5), K); d.text((tx, py - 4), name, font=F8, fill=WHITE)
    if title:
        tw = d.textlength(title, font=F8); R(d, (w / 2 - tw / 2 - 3, h - 16, w / 2 + tw / 2 + 2, h - 5), K)
        d.text((w / 2 - tw / 2, h - 14), title, font=F8, fill=GOLD)
    c.alpha_composite(outline(m), (x, y))

# ---------------- backgrounds ----------------
def grad(d, top, bot, y0=0, y1=GY, steps=12):
    h = (y1 - y0) / steps
    for i in range(steps):
        t = i / (steps - 1); col = tuple(int(top[j] * (1 - t) + bot[j] * t) for j in range(3))
        R(d, (0, y0 + int(i * h), CW, y0 + int((i + 1) * h)), col)

def mountains(d, col, snow, base, peaks):
    for px, ph, hw in peaks:
        d.polygon([(px - hw, base), (px, base - ph), (px + hw, base)], fill=col)
        d.polygon([(px, base - ph), (px + hw, base), (px + hw * 0.4, base)], fill=tint_c(col, 0.82))
        if snow: d.polygon([(px - hw * 0.28, base - ph * 0.72), (px, base - ph), (px + hw * 0.28, base - ph * 0.72),
                            (px + hw * 0.1, base - ph * 0.78), (px - hw * 0.05, base - ph * 0.7)], fill=snow)

def ground(d, col, col2):
    R(d, (0, GY, CW, CH), col)
    rnd = random.Random(3)
    for _ in range(140):
        x, y = rnd.randint(0, CW), rnd.randint(GY + 4, CH); R(d, (x, y, x + rnd.choice((1, 3)), y + 1), col2)
    R(d, (0, GY, CW, GY + 2), col2)

def inca_wall(d, x0, y0, x1, y1, stone=(140, 136, 128), line=(100, 96, 90), doors=(), door_col=(40, 32, 30)):
    R(d, (x0, y0, x1, y1), stone)
    rnd = random.Random(x0 * 7 + y0)
    y = y0
    while y < y1:
        hh = rnd.randint(10, 16); x = x0 - rnd.randint(0, 20)
        while x < x1:
            ww = rnd.randint(18, 34); d.rectangle((max(x0, x), y, min(x1, x + ww), min(y1, y + hh)), outline=line); x += ww
        y += hh
    for dx, dw, dh in doors:
        d.polygon([(dx, y1), (dx + dw * 0.15, y1 - dh), (dx + dw * 0.85, y1 - dh), (dx + dw, y1)], fill=door_col)
        R(d, (dx + dw * 0.1, y1 - dh - 4, dx + dw * 0.9, y1 - dh - 1), line)

def machu_picchu(d, dark=1.0):
    k = lambda c: tint_c(c, dark)
    d.polygon([(0, 700), (0, 560), (120, 525), (300, 505), (370, 470), (420, 330), (452, 300), (488, 330), (520, 430), (540, 470), (540, 700)], fill=k((54, 110, 60)))
    d.polygon([(452, 300), (488, 330), (520, 430), (540, 470), (540, 700), (470, 700)], fill=k((40, 88, 48)))
    for i in range(9):
        y = 690 - i * 18
        R(d, (20 + i * 8, y - 12, 360 - i * 10, y), k((96, 160, 80))); R(d, (20 + i * 8, y, 360 - i * 10, y + 3), k((120, 114, 104)))
    for x in (90, 150, 210, 270):
        y = 690 - 8 * 18 - 12
        R(d, (x, y - 34, x + 40, y), k((150, 146, 136))); d.rectangle((x, y - 34, x + 40, y), outline=k((104, 100, 94)))
        d.polygon([(x - 4, y - 34), (x + 20, y - 54), (x + 44, y - 34)], fill=k((176, 138, 70)))
        d.polygon([(x + 14, y), (x + 16, y - 20), (x + 24, y - 20), (x + 26, y)], fill=k((40, 32, 30)))

def make_bg(i):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0:
        grad(d, (70, 40, 100), (250, 160, 80))
        mountains(d, (96, 60, 86), (240, 210, 210), GY, [(80, 260, 150), (300, 330, 170), (500, 240, 130)])
        ground(d, (170, 132, 84), (140, 104, 64))
    elif i in (1, 6):
        grad(d, (60, 120, 220), (180, 216, 246))
        for cx, cy in ((90, 210), (300, 150)) if i == 6 else ((260, 190),):
            for dx, dy, r in ((0, 0, 22), (22, -8, 26), (46, 0, 20)): d.ellipse((cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r), fill=WHITE)
        mountains(d, (120, 124, 160), (246, 246, 250), GY - 60, [(60, 330, 150), (250, 380, 170), (470, 300, 140)])
        if i == 1: machu_picchu(d)
        else: mountains(d, (60, 120, 66), None, GY, [(120, 160, 200), (420, 140, 200)])
        ground(d, (96, 150, 70), (70, 120, 50))
    elif i == 2:
        grad(d, (14, 10, 34), (60, 40, 90))
        rnd = random.Random(1)
        for _ in range(50): x, y = rnd.randint(0, CW), rnd.randint(0, 400); R(d, (x, y, x, y), WHITE)
        d.ellipse((400, 130, 450, 180), fill=(236, 236, 214)); d.ellipse((414, 124, 460, 170), fill=(14, 10, 34))
        inca_wall(d, 0, 430, CW, GY, (86, 84, 104), (60, 58, 78), doors=((60, 70, 110), (410, 70, 110)), door_col=(20, 16, 24))
        ground(d, (60, 56, 70), (44, 40, 54))
    elif i == 3:
        grad(d, (80, 16, 20), (230, 120, 60))
        mountains(d, (90, 40, 40), (220, 180, 170), GY, [(100, 280, 160), (420, 320, 170)])
        ground(d, (130, 96, 62), (100, 72, 44))
    elif i == 4:
        grad(d, (70, 130, 220), (180, 216, 246))
        mountains(d, (110, 110, 140), (246, 246, 250), 520, [(120, 260, 170), (420, 300, 190)])
        mountains(d, (70, 120, 70), None, 560, [(80, 120, 160), (300, 100, 180), (520, 130, 150)])
        inca_wall(d, 0, 520, CW, 640, doors=[(30 + k * 90, 46, 80) for k in range(6)])
        R(d, (0, 510, CW, 520), (176, 138, 70))
        R(d, (0, 640, CW, GY), (196, 168, 120)); ground(d, (200, 172, 124), (176, 146, 100))
    elif i == 5:
        inca_wall(d, 0, 0, CW, GY, (132, 128, 122), (92, 88, 84), doors=((70, 90, 150), (380, 90, 150)), door_col=(56, 48, 46))
        R(d, (0, 430, CW, 433), RED)
        ground(d, (90, 76, 64), (70, 58, 48))
    elif i == 7:
        grad(d, (22, 22, 32), (70, 70, 88))
        mountains(d, (40, 40, 56), (130, 130, 146), GY - 60, [(60, 330, 150), (250, 380, 170), (470, 300, 140)])
        machu_picchu(d, 0.45)
        ground(d, (36, 50, 36), (26, 38, 26))
    return c

# ---------------- animation per scene ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"
    if i == 0:
        for r in range(3):
            for col in range(10):
                x = 258 + col * 28 + (r % 2) * 14
                if x > CW - 20: continue
                put(c, f"war{st(f, r + col, 9)}", x, FEET - 36 + r * 18, flip=True, k=0.55 + r * 0.22)
        put(c, "rider", 10, FEET); put(c, f"esp{st(f, 0, 9)}", 112, FEET + 4); put(c, f"esp{st(f, 1, 9)}", 160, FEET + 2)
        label(d, "168 ESPAÑOLES", 110, 560, GOLD); label(d, "EJÉRCITO INCA", 400, 560, GOLD)
    elif i == 1:
        draw_map(c, 26, 120, 160, 228, ["QUITO", "CUSCO"], f, "TAWANTINSUYU")
        put(c, "llama", 420, FEET - 4)
        x = -60 + (CW + 80) * (t / sdur)
        put(c, f"run{st(f, 0, 4)}", x, FEET + 2)
        label(d, "MACHU PICCHU", 230, 470, WHITE)
        label(d, "CHASQUI", x + 26, 640, GOLD)
    elif i == 2:
        for tx in (95, 445):
            R(d, (tx - 2, 470, tx + 2, 500), BROWN); fl = (f // 4) % 3
            d.polygon([(tx - 6, 470), (tx, 452 - fl * 3), (tx + 6, 470)], fill=(250, 160, 40)); R(d, (tx - 2, 462, tx + 2, 470), YEL)
        a = 1.0 if li == 0 else max(0.0, 1 - lt / ldur)
        put(c, f"hc0", 218, FEET, sc=2, alpha=a)
        if a > 0.15: label(d, "HUAYNA CÁPAC", 270, 536, GOLD)
        for k in range(26):
            pr = random.Random(k); sx = pr.randint(10, 530); sp = pr.uniform(12, 30)
            y = GY + 20 - ((t * sp + pr.randint(0, 600)) % 560)
            R(d, (sx, y, sx + 3, y + 3), (130, 210, 90)); R(d, (sx + 1, y - 1, sx + 2, y + 4), (130, 210, 90))
    elif i == 3:
        draw_map(c, 195, 118, 150, 214, ["QUITO", "CUSCO"], f)
        for k in range(4):
            put(c, f"warB{st(f, k, 9)}", -10 + k * 30, FEET - 30, k=0.6)
            put(c, f"warO{st(f, k + 1, 9)}", 400 + k * 30, FEET - 30, flip=True, k=0.6)
        lunge = int(16 * max(0, math.sin(t * 3.5)))
        put(c, "hua0", 40 + lunge, FEET, sc=2); put(c, "ata0", 396 - lunge, FEET, sc=2, flip=True)
        label(d, "HUÁSCAR", 92 + lunge, 530, (120, 170, 250)); label(d, "(CUSCO)", 92 + lunge, 554, WHITE, font=F8)
        label(d, "ATAHUALPA", 448 - lunge, 530, GOLD); label(d, "(QUITO)", 448 - lunge, 554, WHITE, font=F8)
        if lunge > 12:
            for a_ in range(0, 360, 45):
                r = math.radians(a_); d.line([270, 640, 270 + 22 * math.cos(r), 640 + 22 * math.sin(r)], fill=YEL, width=3)
        if li == 1 and lt > ldur * 0.35:
            x = min(240, -60 + (lt - ldur * 0.35) * 260)
            put(c, f"piz{st(f, 0, 5)}", x, FEET + 10); label(d, "PIZARRO", x + 26, 640, RED)
    elif i == 4:
        draw_map(c, 370, 112, 150, 214, ["CAJAMARCA"], f)
        put(c, "esp0", 207, 640, crop=60, k=0.75); put(c, "esp1", 387, 640, crop=60, k=0.75)
        put(c, "cannon", 330, FEET + 2, flip=True)
        put(c, "rider", 430, FEET, flip=True); label(d, "PIZARRO", 480, 610, RED)
        lx = (-200 + 300 * min(1, lt / max(0.1, ldur * 0.8))) if li == 0 else 100
        for k, bx in enumerate((0, 34, 68, 102)):
            put(c, f"bear{st(f, k, 6) if li == 0 else 0}", lx + bx - 30, FEET + (k % 2) * 4)
        R(d, (lx - 36, FEET - 50, lx + 120, FEET - 44), GOLD); R(d, (lx - 36, FEET - 44, lx + 120, FEET - 42), GOLD_D)
        put(c, "ata0", lx + 18, FEET - 49, crop=64)
        label(d, "ATAHUALPA", lx + 44, FEET - 130, GOLD)
        if li == 1:
            ph = (lt * 1.1) % 1
            if ph < 0.1: R(d, (300, 680, 330, 700), (255, 250, 210))
            for k in range(4):
                r = int(4 + ph * 14 + k * 3); cx = 322 - k * 10 - ph * 30; cy = FEET - 20 - k * 8 - ph * 26
                d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(236, 236, 236))
            if lt > ldur * 0.55 and (f // 8) % 2: label(d, "¡CAPTURADO!", lx + 44, FEET - 152, WHITE, RED)
    elif i == 5:
        h = int(20 + 240 * (t / sdur))
        d.polygon([(200, FEET), (370, FEET - h), (540, FEET)], fill=GOLD)
        d.polygon([(370, FEET - h), (540, FEET), (450, FEET)], fill=GOLD_D)
        rnd = random.Random(f // 5)
        for _ in range(8):
            sx = rnd.randint(250, 480); sy = rnd.randint(FEET - h + 10, FEET - 4)
            if abs(sx - 370) / 170 < 1 - (FEET - sy) / max(1, h): R(d, (sx, sy, sx + 2, sy + 2), WHITE)
        label(d, "LÍNEA DEL RESCATE", 270, 404, WHITE, RED)
        a = 1.0 if t < sdur - 1.4 else max(0.0, (sdur - t) / 1.4)
        put(c, "ata0", 30, FEET, sc=2, alpha=a)
        if a > 0.2: label(d, "ATAHUALPA", 82, 536, GOLD)
        label(d, "CUARTO DEL RESCATE, CAJAMARCA", 270, 140, GOLD)
    elif i == 6:
        order = ["war", "esp", "war", "war", "piz", "war", "esp", "war"]
        for k, n in enumerate(order):
            x = ((k * 70 + t * 34) % (CW + 140)) - 70
            put(c, f"{n}{st(f, k, 6)}", x, FEET + (k % 2) * 6)
        label(d, "ALIADOS ANDINOS + ESPAÑOLES", 270, 560, GOLD)
    elif i == 7:
        rnd = random.Random(f)
        if (f % 40) < 3:
            pts = [(rnd.randint(150, 400), 0)]
            for _ in range(8): pts.append((pts[-1][0] + rnd.randint(-20, 20), pts[-1][1] + 50))
            d.line(pts, fill=(255, 255, 220), width=4)
        for k in range(110):
            pr = random.Random(k); x = pr.randint(0, CW); y = (pr.randint(0, CH) + f * 14) % GY
            d.line([x, y, x - 3, y + 10], fill=(150, 170, 210))
        words = ["VIRUELA", "GUERRA CIVIL", "ALIADOS"]
        for k, w in enumerate(words):
            if li == 0 and lt > k * 0.6 or li == 1: label(d, w, 270, 330 + k * 40, WHITE, RED_D, F16)

# ---------------- text overlay (full res) ----------------
def overlay(head, cap):
    o = Image.new("RGBA", (FW, FH)); d = ImageDraw.Draw(o)
    for size in (64, 56, 48, 40):
        fh = ImageFont.truetype(FONT, size)
        if d.textlength(head, font=fh) <= FW - 80: break
    d.text((FW // 2 + 8, 168), head, font=fh, fill=K, anchor="mm"); d.text((FW // 2, 160), head, font=fh, fill=GOLD, anchor="mm")
    d.rectangle([40, 1500, 1040, 1860], fill=(0, 0, 0)); d.rectangle([40, 1500, 1040, 1860], outline=WHITE, width=8)
    d.rectangle([56, 1516, 1024, 1844], outline=(120, 120, 120), width=4)
    fc = ImageFont.truetype(FONT, 40); lines = textwrap.wrap(cap, 22); y = 1680 - (len(lines) - 1) * 30
    for ln in lines: d.text((FW // 2, y), ln, font=fc, fill=WHITE, anchor="mm"); y += 60
    return o

def wavdur(p):
    with wave.open(p) as w: return w.getnframes() / w.getframerate()

def compose(i, f, t, li, lt, ldur, sdur, bg, ov):
    c = bg.copy(); d = ImageDraw.Draw(c)
    draw_scene(i, c, d, f, t, li, lt, ldur, sdur)
    big = c.resize((FW, FH), Image.NEAREST); big.alpha_composite(ov); return big.convert("RGB")

if __name__ == "__main__":
    if CHECK:
        for i, (head, caps) in enumerate(SCENES):
            li = len(caps) - 1
            compose(i, 50, 3.0, li, 2.0, 4.0, 8.0, make_bg(i), overlay(head, caps[li])).save(f"{OUT}/check{i}.png")
        sys.exit()

    clips = []
    for i, (head, caps) in enumerate(SCENES):
        ldurs = [round(wavdur(f"{A}/p{i}_{li}.wav") * FPS) / FPS for li in range(len(caps))]
        sdur = sum(ldurs); bg = make_bg(i); ovs = [overlay(head, cap) for cap in caps]
        tmp, fin = f"{OUT}/s{i}.tmp.mp4", f"{OUT}/s{i}.mp4"
        p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{FW}x{FH}", "-r", str(FPS), "-i", "-",
                              "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
        for f in range(int(round(sdur * FPS))):
            t = f / FPS; li, acc = 0, 0.0
            while li < len(ldurs) - 1 and t >= acc + ldurs[li]: acc += ldurs[li]; li += 1
            img = compose(i, f, t, li, t - acc, ldurs[li], sdur, bg, ovs[li])
            if t < 0.25: img = Image.blend(Image.new("RGB", (FW, FH)), img, t / 0.25)
            p.stdin.write(img.tobytes())
        p.stdin.close(); assert p.wait() == 0; os.rename(tmp, fin); clips.append(fin); print("scene", i, flush=True)

    open(f"{OUT}/v.txt", "w").write("".join(f"file '{c}'\n" for c in clips))
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/v.txt", "-c", "copy", f"{OUT}/video.mp4"], check=True)
    final = f"{D}/inca_pixel_03.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{OUT}/video.mp4", "-i", f"{A}/voice.wav", "-i", f"{A}/music.wav",
                    "-filter_complex", "[2:a]volume=0.18[m];[1:a][m]amix=inputs=2:duration=first:normalize=0[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", final], check=True)
    print("done")
