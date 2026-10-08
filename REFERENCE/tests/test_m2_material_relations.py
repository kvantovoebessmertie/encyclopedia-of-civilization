from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REL_DIR = ROOT / "CONTENT" / "vertical-slices" / "cross-slice-linkage" / "records"

EXPECTED = {
    "REL-CROSS-M2-MEASUREMENT-UNCERTAINTY-SCIENCE": {
        "CLM-MEASUREMENT_UNCERTAINTY_BASICS-A",
        "CLM-MEASUREMENT_SCIENCE_BASICS-A",
    },
    "REL-CROSS-M2-STATISTICS-RESEARCH": {
        "CLM-STATISTICS_BASICS-C",
        "CLM-RESEARCH_METHODS_BASICS-B",
    },
    "REL-CROSS-M2-RISK-MANAGEMENT-ANALYSIS": {
        "CLM-RISK_MANAGEMENT_BASICS-B",
        "CLM-RISK_ANALYSIS_BASICS-A",
    },
    "REL-CROSS-M2-AGRICULTURE-SOIL": {
        "CLM-AGRICULTURE_BASICS-B",
        "CLM-SOIL_BASICS-A",
    },
    "REL-CROSS-M2-ENERGY-SECURITY-RESILIENCE": {
        "CLM-ENERGY_SECURITY_BASICS-A",
        "CLM-INFRASTRUCTURE_RESILIENCE-A",
    },
    "REL-CROSS-M2-GEOGRAPHIC-COORDINATES-GEODESY": {
        "CLM-GEOGRAPHIC_COORDINATES_BASICS-C",
        "CLM-GEODESY_BASICS-B",
    },
}

def test_m2_material_relations_are_present_and_exact():
    for relation_id, expected_participants in EXPECTED.items():
        path = REL_DIR / f"{relation_id}.json"
        assert path.exists(), relation_id
        record = json.loads(path.read_text(encoding="utf-8"))
        participants = {
            p["record_id"] for p in record["content"]["participants"]
        }
        assert record["record_type"] == "relation"
        assert record["content"]["direction"] == "undirected"
        assert participants == expected_participants
