# Package A — implementation-readiness QA

Date: 2026-11-21  
Status: **NONCANONICAL RESEARCH / QA ONLY**  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Reviewed proposal HEAD: `9f7ea1c6ef9f93665a5773229474e5fc11850c1b`

## 1. Authorization boundary

This review is within the owner's existing research-only authorization for Package A alternative sources and rights. It does not authorize canonical Source/Evidence Use versions, new Source IDs, Claim changes, status changes, register changes, allowlist changes, publication, merge, or changes to `main`.

All 11 Ancient Civilizations slice records remain HOLD. Existing canonical versions remain unchanged.

## 2. Proposal file re-review

Reviewed:

- `RELEASE/FIRST-EDITION-PACKAGE-A-PROPOSED-EVIDENCE-USE-AND-SOURCE-IMPLEMENTATION-PACKET-2026-11-21.md`
- `IMPLEMENTATION/005-RECORD-SCHEMA.json`
- `STANDARD/001-RECORD.md`
- `STANDARD/003-SOURCE.md`
- `STANDARD/004-EVIDENCE-USE.md`
- `REFERENCE/tests/test_content_ancient_civilizations_basics_vertical_slice.py`
- `CONTENT/vertical-slices/ancient-civilizations-basics/README.md`
- `.github/workflows/reference-tests.yml`
- `.github/workflows/release-gate.yml`

### 2.1 Schema shape

The three proposed Evidence Use payloads use the current schema's allowed core fields:

- top-level Record fields are present;
- `record_version` and references are strings;
- `record_type=evidence_use`;
- `claim_ref`, `source_ref`, `evidence_role`, and `material` are present;
- `evidence_role=supports` is within the current enum;
- `material` uses the supported `locator` and `description` fields;
- no unsupported rights/author/URL fields are placed inside `material`.

The proposed Source payload uses the current Source profile's supported fields and keeps rights/attribution outside the canonical Source payload, consistent with the present schema.

This is a structural review of the draft payloads, not an executed JSON Schema validator run. No CI or test pass is claimed.

### 2.2 Exact OpenStax locator correction

The proposal initially named a non-existent subsection, “Neolithic Peoples,” in §2.3. The proposal was corrected in commit `9f7ea1c6ef9f93665a5773229474e5fc11850c1b`:

- correct section: §2.3 “The Neolithic Revolution”;
- subsection: “The Development of Agriculture”;
- subsection: “How Farming Changed the Human Experience”;
- separate §2 Section Summary locator added.

The corrected description now distinguishes the textbook's broad account of independent agricultural origins and variable adoption from comparative demographic measurement. It does not overstate this textbook section as a causal or quantitative demographic study.

Verified section URLs:

- §3.1: https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations
- §3 Section Summary: https://openstax.org/books/world-history-volume-1/pages/3-section-summary
- §2.3: https://openstax.org/books/world-history-volume-1/pages/2-3-the-neolithic-revolution
- §2 Section Summary: https://openstax.org/books/world-history-volume-1/pages/2-section-summary
- §1.2: https://openstax.org/books/world-history-volume-1/pages/1-2-primary-sources

### 2.3 Claim-specific support limits

**Claim A:** §3.1 and the §3 Section Summary explicitly cover settled populations, urban concentration, surplus, specialization and social stratification. The textbook is an introductory synthesis. Case studies such as Lagash may illustrate a specific trajectory but cannot establish a universal template for all early civilizations.

**Claim B:** §2.3 supports different regional origins and patterns of adoption, continued foraging in some populations, and agricultural capacity to sustain larger populations and surpluses. It is not a comparative demographic dataset and does not establish a single direction or causal mechanism. The independent studies in the evidence map are necessary for the claim's temporal/regional demographic qualification.

**Claim C:** §1.2 identifies documentary/textual and non-textual materials, including artifacts and works of art, but explicitly privileges written evidence in a broad generalization. Any Evidence Use based on this section must be narrow and must not import that hierarchy. Hawkes et al. (2022) is a better independent case-specific example of combining documentary and archaeological evidence. It does not establish that all ancient societies left written sources.

## 3. Source identity continuity — unresolved before canonical versioning

The existing logical Source ID `SRC-ANCIENT_CIVILIZATIONS_BASICS@1` has:

- generic `source_identity`: “Authoritative reference source for ancient-civilizations-basics”;
- representation: “official/public reference”;
- external URI: OpenStax §3.1.

The proposed @2 resolves that generic description to the 2023 OpenStax textbook edition. This is plausible as a metadata clarification because @1 already points to the OpenStax §3.1 page, but the project must not silently assume that a generic placeholder and a specific textbook identity are the same referent.

