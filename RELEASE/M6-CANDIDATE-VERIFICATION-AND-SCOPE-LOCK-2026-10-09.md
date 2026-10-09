# M6 Candidate Verification and Scope Lock — 2026-10-09

## Status
**M6 scope locked for audit only.** This document authorizes review, not content edits. M4 and M5 remain closed; `main` is unchanged.

## Baseline
M5 CLEAN checkpoint: `c911c6b4ad791cb933293608e298e318a608a02f`.
Corpus: 479 vertical slices / 4,754 Records / 19 Record types / 601 Sources / 1,634 Evidence Use / 64 Relations.

## Candidate verification summary
Current Claims A–C, Source, Evidence Use A–C, Context, and Scope were inspected for each candidate. Each has 9 Records, one Source, three Claims, three Evidence Use records, one Context and one Scope. Evidence Use entries are claim-linked but generally use generic descriptions; that alone does not establish source fit. This is a selection-stage review, not the full substantive or evidence audit.

| Slice | Decision and reason | Audit focus |
|---|---|---|
| `sleep-basics` | INCLUDE. Claims cover sleep stages, circadian rhythm and possible health/attention effects; source is NHLBI/NIH “How Sleep Works”. Context explicitly distinguishes general physiology from individual sleep disorders. | Confirm source support per Claim, assess material benefit of independent corroboration, and preserve medical boundaries. |
| `learning-basics` | INCLUDE. Claims cover encoding/consolidation/retrieval/working memory, interacting neural systems and task/population/design dependence; source is NIMH Learning and Memory Program. | Verify that the neuroscience-focused source supports all Claims; do not turn general mechanisms into universal learning prescriptions. |
| `law-basics` | INCLUDE. Claims cover jurisdiction and the jurisdiction-specific nature of rules; source is Cornell Legal Information Institute, Wex “Jurisdiction”. Context identifies this as a US-law teaching example and requires jurisdiction/date for concrete questions. | Check source fit; preserve jurisdiction and effective-date limits; avoid presenting the example as universal. |
| `demography-basics` | INCLUDE. Claims cover fertility, mortality, migration, population momentum and model-based projections; source is UN Population Division, World Population Prospects 2024. | Check conceptual source fit and preserve territory, reference date, assumptions, and observation/projection distinction. |
| `governance-basics` | INCLUDE. Claims cover public governance, OECD's framework and institutional/national variation; source is OECD, “Policy Framework on Sound Public Governance”. Context is descriptive and non-ranking. | Separate the OECD framework from universal claims; assess independent evidence only where materially needed. |
| `education-systems` | INCLUDE. Claims cover education as a right, state responsibilities, and cross-country system variation; source is UNESCO, “The right to education”. Context requires country, period and applicable rules for concrete obligations. | Check whether the rights-focused source supports the broader system-variation Claim; preserve jurisdiction/period limits. |

## Exclusions
- `nutrition-basics`: already has a more developed structure, including an additional Claim and further source/evidence records; no verified reason to reopen it from count alone.
- `mental-health-information-boundaries`: already has a more developed evidence structure, including an additional NIMH source; importance alone is not a gap.
- All M1–M5 target slices are excluded to avoid duplicate maturation.

A filename-level scan found no Relation records inside these six candidate directories. This does not rule out Relations from other slices to these Claims; endpoint and duplicate review remains part of the M6 Relation audit.

## Locked scope
1. `sleep-basics`
2. `learning-basics`
3. `law-basics`
4. `demography-basics`
5. `governance-basics`
6. `education-systems`

No new slice or Record type is authorized. Inclusion is based on specific audit questions and cross-domain value, not a record-count quota.

## Sequence
1. Substantive audit.
2. Evidence independence/diversity audit, evaluated per Claim.
3. Human View/adversarial audit.
4. Relation endpoint, justification and duplicate audit.
5. Unified Debt Map with confirmed findings only.
6. One controlled correction pass.
7. Post-correction substantive re-audit.
8. Synchronize documentation, coverage, registry, provenance and dedicated regressions.
9. Reference tests + Release Conformance Gate + Offline Edition on the exact same HEAD.
10. CLEAN checkpoint only after all three are green on that exact HEAD, followed by independent verification.

## Exclusions and Definition of Done
No mass rewrite, artificial quota, new Record type, metric-driven Relation, unsupported threshold or causal claim, or weakened test/schema/conformance. No promotion based on scope lock alone. M6 is CLEAN only when confirmed substantive, evidence, Human View and Relation debts are resolved; regressions and metadata are synchronized; and exact-HEAD CI is 3/3 green.
