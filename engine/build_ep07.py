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
OUT = f"{D}/out_ep07"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep07_sermon_of_1511_EN.mp4"

_src9 = open(f"{D}/build_ep06.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- maps ----------------")[0]
exec(_src9)  # episode 6: cacica, modern islanders, zemi, hammock, barbacoa, conuco, batey, swirl, cave props
_src9b = open(f"{D}/build_ep06.py").read().split("# ---------------- backgrounds ----------------")[-1].split("def make_bg")[0]
exec(_src9b)  # episode 6 backgrounds: beach, jungle_village, colony
_src9c = open(f"{D}/build_ep05.py").read().split("# ---------------- backgrounds ----------------")[-1].split("def make_bg")[0]
exec(_src9c)  # episode 5 backgrounds: court, room, village, cabin, jamaica_bay

SCENES = [
 ("THE SERMON OF 1511", [
  ("Hispaniola, December twenty-first, fifteen eleven. A friar tells a packed church they are all in mortal sin.", "Hispaniola, December 21, 1511. A friar tells a packed church they are all in mortal sin."),
  ("Their sin? How they treated the {Taíno}.", "Their sin? How they treated the Taíno.")]),
 ("THE DOMINICANS", [
  ("In fifteen ten, Dominican friars led by {Pedro} {de} {Córdoba} arrived on the island.", "In 1510, Dominican friars led by Pedro de Córdoba arrived on the island."),
  ("They saw {Taíno} forced to dig gold and farm for Spanish settlers.", "They saw Taíno forced to dig gold and farm for Spanish settlers."),
  ("So they wrote a sermon together, and every friar signed it.", "So they wrote a sermon together, and every friar signed it.")]),
 ("THE SERMON", [
  ("On the fourth Sunday of Advent, Friar {Antonio} {de} {Montesinos} climbed the pulpit.", "On the fourth Sunday of Advent, Friar Antonio de Montesinos climbed the pulpit."),
  ("Are they not human? Have they no souls?", "\"Are they not human? Have they no souls?\""),
  ("Are you not required to love them as you love yourselves?", "\"Are you not required to love them as you love yourselves?\"")]),
 ("OUTRAGE", [
  ("Governor Diego Columbus, son of Christopher, was among the outraged listeners.", "Governor Diego Columbus, son of Christopher, was among the outraged listeners."),
  ("The colonists demanded a retraction. Instead, the friars refused to hear their confessions.", "The colonists demanded a retraction. Instead, the friars refused to hear their confessions.")]),
 ("BEFORE THE KING", [
  ("The fight crossed the ocean to Spain.", "The fight crossed the ocean to Spain."),
  ("King Ferdinand first called the preaching groundless, and ordered the friars sent home.", "King Ferdinand first called the preaching groundless and ordered the friars sent home."),
  ("But {Montesinos} argued the case at court, and won the king over.", "But Montesinos argued the case at court, and won the king over.")]),
 ("THE LAWS OF BURGOS", [
  ("On December twenty-seventh, fifteen twelve, Ferdinand issued the Laws of {Burgos}. Thirty-five laws.", "On December 27, 1512, Ferdinand issued the Laws of Burgos. 35 laws."),
  ("No physical or verbal abuse of Native workers. Hammocks, not the bare ground.", "No physical or verbal abuse of Native workers. Hammocks, not the bare ground."),
  ("Forty days of rest after five months of mining. No heavy labor for women more than four months pregnant.", "40 days of rest after 5 months of mining. No heavy labor for women more than 4 months pregnant.")]),
 ("ONLY ON PAPER", [
  ("But the laws kept the {encomienda}, and they were poorly enforced.", "But the laws kept the encomienda, and they were poorly enforced."),
  ("Still, one man who heard that sermon never forgot it: {Bartolomé} {de} {las Casas}.", "Still, one man who heard that sermon never forgot it: Bartolomé de las Casas."),
  ("He gave up his own {encomienda}, and spent his life defending Native peoples.", "He gave up his own encomienda and spent his life defending Native peoples.")]),
 ("A VOICE THAT STILL STANDS", [
  ("Today, a fifteen-meter statue of {Montesinos} faces the sea in {Santo Domingo}, a gift from Mexico.", "Today a 15-meter statue of Montesinos faces the sea in Santo Domingo, a gift from Mexico."),
  ("Five centuries later, his sermon is remembered as an early voice for human dignity.", "Five centuries later, his sermon is remembered as an early voice for human dignity.")]),
]

