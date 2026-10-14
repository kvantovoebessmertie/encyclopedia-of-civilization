# MVP GIS-C remediation — candidate technical source review

Date: 2026-10-11  
Branch: `mvp-public-contribution-design-2026-10-11`  
Status: **source candidate identified; GIS-C remains HOLD; no canonical record or preview allowlist changed**

## Candidate sources checked

### 1. Federal Geographic Data Committee (FGDC), Content Standard for Digital Geospatial Metadata (CSDGM)

- Standard landing page: https://www.fgdc.gov/metadata/csdgm-standard
- Data Quality Information section: https://www.fgdc.gov/metadata/csdgm/02.html
- Metadata overview: https://www.fgdc.gov/metadata

The FGDC Data Quality Information section explicitly lists attribute accuracy, logical consistency, completeness, positional accuracy, and lineage. It defines lineage as information about the events, parameters, and source data used to construct a dataset, plus responsible parties. It also identifies source scale as a metadata element. This is a strong topical match for the quality/accuracy/provenance portion of GIS-C, but it is a technical metadata standard, not a general statement that every dataset has known or adequate quality.

The FGDC's general metadata page explains that geospatial metadata documents who, what, when, where, how and why a data resource exists, including maps, GIS files, imagery and other location-based resources. This supports metadata/provenance framing.

### 2. FGDC National Standard for Spatial Data Accuracy (NSSDA)

- Standard landing page: https://www.fgdc.gov/standards/projects/FGDC-standards-projects/accuracy/part3/index_html

This standard sets a methodology for testing and reporting positional accuracy of maps and geospatial data. It supports the narrower proposition that spatial accuracy should be evaluated and reported using a stated method, rather than assumed from the mere existence of a GIS layer. It does not, on its own, support every possible quality dimension or the broad word “scale.”

## Candidate claim-to-evidence map

| GIS-C proposition component | Best candidate evidence | Finding |
|---|---|---|
| Dataset quality must be assessed rather than presumed | FGDC CSDGM, “Data Quality Information” | Direct support for structured reporting of multiple quality dimensions |
| Positional accuracy is a distinct property with a defined assessment method | FGDC NSSDA | Direct support for testing/reporting positional accuracy |
| Provenance/source history matters | FGDC CSDGM, “Lineage” element | Direct support for recording source data, process/events and responsible parties |
| Scale matters | FGDC CSDGM source-scale metadata element | Supports recording scale; does not imply scale alone determines fitness for every use |
| Any GIS analysis is constrained by all these factors | Combined synthesis | Needs carefully bounded wording; do not present as a direct quotation or as a universal law from one source |

## Recommended next editorial action

Before changing canonical data, inspect the exact current wording and decide whether GIS-C should be narrowed to a statement like:

“Качество геопространственных данных следует оценивать по соответствующим характеристикам — например, полноте, логической согласованности, позиционной точности и происхождению данных; пригодность зависит от задачи и документации набора.”

This wording is only a **candidate for human review**, not an approved replacement. If scale remains, preserve it as a distinct metadata characteristic and avoid implying that a nominal map scale alone proves accuracy or fitness for use.

## Rights, citation and publication gates

- These are technical standard/reference pages; link and paraphrase narrowly, and record exact version/date/section used.
- No blanket rights conclusion is made here. Check the specific standard's reuse terms before copying substantial text, tables, or diagrams.
- The canonical GIS Source record currently has a different stored URL from the USGS educational page assessed in the earlier note. Do not silently replace it.
- GIS-C remains **HOLD** until a reviewed versioned source record, exact Evidence Use pinpoint(s), exact record-version allowlist, rights/attribution check, rendered Human View, and editorial approval are all recorded.
- No canonical Claim, Evidence Use or Source JSON changed. No real-record preview allowlist was created. The reader must continue using synthetic fixtures.
