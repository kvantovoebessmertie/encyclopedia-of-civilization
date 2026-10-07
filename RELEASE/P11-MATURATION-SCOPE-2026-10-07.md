# P11 — Maturation Scope

**Дата:** 2026-10-07  
**Protected baseline:** P10 CLEAN — `2754ec7d154e4c5ba329a8b0a9d234dfa7978e45`  
**Baseline corpus:** 478 vertical slices / 4500 records / 19 record types

## Цель

P11 не расширяет корпус механически. Это первый maturation-блок после P10: поднимаем глубину, независимую доказательность, применимость, связи и Human View у десяти существующих высокоценных срезов.

## Scope

1. `construction-safety-basics`
2. `public-risk-communication-basics`
3. `information-literacy-basics`
4. `privacy-and-data-protection-basics`
5. `mental-health-information-boundaries`
6. `infrastructure-resilience-basics`
7. `risk-analysis-basics`
8. `systems-thinking-basics`
9. `critical-thinking-basics`
10. `safety-engineering-basics`

Все десять выбраны из существующего корпуса; новые vertical slices на этом этапе не создаются. Большинство имеют базовый 9-Record профиль и потому дают измеримый прирост зрелости без искусственного увеличения ширины.

## Definition of Done

Для каждого среза:
- substantive content-depth audit;
- независимая/дополнительная доказательность там, где она оправдана;
- механизм, условия, ограничения и uncertainty;
- applicability boundary;
- justified cross-slice linkage;
- Human View / adversarial audit;
- dedicated regression и registry/coverage synchronization;
- unified debt map;
- повторный аудит после исправлений.

После закрытия substantive work: Reference Tests → Release Gate → Offline Edition → новый CLEAN checkpoint. Любой найденный долг исправляется до технического закрытия P11.

## Архитектурное правило

Новый Record type не вводится. Если аудит покажет реальную семантическую недостаточность модели, сначала фиксируются Entity Discipline + ADR и только затем рассматривается изменение архитектуры.

## Порядок

Protected baseline → substantive audit → evidence/provenance → mechanism/depth → applicability/uncertainty → linkage → Human View → debt closure → re-audit → full CI → CLEAN.
