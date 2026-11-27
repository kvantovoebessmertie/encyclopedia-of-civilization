# First Edition — Chemistry, Earth System and Learning: 27-Record Combined Audit

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Inspection HEAD: `8d310f71deb550474a277093e5ad9b03a8e007de`  
Status: BOUNDED RECORD / SOURCE / RIGHTS SCREEN — NO CANONICAL WRITES

## 1. Scope

This package re-fetched 27 records across three foundational slices: Mixtures and Solutions (9), Earth System Basics (9), and Learning Basics (9). Each record was checked at its exact current version and blob SHA. The audit examines Claim wording, Evidence Use locator quality, Source fit, Context/Scope target boundaries, source currentness and rights signals.

It is not a complete subject-matter peer review, legal opinion, full corpus graph audit, or release approval. No canonical record, status, candidate register, allowlist or selection manifest was changed. All nine Claims remain HOLD.

## 2. Mixtures and Solutions — 9 records

### 2.1 Exact record identities

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-MIXTURES_AND_SOLUTIONS-A | 1 | Claim | `69ad55e5dbf0f101cb0ffa3cf2449716456f49f9` |
| CLM-MIXTURES_AND_SOLUTIONS-B | 1 | Claim | `c2fd740ff89000ed712e398e1cc58171aee9ea2c` |
| CLM-MIXTURES_AND_SOLUTIONS-C | 1 | Claim | `ddbf49be51fca3c6521da7e850ab926561f43586` |
| EU-MIXTURES_AND_SOLUTIONS-A | 2 | Evidence Use | `a6ecb5c9eb7cb084d8d35568bb8e21ebbdb30576` |
| EU-MIXTURES_AND_SOLUTIONS-B | 2 | Evidence Use | `dcf4d0587378605223e7938d74eb491be14705b4` |
| EU-MIXTURES_AND_SOLUTIONS-C | 2 | Evidence Use | `80ccc43325b3d6ff50fe7caaa010b005e68ca68b` |
| SRC-MIXTURES_AND_SOLUTIONS | 1 | Source | `d96dda3b7a8cdc19df05ce966336a4f2110264c0` |
| CTX-MIXTURES_AND_SOLUTIONS | 1 | Context | `a65bb56743ac2e0237bc36467ff7f0735a5b1bc0` |
| SCP-MIXTURES_AND_SOLUTIONS | 1 | Scope | `4c8889adca12c89b391ce9b4948fb9d324165067` |

### 2.2 Claim-level findings

**Claim A — solution as homogeneous mixture**

The v2 EU now supplies a reproducible locator: OpenStax Chemistry 2e §11.1, opening definition paragraph. The official section describes solutions as homogeneous and compositionally uniform at all points. This is a strong, direct match.

**Claim B — solvent component**

The v2 EU points to §11.1 and says the solvent is present at significantly greater concentration than the solutes. The canonical Claim says “обычно присутствующий в большей концентрации” and that it determines the physical state. The source says the solvent is typically the most concentrated component and the physical state is typically the same as the solvent. This is close, but the Claim's “обычно” should remain; do not turn the statement into an absolute rule for every edge case or every mixture.

**Claim C — molecular or ionic dispersion**

The v2 EU identifies the sucrose dissolution and potassium dichromate dissociation examples and the discussion of molecular/ionic dispersion. The section says solute particles (molecules, atoms and/or ions) are dispersed on a molecular scale and gives examples of molecular dissolution and ionic dissociation. This directly supports the concept. The Russian “на молекулярном или ионном уровне” is acceptable as an introductory paraphrase, but the precise distinction is between molecular particles and ions dispersed in the solvent; avoid suggesting all solutes dissociate into ions.

### 2.3 Material rights blocker

The live OpenStax Chemistry 2e preface states CC BY-NC-SA 4.0 and separately says the book may not be used for LLM training/ingestion or generative-AI offerings without prior written permission. This is a material blocker for the Encyclopedia's AI-assisted workflow and intended distribution. The current live license/notice must control the rights review; older mirrors or historical PDFs that show CC BY 4.0 cannot silently override it.

No textbook prose, figure, table, exercise, video or image is proposed for reproduction in this report. A future rights review must decide whether independently authored factual paraphrases based on this source are acceptable for the project's processing and distribution model, or obtain written permission/use a cleared alternative.

### 2.4 Context/Scope and disposition

