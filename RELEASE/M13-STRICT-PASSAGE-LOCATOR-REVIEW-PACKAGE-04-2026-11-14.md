# M13 — strict passage/locator review package 04

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Input queue: `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REPORT-MENTION-GAP-QUEUE-2026-11-13.md`  
Scope: 3 exact Claim/Evidence Use/Source triples from the strict 47-item queue — Asset Management A/B/C.  
State: **desk-level source identity, passage, rights and risk-routing review only; no canonical edits, no D/E/B changes, no specialist sign-off, no release clearance.**

## 1. Exact records and linkage

The exact v1 records were retrieved from `CONTENT/vertical-slices/asset-management-basics/records/`:

- `CLM-ASSET_MANAGEMENT_BASICS-A@1` → `EU-ASSET_MANAGEMENT_BASICS-A@1` → `SRC-ASSET_MANAGEMENT_BASICS@1`
- `CLM-ASSET_MANAGEMENT_BASICS-B@1` → `EU-ASSET_MANAGEMENT_BASICS-B@1` → `SRC-ASSET_MANAGEMENT_BASICS@1`
- `CLM-ASSET_MANAGEMENT_BASICS-C@1` → `EU-ASSET_MANAGEMENT_BASICS-C@1` → `SRC-ASSET_MANAGEMENT_BASICS@1`

All three Claim → EU → Source references resolve and versions match. All three EUs have generic descriptions and no reproducible passage locator.

## 2. Critical source identity mismatch

The Source record identifies the reference as **ISO 55000:2024 — Asset management — Vocabulary, overview and principles**, but its stored URI is:

`https://www.iso.org/standard/83054.html`

The live ISO page at that URI is **ISO 55001:2024 — Asset management system — Requirements**, not ISO 55000:2024. ISO's own page identifies the title and standard number explicitly. The correct ISO 55000:2024 product page is:

`https://www.iso.org/standard/83053.html`

This is a material Source identity mismatch, not merely a missing pinpoint. The stored URI must not be treated as if it resolves to the named ISO 55000 standard. Do not silently replace the URI or infer that the two standards are interchangeable: ISO 55000 supplies vocabulary, overview and principles; ISO 55001 specifies requirements for an asset management system.

## 3. Claim-by-Claim findings

### 3.1 Asset management — lifecycle, value, risk and organizational objectives

**Claim:** `CLM-ASSET_MANAGEMENT_BASICS-A@1`  
**Claim text:** “Управление активами рассматривает активы с учетом их жизненного цикла, ценности, рисков и целей организации.”

**Passage result: DIRECT conceptual fit from the correctly identified ISO 55000 preview, but not from the stored URI.** The ISO 55000:2024 preview describes managing assets over their life cycles to enhance value in support of organizational objectives. It defines asset management as coordinated organizational activity to realize value from assets; its note says realization of value normally involves balancing costs, risks, opportunities and performance benefits. These passages support the Claim's core. The registered URI currently points to ISO 55001 instead, so the canonical evidence chain is not accurate.

**Risk route: ELEVATED.** Asset-management decisions can affect infrastructure, service reliability, safety, lifecycle expenditure and organizational objectives. The Claim is a high-level description, not a decision rule for a particular asset class.

**Rights and use restriction:** ISO's page states that all ISO publications/materials are copyright protected and that, except for content specifically made available through ISO Open Data, ISO content may not be used for machine learning or AI technologies, including prompting or enabling AI tools to generate responses. The ISO 55000 preview page also gives a CHF 135 purchase price. The intended AI use of this source is therefore not cleared.

**Disposition: HOLD.** Correct source identity only through a bounded, authorized Source correction after rights review. Do not copy standard text, ingest it into AI workflows, or use it to generate Encyclopedia content unless the specific intended use is authorized by ISO or covered by a verified ISO Open Data license. Consider a rights-compatible secondary source for the general concept.

### 3.2 Asset-management decisions — balancing performance, risk, cost and opportunity

**Claim:** `CLM-ASSET_MANAGEMENT_BASICS-B@1`  
**Claim text:** “Решения по активам связаны с балансированием производительности, риска, затрат и возможностей в течение жизненного цикла.”

**Passage result: DIRECT conceptual fit from ISO 55000:2024, but canonical source identity is wrong.** ISO 55000 clause 3.2.1 Note 1 states that realization of value normally involves balancing costs, risks, opportunities and performance benefits. The registered Source URI points to ISO 55001:2024, not the ISO 55000 text containing the cited vocabulary definition. The Claim's “throughout the lifecycle” context is supported by the ISO 55000 overview, but the exact balance statement should be tied to the correct standard and locator.

