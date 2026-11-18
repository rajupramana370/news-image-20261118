#!/usr/bin/env python3
"""Draw the news-image entry for 18 November 2026.

A one-page newspaper front page, 1024x1024, built only from stories
verified from live reporting on the day itself (The Daily Short, BBC,
Al Jazeera, Reuters, Euronews, Nexus Europa). Run: python3 draw_news.py
Writes entry.png next to this file.
"""

import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
RED = (179, 38, 30)
NAVY = (31, 56, 100)
TEAL = (14, 94, 94)
GOLD = (176, 132, 30)
GREY = (90, 88, 80)
PANEL = (255, 255, 255)
LINE = (200, 194, 178)

F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, max_w, fill=INK, leading=1.28):
    lines = wrap(draw, text, fnt, max_w)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def headline(draw, x, y, text, fnt, max_w, fill=INK, leading=1.08):
    return text_block(draw, x, y, text, fnt, max_w, fill=fill, leading=leading)


def kicker(draw, x, y, text, color=RED):
    fnt = font(F_SANS_B, 21)
    draw.text((x, y), text.upper(), font=fnt, fill=color)
    return y + 30


def panel(draw, x, y, w, h, fill=PANEL):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fill,
                           outline=LINE, width=2)


def draw_burning_tanker(draw, x, y, w, h):
    """A tanker on a grey sea, smoke and flames rising from its deck."""
    sky = (224, 228, 232)
    draw.rectangle([x, y, x + w, y + h], fill=sky)
    # smoke columns
    for sx, sy, sr in ((x + w * 0.32, y + 34, 26), (x + w * 0.52, y + 22, 32),
                       (x + w * 0.68, y + 44, 22)):
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(120, 120, 118))
        draw.ellipse([sx - sr + 10, sy - sr - 12, sx + sr + 10, sy + sr - 12],
                     fill=(150, 150, 148))
    # sea
    draw.rectangle([x, y + h - 40, x + w, y + h], fill=(52, 96, 138))
    for i in range(4):
        wx = x + 16 + i * 86
        draw.arc([wx, y + h - 30, wx + 52, y + h - 12], 0, 180,
                 fill=(255, 255, 255), width=3)
    # hull
    hy = y + h - 78
    draw.polygon([(x + 14, hy), (x + w - 14, hy),
                  (x + w - 40, y + h - 40), (x + 40, y + h - 40)],
                 fill=(148, 38, 28))
    # containers
    for i, col in enumerate(((214, 172, 58), (58, 118, 88), (180, 90, 40))):
        cx0 = x + 34 + i * 62
        draw.rectangle([cx0, hy - 34, cx0 + 56, hy - 2], fill=col,
                       outline=(60, 60, 60), width=2)
    # funnel
    draw.rectangle([x + w - 66, hy - 52, x + w - 36, hy - 2],
                   fill=(240, 240, 240), outline=(90, 90, 90), width=2)
    # flames above the middle container
    fx, fy = x + w // 2 - 10, hy - 34
    draw.polygon([(fx, fy), (fx + 14, fy - 34), (fx + 30, fy - 10),
                  (fx + 44, fy - 40), (fx + 58, fy)],
                 fill=(240, 140, 30), outline=(200, 80, 10))
    draw.polygon([(fx + 16, fy), (fx + 26, fy - 22), (fx + 40, fy)],
                 fill=(245, 200, 60))


