# M8 Post-Correction Audit and Exact-Head Verification — 2026-10-09

## Status

**POST-CORRECTION AUDIT PASS; EXACT-HEAD 3/3 CI PASS at `247007768453f2679cb5823b663e97212449f22c`.** This is the last verified candidate before the documentation status-sync commit. The status-sync commit will create a successor HEAD and therefore requires a fresh exact-head 3/3 run before M8 can be accepted CLEAN.

## Verification snapshot

- Candidate SHA: `247007768453f2679cb5823b663e97212449f22c`.
- Base: accepted M7 CLEAN SHA `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`.
- Corpus preflight: PASS — 4,831 Records, 483 slices, 4,831 unique record identities, 19 Record types.
- Reference implementation tests #2768 — PASS, run https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37922490192; **969 tests passed**.
- Release Conformance Gate #2610 — PASS, final conformance state **CONFORMING**, no blocking or limiting gates: https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37922490288.
- Offline Edition #2242 — PASS: https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37922490191.
- All three workflows passed on the same exact SHA `247007768453f2679cb5823b663e97212449f22c`.
- Coverage manifest and cross-slice audit both report 4,831 Records / 483 slices. The 19 Record types remain unchanged.
- Independent branch comparison: M8 is 71 commits ahead of M7 and 0 behind. PR #13 remains OPEN/DRAFT/UNMERGED against M7. `main` remains at `203a7028e08da394fd44630fe38727be07bc8849`.
- The M8 content diff adds no Relation record and changes no Relation participant. `RELEASE/CONTENT-CROSS-SLICE-AUDIT.json` is changed only to synchronize counts and describe the current baseline.

## Post-correction content review

### M8-DEPTH-001 — mechanics-basics: PASS after correction
Claims A–C now express Newton's first, second and third laws, with explicit conditions: inertial frame and zero net force for the first law; constant mass and classical regime for `F_net = m·a); equal/opposite interaction forces applied to different bodies for the third law. Each Claim links to claim-specific Evidence Use naming the exact OpenStax section and URL (§5.2, §5.3, §5.5). Context/Scope bound the slice to introductory classical mechanics and exclude advanced/relativistic/quantum and specific engineering design. The dedicated regression asserts all three substantive concepts and non-generic evidence descriptions.

Post-correction desk scores:
| Claim | D | E | B | Reason |
|---|---:|---:|---:|---|
| `CLM-MECHANICS_BASICS-A` | 2 | 3 | 2 | Substantive first-law proposition, exact textbook locator and inertial-frame condition. |
| `CLM-MECHANICS_BASICS-B` | 2 | 3 | 3 | Formula and constant-mass/classical boundary explicit. |
| `CLM-MECHANICS_BASICS-C` | 2 | 3 | 3 | Pair forces correctly distinguished as acting on different bodies. |

The source is a canonical university physics textbook and the claims are introductory descriptions of its own chapter; one authoritative source is proportionate here. No corroboration quota is imposed.

### M8-DEPTH-002 — statistics-basics: PASS after correction
Claims B/C now describe assumptions/data representativeness and experimental design without implying that all methods share identical assumptions or that observational comparison establishes causality. Evidence Use B is tied to NIST/SEMATECH handbook material on method assumptions/data; Claim C has specific NIST support plus OpenStax §1.4 Experimental Design and Ethics, with a claim-specific locator and a Russian-language description. Context/Scope and README now state applicability limits. The regression requires the new source and evidence links and rejects generic placeholder material.

Post-correction desk scores:
| Claim | D | E | B | Reason |
|---|---:|---:|---:|---|
| `CLM-STATISTICS_BASICS-B` | 2 | 2 | 2 | Method assumptions and data representativeness are explicit; NIST support is claim-specific. |
| `CLM-STATISTICS_BASICS-C` | 2 | 3 | 3 | Experimental variables, random assignment, and the observational-causality boundary are explicit and independently supported. |

### M8-BOUNDARY-003 — water: PASS after correction
`CTX-WATER-EMERGENCY` and `SCP-WATER-EMERGENCY` now encode the contamination-dependent applicability boundary in Records, each targeted to an existing Claim. The Scope explicitly excludes regional water certification, replaces no local advisory, and states that chemical/fuel/radioactive contamination is not resolved by boiling. The dedicated water regression checks both records, target references and the key boundary. Release Gate G16 now requires the 12-record package shape plus these specific structured boundaries; it does not merely accept an increased count.

### M8-HUMAN-004 — governance-basics: PASS after correction
Three Claim statements, README and four Evidence Use descriptions are Russian-facing. Canonical source identities/titles, IDs, provenance, claim/source references, evidence roles and source scope remain unchanged. The regression checks Russian-facing content and the WGI evidence linkage.

### Relation delta and safety checks
No Relation Records or participants were added, removed or changed. The only Relation-related file in the diff is the audit artifact, synchronized from 4,827 to 4,831 corpus Records and updated to reflect M8's no-Relation delta. G16 was strengthened to check machine-readable Context/Scope rather than weakened.

## Human View and review limitations

Desk-based Human View/adversarial review passes for the four corrected slices: topic and limits are findable, claim/evidence language is consistent with the Russian-facing content, and safety/applicability boundaries are visible. This is **not** a live novice usability study. No independent external human reviewer participated; source fit was rechecked against the named public source material and the changed claims were reviewed again against the locked rubric. This limitation is retained explicitly.

## Final status procedure

The verification above applies only to SHA `247007768453f2679cb5823b663e97212449f22c`. The documentation status-sync commit that records these results creates a new HEAD, so Reference tests, Release Conformance Gate and Offline Edition must all pass again on that exact successor SHA. If they do, record M8 CLEAN in PR #13 discussion without any further code-tree change. Do not merge PR #13 as part of this checkpoint.
