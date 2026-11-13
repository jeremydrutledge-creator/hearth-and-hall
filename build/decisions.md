# Build Decisions Log (safe for the player to read — preferences only, no plot)

## Tools
- Image generation: Gemini API called directly by script (key injected by environment proxy, never in files). Test 3 images first; hard image-count cap in script.
- Godot: skipped (player chose).
- Silas/Obsidian: never connected.
- Old Index.html prototype: deleted (player approved scrapping the repo).

## Build-time preferences (from interview)
- Devil's advocate: YES during building, NO during gameplay.
- Ash's age at start: 20. Gideon ~32, Zeke ~31.
- Ash's livelihood: odd jobs — courier runs, retrieval, minor bounty hunting, enters long-shot contests (some wins, some losses).
- Loss level: B — one or two important, set-up, meaningful deaths of loved NPCs over the whole campaign. Party members (Gideon, Zeke, Moss) die only by dice in play, never by script.
- Names: plain, easy English-style names for ordinary people; distinct sound per region for places and peoples. Always list alternate spellings.
- Character build: Ash built together with player, one choice at a time. Companions assigned by the builder.
- Ability scores: rolled 4d6-drop-lowest by player.

## Rolled ability scores (before background bonuses)
- Ash (player's own set): 17, 16, 14, 14, 13, 13 — assignment TBD with player.
- Gideon (Paladin): STR 17, CHA 16, CON 15, WIS 14, INT 13, DEX 12
- Zeke (Wizard): INT 17, CON 16, DEX 13, WIS 12, CHA 11, STR 8
- Moss (Circle of the Moon Druid): WIS 16, CON 16, DEX 15, STR 12, INT 12, CHA 12
- Party is well above standard-array power (modifier totals +12, +12, +7, +11 vs +5). Encounter tuning must use these actual numbers.