# ---------------- narration: Kokoro (am_michael) with IPA for Spanish names ----------------
import re as _re, soundfile as _sf
from kokoro_onnx import Kokoro as _Kokoro
_KK = _Kokoro(f"{D}/kokoro/kokoro-v1.0.onnx", f"{D}/kokoro/voices-v1.0.bin")
NARRATOR = os.environ.get("HC_VOICE", "am_michael")
IPA = {"Montesinos": "mˌɔntɛsˈiːnoʊs", "Antonio": "ɑntˈoʊnjoʊ", "Córdoba": "kˈɔɹdoʊbɑ", "Pedro": "pˈeɪdɹoʊ", "de": "dɛ",
       "Bartolomé": "bˌɑɹtoʊloʊmˈeɪ", "las Casas": "lɑs kˈɑsɑs", "Taíno": "tɑˈiːnoʊ", "Burgos": "bˈʊɹɡoʊs",
       "encomienda": "ɛŋkˌoʊmiˈɛndɑ", "Santo Domingo": "sˈɑntoʊ doʊmˈiŋɡoʊ"}
def phonemes(text):
    parts = _re.split(r"\{([^}]+)\}", text); out = []
    for j, p in enumerate(parts):
        if j % 2: out.append(IPA[p])
        elif p.strip(): out.append(_KK.tokenizer.phonemize(p, "en-us"))
    return " ".join(x.strip() for x in out if x.strip())
def tts(text, path):
    a, sr = _KK.create(phonemes(text), voice=NARRATOR, speed=1.1, is_phonemes=True); _sf.write(path, a, sr, subtype="PCM_16")

if "durs" in sys.argv:
    tot = 0
    for i, (head, lines) in enumerate(SCENES):
        for li, (sp, cap) in enumerate(lines):
            p = f"{OUT}/t{i}_{li}.wav"; tts(sp, p); dd = wavdur(p) + 0.3; tot += dd; print(i, li, round(dd, 1))
    print("TOTAL", round(tot + 8 * 0.25 + 2, 1)); sys.exit()

_label_orig = label
def label(d, text, cx, y, fg=WHITE, bg=K, font=F16):
    w = d.textlength(text, font=font); cx = min(max(cx, w / 2 + 8), CW - w / 2 - 8)
    _label_orig(d, text, cx, y, fg, bg, font)

# ---------------- extra sprites ----------------
CAPE = (34, 30, 36); CAPE_D = (20, 18, 22); HABIT = (236, 232, 220); HABIT_D = (196, 192, 180)

def dominican(preach=False, hair=(90, 64, 40)):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    R(d, (19, 77, 24, 81), K); R(d, (28, 77, 33, 81), K)
    d.polygon([(16, 36), (36, 36), (39, 78), (13, 78)], fill=HABIT); d.polygon([(30, 36), (36, 36), (39, 78), (33, 78)], fill=HABIT_D)
    d.polygon([(14, 36), (19, 36), (19, 78), (11, 78)], fill=CAPE); d.polygon([(33, 36), (38, 36), (41, 78), (33, 78)], fill=CAPE_D)  # black cappa
    R(d, (17, 34, 35, 40), CAPE)  # hood collar
    R(d, (22, 56, 30, 58), K)
    if preach:
        R(d, (6, 14, 11, 38), HABIT); R(d, (5, 9, 10, 14), SKIN_E)   # raised arm
        R(d, (36, 37, 41, 54), HABIT_D); R(d, (37, 54, 41, 57), SKIN_E)
    else:
        R(d, (11, 37, 16, 54), HABIT); R(d, (36, 37, 41, 54), HABIT_D); R(d, (11, 54, 15, 57), SKIN_E); R(d, (37, 54, 41, 57), SKIN_E)
    face(d); R(d, (17, 15, 35, 18), hair); R(d, (17, 18, 19, 26), hair); R(d, (33, 18, 35, 26), hair)  # tonsure ring
    R(d, (21, 12, 31, 15), SKIN_E)
    return outline(im)

