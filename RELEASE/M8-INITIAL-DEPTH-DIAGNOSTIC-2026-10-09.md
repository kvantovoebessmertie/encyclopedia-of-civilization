# M8 Initial Depth Diagnostic — 2026-10-09

## Snapshot and method

- **Corpus SHA scored:** `66e63e33771da7c82c9e0b89c2cd9d7512e748aa` (accepted M7 CLEAN content snapshot).
- **M8 working branch:** `m8-depth-baseline-2026-10-09`; current work before this audit is documentation-only.
- **Corpus frame:** 483 slices / 4,827 Records / 19 Record types.
- **Sample:** 12 slices; every Claim in each selected slice reviewed (43 Claims total).
- **Design:** stratified, purposive diagnostic sample; not random, not population-weighted, and not a statistical estimate of the entire corpus.
- **Review inputs:** Claim statements, all registered Evidence Use records in the sampled slices, source identities/locators, Context/Scope records when present, and slice READMEs. The four M7 slices also use the recorded M7 substantive/evidence audits.
- **Reviewer status:** first-pass desk scoring. High-consequence findings are explicit; a second independent review is required before final closure of any substantive correction.
- **Rubric:** D = explanatory depth; E = claim-specific evidence fit; B = boundary/epistemic discipline. Each dimension 0–3. No composite score or project-completion percentage is calculated.

## Frozen sample

| Stratum | Slice | Claims reviewed |
|---|---|---:|
| H — high-consequence/practical | `water` | 4 |
| H — high-consequence/practical | `generator-carbon-monoxide-safety` | 4 |
| M — prior maturation | `sleep-basics` | 3 |
| M — prior maturation | `governance-basics` | 3 |
| I — cross-domain/infrastructure | `human-settlement-systems-basics` | 3 |
| I — cross-domain/infrastructure | `supply-chain-basics` | 4 |
| G — general introductory | `mechanics-basics` | 3 |
| G — general introductory | `statistics-basics` | 3 |
| N — newest M7 content | `woodworking-basics` | 4 |
| N — newest M7 content | `papermaking-basics` | 4 |
| N — newest M7 content | `ceramics-basics` | 4 |
| N — newest M7 content | `textile-fibre-processing-basics` | 4 |
| **Total** | **12 slices** | **43** |

The water slice has no dedicated Context or Scope Record in its package; its human-facing README contains use limits. This is scored as a machine-readable boundary gap, not as absence of every safety warning.

## Claim-level scores

D/E/B scores are diagnostic judgements anchored to the published rubric. Notes explain the decisive reason; they are not claims of mathematical precision.

