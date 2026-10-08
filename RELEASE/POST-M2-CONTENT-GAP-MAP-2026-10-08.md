# Post-M2 Content Gap Map — 2026-10-08

## Baseline
- Protected M2 CLEAN checkpoint: `bfd0578ca6f8dae9093a96de4f2bf6139589a40f`
- 479 vertical slices / 4655 Records / 19 Record types
- 577 Sources / 1582 Evidence Use / 57 Relations
- M2 is closed and is not reopened.

## Fresh structural scan
The actual M2 CLEAN tree was scanned. The Record distribution is:
- 1 slice with 7 Records
- 385 slices with 9 Records
- 11 slices with 10 Records
- 22 slices with 11 Records
- 25 slices with 12 Records
- 21 slices with 13 Records
- 1 slice with 14 Records
- 11 slices with 15 Records
- 1 slice with 22 Records
- 1 slice with 57 Records

394 slices currently have one Source record. Record/source count is only a screening signal; it is not a quota.

## Candidate areas for substantive verification
These are candidates only, not a locked scope:
1. `fire-safety-basics` — 9 Records / 1 Source; high-consequence reuse.
2. `shelter-basics` — 9 / 1; practical cross-domain reuse.
3. `energy-basics` — 9 / 1; foundational dependency across energy domains.
4. `water-resources-basics` — 9 / 1; foundational dependency across water, agriculture and infrastructure.
5. `food-preservation-basics` — 9 / 1; practical food-security dependency.
6. `scientific-method-basics` — 9 / 1; foundational epistemic dependency.
7. `emergency-management-basics` — 9 / 1; high-consequence cross-domain reuse.

## Selection boundary
The next scope must exclude already matured M2 slices, prior maturation scopes, and slices whose substantive audit shows no real maturity asymmetry.

No fixed number of candidates is imposed. No new content or Relation is authorized by this Gap Map.

## Next step
Verify candidate Claims, Sources, Evidence Use, Scope/Context and existing Relations. Only after that lock the next controlled maturation scope.

**Sequence:** Gap Map → candidate verification → scope lock → substantive audit → evidence independence → Human View → Relation audit → Debt Map → controlled correction → re-audit → docs/coverage/regressions → exact-head 3/3 CI → CLEAN.
