# M13 Phase 3 — Batch 53 historical Evidence Use / Source recovery, tranche 01

Date: 2026-11-23
Branch: `m13-system-wide-depth-audit-2026-10-09`
Historical Batch 53 Claim snapshot: `33ef97e7ba6a9e91aebaee198cfead532faa4185`
Comparison HEAD: `9e0053a77761afe82373f24918744413b1a9d87f`

## 1. Result

A direct Git-object comparison was completed for the first 31 Batch 53 Claim → Evidence Use → Source chains across ten slices.

- Evidence Use records inspected: **31/31**.
- Exact historical/current Evidence Use Blob SHA matches: **31/31**.
- Evidence Use versions confirmed: **31/31 @1**.
- Unique Source records inspected: **13/13**.
- Exact historical/current Source Blob SHA matches: **13/13**.
- Source versions confirmed: **13/13 @1**.
- Same-version content drift found in this tranche: **0**.
- Historical version labels inferred from names: **0**.

The comparison used the exact historical Batch 53 snapshot and the current M13 HEAD. For each EU, the record version and `source_ref.record_id` were parsed from the historical and current JSON; the corresponding Source JSON was then fetched at both refs. Blob SHAs were compared directly. These are provenance findings only.

## 2. Row-level Evidence Use crosswalk