def diego():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    for x0, x1 in [(20, 23), (29, 32)]: R(d, (x0, 62, x1, 78), K); R(d, (x0 - 1, 77, x1 + 1, 81), K)
    R(d, (14, 36, 38, 62), (130, 24, 36)); R(d, (30, 36, 38, 62), (96, 16, 26))
    R(d, (12, 50, 40, 64), K)  # trunk hose
    R(d, (16, 36, 36, 38), WHITE); d.line([(17, 40), (26, 48), (35, 40)], fill=GOLD, width=2)
    R(d, (10, 37, 15, 56), (130, 24, 36)); R(d, (37, 37, 42, 56), (96, 16, 26)); R(d, (10, 56, 14, 59), SKIN_E); R(d, (38, 56, 42, 59), SKIN_E)
    face(d); R(d, (17, 14, 35, 19), (60, 40, 24)); R(d, (17, 19, 19, 30), (60, 40, 24)); R(d, (33, 19, 35, 30), (60, 40, 24))
    R(d, (15, 9, 37, 14), K); R(d, (31, 4, 33, 9), WHITE)  # black cap with feather
    return outline(im)

def cleric():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, (40, 36, 44), (26, 22, 30)); R(d, (22, 36, 30, 39), WHITE)
    R(d, (24, 44, 27, 56), GOLD); R(d, (21, 48, 30, 50), GOLD)
    face(d); R(d, (17, 13, 35, 18), (60, 50, 44)); R(d, (17, 18, 19, 28), (60, 50, 44)); R(d, (33, 18, 35, 28), (60, 50, 44))
    R(d, (16, 8, 36, 13), K)  # cleric's cap
    return outline(im)

SP.update({"dom": dominican(), "domp": dominican(True), "dom2": dominican(hair=(40, 30, 26)), "dom3": dominican(hair=(150, 140, 130)),
           "diego": diego(), "casas": cleric()})

# ---------------- props ----------------
def pulpit(c, d, x, top, who="domp", f=0):
    put(c, who, x + 24, top + 30, sc=2, crop=58)
    R(d, (x, top, x + 140, top + 70), (110, 70, 36)); R(d, (x - 6, top - 6, x + 146, top + 4), (150, 100, 56))
    for k in range(3): d.rectangle((x + 10 + k * 44, top + 14, x + 40 + k * 44, top + 58), outline=(80, 50, 26), width=2)
    d.polygon([(x + 40, top + 70), (x + 100, top + 70), (x + 80, top + 110), (x + 60, top + 110)], fill=(90, 58, 30))
    R(d, (x + 62, top + 110, x + 78, FEET - 40), (90, 58, 30))

def nave(d):
    grad(d, (80, 72, 66), (130, 120, 104), 0, GY, 10)
    for x in (30, 200, 370):
        R(d, (x, 150, x + 140, GY), (150, 140, 124)); d.ellipse((x, 80, x + 140, 220), fill=(150, 140, 124))
        R(d, (x + 20, 170, x + 120, GY), (60, 54, 52)); d.ellipse((x + 20, 110, x + 120, 230), fill=(60, 54, 52))
    for x in (0, 170, 340, 510): R(d, (x, 100, x + 30, GY), (176, 166, 148)); R(d, (x - 4, 96, x + 34, 108), (196, 186, 168))
    R(d, (0, GY, CW, CH), (120, 96, 70))
    for x in range(0, CW, 40): R(d, (x, GY, x + 1, CH), (96, 74, 52))

def church_window(d, x, y):
    d.ellipse((x, y, x + 40, y + 40), fill=(90, 150, 210)); R(d, (x, y + 20, x + 40, y + 90), (90, 150, 210))
    R(d, (x + 18, y, x + 22, y + 90), (40, 36, 34)); R(d, (x, y + 44, x + 40, y + 48), (40, 36, 34))

def pews(c, d, f, angry=False, n=6, x0=10):
    for k in range(n):
        x = x0 + k * 52
        put(c, ["set1", "set2", "set1", "sailor", "set2", "set1"][k % 6], x, FEET - (k % 2) * 6 + (bob(f, 3, 0.4, k) if angry else 0), flip=True)
    R(d, (0, FEET - 30, x0 + n * 52, FEET - 22), (110, 70, 36)); R(d, (0, FEET - 22, x0 + n * 52, FEET), (90, 58, 30))

def candles_row(d, f, x0, x1, base):
    for x in range(x0, x1, 46): candle(d, x, base, f + x)

def quote_box(d, lines, y, col=YEL):
    for k, ln in enumerate(lines): label(d, ln, 270, y + k * 36, K, col, F16)

