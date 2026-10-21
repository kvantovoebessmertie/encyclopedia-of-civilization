# M13 Machine Census Result — 2026-10-09

## Status

**STRUCTURAL / SCHEMA / REGISTERED TYPE CENSUS: PASS at the recorded SHA. SEMANTIC DEPTH AND FULL LINKAGE MANIFEST: NOT YET COMPLETE.**

This report records an observed full-corpus CI census, not a claim that all content is true, sufficiently deep, or fully usable.

## Exact execution

- Repository: `kvantovoebessmertie/encyclopedia-of-civilization`
- M13 branch: `m13-system-wide-depth-audit-2026-10-09`
- Exact tested HEAD: `bd118b222b97f96e0fb65200f7af363e00400d95`
- Reference implementation tests run: [#37959405779](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37959405779)
- Release Conformance Gate run: [#37959422317](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37959422317)
- Offline Edition run: [#37959422289](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37959422289)

Observed from the Reference workflow log on that HEAD:

`PREFLIGHT PASS: 4831 records, 483 slices, 4831 unique record identities, 19 record types.`

The same workflow reports **969 passed** tests. The three workflow jobs completed successfully on the same HEAD.

## What the existing machine checks establish

The preflight and full-corpus tests in `REFERENCE/preflight_content.py` and `REFERENCE/tests/test_content_coverage.py` perform more than a filename count. They parse the corpus JSON, validate records against `IMPLEMENTATION/005-RECORD-SCHEMA.json`, run the registered dataset-level semantic rules, check duplicate (record ID, version) identities, compare actual `record_type` counts with `RELEASE/CONTENT-COVERAGE.json`, verify slice README/record/regression presence and public registration, and exercise the content package/recovery path.

The passing full-corpus coverage test asserts that the actual type-count mapping equals the manifest mapping. Therefore the manifest's per-type counts are machine-verified at this HEAD, not merely inferred from filename prefixes:

| Record type | Verified count |
|---|---:|
| record | 4 |
| claim | 1,494 |
| source | 617 |
| evidence_use | 1,669 |
| assessment | 1 |
| inference | 1 |
| decision | 1 |
| action | 3 |
| event | 1 |
| result | 2 |
| state | 2 |
| process | 1 |
| relation | 64 |
| identity | 1 |
| context | 484 |
| scope | 483 |
| provenance | 1 |
| authorship_contribution | 1 |
| trust_reputation | 1 |
| **Total** | **4,831** |

The type counts sum to 4,831. The machine check verifies the type set against the 19 registered types and the manifest. The prior filename-prefix mismatch count of 33 remains a naming/identity investigation; a prefix mismatch alone is not a semantic defect when the record's actual `record_type` is valid.

## What is not established by this result

The existing checks do **not** constitute the complete, human-reviewed M13 audit. The following remain open:

1. Produce a persistent per-slice manifest of every record ID, actual type and version, including an explicit disposition for all 33 filename-prefix exceptions.
2. Export and reconcile every Claim → Evidence Use → Source linkage, including missing, duplicate, ambiguous and cross-slice references. Dataset semantic rules passing is useful evidence, but does not replace a readable audit manifest or source-fit review.
3. Inventory every Context/Scope target and each Relation endpoint/justification; classify unresolved or ambiguous references.
4. Reconcile M9–M12 authorization, dedicated regressions and debt dispositions against the actual current diffs.
5. Lock a reproducible high-consequence risk screen.
6. Score every Claim on D/E/B, with rationale and a fixed denominator; retain malformed/unscorable claims in the denominator.
7. Complete the high-consequence overlay, desk-based Human View, integration review and independent scoring review.
8. After any commit, rerun all three workflows on one identical final HEAD and recheck PR/base/main.

## Guardrails

- No content records were changed by this census report.
- No new record types or Relations are authorized.
- `main` remains unchanged; M12 remains open/draft/unmerged and M13 remains a draft.
- CI PASS is evidence of the checks actually executed, not proof of truth, expert certification, or system-wide explanatory depth.
- This report describes the observed pre-commit HEAD above. Adding this report creates a new HEAD and therefore invalidates the old exact-head acceptance evidence for final M13 closure; fresh same-HEAD workflow results are required.
