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
| **Master** (Julian Hume; Tesh Twelve-Bells) | +11 | +8 | 18 | 3d6 × 20 gp |
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

### 5.1 The bout, and the four ring formats (CHG-19: rings must let a Dexterity fighter compete)

**Every ring in Eyrland fights in one of four formats.** Most rings run two or three of them on a card night. **The entrant picks the format when he signs the slate**, from whatever that night's card offers (each city file lists its formats and its opponents per format). A bookie's odds don't care which format; the crowd does.

**Rules in every format, every ring:**
- **One fighter a side**, unless the card says otherwise (Last-Standing, tag bouts).
- **No magic. None.** No spells (that includes the 2024 **Divine Smite**, which is a spell, and every smite spell), no Channel Divinity, no auras, no **Radiant Strikes**, no **Wild Shape**, no magic items (a ring steward checks with a lodestone and a sniff), no familiars in the pit (Bart heckles from the chains). **Gideon fights as a strong, well-trained man with a waster. Moss fights as an old man with a stick** (he usually declines, mildly).
- **Class tricks that aren't magic are allowed:** Cunning Action (Dash, Disengage; **Hide is useless in a lit ring** unless the format says otherwise), Sneak Attack (where the format uses weapons), Cunning Strike, Uncanny Dodge, Evasion, Fancy Footwork, Panache (a taunt; the crowd loves it), Steady Aim, Extra Attack, Second Wind-type features, Lucky, feats, Weapon Mastery.
- **Ring armor:** fighters wear padded jackets at most. **Ring AC = 10 + Dex modifier** (+ shield where the format allows one; no shields in Touches or Beam). Unarmored Defense still works. This alone keeps a heavy-armored brute from being untouchable, and it rewards a quick fighter.
- **Damage is nonlethal** unless a city file says otherwise. 0 HP = unconscious and stable.
- **Healing between bouts:** a short rest's worth of time, no spells; the ring healer restores half HP for 5 gp × tier.
- **Wasters** (wooden practice blades) count as the named weapon for **Finesse, Light and Weapon Mastery** and deal **bludgeoning** damage of the same die. Ash keeps Vex, Nick and Sneak Attack with wasters.

#### Format A · BARE-KNUCKLE (Strength-favored; the old way)
- Fists, elbows, grapples. **Three rounds**; knockdown (0 HP), yield, or thrown out of the ring loses. Still standing: rounds go to whoever dealt more damage; a tie goes to the crowd (contested **Charisma (Performance or Intimidation)**).
- Unarmed strikes use Strength (2024 rules). **Ash's outs:** escaping a grapple with **Dexterity (Acrobatics)**; Disengage + Dash to make a brute chase him (every round a brute spends chasing without landing a blow scores **nothing**, and the crowd jeers the chaser); and the house rule below.
- **The Quick-Hands rule (every ring uses it):** a fighter proficient in Acrobatics may make his unarmed strikes with **Dexterity** instead of Strength, but they deal **1 + Dex** with no damage die. Sneak Attack still doesn't apply (no weapon).
- **Who wins here:** big strong men. Ash can win a Bare-Knuckle bout, but he's the underdog, and the odds say so (one step longer than the Touches line).

#### Format B · WASTERS (TOUCHES) (Dexterity-favored; the fencer's game)
- Wooden wasters (any finesse or light weapon's waster; a waster longsword or club is allowed for strength fighters, used one-handed, no shield). **First to 3 touches wins**, or most touches after **five rounds**.
- **A hit is a touch, whatever the damage.** Roll damage anyway (nonlethal; 0 HP still ends it).
- **A clean touch counts 2:** a hit that **includes Sneak Attack dice**, or a **critical hit**. **A Cunning Strike Trip** (or any knockdown that leaves the other fighter prone) on a hit adds **+1 touch**.
- **Touch cap:** no fighter scores more than **2 touches in one turn** (so a dual-wielder hitting twice scores 2, and a clean touch on the first hit ends his scoring for that turn). Multiattack monsters and Extra Attack fighters follow the same cap.
- **Bart rule:** no familiar, so Ash's Sneak Attack comes from **advantage** (Vex, a prone opponent, Steady Aim if he hasn't moved) or... nothing else; there are no allies in the ring. That's the skill test.
- **Who wins here:** fast, accurate fighters. **Ash is the favorite against most brutes** in this format, and the bookies know it.