CTX and SCP target Claim A only. Their content must not be propagated automatically to B/C.

**Disposition: all 3 Claims HOLD.** Evidence locators are now materially better (EU v2), but rights clearance and independent source strategy remain unresolved. No canonical writes authorized.

## 3. Earth System Basics — 9 records

### 3.1 Exact record identities

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-EARTH_SYSTEM_BASICS-A | 1 | Claim | `7b4045bf4cf16dc31d7e5ba841759d3053a398e2` |
| CLM-EARTH_SYSTEM_BASICS-B | 1 | Claim | `43a2c5623e2b0be92df320bf9378c9ac4e6e2e84` |
| CLM-EARTH_SYSTEM_BASICS-C | 1 | Claim | `9ed16eb74b6b1e1a77271b0bc7de5686ac5df849` |
| EU-EARTH_SYSTEM_BASICS-A | 1 | Evidence Use | `4a71525e2a1a40b41751c98e6faeaf79df2165dc` |
| EU-EARTH_SYSTEM_BASICS-B | 1 | Evidence Use | `72de6fc61e63f7ad918f1c32695b47d445724236` |
| EU-EARTH_SYSTEM_BASICS-C | 1 | Evidence Use | `cf77ef480c7fde54bd04590b8515641e7d23d6ae` |
| SRC-EARTH_SYSTEM_BASICS | 1 | Source | `df54b5ef0d943a34a5066de3a73ca7105a0003f8` |
| CTX-EARTH_SYSTEM_BASICS | 1 | Context | `ecf00cd9c863a18e3db91f811d2ca1dc61ad57f3` |
| SCP-EARTH_SYSTEM_BASICS | 1 | Scope | `ed6919c853344db976384ec7152bebb6f487ad2c` |

### 3.2 Claim-level findings

**Claim A — components of the Earth system**

Canonical statement lists atmosphere, hydrosphere, geosphere and biosphere as interconnected components. NASA's current Earth System Science Spheres material explicitly presents five spheres: atmosphere, biosphere, cryosphere, geosphere and hydrosphere, and says they interact in complex ways.

The canonical four-part list omits the cryosphere. It may be possible to treat cryosphere as part of the hydrosphere in some classification schemes, but the Claim currently gives no such qualification and the NASA source explicitly distinguishes it as a separate sphere. This is a substantive taxonomy mismatch, not merely a missing locator.

**Finding:** HOLD pending an explicit editorial decision: either list five spheres, or explain the chosen four-sphere classification and how cryosphere is treated. Do not silently change the Claim.

**Claim B — changes in one component can interact with others**

NASA's Earth-system material directly supports interaction among spheres. The Claim is appropriately modal (“могут взаимодействовать”) and should not be expanded into a deterministic causal claim. The current EU is generic and points only to the NASA Earth portal.

**Finding:** good conceptual fit; exact interaction examples/locator needed. Preserve the distinction between interaction and demonstrated causation.

**Claim C — Earth-system observation integrates data from different scientific fields**

NASA's 2026 Earth System Science Spheres page describes satellite missions and field campaigns measuring key Earth processes across places and times of year, with multiple sphere-specific datasets. This supports cross-domain observation. However, “данные разных областей науки” is broad; the EU should name the relevant observational domains and avoid implying that every Earth-system observation integrates all disciplines.

**Finding:** plausible, but needs a precise locator and narrower description of the observation programme.

### 3.3 Source/currentness and rights

The existing Source is a broad NASA Earth portal. A better source candidate is NASA Scientific Visualization Studio, “The Earth System Science Spheres” (released 2026-03-01). It is current and explicitly distinguishes five spheres. The page includes animation and data visualizations with asset credits. This audit uses only its textual description; no visual assets are proposed for reuse. Every NASA asset must be checked against its own credit line and terms.

### 3.4 Context/Scope and disposition

CTX and SCP target Claim A only. Context correctly warns that observed sequence alone does not prove causation; this is particularly relevant to Claim B and C but cannot be treated as automatically linked to those claims.

**Disposition: all 3 Claims HOLD.** Claim A has a substantive classification issue (four vs five spheres); B/C need exact pinpoints and tighter evidence-use descriptions.

## 4. Learning Basics — 9 records

