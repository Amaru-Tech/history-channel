import os, sys
D = os.environ.get("HC_DIR", os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else ".")
_src = open(f"{D}/build4.py").read().split("# ---------------- render ----------------")[0]
sys_argv_backup = list(sys.argv); sys.argv = [sys.argv[0]]
exec(_src)  # engine, sprites, maps, overlay, compose, music, tts from episode 1
sys.argv = sys_argv_backup
CHECK = "check" in sys.argv
OUT = f"{D}/out5"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep02_first_fort_EN.mp4"

SCENES = [
 ("CHRISTMAS EVE, 1492", [
  ("On Christmas Eve, fourteen ninety-two, the Santa Maria sailed along the coast of a Caribbean island.", "Christmas Eve, 1492. The Santa María sails along a Caribbean island."),
  ("Columbus went to sleep. By morning, his flagship was gone.", "Columbus went to sleep. By morning, his flagship was gone.")]),
 ("THE BOY AT THE HELM", [
  ("The helmsman broke the rules. He handed the tiller to a ship's boy, and went to sleep too.", "The helmsman broke the rules. He handed the tiller to a ship's boy, and went to sleep too."),
  ("The current pushed the ship onto a reef. The hull cracked open.", "The current pushed the ship onto a reef. The hull cracked open.")]),
 ("A HELPING HAND", [
  ("A Tyeeno chief named Gwakanagaree sent his people in canoes to help.", "A Taíno chief, Guacanagarí, sent his people in canoes to help."),
  ("They worked all night to unload the cargo. Columbus wrote that nothing went missing.", "They worked all night to unload the cargo. Columbus wrote that nothing went missing.")]),
 ("LA NAVIDAD", [
  ("Columbus saw it as a sign. He used the wreck's timbers to build a fort, and named it La Navidad. Christmas.", "Columbus saw it as a sign. He built a fort from the wreck and named it La Navidad: Christmas."),
  ("It was the first European settlement in the Americas since the Vikings, five hundred years earlier.", "It was the first European settlement in the Americas since the Vikings, 500 years earlier.")]),
 ("39 MEN STAY", [
  ("He had one small ship left, the Neenya. There was no room for everyone. So thirty-nine men stayed behind.", "Only the small Niña was left. No room for everyone. So 39 men stayed behind."),
  ("Columbus sailed home to announce his discovery.", "Columbus sailed home to announce his discovery.")]),
 ("NOVEMBER 1493", [
  ("Eleven months later, he returned with seventeen ships. He fired a cannon to greet the fort. No answer.", "11 months later he returned with 17 ships. He fired a cannon to greet the fort. No answer."),
  ("La Navidad had been burned to the ground. All thirty-nine men were dead.", "La Navidad was burned to the ground. All 39 men were dead.")]),
 ("WHO DID IT?", [
  ("Gwakanagaree blamed a rival chief, Kaonabo.", "Guacanagarí blamed a rival chief, Caonabo."),
  ("But the Tyeeno said the Spaniards had brought it on themselves. They stole gold, and took women from the villages.", "But the Taíno said the Spaniards brought it on themselves: they stole gold and took women from the villages.")]),
 ("STILL MISSING", [
  ("The Santa Maria has never been found. A wreck announced in twenty fourteen turned out to be a later ship.", "The Santa María has never been found. A wreck announced in 2014 was a later ship."),
  ("The first European town in the Americas did not last a single year.", "The first European town in the Americas did not last a single year.")]),
]

_label_orig = label
def label(d, text, cx, y, fg=WHITE, bg=K, font=F16):
    w = d.textlength(text, font=font); cx = min(max(cx, w / 2 + 8), CW - w / 2 - 8)
    _label_orig(d, text, cx, y, fg, bg, font)

