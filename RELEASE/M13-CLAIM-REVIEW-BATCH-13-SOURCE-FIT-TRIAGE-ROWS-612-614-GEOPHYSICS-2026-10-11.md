# M13 Batch 13 — source-fit triage (rows 612–614): geophysics

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; stored source locator appears mismatched to the stated subject**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional, not finalized ledger scores. No canonical JSON changed.

## Source trail

All three Claims cite `SRC-GEOPHYSICS_BASICS`, labelled “USGS — Geophysics,” but its stored URI is `https://www.usgs.gov/glossary/earthquake-hazards-program`. That locator is an earthquake-hazards glossary, not a clearly identified general geophysics reference. USGS does have relevant general material: its “Become an Earthquake Scientist” page describes geophysicists studying Earth with gravity, magnetic, electrical and seismic methods, while its groundwater geophysical-methods page lists surface and borehole techniques. These alternatives support parts of the subject but are not the current stored source, and should not silently be substituted into the record. citeturn808355search11turn808355search5

All three Evidence Use records contain a general description without quoted passages, section names, or pinpoint locators. Treat the current source chain as structurally linked but substantively unresolved.

## 1. `CLM-GEOPHYSICS_BASICS-A` — **D2 / E0 / B2**

**Claim:** “Геофизика применяет физические измерения и математические модели для изучения строения и динамики Земли.”

**Assessment:** Gives a concise method-and-purpose summary but does not explain measurement-to-inference limits (D2). The stored earthquake-hazards glossary locator is not demonstrated to support this general definition, and the Evidence Use has no pinpoint (E0). The claim is reasonably bounded to the field, though it groups measurements and models without describing their roles (B2).

**Disposition:** Replace/reconcile the stored source with an explicitly relevant geophysics reference, then add a pinpoint supporting both physical measurements and modeling.

## 2. `CLM-GEOPHYSICS_BASICS-B` — **D2 / E0 / B2**

**Claim:** “Гравитационные, магнитные, сейсмические и другие физические измерения позволяют получать сведения о внутренних структурах Земли.”

**Assessment:** Identifies several methods and their inferential use but does not distinguish which properties each method measures or the uncertainty of interpretation (D2). The current stored locator does not establish the full method list; no claim-specific pinpoint is present (E0). “Позволяют получать сведения” is appropriately less absolute than claiming direct observation, but does not state resolution or limits (B2).

**Disposition:** Use a direct source on geophysical methods and their inference of subsurface structure; retain the indirect-inference wording and document limitations.

## 3. `CLM-GEOPHYSICS_BASICS-C` — **D2 / E0 / B1**

**Claim:** “Геофизические методы могут сочетать наблюдения на поверхности, дистанционные измерения и модели для интерпретации недоступных напрямую областей.”

**Assessment:** The statement conveys indirect investigation but bundles surface observations, remote measurements, and modeling without naming which methods combine them (D2). The stored locator and boilerplate Evidence Use do not support this specific combination (E0). “Дистанционные измерения” and “недоступных напрямую областей” are broad and could conflate distinct method classes (B1).

**Disposition:** Narrow the statement to named methods supported by the chosen source, or split it into separate claims with precise evidence.

## Batch accounting

- Individual Claims triaged: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Source identity/locator mismatch: **open**.
- Exact source pinpoints recorded in canonical Evidence Use: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
