# M11 Substantive Audit — 2026-10-09

## Baseline

Audit target HEAD before this audit commit: `131922b39e24fffb393fca4d7cedd567e5d03a07` (M11 planning/scope-lock branch). The audit is limited to the three locked slices and their existing sources/claims/Evidence Use.

## Findings

### M11-SUB-001 — accessibility Claim C needs a clearer international/local boundary
The current Claim C says concrete accessibility requirements depend on the object, users and applicable jurisdiction. The UN Convention supports an international obligation to improve access and calls for States Parties to develop and monitor minimum standards (Article 9), but the slice should not imply that the Convention itself supplies every technical requirement for a particular object or locality.

**Required correction:** make the Claim distinguish the Convention's international framework from technical/legal criteria that must be checked against applicable rules and the specific use context. Keep the existing Source identity and canonical URL.

### M11-SUB-002 — ergonomics Claim C exceeds the directly described process
The current Claim C includes identification, control selection and evaluation of effectiveness. The recorded NIOSH page explicitly defines an ergonomics program as a systematic process of identifying, analyzing and controlling workplace risk factors; it links to a separate program guide for further detail. The existing broad wording is plausible, but the exact recorded locator does not itself explain the full evaluation method.

**Required correction:** narrow Claim C to the directly supported identify/analyze/control process. Do not add workplace-specific operating advice or thresholds.

### M11-SUB-003 — human-factors Claims remain introductory and bounded
The three Claims describe human-system interaction, human capabilities/limitations and whole-system design. At the current level they are plausible for an introductory NASA human-factors slice; the corrective priority is to make the Evidence Use explain the specific inferential role and its limits. The exact NASA locator could not be independently retrieved by the current web fetch, which is a retrieval limitation, not proof that the URL is broken. Do not assert locator failure or change the Source record without a separate confirmed finding.

## Non-findings

- One Source per slice is not automatically a defect. No source-count quota is justified.
- No confirmed contradiction was found in the existing Context/Scope text.
- No new Claim is needed to resolve the confirmed wording gaps.
- No new Relation is required by the content correction.

## Decision

Proceed with controlled corrections within the M11 lock: narrow the two Claims only as specified above, make all nine existing Evidence Use descriptions claim-specific and source-bounded, improve the three Russian-facing READMEs, and strengthen the three existing regressions. Preserve all record IDs, provenance, source identities/URLs, claim/source references, evidence roles, Context/Scope targets and Relation participants.
