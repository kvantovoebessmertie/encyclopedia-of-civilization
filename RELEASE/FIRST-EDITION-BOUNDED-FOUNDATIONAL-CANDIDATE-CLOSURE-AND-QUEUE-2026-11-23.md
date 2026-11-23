# First Edition — Bounded Foundational Candidate Closure and Next Release Queue

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Inspection HEAD: `e6dfacda3ba579a3a9f8bfb5ebad03dfdf2c795a`

## 1. Purpose and limits

This package advances the first-edition candidate work using the existing record-level register and prior source research. It prioritizes bounded, explanatory, low-consequence foundational material that can add genuine breadth after the Survival opening. It does not restart M13, repeat closed Human View audits, change canonical records, assign INCLUDE/HOLD/EXCLUDE, create a release allowlist, or authorize publication.

The inspection is a targeted read-only re-fetch of exact canonical JSON. It is not a complete audit of the three vertical slices or of the whole Part II corpus.

## 2. Candidate A — SI units: strongest existing private-review candidate

### Exact seven-record closure re-fetched

| Record | Exact version | Type | Current canonical blob SHA |
|---|---:|---|---|
| CLM-SI-SEVEN-BASE | 1 | Claim | `b65880065710de3f09754488cd92cc11c47a1da8` |
| EU-SI-SEVEN-BASE | 2 | Evidence Use | `5ad6170e97c46596727bebd1ac06572533e9e199` |
| CLM-SI-DERIVED | 1 | Claim | `37ba5acfe4973a6b36cf521969bf58f554d07740` |
| EU-SI-DERIVED | 2 | Evidence Use | `35dff2eb3dc3257a34ce7f74d641ebf5283016d2` |
| SRC-NIST-SI-UNITS | 1 | Source | `4ed0464af9083027d97d99ec997fd25df49c2ebb` |
| CTX-SI | 1 | Context | `12e7b6bbd983c8e24d99ad91264a061a9d3e76a1` |
| SCP-SI | 1 | Scope | `6b505b738b6ad4a11fec9ad7c16bbcc941227ced` |

### Exact record-level findings

- Both Claims are Russian-language, factual, explanatory statements about SI structure; they are not operational safety instructions.
- Both Evidence Use records are v2 and point to the exact Claim v1 and NIST Source v1.
- EU for the seven base units pins NIST sections “Defining Constants” and “Base and Derived Units” and explicitly prevents conflating seven base units with seven defining constants.
- EU for derived units pins “Base and Derived Units” and explicitly limits “22” to derived units with special names and symbols, not all possible derived units.
- Source identity and URI are consistent: NIST, “SI Units”.
- The exact Context and Scope both target Claim A only. Their provenance mentions Claim B, but that does not change target applicability. A reader must not display them as governing Claim B.
- No missing edge was found within the seven-record preview closure: Claim A → EU A → Source; Claim B → EU B → Source; Context/Scope → Claim A.

### Existing authorized implementation reused

The existing bounded authorization `MVP-SI-PRIVATE-REVIEW-PREVIEW-001` permits only a private, non-release, seven-record preview. Existing implementation files were re-fetched:

- `REFERENCE/build_si_units_private_review_preview.py` — exact seven-ID/version set, Claim/EU/Source links, Claim-A-only Context/Scope, NIST section names, “22” qualification and source URI are enforced.
- `REFERENCE/src/encyclopedia_reference/public_reader.py` — shared preview renderer; explicitly preview-only.
- `REFERENCE/tests/browser_inspect_si_units_private_preview.cjs` — desktop/mobile browser inspection, seven-record-only rendering, exclusion of the third Claim, search, keyboard order, visible focus, mobile overflow, no external requests and no runtime errors.
- `.github/workflows/mvp-si-private-review-preview.yml` — PR-only private preview workflow; uploaded artifact retention is 14 days.
- `RELEASE/MVP-SI-UNITS-PRIVATE-REVIEW-PREVIEW-AUTHORIZATION-2026-11-13.md` — exact authorization and exclusions.

This is the most mature candidate for the next *private release-candidate engineering step*. It is not a public release candidate: the artifact is expressly non-redistributable, and the preview authorization forbids public allowlist changes, hosting, distribution, merging and changes to canonical records.

