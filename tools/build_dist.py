#!/usr/bin/env python3
"""Build dist/: flat, upload-ready copies of the campaign.

  python3 tools/build_dist.py

dist/project-files/  every text file the DM needs (folder path kept in the name: sealed/truth/03-ledger.md -> sealed__truth__03-ledger.md)
dist/images/         player-safe images (portraits, battle maps, scenes, player maps)
dist/images-sealed/  sealed images (DM only)
dist/MANIFEST.md     every file, its size and purpose, totals, and the minimum set
"""
import os, shutil, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

# Build-only notes that the DM doesn't need in play.
SKIP_NAMES = {"_handoff-notes.md", "_change-requests.md", "_consistency.md", "_author-requests.md",
              "_player-packet-leak-check.md", "art-manifest.md", "art-list.md", ".gitkeep"}
SKIP_DIRS = {"sealed/art-batches", "sealed/art", "sealed/maps", "art", "build", "tools", "dist", ".git"}
TEXT_DIRS = ["sealed", "player", "play-kit"]
PLAYER_IMG_DIRS = ["art/portraits", "art/battlemaps", "art/scenes", "player/maps"]
SEALED_IMG_DIRS = ["sealed/art", "sealed/maps"]
IMG_EXT = (".jpg", ".jpeg", ".png")

def flat(rel):
    return rel.replace(os.sep, "/").replace("/", "__")

def purpose(rel):
    r = rel.replace(os.sep, "/")
    rules = [
        ("sealed/dm-spine.md", "DM spine: every chapter's beats, milestones, secrets due, clock, endings. Read first."),
        ("sealed/truth/00-index.md", "Name lookup by sound, ID scheme, running rule"),
        ("sealed/truth/03-ledger.md", "Relationship Ledger (read before any vouch)"),
        ("sealed/truth/", "Truth File: NPCs, secrets, events, factions, logs"),
        ("sealed/chapters/act1/", "Act I chapter"), ("sealed/chapters/act2/", "Act II chapter"), ("sealed/chapters/act3/", "Act III chapter"),
        ("sealed/campaign/", "Campaign plan"), ("sealed/world/", "World bible"),
        ("sealed/cities/00-index.md", "Shared city rules: contests, rings, hustle, the Long Wall (§14)"),
        ("sealed/cities/", "City: shops, side activities, contests"),
        ("sealed/rules/", "Rules, builds, tuning, prices"),
        ("player/", "Player-safe reference"),
        ("play-kit/templates/", "Template for a living Claude Doc"),
        ("play-kit/project-instructions.md", "Paste into the project instructions box (not needed as a file)"),
        ("play-kit/", "Play kit"),
    ]
    for k, v in rules:
        if r == k or (k.endswith("/") and r.startswith(k)):
            return v
    return ""

def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    pf, im, ims = (os.path.join(DIST, d) for d in ("project-files", "images", "images-sealed"))
    for d in (pf, im, ims):
        os.makedirs(d)
    rows = []
    for top in TEXT_DIRS:
        for dp, dn, fn in os.walk(os.path.join(ROOT, top)):
            reld = os.path.relpath(dp, ROOT).replace(os.sep, "/")
            if any(reld == s or reld.startswith(s + "/") for s in SKIP_DIRS):
                dn[:] = []; continue
            for f in sorted(fn):
                if not f.endswith(".md") or f in SKIP_NAMES:
                    continue
                rel = os.path.join(reld, f)
                shutil.copy2(os.path.join(ROOT, rel), os.path.join(pf, flat(rel)))
                txt = open(os.path.join(ROOT, rel), encoding="utf-8").read()
                rows.append(("project-files", flat(rel), os.path.getsize(os.path.join(ROOT, rel)), len(re.findall(r"\S+", txt)), purpose(rel)))
    for dirs, dest, tag in ((PLAYER_IMG_DIRS, im, "images"), (SEALED_IMG_DIRS, ims, "images-sealed")):
        for top in dirs:
            for dp, dn, fn in os.walk(os.path.join(ROOT, top)):
                for f in sorted(fn):
                    if f.lower().endswith(IMG_EXT):
                        rel = os.path.relpath(os.path.join(dp, f), ROOT)
                        shutil.copy2(os.path.join(ROOT, rel), os.path.join(dest, flat(rel)))
                        rows.append((tag, flat(rel), os.path.getsize(os.path.join(ROOT, rel)), 0, "Player-safe image" if tag == "images" else "SEALED image (DM only)"))
    write_manifest(rows)
    print(f"dist built: {sum(1 for r in rows if r[0]=='project-files')} text files, "
          f"{sum(1 for r in rows if r[0]=='images')} player images, {sum(1 for r in rows if r[0]=='images-sealed')} sealed images")

MIN_SET = ["sealed__dm-spine.md", "sealed__truth__*", "sealed__chapters__act1__*", "sealed__rules__*",
           "sealed__cities__00-index.md", "sealed__cities__01-home-city-shops.md", "sealed__cities__02-enchanters-row.md",
           "sealed__cities__03-emberford.md", "sealed__world__00-core-truths.md", "sealed__world__02-emberford.md",
           "player__*", "play-kit__templates__*", "play-kit__token-tool.md", "play-kit__session-one-opener.md"]

def write_manifest(rows):
    def kb(n): return f"{n/1024:,.0f} KB"
    pfs = [r for r in rows if r[0] == "project-files"]
    lines = ["# MANIFEST (dist/)", "",
             "> Built by `tools/build_dist.py`. File names carry their old folders (`sealed__truth__03-ledger.md` was `sealed/truth/03-ledger.md`). **Anything starting `sealed__` is DM only. Don't open it.**", "",
             "## Totals", "",
             f"- **project-files:** {len(pfs)} files · {sum(r[3] for r in pfs):,} words · {kb(sum(r[2] for r in pfs))}",
             f"- **images (player-safe):** {sum(1 for r in rows if r[0]=='images')} files · {kb(sum(r[2] for r in rows if r[0]=='images'))}",
             f"- **images-sealed (DM only):** {sum(1 for r in rows if r[0]=='images-sealed')} files · {kb(sum(r[2] for r in rows if r[0]=='images-sealed'))}", "",
             "## Minimum set (if the project's knowledge limit is hit)", "",
             "Upload these first. Swap in the next act's chapters (`sealed__chapters__act2__*`, then `act3`) and the other city files when the story gets there.", ""]
    lines += [f"- `{m}`" for m in MIN_SET]
    lines += ["", "`play-kit__project-instructions.md` and `play-kit__UPLOAD-GUIDE.md` don't need uploading as files: the instructions get pasted into the project's instructions box, and the guide is for you.", ""]
    for tag, title in (("project-files", "project-files/"), ("images", "images/ (player-safe)"), ("images-sealed", "images-sealed/ (DM only)")):
        lines += [f"## {title}", "", "| File | Size | Words | Purpose |", "|---|---|---|---|"]
        for r in rows:
            if r[0] == tag:
                lines.append(f"| `{r[1]}` | {kb(r[2])} | {r[3] or ''} | {r[4]} |")
        lines.append("")
    open(os.path.join(DIST, "MANIFEST.md"), "w", encoding="utf-8").write("\n".join(lines))

if __name__ == "__main__":
    main()
