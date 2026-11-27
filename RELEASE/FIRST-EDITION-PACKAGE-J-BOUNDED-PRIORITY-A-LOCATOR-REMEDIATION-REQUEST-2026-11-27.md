# First Edition — Package J: bounded locator-remediation authorization request for four priority candidates

Date: 2026-11-27  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Prepared against exact HEAD: `0b499c019ae79f945e9820f6f5f16cf0e9f00f2a`  
Status: REQUEST FOR EXPLICIT OWNER AUTHORIZATION — NO CANONICAL WRITES PERFORMED.

## 1. Requested decision

Authorize one bounded evidence-locator package covering four already-screened low-/moderate-consequence candidates from Package I Queue A:

1. Food Security Basics — Claim A;
2. Maps and Navigation Basics — Claims A and B;
3. Learning Basics — Claim A;
4. Motion Basics — Claim A, including a coordinated Source URI/version alignment.

The package contains six versioned canonical operations:
- four Evidence Use version bumps with exact locators and bounded descriptions;
- one Motion Source version bump to the exact OpenStax §2.1 page;
- one Motion Evidence Use version bump aligned to Source@2.

It also requests focused regression assertions in four existing slice tests and one exact authorization entry in `RELEASE/EDITORIAL-CORRECTION.json`, including the four affected slice slugs required by the preflight wave-safety guard.

**No operation is applied by this request.** The current records remain unchanged until explicit approval of this exact file list and exact proposed content.

## 2. Why these four candidates

- Food Security A: FAO Handbook §1.4 directly supports the bounded definition; current EU@1 is generic.
- Maps A/B: USGS directly supports topographic-map features/terrain and the definition of map scale; current EU records lack pinpoint locators.
- Learning A: NIMH's program overview directly lists the four named cognitive processes; current EU@1 is generic. The Claim must be read as describing a research program's scope, not a universal exhaustive taxonomy.
- Motion A: OpenStax Physics §2.1 directly supports the selected-reference-frame proposition. Current Source@1 points to a broad chapter introduction rather than the exact §2.1 page, so Source and EU must be versioned together.

These operations do not settle source rights, independent editorial review, or publication eligibility. All four slices and all affected Claims remain HOLD.

## 3. Exact canonical files and current baselines

All current files were fetched from the exact prepared HEAD `0b499c019ae79f945e9820f6f5f16cf0e9f00f2a`.

| File | Current version | Proposed version | Current blob SHA |
|---|---:|---:|---|
| `CONTENT/vertical-slices/food-security-basics/records/EU-FOOD_SECURITY_BASICS-A.json` | 1 | 2 | `39f93d33a4fef420ba52992c4afdf59948de02b3` |
| `CONTENT/vertical-slices/maps-and-navigation-basics/records/EU-MAPS_AND_NAVIGATION_BASICS-A.json` | 1 | 2 | `eaefe0c405544bd318b4590a3624bcbdeebc3a24` |
| `CONTENT/vertical-slices/maps-and-navigation-basics/records/EU-MAPS_AND_NAVIGATION_BASICS-B.json` | 1 | 2 | `a8823811f8ec9c162a9c87f6fe315d68f5d0a761` |
| `CONTENT/vertical-slices/learning-basics/records/EU-LEARNING_BASICS-A.json` | 1 | 2 | `221c07ee66fed96e3ebecd16f0707fa26a364325` |
| `CONTENT/vertical-slices/motion-basics/records/SRC-MOTION_BASICS.json` | 1 | 2 | `08826cd7cd259af2425cdecb59a444d1bb966885` |
| `CONTENT/vertical-slices/motion-basics/records/EU-MOTION_BASICS-A.json` | 1 | 2 | `549bd88b51a89cbbeaed07805cf0e4de7b9e5004` |

No new record IDs are created. Record counts and coverage denominators remain unchanged.

## 4. Proposed complete versioned records

The JSON below is the full proposed content, not illustrative fragments. Every field not expressly described in the allowed changes is preserved from the fetched current record.

### EU-FOOD_SECURITY_BASICS-A: 1 → 2

Current blob SHA: `39f93d33a4fef420ba52992c4afdf59948de02b3`

