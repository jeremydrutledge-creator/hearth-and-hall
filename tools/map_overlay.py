#!/usr/bin/env python3
"""Add numbered markers + a key to a map, or a coordinate grid + tokens to a battle map.

Numbered map:  python3 tools/map_overlay.py key  IN.png OUT.png markers.json
  markers.json: {"title": "...", "markers": [{"n":1,"x":740,"y":390,"label":"Crownhill"}, ...]}
Battle map:    python3 tools/map_overlay.py grid IN.png OUT.png --cols 20 [--tokens tokens.json]
  tokens.json: [{"col":"D","row":4,"text":"A","color":"#2e7d32"}, ...]
Coordinates in markers.json are pixels on the source image.
"""
import json, sys, argparse, string
from PIL import Image, ImageDraw, ImageFont

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def key_map(src, out, spec):
    im = Image.open(src).convert("RGB")
    W, H = im.size
    d = ImageDraw.Draw(im)
    r = max(14, W // 50)
    f = font(F, int(r * 1.1))
    for m in spec["markers"]:
        x, y = m["x"], m["y"]
        d.ellipse([x - r, y - r, x + r, y + r], fill="#7a1f1f", outline="#f3e7c9", width=3)
        t = str(m["n"]); bw = d.textbbox((0, 0), t, font=f)
        d.text((x - (bw[2] - bw[0]) / 2, y - (bw[3] - bw[1]) / 2 - bw[1]), t, font=f, fill="#f3e7c9")
    # key panel on the right
    lf = font(FS, max(18, W // 45)); tf = font(FS, max(24, W // 32))
    lines = [f'{m["n"]}  {m["label"]}' for m in spec["markers"]]
    lh = lf.size + 10
    pw = max(d.textbbox((0, 0), s, font=lf)[2] for s in lines + [spec.get("title", "")]) + 60
    panel = Image.new("RGB", (pw, H), "#efe2c0")
    pd = ImageDraw.Draw(panel)
    y = 30
    if spec.get("title"):
        pd.text((30, y), spec["title"], font=tf, fill="#3b2a1a"); y += tf.size + 24
    for s in lines:
        pd.text((30, y), s, font=lf, fill="#3b2a1a"); y += lh
    pd.line([(0, 0), (0, H)], fill="#3b2a1a", width=4)
    canvas = Image.new("RGB", (W + pw, H)); canvas.paste(im, (0, 0)); canvas.paste(panel, (W, 0))
    canvas.save(out)

def grid_map(src, out, cols, tokens):
    im = Image.open(src).convert("RGB")
    W, H = im.size
    cell = W / cols; rows = int(round(H / cell))
    m = int(cell * 0.9)  # margin for coordinates
    canvas = Image.new("RGB", (W + m, H + m), "#1d1a16"); canvas.paste(im, (m, m))
    d = ImageDraw.Draw(canvas, "RGBA")
    for c in range(cols + 1):
        x = m + c * cell; d.line([(x, m), (x, m + H)], fill=(0, 0, 0, 90), width=1)
    for r in range(rows + 1):
        y = m + r * cell; d.line([(m, y), (m + W, y)], fill=(0, 0, 0, 90), width=1)
    f = font(F, int(cell * 0.45))
    letters = list(string.ascii_uppercase) + ["A" + l for l in string.ascii_uppercase]
    for c in range(cols):
        t = letters[c]; bw = d.textbbox((0, 0), t, font=f)
        d.text((m + c * cell + (cell - bw[2]) / 2, (m - bw[3]) / 2), t, font=f, fill="#efe2c0")
    for r in range(rows):
        t = str(r + 1); bw = d.textbbox((0, 0), t, font=f)
        d.text(((m - bw[2]) / 2, m + r * cell + (cell - bw[3]) / 2), t, font=f, fill="#efe2c0")
    tf = font(F, int(cell * 0.5))
    for tk in tokens or []:
        c = letters.index(tk["col"]); r = tk["row"] - 1
        x0, y0 = m + c * cell + cell * 0.1, m + r * cell + cell * 0.1
        x1, y1 = x0 + cell * 0.8, y0 + cell * 0.8
        d.ellipse([x0, y0, x1, y1], fill=tk.get("color", "#2e7d32"), outline="white", width=3)
        bw = d.textbbox((0, 0), tk["text"], font=tf)
        d.text(((x0 + x1 - bw[2]) / 2, (y0 + y1 - bw[3]) / 2 - bw[1] / 2), tk["text"], font=tf, fill="white")
    canvas.save(out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("mode"); ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("spec", nargs="?"); ap.add_argument("--cols", type=int, default=20); ap.add_argument("--tokens")
    a = ap.parse_args()
    if a.mode == "key": key_map(a.src, a.out, json.load(open(a.spec)))
    else: grid_map(a.src, a.out, a.cols, json.load(open(a.tokens)) if a.tokens else None)
