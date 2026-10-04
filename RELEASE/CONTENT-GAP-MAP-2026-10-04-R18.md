# Gap Map R18 — controlled Wave 18

Date: 4 October 2026

Baseline: **428 vertical slices / 3827 records / 19 Record types / 0 blocking findings**.

## Selection basis

R18 reconciles the current corpus with the practical knowledge needed for future end-to-end human tasks. Priority is given to non-duplicate domains with strong authoritative sources, cross-domain leverage, and high Human View value. No new Record type is introduced.

## Controlled ten-slice set

1. `timber-engineering-basics` — wood as an engineering material, moisture, structural safety.
2. `fire-protection-and-life-safety-basics` — building fire protection, life safety and egress context.
3. `foundation-engineering-basics` — foundations, loads, ground conditions and design boundaries.
4. `building-envelope-basics` — heat, air and moisture interaction in building envelopes.
5. `indoor-air-quality-basics` — indoor pollutants, ventilation and contextual IAQ.
6. `acoustics-basics` — environmental noise, exposure and health context.
7. `accessibility-basics` — accessibility and universal-design principles.
8. `construction-safety-basics` — construction hazards and safety boundaries.
9. `land-use-planning-basics` — land use, spatial planning and site context.
10. `construction-project-management-basics` — project objectives, participants, time, cost, quality and risk.

## Controlled slice contract

**Source → 3 Claims → 3 Evidence Use → Context → Scope + dedicated regression test**

## Expected increment

**10 slices / 90 records**

Target after authoring: **438 vertical slices / 3917 records / 19 Record types**.

## Boundaries

The wave remains descriptive and source-bounded. It does not produce site-specific structural calculations, construction plans, legal determinations, or hazardous operational procedures. Jurisdiction, site conditions, professional review and applicable standards remain explicit constraints.

## Definition of Done

R18 remains open until all ten slices pass dedicated regressions, corpus coverage is synchronized, Human View and evidence boundaries pass, package/recovery integrity passes, Reference Tests/Release Gate/Offline Edition are green, substantive audit finds zero blocking findings, and the resulting CLEAN checkpoint is evidenced.
