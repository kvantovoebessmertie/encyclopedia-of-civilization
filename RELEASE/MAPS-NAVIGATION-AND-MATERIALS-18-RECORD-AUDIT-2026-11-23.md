# First Edition — Maps & Navigation and Materials Basics: 18-Record Audit

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `bc1ff85650f149c9faf0c3d78e7a4fb718e12537`  
PR #22: OPEN / DRAFT / NOT MERGED  
Status: bounded evidence and source-fit review; no canonical writes.

## 1. Scope

Re-fetched all 18 records across Maps and Navigation Basics (9) and Materials Basics (9), including three Claims, three EUs, one Source, Context and Scope per slice. Reviewed exact record versions and blob SHAs, source content, evidence alignment and applicability boundaries. No canonical records were modified; all six Claims remain HOLD.

## 2. Maps and Navigation Basics — 9 records

### 2.1 Exact record identities

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-MAPS_AND_NAVIGATION_BASICS-A | 1 | Claim | `3901ca1a0b4d21eb056548c6ef99e779496a1d90` |
| CLM-MAPS_AND_NAVIGATION_BASICS-B | 1 | Claim | `3fb0f1d2ccd87c4683b636122313cb6244569de0` |
| CLM-MAPS_AND_NAVIGATION_BASICS-C | 1 | Claim | `bee8f7090c4a70e3a8bc6121148cef4afc28c9af` |
| EU-MAPS_AND_NAVIGATION_BASICS-A | 1 | Evidence Use | `eaefe0c405544bd318b4590a3624bcbdeebc3a24` |
| EU-MAPS_AND_NAVIGATION_BASICS-B | 1 | Evidence Use | `a8823811f8ec9c162a9c87f6fe315d68f5d0a761` |
| EU-MAPS_AND_NAVIGATION_BASICS-C | 1 | Evidence Use | `9aab0469bafa871fd3816ef498ff35cc75d2164e` |
| SRC-MAPS_AND_NAVIGATION_BASICS | 1 | Source | `060351a60aee27517fc093765cc098148f912f01` |
| CTX-MAPS_AND_NAVIGATION_BASICS | 1 | Context | `b737d777f76fa2fea75c675cef53186f67533c42` |
| SCP-MAPS_AND_NAVIGATION_BASICS | 1 | Scope | `f77e7d084e17e2a84594f943d8a200f7f6bd79a7` |

### 2.2 Claim-level findings

**Claim A — topographic map shows objects, distances and terrain**

USGS “Finding Your Way With Map and Compass” says topographic maps locate natural and human-made features, describe land shape, show distance and direction, and represent topography through contour lines. This is a direct match to the Claim. USGS “Topographic Mapping” independently explains that contour lines portray terrain shape/elevation and that maps include natural and human-made features.

The existing EU-A has no pinpoint locator. A future EU v2 should identify the introductory paragraph and the sections on contours/features; a second USGS Topographic Mapping page can corroborate the contour/elevation component.

**Claim B — map scale relates map distance to ground distance**

USGS explicitly defines scale as the relationship/ratio between a unit of measurement on the map and the actual ground distance represented. The existing EU-B has no locator. The source's own scale explanation directly supports the Claim.

**Claim C — navigation inference depends on map quality, scale, currency and field conditions**

The current source page covers scale, map content, compass and map-reading basics. It does not directly support all four factors in the Claim, especially map currency and conditions on the ground. A 2001 USGS fact sheet is also archived and is not expected to be updated. The newer USGS “What is a topographic map?” page explains that current US Topo maps are digital products from 2009 onward, while historical maps cover earlier periods; it also notes that older maps may omit or differ in represented features.

**Finding:** Claim C is a sensible caution but broader than the current Source/EU. It needs additional evidence about map currency/data vintages and field verification, or a narrowed Claim. Do not turn it into a claim that a map alone guarantees safe navigation.

### 2.3 Source currentness and rights

The existing Source URI points to the current USGS educational resource. The corresponding USGS numbered fact sheet is dated 2001 and marked archived. Prefer the live educational page for basic concepts and a current USGS FAQ for map product currency. The older fact sheet can remain as a historical supporting item, not as the sole current source for modern map products.

No map images, symbols, figures or copied publication text are proposed for redistribution. Rights and asset credits must be checked individually before reusing USGS map products or third-party data.

### 2.4 Context/Scope and disposition

CTX and SCP target Claim A only. Scope correctly states that this educational slice does not replace local navigation data or professional geodetic work. Preserve this boundary.

**Disposition: A/B have strong source fit but need versioned pinpoint EUs; C remains HOLD pending direct support or narrowing.**

