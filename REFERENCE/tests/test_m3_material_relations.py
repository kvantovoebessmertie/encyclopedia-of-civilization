from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECORD_ROOT = ROOT / "CONTENT" / "vertical-slices"

EXPECTED = {
    "REL_M3_FIRE_SAFETY_EMERGENCY_MANAGEMENT": {
        "a": "CLM_FIRE_SAFETY_BASICS_B",
        "b": "CLM_EMERGENCY_MANAGEMENT_BASICS_A",
    },
    "REL_M3_SHELTER_SETTLEMENT": {
        "a": "CLM_SHELTER_BASICS_A",
        "b": "CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B",
    },
    "REL_M3_WATER_RESOURCES_HYDROLOGY": {
        "a": "CLM_WATER_RESOURCES_BASICS_B",
        "b": "CLM_HYDROLOGY_BASICS_A",
    },
    "REL_M3_FOOD_PRESERVATION_SAFETY": {
        "a": "CLM_FOOD_PRESERVATION_BASICS_B",
        "b": "CLM-FOOD_SAFETY_BASICS-A",
    },
    "REL_M3_SCIENTIFIC_METHOD_RESEARCH": {
        "a": "CLM_SCIENTIFIC_METHOD_BASICS_D",
        "b": "CLM_RESEARCH_METHODS_BASICS_B",
    },
    "REL_M3_EMERGENCY_INFRASTRUCTURE": {
        "a": "CLM_EMERGENCY_MANAGEMENT_BASICS_A",
        "b": "CLM-INFRASTRUCTURE_RESILIENCE-A",
    },
}

def _records():
    out = []
    for p in RECORD_ROOT.rglob("REL-M3-*.json"):
        out.append(json.loads(p.read_text(encoding="utf-8")))
    return out

def test_m3_material_relations_are_present_and_exact():
    records = {r["record_id"]: r for r in _records()}
    assert set(EXPECTED) <= set(records)
    for rid, exp in EXPECTED.items():
        r = records[rid]
        assert r["record_type"] == "relation"
        assert r["content"]["direction"] == "undirected"
        participants = {x["record_id"] for x in r["content"]["participants"]}
        assert participants == {exp["a"], exp["b"]}
