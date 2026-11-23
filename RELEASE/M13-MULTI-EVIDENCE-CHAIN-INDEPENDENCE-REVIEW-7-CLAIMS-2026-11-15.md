# M13 — multi-Evidence-Use chain and corroboration review (7 Claims)

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Reviewed exact revision: `679912a41d3efe8a7d0b9150d531770baedaec1b`
Input: current 356-row generic-EU remediation ledger; seven Claims with two linked Evidence Use records each.
State: **record-chain and source-diversity adjudication only; no canonical edits, no D/E/B changes, no source acceptance or publication clearance**

## 1. Purpose and method

The current 356-row ledger contains seven Claims with more than one Evidence Use record. This pass fetched the exact Claim, all linked EU records and all referenced Source records at the reviewed revision. It checked:
- whether each EU points to the intended Claim version and a distinct, resolvable Source ID/version;
- whether `provenance.created_from` is consistent with the linked Source;
- whether two different Source IDs/URLs actually establish independent corroboration, or merely provide distinct institutional pages, derivative data, overlapping standards, or scope-limited context;
- whether the companion ledger exposes the full source mapping.

This is not a full re-review of every passage and does not supersede the named Claim source-passage reports. A distinct institution, URI or Source ID is not, by itself, proof of independent evidence.

## 2. Exact Claim → EU → Source mapping

All 14 Evidence Use records resolve to the intended Claim v1 and their intended Source v1. All 14 provenance `created_from` entries point to the linked Source ID/version. No broken Claim/EU/Source edge or self-referential provenance defect was found in this seven-Claim subset.

| Claim | Evidence Use | Source | Registered source URI |
|---|---|---|---|
| `CLM-AGRICULTURE_BASICS-B@1` | `EU-AGRICULTURE_BASICS-B@1` | `SRC-AGRICULTURE_BASICS@1` | https://www.fao.org/agriculture/ |
| `CLM-AGRICULTURE_BASICS-B@1` | `EU-AGRICULTURE-USDA-CORROBORATION@1` | `SRC-USDA-AGRICULTURE-CONTEXT@1` | https://www.climatehubs.usda.gov/approach/manage-crops-cope-warmer-drier-conditions |
| `CLM-ALGEBRA_BASICS-B@1` | `EU-ALGEBRA_BASICS-B@1` | `SRC-ALGEBRA_BASICS@1` | https://openstax.org/details/books/college-algebra-2e |
| `CLM-ALGEBRA_BASICS-B@1` | `EU-ALGEBRA-UMN-CORROBORATION@1` | `SRC-UMN-OPEN-ALGEBRA@1` | https://open.umn.edu/opentextbooks/textbooks/376 |
| `CLM-ECONOMIC_HISTORY-A@1` | `EU-ECONOMIC_HISTORY-A@1` | `SRC-ECONOMIC_HISTORY@1` | https://ourworldindata.org/economic-growth |
| `CLM-ECONOMIC_HISTORY-A@1` | `EU-ECONOMIC_HISTORY-INDEPENDENT-A@1` | `SRC-ECONOMIC_HISTORY-INDEPENDENT@1` | https://wdi.worldbank.org/table |
| `CLM-ENERGY_SECURITY_BASICS-A@1` | `EU-ENERGY_SECURITY_BASICS-A@1` | `SRC-ENERGY_SECURITY_BASICS@1` | https://www.iea.org/topics/energy-security |
| `CLM-ENERGY_SECURITY_BASICS-A@1` | `EU-ENERGY_SECURITY_EU@1` | `SRC-EU-ENERGY-SECURITY@1` | https://energy.ec.europa.eu/news/focus-eu-energy-security-explained-2026-04-20_en |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-B@1` | `EU-MEASUREMENT_UNCERTAINTY_BASICS-B@1` | `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1` | https://www.nist.gov/pml/nist-technical-note-1297 |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-B@1` | `EU-MEASUREMENT_UNCERTAINTY_BIPM@1` | `SRC-BIPM-VIM-MEASUREMENT-UNCERTAINTY@1` | https://jcgm.bipm.org/vim/en/2.26.html |
| `CLM-POLITICAL_ECONOMY_BASICS-A@1` | `EU-POLITICAL_ECONOMY_BASICS-A@1` | `SRC-POLITICAL_ECONOMY_BASICS@1` | https://www.imf.org/en/publications/fandd/issues/2020/06/political-economy-of-economic-policy-jeffrieden |
| `CLM-POLITICAL_ECONOMY_BASICS-A@1` | `EU-POLITICAL_ECONOMY_BASICS-INDEPENDENT-A@1` | `SRC-POLITICAL_ECONOMY_BASICS-INDEPENDENT@1` | https://www.worldbank.org/en/programs/building-effective-accountable-and-inclusive-institutions-europe-central-asia/overview |
| `CLM_WATER_RESOURCES_BASICS_A@1` | `EU-WATER_RESOURCES_BASICS-A@1` | `SRC-WATER_RESOURCES_BASICS@1` | https://www.usgs.gov/mission-areas/water-resources |
| `CLM_WATER_RESOURCES_BASICS_A@1` | `EU_WATER_RESOURCES_BASICS_EPA@1` | `SRC_EPA_WATER_RESOURCES@1` | https://www.epa.gov/report-environment/water |

