# M13 — current generic-EU 496 → 356 residual queue checkpoint

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Coverage source revision: `c07a62be7301135eb53315b068ab7283979bc9ca`
Exact queue / worksheet revision: `23e1b24381374193865c68b0ba594cf16d739d2e`
State: **current exact-ID routing reconciliation; proposal-only; no canonical writes**

> This checkpoint supersedes the 507 → 367 and 510 → 370 intermediate routing checkpoints and the older 359-row ledger for current work. Use the current 356-row companion ledger and the artifact revisions recorded below.

## 1. Current exact generic-EU population

| Population | Count |
|---|---:|
| Current generic Evidence Use candidates | 496 |
| Exact Claim/EU mappings | 496 |
| Unmapped Evidence Use IDs | 0 |
| Ambiguous mappings | 0 |
| Candidates with any M13 report mention | 496 |
| Candidates with source-review filename mention | 496 |
| High-consequence candidates within the 496 | 120 |
| Previously reviewed priority second-pass Claims | 20 |
| **Current residual remediation population** | **356** |

Arithmetic: `496 - 120 - 20 = 356`.

The 20 priority Claims were matched by exact Claim ID against the current 496 candidate set. All 20 are present and are disjoint from the 120 high-consequence subset. The 356 residual is unique by EU ID and spans 135 thematic slices.

The generic-EU artifact uses exact ID mapping and report/filename text mentions. A mention is not semantic confirmation that the exact Claim/EU/Source versions and passage were substantively reviewed. It is not source acceptance, rights clearance, specialist approval or publication readiness.

## 2. Why the prior 367-row ledger is superseded

The prior 367-row ledger used the 507-candidate set from revision `42b2bb87f1fae9c0ba2ac99fdfe62ba9668b41b3`. After the bounded cross-queue OpenStax pinpoint corrections and Motion B correction, the latest exact coverage artifact contains 496 candidates.

The exact 11 Claim/EU pairs removed from the generic-description candidate set are:

| Claim | Evidence Use | Current EU version |
|---|---|---:|
| `CLM-CELL_BASICS-A` | `EU-CELL_BASICS-A` | 2 |
| `CLM-CELL_BASICS-B` | `EU-CELL_BASICS-B` | 2 |
| `CLM-COMPUTING_BASICS-A` | `EU-COMPUTING_BASICS-A` | 2 |
| `CLM-COMPUTING_BASICS-B` | `EU-COMPUTING_BASICS-B` | 2 |
| `CLM-COMPUTING_BASICS-C` | `EU-COMPUTING_BASICS-C` | 2 |
| `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-B` | `EU-CONSTITUTIONAL_SYSTEMS_BASICS-B` | 2 |
| `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-C` | `EU-CONSTITUTIONAL_SYSTEMS_BASICS-C` | 2 |
| `CLM-MATTER_BASICS-A` | `EU-MATTER_BASICS-A` | 2 |
| `CLM-MOTION_BASICS-B` | `EU-MOTION_BASICS-B` | 2 |
| `CLM-POLITICAL_SCIENCE_BASICS-B` | `EU-POLITICAL_SCIENCE_BASICS-B` | 2 |
| `CLM-POLITICAL_SCIENCE_BASICS-C` | `EU-POLITICAL_SCIENCE_BASICS-C` | 2 |

All 11 current EU files were fetched from exact revision `23e1b24381374193865c68b0ba594cf16d739d2e`. The ten OpenStax records retain Claim v1 and Source v1 references; Motion B points to corrected Claim v2 and Source v1. These changes remove the records from the generic-description candidate set only. Existing HOLD, PARTIAL and RIGHTS HOLD dispositions remain in force; no record is thereby cleared for publication or AI ingestion.

Set reconciliation is exact: prior residual 367 minus these 11 pairs equals current residual 356; no new residual pair appeared.

## 3. Current separate unassessed-risk queue

The push-triggered M13 Audit Queue Automation run on revision `23e1b24381374193865c68b0ba594cf16d739d2e` selected 41 Claims from 41 candidates, with 59 of 100 requested slots unfilled.

| Queue measure | Count |
|---|---:|
| Claims inventoried | 1,494 |
| Claims without recorded risk signals | 751 |
| Previously screened Claim IDs excluded | 708 |
| Unreconciled holdout Claims excluded | 17 |
| Reviewed-holdout overlap | 15 |
| Unique exclusions | 710 |
| New selected Claims | 41 |
| Unfilled slots | 59 |
| High-consequence screen flags across corpus | 520 |
| Structural finding rows | 1,128 |

The 41 selected risk-queue Claims have **zero** intersection with the current 496 generic-EU candidates and therefore zero intersection with the 356 residual. The earlier 11-Claim cross-queue overlap has been removed from the generic-EU set by the bounded EU corrections. It must not be counted as an additional or still-overlapping current cohort.

Absence of risk metadata is not a low-risk determination. The queue is routing only; it does not assign D/E/B, establish final risk status, or change canonical records.

## 4. Companion ledger and refresh method

The current companion files generated from the exact artifacts are:

- `M13-residual-356-generic-EU-remediation-ledger-current-2026-11-15.csv`
- `M13-residual-356-generic-EU-remediation-ledger-README-current-2026-11-15.md`

The CSV is unique by EU ID and carries exact Claim/EU/Source IDs, slice, canonical EU path, source review report mentions, all M13 report mentions, source identity/URI metadata, risk and score state, and human-review status. Claim-level metadata, risk flags, review status and D/E/B fields were refreshed from the exact-head worksheet; source-review and all-report mentions were refreshed from the latest coverage artifact. All 356 rows have at least one source-review filename mention, but each report body still governs its own semantic disposition.

Every row retains `human_confirmation_required=true` and `canonical_write_authorized=false`. This is a routing ledger only and authorizes no canonical change.

## 5. Exact source artifacts

- Generic-EU coverage workflow run `43745382809`, artifact `14173129606`, revision `c07a62be7301135eb53315b068ab7283979bc9ca`, digest `sha256:6862be6be79441dc77f1fb04e741dacce52fe1b560fd9258a02fc5d17705f5bd`.
- Audit Queue Automation run `43746834938`, artifact `14174428604`, revision `23e1b24381374193865c68b0ba594cf16d739d2e`, digest `sha256:10a1f216ec7446229360cf5a5c7a042d883e9f0a409553f1361e8834129d596d`.
- Claim worksheet from Reference Tests run `43746839045`, artifact `14174388824`, revision `23e1b24381374193865c68b0ba594cf16d739d2e`, digest `sha256:8235cb0027394d8430485e4b4deca1be4e904abd6a95eeed96228f4e0786b3a4`.

## 6. Verification and release boundary

On exact revision `23e1b24381374193865c68b0ba594cf16d739d2e`:
- Reference implementation tests: **PASS**.
- Offline Edition: **PASS**.
- Release Conformance Gate: **PASS**.
- Exact-head CI: **3/3 PASS**.

This checkpoint adds no canonical Claim, Evidence Use, Source, Context, Scope, Relation, risk-metadata or D/E/B changes. The next work remains evidence-led proposal consolidation for the 356 residual Claims, with existing source reviews and rights restrictions reused rather than repeated. Canonical changes require separate bounded authorization.

M13 remains **OPEN / NOT RELEASE-READY**. PR #21 remains Draft/unmerged; `main` remains unchanged.