# ---------------- extra sprites ----------------
def chief(paint=False):
    im = Image.new("RGBA", (52, 84)); d = ImageDraw.Draw(im)
    for x0, x1 in [(20, 23), (29, 32)]: R(d, (x0, 64, x1, 81), SKIN_T)
    R(d, (17, 36, 35, 62), SKIN_T); R(d, (31, 36, 35, 62), SKIN_TD)
    R(d, (17, 58, 35, 67), WHITE); R(d, (21, 67, 31, 74), WHITE)
    R(d, (12, 37, 16, 56), SKIN_T); R(d, (36, 37, 40, 56), SKIN_TD)
    if paint:
        for y in (40, 46, 52): R(d, (18, y, 34, y + 1), K)
    else:
        d.ellipse((21, 40, 31, 50), fill=GOLD); d.ellipse((24, 43, 28, 47), fill=GOLD_D); R(d, (25, 36, 26, 40), GOLD_D)
    face(d, SKIN_T, SKIN_TD); R(d, (17, 13, 35, 21), HAIR); R(d, (16, 21, 19, 40), HAIR); R(d, (33, 21, 36, 40), HAIR)
    if paint:
        R(d, (19, 24, 33, 26), (190, 30, 30)); R(d, (20, 28, 32, 29), K)
        for k, x in enumerate(range(17, 36, 3)): R(d, (x, 4, x + 1, 13), [(190, 30, 30), K, WHITE][k % 3])
    else:
        R(d, (17, 12, 35, 17), GOLD); R(d, (17, 14, 35, 15), GOLD_D)
        for k, x in enumerate(range(18, 35, 4)): R(d, (x, 2, x + 2, 12), [WHITE, (40, 140, 90), (200, 50, 30)][k % 3])
    return outline(im)

def sleeper():
    im = Image.new("RGBA", (60, 30)); d = ImageDraw.Draw(im)
    R(d, (6, 12, 50, 24), (230, 226, 210)); R(d, (46, 10, 58, 22), SKIN_E); R(d, (46, 8, 58, 12), RED); R(d, (2, 14, 8, 22), (110, 80, 50))
    return outline(im)

SP.update({"guaca": chief(False), "caonabo": chief(True), "sleeper": sleeper()})

# ---------------- caribbean map ----------------
HISP2 = [(-73.45, 19.9), (-72.8, 19.95), (-71.7, 19.85), (-70.7, 19.8), (-69.9, 19.65), (-69.2, 19.25), (-68.35, 18.6), (-68.7, 18.2),
         (-69.9, 18.45), (-71.0, 18.3), (-71.4, 17.65), (-72.0, 18.15), (-73.4, 18.2), (-74.45, 18.4), (-74.1, 18.65), (-72.8, 18.65),
         (-72.75, 19.1), (-73.4, 19.7)]
CUBA2 = [(-84.95, 21.85), (-84.4, 22.3), (-82.0, 23.15), (-80.3, 23.1), (-78.0, 22.3), (-75.6, 21.1), (-74.15, 20.25), (-74.9, 20.0),
         (-77.7, 19.85), (-77.2, 20.65), (-78.5, 21.5), (-80.5, 21.8), (-81.8, 22.2), (-83.4, 21.9)]
PR = [(-67.25, 18.5), (-65.6, 18.4), (-65.6, 18.0), (-67.2, 17.95)]
JAM = [(-78.35, 18.45), (-76.8, 18.4), (-76.2, 18.0), (-77.2, 17.8), (-78.3, 18.2)]
FLA = [(-83, 28.5), (-82.7, 27.5), (-81.1, 25.1), (-80.4, 25.2), (-80.0, 27.0), (-80.5, 28.5)]
BAH = [(-77.9, 24.6, 0.6), (-77.6, 26.6, 0.5), (-75.8, 23.6, 0.35), (-74.5, 24.1, 0.3), (-73.6, 21.1, 0.4), (-76.2, 25.0, 0.3)]
NAVIDAD = (-72.1, 19.75)

