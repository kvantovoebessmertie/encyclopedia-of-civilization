# R7 Two-Slice Implementation and Labour Rights Closure Report — 2026-11-19

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Inspection HEAD before this report commit: `1f69ea582a71bb4c25f0668c6bc8d471a70e2820`  
Starting HEAD for this work block: `438eef4f5cae342699373498fab6ece1cc41760a`

## 1. Work completed

### Civil Society Basics — 13 records

All 13 authorized canonical records were re-fetched at v1, then versioned v1→v2 under `REMAINING-R7-SOURCE-REMEDIATION-001`:
- Primary Source now identifies OECD DAC Recommendation OECD/LEGAL/5021.
- Independent Source now identifies the UN DGC Civil Society Unit “About us” page.
- Claims A–C were changed only for `provenance.created_from`; statements and `claim_type` were preserved.
- Three primary and three independent Evidence Use records now carry claim-specific locators, exact Claim/Source v2 references and support boundaries.
- Context and Scope target Claim A@2.
- README and the item-level rights screen were updated.

Validation: 13/13 records v2, published and complete; all six Evidence Use records have non-empty locators and descriptions. No source text, image, layout or expressive material was reproduced. Slice remains HOLD.

### Comparative Civilizations Basics — 9 records

All nine authorized canonical records were re-fetched at v1, then versioned v1→v2 under the same authorization:
- Source now identifies David Smith/AHA, “Introduction to Doing World History” (1998).
- Claims A–C were changed only for provenance alignment; statements and `claim_type` were preserved.
- Evidence Use A–C now carry claim-specific AHA locators and support boundaries.
- EU-C retains one canonical AHA `content.source_ref`; the Singapore MOE 2021 chronology/causation locator is recorded only in schema-supported `provenance.external_sources`.
- Context, Scope and README were updated.

Validation: 9/9 records v2, published and complete; all three Evidence Use records have non-empty locators and descriptions; EU-C has exactly one supplementary MOE reference. No second canonical Source ID or schema change was introduced. No source text, syllabus definitions, tables, images or graphics were reproduced. Slice remains HOLD.

## 2. Exact-version master synchronization

The Part II master was updated for exactly 22 compound keys:
- 13 Civil Society records now reference @2.
- 9 Comparative Civilizations records now reference @2.

Post-update parser result:
- 1,129 rows;
- 1,129 unique compound keys;
- 0 duplicate keys;
- 22 affected rows, all @2;
- 0 remaining @1 rows for either slice;
- all 1,129 decisions remain HOLD.

Declared composition remains 1,058 candidate keys + 71 dependency records = 1,129. No denominator, candidate membership, or slice coverage was expanded.

## 3. Labour Economics — unsafe rights assertion corrected

The active authorization's inaccurate CC BY 4.0 statement for OpenStax *Principles of Economics 3e* was replaced with an explicit unresolved asset/edition-level conflict:
- Current HTML Preface states CC BY-NC-SA 4.0 and a prior-written-permission condition for LLM training/ingestion and generative-AI offerings.
- A separately hosted PDF asset displays CC BY 4.0.
- Neither notice is selected by default.
- The authorization now expressly prohibits OpenStax-dependent Labour canonical changes until the owner records Path A, B or C.

A further check found a similar internal conflict in the official *Principles of Economics 2e* HTML Preface; it is not treated as an automatic workaround.

A BLS-based source alternative was researched and recorded in `reports/agent-work/chief-engineer/r7-labour-economics-rights-compatible-source-options-2026-11-19.md`. BLS public-domain text sources appear promising for text-only factual paraphrase, but their examples are U.S.-specific and do not independently support all general/global Claim wording. ILO page/publication dates and third-party components require item-level review before applying the ILO CC BY 4.0 Open Access policy.

Labour Economics remains 13/13 records v1, aligned and HOLD. No canonical Labour record changed. The owner must choose:
- Path A: written OpenStax clarification/permission for exact asset, AI workflow and intended distribution;
- Path B: approve a rights-compatible replacement graph and a corrected bounded authorization;
- Path C: leave OpenStax unused pending explicit approval of a narrow citation-only workflow.

No path has been selected by this report.

## 4. Files and commit scope

Comparing starting HEAD `438eef4...` to inspection HEAD `1f69ea5...` found 37 commits and 34 changed files:
- 24 `CONTENT/` files: 22 canonical records + 2 READMEs;
- 8 `RELEASE/` files: authorization, queue, exact-version master, owner register, rights screen and three R7 decision/packet documents;
- 2 `reports/` files: exact-version integrity delta and Labour source-option research.

No other vertical slice, Relation, validator, storage, recovery, schema or release-gate semantics was changed. No first-edition allowlist or INCLUDE/EXCLUDE decision changed.

## 5. Branch and CI boundary

At the last pre-report check:
- PR #22: OPEN · DRAFT · NOT MERGED.
- PR head: `1f69ea582a71bb4c25f0668c6bc8d471a70e2820`.
- Base SHA: `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`.
- `main`: `d58289f319993ede5294a46f4741a506fd2fd710`, unchanged.
- Workflow runs associated with that exact HEAD: none returned by the PR-run lookup.

No CI PASS is claimed for this new HEAD. The four required workflows must be rechecked on the final report commit SHA. Historical successes on earlier HEADs are not transferred.

## 6. Remaining owner and release blockers

1. R-01–R-10 project rights, authorship, contributor, editorial accountability, approver and release policy decisions remain open.
2. Civil Society and Comparative Civilizations remain HOLD pending item-level rights review, project licence/distribution decision, independent editorial review and Human View.
3. Labour Economics remains blocked by the OpenStax rights conflict and awaits owner Path A/B/C decision.
4. History of Mathematics Cambridge Source/Claim C branch and Archival Science ICA Source/Claim C branch remain separate authorization/provenance owner blockers.
5. Settlement Geography requires explicit bounded authorization for any canonical source replacement.
6. The two Labour-dependent Relations remain unchanged until Labour Claim C@2 is validly authorized and established.

## 7. Acceptance boundary

This work closes the bounded source/locator remediation for Civil Society and Comparative Civilizations and synchronizes their exact-version master keys. It does **not** close legal rights, factual truth, independent editorial review, Human View, release approval or first-edition eligibility. All affected slices remain HOLD.