def draw_cyclone(draw, x, y, w, h):
    """A spiral storm over a dark sea, rain bands curling in."""
    draw.rectangle([x, y, x + w, y + h], fill=(210, 224, 238))
    cx, cy = x + w // 2, y + h // 2 + 4
    for turn in range(3):
        r0 = 10 + turn * 16
        for a in range(0, 300, 6):
            ang = math.radians(a + turn * 40)
            r = r0 + a * 0.10
            px = cx + r * math.cos(ang)
            py = cy + r * math.sin(ang) * 0.85
            draw.ellipse([px - 5, py - 5, px + 5, py + 5],
                         fill=(40, 80, 140) if turn < 2 else (90, 130, 180))
    draw.ellipse([cx - 14, cy - 12, cx + 14, cy + 12], fill=(240, 240, 235))
    # coastline at the bottom
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=(214, 190, 140))
    draw.line([x, y + h - 26, x + w, y + h - 26], fill=(120, 100, 60), width=2)
    # rain streaks
    for i in range(6):
        rx = x + 18 + i * 30
        draw.line([rx, y + 14, rx - 8, y + 34], fill=(120, 150, 190), width=3)


def draw_chip(draw, x, y, w, h):
    """A green chip on a dark board, pins out, with its headline number."""
    draw.rectangle([x, y, x + w, y + h], fill=(24, 38, 30))
    cx, cy = x + w // 2, y + h // 2 - 8
    # pins
    for i in range(5):
        px = cx - 52 + i * 26
        draw.line([px, cy - 46, px, cy - 62], fill=(200, 200, 190), width=4)
        draw.line([px, cy + 46, px, cy + 62], fill=(200, 200, 190), width=4)
    for j in range(3):
        py = cy - 22 + j * 22
        draw.line([cx - 62, py, cx - 78, py], fill=(200, 200, 190), width=4)
        draw.line([cx + 62, py, cx + 78, py], fill=(200, 200, 190), width=4)
    # die
    draw.rounded_rectangle([cx - 52, cy - 46, cx + 52, cy + 46], radius=8,
                           fill=(28, 110, 66), outline=(140, 220, 170), width=3)
    draw.rounded_rectangle([cx - 30, cy - 24, cx + 30, cy + 24], radius=5,
                           fill=(18, 80, 48))
    draw.text((cx - 22, cy - 12), "AI", font=font(F_SANS_B, 24),
              fill=(180, 240, 200))
    # rising bars
    bx = x + 18
    for i, bh in enumerate((14, 24, 36, 50)):
        draw.rectangle([bx + i * 20, y + h - 18 - bh, bx + i * 20 + 12,
                        y + h - 18], fill=(120, 220, 150))


def draw_bridge_hit(draw, x, y, w, h):
    """A road bridge over water, its middle span hit by a blast."""
    sky = (216, 228, 240)
    draw.rectangle([x, y, x + w, y + h], fill=sky)
    draw.rectangle([x, y + h - 36, x + w, y + h], fill=(58, 110, 158))
    for i in range(4):
        wx = x + 12 + i * 46
        draw.arc([wx, y + h - 28, wx + 34, y + h - 12], 0, 180,
                 fill=(255, 255, 255), width=3)
    deck_y = y + h - 78
    # deck in two pieces with a gap in the middle
    draw.rectangle([x + 8, deck_y, x + w // 2 - 26, deck_y + 10],
                   fill=(70, 70, 74))
    draw.rectangle([x + w // 2 + 26, deck_y, x + w - 8, deck_y + 10],
                   fill=(70, 70, 74))
    # falling span piece
    draw.polygon([(x + w // 2 - 26, deck_y + 4), (x + w // 2 + 26, deck_y + 4),
                  (x + w // 2 + 10, deck_y + 34), (x + w // 2 - 10, deck_y + 34)],
                 fill=(90, 90, 96))
    # pylons
    for px in (x + 34, x + w - 46):
        draw.rectangle([px, y + 22, px + 10, deck_y], fill=(96, 96, 102))
    # blast starburst over the gap
    cx, cy = x + w // 2, deck_y - 22
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        x1, y1 = cx + 10 * math.cos(a), cy + 10 * math.sin(a)
        x2, y2 = cx + 36 * math.cos(a), cy + 36 * math.sin(a)
        draw.line([x1, y1, x2, y2], fill=(230, 120, 20), width=5)
    draw.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(245, 180, 40),
                 outline=(200, 80, 10), width=3)


def draw_cop_globe(draw, x, y, w, h):
    """A globe ringed by leaves: climate talks."""
    draw.rectangle([x, y, x + w, y + h], fill=(228, 238, 228))
    cx, cy, r = x + w // 2, y + h // 2, 52
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(80, 140, 190),
                 outline=NAVY, width=3)
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r],
                 outline=(255, 255, 255), width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=2)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 180,
             fill=(255, 255, 255), width=2)
    # leaves around the globe
    for ang in (200, 250, 290, 340):
        a = math.radians(ang)
        lx, ly = cx + (r + 16) * math.cos(a), cy + (r + 16) * math.sin(a)
        draw.ellipse([lx - 12, ly - 6, lx + 12, ly + 6], fill=(60, 140, 70),
                     outline=(30, 100, 40), width=2)


