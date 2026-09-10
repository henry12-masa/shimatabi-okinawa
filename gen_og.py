import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630

# ---------- background vertical gradient ----------
top = np.array([79, 195, 217])      # sea-light
mid = np.array([14, 124, 157])      # sea
bot = np.array([7, 90, 118])        # sea-deep

ys = np.linspace(0, 1, H)
colors = np.zeros((H, 3))
for i, t in enumerate(ys):
    if t <= 0.45:
        f = t / 0.45
        colors[i] = top * (1 - f) + mid * f
    else:
        f = (t - 0.45) / 0.55
        colors[i] = mid * (1 - f) + bot * f

bg = np.repeat(colors[:, np.newaxis, :], W, axis=1).astype(np.uint8)
img = Image.fromarray(bg, "RGB").convert("RGBA")

# ---------- warm radial glow top-left ----------
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
cx, cy, r = 150, 120, 480
gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 179, 71, 90))
glow = glow.filter(ImageFilter.GaussianBlur(90))
img = Image.alpha_composite(img, glow)

draw = ImageDraw.Draw(img)

# ---------- bottom wave band ----------
sand = (247, 240, 221, 255)
wave_top = H - 100
pts = [(0, H), (0, wave_top)]
n = 14
for i in range(n + 1):
    x = W * i / n
    y = wave_top + (14 if i % 2 == 0 else -14)
    pts.append((x, y))
pts.append((W, H))
draw.polygon(pts, fill=sand)

# ---------- fonts ----------
FONT_DIR = "C:/Windows/Fonts/"
def font(path, size):
    return ImageFont.truetype(FONT_DIR + path, size)

f_eyebrow = font("YuGothB.ttc", 26)
f_title = font("YuGothB.ttc", 84)
f_tag = font("YuGothM.ttc", 32)
f_badge = font("YuGothB.ttc", 26)

WHITE = (255, 255, 255, 255)

# ---------- eyebrow pill ----------
ex, ey, ew, eh = 100, 78, 380, 56
pill = Image.new("RGBA", (W, H), (0, 0, 0, 0))
pd2 = ImageDraw.Draw(pill)
pd2.rounded_rectangle([ex, ey, ex + ew, ey + eh], radius=eh // 2,
                       outline=(255, 255, 255, 190), width=2,
                       fill=(255, 255, 255, 35))
img.alpha_composite(pill)
draw = ImageDraw.Draw(img)
tw = draw.textlength("OKINAWA TRAVEL PORTAL", font=f_eyebrow)
draw.text((ex + (ew - tw) / 2, ey + (eh - 26) / 2 - 4), "OKINAWA TRAVEL PORTAL",
          font=f_eyebrow, fill=WHITE)

# ---------- hibiscus flower icon ----------
def draw_hibiscus(size):
    fl = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    petal = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    pd = ImageDraw.Draw(petal)
    cx = cy = size / 2
    pw, ph = size * 0.30, size * 0.5
    pd.ellipse([cx - pw / 2, cy - size * 0.42 - ph / 2, cx + pw / 2, cy - size * 0.42 + ph / 2],
               fill=(255, 122, 89, 255))
    for angle in range(0, 360, 72):
        rp = petal.rotate(angle, center=(cx, cy), resample=Image.BICUBIC)
        fl.alpha_composite(rp)
    fd = ImageDraw.Draw(fl)
    r = size * 0.13
    fd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 179, 71, 255))
    return fl

flower_size = 150
flower = draw_hibiscus(flower_size)
flower_x, flower_y = 96, 168
img.alpha_composite(flower, (flower_x, flower_y))

# ---------- title ----------
title_x = flower_x + flower_size + 26
title_y = flower_y + 10
draw.text((title_x, title_y), "しまたび沖縄", font=f_title, fill=WHITE)

# ---------- tagline ----------
tag_lines = [
    "沖縄本島の観光スポット・グルメ・航空券をまるごと1サイトに。",
    "旅の計画がこのページだけで完結します。",
]
ty = 372
for line in tag_lines:
    draw.text((100, ty), line, font=f_tag, fill=(255, 255, 255, 235))
    ty += 46

# ---------- badges ----------
badges = ["観光スポット", "グルメ", "航空券比較"]
bx = 100
by = 486
for label in badges:
    tw = draw.textlength(label, font=f_badge)
    pad_x = 34
    bw = tw + pad_x * 2
    bh = 62
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=bh // 2, fill=(255, 255, 255, 240))
    draw.text((bx + pad_x, by + (bh - 26) / 2 - 3), label, font=f_badge, fill=(7, 90, 118, 255))
    bx += bw + 20

img.convert("RGB").save("og-image.png", "PNG")
print("saved", img.size)
