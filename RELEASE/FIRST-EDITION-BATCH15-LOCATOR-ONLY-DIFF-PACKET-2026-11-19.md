# First Edition — Batch 15 Locator-Only Diff Packet (Approval Draft)

Date: 2026-11-19
Target branch: `mvp-public-contribution-design-2026-10-11`
Inspection HEAD: `3ed85e8096231c318c6bd762b32c7c02e57afe21`
Status: **PROPOSED ONLY — NO CANONICAL AUTHORIZATION; NO CANONICAL JSON CHANGED**

## 1. Purpose and selection

This packet converts only the clearly locator-oriented part of Batch 15 into exact, reviewable per-record changes. It does not implement the changes. It excludes source-graph expansion, Claim wording changes, and records whose support is not sufficiently direct.

The packet covers four existing Evidence Use records:
- Law Basics A and B;
- Social Statistics A;
- Units and Measurement B.

All four records were re-fetched from the inspection HEAD. Current versions are v1. No record-version increment or field change has been applied.

## 2. Exact proposed changes

### 2.1 Law Basics A — direct jurisdiction definition

**Current record**
- Path: `CONTENT/vertical-slices/law-basics/records/EU-LAW_BASICS-A.json`
- ID/version/type: `EU-LAW_BASICS-A@1` / `evidence_use`
- Current blob SHA: `2282e6360b38e55c4a13fa61c4c3229805136fc7`
- Claim: `CLM-LAW_BASICS-A@1`
- Source: `SRC-LAW_BASICS@1`

**Proposed version:** EU v1 → v2. Keep Claim and Source references unchanged.

**Proposed `content.material.locator`:**

> Cornell Legal Information Institute, Wex, “Jurisdiction”: opening definition (court power to adjudicate cases and issue orders; territory within which a court or government agency may properly exercise power); “Jurisdiction: An Overview,” opening definition paragraphs.

**Proposed description boundary:** The cited Wex entry supplies a U.S.-law reference definition and examples. Do not present its examples as a universal statement of every country's jurisdictional rules.

**Exact permitted field delta:** increment `record_version`; add `content.material.locator`; replace the generic `content.material.description` with a concise claim-specific description preserving the U.S.-law source boundary. No other field changes.

### 2.2 Law Basics B — jurisdictional dimensions

**Current record**
- Path: `CONTENT/vertical-slices/law-basics/records/EU-LAW_BASICS-B.json`
- ID/version/type: `EU-LAW_BASICS-B@1` / `evidence_use`
- Current blob SHA: `56f8ebe535e7b7dd247681f5fd2eacefe1d5770f`
- Claim: `CLM-LAW_BASICS-B@1`
- Source: `SRC-LAW_BASICS@1`

**Proposed version:** EU v1 → v2. Keep Claim and Source references unchanged.

**Proposed `content.material.locator`:**

> Cornell Legal Information Institute, Wex, “Jurisdiction: An Overview”: opening list of personal jurisdiction, subject-matter jurisdiction and jurisdiction to render the particular judgment sought; paragraphs “Subject matter jurisdiction” and “Territorial jurisdiction.”

**Proposed description boundary:** These passages map to the personal/party, subject-matter and territorial dimensions in the current Claim. Examples and doctrinal detail are U.S.-law-specific; the locator does not establish that every jurisdiction uses identical tests.

**Exact permitted field delta:** increment `record_version`; add `content.material.locator`; replace the generic `content.material.description` with a concise claim-specific description and the U.S.-law boundary. No other field changes.

### 2.3 Social Statistics A — scope of demographic and social statistics

**Current record**
- Path: `CONTENT/vertical-slices/social-statistics-basics/records/EU-SOCIAL_STATISTICS_BASICS-A.json`
- ID/version/type: `EU-SOCIAL_STATISTICS_BASICS-A@1` / `evidence_use`
- Current blob SHA: `6244215f8a6032ec97210cc889880f0c2b052cbc`
- Claim: `CLM-SOCIAL_STATISTICS_BASICS-A@1`
- Source: `SRC-SOCIAL_STATISTICS_BASICS@1`

**Proposed version:** EU v1 → v2. Keep Claim and Source references unchanged.

**Proposed `content.material.locator`:**

> United Nations Statistics Division, “Demographic and Social Statistics”: introductory “Data” section (UNSD collects, compiles and disseminates official statistics on a wide range of social and demographic topics); “Standards and methods” section; “Topics” list.

**Proposed description boundary:** This portal directly establishes the scope and breadth of the UNSD demographic/social statistics programme. It is a subject-area portal, not a single statistical methodology or a source for every possible social indicator.

**Exact permitted field delta:** increment `record_version`; add `content.material.locator`; replace the generic `content.material.description` with a concise claim-specific description and portal-level support boundary. Preserve the existing EU provenance, Claim reference, Source reference and `evidence_role: supports`.

**Explicit non-action:** do not silently change `SRC-SOCIAL_STATISTICS_BASICS@1` provenance.method (`editorial_context`) under this locator-only packet. The Batch 15 dossier flags that Source metadata/method field for separate review.

