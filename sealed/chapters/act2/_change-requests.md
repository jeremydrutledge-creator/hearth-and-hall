# Act II · Change Requests for Shared Files (SEALED — DM ONLY)

> **STATUS: all requests below were resolved in the step-10 consistency pass (CHG-07 to CHG-16 in `truth/08-change-log.md`). Where a request offered options, the change log records the one chosen.**

> Act II's chapter files don't edit `world/`, `campaign/`, `truth/` or `rules/`. Everything below is a **request** to the owner of those files, written in the `truth/08` CHG format. Numbers here are **provisional** (CHG-A2-##); the Truth File's owner assigns real CHG numbers (next free per `truth/00`: CHG-07, unless other steps have used it).
> Format: **CHG-A2-## · build (Act II chapters) · What should change · Why · Records touched**

---

**CHG-A2-01 · build (Act II) · Calendar clash: the Ford Festival.**
- **What:** `campaign/02` Ch11 (Leaffall) uses the Ford Festival (the Lamp-Climb, the pageant, Fight 16; Hollis's offer route C; Clara's locket gift). `world/01` and `world/02` date the Ford Festival to **the 1st of Lantern**, which falls *after* Ch12 (Frostcome) and only a month before Lantern Night.
- **Proposed fix (pick one):** (a) move the Ford Festival to **the 1st of Leaffall** in `world/01` (key days) and `world/02` (festival table and Lamp-Climb line); nothing else in the world files depends on the Lantern date. Or (b) keep the world date and rename Ch11's festival "the Leaffall Lamp-Fair" (same contest, same pageant) in `campaign/02`, `campaign/03` (SEC-06 seed, SEC-21 reveal line), `campaign/05` (gifts table, villain footprints) and `truth/05` EVT-48 / `truth/01` NPC-023.
- **Act II's handling:** `ch11.md` runs the night as written and tells the DM to use the Lamp-Fair name if (b) is chosen.
- **Records touched:** world/01, world/02 (or campaign/02, /03, /05, truth/01, /05).

**CHG-A2-02 · build (Act II) · New NPCs; provisional ID block NPC-140 to NPC-159.**
- **What:** add Tier 2 lines for the twenty Act II NPCs listed in `_index.md` §5 (Lady Honoria Merrow, Valentine Crewe, Julian Hume, Master Otto Varga, Coble Tull, Merrilee, Dughal Brokenhorn, Purser Edwin Lusk, Gert Volker, Sergeant-Mage Ilse Brandt, Thurvig the Gate-Breaker, Bastian Harrow, Lt. Corbin Wade, Sal Pickett, Senior Enchanters Ivo Pryce and Adela Holt, Warden-Sergeant Bryony Nash, Skipper Ottilie Bask, Archivist Sigrun Deeplore, Plish), with alternate spellings, and add them to the `truth/00` name lookup.
- **Why:** `truth/_handoff-notes.md` asked step 6 to name the House of Merrow's head and the Ch9 duelist (done: NPC-140, NPC-141), and these others speak or fight. A high provisional block avoids colliding with other chapter writers working at the same time. **Renumber freely**; the chapter files use names first and IDs second.
- **Sound-alike notes for the lookup:** "Holt" (Adela) vs. "Hale" (Captain) vs. "Hollis"; "Nash" vs. "Ash" (dictation: "Sergeant Nash" is always the warden); "Crewe" vs. "Crane" (the Chancellor); "Wade" vs. "Walt"; "Coble" vs. "Corwin."
- **Records touched:** truth/00, truth/02 (and truth/07 for the Tier 3 names in `_index.md` §5, if they get play).

**CHG-A2-03 · build (Act II) · Ash gains Performance proficiency at Ch9 (story reward, offered).**
- **What:** when Ash opens his first gate (Ch9 SC 9-B, EVT-16), the DM offers Performance proficiency ("the song settles in him"). If the player accepts, add it to Ash's sheet.
- **Why:** `rules/01` (Ash addendum) and `rules/_handoff-notes.md` suggest exactly this for Ch9. Waking DCs (17 → 19) assume it from tier 3.
- **Records touched:** rules/01 (Ash), /player/party-sheets.md (only if accepted, at the table).

**CHG-A2-04 · build (Act II) · Gideon's Bearback boon: *Bear's Ward*.**
- **What:** at Ch10 (EVT-17), Gideon gains: ***Bear's Ward.*** Once per long rest, when a creature in his aura would drop to 0 HP, he can use his reaction to have it drop to 1 HP instead. Plus the story effects already in `rules/01` (bear-shaped aura; dwarves kneel) and Ch8's discovery (greywilt doesn't affect creatures in his aura while he's conscious).
- **Why:** `rules/01` (Gideon addendum) allows "a specific mechanic" if the chapter writer adds one. It fits the "survivable" design and the Oath of the Ancients.
- **Records touched:** rules/01 (Gideon), /player/party-sheets.md (at the table).

**CHG-A2-05 · build (Act II) · Use Magic Device scroll ability (Ch13).**
- **What:** Ch13's Guildhall route (SC 13-A) gives Ash warden-scrolls (Dispel Magic, Counterspell). By the house rule, scrolls use **Int** (+1 for Ash). `rules/01` suggests letting him use **Cha** if the player asks. Ch13 is written to work either way.
- **Records touched:** rules/00 §3 (Use Magic Device) and the player copy, only if the player asks and the DM agrees.

**CHG-A2-06 · build (Act II) · Waking in Act II (interpretation of CHG-01).**
- **What:** Act II sorts Hushed into **recent** (wakeable by Ash's song now), **deep** (only *stirred* by Ash alone; woken by the twins' duet from Ch12, or by Ash after Ch15's discovery) and **Hushed dead** (laid to rest, never woken). Waking DC 17 (L7–10), 19 (L11–13). Details in `_index.md` §3.2.
- **Why:** `campaign/00` §2 / CHG-01 says Ash wakes Hushed "one at a time (from Ch15)," but Act I lets the party wake Borra (Ch3) and the Kessel miners (Ch5), `rules/02` gives waking DCs by tier from L1, and `truth/01` says Walt can be woken only after the Ch12 duet or Ch15. This reading keeps all of them true: "from Ch15" becomes "deep Hushed, by Ash alone, from Ch15."
- **Please check against Act I's chapter files** (Ch3, Ch5) and Act III's Ch15 so the three writers agree.
- **Records touched:** campaign/00 §2 (a clarifying line), world/05 (the Hushed tag), truth/08.

**CHG-A2-07 · build (Act II) · Hart round accounting.**
- **What:** (1) The Ch6 shore transformation *grants* upgrade #2 and doesn't spend tier 2's once-per-tier round, so the party has one Hart round in Ch7–10 and one in Ch11–13. (2) Ch13's "holds the Hall with roots" is a free, scripted story beat, not the tier round. (3) A one-round Hart narrative action is defined in `_index.md` §3.4 for tiers 2–3. The full Hart stat block (upgrade #4, Ch16) is still Act III's.
- **Records touched:** campaign/05 §7 (a clarifying line), rules/01 (Moss addendum).

**CHG-A2-08 · build (Act II) · New ledger edges (provisional R-200 to R-208).**
Add only the ones that get used at the table. Format follows `truth/03`.
- **R-200 · NPC-064 Hilde Strand → NPC-001 Gideon (or PC-01 Ash, whoever fought her)** · BELIEVES: the fighter she's been waiting for; maybe a successor. · WILL VOUCH: for their courage, to any Copperhill crowd or mercenary. · FEELING: amused, mentorly (no romance). · CHANGES VIA: Ch10 bout; EVT-17.
- **R-201 · NPC-065 Ulric Fane → PC-01 Ash (and the party)** · BELIEVES: contract-honest people, or a voided contract's lawful winners. · WILL VOUCH: that they keep their word, in Wolfsgate. · CHANGES VIA: Ch10 (route chosen).
- **R-202 · NPC-063 Dame Constance Abernathy → PC-01 Ash** · BELIEVES: finally, a thief who admits it; useful. · WILL VOUCH: for his usefulness, never his honesty. · CHANGES VIA: EVT-15.
- **R-203 · NPC-061 Saffi-of-the-Lamplight → PC-01 Ash** · BELIEVES: the boy from the stories, now a story she owns. · WILL VOUCH: for him at the Great Telling and to any horned one who'll listen (Ch14). · CHANGES VIA: EVT-16.
- **R-204 · NPC-140 Lady Honoria Merrow → NPC-006 Hollis** · BELIEVES: the Keeper (she knows the face, maybe not the name) offers the only peace. · WILL VOUCH: for the Quiet. · CHANGES VIA: EVT-15, EVT-24.
- **R-205 · NPC-034 Dorcas Fell → NPC-006 Hollis** · BELIEVES: the Lamplighters live on his glimmer; she doesn't like him. · WILL VOUCH: for nothing. · CHANGES VIA: Ch13 (turned with proof).
- **R-206 / R-207 · NPC-154 Ivo Pryce, NPC-155 Adela Holt → NPC-006 Hollis** · BELIEVES: the Keeper is a saint. · WILL VOUCH: for the Keeper, to the death (they don't, in the end). · CHANGES VIA: EVT-23, EVT-24.
- **R-208 · NPC-067 Brynja → PC-01 Ash** · BELIEVES: the Bear's chosen's little brother, a thief with good hands; she forged him a sword. · WILL VOUCH: for his honesty, to dwarves. · FEELING: sisterly (no romance). · CHANGES VIA: EVT-53.
- **Records touched:** truth/03, truth/05 (add these edges under the events named), truth/_consistency.

**CHG-A2-09 · build (Act II) · New seeds placed (add to the seed lists).**
- **SEC-03:** Ch8, Granny Tull's barge-song line "one to hear and one to cry" (an extra hindsight seed).
- **SEC-11:** Ch9, the dwarven "Oath of the Quiet Stone" mark in the Varga vault (already listed; confirmed placement: Fight 12 feature 4).
- **SEC-12:** Ch10, a dwarven sea-chart slate marked "the Island that Sleeps" with the astrolabe's keyhole glyph (matches the existing Ch10 seed).
- **SEC-13 status:** Ch12, the Heron stops listening along Lark's bond and turns to hunting Clara (consistent with `campaign/00` §3 A, "from Ch12 on, it sends the Heron for Clara first").
- **SEC-15:** Ch8 (the reed-boat elf), Ch10 (Torvald), Ch13 (a Warden of the Leaf cuts one district's chain in SC#4): all three seeds placed.
- **Old Varrow (Ch18):** Ch13's Drowned Ford-Knight carries the Fenn-wyck crest (ford with a stag's antlers), matching `world/03`'s Old Varrow tomb. A Fenn-wyck ford-knight among Old Ford's Gate War dead is new detail; it doesn't contradict anything.
- **Records touched:** campaign/03, truth/04 (seed counts).

**CHG-A2-10 · build (Act II) · If Hester is saved (the costly route).**
- **What:** `campaign/00` §7 allows one costly save. Ch13 writes the consequences: Hester lives, her blind spot gone; she becomes an angry witness against Hollis in Ch17; Hollis escapes un-reached toward Mirrowen; EVT-22 is +3 and EVT-23 doesn't happen (SEAL likely 7: the SEAL 7 breach beat; Brannoc's vanguard at dawn).
- **Ask for Act III:** loss level B still caps at two planned deaths; **don't replace Hester with another death.** If Hollis escaped, Ch14 needs a line for where he is (a captive or an adviser among the "horned ones" his letters mention).
- **Records touched:** truth/05 EVT-21 (branch note), truth/01 NPC-007 and NPC-006 (status branches), campaign/02 Ch14 (opening, if SEAL 7).

**CHG-A2-11 · build (Act II) · Gideon's greywilt aura (Ch8) given a rules line.**
- **What:** the Ch8 discovery moment ("greywilt backs off his aura") is given a concrete effect: still-water and greywilt terrain effects don't affect creatures inside Gideon's Aura of Protection while he's conscious. Act II's still-water hazards are written with this in mind (it's why they call out "Gideon's aura protects").
- **Records touched:** rules/01 (Gideon addendum).

**CHG-A2-12 · build (Act II) · Small facts introduced (no conflicts found; log for consistency).**
- The drift-gate ("the Blind Eye") is a minor Wellgate under Driftmarket's usual anchorage (consistent with `campaign/00` §3 C, "Driftmarket's drift-gate").
- The Kessel Workings' old Gate War shaft has a dwarven gate-slab (consistent with the Ch5 warning stone).
- Bearback's shrine has a cracked, iron-capped high shaft of the mountain gate (consistent with `campaign/02` Ch10 ★4 route C, "the cracked Deep Spring"); it leads to Ursk's Den.
- Clara as a noncombatant: AC 12, 44 HP (Ch12–13).
- Lamp House's admission note for Clara mentions "pewter locket (half), kept with child" (consistent with SEC-23: Hollis knows her half came off the Fenwick child).
- Willow Lane floats lamps on the Bend for Tom and Elinor on the fire's anniversary in Leaffall (in addition to the three Midsummer lamps of SEC-16).
- **Records touched:** truth/_consistency (a note), world/02 (optional customs line).
