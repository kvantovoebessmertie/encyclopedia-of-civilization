# M8 Depth and Coverage Gap Map — 2026-10-09

## Status

**OPEN — initial 12-slice diagnostic completed; four controlled corrections implemented; post-correction audits and exact-head CI pending. M8 is not CLEAN.**

Branch: `m8-depth-baseline-2026-10-09`.
Accepted starting point: M7 CLEAN SHA `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`.
Baseline corpus: **483 slices / 4,827 Records / 19 Record types**; 616 Sources / 1,668 Evidence Use / 64 Relations.

M7 acceptance remains a historical immutable checkpoint. The M8 branch first reconciles documentation status and defines reproducible measurement; it does not alter `main`, accepted M6, protected M4/M5, or the accepted M7 SHA.

## Objective

Identify the highest-value verified content gaps by separating five questions:
1. **Breadth:** what important user needs/domains lack adequate coverage?
2. **Depth:** where are claims only asserted rather than explained with conditions, mechanisms, and limitations?
3. **Evidence maturity:** which claims lack traceable, claim-specific source support or warranted independent corroboration?
4. **Human View:** can a non-specialist find, understand and safely interpret the material without knowing the architecture?
5. **Integration:** where are cross-domain dependencies missing or misleading, and which existing Relations actually help a user?

No single maturity percentage will be published until the rubric, denominator and weighting are defensible. The M8 diagnostic sample is purposive/stratified and must not be presented as a statistically representative estimate of all 4,827 Records.

## Measurement authority

Use `RELEASE/M8-DEPTH-MEASUREMENT-PROTOCOL-2026-10-09.md` as the controlling scoring and sampling method. Freeze the exact corpus SHA and sample list before scoring. Every scored claim needs D (depth), E (evidence fit), B (boundary/epistemic discipline), and a rationale. Slice-level H1/H2/H3 and integration review remain separate.

## Initial diagnostic sample strata

Frozen diagnostic list after registry presence checks; claim inventory is verified before scoring:

| Stratum | Candidate slices | Diagnostic purpose |
|---|---|---|
| H — high-consequence/practical | `water`, `generator-carbon-monoxide-safety` | Test whether short safety-relevant records provide sufficient conditions, explicit limits and evidence fit |
| M — prior maturation | `sleep-basics`, `governance-basics` | Compare existing content that underwent previous maturity passes |
| I — cross-domain/infrastructure | `human-settlement-systems-basics`, `supply-chain-basics` | Test integration dependencies and whether relations/contexts support meaningful use |
| G — general introductory | `mechanics-basics`, `statistics-basics` | Establish comparison against ordinary foundational topics |
| N — newest M7 content | `woodworking-basics`, `papermaking-basics`, `ceramics-basics`, `textile-fibre-processing-basics` | Compare newly authored introductory slices and their source/scope boundaries |

This is a diagnostic selection, not random sampling. The 12 selected slice directories were present in the registered corpus. The sample includes 4 newest M7 slices and 8 comparison slices across three other strata. If claim inventory shows an anomaly, record it explicitly; do not silently swap after results are visible. Score every Claim in the final frozen list, not a hand-picked subset.

## Gap hypotheses to test (not yet findings)

- Short canonical profiles may pass schema and CI while still offering limited explanatory depth for some user needs.
- Evidence Use may be structurally valid but vary in how precisely it describes the support and its limitations.
- Safety-relevant claims may need more explicit applicability conditions, prerequisites or decision boundaries.
- Context/Scope may be present as Records yet not always be sufficiently visible or actionable in a human-facing view.
- Cross-domain links may exist structurally without enough explanation of their user-relevant implication.
- Newly added slices may have a different maturity profile from older or previously matured content; this must not be mistaken for regression in accepted slices.

Each hypothesis must be accepted, narrowed or rejected from the sample evidence. Do not convert it into a confirmed debt merely because it appears here.

## Prioritization rules

Prioritize confirmed gaps by:
1. severity and consequence if misunderstood;
2. number and importance of affected user tasks;
3. strength of source evidence for a correction;
4. reuse across multiple slices;
5. ability to add meaningful explanation without overclaiming;
6. regression coverage and maintainability.

Do not prioritize by record count, source count, novelty, or fixed target size. No new Record type is authorized. Relations are added only where the dependency is meaningful and supported.

