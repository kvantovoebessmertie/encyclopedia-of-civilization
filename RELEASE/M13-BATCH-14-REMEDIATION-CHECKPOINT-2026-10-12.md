# M13 Batch 14 Remediation Checkpoint — 2026-10-12

Branch: `m13-system-wide-depth-audit-2026-10-09`
Base/head reviewed: `17c1bb10cdefb2a2a69ec7ff66fdbba221a65ff2`
Status: **bounded remediation review; no D/E/B scores or canonical record edits in this checkpoint**

## Verified state

- Batch 14 covers inventory rows 651–750 (100 Claims) as metadata-level source-fit triage. It does not constitute passage-level verification or D/E/B scoring.
- The current `SRC-HYDROLOGY_BASICS` record is already version 2 and correctly identifies the USGS Water Science School page “What is Hydrology?” at `https://www.usgs.gov/water-science-school/science/what-hydrology`. Its three Evidence Use records are also version 2 and point to Source version 2 with section/paragraph pinpoints. Therefore, Batch 14's hydrology identity finding is stale relative to the exact reviewed head and should be treated as **corrected in the current tree, pending targeted verification**, not as an unimplemented fix.
- `SRC-HUMAN_COMPUTER_INTERACTION_BASICS` remains version 1 with a sentence-like identity and URI `https://www.nist.gov/itl/iad`. The URI now redirects to NIST's “Technology Test and Evaluation Division” page. The current NIST “Human-Centered Technologies” page is `https://www.nist.gov/itl/tted/human-centered-technologies`; it describes human factors, cognitive science, user-centered design, usability, and human-system interaction. This is a better topical candidate, but does not automatically prove every current Claim, especially the interface perception/control statement. Keep this slice on HOLD until a bounded source/Evidence Use version update and claim-by-claim pinpoint review can be validated together.
- `SRC-IMMUNOLOGY_BASICS` remains version 1 with identity “OpenStax Microbiology — Innate and Adaptive Immunity” but URI `https://openstax.org/books/microbiology/pages/18-1-how-pathogens-cause-disease`. The current official OpenStax section is “18.1 Overview of Specific Adaptive Immunity” at `https://openstax.org/books/microbiology/pages/18-1-overview-of-specific-adaptive-immunity`. However, the three current Claims in this slice are editorial/methodological statements about the slice, sources, and specialist review—not substantive immunology Claims. Correcting the URL alone would not fix that Claim/source mismatch. Keep all three out of any publication candidate set pending editorial/type adjudication and a decision on whether to replace the Claims with genuine domain statements or relocate the editorial statements.
- `RELEASE/CONTENT-COVERAGE.json` reports 618 Source records, while `M13-SOURCE-IDENTITY-AND-URI-REUSE-TRIAGE-2026-10-11.md` reports 617 distinct Source IDs referenced by the Claim worksheet. These measures may differ if one Source is unreferenced, but the difference must be reconciled explicitly; do not silently treat the counts as equivalent.

## Controlled next actions

1. Verify the hydrology v2 Source and three v2 Evidence Use records are included in the current reference/linkage checks; close the stale Batch 14 finding in a follow-up note only after that check.
2. Prepare a bounded HCI metadata remediation: version the Source identity/URI to the current NIST Human-Centered Technologies page only if the corresponding Evidence Use records are versioned and pinned in the same change; retain HOLD for any Claim not directly supported.
3. For immunology, do not patch the URI in isolation. Decide the Claim-type disposition first; any replacement domain Claims require appropriate sources and a separate review.
4. Reconcile 618 Source records versus 617 Claim-referenced Source IDs by enumerating the unreferenced Source record(s), if any, and checking whether the inventory scopes match.
5. Rebuild the exact-head unscored Claim worklist from the current branch tree and the consolidated ledger, excluding previously scored, duplicated, or already triaged IDs. Only then start the next non-overlapping 100-Claim batch.

## Guardrails

- No D/E/B scores were assigned here.
- No canonical Claim, Evidence Use, Source, Context, or Relation JSON records were changed here.
- No publication allowlist or release approval was created.
- `main` remains unchanged; M13 and MVP remain separate Draft PR workstreams.