Proposed complete record:

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "EU-FOOD_SECURITY_BASICS-A",
  "record_type": "evidence_use",
  "provenance": {
    "method": "source_based_claim_representation",
    "created_from": [
      {
        "record_id": "SRC-FOOD_SECURITY_BASICS",
        "version": "1"
      }
    ]
  },
  "content": {
    "claim_ref": {
      "record_id": "CLM-FOOD_SECURITY_BASICS-A",
      "version": "1"
    },
    "source_ref": {
      "record_id": "SRC-FOOD_SECURITY_BASICS",
      "version": "1"
    },
    "evidence_role": "supports",
    "material": {
      "description": "FAO §1.4 defines food security through physical and economic access, for all people and at all times, to sufficient, safe and nutritious food. The same section identifies availability, stability, access and biological utilization as classic dimensions. This supports the core definition only; it does not establish individual dietary or medical advice.",
      "locator": "FAO, Food Security Information and Early Warning System Handbook, §1.4 “Definition of Food Security”."
    }
  }
}
```

### EU-MAPS_AND_NAVIGATION_BASICS-A: 1 → 2

Current blob SHA: `eaefe0c405544bd318b4590a3624bcbdeebc3a24`

Proposed complete record:

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "EU-MAPS_AND_NAVIGATION_BASICS-A",
  "record_type": "evidence_use",
  "provenance": {
    "created_from": [
      {
        "record_id": "SRC-MAPS_AND_NAVIGATION_BASICS",
        "version": "1"
      }
    ],
    "method": "evidence_link"
  },
  "content": {
    "claim_ref": {
      "record_id": "CLM-MAPS_AND_NAVIGATION_BASICS-A",
      "version": "1"
    },
    "source_ref": {
      "record_id": "SRC-MAPS_AND_NAVIGATION_BASICS",
      "version": "1"
    },
    "evidence_role": "supports",
    "material": {
      "description": "USGS describes topographic maps as representing natural and human-made features and the shape of the land, including terrain represented through contour lines; the page also explains distance and direction. This supports the descriptive function stated in Claim A, not the safety or currency of any particular route.",
      "locator": "USGS, “Finding Your Way With Map and Compass”, introductory explanation of topographic maps and passages describing natural and human-made features, land shape/contours, distance and direction."
    }
  }
}
```

### EU-MAPS_AND_NAVIGATION_BASICS-B: 1 → 2

Current blob SHA: `a8823811f8ec9c162a9c87f6fe315d68f5d0a761`

Proposed complete record:

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "EU-MAPS_AND_NAVIGATION_BASICS-B",
  "record_type": "evidence_use",
  "provenance": {
    "created_from": [
      {
        "record_id": "SRC-MAPS_AND_NAVIGATION_BASICS",
        "version": "1"
      }
    ],
    "method": "evidence_link"
  },
  "content": {
    "claim_ref": {
      "record_id": "CLM-MAPS_AND_NAVIGATION_BASICS-B",
      "version": "1"
    },
    "source_ref": {
      "record_id": "SRC-MAPS_AND_NAVIGATION_BASICS",
      "version": "1"
    },
    "evidence_role": "supports",
    "material": {
      "description": "The USGS material defines map scale as the relationship between a measured distance on a map and the actual distance represented on the ground. This directly supports the bounded scale proposition; it does not establish that a map is current or sufficient for safe navigation.",
      "locator": "USGS, “Finding Your Way With Map and Compass”, passage defining map scale as the relationship between a unit of map distance and the corresponding ground distance."
    }
  }
}
```

### EU-LEARNING_BASICS-A: 1 → 2

Current blob SHA: `221c07ee66fed96e3ebecd16f0707fa26a364325`

Proposed complete record:

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "EU-LEARNING_BASICS-A",
  "record_type": "evidence_use",
  "provenance": {
    "created_from": [
      {
        "record_id": "SRC-LEARNING_BASICS",
        "version": "1"
      }
    ],
    "method": "evidence_link"
  },
  "content": {
    "claim_ref": {
      "record_id": "CLM-LEARNING_BASICS-A",
      "version": "1"
    },
    "source_ref": {
      "record_id": "SRC-LEARNING_BASICS",
      "version": "1"
    },
    "evidence_role": "supports",
    "material": {
      "description": "The NIMH Learning and Memory Program identifies encoding, consolidation, retrieval and working memory among the cognitive processes within its research scope. This supports a representative description of that program's research focus, not an exhaustive taxonomy or universal theory of learning.",
      "locator": "NIMH, Learning and Memory Program, program-overview passage listing encoding, consolidation, retrieval and working memory among the cognitive processes studied."
    }
  }
}
```

### SRC-MOTION_BASICS: 1 → 2

Current blob SHA: `08826cd7cd259af2425cdecb59a444d1bb966885`

