# Tuning Notes (SEALED — DM ONLY)

> Every fight in `/sealed/chapters/` is tuned from these numbers. They come from the **actual rolled party** (`build/decisions.md`, `01-party-builds.md`), not the standard array. This party is well above average: modifier totals of +12 / +12 / +7 / +11 against the standard array's +5.
> **Design intent (kickoff §6):** above standard from level 1, but survivable. Smart enemies. Fights that change every 3–4 rounds. Ordinary fights last 3–4 rounds, significant 5–6, bosses about 10 (up to 15 only if the fight keeps changing).

---

## 1. Party damage per round (DPR)

**Assumptions** (all estimates; re-check after play and log real numbers in the Sealed GM Notes):
- Baseline **65% hit chance** against an on-level AC (the AC column in §3).
- **Ash:** shortsword (Vex) plus off-hand dagger (Nick) every turn. On about **40% of rounds** his first attack has advantage, from Bart's Help, Vex carry-over or (from L3) Steady Aim. Sneak Attack lands if either attack hits. Dex 20 from L4. Magic weapon bonus assumed: +1 from L6, +2 from L11, +3 from L16.
- **Gideon:** longsword and shield (Str 20 from L4), Extra Attack at L5, Radiant Strikes +1d8 at L11. Divine Smite spending is amortized at roughly a third of his slots per adventuring day of about 3 fights.
- **Zeke:** a cantrip about 60–70% of rounds. Otherwise an area spell of his best slot level, hitting about 2.2 targets at about 75% effective (saves and misses).
- **Moss:** Shillelagh at L1. From L2–3, Wild Shape beasts at his Circle Forms CR (CR 1 at L3, rising to CR 6 at L18). From L5, a concentration spell ticking (Moonbeam or Conjure Animals) amortized in.

**Math, worked at three levels:**
- **L1, Ash:**
  - Shortsword: hit chance 0.65 with no advantage, 0.88 with it. Weighted 0.6×0.65 + 0.4×0.88 = 0.74. Expected damage 0.74 × 7.5 = 5.5.
  - Dagger: 0.65 × 2.5 = 1.6.
  - Sneak Attack: chance at least one attack hits = 1 − (0.26 × 0.35) = 0.91. Expected 0.91 × 3.5 = 3.2.
  - **Total about 10.**
- **L5, Gideon:**
  - Two attacks at 0.65 × (4.5 + 5) = 6.2 each, so 12.4.
  - Smite: about 0.33 per round × 2d8 (9) × 0.95 = 2.9. Rounding brings the total to **about 17**.
- **L11, Ash:**
  - Shortsword: 0.74 × (3.5 + 5 + 2) = 7.8.
  - Dagger: 0.65 × (2.5 + 2) = 2.9.
  - Sneak Attack: 0.91 × 6d6 (21) = 19.1. Rounding brings the total to **about 30**.

| Lvl | Ash | Gideon | Zeke | Moss | **Party DPR** |
|---|---|---|---|---|---|
| 1 | 10 | 6 | 7 | 6 | **28** |
| 2 | 10 | 7 | 7 | 5 | **29** |
| 3 | 14 | 8 | 7 | 8 | **37** |
| 4 | 14 | 8 | 7 | 8 | **38** |
| 5 | 17 | 17 | 13 | 12 | **59** |
| 6 | 19 | 18 | 13 | 14 | **64** |
| 7 | 22 | 19 | 16 | 14 | **71** |
| 8 | 22 | 19 | 16 | 17 | **74** |
| 9 | 25 | 22 | 23 | 21 | **91** |
| 10 | 25 | 22 | 23 | 21 | **91** |
| 11 | 30 | 31 | 27 | 21 | **109** |
| 12 | 30 | 31 | 27 | 27 | **115** |
| 13 | 33 | 35 | 30 | 27 | **124** |
| 14 | 33 | 35 | 30 | 27 | **124** |
| 15 | 36 | 37 | 32 | 29 | **134** |
| 16 | 38 | 38 | 32 | 33 | **140** |
| 17 | 41 | 40 | 36 | 33 | **150** |
| 18 | 41 | 40 | 36 | 35 | **152** |
| 19 | 44 | 42 | 36 | 35 | **157** |
| 20 | 44 | 42 | 36 | 39 | **161** |

