# M13 Phase 3 — Batch 53 historical Evidence Use / Source recovery, tranche 02

Date: 2026-11-23
Branch: m13-system-wide-depth-audit-2026-10-09
Historical Batch 53 Claim snapshot: 33ef97e7ba6a9e91aebaee198cfead532faa4185
Comparison HEAD: 9e0053a77761afe82373f24918744413b1a9d87f

## 1. Result

This second report-only tranche directly compared 16 additional Batch 53 Evidence Use records and their eight distinct Source records between the exact historical snapshot and the comparison HEAD.

- Evidence Use records: 16/16 exact historical/current Blob matches, all @1.
- Unique Source records: 8/8 exact historical/current Blob matches, all @1.
- Same-version content drift: 0.
- Canonical changes: 0.

Combined Batch 53 recovery to date: 47/100 Evidence Use records, with 21 unique Source records recovered. A separate previously documented Batch 54 sample (CLM-SI-ACCURACY-BOUNDARY@1) remains the only Batch 54 chain included in the recovered count at this point.

## 2. Evidence Use crosswalk

| Slice | Evidence Use ID | Historical/current version | Historical Blob SHA = current Blob SHA |
|---|---|---:|---|
| philosophy-of-mind-basics | EU-PHILOSOPHY_OF_MIND_BASICS-A | 1 | 968e5646f11f35c5b4c9f138ec414069deb237da |
| philosophy-of-mind-basics | EU-PHILOSOPHY_OF_MIND_BASICS-B | 1 | f93a36143677afa2d18c100f732b9ca36b8b0760 |
| philosophy-of-science-basics | EU-PHILOSOPHY_OF_SCIENCE_BASICS-B | 1 | 5bb2514b85729a6875ad5c393a066e8098d34461 |
| philosophy-of-science-basics | EU-PHILOSOPHY_OF_SCIENCE_BASICS-C | 1 | 2a7343f1a1585c2d97ebf9957bdb2006439021b4 |
| planetary-science-basics | EU-PLANETARY_SCIENCE_BASICS-A | 1 | ea9a0a5d1d9e07895699c597bd32bc2c4553cd68 |
| planetary-science-basics | EU-PLANETARY_SCIENCE_BASICS-B | 1 | 5c531282b4c41233da267d23d234df6f48080c38 |
| planetary-science-basics | EU-PLANETARY_SCIENCE_BASICS-C | 1 | 0f8f4eed040ce9a0ff23407cedb32176364361d0 |
| money-and-banking-basics | EU-MONEY_AND_BANKING_BASICS-B | 1 | 634c861f8d571eb06fbdaa43163429ff0a8b63e2 |
| migration-basics | EU-MIGRATION_BASICS-B | 1 | 0e7f0455b8e392106813cfb413abc16947bcf17e |
| quality-control-basics | EU-QUALITY_CONTROL_BASICS-A | 1 | 1aa37cec67341f379edc7a3fe35e0f3b14837142 |
| quality-control-basics | EU-QUALITY_CONTROL_BASICS-B | 1 | 9d23a15cfb112379270c0ca1aeb9191a1a34c211 |
| quality-control-basics | EU-QUALITY_CONTROL_BASICS-C | 1 | 875826259e7fc916192a63eaba443fd771c33472 |
| plant-pathology-basics | EU-PLANT_PATHOLOGY_BASICS-C | 1 | 430f0bacf2b912cc8b50f9327f37486e4b43d84d |
| public-data-basics | EU-PUBLIC_DATA_BASICS-A | 1 | 98dc7fc11e9aa993e9dde6c3e68fc030dad71a34 |
| public-data-basics | EU-PUBLIC_DATA_BASICS-B | 1 | 60cca512db8c58ac0a88e5eb2a20b1cdd50eb04f |
| public-data-basics | EU-PUBLIC_DATA_BASICS-C | 1 | 5950e35b32e850e6ad1c7f385a7e7c02b3eeee39 |

## 3. Source crosswalk

| Slice | Source ID | Historical/current version | Historical Blob SHA = current Blob SHA |
|---|---|---:|---|
| philosophy-of-mind-basics | SRC-PHILOSOPHY_OF_MIND_BASICS | 1 | 2e5e33f96dda2d77b8197926b0272c371ad36332 |
| philosophy-of-science-basics | SRC-PHILOSOPHY_OF_SCIENCE_BASICS | 1 | cf468f6079e4d431fbd3913bd2f5e9b9f4d628e8 |
| planetary-science-basics | SRC-PLANETARY_SCIENCE_BASICS | 1 | 053145979ed3b94957b9d74df28b403d3c31e671 |
| money-and-banking-basics | SRC-MONEY_AND_BANKING_BASICS | 1 | 8cbc10225778ee1025ceb58df1278e7a135c639f |
| migration-basics | SRC-MIGRATION_BASICS | 1 | 2ffcbf2ad91efde76b7429b907c0a5f03084cd9 |
| quality-control-basics | SRC-QUALITY_CONTROL_BASICS | 1 | e1389cab681c36a07bb59cce427833f70d66c341 |
| plant-pathology-basics | SRC-PLANT_PATHOLOGY_BASICS | 1 | 3f765ffd679f2239d6b9dbdc9c3ec80e8c5ba541 |
| public-data-basics | SRC-PUBLIC_DATA_BASICS | 1 | a9c08f6b97c787e066846fc5227717fa9d127864 |

## 4. Boundaries

- The prior tranche 01 report records 31 additional Batch 53 EU records and 13 Source records; this tranche adds 16 EU records and eight more unique Source records.
- Combined: 47/100 Batch 53 EU records and 21 unique Batch 53 Source records have exact historical provenance recorded across tranches 01–02.
- One Batch 54 sample (EU-SI-ACCURACY-BOUNDARY@1 → SRC-BIPM-SI-BROCHURE-2026@1) was separately checked and has exact historical/current Blob equality; it is not included in Batch 53 counts.
- Blob equality establishes exact record-content identity at the compared refs. It does not establish source-passage support, locator reproducibility, independence, rights, specialist review, Human View, or publication eligibility.
- Historical D/E/B is not transferred. No current D/E/B assessment is created.
- No canonical records, allowlists, publication decisions, or main files were changed. PR #21 remains Draft/unmerged.
