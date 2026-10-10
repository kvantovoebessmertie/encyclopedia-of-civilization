# M13 Follow-up Audit — Duplicate Scores, Identifier Aliases, and Evidence Linkage

Date: 2026-10-10  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **Findings recorded; no Claim content or identifiers changed. This is not M13 closure.**

## 1. Conflicting scores across review batches 21 and 27

The two reports review the same three foundational water-treatment Claims. The recorded scores differ:

| Claim ID | Batch 21 (D/E/B) | Batch 27 (D/E/B) | Difference |
|---|---:|---:|---|
| `CLM-WATER_TREATMENT_BASICS-A` | 2/2/3 | 2/3/3 | E: 2 → 3 |
| `CLM-WATER_TREATMENT_BASICS-B` | 2/3/3 | 3/3/3 | D: 2 → 3 |
| `CLM-WATER_TREATMENT_BASICS-C` | 2/2/3 | 2/3/3 | E: 2 → 3 |

These are not harmless duplicate rows: the changed dimensions require an explicit adjudication record. Batch 27 gives more specific descriptions of the WHO/EPA roles, but the current record graph is not uniformly aligned with that narrative:

- Claim A's Evidence Use record `EU-WATER_TREATMENT_BASICS-A` links only to `SRC-WATER_TREATMENT_BASICS` (WHO domain-level page). The record does not itself link an EPA technology-overview source, although Batch 27's rationale says WHO and EPA independently support the claim.
- Claim B has two Evidence Use links: `EU-WATER_TREATMENT_BASICS-B` to the WHO domain-level page, and `EU-EPA-WATER-TREATMENT-B` to `SRC-EPA-WATER-TREATMENT-2026`. The latter description is still generic and has no section/passage locator.
- Claim C's Evidence Use record `EU-WATER_TREATMENT_BASICS-C` links only to the WHO domain-level page; its description explains the scope boundary but does not identify a specific passage.

**Disposition:** retain both historical score rows; do not silently replace one with the other or average them. Pending action is to verify the exact cited passages, verify which sources are actually linked to each Claim, and add a documented score-adjudication decision with reasons. Until then these three scores are **conflicted / not adjudicated**.

## 2. Identifier aliases in web-systems-basics

The three files below have short filenames but complete internal IDs:

| File path | Internal record_id |
|---|---|
| `CONTENT/vertical-slices/web-systems-basics/records/CLM-A.json` | `CLM-WEB_SYSTEMS_BASICS-A` |
| `CONTENT/vertical-slices/web-systems-basics/records/CLM-B.json` | `CLM-WEB_SYSTEMS_BASICS-B` |
| `CONTENT/vertical-slices/web-systems-basics/records/CLM-C.json` | `CLM-WEB_SYSTEMS_BASICS-C` |

Their corresponding Evidence Use records are also stored as `EU-A.json`, `EU-B.json`, and `EU-C.json`, while their internal IDs and `claim_ref` values use the full IDs. The links resolve internally when using record_id, but filename-based tools and conventions may fail to find these records. This is a structural alias, not evidence that the Claims are semantically wrong.

**Disposition:** no renames or ID edits made. Before any repair, enumerate and test every path-based reference, manifest, loader, test, and external consumer. Prefer a controlled migration with regression tests over a one-off rename.

## 3. Evidence linkage quality: generic descriptions remain a corpus-wide concern

The web-systems slice illustrates a stronger issue than the filename aliases: each Evidence Use record correctly points to a matching Claim and Source, but all three descriptions say only:

> «Источник используется в пределах заявленного контекста и ограничений.»

That statement does not identify the source's relevant proposition, section, paragraph, or other pinpoint. The linked source is MDN's “How the Web Works” page. The graph is structurally connected, but a reviewer cannot reproduce claim-specific support from the Evidence Use description alone.

This distinction must remain explicit in the audit:
- **Structural link passes:** the Evidence Use record points to the intended Claim and Source.
- **Substantive support is not yet demonstrated:** no pinpoint passage or claim-specific explanation is stored.
- A source attached to Claim A is not corroboration for Claim B unless an Evidence Use record explicitly links that source to Claim B and explains the support.

## 4. Required follow-up gates

1. Adjudicate the three conflicting water-treatment scores against claim-specific source passages.
2. Run a repository-wide filename ↔ internal ID ↔ reference audit; classify separator-only aliases separately from abbreviated filenames such as `CLM-A.json`.
3. Build an evidence-linkage audit that checks both reference integrity and evidentiary specificity, including passage/section locators where feasible.
4. Do not edit published Claim content or identifiers as part of this diagnostic step. Any authorized repair must be isolated, reviewed, and regression-tested.
5. Keep M13 open until score conflicts, identity/linkage exceptions, high-consequence review, and the remaining agreed audit gates are resolved.

## Scope limitation

This report records verified examples and follow-up gates. It does not claim that all 1,494 Claims have been semantically reviewed, that all evidence links are defective, or that the listed examples exhaust all identifier and support problems.
