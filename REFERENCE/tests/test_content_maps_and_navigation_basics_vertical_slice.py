from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SLICE=ROOT/"CONTENT"/"vertical-slices"/"maps-and-navigation-basics"/"records"
def test_maps_and_navigation_basics_slice_is_complete():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records)==9
    assert {"source","claim","evidence_use","context","scope"} <= {r["record_type"] for r in records}
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    claims=[r for r in records if r["record_type"]=="claim"]; evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert len(sources)==1 and len(claims)==3 and len(evidence)==3
    for claim in claims:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"]==claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in evidence)


def test_maps_and_navigation_claim_specific_evidence_is_pinned_to_usgs():
    records = {r["record_id"]: r for r in
               (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    expected = {
        "EU-MAPS_AND_NAVIGATION_BASICS-A": (
            "CLM-MAPS_AND_NAVIGATION_BASICS-A",
            "USGS, “Finding Your Way With Map and Compass”, introductory explanation "
            "of topographic maps and passages describing natural and human-made features, "
            "land shape/contours, distance and direction.",
        ),
        "EU-MAPS_AND_NAVIGATION_BASICS-B": (
            "CLM-MAPS_AND_NAVIGATION_BASICS-B",
            "USGS, “Finding Your Way With Map and Compass”, passage defining map scale "
            "as the relationship between a unit of map distance and the corresponding "
            "ground distance.",
        ),
    }
    for evidence_id, (claim_id, locator) in expected.items():
        evidence = records[evidence_id]
        assert evidence["record_version"] == "2"
        assert evidence["content"]["claim_ref"] == {
            "record_id": claim_id, "version": "1"
        }
        assert evidence["content"]["source_ref"] == {
            "record_id": "SRC-MAPS_AND_NAVIGATION_BASICS", "version": "1"
        }
        assert evidence["provenance"]["created_from"] == [
            {"record_id": "SRC-MAPS_AND_NAVIGATION_BASICS", "version": "1"}
        ]
        assert evidence["content"]["material"]["locator"] == locator
    assert "not the safety or currency of any particular route" in (
        records["EU-MAPS_AND_NAVIGATION_BASICS-A"]["content"]["material"]["description"]
    )
    assert "not establish that a map is current or sufficient for safe navigation" in (
        records["EU-MAPS_AND_NAVIGATION_BASICS-B"]["content"]["material"]["description"]
    )