| Slice | Evidence Use ID | Historical version | Current version | Historical Blob SHA | Current Blob SHA | Result |
|---|---|---:|---:|---|---|---|
| media-literacy-basics | `EU-MEDIA_LITERACY_BASICS-A` | 1 | 1 | `ce88c390fe08f472d887c2a33e5fc6af927343c4` | `ce88c390fe08f472d887c2a33e5fc6af927343c4` | EXACT |
| media-literacy-basics | `EU-MEDIA_LITERACY_BASICS-B` | 1 | 1 | `5fed74611e80ce9e4e7f428fa28f5fffa0f051c3` | `5fed74611e80ce9e4e7f428fa28f5fffa0f051c3` | EXACT |
| media-literacy-basics | `EU-MEDIA_LITERACY_BASICS-C` | 1 | 1 | `cbd7bf5b10e443f4df2f674268a04323f7f24c59` | `cbd7bf5b10e443f4df2f674268a04323f7f24c59` | EXACT |
| metaphysics-basics | `EU-METAPHYSICS_BASICS-A` | 1 | 1 | `e6c6898d50a25bf279c270d32e2a7cd4f2d647c9` | `e6c6898d50a25bf279c270d32e2a7cd4f2d647c9` | EXACT |
| metaphysics-basics | `EU-METAPHYSICS_BASICS-B` | 1 | 1 | `974d76541dce8d75abb165c1d8986e570ca28e39` | `974d76541dce8d75abb165c1d8986e570ca28e39` | EXACT |
| modeling-and-simulation-basics | `EU-MODELING_AND_SIMULATION_BASICS-A` | 1 | 1 | `792332ab0b7fed9e41cfb1f831192647e536867f` | `792332ab0b7fed9e41cfb1f831192647e536867f` | EXACT |
| modeling-and-simulation-basics | `EU-MODELING_AND_SIMULATION_BASICS-B` | 1 | 1 | `fa58f1beea46828cd19c3d7e89249b48f8f1b63b` | `fa58f1beea46828cd19c3d7e89249b48f8f1b63b` | EXACT |
| modeling-and-simulation-basics | `EU-MODELING_AND_SIMULATION_BASICS-C` | 1 | 1 | `c0b7dc0acd0d9013b50aefbdaf6a1d6e17ca9bf4` | `c0b7dc0acd0d9013b50aefbdaf6a1d6e17ca9bf4` | EXACT |
| modeling-basics | `EU-MODELING_BASICS-A` | 1 | 1 | `841bbb36d47169437b7b71d317a3855408fd0522` | `841bbb36d47169437b7b71d317a3855408fd0522` | EXACT |
| modeling-basics | `EU-MODELING_BASICS-B` | 1 | 1 | `8d21ea03952b325c1646fc62e19b39252c5227b0` | `8d21ea03952b325c1646fc62e19b39252c5227b0` | EXACT |
| modeling-basics | `EU-MODELING_BASICS-C` | 1 | 1 | `da6b98cffee4eafa7303ef6c87df2c51002f999d` | `da6b98cffee4eafa7303ef6c87df2c51002f999d` | EXACT |
| music-theory-basics | `EU-MUSIC_THEORY_BASICS-A` | 1 | 1 | `b366b88b652072cab03c37dca42c95949b872306` | `b366b88b652072cab03c37dca42c95949b872306` | EXACT |
| music-theory-basics | `EU-MUSIC_THEORY_BASICS-B` | 1 | 1 | `0df751319d5489f58d81c422cfa73032c29ee7c7` | `0df751319d5489f58d81c422cfa73032c29ee7c7` | EXACT |
| music-theory-basics | `EU-MUSIC_THEORY_BASICS-C` | 1 | 1 | `8d8ab92935c59236fd48639b30d642014ac2733f` | `8d8ab92935c59236fd48639b30d642014ac2733f` | EXACT |
| negotiation-basics | `EU-NEGOTIATION_BASICS-A` | 1 | 1 | `008e32fc8a0bd8af41dfe0289011429c4d39a02b` | `008e32fc8a0bd8af41dfe0289011429c4d39a02b` | EXACT |
| negotiation-basics | `EU-NEGOTIATION_BASICS-B` | 1 | 1 | `17af4eb74c15a08463f032936b9a2b6f14c6ce1c` | `17af4eb74c15a08463f032936b9a2b6f14c6ce1c` | EXACT |
| open-science-basics | `EU-OPEN_SCIENCE_BASICS-B` | 1 | 1 | `af6dc3078dd5fff283ca598f1e03139c2acfe2f6` | `af6dc3078dd5fff283ca598f1e03139c2acfe2f6` | EXACT |
| open-science-basics | `EU-OPEN_SCIENCE_BASICS-C` | 1 | 1 | `75504d7745f98054d27a052aede955b56ee67e73` | `75504d7745f98054d27a052aede955b56ee67e73` | EXACT |
| operations-research-basics | `EU-OPERATIONS_RESEARCH_BASICS-A` | 1 | 1 | `7509a9a25c52e5ac5c52bda0b137ffb63f9d8d29` | `7509a9a25c52e5ac5c52bda0b137ffb63f9d8d29` | EXACT |
| operations-research-basics | `EU-OPERATIONS_RESEARCH_BASICS-B` | 1 | 1 | `e331c86f4d4d33c5d1fb18e1b87ffcc362b83a5c` | `e331c86f4d4d33c5d1fb18e1b87ffcc362b83a5c` | EXACT |
| operations-research-basics | `EU-OPERATIONS_RESEARCH_BASICS-C` | 1 | 1 | `cc7d047a3b3508dc45d53a975eaebf6e30bcec5a` | `cc7d047a3b3508dc45d53a975eaebf6e30bcec5a` | EXACT |
| optimization-basics | `EU-OPTIMIZATION_BASICS-A` | 1 | 1 | `640ba93259cb8d0f6e210c10e6a74e4332449b08` | `640ba93259cb8d0f6e210c10e6a74e4332449b08` | EXACT |
| optimization-basics | `EU-OPTIMIZATION_BASICS-B` | 1 | 1 | `a7709a11310d5f28ec18453516de9355ed6b35df` | `a7709a11310d5f28ec18453516de9355ed6b35df` | EXACT |
| optimization-basics | `EU-OPTIMIZATION_BASICS-C` | 1 | 1 | `26b505bb8500deea3433e850fc5973ed126db44a` | `26b505bb8500deea3433e850fc5973ed126db44a` | EXACT |
| papermaking-basics | `EU-PAPERMAKING_BASICS-B` | 1 | 1 | `dc6b197ef815655b4b361192dcd91e422816b5e6` | `dc6b197ef815655b4b361192dcd91e422816b5e6` | EXACT |
| papermaking-basics | `EU-PAPERMAKING_BASICS-C` | 1 | 1 | `e3a6a7de9642c9a59341d853851199eda47e9031` | `e3a6a7de9642c9a59341d853851199eda47e9031` | EXACT |
| philosophy-of-language-basics | `EU-PHILOSOPHY_OF_LANGUAGE_BASICS-A` | 1 | 1 | `485044566add95b5733c3b22fb40ace497a69339` | `485044566add95b5733c3b22fb40ace497a69339` | EXACT |
| philosophy-of-language-basics | `EU-PHILOSOPHY_OF_LANGUAGE_BASICS-C` | 1 | 1 | `20055f2529fea968ef9136fdc76b0f4834e5ddc6` | `20055f2529fea968ef9136fdc76b0f4834e5ddc6` | EXACT |
| philosophy-of-mathematics-basics | `EU-PHILOSOPHY_OF_MATHEMATICS_BASICS-A` | 1 | 1 | `a57ea060104dc8d1f4a4ae1fe0347d1393cde536` | `a57ea060104dc8d1f4a4ae1fe0347d1393cde536` | EXACT |
| philosophy-of-mathematics-basics | `EU-PHILOSOPHY_OF_MATHEMATICS_BASICS-B` | 1 | 1 | `bf65e10f626e59487ddb8fb0dd9faac27ef37589` | `bf65e10f626e59487ddb8fb0dd9faac27ef37589` | EXACT |
| philosophy-of-mathematics-basics | `EU-PHILOSOPHY_OF_MATHEMATICS_BASICS-C` | 1 | 1 | `5ec6ac7c8e24a08cca1b50ddce984a01a3ed3736` | `5ec6ac7c8e24a08cca1b50ddce984a01a3ed3736` | EXACT |

## 3. Row-level Source crosswalk