Proposed complete record:

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "SRC-MOTION_BASICS",
  "record_type": "source",
  "provenance": {
    "method": "external_official_source"
  },
  "content": {
    "source_identity": "OpenStax Physics — Relative Motion, Distance, and Displacement (§2.1)",
    "representation": "official/public reference",
    "external_ref": {
      "uri": "https://openstax.org/books/physics/pages/2-1-relative-motion-distance-and-displacement"
    },
    "availability": "public",
    "preservation": "external canonical source; local corpus stores identity and locator"
  }
}
```

### EU-MOTION_BASICS-A: 1 → 2

Current blob SHA: `549bd88b51a89cbbeaed07805cf0e4de7b9e5004`

Proposed complete record:

```json
{
  "record_version": "2",
  "type_version": "1.0",
  "publication_status": "published",
  "completion_status": "complete",
  "schema": "record/0.1",
  "record_id": "EU-MOTION_BASICS-A",
  "record_type": "evidence_use",
  "provenance": {
    "created_from": [
      {
        "record_id": "SRC-MOTION_BASICS",
        "version": "2"
      }
    ],
    "method": "evidence_link"
  },
  "content": {
    "claim_ref": {
      "record_id": "CLM-MOTION_BASICS-A",
      "version": "1"
    },
    "source_ref": {
      "record_id": "SRC-MOTION_BASICS",
      "version": "2"
    },
    "evidence_role": "supports",
    "material": {
      "description": "OpenStax Physics §2.1 explains that position and motion are described relative to a selected reference frame. This directly supports Claim A as a foundational physics proposition; it does not resolve the separate terminology issue previously identified in Claim B.",
      "locator": "OpenStax Physics, §2.1 “Relative Motion, Distance, and Displacement”, subsection “Defining Motion”."
    }
  }
}
```

## 5. Exact bounded file authorization requested

The owner authorization should cover only these eleven files:

- `CONTENT/vertical-slices/food-security-basics/records/EU-FOOD_SECURITY_BASICS-A.json`
- `CONTENT/vertical-slices/maps-and-navigation-basics/records/EU-MAPS_AND_NAVIGATION_BASICS-A.json`
- `CONTENT/vertical-slices/maps-and-navigation-basics/records/EU-MAPS_AND_NAVIGATION_BASICS-B.json`
- `CONTENT/vertical-slices/learning-basics/records/EU-LEARNING_BASICS-A.json`
- `CONTENT/vertical-slices/motion-basics/records/SRC-MOTION_BASICS.json`
- `CONTENT/vertical-slices/motion-basics/records/EU-MOTION_BASICS-A.json`
- `REFERENCE/tests/test_content_food_security_basics_vertical_slice.py`
- `REFERENCE/tests/test_content_maps_and_navigation_basics_vertical_slice.py`
- `REFERENCE/tests/test_content_learning_basics_vertical_slice.py`
- `REFERENCE/tests/test_content_motion_basics_vertical_slice.py`
- `RELEASE/EDITORIAL-CORRECTION.json`

### Allowed changes

1. Version `EU-FOOD_SECURITY_BASICS-A@1 → @2`; add locator `§1.4 “Definition of Food Security”` and the bounded factual paraphrase in §4.
2. Version `EU-MAPS_AND_NAVIGATION_BASICS-A@1 → @2`; add the USGS topographic-map/terrain/features locator and the bounded description in §4.
3. Version `EU-MAPS_AND_NAVIGATION_BASICS-B@1 → @2`; add the USGS map-scale passage locator and the bounded description in §4.
4. Version `EU-LEARNING_BASICS-A@1 → @2`; add the NIMH program-overview locator and preserve the representative/non-exhaustive research-scope boundary in §4.
5. Version `SRC-MOTION_BASICS@1 → @2`; preserve source representation, availability and preservation fields, update source identity to identify OpenStax Physics §2.1, and update only the external URI to the exact §2.1 page.
6. Version `EU-MOTION_BASICS-A@1 → @2`; align both `content.source_ref` and `provenance.created_from` to `SRC-MOTION_BASICS@2`, add the §2.1 “Defining Motion” locator and the bounded description in §4.
7. Strengthen only the four named slice regression tests to assert exact versions, Claim/Source references and locator text; do not change test scope or slice counts.
8. Add one nested authorization entry with ID `FIRST-EDITION-PRIORITY-A-LOCATOR-REMEDIATION-2026-11-27` to `RELEASE/EDITORIAL-CORRECTION.json`, append the same ID to its `findings` list, and add only these four slugs to `authorized_slices`:
   - `food-security-basics`
   - `maps-and-navigation-basics`
   - `learning-basics`
   - `motion-basics`

### Explicit prohibitions

- Do not modify any Claim, Context, Scope, Relation, Assessment, Inference or Decision.
- Do not change any other Source or Evidence Use record.
- Do not change the Red Cross alerts EU or Source; their exact prior correction authorization is closed.
- Do not modify any other file or slice.
- Do not change publication_status, completion_status, HOLD/INCLUDE/EXCLUDE, candidate membership, selection manifest, chapter map, allowlist or coverage counts.
- Do not claim rights clearance from public availability; do not reproduce FAO, USGS, NIMH or OpenStax text, images, maps, tables or other assets.
- Do not merge PR #22, change `main`, retarget the PR, publish, deploy or distribute a preview.

## 6. Evidence locators and editorial boundaries

### Food Security A — FAO

Source URI already stored in Source@1:  
https://www.fao.org/4/x8622e/x8622e04.htm

Locator: §1.4, “Definition of Food Security”.

The EU paraphrase is limited to the elements in that section. The four classic dimensions are presented as the handbook's framework, not the only possible contemporary taxonomy. No individual nutrition, clinical or household entitlement recommendation is implied. Item-level FAO rights/terms review remains open.

### Maps A/B — USGS

Source URI already stored in Source@1:  
https://www.usgs.gov/educational-resources/finding-your-way-map-and-compass

Claim A locator: introductory explanation of topographic maps and passages on natural/human-made features, land shape, contour lines, distance and direction.  
Claim B locator: passage defining map scale as the relationship between map distance and actual ground distance.

No maps, images, graphics or other assets are copied. These descriptive Claims do not establish that a particular map is current, that a route is safe, or that map-reading alone is sufficient for navigation. USGS item-level and third-party asset rights remain to be checked.

### Learning A — NIMH

Source URI already stored in Source@1:  
https://www.nimh.nih.gov/about/organization/dnbbs/behavioral-science-and-integrative-neuroscience-research-branch/learning-and-memory-program

Locator: Learning and Memory Program overview passage listing encoding, consolidation, retrieval and working memory.

The Claim is interpreted as describing processes included in the program's research scope. It is not an exhaustive taxonomy of learning/memory or an individual clinical/pedagogical instruction. No images or linked third-party publications are reused. Rights/attribution remains subject to project policy.

### Motion A — OpenStax Physics

Proposed Source@2 URI:  
https://openstax.org/books/physics/pages/2-1-relative-motion-distance-and-displacement

Locator: §2.1, “Relative Motion, Distance, and Displacement”, subsection “Defining Motion”.

The Source/EU alignment makes the pinpoint reproducible. Claim A is limited to the selected-reference-frame proposition. It does not repair, endorse or otherwise alter the separate terminology issue in Motion Claim B. Rights review must apply to the exact Physics title/edition and intended factual paraphrase; no textbook prose, figures, diagrams or other assets are copied.

## 7. Validation required if authorization is granted

Before any write:
1. Re-fetch the exact branch HEAD and all eleven target files; abort if the branch moved or any current blob SHA differs from §3.
2. Validate all six proposed records against `IMPLEMENTATION/005-RECORD-SCHEMA.json`.
3. Confirm each EU Claim reference, Source reference and provenance edge resolves to the exact proposed version.
4. Confirm the Motion Source@2 URI and EU@2 locator identify the same §2.1 section.
5. Update only the four named regression tests and run those tests.
6. Verify the four slice record counts and all coverage counts are unchanged.
7. Verify the new authorization register entry lists exactly the eleven files, four allowed slice slugs, allowed changes and prohibitions above.
8. Re-fetch every changed file and compare it against the approved proposal.
9. Run Reference Tests, Release Conformance Gate, Offline Edition and MVP Browser Tests on one immutable resulting HEAD. Report only actual completed results.

If any baseline changed, stop and reconcile; do not silently adapt the authorization.

## 8. Current release boundary

- All affected Claims remain HOLD.
- No first-edition INCLUDE is created.
- No production allowlist or approved chapter map is created.
- R-01–R-10 remain separate owner decisions; source locator updates do not close rights or editorial governance.
- No qualified review is inferred from these research notes.
- PR #22 remains OPEN / DRAFT / NOT MERGED; `main` remains unchanged.

**Owner authorization: NOT YET RECEIVED. No operation in this request has been applied.**