### Remaining blockers for SI

1. The project-level owner decisions R-01–R-10 remain open; no project licence, rights holder, editor, release approver or public correction contact exists in the approved record.
2. The actual private preview must be built and inspected on the exact intended immutable PR revision, and its artifact/hash/report retained. Prior test design is not a substitute for a current run.
3. The three-reader independent non-specialist protocol is explicitly NOT RUN.
4. Release-facing editorial sign-off is absent.
5. The Context/Scope display boundary must remain Claim-A-only in the reader.

**Disposition remains HOLD.** No canonical file or decision field was changed.

## 3. Candidate B — Climate basics: bounded single-Claim explanatory candidate

### Exact five-record subgraph re-fetched

| Record | Exact version | Type | Current canonical blob SHA |
|---|---:|---|---|
| CLM-CLIMATE_BASICS-A | 1 | Claim | `83e86389e2c7e122ddce0b1e9d066c15147c9cec` |
| EU-CLIMATE_BASICS-A | 1 | Evidence Use | `7356d5b6c7c2c49f0fa119f60726135229d9033e` |
| SRC-CLIMATE_BASICS | 1 | Source | `a5bee4f54821f6e4163d917a9a85d9848118f065` |
| CTX-CLIMATE_BASICS | 1 | Context | `224e05a1b35b3bfc94545069685076b93e69fb2a` |
| SCP-CLIMATE_BASICS | 1 | Scope | `11e44bf4c54c433c5083a198bc213231e8e644a9` |

### Findings

- Claim A states that climate describes long-term characteristics and changes in weather patterns in the Earth system.
- The current EU is generic; it does not yet identify the inspected NASA passage.
- The Source currently points to the broad NASA Climate Change portal.
- Prior exact-source research identifies two better pinpoint pages: NASA “What’s the difference between weather and climate?” and NASA “What Is Climate Change?”. Together they support the long-term-average and long-term-change components, with the important boundary that the Claim does not explain every Earth-system component or causal mechanism.
- Context and Scope both target Claim A only. Context correctly prevents inference from one short-term weather event; Scope limits the slice to basic education rather than a full local climate analysis.
- No NASA image, logo, visualization or third-party credited asset is needed for a factual paraphrase. Asset reuse must remain a separate rights check.

### Remaining blockers

1. The canonical EU remains v1 with generic description; a pinpointed EU correction requires a separate bounded authorization and versioned record.
2. The Source identity/URI should be reviewed against the selected precise NASA locator(s); do not silently change canonical Source metadata.
3. Record the exact NASA asset/attribution boundary for the proposed text-only use.
4. Run exact-version dependency validation and reader Human View on the eventual versioned candidate.
5. Project-level R-01–R-10 decisions remain open.

**Disposition remains HOLD.** This package did not change the Claim, EU, Source, Context or Scope.

## 4. Candidate C — Measurement uncertainty: technically promising, but legacy-source qualification required

### Exact five-record Claim-A subgraph re-fetched

| Record | Exact version | Type | Current canonical blob SHA |
|---|---:|---|---|
| CLM-MEASUREMENT_UNCERTAINTY_BASICS-A | 1 | Claim | `c352d4f41e4a64cfc8747926c5a74bc3cfa8e93f` |
| EU-MEASUREMENT_UNCERTAINTY_BASICS-A | 1 | Evidence Use | `34d962fe7a0f96163cc81e9f3e8a30fed273e0c5` |
| SRC-MEASUREMENT_UNCERTAINTY_BASICS | 1 | Source | `f167d0df955e8ec99a26f64fca9a5a4df49164fd` |
| CTX-MEASUREMENT_UNCERTAINTY_BASICS | 1 | Context | `fdfefe7f5632413306291f947e4ff72049fa1bcd` |
| SCP-MEASUREMENT_UNCERTAINTY_BASICS | 1 | Scope | `9a38ab3081c7b124a488be68f3d8750b38166806` |

### Findings

