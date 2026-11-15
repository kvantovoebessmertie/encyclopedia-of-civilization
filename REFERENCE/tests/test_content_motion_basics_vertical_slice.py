from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "motion-basics" / "records"


def test_motion_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {
        r["record_type"] for r in records
    }
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    assert sources == {"SRC-MOTION_BASICS"}
    for claim in [r for r in records if r["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(
            e["content"]["claim_ref"]["record_id"] == claim["record_id"]
            and e["content"]["source_ref"]["record_id"] in sources
            for e in records if e["record_type"] == "evidence_use"
        )


def test_motion_average_velocity_claim_and_evidence_are_distinct_from_average_speed():
    by_id = {json.loads(p.read_text(encoding="utf-8"))["record_id"]:
             json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")}

    source = by_id["SRC-MOTION_BASICS"]
    claim = by_id["CLM-MOTION_BASICS-B"]
    evidence = by_id["EU-MOTION_BASICS-B"]

    assert source["record_version"] == "1"
    assert source["content"]["external_ref"]["uri"] == (
        "https://openstax.org/books/physics/pages/2-introduction-to-one-dimensional-kinematics"
    )
    assert claim["record_version"] == "2"
    assert claim["provenance"]["created_from"][0] == {
        "record_id": "SRC-MOTION_BASICS", "version": "1"
    }
    assert claim["content"]["statement"] == (
        "Средняя векторная скорость равна отношению перемещения тела "
        "к интервалу времени, за который это перемещение произошло."
    )
    assert evidence["record_version"] == "2"
    assert evidence["content"]["claim_ref"] == {
        "record_id": "CLM-MOTION_BASICS-B", "version": "2"
    }
    assert evidence["content"]["source_ref"] == {
        "record_id": "SRC-MOTION_BASICS", "version": "1"
    }
    description = evidence["content"]["material"]["description"]
    assert "§2.2" in description
    assert "average velocity" in description
    assert "displacement" in description
    assert "average speed" in description
    assert "distance traveled" in description
    assert "https://openstax.org/books/physics/pages/2-2-speed-and-velocity" in description