### 4.1 Exact record identities

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-LEARNING_BASICS-A | 1 | Claim | `c60aa3b2a56bf9a2f3bdb8af0c306bab6b1e7d82` |
| CLM-LEARNING_BASICS-B | 1 | Claim | `ad2abcc341bfe5821f179bdea259f64c86ae06d4` |
| CLM-LEARNING_BASICS-C | 1 | Claim | `761ff58eb11293d88242851dd7a8e442d1626bc4` |
| EU-LEARNING_BASICS-A | 1 | Evidence Use | `221c07ee66fed96e3ebecd16f0707fa26a364325` |
| EU-LEARNING_BASICS-B | 1 | Evidence Use | `76ad4628f7b4cd8423a44f6057a2c5161beea7fb` |
| EU-LEARNING_BASICS-C | 1 | Evidence Use | `af8ba252f4cfa8a2f7a3703e73b9c7087fce78e0` |
| SRC-LEARNING_BASICS | 1 | Source | `644b064a938e1bdb30190a1abac2fa86d6d36b3e` |
| CTX-LEARNING_BASICS | 1 | Context | `6e162b594df1c5cc033fecc06306688315a3659b` |
| SCP-LEARNING_BASICS | 1 | Scope | `5db34a2d87af13241572a235eda84c7120b777a0` |

### 4.2 Claim-level findings

**Claim A — processes examined in learning and memory research**

Canonical statement is in English: “Learning and memory research examines processes including encoding, consolidation, retrieval and working memory.”

NIMH's Learning and Memory Program page directly lists working memory, episodic encoding, consolidation and retrieval as cognitive processes within the program's research scope. This is a direct match to the list. The wording should remain a statement about the research program/field, not a universal taxonomy of all learning and memory processes.

**Finding:** strongest claim in this slice; current EU still needs a direct locator and should specify that this is a representative list, not exhaustive.

**Claim B — interactions among neural systems**

Canonical statement: “Learning and memory involve interactions among neural systems rather than a single isolated mechanism.”

NIMH describes research questions about neural systems and computational algorithms supporting different forms of memory and how brain information is processed. That is relevant, but the current program overview does not directly establish the exact general statement that learning and memory always involve interactions among multiple neural systems rather than a single isolated mechanism. A more direct neuroscience review or textbook section is needed.

**Finding:** current source is relevant background but insufficiently direct for the exact proposition. Do not upgrade based on thematic relevance.

**Claim C — task, population and experimental design dependence**

Canonical statement: “Research findings about learning can depend on the task, population and experimental design.”

The current NIMH program page describes research scope but does not substantiate this methodological generalization. It does not compare populations or task paradigms, nor discuss external validity or experimental design. The EU-C description therefore overstates the source's support.

**Finding:** evidence mismatch. A direct methods/reproducibility or cognitive-science source is required.

### 4.3 Source and rights review

The NIMH page is a U.S. federal government website and a research-program description. This is not a primary scientific review for every claim in the slice. Use it for the program's stated research scope only; do not treat it as a source for universal neuroscience propositions. No images or page text are proposed for reproduction. A separate rights check is required for any third-party assets or linked publications.

### 4.4 Context/Scope and disposition

CTX and SCP target Claim A only. Context appropriately warns against converting general mechanisms into universal individual learning instructions. It should not be displayed as a clinical, pedagogical or individual treatment recommendation.

**Disposition: Claim A HOLD pending exact EU; Claim B HOLD pending direct scientific support; Claim C HOLD due to current evidence mismatch.**

## 5. Combined remediation order

1. **Earth System A:** editorial decision on four-sphere versus five-sphere classification. This is a substantive issue and must be resolved before locator work can close it.
2. **Mixtures and Solutions:** source locators are now good at v2, but resolve OpenStax Chemistry 2e AI-ingestion permission and CC BY-NC-SA terms; consider an independently cleared chemistry source.
3. **Earth System B/C:** add exact NASA Earth System Science Spheres locator and bounded descriptions; keep interaction separate from causation.
4. **Learning A:** add direct NIMH program locator and preserve representative/non-exhaustive list boundary.
5. **Learning B/C:** seek new scientific sources that directly support the exact neural-interaction and task/population/design propositions; do not reuse the NIMH overview as a blanket source.
6. Preserve exact versions and Context/Scope target boundaries; use versioned EU records and explicit editorial authorization for all changes.

**Final disposition: 27 records inspected; 9 Claims remain HOLD; zero canonical writes; zero INCLUDE decisions.**