**Risk route: ELEVATED.** A generalized trade-off statement could influence capital planning, maintenance, infrastructure renewal or service decisions. It must not be interpreted as a quantitative optimization formula or a substitute for asset-specific engineering, financial and safety assessment.

**Rights and use restriction:** Same ISO copyright and AI-use restriction as Claim A. No AI ingestion or AI-enabled reuse is cleared.

**Disposition: HOLD.** Source identity mismatch and rights restrictions must be resolved before any canonical locator proposal. The EU must distinguish the exact ISO 55000 vocabulary definition from ISO 55001 system requirements.

### 3.3 Asset-management system — coordinated planning, decisions and improvement

**Claim:** `CLM-ASSET_MANAGEMENT_BASICS-C@1`  
**Claim text:** “Система управления активами задает согласованный подход к планированию, принятию решений и улучшению управления активами.”

**Passage result: PARTIAL / strong conceptual fit, with source identity mismatch.** ISO's public preview describes ISO 55000 as an overview of asset management and asset-management systems and says the standard provides principles for developing a proactive asset-management system. The preview describes lifecycle management, alignment with organizational objectives and continual improvement. ISO 55001:2024 (the currently stored URI) is the requirements standard and its overview describes establishing, implementing, maintaining and improving an asset-management system. The Claim combines elements from the ISO 55000 overview and ISO 55001 requirements; the current EU does not distinguish these sources or provide an exact locator.

**Risk route: ELEVATED.** The statement may be used to design governance or operational management systems. It must not imply that a generic description constitutes conformity with ISO 55001 or that a management-system certificate guarantees asset safety or performance.

**Rights and use restriction:** Same ISO copyright and AI-use restriction. No AI use is cleared.

**Disposition: HOLD.** Separate the conceptual overview (ISO 55000) from system requirements (ISO 55001) in any future evidence chain. Correct the Source identity and register distinct Sources if both standards are used, but only after a bounded rights review and authorization.

## 4. Consolidated disposition

| Claim | Passage fit | Source identity | Risk route | Rights | Disposition |
|---|---|---|---|---|---|
| Asset Management A | Direct from correct ISO 55000 preview | Stored URL points to ISO 55001 | Elevated | ISO AI-use restriction unresolved | HOLD |
| Asset Management B | Direct from ISO 55000 clause 3.2.1 Note 1 | Stored URL points to ISO 55001 | Elevated | ISO AI-use restriction unresolved | HOLD |
| Asset Management C | Partial; mixes ISO 55000 overview and ISO 55001 system requirements | Stored URL points to ISO 55001 | Elevated | ISO AI-use restriction unresolved | HOLD |

## 5. Integrity and completion boundary

- Claims reviewed: **3**.
- Evidence Use records reviewed: **3**.
- Source records reviewed: **1**.
- Claim/EU/Source identity and version links: **3/3 resolve and match**.
- Generic/non-pinpoint EUs: **3/3**.
- Material Source identity/URI mismatch: **1** (the single Source record points to ISO 55001 while naming ISO 55000).
- Direct or partial conceptual fit located: **3/3**.
- Canonical Claim/Evidence Use/Source records changed: **0**.
- Source URIs corrected: **0**.
- Canonical passage locators added: **0**.
- D/E/B scores assigned or overwritten: **0**.
- Risk metadata assigned or changed: **0**.
- Rights permissions obtained: **0**.
- Specialist reviews completed: **0**.
- Human View / release approval: **0**.

## 6. Required next actions

1. Keep all three Asset Management Claims on HOLD.
2. Treat the stored URI mismatch as a Source identity defect: `83054` is ISO 55001:2024; ISO 55000:2024 is `83053`.
3. Do not perform an automatic URI replacement. Prepare a bounded Source correction proposal that preserves the version history and distinguishes ISO 55000 from ISO 55001.
4. Resolve ISO's copyright and AI-use conditions before any AI-enabled ingestion or generation from the standard. Seek explicit permission or use a rights-compatible alternative source.
5. If both standards are needed, register and assess them separately; do not collapse the overview/principles and requirements standards into one Source identity.
6. Continue the remaining strict-queue rows only after checking exact IDs and prior report coverage.

This package is a desk review and routing artifact. It is not an independent asset-management certification, a full risk assessment, rights clearance, a canonical correction, a specialist approval or M13 closure.
