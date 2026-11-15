# M13 — Package 32 and multi-EU exact-ID cross-audit

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed branch HEAD before this checkpoint: `286ffab5d8e86dc701d3b7e770657b631bc02dee`  
State: **artifact-level reconciliation and normalized sidecar; no canonical writes, no D/E/B changes**

## 1. Exact artifact inputs

- Generic Evidence Use coverage workflow run: `43748097686`, artifact: `14174823129`, source revision: `8cf14e5045f7451ff577b33590f42a582f5f8bcd`.
- Package 32 Audit Queue workflow run: `43748097802`, artifact: `14175530692`, source revision: `8cf14e5045f7451ff577b33590f42a582f5f8bcd`.
- Downloaded ZIP digests:
  - Generic-EU coverage: `sha256:c6b9a522e24d6d94f83a792cdf1011ae9c854df08e09cea84c6e995690ea8c36`.
  - Package 32 queue: `sha256:73ea3a03fa40cd86e0062b10dfa4f978b1b424f0db8e7c98447666fe39ba9cd6`.

## 2. Independent exact-ID set comparison

The downloaded coverage JSON contains 496 candidate rows, 496 unique Claim IDs and 496 unique Evidence Use IDs. The Package 32 evidence-packet JSON contains 41 packets and 41 unique Claim IDs.

Exact set intersection:
- Generic-EU candidate Claim IDs ∩ Package 32 selected Claim IDs = **0**.
- Generic-EU candidate Claim IDs = 496.
- Package 32 selected Claim IDs = 41.
- Duplicate IDs within either population = 0.

This independently reproduces the zero-overlap statement in the current queue checkpoint. It is an ID-set result only; it does not imply semantic review completion or release clearance.

## 3. Seven multi-Evidence-Use Claims — normalized linkage

The 14-row sidecar `M13-MULTI-EU-7-CLAIMS-NORMALIZED-SOURCE-LINKAGE-2026-11-15.csv` normalizes the exact Claim → EU → Source mapping from the reviewed multi-EU report into one row per Evidence Use. This avoids ambiguity from a singular primary-source field and preserves the independent disposition for each row.

Counts: 7 Claims; 14 Evidence Use rows; 14 Source IDs; 14 registered source URIs. The sidecar is a transcription of the reviewed report's exact mapping, not a fresh source-passage adjudication. Its rights, scope and independence notes remain separate; no source is accepted by inclusion in this file.

## 4. Important scope limitation

The 496-row generic-EU coverage artifact is a candidate set in which each row maps one EU to a Claim. The seven-Claim multi-EU audit is a separate crosswalk. The coverage artifact alone is not sufficient to reconstruct all secondary EU links for those seven Claims. Use the normalized 14-row sidecar for that purpose; do not infer missing secondary links from the generic-EU candidate rows.

The current 356-row companion ledger mentioned in the checkpoint was not present in the branch tree at this reviewed HEAD, so this audit does not claim to have verified its CSV schema or its claimed correction. The normalized sidecar is committed separately to make the 14 exact links available in-repository.

## 5. Guardrails and next actions

- No canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON changed.
- No D/E/B values or risk metadata changed.
- No rights hold was cleared.
- No Claim was accepted or release-cleared.
- PR #21 remains Draft/unmerged; `main` is unchanged.

Next: reconcile the external/current 356-row companion ledger against the normalized 14-row sidecar, then continue proposal-only remediation by exact Claim/EU/Source versions, passage locators, rights and source-lineage checks. Canonical changes require separate bounded authorization.
