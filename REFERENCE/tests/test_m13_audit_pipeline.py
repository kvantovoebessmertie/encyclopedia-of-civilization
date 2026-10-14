from __future__ import annotations

import pytest

from REFERENCE.m13_audit_pipeline import build_lanes


def claim(cid, *, file=None, risk=False, flags=None, evidence=None):
    triage = list(flags or [])
    if risk:
        triage.append("high_consequence_screen")
    return {
        "record_id": cid,
        "record_version": "1",
        "slice": "sample-slice",
        "file": file or f"CONTENT/sample-slice/records/{cid}.json",
        "evidence_use_ids": list(evidence or []),
        "source_ids": ["SRC-SAMPLE"],
        "risk_domains": ["health_medical"] if risk else [],
        "machine_triage_flags": triage,
    }


def test_queue_excludes_prior_scored_paths_and_partitions_unique_claims():
    claims = [claim(f"CLM-{i:03}") for i in range(125)]
    scored = {claims[0]["file"], claims[3]["file"], claims[8]["file"]}
    queue = build_lanes(claims, scored, [], batch_size=100, lane_count=5)

    assert queue["selected_claims"] == 100
    assert queue["unique_selected_claim_ids"] == 100
    assert queue["lane_counts"] == {"1": 20, "2": 20, "3": 20, "4": 20, "5": 20}
    selected = [row for lane in queue["lanes"] for row in lane["claims"]]
    assert not ({row["file"] for row in selected} & scored)
    assert all(row["D_score"] is None and row["E_score"] is None and row["B_score"] is None for row in selected)


def test_high_consequence_claims_are_routed_first_without_becoming_scores():
    claims = [claim("CLM-LOW"), claim("CLM-HIGH", risk=True)]
    queue = build_lanes(claims, set(), [], batch_size=2, lane_count=1)
    selected = queue["lanes"][0]["claims"]
    assert [row["record_id"] for row in selected] == ["CLM-HIGH", "CLM-LOW"]
    assert selected[0]["D_score"] is None
    assert selected[0]["review_status"] == "NOT_YET_REVIEWED"


def test_evidence_use_structural_findings_raise_associated_claim_priority():
    claims = [
        claim("CLM-CLEAN", evidence=["EU-CLEAN"]),
        claim("CLM-BROKEN", evidence=["EU-BROKEN"]),
    ]
    findings = [{"record_id": "EU-BROKEN", "severity": "high"}]
    queue = build_lanes(claims, set(), findings, batch_size=2, lane_count=1)
    assert [row["record_id"] for row in queue["lanes"][0]["claims"]] == ["CLM-BROKEN", "CLM-CLEAN"]
    assert queue["lanes"][0]["claims"][0]["structural_finding_priority"] == 3


def test_lane_configuration_must_divide_batch_evenly():
    with pytest.raises(ValueError):
        build_lanes([claim("CLM-A")], set(), [], batch_size=100, lane_count=6)
