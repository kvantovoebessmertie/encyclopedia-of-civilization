# Первая редакция — карта 19 глав, тематических срезов и фактического покрытия

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: карта соответствия редакционной структуры существующим кандидатным реестрам; не publication allowlist.

## 1. Результат сверки

Редакционная структура из 19 глав сопоставлена с существующими Part I / Part II кандидатными реестрами и картой тематических срезов.

| Область | Фактический охват на проверенных реестрах | Что это означает |
|---|---:|---|
| Часть I — выживание | 94/94 тематических среза структурно учтены; 980/980 файлов записей прошли первичный скрининг | Инвентаризация и первичный скрининг завершены; это не означает допуска к публикации |
| Часть II — фундаментальные и цивилизационные знания | 124/385 тематических срезов представлены в exact-version master; 1 146 уникальных строк record/version | Это ограниченный кандидатный корпус, а не весь Part II и не готовый выпуск |
| Part II exact-version rows | 352 Claim, 408 Evidence Use, 171 Source, 107 Context, 108 Scope; всего 1 146 | В проверенной таблице все 1 146 строк имеют HOLD |
| Relations | 63/63 записей прошли инвентаризацию и семантический просмотр; отдельные Relation HOLD остаются | Relations не включаются автоматически из тематической близости |

Part II содержит отдельную служебную метку cross-slice-linkage; она не является самостоятельной тематической главой и исключена из числа 124 тематических срезов. В master представлены 125 различных значений поля slice, включая эту служебную метку.

**Главный вывод:** у нас есть структурно очерченный материал для всех 19 глав, но структурное наличие среза не равно наличию публикационно допущенных записей. На момент сверки нет подтверждённого production INCLUDE manifest.

## 2. Часть I — карта кандидатов по главам 1–10

Срезы ниже — существующие тематические кандидаты из Opening Survival and Domain Map. Список не объявляет их допущенными и не отменяет дополнительные записи/зависимости в controlling register.

| Глава | Основные существующие срезы-кандидаты |
|---:|---|
| **1. Чрезвычайные ситуации и организация действий** | emergency-alert-warning; disaster-response-basics; emergency-management-basics; disaster-risk-reduction-basics; humanitarian-logistics-basics |
| **2. Вода: ресурсы, качество и хранение** | water; water-resources-basics; water-filter-assessment; water-treatment-basics; chemical-water-advisory; emergency-water-storage-state; water-infrastructure-basics; hydrology-basics; wastewater-basics; wastewater-engineering-basics |
| **3. Пища, питание и продовольственная устойчивость** | power-outage-food; flood-food-safety; food-security-basics; food-safety-basics; food-preservation-basics; food-science-basics; nutrition-basics; nutrition-science-basics |
| **4. Укрытие, жильё и строительство** | shelter-basics; construction-basics; housing-systems-basics; architecture-basics; civil-engineering-basics; human-settlement-systems-basics |
| **5. Здоровье, гигиена и санитария** | emergency-hand-hygiene; emergency-waste-sanitation; septic-system-emergency; sanitation-basics; waste-management-basics; public-health-basics; environmental-health-basics; burn-first-aid; anatomy-basics; physiology-basics; microbiology-basics; epidemiology-basics; nutrition-basics; sleep-basics |
| **6. Тепло, огонь, электричество и энергия** | fire; home-fire-smoke-safety; wildfire-smoke-safety; fire-safety-basics; extreme-heat-safety; cold-weather-hypothermia; carbon-monoxide-heating-safety; generator-carbon-monoxide-safety; emergency-lighting-safety; electricity-basics; electrical-safety-basics; energy-basics; energy-systems-basics; energy-storage-basics; renewable-energy-basics |
| **7. Инструменты, материалы, ремонт и производство** | hand-tool-safety; materials-basics; materials-science-basics; manufacturing-basics; manufacturing-systems-basics; robotics-basics |
| **8. Сельское хозяйство, почва и живые ресурсы** | agriculture-basics; early-agriculture; soil-basics; seed-storage-basics; plant-biology-basics; plant-physiology-basics; forestry-basics; fisheries-basics; livestock-systems-basics; zoology-basics; ecology-basics; ecosystems-basics; food-fermentation-basics |
| **9. Природные и экологические опасности** | earthquake-protective-action; earthquake-aftershock-safety; flood; flood-cleanup-safety; flood-food-safety; weather-basics; climate-basics; geology-basics; seismology-basics; volcanology-basics; wildfire-smoke-safety; ocean-basics |
| **10. Связь, навигация, транспорт и логистика** | maps-and-navigation-basics; geographic-coordinates-basics; telecommunications-basics; networks-basics; public-risk-communication-basics; transportation-basics; public-transport-basics; humanitarian-logistics-basics; infrastructure-basics |

