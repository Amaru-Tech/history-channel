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
OUT = f"{D}/out_ep09"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep09_fountain_of_youth_myth_EN.mp4"

_src9 = open(f"{D}/build_ep06.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- maps ----------------")[0]
exec(_src9)  # episode 6: cacica, modern islanders, zemi, hammock, barbacoa, conuco, batey, swirl, cave props
_src9b = open(f"{D}/build_ep06.py").read().split("# ---------------- backgrounds ----------------")[-1].split("def make_bg")[0]
exec(_src9b)  # episode 6 backgrounds: beach, jungle_village, colony
_src9c = open(f"{D}/build_ep05.py").read().split("# ---------------- backgrounds ----------------")[-1].split("def make_bg")[0]
exec(_src9c)  # episode 5 backgrounds: court, room, village, cabin, jamaica_bay

_src10 = open(f"{D}/build_ep07.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- maps ----------------")[0]
exec(_src10)  # episode 7: dominicans, Diego Columbus, cleric, pulpit, nave, calendar, law book, statue, malecon
_src11 = open(f"{D}/build_ep08.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- maps ----------------")[0]
exec(_src11)  # episode 8: recolor, Balboa, dog, Pedrarias, porters, barrel, deck, jungle, vines, parrots, peak, ring, coin, crane, scaffold

SCENES = [
 ("THE FOUNTAIN OF YOUTH?", [
  ("You may have heard that this man searched for a magic Fountain of Youth.", "You may have heard that this man searched for a magic Fountain of Youth."),
  ("There is no evidence that he ever did.", "There is no evidence that he ever did.")]),
 ("THE CONQUISTADOR", [
  ("His name was {Juan Ponce de León}. He probably sailed with Columbus in fourteen ninety-three.", "His name was Juan Ponce de León. He probably sailed with Columbus in 1493."),
  ("In fifteen oh-eight, he began the conquest of Puerto Rico, and soon became its first governor.", "In 1508, he began the conquest of Puerto Rico, and soon became its first governor.")]),
 ("PUSHED OUT", [
  ("In fifteen eleven, he lost that post to {Diego} Columbus, the son of Christopher Columbus.", "In 1511, he lost that post to Diego Columbus, the son of Christopher Columbus."),
  ("In fifteen twelve, King Ferdinand gave him a new contract: find and settle an island called {Bimini}.", "In 1512, King Ferdinand gave him a new contract: find and settle an island called Bimini.")]),
 ("LA FLORIDA", [
  ("In March fifteen thirteen, he sailed north from Puerto Rico with three ships.", "In March 1513, he sailed north from Puerto Rico with three ships."),
  ("In early April, he reached a long green coast. It was the Easter season, {Pascua Florida} in Spanish.", "In early April, he reached a long green coast. It was the Easter season, Pascua Florida in Spanish."),
  ("He named the land {La Florida}, and thought it was an island.", "He named the land La Florida, and thought it was an island.")]),
 ("WHERE DID HE LAND?", [
  ("No one knows exactly where he first came ashore.", "No one knows exactly where he first came ashore."),
  ("Today, both Saint Augustine and Melbourne Beach claim the spot.", "Today, both St. Augustine and Melbourne Beach claim the spot.")]),
 ("A RIVER IN THE SEA", [
  ("Sailing along the coast, his ships met a powerful current: the Gulf Stream.", "Sailing along the coast, his ships met a powerful current: the Gulf Stream."),
  ("It later became the fastest route for ships sailing home to Europe.", "It later became the fastest route for ships sailing home to Europe.")]),
 ("THE LAST VOYAGE", [
  ("In fifteen twenty-one, he returned with two ships and about two hundred people, to found a colony.", "In 1521, he returned with two ships and about 200 people, to found a colony."),
  ("Native warriors fought back. He was wounded by an arrow, and died in Cuba.", "Native warriors fought back. He was wounded by an arrow, and died in Cuba.")]),
 ("HOW THE MYTH WAS BORN", [
  ("In fifteen thirty-five, the royal chronicler {Oviedo}, who disliked him, wrote that he had chased a magic fountain.", "In 1535, the royal chronicler Oviedo, who disliked him, wrote that he had chased a magic fountain."),
  ("It was meant as mockery. In sixteen oh-one, another royal historian repeated the tale, and it stuck.", "It was meant as mockery. In 1601, another royal historian repeated the tale, and it stuck."),
  ("No known document from his lifetime mentions a fountain at all.", "No known document from his lifetime mentions a fountain at all.")]),
 ("THE LEGEND LIVES ON", [
  ("Today, visitors in Saint Augustine still drink from a Fountain of Youth well.", "Today, visitors in St. Augustine still drink from a Fountain of Youth well."),
  ("He gave Florida its name, yet he is remembered for a quest he never made.", "He gave Florida its name, yet he is remembered for a quest he never made.")]),
]

