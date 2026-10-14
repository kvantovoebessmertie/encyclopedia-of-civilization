# M13 Correction Authorization — Human–Computer Interaction Source/Evidence Alignment — 2026-10-14

Authorization ID: `M13-HCI-SOURCE-EVIDENCE-001`

Status: **bounded authorization for controlled metadata/evidence correction; not publication approval**

## Finding and rationale

Batch 14 identified that `SRC-HUMAN_COMPUTER_INTERACTION_BASICS@1` uses a sentence describing the subject as its source identity and points to the NIST Information Access Division landing page. That URI now redirects to a division page rather than a claim-specific HCI reference. The three linked Evidence Use descriptions are generic and do not identify passages.

A more direct NIST reference is “Human Centered Design (HCD)” at:
https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design

The page explicitly describes interactive systems, users and their needs, context of use, user-centered evaluation, iterative design, and principles such as controllability. It also warns that the page is no longer updated and may be out of date. It is therefore a bounded conceptual source, not a current compliance standard and not proof for every Claim in this slice.

## Authorized scope

On branch `m13-system-wide-depth-audit-2026-10-09`, only these existing records may be versioned:

- `SRC-HUMAN_COMPUTER_INTERACTION_BASICS` @1 → @2: correct source identity to the actual NIST page title/publisher and update URI to the exact HCD page above.
- `CLM-HUMAN_COMPUTER_INTERACTION_BASICS-A/B/C` @1 → @2: change only `provenance.created_from` to Source @2; preserve all Claim wording and types.
- `EU-HUMAN_COMPUTER_INTERACTION_BASICS-A/B/C` @1 → @2: update Claim refs to Claim @2 and Source refs to Source @2; add claim-specific source locator and explicit scope limits in `content.material.description`.
- `CTX-HUMAN_COMPUTER_INTERACTION_BASICS` and `SCP-HUMAN_COMPUTER_INTERACTION_BASICS` @1 → @2: change only the target reference to Claim A @2.
- Strengthen only the dedicated HCI slice regression, update the slice README, register this authorization in `RELEASE/EDITORIAL-CORRECTION.json`, and add a bounded M13 checkpoint note.

Evidence-use boundaries:
- Claim A (interface provides means for perception and system control): the NIST HCD page gives relevant conceptual context but does **not** directly establish the complete wording. Record this limitation explicitly; Claim A remains HOLD pending a better pinpoint/source or wording review.
- Claim B (usability depends on user, task, context and interface characteristics): the page supports the user/context and usability framing; it does not independently establish every listed factor in the exact Claim. Keep the statement provisional/HOLD pending passage-level review.
- Claim C (evaluation should use observable tasks and conditions): the page supports user-centered evaluation and iterative evaluation/design. Do not claim it prescribes a universal evaluation protocol or proves all methods valid.

## Exclusions and controls

No Claim wording/type changes, new/deleted records, new Record types, Relation changes, unrelated slices, scoring-ledger edits, D/E/B score assignments, publication allowlist, release status, schemas, or `main` changes are authorized. Preserve prior versions/history and stable internal record IDs. The correction must pass preflight, the dedicated regression, Reference Tests, Release Conformance Gate, and Offline Edition on the same exact final HEAD, followed by independent Human View and diff/base/main verification. The slice and all three Claims remain publication HOLD until those gates are independently closed.