#### Format C · RING-OUT (THE BEAM) (balance and footwork)
- A **beam, barge plank, log or narrow wall**: 5 feet wide, 30 feet long, over water, mud, a sawdust pit or (in the Hold at Saltreach) the harbor. Wasters or bare hands. **First fighter off the beam loses.** No time limit worth mentioning; call it at **six rounds** and go to points (most shoves landed).
- **On the beam:** the beam is **difficult terrain for anyone without proficiency in Acrobatics**. A **Shove** (Strength (Athletics) vs. the target's Athletics **or Acrobatics**, target's choice) that succeeds pushes the target off if he's within 5 feet of an edge, which on a 5-foot beam is always.
- **Taking a hit:** a fighter hit by an attack makes a **Dexterity saving throw (DC 8 + the damage dealt, max DC 20)** or is **knocked off balance** (prone; a prone fighter on the beam who's shoved goes off automatically, and standing up costs half his speed as usual).
- **Dodging the shove:** a fighter who took the **Disengage** or **Dodge** action this round has advantage on his check to resist a Shove. **Fancy Footwork** means the opponent can't make an opportunity attack as Ash slips past him on the beam. Cunning Strike **Trip** works here (Dex save or prone, then shove him off).
- **Who wins here:** whoever keeps his feet. Strength still matters (shoves), but Ash's +6 Acrobatics and +6 Dex save make it a fair fight, and it's the crowd's favorite format.

#### Format D · LAST-STANDING (the melee; pot format)
- **4 to 8 fighters** in the pit at once, wasters or fists (the card says which). **Last one on his feet takes the pot** (entry fees × fighters, minus the house's 20%); second-last gets his fee back.
- **Everyone's an enemy.** NPC fighters in a melee **attack whoever hit them last, or the nearest strong-looking fighter**; they gang up on the biggest man in the pit first (that's the crowd's tradition and the fighters' sense). Roll initiative for all.
- **Cunning Action is king here:** Disengage and Dash let a quick fighter stay out of the thick of it while the brutes knock each other down; but **any fighter who hasn't attacked anyone for two rounds** is fair game for everyone (the steward points at him with the pole).
- **Who wins here:** a clever fighter as often as a strong one.

**Gideon in the ring:** he fights with a waster longsword, no smites, no auras, and he's still very good. The crowd adores him. In Bare-Knuckle he's a heavy favorite; in Touches he's even money against a good fencer; on the Beam he's a big target.

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

**Tuning by format.** The HP/DPR targets above are for Bare-Knuckle and Last-Standing. In **Touches**, HP barely matters: what matters is **AC (ring AC = 10 + Dex)** and to-hit. A Touches opponent for Ash at L1–4 has ring AC 12–14 and +4 to +5 to hit (T2: AC 14–15, +6; T3: AC 15–16, +8; T4: AC 17, +10), and **one** good feature (a parry reaction, a lunge, a feint). In **Ring-Out**, what matters is Athletics (to shove) and Acrobatics/Dex save (to stay up): T1 opponents +3 to +5 Athletics and +2 to +4 Dex save; T2 +6/+5; T3 +8/+7; T4 +10/+9.

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
| 1 Leaffall | Ford Festival; the Lamp-Climb | Emberford | 03 |
| Frostcome, first snow | The Kettle Plunge season opens | Dun Morrach | 11 |
| 21 Deepwinter | The Re-Striking Eve (every 10th year; next is YF 1106) and the Anvil Test (every year) | Dun Morrach | 11 |
| Last night of Lantern | Lantern Night | Emberford | 03 |
| Mirrowen: the Great Telling (Eyrland Thawing equivalent) | Saffra | 17 |
| Mirrowen: the Drum Moot (Eyrland Seedtide) | Horngard | 19 |

---

## 10. Provisional IDs used in this folder

`truth/00` gave NPC-080 as next free. Act II's chapters used a provisional block (NPC-140 to NPC-159). **This folder uses its own provisional block, NPC-300 to NPC-356**, so it can't collide with chapter writers working at the same time. `_change-requests.md` (CHG-CY-01) asks the Truth File's owner to confirm or renumber. All names were checked against the banned list in `world/04` and the existing name lookup.

Existing NPCs reused here (no new IDs): every Emberford shopkeeper (NPC-043 to NPC-056), Simon Shaw (NPC-025), Peg (NPC-015), Netta (NPC-016), Bess (NPC-011), Tam Hollin (NPC-035), Ma Garrow (NPC-024), Rook (NPC-010), Hugh Dale (NPC-029), Old Bram (NPC-030), the city leaders (NPC-062 to NPC-077), Julian Hume (NPC-142), Gert Volker (NPC-148), Sal Pickett (NPC-153), Saffi (NPC-061), and the Act I Tier 3 fighters (Big Lottie Sparrow, Hal Brindle, Morwenna Kell).

---

## 11. Skill contests (CHG-20: the rogue's side of every city)

Fights aren't the only way to win a purse. **Every city runs skill contests**, and they're where Ash should shine. They're all built from the pieces below, so the DM can run any of them from this page; each city file names its local versions (§11.9 lists them).

**Common rules for every skill contest:**
- **No magic** (same as the rings: no spells, no magic items, no familiars; Bart watches and heckles). **Class features that aren't magic are allowed**, and the notes below say where Ash's apply.
- **Lucky:** Ash may spend Luck Points on contest rolls. They come back on a long rest, so spending them on a contest is a real choice.
- **Help:** contests are solo unless the contest says "team." A brother shouting advice is flavor, not the Help action.
- **Taking 10:** never in a contest. It's pressure by definition.
- **Tier DCs:** every DC below is written for **T1 (L1–4)**. **Add +2 per tier** (T2 +2, T3 +4, T4 +6). Purses and fees scale by tier as listed.
- **Balance target:** at **L1**, Ash should pass a **Standard T1** contest about **half the time**, a **Hard** one about a third of the time, and a **Brutal** one rarely. By L4 (Dex 20, Second-Story Work, Cunning Action), he should be a favorite on Standard. That's on purpose: the player gets to watch him get good.

### 11.1 The Gauntlet (the pot format)
Most skill contests in Eyrland are run this way: **pay to try, and the passers split the pot.** The crowd pays to watch, the bookies take bets, and the organizer takes his cut.

| Tier | Entry fee | Field (entrants, roll) | Typical pot (before cut) |
|---|---|---|---|
| T1 | 2 gp | 3d6 + 5 (avg 15) | ~30 gp |
| T2 | 10 gp | 3d6 + 5 | ~150 gp |
| T3 | 50 gp | 2d6 + 4 (avg 11) | ~550 gp |
| T4 | 200 gp | 2d6 + 2 (avg 9) | ~1,800 gp |

- **The organizer's cut:** honest house **10%**, ordinary **15%**, shady **20%**. **Insight DC 13** (T1) spots a crooked organizer who means to run with the pot, or who's greased a station for a favorite.
- **How many NPCs pass?** Don't roll every entrant. Roll **1d6** on the course's difficulty:

| d6 | Easy course | Standard | Hard | Brutal |
|---|---|---|---|---|
| 1 | 2 others pass | nobody else | nobody else | nobody else |
| 2 | 3 | nobody else | nobody else | nobody else |
| 3 | 3 | 1 | nobody else | nobody else |
| 4 | 4 | 1 | 1 | nobody else |
| 5 | 5 | 2 | 1 | nobody else |
| 6 | 6 | 3 | 2 | 1 |

- **Named rivals** (the city file lists them) don't use the table; **roll their checks for real** with their bonuses, station by station, in front of the player. That's the drama.
- **The pot:** entry fees × field, minus the cut, **split evenly among everyone who passes.** If one person passes, he takes it all. If **nobody passes, the pot rolls over** to the next contest night (the crowd doubles, and so does the field roll's +5).
- **Speed bonus:** most Gauntlets pay a **flat 10% of the pot** extra (from the house's cut) to the passer with the **fewest penalties**; ties split it.
- **Side bets:** the bookie offers odds on Ash **passing** (§4: first time in a city 3 to 1, then evens, then 1 to 3). Ash may bet on himself everywhere except Dun Morrach.
- **Repeat entries:** the same course runs again next contest night. A passer can't enter the same course again that month (house rule everywhere; "give the others a chance"), so the rich vein is moving between courses and cities.

### 11.2 The obstacle course builder
Build any course from **5–8 stations**. Each station is **one quick check under pressure**. Narrate it fast: the crowd, the splash, the clock.

- **Drop stations** (marked ⬇): fail and you **fall out** (into the water, the mud, the net). You're done.
- **Clock stations** (marked ⏱): fail and you take **1 penalty** (lost time) but keep going. **3 penalties and you're timed out.**
- A **Standard** T1 course: **6 stations, 2 of them ⬇, DC 12.** **Hard:** 7 stations, 3 ⬇, DC 13–14. **Brutal:** 8 stations, 4 ⬇, DC 14–16. **Easy** (kids' day, festival warm-up): 5 stations, 1 ⬇, DC 10.
- **Ash's odds, L1, Standard:** about **55%** (≈70% across the two drop stations with Luck Points held back for them, ≈75% of finishing with 2 penalties or fewer). Hard: about **30%**. Brutal: under **10%**. At L4 Standard: about **80%**.

**Station menu** (pick and reskin):

| Station | Check | Type | Ash's features |
|---|---|---|---|
| **Swinging logs / spinning barrels** | Dexterity (Acrobatics) | ⬇ | Acrobatics +6. **Fancy Footwork** doesn't apply (no attack). |
| **Rope climb / cargo net / greased pole** | Strength (Athletics) or Dex (Acrobatics), climber's choice | ⏱ | **Second-Story Work (L3): climb speed means advantage**, and on an ordinary rope or wall, **automatic success**. Before L3, Acrobatics +6 is his better bet. |
| **The gap jump** (a plank gap over water) | Strength (Athletics), or a straight distance test | ⬇ | **Second-Story Work (L3): jump with Dex.** Ash clears 18 ft with a run-up: any gap of 15 ft or less is **automatic**; the station becomes "land it": Acrobatics DC 10. |
| **The tilting beam** | Dexterity saving throw | ⬇ | Dex save +6 (rogue proficiency). **Evasion** (L7): advantage. |
| **The sprint** (along the quay, across a market) | Strength (Athletics) or Con save, runner's choice | ⏱ | **Cunning Action Dash (L2): automatic success** on one sprint station per course. |
| **The wall run / rooftop leg** | Acrobatics | ⏱ | **Second-Story Work:** advantage. |
| **The crawl** (under a net, through a pipe) | Dexterity (Stealth or Acrobatics) | ⏱ | **Stealth +8 (expertise)** counts here, and it's the station rivals hate. |
| **The ribbon grab** (snatch a ribbon off a swinging dummy without ringing its bell) | Dexterity (Sleight of Hand) | ⏱ | Sleight of Hand +6 (+8 from L6 if he takes expertise). **Fast Hands (L3):** advantage. |
| **The spot** (find the right door, the false handhold, the loose stone) | Wisdom (Perception) | ⏱ | **Perception +6 (expertise).** |
| **The long haul** (carry a sack up the steps, hold on a bar for a minute) | Constitution saving throw | ⏱ | Ash's weak spot (+2). The rivals' strong one. |
| **The finish bell** (one last swing up to ring it) | Athletics or Acrobatics | ⬇ | Climb speed: advantage. |

**Sample Standard T1 course ("the Wharfmaster's Run," Emberford):** the barrels ⬇ (Acrobatics 12) · the cargo net ⏱ (Athletics or Acrobatics 12) · the sprint ⏱ (Athletics or Con 12) · the ribbon grab ⏱ (Sleight of Hand 12) · the tilting plank ⬇ (Dex save 12) · the bell ⏱ (Athletics or Acrobatics 12).

### 11.3 Knife-throwing
- **Format:** five daggers at five painted targets, **AC 12, 14, 16, 18, 20** (T1). Thrown dagger: Ash **+6**. Score = hits.
- **Weekly board** (Gauntlet-style): 1 sp a try, champion of the week (most hits, ties throw again at AC 18) takes **10 gp** (T1) / 50 / 250 / 1,000.
- **Rounds of a festival knife contest:** Round 1, the board (top 4 go through). Round 2, **moving targets** (a swinging plank: +2 AC). Round 3, **the trick throw**, one each, judged: pin a sleeve to the board without touching the arm (**AC 18**; a miss by 5 or more nicks the volunteer: the crowd gasps, and the judge disqualifies you), split a hanging cord (**AC 20**), or snuff a candle (**AC 17**).
- **Ash's features:** **Steady Aim (L3)** gives advantage if he hasn't moved (perfect for the board). Sneak Attack doesn't apply (no creature). **Luck Points** turn a miss into a hit.
- **Rivals:** +5 (a sailor), +6 (a circus thrower), +7 (a champion at T2).

### 11.4 Archery
- **Short round:** three arrows at **30 ft**, targets **AC 12 / 14 / 16**. **Long round:** three arrows at **100 / 150 / 200 ft**, targets **AC 13 / 15 / 17**. **Moving round:** three arrows at a target dragged on a rope or swung on a pole, **AC 15**, and a missed shot by 5 or more is a "wide" (penalty point for the crowd, nothing more).
- **Range matters:** a **shortbow** fires 80/320, so at 100 ft and beyond it shoots with **disadvantage**. A **longbow** (150/600) has no disadvantage until 150 ft... but **Ash isn't proficient** with longbows (2024 rogues aren't), so with a borrowed longbow he loses his proficiency bonus (+4 instead of +6). The choice is real: shortbow with disadvantage at long range, or longbow without proficiency.
- **Scoring:** 1 point a hit, **2 for a hit by 5 or more** ("the gold"). Top score wins; ties shoot one arrow at AC 18.
- **Trick shots** (finals, judged): split the apple on the post (AC 17), cut the ribbon (AC 19), shoot through the swinging ring (AC 18, and a Dex check DC 12 for timing first).
- **Ash's features:** **Steady Aim (L3)** (advantage if he hasn't moved this turn: every round except the moving one). **Luck Points.**
- **Prizes:** T1 festival archery: **25 gp** and a fletcher's prize (20 good arrows), Gauntlet weekly: 2 gp entry, pot split. Rivals: the Watch's best (+6), a hunter (+5), Grey Wolf archers (+7, T2).

### 11.5 Lock-picking (the Locksmiths' Race)
- **Format:** five locks on a board, **DC 10 / 12 / 14 / 16 / 18** (T1), against a sand-glass of **five "minutes."** Each attempt takes one minute. **Thieves' Tools: Ash +6.** Fail and retry costs another minute. Most locks opened wins; ties go to fewer minutes.
- **The final lock is trapped:** a needle (DC 13 **Perception** or **Investigation** to spot; a missed spot means a jab: 1 damage and **disadvantage on the next check**), or a jammer that snaps your pick if you fail by 5 or more (lose a minute fitting a new one).
- **Head-to-head final:** two pickers, two identical boxes, the same five locks: roll at the same time each minute; the crowd counts aloud. First to open the last lock wins.
- **Blindfold round** (finals or a separate contest): the same locks by feel, **+2 DC**, and the **Perception** trap-spot becomes **Investigation by touch** at the same DC.
- **Ash's features:** **Fast Hands (L3)** doesn't speed a contest (no combat turns), but **Reliable Talent (L7)** makes him nearly unbeatable from then on: the city files raise the locks to **Hard** (+2 DC) and add a second trap for T2+. **Luck Points.**
- **Legal note:** every city that runs one sets it in daylight, with the Watch watching and the locksmiths' guild running the book, because **everyone watching is also learning who the city's best picks are.** Winning one is a reputation, not just a purse (some nobles hire from the winner's list; some guards memorize it).
- **Prizes:** T1 entry 3 gp, prize **40 gp** and a masterwork pick set (+1 to Thieves' Tools checks, non-magical; the Locksmiths' Guild's own). Rivals +5 (a guild apprentice), +6 (a "retired" burglar), +8 (the guild's champion, T2).

### 11.6 More rogue contests (pick any, reskin to the city)

**Rooftop Race** (Gauntlet or straight race). Over the roofs from A to B with a dozen runners. **Five legs:** a ridge run (Acrobatics), a gap jump (Athletics, or automatic with Second-Story Work up to 15 ft... 18 ft with a run-up), a chimney climb (climb: automatic with climb speed), a slide down wet slates (Dex save ⬇), the drop to the street (Acrobatics to land; fail = 1d6 and a penalty). Each leg, the leader is whoever has the most successes; ties go to the higher roll. **Cunning Action Dash** gains one leg's lead once. Entry 2 gp, pot format. Rivals: Rook (+6 Acrobatics, cheats on the drop by shoulder-barging), roof-tilers (+5). **Ash's signature contest.**

**The Ribbon Pull** (the pickpocket's contest; run at fairs, half-legal, everybody loves it). Ten "marks" (actors with bells sewn into their coats and a ribbon tucked somewhere) walk a crowded square for one sand-glass. Pull as many ribbons as you can without a bell ringing. Each pull: **Sleight of Hand vs. the mark's passive Perception (11–15)**; fail by 5 or more and the bell rings and you're **out**. Most ribbons wins. **Stealth** to get close without being "spotted" (DC 12) gives advantage on that pull. Entry 1 gp, prize **25 gp** (T1) plus a silk purse. **Watch out:** the Watch also watches who wins this one.

**The Knife-Catch / Juggler's Show** (a showman's contest, judged). Three passes: juggle (**Sleight of Hand DC 12**), catch thrown knives (**Dex save DC 13**, a fail = 1d4 and the crowd groans), a finale (**Charisma (Performance)**: Ash is +4 untrained; **advantage** if the player describes something genuinely good). The judge scores each pass 0–3; best total wins. Prize: the crowd's hat (**2d6 × 5 gp**, T1). **Panache (L9)**: advantage on the finale.

**The Mast Climb / Cliff Climb** (a straight race up). Three stages, each **Athletics or Acrobatics**, DC 12 / 14 / 16, with a ⬇ fall (into water or a net) on a fail by 5 or more. **Climb speed (L3): advantage on every stage** and no fall on a plain fail. First to the top. Entry 2 gp, pot. Rivals: sailors (+6 Athletics).

**The Shell-Game Tournament** (hustlers' night; `§3` rules). Each round, two hustlers run the cups for each other: one runs, one watches; **Sleight of Hand (runner) vs. Perception (watcher)**; best of three rounds per pair, a knockout bracket of eight. **Ash runs at +6, watches at +6 (expertise).** Entry 5 gp; winner takes the entries (**40 gp** T1). Every sharp in town shows up, and they all cheat; spotting a cheat is **Insight DC 14**, and calling it right gets the cheat thrown out (calling it wrong gets *you* thrown out).

**Escape Artist's Chains** (a show and a contest). Locked in manacles, then a sack, then a crate in the river shallows (or a sealed barrel on stage). Three stages: **Dex (Sleight of Hand) or Thieves' Tools** for the manacles (DC 13; Ash has manacles of his own to practice on), **Acrobatics** to wriggle the sack (DC 12), **Athletics or Thieves' Tools** for the crate lid (DC 13), each against a sand-glass of three tries total, then **Con save DC 10 + 2 per extra try** if the crate's in water. Fastest out wins; the crowd's hat plus a purse (**30 gp** T1). Nobody actually drowns: the stagehands have hooks.

**The Night Climb** (an illegal contest, run by thieves, never written down). Climb into a locked, guarded building (usually a sponsoring merchant's empty warehouse; he's in on it for the publicity... or isn't), take a marked token, get out unseen. It's the quick heist (`§8.1`) run as a race against two rival crews. Pot: whatever the crews stake (**50 gp** T1). The law treats it as burglary, because it is.

### 11.7 Odds for named rivals (quick reference)
Use these bonuses for rivals in any skill contest at the tier shown, unless a city file names its own. A rival has **one specialty** (+2 more) and **one weakness** (−2).

| Tier | Ordinary entrant | Good rival | Champion |
|---|---|---|---|
| T1 | +3 | +5 | +6 |
| T2 | +5 | +7 | +8 |
| T3 | +7 | +9 | +11 |
| T4 | +9 | +11 | +13 |

### 11.8 Rewards and the treasure budget
Skill-contest purses come out of the **same side-activity allowance** as ring purses and hustles (§3.7, §5.3). **Rule of thumb:** a skill contest pays like an **undercard bout** of its tier (T1 20–40 gp), a festival final like a **main card**. A big win is a story, not a payday every week: the "no repeat entries in a month" rule and the travel schedule keep it honest.

### 11.9 Where the contests are (every city has at least two)
| City | File | Local skill contests |
|---|---|---|
| Emberford | 03 | Knife Wall (§2.3), Lamp-Climb (§2.2), **the Wharfmaster's Run** (Gauntlet), **the Locksmiths' Race** (Glimmerway, monthly), **Rooftop Race** (Fringe to Crownhill, Tenth-days, unofficial), **the Ribbon Pull** (Highwater Fair) |
| Hobb's Ferry | 04 | **Ferry-Rope Run** (Gauntlet over the ferry cables), **the Pike Shoot** (archery at fish-shaped targets on the water) |
| Driftmarket | 05 | **Barge-Hop** (Gauntlet across moving barges, Brutal at the festival), **Mast Climb** |
| Tollhaven | 06 | **The Eleven Locks** (the Purses' lock-picking prize, Hard), **Ribbon Pull** (Countinghouse Fair) |
| Bramblecog | 07 | **The Clockwork Gauntlet** (moving obstacles: +1 DC, and a Perception station every course), **Blindfold Lock** |
| Corriemount | 08 | **The Bell-Ringers' Challenge** (§3.2: a climb), **Bee-Skep Archery** (moving targets) |
| Copperhill | 09 | **The Pit-Head Run** (Gauntlet down and up a mine scaffold), **Knife-Throw at the Square** |
| Wolfsgate | 10 | **The Hiring Yard Trials** (archery and knife-throwing for contracts), **Escape Artist's Chains** (the Company's stockade) |
| Dun Morrach | 11 | **The Kettle Steps** (Gauntlet up the steaming spring terraces; Con stations), **Dwarven Lock-Box** (Brutal; the prize is respect and a dwarven pick set) |
| Kesselby | 12 | **The Wager Board's Rooftop Race**, **Shell-Game Tournament** |
| Highmarch | 13 | **The King's Archery** (festival, long rounds), **The Night Climb** (Lowtown, illegal) |
| Aranhollow | 14 | **The Canopy Run** (Gauntlet in the trees, Hard; elves +7), **Silent Arrow** (archery with a Stealth check before each shot) |
| Old Varrow | 15 | **Ring the Bell** (§3.1, a dare), **The Night Climb** (salvagers' version) |
| Saltreach | 16 | **The Rigging Race** (Mast Climb, three masts), **Escape Artist's Chains** (the harbor drop) |
| Saffra | 17 | **The Awning Run** (tabaxi Gauntlet over awnings and bell-ropes; tabaxi +8 climb and jump), **The Tumbling** (Acrobatics show, judged), plus Ch14's rooftop chase race |
| Tuskhold | 18 | **The Weight-and-Balance** (carry and balance stations), **Trunk-Throw** (knife-throwing at the elephant-folk's swinging targets) |
| Horngard | 19 | **The Maze Run** (Perception and sprint stations in the hedge maze), **Horn-Archery** (long rounds) |
| Hollowmere | 20 | **The Leaping Fair** (hare-folk Gauntlet: jump stations dominate; hare-folk +8 jump), **The Reed Run** (otter-raft Gauntlet across floating reed mats, Hard) |

---

## 12. STRANGE ARMS (CHG-22: the "never held one before" contest)

> **The pitch, in the world:** a traveling collector named **Odo Fairlie** ("the Collector," NPC-097) buys odd weapons from every corner of Eyrland, and later from Mirrowen, and stages contests where good shots and good throwers are handed something **none of them has ever used.** Nobody's proficient. Everybody's guessing. The crowd loves watching a champion archer fumble a bola. The player gets the fun of **working out a strange weapon in real time.**
> **Player-safe:** the format (Study, Practice, Challenge, Elimination) is public; locals know it. **The weapons are not.** Never list them for the player. Reveal each one when it's set on the table.

### 12.1 Common rules
- **No proficiency.** Every competitor attacks with **Dex or Str modifier only** (the weapon says which; finesse-like ones let you pick), plus **Feel** (below). Ash at L1: **+4**.
- **No magic, no familiars** (same as every contest). **Non-magical class features apply:** **Steady Aim** (L3) on ranged rounds where he doesn't move, **Lucky**, **Reliable Talent** on the Study check (L7). **Sneak Attack doesn't** (no creature).
- **Feel:** a bonus to every Strange Arms roll **with that weapon, that day**. It comes from Study and Practice, **stacks**, and is **capped at Ash's proficiency bonus** (+2 at L1–4, +3 at L5–8, and so on). It's "learning the thing," and the cap is on purpose: by the end of the day he's as good as if he'd trained, never better.
- **Tier DCs:** written for **T1**. **+2 per tier** to every target AC and DC; purses as §11.1.
- **Every weapon has a Quirk** (a built-in way to fumble it) and a **Hidden Trick** (a way to use it that the demonstrator doesn't mention). Finding the Trick is the swingy moment of the day.

### 12.2 The four phases (about 20 minutes at the table)

**1. STUDY (one roll).** The Collector sets it on the table and says one line about where it's from. Each competitor gets a minute to look it over, heft it, or watch the demonstrator's single throw. Ash picks **one**:
- **Intelligence (Investigation) DC 12:** take it apart with your eyes.
- **Wisdom (Insight) DC 12:** watch the demonstrator's hands, not the weapon.
- **A relevant tool, DC 10:** Thieves' Tools for anything with a catch or trigger; Tinker's Tools for clockwork; Weaver's/Leatherworker's for cords, nets and whips; Smith's for iron. (Zeke's or Gideon's advice counts as flavor only; they're not competing... unless they enter, which they may.)
- **Results:** **Success:** Ash learns the **Quirk** (he's immune to it all day) and gets **+1 Feel**. **Success by 5+:** also a **hint** at the Hidden Trick (tell the player one true sentence about it), and his Trick-discovery range widens (below). **Failure:** no Feel, and the Quirk bites the first time it can.

**2. PRACTICE (three shots).** Three practice attempts at a plain target (**AC 12**). **Each attempt, hit or miss, gives +1 Feel** (to the cap). Describe each one: what went right, what went wrong.
- **Discovering the Hidden Trick:** a practice roll of **natural 18–20** (or **15–20** if Study succeeded by 5+) reveals it. The player may also **describe trying something specific**; if it matches the Trick's description, he finds it automatically. **Reward the player who thinks about the weapon.**
- **Bart** heckles from the rail, because he can't compete. (Bart: "You're holding it upside down." He's lying about half the time. Roll a d6: on 1–3 he's right.)

**3. CHALLENGE ROUND (everyone).** Each competitor shoots the weapon's **target course** (each weapon lists one: usually 3–5 targets of rising AC). Score = hits (**2 for a hit by 5+**). The **bottom two** go to elimination (in a field of 6; with 8, the bottom four go to two duels). Using the **Hidden Trick** on its target scores **3**.

**4. ELIMINATION (head to head).** Two competitors, the same weapon (or **a new one**: the Collector's favorite twist, which resets Feel to 0 and runs a quick Study and one practice shot first). **Best of three targets, alternating shots, ties shoot again at AC 18.** Loser goes home. Repeat until **the final two** shoot the **showpiece course**: moving targets, a trick shot, and the crowd on its feet.

**Field:** 6 competitors (T1), 8 (T2+). Ash is one; the rest come from §12.4 and the city's own rivals. **Roll rivals for real at the elimination stage**; earlier, use §11.7 bonuses and the d6 pass table if you need speed.

**Prizes:** Entry **5 gp** (T1) / 25 / 100 / 400. **Winner:** the purse (**60 gp** T1 / 300 / 1,200 / 4,000) **and the day's weapon** (a fine mundane example, worth the listed price; sometimes the magic version, as each weapon says). Runner-up: a quarter of the purse. **Circuit points:** 3 for a win, 2 for the final, 1 for reaching elimination and surviving one duel.

### 12.3 The weapons (14; three are Mirrowen's and appear only once Act II opens the way)

Damage is for completeness (ring and contest use is targets only; if Ash buys one, it's a real weapon). **Proficiency:** once Ash **wins** with a weapon, or practices it for a week of downtime, treat it as a Simple weapon he's proficient with (DM's call; it's a reward, not a loophole).

| # | Weapon (where from) | How it works | Quirk | Hidden Trick | Target course (T1) | Prize / buy |
|---|---|---|---|---|---|---|
| 1 | **Kettle-sling** (Dun Morrach: a staff-sling the dwarves use to lob hot stones up the spring terraces) | A 5-ft staff with a sling pouch at the tip; two-handed overhead whip. **Str or Dex**, 1d6 bludgeoning, range 60/240. | Releases late if you think of it as a sling: **first shot goes straight up** (automatic miss) unless Study succeeded. | **The skip:** bounce the stone off flat rock to hit a target behind low cover; ignores half cover, and the "behind the wall" target (AC 16) scores 3. | 3 clay pots on posts at 60 ft (AC 12/14/16) and one behind a low wall (AC 16) | 15 gp mundane. Hakon (Iron Kettle) sells them and will lecture. |
| 2 | **Spring-bow** (Bramblecog: gnomish clockwork repeating crossbow) | Crank winds a spring; holds 4 bolts. **Dex**, 1d6 piercing, 60/240, **fires twice per Attack action if you didn't move**. | **Jams** on a natural 1 or 2 (lose the next shot clearing it). | **Half-wind:** a quarter-crank turn fires a weak bolt with no jam chance; perfect for the "ring the bell" target (a hit by any margin scores 3). | 4 rapid targets that pop up (AC 13 each, 2 attempts per turn), then the bell (AC 17) | 75 gp; the **+1 version** is the circuit final prize option. Nim Gearwright drools over it. |
| 3 | **Shepherd's knot** (the Hobbland: gnome sheep-herders' bola) | Three cords, three weights; whirl and throw at legs. **Dex**, range 20/60. A hit on a creature: **DC 12 Str save or prone and speed 0** until it uses an action to free itself. | **Needs two full whirls:** if you moved more than half your speed this turn, disadvantage. | **The low throw:** aim at the ground just in front; it skips up and wraps. +2 to hit the "running post" (a sledge dragged across the yard). | Tangle 3 posts (AC 12/14/16), then the running post (AC 16) | 5 gp. Pip will want one. **Combat use is legitimately good** for a rogue; that's a fine prize. |
| 4 | **Drift hook-and-cast** (Driftmarket: the river clans' net on a hooked pole) | A 10-ft hooked pole in one hand, a weighted casting net in the other. **Str or Dex**; net: range 10/15, Restrained (DC 10 Str to escape); hook: reach, 1d4, pull 5 ft. | **The net spreads with the wind:** roll a d6 before each cast; on a 1 it drifts 5 ft left. | **Cast-and-hook:** net first, hook the net's drawline the same turn and haul the whole catch in: the "bag the buoy" target (a floating barrel, AC 16) scores 3. | Net 3 floating buoys (AC 12/14/16), then haul a buoy to the jetty | 10 gp. The otter-folk use something almost identical (Ch14 callback). |
| 5 | **Harpoon-thrower** (Saltreach and the Salt Isles: a throwing-stick that hurls a lined harpoon) | A notched stick that throws a light harpoon on a line. **Str or Dex**, 1d8 piercing, range 40/160. Line: retrieve as a bonus action. | **The line tangles** on a miss by 5+: lose the next shot. | **The rope return:** throw past the target and yank the line so it swings back in (hits a target **behind** you or around a mast: AC 17, scores 3). | Three hanging fish-shapes at 40 / 80 / 120 ft (AC 12/14/16), then the mast-shot | 12 gp. Saba Mercer's own weapon at home; she's terrifying with it. |
| 6 | **Company whip** (Wolfsgate: a Grey Wolf drover's lead-tipped war-whip) | **Dex**, reach 15 ft, 1d4 slashing. Can **disarm** (contest vs Str/Dex) or snuff a flame. | **The crack comes back:** a miss by 5+ snaps back at you (1 damage, and the crowd howls). | **The wrap:** wrap a post and pull yourself or swing across a gap (the "creek swing" scores 3). Also snuffs two candles with one crack. | Snuff 3 candles at 10/12/15 ft (AC 12/14/16), then the creek swing (Acrobatics DC 13 after a hit vs AC 14) | 2 gp, mundane. A nice prize for Gideon to disapprove of. |
| 7 | **Pit-chain** (Copperhill: a weighted miners' chain thrown from scaffolds to snag loads) | 10 ft of chain with a pear-shaped weight. **Str**, 1d6 bludgeoning, range 10/20, or reach 10 ft. | **Heavy:** Dex users take −2 unless they discover the Trick. | **The pendulum:** let it swing and only *steer*: use **Dex** with no penalty and +1. (The miners know; the Collector doesn't.) | Knock 3 ore-buckets off hooks (AC 12/14/16), then the swinging bucket (AC 17) | 5 gp. Copperhill's Champion's Bout bans it ("too mean"). |
| 8 | **Whisper-tube** (Aranhollow: the elves' silent blowpipe for birds) | **Dex**, 1 piercing, range 25/100, **near silent** (no Stealth penalty to stay hidden after firing). | **Breath:** each shot past 25 ft needs a **DC 10 Con save** or it drops short. Ash's weak spot. | **The held breath:** skip a turn's attack to breathe deep; the next shot ignores the Con save and crits on 19–20. | Darts into 3 hanging leaves at 20 / 40 / 60 ft (AC 13/15/17), then the "between the bells" shot (hit without ringing two bells on either side: AC 18) | Elves don't sell them. Win one, or earn it in Ch17. A **Whisper-tube of Sleep** (darts of *Sleep*, Uncommon, 400 gp) is the circuit's sealed favorite prize. |
| 9 | **Return-iron** (Old Varrow: an ancient curved bronze throwing blade, dug out of the marsh by salvagers; nobody alive has used one) | **Dex**, 1d6 slashing, range 30/90. **Comes back** to your hand on a miss if you catch it. | **Catching it:** DC 12 Dex save when it returns, or **1d4 to you** and it clatters into the crowd. | **The curve:** throw it wide so it bends around an obstacle (hits the target behind the pillar, AC 17, scores 3). | 3 stakes at 20/40/60 ft (AC 12/14/16), then the pillar shot | Priceless as an antique (**150 gp** to a collector; the Collector bids). The Old Varrow pop-up has one; a second one is in Ch18's ruins. |
| 10 | **Skimming ring** (the Salt Isles: a flat bronze ring sailors spin across water to cut lines) | **Dex**, 1d4 slashing, range 30/120; **skips off water** once to extend range. | **Spin:** without the wrist-snap (Study), disadvantage beyond 30 ft. | **The double skip:** two skips off calm water, hits the "far rope" (AC 18) and cuts it: scores 3, and the flag on it drops into the harbor. | Cut 3 ropes over water at 30/60/90 ft (AC 13/15/17) | 8 gp; Saltreach dockside. |
| 11 | *Reserve slot* | Reuse any weapon above with **a new course** (e.g. the Kettle-sling: smash the dwarven lantern shades without breaking the glass globes beneath; Trick needed), or a weapon a chapter introduces. | | | | |
| 12 | **Bell-chain** (Saffra, Mirrowen: the tabaxi dancer-fighters' chain with bells and a hook) — **Act II+ only** | **Dex**, reach 10 ft, 1d4; the bells **jangle** loudly. | **Noisy:** disadvantage on any Stealth roll that turn. | **The jangle feint:** ring it on purpose before striking; the target (a dummy rigged by the tabaxi to "flinch") opens: advantage, and the "cat's eye" target (AC 18) scores 3. | Hook 3 rings off posts (AC 14/16/18), then the cat's eye | 30 gp in Saffra. Tabaxi rivals get +2 with it. |
| 13 | **Stone-bow** (Tuskhold, Mirrowen: the elephant-folk's pellet bow, a heavy bow that throws stones) — **Act II+ only** | **Str**, 1d8 bludgeoning, range 80/320, **needs Str 13** or disadvantage (Ash has 13: just enough). | **Draw weight:** after two shots in a row, DC 12 Con save or disadvantage on the third. | **Low arc:** shoot it flat, skimming the grass; it rolls on and hits the "rolling gourd" (AC 17, moving), scoring 3. | 3 hanging gongs at 80/160/240 ft (AC 14/16/18), then the rolling gourd | 40 gp. Elephant-folk don't race; they *remember* scores, all of them, forever. |
| 14 | **Herd-crook** (Horngard, Mirrowen: the minotaur herders' long crook) — **Act II+ only** | **Str or Dex**, reach 10 ft, 1d6; hook to **pull a target 10 ft** or trip (contest). | **Long:** two-handed, and you can't use it within 5 ft. | **The calf-lift:** hook and *lift* rather than pull: the "lamb" (a straw bundle, Medium, 40 lb) is lifted clear of the pen rail in one smooth move (Athletics DC 13 after the hook), scoring 3. | Hook 3 straw lambs out of a pen (AC 14/16/18), then the lift | Not sold; given. A minotaur who sees Ash use one well will gift him one, and it means something in Horngard. |

*(Item 11 is a deliberate reuse slot so the DM always has a 14th draw; swap in any weapon the chapters introduce.)*

### 12.4 Strange Arms rivals (Top Shot types; reuse at every stop, scaled by §11.7)

| Rival | Type | How they play | Bonus (T1 base) |
|---|---|---|---|
| **Odo Fairlie** (NPC-097), the Collector | Host, not a competitor | Plump, delighted, sixty, a magnifying glass on a chain, travels with a cart of locked cases. Talks to every weapon like an old friend. "Now *this* one has a temper." Fair, but loves a twist. Never cheats; does **swap weapons mid-elimination** when the crowd's bored. | — |
| **Sergeant Garnet Haddow** (NPC-098) | **The Veteran** | Grey Wolf Company crossbow sergeant, 50s, scarred, methodical. Starts **+2 Feel on anything with a trigger** but **gains only +1 total from Practice** (set in her ways). Hates whips. | +5 (+7 with triggers) |
| **Saba Mercer** (NPC-099) | **The Natural** | Saltreach harpooner, late 20s, laughs a lot, never studies. **Study automatically fails; Practice gives +2 Feel each** (cap still applies). Terrifying with anything thrown. | +5 (+7 thrown) |
| **Dilly Bellamy** (NPC-100) | **The Scholar** | Bramblecog gnome, 40s, notebook, asks the Collector a hundred questions. **Study automatically succeeds by 5+**; physically weak (−2 on Str weapons). Shares what she learns with anyone polite (Persuasion DC 12: Ash gets her Study result). | +4 (+6 with clockwork) |
| **Lord Teddy Rowntree** (NPC-101) | **The Showboat** | A Highmarch lordling slumming the circuit, 20s, very handsome, very loud. **Advantage on every Trick shot attempt; disadvantage on any roll while behind.** The crowd adores him. The Final's villain-for-a-day, not a real villain. | +5 |
| **Pashi Two-Rivers** (NPC-102) | **The Wanderer** (Act II+, Saffra on) | Tabaxi collector-competitor, the Collector's friendly rival and best customer. Knows half the weapons already (**+2 Feel** on Mirrowen ones). Gossips to Ash between rounds; a good source for Saffra rumors. | +7 (T3) |
| **Rook** | **The Rival** (Emberford only) | Enters the first Strange Arms day in Emberford because Ash did. Treat as a Natural with +5. If he beats Ash he will never, ever stop talking about it. | +5 |
| Local entrants | as the city file | | §11.7 |

### 12.5 The Strange Arms Circuit (recurring, with a final)

The Collector runs a **circuit** across the river country, and later across the water. Each stop is one Strange Arms day (three weapons drawn from his cases; one is always new).

| Stop | Where / when | Tier | Notes |
|---|---|---|---|
| **1. The Strangers' Booth** | **Emberford, Highwater Fair** (Ch4 side-activity window; also offered in Ch5's window if Ash missed it) | T1 | The Collector arrives with the Fair. Weapons: draw from 1, 3, 6, 7. Rook enters. **The Lane comes to watch.** First prize: 60 gp + the weapon. |
| **2. The Purse Cup** | **Tollhaven, the Grand Wager** (Ch8–10 window) | T2 | A Purse sponsors it (the Collector's patron). Bets are enormous. Weapons: 2, 4, 5, 10. |
| **3. The Hiring Yard Strangers** | **Wolfsgate** (Ch10 window) | T2 | Garnet Haddow's home stop. The Company **hires** the winner for a day (a contract worth 100 gp). Weapons: 2, 6, 7. |
| *(exhibitions)* | Dun Morrach (Ch10: the Kettle-sling only; the prize is respect), Old Varrow pop-up (salvagers; the Return-iron) | T2 | Not circuit points; side fun. |
| **4. The Far Booth** | **Saffra** (Ch14 window) | T3 | **Mirrowen's weapons arrive:** 12, 13, 14 plus one Eyrland weapon for the tabaxi to fumble (they love that). Pashi joins. |
| **5. FINAL: the Stranger's Crown** | **Highmarch, the King's Tourney** (Ch17 window) | T4 | Eight finalists (anyone with **5+ circuit points**, or any stop's winner). Three rounds, all Elimination; the Collector brings **a weapon nobody has ever seen**, not on the list (DM's invention: make it from the world, e.g., a dwarven tuning-fork bolt that hums on target, or a Gate War relic). **Prize: 2,000 gp and the champion's pick of a Rare magic weapon from his case** (4,000 gp value; pick one that suits Ash: a **+2 dagger**-equivalent throwing iron, or the +1 Spring-bow and 1,000 gp more). **This counts against Act III's treasure budget.** |

**Missing stops is fine.** The final takes anyone who won a stop. If Ash never enters, the Collector still turns up in Ch17's crowd, recognizes the Fenwick name ("Your brother fumbled my whip at Wolfsgate"), and invites him anyway.

---

## 13. Novel rogue contests (CHG-22)

> **The idea:** contests the player hasn't heard of. Each is short (two to five rolls), has a clear choice at every step, and has one swingy moment. Each says its **player-safe** status. **Five are player-safe** (the player was told about them in chat): **The Switch, Shadow-Tail, the Lamp Run, Who's the Duke, the Moth Post.** The rest are **sealed for discovery**: don't announce them; let him find them in a city.
> All use §11 common rules (no magic, no familiars **except the Moth Post**), T1 DCs (+2 per tier), §11.7 rival bonuses, and the side-activity budget.

### 13.1 THE SWITCH (player-safe)
**Swap a marked object for a fake, right under the judges' noses.** On a table: a jeweled egg (or a seal, a ring, a dwarven token: local flavor). Three judges stand around it. You get a convincing fake.
- **Setup (choose one):** distract (**Deception or Performance DC 13**: one judge looks away), crowd (**Stealth DC 13**: you get to the table unnoticed), or straight nerve (no setup; the swap is at disadvantage).
- **The swap:** **Sleight of Hand vs. the judges' best passive Perception (13)**, +2 per judge still watching.
- **The walk-away (swingy):** a judge picks up the egg and examines it. **The fake holds** if Ash rolls **Deception DC 13** to keep a straight face, **or** if he bought the good fake (5 gp more at registration, which the judges allow: "a craftsman's contest too").
- **Score:** clean swap and the fake holds = win. Judges catch it = out. Catch *another* contestant's swap and call it (**Insight DC 14**) = a bonus share.
- **Entry 3 gp; prize 50 gp (T1)** and the real object's replica as a trophy. **Rivals:** a Tollhaven counting-house clerk (+6 Sleight), Old Merrit (+6), Rook (+6, always picks "crowd").

### 13.2 SHADOW-TAIL (player-safe)
**Follow a hired "rabbit" through a crowded market for an hour without being spotted.** The rabbit is paid **1 gp per tail she catches**, so she's trying.
- **Four stretches** (each one quick choice + roll): the crowd (**Stealth DC 12**), the doubling-back (**Perception DC 13** to notice she's turned around before she sees you), the change (she swaps coats in a shop: **Investigation or Perception DC 14** to pick her out), the last alley (**Stealth DC 15**; she stops and listens).
- **A failure isn't out:** she gets a "glance." **Two glances = she points and calls "Tail!"** and you're out. A **natural 20** on any stretch gets a bonus: you learn something the rabbit wasn't meant to show (she meets someone; local plot hook, or just gossip).
- **Disguise (Charisma (Deception) DC 12 once, before you start)** erases one glance.
- **Entry 2 gp; pot format** (§11.1). Typically 1–2 of 10 tails make it. **The rabbits are retired spies, actors, or a Copperhill Seat's "shadows."** Rivals: Magpies, a Toll Guard runner, an elf (Aranhollow's Leaf-Follow: Perception +8 rabbit, Hard).

### 13.3 THE LAMP RUN (player-safe)
**A night rooftop race: tap the city's lamps in a set order.** The Lamplighters' apprentices run it once a month (unofficially). Ten numbered lamps across the roofs; tapping one lights it **blue**, and if you tap one **out of order** it flashes **red**, and everyone below sees.
- **Five legs**, each two lamps: a ridge run (**Acrobatics DC 12**), a gutter climb (**Athletics DC 12**, automatic with climb speed), a wide street gap (**Athletics DC 14**, or jump distance with Second-Story Work), a swinging sign (**Dex save DC 13**), the dome (**Acrobatics DC 15**).
- **The choice each leg:** the **safe route** (as written) or the **short route** (+3 DC, but you gain a leg on the field). **Order:** every leg, a **Perception DC 11** to spot the next number painted small on the lamp's bracket. Fail and you tap the wrong one: **red flash**, one penalty, and you must come back for it.
- **The Watch** below: two red flashes and a whistle blows; one more and you're running from them, not racing.
- **Entry 2 gp; pot.** Rivals: Lamplighters' apprentices (+5 Athletics, **+2 knowing the order**), Rook. **In Emberford it's the Fringe to Old Ford; the last lamp is above the Ford Stone.**

### 13.4 WHO'S THE DUKE (player-safe)
**A masquerade game for the rich.** Four "impostors" (contestants) go into a masked ball pretending to be a guest, a servant, a musician or a lord; four "hunters" (paid) roam the floor for two hours trying to spot them. Hunters tap a shoulder and say "Your Grace?" If they're right, you're out.
- **Pick your cover** (each favors a skill): Guest (**Persuasion**), Servant (**Stealth**), Musician (**Performance**; Ash isn't trained: −), Lord (**Deception**, and the hunters look hardest at lords).
- **Three "moments"** (each a roll at DC 13 vs. the cover's skill): the arrival, a conversation that goes wrong (a real guest asks a question only a real guest would know: **History or Insight DC 14** or bluff at disadvantage), and the hunter's pass (**Deception vs. the hunter's Insight +5**).
- **Swingy moment:** once per night, Ash may **accuse another guest** of being an impostor to deflect a hunter (**Deception DC 15**; if they're a real guest, it's a scene).
- **Win:** last impostor uncaught at midnight, **or** spot the hunters first (**Insight DC 15**; tell the judge and he gets a bonus).
- **Entry 10 gp (it's a rich man's game; T1 Emberford Assembly Rooms or Tollhaven's masquerade tables); prize 80 gp** and an invitation that's worth more. Rivals: a Purse heir (+6 Deception), an actress (+7 Performance).

### 13.5 THE MOTH POST (player-safe; familiars allowed)
**Emberford's message-moths race... against everybody's pets, familiars, birds and the odd cat.** Each racer's courier must carry a sealed note from the Guildhall steps to a named house across the city and bring back a reply. The owner can't touch the courier after the start.
- **Three legs:** the launch (**Animal Handling** or, for a familiar, **Ash's Charisma** check DC 12: does it go the right way?), the city (the courier's **Perception or Dex** vs. DC 13: kites, cats, gulls, a sudden Lamplighter), the reply (the recipient must be found: **Ash's Investigation DC 12** to have named the right house at registration).
- **Bart's complication (the comedy):** before each leg roll a d6. On **1–2 Bart negotiates** (he wants a fee: a sausage, an apology, "say I'm handsome in front of Gideon"). Ash can pay it (automatic success on that leg) or refuse (disadvantage). On a **6 Bart heckles a rival courier** and the rival takes disadvantage.
- **Bart's form swap is legal** (he's not in combat): a **rat** is slow but can't be stopped by birds; Bart picks.
- **Entry 1 gp; prize 20 gp** and a brass moth pin. **Rivals:** a Lyceum student's pigeon (+5), the official message-moths (+6, no personality, cheat by flying straight), Nim Gearwright's clockwork sparrow (+4, falls apart on a 1, the crowd loves it). **Elsewhere:** Hollowmere's **Burrow Post** (hare-folk messengers race in tunnels; T1/T3; the Warren Mothers judge).

### 13.6 CANDLE-AND-BELL (sealed: discovery)
Cross a dark hall strung with **bells on threads** and set with **forty lit candles**, from one door to the other, without **ringing a bell or blowing out a candle**. Judges in the gallery count.
- **Four crossings** (each a choice between two paths): the threads (**Perception DC 13** to see them; then **Acrobatics DC 13** to step through), the candle aisle (**Stealth DC 12**; your passing draught: a fail by 5+ snuffs one), the stair (**Dex save DC 12**), the last door (**Thieves' Tools DC 13**, quietly).
- Each ring or snuff is a **mark**; three marks and you're out. Fewest marks wins.
- **Twist:** the judges cut one thread at random each round, and a bell falls and **rings by itself**; Ash can claim it wasn't him (**Deception DC 12**).
- **Variants:** Wolfsgate's **Picket Test** (cross a line of "sleeping" Company pickets with bells on their boots; the prize is a scout's contract), Corriemount's **Silent Crossing** (cross the chapter house during vespers; the abbot judges; prize: a blessing and a jar of the good honey).

### 13.7 STEAL THE PURSE (sealed: discovery)
**A legal festival heist.** A lockmaker (or a rich patron) displays a **purse of gold** in a glass case in a booth for a whole festival day and dares anyone to steal it. It's the quick heist (§8.1) as a **sanctioned** contest: the Watch stands down; the booth's guards don't.
- **Rules:** no violence, no magic. If you're caught, you pay a 5 gp fine and buy the guards a drink. **If you get it out of the booth, it's yours** (**100 gp** T1), and the lockmaker gets the best advertising of his life whether you win or not.
- **The swingy moment:** the lockmaker's **new lock** (DC 17; one try; a trapped dye-needle marks your hand blue for a week: everyone knows you tried).
- **Where:** Emberford (Ford Festival; the Locksmiths' Guild's booth), Tollhaven (the Seal-Breaking, as a Purse's showpiece).

### 13.8 THE WEIR RUN (sealed: discovery)
**Ride a barrel down a mill weir.** The village pays out to anyone who rides the old weir in a cask and comes up holding the flag.
- **Three drops** (each **Acrobatics or Con save DC 12/14/16**: you choose which every drop), a fail is **1d6 bludgeoning** and a **mark**; two marks and you're fished out by the miller's sons. A **natural 1** on the last drop: the barrel splits, swim (**Athletics DC 12**) and the crowd roars anyway.
- **The flag:** at the bottom, grab the flag on the pole (**Sleight of Hand or Athletics DC 13** while spinning).
- **Entry 1 gp; pot.** **Hobb's Ferry** runs it at the old mill weir on Rope-Breaking day; **Saltreach's Tide-Race** is the harbor version (T4: DC +6, and the tide is the weir).

### 13.9 THE GLASS MAZE (sealed: discovery)
**A gnome mirror-maze with a hunter inside.** Contestants enter; a "Minotaur" (a gnome on stilts in a horned helmet, very proud of it) hunts them by sight. Get out the far door without being tagged.
- **Four turns**, each a fork: **Perception or Investigation DC 13** to read which mirror is a door; a fail is a dead end and the hunter gains a step. The hunter's tag is **Stealth vs. his Perception (+4)**, rolled whenever he gains three steps.
- **Swingy:** the gnomes **rotate the mirrors** mid-run (once): everyone's map resets, and a **natural 18+** on the next check means you saw them do it.
- **Entry 2 gp; prize 30 gp** and a pocket mirror that's slightly enchanted (it always shows the room behind you: a Common item, 100 gp value). **Bramblecog only** (Contraption Fair).

### 13.10 PATTER NIGHT (sealed: discovery)
**Sell a worthless thing to a crowd.** Each contestant gets the same rubbish (a chipped teapot, a bent spoon, a jar of river water) and five minutes on a barrel. The crowd's coins are the score.
- **Three beats:** the hook (**Performance or Persuasion DC 12**; Ash may use Persuasion), the story (**Deception DC 13**: where it came from; **the player tells the story out loud** and a good one gets advantage), the close (**Persuasion vs. the crowd's Insight +3**).
- Each success = **1d6 gp** from the crowd; a **20** = a buyer pays **5d6** and wants another one tomorrow.
- **Swingy:** a heckler (a rival's plant) calls you a fraud: **Intimidation or Performance DC 13** to turn the crowd, or lose a beat.
- **Driftmarket** (Swap Deck night) and **Saffra** (the tabaxi call it a "small telling" and judge the story, not the coins: tabaxi rivals +8).

### 13.11 COPPER TO CROWN (sealed: discovery)
**Start with one copper at dawn; trade up across the city; whoever holds the most valuable thing at dusk wins.** No buying, no stealing (that's the rule, and judges follow you).
- **Five trades** (each a scene the player plays briefly): pick a mark (street, market, guild, Crownhill, an odd one the DM invents), roll **Persuasion or Deception DC 12/13/14/15/16** (rising), and on a success the item's value roughly **triples**. A **natural 20** finds a "sleeper" (something worth far more than either side thinks).
- **Fail:** the trade goes sideways (you end up with a goat; the goat is a scene).
- **Winner:** the highest value at dusk, judged by a pawnbroker (Jory, in Emberford, who is *thrilled* to judge). **Entry 1 gp; prize 50 gp, and you keep whatever you ended with.**
- **Where:** Emberford (Market Steps, monthly), Driftmarket (**One Knot to a Boat**, barter only: start with a knot of string), Kesselby (the Wager Board's version, mining scrip).

### 13.12 THE PLANT (sealed: discovery)
**Pickpocketing in reverse.** Each contestant gets a marked brass token and must **plant it** on a named judge (a fussy guildmaster, a priest, a Toll Guard captain) without them noticing, then tell the judge where it is at the closing bell.
- **Three steps:** get close (**Stealth or Deception DC 12**), plant it (**Sleight of Hand vs. the judge's passive Perception 13**; **advantage** if Ash says *where* and it's clever: a hatband, a sword scabbard, the judge's own collection plate), survive the pat-down (the judge searches himself once at noon: **the planted spot holds on Sleight of Hand DC 14**, or Ash's description was clever enough).
- **Best plant wins** (the judge votes on cleverness). **Entry 2 gp; prize 30 gp.** **Bramblecog** (planting on the lottery judge is a tradition), **Saltreach's Customs Plant** (smugglers' version: plant a "contraband" token on a customs man; illegal, very popular, T4).

### 13.13 Placement (every city gets one or two)

| City | New contests (and local twist) |
|---|---|
| **Emberford** | **Strange Arms** (Highwater Fair, circuit stop 1), **the Lamp Run** (monthly, Fringe to Old Ford), **the Moth Post** (Tenth-days, Guildhall steps), **Copper to Crown** (monthly), **Steal the Purse** (Ford Festival), **Who's the Duke** (Assembly Rooms, Lantern month: Act I–II) |
| Hobb's Ferry | **The Weir Run** (old mill weir; Rope-Breaking day) |
| Driftmarket | **Patter Night** (Swap Deck), **One Knot to a Boat** (Copper to Crown variant) |
| Tollhaven | **Strange Arms** (Grand Wager, stop 2), **The Switch** (the counting-houses: swap a seal), **Who's the Duke** (masquerade tables), **Steal the Purse** (Seal-Breaking) |
| Bramblecog | **The Glass Maze** (Contraption Fair), **The Plant** (Drawing day) |
| Corriemount | **Candle-and-Bell: the Silent Crossing** |
| Copperhill | **Shadow-Tail: the Seat's Shadows** (the town's champion keeps "shadows"; they're the rabbits); a **Pit-chain** exhibition |
| Wolfsgate | **Strange Arms** (Hiring Yard, stop 3), **Candle-and-Bell: the Picket Test** |
| Dun Morrach | **Strange Arms exhibition** (the Kettle-sling; respect, not gold) |
| Kesselby | **Copper to Crown** (scrip version) |
| Highmarch | **Strange Arms FINAL: the Stranger's Crown** (King's Tourney), **Who's the Duke** (the court version: T4, the King's own steward hunts) |
| Aranhollow | **Shadow-Tail: Leaf-Follow** (tail an elf through the canopy; Hard) |
| Old Varrow | **Strange Arms pop-up** (salvagers; the Return-iron) |
| Saltreach | **The Tide-Race** (Weir Run), **the Customs Plant** (The Plant) |
| Saffra | **Strange Arms** (stop 4, Mirrowen weapons), **Patter Night: the Small Telling** |
| Tuskhold | **The Switch: the Rememberer's Stones** (swap one stone in a pattern of a hundred while elephant-folk watch; they remember everything: **Brutal**, DC +4; the prize is a story about you told forever) |
| Horngard | **The Lamp Run: the Beacon Run** (light the highland beacons in order, on foot, at night) |
| Hollowmere | **The Moth Post: the Burrow Post** (hare-folk messenger race in the tunnels; Bart hates tunnels) |

---

## 14. The Tavern Board (CHG-23: a living leaderboard)

> Every city can have one; **Emberford's is the Long Wall at the Willow** (`03-emberford.md` §10 has the day-one standings and the rivals' numbers). It's flavor first and a light mechanic second: the player should feel he's **one of the regulars** in a scene full of named rivals whose numbers move while he's away.

### 14.1 What's on a board
1. **Jobs** (from §7, copied by the landlord), 2. **What's coming** (the contest calendar with entry fees, from the city file and §9), 3. **Tavern Champs** (one current holder per contest type), 4. **The season race** (points; the Willow calls it **the Willow Cup**).

### 14.2 Points and titles
- **Points:** win **5**, second **3**, "in the money" (passed a Gauntlet, reached elimination in Strange Arms, won a bout on the undercard) **1**. **Festival contests and circuit stops count double.** Ring bouts count by format (each format is its own title).
- **Titles:** winning a contest takes its title. A holder who **doesn't defend** (enter) for **two contest nights** is wiped and the title goes vacant. A title can be **challenged** in the tavern on any night for a 1 gp side bet (a straight contest from §11; the crowd decides the terms).
- **The season:** Lantern Night to Lantern Night. The leader takes the **jar** (a silver per round bought on contest nights: **40–60 gp** at the Willow) and a name painted on the beam. Second and third get drinks on the house for a month. **Ash's name on the beam is a real, cheap, lovely campaign goal**: use it.

### 14.3 Making it live (between sessions)
- **Per in-game week, roll a d6 for each board rival** (it's ten rolls; do it in one code block at wrap-up):
  - **1–2:** nothing. **3–4:** +1 point. **5:** +3 points (a second place somewhere). **6:** +5 points, and if the rival's **specialty title** is held by someone else, roll a contest: rival's bonus vs. the holder's (d20 each); the winner keeps or takes the title.
- **Rivals have a specialty (+2) and a weakness (−2)** (`03` §10 lists them). Use their bonus whenever they appear in a contest Ash enters: roll them for real.
- **Ash's points** come only from contests actually played. Never move his line off-screen.
- **Movement is news.** When Ash walks into the tavern after a few days away, **tell him one change on the wall** ("Lenny Swann's name is over Jenny's on the Plank now, and she's not speaking to anyone"). Rivals react to Ash's wins (Rook especially; R-037).
- **Away from home:** the board keeps running. Ash's line freezes. When he comes back after months, the season may be over: tell him who won the jar, and let it sting or delight.

### 14.4 The economics (keep it a meager living at T1)
- **The player's framing (locked):** Ash isn't good enough to be a professional, and **the real pro circuits are closed to him**: jousting lists, the King's Tourney lists, Tollhaven's Golden Cage title fights and the noble archery are for lords' sons and sponsored men. He **wins sometimes, places often enough to get his fee back**, and that plus odd jobs and quiet theft keeps the brothers' house fed. **It is not always on the up and up, and he has no legit job.**
- **Budget check (T1):** a normal week of contests costs Ash **4–8 gp** in fees and returns **0–30 gp**; **expected net about +5 to +10 gp a week**. The Fenwick house runs on roughly **1 gp a day** for three men (food, fuel, saving for the house tax), and Gideon's door wages cover most of it. Ash's contest money is the difference between eating meat on Restday and not. **Don't let contests become the treasure engine:** a T1 jackpot (a 60 gp Strange Arms win, a lone Gauntlet pass) is a celebration and a scene, not a weekly event. §11.8 and §3.7 caps still apply.
- **T2+:** fees and purses rise with tier (§11.1), and by then Ash's real money is from the story. The board stays for pride and the beam.

### 14.5 Art (optional, reusable)
`art/battlemaps/` style is wrong for this; use a scene painting: *"A tavern's back wall of black-painted boards covered in chalk columns and tally marks, a wet rag and a stick of chalk on a ledge, a cast-iron pan hanging beside it, lamplight, regulars' silhouettes at the bar; the chalk marks are abstract scribbles and tallies only, absolutely no readable text, letters or numbers."* Standings live in text, never in the picture.
