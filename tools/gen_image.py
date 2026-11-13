#!/usr/bin/env python3
"""Generate or edit an image with the Gemini API.

The API key is injected by the environment's network proxy; this script sends a
placeholder header that the proxy replaces. No key is stored anywhere.

Usage:
  python3 tools/gen_image.py OUT.png "prompt text" [--ref REF1.png ...] [--model MODEL] [--aspect 3:4]

A hard cap on the number of images lives in tools/.image_budget (a single integer:
images remaining). The script refuses to run when it reaches 0.
"""
import argparse, base64, json, os, sys, urllib.request, mimetypes

HERE = os.path.dirname(os.path.abspath(__file__))
BUDGET = os.path.join(HERE, ".image_budget")
STYLE = ("Classic painted fantasy illustration in the manner of a 1980s adventure book cover: "
         "rich oil painting, visible brushwork, dramatic warm-and-cool lighting with deep shadows, "
         "painterly detail, period-accurate medieval clothing and materials, grounded and heroic rather "
         "than cartoonish, no text, no letters, no watermark, no border.")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("prompt")
    ap.add_argument("--ref", nargs="*", default=[])
    ap.add_argument("--model", default=os.environ.get("IMG_MODEL", "gemini-3-pro-image-preview"))
    ap.add_argument("--aspect", default=None)
    a = ap.parse_args()

    left = int(open(BUDGET).read().strip()) if os.path.exists(BUDGET) else 0
    if left <= 0:
        sys.exit("Image budget is 0. Raise it in tools/.image_budget only with the player's OK.")

    parts = []
    for r in a.ref:
        mt = mimetypes.guess_type(r)[0] or "image/png"
        parts.append({"inline_data": {"mime_type": mt, "data": base64.b64encode(open(r, "rb").read()).decode()}})
    parts.append({"text": a.prompt.strip() + "\n\n" + STYLE})
    body = {"contents": [{"parts": parts}], "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]}}
    if a.aspect:
        body["generationConfig"]["imageConfig"] = {"aspectRatio": a.aspect}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{a.model}:generateContent"
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": "placeholder"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.load(resp)

    for cand in data.get("candidates", []):
        for p in cand.get("content", {}).get("parts", []):
            blob = p.get("inline_data") or p.get("inlineData")
            if blob:
                os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
                open(a.out, "wb").write(base64.b64decode(blob["data"]))
                open(BUDGET, "w").write(str(left - 1))
                print(f"saved {a.out} (budget left: {left - 1})")
                return
    sys.exit("No image returned: " + json.dumps(data)[:800])

if __name__ == "__main__":
    main()
