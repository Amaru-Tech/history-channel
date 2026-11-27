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
OUT = f"{D}/out_ep10"; os.makedirs(OUT, exist_ok=True)
FINAL = f"{D}/ep10_18_men_around_the_world_EN.mp4"

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
_src12 = open(f"{D}/build_ep09.py").read().split("# ---------------- extra sprites ----------------")[-1].split("# ---------------- maps ----------------")[0]
exec(_src12)  # episode 9: Ponce, chroniclers, old man, archers, fountain, stamp, flowers, sign, current arrows, flying arrows, well, oak, old book

SCENES = [
 ("AROUND THE WORLD", [
  ("In September fifteen twenty-two, a battered ship limped into Spain with just eighteen men on board.", "In September 1522, a battered ship limped into Spain with just 18 men on board."),
  ("They had just sailed all the way around the world.", "They had just sailed all the way around the world.")]),
 ("THE PLAN", [
  ("Three years earlier, Portuguese navigator Ferdinand Magellan made a deal with Spain's King Charles the First.", "Three years earlier, Portuguese navigator Ferdinand Magellan made a deal with Spain's King Charles I."),
  ("He promised a western route to the Spice Islands.", "He promised a western route to the Spice Islands."),
  ("In September fifteen nineteen, five ships and about two hundred and seventy men left Spain.", "In September 1519, five ships and about 270 men left Spain.")]),
 ("MUTINY", [
  ("In Patagonia, in April fifteen twenty, Spanish captains rose against their Portuguese commander.", "In Patagonia, in April 1520, Spanish captains rose against their Portuguese commander."),
  ("Magellan crushed the mutiny. Later, one ship was wrecked in a storm, and another deserted and sailed home.", "Magellan crushed the mutiny. Later, one ship was wrecked in a storm, and another deserted and sailed home.")]),
 ("THE STRAIT", [
  ("On October twenty-first, fifteen twenty, he found a passage near the tip of South America.", "On October 21, 1520, he found a passage near the tip of South America."),
  ("It took thirty-eight days to cross. He called the calm ocean beyond the Pacific: the peaceful sea.", "It took 38 days to cross. He called the calm ocean beyond the Pacific: the peaceful sea.")]),
 ("THE HUNGRY OCEAN", [
  ("The Pacific was far bigger than anyone imagined. The crossing took over three months.", "The Pacific was far bigger than anyone imagined. The crossing took over three months."),
  ("The men ate sawdust, ox hides and wormy biscuits. Scurvy swelled their gums, and nineteen men died.", "The men ate sawdust, ox hides and wormy biscuits. Scurvy swelled their gums, and 19 men died.")]),
 ("MACTAN", [
  ("In April fifteen twenty-one, in what is now the Philippines, Magellan attacked the island of {Mactan}.", "In April 1521, in what is now the Philippines, Magellan attacked the island of Mactan."),
  ("On the shore, he was killed by the warriors of the chief {Lapulapu}.", "On the shore, he was killed by the warriors of the chief Lapulapu.")]),
 ("ELCANO TAKES OVER", [
  ("The Basque navigator {Juan Sebastián Elcano} led the survivors on.", "The Basque navigator Juan Sebastián Elcano led the survivors on."),
  ("In November fifteen twenty-one, they reached the Spice Islands.", "In November 1521, they reached the Spice Islands."),
  ("Loaded with cloves, the Victoria sailed home alone, across the Indian Ocean and around Africa.", "Loaded with cloves, the Victoria sailed home alone, across the Indian Ocean and around Africa.")]),
 ("THE LOST DAY", [
  ("In July fifteen twenty-two, they stopped at the Cape Verde islands. Their log said it was Wednesday.", "In July 1522, they stopped at the Cape Verde islands. Their log said it was Wednesday."),
  ("On shore, it was Thursday. Sailing west with the sun, they had lost a full day.", "On shore, it was Thursday. Sailing west with the sun, they had lost a full day.")]),
 ("THE FIRST LAP", [
  ("Their cargo of cloves was worth more than all five ships that had set out.", "Their cargo of cloves was worth more than all five ships that had set out."),
  ("Magellan began the first voyage around the world. {Elcano} finished it.", "Magellan began the first voyage around the world. Elcano finished it.")]),
]

# ---------------- narration: piper ryan-high (channel voice) with raw IPA for Spanish and Filipino names ----------------
import re as _re
IPA = {"Mactan": "mɑktˈɑn", "Lapulapu": "lˌɑpulˈɑpu", "Juan Sebastián Elcano": "hwˈɑn sɛbɑstjˈɑn ɛlkˈɑnoʊ", "Elcano": "ɛlkˈɑnoʊ"}
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
NAVY_C = (40, 60, 130); NAVY_CD = (26, 38, 86); OCHRE_C = (176, 120, 40); OCHRE_CD = (120, 80, 26)
def magellan_sprite(step=0):  # conquistador leader recolored: navy cape, black beard
    return recolor(SP[f"piz{step}"], {RED: NAVY_C, RED_D: NAVY_CD, tint_c(RED, 0.8): NAVY_CD, (150, 140, 132): (34, 28, 26), (150, 40, 40): (30, 30, 50)})