## 3. Materials Basics — 9 records

### 3.1 Exact record identities

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-MATERIALS_BASICS-A | 1 | Claim | `b4b695817949e4832fb6a946ecd6f559bb49fc43` |
| CLM-MATERIALS_BASICS-B | 1 | Claim | `a52578a528242effbad9662b435f58047c931cbf` |
| CLM-MATERIALS_BASICS-C | 1 | Claim | `6ae99e91131c92bc119181c7bf6f7887c4ab9d2b` |
| EU-MATERIALS_BASICS-A | 1 | Evidence Use | `c4b896106a8985ac86521b3fd774828d5eeabc34` |
| EU-MATERIALS_BASICS-B | 1 | Evidence Use | `4c51ea38769fa3cded387ed772726f318152eff6` |
| EU-MATERIALS_BASICS-C | 1 | Evidence Use | `0b352a0accaa0befc557cbcb9623d468a87dc45f` |
| SRC-MATERIALS_BASICS | 1 | Source | `594e94e7c861ec5faec6e58ef6277212b52bc3ea` |
| CTX-MATERIALS_BASICS | 1 | Context | `13d4b16a97fc181fa98d8a090e6d3457c88f423d` |
| SCP-MATERIALS_BASICS | 1 | Scope | `6a46ed5ebee6115ce0d7f6da6ad01b789b8f260b` |

### 3.2 Claim-level findings

**Claim A — materials science relationships among materials, measurements, models, data and performance**

The current NIST Materials Science and Engineering Division page says the division develops measurements, models, data and standards and grounds its competence in structure–property–processing relationships. It also describes measurement science and materials data infrastructure. This directly supports much of the Claim, although “relationships among” is a synthesized summary of the NIST description rather than a direct definition of the entire discipline.

**Finding:** promising source fit, but the EU should pinpoint the division's overview and structure-property-processing passage. The Claim should not imply that this one division exhaustively defines all materials science.

**Claim B — physical, chemical and mechanical properties**

The NIST division page supports material properties broadly and lists groups focused on mechanical performance, functional properties, polymer properties and chemical composition measurements. The page does not present a single concise taxonomy that explicitly says materials are characterized by the complete three-part list “physical, chemical and mechanical properties.”

**Finding:** partial support. A versioned EU should cite separate NIST pages/groups for mechanical performance and chemical/physical characterization, or the Claim should be narrowed to the property classes directly demonstrated by the source. Avoid treating the list as exhaustive.

**Claim C — behavior depends on composition, structure, processing and operating conditions**

NIST's overview explicitly emphasizes structure-property-processing relationships. NIST's Mechanical Performance Group further addresses material properties under extreme environmental and operating conditions. NIST's Thermodynamics and Kinetics Group describes composition-related material systems, phase transformations, microstructure evolution, properties and processing/structure/performance relations.

**Finding:** broad support exists across multiple NIST divisions/groups, but not from the single generic Source record as currently linked. Claim C needs multiple direct evidence tracks and exact locators. “Composition” and “operating conditions” must each be supported explicitly; do not rely on the phrase structure-property-processing alone.

### 3.3 Source and rights review

The Source currently points to the NIST Materials Science and Engineering Division page. Better specific source candidates include:
- NIST MSED overview for measurement/model/data/standards and structure-property-processing;
- NIST Mechanical Performance Group for mechanical properties and operating conditions;
- NIST Thermodynamics and Kinetics Group for processing, phase transformations, microstructure and properties.

The report proposes factual paraphrase and citations only. It does not establish blanket rights for third-party datasets, standards, images, or external linked content. Check each asset and referenced standard separately.

### 3.4 Context/Scope and disposition

CTX and SCP target Claim A only. Context correctly requires composition, state, measurement method and conditions to be specified when describing a particular material. It must not be silently applied to Claims B/C.

**Disposition: Claim A is the strongest candidate; B/C need a multi-source evidence structure. All three remain HOLD pending versioned locators, source coverage and reader review.**

## 4. Consolidated next actions

1. Maps A/B: prepare versioned EUs with exact USGS locators; use current USGS topographic mapping pages for current map products.
2. Maps C: either find direct support for currency/field conditions or narrow the Claim; preserve the explicit safety boundary.
3. Materials A: add NIST overview pinpoint.
4. Materials B/C: split evidence across relevant NIST group pages; ensure each property/process phrase has a direct source.
5. Do not promote either slice to INCLUDE until rights, Human View, exact reader display, and project owner gates pass.

**Final disposition: 18 records inspected; 6 Claims remain HOLD; zero canonical writes; zero INCLUDE decisions.**
