# Token Tool (for the DM)

> Player-safe. Use this in a fight that has a battle map, **if** you can run Python and open the map image. If you can't, track positions in text instead (see the project instructions, section 9).

## What it does
Takes an overhead battle map, adds a **lettered/numbered grid** around the edge (A, B, C… across the top; 1, 2, 3… down the side; one square = 5 ft), and draws a colored circle token with a letter for each creature at its square. Show the result to Jeremy at the start of a round, or whenever positions change a lot.

## Token colors (keep them consistent)
| Who | Text | Color |
|---|---|---|
| Ash | A | `#2e7d32` (green) |
| Gideon | G | `#1565c0` (blue) |
| Zeke | Z | `#6a1b9a` (purple) |
| Moss | M | `#8d6e63` (brown) |
| Bart | B | `#f9a825` (gold) |
| Allies | first letter | `#00838f` (teal) |
| Enemies | 1, 2, 3… | `#b71c1c` (red) |

## Choosing the grid size
`cols` = how many 5-ft squares wide the room is. A 40 × 60 ft room drawn 2 wide by 3 tall is `cols = 8`. If you don't know, use **20** for a big room and **12** for a small one, and say so. The rows are worked out from the image's shape.

## The code
```python
from PIL import Image, ImageDraw, ImageFont
import string

def token_map(src, out, cols, tokens):
    """tokens: list of dicts like {"col": "J", "row": 10, "text": "A", "color": "#2e7d32"}"""
    im = Image.open(src).convert("RGB")
    W, H = im.size
    cell = W / cols
    rows = int(round(H / cell))
    m = int(cell * 0.9)                      # margin for the coordinates
    canvas = Image.new("RGB", (W + m, H + m), "#1d1a16")
    canvas.paste(im, (m, m))
    d = ImageDraw.Draw(canvas, "RGBA")
    for c in range(cols + 1):
        x = m + c * cell; d.line([(x, m), (x, m + H)], fill=(0, 0, 0, 90), width=1)
    for r in range(rows + 1):
        y = m + r * cell; d.line([(m, y), (m + W, y)], fill=(0, 0, 0, 90), width=1)
    try:
        f = ImageFont.truetype("DejaVuSans-Bold.ttf", int(cell * 0.45))
        tf = ImageFont.truetype("DejaVuSans-Bold.ttf", int(cell * 0.5))
    except OSError:
        f = tf = ImageFont.load_default()
    letters = list(string.ascii_uppercase) + ["A" + l for l in string.ascii_uppercase]
    for c in range(cols):
        d.text((m + c * cell + cell * 0.35, m * 0.2), letters[c], font=f, fill="#efe2c0")
    for r in range(rows):
        d.text((m * 0.15, m + r * cell + cell * 0.25), str(r + 1), font=f, fill="#efe2c0")
    for t in tokens:
        c = letters.index(t["col"]); r = t["row"] - 1
        x0, y0 = m + c * cell + cell * 0.1, m + r * cell + cell * 0.1
        x1, y1 = x0 + cell * 0.8, y0 + cell * 0.8
        d.ellipse([x0, y0, x1, y1], fill=t.get("color", "#b71c1c"), outline="white", width=3)
        d.text((x0 + cell * 0.25, y0 + cell * 0.12), t["text"], font=tf, fill="white")
    canvas.save(out)
    return out

# Example
# token_map("ch01-the-willow.jpg", "round1.jpg", 12, [
#     {"col": "F", "row": 6, "text": "A", "color": "#2e7d32"},
#     {"col": "H", "row": 7, "text": "1", "color": "#b71c1c"},
# ])
```

## Round line (always, even when you show the picture)
`Round 2 · Ash J10 · Gideon E4 · Zeke F4 · Moss — · Bart rafter above J9 · brute L11 (bloodied) · cutpurse N3`
