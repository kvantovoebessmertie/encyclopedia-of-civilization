# M13 Batch 13 — remediation checkpoint: history-methods evidence and health-resilience link audit

Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **direct history-methods sources identified; health-resilience Evidence Use corrected in a new version with regression coverage; history-methods canonical records remain on HOLD pending pinpoint remediation**

## 1. History-methods Claims 649–650 — source-fit remediation

Current canonical source:
- Record: `SRC-HISTORY_METHODS_BASICS@1`
- Stored identity: “Исторические методы устанавливают и интерпретируют свидетельства о прошлом.”
- Stored URI: https://www.historians.org/teaching-learning/
- Finding: the broad AHA teaching-and-learning landing page does not adequately identify the source-methods material needed for these Claims.

### Candidate replacement/supplement sources

1. American Historical Association, *The Historian’s Toolbox: Source Evaluation Worksheet*:
   https://www.historians.org/resource/the-historians-toolbox-source-evaluation-worksheet/
   The page identifies an explicit source-evaluation workflow and criteria such as authority, author expertise, source context and evaluation. This is a closer match to Claim B than the current broad landing page. It may also support Claim A only when paired with a resource explicitly addressing the use of sources in historical inquiry. Confirm current page contents and record exact sections before changing the canonical source record.

2. Library of Congress, *Getting Started with Primary Sources*:
   https://www.loc.gov/programs/teachers/getting-started-with-primary-sources
   Directly distinguishes primary sources from secondary accounts, describes using sources to ask questions and make evidence-based inferences, and recommends considering creator, historical context, purpose, audience and comparison with other sources. This is a strong fit for Claim A and supports the context/provenance dimensions in Claim B.

3. U.S. National Archives, *Analyze a Written Document*:
   https://www.archives.gov/education/lessons/worksheets/analyze-a-written-document-intermediate
   The worksheet asks who created a document, who received it, when and where it originated, why it was created, what was happening at the time, and what other evidence should be consulted. The page states that materials created by NARA are public domain. Verify reuse scope for any non-NARA material and do not copy more text than necessary.

4. U.S. National Archives, *Record Group Concept*:
   https://www.archives.gov/research/guide-fed-records/index-numeric/concept.html
   Explains archival provenance in terms of attribution to the creating/maintaining agency and original arrangement. This is a focused supplementary source for provenance, but it does not alone support the entirety of Claim A.

### Claim-level mapping and disposition

- `CLM-HISTORY_METHODS_BASICS-A@1`: “Историческое исследование использует источники для реконструкции и интерпретации прошлого.”
  - Best fit: LOC primary-source guide, supplemented by a focused research-methods resource if needed.
  - Why: the guide directly explains source-based inquiry, evidence, inference and comparison across sources.
  - Disposition: **HOLD until a versioned source record and claim-specific Evidence Use pinpoint are recorded.** Avoid asserting that a teaching guide proves every form of historical research.

- `CLM-HISTORY_METHODS_BASICS-B@1`: “Источник имеет происхождение и контекст, которые влияют на его использование как свидетельства.”
  - Best fit: LOC primary-source guide plus NARA provenance explanation; AHA source-evaluation worksheet is a useful complementary source.
  - Why: creator, date, audience, purpose, context and provenance are directly addressed by these resources.
  - Disposition: **HOLD until a versioned source record and claim-specific Evidence Use pinpoint are recorded.** Keep provenance and contextual interpretation distinct; context informs evaluation but does not automatically invalidate a source.

- Claim C was not part of this specific remediation request and remains outside this note’s disposition.

### Source and reuse safeguards

This note records candidate sources, not an approved canonical source change. Before editing canonical data:
- inspect the exact page and select a stable section/heading or worksheet prompt as pinpoint;
- record a versioned Source identity/locator and why that source supports the specific Claim;
- verify the reuse terms for the exact material to be quoted or reproduced;
- retain the original record/version history under the Authoring Contract;
- update tests and re-run schema, semantic, reference, offline and release-gate checks.

## 2. Health resilience row 639 — exact Evidence Use mismatch and duplicate candidate

Canonical records inspected in the current branch:

- Claim: `CLM-M4-HEALTH-RESILIENCE-A@1`, file `CONTENT/vertical-slices/health-systems-basics/records/CLM-M4-HEALTH-RESILIENCE-A.json`.
- Source: `SRC-M4-HEALTH-RESILIENCE-WHO@1`, file `CONTENT/vertical-slices/health-systems-basics/records/SRC-M4-HEALTH-RESILIENCE-WHO.json`.
- Mislinked Evidence Use: `EU-M4-HEALTH-RESILIENCE-WHO@1`, file `CONTENT/vertical-slices/health-systems-basics/records/EU-M4-HEALTH-RESILIENCE-WHO.json`, whose `claim_ref` is `CLM_HEALTH_SYSTEMS_BASICS_C@1`.
- A second Evidence Use already exists: `EU-CLM-M4-HEALTH-RESILIENCE-A@1`, file `CONTENT/vertical-slices/health-systems-basics/records/EU-CLM-M4-HEALTH-RESILIENCE-A.json`, and it correctly references `CLM-M4-HEALTH-RESILIENCE-A@1` and the same WHO source.

### Finding

This is not merely a missing link. There is a correctly linked Evidence Use and a second record with a different ID that references the wrong Claim. The two Evidence Use records also have different descriptions. Automatically repointing the malformed record could leave duplicate evidence records and obscure the history of the correction; deleting it would be equally premature.

### Remediation applied on the M13 branch

1. Inspected the canonical health-systems slice and confirmed that `CLM_HEALTH_SYSTEMS_BASICS_C@1` describes health-system performance interactions, while the material description in `EU-M4-HEALTH-RESILIENCE-WHO@1` describes resilience and continuity planning. The mismatch is substantive, not a cosmetic ID alias.
2. Created `EU-M4-HEALTH-RESILIENCE-WHO@2` by updating the existing canonical file with `record_version: 2` and correcting `claim_ref` to `CLM-M4-HEALTH-RESILIENCE-A@1`. The original version remains recoverable in Git history; no Claim or Source content was rewritten.
3. Added `test_health_resilience_evidence_use_targets_the_resilience_claim` to `REFERENCE/tests/test_content_health_systems_basics_vertical_slice.py`. It asserts the exact Claim/Source references and their record types.
4. A separate Evidence Use `EU-CLM-M4-HEALTH-RESILIENCE-A@1` still exists and may be an additional distinct evidence link. Its material must be given an exact source pinpoint and compared against version 2 before considering any de-duplication; it was not deleted or silently merged.
5. Exact-head Reference Tests, Release Gate and Offline Edition must all pass before this remediation is treated as verified. The source pinpoint remains open.

**Disposition: corrected linkage, publication HOLD remains** until the pinpoint and exact-head checks are complete.

## 3. Batch 13 accounting after this checkpoint

- Initial provisional review coverage: 100/100 candidates.
- Finalized scored-ledger rows from this checkpoint: 0.
- Canonical JSON records changed: 1 versioned Evidence Use correction (`EU-M4-HEALTH-RESILIENCE-WHO@2`); no Claim or Source record changed.
- New release holds retained: health resilience row 639; history-methods rows 649–650.
- Next closure gates: versioned evidence remediation, exact source pinpoints, alias/duplicate and high-consequence checks, Human View, finalized ledger reconciliation, and green exact-HEAD CI.
