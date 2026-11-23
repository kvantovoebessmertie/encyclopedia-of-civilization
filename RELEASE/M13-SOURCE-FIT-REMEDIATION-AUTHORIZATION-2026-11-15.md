# M13 bounded remediation authorization — Packages 29–31 source-fit follow-up

Date: 2026-11-15
Authorization ID: M13-SOURCE-FIT-REMEDIATION-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `7b680dec27ec3b25cd45779b7f0988141ee558ac`
Status: AUTHORIZED FOR THE EXACT RECORDS AND FILES LISTED BELOW

## 1. Purpose and limits

The project owner has directed that all known M13 defects be consolidated and corrected before final verification. This authorization covers only bounded source-fit corrections arising from Packages 29–31 and the exact records listed here. It does not close M13, assign D/E/B scores, clear publication or rights holds, or authorize a merge.

All new Evidence Use records are claim-specific and must describe the precise proposition supported and the limits of that support. Do not use an institutional landing page as a substitute for a technical source. Do not turn US-specific mapping practice into a global rule. Do not claim that measurement-system repeatability proves repeatability of manufactured output.

## 2. Exact authorized new Source records

Create each as record_version "1", type_version "1.0", record_type "source", publication_status "published", completion_status "complete", schema "record/0.1", with exact ID and URL:

1. `CONTENT/vertical-slices/maps-and-navigation-basics/records/SRC-USGS-US-TOPO-ACCURACY.json`
   - ID: `SRC-USGS-US-TOPO-ACCURACY`
   - Identity: U.S. Geological Survey — How accurate are US Topo maps, and why don't they have an accuracy statement?
   - URI: https://www.usgs.gov/faqs/how-accurate-are-us-topo-maps-and-why-dont-they-have-accuracy-statement
   - Rights note: USGS public-domain page; inspect page-level third-party notices and use only USGS-authored factual text.

2. `CONTENT/vertical-slices/maps-and-navigation-basics/records/SRC-USGS-US-TOPO-CURRENCY.json`
   - ID: `SRC-USGS-US-TOPO-CURRENCY`
   - Identity: U.S. Geological Survey — How current are US Topo maps?
   - URI: https://www.usgs.gov/faqs/how-current-are-us-topo-maps
   - Rights note: USGS public-domain page; use the U.S. production-cycle statement only as a U.S.-specific example, with current variation caveat.

3. `CONTENT/vertical-slices/materials-basics/records/SRC-NIST-MATERIALS-SCIENCE-ENGINEERING-DIVISION.json`
   - ID: `SRC-NIST-MATERIALS-SCIENCE-ENGINEERING-DIVISION`
   - Identity: NIST — Materials Science and Engineering Division
   - URI: https://www.nist.gov/mml/materials-science-and-engineering-division
   - Rights note: NIST public information except material explicitly marked copyrighted; attribute NIST and inspect the page for third-party exceptions.

4. `CONTENT/vertical-slices/materials-basics/records/SRC-NIST-MECHANICAL-PERFORMANCE-GROUP.json`
   - ID: `SRC-NIST-MECHANICAL-PERFORMANCE-GROUP`
   - Identity: NIST — Mechanical Performance Group
   - URI: https://www.nist.gov/mml/materials-science-and-engineering-division/mechanical-performance-group
   - Rights note: NIST public information except material explicitly marked copyrighted; attribute NIST and inspect the page for third-party exceptions.

5. `CONTENT/vertical-slices/materials-science-basics/records/SRC-NIST-MECHANICAL-PERFORMANCE.json`
   - ID: `SRC-NIST-MECHANICAL-PERFORMANCE`
   - Identity: NIST — Mechanical Performance Group
   - URI: https://www.nist.gov/mml/materials-science-and-engineering-division/mechanical-performance-group
   - Rights note: NIST public information except material explicitly marked copyrighted; attribute NIST and inspect the page for third-party exceptions.

6. `CONTENT/vertical-slices/manufacturing-systems-basics/records/SRC-NIST-SMART-MANUFACTURING-TEST-BED.json`
   - ID: `SRC-NIST-SMART-MANUFACTURING-TEST-BED`
   - Identity: NIST — Smart Manufacturing Systems Test Bed
   - URI: https://www.nist.gov/laboratories/tools-instruments/smart-manufacturing-systems-sms-test-bed
   - Rights note: NIST public information except material explicitly marked copyrighted; attribute NIST and inspect the page for third-party exceptions.

7. `CONTENT/vertical-slices/manufacturing-systems-basics/records/SRC-NIST-AMS-200-2.json`
   - ID: `SRC-NIST-AMS-200-2`
   - Identity: NIST — Connecting, Deploying, and Using the Smart Manufacturing Systems Test Bed (AMS 200-2)
   - URI: https://www.nist.gov/publications/connecting-deploying-and-using-smart-manufacturing-systems-test-bed
   - Rights note: NIST Technical Series policy permits worldwide reuse/derivatives to the extent NIST may assert foreign rights for NIST-employee-authored works; verify the report's author and copyright page before relying on full-text reuse. The canonical evidence description must paraphrase and pinpoint, not reproduce passages.

