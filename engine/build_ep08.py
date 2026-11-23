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
OUT = f"{D}/out_ep08"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep08_man_who_found_the_pacific_EN.mp4"

_src9 = open(f"{D}/build_ep06.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- maps ----------------")[0]
exec(_src9)  # episode 6: cacica, modern islanders, zemi, hammock, barbacoa, conuco, batey, swirl, cave props
_src9b = open(f"{D}/build_ep06.py").read().split("# ---------------- backgrounds ----------------")[-1].split("def make_bg")[0]
exec(_src9b)  # episode 6 backgrounds: beach, jungle_village, colony
_src9c = open(f"{D}/build_ep05.py").read().split("# ---------------- backgrounds ----------------")[-1].split("def make_bg")[0]
exec(_src9c)  # episode 5 backgrounds: court, room, village, cabin, jamaica_bay

_src10 = open(f"{D}/build_ep07.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- maps ----------------")[0]
exec(_src10)  # episode 7: dominicans, Diego Columbus, cleric, pulpit, nave, calendar, law book, statue, malecon

SCENES = [
 ("THE MAN IN THE BARREL", [
  ("In fifteen ten, a man deep in debt hid in a barrel on a ship, to escape his creditors.", "In 1510, a man deep in debt hid in a barrel on a ship, to escape his creditors."),
  ("Three years later, he became the first European to see the Pacific from the Americas.", "Three years later, he became the first European to see the Pacific from the Americas.")]),
 ("THE STOWAWAY", [
  ("His name was {Vasco} {Núñez} {de} {Balboa}, a failed farmer on Hispaniola.", "His name was Vasco Núñez de Balboa, a failed farmer on Hispaniola."),
  ("His dog {Leoncico} came with him. Stowing away could be punished by death.", "His dog Leoncico came with him. Stowing away could be punished by death.")]),
 ("A NEW TOWN", [
  ("On the coast of {Darién}, in today's Panama, the settlers founded {Santa María la Antigua}.", "On the coast of Darién, in today's Panama, the settlers founded Santa María la Antigua."),
  ("Balboa took charge. In fifteen eleven, the king made him interim governor.", "Balboa took charge. In 1511, the king made him interim governor.")]),
 ("THE MARCH", [
  ("On September first, fifteen thirteen, he set out with about one hundred ninety Spaniards.", "On September 1, 1513, he set out with about 190 Spaniards."),
  ("Hundreds of Native guides and porters went with them, through jungle and mountains.", "Hundreds of Native guides and porters went with them, through jungle and mountains."),
  ("Among the Spaniards was Francisco {Pizarro}.", "Among the Spaniards was Francisco Pizarro.")]),
 ("THE PEAK", [
  ("On September twenty-fifth, Balboa climbed a peak ahead of his men.", "On September 25, Balboa climbed a peak ahead of his men."),
  ("Below him lay a vast sea that Europeans had never seen from this side of the world.", "Below him lay a vast sea that Europeans had never seen from this side of the world.")]),
 ("THE SOUTH SEA", [
  ("On September twenty-ninth, he waded into the water at the Gulf of {San Miguel}, sword in hand.", "On September 29, he waded into the water at the Gulf of San Miguel, sword in hand."),
  ("He claimed the sea and all its shores for the Crown of Castile. He called it the South Sea.", "He claimed the sea and all its shores for the Crown of Castile. He called it the South Sea.")]),
 ("A DANGEROUS BOSS", [
  ("In fifteen fourteen, a new governor arrived: {Pedrarias Dávila}.", "In 1514, a new governor arrived: Pedrarias Dávila."),
  ("The two men were rivals. Still, {Pedrarias} promised Balboa his daughter {María} in marriage.", "The two men were rivals. Still, Pedrarias promised Balboa his daughter María in marriage."),
  ("Balboa had ships carried in pieces over the mountains, to sail the new sea.", "Balboa had ships carried in pieces over the mountains, to sail the new sea.")]),
 ("BETRAYED", [
  ("In fifteen nineteen, {Pedrarias} had him arrested. The arresting officer was Francisco {Pizarro}.", "In 1519, Pedrarias had him arrested. The arresting officer was Francisco Pizarro."),
  ("Charged with treason, Balboa was beheaded at {Acla}, along with four companions.", "Charged with treason, Balboa was beheaded at Acla, along with four companions.")]),
 ("HIS NAME LIVES ON", [
  ("Today, Panama's currency is called the {balboa}.", "Today, Panama's currency is called the balboa."),
  ("The port at the Pacific entrance of the Panama Canal bears his name too.", "The port at the Pacific entrance of the Panama Canal bears his name too."),
  ("The man who fled in a barrel is remembered on the shores of the ocean he reached.", "The man who fled in a barrel is remembered on the shores of the ocean he reached.")]),
]