### 2.4 Units and Measurement B — SI unit system

**Current record**
- Path: `CONTENT/vertical-slices/units-and-measurement/records/EU-UNITS_AND_MEASUREMENT-B.json`
- ID/version/type: `EU-UNITS_AND_MEASUREMENT-B@1` / `evidence_use`
- Current blob SHA: `498d30cf6acf294ed6ac9e1e5269dcce728c5285`
- Claim: `CLM-UNITS_AND_MEASUREMENT-B@1`
- Source: `SRC-UNITS_AND_MEASUREMENT@1`

**Proposed version:** EU v1 → v2. Keep Claim and Source references unchanged.

**Proposed `content.material.locator`:**

> National Institute of Standards and Technology, “SI Units,” “Base and Derived Units” section: paragraph beginning “Definitions of all seven (7) SI base units…” and the following paragraph describing the seven base units, 22 derived units with special names and symbols, and the core set of SI units.

**Proposed description boundary:** The page directly supports the SI's base/derived-unit structure and its role as an international measurement standard. It does not by itself provide a full metrological treatment of measurement, uncertainty or every formal property of a coherent unit system.

**Exact permitted field delta:** increment `record_version`; add `content.material.locator`; replace the generic `content.material.description` with a concise claim-specific description and support boundary. Keep Claim/Source references and `evidence_role: supports` unchanged.

**Open support dependency:** The exact Claim uses the qualifier “coherent set.” The NIST page establishes the base/derived architecture, but the formal coherence wording should be checked against BIPM SI Brochure §1.1. If that qualifier is retained as a technical proposition, a distinct BIPM Source/EU dependency or an editorially approved narrowing is required; do not silently add BIPM under this locator-only packet.

## 3. Explicit exclusions and unresolved items

### Law Basics C — not included in the apply-ready set

- Current record: `EU-LAW_BASICS-C@1`, blob SHA `4af7bad2fccb8fb6be0ea56ebb2cbaa5177085b4`.
- The Wex “Jurisdiction” page gives U.S. federal/state examples and supports the U.S.-specific character of those examples. It does not independently establish the broader comparative proposition that legal rules and procedures are jurisdiction-specific across legal systems.
- Do not add a locator and treat the claim as fully supported. Keep the record unchanged pending a separate comparative source and/or editorial review of the Claim's methodological wording.

### Not included

- Public Administration A–C: requires a separate UN Human Rights Council Source/EU chain and canonical ID allocation.
- Social Statistics B/C: require separate UN Fundamental Principles of Official Statistics and Statistics Canada Source/EU chains.
- Units and Measurement A/C: require separate VIM/NIST uncertainty Source/EU chains.
- Sociology A–C: substantive Claim replacements; separate editor/subject-matter approval and rights review.
- Batch 16 Migration Claim C: separate UNHCR and UN Guiding Principles dependencies; no guessed IDs.
- P4/P5: separate 49-record proposal; its three Claim wording changes remain in the editor-approval lane.
- Settlement Geography: separate nine-record proposal using the Eurostat 2026 CC BY 4.0 source alternative; no authorization inferred.

## 4. Rights and editorial gates

- Cornell LII Wex is a U.S.-law reference, not an official statement of Cornell Law School and not legal advice. It is not a universal law source. Use factual paraphrase and attribution only; item-level reuse review remains open.
- The UN Statistics Division portal is an official UN statistical programme page. Public access is not blanket permission to reproduce text, tables or graphics; use factual paraphrase and attribution.
- NIST's SI page is an official U.S. government technical source. The proposed change uses factual paraphrase and a text locator only; exclude NIST/third-party graphics and posters.
- These locator proposals do not close project-level rights decisions R-01–R-10, appoint an editor, or constitute qualified legal/metrology review.

## 5. Change-control and validation contract

If and only if the owner approves this exact packet and the authorization is recorded:

1. Freeze a new exact PR HEAD and re-fetch the four proposed EU records plus their referenced Claims and Sources.
2. Verify each current blob SHA/version before editing; abort any record that has drifted.
3. Apply only the four listed EU v1→v2 changes. Do not modify Claims, Sources, Context, Scope, Relations, README files, coverage, allowlists or publication/completion states under this packet.
4. Re-fetch all four changed EUs and verify exact Claim→EU→Source references, record types, version increments, locators and `evidence_role: supports`.
5. Run affected-slice schema/graph tests and then exact-head Reference Tests, Release Conformance Gate, Offline Edition and Browser Tests on one immutable HEAD.
6. Preserve HOLD for every affected slice until rights, editorial review, Human View and the remaining release gates are independently closed.

## 6. Owner decision requested

Approve, reject or amend the exact four EU v1→v2 changes in §2. Approval of this packet does not approve Law Basics C, any new Source/EU dependency, any Claim wording change, any rights decision, or any INCLUDE/HOLD/EXCLUDE change.

**No canonical edit is authorized by this document. All affected slices remain HOLD.**
