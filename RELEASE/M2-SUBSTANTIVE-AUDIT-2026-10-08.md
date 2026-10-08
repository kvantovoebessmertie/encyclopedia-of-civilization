# M2 SUBSTANTIVE AUDIT — 2026-10-08

## Baseline

- Protected M1 CLEAN checkpoint: `0019aa2376fd45ecc063f3f6ee680e087ab8d729`
- Fresh M2 Content Gap Map: `2f19e7b1b70dbfb3aecd18b476dbd7d127a13a45`
- M2 scope lock: `8e6e887e186eab40f60e8d0b2107397a7b6a3397`
- Corpus at Gap Map baseline: 479 vertical slices / 4619 Records / 19 Record types / 51 Relations.

## Audit scope

Six existing slices were reviewed without modifying their content:

1. `measurement-uncertainty-basics`
2. `statistics-basics`
3. `risk-management-basics`
4. `agriculture-basics`
5. `energy-security-basics`
6. `geographic-coordinates-basics`

The substantive pass evaluates semantic correctness, claim adequacy for the declared educational scope, applicability boundaries, and Claim → Evidence Use linkage. Evidence independence is intentionally left to the next audit stage.

## Result

**SUBSTANTIVE AUDIT: PASS for content correctness; M2 remains OPEN.**

No semantic correction to a Claim is justified at this stage.

### 1. measurement-uncertainty-basics — PASS

- Three Claims are coherent with the declared basic educational scope.
- Claim A correctly links measurement results with an uncertainty statement.
- Claim B correctly distinguishes measurement uncertainty from measurement error.
- Claim C correctly places measurand definition and the measurement model inside uncertainty evaluation.
- Scope and Context prevent the slice from presenting itself as an exhaustive metrology reference.

External semantic verification: NIST TN 1297 and the VIM terminology support the stated concepts.

**No substantive content correction authorized.**

### 2. statistics-basics — PASS with applicability watch

- Claims A–C are semantically coherent and mutually consistent.
- The claims correctly emphasize data description/analysis, method assumptions and data acquisition, and the dependence of conclusions on study design.
- The NIST/SEMATECH source is relevant to statistical methods and explicitly covers underlying assumptions and experimental design.
- The source is engineering/scientific in orientation, so broader transfer of the slice must remain bounded by the existing Scope/Context.

**No substantive content correction authorized.**

Applicability/source-diversity review remains open for the next stage.

### 3. risk-management-basics — PASS

- Claim A correctly describes risk management as a systematic process for handling uncertainty in decision-making.
- Claim B correctly preserves the objective/context dependence of risk.
- Claim C correctly describes integration with governance and decision-making rather than post-event checking only.
- Scope explicitly prevents substitution for jurisdictional, professional or operational requirements.

The claims align with ISO 31000:2018, which remains the current published edition.

**No substantive content correction authorized.**

### 4. agriculture-basics — PASS

- Claims A–C are appropriately general and do not prescribe a universal farming practice.
- Context explicitly states dependence on crop, environment and management.
- Scope correctly excludes individualized agronomic recommendations.
- The current slice already contains two source records (FAO and independent USDA Climate Hubs evidence) and a dedicated corroborating Evidence Use.

**Important metadata finding:** the fresh Gap Map describes `agriculture-basics` as a 9-Record / single-source slice, but the actual current tree contains 11 Records and 2 source records. This is a confirmed Gap Map/actual-tree synchronization debt, not a substantive content debt.

**No substantive content correction authorized.**

### 5. energy-security-basics — PASS

- Claim A correctly frames energy security around reliable/affordable access and resilience to supply disruption.
- Claim B correctly identifies geopolitical, cyber, supply-chain and weather-related risk classes.
- Claim C correctly makes assessment dependent on fuel, infrastructure, time horizon and regional context.
- Scope appropriately prevents the basic slice from becoming project-specific or jurisdiction-specific advice.

External verification against current IEA material confirms the conceptual framing and the importance of context, resilience and differing fuel/system dimensions.

**No substantive content correction authorized.**

Evidence-diversity review remains open.

### 6. geographic-coordinates-basics — PASS

- Claim A correctly identifies coordinates as a way to specify location.
- Claim B correctly identifies latitude and longitude as the basic geographic coordinate pair.
- Claim C correctly makes precision and coordinate-system choice task-dependent.
- Context and Scope prevent direct transfer into specialized operational use without additional context.

The cited USGS educational source itself covers coordinate systems, latitude/longitude, precision, datums and the use-dependent choice between coordinate systems.

**No substantive content correction authorized.**

Evidence-diversity review remains open.

## Confirmed findings after substantive pass

### M2-SUB-01 — Gap Map synchronization debt

**Severity:** documentation/metadata, not semantic content.

The fresh M2 Gap Map states that `agriculture-basics` has 9 Records and one source. The actual current tree and its dedicated regression show 11 Records and two source records.

Required later action:
- reconcile the Gap Map against the actual M2 baseline;
- do not remove or rewrite the already-valid USDA corroboration;
- re-run coverage/regression after metadata synchronization.

This finding is sufficient to keep M2 open, but it does not authorize content correction.

## Deferred audit stages

The following are deliberately not closed by this substantive pass:

1. evidence independence/diversity;
2. Human View/adversarial audit;
3. cross-domain Relation audit;
4. unified M2 Debt Map;
5. correction pass;
6. substantive re-audit;
7. exact-head Reference + Release Gate + Offline verification.

## Closure rule

M2 must not be marked CLEAN from this audit alone.

The next controlled step is the **evidence-independence/diversity audit** of the six scoped slices, with confirmed findings only.
