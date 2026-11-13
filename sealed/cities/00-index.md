# Cities Index and Shared City Rules (SEALED — DM ONLY)

> **What this folder is:** the city-life layer. Shops, workshops, merchants, festivals, contests, fight rings, betting, odd jobs, things worth stealing and rivals for every settlement in the world bible (`world/02`, `world/03`, `world/05`), plus the reusable rules those menus share (§2–§9 below).
> **What it isn't:** plot. Nothing here forces a beat. Every activity is optional, and every menu is something the player picks from. Chapter files already name their own side-activity windows. Where a chapter has written a specific version of an activity (a named opponent, a purse), **the chapter wins** for that scene, and these files supply everything around it.
> **Read with:** `rules/00` (house rules: all coin is gold; 2024 prices; potions are bonus actions), `rules/02` (tuning), `rules/03` (price check), `truth/00` (name lookup and the running rule), `campaign/05` §4 (gift moments).

---

## 1. Files

| File | What's in it |
|---|---|
| `00-index.md` | This file. Shared rules: haggling and selling, the **street hustle**, betting odds, ring bouts and ring math, street fights, odd jobs, heists and fences, festival calendar |
| `01-home-city-shops.md` | Emberford's seven magic shops (keeper, personality, interior, full inventory with 2024 prices, how stock changes by act) and the mundane merchants the Fringe and Market Steps use |
| `02-enchanters-row.md` | The eight Row workshops, each maker's commission menu (prices and lead times), the gift-commission procedure, and the Gifts Given log format |
| `03-emberford.md` | Emberford's side-activity menu: festivals with dates, contests as check chains, the Bucket's fighter ladder by tier (stat blocks), street fights, betting, the odd-jobs board, things worth stealing, rivals |
| `04-hobbs-ferry.md` | Hobb's Ferry |
| `05-driftmarket.md` | Driftmarket |
| `06-tollhaven.md` | Tollhaven |
| `07-bramblecog.md` | Bramblecog |
| `08-corriemount.md` | Corriemount Abbey and village |
| `09-copperhill.md` | Copperhill |
| `10-wolfsgate.md` | Wolfsgate |
| `11-dun-morrach.md` | Dun Morrach |
| `12-kesselby.md` | Kesselby (the mining village at the Kessel Workings; Ch12) |
| `13-highmarch.md` | Highmarch |
| `14-aranhollow.md` | Aranhollow |
| `15-old-varrow.md` | Old Varrow (the ruin: dares, diving, scavengers) |
| `16-saltreach.md` | Saltreach |
| `17-saffra.md` | Saffra (Mirrowen) |
| `18-tuskhold.md` | Tuskhold (Mirrowen) |
| `19-horngard.md` | The Horngard and Cairn Answer (Mirrowen) |
| `20-hollowmere.md` | Hollowmere and the Rennet otter-rafts (Mirrowen) |
| `art-list.md` | Every shop interior and shopkeeper portrait to paint, with file names |
| `_change-requests.md` | Requests for shared files (new NPC IDs, edges, small facts), CHG style |

### When each place is likely visited (sets the tier of its menu)

| Place | Chapters (outline) | Party level | Tier used in its file |
|---|---|---|---|
| Emberford | every act | 1–20 | all four tiers |
| Hobb's Ferry | Ch8 (and any trip down the King's Road) | 3–10 | T1–T2 |
| Driftmarket | Ch7–9, Ch20 | 7–9, 20 | T2 (T4 notes) |
| Tollhaven | Ch8–10, Ch14, Ch20 | 8–10, 14 | T2–T3 |
| Bramblecog | optional (Ch8–9 raids) | 8–9 | T2 (T3 notes) |
| Corriemount | optional (Act II side thread) | 7–13 | T2–T3 |
| Copperhill · Wolfsgate | Ch10 | 10 | T2 (T4 notes for a return) |
| Dun Morrach | Ch10, Ch17 | 10, 17 | T2 and T4 |
| Kesselby | Ch12 | 12 | T3 |
| Highmarch | Ch17–18 | 17–18 | T4 |
| Aranhollow | Ch17 | 17 | T4 |
| Old Varrow | Ch10 (passing), Ch18 | 10, 18 | T2 and T4 |
| Saltreach | Ch19 | 19 | T4 |
| Saffra | Ch14 (and Ch9 mentions) | 14 | T3 |
| Tuskhold | Ch14, Ch16 | 14–16 | T3 |
| Horngard / Cairn Answer | Ch15 | 15 | T3 |
| Hollowmere | Ch3, Ch6, Ch14 | 3–6, 14 | T1 (occupied), T3 (freed) |

