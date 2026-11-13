# Consistency Check: Truth File step (SEALED)

Run at build time by script over `truth/*.md`, plus manual review against `world/` and `campaign/`.

| Check | Result |
|---|---|
| Every R-### referenced (Tier 1, Tier 2, Events, Secrets) exists in the Ledger | **PASS**: 96 edges defined, 0 missing |
| Every EVT-## referenced (Ledger, Tier 1, Secrets) exists in Events | **PASS**: 55 events defined, 0 missing |
| Two-way agreement: each edge's CHANGES ONLY VIA lists the event, and that event lists the edge | **PASS** after 2 fixes (R-091 ↔ EVT-23, R-075 ↔ EVT-31) |
| Every edge has at least one changing event | **PASS** |
| Every NPC-### used in Ledger, Events, Secrets, Factions is defined in Tier 1 or Tier 2 | **PASS** |
| Every SEC has 2+ seeds before its reveal | **PASS**: 22/22. SEC-18 was at 1 real seed before its lead-in; a third seed was added (CHG-03). SEC-20 and SEC-21 have exactly 2. |
| Every vouch scene in campaign/02–03 maps to a ledger edge | **PASS**: #1 and #2 (R-040), #3 (R-050), #4 (R-007), #5 (R-070, true), #6 (R-057) |
| One ID means one thing (EVT numbering) | **FIXED**: the Concord vote was renumbered EVT-31 → EVT-36 (CHG-02); campaign/00 updated |
| Banned Shackled City names / "Silas" | **PASS**: no NPC uses one. "Ashe" appears only as a dictation spelling of Ash in the index. |
| Forbidden content (demonic, infernal, fae courts) | **PASS** |
| Female major allies older, wiser or sisterly; no romance | **PASS**: Hester, Aggie, Brynja, Hilde, Maud, Burdock, Umbari, Wenna, Bess, Peg, Dora; Clara is a sister |
| Loss level B (two planned deaths only) | **PASS**: Hester (EVT-21), Umbari (EVT-31). No Lane member dies by script. |

## Known soft spots (not failures)
- SEC-20 and SEC-21 have exactly two seeds each. Add a third at the table if play gives a natural moment.
- Tier 1 is at the 25 cap. Promote Russet, Brynja or Hale to Tier 1 only by demoting someone (Simon Shaw is the easiest).
- Name clash risk: Pip (Carter) vs. the world list's "Pip Copperkettle." Logged (CHG-05).