| Slice | Claim ID | D | E | B | Rationale |
|---|---|---:|---:|---:|---|
| water | `CLM-WATER-BOILING-EFFECTIVE` | 1 | 2 | 1 | Useful basic claim; record-level Context/Scope absent although README limits use. |
| water | `CLM-WATER-BOILING-TIME` | 2 | 2 | 2 | Specific duration and altitude condition linked to CDC. |
| water | `CLM-WATER-CHEMICAL-LIMIT` | 2 | 2 | 3 | Explicit chemical/fuel/radioactive boundary. |
| water | `CLM-WATER-INDEPENDENT-CORROBORATION` | 2 | 3 | 3 | CDC/EPA triangulation and contamination-dependent boundary; partly overlaps other water claims. |
| generator-carbon-monoxide-safety | `CLM-GENERATOR-CO-ALARM-EMERGENCY` | 3 | 2 | 3 | Clear escalation action and no-return boundary; CDC directly supports. |
| generator-carbon-monoxide-safety | `CLM-GENERATOR-NO-INDOOR` | 2 | 2 | 3 | Direct prohibition, causal CO risk, Context/Scope. |
| generator-carbon-monoxide-safety | `CLM-GENERATOR-OUTSIDE-20FT` | 2 | 2 | 3 | Specific placement boundary with linked source. |
| generator-carbon-monoxide-safety | `CLM-GENERATOR-REFUEL-COOL` | 2 | 2 | 3 | Specific fire-safety action with CPSC evidence. |
| sleep-basics | `CLM-SLEEP_BASICS-A` | 1 | 2 | 2 | Correct high-level description; little explanation of cycle structure. |
| sleep-basics | `CLM-SLEEP_BASICS-B` | 1 | 2 | 2 | Basic rhythm statement with light/dark context, little mechanism. |
| sleep-basics | `CLM-SLEEP_BASICS-C` | 1 | 3 | 2 | Cautious broad claim with NHLBI and independent CDC corroboration. |
| governance-basics | `CLM-GOVERNANCE_BASICS-A` | 1 | 2 | 2 | Framework-attributed definition; statement and README are English. |
| governance-basics | `CLM-GOVERNANCE_BASICS-B` | 1 | 2 | 2 | Reports OECD framework structure without explaining interactions. |
| governance-basics | `CLM-GOVERNANCE_BASICS-C` | 2 | 3 | 3 | Methodological uncertainty boundary with OECD/WGI evidence; English-facing text remains. |
| human-settlement-systems-basics | `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_A` | 1 | 2 | 2 | Broad system definition, limited mechanisms/examples. |
| human-settlement-systems-basics | `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B` | 2 | 2 | 2 | Names interdependent components but not dependency pathways. |
| human-settlement-systems-basics | `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C` | 2 | 2 | 3 | Integrated-planning boundary; no concrete example. |
| supply-chain-basics | `CLM-M5-SUPPLY-CHAIN-VISIBILITY-D` | 3 | 2 | 3 | Nuanced traceability limitation; OECD support; English Evidence Use description. |
| supply-chain-basics | `CLM-SUPPLY_CHAIN_BASICS-A` | 2 | 3 | 2 | NIST and CISA support multi-tier cyber risk; scope is bounded to cyber. |
| supply-chain-basics | `CLM-SUPPLY_CHAIN_BASICS-B` | 2 | 2 | 2 | Risk process and contextual dependence present; no operational detail. |
| supply-chain-basics | `CLM-SUPPLY_CHAIN_BASICS-C` | 2 | 2 | 2 | Specific visibility limitation with claim-specific NIST evidence. |
| mechanics-basics | `CLM-MECHANICS_BASICS-A` | 0 | 1 | 1 | Self-referential statement, not a mechanics proposition; evidence text generic. |
| mechanics-basics | `CLM-MECHANICS_BASICS-B` | 0 | 1 | 1 | Generic source/context caveat rather than mechanics knowledge. |
| mechanics-basics | `CLM-MECHANICS_BASICS-C` | 0 | 1 | 1 | Generic disclaimer, not a mechanics proposition; Newton's-law source not tied to a substantive claim. |
| statistics-basics | `CLM-STATISTICS_BASICS-A` | 1 | 3 | 2 | Broad definition independently corroborated by OpenStax, but no example/method detail. |
| statistics-basics | `CLM-STATISTICS_BASICS-B` | 1 | 1 | 2 | Generic assumptions/data-source statement; Evidence Use does not identify specific support. |
| statistics-basics | `CLM-STATISTICS_BASICS-C` | 1 | 1 | 2 | Broad research-design statement; Evidence Use material is generic. |
| woodworking-basics | `CLM-WOODWORKING_BASICS-A` | 2 | 2 | 2 | Mechanism and material dependencies at introductory level. |
| woodworking-basics | `CLM-WOODWORKING_BASICS-B` | 2 | 2 | 3 | Relevant variability and explicit exclusion of structural-design inference. |
| woodworking-basics | `CLM-WOODWORKING_BASICS-C` | 1 | 2 | 2 | Useful operation taxonomy but little explanation of when operations differ. |
| woodworking-basics | `CLM-WOODWORKING_BASICS-D` | 2 | 3 | 3 | Direct occupational-hazard source and process/jurisdiction limits. |
| papermaking-basics | `CLM-PAPERMAKING_BASICS-A` | 2 | 3 | 2 | Process stages explained and independently corroborated. |
| papermaking-basics | `CLM-PAPERMAKING_BASICS-B` | 1 | 3 | 2 | Fibre/mass variation described; no universal formula asserted. |
| papermaking-basics | `CLM-PAPERMAKING_BASICS-C` | 2 | 3 | 2 | Distinct functions of process stages with complementary sources. |
| papermaking-basics | `CLM-PAPERMAKING_BASICS-D` | 2 | 2 | 3 | Explicit epistemic boundary on food/archive suitability. |
| ceramics-basics | `CLM-CERAMICS_BASICS-A` | 2 | 3 | 3 | Silica-dust risk, complementary EHS evidence and exposure boundary. |
| ceramics-basics | `CLM-CERAMICS_BASICS-B` | 1 | 3 | 3 | Glaze-composition warning with complementary university EHS evidence. |
| ceramics-basics | `CLM-CERAMICS_BASICS-C` | 2 | 3 | 3 | Firing/ventilation hazards; no universal kiln design asserted. |
| ceramics-basics | `CLM-CERAMICS_BASICS-D` | 2 | 3 | 3 | Food-contact boundary supported by EHS and FDA. |
| textile-fibre-processing-basics | `CLM-TEXTILE_FIBRE_PROCESSING_BASICS-A` | 1 | 2 | 3 | Coir-specific source distinguished from other fibres. |
| textile-fibre-processing-basics | `CLM-TEXTILE_FIBRE_PROCESSING_BASICS-B` | 1 | 2 | 3 | Introductory preparation operations; FAO AGRIS is scope-level only. |
| textile-fibre-processing-basics | `CLM-TEXTILE_FIBRE_PROCESSING_BASICS-C` | 2 | 2 | 3 | Joining/twisting and process variation; quantitative properties absent. |
| textile-fibre-processing-basics | `CLM-TEXTILE_FIBRE_PROCESSING_BASICS-D` | 2 | 2 | 3 | Suitability tied to intended product; no false universal equivalence. |

## Claim-level distribution

| Dimension | Score 0 | Score 1 | Score 2 | Score 3 | Mean / median |
|---|---:|---:|---:|---:|---|
| D — depth (n=43) | 3 | 15 | 23 | 2 | 1.56 / 2 |
| E — evidence fit (n=43) | 0 | 5 | 25 | 13 | 2.19 / 2 |
| B — boundary discipline (n=43) | 0 | 4 | 19 | 20 | 2.37 / 2 |

