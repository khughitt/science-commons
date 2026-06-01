from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from build import (
    OBO_REPLACED_BY,
    build_go_tables,
    curie_or_iri,
    load_obograph,
)

OBO_NAMESPACE = "http://www.geneontology.org/formats/oboInOwl#hasOBONamespace"


def _fixture_graph() -> dict[str, Any]:
    return {
        "graphs": [
            {
                "nodes": [
                    {
                        "id": "http://purl.obolibrary.org/obo/GO_0008150",
                        "lbl": "biological_process",
                        "type": "CLASS",
                        "meta": {
                            "basicPropertyValues": [
                                {
                                    "pred": OBO_NAMESPACE,
                                    "val": "biological_process",
                                }
                            ],
                            "xrefs": [{"val": "Wikipedia:Biological_process"}],
                        },
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/GO_0003674",
                        "lbl": "molecular_function",
                        "type": "CLASS",
                        "meta": {
                            "basicPropertyValues": [
                                {
                                    "pred": OBO_NAMESPACE,
                                    "val": "molecular_function",
                                }
                            ],
                        },
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/GO_0005575",
                        "lbl": "cellular_component",
                        "type": "CLASS",
                        "meta": {
                            "basicPropertyValues": [
                                {
                                    "pred": OBO_NAMESPACE,
                                    "val": "cellular_component",
                                }
                            ],
                        },
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/GO_0009987",
                        "lbl": "cellular process",
                        "type": "CLASS",
                        "meta": {
                            "basicPropertyValues": [
                                {
                                    "pred": OBO_NAMESPACE,
                                    "val": "biological_process",
                                }
                            ],
                        },
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/GO_0065007",
                        "lbl": "biological regulation",
                        "type": "CLASS",
                        "meta": {
                            "basicPropertyValues": [
                                {
                                    "pred": OBO_NAMESPACE,
                                    "val": "biological_process",
                                }
                            ],
                        },
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/GO_0000000",
                        "lbl": "obsolete go term",
                        "type": "CLASS",
                        "meta": {
                            "deprecated": True,
                            "basicPropertyValues": [
                                {
                                    "pred": OBO_NAMESPACE,
                                    "val": "biological_process",
                                },
                                {
                                    "pred": OBO_REPLACED_BY,
                                    "val": "http://purl.obolibrary.org/obo/GO_0008150",
                                },
                            ],
                        },
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/GO_0099999",
                        "lbl": "go term without namespace",
                        "type": "CLASS",
                    },
                    {
                        "id": "http://purl.obolibrary.org/obo/CL_0000000",
                        "lbl": "cell",
                        "type": "CLASS",
                    },
                ],
                "edges": [
                    {
                        "sub": "http://purl.obolibrary.org/obo/GO_0009987",
                        "pred": "is_a",
                        "obj": "http://purl.obolibrary.org/obo/GO_0008150",
                    },
                    {
                        "sub": "http://purl.obolibrary.org/obo/GO_0009987",
                        "pred": "http://purl.obolibrary.org/obo/BFO_0000050",
                        "obj": "http://purl.obolibrary.org/obo/GO_0008150",
                    },
                    {
                        "sub": "http://purl.obolibrary.org/obo/GO_0065007",
                        "pred": "http://purl.obolibrary.org/obo/RO_0002211",
                        "obj": "http://purl.obolibrary.org/obo/GO_0009987",
                    },
                    {
                        "sub": "http://purl.obolibrary.org/obo/GO_0008150",
                        "pred": "http://purl.obolibrary.org/obo/BFO_0000066",
                        "obj": "http://purl.obolibrary.org/obo/CL_0000000",
                    },
                    {
                        "sub": "http://purl.obolibrary.org/obo/CL_0000000",
                        "pred": "is_a",
                        "obj": "http://purl.obolibrary.org/obo/CL_0000001",
                    },
                ],
            }
        ]
    }


def test_curie_or_iri_normalizes_obo_purls_only() -> None:
    assert curie_or_iri("http://purl.obolibrary.org/obo/GO_0008150") == "GO:0008150"
    assert curie_or_iri("http://purl.obolibrary.org/obo/BFO_0000050") == "BFO:0000050"
    assert curie_or_iri("http://purl.obolibrary.org/obo/RO_0002211") == "RO:0002211"
    assert curie_or_iri("is_a") == "is_a"
    assert curie_or_iri("http://identifiers.org/hgnc/10001") == "http://identifiers.org/hgnc/10001"


def test_load_obograph_requires_single_graph(tmp_path: Path) -> None:
    path = tmp_path / "go.json"
    path.write_text(json.dumps(_fixture_graph()), encoding="utf-8")

    graph = load_obograph(path)

    assert len(graph["nodes"]) == 8
    assert len(graph["edges"]) == 5