- Claim A states that a measurement result should be interpreted together with an assessment of its uncertainty.
- The current EU is generic and does not record a pinpoint.
- The existing source points to NIST Technical Note 1297.
- Prior source research identifies NIST TN 1297 §2.1 as directly relevant and §7.1–7.2 as reporting guidance. The existing review also records that the §7 page says it is no longer being updated and may be out of date.
- The current NIST Measurement Uncertainty topic page was identified as corroboration; it must be included in a currentness review rather than treating the legacy TN 1297 material as the sole current authority.
- Context and Scope both target Claim A; no target mismatch was found in this five-record subgraph.
- This is a metrology concept, not an operational safety instruction, but careless wording could conflate uncertainty with error or imply one universal uncertainty model.

### Remaining blockers

1. Versioned EU locator correction is needed; do not alter the canonical v1 record in place.
2. Confirm current NIST guidance and distinguish the legacy TN 1297 reporting material from maintained explanatory guidance.
3. Inspect the full slice before selection: the candidate register records additional Claims and a BIPM VIM Evidence Use/Source track. This five-record read does not certify the complete slice or authorize dropping dependencies.
4. Reader review must distinguish uncertainty from error and preserve the limits of the source.
5. Project-level rights/editorial decisions remain open.

**Disposition remains HOLD.** No canonical record changed.

## 5. Ordered next-candidate queue

This order is based on boundedness, source-pinpoint maturity, current exact-record topology and consequence level—not on an inferred publication decision.

| Order | Candidate | Current review state | Next useful action | Why this order |
|---:|---|---|---|---|
| 1 | SI units — two Claims / seven records | HOLD; private-preview authorization exists | Build and inspect the exact private preview on the current immutable PR revision; retain artifact evidence; close Claim-A-only Context/Scope display test; obtain independent reader protocol | Strongest exact closure, versioned pinpoints, existing dedicated builder and browser suite |
| 2 | Climate basics — Claim A / five records re-fetched | HOLD | Prepare a narrowly scoped, versioned EU/Source remediation proposal and request bounded authorization; do not change canonical JSON before approval | Low-consequence explanatory content, direct NASA locators already identified, explicit Context/Scope |
| 3 | Measurement uncertainty — Claim A / five records re-fetched | HOLD | Prepare a versioned EU/Source remediation proposal with legacy/current NIST distinction; inspect remaining slice records before proposing any exact selection | Strong metrology source fit, but currentness and wider dependency track require care |
| 4 | Statistics basics — Claim A | HOLD | Retain as a later candidate; reconcile NIST locator and OpenStax secondary dependency/rights before proposing a bounded selection | Good breadth and multiple sources, but secondary-source rights/attribution and EU pinpoints add complexity |
| 5 | Motion basics / Cell basics | HOLD | Do not advance ahead of the three above until exact locators and source terms are reviewed | Current Evidence Use is generic and exact dependency closure is incomplete |
| Deferred | Water-treatment, emergency water, fire, electrical, structural, chemical and sanitation procedures | HOLD / high consequence | Keep outside fast-track; require exact passage review, applicability boundaries and qualified specialist approval | Risk of harmful use; cannot be treated as low-risk breadth |

## 6. Cross-cutting release constraints

- The candidate register still records no public INCLUDE.
- Part I's 112-record early manifest remains 0 INCLUDE / 112 HOLD; the wider 980-record Part I screen does not confer admission.
- Part II's consolidated exact-version register remains a candidate/dependency inventory, not an allowlist; its rows remain HOLD.
- R-01–R-10 remain open.
- The selection-aware schema-1.1 builder is fail-closed, but no production INCLUDE manifest is supplied.
- The SI preview is private and non-redistributable by design. It must never be relabelled as the first edition.
- Do not turn this queue into a public allowlist by copying candidate records. Each exact selection requires the complete gates and owner approvals.

## 7. Change-control and verification

- Re-fetched exact canonical records from branch `mvp-public-contribution-design-2026-10-11` at inspection HEAD `e6dfacda3ba579a3a9f8bfb5ebad03dfdf2c795a`.
- Only the listed exact record blobs were inspected for the bounded candidate subgraphs; no canonical files were written.
- No Claim, Evidence Use, Source, Context, Scope, Relation, Assessment, Inference, Decision, publication status, disposition or allowlist was changed.
- No merge, deployment, public release, or main-branch update was performed.
- This report is a read-only audit and execution-queue artifact, not a release approval.