Interpretation: this diagnostic sample shows a clearer weakness in explanatory depth than in evidence linkage or boundary discipline. Means are descriptive only; the sample is purposive and not population-weighted. The 18 claims with D≤1 are not automatically all defects: several are intentionally introductory or safety-boundary claims. Confirmed severe findings are separated below.

## Slice-level Human View desk scores

H1 = findability; H2 = comprehension; H3 = safe interpretation. These are desk-review scores, not live user-study results.

| Slice | H1 | H2 | H3 | Observation |
|---|---:|---:|---:|---|
| water | 3 | 3 | 2 | Russian README makes use limits discoverable; no record-level Context/Scope. |
| generator-carbon-monoxide-safety | 3 | 3 | 3 | Clear Russian practical summary, explicit scope and emergency boundary. |
| sleep-basics | 2 | 2 | 3 | Context/Scope clear; README is a terse English template. |
| governance-basics | 2 | 1 | 2 | Claim statements and README are English; Context/Scope are Russian. |
| human-settlement-systems-basics | 2 | 2 | 3 | Purpose/boundaries present; README template is English. |
| supply-chain-basics | 2 | 2 | 3 | Useful Russian summary; some Evidence Use text remains English. |
| mechanics-basics | 1 | 1 | 1 | README and Claims are generic; no substantive mechanics teaching. |
| statistics-basics | 2 | 2 | 2 | Sources and general scope identified; Claims/Evidence Use B/C are generic. |
| woodworking-basics | 3 | 3 | 3 | Clear coverage, sources and boundaries; introductory depth remains limited by design. |
| papermaking-basics | 3 | 3 | 3 | Process stages and product-suitability exclusions are discoverable. |
| ceramics-basics | 3 | 3 | 3 | Safety risks and boundaries are discoverable; claim depth varies. |
| textile-fibre-processing-basics | 3 | 3 | 3 | Fibre-specific and source-quality limits are explicit. |

Slice-level distributions (n=12): H1: 1/5/6 at scores 1/2/3; H2: 2/4/6; H3: 1/3/8. No live novice study was performed.

## Confirmed findings

### M8-DEPTH-001 — CRITICAL: mechanics-basics is structurally present but substantively hollow
All three Claims score D=0: they describe the slice or offer generic caveats rather than stating a mechanics principle, despite the cited OpenStax University Physics/Newton's Laws source. All three Evidence Use descriptions say only that the source is used “within the stated material.” This is not a request to add more records; it is a confirmed content/evidence-fit failure. Proposed correction: replace the meta-claims with bounded, source-supported introductory mechanics propositions and claim-specific Evidence Use; add/adjust dedicated regressions without weakening existing checks.

### M8-DEPTH-002 — HIGH: statistics-basics has generic evidence material for Claims B and C
Claims B/C are broad statements about assumptions/data collection and experimental design, while their Evidence Use descriptions are generic and do not identify specific support. Claim A has a more useful independent OpenStax corroboration. Proposed correction: either narrow B/C to directly supported propositions with source-specific evidence material or find the precise supporting sections and describe them. Do not add sources merely to increase count.

### M8-BOUNDARY-003 — HIGH: water slice lacks machine-readable Context and Scope
The README clearly warns that boiling does not remove some chemical/fuel/radioactive contaminants and excludes region-specific water quality and individualized decisions. The package nevertheless contains only two Sources, four Claims and four Evidence Use records, with no Context or Scope Record. This leaves important limits outside the structured Record graph. Proposed correction: add appropriately targeted Context/Scope records and dedicated regression assertions, without rewriting the already supported safety claims absent a substantive finding.

### M8-HUMAN-004 — MEDIUM: language inconsistency in governance-basics
All three Claim statements and the README are in English while the Context/Scope records are Russian. This is a concrete accessibility mismatch for the Russian-facing corpus. Proposed correction: translate human-facing Claim/README wording without changing claim semantics, provenance, source identity or Evidence Use links; add a language-consistency regression if an established pattern exists.

### M8-HUMAN-005 — LOW/MEDIUM: residual English Evidence Use material in comparison slices
English Evidence Use descriptions remain in parts of `supply-chain-basics` and the older `sleep-basics` evidence records. This is not a source-fit failure by itself. Normalize only where needed for the intended human-facing language and only if the correction is authorized and testable; do not bulk-translate canonical source titles or identities.

## Limits and next gate

- This first pass is one reviewer’s desk assessment; it must not be reported as a statistically representative score for all 483 slices.
- M7 remains accepted CLEAN at its immutable SHA. Findings in M8 do not retroactively change M7 acceptance; they identify older/newer corpus maturity gaps in the broader sample.
- No content correction is included in this measurement commit. The next action is a controlled M8 scope lock for M8-DEPTH-001, M8-DEPTH-002, M8-BOUNDARY-003 and M8-HUMAN-004, followed by exact source rechecks, dedicated regression work, post-correction audit and exact-head CI.