def carib_map(f, w=490, h=300, labels=(), dot=True, route=None, title=None):
    m = Image.new("RGBA", (w, h)); d = ImageDraw.Draw(m); d.fontmode = "1"
    P = lambda lon, lat: (6 + (lon + 86) / 22 * (w - 12), 6 + (28.5 - lat) / 13 * (h - 12))
    R(d, (0, 0, w - 1, h - 1), (58, 98, 150))
    for poly in (HISP2, CUBA2, PR, JAM, FLA): d.polygon([P(*p) for p in poly], fill=(118, 150, 84), outline=(52, 74, 38))
    for lon, lat, r in BAH:
        x, y = P(lon, lat); rr = r * (w - 12) / 22; d.ellipse((x - rr, y - rr / 2, x + rr, y + rr / 2), fill=(118, 150, 84))
    if route:
        pts, prog = route; seg = [P(*p) for p in pts]; n = int(len(seg[:-1]) * 40 * prog)
        for k in range(len(seg) - 1):
            for s in range(40):
                if k * 40 + s > n: break
                a, b = seg[k], seg[k + 1]; tt = s / 40; x, y = a[0] + (b[0] - a[0]) * tt, a[1] + (b[1] - a[1]) * tt
                if s % 3 == 0: R(d, (x - 1, y - 1, x + 1, y + 1), WHITE)
    if dot:
        x, y = P(*NAVIDAD); on = (f // 10) % 2 == 0
        R(d, (x - 4, y - 4, x + 4, y + 4), RED if on else WHITE); d.rectangle((x - 4, y - 4, x + 4, y + 4), outline=K)
    for text, lon, lat, fg, bg in labels:
        x, y = P(lon, lat); tw = d.textlength(text, font=F16); x = min(max(x, tw / 2 + 8), w - tw / 2 - 8)
        R(d, (x - tw / 2 - 4, y - 10, x + tw / 2 + 3, y + 9), bg); d.text((x - tw / 2, y - 8), text, font=F16, fill=fg)
    if title:
        tw = d.textlength(title, font=F16); R(d, (w / 2 - tw / 2 - 5, 8, w / 2 + tw / 2 + 4, 30), K); d.text((w / 2 - tw / 2, 11), title, font=F16, fill=GOLD)
    d.rectangle((0, 0, w - 1, h - 1), outline=(240, 220, 170), width=3)
    return outline(m)

# ---------------- props ----------------
def fort(d, x0, base, prog=1.0, burned=False, f=0):
    logs = list(range(x0, x0 + 230, 10)); n = int(len(logs) * prog)
    for k, x in enumerate(logs[:n]):
        h = 70 + (k % 3) * 4
        if burned: h = 18 + (k * 37) % 40
        col = (40, 30, 26) if burned else ((150, 100, 56) if k % 2 else (126, 82, 44))
        R(d, (x, base - h, x + 8, base), col)
        if not burned: d.polygon([(x, base - h), (x + 4, base - h - 8), (x + 8, base - h)], fill=col)
    if prog >= 1 and not burned:
        tx = x0 + 90; R(d, (tx, base - 130, tx + 50, base - 60), (120, 74, 38)); d.polygon([(tx - 6, base - 130), (tx + 25, base - 156), (tx + 56, base - 130)], fill=(176, 138, 70))
        R(d, (tx + 22, base - 186, tx + 24, base - 150), BROWN_D); R(d, (tx + 24, base - 186, tx + 46, base - 172), WHITE); R(d, (tx + 32, base - 186, tx + 36, base - 172), RED); R(d, (tx + 24, base - 181, tx + 46, base - 177), RED)
    if burned:
        for k in range(6):
            pr = random.Random(k); sx = x0 + pr.randint(10, 220); ph = ((f * 0.6 + pr.randint(0, 100)) % 100) / 100
            r = int(6 + ph * 18); y = base - 30 - ph * 160
            d.ellipse((sx - r, y - r, sx + r, y + r), fill=(90, 90, 96) if ph < 0.6 else (70, 70, 76))

def canoe(c, d, x, y, f, k=0):
    d.polygon([(x, y), (x + 120, y), (x + 108, y + 14), (x + 12, y + 14)], fill=(120, 74, 38)); R(d, (x + 4, y, x + 116, y + 2), (150, 100, 56))
    for j in range(3):
        put(c, "tai2", x + 10 + j * 34, y + 4, crop=46)
        a = math.sin(f * 0.25 + j + k) * 8; d.line([(x + 40 + j * 34, y - 12), (x + 34 + j * 34 + a, y + 22)], fill=BROWN_D, width=2)

def reef(d, base):
    rnd = random.Random(11)
    for _ in range(14):
        x = rnd.randint(60, 480); w = rnd.randint(14, 34); h = rnd.randint(6, 16)
        d.polygon([(x, base), (x + w * 0.3, base - h), (x + w * 0.7, base - h + 4), (x + w, base)], fill=(100, 92, 84))

# ---------------- backgrounds ----------------
def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    night = i in (0, 1, 5) or (i == 2 and li == 1)
    if i in (0, 1, 2, 5):
        if night: sea(d, (10, 14, 40), (60, 70, 120), 600, (20, 30, 70), (80, 100, 160))
        else: sea(d, (240, 150, 90), (250, 210, 150), 600, (40, 90, 150), (240, 200, 160))
        if night:
            rnd = random.Random(4)
            for _ in range(60): x, y = rnd.randint(0, CW), rnd.randint(0, 500); R(d, (x, y, x, y), WHITE)
            d.ellipse((420, 120, 466, 166), fill=(236, 236, 214))
        d.polygon([(0, 600), (30, 570), (90, 556), (150, 566), (200, 590), (240, 600)], fill=(16, 30, 26) if night else (60, 110, 70))
        if i == 5: d.polygon([(0, 600), (30, 570), (90, 556), (150, 566), (200, 590), (240, 600)], fill=(16, 30, 26))
    elif i in (3, 4, 6):
        sea(d, (80, 170, 240), (200, 230, 250), 560, (40, 170, 190), (200, 240, 240))
        R(d, (0, 640, CW, CH), (236, 214, 150))
        rnd = random.Random(8)
        for _ in range(90): x, y = rnd.randint(0, CW), rnd.randint(644, CH); R(d, (x, y, x + 1, y), (210, 186, 124))
        palm(d, 500, 650, 200, -1)
    elif i == 7:
        grad(d, (10, 40, 70), (20, 90, 120), 0, CH, 12)
        rnd = random.Random(3)
        for _ in range(40): x, y = rnd.randint(0, CW), rnd.randint(0, 700); R(d, (x, y, x + 2, y + 2), (120, 190, 210))
        R(d, (0, 700, CW, CH), (194, 176, 128))
        for x in range(0, CW, 40): d.polygon([(x, 700), (x + 20, 690), (x + 40, 700)], fill=(194, 176, 128))
    return c

def tilt(key, deg):
    im = SP[key]; return im.rotate(deg, resample=Image.NEAREST, expand=True)

# ---------------- scenes ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        waves(d, f, 600, (80, 100, 160))
        if li == 0 or prog < 0.35:
            x = 120 + t * 6; put(c, "ship", x, 690 + bob(f, 3, 0.1)); label(d, "SANTA MARÍA", x + 80, 520, GOLD)
            if li == 1: bubble(d, "Z z z", x + 30, 500)
        else:
            reef(d, 700); put(c, tilt("ship", -14), 150, 720); bubble(d, "CRACK!", 300, 470)
    elif i == 1:
        waves(d, f, 600, (80, 100, 160))
        if li == 1 and prog > 0.4: reef(d, 760)
        ang = 0 if li == 0 else -10 * min(1, max(0, (prog - 0.4) * 3))
        ship = tilt("ship", ang).resize((tilt("ship", ang).width * 2, tilt("ship", ang).height * 2), Image.NEAREST)
        c.alpha_composite(ship, (110, int(770 - ship.height + bob(f, 3, 0.08))))
        if li == 0:
            put(c, "sailor", 128, 560, crop=60); label(d, "SHIP'S BOY", 110, 440, GOLD)
            c.alpha_composite(SP["sleeper"], (190, 520))
            if prog > 0.5: label(d, "HELMSMAN", 330, 500, WHITE, RED_D); bubble(d, "Z z z", 330, 440)
        else:
            label(d, "REEF!", 270, 300, WHITE, RED, F16)
            if prog > 0.6: bubble(d, "CRACK!", 380, 360)
    elif i == 2:
        waves(d, f, 600, (240, 200, 160) if li == 0 else (80, 100, 160))
        reef(d, 700); put(c, tilt("ship", -14), 250, 700, k=0.8)
        for k in range(2):
            x = -130 + (t * 40 + k * 160) % 420; canoe(c, d, x, 640 + k * 50, f, k)
        put(c, "guaca", 10, 600, sc=2); label(d, "GUACANAGARÍ", 62, 400, GOLD)
        if li == 1 and prog > 0.4: label(d, "NOTHING WENT MISSING", 330, 260, K, YEL, F16)
    elif i == 3:
        waves(d, f, 560, (200, 240, 240))
        fort(d, 150, 720, prog if li == 0 else 1.0, f=f)
        put(c, "col", 30, FEET + 8, sc=2) if li == 0 else None
        if li == 0: label(d, "COLUMBUS", 82, 540, GOLD); label(d, "FORT LA NAVIDAD", 330, 470, GOLD) if prog > 0.6 else None
        else:
            c.alpha_composite(carib_map(f, labels=[("LA NAVIDAD", -72.1, 21.2, K, YEL), ("CUBA", -79.5, 23.6, WHITE, K)], title="HISPANIOLA, 1492"), (25, 110))
            label(d, "FIRST SINCE THE VIKINGS", 270, 450, WHITE, RED_D, F16)
    elif i == 4:
        waves(d, f, 560, (200, 240, 240))
        fort(d, 40, 720, 1.0, f=f)
        for k in range(5): put(c, f"esp{st(f, k, 9)}", 40 + k * 40, FEET + 6)
        label(d, "39 MEN", 150, 560, K, YEL, F16)
        x = 330 + (prog * 260 if li == 1 else 0); put(c, "ship", x, 640 + bob(f, 3, 0.1), k=0.9); label(d, "NIÑA", x + 80, 470, GOLD)
        if li == 1: label(d, "BACK TO SPAIN", 300, 250, WHITE, K, F16)
    elif i == 5:
        waves(d, f, 600, (80, 100, 160))
        if li == 0:
            for k in range(5):
                x = 200 + k * 64 - prog * 40; put(c, "ship", x, 640 + k * 10 + bob(f, 3, 0.1, k), k=0.55 + 0.1 * (k % 2))
            label(d, "17 SHIPS", 330, 380, GOLD, K, F16)
            if prog > 0.5:
                ph = ((lt - ldur * 0.5) * 1.5) % 1
                if ph < 0.15: R(d, (180, 560, 210, 580), (255, 250, 210))
                if prog > 0.75: bubble(d, "...", 120, 470)
        else:
            fort(d, 150, 740, 1.0, burned=True, f=f)
            label(d, "NO SURVIVORS", 270, 330, WHITE, RED, F16)
    elif i == 6:
        put(c, "guaca", 30, FEET, sc=2); label(d, "GUACANAGARÍ", 82, 536, GOLD)
        if li == 0:
            put(c, "caonabo", 386, FEET, sc=2, flip=True); label(d, "CAONABO?", 438, 536, WHITE, RED_D)
            bubble(d, "IT WAS HIM!", 200, 470)
        else:
            put(c, "esp0", 300, FEET); put(c, "esp1", 380, FEET, flip=True)
            for k, (x, y) in enumerate(((330, 690), (420, 700))): d.ellipse((x, y, x + 26, y + 26), fill=(150, 110, 60)); R(d, (x + 9, y - 4, x + 17, y + 2), (150, 110, 60)); R(d, (x + 8, y + 10, x + 18, y + 16), GOLD)
            label(d, "STOLEN GOLD", 380, 300, K, YEL, F16); label(d, "RAIDED VILLAGES", 380, 340, WHITE, RED_D, F16)
    elif i == 7:
        if li == 0:
            for k in range(8): R(d, (60 + k * 50, 690 - (k % 3) * 6, 90 + k * 50, 700), (110, 80, 50) if k % 2 else (90, 64, 40))
            d.text((270, 560), "?", font=ImageFont.truetype(FONT, 64), fill=YEL, anchor="mm")
            label(d, "SANTA MARÍA: NEVER FOUND", 270, 240, WHITE, K, F16)
            if prog > 0.45: label(d, "2014 WRECK: A LATER SHIP", 270, 290, K, YEL, F16)
        else:
            c.alpha_composite(carib_map(f, labels=[("LA NAVIDAD", -72.1, 21.2, K, YEL)], title="DEC 1492 - NOV 1493"), (25, 110))
            label(d, "LASTED LESS THAN A YEAR", 270, 470, WHITE, RED_D, F16)
            if prog > 0.4: label(d, "FOLLOW FOR MORE HISTORY", 270, 620, WHITE, RED, F16)

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
