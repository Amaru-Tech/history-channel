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
OUT = f"{D}/out_ep04"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep04_great_swap_EN.mp4"

SCENES = [
 ("BEFORE 1492", [
  ("Before fourteen ninety-two, Italy had no tomatoes. Ireland had no potatoes.", "Before 1492, Italy had no tomatoes. Ireland had no potatoes."),
  ("And the Americas had no horses.", "And the Americas had no horses.")]),
 ("THE GREAT SWAP", [
  ("In nineteen seventy-two, historian Alfred Crosby gave it a name: the Columbian Exchange.", "In 1972, historian Alfred Crosby gave it a name: the Columbian Exchange."),
  ("Plants, animals and germs crossed the Atlantic, in both directions.", "Plants, animals and germs crossed the Atlantic, in both directions.")]),
 ("GOING EAST", [
  ("From the Americas came maize, potatoes, beans, tomatoes, peanuts, tobacco and cacao, the bean behind chocolate.", "From the Americas: maize, potatoes, beans, tomatoes, peanuts, tobacco and cacao."),
  ("By around fifteen hundred, the Portuguese had carried the chili pepper to India.", "By around 1500, the Portuguese had carried the chili pepper to India.")]),
 ("GOING WEST", [
  ("The Spanish brought wheat, olives and grapevines.", "The Spanish brought wheat, olives and grapevines."),
  ("Columbus's second voyage carried horses, cattle, pigs and chickens.", "Columbus's second voyage carried horses, cattle, pigs and chickens."),
  ("Later, sugar, coffee, bananas and oranges became giant crops in the Americas.", "Later, sugar, coffee, bananas and oranges became giant crops in the Americas.")]),
 ("THE HUMBLE POTATO", [
  ("Of all the new crops, the potato may have changed Europe the most.", "Of all the new crops, the potato may have changed Europe the most."),
  ("It helped end centuries-old cycles of hunger and famine.", "It helped end centuries-old cycles of hunger and famine.")]),
 ("THE HORSE", [
  ("The horse spread quickly across the Americas.", "The horse spread quickly across the Americas."),
  ("Native peoples adopted it, for travel and for war.", "Native peoples adopted it, for travel and for war.")]),
 ("INVISIBLE CARGO", [
  ("But the deadliest cargo was invisible: smallpox, measles, influenza and typhus.", "The deadliest cargo was invisible: smallpox, measles, influenza and typhus."),
  ("Historians estimate that by sixteen fifty, about ninety percent of the native population had died.", "Historians estimate that by 1650, about 90% of the native population had died.")]),
 ("ONE WORLD", [
  ("The exchange reshaped what the whole planet eats.", "The exchange reshaped what the whole planet eats."),
  ("Pizza with tomato, Irish potatoes, Indian curry with chili. All of them began with fourteen ninety-two.", "Pizza with tomato. Irish potatoes. Indian curry with chili. All began with 1492.")]),
]

_label_orig = label
def label(d, text, cx, y, fg=WHITE, bg=K, font=F16):
    w = d.textlength(text, font=font); cx = min(max(cx, w / 2 + 8), CW - w / 2 - 8)
    _label_orig(d, text, cx, y, fg, bg, font)

# ---------------- extra sprites: crops and animals ----------------
def icon(draw, size=(28, 28)):
    im = Image.new("RGBA", size); d = ImageDraw.Draw(im); draw(d); return outline(im)

