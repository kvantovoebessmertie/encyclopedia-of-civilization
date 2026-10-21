from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "hydrology-basics" / "records"
USGS_URI = "https://www.usgs.gov/water-science-school/science/what-hydrology"


def test_hydrology_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"]: r for r in records if r["record_type"] == "source"}
    assert set(sources) == {"SRC-HYDROLOGY_BASICS"}
    for claim in [r for r in records if r["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"] == "evidence_use")


def test_hydrology_source_identity_and_evidence_pinpoints_are_versioned():
    records = {r["record_id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json"))}
    source = records["SRC-HYDROLOGY_BASICS"]
    assert source["record_version"] == "2"
    assert source["content"]["source_identity"] == 'U.S. Geological Survey, Water Science School, “What is Hydrology?” (updated 2026-09-17)'
    assert source["content"]["external_ref"]["uri"] == USGS_URI

    expected = {
        "EU-HYDROLOGY_BASICS-A": ("CLM-HYDROLOGY_BASICS-A", ("occurrence, distribution, movement and properties",)),
        "EU-HYDROLOGY_BASICS-B": ("CLM-HYDROLOGY_BASICS-B", ("water-cycle", "atmosphere", "beneath the surface")),
        "EU-HYDROLOGY_BASICS-C": ("CLM-HYDROLOGY_BASICS-C", ("rainfall/snowfall", "infiltration", "evaporation", "transpiration")),
    }
    for eu_id, (claim_id, markers) in expected.items():
        eu = records[eu_id]
        claim = records[claim_id]
        assert claim["record_version"] == "2"
        assert claim["provenance"]["created_from"] == [{"record_id": "SRC-HYDROLOGY_BASICS", "version": "2"}]
        assert eu["record_version"] == "2"
        assert eu["content"]["claim_ref"] == {"record_id": claim_id, "version": "2"}
        assert eu["content"]["source_ref"] == {"record_id": "SRC-HYDROLOGY_BASICS", "version": "2"}
        assert eu["provenance"]["created_from"] == [{"record_id": "SRC-HYDROLOGY_BASICS", "version": "2"}]
        description = eu["content"]["material"]["description"].lower()
        assert "what is hydrology?" in description
        assert all(marker in description for marker in markers)

    for context_id in ("CTX-HYDROLOGY_BASICS", "SCP-HYDROLOGY_BASICS"):
        context_or_scope = records[context_id]
        assert context_or_scope["record_version"] == "2"
        assert context_or_scope["content"]["target_ref"] == {"record_id": "CLM-HYDROLOGY_BASICS-A", "version": "2"}

    relation_path = ROOT / "CONTENT" / "vertical-slices" / "water-resources-basics" / "records" / "REL-M3-WATER-RESOURCES-HYDROLOGY.json"
    relation = json.loads(relation_path.read_text(encoding="utf-8"))
    assert relation["record_version"] == "2"
    assert relation["provenance"]["created_from"][1] == {"record_id": "SRC-HYDROLOGY_BASICS", "version": "2"}
    assert {"record_id": "CLM-HYDROLOGY_BASICS-A", "version": "2"} in relation["content"]["participants"]
