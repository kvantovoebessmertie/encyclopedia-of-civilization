# M13 Batch 47 — reconciliation and Batch 48 handoff

Date: 2026-11-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Frozen Batch 47 selection revision: `677dff36c04e8593b74b0b4c6b6323cdadd12fa7`  
Queue workflow: `43189183999`; artifact: `13929592813`  
Review reports: Batch 47 Lanes 1–5, each 20 Claims.

## Reconciled Batch 47 totals

| Measure | Result |
|---|---:|
| Frozen Claims selected | 100 |
| Exact unique Claim IDs | 100 |
| Separator-normalized unique Claim IDs | 100 |
| Lane distribution | 5 × 20 |
| Claim statements reviewed | 100/100 |
| Evidence packet entries reviewed | 100/100 |
| Reviewer D/E/B rows recorded | 100/100 |
| Entries with explicit claim-specific section/page locator | 0/100 |
| Canonical Claim/Evidence Use/Source JSON changes | 0 |
| Dispositions | 100 HOLD |

The frozen queue was generated from 759 scored report rows and 742 Claims without a scored-row match. It contained 100 unique Claim versions and 100 evidence packets in five lanes of 20. Automated D/E/B scores were null in every packet. Exact and separator-normalized overlap with Batch 46 was zero.

## D/E/B distribution

| Dimension | Score 1 | Score 2 | Score 3 | Mean |
|---|---:|---:|---:|---:|
| D — depth | 12 | 45 | 43 | 2.31 |
| E — evidence | 100 | 0 | 0 | 1.00 |
| B — boundary/robustness | 10 | 57 | 33 | 2.23 |

All 100 entries lack a sufficiently precise claim-specific pinpoint in Evidence Use. E=1 means the support trail is not yet adequate for acceptance; it does not mean every source is irrelevant or every Claim is false.

## Cross-lane findings

1. **Evidence Use locator debt:** 100/100 entries have E=1. Add precise section/page/table/figure locators and verify the exact source edition.
2. **Source identity/URI defects:** The mineralogy Source identity and USGS URI are generic/misaligned with the actual USGS mineral definition; the measurement/sensor claim points to NIST IoT cybersecurity rather than metrology; the NIST ITL landing page is repeatedly used for computer architecture, databases, and distributed-systems propositions without topic-specific evidence.
3. **Strong sources need exact locators:** BIPM VIM 2.9, FRA Railroad Safety, NASA Appendix C, NIST C-SCRM, EPA municipal wastewater, IPCC AR6 WGII, NIST SP 800-145, MDN, NASA Systems Engineering, USGS/USDA soil material, OSHA PSM, UNDRR, and the Vienna Convention are relevant sources, but Evidence Use still needs precise passages.
4. **Scope boundaries:** U.S.-specific FRA, USACE, EPA, USDA, OSHA and FEMA/Ready.gov sources must remain jurisdictionally bounded. WHO human genome editing cannot alone support all genetic engineering. NIST C-SCRM sources support ICT/technology supply chains, not every supply chain.
5. **Template/editorial claims:** Several genetics/networking/database A/B/C statements are generic source-method cautions or slice-purpose claims, not substantive domain propositions. They need taxonomy/editorial treatment rather than automatic rewriting.
6. **No canonical edits:** No Claim, Evidence Use, or Source JSON was changed. No source substitution, ID rewrite, specialist sign-off, Human View clearance, rights clearance, editorial approval, or publication release is authorized.

## Scored-ledger integration

The shared ledger extractor and regression test have been updated to include Batch 47 lane reports. The test now expects:

- scored report rows: 859 (previous 759 + Batch 47's 100);
- unique normalized report IDs: 852 (previous 752 + 100 new unique IDs);
- existing duplicate report-ID groups: 7, unchanged;
- unmatched scored report rows: 0;
- Claims without a scored-row match: 642.

These are expected totals pending exact-HEAD CI and ledger-artifact verification.

## Batch 48 handoff

- Batch 47 is closed as a first-pass review batch, not as a set of accepted Claims.
- Queue automation should generate Batch 48 only after Batch 47 is included in the scored ledger.
- Verify exact source SHA, 100 unique Claim versions (or explicit shortfall), five lanes of 20, matching evidence packets, and no overlap with Batch 46/47 or prior scored worklists.
- No automated D/E/B scores; no canonical content mutation.
- Continue batch-level reconciliation and exact-HEAD Reference Tests, Release Conformance Gate, and Offline Edition. Do not merge this PR or publish a release.

## Current CI boundary

This is a review/handoff record only. CI status must be read from completed workflow runs attached to the exact commit containing the Batch 47 ledger integration and this reconciliation document. Queued or in-progress runs are not PASS.