def gold_mine(c, d, f, x0=0):
    d.polygon([(x0 + 300, GY), (x0 + 360, 470), (x0 + 450, 430), (CW, 460), (CW, GY)], fill=(130, 110, 86))
    d.polygon([(x0 + 390, GY), (x0 + 410, 600), (x0 + 470, 590), (x0 + 490, GY)], fill=(40, 30, 26))
    R(d, (0, 700, CW, 724), (60, 140, 190))
    for k in range(6): R(d, (20 + k * 80 + (f // 4 + k) % 10, 708, 26 + k * 80 + (f // 4 + k) % 10, 710), GOLD)

def whip_cross(d, x, y):
    d.line([(x, y + 40), (x + 30, y)], fill=BROWN, width=4); d.arc((x + 18, y - 10, x + 58, y + 30), 180, 330, fill=BROWN, width=3)
    d.ellipse((x - 8, y - 14, x + 62, y + 52), outline=RED, width=6); d.line([(x + 2, y + 44), (x + 52, y - 6)], fill=RED, width=6)

def calendar(d, x, y, big, small, col):
    R(d, (x, y, x + 100, y + 90), WHITE); R(d, (x, y, x + 100, y + 24), col); d.rectangle((x, y, x + 100, y + 90), outline=K, width=3)
    for k in (20, 76): R(d, (x + k, y - 8, x + k + 4, y + 6), K)
    d.text((x + 50, y + 54), big, font=ImageFont.truetype(FONT, 28), fill=K, anchor="mm"); d.text((x + 50, y + 13), small, font=F8, fill=WHITE, anchor="mm")

def law_book(d, x, y, open_prog=1.0):
    R(d, (x, y, x + 200, y + 130), (130, 30, 34)); R(d, (x + 8, y + 6, x + 192, y + 124), (240, 230, 200)); R(d, (x + 98, y + 6, x + 102, y + 124), (160, 140, 110))
    n = int(10 * open_prog)
    for k in range(n): R(d, (x + 16 + (k // 5) * 96, y + 18 + (k % 5) * 20, x + 86 + (k // 5) * 96, y + 21 + (k % 5) * 20), (140, 120, 90))

def quill(d, x, y, f):
    dx = int(math.sin(f * 0.5) * 8)
    d.line([(x + dx, y), (x + dx + 30, y - 50)], fill=WHITE, width=4); d.line([(x + dx + 10, y - 16), (x + dx + 34, y - 46)], fill=(220, 220, 210), width=6)

def burgos_skyline(d, base):
    R(d, (300, base - 60, CW, base), (200, 190, 170))
    for x, h in ((320, 150), (440, 150)):
        R(d, (x, base - h, x + 40, base), (210, 200, 180)); d.polygon([(x - 2, base - h), (x + 20, base - h - 50), (x + 42, base - h)], fill=(190, 180, 160))
        for y in range(base - h + 10, base - 20, 30): R(d, (x + 14, y, x + 26, y + 16), (90, 80, 70))
    R(d, (360, base - 100, 440, base), (220, 210, 190)); d.ellipse((380, base - 80, 420, base - 40), fill=(90, 80, 70))

def statue(d, x, base, f, h=420):
    S = (196, 190, 178); SD = (150, 144, 134)
    R(d, (x - 54, base - 20, x + 54, base), SD); R(d, (x - 46, base - 150, x + 46, base - 20), S); R(d, (x + 16, base - 150, x + 46, base - 20), SD)
    R(d, (x - 52, base - 160, x + 52, base - 150), (210, 204, 192))
    for y in range(base - 140, base - 20, 20): R(d, (x - 46, y, x + 46, y), SD)
    top = base - h; B = (120, 96, 62); BD = (78, 60, 36); BL = (160, 130, 84)
    fb = base - 160
    d.polygon([(x - 48, fb), (x + 48, fb), (x + 30, top + 110), (x - 30, top + 110)], fill=B)  # robe
    d.polygon([(x + 10, fb), (x + 48, fb), (x + 30, top + 110), (x + 8, top + 110)], fill=BD)
    for k in range(3): d.line([(x - 30 + k * 14, fb), (x - 20 + k * 10, top + 130)], fill=BD, width=3)
    d.polygon([(x - 34, top + 110), (x + 34, top + 110), (x + 26, top + 80), (x - 26, top + 80)], fill=BD)  # cape shoulders
    d.ellipse((x - 20, top + 34, x + 20, top + 86), fill=BD)  # hood
    d.ellipse((x - 13, top + 44, x + 13, top + 78), fill=BL); R(d, (x - 7, top + 56, x - 4, top + 59), K); R(d, (x + 4, top + 56, x + 7, top + 59), K)
    d.polygon([(x - 26, top + 92), (x - 78, top + 6), (x - 62, top - 2), (x - 12, top + 84)], fill=B)  # raised arm
    d.ellipse((x - 86, top - 22, x - 58, top + 8), fill=BL)  # fist
    d.line([(x + 30, top + 100), (x + 40, top + 180)], fill=B, width=12); d.ellipse((x + 32, top + 172, x + 50, top + 190), fill=BL)

def malecon(d, f, sunset=False):
    if sunset: sea(d, (250, 150, 90), (250, 210, 150), 600, (40, 110, 170), (240, 200, 160))
    else: sea(d, (80, 170, 240), (200, 230, 250), 600, (40, 150, 190), (200, 240, 240))
    R(d, (0, 690, CW, 706), (200, 196, 186)); R(d, (0, 706, CW, CH), (90, 90, 96))
    for x in range(0, CW, 40): R(d, (x, 724, x + 20, 728), WHITE)

# ---------------- maps ----------------
STODOM_W = (-70, 18.28); SPAIN_W = (-6, 36)
HISP_BOX = (-76, -66, 16.5, 21.5)

# ---------------- backgrounds ----------------
def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i in (0, 2) and not (i == 0 and li == 1): nave(d); church_window(d, 230, 180)
    elif i == 0 and li == 1: jungle_village(d)
    elif i == 1:
        if li == 0: day_sea(d, 600); town(d, 600, 300, CW); dock(d, 300)
        elif li == 1: jungle_village(d)
        else: room(d)
    elif i == 3:
        if li == 0: nave(d); church_window(d, 400, 180)
        else: colony(d); church(d, 400, 690)
    elif i == 4:
        if li == 0: day_sea(d, 600); dock(d, 160)
        else: court(d)
    elif i == 5:
        if li == 0: court(d)
        elif li == 1: beach(d); palm(d, 470, 655, 200, -1)
        else: jungle_village(d)
    elif i == 6:
        if li == 0: jungle_village(d)
        elif li == 1: nave(d); church_window(d, 60, 180)
        else: village(d)
    elif i == 7:
        malecon(d, 0, sunset=(li == 1))
    return c

# ---------------- scenes ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        if li == 0:
            candles_row(d, f, 30, 200, 560)
            pulpit(c, d, 340, 470, "domp", f); label(d, "FRIAR", 410, 380, GOLD)
            pews(c, d, f, angry=prog > 0.6, n=6)
            label(d, "COLONISTS", 160, 620, WHITE, K)
            label(d, "HISPANIOLA, 1511", 270, 250, K, YEL, F16)
            if prog > 0.55: label(d, "\"MORTAL SIN!\"", 300, 300, WHITE, RED, F16)
        else:
            gulls(d, f, 3, 330)
            conuco(d, 280, 700, 4); clouds(d, f, 140, seed=5)
            for k in range(4):
                x = 20 + k * 62 + (f * 0.8 + k * 20) % 20; put(c, f"tai{st(f, k, 6)}", x, FEET - (k % 2) * 10)
                put(c, "sack", x + 10, FEET - 80 - (k % 2) * 10)
            put(c, "set2", 420, FEET, sc=2, flip=True); label(d, "OVERSEER", 472, 545, GOLD)
            label(d, "TAÍNO WORKERS", 140, 620, WHITE, K)
            label(d, "ENCOMIENDA", 270, 250, WHITE, RED_D, F16)
    elif i == 1:
        if li == 0:
            c.alpha_composite(region_map(f, HISP_BOX, h=250, labels=[("HISPANIOLA", -71.2, 20.6, K, YEL), ("SANTO DOMINGO", -69.6, 17.5, WHITE, K)],
                                         title="DOMINICANS ARRIVE, 1510", dots=[STODOM]), (25, 110))
            clouds(d, f, 400, seed=2); gulls(d, f, 3, 420)
            put(c, "ship", 340, 600 + bob(f, 3, 0.1), k=0.9)
            waves(d, f, 600, (200, 230, 250))
            for k, key in enumerate(("dom", "dom2", "dom3")): put(c, key, 20 + k * 56 + min(1, prog * 1.5) * 60, 690, flip=True)
            put(c, "domp", 200, FEET, sc=2); label(d, "PEDRO DE CÓRDOBA", 250, 545, GOLD)
            label(d, "DOMINICAN FRIARS", 110, 580, WHITE, K)
        elif li == 1:
            gold_mine(c, d, f)
            for k in range(3):
                x = 200 + k * 60 + (f * 0.8 + k * 20) % 20; put(c, f"tai{st(f, k, 6)}", x, FEET - (k % 2) * 8)
                put(c, "sack", x + 10, FEET - 80 - (k % 2) * 8)
            put(c, "set1", 400, FEET, flip=True); label(d, "SETTLER", 426, 630, WHITE, K)
            put(c, "dom", 10, FEET, sc=2); put(c, "dom2", 100, FEET, sc=1)
            label(d, "FRIARS", 62, 545, GOLD); label(d, "TAÍNO", 270, 600, GOLD)
            label(d, "RIVER GOLD", 140, 670, K, YEL)
            label(d, "FORCED LABOR", 270, 250, WHITE, RED, F16)
        else:
            R(d, (120, 560, 420, 580), (110, 70, 36)); R(d, (140, 580, 150, FEET), (90, 58, 30)); R(d, (390, 580, 400, FEET), (90, 58, 30))
            scroll(d, 230, 500); candle(d, 160, 560, f); candle(d, 360, 560, f + 3)
            window(d, 200, 250, 140, 120, night=True)
            for k, key in enumerate(("dom", "dom2", "dom3", "dom")): put(c, key, 20 + k * 130 if k < 2 else 20 + k * 130, FEET, sc=1, flip=k >= 2)
            put(c, "domp", 30, FEET, sc=2); label(d, "PEDRO DE CÓRDOBA", 130, 420, GOLD)
            n = min(4, int(prog * 5))
            for k in range(n): d.line([(244 + k * 10, 538), (250 + k * 10, 532)], fill=K, width=2)
            label(d, "SIGNED BY ALL", 300, 640, WHITE, RED_D)
            label(d, "ONE SERMON", 270, 200, K, YEL, F16)
    elif i == 2:
        candles_row(d, f, 30, 200, 560)
        pulpit(c, d, 340, 470, "domp" if (li > 0 and (f // 20) % 2 == 0) or li == 0 else "dom", f)
        pews(c, d, f, angry=li == 2, n=6)
        label(d, "ANTONIO DE MONTESINOS", 300, 380, GOLD)
        if li == 0:
            label(d, "4TH SUNDAY OF ADVENT", 270, 250, K, YEL, F16); label(d, "DECEMBER 21, 1511", 270, 290, WHITE, K, F16)
        elif li == 1:
            quote_box(d, ["ARE THEY NOT HUMAN?", "HAVE THEY NO SOULS?"][: 1 + (prog > 0.45)], 240)
        else:
            quote_box(d, ["LOVE THEM AS", "YOURSELVES"], 240)
    elif i == 3:
        if li == 0:
            candles_row(d, f, 30, 200, 560)
            put(c, "diego", 30, FEET, sc=2); label(d, "DIEGO COLUMBUS", 120, 545, GOLD)
            label(d, "GOVERNOR", 90, 585, WHITE, K)
            for k in range(4): put(c, ["set1", "set2", "sailor", "set1"][k], 200 + k * 52, FEET - (k % 2) * 6 + bob(f, 4, 0.5, k), flip=k % 2 == 1)
            label(d, "OUTRAGED", 300, 620, WHITE, RED_D)
            for k in range(3):
                if (f // 6 + k) % 3: d.text((230 + k * 60, 520 - (f % 12)), "!", font=ImageFont.truetype(FONT, 24), fill=RED)
            label(d, "SON OF CHRISTOPHER", 270, 250, K, YEL, F16)
        else:
            for k in range(5): put(c, ["set1", "set2", "set1", "sailor", "set2"][k], 10 + k * 50, FEET - (k % 2) * 6 + bob(f, 4, 0.5, k))
            label(d, "COLONISTS", 130, 620, WHITE, K)
            if prog < 0.5: label(d, "\"TAKE IT BACK!\"", 140, 560, WHITE, RED)
            put(c, "domp", 330, FEET, sc=2, flip=True); put(c, "dom2", 450, FEET, flip=True)
            label(d, "MONTESINOS", 382, 545, GOLD)
            if prog > 0.45: label(d, "NO CONFESSION", 380, 300, WHITE, RED_D, F16)
            label(d, "SANTO DOMINGO", 270, 250, K, YEL, F16)
    elif i == 4:
        if li == 0:
            m = world_map(f, labels=[("HISPANIOLA", -80, 12, K, YEL), ("SPAIN", -4, 44, K, YEL)], title="ACROSS THE ATLANTIC")
            md = ImageDraw.Draw(m); w, h = m.size
            P = lambda lon, lat: (6 + (lon + 100) / 125 * (w - 12), 6 + (64 - lat) / 104 * (h - 12))
            draw_route(md, [P(*p) for p in (STODOM_W, (-62, 20), (-40, 30), (-20, 35.5), SPAIN_W)], min(1, prog * 1.3))
            c.alpha_composite(m, (25, 110))
            clouds(d, f, 560, seed=7); waves(d, f, 600, (200, 230, 250))
            put(c, "ship", 260 + prog * 60, 690 + bob(f, 3, 0.1))
            put(c, "domp", 20, 700); put(c, "set1", 80, 700); label(d, "MONTESINOS", 60, 590, GOLD); label(d, "ENVOY", 112, 630, WHITE, K)
            label(d, "SANTO DOMINGO", 90, 550, K, YEL)
        elif li == 1:
            castile_banner(d, 40, 160); aragon_banner(d, 450, 160)
            R(d, (220, 540, 320, 700), (150, 30, 40)); R(d, (210, 530, 330, 548), GOLD)
            put(c, "ferd", 218, 700, sc=2); label(d, "KING FERDINAND", 270, 420, GOLD)
            put(c, "set1", 400, FEET, flip=True); put(c, "set2", 450, FEET, flip=True); label(d, "COLONISTS' ENVOYS", 400, 630, WHITE, K)
            put(c, "dom", 40, FEET); label(d, "FRIAR", 66, 630, GOLD)
            if prog > 0.3: label(d, "\"GROUNDLESS!\"", 270, 250, WHITE, RED, F16)
            if prog > 0.65: label(d, "SEND THEM HOME", 270, 290, K, YEL, F16)
        else:
            castile_banner(d, 40, 160); aragon_banner(d, 450, 160)
            R(d, (220, 540, 320, 700), (150, 30, 40)); R(d, (210, 530, 330, 548), GOLD)
            put(c, "ferd", 218, 700, sc=2); label(d, "KING FERDINAND", 270, 420, GOLD)
            put(c, "domp", 20, FEET, sc=2); label(d, "MONTESINOS", 72, 545, GOLD)
            put(c, "set1", 420, FEET, flip=True); put(c, "set2", 470, FEET, flip=True)
            label(d, "DEBATE AT COURT", 270, 250, K, YEL, F16)
            if prog > 0.55: label(d, "THE KING AGREES", 270, 290, WHITE, (40, 120, 60), F16)
    elif i == 5:
        if li == 0:
            castile_banner(d, 40, 160); aragon_banner(d, 450, 160)
            R(d, (120, 600, 420, 620), (110, 70, 36)); R(d, (140, 620, 150, FEET), (90, 58, 30)); R(d, (390, 620, 400, FEET), (90, 58, 30))
            law_book(d, 170, 470, prog); quill(d, 360, 520, f)
            put(c, "ferd", 400, FEET, sc=2, flip=True); label(d, "KING FERDINAND", 420, 545, GOLD)
            label(d, "LAWS OF BURGOS", 270, 250, K, YEL, F16); label(d, "DEC 27, 1512", 270, 290, WHITE, K, F16)
            if prog > 0.6: label(d, "35 LAWS", 270, 430, WHITE, RED_D, F16)
        elif li == 1:
            whip_cross(d, 60, 310); label(d, "NO ABUSE", 92, 400, WHITE, RED_D)
            hammock(c, d, 200, 440, 520, f); label(d, "HAMMOCKS", 320, 470, GOLD)
            put(c, "tai0", 20, FEET); put(c, "tai1", 80, FEET); put(c, "cacica", 130, FEET); label(d, "TAÍNO", 100, 620, GOLD)
            label(d, "NEW RULES", 380, 250, K, YEL, F16)
        else:
            for k in range(3): hut(d, 300 + k * 80, 640, 54)
            calendar(d, 50, 250, "5", "MONTHS", RED_D); calendar(d, 210, 250, "40", "DAYS", (40, 120, 60))
            label(d, "MINING", 100, 360, WHITE, RED_D); label(d, "REST", 260, 360, WHITE, (40, 120, 60))
            put(c, "cacica", 380, FEET, sc=2, flip=True); label(d, "PREGNANT WOMEN", 400, 545, GOLD)
            label(d, "NO HEAVY LABOR", 400, 500, WHITE, K)
            for k in range(3): put(c, f"tai{k % 2}", 40 + k * 60, FEET - (k % 2) * 6)
            label(d, "WORKERS REST", 130, 620, WHITE, K)
    elif i == 6:
        if li == 0:
            conuco(d, 280, 700, 4)
            for k in range(4):
                x = 20 + k * 62 + (f * 0.8 + k * 20) % 20; put(c, f"tai{st(f, k, 6)}", x, FEET - (k % 2) * 10)
                put(c, "sack", x + 10, FEET - 80 - (k % 2) * 10)
            put(c, "set2", 420, FEET, sc=2, flip=True); label(d, "ENCOMENDERO", 450, 545, GOLD)
            clouds(d, f, 140, seed=4); law_book(d, 170, 300, 1.0); label(d, "LAWS OF BURGOS", 270, 260, K, YEL, F16)
            if prog > 0.45:
                R(d, (120, 345, 420, 385), WHITE); d.rectangle((120, 345, 420, 385), outline=RED, width=4)
                d.text((270, 366), "POORLY ENFORCED", font=F16, fill=RED, anchor="mm")
            label(d, "STILL FORCED LABOR", 150, 620, WHITE, K)
        elif li == 1:
            candles_row(d, f, 300, 520, 560)
            pulpit(c, d, 340, 470, "domp", f); label(d, "MONTESINOS", 410, 380, GOLD)
            put(c, "casas", 40, FEET, sc=2); label(d, "BARTOLOMÉ DE LAS CASAS", 200, 545, GOLD)
            put(c, "set1", 160, FEET, flip=True); put(c, "set2", 220, FEET, flip=True)
            label(d, "HE WAS LISTENING", 270, 250, K, YEL, F16)
        else:
            for k in range(2): hut(d, 300 + k * 110, 640, 60)
            clouds(d, f, 140, seed=6); gulls(d, f, 3, 330)
            put(c, "casas", 30, FEET, sc=2); label(d, "LAS CASAS", 82, 545, GOLD)
            sx = 130; R(d, (sx, 620, sx + 24, 660), (240, 226, 180)); R(d, (sx + 30 + int(prog * 40), 620 + int(prog * 50), sx + 54 + int(prog * 40), 660 + int(prog * 50)), (240, 226, 180))
            d.line([(sx + 24, 620), (sx + 30 + int(prog * 40), 620 + int(prog * 50))], fill=K, width=1)
            label(d, "ENCOMIENDA", 225, 592, WHITE, RED_D)
            for k in range(3): put(c, f"tai{st(f, k, 8)}", 290 + k * 70, FEET - (k % 2) * 6, flip=True)
            put(c, "cacica", 470, FEET, flip=True); label(d, "TAÍNO", 400, 620, GOLD)
            label(d, "A LIFE OF DEFENSE", 270, 250, K, YEL, F16)
    elif i == 7:
        gulls(d, f, 3, 260, WHITE if li == 0 else (80, 50, 50))
        if li == 0: clouds(d, f, 150)
        waves(d, f, 600, (200, 240, 240) if li == 0 else (240, 200, 160))
        statue(d, 440, 690, f, 430)
        label(d, "MONTESINOS", 440, 300, GOLD); label(d, "15 M", 520, 470, WHITE, K)
        put(c, "pr1", 30, FEET); put(c, "pr2", 90, FEET, flip=True); put(c, "pr3", 150, FEET)
        if li == 0:
            label(d, "SANTO DOMINGO", 120, 250, K, YEL, F16); label(d, "GIFT FROM MEXICO, 1982", 130, 380, WHITE, K)
            label(d, "VISITORS", 120, 630, WHITE, K)
        else:
            quote_box(d, ["A VOICE FOR", "HUMAN DIGNITY"], 160)
            if prog > 0.45: label(d, "FOLLOW FOR MORE HISTORY", 192, 610, WHITE, RED, F16)
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
