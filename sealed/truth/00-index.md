# 00 · Truth File Index (SEALED — DM ONLY)

## Files
| File | What's in it |
|---|---|
| `00-index.md` | ID scheme, running rule, name lookup with every spelling |
| `01-tier1.md` | 25 Tier 1 entries, full block format (incl. the three companions), plus 2 non-person entities |
| `02-tier2.md` | Tier 2 entries, 2–3 lines each, plus historical figures |
| `03-ledger.md` | Relationship Ledger: 116 directional edges (R-001 to R-096, R-200 to R-208, R-230 to R-240) |
| `04-secrets.md` | Secrets register SEC-01 to SEC-24 (holders, seed counts, reveal events, edges) |
| `05-events.md` | Events EVT-01 to EVT-60, the only things that change beliefs or the SEAL clock |
| `06-factions.md` | FAC-01 to FAC-18 with leaders, secrets and attitude moves |
| `07-tier3-log.md` | Improvised NPCs during play |
| `08-change-log.md` | CHG entries: play overrides the plan |
| `_consistency.md` | Build-time consistency check results |
| `_handoff-notes.md` | Notes for the chapter-detail step |

## ID scheme (permanent; never reuse a number)
| Prefix | Meaning | Range in use |
|---|---|---|
| `PC-01` | Ash (the player character). No Truth entry. | PC-01 |
| `NPC-###` | Characters. 001–003 companions; 004–025 Tier 1; 026+ Tier 2 | NPC-001 to NPC-096, NPC-140 to NPC-159, NPC-180 to NPC-196 (185–186 reserved, unused), NPC-300 to NPC-356 (next: NPC-097) |
| `ENT-##` | Non-person powers | ENT-01, ENT-02 |
| `HIST-##` | Dead or historical figures | HIST-01 to HIST-06 |
| `T3-###` | Tier 3, improvised in play | T3-001 next |
| `FAC-##` | Factions | FAC-01 to FAC-18 |
| `R-###` | Ledger edges (one direction each) | R-001 to R-096, R-200 to R-208, R-230 to R-240 (R-241 next) |
| `SEC-##` | Secrets | SEC-01 to SEC-24 (SEC-25 next) |
| `EVT-##` | Events | EVT-01 to EVT-60 (EVT-61 next) |
| `CHG-##` | Change log entries | CHG-01 to CHG-18 (CHG-19 next) |

## The running rule
> **Before any NPC vouches for, speaks about or reacts to another, read that edge in `03-ledger.md`.**
> - If the edge exists, play its BELIEVES, BLIND SPOT and WILL VOUCH exactly. NPCs say what they *believe*, not what's true.
> - If no edge exists, the NPC has no special knowledge. Use their public face, and add an edge if the moment matters.
> - Beliefs change only through an EVT. If play changes one some other way, add the event and log a CHG.
> - Before shaping how any NPC sees another, read ahead in the sealed chapter where they next meet.

## Name lookup (the player dictates by voice: match by sound)

> Search this table by any spelling. If a dictated name sounds close to two entries, pick the one in the current scene.

