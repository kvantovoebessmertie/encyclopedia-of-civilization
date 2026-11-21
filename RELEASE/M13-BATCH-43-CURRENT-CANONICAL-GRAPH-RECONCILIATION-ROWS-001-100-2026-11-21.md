# M13 Batch 43 — current canonical graph reconciliation, rows 001–100

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Inspected tree: `4fb1791a9b79569672ddb3bd6af72a85ffa3b2e1`  
Scope: all 100 Batch 43 report headers and the corresponding current canonical Claim, Evidence Use and Source records.  
Method: resolved record paths from the branch's recursive Git tree; fetched and read each current Claim and its historical-header Evidence Use; fetched each distinct primary Source; compared IDs, `record_version`, Claim provenance, EU `claim_ref` and `source_ref`; preserved multi-EU and multi-Source links as separate evidence edges.  
Mutation boundary: **read-only reconciliation. No canonical records changed.**

## 1. Executive result

**100/100 Batch 43 report rows have an exact current canonical primary Claim/Evidence Use/Source ID-and-version chain matching the historical report header.**

- 100/100 current Claim records exist at the report's Claim ID and version.
- 100/100 primary Evidence Use records exist at the report's Evidence Use ID and version.
- 100/100 primary Source records exist at the report's Source ID and version.
- All inspected primary EU records point to the matching Claim and Source at the versions named in their canonical records.
- All inspected Claim provenance references point to the same primary Source ID/version as the current chain.
- No missing primary record, primary ID mismatch, primary version mismatch, Claim↔EU mismatch or EU↔Source mismatch was observed in this 100-row cohort.

This is a graph identity result, **not** a finding that every Claim is well evidenced. The current EU records often use broad summaries and generic “supports” descriptions without a reproducible passage locator. Historical D/E/B scores were not accepted or transferred.

## 2. Version and graph exceptions preserved

### 2.1 Hydrology row 098 — verified exact version 2 chain

Row 098 is an exact **Claim@2 → EU@2 → Source@2** match. The current canonical records preserve:
- USGS Water Science School, “What is Hydrology?”;
- section “What is Hydrology?”;
- paragraph beginning “There are many pathways the water may take”;
- a concise description of runoff/river flow, infiltration, evaporation, transpiration and groundwater storage;
- an explicit non-exhaustive boundary.

This is the one clear current EU passage-level pinpoint verified in this 100-row graph pass. It matches the historical row's D/E/B 3/3/2 report assessment, but that historical score remains unaccepted until the required current assessment/review process is completed. OpenStax/USGS rights and attribution checks remain separate.

### 2.2 Multiple-EU and multi-Source cases

The following current graph structures were preserved rather than flattened into a single source edge:

- **Row 032 — health-system resilience:** the historical chain lists two EU records (EU-CLM-M4-HEALTH-RESILIENCE-A@1 and EU-M4-HEALTH-RESILIENCE-WHO@2) pointing to the same Claim@1 and WHO Source@1. Both current EU records exist and their links agree. The @2 EU explicitly states that the exact passage-level pinpoint still needs to be recorded.
- **Row 034 — manufacturing operations:** the primary NIST EU/Source@1 chain matches; a second current UNIDO EU/Source@1 edge also links to the same Claim@1. The UNIDO edge is complementary, not a replacement for NIST.
- **Rows 038–040 — mental-health information:** each primary WHO EU/Source@1 chain matches. Additional NIMH EU/Source@1 records are present for the related claims; they are separate corroborating edges, not a rewrite of the historical WHO chain.
- **Rows 054–055 — risk communication:** the primary UNDRR EU/Source@1 chains match. Additional CDC EU/Source@1 records are present for the related claims. These supplementary edges do not automatically prove every listed clause or remove the need for passage locators.
- **Rows 064–066 — systems thinking:** primary CDC EU/Source@1 chains match; additional WHO-linked EU records are present for the related claims. Preserve the separate source roles and do not collapse them into one generic “reviewed” flag.
- **Row 068 — wastewater:** the primary EPA EU/Source@1 chain matches; a separate WHO EU/Source@1 edge also exists for the same Claim.
- **Row 081 — food temperature:** the historical primary USDA FSIS EU/Source@1 chain matches, but the USDA outage page does not establish the 40°F/0°F target temperatures. A separate FDA EU/Source@1 edge exists, but its linked FDA page (`Power Outages: Key Tips for Consumers About Food Safety`) directly states the refrigerator 40°F threshold and the four-hour outage interval, not the freezer 0°F target. A different FDA page (`Food and Water Safety During Power Outages and Floods`) directly states freezer ≤0°F and refrigerator ≤40°F under “Prepare Yourself Before Power Emergencies”; that page is not the current canonical FDA Source URI. The current FDA EU therefore does not close the freezer-threshold gap. A separately authorized Source/EU edge to the exact FDA page is required before reconsideration.
- **Row 083 — wastewater requirements:** the primary EPA EU/Source@1 chain matches; a separate WHO EU/Source@1 edge also exists. The EPA source does not, by itself, establish the full local-regulatory-variation clause.
- **Row 098 — hydrology:** exact version 2 chain as detailed above.

These extra edges are current graph facts. They do not change the historical report header's primary chain and do not themselves prove source-passage review.

## 3. Row-level current graph status