# ---------------- narration: piper ryan-high (channel voice) with raw IPA for Spanish names ----------------
import re as _re
IPA = {"Juan Ponce de León": "hwˈɑn pˈɔnseɪ dɛ leɪˈoʊn", "Diego": "diˈeɪɡoʊ", "Bimini": "bˈɪmɪni",
       "Pascua Florida": "pˈɑskwɑ floʊɹˈiːdɑ", "La Florida": "lɑ floʊɹˈiːdɑ", "Oviedo": "ˌoʊviˈeɪdoʊ"}
_tts_piper = tts
def tts(text, path):
    _tts_piper(_re.sub(r"\{([^}]+)\}", lambda m: f"[[ {IPA[m.group(1)]} ]]", text), path)

if "durs" in sys.argv:
    tot = 0
    for i, (head, lines) in enumerate(SCENES):
        for li, (sp, cap) in enumerate(lines):
            p = f"{OUT}/t{i}_{li}.wav"; tts(sp, p); dd = wavdur(p) + 0.3; tot += dd; print(i, li, round(dd, 1))
    print("TOTAL", round(tot + len(SCENES) * 0.25 + 2, 1)); sys.exit()

_label_orig = label
def label(d, text, cx, y, fg=WHITE, bg=K, font=F16):
    w = d.textlength(text, font=font); cx = min(max(cx, w / 2 + 8), CW - w / 2 - 8)
    _label_orig(d, text, cx, y, fg, bg, font)

# ---------------- extra sprites ----------------
GREEN_C = (40, 120, 70); GREEN_CD = (26, 84, 48)
def ponce_sprite(step=0):  # conquistador leader recolored: green cape and sleeves, reddish beard
    return recolor(SP[f"piz{step}"], {RED: GREEN_C, RED_D: GREEN_CD, tint_c(RED, 0.8): GREEN_CD, (150, 140, 132): (150, 80, 40), (150, 40, 40): (40, 60, 40)})

def chronicler(robe=(30, 30, 36), robe_d=(18, 18, 22), hair=(60, 44, 30), beard=True):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, robe, robe_d); R(d, (16, 36, 36, 40), WHITE)  # ruff collar
    R(d, (34, 46, 44, 58), (130, 30, 34)); d.rectangle((34, 46, 44, 58), outline=K)  # book under arm
    face(d); R(d, (17, 13, 35, 18), hair); R(d, (17, 18, 19, 26), hair); R(d, (33, 18, 35, 26), hair)
    if beard: d.polygon([(19, 28), (33, 28), (31, 36), (26, 39), (21, 36)], fill=hair); R(d, (24, 30, 28, 30), (150, 80, 70))
    R(d, (16, 9, 36, 13), K)
    return outline(im)

