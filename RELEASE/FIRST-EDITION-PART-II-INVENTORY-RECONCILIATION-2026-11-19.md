# PR #22 — Part II inventory reconciliation checkpoint

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspected baseline HEAD: `2d548434ce465d47320eb8de911f5fbf7ecaec0b`  
Workstream: Work Package 1 — first-edition corpus selection  
Status: **SLICE-LEVEL RECONCILIATION COMPLETE; EXACT-VERSION MASTER REGISTER STILL INCOMPLETE**

## 1. Purpose and boundaries

This report reconciles the current corpus slice inventory with the existing first-edition candidate register and the ten Part II addenda. It is a deduplication and coverage checkpoint, not a new substantive adjudication.

- No M13 batch was started.
- No closed Part I or prior domain audit was repeated.
- No INCLUDE/HOLD/EXCLUDE decision was changed.
- No public allowlist or preview allowlist was created.
- No canonical Claim, Evidence Use, Source, Context, Scope or Relation was changed by this report.
- The unregistered Part II slices below are a backlog for scope triage, not an instruction to audit every repository slice or a release requirement. The controlling first-edition map explicitly describes its examples as non-exhaustive.

## 2. Corpus denominator and slice coverage

Source: `CONTENT/README.md` machine-checked slice registry and `RELEASE/FIRST-EDITION-PART-I-SURVIVAL-FULL-SLICE-INVENTORY-2026-11-18.md`.

| Measure | Count |
|---|---:|
| Current vertical-slice directories in the corpus registry | 479 |
| Part I survival slices, exact inventory | 94 |
| Remaining non-Part-I / wider-corpus slices | 385 |
| Part II slices represented in the base candidate register | 37 |
| Additional Part II slices represented in the ten addenda | 64 |
| Unique Part II slices represented after slice-level deduplication | 99 |
| Part II slices not yet represented in the candidate registers | 286 |

The Part I denominator remains 94/94. The arithmetic Part II pool is 385 slices. 99 of those have an existing candidate-register or addendum reference after slice-level deduplication; 286 do not. This is not a claim that all 385 slices belong in the first edition.

## 3. Base Part II candidate register — 37 slices

The base register contains candidate-level material for these 37 non-Part-I slices. Counts below are explicit `RECORD_ID@version` tokens mapped from the base register text; some identifiers are nonstandard or abbreviated, so the master ledger preserves the source spelling until canonical JSON verification.

- `agricultural-engineering-basics` — 4 explicit identifier tokens; HOLD
- `agrifood-systems-basics` — 4 explicit identifier tokens; HOLD
- `antimicrobial-resistance-basics` — 1 explicit identifier tokens; HOLD
- `astronomy-basics` — 3 explicit identifier tokens; HOLD
- `biodiversity-basics` — 5 explicit identifier tokens; HOLD
- `cell-basics` — 3 explicit identifier tokens; HOLD
- `cell-biology-basics` — 3 explicit identifier tokens; HOLD
- `conservation-biology-basics` — 4 explicit identifier tokens; HOLD
- `disaster-recovery-basics` — 11 explicit identifier tokens; HOLD
- `disaster-response-logistics-basics` — 12 explicit identifier tokens; HOLD
- `ecophysiology-basics` — 6 explicit identifier tokens; HOLD
- `ecotoxicology-basics` — 4 explicit identifier tokens; HOLD
- `electrical-grid-basics` — 11 explicit identifier tokens; HOLD
- `entomology-basics` — 4 explicit identifier tokens; HOLD
- `evolution-basics` — 3 explicit identifier tokens; HOLD
- `food-distribution-basics` — 10 explicit identifier tokens; HOLD
- `food-systems-basics` — 10 explicit identifier tokens; HOLD
- `genetics-basics` — 3 explicit identifier tokens; HOLD
- `immunology-basics` — 3 explicit identifier tokens; HOLD
- `infrastructure-resilience-basics` — 14 explicit identifier tokens; HOLD
- `marine-biology-basics` — 4 explicit identifier tokens; HOLD
- `measurement-uncertainty-basics` — 3 explicit identifier tokens; HOLD
- `motion-basics` — 4 explicit identifier tokens; HOLD
- `parasitology-basics` — 1 explicit identifier tokens; HOLD
- `pathology-basics` — 6 explicit identifier tokens; HOLD
- `plant-pathology-basics` — 6 explicit identifier tokens; HOLD
- `si-units-basics` — 6 explicit identifier tokens; HOLD
- `soil-microbiology-basics` — 4 explicit identifier tokens; HOLD
- `soil-science-basics` — 4 explicit identifier tokens; HOLD
- `statistics-basics` — 4 explicit identifier tokens; HOLD
- `thermodynamics-basics` — 3 explicit identifier tokens; HOLD
- `units-and-measurement` — 9 explicit identifier tokens; HOLD
- `vaccination-information-basics` — 1 explicit identifier tokens; HOLD
- `virology-basics` — 1 explicit identifier tokens; HOLD
- `water-quality-basics` — 11 explicit identifier tokens; HOLD
- `water-resource-management-basics` — 5 explicit identifier tokens; HOLD
- `water-security-basics` — 7 explicit identifier tokens; HOLD

