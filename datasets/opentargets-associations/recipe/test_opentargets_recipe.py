from __future__ import annotations

import math

from pathlib import Path

import pytest
import yaml

from build import (
    KNOWN_DISEASE_PREFIXES,
    PREDICATE,
    build_opentargets_tables,
)
from fetch import LOCKFILE, _reject_mutable_url


def test_lockfile_has_31_files():
    assert len(LOCKFILE["files"]) == 31
    assert LOCKFILE["release"] == "25.12"


def test_lockfile_yaml_matches_constant():
    lock_path = Path(__file__).with_name("lockfile.yaml")
    on_disk = yaml.safe_load(lock_path.read_text(encoding="utf-8"))
    assert on_disk["files"].keys() == LOCKFILE["files"].keys()
    assert on_disk["release"] == LOCKFILE["release"]


def test_reject_mutable_url_accepts_pinned_2512():
    _reject_mutable_url(
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/25.12/output/"
        "association_overall_direct/part-00000-aaa1c63d-a07c-4486-af49-f58da5ca71d5-c000.snappy.parquet"
    )


@pytest.mark.parametrize(
    "url",
    [
        "http://ftp.ebi.ac.uk/pub/databases/opentargets/platform/25.12/output/disease/disease.parquet",
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/latest/output/disease/disease.parquet",
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/master/output/disease/disease.parquet",
        "https://example.com/25.12/output/disease/disease.parquet",
        "https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/25.12/output/disease/disease.csv",
    ],
)
def test_reject_mutable_url_rejects(url):
    with pytest.raises(ValueError):
        _reject_mutable_url(url)


_TARGETS = {
    "ENSG00000157764": {"approvedSymbol": "BRAF", "approvedName": "B-Raf proto-oncogene", "biotype": "protein_coding"},
    "ENSG00000999999": {"approvedSymbol": "", "approvedName": "Only A Name", "biotype": "lncRNA"},
}
_DISEASES = {
    "EFO_0000305": {"name": "breast carcinoma"},
    "MONDO_0007254": {"name": "breast cancer"},
}


def _assoc(t, d, s):
    return {"targetId": t, "diseaseId": d, "score": s}


def test_orientation_and_normalization():
    tables = build_opentargets_tables([_assoc("ENSG00000157764", "EFO_0000305", 0.5)], _TARGETS, _DISEASES)
    assert tables.edges == [("ENSEMBL:ENSG00000157764", "EFO:0000305", 0.5)]
    by_key = {n["member_key"]: n for n in tables.nodes}
    assert by_key["ENSEMBL:ENSG00000157764"]["member_kind"] == "target"
    assert by_key["EFO:0000305"]["member_kind"] == "disease"
    assert PREDICATE == "associated_with"


def test_target_label_prefers_symbol_then_name():
    tables = build_opentargets_tables(
        [_assoc("ENSG00000157764", "EFO_0000305", 0.5), _assoc("ENSG00000999999", "EFO_0000305", 0.5)],
        _TARGETS,
        _DISEASES,
    )
    by_key = {n["member_key"]: n for n in tables.nodes}
    assert by_key["ENSEMBL:ENSG00000157764"]["label"] == "BRAF"
    assert by_key["ENSEMBL:ENSG00000157764"]["symbol"] == "BRAF"
    assert by_key["ENSEMBL:ENSG00000157764"]["biotype"] == "protein_coding"
    assert by_key["ENSEMBL:ENSG00000999999"]["label"] == "Only A Name"  # blank symbol -> name


def test_disease_label_is_name():
    tables = build_opentargets_tables([_assoc("ENSG00000157764", "MONDO_0007254", 0.5)], _TARGETS, _DISEASES)
    by_key = {n["member_key"]: n for n in tables.nodes}
    assert by_key["MONDO:0007254"]["label"] == "breast cancer"
    assert by_key["MONDO:0007254"]["symbol"] == ""


def test_id_form_gate_rejects_non_ensg_target():
    with pytest.raises(ValueError, match="ENSG"):
        build_opentargets_tables([_assoc("FOO123", "EFO_0000305", 0.5)], _TARGETS, _DISEASES)


def test_unknown_or_malformed_disease_prefix_rejected():
    with pytest.raises(ValueError, match="prefix"):
        build_opentargets_tables([_assoc("ENSG00000157764", "XYZ_1", 0.5)], _TARGETS, _DISEASES)
    with pytest.raises(ValueError, match="prefix"):
        build_opentargets_tables([_assoc("ENSG00000157764", "EFO00000", 0.5)], _TARGETS, _DISEASES)  # no underscore
    assert "EFO" in KNOWN_DISEASE_PREFIXES and "Orphanet" in KNOWN_DISEASE_PREFIXES


@pytest.mark.parametrize("bad", [None, -0.1, 1.1, float("nan"), float("inf"), "0.5", True])
def test_score_gate(bad):
    with pytest.raises(ValueError):
        build_opentargets_tables([_assoc("ENSG00000157764", "EFO_0000305", bad)], _TARGETS, _DISEASES)


def test_duplicate_edge_rejected():
    with pytest.raises(ValueError, match="duplicate"):
        build_opentargets_tables(
            [_assoc("ENSG00000157764", "EFO_0000305", 0.5), _assoc("ENSG00000157764", "EFO_0000305", 0.6)],
            _TARGETS,
            _DISEASES,
        )


def test_edges_sorted_by_subject_then_object():
    tables = build_opentargets_tables(
        [_assoc("ENSG00000157764", "MONDO_0007254", 0.5), _assoc("ENSG00000157764", "EFO_0000305", 0.5)],
        _TARGETS,
        _DISEASES,
    )
    pairs = [(s, o) for s, o, _ in tables.edges]
    assert pairs == sorted(pairs)


def test_nodes_sorted_and_unique():
    tables = build_opentargets_tables(
        [_assoc("ENSG00000157764", "EFO_0000305", 0.5), _assoc("ENSG00000157764", "MONDO_0007254", 0.5)],
        _TARGETS,
        _DISEASES,
    )
    keys = [n["member_key"] for n in tables.nodes]
    assert keys == sorted(keys)
    assert len(keys) == len(set(keys))


def test_join_miss_target_falls_back_to_curie_and_counts():
    tables = build_opentargets_tables([_assoc("ENSG00000000001", "EFO_0000305", 0.5)], {}, _DISEASES)
    by_key = {n["member_key"]: n for n in tables.nodes}
    assert by_key["ENSEMBL:ENSG00000000001"]["label"] == "ENSEMBL:ENSG00000000001"
    assert tables.summary["join_miss_target_count"] == 1
    assert tables.summary["label_fallback_count"] >= 1


def test_summary_keys_counts_and_prefixes():
    tables = build_opentargets_tables(
        [_assoc("ENSG00000157764", "EFO_0000305", 0.5), _assoc("ENSG00000157764", "MONDO_0007254", 0.5)],
        _TARGETS,
        _DISEASES,
    )
    s = tables.summary
    assert s["edge_count"] == 2
    assert s["member_count"] == len(tables.nodes) == 3
    assert s["kind_counts"] == {"target": 1, "disease": 2}
    assert s["participating_target_count"] == 1
    assert s["participating_disease_count"] == 2
    assert s["disease_prefix_counts"] == {"EFO": 1, "MONDO": 1}
    assert {
        "member_count", "edge_count", "kind_counts", "participating_target_count",
        "participating_disease_count", "disease_prefix_counts", "label_fallback_count",
        "join_miss_target_count", "join_miss_disease_count",
    } <= set(s)