Tiers: **T1** L1–4 · **T2** L5–10 · **T3** L11–16 · **T4** L17–20.

---

## 2. Prices, haggling and selling

**Book prices** (`rules/00` §2, `rules/03`): magic items Common **100** · Uncommon **400** · Rare **4,000** · Very Rare **40,000** · Legendary **200,000** gp. Consumables (potions, scrolls, oils, dusts, single-use ammunition) are **half**. Magic weapons and armor add the base item's price. Gear follows the 2024 PHB. All coin is gold; anything under 1 gp is bundled or ignored.

**Spell scrolls** by rarity (2024 DMG), at the consumable half price: cantrip or 1st level **50** · 2nd–3rd **200** · 4th–5th **2,000** · 6th–8th **20,000** · 9th **100,000**. Zeke copying a spell into his book: **50 gp and 2 hours per spell level** (2024 PHB).

**"Glimmer charms"** (not book magic items): Emberford's everyday glimmer goods, like heat-stones, lamp chips, warm-collar charms and self-stirring spoons. They're priced in this folder at 1–50 gp. They do one small cantrip-sized thing, need a fresh chip every month or so, and **all die if glimmer dies** (Endings 1 and 2).

**The house rule:** the **starting price is the book price.** Shops have personalities, and the haggle moves the price from there.