**Nova warning:** a round where everything lines up (Bless, Ash with advantage and a crit, Zeke's best area spell, Gideon's two smites) can hit **2–2.5× DPR**. Bosses need a phase or form change, not one HP bar, so a single nova round can't skip a fight's story. At L17+, **Thief's Reflexes** gives Ash two turns in round 1. Add about 40 to round-1 damage in boss maths.

---

## 2. Party hit points and staying power

| Lvl | Ash HP | Gideon HP | Zeke HP | Moss HP (+wild shape temp) | Party HP | Effective (with healing) |
|---|---|---|---|---|---|---|
| 1 | 10 | 14 | 10 | 13 (+0) | 47 | ~60 |
| 2 | 17 | 24 | 18 | 23 (+2) | 82 | ~102 |
| 3 | 24 | 34 | 26 | 33 (+9) | 117 | ~149 |
| 4 | 31 | 44 | 34 | 43 (+12) | 152 | ~192 |
| 5 | 38 | 54 | 42 | 53 (+15) | 187 | ~247 |
| 6 | 45 | 64 | 50 | 63 (+18) | 222 | ~294 |
| 7 | 52 | 74 | 58 | 73 (+21) | 257 | ~341 |
| 8 | 59 | 84 | 66 | 83 (+24) | 292 | ~388 |
| 9 | 66 | 94 | 74 | 93 (+27) | 327 | ~435 |
| 10 | 73 | 104 | 82 | 103 (+30) | 362 | ~482 |
| 11 | 80 | 114 | 90 | 113 (+33) | 397 | ~529 |
| 12 | 87 | 124 | 98 | 123 (+36) | 432 | ~576 |
| 13 | 94 | 134 | 106 | 133 (+39) | 467 | ~623 |
| 14 | 101 | 144 | 114 | 143 (+42) | 502 | ~670 |
| 15 | 108 | 154 | 122 | 153 (+45) | 537 | ~717 |
| 16 | 115 | 164 | 130 | 163 (+48) | 572 | ~764 |
| 17 | 122 | 174 | 138 | 173 (+51) | 607 | ~811 |
| 18 | 129 | 184 | 146 | 183 (+54) | 642 | ~858 |
| 19 | 136 | 194 | 154 | 193 (+57) | 677 | ~905 |
| 20 | 143 | 204 | 162 | 203 (+60) | 712 | ~952 |

"Effective" adds Moss's wild-shape temporary HP (one use) plus a share of Lay on Hands and Moss's and Gideon's healing for a single fight. Moss's Resilient (Con) at L4 adds about 1 HP per level, which isn't included.

**Armor class (L1 → L20, with expected magic):** Gideon 18 → 21–22 · Ash 15 → 18–19 · Moss 16 (beast forms 13 + Wis = 17 → 18) · Zeke 11 (14 with Mage Armor, 19 with Shield) → 15–17 base.
**Squishy targets:** Zeke and Ash at L1–4. Bart has 1 HP.