## 8. Remediation proposal package — climate and measurement uncertainty — 2026-11-23

Two source-backed, versioned remediation proposals have now been prepared on this branch. Both are proposal-only; neither authorizes or performs canonical writes.

### Candidate B — Climate basics / Claim A

- Proposal: `RELEASE/CLIMATE-BASICS-CLAIM-A-VERSIONED-EVIDENCE-REMEDIATION-PROPOSAL-2026-11-23.md`
- Exact five-record baseline re-fetched by blob SHA.
- Inspected NASA’s official “What’s the difference between weather and climate?” and “What Is Climate Change?” pages.
- The proposal distinguishes direct support for long-term averages from direct support for long-term changes in average weather patterns.
- It flags that “Earth system” may be broader than the narrowly inspected definition pages and forbids silently widening the evidence claim.
- It preserves Claim A v1, Context v1 and Scope v1; no canonical changes.
- Preferred bounded path is a schema-checked, versioned EU/Source correction. The current EU schema has a singular `source_ref`; no unsupported multi-source field is proposed.
- Disposition: HOLD. Separate owner authorization is required before canonical writes.

### Candidate C — Measurement uncertainty / Claim A

- Proposal: `RELEASE/MEASUREMENT-UNCERTAINTY-CLAIM-A-VERSIONED-EVIDENCE-REMEDIATION-PROPOSAL-2026-11-23.md`
- Exact five-record Claim-A subgraph re-fetched by blob SHA.
- Inspected NIST TN 1297 §2.1, the maintained NIST Measurement Uncertainty topic page, NIST TN 1900 and TN 1297 terminology/reporting sections.
- NIST TN 1297 §2.1 directly supports the proposition that a measurement result is complete only with a quantitative uncertainty statement.
- TN 1900 is described by NIST as supplementing, not replacing, TN 1297; the proposal therefore avoids the unsupported label “obsolete”.
- Explicitly preserves the distinction between uncertainty and error and warns against assuming universal confidence levels or methods.
- The wider slice’s BIPM/VIM dependency track remains unreviewed by this Claim-A proposal and cannot be dropped.
- Disposition: HOLD. Separate owner authorization is required before canonical writes.

### Change and verification boundary

- Both proposals are documentation-only files.
- No canonical Claim, Evidence Use, Source, Context, Scope, Relation, Assessment, Inference or Decision changed.
- No candidate membership, denominator, coverage manifest, allowlist or release state changed.
- No CI workflow was returned for the documentation-only head; no CI PASS is claimed for this new HEAD.
- PR #22 remains OPEN / DRAFT / NOT MERGED. No merge, deployment, public distribution or main-branch update occurred.

### Next bounded sequence

1. Continue the already-authorized SI private-preview engineering path and obtain an actual artifact/test result only if the dedicated workflow can be run on the intended exact revision.
2. Resolve schema/versioning questions for Climate and Measurement Uncertainty before requesting narrowly scoped owner authorizations.
3. For Measurement Uncertainty, inspect the full slice and BIPM/VIM dependencies before any selection proposal.
4. Keep all three candidates HOLD until independent editorial/rights gates and explicit owner decisions are complete.


## 9. Three additional foundational slices screened — 2026-11-23

A further read-only evidence and semantic audit is complete:
`RELEASE/FOUNDATIONAL-SCIENCES-MOTION-CELLS-STATISTICS-BOUNDED-EVIDENCE-AUDIT-2026-11-23.md`.

### Motion basics — 9/9 canonical records re-fetched

- OpenStax Physics §§2.1, 2.2 and 2.4 provide direct, section-level support for reference frames, average speed/velocity and acceleration.
- Source is CC BY 4.0, unlike Biology 2e and some other OpenStax titles.
- Critical semantic defect identified in Claim B: its formula/description is displacement divided by time, which is average velocity, not scalar average speed. A bounded editor decision is required; no Claim rewrite was made.
- Claim C should explicitly mean change in the velocity vector; acceleration can arise from a direction change even at constant speed.
- All three EUs are generic and need pinpoints. Context/Scope target Claim A only.
- All remain HOLD.