All 100 rows in the Batch 43 supplementary report have status **EXACT_PRIMARY_CHAIN** at the current branch revision. The row-to-Claim mapping is preserved in that report's 100-row table; the primary Evidence Use and Source IDs are the exact IDs declared in each corresponding historical report header and verified against current canonical records.

| Batch 43 rows | Current primary Claim/EU/Source ID+version match | Primary cross-links | Current passage-level EU locator accepted in this pass |
|---|---:|---:|---:|
| 001–008 | 8/8 | 8/8 | 0 |
| 009–016 | 8/8 | 8/8 | 0 |
| 017–024 | 8/8 | 8/8 | 0 |
| 025–032 | 8/8 | 8/8 | 0 |
| 033–040 | 8/8 | 8/8 | 0 |
| 041–048 | 8/8 | 8/8 | 0 |
| 049–056 | 8/8 | 8/8 | 0 |
| 057–064 | 8/8 | 8/8 | 0 |
| 065–072 | 8/8 | 8/8 | 0 |
| 073–080 | 8/8 | 8/8 | 0 |
| 081–088 | 8/8 | 8/8 | 0 |
| 089–096 | 8/8 | 8/8 | 0 |
| 097–100 | 4/4 | 4/4 | 1 (row 098) |
| **Total** | **100/100** | **100/100** | **1/100** |

“0” means no passage-level locator was accepted in the current EU record for that row during this pass. A report's narrative may describe a source passage, and a source URI may point to a relevant page, but neither substitutes for a reproducible canonical EU locator.

## 4. Material source-fit findings that survive exact graph matching

Exact IDs and versions do not cure these defects:

1. **Rows 006 and 008 — access/source verification:** Ready.gov/FEMA and EPA pages were unavailable to the report reviewer; no substitute source may be silently substituted for the canonical Source.
2. **Row 012 — WHO drinking-water quality:** the historical report quotes an older URL path that omits `water-safety-and-quality`; that quoted URL returns 404. The current canonical Source record uses the valid `.../water-safety-and-quality/drinking-water-quality-guidelines` URI. Git path history shows one introduction commit (`9c1df38dcab8ff76e5103799cd1f360536530444`, 2026-10-05); fetching the Source at that commit and at the current branch returns the same URI and `record_version=1`. No unversioned Source mutation was observed. The discrepancy is therefore a report-to-record URI transcription/staleness issue, not a demonstrated Source version-history defect. The EU remains generic and still needs a precise WHO passage locator.
3. **Rows 015, 023, 025, 028, 037, 040 and 076:** reports identified more directly matched authoritative material outside the primary canonical source chain. Current graph identity is not a substitute for adding or formally adjudicating those evidence edges.
4. **Rows 057 and 096–097:** the current source identity is related to the topic but does not fully establish the Claim's complete proposition. A new direct source may be needed.
5. **Rows 077–079:** broad WHO digital-health programme page is not a direct telemedicine definition or support for the complete service/quality factor lists.
6. **Row 081:** primary USDA source does not establish the temperature thresholds; the current FDA secondary EU is a remediation candidate, not automatic clearance.
7. **Row 082:** USDA/NRCS source identity and URL pairing still needs direct verification; the separate University of Minnesota extension Source exists in the corpus, but no substitution is assumed.
8. **Row 083:** EPA fundamentals page does not establish the full local regulatory variation clause; separate WHO link does not establish jurisdiction-specific requirements.
9. **Rows 087–089 and 096–097:** broad source pages or chapter-level links need exact subpage/section passages for the full Claim scope.
10. **Editorial text:** rows 007 and 045–047 still contain slice-name parenthetical artifacts in Claim wording. Exact graph matching is not authorization to edit the canonical Claims.

## 5. Batch 42–43 graph reconciliation accounting

The report-body inspection sweep is complete at 200/200 reports. Current canonical graph comparison now covers:
- Batch 42 rows 069–100: 32/32 exact primary chains (separate report).
- Batch 43 rows 001–100: 100/100 exact primary chains (this report).

Combined current graph comparison: **132/200 report rows**, all exact primary ID/version matches in the compared subset. The remaining current graph comparisons are Batch 42 rows 001–068: **68 report rows**. Do not treat 132 report-row occurrences as 132 unique normalized Claim IDs until the master crosswalk deduplicates them and adjudicates duplicate groups.

## 6. Assessment and release boundary

- Historical Batch 43 D/E/B distribution remains D1=5/D2=29/D3=66; E1=26/E2=67/E3=7; B1=6/B2=61/B3=33.
- Current accepted D/E/B from this graph pass: **0**.
- Current Human View/independent/specialist review completed by this pass: **0**.
- Current formal risk assessments or release clearances created by this pass: **0**.
- Current worksheet statuses remain unchanged; no historical score was transferred.
- No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record changed.
- No queue exclusions or priorities changed.

## 7. Next work

1. Complete current canonical graph reconciliation for Batch 42 rows 001–068.
2. Rerun the master 200-report normalized-ID/version join, including multiple-EU and multiple-Source edges, and adjudicate duplicates without automatic score selection.
3. Investigate the row 012 WHO Source version-history question and preserve immutable version semantics.
4. Directly verify the FDA secondary source for row 081 and the other supplementary evidence edges; do not silently replace primary canonical sources.
5. Only after graph reconciliation, proceed to current passage verification, evidence diversity, risk screening, specialist review, independent Human View, rights/editorial review and release gates.
