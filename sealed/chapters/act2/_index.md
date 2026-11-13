# Act II · Protect and Uncover · Chapter Index and Shared Rules (SEALED — DM ONLY)

> **Act II** runs **Ch7 to Ch13**, levels **7 → 14**, about **14 sessions** (S9–S22), Midsummer to Lantern Night, YF 1104 (`campaign/01`).
> **Read this file first.** It holds the rules every Act II chapter uses: the Hushed template as applied, waking, the skill-challenge chain format, the Hart round, the locket token, the counter log and the tuning summary.
> Anything here that adds to or interprets a shared file is listed in `_change-requests.md` for the owners of those files to confirm. **Nothing here overrides `world/`, `campaign/`, `truth/` or `rules/`.** If one of those changes, it wins.

---

## 1. Chapter list

| File | Chapter | Level (during → exit) | Sessions | When | Where | SEAL in → out | Fights | Skill challenges |
|---|---|---|---|---|---|---|---|---|
| `ch07.md` | Hiding a Song | 7 → 8 | 2 | Midsummer–Haymonth | Willow Lane | 4 → 4 | F7 | SC 7-A, SC 7-B |
| `ch08.md` | Driftmarket | 8 → 9 | 2 | Haymonth | The Tamber, the Glasswater, Driftmarket | 4 → 5 | F8, F9, F10 | **SC#3**, SC 8-A |
| `ch09.md` | The Purse and the Vault | 9 → 10 | 2 | Harvest | Tollhaven; Saffra (a few hours) | 5 → 5 | F11, F12 | SC 9-A, SC 9-B |
| `ch10.md` | Bearback | 10 → 11 | 2 | Harvest–Leaffall | Copperhill, Wolfsgate, Bearback Pass, Dun Morrach | 5 → 5 | F13 (contest), F14, F15 | SC 10-A, SC 10-B |
| `ch11.md` | The Same Tune | 11 → 12 | 2 | Leaffall | Emberford | 5 → 5 | F16 | SC 11-A, SC 11-B, SC 11-C |
| `ch12.md` | The Kessel Workings | 12 → 13 | 2 | Frostcome | Kesselby, the Kessel Workings | 5 → 4 | F17, F18, **F19 (boss)** | SC 12-A, SC 12-B |
| `ch13.md` | Lantern Night | 13 → 14 | 2 | Last night of Lantern | All of Emberford | 4 → 4 (range 4–7) | F20, **F21 (boss)** | **SC#4**, SC 13-A, SC 13-B, SC 13-C |