### Cell basics — 9/9 canonical records re-fetched

- OpenStax Biology 2e §§4.1–4.3 directly support the three basic propositions: cell as basic unit of life, prokaryotic/eukaryotic nuclear distinction, and differentiated functions of cellular structures.
- Current Source points only to the chapter introduction; EU records need exact section pinpoints.
- Biology 2e is CC BY-NC-SA 4.0, including noncommercial and ShareAlike conditions and a separate restriction on LLM training/ingestion. Rights compatibility with the planned distribution model remains unresolved.
- Claim C is broad and may add limited informational value; editorial review required.
- Context/Scope target Claim A only; no automatic propagation to Claims B/C.
- All remain HOLD.

### Statistics basics — 11/11 canonical records re-fetched

- NIST/SEMATECH Handbook sections support variability, assumptions/data collection and experimental design.
- OpenStax Introductory Statistics 2e independently supports the basic definition in Claim A.
- Three primary EUs are generic; the additional OpenStax EU targets Claim A only.
- Need exact section pinpoints, method-specific boundaries, and separate NIST/OpenStax rights checks. Do not transfer the Physics CC BY licence to the Statistics textbook.
- All remain HOLD.

### Combined change boundary

- One 331-line read-only audit report was added to this PR branch.
- No canonical JSON, Claim, EU, Source, Context, Scope, Relation, assessment, inference, decision, candidate status, denominator, coverage manifest or allowlist changed.
- No exact-head CI PASS is claimed; the documentation-only commit did not return workflow runs.
- PR #22 remains OPEN / DRAFT / NOT MERGED.

### Queue refinement

1. SI private preview — only under the existing seven-record private authorization.
2. **Motion — bounded terminology/evidence package completed:** all 9 records re-fetched; exact §2.1/§2.2/§2.4 locators verified; Claim B ambiguity isolated into two mutually exclusive editorial options; Claim C vector boundary clarified; OpenStax Physics CC BY 4.0 source-specific rights noted. See `RELEASE/MOTION-BASICS-CLAIM-B-TERMINOLOGY-AND-THREE-CLAIM-EVIDENCE-REMEDIATION-PACKET-2026-11-23.md`. No canonical writes; Claim B editorial choice still open; all records HOLD.
3. Cell — prepare EU pinpoint corrections and explicit Biology 2e rights decision.
4. Statistics — prepare NIST/OpenStax locator and rights corrections.
5. Climate and Measurement Uncertainty — retain the two proposals already completed; do not begin canonical writes without bounded authorization.

No candidate is promoted to INCLUDE by this audit.


## 6. Cell basics and Statistics basics — combined rights and record-level recheck

A further bounded package re-fetched all nine Cell Basics records and all eleven Statistics Basics records at the current inspection line and checked the claim/EU/source relationships and source-rights blockers:

- `RELEASE/CELL-AND-STATISTICS-BASICS-SOURCE-RIGHTS-AND-RECORD-LEVEL-RECHECK-2026-11-23.md`
- Commit: `f188df37f43b4f9a108446a8d537532cfe41552e`

### Cell basics — 9 records / 3 Claims

- Claim A is close to OpenStax Biology 2e §4.1, but “structural and functional” is broader than the exact passage currently pinned.
- Claim B is directly supported in concept by §§4.2–4.3; current EU is not section-pinned.
- Claim C (“cellular structures perform different functions”) is underspecified and needs decomposition or narrowing.
- OpenStax Biology 2e's official pages explicitly prohibit LLM training/ingestion or generative-AI use without prior written permission. This is a material unresolved issue for the project's AI-assisted workflow.
- An NCBI Bookshelf alternative was found for cell evolution/nucleus distinction, but the underlying book is publisher-copyrighted; NCBI hosting is not a redistribution licence. It is not a cleared replacement.

**Disposition: all 3 Claims HOLD.**

### Statistics basics — 11 records / 3 Claims