## 3. Exact authorized new Evidence Use records

Create each as record_version "1", type_version "1.0", record_type "evidence_use", publication_status "published", completion_status "complete", schema "record/0.1", evidence_role "supports", with claim_ref version "1" and source_ref version "1":

- `CONTENT/vertical-slices/maps-and-navigation-basics/records/EU-MAPS_AND_NAVIGATION_BASICS-C-US-TOPO-ACCURACY.json`
  - ID: `EU-MAPS_AND_NAVIGATION_BASICS-C-US-TOPO-ACCURACY`
  - Claim: `CLM-MAPS_AND_NAVIGATION_BASICS-C@1`
  - Source: `SRC-USGS-US-TOPO-ACCURACY@1`
  - Limit: accuracy varies with the underlying datasets; no single map-wide accuracy statement; metadata is layer/source-specific; USGS maps are general reference and not authoritative/official for navigation.

- `CONTENT/vertical-slices/maps-and-navigation-basics/records/EU-MAPS_AND_NAVIGATION_BASICS-C-US-TOPO-CURRENCY.json`
  - ID: `EU-MAPS_AND_NAVIGATION_BASICS-C-US-TOPO-CURRENCY`
  - Claim: `CLM-MAPS_AND_NAVIGATION_BASICS-C@1`
  - Source: `SRC-USGS-US-TOPO-CURRENCY@1`
  - Limit: the three-year production cycle is a historical/current U.S. US Topo programme description, not a universal or guaranteed age for every layer; preserve the source's variation caveat.

- `CONTENT/vertical-slices/materials-basics/records/EU-MATERIALS_BASICS-A-NIST-MSED.json`
  - ID: `EU-MATERIALS_BASICS-A-NIST-MSED`
  - Claim: `CLM-MATERIALS_BASICS-A@1`
  - Source: `SRC-NIST-MATERIALS-SCIENCE-ENGINEERING-DIVISION@1`
  - Limit: support only the NIST division's stated work on measurement methods, models, data, standards and structure/property/processing relationships; do not claim exhaustive definition of the entire discipline.

- `CONTENT/vertical-slices/materials-basics/records/EU-MATERIALS_BASICS-C-NIST-MECHANICAL-PERFORMANCE.json`
  - ID: `EU-MATERIALS_BASICS-C-NIST-MECHANICAL-PERFORMANCE`
  - Claim: `CLM-MATERIALS_BASICS-C@1`
  - Source: `SRC-NIST-MECHANICAL-PERFORMANCE-GROUP@1`
  - Limit: supports mechanical properties under extreme environmental/operating conditions and performance within/outside design limits; do not imply this single page fully establishes every composition/structure/processing pathway.

- `CONTENT/vertical-slices/materials-science-basics/records/EU-M5-MATERIALS-SCIENCE-NIST-B.json`
  - ID: `EU-M5-MATERIALS-SCIENCE-NIST-B`
  - Claim: `CLM-MATERIALS_SCIENCE_BASICS-B@1`
  - Source: `SRC-NIST-MECHANICAL-PERFORMANCE@1`
  - Limit: NIST explicitly names composites alongside steel and aluminum alloys as examples of advanced materials. This supplements, but does not replace, NSF's separate listing of metals, ceramics, polymers and semiconductors.

- `CONTENT/vertical-slices/materials-science-basics/records/EU-M5-MATERIALS-PERFORMANCE-NIST-D.json`
  - ID: `EU-M5-MATERIALS-PERFORMANCE-NIST-D`
  - Claim: `CLM-M5-MATERIALS-PERFORMANCE-D@1`
  - Source: `SRC-NIST-MECHANICAL-PERFORMANCE@1`
  - Limit: supports mechanical property data, extreme environmental/operating conditions, performance within/outside design limits and forensic failure analysis. It does not fully establish a general application-specific material-selection framework; Claim remains PARTIAL/HOLD.

- `CONTENT/vertical-slices/manufacturing-systems-basics/records/EU-MANUFACTURING_SYSTEMS_BASICS-B-SMS.json`
  - ID: `EU-MANUFACTURING_SYSTEMS_BASICS-B-SMS`
  - Claim: `CLM-MANUFACTURING_SYSTEMS_BASICS-B@1`
  - Source: `SRC-NIST-SMART-MANUFACTURING-TEST-BED@1`
  - Limit: supports integrated fabrication/inspection equipment, MTConnect data collection, digital-thread information flow, first-pass success and overall production-process performance. It does NOT directly prove that measurement and process control universally increase manufactured-output reproducibility. Keep the Claim PARTIAL unless separately evidenced.

