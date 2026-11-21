# M13 — consolidated remediation and validation register (359-Claim cohort)

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Validation head: `098ee29b5db089e818dfc002547b917fa07e2833`
Prior exact-reference verification baseline: `967da40d66650b1d535744ac676be28519ebc57c`

## 1. Completion boundary

The 359-row residual Generic Evidence Use cohort now has exact report-body coverage **359/359** across Imports 01–21 and prior report-body evidence. The 21 import artifacts are append-only audit records; they do not modify canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON.

Coverage is not evidence acceptance. All 359 Claims remain **HOLD**. No canonical write is authorized for this cohort, no official D/E/B value was overwritten, and no specialist, independent, rights, Human View or publication gate is cleared by this register.

## 2. Exact Claim → EU → Source validation

- Cohort size: **359** unique Claim IDs.
- Report-body coverage: **359/359**.
- Current EU record version: **v1 for all 359**.
- Exact `content.claim_ref` and `content.source_ref` IDs and versions: **359/359 confirmed**.
- Newly fetched at current branch head: **44 EU JSON files**. Each parsed as version 1 and matched the expected Claim v1 and Source v1 IDs.
- Previously fetched and checked: **315 EU records**. A GitHub comparison from `967da40d66650b1d535744ac676be28519ebc57c` to `098ee29b5db089e818dfc002547b917fa07e2833` returned only added RELEASE Markdown import artifacts; no canonical JSON path changed. Their exact prior Claim/Source reference checks therefore remain current.
- The 44 current-fetch blob SHAs and the verification basis for all 359 are recorded in the downloadable consolidated CSV.

This is a structural reference-integrity check. It does not establish that a Source passage supports the Claim, that the Source identity is correct, that the source is independent, or that rights permit reuse.

## 3. Consolidated support dispositions

Each row retains its report-specific findings. Where more than one report exists, the underlying report refs remain separately recorded; multiple mentions are not counted as new Claims.

| Consolidated disposition | Claims |
|---|---:|
| DIRECT_WITH_PINPOINT_GAP | 159 |
| PARTIAL | 84 |
| NOT_ESTABLISHED_BY_CURRENT_SOURCE | 66 |
| DIRECT | 26 |
| DIRECT_WITH_SCOPE_LIMIT | 15 |
| DIRECT_WITH_RIGHTS_HOLD | 3 |
| DIRECT_WITH_SOURCE_IDENTITY_AND_RIGHTS_HOLD | 2 |
| PARTIAL_WITH_RIGHTS_HOLD | 2 |
| PARTIAL_WITH_SOURCE_IDENTITY_AND_RIGHTS_HOLD | 1 |
| DIRECT_WITH_SCOPE_GAP | 1 |
| **Total** | **359** |

The largest group is not “accepted”: 159 direct-fit rows still lack exact locators; 84 are partial; 66 are not established by their current registered source. Only 26 carry an unqualified DIRECT disposition, and even those remain HOLD pending the remaining gates.

## 4. Rights and source-identity status

- **35 rows** contain an explicit rights/attribution review note or restriction in the imported report bodies.
- **324 rows** have no rights issue reported in the imported material. This is **not** a rights clearance; rights must be checked before copying, adapting, ingesting or redistributing source material.
- **30 rows** contain an explicit source-identity, URI, source-chain or source-scope caveat.
- **329 rows** have no specific identity defect recorded in the imported reports. Source independence is **not assessed** merely because no identity defect was reported.

Material examples requiring separate handling:
- OpenStax textbooks: prior written permission is stated as required for LLM/generative-AI ingestion; CC BY-NC-SA conditions remain separate.
- ISO 55000/55001: stored URI `83054` identifies ISO 55001:2024 while the Source title names ISO 55000:2024 (`83053`). Do not silently swap or conflate the standards; ISO's AI-use restriction remains unresolved.
- DACS: retain version 2022.0.4 and U.S. archival-community scope; do not treat it as universal records law or assume a blanket open licence.
- NIGMS Anatomy: the legacy URL could not be independently confirmed; Open RN is a distinct CC BY 4.0 candidate, not yet registered in the canonical chain.
- NIST AI and Atmospheric Science: broad landing pages/descriptive Source identities need bibliographic Sources and distinct EU locators for the specific passages.
- UNESCO AI Ethics: the Recommendation is correctly identified, but public accessibility is not blanket permission for unrestricted reuse or AI ingestion.

## 5. Non-exclusive remediation flags

The following are screening flags derived from the imported report findings/actions. They are non-exclusive and should guide the defect queue, not be read as a second independent adjudication:

| Screening flag | Claims flagged |
|---|---:|
| Pinpoint / locator issue mentioned | 332 |
| New or distinct Source/EU registration mentioned | 103 |
| Scope / jurisdiction / Claim-boundary issue mentioned | 68 |
| Specialist / independent / Human View review mentioned | 67 |
| Rights / attribution / permission issue mentioned | 35 |
| Source identity / URI / source-chain caveat mentioned | 30 |

## 6. Consolidated remediation workstreams

1. **Exact locator additions.** For direct-fit Claims, identify the smallest reproducible section, paragraph, table, figure or page locator. Keep locator work separate from source-identity changes.
2. **Source identity and URI correction proposals.** Correct only material identity defects; preserve version history and distinguish related standards or publications.
3. **New Source/EU proposals.** Register supplementary authorities as distinct Sources and EUs. Never silently attach a new passage to an existing Source ID.
4. **Partial support and Claim-scope proposals.** Map each Claim clause to evidence. Narrow unsupported clauses or add independently suitable sources; preserve jurisdictional and product/series boundaries.
5. **Rights and permissions.** Resolve explicit restrictions before ingestion, copying, adaptation or redistribution. “Publicly accessible” is not equivalent to “licensed for reuse.”
6. **No-support / source-mismatch decisions.** Where the current source does not establish the Claim, require source replacement, a separately registered corroborating Source, or an expert decision to narrow/retire the Claim.
7. **Independent and specialist review.** Risk-relevant or domain-specific Claims still need the appropriate specialist and Human View gates after source remediation.

## 7. Protected-state and CI

- Canonical Claim/EU/Source/Context/Scope/Relation writes in this pass: **0**.
- Official D/E/B values changed: **0**.
- Canonical write authorization for this 359-Claim cohort: **none**.
- All 359 Claims: **HOLD**.
- PR #21 remains open, Draft and unmerged. PR #22 remains open, Draft and unmerged.
- On validation head `098ee29`: Offline Edition completed **success**; Reference implementation tests and Release Conformance Gate were still **in progress** at the last check. Combined commit status was empty. Do not call the commit fully CI-verified until both remaining workflows explicitly conclude success.

## 8. Files and next gate

The consolidated CSV is the row-level source of truth for:
- exact report refs and findings;
- support disposition;
- rights status;
- source identity/source-chain status;
- next actions;
- current-head EU version and Claim/Source reference verification;
- authorization and HOLD state.

Next gate is **remediation proposal consolidation**, not canonical mutation: group exact locator additions, Source identity/URI corrections, new Source/EU proposals, Claim narrowing, rights holds and no-support/expert decisions into bounded packages. Obtain explicit authorization for each permitted canonical change before touching JSON. Then run the local regression suite after each authorized batch and full CI after the consolidated changes.

This register closes report-body coverage and current EU-link validation for the 359-row cohort. It does **not** close remediation, M13, release conformance or publication approval.