**Survivability rules at L1–2 (kickoff: survivable at L1):**
- No single enemy attack routine should be able to drop Zeke or Ash **from full HP** in one turn at L1–2. Cap any single creature's max damage per turn at **9** (L1) or **14** (L2).
- Ordinary L1 fights may use **0.8×** the HP pool below if the party is already hurt.
- Enemies with non-lethal intent (the Tolleys' nets and clubs) should **knock out**, not kill.

---

## 3. Encounter targets by level

**How to read this:**
- **Total enemy HP** is the combined HP of everything on the enemy side.
  - Ordinary ≈ **2.8 × party DPR**: about 3–4 rounds, after waste, movement and misses.
  - Significant ≈ **4.5 × DPR**: about 5–6 rounds.
- **Boss HP** is the boss's own total across all phases ≈ **7 × DPR**, plus adds of about 2 × DPR. Legendary Resistance, phase changes and objective changes stretch that to about 10 rounds. The cap (9 × DPR) is only for a fight that changes form at least three times.
- **Enemy DPR** is the expected damage per round *after* misses, from all enemies together:
  - Ordinary ≈ 10% of the party's effective HP per round (about 30–35% over the fight)
  - Significant ≈ 12% (about 60%)
  - Boss ≈ 10% sustained, with **spike rounds at 15%** at phase changes. That totals about 80–100% over 10 rounds, offset by healing.
- **AC, Attack and Save DC** are the enemy-side targets, tuned about +1 above standard. **Boss best saves** are the boss's two or three best saving throws. Its weak saves should be 3–5 lower, so the party has something to find.

| Lvl | Party DPR | Ordinary: total enemy HP | Ordinary: enemy DPR | Significant: total HP | Significant: enemy DPR | Boss HP (all phases) | Boss + adds DPR (sustained / spike) | AC | Attack | Save DC | Boss best saves |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 28 | 80 | 6 | 125 | 7 | 200 (cap 250) | 6 / 9 | 13–15 | +4–+5 | 12–13 | +4–+5 |
| 2 | 29 | 80 | 10 | 130 | 12 | 200 (cap 260) | 10 / 15 | 13–15 | +4–+5 | 12–13 | +4–+5 |
| 3 | 37 | 105 | 15 | 165 | 18 | 260 (cap 330) | 15 / 22 | 13–15 | +4–+5 | 12–13 | +4–+5 |
| 4 | 38 | 105 | 19 | 170 | 23 | 270 (cap 340) | 19 / 29 | 13–15 | +4–+5 | 12–13 | +4–+5 |
| 5 | 59 | 165 | 25 | 265 | 30 | 410 (cap 530) | 25 / 37 | 15–17 | +6–+8 | 14–15 | +6–+7 |
| 6 | 64 | 180 | 29 | 290 | 35 | 450 (cap 580) | 29 / 44 | 15–17 | +6–+8 | 14–15 | +6–+7 |
| 7 | 71 | 200 | 34 | 320 | 41 | 500 (cap 640) | 34 / 51 | 15–17 | +6–+8 | 14–15 | +6–+7 |
| 8 | 74 | 205 | 39 | 335 | 47 | 520 (cap 670) | 39 / 58 | 15–17 | +6–+8 | 14–15 | +6–+7 |
| 9 | 91 | 255 | 44 | 410 | 52 | 640 (cap 820) | 44 / 65 | 15–17 | +6–+8 | 14–15 | +6–+7 |
| 10 | 91 | 255 | 48 | 410 | 58 | 640 (cap 820) | 48 / 72 | 15–17 | +6–+8 | 14–15 | +6–+7 |
| 11 | 109 | 305 | 53 | 490 | 63 | 760 (cap 980) | 53 / 79 | 17–18 | +9–+11 | 16–17 | +7–+9 |
| 12 | 115 | 320 | 58 | 520 | 69 | 800 (cap 1040) | 58 / 86 | 17–18 | +9–+11 | 16–17 | +7–+9 |
| 13 | 124 | 345 | 62 | 560 | 75 | 870 (cap 1120) | 62 / 93 | 17–18 | +9–+11 | 16–17 | +7–+9 |
| 14 | 124 | 345 | 67 | 560 | 80 | 870 (cap 1120) | 67 / 100 | 17–18 | +9–+11 | 16–17 | +7–+9 |
| 15 | 134 | 375 | 72 | 605 | 86 | 940 (cap 1210) | 72 / 108 | 17–18 | +9–+11 | 16–17 | +7–+9 |
| 16 | 140 | 390 | 76 | 630 | 92 | 980 (cap 1260) | 76 / 115 | 17–18 | +9–+11 | 16–17 | +7–+9 |
| 17 | 150 | 420 | 81 | 675 | 97 | 1050 (cap 1350) | 81 / 122 | 18–20 | +11–+13 | 18–19 | +8–+10 |
| 18 | 152 | 425 | 86 | 685 | 103 | 1060 (cap 1370) | 86 / 129 | 18–20 | +11–+13 | 18–19 | +8–+10 |
| 19 | 157 | 440 | 90 | 705 | 109 | 1100 (cap 1410) | 90 / 136 | 18–20 | +11–+13 | 18–19 | +8–+10 |
| 20 | 161 | 450 | 95 | 725 | 114 | 1130 (cap 1450) | 95 / 143 | 18–20 | +11–+13 | 18–19 | +8–+10 |
**Cunning Strike check** (Ash's save DC = 8 + Dex + prof): L5 **16** · L9 **17** · L13 **18** · L17 **19**.
- Against a boss's best save of +10, Ash's DC 19 lands 40% of the time.
- Against a boss's weak save (+5), it lands 65%.
- **Always give bosses at least one weak save among Dex, Con and Wis**, so his Cunning Strikes (Poison, Trip, Daze and so on) have a real target.
- Keep the best saves at **+8 to +10** at L17–20, and never higher than +11.

---

## 4. The phase-change template (every significant fight and boss)

> **Rule:** no rinse-and-repeat. Every significant fight changes about every **3–4 rounds**. Bosses change at least **twice**. Each change must make **movement and choices matter**.

```
FIGHT ## · Name · Chapter · Type (Ordinary / Significant / Boss) · Party level
Target numbers (from §3): total HP ___ · enemy DPR ___ · AC ___ · attack ___ · DC ___
Battlefield: 3–5 named features (cover, height, hazards, water, objectives). Crop-friendly map ref.
Opening: where everyone is; enemy pre-buffs; what the enemies know about the party.
Enemy plan: focus target and why; what they do if the plan fails; when they flee or surrender.

PHASE 1 · rounds 1–3 · "The setup"
  What's happening / enemy tactics / the objective
PHASE 2 · trigger: round 3–4 OR boss at ~2/3 HP OR objective event
  Change type (pick 1–2): TERRAIN (collapse, flood, fire, ice, darkness, gate tearing)
                          OBJECTIVE (rescue, close, hold, escape, protect, stop the ritual)
                          FORM (boss transforms, splits, takes to the air or water)
                          COUNTER (it now answers the party's favorite move; see §6)
  Telegraph one round early: what the party sees, hears or feels
  New tactics
PHASE 3 · trigger: round 6–8 OR boss at ~1/3 HP
  (as above; must differ from phase 2's change type)
FINAL BEAT · how it ends: kill, rout, surrender, wake (Hushed), escape, the objective met
Fail-forward: what happens if the party loses or runs
Rewards: treasure, story, EVT-## granted
DM notes: damage-per-round check, the expected round count, what to cut if it drags
```

**Pacing guard (from kickoff §6):** if a boss fight passes round 10 and **the last phase change was 4+ rounds ago**, trigger the next phase now, or end the fight on the objective. Never let a fight run long without changing.

---

## 5. Stat-block template (2024 style; chapter writers must use it)

```
### NAME
*Size Type (tag), Alignment*
**AC** __ · **Initiative** +__ (__) · **HP** __ (__d__ + __)
**Speed** __ ft., (fly/swim/climb __ ft.)

|   | Score | Mod | Save |   | Score | Mod | Save |   | Score | Mod | Save |
|---|---|---|---|---|---|---|---|---|---|---|---|
| STR | | | | DEX | | | | CON | | | |
| INT | | | | WIS | | | | CHA | | | |

**Skills** … · **Resistances / Immunities / Vulnerabilities** … · **Condition Immunities** …
**Senses** … passive Perception __ · **Languages** … · **CR** __ (XP __; PB +__)
*Tuned for party level __: role (brute / skirmisher / controller / artillery / leader / guard / boss)*

**Traits**
- ***Name.*** Plain-English rules text.
- ***Legendary Resistance (3/Day, or 4/Day in Lair).*** If it fails a saving throw, it can choose to succeed instead. *(Bosses only. Spend on effects that end the fight's story early, like stuns or banishment, not on minor ones. Tell the player when it's used: "it shrugs it off; that's one.")*

**Actions**
- ***Multiattack.*** …
- ***Attack name.*** *Melee/Ranged Attack Roll:* +__, reach/range __. *Hit:* __ (__d__ + __) type damage, plus rider.
- ***Save ability (Recharge 5–6).*** *Dex/Con/Wis Saving Throw:* DC __, area. *Failure:* __ damage, plus rider. *Success:* half damage.

**Bonus Actions** / **Reactions**
- ***Guard reaction example: Interpose.*** When an attack hits the boss and this guard is within 5 ft, the guard takes the hit instead.

**Legendary Actions** *(bosses only)*
*Uses: 3 (4 in Lair). Right after another creature's turn, it spends a use on one option. It regains all uses at the start of its turn.*
- ***Move/Strike/Spell option.*** …
- ***Phase-linked option*** (unlocked in phase 2 or 3) …

**Lair Actions** *(where it fits; on initiative count 20, losing ties; no repeats two rounds running)*
- Terrain-changing option (fits a phase change)
- Objective-pressure option (the ritual advances, the gate widens, the water rises)
- Counter option (see §6)

**Phases:** link to the fight's phase template (§4). State what changes in the stat block at each phase: new actions, lost traits, AC or speed changes, the new form's HP pool.
**Tactics:** focus fire and best targets. Never makes an attack at disadvantage when a better option exists. Uses cover. Retreats to heal. Guards protect the caster or leader.
```

**Boss checklist:**
- [ ] Legendary Resistance 3 (4 in lair)
- [ ] Legendary actions 3 (4 in lair), with at least one movement option
- [ ] Lair actions where a lair fits
- [ ] **Guards or counters for priority targets:** a bodyguard with Interpose, a ward that must be broken, a minion that can raise or heal
- [ ] At least one weak save (Dex, Con or Wis)
- [ ] Best saves +8 to +10 at L17–20, scaled down by tier (see §3)
- [ ] At least two phase changes of different types
- [ ] A "hope" lever: Hushed bosses or adds can be **woken** (DC 15 Performance with the tune, scaled up by tier: DC 15 / 17 / 19 / 21) instead of killed

---

## 6. Counters to the party's favorite moves

> Use **one counter per phase at most**, **telegraph it one round early**, and **never counter the same move two fights in a row**. The point is to make choices matter, not to punish the player for playing well.

| Party move | Fair counters |
|---|---|
| **Bart's Help, giving Ash advantage** | Enemies notice the owl and swat it (it has 1 HP). Area pulses (a ripple of greywilt, a shriek) that hit small flyers. Enemies with blindsight or tremorsense who aren't fooled by flyby angles. *Bart dies, comes back the next day, and makes jokes about it.* |
| **Ash's Sneak Attack from flanking** | Enemies fight back-to-back or keep a reach guard. A shove or grapple to drag Ash out of position. A guard's Interpose. "Watchful" leaders who can't be ganged up on (once per round, an ally within 5 ft doesn't count for Sneak Attack). |
| **Ash's Cunning Action Hide** | Tremorsense, scent, lanterns and light, a hound or familiar of its own, a "hush" field where his footsteps echo. |
| **Gideon's Protection style and smites** | Ranged enemies who ignore him. Enemies that pull or push a protected ally away from him (shove, tentacle, current). A boss that makes Gideon's smite target a temporary shell or decoy. |
| **Zeke's area spells (Thunderwave, Fireball)** | Spread formation. Enemies that close fast and grapple him. A caster with **Counterspell (2014)**. Wards that absorb one spell. Water or wind that disperses fire. |
| **Zeke's Shield spell** | Saving-throw attacks instead of attack rolls. Multi-hit routines that burn the reaction early. |
| **Moss's wild shape as a front-line beast** | Big single hits that burn temporary HP. Grapple and restrain to pin the beast. Concentration-breaking volleys on his spell. Psychic or Wisdom-save effects, which hit his Wis +6 (fairly). |
| **Gideon's Initiative Swap** | Bosses with high initiative and legendary movement. Reinforcements that arrive on initiative count 10. |
| **Healing Word and Lay on Hands yo-yo** | Enemies that "keep" a downed hero: drag them toward water, the gate or the greywilt (an objective change, not an execution). |
| **Long rest after every fight** (no rest gap, house rule) | The world clock: the SEAL track, Lark's hushing, a rival getting there first. Time pressure on chapters, never denial of rest. |

---

## 7. Quick reference: building a fight in five minutes

1. Look up the party level in §3. Note total HP, enemy DPR, AC, attack and DC.
2. Pick 2–4 enemy roles: one brute, one controller or leader, plus skirmishers or guards.
3. Split the HP pool among them. Set the attack count so their combined expected damage after misses matches enemy DPR.
4. Write phase 2 and (for significant fights) phase 3 from §4.
5. Choose one counter from §6, telegraph it, and write what the party sees.
6. Check the L1–2 survivability caps (§2) if the party is level 1–2.
7. Log the expected round count. After the session, log the **real** round count and the party's real DPR in the Sealed GM Notes, and adjust this file if they're off by more than 25%.
