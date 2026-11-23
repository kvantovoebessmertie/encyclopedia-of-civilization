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