- Claim A has broad support in NIST/SEMATECH's handbook overview, but each bundled phrase needs a pinpoint.
- Claim B's general principle about assumptions and data acquisition is supported at handbook-purpose level; it is not yet supported as a universal method checklist.
- Claim C has a relevant NIST source family, but the exact design principle and analysis locator are missing.
- NIST Handbook 151 dates to 2002 (record updated 2021). Rights for every handbook component are not settled by the NIST landing page; do not assume all SEMATECH/contributor content is public domain.
- OpenStax Introductory Statistics 2e live preface carries both CC BY-NC-SA 4.0 and the explicit LLM-ingestion restriction. A downloadable PDF surfaced with a CC BY 4.0 statement, creating a version/representation discrepancy that must be resolved rather than silently choosing the permissive line.

**Disposition: all 3 Claims HOLD.**

### Queue adjustment

Neither slice is ready for reader selection. The next useful work is not writing new prose into canonical files: it is finding rights-compatible primary sources, pinning each EU, and preparing narrowly authorized versioned corrections only after editorial decisions. High-consequence Survival content remains ahead of these candidates in the overall first-edition release sequence.


## 7. Climate Basics and Measurement Uncertainty — combined 20-record refresh

Completed a second combined package covering both remaining top-priority foundational candidates:

- `RELEASE/CLIMATE-AND-MEASUREMENT-UNCERTAINTY-20-RECORD-RECHECK-AND-SOURCE-REFRESH-2026-11-23.md`
- Report commit: `12d493239c349fe80e92210770450364f2a1b7ff`

### Climate Basics — 9 records / 3 Claims

- Claim A is supported by NASA/NOAA definitions of climate as long-term weather characteristics, but “Earth system” is broader and needs a corresponding locator.
- Claim B bundles observational measurements and model outputs; those are distinct evidence modes and need separate pinpoints and careful wording.
- Claim C has strong NASA/NOAA support: individual weather and climate operate on different time scales. The EU should explicitly avoid the overreach that single events can never be climate-related.
- Candidate sources now include exact NASA weather/climate FAQ, NOAA weather/climate explainer, NOAA climate monitoring and climate data resources. Text-only factual paraphrase is proposed; images and third-party assets are excluded pending separate rights checks.

**Disposition: all 3 Claims HOLD; evidence pinpoint remediation is the primary task.**

### Measurement Uncertainty — 11 records / 3 Claims

- NIST TN 1297 §2.1 says a measurement result is complete only with a quantitative uncertainty statement; this supports Claim A but its unconditional “must” needs qualification.
- VIM 2.26 defines uncertainty as a non-negative parameter characterizing dispersion of values attributed to a measurand; VIM 2.16 defines measurement error separately. Claim B is directionally sound but should not reduce uncertainty to repeated-observation spread.
- Claim C has relevant VIM/GUM support around the measurand and measurement model, but the current canonical graph does not link its EU to the BIPM source.
- Current BIPM guide listings include GUM-1:2023, GUM-6:2020, JCGM 100:2008 with Amendment 1:2026, and GUM-5:2026. This supersedes the assumption that GUM 2008 alone represents the current guide suite.
- JCGM publications carry explicit copyright/reproduction restrictions. Free download is not redistribution permission.

**Disposition: all 3 Claims HOLD; exact EU pinpoints, graph repair by versioned records, technical currentness and rights review remain.**

### Queue adjustment

Both chapters now have sufficiently specific source maps to support a future versioned EU remediation proposal, but neither is approved for selection. The next package should prioritize authorized versioned evidence corrections and rights-compatible text-only use, not canonical rewrites or release inclusion by inference.


## 8. Chemistry, Earth System and Learning — 27-record combined audit

Completed a third combined package covering three additional foundational chapters:

- `RELEASE/CHEMISTRY-EARTH-SYSTEM-LEARNING-27-RECORD-AUDIT-2026-11-23.md`
- Commit: `08c78eb91282dad93732784c418f3d8a4521b995`

### Mixtures and Solutions — 9 records / 3 Claims

- All three Claims now have meaningful v2 Evidence Use locators in §11.1 of OpenStax Chemistry 2e; exact page passages match homogeneous mixture, solvent/solute concentration relationship, and molecular/ionic dispersion.
- Critical rights finding: the current live Chemistry 2e preface states CC BY-NC-SA 4.0 and expressly prohibits LLM training/ingestion or generative-AI use without prior written permission. Historical mirrors/PDFs that show CC BY 4.0 cannot override the current live rights notice.
- Context/Scope target Claim A only.