## 3. Claim-level corroboration adjudication

| Claim | Distinct-source finding | Independence / scope disposition |
|---|---|---|
| Agriculture B — productivity depends on soil, water, biological factors, climate and management | FAO and USDA Climate Hubs are different institutions. USDA's linked crop-management page is a meaningful additional source for soil, water and climate adaptation; it is not a full independent confirmation of every element in the Claim. The existing FAO Agriculture landing-page URI was reported unavailable (404) in the thematic source review. | **Complementary institutional corroboration, not full independent coverage.** Reuse the thematic review: FAO AEZ, agroecology and agrifood-system passages are needed for the broader interaction claim. Do not count the broken FAO landing page as supporting evidence. No canonical correction is authorized. |
| Algebra B — equation states equality of two expressions and is solved for unknowns by permissible transformations | OpenStax College Algebra 2e and UMN Open Textbook Library's *Introductory Algebra* are distinct textbooks/institutions. The UMN record identifies CC BY-NC-SA; the OpenStax book is separately subject to CC BY-NC-SA and its own express AI-ingestion restriction already recorded in the M13 rights hold. The Open Textbook Library's review page also reports specific mathematical errors in the UMN textbook and notes missing references. | **Two distinct texts, but not automatically rights-compatible or equally reliable corroboration.** Exact chapter/page pinpoints and a content-quality check are required. OpenStax remains RIGHTS HOLD for AI ingestion absent prior written permission. UMN's CC BY-NC-SA conditions require separate intended-use review; the review's documented errors mean it should not be accepted as unqualified corroboration. |
| Economic History A — historical production and income estimates allow study of long-term economic change | Our World in Data and World Bank WDI are distinct publisher/source endpoints, but OWID's long-run global GDP series explicitly combines the Maddison Database, Maddison Project Database and World Bank; the post-1990 segment is World Bank data. | **Not fully independent for the overlapping WDI period.** Treat OWID as a processed presentation/long-run reconstruction and WDI as an underlying source for relevant years, not two independent confirmations of the same data points. The pre-1990 Maddison components provide a different historical evidence lineage. Record indicator, period, price basis, PPP basis and dataset vintage before relying on the pair. |
| Energy Security A — reliable and affordable access and resilience to supply disruption | IEA and European Commission are distinct institutions. The EU Commission page gives a concrete EU policy context; it is not globally scoped and cannot establish the whole Claim for all energy systems. | **Complementary institutional corroboration with a jurisdiction boundary.** Reuse the thematic Energy Security review: IEA topic page/glossary/analytical framework are needed for the definition and resilience dimensions; Commission evidence is EU-specific only. The second EU is not a substitute for IEA claim-specific pinpoints. |
| Measurement Uncertainty B — uncertainty characterizes dispersion of values attributed to a measurand and is not automatically error | NIST TN 1297 and BIPM/JCGM VIM are distinct publications, but their metrological definitions are aligned within the same international GUM/VIM framework. | **Authoritative complementary standards references, not fully independent conceptual evidence.** Reuse the thematic review's exact pinpoints: VIM 2.26 for uncertainty, VIM 2.16 for error, and NIST TN 1297 §2.3 for the distinction. Keep the wording aligned with the current VIM definition; do not overstate “dispersion” as simple observed scatter. |
| Political Economy A — political economy studies mutual influence of political institutions and economic processes | The IMF Finance & Development article is a focused political-economy explanation. The World Bank ECA institutions programme overview is a regional programme page on institution-building, not necessarily a direct conceptual definition of political economy or the full mutual-influence proposition. | **Complementary institutional corroboration is present, with a regional boundary.** The World Bank overview states that economic institutions affect investment, saving, education and technology creation, while political institutions shape the form, function and effectiveness of economic institutions; it also describes political-economy factors shaping institutional incentives and interactions. This directly supports the mutual-influence proposition at a governance/institutional level. The page is explicitly focused on Europe and Central Asia, so it is not a universal/global account. The IMF article gives a broader conceptual account of politics affecting the economy and the economy affecting politics. The two sources are distinct institutional perspectives, but the World Bank locator must be made section-specific and its regional scope retained. |
| Water Resources A — water resources include surface/groundwater, wetlands and other aquatic components supporting ecosystems and human use | USGS Water Resources Mission Area and EPA Report on the Environment Water page are distinct institutions and source pages. EPA explicitly enumerates lakes, streams, groundwater, coastal waters, wetlands, associated ecosystems and human uses. | **Direct cross-institution corroboration for Claim A.** This is the strongest genuine independent institutional pair in this subset. Keep each EU linked to its own Source. Do not infer that the EPA source is linked to Water Resources B/C merely because an EPA Source appears in Claim provenance elsewhere. |

