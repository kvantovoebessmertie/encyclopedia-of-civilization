# M13 Duplicate-Score Adjudication — Water Treatment A–C and Emergency Disinfection D
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: report-level adjudication only; no Claim, Evidence Use, Source, or Relation JSON changed.

## Scope
Reconcile repeated scores in Batch 21 and Batch 27 for four normalized Claim IDs. Scores use the existing D/E/B 0–3 rubric. This is an audit-triage decision based on the Claim statements, the two reports, and the linked records fetched from the audit branch; it is not independent expert certification.

## Adjudicated scores

| Claim | Batch 21 D/E/B | Batch 27 D/E/B | Adjudicated D/E/B | Rationale |
|---|---:|---:|---:|---|
| `CLM-WATER_TREATMENT_BASICS-A` | 2/2/3 | 2/3/3 | **2/2/3** | The Claim says treatment reduces/removes contaminants to levels appropriate for the intended use. This is a useful conceptual definition, but the linked Evidence Use points to the WHO water/sanitation/health programme at domain level, not a pinpoint passage. The EU description is scoped, but its linked source is broad; E=2 is better supported than 3 until direct passage-level support is recorded. |
| `CLM-WATER_TREATMENT_BASICS-B` | 2/3/3 | 3/3/3 | **2/2/3 (provisional)** | The Claim correctly says method choice depends on source-water quality, target contaminants, and required output quality. It is a concise selection principle rather than a developed explanation, so D=2. Critical linkage issue: the Evidence Use description says EPA emergency-disinfection guidance contributes support, but its `source_ref` points only to `SRC-WATER_TREATMENT_BASICS` (WHO). The EPA source is not represented in this EU's direct pointer. Until the second source is explicitly linked in the record graph and its exact applicability is pinned, E=2 rather than 3. This is a linkage/provenance defect to resolve only in the authorized correction pass, not a finding that the Claim is false. |
| `CLM-WATER_TREATMENT_BASICS-C` | 2/2/3 | 2/3/3 | **2/2/3** | The Claim appropriately rejects one universally suitable treatment method without analysis of the specific water. It is a sound boundary, but the Evidence Use points to a broad WHO programme rather than a specific passage; E=2 pending a direct locator. Do not overread this as requiring laboratory analysis before every emergency action; applicable public-health guidance governs. |
| `CLM-M5-WATER-EMERGENCY-DISINFECTION-D` | 3/3/3 | 3/3/3 | **3/3/3** | Both reports agree. The Claim explicitly distinguishes microbial risk reduction from automatic removal of heavy metals, salts, and most chemical contaminants. The linked EU points to the EPA emergency-disinfection Source and describes that distinction specifically. Preserve this safety boundary prominently. |

## Identity and linkage checks
- The four Claim filenames and internal `record_id` values match exactly.
- For A, B, and C, each Evidence Use `claim_ref` points to the intended Claim; each `source_ref` points to `SRC-WATER_TREATMENT_BASICS`; role is `supports`.
- For D, the Evidence Use `claim_ref` points to the intended Claim and `source_ref` points to `SRC-EPA-WATER-TREATMENT-2026`; role is `supports`.
- No Claim or Evidence Use identifiers were normalized or rewritten.
- B's prose refers to an EPA source not directly named in its `source_ref`. This should be logged as a graph/provenance inconsistency, not silently treated as two-source corroboration.
- This review does not establish source independence merely from separate organizations or separate Evidence Use records; independence requires source-level and passage-level assessment.

## Disposition
1. Use the adjudicated scores above as the single report-ledger values for these repeated IDs; retain both original report scores as history.
2. Count these four normalized IDs once, not eight times.
3. In the separately authorized correction pass, either add an explicit Evidence Use/Source link for the EPA material used by Claim B or remove the unsupported source attribution from the EU description, then re-review E.
4. Improve direct source locators for A and C before treating their evidence fit as fully traceable.
5. Do not edit substantive JSON as part of this adjudication.
6. This resolves one duplicate-score group only. Full inventory-to-ledger reconciliation, semantic duplicate detection, all-record linkage review, Relations, evidence independence, Human View/adversarial review, independent scoring review, authorized corrections, regression checks, and same-HEAD CI remain open.