LEAF = (70, 150, 60); LEAF_D = (40, 100, 40)
CROPS = {
 "tomato": lambda d: (d.ellipse((3, 6, 25, 26), fill=(214, 40, 30)), d.ellipse((6, 9, 12, 14), fill=(250, 120, 100)), d.polygon([(9, 5), (14, 9), (19, 5), (14, 3)], fill=LEAF)),
 "potato": lambda d: (d.ellipse((2, 7, 26, 23), fill=(176, 130, 76)), [R(d, (x, y, x + 1, y + 1), (110, 76, 40)) for x, y in ((8, 12), (16, 15), (20, 11), (12, 18))]),
 "maize": lambda d: (d.ellipse((9, 2, 19, 26), fill=(240, 200, 50)), [R(d, (10, y, 18, y), (200, 150, 30)) for y in range(5, 24, 4)], d.polygon([(8, 26), (4, 10), (12, 22)], fill=LEAF), d.polygon([(20, 26), (24, 10), (16, 22)], fill=LEAF_D)),
 "cacao": lambda d: (d.ellipse((5, 3, 23, 26), fill=(190, 110, 40)), [R(d, (x, 6, x, 23), (140, 70, 20)) for x in (10, 14, 18)]),
 "chili": lambda d: (d.polygon([(6, 6), (12, 4), (22, 18), (24, 26), (16, 20)], fill=(220, 40, 30)), R(d, (5, 2, 9, 6), LEAF)),
 "tobacco": lambda d: (d.ellipse((5, 2, 23, 26), fill=(90, 150, 60)), R(d, (13, 3, 14, 26), LEAF_D)),
 "bean": lambda d: [d.ellipse((4 + k * 7, 8 + (k % 2) * 4, 12 + k * 7, 20 + (k % 2) * 4), fill=(140, 50, 40)) for k in range(3)],
 "peanut": lambda d: (d.ellipse((4, 4, 16, 16), fill=(210, 170, 110)), d.ellipse((12, 12, 24, 24), fill=(210, 170, 110))),
 "wheat": lambda d: (R(d, (13, 6, 14, 27), (200, 170, 60)), [d.ellipse((x, y, x + 5, y + 7), fill=(230, 196, 80)) for x, y in ((8, 2), (15, 2), (8, 9), (15, 9), (11, 0))]),
 "olive": lambda d: (d.ellipse((4, 8, 16, 22), fill=(90, 110, 40)), d.ellipse((13, 6, 25, 20), fill=(60, 80, 30)), R(d, (12, 2, 13, 8), BROWN)),
 "grape": lambda d: ([d.ellipse((x, y, x + 7, y + 7), fill=(110, 50, 130)) for x, y in ((6, 6), (13, 6), (20, 6), (9, 12), (16, 12), (12, 18))], R(d, (13, 1, 14, 6), BROWN)),
 "coffee": lambda d: [(d.ellipse((x, y, x + 9, y + 12), fill=(110, 60, 30)), R(d, (x + 4, y + 2, x + 4, y + 10), (60, 30, 10))) for x, y in ((4, 4), (15, 12))],
 "banana": lambda d: d.arc((0, -10, 28, 24), 30, 150, fill=(240, 210, 60), width=7),
 "orange": lambda d: (d.ellipse((3, 5, 25, 27), fill=(240, 140, 30)), d.ellipse((8, 9, 13, 14), fill=(255, 190, 110)), R(d, (13, 1, 16, 5), LEAF)),
 "germ": lambda d: (d.ellipse((5, 5, 23, 23), fill=(110, 170, 70)), [R(d, (x, y, x + 2, y + 2), (110, 170, 70)) for x, y in ((1, 13), (25, 13), (13, 1), (13, 25), (4, 4), (22, 22), (22, 4), (4, 22))], R(d, (10, 10, 12, 12), (60, 110, 40)), R(d, (16, 15, 18, 17), (60, 110, 40))),
}
for k, fn in CROPS.items(): SP["c_" + k] = icon(fn)

def cow():
    im = Image.new("RGBA", (70, 50)); d = ImageDraw.Draw(im)
    for x in (12, 20, 46, 54): R(d, (x, 32, x + 4, 46), WHITE); R(d, (x, 44, x + 4, 47), K)
    R(d, (8, 12, 58, 34), WHITE); R(d, (18, 14, 30, 24), K); R(d, (40, 22, 50, 32), K)
    R(d, (54, 6, 68, 22), WHITE); R(d, (60, 16, 68, 22), (232, 170, 160)); R(d, (58, 9, 59, 10), K); R(d, (54, 2, 56, 6), (220, 210, 180)); R(d, (66, 2, 68, 6), (220, 210, 180))
    d.line([(8, 14), (3, 26)], fill=WHITE, width=2)
    return outline(im)