## 4. Companion ledger field limitation

The 356-row companion CSV carries all 14 Evidence Use IDs and parallel ordered arrays of source identities, source URIs, source versions and material descriptions for these seven Claims. However, its singular `source_ids` column contains only the primary Claim Source ID per row and omits the secondary Source IDs for multi-EU Claims. This can mislead a consumer who reads that column alone.

The companion ledger is therefore not a complete normalized EU→Source join for multi-EU Claims. The table in §2 is the exact sidecar mapping for this seven-Claim subset. Any next CSV revision should either:
1. encode all source IDs in a delimiter-separated `source_ids` field aligned with `evidence_use_ids`; or
2. provide a separate one-row-per-EU normalized linkage table.

Do not infer the missing secondary Source IDs from the singular column.

## 5. Required follow-up

1. Preserve this 14-row mapping as the exact secondary-source crosswalk for the seven Claims.
2. Add exact claim-specific locators before any of these EU records are considered passage-reproducible.
3. Keep OpenStax rights hold and separately assess the UMN CC BY-NC-SA conditions and textbook quality.
4. Treat OWID/WDI overlap by indicator and time period; do not double-count one data lineage as independent evidence.
5. Keep IEA/European Commission and USGS/EPA jurisdictional scopes explicit.
6. Add an exact locator to the World Bank overview's “Public Institutions” / “Political Economy Analysis” content and retain its Europe-and-Central-Asia boundary.
7. Repair the companion CSV schema in a future generated-ledger refresh; no canonical record changes are needed for this metadata correction.

## 6. Integrity

- Claims checked: 7.
- Evidence Use records checked: 14.
- Source records checked: 14.
- Claim→EU→Source version edges resolving: 14/14.
- Provenance created_from aligned to EU source_ref: 14/14.
- Claims with at least one genuinely distinct institutional source pair: 7, but strength and independence vary as described above.
- Canonical JSON changes: 0.
- D/E/B changes: 0.
- Rights holds cleared: 0.
- Publication or Human View approvals: 0.

M13 remains **OPEN / NOT RELEASE-READY**. This report is a source-diversity and linkage audit, not acceptance of any Claim.


## 7. Follow-up addendum — normalized source-linkage sidecar (2026-11-15)

The historical limitation in §4 is addressed for repository consumers by the companion normalized file:

- `RELEASE/M13-MULTI-EU-7-CLAIMS-NORMALIZED-SOURCE-LINKAGE-2026-11-15.csv`

It contains one row per exact Claim → Evidence Use → Source link (14 rows for 7 Claims), preserving each Source ID, version, URI, independence disposition and scope/rights note. This sidecar is the authoritative normalized crosswalk for this seven-Claim subset. It does not establish that the separate 356-row companion ledger was corrected; that CSV was not present in the branch tree at the cross-audit checkpoint. The original §4 description remains a historical observation about the ledger version reviewed in this report.

No canonical records, D/E/B values, risk metadata or rights dispositions were changed by this addendum.