Before a canonical write, the owner/editor must decide one of these identity treatments:

1. **Continuity confirmed:** the existing Source ID always represented this OpenStax textbook; @2 is a clarification of the same source identity and preserves the history of the earlier underspecified description.
2. **Continuity not confirmed:** the existing Source ID is only a generic placeholder or another logical object; create a new, distinct Source ID for the 2023 OpenStax textbook and point new Evidence Use versions to it, preserving the old Source and its historical links.

No automated choice is made here. This is a genuine identity decision under the Source standard, not just a URL correction.

## 4. Slice-test and release-gate implications

The existing slice test `REFERENCE/tests/test_content_ancient_civilizations_basics_vertical_slice.py` asserts:

- exactly 11 canonical records;
- 2 Source records;
- 3 Claim records;
- 4 Evidence Use records;
- 1 Context and 1 Scope;
- every Claim and Evidence Use resolves to a Source and each Evidence Use resolves to a Claim.

Therefore:

- the proposed minimal version-only pass (one Source version plus three Evidence Use versions, without creating additional logical records) should preserve the record counts;
- any selected independent corroboration Source/Evidence Use additions would change the canonical record count and require separately authorized updates to the slice test, content coverage/accounting and any affected manifests;
- adding a new Source ID instead of versioning the current one still changes the logical record count and therefore needs corresponding test/coverage work;
- the current README's source description also remains stale/oversimplified (“Smithsonian research”) if the Smithsonian link is retired from affirmative support. A later authorized implementation must decide whether and how to update it; this research-only pass does not.

The reference-tests workflow runs on PR changes to `REFERENCE/**`, `IMPLEMENTATION/005-RECORD-SCHEMA.json`, `CONTENT/**`, `ROADMAP.md`, and `RELEASE/CONTENT-COVERAGE.json`. The release-gate workflow includes `RELEASE/**` changes on pull requests. These workflow definitions do not establish that a run occurred or passed.

## 5. Rights gate

OpenStax's current *World History Volume 1, to 1500* page identifies the 2023 edition and states CC BY-NC-SA 4.0, including attribution, NonCommercial and ShareAlike conditions. It also states that the book may not be used for LLM/generative-AI ingestion without prior written permission. The project must not treat “free to read” or the CC licence as permission for commercial reuse or AI ingestion.

Official references:

- Book preface/licence and reuse notice: https://openstax.org/books/world-history-volume-1/pages/preface
- OpenStax licence guidance: https://help.openstax.org/s/article/Licensing-information-of-OpenStax-textbooks

The proposal's conservative use boundary (bibliographic identification, citation/link and independently authored factual summaries only; no copying, translation, figures, maps, tables, images, bulk extraction or AI ingestion) should remain in place pending the project-owner's distribution/licence decision and any needed permission.

The separate CC BY 4.0 research articles remain item-level candidates, not a blanket clearance of their third-party images, figures, tables or datasets.

## 6. Implementation blockers remaining

Before a separate canonical authorization is requested, resolve:

1. Source identity continuity decision in §3.
2. Whether Claim C's current Evidence Use should remain linked to OpenStax §1.2 with a strict anti-hierarchy limitation, or be supported by a distinct source set led by Hawkes et al. (2022).
3. Whether the minimal first implementation should leave the Smithsonian EU @1 untouched as historical evidence and add no replacement EU, or create a separately identified Zeder article Source/EU after article review. The conservative recommendation is to preserve @1 and not create a Zeder EU in the minimal pass.
4. Whether the project wants any independent CC BY corroboration sources in the same implementation pass. The current slice test requires a separate test/coverage change if new logical records are added; this is not covered by the existing minimal proposal.
5. Owner/editor confirmation that the OpenStax rights conditions are compatible with the intended use. No project licence or legal clearance is inferred.

## 7. Recommended next bounded sequence

1. Complete the owner/editor identity and evidence-source decisions above.
2. If the owner chooses the minimal path, request separate exact authorization for the Source identity operation and three Evidence Use version operations only.
3. Execute only the approved operations on the PR branch; keep Claims, Context, Scope, Relations, master register, denominator, allowlist and all HOLD states unchanged.
4. Re-fetch every affected record and validate schema, reference graph, exact version links and slice tests at the resulting immutable HEAD.
5. Run the relevant PR workflows on that exact HEAD and report each observed result independently.
6. Keep WP2 owner decisions and first-edition inclusion decisions separate from technical remediation.

No canonical record, test, README, coverage file, workflow, allowlist, release artifact, or main-branch file was modified by this QA review.