def chicken():
    im = Image.new("RGBA", (30, 30)); d = ImageDraw.Draw(im)
    d.ellipse((4, 10, 22, 24), fill=WHITE); d.ellipse((15, 4, 25, 14), fill=WHITE); R(d, (18, 1, 21, 4), RED); R(d, (25, 8, 28, 9), GOLD); R(d, (20, 7, 21, 8), K)
    R(d, (11, 24, 12, 28), GOLD); R(d, (16, 24, 17, 28), GOLD)
    return outline(im)

def native_rider():
    h = horse(); tr = taino(0).crop((0, 0, 52, 58))
    im = Image.new("RGBA", (100, 110)); im.alpha_composite(tr, (24, 4)); im.alpha_composite(h, (0, 38))
    d = ImageDraw.Draw(im); R(d, (44, 60, 49, 76), SKIN_T); R(d, (66, 30, 68, 70), BROWN_D); R(d, (64, 26, 70, 30), STEEL)
    return outline(im)

def farmer(shirt=(170, 60, 50)):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    for x0, x1 in [(20, 23), (29, 32)]: R(d, (x0, 62, x1, 78), (90, 70, 50)); R(d, (x0 - 1, 77, x1 + 1, 81), K)
    R(d, (16, 36, 36, 63), shirt); R(d, (16, 54, 36, 64), (80, 64, 50)); R(d, (11, 37, 16, 52), shirt); R(d, (36, 37, 41, 52), shirt)
    face(d); R(d, (14, 10, 38, 14), (120, 90, 50)); R(d, (19, 4, 33, 10), (120, 90, 50))
    return outline(im)

SP.update({"cow": cow(), "chicken": chicken(), "nrider": native_rider(), "farmerIE": farmer((60, 120, 70)), "farmerIT": farmer((170, 60, 50))})

ITALY = (12.5, 42.5); IRELAND = (-8, 53); AMER_PT = (-75, 10); EUR_PT = (-5, 40)

def crop_row(c, keys, y, n_show, sc=2, x0=None):
    w = 28 * sc + 10; total = len(keys) * w; x = x0 if x0 is not None else (CW - total) // 2 + 5
    for k, key in enumerate(keys[:n_show]): put(c, "c_" + key, x + k * w, y, sc=sc)