- `CONTENT/vertical-slices/manufacturing-systems-basics/records/EU-MANUFACTURING_SYSTEMS_BASICS-C-SMS.json`
  - ID: `EU-MANUFACTURING_SYSTEMS_BASICS-C-SMS`
  - Claim: `CLM-MANUFACTURING_SYSTEMS_BASICS-C@1`
  - Source: `SRC-NIST-SMART-MANUFACTURING-TEST-BED@1`
  - Limit: supports information flow and integration across design, fabrication and inspection, including quality and equipment performance/health; describe it as a NIST test-bed example, not a universal production architecture.

- `CONTENT/vertical-slices/manufacturing-systems-basics/records/EU-MANUFACTURING_SYSTEMS_BASICS-C-AMS-200-2.json`
  - ID: `EU-MANUFACTURING_SYSTEMS_BASICS-C-AMS-200-2`
  - Claim: `CLM-MANUFACTURING_SYSTEMS_BASICS-C@1`
  - Source: `SRC-NIST-AMS-200-2@1`
  - Limit: supports integration of MTConnect and other standards/technologies to collect, curate and reuse shop-floor manufacturing data to improve production-system performance. Preserve the NIST employee authorship/rights caveat and do not quote extended text.

## 4. Exact authorized existing-record correction

- Path: `CONTENT/vertical-slices/materials-science-basics/records/EU-M5-MATERIALS-SCIENCE-NSF-B.json`
- ID: `EU-M5-MATERIALS-SCIENCE-NSF-B`
- Version 1 → 2.
- Change only `record_version`, `provenance.created_from[0].record_id` only if required by the registered provenance standard and in that case set it to `SRC-M5-MATERIALS-SCIENCE-NSF@1` (preserve version 1), and `content.material.description`.
- Correct description: NSF's Materials Research page names metals, ceramics, polymers and semiconductors; it does not explicitly name composites. The composite example is separately supported by the NIST Mechanical Performance Group Evidence Use.
- Preserve claim_ref, source_ref, evidence_role, record ID, type/schema/status and all other fields. Do not claim NSF supports composites.

## 5. Exact documentation, regression and registry files

Only these supporting files may be changed for this authorization:
- `CONTENT/vertical-slices/maps-and-navigation-basics/README.md`
- `CONTENT/vertical-slices/materials-basics/README.md`
- `CONTENT/vertical-slices/materials-science-basics/README.md`
- `CONTENT/vertical-slices/manufacturing-systems-basics/README.md`
- `REFERENCE/tests/test_m13_evidence_linkage_audit.py`
- `REFERENCE/tests/test_content_maps_and_navigation_basics_vertical_slice.py`
- `REFERENCE/tests/test_content_materials_basics_vertical_slice.py`
- `REFERENCE/tests/test_content_materials_science_basics_vertical_slice.py`
- `REFERENCE/tests/test_content_manufacturing_systems_basics_vertical_slice.py`
- `RELEASE/CONTENT-COVERAGE.json` — only record-type totals and total_records, calculated from the actual post-write tree; do not alter slice count or unrelated coverage statements.
- `RELEASE/EDITORIAL-CORRECTION.json` — add one authorization entry with this ID and exact scope.
- `RELEASE/M13-SOURCE-FIT-REMEDIATION-CHECKPOINT-2026-11-15.md` — record exact changes, limitations and checks.

## 6. Required regression assertions

- Every new Source and Evidence Use resolves by exact record ID and version.
- Each new Evidence Use claim_ref and source_ref resolve to the exact version-1 records named above; evidence_role is supports.
- The NSF Evidence Use v2 no longer attributes composites to NSF.
- The separate NIST Evidence Use explicitly supports composites.
- USGS accuracy and currency Evidence Uses retain the non-authoritative-for-navigation caveat and U.S.-only scope of the production cycle.
- Manufacturing B test explicitly preserves its PARTIAL limitation; manufacturing C test checks the two distinct NIST source links.
- Materials Performance D remains PARTIAL/HOLD; no test may assert that the full application-specific selection framework is established.
- All original Claims, existing Source records other than no change, Context, Scope, Relations, D/E/B ledgers and risk metadata remain unchanged.
- No duplicate record IDs or path collisions.

## 7. Mandatory verification and exclusions

Run JSON/schema/content preflight, all four dedicated slice regressions, M13 evidence-linkage audit, Reference Tests, Release Conformance Gate and Offline Edition on the same exact final HEAD. Independently inspect the final diff and the post-write tree. Update coverage totals only from actual files.

No Claim wording/version changes, no new Claim, no Relation, no Context/Scope, no D/E/B assignment, no rights clearance for ISO 31000, no use of Orange Book Annex 5's ISO-derived definition, no use of copyrighted National Academies Press material, no publication/release approval, no main changes, no PR merge. PR #21 remains Draft and unmerged. M13 remains OPEN / NOT RELEASE-READY.