### Важные пересечения Part I

- flood-food-safety относится и к продовольственной безопасности, и к наводнениям; в навигации допускается несколько точек входа, но запись не дублируется.
- wildfire-smoke-safety и humanitarian-logistics-basics могут иметь несколько тематических точек входа.
- Водоснабжение, очистка, санитария и сточные воды — разные предметные контуры; нельзя сводить их к одной универсальной «инструкции по воде».
- Аварийные, медицинские, электрические, химические и строительные процедуры требуют усиленной проверки и могут быть исключены из первой редакции даже при наличии главы.

## 3. Часть II — полный список 124 представленных тематических срезов

Ниже каждому из 124 Part II slice IDs присвоена одна первичная глава. Кросс-ссылки в интерфейсе возможны, но первичная принадлежность нужна для учёта покрытия и предотвращения двойного счёта. Все срезы в текущем master остаются HOLD.

### Глава 11. Математика и измерения — 9 срезов

- algebra-basics
- calculus-basics
- geometry-basics
- measurement-uncertainty-basics
- probability-basics
- ratios-and-percentages
- si-units-basics
- statistics-basics
- units-and-measurement

### Глава 12. Физические науки — 9 срезов

- electromagnetism-basics
- fluid-mechanics-basics
- magnetism-basics
- matter-basics
- motion-basics
- optics-basics
- temperature-basics
- thermodynamics-basics
- waves-and-sound-basics

### Глава 13. Химические науки — 6 срезов

- acid-base-basics
- analytical-chemistry-basics
- biochemistry-basics
- chemical-reactions-basics
- mixtures-and-solutions
- organic-chemistry-basics

### Глава 14. Науки о жизни — 20 срезов

- antimicrobial-resistance-basics
- biodiversity-basics
- cell-basics
- cell-biology-basics
- conservation-biology-basics
- developmental-biology-basics
- ecophysiology-basics
- ecotoxicology-basics
- entomology-basics
- evolution-basics
- genetics-basics
- immunology-basics
- marine-biology-basics
- parasitology-basics
- pathology-basics
- plant-pathology-basics
- soil-microbiology-basics
- soil-science-basics
- vaccination-information-basics
- virology-basics

### Глава 15. Земля, климат и космос — 12 срезов

- astronomy-basics
- astronomy-observation-basics
- climate-science-basics
- earth-system-basics
- historical-geography-basics
- oceanography-basics
- remote-sensing-basics
- settlement-geography-basics
- solar-system-basics
- water-quality-basics
- water-resource-management-basics
- water-security-basics

### Глава 16. Инженерия и вычисления — 12 срезов

- agricultural-engineering-basics
- artificial-intelligence-basics
- computer-networks-basics
- computer-science-algorithms-basics
- cybersecurity-basics
- databases-basics
- distributed-systems-basics
- electrical-grid-basics
- hydraulic-engineering-basics
- infrastructure-resilience-basics
- mechanics-basics
- software-engineering-basics

### Глава 17. Науки о человеке — 3 среза

- learning-basics
- neuroscience-basics
- psychology-basics

### Глава 18. Общество и институты — 25 срезов

