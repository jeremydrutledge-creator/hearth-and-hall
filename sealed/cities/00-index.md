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
