# M2 Content Gap Map — 2026-10-08

## Baseline

- Protected M1 CLEAN HEAD: `0019aa2376fd45ecc063f3f6ee680e087ab8d729`
- Corpus: 479 vertical slices / 4619 Records / 19 Record types
- Relations: 51 total
- M1 is CLOSED CLEAN and is not reopened without verified regression.

## Audit method

This Gap Map is freshly derived from the M1 CLEAN corpus. It does not reuse the M1 candidate list.

Priority is based on material maturity asymmetry and consequence, not on an artificial number of slices or Records.

The current corpus has 400 slices at the standard 9-record profile (3 Claims, 1 Source, 3 Evidence Use, Context, Scope). Therefore a 9-record profile is not itself a defect. A candidate enters M2 only where the subject's risk/reuse profile makes additional evidence or boundary verification materially valuable.

## Findings

### G1 — High-consequence slices with a single evidence track

The following existing slices are at the 9-record profile and currently have one Source:

- `fire`
- `flood`
- `emergency-management-basics`
- `industrial-process-safety-basics`
- `occupational-safety-basics`
- `risk-management-basics`

These are not declared defective merely because they have one source. They are priority candidates because incorrect interpretation can materially affect safety, emergency decisions, or risk management, and independent corroboration may improve applicability and Human View.

### G2 — Safety semantics and applicability boundaries

For the priority candidates, verify whether the current Claims preserve:
- conditions under which the guidance applies;
- distinction between descriptive knowledge and operational instruction;
- escalation to competent/local emergency authorities where relevant;
- uncertainty and limitations;
- distinction between general principles and jurisdiction/equipment-specific requirements.

No claim is rewritten unless a substantive semantic gap is confirmed.

### G3 — Evidence independence

Audit whether an independent second source materially strengthens a Claim or boundary.

A second source is not added for counting purposes. If the existing source is already sufficient for the Claim, the correct result is to leave it unchanged.

### G4 — Cross-domain linkage

Evaluate only material dependencies, especially:

- fire ↔ emergency management / building and infrastructure systems;
- flood ↔ hydrology / infrastructure / emergency management;
- industrial process safety ↔ risk management / engineering;
- occupational safety ↔ human factors / public health / risk management;
- risk management ↔ decision analysis / probability / safety engineering.

Relations are added only where they improve conceptual reuse.

### G5 — Human View

The candidate set must be readable without turning general safety knowledge into universal instructions. The audit must specifically test for:
- hidden assumptions;
- omitted conditions;
- false certainty;
- missing escalation;
- unsafe interpretation when detached from source context.

## Priority decision

M2 is a controlled **Safety, Risk and Emergency Decision Maturation** package.

Priority scope for substantive audit:

1. `fire`
2. `flood`
3. `emergency-management-basics`
4. `industrial-process-safety-basics`
5. `occupational-safety-basics`
6. `risk-management-basics`

This is a priority-derived scope, not a quota.

## Explicit exclusions

- no reopening of M1;
- no artificial expansion to ten slices;
- no mass rewrite of the 479-slice corpus;
- no second source added solely to increase counts;
- no Relations added for superficial topical overlap;
- no new Record type.

## M2 sequence

1. Substantive audit of the six priority slices.
2. Correct only confirmed debts.
3. Re-audit.
4. Evidence-independence audit.
5. Human View/adversarial audit.
6. Add Relations only where justified.
7. Update unified M2 Debt Map.
8. Full Reference / Release / Offline CI.
9. Exact-head CLEAN checkpoint.