def old_man():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im); GR = (200, 200, 196)
    robe_body(d, (120, 100, 80), (90, 74, 58)); face(d)
    R(d, (17, 13, 35, 17), GR); R(d, (17, 17, 19, 26), GR); R(d, (33, 17, 35, 26), GR)
    d.polygon([(18, 27), (34, 27), (32, 42), (26, 48), (20, 42)], fill=GR); R(d, (24, 30, 28, 30), (150, 80, 70))
    d.line([(44, 40), (46, 80)], fill=BROWN_D, width=3)  # cane
    return outline(im)

def archer(step=0):
    im = SP[f"tai{step}"].copy(); d = ImageDraw.Draw(im)
    d.arc((30, 24, 50, 64), 270, 90, fill=BROWN_D, width=3); d.line([(40, 24), (40, 64)], fill=(230, 220, 200), width=1)
    return im

SP.update({"pon0": ponce_sprite(0), "pon1": ponce_sprite(1), "ovi": chronicler(), "herr": chronicler((60, 30, 70), (40, 20, 48), (120, 110, 100)),
           "old": old_man(), "arch0": archer(0), "arch1": archer(1)})

# ---------------- props ----------------
def fountain(d, cx, base, f, dry=False):
    S = (176, 170, 160); SD = (130, 124, 116)
    d.ellipse((cx - 110, base - 40, cx + 110, base + 10), fill=SD); d.ellipse((cx - 100, base - 44, cx + 100, base - 4), fill=S)
    d.ellipse((cx - 86, base - 38, cx + 86, base - 10), fill=(110, 110, 100) if dry else (70, 160, 210))
    R(d, (cx - 12, base - 140, cx + 12, base - 24), S); R(d, (cx + 2, base - 140, cx + 12, base - 24), SD)
    d.ellipse((cx - 50, base - 152, cx + 50, base - 130), fill=SD); d.ellipse((cx - 44, base - 156, cx + 44, base - 136), fill=(70, 160, 210) if not dry else (110, 110, 100))
    if not dry:
        for k in range(6):
            ph = (f * 2 + k * 9) % 54
            for s in (-1, 1):
                x = cx + s * (20 + ph * 1.1); y = base - 160 + (ph * ph) / 22 - ph * 0.6
                if y < base - 20: R(d, (x, y, x + 3, y + 5), (170, 220, 250))
        for k in range(5):
            if (f // 6 + k) % 3 == 0: x = cx - 70 + k * 34; y = base - 190 + (k % 2) * 20; d.line([(x - 5, y), (x + 5, y)], fill=WHITE); d.line([(x, y - 5), (x, y + 5)], fill=WHITE)

def stamp(d, text, cx, cy, sc=1.0):
    fnt = ImageFont.truetype(FONT, int(28 * sc)); w = d.textlength(text, font=fnt)
    d.rectangle((cx - w / 2 - 14, cy - 26 * sc, cx + w / 2 + 14, cy + 26 * sc), outline=RED, width=6)
    d.text((cx, cy), text, font=fnt, fill=RED, anchor="mm")

def flowers(d, y0, y1, seed=5, n=40):
    rnd = random.Random(seed)
    for _ in range(n):
        x, y = rnd.randint(0, CW), rnd.randint(y0, y1); col = rnd.choice([(240, 90, 120), (250, 220, 80), (250, 250, 250), (200, 110, 220)])
        R(d, (x, y, x + 4, y + 4), col); R(d, (x + 1, y + 5, x + 2, y + 9), (40, 110, 50))

def sign(d, x, base, text, col=(120, 80, 40)):
    w = d.textlength(text, font=F8) + 20
    R(d, (x + w / 2 - 3, base - 90, x + w / 2 + 3, base), BROWN_D)
    R(d, (x, base - 120, x + w, base - 84), col); d.rectangle((x, base - 120, x + w, base - 84), outline=K, width=2)
    d.text((x + w / 2, base - 102), text, font=F8, fill=WHITE, anchor="mm")

def current_arrows(d, f, y0, y1, col=(170, 220, 250), speed=4):
    for k in range(10):
        y = y0 + (k * 37) % max(1, (y1 - y0)); x = (k * 83 + f * speed) % (CW + 80) - 40
        d.line([(x, y), (x + 50, y)], fill=col, width=3); d.polygon([(x + 50, y - 6), (x + 62, y), (x + 50, y + 6)], fill=col)

def arrow_fly(d, f, k, x0, y0, x1, y1, period=24):
    p = ((f + k * 7) % period) / period; x = x0 + (x1 - x0) * p; y = y0 + (y1 - y0) * p - math.sin(p * math.pi) * 40
    d.line([(x, y), (x - 22, y + 4)], fill=BROWN_D, width=2); d.polygon([(x, y - 3), (x + 7, y), (x, y + 3)], fill=STEEL_D)

def well(d, cx, base):
    S = (170, 160, 140); SD = (130, 120, 104)
    R(d, (cx - 60, base - 70, cx + 60, base), S)
    for y in range(base - 70, base, 14):
        for x in range(cx - 60 + ((y // 14) % 2) * 15, cx + 60, 30): d.rectangle((x, y, x + 30, y + 14), outline=SD)
    R(d, (cx - 66, base - 78, cx + 66, base - 70), SD)
    R(d, (cx - 56, base - 170, cx - 48, base - 78), BROWN_D); R(d, (cx + 48, base - 170, cx + 56, base - 78), BROWN_D)
    d.polygon([(cx - 80, base - 166), (cx, base - 210), (cx + 80, base - 166)], fill=(150, 60, 40))
    d.line([(cx, base - 166), (cx, base - 110)], fill=K, width=2); R(d, (cx - 10, base - 110, cx + 10, base - 94), BROWN)

def oak(d, x, base, h=200):
    R(d, (x - 8, base - h, x + 8, base), BROWN_D)
    for k in range(5): d.ellipse((x - 70 + k * 20, base - h - 40 + (k % 2) * 20, x - 10 + k * 20, base - h + 30), fill=(50, 100, 50))
    for k in range(4): d.line([(x - 50 + k * 30, base - h + 20), (x - 52 + k * 30, base - h + 90)], fill=(150, 160, 140), width=2)  # spanish moss

def old_book(d, x, y, title, col=(130, 30, 34)):
    R(d, (x, y, x + 120, y + 150), col); R(d, (x + 8, y + 8, x + 112, y + 142), tint_c(col, 0.8)); d.rectangle((x, y, x + 120, y + 150), outline=K, width=2)
    d.text((x + 60, y + 50), title, font=F8, fill=GOLD, anchor="mm")

# ---------------- maps ----------------
FLA = [(-88, 31.8), (-88, 30.4), (-87.3, 30.35), (-86.5, 30.4), (-85.4, 29.9), (-84.9, 29.7), (-84.3, 30.0), (-83.6, 29.9), (-83.0, 29.1),
       (-82.7, 28.2), (-82.8, 27.8), (-82.6, 27.4), (-82.2, 26.7), (-81.8, 26.1), (-81.3, 25.6), (-80.9, 25.15), (-80.4, 25.2), (-80.1, 25.8),
       (-80.05, 26.6), (-80.2, 27.3), (-80.6, 28.3), (-80.6, 28.6), (-81.0, 29.2), (-81.3, 29.9), (-81.45, 30.7), (-81.2, 31.8)]
FLA_BOX = (-88, -64, 16.5, 31.5)
PR_W = (-67.2, 18.3); LAND = (-81.0, 29.2); STAUG = (-81.3, 29.9); MELB = (-80.6, 28.3); HAVANA = (-82.3, 23.14); CHARL = (-82.2, 26.7)
def fla_map(f, title, route=None, dots=(), labels=(), h=320):
    return region_map(f, FLA_BOX, h=h, labels=labels, route=route, title=title, dots=dots)
# a tighter box for the landing question
LAND_BOX = (-84.5, -77.5, 24.4, 31.2)

# ---------------- backgrounds ----------------
def fla_coast(d, sunset=False):
    beach(d, "sunset" if sunset else "day")
    for k in range(4): palm(d, 380 + k * 50, 660 - k * 4, 140 + (k % 2) * 40, -1 if k % 2 else 1)
    flowers(d, 700, 760, 3, 30)

def park(d):
    grad(d, (90, 170, 240), (210, 230, 250), 0, 640, 10); clouds_static = None
    R(d, (0, 640, CW, CH), (110, 160, 80))
    rnd = random.Random(4)
    for _ in range(80): x, y = rnd.randint(0, CW), rnd.randint(644, CH); R(d, (x, y, x + 2, y), (90, 140, 60))
    oak(d, 60, 650, 220); oak(d, 470, 650, 200)

def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0: fla_coast(d)
    elif i == 1:
        if li == 0: day_sea(d, 600); dock(d, 300)
        else: village(d)
    elif i == 2: court(d)
    elif i == 3:
        if li == 0: day_sea(d, 600)
        else: fla_coast(d)
    elif i == 4:
        if li == 0: day_sea(d, 600)
        else: beach(d)
    elif i == 5:
        if li == 0: day_sea(d, 560)
        else: day_sea(d, 600)
    elif i == 6:
        if li == 0: fla_coast(d)
        else: fla_coast(d, sunset=True)
    elif i == 7: room(d)
    elif i == 8:
        if li == 0: park(d)
        else: beach(d, "sunset")
    return c

# ---------------- scenes ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        clouds(d, f, 150, seed=2); gulls(d, f, 3, 300)
        fountain(d, 330, 730, f, dry=(li == 1 and prog > 0.3))
        put(c, "pon0", 20, FEET + 10, sc=2); label(d, "JUAN PONCE DE LEÓN", 150, 555, GOLD)
        label(d, "FLORIDA, 1513", 270, 250, K, YEL, F16)
        if li == 0:
            label(d, "FOUNTAIN OF YOUTH", 330, 470, WHITE, K, F16)
            put(c, "old", 450, FEET + 10, flip=True); label(d, "OLD MEN YOUNG AGAIN?", 270, 290, WHITE, K)
        else:
            if prog > 0.3: stamp(d, "NO EVIDENCE", 330, 470, 0.9)
            label(d, "A MYTH", 330, 400, WHITE, RED_D, F16)
    elif i == 1:
        if li == 0:
            clouds(d, f, 140, seed=1); gulls(d, f, 3, 300)
            for k in range(3): put(c, "ship" if k == 0 else tint(SP["ship"], 0.8), 320 + k * 70 - t * 3, 620 + k * 30 + bob(f, 3, 0.1, k))
            put(c, "col", 40, 690); label(d, "COLUMBUS", 66, 590, WHITE, K)
            put(c, "pon0", 130, 690, sc=2); label(d, "PONCE DE LEÓN", 182, 497, GOLD)
            label(d, "SECOND VOYAGE, 1493", 270, 250, K, YEL, F16); label(d, "PROBABLY ABOARD", 270, 290, WHITE, K, F16)
        else:
            c.alpha_composite(fla_map(f, "PUERTO RICO, 1508", dots=[PR_W], labels=[("PUERTO RICO", -66.4, 19.6, K, YEL), ("HISPANIOLA", -71.0, 17.6, WHITE, K)], h=300), (25, 110))
            put(c, "pon0", 200, FEET, sc=2); label(d, "PONCE DE LEÓN", 252, 545, GOLD)
            castile_banner(d, 40, 470); R(d, (38, 470, 41, 700), BROWN_D)
            march(c, f, 330, 3, ["esp"], base=FEET, dx=60, speed=0.3)
            if prog > 0.4: label(d, "FIRST GOVERNOR", 400, 620, WHITE, RED_D)
    elif i == 2:
        castile_banner(d, 40, 160); castile_banner(d, 450, 160)
        if li == 0:
            put(c, "pon0", 20, FEET, sc=2); label(d, "PONCE DE LEÓN", 90, 545, GOLD)
            put(c, "diego", 416, FEET, sc=2, flip=True); label(d, "DIEGO COLUMBUS", 450, 545, GOLD)
            label(d, "COLUMBUS'S SON", 450, 580, WHITE, K)
            label(d, "1511", 270, 250, K, YEL, F16)
            if prog > 0.4: label(d, "GOVERNOR NO MORE", 270, 400, WHITE, RED, F16)
        else:
            put(c, "ferd", 330, FEET, sc=2, flip=True); label(d, "KING FERDINAND", 400, 545, GOLD)
            put(c, "pon0", 20, FEET, sc=2); label(d, "PONCE DE LEÓN", 90, 545, GOLD)
            scroll(d, 230, 470 + bob(f, 3, 0.1)); label(d, "CONTRACT, 1512", 270, 250, K, YEL, F16)
            if prog > 0.4: label(d, "FIND AND SETTLE BIMINI", 270, 400, WHITE, K, F16)
    elif i == 3:
        if li == 0:
            c.alpha_composite(fla_map(f, "MARCH 1513", route=([PR_W, (-70, 20.6), (-74, 23.4), (-78.4, 27.2), LAND], min(1, prog * 1.15)), dots=[PR_W],
                                      labels=[("PUERTO RICO", -66.4, 19.6, K, YEL), ("FLORIDA", -83.6, 29.0, WHITE, K), ("BAHAMAS", -73.4, 25.6, WHITE, K)]), (25, 110))
            waves(d, f, 600, (200, 230, 250)); gulls(d, f, 2, 470)
            for k in range(3): put(c, "ship" if k == 0 else tint(SP["ship"], 0.8), 40 + k * 140 + t * 4, 690 + (k % 2) * 30 + bob(f, 3, 0.1, k))
            label(d, "3 SHIPS", 270, 470, WHITE, K, F16)
        elif li == 1:
            clouds(d, f, 150, seed=5); gulls(d, f, 3, 300)
            put(c, "ship", 40, 600 + bob(f, 3, 0.1)); waves(d, f, 560, (200, 240, 240))
            x = 200 + min(1, prog * 1.5) * 40
            put(c, f"pon{st(f, 0, 6)}", x, FEET, sc=2); label(d, "PONCE DE LEÓN", x + 52, 545, GOLD)
            label(d, "EARLY APRIL 1513", 270, 250, K, YEL, F16)
            if prog > 0.45: label(d, "EASTER: PASCUA FLORIDA", 270, 290, WHITE, RED_D, F16)
        else:
            clouds(d, f, 150, seed=5); gulls(d, f, 3, 300)
            put(c, "ship", 40, 600 + bob(f, 3, 0.1))
            R(d, (180, 460, 184, 740), BROWN_D); castile_banner(d, 126, 464)
            put(c, "pon0", 200, FEET, sc=2); label(d, "PONCE DE LEÓN", 252, 545, GOLD)
            march(c, f, 380, 2, ["esp"], base=FEET, dx=60, speed=0.1)
            label(d, "LA FLORIDA", 270, 250, K, YEL, F16)
            if prog > 0.45: label(d, "AN ISLAND?", 270, 400, WHITE, K, F16)
    elif i == 4:
        if li == 0:
            c.alpha_composite(region_map(f, LAND_BOX, h=330, title="APRIL 1513", dots=[STAUG, MELB],
                                         labels=[("ST. AUGUSTINE", -78.9, 29.9, K, YEL), ("MELBOURNE BEACH", -80.0, 27.5, K, YEL), ("FLORIDA", -82.6, 28.6, WHITE, K)]), (25, 110))
            waves(d, f, 600, (200, 230, 250))
            put(c, "ship", 200 + bob(f, 6, 0.05), 700 + bob(f, 3, 0.1))
            for k in range(3):
                if (f // 12 + k) % 2: d.text((80 + k * 170, 520 + (k % 2) * 20), "?", font=ImageFont.truetype(FONT, 36), fill=YEL)
            label(d, "NO ONE KNOWS", 270, 480, WHITE, RED_D, F16)
        else:
            clouds(d, f, 150, seed=7); gulls(d, f, 3, 300)
            sign(d, 30, 730, "ST. AUGUSTINE"); sign(d, 300, 730, "MELBOURNE BEACH")
            put(c, "pr1", 50, FEET); put(c, "pr2", 110, FEET, flip=True)
            put(c, "pr3", 330, FEET); put(c, "pr1", 400, FEET, flip=True)
            label(d, "TWO CITIES, ONE CLAIM", 270, 250, K, YEL, F16)
            if prog > 0.35: label(d, "HE LANDED HERE!", 120, 500, WHITE, K); label(d, "NO, HERE!", 420, 500, WHITE, K)
    elif i == 5:
        clouds(d, f, 140, seed=4)
        if li == 0:
            current_arrows(d, f, 580, 740, speed=5)
            for k in range(3): put(c, "ship" if k == 0 else tint(SP["ship"], 0.8), 120 + k * 120 + (f * 1.2) % 40 - 20, 660 + (k % 2) * 40 + bob(f, 4, 0.2, k))
            label(d, "THE GULF STREAM", 270, 250, K, YEL, F16); label(d, "A POWERFUL CURRENT", 270, 290, WHITE, K, F16)
            gulls(d, f, 2, 330)
        else:
            c.alpha_composite(fla_map(f, "THE GULF STREAM", labels=[("FLORIDA", -83.6, 29.0, WHITE, K), ("CUBA", -79.0, 21.0, WHITE, K)]), (25, 110))
            # current band: Florida Straits up the coast and out to the east
            pts = [(70, 330), (170, 300), (225, 250), (250, 190), (290, 180), (380, 165), (500, 155)]
            for a, b in zip(pts, pts[1:]): d.line([a, b], fill=(120, 200, 250), width=10)
            k = (f // 3) % 12
            for j in range(len(pts) - 1):
                a, b = pts[j], pts[j + 1]; tt = (k / 12 + j * 0.3) % 1; x = a[0] + (b[0] - a[0]) * tt; y = a[1] + (b[1] - a[1]) * tt
                R(d, (x - 3, y - 3, x + 3, y + 3), WHITE)
            label(d, "TO EUROPE", 450, 190, K, YEL)
            waves(d, f, 600, (200, 230, 250))
            for k in range(3): put(c, "ship" if k == 0 else tint(SP["ship"], 0.85), 60 + k * 150 + t * 6, 700 + (k % 2) * 30 + bob(f, 3, 0.1, k))
            label(d, "FASTEST WAY HOME", 270, 480, WHITE, RED_D, F16)
    elif i == 6:
        if li == 0:
            clouds(d, f, 150, seed=8); gulls(d, f, 3, 300)
            put(c, "ship", 30, 610 + bob(f, 3, 0.1)); put(c, tint(SP["ship"], 0.8), 120, 590 + bob(f, 3, 0.1, 1))
            put(c, "pon0", 210, FEET, sc=2); label(d, "PONCE DE LEÓN", 262, 545, GOLD)
            put(c, "horse", 360, FEET - 6); put(c, "set1", 430, FEET); put(c, "set2", 480, FEET, flip=True)
            label(d, "1521: A COLONY", 270, 250, K, YEL, F16); label(d, "ABOUT 200 PEOPLE", 270, 290, WHITE, K, F16)
        else:
            gulls(d, f, 2, 280, (80, 50, 50))
            put(c, "pon0", 60, FEET, sc=2); label(d, "PONCE DE LEÓN", 112, 545, GOLD)
            for k in range(3): put(c, f"arch{st(f, k, 8)}", 340 + k * 60, FEET - (k % 2) * 10, flip=True)
            label(d, "NATIVE WARRIORS", 420, 620, WHITE, K)
            for k in range(3): arrow_fly(d, f, k, 330, 600, 150, 620)
            if prog > 0.35: label(d, "WOUNDED BY AN ARROW", 270, 250, WHITE, RED_D, F16)
            if prog > 0.65: label(d, "DIED IN CUBA, 1521", 270, 290, K, YEL, F16)
    elif i == 7:
        window(d, 380, 150, 110, 140, night=False)
        if li == 0:
            put(c, "ovi", 40, FEET, sc=2); label(d, "OVIEDO", 92, 545, GOLD)
            R(d, (200, 640, 420, 652), BROWN); R(d, (220, 652, 232, 740), BROWN_D); R(d, (390, 652, 402, 740), BROWN_D)
            law_book(d, 210, 560, min(1, prog * 1.5)); quill(d, 380, 600, f); candle(d, 400, 640, f)
            label(d, "ROYAL CHRONICLER, 1535", 270, 250, K, YEL, F16)
            if prog > 0.5: label(d, "A MAGIC FOUNTAIN!", 300, 470, WHITE, K, F16)
        elif li == 1:
            label(d, "MOCKERY", 270, 250, WHITE, RED_D, F16)
            old_book(d, 30, 470, "1535"); label(d, "OVIEDO", 90, 645, WHITE, K); label(d, "1535", 90, 680, K, YEL)
            if prog > 0.4:
                old_book(d, 220, 470, "1601", (40, 60, 120)); label(d, "HERRERA", 280, 645, WHITE, K); label(d, "1601", 280, 680, K, YEL)
                put(c, "herr", 400, FEET, sc=2, flip=True)
            if prog > 0.7: label(d, "THE TALE STUCK", 270, 290, K, YEL, F16)
        else:
            scroll(d, 60, 480); scroll(d, 220, 500); letter(d, 380, 500); letter(d, 420, 520); letter(d, 400, 470)
            label(d, "CONTRACT", 90, 580, WHITE, K); label(d, "LETTERS", 410, 580, WHITE, K)
            label(d, "HIS LIFETIME", 270, 250, K, YEL, F16)
            if prog > 0.4: stamp(d, "NO FOUNTAIN", 270, 400, 0.9)
    elif i == 8:
        if li == 0:
            clouds(d, f, 140, seed=9); gulls(d, f, 2, 300)
            well(d, 270, 690)
            sign(d, 150, 520, "FOUNTAIN OF YOUTH", (40, 90, 60))
            for k, key in enumerate(("pr1", "pr2", "pr3")): put(c, key, 60 + k * 180 if k < 2 else 380, FEET + 10, flip=k == 2)
            label(d, "ST. AUGUSTINE TODAY", 270, 250, K, YEL, F16)
            if prog > 0.4: label(d, "VISITORS DRINK THE WATER", 270, 290, WHITE, K, F16)
        else:
            gulls(d, f, 3, 260, (80, 50, 50)); waves(d, f, 560, (240, 200, 160))
            R(d, (380, 560, 500, 690), (196, 190, 178)); R(d, (372, 550, 508, 562), (210, 204, 192))
            put(c, tint(SP["pon0"], 0.75, (40, 30, 0)), 362, 550, sc=3)
            label(d, "PONCE DE LEÓN", 420, 232, GOLD); label(d, "STATUE", 420, 262, WHITE, K)
            put(c, "pr1", 30, FEET); put(c, "pr2", 90, FEET, flip=True)
            label(d, "HE NAMED FLORIDA", 190, 330, K, YEL, F16); label(d, "THE MYTH CAME LATER", 190, 366, K, YEL, F16)
            if prog > 0.45: label(d, "FOLLOW FOR MORE HISTORY", 192, 610, WHITE, RED, F16)

def march(c, f, x0, n, keys, base=FEET, dx=58, speed=0.6, flip=False):
    for k in range(n):
        x = x0 + k * dx + (f * speed) % dx
        put(c, f"{keys[k % len(keys)]}{st(f, k, 6)}", x, base - (k % 2) * 8, flip=flip)
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
