# Build-Time Consistency Report (SEALED — DM ONLY)

> Fresh full report from the step-10 consistency pass. Supersedes the step-5 report. Fixes are logged as CHG-07 to CHG-18 in `08-change-log.md`.

## Results

| Check | Result | Notes |
|---|---|---|
| Every vouch scene backed by an edge | **PASS** | All six planned vouch scenes (Ch5, Ch6, Ch7, Ch10 and the two Hester vouches) cite edges that exist (R-026, R-040, R-052, R-068, R-208, and others). |
| Every belief change backed by an event | **PASS** (after fix) | 116 edges; every CHANGES ONLY VIA names an existing EVT. Three new edges changed on chapter beats; EVT-58, 59, 60 added (CHG-18). |
| Events ↔ edges agree both ways | **PASS** | 0 events cite a missing edge; 0 edges cite an event that doesn't list them back (links section added, CHG-11). |
| Every SEC has 2+ seeds before its reveal | **PASS** | SEC-01 to SEC-24; lowest are SEC-20 and SEC-21 at 2. SEC-03 now 9. SEC-24 (optional) has 5. |
| Every referenced ID exists (NPC, R, EVT, SEC, FAC, CHG, HIST) | **PASS** | Only "next free" and reserved-range mentions point at unused numbers (NPC-185/186 reserved; R-097–199 and R-209–229 unused). Defined: 187 NPC IDs, 116 edges, 60 events, 24 secrets, 18 factions, 6 historical figures. |
| No duplicate IDs | **PASS** | Provisional blocks made permanent with no overlaps (CHG-10). |
| Forbidden content (demons, devils, hells, fae courts) | **PASS** | 32 keyword hits across the repo, every one a prohibition or a "not a demon" ruling. None in play content. |
| No reused Shackled City names | **PASS** (after fix) | Exact banned names appear only in the ban lists. Near-misses fixed: Mirra → Zuri, Percival → Julian (CHG-07). Judged acceptable (different first sound, ordinary names): Nell, Fell, Kell, Billy, Gilly, Tilly, Hatch. |
| Duplicate or confusing first names | **PASS** (after fix) | Five renames to stop two characters sharing a first name or surname (CHG-10, CHG-17). Sound-alike traps added to the name lookup. |
| Female major allies: no romance | **PASS** (after fix) | One designed joke on the Row implied romance between Ash and his secret twin; replaced with a twin-resemblance joke (CHG-17). Remaining hits are explicit "never romantic" notes or a comic peck from a ninety-year-old. |
| Level milestones consistent | **PASS** | Arc overview, DM spine and all 20 chapter files agree: chapter N is played at level N and ends at level N+1; Ch20 ends the campaign. |
| Festival calendar consistent | **PASS** (after fix) | Ford Festival moved to 1 Leaffall everywhere (CHG-09). Highmarch's extra Blossom tourney noted (CHG-14). |
| Art paths consistent | **PASS** (after fix) | Packet, truth PORTRAIT lines and the city art list now match; unmet characters' art lives in `/sealed/art/` so file names can't spoil (CHG-17). One consolidated list: `sealed/art-manifest.md`. |
| Player-facing spoiler audit (`player/`, `play-kit/`) | **PASS** | Grepped every sealed key term; only surface details already in the leak-check's accepted list appear (the locket crest, the Glass, still lakes). The session-one opener delivers the tune and the grey-water dream as the leak check required. |
| Change requests resolved | **PASS** | All requests in the four `_change-requests.md` files and the open handoff items are applied or ruled on (CHG-07 to CHG-18). |

## Open items (not failures)
- **Treasure** was summed (about 48,000–60,000 gp; about 38 permanent items) but **not** checked against the 2024 DMG's treasure guidance, which wasn't available to verify (`rules/03`).
- **Art manifest T3 descriptions** were drawn automatically from the city and chapter text. Tighten each one into a clean visual paragraph before generating it.
- **Showing images to the player** is still untested (`play-kit/project-instructions.md` §9).