**Haggling (one check per purchase, or one per shopping trip for a pile):**
- Ash rolls **Charisma (Persuasion)** or **(Deception)** against the shop's **Haggle DC** (each shop lists one; 12–18).
- **Success:** −10%. **Success by 5 or more:** −20%. **Natural 20:** −25%, and a story (the keeper remembers him).
- **Failure:** book price. **Failure by 5 or more:** the keeper is offended. Book price, and the next haggle in that shop this chapter is at disadvantage.
- Some keepers have special levers (Ambrose Webb rewards patience, Jory Tolliver loves a counter-offer, Hakon Stonebrow won't haggle with anyone who carries glimmer). These are listed per shop.
- **Never below 70% of book,** whatever happens. Shopkeepers have rent.

**Selling to a shop:** an honest shop buys magic items at **50% of book** (2024 DMG norm), mundane gear at 50%, art and gems at full value if the shop deals in them. Consumables sell at 50% of their (already halved) price.
**Selling hot goods:** see §8 (fences).

---

## 3. The Street Hustle (reusable rule for Ash's shell game, cards and dice)

> One **set** is about an hour of in-world time and three quick rounds at the table. It's built so the player can run it in two minutes, or make a scene of it. Ch1's shell game ("Sleight of Hand against the mark's passive Perception, 1d4 gp per success") is this rule at its simplest. Everything below extends it and stays compatible.

### 3.1 Pick the game

| Game | What Ash rolls | Against | Notes |
|---|---|---|---|
| **Shells** (cups and ball) | **Dexterity (Sleight of Hand)** | Each mark's **passive Perception** (or an active Wisdom (Perception) roll if the mark is suspicious) | Ash owns the set. It's his game. |
| **Cards** (Kings and Ferrymen, or the local game) | **Charisma + proficiency with playing cards** (Ash is proficient) | Contested: the table's best player rolls their own card bonus | Honest play is a real contest. Cheating is below. |
| **Dice** (the Bones, Bone Table rules) | Ash isn't proficient with dice. Honest play is **pure luck: d20, 11+ wins** | Luck Points (Lucky feat) can be spent on it | The edge comes only from loaded dice or reading the dealer. |

### 3.2 Pick the pitch (sets the marks and the purse)

| Pitch grade | Example spots | Mark's passive Perception / active bonus | Purse per winning round | Starting Heat |
|---|---|---|---|---|
| **Easy** | Market day crowd, a festival, a barge landing | 10 / +0 | 1d4 gp | 0 |
| **Street** | Market Steps, the Wharves, a Commons tavern, Hobb's Ferry inn | 12 / +2 | 1d6 gp | 0 |
| **Comfortable** | Crownhill strollers, a Tollhaven quay, Highmarch Kingsbridge | 13 / +3 | 2d6 gp | 1 (people here notice) |
| **Rich** | Tollhaven's Lamplight Row, a Crownhill ball, the King's Tourney stands | 14 / +4 | 4d6 gp | 1 |
| **High table** (by invitation or buy-in only) | Purse heirs' card rooms, a dwarven token table, Saffra's bell-houses | Sharps (§3.5) | 10d6 gp (or the table's stake) | 2 |

**Ash's code:** he never hustles the Fringe. If he does, every Willow Lane edge that hears of it (Netta hears of everything) takes a bad note, and Rook (R-037) laughs at him for a week.

### 3.3 Run the set: three rounds

Each round has three short steps. Most rounds need only the middle one.

1. **The hook (optional).** Ash talks the mark into a bigger stake. **Charisma (Deception)** against the mark's **Wisdom (Insight)** (the passive number, or an active roll if the mark is suspicious). **Success:** this round's purse is **doubled.** **Failure:** the mark walks, and the round is lost (no Heat).
2. **The play.** The game's check from §3.1. **Win:** roll the purse. **Lose:** Ash pays out the same purse (he has to look honest) and gains **+1 Heat**.
3. **The tell.** A win by **10 or more** draws a crowd: the next round's mark is one grade up, and Heat goes up by 1.

**The come-on.** Ash can let round 1 go on purpose (no roll, he pays out 1 purse). Rounds 2 and 3 then have their hooks at **advantage**.

**Take 10.** When nobody is watching closely (Easy or Street pitch, Heat 0–1), Ash can take 10 on the play instead of rolling. That's the house rule from `rules/00` §6.

### 3.4 Cheating (cards and dice), and Bart

| Trick | Check | DC | Effect | If it fails |
|---|---|---|---|---|
| **Palm a card** (cards) | Dexterity (Sleight of Hand) | Table's best passive Perception + 2 | The hand's contest is at advantage | +2 Heat. Fail by 5+: caught; the set ends (§3.6) |
| **Switch in loaded dice** (dice) | Dexterity (Sleight of Hand) | Dealer's passive Perception + 2 | Ash wins on **6+** instead of 11+ for the rest of the set | Caught (§3.6) |
| **Switch them back out** at the end of the set | Dexterity (Sleight of Hand) | same | Clean exit | +2 Heat, and the dealer checks the dice next time |
| **Bart peeks** (any game) | none for Ash. Bart rolls Dexterity (Stealth) +3 (owl) against the room's best passive Perception | — | One round of Ash's choice at **advantage** (Bart's Help) | The room notices "that owl's looking at your cards": +1 Heat and a laugh. Bart: "I was looking at the *sausage*." |
| **Read the dealer** (being hustled) | Wisdom (Insight) | 13 (Street) / 15 (Rich) / Sharp's Deception + 10 | Ash spots the crooked game and can call it out, exploit it, or walk | He plays the crooked game: his rounds are at disadvantage |

**Bart's rate:** one sausage per set, payable in advance. He will remind Ash. Bart can't help in a game where familiars are banned (Tollhaven's high tables; any dwarven token table).

### 3.5 Sharps (high tables and named rivals)

When the mark is a professional, swap the passive number for a real opponent:

| Sharp grade | Card / dice bonus | Insight | Passive Perception | Typical stake per round |
|---|---|---|---|---|
| **Street sharp** (Bone Table dealer, Rook) | +5 | +4 | 14 | 1d6 × 5 gp |
| **Professional** (Lamplight Row dealer, mercenary card house) | +8 | +6 | 16 | 2d6 × 10 gp |
| **Master** (Percival Hume; Tesh Twelve-Bells) | +11 | +8 | 18 | 3d6 × 20 gp |
| **Legend** (the Grand Wager final; a Saffra bell-house mistress) | +14 | +10 | 20 | 4d6 × 50 gp |

Ash's card bonus (Cha + proficiency): **+6** at L1, **+7** at L5, **+8** at L9, **+9** at L10 (Cha 20), **+10** at L13, **+11** at L17. His Sleight of Hand: **+6** (L1), **+7** (L4), **+8** (L5), **+11** (L6, expertise), **+13** (L9), **+15** (L13), **+17** (L17). He'll outgrow the Street pitches by tier 2. That's the point: the fun moves to the sharps and the high tables.
**Panache (L9+):** against a non-hostile mark, a successful Panache (Persuasion vs Insight) charms the mark for the set. Hooks succeed automatically and the mark won't call Heat on a failed round.

### 3.6 Heat

Heat is how much attention the set is drawing. It's tracked **per pitch** (Market Steps' Heat doesn't follow Ash to Crownhill) and drops by **2 per day** Ash stays away.

| Heat | What happens |
|---|---|
| **2** | **An angry mark** wants his money back. Charisma (Persuasion) DC 12, or Charisma (Intimidation) DC 14, or give it back. A failure turns into a shove and a crowd. |
| **4** | **The local muscle** notices. In Emberford it's Rook's Magpies (NPC-010) or Swift and Sons; elsewhere, the city's rival (each city file names one). They want a cut (half the take), or they want him gone. A refusal is a **street fight** (§6). |
| **6** | **The law.** Hugh Dale (NPC-029) in the Fringe and Commons, the Toll Guard in Tollhaven, the Crown Guard in Highmarch, and so on. Dexterity (Acrobatics) or (Stealth) DC 15 to be gone before they arrive. Otherwise: a fine of **5 gp × tier**, or a night in the cells (the Cage, in Emberford). |
| **Caught cheating** | The set ends at once. The mark (and friends) want blood or money: **double the set's take back**, or a street fight. At Rich and High-table pitches the house bars him for the rest of the chapter. |

### 3.7 What a set is worth (so it doesn't break the treasure budget)

| Tier | Typical honest set (3 rounds) | A good high-table night |
|---|---|---|
| T1 | 2–12 gp | — |
| T2 | 5–30 gp | 100–300 gp |
| T3 | 10–50 gp | 300–800 gp |
| T4 | 10–50 gp (he's famous now; marks recognize him) | 600–2,000 gp |

**Fame in T4:** from Ch17 on, the party are known. At Comfortable and Rich pitches, a mark recognizes Ash on a d6 roll of 1–2. A recognized mark won't play, but buys him a drink and asks for the story. (It's a nice beat. Let it be.)

---

## 4. Betting and odds

Every city has bookies. Use one table everywhere.

| Odds quoted | Bookie thinks the chance is | A 10 gp bet returns (stake included) |
|---|---|---|
| 1 to 3 (odds-on) | 75% | 13 gp |
| Evens | 50% | 20 gp |
| 2 to 1 | 33% | 30 gp |
| 3 to 1 | 25% | 40 gp |
| 5 to 1 | 17% | 60 gp |
| 10 to 1 | 9% | 110 gp |

- **The bookie's shave:** every book is 10% short (the bookie's living). It's already in the odds above.
- **Odds on the party:** a party member's first public contest in a city is offered at **3 to 1** (unknown). After a win there, **evens**. After two, **1 to 3**. A famous party (T4) starts at evens everywhere.
- **Betting on yourself** is legal everywhere except Dun Morrach's Shield Ring (dishonorable) and the Golden Cage's sealed books (Tollhaven rule: fighters may bet only through a registered agent, 5% fee).
- **Spotting a crooked book:** Wisdom (Insight) DC 14 (T1–2) or 16 (T3–4). The crooked bookie plans to run with the takings, or the fight's fixed.
- **Taking a dive:** someone offers Ash **twice the purse** to lose. If he does, he gets paid, the crowd that backed him remembers, and the ring's owner (Ma Garrow, if it's the Bucket) cools one attitude step when she finds out (she always finds out). If he takes the money **and wins anyway**, the fixer's muscle comes for him within the week (a street fight at the next tier up).
- **Laying off the risk:** Ash can place a bet for someone else (Lark, Pip, Netta) for 1 gp's fun, and they win or lose by the same table. Nothing mechanical; a lot of joy.

---

## 5. Ring bouts (every city's fight ring uses these)

### 5.1 The bout
- **One fighter a side**, unless the card says otherwise (tag bouts, gauntlets).
- **Three rounds** (combat rounds). A fighter who drops to 0 HP, yields, or is pushed out of the ring (where the ring has an edge) **loses**.
- **Still standing after three?** The round-by-round **points**: each round goes to whoever dealt more damage that round. Tied on rounds: the crowd decides with a contested **Charisma (Performance or Intimidation)**.
- **Damage is nonlethal** in every ring in this folder unless the file says otherwise. A fighter at 0 HP is unconscious and stable.
- **No magic, no familiars** in the ring (house rules everywhere except where noted). Bart watches from the rafters and heckles.
- **Weapons:** each ring lists its own. Where "wasters" are allowed (wooden practice blades), they count as the named weapon for **Finesse** and **Weapon Mastery**, and deal **bludgeoning** damage of the same die. So Ash keeps Vex, Nick and Sneak Attack with wasters. In fists-only rings he fights with unarmed strikes (Sneak Attack doesn't apply).
- **Healing between bouts** in a multi-bout card: a short rest's worth of time, no spells (most rings have a healer for 5 gp × tier who restores half HP).

### 5.2 Ring math (how every ring opponent in this folder is tuned)

Ring opponents are tuned against **one entrant**, not the party. Reference entrant: **Ash** (the most likely to sign up). The ring takes away Bart, allies and magic, so the entrant's **ring DPR ≈ 0.8 × his `rules/02` §1 DPR**.
- **Opponent HP ≈ 3 × the entrant's ring DPR.** A good bout ends by knockdown around round 3, or goes to points.
- **Opponent DPR ≈ 30% of the entrant's HP per round, after misses.** In three rounds that's a real beating, and a bad night can put Ash down. That's "above standard," on purpose.
- **Against Gideon:** use the same block, with **+2 to hit** (his AC 18–20) and **+25% HP** (he has more hit points and no Sneak Attack to burst).
- **At L1–2** the survivability caps apply (max 9 damage per turn at L1, 14 at L2).
- **At L17+** add Thief's Reflexes (Ash's two turns in round 1): opponent HP gets **+32** (0.8 × the +40 round-one estimate).

| Ash's level | Ash DPR (rules/02) | Ring DPR | Ash HP | **Opponent HP target** | **Opponent DPR target** |
|---|---|---|---|---|---|
| 1 | 10 | 8 | 10 | 24 | 3–4 (cap 9 max) |
| 2 | 10 | 8 | 17 | 25 | 5 (cap 14 max) |
| 3 | 14 | 11 | 24 | 33 | 7 |
| 4 | 14 | 11 | 31 | 34 | 9 |
| 5 | 17 | 14 | 38 | 41 | 11 |
| 6 | 19 | 15 | 45 | 46 | 13 |
| 7 | 22 | 18 | 52 | 53 | 15 |
| 8 | 22 | 18 | 59 | 53 | 18 |
| 9 | 25 | 20 | 66 | 60 | 20 |
| 10 | 25 | 20 | 73 | 60 | 22 |
| 11 | 30 | 24 | 80 | 72 | 24 |
| 12 | 30 | 24 | 87 | 72 | 26 |
| 13 | 33 | 26 | 94 | 79 | 28 |
| 14 | 33 | 26 | 101 | 79 | 30 |
| 15 | 36 | 29 | 108 | 86 | 32 |
| 16 | 38 | 30 | 115 | 91 | 35 |
| 17 | 41 | 33 | 122 | 131 (incl. +32) | 37 |
| 18 | 41 | 33 | 129 | 131 | 39 |
| 19 | 44 | 35 | 136 | 137 | 41 |
| 20 | 44 | 35 | 143 | 137 | 43 |

**Scaling a ring opponent one level up or down:** ±6 HP and ±2 DPR per level in T1–T2, ±8 HP and ±3 DPR in T3–T4. Up a whole tier: +2 AC, +2 to hit, +1 save DC, double the HP and damage. Down a tier: the reverse.

**Every bout changes once.** Bouts are short, but the template's rule still applies in miniature. Each ring opponent has a **round-2 or round-3 turn** (a second wind, a dirty trick, the crowd, the ring itself) written into its block.

### 5.3 Purses by tier
| Tier | Undercard | Main card | Championship / festival card |
|---|---|---|---|
| T1 | 20 gp | 40 gp | 100 gp |
| T2 | 50 gp | 80–150 gp | 300 gp |
| T3 | 150 gp | 200–400 gp | 750 gp |
| T4 | 300 gp | 500–1,000 gp | 2,000 gp |
Entry fee: 5 gp × tier, unless the ring says otherwise.

---

## 6. Street fights

Informal brawls behind taverns, on quays, in market squares. **Fists, cudgels and the furniture.** Nobody draws steel in a street fight unless they want the whole street against them.
- **Nonlethal by default.** Anyone who draws a blade turns the crowd: the other side gets advantage on its next attack, and the law arrives in 1d4 rounds.
- **The hat:** a street fight with a crowd has a hat for coins. Winners split **1d6 × 5 gp × tier**.
- **Use the Street Tough block** in `03-emberford.md` §4.3, scaled by tier there (it lists crew sizes so the total HP matches the `rules/02` §3 ordinary-fight target). Each city file names its own crew and adds one local trick.
- **Three rounds and done.** Street fights are ordinary fights: 3–4 rounds. At the end of round 3, the crowd or the law breaks it up whatever the state.

---

## 7. Odd jobs boards

Every city file lists 6–10 jobs. Use this pay scale everywhere so coin stays inside the chapter treasure budgets.

| Tier | Courier and errand | Retrieval | Bounty (small) | Guard/escort per night | Risky job (heist-adjacent, monster) |
|---|---|---|---|---|---|
| T1 | 2–20 gp | 10–100 gp | 5–50 gp | 2–10 gp | 50–150 gp |
| T2 | 10–50 gp | 50–250 gp | 50–200 gp | 10–30 gp | 150–500 gp |
| T3 | 25–100 gp | 150–600 gp | 200–750 gp | 30–75 gp | 500–1,500 gp |
| T4 | 50–200 gp | 400–1,500 gp | 500–2,000 gp | 75–150 gp | 1,500–4,000 gp |

**Running a job quickly:** one to three quick checks (DC by tier: **12 / 14 / 16 / 18**), with one complication if any check fails by 5 or more. Most odd jobs take a few hours. A job that turns into a fight uses the street-fight rules or a stat block from the city file.

---

## 8. Things worth stealing: heists and fences

Every city file lists targets with a **Security** rating and a **fence price**. Ash's code (`build/decisions.md`): never the Fringe. Stealing *for* someone (taking back what was taken) is his favorite kind.

### 8.1 The quick heist (a chain of checks under pressure)
A heist is five links. Each link is one quick check from a short menu (the city file gives the specifics). **Need 4 successes before the Alarm reaches its limit.**

| Link | Typical checks |
|---|---|
| 1. **Case it** | Intelligence (Investigation) · Wisdom (Perception) · Bart's eyes (automatic success, but Bart demands two sausages) · a bribe (Persuasion, plus 1d6 × 5 gp × tier) |
| 2. **Get in** | Dexterity (Stealth) · Charisma (Deception) (a disguise or a story) · climbing (automatic with Ash's L3 climb speed, if the route is a wall) |
| 3. **Beat the lock or ward** | Thieves' Tools · Intelligence (Arcana) for glimmer ward-chimes · Zeke's *Dispel Magic* (automatic) · Fast Hands (L3: as a bonus action, so the link takes no extra time) |
| 4. **Take it** | Dexterity (Sleight of Hand) · Strength (Athletics) for something heavy |
| 5. **Get out** | Dexterity (Acrobatics) · Dexterity (Stealth) · Charisma (Deception) (walk out like you own it) |

| Security | DCs | Alarm limit | Who comes when the Alarm fills |
|---|---|---|---|
| **Low** (a stall, a warehouse, a skiff) | 12 | 3 failures | a watchman or two (street-fight scale) |
| **Medium** (a merchant's house, a guild office) | 15 | 3 failures | guards: an ordinary fight at the party's level |
| **High** (a Crownhill vault, a Purse strongroom) | 17 | 2 failures | guards plus wards: a significant fight, or flight |
| **Very High** (a royal archive, a dwarven treasury) | 19 | 2 failures | a significant fight and a manhunt; the party is known |

**Each failure** adds 1 to the Alarm. A failure by 5 or more adds 2. **Fail forward:** if the Alarm fills, the party can still get the item, but they're seen, chased or identified.

### 8.2 Fences
| Fence | Where | Pays (of book or fair value) | Notes |
|---|---|---|---|
| **Jory Tolliver** (NPC-045), Odd Lot | Emberford, Market Steps | **30%** hot, **50%** cold (a month later) | Won't take anything from the Fringe once he knows (he's sentimental; he'd deny it) |
| **Ma Garrow** (NPC-024) | Emberford, the Bucket | **40%**, coin only, no questions | Only for people she likes (R-062 friendly). Never glimmer: "Guild hunts glimmer." |
| Each city file names its fence | | usually 25–40% | |

**Glimmer is hot everywhere.** Raw glimmer and Guild-stamped goods sell at **20%** to fences, because the lamp-wardens hunt them. After Ch13 (if the Guild falls), they sell at 50%, and nobody's buying by Ch17.

---

## 9. Festivals at a glance (all cities)

Calendar (`world/01`): Thawing, Seedtide, Highwater, Blossom, Midsummer, Haymonth, Harvest, Leaffall, Frostcome, Deepwinter, Longnight, Lantern. 30 days each. The campaign opens early Thawing YF 1104; the finale is Midsummer's Eve YF 1105. **Midsummer's Eve** is the evening of the last day of Blossom, the night before 1 Midsummer.

| Date | Festival | Where | File |
|---|---|---|---|
| Every 10th day | Tenth-day market | Emberford | 03 |
| 3 Thawing | Rope-Breaking (the ice ropes come off the ferry) | Hobb's Ferry | 04 |
| 20 Seedtide | Swarm Day (the abbey's first bee-swarm) | Corriemount | 08 |
| 14–16 Highwater | Highwater Fair; the Bargerace (16th) | Emberford | 03 |
| 1 Blossom | The Cheese Roll | Bramblecog | 07 |
| Last day of Blossom (eve) | Turn of Light (Midsummer's Eve) | Emberford, everywhere on the river | 03 |
| 10–12 Midsummer | The Gull Race and the Shanty Contest | Saltreach | 16 |
| 1–7 Haymonth | The King's Tourney | Highmarch | 13 |
| 15 Haymonth | The Champion's Bout | Copperhill | 09 |
| 20–21 Haymonth | The Lashing (the Drift's year-turn: the Seven Mothers re-tie the town's ropes) | Driftmarket | 05 |
| Harvest (whole month) | Provost Election; Guild Games (last week) | Emberford | 03 |
| 1–7 Harvest | The Grand Wager | Tollhaven | 06 |
| 25 Harvest | The Wolf Run | Wolfsgate | 10 |
| 1 Leaffall | The Drawing (the Fairest Machine picks the council) and the Contraption Fair (the week before) | Bramblecog | 07 |
| 1 Lantern (or 1 Leaffall; see CHG-A2-01) | Ford Festival; the Lamp-Climb | Emberford | 03 |
| Frostcome, first snow | The Kettle Plunge season opens | Dun Morrach | 11 |
| 21 Deepwinter | The Re-Striking Eve (every 10th year; next is YF 1106) and the Anvil Test (every year) | Dun Morrach | 11 |
| Last night of Lantern | Lantern Night | Emberford | 03 |
| Mirrowen: the Great Telling (Eyrland Thawing equivalent) | Saffra | 17 |
| Mirrowen: the Drum Moot (Eyrland Seedtide) | Horngard | 19 |

---

## 10. Provisional IDs used in this folder

`truth/00` gave NPC-080 as next free. Act II's chapters used a provisional block (NPC-140 to NPC-159). **This folder uses its own provisional block, NPC-300 to NPC-356**, so it can't collide with chapter writers working at the same time. `_change-requests.md` (CHG-CY-01) asks the Truth File's owner to confirm or renumber. All names were checked against the banned list in `world/04` and the existing name lookup.

Existing NPCs reused here (no new IDs): every Emberford shopkeeper (NPC-043 to NPC-056), Simon Shaw (NPC-025), Peg (NPC-015), Netta (NPC-016), Bess (NPC-011), Tam Hollin (NPC-035), Ma Garrow (NPC-024), Rook (NPC-010), Hugh Dale (NPC-029), Old Bram (NPC-030), the city leaders (NPC-062 to NPC-077), Percival Hume (NPC-142), Gert Volker (NPC-148), Sal Pickett (NPC-153), Saffi (NPC-061), and the Act I Tier 3 fighters (Big Lottie Sparrow, Hal Brindle, Morwenna Kell).
