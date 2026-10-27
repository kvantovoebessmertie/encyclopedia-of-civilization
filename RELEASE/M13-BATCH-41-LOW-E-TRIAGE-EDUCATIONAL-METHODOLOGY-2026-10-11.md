# M13 Batch 41 — Low Evidence-Fit Triage: Editorial and Methodological Claims
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: triage only; no content JSON changed.

## Scope

This note deepens the first pass on the ten Batch 41 Claims scored E=0 in the six provisional score reports. Each Claim JSON, its Evidence Use JSON, and the linked Source JSON were fetched from the audit branch. The score reports' low-E rationale was compared with the actual stored Claim type, statement, Evidence Use description, and Source identity/URI.

The result is a classification of likely remediation type, **not** authorization to rewrite records or a final independent re-score.

## Findings

| Candidate | Claim ID | Stored type and substance | Current linked source / Evidence Use | Triage disposition |
|---:|---|---|---|---|
| 32 | `CLM-ANTHROPOLOGY_BASICS-A` | `documented_fact`; describes the purpose/design of this project slice | American Anthropological Association overview; generic EU description | Project-design/editorial metadata, not an externally documented fact about anthropology. Move to an appropriate editorial/design layer or support it with the project's own learning-design specification. |
| 33 | `CLM-ANTHROPOLOGY_BASICS-B` | `documented_fact`; general rule that interpretation depends on source, context, and applicability limits | AAA anthropology overview; generic EU description | General epistemic/editorial guidance. Current source does not establish this as an anthropology-specific fact. Move to shared methodology guidance or use an appropriate methodology source. |
| 34 | `CLM-ANTHROPOLOGY_BASICS-C` | `documented_fact`; general rule that basic knowledge does not replace specialist checking | AAA anthropology overview; generic EU description | General editorial/safety boundary, not anthropology-specific evidence. Move to shared guidance or cite an appropriate professional/methodological authority. |
| 42 | `CLM-ARCHITECTURE_BASICS-B` | `documented_fact`; general rule to account for source, context, and applicability limits | Britannica architecture overview; generic EU description | General epistemic/editorial guidance. Architecture source is a domain mismatch for this rule. |
| 43 | `CLM-ARCHITECTURE_BASICS-C` | `documented_fact`; general warning that general information cannot replace specialist verification | Britannica architecture overview; generic EU description | General professional-boundary guidance, not an architecture-specific fact. Move to shared guidance or cite a suitable methodological/professional authority. |
| 45 | `CLM-ARCHIVAL_DESCRIPTION_BASICS-B` | `documented_fact`; distinguishes records-management information from non-record materials and consistent organizational handling | Society of American Archivists' *Describing Archives: A Content Standard*; EU description names DACS | **Substantive source-scope mismatch.** DACS is an archival-description standard, not the right primary authority for the full records-management proposition. Find an authoritative records-management source or narrow the Claim to what DACS actually governs. |
| 76 | `CLM-BEHAVIORAL_BIOLOGY_BASICS-C` | `documented_fact`; methodological rule to describe observable conditions rather than attribute untestable motives | OpenStax Biology 2e introduction; generic EU description | Methodological/ethology guidance rather than a claim established by the linked introductory source. Find a direct source on operationalization/ethological inference or move the rule to shared methodology guidance. |
| 80 | `CLM-BIOCHEMISTRY_BASICS-A` | `documented_fact`; describes the purpose/design of this project slice | OpenStax Biology 2e metabolism introduction; generic EU description | Project-design/editorial metadata, not an externally documented biochemistry fact. Support it with project learning-design documentation or move it out of the domain Claim set. |
| 81 | `CLM-BIOCHEMISTRY_BASICS-B` | `documented_fact`; general rule that interpretation depends on source, context, and applicability limits | OpenStax Biology 2e metabolism introduction; generic EU description | General epistemic/editorial guidance. The metabolism source does not establish this general rule. |
| 82 | `CLM-BIOCHEMISTRY_BASICS-C` | `documented_fact`; general rule that basic knowledge does not replace specialist checking | OpenStax Biology 2e metabolism introduction; generic EU description | General professional-boundary guidance, not a biochemistry-specific fact. |

## Cross-cutting result

- All ten records use `claim_type: documented_fact`.
- Nine of ten are primarily editorial/design or general methodology/boundary propositions, not ordinary domain facts directly established by their linked subject-matter Source.
- One (`CLM-ARCHIVAL_DESCRIPTION_BASICS-B`) is a domain claim whose current Source appears out of scope; it needs a better records-management authority or a narrower proposition.
- The corresponding Evidence Use descriptions are generic or near-generic and do not name a specific supporting passage.
- These issues do **not** establish that the propositions are false. They establish that the current claim type/source/evidence mapping is not adequate for the proposition as written.
- This classification overlaps the score reports' D/E/B judgements and must not be added as ten extra Claims or ten extra defects without deduplication in the consolidated ledger.

## Authorized-correction queue (not performed)

1. Decide at the project-model level how slice-purpose statements and cross-domain epistemic safeguards should be represented: shared editorial guidance, learning-design metadata, or sourced domain Claims.
2. For `CLM-ARCHIVAL_DESCRIPTION_BASICS-B`, locate a direct records-management authority or narrow the wording to archival description.
3. For `CLM-BEHAVIORAL_BIOLOGY_BASICS-C`, locate a direct ethology/methodology authority if it is to remain a factual Claim.
4. Replace generic EU descriptions with claim-specific descriptions and section/paragraph locators after selecting the correct source.
5. Re-score E only after the actual supporting passages and the record-type decision are settled.

No Claim, Evidence Use, Source, or Relation JSON was changed. Keep `main` unchanged, PR #21 open Draft/unmerged, and M13 open.
