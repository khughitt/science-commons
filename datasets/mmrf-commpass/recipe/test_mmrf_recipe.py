from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pandas as pd
import pytest
import yaml

RECIPE_DIR = Path(__file__).parent
sys.path.insert(0, str(RECIPE_DIR))


def _fixture(name: str) -> Path:
    return RECIPE_DIR / "fixtures" / name


def _load_json(name: str) -> dict:
    return json.loads(_fixture(name).read_text(encoding="utf-8"))


def test_file_filter_is_open_rnaseq_gene_expression_tsv():
    from fetch_manifest import build_file_filter

    filt = build_file_filter()
    assert filt == {
        "op": "and",
        "content": [
            {"op": "in", "content": {"field": "cases.project.project_id", "value": ["MMRF-COMMPASS"]}},
            {"op": "in", "content": {"field": "access", "value": ["open"]}},
            {"op": "in", "content": {"field": "data_type", "value": ["Gene Expression Quantification"]}},
            {"op": "in", "content": {"field": "experimental_strategy", "value": ["RNA-Seq"]}},
            {"op": "in", "content": {"field": "data_format", "value": ["TSV"]}},
        ],
    }


def test_normalize_file_hit_extracts_case_sample_and_gdc_url():
    from fetch_manifest import normalize_file_hit

    hit = _load_json("files_page.json")["data"]["hits"][0]
    row = normalize_file_hit(hit)
    assert row["file_id"] == "01888e3c-45ec-493f-9a8a-57cada28dc6c"
    assert row["case_id"] == "case-1"
    assert row["case_submitter_id"] == "MMRF_0001"
    assert row["sample_submitter_id"] == "MMRF_0001_1_BM_CD138pos"
    assert row["access"] == "open"
    assert row["gdc_download_url"].endswith("/data/01888e3c-45ec-493f-9a8a-57cada28dc6c")


def test_normalize_file_hit_rejects_ambiguous_case_or_sample_links():
    from fetch_manifest import normalize_file_hit

    hit = dict(_load_json("files_page.json")["data"]["hits"][0])
    hit["cases"] = [hit["cases"][0], hit["cases"][0]]
    with pytest.raises(ValueError, match="exactly one linked case"):
        normalize_file_hit(hit)

    hit = dict(_load_json("files_page.json")["data"]["hits"][0])
    case = dict(hit["cases"][0])
    case["samples"] = [case["samples"][0], case["samples"][0]]
    hit["cases"] = [case]
    with pytest.raises(ValueError, match="exactly one linked sample"):
        normalize_file_hit(hit)


def test_normalize_file_hit_requires_explicit_file_id():
    from fetch_manifest import normalize_file_hit

    hit = dict(_load_json("files_page.json")["data"]["hits"][0])
    hit["id"] = hit.pop("file_id")
    with pytest.raises(ValueError, match="file_id"):
        normalize_file_hit(hit)


def test_manifest_count_must_match_independent_count():
    from fetch_manifest import validate_manifest_count

    with pytest.raises(ValueError, match="manifest count"):
        validate_manifest_count([{"file_id": "a"}, {"file_id": "b"}], expected_total=3)
    validate_manifest_count([{"file_id": "a"}, {"file_id": "b"}], expected_total=2)


def test_endpoint_discovery_accepts_progression_and_rejects_survival_only():
    from fetch_manifest import discover_endpoint_fields

    progression = discover_endpoint_fields(_load_json("cases_progression.json")["data"]["hits"])
    assert progression["status"] == "progression-ready"
    assert "days_to_recurrence" in progression["progression_fields"]
    assert "progression_or_recurrence" in progression["progression_fields"]
    assert progression["usable_progression_outcome_count"] == 3

    survival_only = discover_endpoint_fields(_load_json("cases_survival_only.json")["data"]["hits"])
    assert survival_only["status"] == "survival-only"
    assert "vital_status" in survival_only["survival_fields"]
    assert survival_only["progression_fields"] == []
    assert survival_only["usable_progression_outcome_count"] == 0


