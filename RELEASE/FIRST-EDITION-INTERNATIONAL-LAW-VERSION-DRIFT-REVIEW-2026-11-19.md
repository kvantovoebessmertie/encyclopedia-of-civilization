# International Law — Canonical Version Drift Review

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Comparison base: `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`  
Current inspection HEAD: `d5f81dab7abe73270274e0ceaec2bb2d29fd2cf2`  
Source audit: `RELEASE/FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md`

## Finding

The Legal/Trade/Institutional addendum records 13 canonical records in `international-law-basics` at version 1. At the current inspection HEAD, all 13 canonical JSON files exist at version 2 and their record types match. The record IDs match, but the versions do not.

**Result:** the audit table is stale for these 13 records. The v1 review decision remains historical HOLD. The v2 records are separately held pending review of the changed fields. No automatic decision transfer is permitted.

## Exact version map

| Audited version | Current canonical version | Type |
|---|---|---|
| `SRC-INTERNATIONAL_LAW_BASICS@1` | `SRC-INTERNATIONAL_LAW_BASICS@2` | source |
| `CLM-INTERNATIONAL_LAW_BASICS-A@1` | `CLM-INTERNATIONAL_LAW_BASICS-A@2` | claim |
| `CLM-INTERNATIONAL_LAW_BASICS-B@1` | `CLM-INTERNATIONAL_LAW_BASICS-B@2` | claim |
| `CLM-INTERNATIONAL_LAW_BASICS-C@1` | `CLM-INTERNATIONAL_LAW_BASICS-C@2` | claim |
| `EU-INTERNATIONAL_LAW_BASICS-A@1` | `EU-INTERNATIONAL_LAW_BASICS-A@2` | evidence_use |
| `EU-INTERNATIONAL_LAW_BASICS-B@1` | `EU-INTERNATIONAL_LAW_BASICS-B@2` | evidence_use |
| `EU-INTERNATIONAL_LAW_BASICS-C@1` | `EU-INTERNATIONAL_LAW_BASICS-C@2` | evidence_use |
| `CTX-INTERNATIONAL_LAW_BASICS@1` | `CTX-INTERNATIONAL_LAW_BASICS@2` | context |
| `SCP-INTERNATIONAL_LAW_BASICS@1` | `SCP-INTERNATIONAL_LAW_BASICS@2` | scope |
| `SRC-INTERNATIONAL_LAW_BASICS-INDEPENDENT@1` | `SRC-INTERNATIONAL_LAW_BASICS-INDEPENDENT@2` | source |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-A@1` | `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-A@2` | evidence_use |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-B@1` | `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-B@2` | evidence_use |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-C@1` | `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-C@2` | evidence_use |

## Change impact by record family

| Record family | Changed fields | What changed |
|---|---|---|
| Primary UN Charter Source | `record_version`, `content` | Source identity now names the UN Charter (1945) and adds exact Preamble / Articles 1–2 / 33 / 110–111 locators |
| Three Claims A–C | `record_version`, `provenance` | Claim statements are unchanged; provenance is re-linked to v2 Source and Evidence Use versions |
| Three primary Evidence Use records A–C | `record_version`, `provenance`, `content` | Exact UN Charter article locators were added; descriptions now bound what the Charter does and does not support |
| Context | `record_version`, `content` | Target reference advanced from Claim A v1 to Claim A v2; context text remains substantively unchanged |
| Scope | `record_version`, `content` | Target reference advanced from Claim A v1 to Claim A v2; scope text remains substantively unchanged |
| Independent ICRC Source | `record_version`, `content` | Britannica source was replaced by the ICRC *Handbook on International Rules Governing Military Operations* (2013), with §2.1 page locators |
| Three independent Evidence Use records | `record_version`, `provenance`, `content` | References advanced to Claim/Source v2; precise ICRC section/page locators and explicit limits on what the independent source supports were added |

## Assessment and required handling

1. The primary Source change is substantive: it now identifies the UN Charter directly and supplies exact article locators.
2. Claim A–C statements did not change, but their provenance and supporting evidence graph did.
3. The primary and independent Evidence Use records changed substantively. The new locators and boundary descriptions improve traceability, but they still require evidence-role and pinpoint review.
4. The independent source changed from Encyclopaedia Britannica to an ICRC handbook. Rights, source authority, relevance and scope must be reviewed against the new source.
5. Context and Scope now target Claim A v2. Their target closure is correct at the current version, but the applicability text must be checked against the revised evidence graph.

## Decision state

- v1 records: historical audit HOLD; retain for lineage, do not delete.
- v2 records: HOLD — CURRENT VERSION NOT COVERED BY THE EXISTING LEGAL AUDIT.
- INCLUDE: 0.
- EXCLUDE: 0.
- No allowlist entry created.
- No canonical JSON changed by this review.

## Required next work

1. Re-review the 13 v2 records as one coherent dependency unit: 2 Sources, 3 Claims, 6 Evidence Use records, Context and Scope.
2. Check UN Charter Articles 1–2 and 33/110–111 against each claim's exact wording and Evidence Use role.
3. Check ICRC Handbook §§2.1.0.1, 2.1.0.3, 2.1.0.5–2.1.0.6 and page locators; preserve the stated limits on independent support.
4. Revalidate all Claim → Evidence Use → Source references and Context/Scope targets at the same frozen HEAD.
5. Update the consolidated master register with both v1 historical audit rows and v2 current HOLD rows.



## Substantive re-review closure — 2026-11-19

The bounded current-version review is complete and recorded in `FIRST-EDITION-INTERNATIONAL-LAW-V2-SUBSTANTIVE-DEPENDENCY-REREVIEW-2026-11-19.md`.

- All 13 current v2 canonical records were re-fetched at PR HEAD `50d37a3da7c66fc383783d21cf3fd08d9aa6038f`: 13/13 exact IDs, versions and types match.
- All nine Claim→Evidence Use→Source edges resolve to exact declared versions.
- All three primary UN Charter Evidence Use records have claim-specific article locators. The direct fit is strongest for Claims B and C; Claim A's general definition is directly supported by ICRC Handbook §2.1.0.1, while the UN Charter passage is contextual rather than a general definition.
- Independent ICRC Evidence Use A has a direct definition locator. Independent B is only partial treaty-definition context and does not itself identify the UN Charter. Independent C's locator on sources of international law does not support Claim C's sovereign-equality/peaceful-settlement propositions.
- Claims B and C need editorial consideration of the UN Member boundary; Claim B's phrase “principles of international relations” is broader than the Charter's express framing for the Organization and its Members.
- Context and Scope both target Claim A v2 exactly. No applicability is inferred for Claims B or C.
- The controlling Evidence Use Standard permits only `supports` and `contradicts`; do not invent a “contextualizes” base role to mask a weak support edge.
- All 13 v2 records remain HOLD. No canonical JSON, version, allowlist or publication state changed. Rights clearance and qualified legal/editorial sign-off remain open.

The prior “required next work” list is superseded for identity/version re-fetch and the bounded substantive re-review. Remaining actions are the authorized Claim/EU wording and role decisions, source-rights review, and independent legal/editorial approval. No canonical change is authorized by this review.