- accounting-basics
- administrative-law-basics
- civil-society-basics
- comparative-law-basics
- democratic-institutions-basics
- demography-basics
- economics-basics
- education-systems
- governance-basics
- international-law-basics
- labor-economics-basics
- law-basics
- macroeconomics-basics
- microeconomics-basics
- migration-and-mobility-basics
- migration-basics
- money-and-banking-basics
- organizational-behavior-basics
- political-economy-basics
- public-administration-basics
- public-budgeting-basics
- social-policy-basics
- social-statistics-basics
- sociology-basics
- taxation-basics

### Глава 19. История и культура — 22 среза

- ancient-civilizations-basics
- anthropology-basics
- archaeology-basics
- archival-science-basics
- chronology-methods
- comparative-civilizations-basics
- cultural-anthropology-basics
- cultural-heritage-basics
- ethics-basics
- history-of-engineering-basics
- history-of-mathematics-basics
- history-of-medicine-basics
- history-of-science-basics
- history-of-technology-basics
- library-science-basics
- linguistics-basics
- literature-basics
- philosophy-basics
- religious-studies-basics
- state-formation
- trade-networks
- writing-systems

### Шесть Part II срезов с первичным входом в Part I

Эти записи входят в Part II exact-version master, но по пользовательскому смыслу открывают практические главы первой части. Они учитываются в Part II master и не добавляются повторно к Part I slice denominator.

- Глава 1: disaster-recovery-basics; disaster-response-logistics-basics.
- Глава 3: food-distribution-basics; food-systems-basics.
- Глава 8: agrifood-systems-basics.
- Глава 10: cartography-basics.

Контрольная сумма: 9+9+6+20+12+12+3+25+22 = 118 срезов в главах 11–19; плюс 6 срезов с первичным входом в Part I = ровно 124 уникальных Part II slice IDs. Служебный cross-slice-linkage исключён.

## 4. Что из этого следует для первой редакции

1. **Часть I структурно широка.** Не нужно заново инвентаризировать все 94 среза. Следующая работа — выбирать отдельные Claims и полные зависимости из существующих screened records, переиспользуя закрытые P1/P2/M3 проверки там, где exact-version evidence восстановлено.
2. **Part II не должен быть сведен к математике и физике.** В первом выпуске нужно стремиться к минимальному представительству всех девяти цивилизационных доменов, но только там, где конкретные записи проходят допуск.
3. **Первая редакция может иметь пустые подтемы.** Интерфейс показывает карту знаний и честно помечает темы, которые ещё не опубликованы.
4. **Не все 124 Part II slices должны попасть в первый выпуск.** 124/385 — охват кандидатного инвентаря, а не план обязательной публикации.
5. **Не нужно начинать новые широкие аудиты.** Следующий шаг — exact-version выборка из уже представленных срезов и закрытие конкретных release blockers.
6. **Высокорисковые практические темы не должны ускоряться ради красивого оглавления.** Их можно оставить в структуре, пока они не прошли нужную проверку.

## 5. Обязательная техническая сверка перед заморозкой

- Машинно извлечь все slice IDs из master и убедиться, что Part II primary mapping покрывает ровно 124 из 124 зарегистрированных тематических slice IDs, исключая cross-slice-linkage.
- Сверить Part I 94 slices с контролирующим record-level register, не считать пересечения между главами как отдельные срезы.
- Для каждой кандидатной записи зафиксировать exact ID@version, тип, источник, Evidence Use, Context/Scope и все прямые зависимости.
- Отдельно пометить высокорисковые темы, требующие qualified review.
- Не переводить HOLD в INCLUDE без прав, редакционной ответственности, точной версии, dependency closure и явного owner/editor approval.
- После любых canonical changes повторно проверить все четыре обязательных CI workflow на одном immutable HEAD.

## 6. Решения и статусы, которые остаются вне полномочий этой карты

R-01–R-10 по правам, лицензиям, авторству, редакционной ответственности, release approver и correction/takedown процессу остаются решениями владельца проекта. Ни эта карта, ни зелёный CI не заменяют их.

Никакие canonical Claim/Evidence Use/Source/Context/Scope/Relation записи, версии, candidate decisions, allowlist, content coverage manifest, production state, main или deployment не изменены этим документом.