def draw_winter_tent(draw, x, y, w, h):
    """A tent in falling snow: Gaza faces winter without shelter."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 238, 244))
    # snowflakes
    for sx, sy in ((x + 24, y + 20), (x + w - 30, y + 26), (x + w // 2, y + 16),
                   (x + 40, y + h - 30), (x + w - 44, y + h - 36)):
        for ang in range(0, 180, 60):
            a = math.radians(ang)
            draw.line([sx - 8 * math.cos(a), sy - 8 * math.sin(a),
                       sx + 8 * math.cos(a), sy + 8 * math.sin(a)],
                      fill=(140, 170, 200), width=2)
    # ground snow
    draw.rectangle([x, y + h - 24, x + w, y + h], fill=(255, 255, 255))
    # tent
    cx = x + w // 2
    ty = y + h - 24
    draw.polygon([(cx - 58, ty), (cx, y + 26), (cx + 58, ty)],
                 fill=(200, 170, 120), outline=(120, 90, 50), width=3)
    draw.polygon([(cx - 14, ty), (cx, y + 58), (cx + 14, ty)],
                 fill=(90, 70, 40))
    # cold moon
    draw.ellipse([x + w - 46, y + 16, x + w - 18, y + 44], fill=(220, 225, 235),
                 outline=(160, 170, 190), width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36  # margin

    # ---- Masthead ----
    d.text((M, 22), "THE WORLD IN ONE DAY", font=font(F_SERIF, 58), fill=INK)
    d.line([M, 96, W - M, 96], fill=INK, width=4)
    d.line([M, 102, W - M, 102], fill=INK, width=2)
    d.text((M, 112), "WEDNESDAY, 18 NOVEMBER 2026",
           font=font(F_SANS_B, 26), fill=RED)
    right_label = "SIX STORIES  •  EVERY REGION"
    rl_font = font(F_SANS_B, 20)
    d.text((W - M - d.textlength(right_label, font=rl_font), 114),
           right_label, font=rl_font, fill=GREY)

    # ---- Lead story: US-Iran clash in Hormuz ----
    x, y, w, h = M, 158, W - 2 * M, 296
    panel(d, x, y, w, h)
    tx = x + 24
    ty = y + 16
    ty = kicker(d, tx, ty, "Middle East — US-Iran clash")
    ty = headline(d, tx, ty, "WAR DRUMS IN THE STRAIT",
                  font(F_SERIF, 46), 540, leading=1.05)
    ty += 6
    ty = text_block(d, tx, ty,
                    "US jets struck a Revolutionary Guards missile site on "
                    "Qeshm Island, and Washington said it sank five "
                    "Iranian tankers. Iran fired drones at a US radar base "
                    "in Bahrain and warned ships away from the Strait of "
                    "Hormuz.",
                    font(F_SANS, 22), 540)
    draw_burning_tanker(d, x + w - 392, y + 16, 368, h - 32)

    # ---- Row 2: two stories ----
    y2, h2 = 470, 232
    w2 = (W - 2 * M - 16) // 2
    # Cyclone Akvan
    panel(d, M, y2, w2, h2)
    tx = M + 18
    ty = kicker(d, tx, y2 + 12, "Asia — Weather", color=TEAL)
    ty = headline(d, tx, ty, "CYCLONE AKVAN BEARS DOWN",
                  font(F_SERIF, 25), w2 - 206, leading=1.05)
    ty += 4
    text_block(d, tx, ty,
               "A cyclone strengthening over the Bay of Bengal is set to "
               "hit the Andhra Pradesh coast on Friday, with officials "
               "warning coastal districts to prepare.",
               font(F_SANS, 17), w2 - 206)
    draw_cyclone(d, M + w2 - 180, y2 + 52, 168, h2 - 68)
    # Nvidia
    x3 = M + w2 + 16
    panel(d, x3, y2, w2, h2)
    tx = x3 + 18
    ty = kicker(d, tx, y2 + 12, "Business — Tech", color=NAVY)
    ty = headline(d, tx, ty, "NVIDIA DOUBLES ITS REVENUE",
                  font(F_SERIF, 25), w2 - 206, leading=1.05)
    ty += 4
    text_block(d, tx, ty,
               "Nvidia reported quarterly revenue of $115.8 billion, up "
               "103% on a year ago, as data-centre sales passed "
               "$107 billion.",
               font(F_SANS, 17), w2 - 206)
    draw_chip(d, x3 + w2 - 180, y2 + 52, 168, h2 - 68)

    # ---- Row 3: three stories ----
    y3, h3 = 718, 196
    w3 = (W - 2 * M - 32) // 3
    stories = [
        ("Europe — War", "KERCH BRIDGE HIT AGAIN",
         "Ukraine struck the bridge to Crimea for a second night "
         "running, shutting it down, as Russia hit bridges around "
         "Kyiv in reply.", RED, draw_bridge_hit),
        ("World — Climate", "COP31 ENTERS FINAL DAYS",
         "Climate talks in Antalya enter their decisive phase, with "
         "144 disputed items still on the table before Friday's "
         "deadline.", TEAL, draw_cop_globe),
        ("Middle East — Gaza", "GAZA FACES A COLD WINTER",
         "The UN warns more people will die of cold as winter sets "
         "in: 1.7 million remain displaced, most without adequate "
         "shelter.", NAVY, draw_winter_tent),
    ]
    for i, (kick, head, body, col, icon) in enumerate(stories):
        px = M + i * (w3 + 16)
        panel(d, px, y3, w3, h3)
        tx = px + 16
        ty = kicker(d, tx, y3 + 12, kick, color=col)
        ty = headline(d, tx, ty, head, font(F_SERIF, 23), w3 - 32, leading=1.05)
        ty += 4
        text_block(d, tx, ty, body, font(F_SANS, 16), w3 - 32)

    # ---- Bottom strip ----
    y4 = 930
    d.rectangle([M, y4, W - M, y4 + 56], fill=NAVY)
    d.text((M + 16, y4 + 6), "ALSO TODAY:",
           font=font(F_SANS_B, 20), fill=(255, 210, 90))
    text_block(d, M + 170, y4 + 8,
               "Trump arrives in Manila for Quad talks  •  India and "
               "Japan hold 2+2 talks in Tokyo  •  Pattinson named the "
               "new James Bond  •  Romania hit by a 5.3 quake",
               font(F_SANS, 18), W - 2 * M - 186, fill=(255, 255, 255))

    # ---- Footer ----
    foot = "Drawn from live reporting: The Daily Short  •  BBC  •  Al Jazeera  •  Reuters  •  Euronews"
    d.text((M, 996), foot, font=font(F_SANS, 15), fill=GREY)
    right = "make.fun  •  @raju-pramana"
    rf = font(F_SANS, 15)
    d.text((W - M - d.textlength(right, font=rf), 996), right, font=rf, fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
