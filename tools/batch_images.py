#!/usr/bin/env python3
"""Submit / poll / collect a Gemini Batch API image job (half price, up to 24h).

  python3 tools/batch_images.py submit jobs.json   # reserves budget, submits, saves state
  python3 tools/batch_images.py poll  state.json   # prints status
  python3 tools/batch_images.py collect state.json # saves images when done

jobs.json: [{"key":"npc-010","out":"art/portraits/npc-010-rook.jpg","prompt":"...","aspect":"3:4","refs":["art/portraits/pc-01-ash.jpg"]}]
The API key is injected by the network proxy (placeholder header below).
"""
import base64, json, os, sys, urllib.request, mimetypes, fcntl, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_image import STYLE, BUDGET

API = "https://generativelanguage.googleapis.com/v1beta"
MODEL = os.environ.get("IMG_MODEL", "gemini-3-pro-image")
H = {"Content-Type": "application/json", "x-goog-api-key": "placeholder"}

def call(url, body=None, method=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, headers=H, method=method)
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)

def submit(path):
    jobs = json.load(open(path))
    with open(BUDGET, "r+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        left = int(f.read().strip() or 0)
        if left < len(jobs):
            sys.exit(f"Budget {left} < {len(jobs)} jobs. Get the player's OK first.")
        f.seek(0); f.truncate(); f.write(str(left - len(jobs)))
    reqs = []
    for j in jobs:
        parts = []
        for r in j.get("refs", []):
            parts.append({"inline_data": {"mime_type": mimetypes.guess_type(r)[0] or "image/png",
                                          "data": base64.b64encode(open(r, "rb").read()).decode()}})
        parts.append({"text": j["prompt"].strip() + "\n\n" + STYLE})
        ic = {"imageSize": j.get("size", "2K")}
        if j.get("aspect"): ic["aspectRatio"] = j["aspect"]
        reqs.append({"request": {"contents": [{"parts": parts}],
                                 "generationConfig": {"responseModalities": ["IMAGE", "TEXT"], "imageConfig": ic}},
                     "metadata": {"key": j["key"]}})
    body = {"batch": {"display_name": os.path.basename(path), "input_config": {"requests": {"requests": reqs}}}}
    res = call(f"{API}/models/{MODEL}:batchGenerateContent", body)
    state = {"batch": res.get("name"), "jobs": jobs, "submitted": time.time(), "raw": {k: v for k, v in res.items() if k != "metadata"}}
    out = path.replace(".json", ".state.json")
    json.dump(state, open(out, "w"), indent=1)
    print("submitted", res.get("name"), "->", out)

def poll(path):
    st = json.load(open(path))
    r = call(f"{API}/{st['batch']}")
    meta = r.get("metadata", {})
    print(meta.get("state"), meta.get("batchStats"), "done" if r.get("done") else "")
    return r

def collect(path):
    st = json.load(open(path))
    r = call(f"{API}/{st['batch']}")
    if not r.get("done"):
        print("not done:", r.get("metadata", {}).get("state")); return
    outs = {j["key"]: j["out"] for j in st["jobs"]}
    resp = r.get("response", {})
    inl = resp.get("inlinedResponses", {}).get("inlinedResponses", resp.get("inlinedResponses", []))
    ok, bad = 0, []
    for item in inl:
        key = item.get("metadata", {}).get("key")
        saved = False
        for c in item.get("response", {}).get("candidates", []):
            for p in c.get("content", {}).get("parts", []):
                b = p.get("inlineData") or p.get("inline_data")
                if b and key in outs:
                    os.makedirs(os.path.dirname(outs[key]), exist_ok=True)
                    open(outs[key], "wb").write(base64.b64decode(b["data"])); saved = True; ok += 1; break
            if saved: break
        if not saved: bad.append((key, json.dumps(item)[:300]))
    print(f"saved {ok}; failed {len(bad)}")
    for b in bad: print("FAILED", b)

if __name__ == "__main__":
    {"submit": submit, "poll": poll, "collect": collect}[sys.argv[1]](sys.argv[2])
