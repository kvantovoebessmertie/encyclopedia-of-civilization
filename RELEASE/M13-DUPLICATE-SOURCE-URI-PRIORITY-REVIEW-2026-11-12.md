# M13 — priority duplicate-Source-URI adjudication review

Date: 2026-11-12
Basis: 33 duplicate-URI groups / 77 Source rows from the full-inventory evidence-linkage audit.
Scope: eight duplicate-URI groups with health, water, electricity, wastewater, infrastructure or other high-consequence relevance. This is a source-identity review, not a source deletion/merge, source-independence certification or Claim acceptance decision.

## 1. Rule

A shared external URI is a reconciliation signal only. It does not automatically prove:
- that two Source records are the same source edition or content revision;
- that one record is redundant or safe to delete;
- that two different Source IDs represent independent corroboration.

The inspected Source records are all record_version 1 and preserve only a title/identity, representation, external URI, availability and preservation note. They do not preserve an archived page snapshot, external publication date or content hash. Therefore the groups below are classified as duplicate-URI candidates, with identity confidence noted, not automatically merged.

## 2. High-consequence duplicate-URI groups

### Group A — EPA Emergency Disinfection of Drinking Water

<badge>3 Source records · one canonical URL</badge>

URI: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water

Source IDs:
- `SRC-EPA-EMERGENCY-DISINFECTION-WATER` — “U.S. EPA — Emergency Disinfection of Drinking Water”
- `SRC-EPA-EMERGENCY-WATER-2026` — “US EPA — Emergency Disinfection of Drinking Water”
- `SRC-EPA-WATER-TREATMENT-2026` — “US EPA — Emergency Disinfection of Drinking Water”

All three records have the same URL and version 1; two title strings differ only by “U.S.” versus “US”. Strong duplicate-source candidate. Do not treat the three IDs as three independent sources.

Linked Claims:
- `CLM-CHEM-WATER-NO-BOIL` — `EU-CHEM-WATER-NO-BOIL-EPA` uses the first Source ID.
- `CLM-WATER-INDEPENDENT-CORROBORATION` — `EU-WATER-INDEPENDENT-CORROBORATION` uses the second Source ID.
- `CLM-M5-WATER-EMERGENCY-DISINFECTION-D` — `EU-M5-WATER-EMERGENCY-DISINFECTION-D` uses the third Source ID.
- `CLM-WATER_TREATMENT_BASICS-B` — `EU-EPA-WATER-TREATMENT-B` uses the third Source ID.

Passage check: the current EPA page explicitly distinguishes microbial disinfection from contaminants such as heavy metals, salts and most other chemicals; it also gives boiling and disinfection instructions. The page itself cites WHO (2015) for the pathogen-kill statement. It is one EPA page, not three independent corroborating publications.

Specific finding: the Evidence Use description for `CLM-WATER-INDEPENDENT-CORROBORATION` says “EPA independently confirms”, but the Claim has one linked Evidence Use/Source record, pointing to this EPA page. The word “independently” is not established by a second independent Source in that Claim's stored chain. Reword or add an actually independent source only under bounded editorial authorization.

Disposition: likely duplicate Source records; preserve all three IDs until source-owner/editorial adjudication. For evidence-independence assessment, count this URL as one source, not three.

### Group B — CDC emergency water safety page

<badge>2 Source records · one canonical URL</badge>

URI: https://www.cdc.gov/water-emergency/about/index.html

Source IDs:
- `SRC-CDC-WATER-EMERGENCY-2024` — “CDC — How to Make Water Safe in an Emergency”
- `SRC-CDC-WATER-FILTER-2025` — “CDC — How to Make Water Safe in an Emergency”

Exact title and URL match; both version 1. Strong duplicate-source candidate.

Linked Claims:
- `CLM-WATER-BOILING-EFFECTIVE`
- `CLM-WATER-BOILING-TIME`
- `CLM-WATER-CHEMICAL-LIMIT`
- `CLM-WATER-FILTER-LIMITS`

Disposition: likely one CDC page represented twice. Confirm whether the 2024/2025 suffixes were intended to represent distinct archived page states; if not, propose a single canonical Source record and preserve historical IDs through explicit alias/redirect metadata rather than deleting records.

### Group C — CDC emergency water storage page

<badge>2 Source records · one canonical URL</badge>

URI: https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html

Source IDs:
- `SRC-CDC-WATER-STORAGE-2025` — “CDC — How to Create an Emergency Water Supply”
- `SRC-CDC-WATER-STORAGE-ATTRIBUTION-2025` — “CDC — About Creating and Storing an Emergency Water Supply”

Exact URL, version 1; title strings are near-identical descriptions of the same CDC page.

Linked Claims:
- `CLM-WATER-STORAGE-CONTAINER`
- `CLM-CDC-FOOD-GRADE-CONTAINER`

Disposition: strong duplicate-source candidate. Preserve distinct Claim/Evidence Use records; source deduplication must not collapse distinct claim-specific locators or material descriptions.

### Group D — CDC/NIOSH electrical safety page

<badge>2 Source records · one canonical URL</badge>

URI: https://cdc.gov/niosh/electrical-safety/about/

Source IDs:
- `SRC-ELECTRICAL_SAFETY_BASICS` — “Электробезопасность: CDC/NIOSH”
- `SRC_ELECTRICAL_SAFETY_NIOSH` — “CDC/NIOSH — Electrical Safety”

Same URL and version 1; the title difference is language/wording, not evidence of separate publications.

Linked Claims:
- `CLM-ELECTRICAL_SAFETY_BASICS-A`
- `CLM-ELECTRICAL_SAFETY_BASICS-B`
- `CLM-ELECTRICAL_SAFETY_BASICS-C`
- `CLM_ELECTRICAL_SAFETY_NIOSH_A`