**Every chapter file has:** at-a-glance, threads coming in, ★ beats with ≥3 routes each (copied from `campaign/02` and expanded), scenes, an NPC appearances table (NPC-### and the R-### edges each scene relies on), encounters in the `rules/02` §4 phase template with HP and damage math shown, full stat blocks in the `rules/02` §5 template, skill challenges as chains, a side-activity window, treasure (gold and items priced to `rules/03`), seeds, SEAL and events, the level milestone, "if the party goes off-route," and threads for the next chapter.

## 2. Act II at a glance (what has to be true at the end)
- Lark is safe on the Drift (Ch8), and the bond has become a liability (the Heron listens along it; then hunts Clara).
- Ash can open gates (Ch9). Gideon is the Bear's chosen (Ch10). The dwarves have broken their oath (SEC-05 proven).
- Clara knows who she is, in some measure (Ch11), and the twins have sung together, or not (Ch12).
- Hollis's order is found (Ch12). Zeke's hero has fallen.
- Lantern Night is survived; the Reserve is broken or not; Hester dies or is saved at a price; Hollis is killed, captured, reached or escaped (Ch13).

---

## 3. Shared rules for Act II

### 3.1 The Hushed template, as applied here
From `world/05` and `world/_handoff-notes.md`: **immune to Charmed and Frightened, resistant to psychic, vulnerable to thunder, −2 initiative, never flee.** Every Act II block tagged **Hushed** has these built in (initiative values already include the −2). Act II sorts them into three kinds, stated in each block:

| Kind | Who | Can be… |
|---|---|---|
| **Recent** | Hushed within the last year or so: conscripts, miners, Calm devotees' victims, Mabry's watchmen, Rook (fall branch) | **Woken** by Ash's song this act (see 3.2) |
| **Deep** | Hushed by long years or by the Stillness's own touch: Moth-of-the-Long-Dusk, the Varga Crab, Walt Finch | **Stirred** by Ash alone; **woken** only by the twins' duet (from Ch12) or by Ash after Ch15's discovery |
| **Hushed dead** | The Gate War dead (Thurvig, Shieldbearers, Revenants, the Ford-Knight, Old Ford's dead, Stillwracks) | **Laid to rest** (at 0 HP, or by the listed song/rest-words), never woken. Treated as Undead for spells. |

**Gideon's discovery (Ch12):** from S12.6 on, he always knows which kind a Hushed creature is.

### 3.2 Waking and stirring (Ash's song) in Act II
- **Action:** Ash hums the tune at a Hushed creature within 30 ft that can hear him.
- **Check:** **Performance**, DC **17 at L7–10**, DC **19 at L11–13** (`rules/02`, tuning handoff: 15 / 17 / 19 / 21 by tier). If Ash gained Performance proficiency at Ch9 (CHG-A2-03), add it.
- **Help:** Bart's Help; a Luck Point; Lark humming with him (advantage; her greying advances a stage if she's tired); the whole locket (once per long rest, advantage: 3.5); Gideon pointing out which one is recent (Ch12+: advantage on the first attempt in a fight).
- **On a success:** a **recent** Hushed creature **wakes** (it drops out of the fight: frightened, confused, often helpful). A **deep** Hushed creature or a **Hushed dead** is **stirred**: it loses its next action (or its reaction and next legendary action, for a boss) and stares at something only it can see.
- **The duet (Ch12+):** when Ash and Clara sing together (SC 12-B, SC 13-B), every *recent* Hushed creature in earshot wakes when the gate closes or the Reserve breaks, and the twins together can wake a *deep* Hushed person in a quiet scene with no roll (that's how Walt wakes: EVT-50).
- **Mercy:** waking or sparing instead of killing is the hopeful mechanic. Score Mercy per `campaign/04` (Ch7 Rook, Ch12 miners, Ch13 Hollis); don't moralize at the table.
- *This is an interpretation of CHG-01's "wake Hushed one at a time (from Ch15)" that keeps Act I's wakings (Borra, the Kessel miners) and the tuning notes' DCs consistent. Logged as CHG-A2-06 for confirmation.*

### 3.3 Skill challenges as chains
Every Act II skill challenge is a **chain of quick links**: one decision under pressure each, resolved by one roll *or* a smart plan that skips the roll.
- **Links** list two or three ways through (skills, spells, an ally, a clever idea). The player picks who takes each link.
- **Pressure** goes up on a failure. Each chain says exactly what each Pressure point costs. **Pressure never ends the story;** it changes what's waiting next (fail-forward).
- **Campaign skill challenges** (#3 in Ch8, #4 in Ch13) keep their `campaign/02` structure (successes before failures) and are run as chains of stations or districts.
- **Reliable Talent (Ash, L7+):** with expertise and Reliable Talent, Ash can't fail most Stealth, Perception, Sleight of Hand or Deception/Persuasion checks at these DCs. That's fine. Every chain is built so **one character can't cover every link**: there are always more links than Ash can take, or links that need other skills.
- **DCs by level (Act II):** L7–10: easy 13, standard 15, hard 17, very hard 19. L11–13: standard 17, hard 19, very hard 21.

### 3.4 The Hart round (Moss's story upgrade #2)
`campaign/05` §7: **once per tier**, Moss can take his true form **for one round as a narrative action.** In Act II that means **one round in Ch7–10 (tier 2)** and **one round in Ch11–13 (tier 3)**. The Ch6 shore transformation is the story beat that *grants* the upgrade; it doesn't spend the tier 2 round (CHG-A2-07). **Ch13's "holds the Hall with roots" moment is a free, scripted story beat** and doesn't spend the tier 3 round. If Ch6's escape failed, upgrade #2 is delayed until Ch10 (no tier 2 round).

**The Hart (one round).** On Moss's turn, as a narrative action, he becomes the Hart (a stag nearly twelve feet at the shoulder, antlers of living moss and white flowers) until the start of his next turn. Choose **one**:
- ***Carry.*** Up to six willing allies within 10 ft climb on or hold on; he moves up to 80 ft, and none of them provoke opportunity attacks.
- ***Break the Line.*** He charges up to 60 ft in a straight line through enemies. Each creature in the line makes a **DC 18 Strength save** (DC 19 in tier 3): on a failure, 6d10 bludgeoning and knocked prone; on a success, half and pushed aside.
- ***Stand.*** Every enemy within 60 ft that can see him has disadvantage on attacks against anyone but him until his next turn, and he has 100 temporary HP (150 in tier 3) for the round.
- ***Bloom.*** Moss and white flowers spread 30 ft around him: allies there regain 4d10 HP (6d10 in tier 3), and greywilt terrain there ends.
(Moss's druid stat block is unchanged otherwise. The full Hart stat block for upgrade #4 belongs to Ch16.)

### 3.5 The locket token (SEC-23, Ch12+)
From `campaign/03` SEC-23's rules note. Once the two halves have clicked shut (Ch11 route E, or later):
- While the locket is whole and both twins are within 1 mile, each knows the other's direction and whether he or she is in pain.
- **Once per long rest,** the twin holding it gains **advantage on one check to wake a Hushed creature or to open or close a Wellgate.**
- Plain pewter: not glimmer, no attunement, can't be dispelled, survives Ending 1.
- In Ch12–13 it applies to SC 12-B, SC 13-B and waking checks.

### 3.6 Story upgrades and discovery moments placed in Act II

| Who | Moment | Chapter |
|---|---|---|
| Moss | Sparrows as early warning (no ambush on the Lane) | Ch7 S7.1 |
| Lark | Quiets the water (once per long rest) | Ch7 Fight 7 |
| Zeke | Maps the silence (advantage at SC#3's still patch) | Ch8 S8.3 |
| Gideon | His aura holds back greywilt (creatures in it ignore still-water effects) | Ch8 S8.9 |
| Zeke | Reads the astrolabe (Midsummer's Eve alignment; "the keyhole") | Ch9 S9.2 |
| Ash | Opens a gate alone (EVT-16); Performance proficiency offered (CHG-A2-03) | Ch9 SC 9-B |
| Gideon | Ursk's mark ("Hearth-Warden"); *Bear's Ward* boon (CHG-A2-04) | Ch10 S10.6 |
| Moss | Upgrade #3: *Commune with Nature* and *Speak with Plants* at will; antler shadow | Ch10 S10.6 |
| Clara / Ash | She lights a lamp across the river; he hears her like a second rope | Ch11 S11.4 |
| Gideon | Knows which Hushed can be woken | Ch12 S12.6 |
| Ash & Clara | The first duet | Ch12 SC 12-B |
| Ash | Hears every lamp in the city as one song | Ch13 S13.2 |
| Zeke | Unweaves the city's lamp-chain | Ch13 SC#4 (Islands) |
| Moss | Holds the Hall with roots (free story beat) | Ch13 Fight 20 |
| Clara | Sings the Reserve apart | Ch13 SC 13-B |

---

## 4. Tuning summary (from `rules/02` §3)

| Lvl | Party DPR | Ordinary HP / DPR | Significant HP / DPR | Boss HP (cap) / DPR | AC | Atk | DC | Boss saves |
|---|---|---|---|---|---|---|---|---|
| 7 | 71 | 200 / 34 | 320 / 41 | 500 (640) / 34–51 | 15–17 | +6–8 | 14–15 | +6–7 |
| 8 | 74 | 205 / 39 | 335 / 47 | 520 (670) / 39–58 | 15–17 | +6–8 | 14–15 | +6–7 |
| 9 | 91 | 255 / 44 | 410 / 52 | 640 (820) / 44–65 | 15–17 | +6–8 | 14–15 | +6–7 |
| 10 | 91 | 255 / 48 | 410 / 58 | 640 (820) / 48–72 | 15–17 | +6–8 | 14–15 | +6–7 |
| 11 | 109 | 305 / 53 | 490 / 63 | 760 (980) / 53–79 | 17–18 | +9–11 | 16–17 | +7–9 |
| 12 | 115 | 320 / 58 | 520 / 69 | 800 (1,040) / 58–86 | 17–18 | +9–11 | 16–17 | +7–9 |
| 13 | 124 | 345 / 62 | 560 / 75 | 870 (1,120) / 62–93 | 17–18 | +9–11 | 16–17 | +7–9 |

### Fight roster (Act II)

| Fight | Ch | Type | Lvl | Enemy HP (target) | Enemy DPR (target) | Expected rounds | Phases |
|---|---|---|---|---|---|---|---|
| 7 · The Siege of Willow Lane | 7 | Significant | 7 | 384 raw → ~294 effective (320) | ~41, spike ~50 (41) | 6 | 3 (roofs → still Bend → get her to the water) |
| 8 · The Toll-Cutter | 8 | Ordinary | 8 | 204 (205) | ~39 (39) | 3–4 | twist at round 3 (ram) |
| 9 · The Drift-Gate Raid | 8 | Significant | 8 | 335 (335) | ~47 (47) | 5–6 | 3 (up from the Eye → lashings part → the last boat) |
| 10 · The Storm's Beats | 8 | 3 short beats in SC#3 | 8 | ~70 each (205 ÷ 3) | ~13 each | 1–2 each | — |
| 11 · Chandeliers and Balconies | 9 | Ordinary (upper) | 9 | 255 (255) | ~44 (44) | 3–4 | twist at round 3 (the grate) |
| 12 · The Varga Vault | 9 | Significant | 9 | 409 (410) | ~52 (52) | 6 | 3 (the crab → flood → the key note) |
| 13 · The Copperhill Bout | 10 | Contest | 10 | — | — | 3 | — |
| 14 · The Switchbacks | 10 | Significant | 10 | 420 raw → ~330 with parley (410) | ~58 (58) | 5–6 | 3 (up the road → rockslide → snow-bridge/parley) |
| 15 · The Gate-Breaker | 10 | Significant | 10 | 410 → ~375 effective (410) | ~54–58 (58) | 6 | 3 (desecration → the Bear answers → seal the shaft) |
| 16 · The Lamp-Climb Attack | 11 | Significant | 11 | 500 (490) | ~60–63 (63) | 6 | 3 (crush → pole falls → into the river) |
| 17 · The Garrison | 12 | Ordinary | 12 | 318 (320) | ~59 (58) | 3–4 | counter shift at round 3 |
| 18 · The Old Shaft | 12 | Significant | 12 | 525 (520) | ~67–70 (69) | 5–6 | 3 (quiet workers → the stone remembers → hold the shaft) |
| **19 · Lucan Hask** | 12 | **Boss** | 12 | 810 (800; cap 1,040) | 56–58 / spike 86 (58 / 86) | ~10 | 3 (chamber → overload → the gate opens) |
| 20 · Old Ford's Dead | 13 | Ordinary (in SC#4) | 13 | 345 (345) | ~60 (62) | 3–4 | terrain drop at round 3 |
| **21 · The Reserve's Warden** | 13 | **Boss** | 13 | 870 (+Rebuild headroom; cap 1,120) | 62–65 / spike 93 (62 / 93) | 10–12 | 3 (wakes → floods with light → rebuild/unmake) |

### Boss checklist (`rules/02` §5)

| | Hask (F19) | Reserve's Warden (F21) |
|---|---|---|
| Legendary Resistance 3 (4 in lair) | ✔ 4 (the gate chamber is his lair) | ✔ 4 (the Reserve chamber) |
| Legendary actions 3 (4 in lair), with movement | ✔ Lamp-Step (teleport), Glaive Sweep, Order the Guard, Flare, Bring Me the Child | ✔ Stride/Glide, Slam, Hum, Guard the Console |
| Lair actions | ✔ Glimmer Flare, Greywilt Wave, Collapse, Counter-Hum | ✔ Radiant Flare, Greywilt Wave, the Floor Breaks, Pull of the Reserve |
| Guards / counters for priority targets | ✔ Hushed Lamp-Wardens (Interpose); Glimmer Shell | ✔ Guardian Lattice (protects Hollis); Hushed Lamp-Wardens; enchanters (Re-Tune, Counterspell) |
| A weak save among Dex/Con/Wis | ✔ Dex +4, Wis +5 | ✔ Dex +3, Wis +4 |
| Best saves in the tier band (+7–9) | ✔ Str/Con +9 | ✔ Str/Con +9 |
| Two or more phase changes, different types | ✔ FORM+TERRAIN (overload) → OBJECTIVE (the gate) | ✔ FORM+TERRAIN (light) → OBJECTIVE (rebuild/unmake) |
| A hope lever | ✔ Stir him; the duet wakes his guards; he can surrender when the gate closes | ✔ Rook (fall branch) wakeable; the wardens wake when the Reserve breaks; reach Hollis |

### Counter log (`rules/02` §6: one per phase, telegraphed, never the same move two fights in a row)

| Fight | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| 7 | Ash's Hide (lanterns, flare) | Bart's Help (Moth swats him) | — (objective) |
| 8 | Zeke's area spells (spread out) | — | — |
| 9 | — | Gideon's Protection (the current pulls allies away) | Moss's beast form (the pike swallows) |
| 10 | Healing yo-yo (drag to the still patch) | — | — |
| 11 | Ash's flanking Sneak Attack (Watchful duelist; back-to-back guards) | — | — |
| 12 | Zeke's spells (ward-lantern) | — | Gideon's Initiative Swap (reinforcements on count 10) |
| 13 | — (contest) | — | — |
| 14 | Zeke's Shield (volleys, saves) | Ash's Hide (the war-dog) | — |
| 15 | Moss's beast form (big hits, grip) | — (the echo helps the party) | — |
| 16 | Bart's Help (crossbow at the bird) | Gideon's Protection (ranged knives ignore him) | — |
| 17 | Zeke's area spells (spread out) | Ash's Hide (all lamps flared) | — |
| 18 | Healing yo-yo (the dead keep the downed) | — | — |
| 19 | Gideon's smites (Glimmer Shell) | Ash's Hide (no dim light) | Gideon's Initiative Swap (Gate-Hushed on count 10) |
| 20 | Moss's beast form (pinned by the dead) | — | — |
| 21 | Zeke's Forcecage-type spells (Abandon Shell) | Bart's Help (the pulse catches small flyers) | Healing yo-yo (the floor takes the downed) |

---

## 5. NPCs introduced in Act II (provisional IDs)

> The Truth File's next free ID was NPC-080. Other chapter writers may be using that range at the same time, so Act II uses a **provisional block, NPC-140 to NPC-159**, to avoid collisions. `_change-requests.md` (CHG-A2-02) asks the Truth File's owner to confirm or renumber. Names were checked against the banned list in `world/04`.

| ID (prov.) | Name (alternate spellings) | Who | Chapters |
|---|---|---|---|
| NPC-140 | **Lady Honoria Merrow** (Honora, Merow) | Head of the House of Merrow, Tollhaven; Calm | 9, (13) |
| NPC-141 | **Valentine Crewe** (Val, Crew) | The Calm-hired duelist (Ch9's unnamed role) | 9 |
| NPC-142 | **Percival Hume** (Percy, Hewm) | Smooth young Tollhaven broker; the party's rival there | 9, (11) |
| NPC-143 | **Master Otto Varga** (Varga, Vargas) | Head of the House of Varga | 9 |
| NPC-144 | **Coble Tull** (Cobble) | Granny Tull's grandson; messenger | 8, 9, 11 |
| NPC-145 | **Merrilee** (Merrily) | Otter-folk refugee elder | 8 |
| NPC-146 | **Dughal Brokenhorn** (Dugal, Dougal) | Minotaur raid-captain | 8 |
| NPC-147 | **Purser Edwin Lusk** (Ed, Lusck) | Merrow-paid toll-boat purser | 8 |
| NPC-148 | **Gert Volker** (Gerd) | Mercenary who wants Copperhill's Seat | 10 |
| NPC-149 | **Sergeant-Mage Ilse Brandt** (Ilsa) | Grey Wolf battle-mage | 10 |
| NPC-150 | **Thurvig the Gate-Breaker** (Thurvik) | Hushed frost giant of the Gate War (dead) | 10 |
| NPC-151 | **Dob Harrow** (Dobbin) | Leader of the Quiet Knives (hired killers) | 11 |
| NPC-152 | **Lieutenant Corbin Wade** (Corbyn) | Lamp-warden lieutenant at Kessel; not Calm | 12 |
| NPC-153 | **Sal Pickett** (Sally) | Keeper of the Pick and Lantern, Kesselby | 12 |
| NPC-154 | **Senior Enchanter Ivo Pryce** (Price) | Calm inner circle (FAC-02's "two senior enchanters") | 13 |
| NPC-155 | **Senior Enchanter Adela Holt** (Adella) | Calm inner circle | 13 |
| NPC-156 | **Warden-Sergeant Bryony Nash** (Briony) | Lamp-warden sergeant who leads the Calm crew's muscle | 7 |
| NPC-157 | **Skipper Ottilie Bask** (Ottily) | River-clan barge skipper of the *Dun Heifer* | 8 |
| NPC-158 | **Archivist Sigrun Deeplore** | Dun Morrach's archivist | 10 |
| NPC-159 | **Plish** | Otter-folk refugee freed from the Bucket (optional) | 7, 8 |

Tier 3 names used at the table level (log in `truth/07` if they get play): Abel Penny (Lamp House clerk), the six Mothers of Driftmarket besides Granny Tull (Ma Kettering, Old Saltash, Mother Reed, Dace Corran, Mother Fennimore, Hettie Brine-no-relation), Brock Underhill (badger-folk sett-elder), Lettice Grey (a Purse heir; a `world/04` example name), Gristle (the Wolves' war-dog), Annie (Mabry's late wife), Orm Coalbeard (a clan head), Davey Pickett.

---

## 6. Stat-block index (Act II)

| Block | File | Role / CR |
|---|---|---|
| Calm Knife | ch07 | skirmisher, CR 3 |
| Warden-Sergeant Bryony Nash | ch07 | controller, CR 4 |
| Rook (Magpie leader) | ch07 | rival skirmisher, CR 3 |
| Moth-of-the-Long-Dusk | ch07 | Hushed hunter, CR 7 |
| Hushed Host Hunter | ch07 | Hushed brute, CR 3 |
| Host Outrider | ch07 | artillery, CR 2 |
| Purser Edwin Lusk | ch08 | controller, CR 3 |
| Toll Bravo | ch08 | skirmisher, CR 2 |
| Horned Host Raider | ch08 | brute, CR 3 |
| Raid-Captain Dughal Brokenhorn | ch08 | leader/brute, CR 6 |
| Hushed Rennet Pike | ch08 | Hushed water brute, CR 5 |
| Stillwrack | ch08 | Hushed dead grappler, CR 2 |
| Merrow House Guard | ch09 | guard, CR 2 |
| Valentine Crewe | ch09 | duelist, CR 6 |
| The Varga Crab | ch09 | Hushed brute/guard, CR 8 |
| Lamp-Warden (L9) | ch09 | line infantry, CR 3 |
| Lamp-Warden Spellward | ch09 | anti-caster, CR 5 |
| Hilde Strand | ch10 | champion (contest), CR 9 |
| Grey Wolf Veteran | ch10 | line infantry, CR 3 |
| Grey Wolf Crossbow | ch10 | artillery, CR 2 |
| Sergeant-Mage Ilse Brandt | ch10 | counter-caster, CR 5 |
| Captain-General Ulric Fane | ch10 | leader, CR 8 |
| Thurvig the Gate-Breaker | ch10 | Hushed dead giant, CR 11 |
| Gate War Shieldbearer | ch10 | Hushed dead guard, CR 5 |
| Ursk's Echo | ch10 | ally effect |
| Sgt. Giles Mabry | ch11 | leader, CR 8 |
| Quiet Knife | ch11 | assassin, CR 7 |
| Dob Harrow | ch11 | assassin leader, CR 8 |
| Hushed Watchman | ch11 | Hushed guard, CR 4 |
| Lt. Corbin Wade | ch12 | leader, CR 8 |
| Glimmer-Warden (L12) | ch12 | line infantry, CR 5 |
| Hushed Miner | ch12 | Hushed blocker, CR 3 |
| Gate War Revenant | ch12 | Hushed dead keeper, CR 8 |
| **Lucan Hask** | ch12 | **boss**, CR 16 |
| Hushed Lamp-Warden (Hask's guard) | ch12 | Hushed guard, CR 5 |
| Gate-Hushed | ch12 | Hushed swarm, CR 3 |
| The Drowned Ford-Knight | ch13 | Hushed dead leader, CR 10 |
| Old Ford Dead | ch13 | Hushed dead blocker, CR 4 |
| **The Reserve's Warden** | ch13 | **boss**, CR 18 |
| Hushed Lamp-Warden (L13) | ch13 | Hushed guard, CR 4 |
| Calm Senior Enchanter | ch13 | artillery / anti-unweaver, CR 6 |
| Hollis Grane (noncombatant) | ch13 | — |
| The Hart (one round) | `_index.md` §3.4 | narrative action |

**Count:** 40 creature stat blocks, plus the Ursk's Echo ally effect, Hollis's noncombatant line and the Hart's one-round action.

---

## 7. Treasure by chapter (priced to `rules/03`: Common 100 · Uncommon 400 · Rare 4,000 · Very Rare 40,000; consumables half; weapons and armor add the base item)

| Ch | Coin (about) | Permanent magic items | Consumables |
|---|---|---|---|
| 7 | 275–400 gp | Glimmer-lance (+1 spear, Uncommon; glimmer) | 2 Greater Healing, Charm of the Rennet, Sleep-Dust Sack |
| 8 | 1,100 gp | Stone of Good Luck (Uncommon), Pearl of Power (Uncommon), Dughal's war-horn (Common) | 2 Greater Healing |
| 9 | 2,500–4,000 gp | Shield +1 (Uncommon), Lantern of Revealing (Uncommon), Clockwork Amulet (Common) | — |
| 10 | 1,000–2,000 gp | **Bearward** (+2 longsword, Rare, Gideon), **+2 shortsword** (Rare, Ash) | — |
| 11 | ~1,100 gp | Cloak of Displacement (Rare) | 4 Assassin's Blood |
| 12 | ~3,300 gp (+glimmer, a choice) | Lantern-Glaive (+2, Rare; glimmer), +1 Half Plate (Rare), Wand of the War Mage +2 (Rare), Staff of the Woodlands (Rare) | — |
| 13 | up to 5,850 gp | Wand of Binding (Rare), the Ford-Knight's sword (+2 longsword, Rare) | warden-scrolls |
| **Act II** | **~14,000–17,000 gp** | **5 Uncommon, 2 Common, 9 Rare** (two glimmer-cored; the glaive and the half plate are optional) | |

`rules/02` assumes Ash has a **+2 weapon by L11**: delivered at the end of Ch10 (Brynja's shortsword). Very Rare items start in Act III. Gifts from the Row are tracked separately (Campaign Bible gifts list): Lark's lamp, Gideon's Dry Cloak (Ch7); Zeke's never-blot pen (Ch9); Clara's moving-picture locket (Ch11); Moss's compass (Ch13).

---

## 8. Events, SEAL and tracks across Act II

| Ch | Events | SEAL (expected) | Tracks |
|---|---|---|---|
| 7 | EVT-10, 44, 45, 46, 11 (+55 optional) | 4 → 4 | Mercy (Rook; first waking); Twin Bond (the lamp) |
| 8 | EVT-12, 14 (+1), 13 | 4 → 5 | Mercy (−1 if a surrendered Dughal is killed) |
| 9 | EVT-15, 16 (+52 step) | 5 → 5 | — |
| 10 | EVT-17, 53 | 5 → 5 | — |
| 11 | EVT-51, 47, 48, 49, 52, 18 | 5 → 5 | **Twin Bond** (SC 11-C); Mercy (Rook) |
| 12 | EVT-19 (−1), 20, 50, 52 | 5 → 4 | Twin Bond (the duet); Mercy (the miners) |
| 13 | EVT-21, 22 (+1 or +3), 23 (−1), 24 | 4 → 4 (range 4–7) | Mercy and Twin Bond (Hollis's fate) |

---

## 9. Files in this folder
- `_index.md` (this file)
- `ch07.md` to `ch13.md`
- `_change-requests.md`: everything Act II needs from the shared files, as CHG-style notes for their owners.