def test_endpoint_discovery_ignores_unknown_progression_status_without_usable_time():
    from fetch_manifest import discover_endpoint_fields

    report = discover_endpoint_fields(
        [
            {
                "case_id": "case-1",
                "submitter_id": "MMRF_0001",
                "diagnoses": [
                    {
                        "progression_or_recurrence": "unknown",
                        "days_to_last_follow_up": 500,
                    }
                ],
            }
        ]
    )

    assert report["status"] == "missing-endpoint"
    assert report["progression_fields"] == []
    assert report["usable_progression_outcome_count"] == 0


def test_write_dry_run_outputs_manifest_query_and_validation(tmp_path):
    from fetch_manifest import StaticGdcClient, build_file_filter, write_dry_run

    client = StaticGdcClient(
        status_payload={
            "data_release": "Data Release 45.0 - December 04, 2025",
            "commit": "fixture",
            "status": "OK",
        },
        file_total=3,
        file_pages=[_load_json("files_page.json")],
        case_pages=[_load_json("cases_progression.json")],
    )
    report = write_dry_run(output_dir=tmp_path, client=client)
    assert report["endpoint_status"] == "progression-ready"
    assert report["file_count"] == 3
    assert (tmp_path / "manifest" / "files.parquet").is_file()
    assert (tmp_path / "manifest" / "query.json").is_file()
    assert (tmp_path / "reports" / "validation.json").is_file()
    query = json.loads((tmp_path / "manifest" / "query.json").read_text(encoding="utf-8"))
    validation = json.loads((tmp_path / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert query == build_file_filter()
    assert validation["file_filter"] == build_file_filter()
    assert validation["file_count"] == 3
    assert validation["independent_file_total"] == 3
    assert validation["case_count"] == 3
    assert validation["endpoint_status"] == "progression-ready"
    assert validation["gdc_data_release"] == "Data Release 45.0 - December 04, 2025"
    assert validation["promotable"] is True
    manifest = pd.read_parquet(tmp_path / "manifest" / "files.parquet")
    assert list(manifest["file_id"]) == [
        "01888e3c-45ec-493f-9a8a-57cada28dc6c",
        "cecfa7eb-7774-4acb-a939-7fc2c6e6ef10",
        "438b6fcb-c193-49bb-8fc8-796ab701f0eb",
    ]


def test_write_dry_run_refuses_survival_only_for_progression_task(tmp_path):
    from fetch_manifest import StaticGdcClient, write_dry_run

    survival_page = _load_json("cases_survival_only.json")
    survival_page["data"]["hits"].append(
        {
            "case_id": "case-3",
            "submitter_id": "MMRF_0003",
            "diagnoses": [{"days_to_last_follow_up": 700}],
            "demographic": {
                "vital_status": "Alive",
                "days_to_death": None,
            },
        }
    )
    survival_page["data"]["pagination"]["count"] = 3
    survival_page["data"]["pagination"]["total"] = 3
    client = StaticGdcClient(
        status_payload={
            "data_release": "Data Release 45.0 - December 04, 2025",
            "commit": "fixture",
            "status": "OK",
        },
        file_total=3,
        file_pages=[_load_json("files_page.json")],
        case_pages=[survival_page],
    )
    with pytest.raises(ValueError, match="overall-survival"):
        write_dry_run(output_dir=tmp_path, client=client)


def test_write_dry_run_refuses_missing_manifest_case_metadata(tmp_path):
    from fetch_manifest import StaticGdcClient, write_dry_run

    progression_subset = _load_json("cases_progression.json")
    progression_subset["data"]["hits"] = progression_subset["data"]["hits"][:2]
    progression_subset["data"]["pagination"]["count"] = 2
    progression_subset["data"]["pagination"]["total"] = 2

    client = StaticGdcClient(
        status_payload={
            "data_release": "Data Release 45.0 - December 04, 2025",
            "commit": "fixture",
            "status": "OK",
        },
        file_total=3,
        file_pages=[_load_json("files_page.json")],
        case_pages=[progression_subset],
    )

    with pytest.raises(ValueError, match="missing manifest cases"):
        write_dry_run(output_dir=tmp_path, client=client)

    assert (tmp_path / "manifest" / "files.parquet").is_file()
    assert (tmp_path / "manifest" / "cases.json").is_file()
    assert (tmp_path / "manifest" / "query.json").is_file()
    validation = json.loads((tmp_path / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert validation["endpoint_status"] == "progression-ready"
    assert validation["missing_manifest_case_ids"] == ["case-3"]
    assert validation["promotable"] is False


def test_write_dry_run_requires_progression_on_manifest_cases(tmp_path):
    from fetch_manifest import StaticGdcClient, write_dry_run

    off_manifest_progression_case = {
        "case_id": "case-99",
        "submitter_id": "MMRF_0099",
        "diagnoses": [
            {
                "days_to_recurrence": 100,
                "progression_or_recurrence": "yes",
                "days_to_last_follow_up": 150,
            }
        ],
    }
    manifest_case_without_progression = {
        "case_id": "case-1",
        "submitter_id": "MMRF_0001",
        "diagnoses": [{"days_to_last_follow_up": 500}],
    }
    case_page = {
        "data": {
            "hits": [off_manifest_progression_case, manifest_case_without_progression],
            "pagination": {"count": 2, "total": 2, "size": 2, "from": 0, "page": 1, "pages": 1},
        }
    }

    client = StaticGdcClient(
        status_payload={
            "data_release": "Data Release 45.0 - December 04, 2025",
            "commit": "fixture",
            "status": "OK",
        },
        file_total=1,
        file_pages=[
            {
                "data": {
                    "hits": [_load_json("files_page.json")["data"]["hits"][0]],
                    "pagination": {"count": 1, "total": 1, "size": 1, "from": 0, "page": 1, "pages": 1},
                }
            }
        ],
        case_pages=[case_page],
    )

    with pytest.raises(ValueError, match="progression endpoint"):
        write_dry_run(output_dir=tmp_path, client=client)
    validation = json.loads((tmp_path / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert validation["endpoint_status"] == "missing-endpoint"
    assert validation["case_count"] == 1
    assert validation["promotable"] is False


def test_live_gdc_client_rejects_empty_page_before_total():
    from fetch_manifest import LiveGdcClient

    class EmptySecondPageClient(LiveGdcClient):
        def __init__(self) -> None:
            super().__init__(api_base="https://example.test", page_size=1)
            self.calls = 0

        def _post_json(self, url, payload):
            self.calls += 1
            if self.calls == 1:
                return {
                    "data": {
                        "hits": [{"case_id": "case-1"}],
                        "pagination": {"count": 1, "total": 2, "size": 1, "from": 0},
                    }
                }
            return {
                "data": {
                    "hits": [],
                    "pagination": {"count": 0, "total": 2, "size": 1, "from": 1},
                }
            }

    client = EmptySecondPageClient()
    with pytest.raises(ValueError, match="empty cases page"):
        list(client._iter_endpoint("cases", filters={}, fields=["case_id"], expand=None))


def test_parse_expression_tsv_selects_measure_and_skips_summary_rows(tmp_path):
    from build import parse_expression_tsv

    rows = parse_expression_tsv(
        _fixture("expression_counts.tsv"),
        sample_submitter_id="MMRF_0001_1_BM_CD138pos",
        case_submitter_id="MMRF_0001",
        measure="tpm_unstranded",
    )
    assert rows == [
        {
            "case_submitter_id": "MMRF_0001",
            "sample_submitter_id": "MMRF_0001_1_BM_CD138pos",
            "gene_id": "ENSG00000141510.18",
            "gene_name": "TP53",
            "measure": "tpm_unstranded",
            "value": 12.5,
        },
        {
            "case_submitter_id": "MMRF_0001",
            "sample_submitter_id": "MMRF_0001_1_BM_CD138pos",
            "gene_id": "ENSG00000171862.13",
            "gene_name": "PTEN",
            "measure": "tpm_unstranded",
            "value": 9.0,
        },
    ]


def test_build_package_writes_tables_and_deterministic_splits(tmp_path):
    from build import build_package

    source_dir = tmp_path / "_src" / "expression"
    source_dir.mkdir(parents=True)
    for file_id in [
        "01888e3c-45ec-493f-9a8a-57cada28dc6c",
        "cecfa7eb-7774-4acb-a939-7fc2c6e6ef10",
        "438b6fcb-c193-49bb-8fc8-796ab701f0eb",
    ]:
        (source_dir / f"{file_id}.tsv").write_text(_fixture("expression_counts.tsv").read_text(encoding="utf-8"), encoding="utf-8")

    manifest_dir = tmp_path / "manifest"
    manifest_dir.mkdir()
    rows = []
    for hit in _load_json("files_page.json")["data"]["hits"]:
        from fetch_manifest import normalize_file_hit

        rows.append(normalize_file_hit(hit))
    pd.DataFrame(rows).to_parquet(manifest_dir / "files.parquet", index=False)
    (manifest_dir / "cases.json").write_text(json.dumps(_load_json("cases_progression.json")["data"]["hits"]), encoding="utf-8")

    summary = build_package(output_dir=tmp_path, measure="tpm_unstranded", split_salt="fixture-salt")
    assert summary["expression_rows"] == 6
    assert summary["outcome_rows"] == 3
    assert summary["split_salt"] == "fixture-salt"
    assert (tmp_path / "data" / "expression.parquet").is_file()
    assert (tmp_path / "data" / "samples.parquet").is_file()
    assert (tmp_path / "data" / "outcomes.parquet").is_file()
    assert (tmp_path / "splits" / "heldout_patient_v1.parquet").is_file()

    expression = pd.read_parquet(tmp_path / "data" / "expression.parquet")
    samples = pd.read_parquet(tmp_path / "data" / "samples.parquet")
    sample_records = samples.sort_values("case_submitter_id").to_dict(orient="records")
    assert sample_records == [
        {
            "case_id": "case-1",
            "case_submitter_id": "MMRF_0001",
            "sample_submitter_id": "MMRF_0001_1_BM_CD138pos",
            "sample_type": "Primary Blood Derived Cancer - Bone Marrow",
            "file_id": "01888e3c-45ec-493f-9a8a-57cada28dc6c",
            "file_name": "1b166f66-85d0-4c18-aaee-fe0abe0338d1.rna_seq.augmented_star_gene_counts.tsv",
        },
        {
            "case_id": "case-2",
            "case_submitter_id": "MMRF_0002",
            "sample_submitter_id": "MMRF_0002_1_BM_CD138pos",
            "sample_type": "Primary Blood Derived Cancer - Bone Marrow",
            "file_id": "cecfa7eb-7774-4acb-a939-7fc2c6e6ef10",
            "file_name": "28ee3050-59fa-4b12-ae15-94b8314e6f6b.rna_seq.augmented_star_gene_counts.tsv",
        },
        {
            "case_id": "case-3",
            "case_submitter_id": "MMRF_0003",
            "sample_submitter_id": "MMRF_0003_1_BM_CD138pos",
            "sample_type": "Primary Blood Derived Cancer - Bone Marrow",
            "file_id": "438b6fcb-c193-49bb-8fc8-796ab701f0eb",
            "file_name": "ce2a08cd-8f72-403f-afa9-d378bc0df604.rna_seq.augmented_star_gene_counts.tsv",
        },
    ]
    expression_records = sorted(
        (
            row["case_submitter_id"],
            row["sample_submitter_id"],
            row["gene_id"],
            row["gene_name"],
            row["measure"],
            row["value"],
        )
        for row in expression.to_dict(orient="records")
    )
    assert expression_records == [
        ("MMRF_0001", "MMRF_0001_1_BM_CD138pos", "ENSG00000141510.18", "TP53", "tpm_unstranded", 12.5),
        ("MMRF_0001", "MMRF_0001_1_BM_CD138pos", "ENSG00000171862.13", "PTEN", "tpm_unstranded", 9.0),
        ("MMRF_0002", "MMRF_0002_1_BM_CD138pos", "ENSG00000141510.18", "TP53", "tpm_unstranded", 12.5),
        ("MMRF_0002", "MMRF_0002_1_BM_CD138pos", "ENSG00000171862.13", "PTEN", "tpm_unstranded", 9.0),
        ("MMRF_0003", "MMRF_0003_1_BM_CD138pos", "ENSG00000141510.18", "TP53", "tpm_unstranded", 12.5),
        ("MMRF_0003", "MMRF_0003_1_BM_CD138pos", "ENSG00000171862.13", "PTEN", "tpm_unstranded", 9.0),
    ]

    splits = pd.read_parquet(tmp_path / "splits" / "heldout_patient_v1.parquet")
    split_rows = splits.sort_values("case_submitter_id").to_dict(orient="records")
    assert split_rows == [
        {
            "case_submitter_id": "MMRF_0001",
            "split": "validation",
            "split_basis": "f08b1e03337b2185919b4abc9c92f2d8b45dd5dbb45074a215fca9669b3a20b5",
        },
        {
            "case_submitter_id": "MMRF_0002",
            "split": "test",
            "split_basis": "f5fb52d88e1575e01d6d3c2a7a9bc80d2d619a3bd4f93a3693bcf29109cf4952",
        },
        {
            "case_submitter_id": "MMRF_0003",
            "split": "train",
            "split_basis": "976a9375c856d8b5f682c01e3492815690f34d997bad97d0cbb20ef9c8fd082a",
        },
    ]
    outcomes = pd.read_parquet(tmp_path / "data" / "outcomes.parquet")
    censored = outcomes.set_index("case_submitter_id").loc["MMRF_0002"]
    assert bool(censored["event_observed"]) is False
    assert censored["time_to_event_days"] == 900


def test_build_package_refuses_manifest_case_without_outcome(tmp_path):
    from build import build_package
    from fetch_manifest import normalize_file_hit

    source_dir = tmp_path / "_src" / "expression"
    source_dir.mkdir(parents=True)
    rows = []
    for hit in _load_json("files_page.json")["data"]["hits"]:
        row = normalize_file_hit(hit)
        rows.append(row)
        (source_dir / f"{row['file_id']}.tsv").write_text(_fixture("expression_counts.tsv").read_text(encoding="utf-8"), encoding="utf-8")

    manifest_dir = tmp_path / "manifest"
    manifest_dir.mkdir()
    pd.DataFrame(rows).to_parquet(manifest_dir / "files.parquet", index=False)
    cases = _load_json("cases_progression.json")["data"]["hits"]
    cases[1]["diagnoses"][0]["progression_or_recurrence"] = "not reported"
    (manifest_dir / "cases.json").write_text(json.dumps(cases), encoding="utf-8")

    with pytest.raises(ValueError, match="outcome.*MMRF_0002"):
        build_package(output_dir=tmp_path, measure="tpm_unstranded", split_salt="fixture-salt")


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("case_id", ""),
        ("case_submitter_id", " "),
        ("sample_submitter_id", None),
        ("file_id", float("nan")),
        ("file_name", ""),
    ],
)
def test_build_package_refuses_blank_manifest_identity_fields(tmp_path, field, bad_value):
    from build import build_package
    from fetch_manifest import normalize_file_hit

    source_dir = tmp_path / "_src" / "expression"
    source_dir.mkdir(parents=True)
    rows = []
    for hit in _load_json("files_page.json")["data"]["hits"]:
        row = normalize_file_hit(hit)
        rows.append(row)
        (source_dir / f"{row['file_id']}.tsv").write_text(_fixture("expression_counts.tsv").read_text(encoding="utf-8"), encoding="utf-8")
    rows[0][field] = bad_value

    manifest_dir = tmp_path / "manifest"
    manifest_dir.mkdir()
    pd.DataFrame(rows).to_parquet(manifest_dir / "files.parquet", index=False)
    (manifest_dir / "cases.json").write_text(json.dumps(_load_json("cases_progression.json")["data"]["hits"]), encoding="utf-8")

    with pytest.raises(ValueError, match=f"Manifest.*{field}"):
        build_package(output_dir=tmp_path, measure="tpm_unstranded", split_salt="fixture-salt")


def test_build_package_refuses_patient_leakage_and_empty_splits():
    from build import validate_no_patient_leakage, validate_nonempty_splits

    validate_no_patient_leakage(
        pd.DataFrame(
            [
                {"case_submitter_id": "MMRF_0001", "split": "train"},
                {"case_submitter_id": "MMRF_0002", "split": "test"},
            ]
        )
    )
    with pytest.raises(ValueError, match="leakage"):
        validate_no_patient_leakage(
            pd.DataFrame(
                [
                    {"case_submitter_id": "MMRF_0001", "split": "train"},
                    {"case_submitter_id": "MMRF_0001", "split": "test"},
                ]
            )
        )
    validate_nonempty_splits(
        pd.DataFrame(
            [
                {"case_submitter_id": "MMRF_0001", "split": "train"},
                {"case_submitter_id": "MMRF_0002", "split": "validation"},
                {"case_submitter_id": "MMRF_0003", "split": "test"},
            ]
        )
    )
    with pytest.raises(ValueError, match="nonempty"):
        validate_nonempty_splits(
            pd.DataFrame(
                [
                    {"case_submitter_id": "MMRF_0001", "split": "train"},
                    {"case_submitter_id": "MMRF_0002", "split": "train"},
                    {"case_submitter_id": "MMRF_0003", "split": "test"},
                ]
            )
        )


def test_build_datapackage_doc_records_resources_and_split_method(tmp_path):
    from build_datapackage import build_datapackage_doc

    for rel, payload in {
        "manifest/files.parquet": b"manifest",
        "manifest/query.json": b"{}",
        "manifest/cases.json": b"[]",
        "data/expression.parquet": b"expr",
        "data/samples.parquet": b"samples",
        "data/outcomes.parquet": b"outcomes",
        "splits/heldout_patient_v1.parquet": b"splits",
        "reports/validation.json": b'{"split_salt":"fixture-salt"}',
        "reports/build-summary.json": b'{"split_salt":"fixture-salt"}',
    }.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)

    doc = build_datapackage_doc(tmp_path, split_salt="fixture-salt", gdc_data_release="Data Release 45.0 - December 04, 2025")
    assert doc["name"] == "mmrf-commpass"
    assert doc["profile"] == "data-package"
    assert doc["gdc_data_release"] == "Data Release 45.0 - December 04, 2025"
    assert doc["split"]["method"] == "sha256(case_submitter_id || split_salt)"
    assert doc["split"]["split_salt"] == "fixture-salt"
    resource_names = {r["name"] for r in doc["resources"]}
    assert resource_names == {
        "files_manifest",
        "query",
        "cases",
        "expression",
        "samples",
        "outcomes",
        "heldout_patient_split",
        "validation",
        "build_summary",
    }
    expression = next(r for r in doc["resources"] if r["name"] == "expression")
    assert expression["hash"] == "sha256:" + hashlib.sha256(b"expr").hexdigest()
    assert expression["source"]["ref"].endswith("/mmrf-commpass/data/expression.parquet")
    assert doc["provenance"] == [{"tool": "recipe/build.py"}]


def test_entity_remains_pointer_until_promoted():
    entity_text = (RECIPE_DIR.parent / "entity.md").read_text(encoding="utf-8")
    fm = yaml.safe_load(entity_text.split("---", 2)[1])
    assert fm["dataset_class"] == "pointer"
    assert "datapackage" not in fm
