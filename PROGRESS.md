# Hearth & Hall — progress notes

Single-file 3D browser game (`index.html`, Three.js r128 from CDN). Mobile-first,
touch controls. A village-builder; the brief is "nail the first 30 minutes of an
Age of Empires-style game."

**Live (GitHub Pages):** https://jeremydrutledge-creator.github.io/hearth-and-hall/
**Working branch:** `claude/title-screen-tweak-f01hwq`
(Pages serves from this branch. Repo is public so Pages works on the free plan.)

## Done so far
1. Title-screen tagline; renamed `Index.html` → `index.html` (case-sensitive hosting).
2. **Visual overhaul** — sRGB + ACES color pipeline with linear-converted palette
   (deep greens), warm sun + crisp shadows, richer terrain (meadow patches,
   forest floor, sandy shore, dirt courtyard around the keep), distant mountain
   ring, instanced grass/flowers/reeds/pebbles, mushrooms & ferns, clouds, birds,
   pollen motes, specular pond water.
3. **Life & juice** — chimney smoke (keep/houses/hall), flying work chips when
   gathering, tree stumps after felling, starter hens by the keep.
4. **Ground patches** — trampled-earth disc under each building (planted look).
5. **Fishing activity** — Assign → 🎣 Fish, or tap the pond. Settler walks to dry
   shore, casts with a rod, catches fish (food), hauls home. Phases `toFish`/`fishing`.
6. **Grander keep** — turrets, crenellations, arched gate, banner.
7. **Floating "+N" popups** on resource drop-off (DOM overlay, `floatGain`).
8. **Pond polish** — lily pads + blossoms.
9. **Building overhaul** — all models rebuilt to match the keep: shared palette
   (`bPlaster/bTimber/bStone/bTile/bThatch/bPlank...`) + a `gableRoof()` ridge-roof
   helper. House=Tudor cottage w/ chimney, storehouse=timber+barrels, farm=fenced
   crops+scarecrow, coop/pen improved, lumber=open shed+log pile+axe, quarry=pit+
   hoist+cut blocks, hall=grand stone/timber longhall w/ twin banners.
10. **Bugfix:** placement no longer falsely says "Can't build in the pond" on low
    but dry ground — the check now tests proximity to the actual pond disc.

11. **Worn paths** — dirt trails (`wornPath()` ribbon meshes w/ a generated fade
    texture) trodden from the keep out to grove/pond/rocks/forest/hills.
12. **Ducks** — 4 paddle around the pond (`ducks[]` + `tickDuck`, float at WATER_Y).
13. **Fish shoals** — depletable+replenishing fishing spots (`shoals[]`, `makeShoal`/
    `tickShoal`/`nearestShoal`/`shoreNear`/`depleteShoal`). Ripple rings + circling
    fish + invisible tap-disc. Fishing now targets the nearest shoal (`u.shoal`),
    casts from the shore nearest it, and each catch removes 9; an emptied shoal
    despawns and a new one fades in elsewhere after ~9-16s. Tap a shoal to fish it.
14. **Day cycle** — `updateDay(t)` sweeps the sun golden-morning→noon→amber-evening
    over `DAYLEN=200s` (never full night). Drives sun pos/color/intensity, hemi
    tint, fog, and a redrawn sky gradient (`drawSky`). Always playable/bright.

15. **Progression spine (Ages + objectives)** — FIRST pillar of the vision below.
    `AGES[]` (Camp→Hamlet→Village→Town→City), each with an objective checklist
    (`objs[].check()` against G state). `checkObjectives()` (loop, ~3/s) latches
    done objectives in `G.objDone`, toasts each, and auto-advances the age when all
    are met (`advanceAge()` bumps `G.popCap`). `AGE_UNLOCK` gates each building by
    age — refreshHUD adds `.locked` 🔒 + disables until unlocked. Live panel
    `#quests` (top-left, collapsible) via `renderQuests()`. Raising the Great Hall
    in the City age = victory (`G.victory`). All gameplay-gated, no money/timers.
    NEXT pillars (see vision): building upgrade levels, wider economy (gold/market),
    stakes/defense (raids, walls, soldiers).

