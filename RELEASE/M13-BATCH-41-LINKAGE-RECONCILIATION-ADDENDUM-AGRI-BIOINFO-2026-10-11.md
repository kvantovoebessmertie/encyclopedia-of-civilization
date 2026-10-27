# M13 Batch 41 Linkage Reconciliation — Agricultural Engineering and Bioinformatics Addendum

Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: candidates 95–100 from `M13-BATCH-41-LINKAGE-RECONCILIATION-2026-10-11.md`.
Method: fetched Claim, Evidence Use (EU), and Source JSON records individually; compared exact record IDs, Claim `provenance.created_from`, EU `claim_ref`, EU `source_ref`, and `evidence_role`. No content JSON was changed.

## Structural linkage results

All six rows pass the structural pointer checks:
- Claim records have `record_type=claim`.
- EU records have `record_type=evidence_use`.
- Each EU `claim_ref.record_id` matches its Claim's internal `record_id`.
- Each EU `source_ref.record_id` matches the Source ID in Claim provenance.
- Each EU `evidence_role=supports`.
- Each referenced Source record exists.

Separator differences are preserved; no IDs were renamed or merged.

## Per-claim source-fit results

| Candidate | Claim statement (short) | Source and fit | Disposition |
|---|---|---|---|
| 95 — `CLM-AGRICULTURAL_ENGINEERING_BASICS-A` | Agricultural engineering discipline overview | FAO land/water management is relevant but does not define the full discipline. EU description is generic. | Structural pass; source-fit weak. Add a direct engineering-discipline definition and claim-specific EU locator under authorized correction scope. |
| 96 — `CLM-AGRICULTURAL_ENGINEERING_BASICS-B` | Irrigation, drainage, land/water operations | FAO supports irrigation and water management, but the stored URL does not pinpoint drainage or the full “other operations” scope. | Structural pass; source-fit partial. Add a direct drainage locator or narrow the statement after authorization. |
| 97 — `CLM-AGRICULTURAL_ENGINEERING_BASICS-C` | Crop, soil, water, climate, energy, labour and operating conditions | FAO supports land/water management and agricultural water management, but does not establish this complete factor list at the stored locator. | Structural pass; source-fit partial/weak. Need direct sources for the complete systems list or a narrower statement. |
| 98 — `CLM-BIOINFORMATICS_BASICS-A` | Computational methods applied to biological data | NCBI computational-biology/bioinformatics material supports computational analysis of biological data. Stored Source URI is only the Bookshelf root. | Structural pass; source-fit partial due to imprecise locator. Direct candidate: https://www.ncbi.nlm.nih.gov/books/NBK550342/ |
| 99 — `CLM-BIOINFORMATICS_BASICS-B` | Databases organize storage/retrieval of biological information | NCBI documents broad database/resource collections and online access; stored root URI is not claim-specific. | Structural pass; source-fit partial. Add a direct database/resource locator. |
| 100 — `CLM-BIOINFORMATICS_BASICS-C` | Sequence analysis identifies similarities/differences | NCBI *Biological Sequence Analysis* explicitly describes comparing biological sequences and identifying similarities/differences. Stored Source URI remains the Bookshelf root. | Structural pass; source-fit good, locator weak. Direct candidate: https://www.ncbi.nlm.nih.gov/books/NBK550342/ |

## Evidence Use quality

All six EU records use generic descriptions (e.g. “Source supports the claim within the stated scope” or “Source is used within the stated material”). These descriptions do not identify the passage or the specific proposition supported. This is an evidence-description quality issue, not proof that the Claims are false.

## Source-locator discrepancies

- Agricultural engineering Source record `SRC_AGRICULTURAL_ENGINEERING_BASICS` points to FAO land/soil/water management: https://www.fao.org/land-water/land/soil-water-management/en/
- Bioinformatics Source record `SRC_BIOINFORMATICS_BASICS` points only to https://www.ncbi.nlm.nih.gov/books/ although the NCBI sequence-analysis chapter provides a more direct locator.
- Biodiversity records 80–82 are structurally linked, but the stored Source URI points to OpenStax §47.4 while the scored review cites §47.1. This mismatch must be reconciled before source-fit acceptance.

## Gate status

- Structural linkage checks for candidates 95–100: PASS.
- Claim-specific EU descriptions for candidates 95–100: NEED IMPROVEMENT.
- Source-fit for agricultural engineering: PARTIAL/WEAK.
- Source-fit for bioinformatics: PARTIAL to GOOD, but stored locators need precision.
- No content JSON changes authorized or made.
- This addendum does not establish global Batch 41 closure or M13 completion.
