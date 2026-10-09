# Unified M6 Debt Map — 2026-10-09

## Status
**OPEN — NOT CLEAN.** This map consolidates confirmed findings from the substantive, evidence, and Human View passes. It does not treat every one-source slice or every missing Relation as a defect. No content correction is authorized by this map alone; finish the Relation justification/duplicate sign-off first. M4/M5 and `main` remain unchanged.

## Confirmed debt register

| ID | Record / surface | Confirmed debt | Planned resolution | State |
|---|---|---|---|---|
| M6-SUB-01 | `CLM-LEARNING_BASICS-C` | The cited NIMH program page does not directly establish the full broad task/population/design generalization. | Narrow to a proposition directly supported by the NIMH source or add a suitable methods source. | OPEN |
| M6-SUB-02 | `CLM-LAW_BASICS-C` | The general statement about all legal rules/procedures exceeds the specific Cornell LII jurisdiction locator. | Narrow to the jurisdiction dimensions/examples the source actually describes, preserving the US-law boundary. | OPEN |
| M6-SUB-03 | `CLM-GOVERNANCE_BASICS-C` | Broad cross-country/institutional variation is not precisely supported by the single OECD framework locator. | Attribute narrowly to the OECD framework or add comparative support. | OPEN |
| M6-SUB-04 | `CLM-EDUCATION_SYSTEMS-C` | UNESCO’s rights-focused page alone does not adequately support the full comparison across financing, governance, curriculum, and delivery. | Narrow to the country/period-specific implementation point supported by UNESCO or add a comparative education source. | OPEN |
| M6-EV-01 | 18 Evidence Use records in the six slices | Evidence Use descriptions are boilerplate and do not identify passages, sections, tables, or the exact inferential role. | Replace with claim-specific support descriptions tied to the actual source material. | OPEN |
| M6-EV-02 | `CLM-SLEEP_BASICS-C` | Health-outcome claim has only one source; independent corroboration would materially improve confidence. | Add an independent public-health/clinical source and claim-linked Evidence Use, or document a defensible single-source rationale. | OPEN |
| M6-EV-03 | `CLM-LEARNING_BASICS-C` | The claim needs narrower source-supported wording or a suitable methodological source. | Resolve together with M6-SUB-01; do not create duplicate or cosmetic evidence records. | OPEN |
| M6-EV-04 | `CLM-LAW_BASICS-C` | Broad legal generalization needs narrower wording or a broader legal authority. | Resolve together with M6-SUB-02. | OPEN |
| M6-EV-05 | `CLM-DEMOGRAPHY_BASICS-B/C` | The source locator is too coarse to trace population momentum and projection assumptions to specific material. | Pinpoint relevant WPP methods/results material or add a suitable demographic-methods source; preserve reference dates and the observation/projection distinction. | OPEN |
| M6-EV-06 | `CLM-GOVERNANCE_BASICS-C` | Comparative governance claim needs comparative support or narrower attribution. | Resolve together with M6-SUB-03. | OPEN |
| M6-EV-07 | `CLM-EDUCATION_SYSTEMS-C` | Broad comparative systems claim needs comparative education evidence or narrower wording. | Resolve together with M6-SUB-04. | OPEN |
| M6-HV-01 | `CTX-DEMOGRAPHY_BASICS` | A single Context sentence mixes Russian and English. | Normalize the sentence to the corpus’s intended language convention. | OPEN |

## Non-debt observations / decisions
- One Source per slice is not automatically a defect. Add sources only where the specific Claim needs independent corroboration, broader scope, or better source fit.
- No Relation currently targets any of the six M6 slices. That absence is not itself a debt; no Relation should be created for metrics.
- Initial filename/ID mismatches in the Relation scan were false positives caused by the repository’s non-identical filename and `record_id` conventions. The inspected examples’ actual IDs were valid. No broken Relation endpoint is confirmed from that check.
- Mixed English Claim text and Russian Context/Scope/Evidence Use text may reflect a corpus convention; this is a policy ambiguity, not a confirmed debt. Do not translate broadly without checking adjacent slices and standards.
- The generic Scope anchor to Claim A may be a schema convention. Do not duplicate Context/Scope records mechanically; confirm expected reader navigation before changing it.

## Remaining audit gate before correction
1. Finish corpus-wide Relation participant identity, justification, and pairwise duplicate review; record only actual findings.
2. Freeze the final debt set.
3. Perform one controlled correction pass against the debt IDs above.
4. Re-audit all six slices and any touched Relations.
5. Synchronize relevant documentation/registry/coverage/regressions only where required by the actual diff.
6. Run Reference tests, Release Conformance Gate, and Offline Edition on the same exact HEAD. M6 CLEAN requires 3/3 green and independent verification.

No mass rewrite, quota-driven source expansion, new Record type, speculative Relation, unsupported claim, or weakened validation is authorized.