# ---------------- backgrounds ----------------
def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i in (1, 6) and not (i == 6 and li == 1):
        grad(d, (24, 44, 70), (60, 90, 120), 0, CH, 12)
    elif i in (0, 4, 7):
        grad(d, (110, 180, 240), (210, 230, 250), 0, 600, 10)
        R(d, (0, 600, CW, CH), (110, 150, 80))
        for k in range(0, CW, 36):
            for y in range(612, 760, 26): R(d, (k + (y // 26 % 2) * 18, y, k + (y // 26 % 2) * 18 + 10, y + 3), (90, 128, 64))
        d.polygon([(0, 600), (90, 540), (200, 570), (320, 530), (440, 560), (CW, 540), (CW, 600)], fill=(90, 130, 70))
    elif i in (2, 3):
        grad(d, (40, 30, 26), (90, 64, 44), 0, CH, 12)
        R(d, (0, GY, CW, CH), (110, 72, 40))
        for x in range(0, CW, 30): R(d, (x, GY, x + 1, CH), (80, 50, 26))
    elif i == 5:
        grad(d, (240, 150, 90), (250, 210, 150), 0, 600, 10)
        d.polygon([(0, 600), (100, 500), (200, 560), (300, 470), (420, 540), (CW, 490), (CW, 600)], fill=(170, 110, 80))
        R(d, (0, 600, CW, CH), (206, 170, 100))
        rnd = random.Random(3)
        for _ in range(80): x, y = rnd.randint(0, CW), rnd.randint(604, CH); R(d, (x, y, x + 3, y), (180, 146, 80))
    elif i == 6:
        grad(d, (30, 30, 40), (70, 60, 70), 0, CH, 12)
        R(d, (0, 600, CW, CH), (110, 120, 90))
    return c

# ---------------- scenes ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        if li == 0:
            put(c, "farmerIT", 40, FEET, sc=2); label(d, "ITALY", 92, 548, GOLD)
            put(c, "farmerIE", 400, FEET, sc=2, flip=True); label(d, "IRELAND", 452, 548, GOLD)
            for x, key in ((150, "c_tomato"), (330, "c_potato")):
                put(c, key, x, 420, sc=3); d.line([(x, 340), (x + 84, 424)], fill=RED, width=6); d.line([(x + 84, 340), (x, 424)], fill=RED, width=6)
            label(d, "NO TOMATOES", 150, 300, WHITE, RED_D, F16); label(d, "NO POTATOES", 390, 300, WHITE, RED_D, F16)
        else:
            put(c, "tai0", 60, FEET, sc=2); label(d, "TAINO", 112, 548, GOLD)
            put(c, "horse", 280, 520, sc=2, alpha=0.35); d.line([(280, 380), (480, 520)], fill=RED, width=8); d.line([(480, 380), (280, 520)], fill=RED, width=8)
            label(d, "NO HORSES", 380, 300, WHITE, RED_D, F16)
    elif i == 1:
        if li == 0:
            c.alpha_composite(world_map(f, labels=[("AMERICAS", -70, -12, K, YEL), ("EUROPE", 5, 52, K, YEL), ("AFRICA", 15, 5, K, YEL)], title="THE COLUMBIAN EXCHANGE"), (25, 140))
            R(d, (190, 590, 350, 745), (150, 40, 40)); R(d, (196, 596, 344, 739), (176, 56, 50)); R(d, (346, 594, 356, 745), (240, 230, 210))
            d.text((270, 630), "THE", font=F16, fill=GOLD, anchor="mm"); d.text((270, 656), "COLUMBIAN", font=F16, fill=GOLD, anchor="mm"); d.text((270, 682), "EXCHANGE", font=F16, fill=GOLD, anchor="mm"); d.text((270, 714), "1972", font=F16, fill=WHITE, anchor="mm")
            label(d, "HISTORIAN ALFRED CROSBY", 270, 562, K, YEL, F16)
        else:
            m = world_map(f, route=([AMER_PT, (-40, 30), EUR_PT], min(1, prog * 2)), title="BOTH DIRECTIONS")
            c.alpha_composite(m, (25, 140))
            if prog > 0.5:
                m2 = world_map(f, route=([EUR_PT, (-40, 20), AMER_PT], min(1, (prog - 0.5) * 2)), title="BOTH DIRECTIONS"); c.alpha_composite(m2, (25, 140))
            label(d, "PLANTS", 100, 600, K, YEL, F16); label(d, "ANIMALS", 270, 600, K, YEL, F16); label(d, "GERMS", 440, 600, WHITE, RED_D, F16)
            for k, key in enumerate(("c_maize", "cow", "c_germ")): put(c, key, 70 + k * 170, 720, sc=2)
    elif i == 2:
        if li == 0:
            label(d, "AMERICAS -> OLD WORLD", 270, 140, K, YEL, F16)
            keys = ["maize", "potato", "bean", "tomato", "peanut", "tobacco", "cacao"]
            n = 1 + int(prog * 7)
            crop_row(c, keys[:4], 360, n); crop_row(c, keys[4:], 480, max(0, n - 4))
            for k, nm in enumerate(("MAIZE", "POTATO", "BEANS", "TOMATO")): label(d, nm, 82 + k * 132 - 4, 380, WHITE, K) if k < n else None
            for k, nm in enumerate(("PEANUTS", "TOBACCO", "CACAO")): label(d, nm, 148 + k * 66 * 2 - 4, 500, WHITE, K) if k + 4 < n else None
        else:
            put(c, "ship", 40 + prog * 160, 700 + bob(f, 3, 0.1)); put(c, "c_chili", 380, 560, sc=4)
            label(d, "PORTUGUESE", 120 + prog * 160, 520, GOLD); label(d, "CHILI -> INDIA, c.1500", 270, 250, K, YEL, F16)
    elif i == 3:
        label(d, "OLD WORLD -> AMERICAS", 270, 140, K, YEL, F16)
        if li == 0:
            crop_row(c, ["wheat", "olive", "grape"], 450, 3, sc=3)
            for k, nm in enumerate(("WHEAT", "OLIVES", "GRAPES")): label(d, nm, 102 + k * 140, 470, WHITE, K)
        elif li == 1:
            put(c, "horse", 10, FEET, sc=2); put(c, "cow", 210, FEET, sc=2); put(c, f"pig{st(f, 0, 5)}", 370, FEET, sc=2); put(c, "chicken", 470, FEET, sc=2)
            label(d, "HORSES", 100, 540, WHITE, K); label(d, "CATTLE", 280, 580, WHITE, K); label(d, "PIGS", 410, 620, WHITE, K); label(d, "CHICKENS", 470, 660, WHITE, K)
        else:
            put(c, "cane", 50, 560, sc=2); crop_row(c, ["coffee", "banana", "orange"], 520, 3, sc=3, x0=170)
            for k, nm in enumerate(("SUGAR", "COFFEE", "BANANAS", "ORANGES")): label(d, nm, 90 + k * 125, 560 + (k % 2) * 40, WHITE, K)
    elif i == 4:
        put(c, "farmerIE", 60, FEET, sc=2); label(d, "FARMER", 112, 548, GOLD)
        for k in range(6): put(c, "c_potato", 250 + (k % 3) * 70, 680 - (k // 3) * 50, sc=2)
        if li == 0: label(d, "THE POTATO", 330, 300, K, YEL, F16)
        else: label(d, "LESS HUNGER", 330, 300, K, YEL, F16); label(d, "FEWER FAMINES", 330, 340, WHITE, K, F16)
    elif i == 5:
        if li == 0:
            for k in range(3): x = (-120 + t * 50 + k * 190) % 680 - 100; put(c, "nrider", x, 700 + k * 12)
            label(d, "THE HORSE SPREADS", 270, 300, K, YEL, F16)
        else:
            put(c, "nrider", 170, FEET, sc=2); label(d, "TRAVEL + WAR", 270, 300, K, YEL, F16)
    elif i == 6:
        if li == 0:
            put(c, "ship", 30, 640); 
            for k in range(10):
                pr = random.Random(k); x = pr.randint(200, 500) + int(math.sin(f * 0.1 + k) * 12); y = pr.randint(380, 640) + int(math.cos(f * 0.08 + k) * 10)
                put(c, "c_germ", x, y, sc=2)
            for k, nm in enumerate(("SMALLPOX", "MEASLES", "INFLUENZA", "TYPHUS")): label(d, nm, 120 + (k % 2) * 300, 250 + (k // 2) * 44, WHITE, RED_D, F16)
        else:
            for k in range(10):
                x = 8 + (k % 5) * 106; fe = FEET - 100 if k < 5 else FEET
                put(c, SP["tai0"].copy(), x, fe, alpha=1.0 if k == 0 or prog < 0.3 else 0.3)
            label(d, "~90% BY 1650", 270, 330, WHITE, RED, F16); label(d, "(ESTIMATE)", 270, 370, WHITE, K, F16)
    elif i == 7:
        if li == 0:
            c.alpha_composite(world_map(f, labels=[("AMERICAS", -70, -12, K, YEL), ("EUROPE", 5, 52, K, YEL), ("AFRICA", 15, 5, K, YEL)], title="ONE WORLD, ONE TABLE"), (25, 140))
            crop_row(c, ["tomato", "potato", "maize", "wheat", "coffee"], 690, 5, sc=2)
        else:
            R(d, (60, 560, 480, 600), (150, 100, 56)); R(d, (60, 600, 480, 610), (110, 72, 40))
            d.ellipse((90, 500, 210, 560), fill=(230, 190, 110)); d.ellipse((100, 506, 200, 552), fill=(214, 40, 30))
            for x, y in ((120, 520), (160, 530), (140, 540)): d.ellipse((x, y, x + 12, y + 8), fill=(250, 230, 180))
            for k in range(4): put(c, "c_potato", 230 + k * 28, 560 - (k % 2) * 14)
            d.ellipse((370, 516, 460, 560), fill=(230, 140, 40)); put(c, "c_chili", 400, 530)
            label(d, "PIZZA", 150, 630, WHITE, K); label(d, "POTATOES", 280, 650, WHITE, K); label(d, "CURRY", 415, 630, WHITE, K)
            if prog > 0.4: label(d, "ALL FROM 1492", 270, 300, K, YEL, F16)
            if prog > 0.55: label(d, "FOLLOW FOR MORE HISTORY", 270, 380, WHITE, RED, F16)

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