Disposition: strong duplicate-source candidate. Count as one source for independence. Electrical-safety Claims remain subject to qualified safety review and exact passage locators.

### Group E — EPA Municipal Wastewater page

<badge>2 Source records · one canonical URL</badge>

URI: https://www.epa.gov/npdes/municipal-wastewater

Source IDs:
- `SRC-WASTEWATER_ENGINEERING_BASICS` — “U.S. Environmental Protection Agency — Municipal Wastewater”
- `SRC-WASTEWATER_TREATMENT_BASICS` — “U.S. EPA — Municipal Wastewater”

Same URL and version 1; title strings are equivalent.

Linked Claims:
- `CLM_WASTEWATER_ENGINEERING_BASICS_A`
- `CLM_WASTEWATER_ENGINEERING_BASICS_B`
- `CLM_WASTEWATER_ENGINEERING_BASICS_C`
- `CLM-WASTEWATER_TREATMENT_BASICS-A`
- `CLM-WASTEWATER_TREATMENT_BASICS-B`
- `CLM-WASTEWATER_TREATMENT_BASICS-C`

Disposition: likely same EPA page reused for two thematic slices. Reuse is appropriate if the relevant passages support each Claim, but the two Source IDs must not be counted as independent evidence.

### Group F — USGS Water Resources Mission Area page

<badge>2 Source records · one canonical URL</badge>

URI: https://www.usgs.gov/mission-areas/water-resources

Source IDs:
- `SRC-WATER_RESOURCES_BASICS` — “USGS Water Resources Mission Area”
- `SRC-WATER_RESOURCES_MANAGEMENT_BASICS` — “U.S. Geological Survey — Water Resources Mission Area”

Same URL and version 1; title strings are equivalent.

Linked Claims:
- `CLM_WATER_RESOURCES_BASICS_A`
- `CLM_WATER_RESOURCES_BASICS_B`
- `CLM_WATER_RESOURCES_BASICS_C`
- `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-A`
- `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-B`
- `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-C`

Disposition: likely same USGS overview page reused across adjacent slices. It may be a useful general Source, but exact section-level support for each Claim is still required. Count as one Source for independence.

### Group G — FEMA Infrastructure Dependency Primer

<badge>2 Source records · one canonical URL</badge>

URI: https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/infrastructure-dependency

Source IDs:
- `SRC-M4-INFRASTRUCTURE-DEPENDENCY-FEMA`
- `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025`

Both have identical source identity (“FEMA — Infrastructure Dependency Primer”), identical URL and version 1.

Linked Claims:
- `CLM-INFRASTRUCTURE_BASICS-C`
- `CLM-M4-INFRASTRUCTURE-DEPENDENCY-A`
- `CLM-INFRASTRUCTURE_RESILIENCE-A`
- `CLM-INFRASTRUCTURE_RESILIENCE-B`
- `CLM-INFRASTRUCTURE_RESILIENCE-C`
- `CLM-INFRASTRUCTURE_RESILIENCE-D`

Disposition: very strong duplicate-record candidate. Retain one canonical source identity after editorial approval; preserve the other record ID as an explicit alias if required for stable references.

### Group H — WHO Sexual and Reproductive Health and Rights page

<badge>2 Source records · one canonical URL</badge>

URI: https://www.who.int/health-topics/sexual-and-reproductive-health-and-rights

Source IDs:
- `SRC_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES` — “Sexual and reproductive health and rights — WHO”
- `SRC_WHO_SRH_FACTS_2026` — “WHO — Sexual and reproductive health and rights”

Same URL and version 1; title strings are equivalent. The two Source IDs are used for separate Evidence Use records for the same three Claims:
- `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_A`
- `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_B`
- `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_C`

Disposition: strong duplicate-source candidate. The presence of two Evidence Use records with two Source IDs does not create independent corroboration if both point to the same WHO overview page. Specialist review remains necessary for health claims.

## 3. Findings and impact

- Eight high-consequence duplicate-URI groups reviewed.
- 19 Source records across these groups (3 + 2 + 2 + 2 + 2 + 2 + 2 + 2).
- Every group shares one exact external URI among its Source records.
- Most groups have identical or near-identical titles and version 1; they are strong candidates for duplicate Source identity.
- No canonical Source, Evidence Use or Claim records were modified.
- No Source IDs were deleted, merged or rewritten.
- No claim was accepted or release-cleared.

The largest evidence risk is false independence: separate Source IDs for one shared URL must not be counted as independent sources. The EPA “independent corroboration” wording is an explicit case requiring review.

## 4. Required next actions

1. Editorially adjudicate each candidate group using source content, edition/date and archived snapshots; do not merge solely on URL equality.
2. Choose a canonical Source record only after identity is established; preserve old IDs as explicit aliases or redirects where stable references depend on them.
3. Recheck every linked Evidence Use after any Source consolidation. Preserve Claim-specific material descriptions and exact section/page/table/figure locators.
4. Recompute source-independence assessments after deduplication; distinct Source IDs pointing to the same publication/page are one source for independence purposes.
5. Correct the “independently confirms” description for `CLM-WATER-INDEPENDENT-CORROBORATION` or add a truly independent Source and exact locator.
6. Keep high-consequence water, wastewater, electrical-safety, infrastructure and reproductive-health Claims on HOLD pending specialist review and Human View.

## 5. Scope limitation

This report reviews eight of the 33 URI groups because of their risk relevance. The remaining 25 groups are still candidates for source identity review. A URI match alone is not proof of duplicate identity, but it is a reason not to claim independent corroboration until the underlying publications and versions are distinguished.