## VISION (user, 2026-06-13): aim for the depth Rise of Kingdoms / Rise of
Empires *advertise* — lots to build, research, and grow, a long progression
arc — but WITHOUT pay-to-play gates. Everything gated by gameplay only (time,
resources, planning), never by money/timers-you-pay-to-skip. Next work should
build toward meaningful progression systems (tech/ages, more buildings &
resources, population growth, maybe simple threats/quests) while keeping the
no-paywall, satisfying-loop ethos. See "Candidate next steps" below.

NOTE: temporary debug hooks used while iterating, all REMOVED before commit —
re-add if needed: `#gallery` hash (building grid), `window.__G=G` (state), and
`window.__look=(x,z,zoom)=>{...}` right after `updateCam()` (aim camera; the
`/tmp/look.js` harness drives it). Strict mode: functions the loop calls must be
declared at IIFE scope, NOT inside a `{}` block (block-scoped) — see `tickDuck`.

## How to develop/test in this environment (IMPORTANT)
The CDN (cdnjs) is **blocked behind a cert proxy** in the container, so a headless
browser can't load Three.js normally. The screenshot harness vendors Three locally
and injects it via request interception. To re-create it:
```
cd /tmp && npm init -y && npm i puppeteer three@0.128.0
npx puppeteer browsers install chrome
```
Then a puppeteer script: launch with
`--no-sandbox --use-gl=angle --use-angle=swiftshader --ignore-certificate-errors`,
intercept any request whose URL contains `three`+`.js` and `respond` with the
contents of `/tmp/node_modules/three/build/three.min.js`, `goto` the `file://`
path, click `#startBtn`, wait, `page.screenshot`. Read the PNG to view it.
Note: swiftshader renders at low FPS and the sim clamps `dt` to 0.05, so the game
runs in **slow motion** in captures — time-based checks need long waits.
For state debugging, temporarily add `try{window.__G=G;}catch(e){}` after the `G={}`
definition, read via `page.evaluate`, then remove it before committing.

## Code map (`index.html`, ~1080 lines, all in one IIFE)
- Terrain: `getH`, vertex-colored `PlaneGeometry`. Regions: `FOREST/ROCKY/POND`.
- Materials are **color-managed**: use `wM(hex)` / `bM(hex)` (convert sRGB→linear)
  for any new material, or colors render pale.
- Buildings: `*Mesh()` factories + `MESH{}` map; `keepMesh` is the hero model.
- Settlers: `makeSettler` (has `rod`, `load`, `ring` props in userData).
- Sim: `tickVillager` state machine (phases: move/toNode/gather/toDepot/deposit/
  toSite/build/toPrey/toFish/fishing/idle). Animals: `tickDeer`, `tickCritter`.
- Particles: `spawnChips`/`updateChips`, smoke `addSmoke`/`updateSmoke`, `floatGain`.
- Input: `handleTap` (later wrapped for keep-recruit). Build flow: `enterBuild`/
  `confirmBuild`. Jobs menu sets standing orders via `setOrder`.

## Candidate next steps (pick up here)
- Depletable/replenishing **fish shoals** in the pond (so fishing has a resource,
  not infinite) — mirror the node system.
- **Golden-hour lighting** option / longer shadows / subtle day cycle.
- Match the new keep's quality: **nicer houses, farms, storehouse, great hall**.
- Bigger/juicier gather feedback ("+1" on every swing, chunkier chips).
- Sheep/cattle decor near the keep; market stall; worn paths between keep & forest.

## Constraints / guardrails
- Don't break gameplay: keep edits visual/additive; the sim logic is solid.
- Mobile perf: prefer `InstancedMesh` for dense scatter (one draw call).
- Verify renders show `NO_JS_ERRORS` before committing.
