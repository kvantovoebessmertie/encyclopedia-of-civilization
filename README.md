# Энциклопедия цивилизации

> Чтобы знания пережили нас.

**Энциклопедия цивилизации** — открытая библиотека проверяемых и долговечных знаний, предназначенная для сохранения, передачи и практического применения человеческого опыта независимо от времени, места и доступности современных технологий.

## Текущий статус

**M4 — CLOSED CLEAN.** Защищённый принятый content HEAD: `83b2e3185cd92c55d53a5ce661be384508870e1a`. M4 не переоткрывается.

Текущий рабочий этап — **M5 controlled content maturation** в отдельной ветке `m5-content-maturation-2026-10-09`:

- **479 vertical slices**
- **4753 Records**
- **19 Record types**
- **601 Sources**
- **1634 Evidence Use**
- **63 Relations**
- M5 scope: 9 существующих срезов; новые срезы и Record types не добавлялись
- Substantive audit: **PASS — content level**
- Evidence-independence audit: **PASS — slice level; single-source Claims explicitly recorded**
- Human View/adversarial audit: **PASS — content level**
- Relation audit: **PASS**
- Exact-head Reference tests: **PENDING**
- Release Conformance Gate: **PENDING**
- Offline Edition: **PENDING**
- M5 CLEAN checkpoint: **NOT CLAIMED**

M5 не считается закрытым до GREEN всех трёх CI-проверок на одном и том же окончательном HEAD и финального post-CI re-audit. Счётчики корпуса сами по себе не подтверждают истинность утверждений.

**M4 CLEAN baseline:** 479 vertical slices / 4698 Records / 19 Record types / 601 Sources / 1634 Evidence Use / 63 Relations. Подробности — `RELEASE/M4-CLEAN-CHECKPOINT-2026-10-08.md`.

## Главная цель

Создать понятную, проверяемую и долговечную систему знаний, которая поможет человеку:

- сохранять жизнь и здоровье;
- находить и очищать воду;
- добывать и готовить пищу;
- строить жильё;
- создавать инструменты и материалы;
- выращивать растения и содержать животных;
- восстанавливать ремёсла, производство и технологии;
- передавать знания следующим поколениям.

## Основные принципы

1. Истина выше авторитета.
2. Каждое важное утверждение должно быть проверяемым.
3. Научное знание и подтверждённый практический опыт дополняют друг друга.
4. История изменений должна сохраняться.
5. Опасные инструкции требуют усиленной экспертной проверки.
6. Иллюстрации обязательны там, где без них трудно понять действие или объект.
7. Знания должны быть доступны офлайн.
8. Проект не должен зависеть от одной платформы, компании или технологии.
9. Ошибки должны исправляться открыто.
10. Знания должны оставаться понятными людям без специального образования.

## Как развивается корпус

Следующая фаза оптимизирует не только количество срезов, но и их зрелость:

**breadth → depth → independent triangulation → cross-domain integration → Human View validation → CLEAN checkpoint**

Новые вертикальные срезы продолжаются там, где Gap Map показывает существенный пробел. Приоритет также отдаётся углублению важных, рискованных и высокозависимых существующих срезов.

## Что означает зрелый срез

Одного прохождения schema/CI недостаточно для зрелого знания. В зависимости от предметной области зрелый срез должен иметь:

- достаточную разнообразность источников;
- явное использование доказательств;
- контекст и область применимости;
- разделение known / unknown;
- обработку существенных противоречий;
- полезные cross-domain связи;
- понятное Human View представление;
- усиленную проверку для safety-sensitive и high-consequence знаний.

## Основание

Проект начат 27 июля 2026 года.

Версия фундамента: `0.0.1`

Текущий Reference Implementation: `0.1.0`

Текущий conformance state: **CONFORMING** для объявленного Reference Implementation applicability contour.

Подробный readiness-аудит: `RELEASE/PROJECT-READINESS-AUDIT-2026-10-05.md`

План следующей фазы: `RELEASE/READINESS-ROADMAP-2026-10-05.md`


## M2 post-correction status — 8 October 2026

M2 substantive debt is closed after controlled evidence-independence and cross-domain linkage corrections. The audited state is **479 vertical slices / 4655 Records / 19 Record types / 577 Sources / 1582 Evidence Use / 57 Relations**. Human View remains PASS; no Claim rewrite was required. The protected M2 CLEAN checkpoint `bfd0578ca6f8dae9093a96de4f2bf6139589a40f` is CLOSED CLEAN after exact-head Reference, Release Conformance Gate and Offline Edition GREEN.


## M3 CLEAN status — 8 October 2026

M3 is CLOSED CLEAN at the protected checkpoint `2434f3a06618543b4534ff4b12a45ad0b87e10f4`. The six-slice scope passed substantive, evidence-independence, Human View and Relation review; exact-head Reference, Release Gate and Offline CI were GREEN. Historical M3 baseline: **479 vertical slices / 4674 Records / 19 Record types / 583 Sources / 1588 Evidence Use / 63 Relations**.

## M4 CLEAN status — 9 October 2026

M4 is CLOSED CLEAN at accepted content HEAD `83b2e3185cd92c55d53a5ce661be384508870e1a`. Its checkpoint, post-correction audits and exact-head Reference, Release Gate and Offline results are recorded in `RELEASE/M4-CLEAN-CHECKPOINT-2026-10-08.md` and `RELEASE/M4-UNIFIED-DEBT-MAP-2026-10-08.md`.
