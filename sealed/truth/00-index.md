# 00 · Truth File Index (SEALED — DM ONLY)

## Files
| File | What's in it |
|---|---|
| `00-index.md` | ID scheme, running rule, name lookup with every spelling |
| `01-tier1.md` | 25 Tier 1 entries, full block format (incl. the three companions), plus 2 non-person entities |
| `02-tier2.md` | Tier 2 entries, 2–3 lines each, plus historical figures |
| `03-ledger.md` | Relationship Ledger: 96 directional edges (R-001 to R-096) |
| `04-secrets.md` | Secrets register SEC-01 to SEC-22 (holders, seed counts, reveal events, edges) |
| `05-events.md` | Events EVT-01 to EVT-55, the only things that change beliefs or the SEAL clock |
| `06-factions.md` | FAC-01 to FAC-18 with leaders, secrets and attitude moves |
| `07-tier3-log.md` | Improvised NPCs during play |
| `08-change-log.md` | CHG entries: play overrides the plan |
| `_consistency.md` | Build-time consistency check results |
| `_handoff-notes.md` | Notes for the chapter-detail step |

## ID scheme (permanent; never reuse a number)
| Prefix | Meaning | Range in use |
|---|---|---|
| `PC-01` | Ash (the player character). No Truth entry. | PC-01 |
| `NPC-###` | Characters. 001–003 companions; 004–025 Tier 1; 026+ Tier 2 | NPC-001 to NPC-079 (NPC-080 next) |
| `ENT-##` | Non-person powers | ENT-01, ENT-02 |
| `HIST-##` | Dead or historical figures | HIST-01 to HIST-05 |
| `T3-###` | Tier 3, improvised in play | T3-001 next |
| `FAC-##` | Factions | FAC-01 to FAC-18 |
| `R-###` | Ledger edges (one direction each) | R-001 to R-096 (R-097 next) |
| `SEC-##` | Secrets | SEC-01 to SEC-22 (SEC-23 next) |
| `EVT-##` | Events | EVT-01 to EVT-55 (EVT-56 next) |
| `CHG-##` | Change log entries | CHG-01 to CHG-05 (CHG-06 next) |

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