# ---------------- narration: piper ryan-high (channel voice) with raw IPA for Spanish names ----------------
import re as _re
IPA = {"Vasco": "bˈɑskoʊ", "Núñez": "nˈuːnjɛs", "de": "dɛ", "Balboa": "bɑlbˈoʊɑ", "balboa": "bɑlbˈoʊɑ", "Leoncico": "lˌeɪɔnsˈiːkoʊ",
       "Darién": "dˌɑɹiˈɛn", "Santa María la Antigua": "sˈɑntɑ mɑɹˈiːɑ lɑ ɑntˈiːɡwɑ", "Pizarro": "pɪzˈɑɹoʊ",
       "San Miguel": "sˈɑn miɡˈɛl", "Pedrarias Dávila": "pɛdɹˈɑɹiɑs dˈɑvilɑ", "Pedrarias": "pɛdɹˈɑɹiɑs", "María": "mɑɹˈiːɑ", "Acla": "ˈɑklɑ"}
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
BLUE_C = (40, 80, 170); BLUE_CD = (26, 52, 120)
def recolor(im, mapping):
    a = np.array(im); out = a.copy()
    for src, dst in mapping.items():
        m = (a[..., 0] == src[0]) & (a[..., 1] == src[1]) & (a[..., 2] == src[2]) & (a[..., 3] > 0)
        out[m, 0], out[m, 1], out[m, 2] = dst
    return Image.fromarray(out)

def balboa_sprite(step=0):  # conquistador leader recolored: blue cape and sleeves, gold plume, dark beard
    im = recolor(SP[f"piz{step}"], {RED: BLUE_C, RED_D: BLUE_CD, tint_c(RED, 0.8): BLUE_CD, (150, 140, 132): (70, 46, 28), (150, 40, 40): (40, 40, 60)})
    return im

def farmer_balboa():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    for x0, x1 in [(20, 23), (29, 32)]: R(d, (x0, 62, x1, 78), (90, 70, 50)); R(d, (x0 - 1, 77, x1 + 1, 81), K)
    R(d, (16, 36, 36, 63), (150, 130, 90)); R(d, (16, 58, 36, 60), BROWN)
    R(d, (11, 37, 16, 56), (150, 130, 90)); R(d, (36, 37, 41, 56), (120, 104, 70)); R(d, (11, 56, 15, 59), SKIN_E); R(d, (37, 56, 41, 59), SKIN_E)
    face(d); R(d, (17, 13, 35, 19), (70, 46, 28))
    d.polygon([(18, 27), (34, 27), (32, 37), (26, 40), (20, 37)], fill=(70, 46, 28)); R(d, (22, 27, 30, 28), (70, 46, 28)); R(d, (24, 30, 28, 30), (150, 80, 70))
    return outline(im)

def dog(step=0):
    im = Image.new("RGBA", (52, 40)); d = ImageDraw.Draw(im); C = (176, 120, 60); CD = (130, 84, 40)
    R(d, (10, 14, 38, 28), C); R(d, (10, 24, 38, 28), CD)
    for x, ph in ((12, 0), (18, 1), (30, 0), (35, 1)): R(d, (x, 28, x + 3, 36 - (2 if (step + ph) % 2 else 0)), CD)
    R(d, (36, 6, 48, 18), C); R(d, (44, 12, 51, 17), C); R(d, (49, 12, 51, 14), K); R(d, (41, 9, 42, 10), K)
    R(d, (36, 3, 40, 8), CD)  # ear
    d.line([(10, 16), (3, 8)], fill=C, width=3)  # tail
    R(d, (36, 18, 42, 20), RED_D)  # collar
    return outline(im)

