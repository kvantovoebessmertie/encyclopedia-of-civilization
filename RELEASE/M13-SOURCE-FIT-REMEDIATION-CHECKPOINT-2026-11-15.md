# M13 source-fit remediation checkpoint — Packages 29–31 follow-up

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Authorization: `M13-SOURCE-FIT-REMEDIATION-001`
Authorization document: `RELEASE/M13-SOURCE-FIT-REMEDIATION-AUTHORIZATION-2026-11-15.md`
Checkpoint HEAD before this document: `0c20a41f8e28e9ebeacb70febbb75739d28b1495`

## 1. Changes made within the authorization

### New Sources — 7
- Maps and navigation: USGS US Topo accuracy FAQ; USGS US Topo currency FAQ.
- Materials basics: NIST Materials Science and Engineering Division; NIST Mechanical Performance Group.
- Materials science: NIST Mechanical Performance Group.
- Manufacturing systems: NIST Smart Manufacturing Systems Test Bed; NIST AMS 200-2.

### New Evidence Use — 9
- Maps and navigation Claim C: separate accuracy and currency evidence links, preserving the US-specific scope and non-authoritative-for-navigation caveat.
- Materials basics: NIST division source for Claim A; Mechanical Performance Group for Claim C's operating-condition component.
- Materials science: NIST composites evidence for Claim B; NIST mechanical-performance/failure-analysis evidence for Claim D.
- Manufacturing systems: Test Bed evidence for Claims B and C; AMS 200-2 evidence for Claim C.

### Existing Evidence Use correction — 1
`EU-M5-MATERIALS-SCIENCE-NSF-B` version 1 → 2. Its description now correctly says NSF names metals, ceramics, polymers and semiconductors and does not explicitly name composites. The composite example is supported separately by the NIST Evidence Use. All references, provenance, role and unrelated fields are preserved.

### Documentation and regression
- Updated the four authorized slice READMEs.
- Updated the four dedicated slice regressions to the actual new record counts and evidence relationships.
- Extended `REFERENCE/tests/test_m13_evidence_linkage_audit.py` with exact Claim/Source/Evidence Use reference and limitation assertions.
- Updated `RELEASE/CONTENT-COVERAGE.json` from actual tree counts only.

## 2. Reconciled corpus counts

| Measure | Before | After |
|---|---:|---:|
| Total records | 4,834 | 4,850 |
| Source records | 619 | 626 |
| Evidence Use records | 1,670 | 1,679 |
| Vertical slices | 483 | 483 |
| Claims | 1,494 | 1,494 |

The additions are exactly 7 Source and 9 Evidence Use records. No Claim, Context, Scope, Relation, risk metadata or D/E/B ledger record was changed.

## 3. Source-fit disposition and limitations

- **Maps and Navigation C:** source support is improved for map accuracy and currency. USGS states that accuracy varies by underlying datasets and that its maps are general-reference products, not authoritative/official navigation products. The three-year cycle is a U.S. US Topo programme example and has source-layer variation; it is not a universal rule.
- **Materials A:** the NIST division page directly supports work involving measurement methods, models, data and standards, including structure/property/processing relationships.
- **Materials C:** the NIST Mechanical Performance Group supports the operating-condition and performance-within/outside-design-limits component; it does not by itself establish every composition/structure/processing pathway.
- **Materials Science B:** the NSF attribution has been corrected; NIST separately supplies the composites example. The classification remains non-exhaustive/non-mutually-exclusive, and the class label alone does not determine application suitability.
- **Materials Performance D:** NIST supports mechanical property data, extreme conditions and failure analysis. The application-specific material-selection framework remains only partially supported. Claim stays PARTIAL/HOLD.
- **Manufacturing Systems B:** the NIST Test Bed supplies a concrete example of integrated fabrication/inspection, data collection and performance improvement. It does not directly prove universal improvement in manufactured-output reproducibility. Claim stays PARTIAL.
- **Manufacturing Systems C:** the NIST Test Bed and AMS 200-2 support one concrete digital integration/data collection/curation/reuse pathway. Do not generalize this to every manufacturing system.

## 4. Rights and use boundaries

- USGS pages are official public-domain references; inspect page-level third-party markings and use only USGS-authored factual content.
- NIST pages are public information except material marked copyrighted; attribution and page-level exception checks remain required.
- NIST AMS 200-2 is a NIST Technical Series publication by Moneer Helu and Thomas Hedberg Jr., identified in NIST material as Engineering Laboratory staff. NIST's technical-series policy provides reuse rights for NIST-employee-authored works to the extent NIST may assert rights abroad; preserve attribution and avoid extended quotation. Third-party material, if marked, remains excluded.
- NSF text reuse remains subject to NSF's own page-level copyright notice; this correction is a factual evidence description and does not reproduce the NSF page.
- ISO 31000 remains RIGHTS HOLD. The metadata-only EU provenance correction previously authorized does not permit use of ISO content. Orange Book Annex 5's ISO-derived definition remains excluded from AI evidence use.
- National Academies Press copyrighted material remains excluded absent permission.

## 5. Verification state

- The prior baseline HEAD `7b680dec27ec3b25cd45779b7f0988141ee558ac` passed Reference Tests, Release Conformance Gate and Offline Edition (3/3).
- The source-fit changes are now present in the branch tree at `0c20a41f8e28e9ebeacb70febbb75739d28b1495`.
- The current final checkpoint document creates a new HEAD; therefore CI must be checked again on the exact HEAD after this document is committed.
- Required checks: JSON/schema/content preflight; all four dedicated slice regressions; M13 evidence-linkage audit; Reference Tests; Release Conformance Gate; Offline Edition; independent exact diff/tree audit.

## 6. Decision

This checkpoint records bounded source-fit remediation, not final D/E/B assessment. No Claim is declared assessed or cleared for publication by these additions. Manufacturing Systems B and Materials Performance D remain PARTIAL/HOLD; Materials Science B retains an application-suitability caveat; Maps and Navigation C remains scoped to U.S. US Topo examples and their stated limitations.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft and unmerged. `main` remains unchanged.
