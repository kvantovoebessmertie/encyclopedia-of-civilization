# M13 Batch 43 — Scored row 009: limits of portable water filters

Date: 2026-10-20  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Claim version: `CLM-WATER-FILTER-LIMITS@1`  
Evidence Use version: `EU-WATER-FILTER-LIMITS@1`  
Source version: `SRC-CDC-WATER-FILTER-2025@1`

## Claim under review

> Портативные фильтры для воды не удаляют все типы возбудителей: CDC указывает, что они не удаляют вирусы, а для удаления бактерий и паразитов важен размер абсолютных пор.

## Passage checked

Canonical Source: CDC, “How to Make Water Safe in an Emergency,” https://www.cdc.gov/water-emergency/about/index.html.

The CDC page states “Portable water filters do not remove all types of germs from water” and specifies that filters “will not remove viruses,” need an absolute pore size of 0.3 micron or smaller to remove bacteria, and 1 micron or smaller to remove parasites such as Giardia or Cryptosporidium (retrieved page lines 139–147). This directly supports the Claim's core points. The page further cautions that most filters remove parasites but not viruses or bacteria (line 154), underscoring the importance of not implying that any portable filter makes water safe.

The canonical Evidence Use does not preserve the exact “Filter” section locator. The Claim is a summary, not a full treatment of filter performance or disinfection requirements.

## D/E/B assessment

| Claim ID | D | E | B | Rationale |
|---|---:|---:|---:|---|
| `CLM-WATER-FILTER-LIMITS` | 2 | 2 | 2 | **D=2:** incorrect interpretation could lead to unsafe drinking-water decisions. **E=2:** current CDC passage directly supports the limits and pore-size thresholds, but the stored Evidence Use lacks the section locator. **B=2:** the Claim names portable filters and key limitations, but must not imply that pore size alone guarantees safety for every device, water condition or pathogen. |

## Disposition

**HOLD for qualified public-health Human View and exact locator; not cleared for public pilot.** Preserve the warning that filters do not remove all pathogens and that treatment depends on the device and conditions. No canonical record changed.
