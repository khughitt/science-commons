from __future__ import annotations

import json
from pathlib import Path

import pytest

from build import (
    OBO_REPLACED_BY,
    build_mondo_tables,
    curie_or_iri,
    load_obograph,
)


def _fixture_graph() -> dict[str, object]:
    return {
        "graphs": [
            {
                "nodes": [
                    {
                        "id": "http://purl.obolibrary.org/obo/MONDO_0000001",
                        "lbl": "disease",
                        "type": "CLASS",
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/MONDO_0005148",
                        "lbl": "type 2 diabetes mellitus",
                        "type": "CLASS",
                        "meta": {
                            "xrefs": [{"val": "OMIM:125853"}, {"val": "NCIT:C26747"}],
                        },
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/MONDO_0008549",
                        "lbl": "obsolete thoracic dysostosis, isolated",
                        "type": "CLASS",
                        "meta": {
                            "deprecated": True,
                            "basicPropertyValues": [
                                {
                                    "pred": OBO_REPLACED_BY,
                                    "val": "http://purl.obolibrary.org/obo/MONDO_0979242",
                                }
                            ],
                        },
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/HP_0000001",
                        "lbl": "external phenotype",
                        "type": "CLASS",
                    },
                ],
                "edges": [
                    {
                        "sub": "http://purl.obolibrary.org/obo/MONDO_0005148",
                        "pred": "is_a",
                        "obj": "http://purl.obolibrary.org/obo/MONDO_0000001",
                    },
                    {
                        "sub": "http://purl.obolibrary.org/obo/MONDO_0005148",
                        "pred": "http://purl.obolibrary.org/obo/RO_0004024",
                        "obj": "http://purl.obolibrary.org/obo/GO_0034651",
                    },
                    {
                        "sub": "http://purl.obolibrary.org/obo/HP_0000001",
                        "pred": "is_a",
                        "obj": "http://purl.obolibrary.org/obo/MONDO_0000001",
                    },
                ],
            }
        ]
    }


def test_curie_or_iri_normalizes_obo_purls_only() -> None:
    assert curie_or_iri("http://purl.obolibrary.org/obo/MONDO_0005148") == "MONDO:0005148"
    assert curie_or_iri("http://purl.obolibrary.org/obo/RO_0004024") == "RO:0004024"
    assert curie_or_iri("http://identifiers.org/hgnc/10001") == "http://identifiers.org/hgnc/10001"


def test_load_obograph_requires_single_graph(tmp_path: Path) -> None:
    path = tmp_path / "mondo.json"
    path.write_text(json.dumps(_fixture_graph()), encoding="utf-8")

    graph = load_obograph(path)

    assert len(graph["nodes"]) == 4
    assert len(graph["edges"]) == 3


def test_build_mondo_tables_extracts_nodes_edges_xrefs_and_replacements() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_mondo_tables(graph)

    assert tables.nodes == [
        {
            "member_key": "MONDO:0000001",
            "member_kind": "term",
            "label": "disease",
            "status": "active",
            "replaced_by": "",
            "dataset_usage": "[]",
        },
        {
            "member_key": "MONDO:0005148",
            "member_kind": "term",
            "label": "type 2 diabetes mellitus",
            "status": "active",
            "replaced_by": "",
            "dataset_usage": "[]",
        },
        {
            "member_key": "MONDO:0008549",
            "member_kind": "term",
            "label": "obsolete thoracic dysostosis, isolated",
            "status": "deprecated",
            "replaced_by": "MONDO:0979242",
            "dataset_usage": "[]",
        },
    ]
    assert {
        (row["subject"], row["predicate"], row["object"])
        for row in tables.edges
    } == {
        ("MONDO:0005148", "is_a", "MONDO:0000001"),
        ("MONDO:0005148", "RO:0004024", "GO:0034651"),
        ("HP:0000001", "is_a", "MONDO:0000001"),
        ("MONDO:0005148", "xref", "OMIM:125853"),
        ("MONDO:0005148", "xref", "NCIT:C26747"),
    }
    assert tables.summary["member_count"] == 3
    assert tables.summary["status_counts"] == {"active": 2, "deprecated": 1, "withdrawn": 0}
    assert tables.summary["label_fallback_count"] == 0
    assert tables.summary["skipped_non_class_mondo_count"] == 0
    assert tables.summary["edge_count"] == 5


def test_build_mondo_tables_rejects_blank_active_mondo_label() -> None:
    graph = _fixture_graph()["graphs"][0]
    graph["nodes"][0]["lbl"] = ""

    with pytest.raises(ValueError, match="blank label"):
        build_mondo_tables(graph)


def test_build_mondo_tables_uses_counted_member_key_label_for_blank_deprecated_terms() -> None:
    graph = _fixture_graph()["graphs"][0]
    graph["nodes"][2]["lbl"] = ""

    tables = build_mondo_tables(graph)

    deprecated = [row for row in tables.nodes if row["member_key"] == "MONDO:0008549"][0]
    assert deprecated["label"] == "MONDO:0008549"
    assert tables.summary["label_fallback_count"] == 1


def test_build_mondo_tables_rejects_duplicate_mondo_ids() -> None:
    graph = _fixture_graph()["graphs"][0]
    graph["nodes"].append(dict(graph["nodes"][1]))

    with pytest.raises(ValueError, match="duplicate MONDO node"):
        build_mondo_tables(graph)


def test_build_mondo_tables_skips_mondo_non_class_nodes() -> None:
    graph = _fixture_graph()["graphs"][0]
    graph["nodes"].append(
        {
            "id": "http://purl.obolibrary.org/obo/MONDO_0100332",
            "lbl": "disease has primary infectious agent",
            "type": "PROPERTY",
        }
    )

    tables = build_mondo_tables(graph)

    assert "MONDO:0100332" not in {row["member_key"] for row in tables.nodes}
    assert tables.summary["skipped_non_class_mondo_count"] == 1