def elcano_sprite(step=0):  # ochre cape, brown beard
    return recolor(SP[f"piz{step}"], {RED: OCHRE_C, RED_D: OCHRE_CD, tint_c(RED, 0.8): OCHRE_CD, (150, 140, 132): (110, 70, 40), (150, 40, 40): (70, 50, 30)})
def charles_sprite():  # young King Charles I: Ferdinand recolored to a dark purple robe
    return recolor(SP["ferd"], {RED: (90, 40, 120), RED_D: (60, 26, 84), tint_c(RED, 0.8): (60, 26, 84)})
def lapulapu(step=0):  # Visayan warrior chief: red headcloth, tattoos, round shield, kampilan sword
    im = SP[f"tai{step}"].copy(); d = ImageDraw.Draw(im)
    R(d, (16, 8, 36, 14), (190, 30, 30)); R(d, (34, 10, 40, 16), (190, 30, 30))
    for y in range(40, 56, 5): d.line([(18, y), (34, y + 2)], fill=(40, 50, 90))
    d.ellipse((2, 40, 22, 62), fill=(150, 100, 50), outline=K); R(d, (11, 50, 13, 52), GOLD)
    d.line([(40, 54), (48, 20)], fill=STEEL_L, width=3); R(d, (38, 54, 44, 58), BROWN_D)
    return outline(im)
def visayan(step=0):  # warrior with spear and shield
    im = SP[f"tai{step}"].copy(); d = ImageDraw.Draw(im)
    R(d, (16, 8, 36, 12), (60, 60, 140))
    d.line([(42, 76), (46, 4)], fill=BROWN_D, width=2); d.polygon([(44, 0), (49, 0), (46, 8)], fill=STEEL)
    d.ellipse((4, 42, 22, 62), fill=(140, 90, 40), outline=K)
    return outline(im)
def portuguese_local():
    return recolor(SP["set1"], {}) if "set1" in SP else SP["sailor"]
def rat():
    im = Image.new("RGBA", (26, 14)); d = ImageDraw.Draw(im)
    d.ellipse((4, 3, 20, 13), fill=(110, 100, 96)); d.ellipse((17, 4, 25, 11), fill=(110, 100, 96)); R(d, (23, 6, 24, 7), K)
    d.ellipse((17, 2, 21, 6), fill=(200, 150, 150)); d.line([(4, 9), (0, 5)], fill=(200, 150, 150))
    return outline(im)
SP.update({"mag0": magellan_sprite(0), "mag1": magellan_sprite(1), "elc0": elcano_sprite(0), "elc1": elcano_sprite(1),
           "charles": charles_sprite(), "lapu0": lapulapu(0), "lapu1": lapulapu(1), "vis0": visayan(0), "vis1": visayan(1),
           "piga": chronicler((60, 80, 60), (40, 56, 40), (90, 60, 40), beard=False), "rat": rat()})

# ---------------- props ----------------
def clove(d, x, y, s=1):
    R(d, (x, y, x + 2 * s, y + 9 * s), (110, 60, 30)); d.ellipse((x - 2 * s, y - 4 * s, x + 4 * s, y + 2 * s), fill=(140, 70, 40)); R(d, (x - 2 * s, y - 2 * s, x + 4 * s, y - 2 * s), (80, 40, 20))
def clove_sack(d, x, base, f=0, k=0):
    R(d, (x, base - 40, x + 44, base), (200, 176, 120)); d.ellipse((x - 2, base - 50, x + 46, base - 30), fill=(200, 176, 120))
    d.rectangle((x, base - 40, x + 44, base), outline=K); R(d, (x + 16, base - 54, x + 28, base - 46), (150, 120, 80))
    for j in range(4): clove(d, x + 6 + j * 10, base - 46 + (j % 2) * 2)
def clove_tree(d, x, base, h=180):
    R(d, (x - 6, base - h, x + 6, base), BROWN_D)
    for k in range(5): d.ellipse((x - 54 + k * 18, base - h - 50 + (k % 2) * 24, x - 4 + k * 18, base - h + 30), fill=(40, 120, 60))
    for k in range(9): R(d, (x - 40 + k * 10, base - h - 10 + (k % 3) * 14, x - 37 + k * 10, base - h - 6 + (k % 3) * 14), (220, 90, 70))
def sun(d, cx, cy, r=26):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(250, 220, 90), outline=(240, 170, 50), width=3)
def log_book(d, x, y, word, col=K):
    R(d, (x, y, x + 210, y + 120), (110, 60, 30)); R(d, (x + 8, y + 6, x + 202, y + 114), (240, 230, 200)); R(d, (x + 103, y + 6, x + 107, y + 114), (160, 140, 110))
    for k in range(4): R(d, (x + 16, y + 20 + k * 18, x + 92, y + 22 + k * 18), (150, 130, 100))
    d.text((x + 156, y + 40), "JULY 1522", font=F8, fill=K, anchor="mm"); d.text((x + 156, y + 72), word, font=F8, fill=col, anchor="mm")