| Slice | Source ID | Historical version | Current version | Historical Blob SHA | Current Blob SHA | Result |
|---|---|---:|---:|---|---|---|
| media-literacy-basics | `SRC-MEDIA_LITERACY_BASICS` | 1 | 1 | `009cad172c74a9de490444cba4199ab32530882a` | `009cad172c74a9de490444cba4199ab32530882a` | EXACT |
| metaphysics-basics | `SRC-METAPHYSICS_BASICS` | 1 | 1 | `a1dfe9fc5bc58ba80ef59fd779bef9adec690823` | `a1dfe9fc5bc58ba80ef59fd779bef9adec690823` | EXACT |
| modeling-and-simulation-basics | `SRC-MODELING_AND_SIMULATION_BASICS` | 1 | 1 | `dcd35cac57f56be7381df1b74bd9839864ffd8d9` | `dcd35cac57f56be7381df1b74bd9839864ffd8d9` | EXACT |
| modeling-basics | `SRC-MODELING_BASICS` | 1 | 1 | `c2fd45047a19b857df61733944f7f4ec45bf625a` | `c2fd45047a19b857df61733944f7f4ec45bf625a` | EXACT |
| music-theory-basics | `SRC-MUSIC_THEORY_BASICS` | 1 | 1 | `c1b8ec29d5768a5a1c74290ea8232e911e35a2a0` | `c1b8ec29d5768a5a1c74290ea8232e911e35a2a0` | EXACT |
| negotiation-basics | `SRC-NEGOTIATION_BASICS` | 1 | 1 | `6a4a71ea044ec48942ec55bc89746b7c8d22704a` | `6a4a71ea044ec48942ec55bc89746b7c8d22704a` | EXACT |
| open-science-basics | `SRC-OPEN_SCIENCE_BASICS` | 1 | 1 | `fde673b00c1b898eb9e2d01462d0c92a76fe0e43` | `fde673b00c1b898eb9e2d01462d0c92a76fe0e43` | EXACT |
| operations-research-basics | `SRC-OPERATIONS_RESEARCH_BASICS` | 1 | 1 | `6a13eba7bda18acc523fe82a06e6be2cfb544da1` | `6a13eba7bda18acc523fe82a06e6be2cfb544da1` | EXACT |
| optimization-basics | `SRC-OPTIMIZATION_BASICS` | 1 | 1 | `c160375c7d9d4498de48737fb4b75fc2f632b346` | `c160375c7d9d4498de48737fb4b75fc2f632b346` | EXACT |
| papermaking-basics | `SRC-PAPERMAKING_BASICS-TECHNIKMUSEUM` | 1 | 1 | `74bf77c60d8827f5e482893b0a8378da12f2befa` | `74bf77c60d8827f5e482893b0a8378da12f2befa` | EXACT |
| papermaking-basics | `SRC-PAPERMAKING_BASICS-MFA` | 1 | 1 | `ef44485d665cb4e84a6a15f7250a2aa1f5b3b5fa` | `ef44485d665cb4e84a6a15f7250a2aa1f5b3b5fa` | EXACT |
| philosophy-of-language-basics | `SRC-PHILOSOPHY_OF_LANGUAGE_BASICS` | 1 | 1 | `b7e5969030c2e0f79a36ab2a97071221066ed92a` | `b7e5969030c2e0f79a36ab2a97071221066ed92a` | EXACT |
| philosophy-of-mathematics-basics | `SRC-PHILOSOPHY_OF_MATHEMATICS_BASICS` | 1 | 1 | `e75530af8491107d8fa9614221efb0ea58018edb` | `e75530af8491107d8fa9614221efb0ea58018edb` | EXACT |

## 4. Interpretation and guardrails

- This tranche recovers exact EU and Source version provenance for 31 Batch 53 chains; it does not claim the remaining 69 Batch 53 chains or any Batch 54 chain is resolved.
- The Batch 54 sample `CLM-SI-ACCURACY-BOUNDARY@1` was previously reported as one directly verified EU@1 / Source@1 exact match. It is not included in this 31-row Batch 53 tranche.
- Exact Blob equality establishes content identity at the compared Git refs. It does not establish that the cited source passage supports the Claim, that a locator is reproducible, that sources are independent, or that rights are clear.
- The Batch 53 source-passage reports explicitly identify missing claim-specific locators; the historical score E=1 remains historical only and is not promoted or transferred.
- No canonical Claim, Evidence Use, Source, Assessment, Relation, risk record, allowlist, or publication decision was modified.
- No D/E/B score was assigned or changed.
- This report is noncanonical audit evidence only. PR #21 remains Draft/unmerged; `main` is untouched.

## 5. Remaining work

Continue with the remaining Batch 53 EU/Source chains, then Batch 54. For every chain, retain the exact historical snapshot, current comparison HEAD, record version, path and Blob SHA; distinguish exact matches from versioned successors, missing historical objects, and same-version content drift. Do not infer version numbers from current files or filenames.