def pedrarias():
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    robe_body(d, (30, 28, 34), (18, 16, 22))
    for x in range(16, 37, 4): R(d, (x, 38 + abs(26 - x) // 3, x + 2, 40 + abs(26 - x) // 3), GOLD)  # gold chain
    face(d); HW = (220, 218, 212)
    R(d, (17, 14, 35, 18), HW); R(d, (17, 18, 19, 26), HW); R(d, (33, 18, 35, 26), HW)
    d.polygon([(18, 27), (34, 27), (32, 38), (26, 42), (20, 38)], fill=HW); R(d, (24, 30, 28, 30), (150, 80, 70))
    R(d, (15, 8, 37, 14), K); R(d, (18, 5, 34, 8), K)
    return outline(im)

def cueva(step=0, load=False):  # Native guide/porter of the isthmus
    im = SP[f"tai{step}"].copy()
    if load:
        d = ImageDraw.Draw(im); R(d, (8, 20, 44, 30), (150, 110, 60)); d.rectangle((8, 20, 44, 30), outline=K)
    return im

SP.update({"bal0": balboa_sprite(0), "bal1": balboa_sprite(1), "balf": farmer_balboa(), "dog0": dog(0), "dog1": dog(1),
           "pedr": pedrarias(), "port0": cueva(0, True), "port1": cueva(1, True)})
SP["balc"] = chains(SP["bal0"])

# ---------------- props ----------------
def big_barrel(c, d, x, base, f, peek=0.0):
    W, H = 110, 150
    d.ellipse((x, base - H, x + W, base), fill=(130, 84, 44))
    d.chord((x, base - H, x + W, base), 270, 90, fill=(104, 66, 34))
    for yy in (base - H + 26, base - H / 2 - 4, base - 30): R(d, (x + 4, yy, x + W - 4, yy + 6), (70, 70, 76))
    d.ellipse((x, base - H, x + W, base), outline=K, width=2)
    d.text((x + W / 2, base - H / 2 + 22), "FLOUR", font=F8, fill=(230, 210, 170), anchor="mm")
    if peek > 0:
        hy = base - H + 16 - int(40 * peek)
        put(c, "balf", x + 3, hy + 60, sc=2, crop=30)
        im = SP["dog0"].crop((30, 0, 52, 22)); put(c, im.resize((44, 44), Image.NEAREST), x + 62, hy + 50)
        R(d, (x + 6, base - H + 12, x + W - 6, base - H + 18), (104, 66, 34))

def ship_deck(d, f):
    R(d, (0, 640, CW, CH), (120, 80, 46))
    for x in range(0, CW, 30): R(d, (x, 640, x + 1, CH), (90, 58, 30))
    R(d, (0, 600, CW, 640), (100, 64, 34)); R(d, (0, 596, CW, 602), (150, 104, 60))
    R(d, (440, 120, 452, 640), BROWN_D)
    for y in (200, 330): d.line([(452, y), (CW, y + 160)], fill=(60, 40, 24), width=2)

def jungle(d, dark=False):
    grad(d, (60, 140, 120) if not dark else (30, 60, 50), (150, 200, 160) if not dark else (70, 100, 80), 0, 620, 10)
    for k in range(10):
        x = k * 60 - 30; d.ellipse((x, 300 + (k % 3) * 40, x + 120, 660), fill=(30, 100, 50) if not dark else (20, 60, 34))
    for k in range(7):
        x = k * 90 - 10; d.ellipse((x, 420 + (k % 2) * 30, x + 110, 680), fill=(40, 120, 60) if not dark else (26, 70, 40))
    R(d, (0, 660, CW, CH), (96, 80, 46))
    rnd = random.Random(8)
    for _ in range(70): x, y = rnd.randint(0, CW), rnd.randint(664, CH); R(d, (x, y, x + 3, y + 1), (70, 60, 34))

def vines(d, f):
    for k, x in enumerate((40, 170, 300, 470)):
        sway = int(math.sin(f * 0.08 + k) * 4)
        d.line([(x, 0), (x + sway, 180 + k * 30)], fill=(30, 90, 40), width=3)
        for y in range(30, 180 + k * 30, 36): d.ellipse((x + sway - 8, y, x + sway + 4, y + 8), fill=(50, 140, 60))

def parrots(d, f, n=2):
    for k in range(n):
        x = (80 + k * 230 + f * 2) % (CW + 40) - 20; y = 220 + k * 50 + int(math.sin(f * 0.15 + k) * 8); w = 6 if (f // 4 + k) % 2 else 1
        R(d, (x, y, x + 12, y + 5), RED); d.line([(x + 2, y), (x + 6, y - w), (x + 10, y)], fill=(40, 120, 200), width=3); R(d, (x + 12, y, x + 15, y + 3), YEL)

def peak_bg(d, sea_y=430):
    grad(d, (120, 180, 240), (230, 230, 220), 0, sea_y, 10)
    R(d, (0, sea_y, CW, 560), (40, 120, 190)); R(d, (0, 560, CW, 760), (60, 120, 54))
    for y in range(sea_y + 8, 560, 14): R(d, ((y * 37) % 400, y, (y * 37) % 400 + 60, y + 1), (150, 200, 240))
    mountains(d, (50, 110, 60), None, 640, [(60, 180, 160), (470, 160, 170)])
    d.polygon([(120, CH), (236, 522), (304, 522), (420, CH)], fill=(70, 130, 60)); d.polygon([(304, 522), (420, CH), (340, CH)], fill=(56, 110, 50))
    R(d, (236, 520, 304, 526), (90, 150, 70))
    R(d, (0, 760, CW, CH), (60, 120, 54))

def ring(d, x, y):
    d.ellipse((x, y, x + 50, y + 50), outline=GOLD, width=7); d.ellipse((x + 18, y - 10, x + 32, y + 4), fill=(170, 230, 250)); d.ellipse((x + 18, y - 10, x + 32, y + 4), outline=K)

def portrait(d, x, y):
    R(d, (x, y, x + 90, y + 110), GOLD); R(d, (x + 8, y + 8, x + 82, y + 102), (80, 40, 50))
    d.ellipse((x + 28, y + 26, x + 62, y + 66), fill=SKIN_E); d.chord((x + 22, y + 18, x + 68, y + 70), 180, 360, fill=(90, 60, 30))
    R(d, (x + 26, y + 30, x + 31, y + 72), (90, 60, 30)); R(d, (x + 59, y + 30, x + 64, y + 72), (90, 60, 30))
    R(d, (x + 37, y + 44, x + 39, y + 46), K); R(d, (x + 51, y + 44, x + 53, y + 46), K); R(d, (x + 41, y + 56, x + 49, y + 57), (170, 70, 70))
    d.polygon([(x + 20, y + 102), (x + 30, y + 74), (x + 60, y + 74), (x + 70, y + 102)], fill=(170, 40, 70))

def ship_piece(d, x, y, kind):
    if kind == 0: R(d, (x, y, x + 90, y + 10), (150, 100, 56)); d.rectangle((x, y, x + 90, y + 10), outline=K)
    elif kind == 1: d.arc((x, y - 30, x + 70, y + 30), 0, 180, fill=(150, 100, 56), width=8)
    else: R(d, (x + 30, y - 40, x + 36, y + 10), BROWN_D); R(d, (x + 10, y - 34, x + 56, y - 30), BROWN_D)

def coin(d, cx, cy, r, f):
    sq = abs(math.cos(f * 0.06)); rx = max(4, int(r * sq))
    d.ellipse((cx - rx, cy - r, cx + rx, cy + r), fill=GOLD); d.ellipse((cx - rx, cy - r, cx + rx, cy + r), outline=GOLD_D, width=4)
    if sq > 0.6:
        d.text((cx, cy - 14), "1", font=ImageFont.truetype(FONT, 28), fill=GOLD_D, anchor="mm"); d.text((cx, cy + 22), "BALBOA", font=F8, fill=GOLD_D, anchor="mm")

def cargo_ship(d, x, y):
    d.polygon([(x, y), (x + 300, y), (x + 280, y + 50), (x + 16, y + 50)], fill=(160, 40, 40)); R(d, (x, y, x + 300, y + 10), (40, 40, 50))
    cols = [(40, 110, 170), (200, 140, 40), (60, 140, 80), (180, 60, 50)]
    for k in range(9):
        for r in range(2): R(d, (x + 30 + k * 26, y - 22 - r * 22, x + 54 + k * 26, y - 2 - r * 22), cols[(k + r) % 4]); d.rectangle((x + 30 + k * 26, y - 22 - r * 22, x + 54 + k * 26, y - 2 - r * 22), outline=K)
    R(d, (x + 250, y - 70, x + 290, y), WHITE); R(d, (x + 256, y - 62, x + 284, y - 54), (60, 120, 180))

def crane(d, x, base):
    R(d, (x, base - 260, x + 14, base), (220, 120, 40)); R(d, (x + 40, base - 260, x + 54, base), (220, 120, 40))
    R(d, (x - 60, base - 270, x + 160, base - 256), (220, 120, 40)); d.line([(x + 140, base - 256), (x + 140, base - 180)], fill=K, width=2)
    R(d, (x + 128, base - 180, x + 152, base - 170), (120, 120, 130))

def scaffold(d, x, base):
    R(d, (x, base - 50, x + 200, base - 40), (90, 58, 30))
    for k in (0, 190): R(d, (x + k, base - 40, x + k + 10, base), (70, 44, 22))
    R(d, (x + 90, base - 72, x + 120, base - 50), (70, 44, 22))

# ---------------- maps ----------------
PAN_BOX = (-83, -75.5, 6.3, 10.5)
STA_MARIA = (-77.2, 8.6); ACLA = (-77.8, 8.89); SANMIG = (-78.2, 8.0)
def panama_map(f, title, route=None, dots=(), extra_labels=()):
    labels = [("CARIBBEAN SEA", -80.6, 9.7, WHITE, K), ("SOUTH SEA", -80.2, 6.9, K, YEL)] + list(extra_labels)
    return region_map(f, PAN_BOX, h=300, labels=labels, route=route, title=title, dots=dots)

def hisp_map(f, prog):
    return region_map(f, (-80, -66, 7, 21), h=330, labels=[("HISPANIOLA", -71.5, 17.0, K, YEL), ("DARIÉN", -77.3, 9.6, WHITE, K)],
                      route=([STODOM, (-71, 16), (-75, 11.5), (-76.8, 8.6)], prog), title="STOWAWAY, 1510", dots=[STODOM])

def skyline_panama(d, base):
    rnd = random.Random(21); x = 0
    while x < CW:
        w = rnd.randint(28, 50); h = rnd.randint(90, 240)
        col = rnd.choice([(150, 170, 190), (120, 140, 170), (180, 190, 200)])
        R(d, (x, base - h, x + w - 4, base), col)
        for y in range(base - h + 8, base - 6, 14):
            for xx in range(x + 4, x + w - 8, 8): R(d, (xx, y, xx + 3, y + 5), (230, 230, 200))
        x += w

# ---------------- backgrounds ----------------
def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0:
        if li == 0: day_sea(d, 600); town(d, 600, 0, 300); ship_deck(d, 0)
        else: peak_bg(d)
    elif i == 1:
        if li == 0: village(d); conuco(d, 300, 700, 3)
        else: day_sea(d, 600)
    elif i == 2:
        if li == 0: jungle(d)
        else: jungle(d); [hut(d, 300 + k * 80, 650, 60) for k in range(3)]; church(d, 60, 650)
    elif i == 3: jungle(d, dark=(li == 2))
    elif i == 4: peak_bg(d)
    elif i == 5: beach(d)
    elif i == 6:
        if li == 0: day_sea(d, 600); dock(d, 300)
        elif li == 1: court(d)
        else: peak_bg(d, 470)
    elif i == 7:
        if li == 0: jungle(d)
        else: grad(d, (50, 30, 60), (210, 110, 80), 0, 660, 12); R(d, (0, 660, CW, CH), (110, 90, 60))
    elif i == 8:
        if li == 0: grad(d, (80, 170, 240), (210, 230, 250), 0, 640, 10); skyline_panama(d, 640); R(d, (0, 640, CW, CH), (90, 90, 96))
        elif li == 1: day_sea(d, 560)
        else: sea(d, (250, 150, 90), (250, 210, 150), 600, (40, 110, 170), (240, 200, 160)); skyline_panama(d, 600); R(d, (0, 690, CW, CH), (150, 140, 120))
    return c

# ---------------- scenes ----------------
def march(c, f, x0, n, keys, base=FEET, dx=58, speed=0.6, flip=False):
    for k in range(n):
        x = x0 + k * dx + (f * speed) % dx
        put(c, f"{keys[k % len(keys)]}{st(f, k, 6)}", x, base - (k % 2) * 8, flip=flip)

def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        if li == 0:
            gulls(d, f, 3, 300); clouds(d, f, 140, seed=3)
            for k in range(3): barrel(d, 40 + k * 30, 640)
            crate(d, 410, 640, 36); crate(d, 380, 640, 30)
            big_barrel(c, d, 200, 690, f, peek=max(0, (prog - 0.5) * 2))
            put(c, "sailor", 380, FEET, flip=True); put(c, "set1", 20, FEET); put(c, "set2", 80, FEET)
            label(d, "CREDITORS", 76, 620, WHITE, RED_D); label(d, "SAILOR", 406, 620, WHITE, K)
            if (f // 15) % 2 and prog < 0.5: d.text((60, 560), "?", font=ImageFont.truetype(FONT, 24), fill=RED); d.text((120, 556), "?", font=ImageFont.truetype(FONT, 24), fill=RED)
            label(d, "HISPANIOLA, 1510", 270, 250, K, YEL, F16)
            if prog > 0.55: label(d, "A STOWAWAY", 256, 470, WHITE, K, F16)
        else:
            clouds(d, f, 150, seed=2); gulls(d, f, 3, 300)
            put(c, "bal0", 218, 524, sc=2); label(d, "BALBOA", 270, 330, GOLD)
            label(d, "THE PACIFIC", 100, 440, K, YEL, F16)
            label(d, "1513", 270, 250, WHITE, K, F16)
            march(c, f, 30, 3, ["esp"], base=FEET, dx=60, speed=0.3); march(c, f, 380, 2, ["tai"], base=FEET, dx=60, speed=0.3)
            label(d, "FIRST EUROPEAN", 150, 610, WHITE, RED_D)
    elif i == 1:
        if li == 0:
            clouds(d, f, 140, seed=1); gulls(d, f, 2, 300)
            put(c, "balf", 40, FEET, sc=2); label(d, "VASCO NÚÑEZ DE BALBOA", 200, 545, GOLD)
            put(c, "dog0", 150, FEET); put(c, "pig0", 420, FEET - 10, flip=True)
            for k in range(4):
                yy = 470 - ((f * 2 + k * 30) % 120); xx = 180 + k * 40
                if yy > 330: d.ellipse((xx, yy, xx + 18, yy + 18), fill=GOLD); d.ellipse((xx, yy, xx + 18, yy + 18), outline=K)
            label(d, "DEBTS", 250, 300, WHITE, RED_D, F16)
            label(d, "FAILED FARM", 400, 620, WHITE, K)
            label(d, "HISPANIOLA", 270, 250, K, YEL, F16)
        else:
            c.alpha_composite(hisp_map(f, min(1, prog * 1.3)), (25, 110))
            waves(d, f, 600, (200, 230, 250)); gulls(d, f, 2, 470)
            put(c, "ship", 300, 700 + bob(f, 3, 0.1))
            big_barrel(c, d, 60, 735, f, peek=1.0)
            label(d, "BALBOA", 70, 520, GOLD); label(d, "LEONCICO", 230, 560, GOLD)
            if prog > 0.45: label(d, "PUNISHABLE BY DEATH", 380, 470, WHITE, RED, F16)
    elif i == 2:
        if li == 0:
            vines(d, f); parrots(d, f, 2)
            c.alpha_composite(panama_map(f, "DARIÉN, 1510", dots=[STA_MARIA], extra_labels=[("SANTA MARÍA", -77.0, 9.4, K, YEL)]), (25, 110))
            for k in range(2): hut(d, 300 + k * 90, 660, 60)
            march(c, f, 20, 4, ["esp"], base=FEET, dx=60, speed=0.4)
            label(d, "SETTLERS", 130, 620, WHITE, K)
            label(d, "TODAY: PANAMA", 400, 450, WHITE, K, F16)
        else:
            vines(d, f); parrots(d, f, 1)
            put(c, "bal0", 200, FEET, sc=2); label(d, "BALBOA", 252, 545, GOLD)
            scroll(d, 330, 470)
            for k, key in enumerate(("set1", "set2", "set1")): put(c, key, 20 + k * 56, FEET - abs(bob(f, 6, 0.3, k)))
            put(c, "esp0", 400, FEET, flip=True); put(c, "esp1", 460, FEET, flip=True)
            label(d, "SANTA MARÍA LA ANTIGUA", 270, 300, WHITE, K)
            label(d, "INTERIM GOVERNOR", 270, 250, K, YEL, F16)
            if prog > 0.4: label(d, "BY ORDER OF THE KING, 1511", 270, 400, WHITE, RED_D)
    elif i == 3:
        if li == 0:
            vines(d, f)
            c.alpha_composite(panama_map(f, "SEPT 1, 1513", route=([ACLA, (-78.0, 8.5), SANMIG], min(1, prog * 1.2)), dots=[ACLA],
                                         extra_labels=[("ACLA", -77.2, 9.35, WHITE, K)]), (25, 110))
            put(c, "bal0", 20, FEET, sc=2); label(d, "BALBOA", 72, 545, GOLD)
            march(c, f, 140, 6, ["esp"], base=FEET, dx=62, speed=0.6)
            label(d, "ABOUT 190 SPANIARDS", 330, 620, WHITE, K)
        elif li == 1:
            vines(d, f); parrots(d, f, 2)
            march(c, f, -10, 5, ["port"], base=FEET, dx=64, speed=0.7)
            march(c, f, 330, 3, ["esp"], base=FEET - 40, dx=64, speed=0.7)
            put(c, f"dog{st(f, 0, 5)}", 300 + (f * 0.7) % 64, FEET)
            label(d, "NATIVE GUIDES AND PORTERS", 270, 620, WHITE, K)
            label(d, "HUNDREDS", 270, 250, K, YEL, F16)
            label(d, "JUNGLE AND MOUNTAINS", 270, 290, WHITE, K, F16)
        else:
            vines(d, f)
            put(c, "piz0", 60, FEET, sc=2); label(d, "FRANCISCO PIZARRO", 150, 545, GOLD)
            put(c, "bal0", 340, FEET, sc=2, flip=True); label(d, "BALBOA", 392, 545, GOLD)
            label(d, "THE FUTURE CONQUEROR", 270, 250, K, YEL, F16); label(d, "OF PERU", 270, 290, K, YEL, F16)
    elif i == 4:
        clouds(d, f, 150, seed=6); gulls(d, f, 2, 330)
        if li == 0:
            p = min(1, prog * 1.2); x = 120 + p * 98; y = FEET - p * 214
            put(c, f"bal{st(f, 0, 6)}", x, y, sc=2)
            label(d, "BALBOA", x + 52, y - 193, GOLD)
            march(c, f, 10, 2, ["esp"], base=FEET, dx=58, speed=0.2); march(c, f, 400, 2, ["tai"], base=FEET, dx=58, speed=0.2)
            label(d, "HIS MEN", 70, 620, WHITE, K)
            label(d, "SEPTEMBER 25, 1513", 270, 250, K, YEL, F16)
        else:
            put(c, "bal0", 218, 524, sc=2); label(d, "BALBOA", 270, 330, GOLD)
            if prog > 0.25: label(d, "PACIFIC OCEAN", 110, 440, K, YEL, F16)
            label(d, "FIRST SIGHT", 270, 250, WHITE, RED_D, F16)
            for k in range(3): put(c, ["esp0", "tai0", "esp1"][k], 20 + k * 60, FEET - k * 30)
            put(c, "tai1", 430, FEET, flip=True)
    elif i == 5:
        clouds(d, f, 150, seed=4); gulls(d, f, 3, 300)
        waves(d, f, 560, (200, 240, 240))
        if li == 0:
            x = 280 - (1 - min(1, prog * 1.5)) * 80
            put(c, "bal0", x, 700, sc=2); shallow(c, 650, 700, int(x) - 10, int(x) + 120)
            d.line([(x + 98, 560), (x + 112, 520)], fill=STEEL_L, width=3)
            label(d, "BALBOA", x + 52, 505, GOLD)
            for k in range(3): put(c, ["esp0", "tai0", "esp1"][k], 20 + k * 56, FEET + 10)
            label(d, "GULF OF SAN MIGUEL", 270, 250, K, YEL, F16); label(d, "SEPTEMBER 29, 1513", 270, 290, WHITE, K, F16)
        else:
            c.alpha_composite(panama_map(f, "THE SOUTH SEA", dots=[SANMIG], extra_labels=[("SAN MIGUEL", -77.0, 7.5, WHITE, K)]), (25, 110))
            put(c, "bal0", 250, 700, sc=2); shallow(c, 650, 700, 240, 370)
            R(d, (240, 470, 244, 640), BROWN_D); castile_banner(d, 186, 474)
            label(d, "BALBOA", 330, 450, GOLD)
            for k in range(3): put(c, ["esp0", "esp1", "tai1"][k], 20 + k * 56, FEET + 10)
            label(d, "FOR CASTILE", 440, 620, WHITE, RED_D)
    elif i == 6:
        if li == 0:
            clouds(d, f, 140, seed=7); gulls(d, f, 3, 300)
            for k in range(3): put(c, "ship" if k == 0 else tint(SP["ship"], 0.8), 300 + k * 60 - t * 3, 640 + k * 25 + bob(f, 3, 0.1, k))
            put(c, "pedr", 120, 690, sc=2); label(d, "PEDRARIAS DÁVILA", 170, 497, GOLD)
            put(c, "esp0", 30, 690); put(c, "esp1", 250, 690, flip=True)
            label(d, "NEW GOVERNOR, 1514", 270, 250, K, YEL, F16)
        elif li == 1:
            castile_banner(d, 40, 160); castile_banner(d, 450, 160)
            put(c, "pedr", 20, FEET, sc=2); label(d, "PEDRARIAS", 72, 545, GOLD)
            put(c, "bal0", 416, FEET, sc=2, flip=True); label(d, "BALBOA", 468, 545, GOLD)
            portrait(d, 225, 400); label(d, "MARÍA (IN SPAIN)", 270, 525, WHITE, K)
            if prog > 0.15: label(d, "RIVALS", 270, 250, WHITE, RED, F16)
            if prog > 0.5: ring(d, 245, 600); label(d, "BETROTHED", 270, 670, K, YEL)
        else:
            clouds(d, f, 150, seed=8)
            for k in range(4):
                x = 30 + k * 120 + (f * 0.5) % 40; y = FEET - k * 6
                put(c, f"tai{st(f, k, 6)}", x, y); ship_piece(d, x - 20, y - 86, k % 3)
            put(c, "bal0", 420, FEET - 60, sc=2, flip=True); label(d, "BALBOA", 472, 485, GOLD)
            label(d, "SHIPS IN PIECES", 270, 250, K, YEL, F16); label(d, "TO THE SOUTH SEA", 270, 290, WHITE, K, F16)
            label(d, "PORTERS", 150, 620, WHITE, K)
    elif i == 7:
        if li == 0:
            vines(d, f)
            put(c, "piz0", 20, FEET, sc=2); label(d, "PIZARRO", 72, 545, GOLD)
            put(c, "balc", 300, FEET, sc=2, flip=True); label(d, "BALBOA", 352, 545, GOLD)
            put(c, "esp0", 440, FEET, flip=True); put(c, "esp1", 200, FEET)
            label(d, "ARRESTED, 1519", 270, 250, WHITE, RED_D, F16)
            label(d, "ORDERS OF PEDRARIAS", 270, 290, K, YEL, F16)
        else:
            scaffold(d, 170, 660)
            put(c, "balc", 220, 610, sc=2); label(d, "BALBOA", 272, 420, GOLD)
            for k, key in enumerate(("esp0", "esp1")): put(c, key, 150 + k * 280, 650, flip=k == 1)
            for k in range(4): put(c, chains(SP["set1" if k % 2 else "set2"]), 20 + k * 30 if k < 2 else 410 + (k - 2) * 50, FEET, flip=k >= 2)
            label(d, "4 COMPANIONS", 270, 690, WHITE, K)
            for k in range(3): torch(d, 40 + k * 230, 600, f + k)
            label(d, "ACLA, 1519", 270, 250, K, YEL, F16)
            if prog > 0.3: label(d, "TREASON", 270, 290, WHITE, RED_D, F16)
            if prog > 0.6: label(d, "BEHEADED", 270, 330, WHITE, RED, F16)
    elif i == 8:
        if li == 0:
            clouds(d, f, 140, seed=9)
            coin(d, 270, 420, 90, f)
            for k, key in enumerate(("pr1", "pr2", "pr3")): put(c, key, 60 + k * 170, FEET, flip=k == 2)
            label(d, "PANAMA", 270, 250, K, YEL, F16); label(d, "CURRENCY: THE BALBOA", 270, 560, WHITE, K, F16)
        elif li == 1:
            clouds(d, f, 140, seed=3); gulls(d, f, 3, 300)
            crane(d, 40, 640); crane(d, 300, 640)
            R(d, (0, 640, CW, 660), (120, 120, 130)); R(d, (0, 660, CW, CH), (90, 90, 96))
            cargo_ship(d, 100 + bob(f, 2, 0.05), 560)
            label(d, "PORT OF BALBOA", 270, 250, K, YEL, F16); label(d, "PANAMA CANAL, PACIFIC SIDE", 270, 290, WHITE, K, F16)
            put(c, "pr1", 40, FEET); put(c, "pr3", 440, FEET, flip=True)
        else:
            gulls(d, f, 3, 260, (80, 50, 50)); waves(d, f, 600, (240, 200, 160))
            R(d, (380, 560, 500, 690), (196, 190, 178)); R(d, (372, 550, 508, 562), (210, 204, 192))
            put(c, tint(SP["bal0"], 0.75, (40, 30, 0)), 362, 550, sc=3)
            label(d, "BALBOA MONUMENT", 410, 232, GOLD); label(d, "PANAMA CITY", 410, 262, WHITE, K)
            put(c, "pr1", 30, FEET); put(c, "pr2", 90, FEET, flip=True); put(c, "pr3", 150, FEET)
            quote_box(d, ["FROM A BARREL", "TO THE PACIFIC"], 160)
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
