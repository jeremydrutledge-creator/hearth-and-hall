# Art assets guide (free CC0 + Mixamo route)

Goal: replace the procedural (code-built) meshes with real textured 3D models to
push the look toward Age of Empires Mobile — using only **web-safe, free** art.

The game already has a loader scaffold (`MODELS` / `getMesh()` in `index.html`).
While `MODELS` is empty it uses the built-in meshes, so nothing breaks. As soon as
you add files to `/assets` and list them, they appear in-game.

---

## The one hard licensing rule

A web game sends every asset to the browser, where anyone can download it. So we
can ONLY use licenses that allow that:

- ✅ **CC0** (public domain) — Kenney, Quaternius, Poly Pizza CC0 items
- ✅ **Mixamo** (Adobe, free account) — fine to use in your project
- ❌ Most **paid** packs (incl. Synty) — their license restricts assets being
  extractable/redistributable, which a public web build can't guarantee. Avoid.

When in doubt, the asset page must say **CC0 / public domain / "use anywhere incl.
commercial, no attribution required."**

---

## Where to get it (all free)

### Buildings & props
- **Kenney.nl** → "Castle Kit", "Medieval Town", "Fantasy Town Kit", "Nature Kit".
  CC0. Download includes GLTF/GLB (and OBJ/FBX). https://kenney.nl/assets
- **Quaternius** → "Medieval Village", "Modular buildings", "Survival" packs. CC0,
  GLB. https://quaternius.com

### Villagers / characters (animated)
- **Quaternius "Ultimate Animated Character" / "RPG Characters"** — CC0, **GLB with
  built-in walk/idle/etc. animations**. Easiest path (no conversion). ← recommended
- **Mixamo** (optional, for more animations) — pick a character, add animations
  (Idle, Walk, Axe Chop, Mining, Carry). Export **FBX**, then convert to GLB (see
  below). https://mixamo.com

### Nature (trees / rocks / bushes)
- **Kenney "Nature Kit"** or **Quaternius "Stylized Nature"** — CC0, GLB.

---

## Format: the game wants **.glb**

- Kenney/Quaternius usually offer **GLTF/GLB** directly → use those.
- If you only have FBX/OBJ (e.g. Mixamo), convert to GLB:
  - Easiest: import into **Blender** (free) and `File ▸ Export ▸ glTF 2.0 (.glb)`.
  - Or an online converter (e.g. products that convert FBX→GLB). Verify the result
    opens in https://gltf-viewer.donmccurdy.com before committing.

---

## What to add to the repo

1. Create a folder **`/assets`** at the repo root.
2. Put GLB files in it, named to match the building types, e.g.:
   ```
   assets/keep.glb  assets/house.glb  assets/storehouse.glb  assets/farm.glb
   assets/coop.glb  assets/pen.glb    assets/lumber.glb       assets/quarry.glb
   assets/hall.glb  assets/villager.glb
   ```
3. In `index.html`, uncomment/extend the `MODELS` map (search "optional glTF asset
   layer"):
   ```js
   const MODELS={
     house:'assets/house.glb',
     hall:'assets/hall.glb',
     // ...one line per model you've added
   };
   ```
4. Commit + push. GitHub Pages serves the files; they load at runtime.

Buildings you don't list keep using the nice procedural versions — so you can
migrate one at a time.

---

## Per-model fitting

Every pack uses different scales/orientations. After adding a model, tune it once
in `MODEL_XF` (same file):
```js
const MODEL_XF={
  house:{scale:1.0, y:0, ry:0},   // scale up/down, lift off ground, rotate (radians)
};
```
Tell me the model and I'll dial in the numbers with you (the footprint should
roughly match the build patch / collision radius).

---

## What I'll do once assets are in the repo

- Wire building GLBs through the existing build/placement flow (already routed via
  `getMesh()`), fit scales, hook them to our lighting + shadows.
- Integrate the **animated villager** (skeletal `AnimationMixer`): map game states
  → clips (idle / walk / chop / mine / carry / build), replacing the procedural
  settler. This is the bigger piece and needs the real rigged GLB to wire up.
- Add instancing/LOD where needed for mobile performance.

## Honest expectations

- Result: **clearly inspired by** AoE Mobile, cohesive and a big jump — not an
  exact match (that needs a pro art team / commissioned art).
- I integrate somewhat **blind** in this dev sandbox (it can't fetch your assets),
  so we'll iterate scale/look on your device after each drop-in.
- Pick assets from **one or two families** (e.g. all-Kenney or all-Quaternius) for
  visual cohesion rather than mixing many sources.