def test_build_go_tables_only_go_class_nodes_are_members() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)

    member_keys = {row["member_key"] for row in tables.nodes}
    assert "CL:0000000" not in member_keys
    assert all(key.startswith("GO:") for key in member_keys)
    assert member_keys == {
        "GO:0008150",
        "GO:0003674",
        "GO:0005575",
        "GO:0009987",
        "GO:0065007",
        "GO:0000000",
        "GO:0099999",
    }


def test_build_go_tables_member_kind_is_namespace_or_term() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)
    by_key = {row["member_key"]: row for row in tables.nodes}

    assert by_key["GO:0008150"]["member_kind"] == "biological_process"
    assert by_key["GO:0003674"]["member_kind"] == "molecular_function"
    assert by_key["GO:0005575"]["member_kind"] == "cellular_component"
    assert by_key["GO:0099999"]["member_kind"] == "term"


def test_build_go_tables_nodes_sorted_by_member_key() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)

    keys = [row["member_key"] for row in tables.nodes]
    assert keys == sorted(keys)


def test_build_go_tables_edges_sorted_by_subject_predicate_object() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)

    triples = [(row["subject"], row["predicate"], row["object"]) for row in tables.edges]
    assert triples == sorted(triples)


def test_build_go_tables_predicates_and_keep_drop_rule() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)
    triples = {
        (row["subject"], row["predicate"], row["object"]) for row in tables.edges
    }

    # is_a stays a bare label
    assert ("GO:0009987", "is_a", "GO:0008150") in triples
    # part_of -> BFO:0000050
    assert ("GO:0009987", "BFO:0000050", "GO:0008150") in triples
    # regulates -> RO:0002211
    assert ("GO:0065007", "RO:0002211", "GO:0009987") in triples
    # occurs_in edge into a non-GO class kept because subject is a GO member
    assert ("GO:0008150", "BFO:0000066", "CL:0000000") in triples
    # edge with neither endpoint a GO member is dropped
    assert ("CL:0000000", "is_a", "CL:0000001") not in triples


def test_build_go_tables_emits_xref_edges() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)
    triples = {
        (row["subject"], row["predicate"], row["object"]) for row in tables.edges
    }

    assert ("GO:0008150", "xref", "Wikipedia:Biological_process") in triples


def test_build_go_tables_deprecated_blank_label_falls_back_and_counts() -> None:
    graph = _fixture_graph()["graphs"][0]
    deprecated = [
        node
        for node in graph["nodes"]
        if node["id"].endswith("GO_0000000")
    ][0]
    deprecated["lbl"] = ""

    tables = build_go_tables(graph)
    by_key = {row["member_key"]: row for row in tables.nodes}

    assert by_key["GO:0000000"]["status"] == "deprecated"
    assert by_key["GO:0000000"]["label"] == "GO:0000000"
    assert by_key["GO:0000000"]["replaced_by"] == "GO:0008150"
    assert tables.summary["label_fallback_count"] == 1


def test_build_go_tables_replaced_by_populated() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)
    by_key = {row["member_key"]: row for row in tables.nodes}

    assert by_key["GO:0000000"]["replaced_by"] == "GO:0008150"


def test_build_go_tables_rejects_blank_active_go_label() -> None:
    graph = _fixture_graph()["graphs"][0]
    graph["nodes"][0]["lbl"] = ""

    with pytest.raises(ValueError, match="blank label"):
        build_go_tables(graph)


def test_build_go_tables_rejects_duplicate_go_ids() -> None:
    graph = _fixture_graph()["graphs"][0]
    graph["nodes"].append(dict(graph["nodes"][0]))

    with pytest.raises(ValueError, match="duplicate GO node"):
        build_go_tables(graph)


def test_build_go_tables_namespace_fallback_counted() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)

    assert tables.summary["namespace_fallback_count"] == 1


def test_build_go_tables_summary_has_all_keys() -> None:
    graph = _fixture_graph()["graphs"][0]

    tables = build_go_tables(graph)
    summary = tables.summary

    assert summary["member_count"] == 7
    assert summary["edge_count"] == len(tables.edges)
    assert summary["status_counts"] == {"active": 6, "deprecated": 1, "withdrawn": 0}
    assert summary["namespace_counts"] == {
        "biological_process": 4,
        "molecular_function": 1,
        "cellular_component": 1,
    }
    assert summary["namespace_fallback_count"] == 1
    assert summary["label_fallback_count"] == 0
    assert summary["skipped_non_class_go_count"] == 0


def test_build_go_tables_skips_go_non_class_nodes() -> None:
    graph = _fixture_graph()["graphs"][0]
    graph["nodes"].append(
        {
            "id": "http://purl.obolibrary.org/obo/GO_0100000",
            "lbl": "some property",
            "type": "PROPERTY",
        }
    )

    tables = build_go_tables(graph)

    assert "GO:0100000" not in {row["member_key"] for row in tables.nodes}
    assert tables.summary["skipped_non_class_go_count"] == 1