The base candidate register contains 595 distinct explicit `RECORD_ID@version` tokens across its full contents, including Part I. The Part II subset mapped here is 197 references across 37 slices. Do not treat the full 595 as a Part II-only denominator.

## 4. Ten Part II addenda — 64 slices (62 new after two base-register overlaps)

Reported addendum record total: **621 records before cross-document deduplication**. All 621 records across the ten addenda are now enumerated as exact canonical record/version rows. No addendum remains summary-only. Legal/trade/institutional's three dependent relation-alignment rows are not counted as vertical-slice records.

### Foundations
- `units-and-measurement` — 9 records (exact IDs pinned in FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `geometry-basics` — 9 records (exact IDs pinned in FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `calculus-basics` — 9 records (exact IDs pinned in FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)

### Physical sciences
- `temperature-basics` — 9 records (exact IDs pinned in FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `waves-and-sound-basics` — 9 records (exact IDs pinned in FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `optics-basics` — 9 records (exact IDs pinned in FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `magnetism-basics` — 9 records (exact IDs pinned in FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `mechanics-basics` — 9 records (exact IDs pinned in FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `fluid-mechanics-basics` — 9 records (exact IDs pinned in FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `electromagnetism-basics` — 9 records (exact IDs pinned in FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)

### Chemical sciences
- `mixtures-and-solutions` — 9 records (exact IDs pinned in FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `chemical-reactions-basics` — 9 records (exact IDs pinned in FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `organic-chemistry-basics` — 9 records (exact IDs pinned in FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `biochemistry-basics` — 9 records (exact IDs pinned in FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)

### Economic systems
- `accounting-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `macroeconomics-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `microeconomics-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `money-and-banking-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `organizational-behavior-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)

### History and culture
- `historical-geography-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md)
- `history-of-science-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md)
- `history-of-technology-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md)
- `religious-studies-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md)
- `literature-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md)
- `cultural-anthropology-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md)

### Society and public institutions
- `sociology-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `law-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `demography-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `governance-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `public-administration-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `education-systems` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `democratic-institutions-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `public-budgeting-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `social-statistics-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)
- `migration-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md)

### Legal, trade and institutional systems
- `political-economy-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `comparative-law-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `administrative-law-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `international-law-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `civil-society-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `social-policy-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `taxation-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `labor-economics-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `migration-and-mobility-basics` — 13 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)
- `comparative-civilizations-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md)

### Engineering and computing
- `software-engineering-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `computer-science-algorithms-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `databases-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `distributed-systems-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `artificial-intelligence-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `computer-networks-basics` — 9 records (exact IDs pinned in FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)

### Earth, climate and space
- `climate-science-basics` — 9 records (exact IDs pinned in FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `solar-system-basics` — 9 records (exact IDs pinned in FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)
- `remote-sensing-basics` — 9 records (exact IDs pinned in FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md; HOLD)

### R9 evidence-depth follow-up
- `history-of-medicine-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `history-of-mathematics-basics` — 11 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `history-of-engineering-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `cartography-basics` — 10 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `hydraulic-engineering-basics` — 10 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `food-systems-basics` — 12 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `cultural-heritage-basics` — 10 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `library-science-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `archival-science-basics` — 10 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)
- `settlement-geography-basics` — 9 records (distinct exact-version rows; HOLD; FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md)

## 5. Duplicate and normalization findings

1. **Slice-level overlap:** `units-and-measurement` and `food-systems-basics` appear in both the base register and addenda. Each is counted once in the 99-slice union.
2. **Exact-version duplication:** the base register and Foundations addendum repeat these nine exact `record_id@version` keys in `units-and-measurement`: `SRC-UNITS_AND_MEASUREMENT@1`, `CLM-UNITS_AND_MEASUREMENT-A@1`, `CLM-UNITS_AND_MEASUREMENT-B@1`, `CLM-UNITS_AND_MEASUREMENT-C@1`, `EU-UNITS_AND_MEASUREMENT-A@1`, `EU-UNITS_AND_MEASUREMENT-B@1`, `EU-UNITS_AND_MEASUREMENT-C@1`, `CTX-UNITS_AND_MEASUREMENT@1`, `SCP-UNITS_AND_MEASUREMENT@1`. These are merged once in the 809-row master.
3. **Version lineage, not duplication:** the base register screens the `food-systems-basics` record family at version 1, while R9 screens the same record identities at version 2. Keep v1 as historical screening evidence and v2 as the later candidate version. Deduplication uses the compound key `record_id + record_version`, never record ID alone.
4. **R9 identifier normalization:** the R9 table contains both `SRC-HISTORY_OF_MATHEMATICS-CAMBRIDGE@1` (underscore form, matching the canonical filename) and `SRC-HISTORY_OF-MATHEMATICS-CAMBRIDGE@1` (hyphen form, not canonical). The hyphenated form is malformed and was normalized to the canonical underscore-form identity; the R9 denominator remains 99 canonical records.
5. **Legal/trade/institutional count:** the addendum contains 126 canonical slice-record versions plus three dependent cross-slice relation alignments. The relation rows are not part of the 126-record denominator. The consolidated Part II master now contains 809 unique candidate keys: 621 addendum keys + 197 base-register references − 9 exact duplicate keys.
7. **International-law version drift:** all 13 records in `international-law-basics` were audited as v1, but the current canonical JSON is v2. The v2 Source, Evidence Use, Context and Scope changed; the Claim statements are unchanged but provenance moved. v1 remains historical HOLD; v2 remains HOLD pending review. See `FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md`.
6. **Exact-version closure:** all ten Part II addenda now have exact-version rows. The six formerly summary-only addenda contribute 252 canonical-JSON-verified rows; the four original detailed addenda contribute 369 audit-table rows. After R9 malformed-ID normalization, the addenda contribute 621 unique compound keys.

## 6. Part II slices not yet represented in a candidate register

The following 286 slices are present in the current corpus registry but are not named in the base candidate register or ten addenda. They are **untriaged**, not automatically release candidates:

`accessibility-basics`, `acid-base-basics`, `acoustics-basics`, `ai-ethics-basics`, `air-quality-basics`, `algebra-basics`, `analytical-chemistry-basics`, `ancient-civilizations-basics`, `anthropology-basics`, `archaeology-basics`, `archival-description-basics`, `art-history-basics`, `asset-management-basics`, `astronomy-observation-basics`, `astrophysics-basics`, `atmospheric-chemistry-basics`, `atmospheric-science-basics`, `behavioral-biology-basics`, `behavioral-economics-basics`, `bioinformatics-basics`, `biomedical-engineering-basics`, `biostatistics-basics`, `bridge-engineering-basics`, `building-envelope-basics`, `building-science-basics`, `building-services-engineering-basics`, `calibration-basics`, `causal-inference-basics`, `central-banking-basics`, `chemical-engineering-basics`, `chronology-methods`, `climate-adaptation-basics`, `clinical-trials-basics`, `cloud-computing-basics`, `combinatorics-basics`, `communication-basics`, `competition-policy-basics`, `compiler-basics`, `computer-architecture-basics`, `computer-graphics-basics`, `computing-basics`, `conflict-resolution-basics`, `constitutional-law-basics`, `constitutional-systems-basics`, `construction-project-management-basics`, `construction-safety-basics`, `consumer-protection-basics`, `control-systems-basics`, `corporate-governance-basics`, `critical-thinking-basics`, `cross-slice-linkage`, `cryptography-basics`, `culture-and-language`, `cybersecurity-basics`, `data-ethics-basics`, `data-governance-basics`, `data-science-basics`, `data-visualization-basics`, `database-systems-basics`, `decision-analysis-basics`, `decision-theory-basics`, `demographic-methods-basics`, `development-economics-basics`, `developmental-biology-basics`, `digital-communications-basics`, `digital-identity-basics`, `digital-preservation-basics`, `diplomacy-basics`, `disaster-behavioral-health-basics`, `disaster-financing-basics`, `earth-system-basics`, `econometrics-basics`, `economic-geography-basics`, `economic-history-basics`, `economics-basics`, `education-science-basics`, `electoral-systems-basics`, `electrical-machines-basics`, `electronics-basics`, `embedded-systems-basics`, `energy-efficiency-basics`, `energy-markets-basics`, `energy-policy-basics`, `energy-security-basics`, `engineering-design-basics`, `environmental-biology-basics`, `environmental-economics-basics`, `environmental-engineering-basics`, `environmental-monitoring-basics`, `environmental-policy-basics`, `epigenetics-basics`, `epistemology-basics`, `ergonomics-basics`, `ethics-basics`, `ethnobotany-basics`, `finance-basics`, `financial-literacy-basics`, `financial-markets-basics`, `fire-protection-and-life-safety-basics`, `formal-methods-basics`, `foundation-engineering-basics`, `game-theory-basics`, `genetic-engineering-basics`, `genomics-basics`, `geochemistry-basics`, `geodesy-basics`, `geographic-information-systems-basics`, `geologic-mapping-basics`, `geomorphology-basics`, `geophysics-basics`, `geospatial-analysis-basics`, `geotechnical-engineering-basics`, `graph-theory-basics`, `groundwater-basics`, `health-economics-basics`, `health-systems-basics`, `health-technology-assessment-basics`, `heat-transfer-basics`, `history-methods-basics`, `human-ai-interaction-basics`, `human-computer-interaction-basics`, `human-factors-basics`, `human-rights-basics`, `hydropower-basics`, `indoor-air-quality-basics`, `industrial-engineering-basics`, `industrial-process-safety-basics`, `industrial-safety-basics`, `information-ethics-basics`, `information-literacy-basics`, `information-retrieval-basics`, `information-security-operations-basics`, `information-theory-basics`, `infrastructure-governance-basics`, `inspection-basics`, `insurance-basics`, `intellectual-property-basics`, `international-relations-basics`, `international-trade-basics`, `labor-law-basics`, `labor-markets-basics`, `labor-relations-basics`, `land-use-planning-basics`, `learning-basics`, `legal-research-basics`, `linear-algebra-basics`, `linguistic-typology-basics`, `linguistics-basics`, `logic-basics`, `logistics-basics`, `maintenance-engineering-basics`, `manufacturing-processes-basics`, `market-design-basics`, `matter-basics`, `measurement-instrumentation-basics`, `measurement-science-basics`, `mechanical-engineering-basics`, `media-literacy-basics`, `medical-devices-basics`, `medical-imaging-basics`, `mental-health-information-boundaries`, `metallurgy-basics`, `metaphysics-basics`, `meteorology-basics`, `metrology-basics`, `microbiome-basics`, `mineralogy-basics`, `mining-engineering-basics`, `modeling-and-simulation-basics`, `modeling-basics`, `molecular-biology-basics`, `music-theory-basics`, `negotiation-basics`, `network-analysis-basics`, `neuroscience-basics`, `nuclear-physics-information-basics`, `number-theory-basics`, `numerical-methods-basics`, `occupational-health-basics`, `occupational-safety-basics`, `oceanography-basics`, `open-science-basics`, `operating-systems-basics`, `operations-management-basics`, `operations-research-basics`, `optimization-basics`, `organizational-management-basics`, `paleontology-basics`, `particle-physics-basics`, `payment-systems-basics`, `petrology-basics`, `pharmacology-information-basics`, `pharmacovigilance-basics`, `philosophy-basics`, `philosophy-of-language-basics`, `philosophy-of-mathematics-basics`, `philosophy-of-mind-basics`, `philosophy-of-science-basics`, `physical-chemistry-basics`, `physiology-of-exercise-basics`, `physiology-of-systems-basics`, `planetary-geology-basics`, `planetary-science-basics`, `political-science-basics`, `power-electronics-basics`, `power-systems-basics`, `privacy-and-data-protection-basics`, `probability-basics`, `programming-languages-basics`, `project-management-basics`, `psychology-basics`, `public-data-basics`, `public-finance-basics`, `public-health-ethics-basics`, `public-health-surveillance-basics`, `public-policy-basics`, `public-procurement-basics`, `public-works-basics`, `quality-control-basics`, `quality-management-basics`, `quantum-mechanics-basics`, `quantum-physics-basics`, `queueing-theory-basics`, `railway-systems-basics`, `ratios-and-percentages`, `records-management-basics`, `rehabilitation-basics`, `reliability-basics`, `reliability-engineering-basics`, `reproductive-health-information-boundaries`, `requirements-engineering-basics`, `research-data-management-basics`, `research-design-basics`, `research-integrity-basics`, `research-methods-basics`, `resource-allocation-basics`, `risk-analysis-basics`, `risk-management-basics`, `robotics-engineering-basics`, `safety-engineering-basics`, `sampling-basics`, `science-policy-basics`, `scientific-communication-basics`, `scientific-method-basics`, `scientific-publishing-basics`, `scientific-reproducibility-basics`, `seasons-and-orbits`, `semiconductor-basics`, `sensor-systems-basics`, `signal-processing-basics`, `social-insurance-basics`, `social-protection-basics`, `software-architecture-basics`, `software-testing-basics`, `source-provenance-authorship-trust`, `standards-and-certification-basics`, `state-formation`, `statistics-inference-basics`, `structural-engineering-basics`, `supply-and-demand-infrastructure-basics`, `supply-chain-basics`, `supply-chain-risk-basics`, `surveying-basics`, `sustainable-development-basics`, `systems-biology-basics`, `systems-engineering-basics`, `systems-modeling-basics`, `systems-thinking-basics`, `telemedicine-basics`, `timber-engineering-basics`, `time-standard-basics`, `toxicology-basics`, `traceability-systems-basics`, `trade-networks`, `transportation-infrastructure-basics`, `trigonometry-basics`, `urban-economics-basics`, `urban-planning-basics`, `urbanization`, `version-control-basics`, `waste-infrastructure-basics`, `wastewater-treatment-basics`, `water-governance-basics`, `water-resources-management-basics`, `web-systems-basics`, `writing-systems`

## 7. CI authorization issue discovered and corrected

At the pre-fix HEAD `00f5e8ec681e76156a9cf7c9abe474b5d9d34444`, Reference Tests, Release Conformance Gate and Offline Edition all failed at Content preflight with the same finding: `food-systems-basics` was modified without explicit editorial correction authorization.

Inspection established that the bounded authorization `R9-FOOD-SYSTEMS-REMEDIATION-001` already existed in `RELEASE/EDITORIAL-CORRECTION.json` and explicitly scoped the authorized changes to `food-systems-basics`, but the slug was missing from the top-level `authorized_slices` list consumed by `REFERENCE/preflight_content.py`.

Corrective action: added only `food-systems-basics` to the sorted top-level `authorized_slices` list. No authorization scope, allowed/prohibited changes, canonical content, publication state or decision was broadened.  
Fix commit: `2f853c454344a20b3cbbf2bc6ca09ad0b6c02986`.

The fix must be validated by new exact-head CI on the resulting branch HEAD. No PASS is claimed here.

## 8. Next bounded actions

1. Re-read the 197 `base_register_reference` rows from canonical JSON at one frozen HEAD; confirm `record_id`, `record_version`, type and current-version status. The 252 newly expanded rows have canonical JSON snapshots; the 356 detailed audit rows matched canonical JSON across the pinned verification batches, but must be rechecked at one final HEAD before release.
2. Re-review the 13 current `international-law-basics@2` records as one coherent dependency unit. Their v1 audit versions are historical HOLD; v2 is HOLD pending review of the changed source, provenance, Evidence Use content, Context and Scope.
3. Validate dependency closure across the 822 master keys: Claim → exact Evidence Use → exact Source, plus Context/Scope targets and applicability. Keep Relations in a separate ledger.
4. Normalize the base/R9 `food-systems-basics` version lineage: preserve base v1 as historical and R9 v2 as the later candidate; resolve the base register's abbreviated EU-B/EU-C references without inventing tokens.
5. After exact versions and dependencies are stable, triage the 286-slice unregistered pool against the controlling first-edition architecture and choose the next bounded domain group. Do not launch a blanket sweep.
6. Re-check release gates on the content-bearing post-authorization commit. Offline Edition and Browser Tests passed there; Reference Tests and Release Conformance Gate were cancelled by later branch updates and are being rerun. Do not claim final exact-HEAD PASS until all gates complete.

## 9. Sources used

- `CONTENT/README.md`
- `RELEASE/FIRST-EDITION-PART-I-SURVIVAL-FULL-SLICE-INVENTORY-2026-11-18.md`
- `RELEASE/FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md`
- `RELEASE/FIRST-EDITION-PART-II-EXACT-VERSION-MASTER-REGISTER-2026-11-19.md`
- `RELEASE/FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-OPENING-SURVIVAL-AND-DOMAIN-MAP-2026-11-18.md`
- All ten Part II addenda listed in §4
- `RELEASE/EDITORIAL-CORRECTION.json`
- `REFERENCE/preflight_content.py`