**Disposition: all 3 Claims HOLD pending written rights permission or a rights-compatible replacement source.**

### Earth System Basics — 9 records / 3 Claims

- NASA's 2026 Earth System Science Spheres material identifies five spheres: atmosphere, biosphere, cryosphere, geosphere and hydrosphere.
- Canonical Claim A lists only four and omits cryosphere. This is a substantive classification issue, not just a missing locator; an editorial decision is required.
- Claim B's interaction idea is supported at high level; preserve the distinction between interaction and causation.
- Claim C's multi-domain observation idea is plausible but needs an exact locator and bounded wording.
- The source page includes credited visual assets; this audit proposes text-only factual paraphrase, not asset reuse.

**Disposition: all 3 Claims HOLD.**

### Learning Basics — 9 records / 3 Claims

- NIMH's Learning and Memory Program page directly lists working memory, episodic encoding, consolidation and retrieval, supporting Claim A's representative list.
- The same page does not directly support Claim B's categorical assertion about interaction among neural systems or Claim C's generalization about task, population and experimental design.
- Claim A still needs a pinpointed EU; B/C need more direct scientific sources.

**Disposition: all 3 Claims HOLD.**

### Queue refinement

Earth System A now requires an explicit four-/five-sphere editorial decision. Chemistry cannot progress to publication on the current OpenStax source without resolving the AI-ingestion and licence restrictions. Learning A is the most bounded of these three; Learning B/C need replacement evidence rather than generic source descriptions.


## 9. Emergency Alerts, Hand Hygiene and Food Security — 33-record audit

Completed the next operationally important package:

- `RELEASE/EMERGENCY-ALERTS-HAND-HYGIENE-FOOD-SECURITY-33-RECORD-AUDIT-2026-11-23.md`
- Commit: `46956ca80b38378edf52bd19e4ff35e2afaae2f5`

### Emergency Alert Warning — 10 records / 3 Claims

- Red Cross Claim v2 and EU v2 are well bounded to U.S. disaster preparedness: local notification channels, watch/warning distinction and knowing protective actions. It does not recommend enabling mobile alerts.
- Two FEMA IPAWS Claims have exact locators in TIP 44 §II.A–B and §II.B, printed page 1. They concern WEA message content and message elements, not universal guarantees about every alert channel.
- Context/Scope target the content Claim only, not the message-elements Claim.

**Disposition:** promising evidence fit; all three HOLD pending Human View, reader and rights review.

### Emergency Hand Hygiene — 11 records / 1 Claim plus process/action/result chain

- CDC's current emergency hygiene page (2024-08-05) directly confirms soap-and-water handwashing for at least 20 seconds.
- The CDC EU still lacks a formal locator; the WHO corroboration EU is also generic.
- The process/action chain is explicit, but its steps need their own evidence mapping. The Result record must not imply guaranteed removal of every contaminant; CDC distinguishes soap/water from sanitizer and warns about water-safety conditions.

**Disposition:** Claim supported, but all records HOLD pending versioned EU pinpoints, step-level evidence and safety Human View.

### Food Security Basics — 12 records / 4 Claims

- FAO handbook §1.4 directly supports Claim A's physical/economic access definition and Claim B's three classic dimensions: availability, stability and access.
- FAO's information and early-warning handbook supports Claim C at high level; exact chapter/section locator is missing.
- USDA ERS Measurement page updated 2026-03-30 directly supports household Claim D; it must retain its U.S. household-measurement context.
- All four EUs are currently generic; they need exact locators. The three classic dimensions should not be presented as the only modern taxonomy.

**Disposition:** all four HOLD pending versioned EU pinpoints, rights and reader review.

### Queue refinement

These three slices have stronger source fit than many generic candidates. Next execution should prioritize versioned Evidence Use locator proposals and Human View for the two emergency slices, while keeping safety review distinct from public release approval. Food Security can be remediated as an explanatory foundational slice once its four locators and attribution are fixed.