## Current gates

- [x] M7 accepted CLEAN SHA and exact-head 3/3 results recorded.
- [x] Stale M7 pending-gate wording reconciled on this successor branch without rewriting the M7 checkpoint.
- [x] Reproducible scoring protocol drafted.
- [x] Confirm the 12-slice list against the registered corpus directories.
- [x] Freeze the exact Claim inventory and score every Claim in the selected slices: 43 Claims across 12 slices.
- [x] Record first-pass results, denominators, distributions, and corpus SHA in `M8-INITIAL-DEPTH-DIAGNOSTIC-2026-10-09.md`.
- [x] Lock a narrow correction scope in `M8-CORRECTION-SCOPE-LOCK-2026-10-09.md`.
- [ ] Complete independent review of high-consequence and low-scoring findings.
- [ ] Implement controlled corrections and dedicated regression updates.
- [ ] Post-correction substantive/evidence/Human View/Relation audit.
- [ ] Reconcile actual coverage and registry metadata, then run exact-head 3/3 CI and independent verification.

## Constraints

- Preserve accepted M7 SHA `66e63e33771da7c82c9e0b89c2cd9d7512e748aa` and M6 CLEAN SHA `cda7c10a24a2c48249e6a781a9e5976da69d4562`.
- Do not modify `main` or protected M4/M5 states.
- No M8 PR merge or promotion is implied by this planning artifact.
- No claim of statistical representativeness, live usability or project completion percentage.
- If the diagnostic sample shows a quality problem, investigate and fix the underlying mechanism; do not reduce the rubric or weaken tests.


## Initial diagnostic results — 2026-10-09

The first-pass desk score covers 43 Claims across 12 slices at corpus SHA `66e63e33771da7c82c9e0b89c2cd9d7512e748aa`. D (depth) distribution: 3 scores of 0, 15 of 1, 23 of 2, 2 of 3 (mean 1.56). E (evidence fit): 0/5/25/13 at scores 0/1/2/3 (mean 2.19). B (boundary discipline): 0/4/19/20 (mean 2.37). These are descriptive scores for a purposive sample, not a population estimate or project-completion percentage.

The most important signal is that depth is weaker than evidence linkage/boundaries in this sample. The three `mechanics-basics` Claims are meta-statements rather than mechanics principles, while their Evidence Use descriptions are generic. Two `statistics-basics` Evidence Use records are generic. The `water` package lacks machine-readable Context/Scope Records despite useful README limitations. `governance-basics` mixes English Claims/README with Russian Context/Scope.

Twelve slice-level Human View desk reviews: H1 findability mean 2.42; H2 comprehension mean 2.33; H3 safe interpretation mean 2.58 (each n=12). This is not a live novice study. See the complete claim-by-claim table and rationale in `M8-INITIAL-DEPTH-DIAGNOSTIC-2026-10-09.md`.

### Controlled scope selected from evidence

The M8 correction scope is limited to four confirmed targets: `mechanics-basics`, `statistics-basics`, `water`, and `governance-basics`. Scope details and exclusions are locked in `M8-CORRECTION-SCOPE-LOCK-2026-10-09.md`. No new Record type, Relation, or unrelated rewrite is authorized. Existing accepted M7 content is not retroactively reopened; M8 repairs are isolated on this successor branch.


## Controlled correction status — 2026-10-09

The first correction pass has been implemented on the M8 branch:
- `mechanics-basics`: three substantive Newton-law Claims, specific Evidence Use, improved Context/Scope/README and strengthened regression.
- `statistics-basics`: Claims B/C and Evidence Use tightened; precise OpenStax experimental-design source/evidence added; regression strengthened.
- `water`: machine-readable Context/Scope added with regression assertions.
- `governance-basics`: Claims, README and Evidence Use descriptions normalized to Russian; regression strengthened.

The unified finding ledger is `RELEASE/M8-UNIFIED-DEBT-MAP-2026-10-09.md`. These changes are not yet accepted: schema/semantic checks, targeted tests, post-correction audits, actual-tree coverage verification and same-HEAD Reference + Release Gate + Offline Edition 3/3 are still required. The measured 43-Claim scores remain a historical pre-correction baseline and must not be silently replaced with post-correction scores.