| Heard as… | Is | ID |
|---|---|---|
| Ash, Asheron, Asherin, Ashton*, Ashe† | Ash Fenwick (the player) | PC-01 |
| Gideon, Gidion, Gid, Giddy | Gideon Fenwick | NPC-001 |
| Zeke, Zeek, Ezekiel, Ezekial, Zee | Zeke Fenwick | NPC-002 |
| Moss, Mos, Old Moss, Mossoran, Mossoren, Moss-Oran, Mossorin, Old Mossback, the Hart, the Stag | Moss | NPC-003 |
| Lark, Larke, the little Hearkener | Lark | NPC-004 |
| Clara, Klara, Claire, Clare, Clarra, Wren, Ren, Wrenn | Clara Grane (born Wren Fenwick) | NPC-005 |
| Hollis, Hollace, Holis, Hollis Grain, Master Grane, the Keeper, Keeper of the Still Lamp | Hollis Grane | NPC-006 |
| Hester, Hestor, Esther Grane, Mistress Grane, Aunt Hester | Hester Grane | NPC-007 |
| Brannoc, Brannock, Brannick, Branok, the Regent, Horned Regent | Brannoc Ironhorn | NPC-008 |
| Vessimer, Vessimar, Vesimer, Vessamer, the Grey Heron, the Heron, the bird that doesn't blink | Vessimer | NPC-009 |
| Rook, Rooke, Ruk, Rouk, Danny Pratt, Dan Pratt | Rook | NPC-010 |
| Bess, Bes, Beth Carter, Bessie, Widow Carter | Bess Carter | NPC-011 |
| Dora, Dorrie, Dorothy, Dora Fink | Dora Finch | NPC-012 |
| Walt, Walter, Wal, Walt Fink | Walt Finch | NPC-013 |
| Aggie, Aggy, Agatha, Thorne, Thorn | Aggie Thorne | NPC-014 |
| Peg, Peggy, Peg Malory, Margaret Mallory, Mother Willow | Peg Mallory | NPC-015 |
| Netta, Nettie, Neta, Annette, Netta Low | Netta Lowe | NPC-016 |
| Ostley, Ostly, Osley, Bill, Billy, Sarge | Sgt. Bill Ostley | NPC-017 |
| Thistle, Thistel, Thissle | Thistle of the Mere | NPC-018 |
| Burdock, Burdok, Gran Burdock, the Warren Mother | Mother Burdock | NPC-019 |
| Hask, Hassk, Ask, Lucan, Lukan, Lucas | Warden-Captain Lucan Hask | NPC-020 |
| Umbari, Umbarri, Oombari, Gran Umbari, the Rememberer | Grandmother Umbari | NPC-021 |
| Fergan, Fergen, Fergus, Fergun | Fergan Ironhorn | NPC-022 |
| Mabry, Mabrey, Maybry, Giles, Jiles, Gyles | Sgt. Giles Mabry | NPC-023 |
| Ma Garrow, Garo, Ma Garro, Ma | Ma Garrow | NPC-024 |
| Simon, Si, Simeon, Simon Shore | Simon Shaw | NPC-025 |
| Pip, Pipp | Pip Carter | NPC-026 |
| Nell, Nel, Nelly | Nell Carter | NPC-027 |
| Martha, Marth, Mother Pratt | Martha Pratt | NPC-028 |
| Hugh, Hew, Huey, Hugh Dale | Hugh Dale | NPC-029 |
| Bram, Bramm, Old Bram | Old Bram | NPC-030 |
| Teague, Teeg, Margery, Margie, Marjorie, the Provost | Provost Margery Teague | NPC-031 |
| Osric, Ozrick, Oswald, Vane, Vain | Osric Vane | NPC-032 |
| Hale, Rod, Roddy, Roderick, Rodrick, the Captain | Captain Roderick Hale | NPC-033 |
| Dorcas, Dorkas, Dorcus, Fell | Dorcas Fell | NPC-034 |
| Tam, Tom Hollin, Hollen, Big Tam | Tam Hollin | NPC-035 |
| Agnes Brack, Brak, Widow Brack | Agnes Brack | NPC-036 |
| Lionel, Lyonel, Hartley, Hartly | Lionel Hartley | NPC-037 |
| Garrick, Garrik, Gary Stone | Garrick Stone | NPC-038 |
| Prudence, Prue, Ames, Aims, Doctor Ames | Doctor Prudence Ames | NPC-039 |
| Doone, Dune, Cyril, Sirril, Cyrel | Professor Cyril Doone | NPC-040 |
| Orla, Orlah, Venn, Ven, Orla Fenn | Mine-Warden Orla Venn | NPC-041 |
| Imelda, Rusk, Rusck | Chancellor-Professor Imelda Rusk | NPC-042 |
| Mother Brine, Brine, Bryne, Bethany Rourke, Beth | Mother Brine | NPC-043 |
| Tolley, Tolly, Toley, Hob, Arn | Hob and Arn Tolley | NPC-044 |
| Jory, Jorrie, Jorey, Tolliver | Jory Tolliver | NPC-045 |
| Ambrose, Ambros, Webb, Web, Weeb | Master Ambrose Webb | NPC-046 |
| Ottoline, Otteline, Brightwell, Brightwel | Madame Ottoline Brightwell | NPC-047 |
| Nim, Nimm, Gearwright, Gearwrite | Nim Gearwright | NPC-048 |
| Hakon, Haakon, Hakkon, Stonebrow | Hakon Stonebrow | NPC-049 |
| Wat, Watt, Wat Ember, Old Wat | Old Wat Ember | NPC-050 |
| Rosalind, Roz, Rosalyn, Fairweather, Sister Rosalind | Sister Rosalind Fairweather | NPC-051 |
| Jem, Jemm, Tapper, Taper | Jem Tapper | NPC-052 |
| Elspeth, Elsbeth, Elspith, Widow Marsh | Elspeth Marsh | NPC-053 |
| Corwin, Corwen, Lockley, Lockly | Corwin Lockley | NPC-054 |
| Dagny, Dagney, Coalbeard, Coalbeerd | Dagny Coalbeard | NPC-055 |
| Tobias, Toby, Neat, Neet | Tobias Neat | NPC-056 |
| Russet, Rusty, Russett, Tamsworth, Tamsworthe | Russet Tamsworth | NPC-057 |
| Hoard, Hord, Horde, Captain Hoard | Captain Hoard | NPC-058 |
| Ama, Amma, Amah | Ama | NPC-059 |
| Borra, Bora, Borrah | Borra | NPC-060 |
| Saffi, Saffy, Saffie, Saffi-of-the-Lamplight, the Tale-Keeper | Saffi-of-the-Lamplight | NPC-061 |
| Wenna, Wena, Granny Tull, Gran Tull, Eldest Mother | Granny Wenna Tull | NPC-062 |
| Constance, Connie, Abernathy, Abernethy, First Purse | Dame Constance Abernathy | NPC-063 |
| Hilde, Hilda, Strand, the Champion | Hilde Strand | NPC-064 |
| Ulric, Ulrich, Ulrik, Fane | Captain-General Ulric Fane | NPC-065 |
| Torvald, Thorvald, Tor, Deepanvil | King Torvald Deepanvil | NPC-066 |
| Brynja, Brinya, Brynya | Princess Brynja | NPC-067 |
| Amarys, Amaris, Ah-MAR-iss, the Queen | Queen Amarys | NPC-068 |
| Edric, Edrick, the boy-king | King Edric II | NPC-069 |
| Crane, Crain, Anselm, Ansel, the Chancellor | Lord Chancellor Anselm Crane | NPC-070 |
| Maud, Maude, Penrose, Pen-rose, the Governor | Lady Governor Maud Penrose | NPC-071 |
| Jago, Yago, Trelawn, Trelawne | Captain Jago Trelawn | NPC-072 |
| Dabble, Dabbel, Quickwhistle | Dabble Quickwhistle | NPC-073 |
| Fenna, Fena, Hobbs, Hobs | Constable Fenna Hobbs | NPC-074 |
| Nan, Nann, Old Nan, Nan Pike | Old Nan Pike | NPC-075 |
| Tobin, Tobyn, Tobin Pike | Tobin Pike | NPC-076 |
| Hilary, Hillary, Mother Vance, the Abbess | Mother Hilary Vance | NPC-077 |
| Tansy, Tansey | Tansy | NPC-078 |
| Moth, Moth-of-the-Long-Dusk | Moth-of-the-Long-Dusk | NPC-079 |
| Omeruth, Omerooth, Omeroth, Omeruthe, the Stillness, the Quiet under the water | Omeruth | ENT-01 |
| Thalassa, Ommu, Old Ommu, Thalassa-Ommu, the Deep Tortoise, the Island that Sleeps | Thalassa-Ommu | ENT-02 |
| Tom, Thom Fenwick | Tom Fenwick (father, dead) | HIST-01 |
| Elinor, Eleanor, Ellie | Elinor Fenwick (mother, dead) | HIST-02 |
| Wynne, Win, Fenn-wyck | Wynne Fenn-wyck (first Hearkener) | HIST-03 |
| Ursk, Ursc, Ursek, the Mountain Bear | Ursk | HIST-04 |
| Edmund, Ned Grane | Hollis's son (dead) | HIST-05 |