def sawdust(d, x, base):
    d.polygon([(x, base), (x + 30, base - 22), (x + 60, base)], fill=(220, 190, 130))
    for k in range(10): R(d, (x + 6 + k * 5, base - 6 - (k % 3) * 4, x + 7 + k * 5, base - 5 - (k % 3) * 4), (170, 140, 90))
def hide(d, x, y):
    d.polygon([(x, y + 10), (x + 14, y), (x + 50, y + 2), (x + 64, y + 14), (x + 52, y + 34), (x + 10, y + 32)], fill=(150, 100, 60), outline=K)
def biscuit(d, x, y, f):
    d.ellipse((x, y, x + 40, y + 26), fill=(214, 180, 120), outline=K)
    for k in range(3): wx = x + 8 + ((f // 4 + k * 5) % 24); R(d, (wx, y + 8 + k * 5, wx + 4, y + 9 + k * 5), WHITE)
def sword_clash(d, cx, cy, f):
    if (f // 4) % 2: 
        for a in range(0, 360, 45): d.line([(cx, cy), (cx + 14 * math.cos(math.radians(a)), cy + 14 * math.sin(math.radians(a)))], fill=YEL, width=2)
def patagonia(d):
    sea(d, (110, 130, 150), (200, 210, 220), 560, (40, 70, 100), (150, 170, 190))
    d.polygon([(0, 560), (120, 500), (260, 540), (400, 490), (CW, 530), (CW, 560)], fill=(130, 120, 100))
    d.polygon([(0, 690), (CW, 650), (CW, CH), (0, CH)], fill=(170, 160, 120))
    rnd = random.Random(3)
    for _ in range(40): x, y = rnd.randint(0, CW), rnd.randint(680, CH); R(d, (x, y, x + 6, y + 2), (110, 120, 70))
def cape_verde(d):
    sea(d, (80, 170, 240), (200, 230, 250), 560, (40, 150, 190), (200, 240, 240))
    d.polygon([(260, 560), (330, 470), (380, 430), (440, 470), (CW, 500), (CW, 560)], fill=(140, 110, 80))
    d.polygon([(330, 470), (380, 430), (410, 450)], fill=(110, 140, 80))
    d.polygon([(0, 690), (CW, 650), (CW, CH), (0, CH)], fill=(200, 180, 130))
def fort_pt(d, x, base):  # small Portuguese fort with flag
    R(d, (x, base - 70, x + 110, base), (220, 210, 190)); 
    for k in range(5): R(d, (x + k * 24, base - 82, x + k * 24 + 12, base - 70), (220, 210, 190))
    R(d, (x + 40, base - 40, x + 66, base), (80, 60, 50)); d.rectangle((x, base - 70, x + 110, base), outline=K)
    R(d, (x + 96, base - 130, x + 99, base - 82), BROWN_D); R(d, (x + 99, base - 130, x + 130, base - 112), (250, 250, 250)); R(d, (x + 110, base - 126, x + 118, base - 116), (40, 60, 160))

# ---------------- maps ----------------
G_AMER = [(-168, 66), (-160, 71), (-140, 70), (-120, 72), (-95, 72), (-80, 68), (-65, 60), (-56, 52), (-66, 45), (-70, 42), (-76, 35), (-81, 31),
          (-80, 25.5), (-83, 29), (-90, 30), (-97, 27), (-97, 21), (-94, 18.2), (-90.5, 21), (-87, 21), (-88, 16), (-83, 15), (-83, 10), (-77, 8.5),
          (-75, 11), (-62, 10.5), (-52, 5), (-35, -5), (-39, -15), (-48, -26), (-58, -35), (-62, -39), (-65, -42), (-67.7, -49.3), (-68.4, -52.3),
          (-71, -52.8), (-73, -50), (-75, -45), (-73, -37), (-71, -28), (-70, -18), (-76, -14), (-81, -5), (-80, 1), (-78, 7), (-80, 8.5), (-86, 12),
          (-92, 15), (-105, 20), (-110, 24), (-117, 32), (-124, 40), (-125, 48), (-135, 58), (-150, 60), (-165, 60)]
G_TDF = [(-68.6, -53.3), (-65.2, -54.7), (-68, -55.4), (-71.5, -55), (-74.4, -52.9), (-71.6, -53.6)]
G_EUAS = [(-10, 36.5), (-6.35, 36.8), (-9, 39), (-9, 43), (-2, 43.5), (-1.5, 46.5), (-4.5, 48.5), (2, 51), (8, 54), (10, 58), (5, 62), (15, 69), (30, 71),
          (60, 70), (80, 73), (110, 75), (140, 72), (170, 70), (180, 68), (180, 62), (160, 60), (155, 52), (140, 48), (135, 43), (129, 35), (122, 31),
          (120, 25), (110, 21), (108, 16), (109, 11), (105, 9), (103, 1.5), (100, 6), (98, 16), (94, 17), (90, 22), (80, 15), (77, 8), (73, 18), (67, 24),
          (57, 25), (52, 24), (50, 30), (48, 29.5), (51, 24), (56, 22), (58, 20), (52, 16), (44, 12.5), (39, 21), (33, 29), (35, 36), (28, 37),
          (26, 40), (23, 37), (20, 40), (13, 45), (18, 40), (16, 38), (10, 44), (3, 43), (-1, 37)]
G_AFR = [(-17, 21), (-17, 14), (-12, 8), (-8, 4.5), (0, 5), (9, 4), (9, -1), (12, -6), (13, -12), (12, -17), (15, -27), (18, -34.5), (20, -35),
         (27, -34), (33, -28), (35, -24), (40, -15), (40, -10), (39, -5), (42, 0), (51, 11.5), (43, 11.5), (39, 17), (35, 24), (33, 29), (32, 31),
         (20, 32), (10, 37), (-1, 35.5), (-6, 35.8), (-10, 30), (-13, 27)]
G_ISL = [
    [(114, -22), (122, -17), (130, -12), (137, -12), (142, -11), (145, -15), (153, -25), (150, -37), (141, -38), (135, -35), (130, -32), (115, -34)],  # Australia
    [(109, 2), (117, 7), (119, 5), (118, 1), (116, -4), (110, -3)], [(95, 5.5), (98, 4), (106, -6), (102, -4)], [(105, -6), (114, -7), (114, -8.5), (105, -7)],
    [(131, -1), (141, -2.5), (150, -6), (147, -10), (141, -9), (135, -4)], [(119, 1), (125, 1.5), (121, -1), (123, -5), (120, -5.5)],  # New Guinea, Sulawesi
    [(120.6, 18.5), (122.2, 18.5), (122.0, 16.5), (121.6, 15.0), (122.0, 14.0), (124.0, 13.0), (124.1, 12.6), (123.0, 13.0), (121.7, 13.9), (120.6, 14.2), (120.9, 15.5), (119.8, 16.2), (120.4, 17.0)],  # Luzon
    [(120.3, 13.5), (121.5, 13.2), (121.2, 12.2), (120.4, 12.6)], [(124.3, 12.5), (125.7, 12.4), (125.7, 11.0), (124.9, 11.3)],  # Mindoro, Samar
    [(124.3, 11.5), (125.0, 11.3), (125.2, 10.1), (124.7, 10.0), (124.3, 10.8)], [(123.9, 11.3), (124.1, 11.0), (123.9, 10.2), (123.3, 9.4), (123.4, 10.1)],  # Leyte, Cebu
    [(123.8, 10.1), (124.5, 10.1), (124.6, 9.6), (123.9, 9.6)], [(122.9, 10.9), (123.5, 10.8), (123.3, 9.3), (122.5, 9.9)],  # Bohol, Negros
    [(121.9, 11.9), (122.8, 11.6), (123.1, 11.1), (122.4, 10.5), (121.9, 10.6)], [(119.3, 11.4), (119.8, 10.6), (118.3, 9.0), (117.2, 8.4), (117.4, 8.8), (119.0, 10.6)],  # Panay, Palawan
    [(122.0, 7.0), (123.5, 8.6), (124.5, 8.9), (125.5, 9.8), (126.6, 8.0), (126.2, 6.3), (125.4, 5.6), (124.0, 6.3), (122.1, 6.8)],  # Mindanao
    [(127.4, 1.8), (128.6, 1.4), (127.9, 0.2), (127.2, 0.4)],  # Halmahera / Moluccas
    [(130, 31), (135, 34), (140, 36), (141, 41), (140, 42), (136, 36), (131, 34)], [(44, -25), (47, -25), (50, -15), (49, -12), (44, -17)],  # Japan, Madagascar
    [(-5.5, 50), (1.5, 51), (0.5, 53), (-2, 56), (-2, 58.6), (-5, 58.6), (-6, 56), (-3, 54.5), (-4.5, 52)], [(-24, 64), (-14, 65), (-15, 66.5), (-22, 66.4)],
    [(-55, 60), (-42, 60), (-22, 70), (-20, 76), (-60, 76), (-70, 75)], [(-85, 22), (-80, 23.2), (-74.2, 20.2), (-77, 19.9), (-80, 21.5), (-85, 21.6)],
    [(-74.5, 19.8), (-69, 19.7), (-68.4, 18.5), (-72, 18), (-74.5, 18.4)]]
SANLUCAR = (-6.35, 36.8); SANJULIAN = (-67.7, -49.3); STRAIT_E = (-68.4, -52.6); STRAIT_W = (-74.4, -52.6); GUAM = (144.8, 13.4)
MACTAN = (124.05, 10.3); TIDORE = (127.4, 0.7); CAPEVERDE = (-23.5, 15.0); CEBU = (123.9, 10.4)
# full route, westward, longitudes unwrapped (Pacific crossing continues below -180)
VOY = [SANLUCAR, (-16, 28), (-25, 10), (-33, -5), (-40, -22), (-50, -32), (-60, -42), SANJULIAN, STRAIT_E, (-71, -53.3), STRAIT_W,
       (-82, -40), (-100, -22), (-140, -5), (-180, 8), (GUAM[0] - 360, GUAM[1]), (128 - 360, 10.5), (MACTAN[0] - 360, MACTAN[1]),
       (122 - 360, 8.5), (124.5 - 360, 5), (TIDORE[0] - 360, TIDORE[1]), (126 - 360, -4), (124 - 360, -8.6), (120 - 360, -12), (100 - 360, -18),
       (60 - 360, -32), (30 - 360, -38), (18 - 360, -36), (10 - 360, -25), (2 - 360, -5), (-15 - 360, 8), (CAPEVERDE[0] - 360, CAPEVERDE[1]),
       (-22 - 360, 30), (SANLUCAR[0] - 360, SANLUCAR[1])]
def _cum(pts):
    L = [0.0]
    for a, b in zip(pts, pts[1:]): L.append(L[-1] + math.dist(a, b))
    return L
_VL = _cum(VOY)
def voy_prog(pt):  # fraction of the route length at a given waypoint
    return _VL[VOY.index(pt)] / _VL[-1]

def poly_map(f, box, w=490, h=300, labels=(), route=None, title=None, dots=(), grid=30, wrap=False, ships=()):
    lon0, lon1, lat0, lat1 = box
    m = Image.new("RGBA", (w, h)); d = ImageDraw.Draw(m); d.fontmode = "1"
    P = lambda lon, lat: (6 + (lon - lon0) / (lon1 - lon0) * (w - 12), 6 + (lat1 - lat) / (lat1 - lat0) * (h - 12))
    R(d, (0, 0, w - 1, h - 1), (58, 98, 150))
    for lon in range(-180, 181, grid):
        x = P(lon, 0)[0]
        if 0 < x < w: d.line([(x, 0), (x, h)], fill=(52, 88, 136))
    for lat in range(-60, 81, grid):
        y = P(0, lat)[1]
        if 0 < y < h: d.line([(0, y), (w, y)], fill=(52, 88, 136))
    for poly in [G_AMER, G_TDF, G_EUAS, G_AFR] + G_ISL: d.polygon([P(*p) for p in poly], fill=(118, 150, 84), outline=(52, 74, 38))
    if route:
        pts, prog = route; seg = [P(*p) for p in pts]
        draw_route(d, seg, prog, head=False)
        if wrap: draw_route(d, [(x + (w - 12), y) for x, y in seg], prog, head=False)
        # ship head at the current point
        want = _cum(pts)[-1] * prog; L = _cum(pts); k = max(0, min(len(pts) - 2, next((j for j in range(len(L) - 1) if L[j + 1] >= want), len(pts) - 2)))
        a, b = pts[k], pts[k + 1]; tt = 0 if L[k + 1] == L[k] else (want - L[k]) / (L[k + 1] - L[k]); lon, lat = a[0] + (b[0] - a[0]) * tt, a[1] + (b[1] - a[1]) * tt
        if wrap and lon < -180: lon += 360
        if prog < 1:
            x, y = P(lon, lat); d.polygon([(x - 6, y + 3), (x + 6, y + 3), (x + 4, y + 7), (x - 4, y + 7)], fill=BROWN); d.polygon([(x, y - 8), (x, y + 2), (x + 6, y + 1)], fill=WHITE)
    for lon, lat in dots:
        x, y = P(lon, lat); on = (f // 10) % 2 == 0
        R(d, (x - 4, y - 4, x + 4, y + 4), RED if on else WHITE); d.rectangle((x - 4, y - 4, x + 4, y + 4), outline=K)
    for text, lon, lat, fg, bg in labels:
        x, y = P(lon, lat); tw = d.textlength(text, font=F16); x = min(max(x, tw / 2 + 8), w - tw / 2 - 8)
        R(d, (x - tw / 2 - 4, y - 10, x + tw / 2 + 3, y + 9), bg); d.text((x - tw / 2, y - 8), text, font=F16, fill=fg)
    if title:
        tw = d.textlength(title, font=F16); R(d, (w / 2 - tw / 2 - 5, 8, w / 2 + tw / 2 + 4, 30), K); d.text((w / 2 - tw / 2, 11), title, font=F16, fill=GOLD)
    cx, cy = w - 30, h - 34; d.polygon([(cx, cy - 16), (cx + 4, cy), (cx, cy + 16), (cx - 4, cy)], fill=WHITE); d.polygon([(cx - 16, cy), (cx, cy - 4), (cx + 16, cy), (cx, cy + 4)], fill=(200, 200, 190))
    R(d, (cx - 3, cy - 26, cx + 3, cy - 20), K); d.text((cx, cy - 23), "N", font=F8, fill=WHITE, anchor="mm")
    d.rectangle((0, 0, w - 1, h - 1), outline=(240, 220, 170), width=3)
    return outline(m)
GLOBE = (-180, 180, -60, 75)
def globe(f, title, p0, p1, prog, labels=(), dots=(), h=300):
    return poly_map(f, GLOBE, h=h, labels=labels, title=title, dots=dots, route=(VOY, p0 + (p1 - p0) * prog), wrap=True)

# ---------------- backgrounds ----------------
def make_bg(i, li):
    c = Image.new("RGBA", (CW, CH)); d = ImageDraw.Draw(c)
    if i == 0:
        if li == 0: day_sea(d, 600); town(d, 600, 300, CW); dock(d, 540, 700)
        else: night_sea(d, 600)
    elif i == 1:
        if li < 2: court(d)
        else: day_sea(d, 600); town(d, 600, 0, 200)
    elif i == 2: patagonia(d)
    elif i == 3:
        if li == 0: sea(d, (110, 130, 150), (200, 210, 220), 600, (40, 70, 100), (150, 170, 190))
        else: day_sea(d, 560)
    elif i == 4:
        if li == 0: day_sea(d, 600)
        else: day_sea(d, 590); ship_deck(d, 0)
    elif i == 5:
        if li == 0: beach(d)
        else: beach(d, "sunset")
    elif i == 6:
        if li < 2: beach(d)
        else: night_sea(d, 600)
    elif i == 7: cape_verde(d)
    elif i == 8:
        if li == 0: day_sea(d, 600); town(d, 600, 260, CW); dock(d, 540, 700)
        else: beach(d, "sunset")
    return c

def march(c, f, x0, n, keys, base=FEET, dx=58, speed=0.6, flip=False):
    for k in range(n):
        x = x0 + k * dx + (f * speed) % dx
        put(c, f"{keys[k % len(keys)]}{st(f, k, 6)}", x, base - (k % 2) * 8, flip=flip)

# ---------------- scenes ----------------
def draw_scene(i, c, d, f, t, li, lt, ldur, sdur):
    d.fontmode = "1"; prog = min(1.0, lt / max(0.1, ldur))
    if i == 0:
        if li == 0:
            clouds(d, f, 150, seed=2); gulls(d, f, 3, 300)
            vic = tint(SP["wreck"], 0.85); put(c, vic, 40 + min(1, prog * 1.4) * 60, 660 + bob(f, 3, 0.1))
            label(d, "VICTORIA", 150, 470, GOLD)
            for k in range(6): put(c, "sailor", 300 + k * 38, 700 - (k % 2) * 6, flip=True)
            label(d, "SPAIN, 1522", 270, 250, K, YEL, F16)
            if prog > 0.45: label(d, "ONLY 18 MEN", 270, 300, WHITE, RED_D, F16)
        else:
            c.alpha_composite(globe(f, "1519-1522", 0, 1, min(1, prog * 1.3), dots=[SANLUCAR], labels=[("SPAIN", 8, 47, K, YEL)]), (25, 130))
            gulls(d, f, 2, 470); waves(d, f, 600, (200, 230, 250))
            put(c, "wreck", 190 + bob(f, 5, 0.05), 640 + bob(f, 3, 0.1)); label(d, "VICTORIA", 270, 520, GOLD)
            if prog > 0.5: label(d, "ALL THE WAY AROUND", 270, 470, WHITE, RED_D, F16)
    elif i == 1:
        if li < 2:
            castile_banner(d, 40, 160); castile_banner(d, 450, 160)
            put(c, "mag0", 20, FEET, sc=2); label(d, "MAGELLAN", 82, 545, GOLD); label(d, "PORTUGUESE", 90, 580, WHITE, K)
            put(c, "charles", 416, FEET, sc=2, flip=True); label(d, "KING CHARLES I", 440, 545, GOLD); label(d, "SPAIN", 450, 580, WHITE, K)
            label(d, "1518: A DEAL", 270, 250, K, YEL, F16)
            if li == 1:
                label(d, "WEST TO THE SPICE ISLANDS", 270, 300, WHITE, K, F16)
                clove_sack(d, 224, 520 + bob(f, 3, 0.1)); clove_sack(d, 274, 526 + bob(f, 3, 0.1, 1))
                label(d, "CLOVES", 270, 560, WHITE, K)
        else:
            c.alpha_composite(globe(f, "SEPTEMBER 1519", 0, voy_prog(SANJULIAN), prog * 0.9, dots=[SANLUCAR], labels=[("SPAIN", 8, 47, K, YEL), ("SPICE ISLANDS", 128, -8, WHITE, K)]), (25, 110))
            waves(d, f, 600, (200, 230, 250)); gulls(d, f, 2, 450)
            for k in range(5): put(c, "ship" if k == 0 else tint(SP["ship"], 0.8 + 0.04 * k), 30 + k * 95 + t * 3, 640 + (k % 2) * 34 + bob(f, 3, 0.1, k))
            label(d, "5 SHIPS", 150, 470, WHITE, K, F16); label(d, "ABOUT 270 MEN", 390, 470, K, YEL, F16)
    elif i == 2:
        clouds(d, f, 160, col=(220, 224, 230), seed=3)
        if li == 0:
            put(c, f"mag{st(f, 0, 6)}", 30, FEET, sc=2); label(d, "MAGELLAN", 82, 545, GOLD)
            for k in range(3): put(c, f"esp{st(f, k, 6)}", 330 + k * 60, FEET - (k % 2) * 8, flip=True)
            label(d, "SPANISH CAPTAINS", 410, 620, WHITE, K)
            sword_clash(d, 250, 630, f)
            label(d, "PATAGONIA, APRIL 1520", 270, 250, K, YEL, F16)
            if prog > 0.4: label(d, "MUTINY!", 270, 300, WHITE, RED, F16)
        else:
            waves(d, f, 560, (200, 210, 220))
            if prog < 0.35:
                put(c, "mag0", 200, FEET, sc=2); label(d, "MAGELLAN", 252, 545, GOLD)
                label(d, "REVOLT CRUSHED", 270, 250, K, YEL, F16)
            else:
                put(c, "wreck", 10, 640 + bob(f, 3, 0.1)); label(d, "SANTIAGO", 90, 420, GOLD); label(d, "WRECKED", 90, 455, WHITE, RED_D)
                put(c, tint(SP["ship"], 0.85), 360 + (prog - 0.35) * 120, 600 + bob(f, 3, 0.1, 1), flip=True)
                label(d, "SAN ANTONIO", 440, 420, GOLD)
                if prog > 0.6: label(d, "DESERTED", 440, 455, WHITE, RED_D)
                lightning(d, f, 120) if (f // 20) % 4 == 0 else None
                label(d, "TWO SHIPS LOST", 270, 250, K, YEL, F16)
    elif i == 3:
        if li == 0:
            c.alpha_composite(poly_map(f, (-80, -58, -57, -45), h=330, grid=5, title="OCTOBER 21, 1520", dots=[STRAIT_E],
                                       route=([SANJULIAN, (-67.5, -51), STRAIT_E, (-70.5, -53.2), (-71, -53.6), STRAIT_W, (-77, -51.5)], min(1, prog * 1.2)),
                                       labels=[("SOUTH AMERICA", -67, -46.5, WHITE, K), ("THE STRAIT", -63.5, -52.6, K, YEL), ("TIERRA DEL FUEGO", -67.5, -55.8, WHITE, K), ("ATLANTIC", -61, -49, WHITE, K)]), (25, 110))
            waves(d, f, 600, (180, 200, 220)); gulls(d, f, 2, 470)
            for k in range(3): put(c, "ship" if k == 0 else tint(SP["ship"], 0.8), 60 + k * 140 + t * 3, 650 + (k % 2) * 30 + bob(f, 3, 0.1, k))
            label(d, "3 SHIPS LEFT", 270, 490, WHITE, RED_D, F16)
        else:
            clouds(d, f, 150, seed=6); gulls(d, f, 3, 320)
            sun(d, 440, 200)
            for k in range(3): put(c, "ship" if k == 0 else tint(SP["ship"], 0.8), 40 + k * 150 + t * 4, 600 + (k % 2) * 30 + bob(f, 2, 0.05, k))
            label(d, "38 DAYS", 270, 250, K, YEL, F16)
            if prog > 0.4: label(d, "THE PACIFIC", 270, 420, WHITE, K, F16); label(d, "THE PEACEFUL SEA", 270, 460, K, YEL, F16)
    elif i == 4:
        if li == 0:
            c.alpha_composite(globe(f, "THE PACIFIC", voy_prog(STRAIT_W), voy_prog((GUAM[0] - 360, GUAM[1])), prog,
                                    labels=[("PACIFIC OCEAN", -130, 30, WHITE, K), ("AMERICA", -95, 50, WHITE, K), ("ASIA", 95, 50, WHITE, K)]), (25, 110))
            waves(d, f, 600, (200, 230, 250))
            put(c, "ship", 190 + bob(f, 6, 0.05), 650 + bob(f, 3, 0.1))
            label(d, "OVER 3 MONTHS", 270, 470, WHITE, RED_D, F16)
            for k in range(3):
                if (f // 14 + k) % 3 == 0: d.text((60 + k * 200, 540), "?", font=ImageFont.truetype(FONT, 30), fill=YEL)
        else:
            hunger_crew(c, 30, FEET, 3); label(d, "STARVING CREW", 100, 560, WHITE, K)
            sawdust(d, 220, 720); label(d, "SAWDUST", 250, 650, WHITE, K)
            hide(d, 320, 690); label(d, "OX HIDE", 350, 620, WHITE, K)
            biscuit(d, 440, 700, f); label(d, "BISCUIT", 460, 680, WHITE, K)
            put(c, "rat", 260 + (f * 3) % 200, 742)
            label(d, "WORMS AND RATS", 270, 250, K, YEL, F16)
            if prog > 0.5: label(d, "SCURVY: 19 DEAD", 270, 300, WHITE, RED_D, F16)
    elif i == 5:
        if li == 0:
            c.alpha_composite(poly_map(f, (116, 132, 4, 20), h=330, grid=5, title="APRIL 1521", dots=[MACTAN],
                                       labels=[("PHILIPPINES", 118.5, 16.5, WHITE, K), ("MACTAN", 128.0, 10.3, K, YEL), ("CEBU", 120.0, 10.0, WHITE, K)]), (25, 110))
            waves(d, f, 600, (200, 230, 250)); gulls(d, f, 2, 480)
            put(c, "ship", 40, 620 + bob(f, 3, 0.1)); put(c, tint(SP["ship"], 0.8), 200, 600 + bob(f, 3, 0.1, 1))
            put(c, f"mag{st(f, 0, 6)}", 380, FEET, sc=2); label(d, "MAGELLAN", 430, 545, GOLD)
        else:
            put(c, "mag0", 70, FEET + 14, sc=2); label(d, "MAGELLAN", 122, 545, GOLD)
            put(c, "esp0", 10, FEET + 10)
            put(c, f"lapu{st(f, 0, 6)}", 300, FEET, sc=2, flip=True); label(d, "LAPULAPU", 352, 545, GOLD)
            for k in range(2): put(c, f"vis{st(f, k + 1, 8)}", 420 + k * 60, FEET - 6 - k * 8, flip=True)
            for k in range(3): arrow_fly(d, f, k, 420, 600, 180, 630)
            label(d, "MACTAN, APRIL 27, 1521", 270, 250, K, YEL, F16)
            if prog > 0.5: label(d, "MAGELLAN IS KILLED", 270, 300, WHITE, RED_D, F16)
    elif i == 6:
        if li < 2:
            clouds(d, f, 150, seed=4); gulls(d, f, 2, 300)
            clove_tree(d, 400, 690, 200); clove_tree(d, 500, 670, 160)
            put(c, tint(SP["ship"], 0.9), 20, 600 + bob(f, 3, 0.1))
            put(c, f"elc{st(f, 0, 6)}", 180, FEET, sc=2); label(d, "JUAN SEBASTIÁN ELCANO", 230, 545, GOLD)
            label(d, "SURVIVORS' NEW LEADER", 270, 250, K, YEL, F16) if li == 0 else (label(d, "SPICE ISLANDS", 270, 250, K, YEL, F16), label(d, "NOVEMBER 1521", 270, 290, WHITE, K, F16))
            if li == 1: clove_sack(d, 360, 740); clove_sack(d, 420, 745)
        else:
            c.alpha_composite(globe(f, "HOMEWARD", voy_prog((TIDORE[0] - 360, TIDORE[1])), voy_prog((CAPEVERDE[0] - 360, CAPEVERDE[1])), prog,
                                    dots=[TIDORE], labels=[("SPICE ISLANDS", 128, 8, K, YEL), ("INDIAN OCEAN", 60, -35, WHITE, K), ("AFRICA", 20, 20, WHITE, K)]), (25, 110))
            waves(d, f, 600, (120, 140, 190)); put(c, "ship", 180 + t * 4, 650 + bob(f, 3, 0.1))
            label(d, "VICTORIA SAILS ALONE", 270, 470, WHITE, K, F16); label(d, "FULL OF CLOVES", 270, 510, K, YEL, F16)
    elif i == 7:
        clouds(d, f, 140, seed=7); gulls(d, f, 2, 300)
        fort_pt(d, 400, 560)
        label(d, "CAPE VERDE, JULY 1522", 270, 250, K, YEL, F16)
        put(c, "piga", 30, FEET, sc=2); label(d, "PIGAFETTA", 82, 545, GOLD); label(d, "CHRONICLER", 82, 580, WHITE, K)
        if li == 0:
            log_book(d, 220, 600, "WEDNESDAY"); label(d, "SHIP'S LOG", 325, 580, WHITE, K)
            sun(d, 470, 330)
        else:
            put(c, "set1", 420, FEET, flip=True); label(d, "PORTUGUESE", 446, 620, WHITE, K)
            bubble(d, "THURSDAY!", 430, 500)
            log_book(d, 200, 640, "WEDNESDAY", RED)
            sx = 470 - prog * 300; sun(d, sx, 400)
            if prog > 0.5: label(d, "ONE DAY LOST", 270, 300, WHITE, RED_D, F16)
    elif i == 8:
        if li == 0:
            clouds(d, f, 150, seed=2); gulls(d, f, 3, 300)
            put(c, "wreck", 30, 640 + bob(f, 3, 0.1)); label(d, "VICTORIA", 110, 470, GOLD)
            for k in range(4): clove_sack(d, 250 + k * 64, 745 - (k % 2) * 6)
            label(d, "CLOVES", 360, 640, WHITE, K)
            label(d, "SEVILLE, 1522", 270, 250, K, YEL, F16)
            if prog > 0.4: label(d, "WORTH MORE THAN", 270, 300, WHITE, RED_D, F16); label(d, "ALL 5 SHIPS", 270, 336, WHITE, RED_D, F16)
        else:
            gulls(d, f, 3, 260, (80, 50, 50)); waves(d, f, 560, (240, 200, 160))
            put(c, "mag0", 30, FEET, sc=2); label(d, "MAGELLAN", 82, 545, GOLD); label(d, "BEGAN IT", 82, 580, WHITE, K)
            put(c, "elc0", 400, FEET, sc=2, flip=True); label(d, "ELCANO", 452, 545, GOLD); label(d, "FINISHED IT", 452, 580, WHITE, K)
            label(d, "THE FIRST VOYAGE", 270, 250, K, YEL, F16); label(d, "AROUND THE WORLD", 270, 290, K, YEL, F16)
            if prog > 0.45: label(d, "FOLLOW FOR MORE HISTORY", 270, 400, WHITE, RED, F16)
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