\* "Ashton" is a likely dictation slip for Ash. † "Ashe" is a banned *name* for any NPC (Shackled City list), but it's an obvious misspelling of Ash in dictation; read it as Ash.

### Sound-alike traps
- **Aggie** (Thorne, Moss's assistant) vs. **Agnes** (Brack, Brewers' Guild). Default to Aggie on Willow Lane.
- **Clara** (the twin) vs. **Clara** (Hollis's dead wife, HIST-05). The living one, always, unless the talk is about Hollis's past.
- **Hollis Grane** vs. **Hester Grane**: "the Grane" alone usually means Hollis in a Guild scene and Hester at Lamp House.
- **Tam Hollin** vs. **Tom Fenwick**: "Tom" alone is probably the father in family talk.
- **Moth** (tabaxi) vs. **Moss**. In Mirrowen with a tracker present, ask nothing; read for intent.
- **Hask** vs. **Hoard**: different realms. Use the scene.
- **Tolley** (brothers) vs. **Tolliver** (Jory).


### Added in the consistency pass (CHG-10)

| Heard as… | Is | ID |
|---|---|---|
| Joss Kettering, Joss, Kettring | Joss Kettering | NPC-080 |
| Wharfmaster Joan Huckle, Huckel | Wharfmaster Joan Huckle | NPC-081 |
| Mistress Rose Ainslie, Ainsley | Mistress Rose Ainslie | NPC-082 |
| Dob Rushby, Dob, Rushbee | Dob Rushby | NPC-083 |
| Jenny Wick, Jen Wick | Jenny Wick | NPC-084 |
| Tad Sallow, Taddy | Tad Sallow | NPC-085 |
| Big Lottie Sparrow, Lotty | Big Lottie Sparrow | NPC-086 |
| Hal Brindle | Hal Brindle | NPC-087 |
| Morwenna Kell, "the Anvil", Morwena | Morwenna Kell, "the Anvil" | NPC-088 |
| Wilf Applegarth | Wilf Applegarth | NPC-089 |
| Warden Abel Crouch | Warden Abel Crouch | NPC-090 |
| Davy, Ma Garrow's cousin | Davy | NPC-091 |
| Tom Penny | Tom Penny | NPC-092 |
| Sergeant Murdo Blackhoof, Murdoch | Sergeant Murdo Blackhoof | NPC-093 |
| Sorrel | Sorrel | NPC-094 |
| Bracken | Bracken | NPC-095 |
| Teasel, Teazel | Teasel | NPC-096 |
| Lady Honoria Merrow, Honora, Merow | Lady Honoria Merrow | NPC-140 |
| Valentine Crewe, Val, Crew | Valentine Crewe | NPC-141 |
| Julian Hume, Jules, Hewm | Julian Hume | NPC-142 |
| Master Otto Varga, Varga, Vargas | Master Otto Varga | NPC-143 |
| Coble Tull, Cobble | Coble Tull | NPC-144 |
| Merrilee, Merrily | Merrilee | NPC-145 |
| Dughal Brokenhorn, Dugal, Dougal | Dughal Brokenhorn | NPC-146 |
| Purser Edwin Lusk, Ed, Lusck | Purser Edwin Lusk | NPC-147 |
| Gert Volker, Gerd | Gert Volker | NPC-148 |
| Sergeant-Mage Ilse Brandt, Ilsa | Sergeant-Mage Ilse Brandt | NPC-149 |
| Thurvig the Gate-Breaker, Thurvik | Thurvig the Gate-Breaker | NPC-150 |
| Bastian Harrow, Bas, Bastien | Bastian Harrow | NPC-151 |
| Lieutenant Corbin Wade, Corbyn | Lieutenant Corbin Wade | NPC-152 |
| Sal Pickett, Sally | Sal Pickett | NPC-153 |
| Senior Enchanter Ivo Pryce, Price | Senior Enchanter Ivo Pryce | NPC-154 |
| Senior Enchanter Adela Holt, Adella | Senior Enchanter Adela Holt | NPC-155 |
| Warden-Sergeant Bryony Nash, Briony | Warden-Sergeant Bryony Nash | NPC-156 |
| Skipper Ottilie Bask, Ottily | Skipper Ottilie Bask | NPC-157 |
| Archivist Sigrun Deeplore | Archivist Sigrun Deeplore | NPC-158 |
| Plish | Plish | NPC-159 |
| Mairead of the Seven Drums, Mairead, Maired, Mared, Maraid | Mairead of the Seven Drums | NPC-180 |
| Tesh Twelve-Bells, Tesh, Tess, Twelve-Bells | Tesh Twelve-Bells | NPC-181 |
| Ronan Ironvoice, Ronan, Ronin, Rowan | Ronan Ironvoice | NPC-182 |
| Nkemba, Nkemba, Kemba, En-Kemba, Inkemba | Nkemba | NPC-183 |
| Fiachra Hollowhorn, Fiachra, Feeakra, Fiacra | Fiachra Hollowhorn | NPC-184 |
| Breeda Stonefield, Breeda, Brida, Bridget | Breeda Stonefield | NPC-187 |
| Dunmore Breakhorn, Dunmore, Dunmoor, Dun More | Dunmore Breakhorn | NPC-190 |
| Den-Mother Hulda Greypaw, Hulda, Hilda, Greypaw | Den-Mother Hulda Greypaw | NPC-191 |
| Leaf-Warden Ithiel, Ithiel, Ithil, Ithiell | Leaf-Warden Ithiel | NPC-192 |
| Brother Wendell, Wendell, Wendel | Brother Wendell | NPC-193 |
| The Bell-Warden, Bell-Warden | The Bell-Warden | NPC-194 |
| Captain Hattie Slade, Hattie, Hatty, Slade | Captain Hattie Slade | NPC-195 |
| Bosun Ezzard Cole, Ezzard, Ezard, Cole, Coal | Bosun Ezzard Cole | NPC-196 |
| Clementine Brightwell | Clementine Brightwell | NPC-300 |
| Rosamund Brightwell | Rosamund Brightwell | NPC-301 |
| Violet Brightwell | Violet Brightwell | NPC-302 |
| Hettie Bunce, Hetty, Bunse | Hettie Bunce | NPC-303 |
| Sam Clay, Sammy | Sam Clay | NPC-304 |
| Mags Weller, Maggie, Weler | Mags Weller | NPC-305 |
| Bertram Cole, Bert Cole | Bertram Cole | NPC-306 |
| Fat Lem Gilly, Lemuel, Lem Gilley | Fat Lem Gilly | NPC-307 |
| Clem Raddle, Clement, Clem Radle | Clem Raddle | NPC-308 |
| Saul Hennet, Saul Hennett | Saul Hennet | NPC-309 |
| Little Ned Garrow, Ned, Neddy | Little Ned Garrow | NPC-310 |
| "Gentle" Joe Barrow | "Gentle" Joe Barrow | NPC-311 |
| Brannagh "Bonebreaker" Reece | Brannagh "Bonebreaker" Reece | NPC-312 |
| Jonas Hatch, "the Bellman" | Jonas Hatch, "the Bellman" | NPC-313 |
| Barnaby Coyle, Barney Coil | Barnaby Coyle | NPC-314 |
| Gilbert Swift | Gilbert Swift | NPC-315 |
| Percy Lisle, Percy Lyle | Percy Lisle | NPC-316 |
| Hortensia Vale, Tensy | Hortensia Vale | NPC-317 |
| Molly Pike, Mollie | Molly Pike | NPC-318 |
| Gerald Hatherley | Gerald Hatherley | NPC-319 |
| Brother Ivo, Eye-vo, Evo | Brother Ivo | NPC-320 |
| Sergeant Ruth Dane, Ruthie | Sergeant Ruth Dane | NPC-321 |
| Old Corrie Bask, Cory Bask | Old Corrie Bask | NPC-322 |
| Hob Rudd, Robb Rudd | Hob Rudd | NPC-323 |
| Father Malory Wake, Mallory | Father Malory Wake | NPC-324 |
| Captain Rafe Lennick, Raif | Captain Rafe Lennick | NPC-325 |
| Mistress Odile Fairbanks, Odeel | Mistress Odile Fairbanks | NPC-326 |
| Gaspard Quist, Gaspar, Kwist | Gaspard Quist | NPC-327 |
| Mother Hollyhock, Holly Hock | Mother Hollyhock | NPC-328 |
| Leopold Quarry, Leo Quarrie | Leopold Quarry | NPC-329 |
| Cassius Dray, "the Gilded Lion" | Cassius Dray, "the Gilded Lion" | NPC-330 |
| Pim Saddler, Pimm Sadler | Pim Saddler | NPC-331 |
| Fizzwick Brassbottom | Fizzwick Brassbottom | NPC-332 |
| Pernella Gearspring, Nella | Pernella Gearspring | NPC-333 |
| Prior Benedict Lowry, Ben Lowery | Prior Benedict Lowry | NPC-334 |
| Sister Winifred Oake, Winnie | Sister Winifred Oake | NPC-335 |
| Oswald Penk, Ozzie | Oswald Penk | NPC-336 |
| Hesketh Vonn, Hesky, Von | Hesketh Vonn | NPC-337 |
| Quartermaster Dorran Kemp | Quartermaster Dorran Kemp | NPC-338 |
| Captain Merrick Dunstan, Merik | Captain Merrick Dunstan | NPC-339 |
| Bersi Flintfist, Bersy | Bersi Flintfist | NPC-340 |
| Gudrun Stonemantle, Gudrin | Gudrun Stonemantle | NPC-341 |
| Clerk Amos Pruett, Amos Prewitt | Clerk Amos Pruett | NPC-342 |
| Sir Edmund Carrow, Ed Carrow | Sir Edmund Carrow | NPC-343 |
| Master Felix Dorne, Felix Dorn | Master Felix Dorne | NPC-344 |
| Mistress Hesper Graves | Mistress Hesper Graves | NPC-345 |
| Black Tom Rudge, Tommy | Black Tom Rudge | NPC-346 |
| Warden Caelir, Kay-leer, Caylear | Warden Caelir | NPC-347 |
| Elowen Fairbough, Elowyn, Fairbow | Elowen Fairbough | NPC-348 |
| Bertie Gall, Bert Gaul, Burty | Bertie Gall | NPC-349 |
| Captain Tamsin Gale, Tam, Tamzin | Captain Tamsin Gale | NPC-350 |
| Old Enoch Fathom, Nock | Old Enoch Fathom | NPC-351 |
| Gussie Crabb, Augusta | Gussie Crabb | NPC-352 |
| Yesh Copper-Whisker | Yesh Copper-Whisker | NPC-353 |
| Lio-of-the-Long-Shelf, Leo | Lio-of-the-Long-Shelf | NPC-354 |
| Oyelu the Stonewright, Oyello | Oyelu the Stonewright | NPC-355 |
| Sorcha Drumhand, Sorsha | Sorcha Drumhand | NPC-356 |
| Edwin, Edwin Fenwick | Edwin Fenn-wyck (Gate War knight) | HIST-06 |

### More sound-alike traps (CHG-10)
- **Hal Brindle** (docker, NPC-087) vs. **the Brindle River**. A person in the Bucket; a river on the map.
- **Abel Crouch** (lamp-warden, NPC-090) is the only Abel now. Other Abels were renamed (CHG-10).
- **Tom Penny** (Kessel miner, NPC-092) vs. **Tom Fenwick** (father) vs. **Black Tom Rudge** (NPC-346). Family talk = the father; Kessel = Penny; Highmarch Lowtown = Rudge.
- **Davy** (Ma Garrow's cousin, NPC-091) vs. **Danny** (Rook's real name). Use the scene.
- **Hettie Bunce** (NPC-303, Willow Lane baker) vs. **Hettie Brine-no-relation** (Driftmarket) vs. **Hattie Slade** (NPC-195, coast) vs. **Hester** (NPC-007). Place decides.
- **Hob Rudd** (NPC-323) vs. **Hob Tolley** (NPC-044). Say the surname.
- **Ned Garrow** (NPC-310) vs. **Ma Garrow** (NPC-024) vs. **Ned Grane** (HIST-05).
- **Holt** (Adela, NPC-155) vs. **Hale** (Captain) vs. **Hollis**. **Nash** (NPC-156) vs. **Ash**: "Sergeant Nash" is always the warden. **Crewe** (NPC-141) vs. **Crane** (Chancellor). **Wade** (NPC-152) vs. **Walt**. **Coble** (NPC-144) vs. **Corwin** vs. **Ezzard Cole** (NPC-196) vs. **Bertram Cole** (NPC-306).
- **Dunmore** (NPC-190) vs. **Dun Morrach**: in Mirrowen, the Warlord; in Eyrland, the hold. **Hulda** (NPC-191) vs. **Hilde** (Strand). **Godric Marsh** vs. **Elspeth Marsh**. **Nkemba** may come through as "Kimba" or "in Kemba."
- **Reece** (NPC-312) vs. **Rook**: low risk.
- **Julian Hume** (NPC-142) vs. **Percy Lisle** (NPC-316): different cities.
