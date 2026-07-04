from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml

RECIPE_DIR = Path(__file__).parent
DATASET_DIR = RECIPE_DIR.parent
sys.path.insert(0, str(RECIPE_DIR))


def _fixture(name: str) -> Path:
    return RECIPE_DIR / "fixtures" / name


def _load_json(name: str) -> dict | list:
    return json.loads(_fixture(name).read_text(encoding="utf-8"))


def test_entity_declares_concrete_child_deposit_and_cross_modal_task():
    text = (DATASET_DIR / "entity.md").read_text(encoding="utf-8")
    frontmatter = yaml.safe_load(text.split("---", 2)[1])

    assert frontmatter["id"] == "dataset:cptac-gbm-2021-proteogenomics"
    assert frontmatter["dataset_class"] == "deposit"
    assert frontmatter["source_class"] == "derived"
    assert frontmatter["license"] == "ODbL-1.0"
    assert frontmatter["datapackage"] == "datapackage.yaml"
    assert frontmatter["access"] == {
        "level": "public",
        "availability": "available",
        "verified": True,
        "verification_method": "metadata-confirmed",
        "source_url": "https://github.com/cBioPortal/datahub/tree/master/public/gbm_cptac_2021",
    }

    benchmark = frontmatter["benchmark"]
    assert "dataset:cptac-proteogenomics" in benchmark["source_datasets"]
    assert {"proteomics", "bulk-rna-seq", "multimodal"}.issubset(set(benchmark["modalities"]))
    assert "multi-omic" in benchmark["signal_types"]

    tasks = {task["id"]: task for task in benchmark["tasks"]}
    task = tasks["protein-rna-cross-modal"]
    assert task["task_type"] == "cross-modal-prediction"
    assert task["prediction_target"] == "mass-spectrometry protein abundance from mRNA expression"
    assert task["held_out_unit"] == "gene-by-sample protein measurements"
    assert task["metric"] == "held-out Pearson correlation"
    assert task["baseline"] == "per-protein training-set mean"
    assert task["ground_truth"]["type"] == "measured-proteomics"
    assert task["support"]["state"] == "candidate"
    assert task["support"]["reason"] == "recipe-staged-validation-needed"


def test_parse_lfs_pointer_extracts_oid_and_size():
    from fetch_manifest import parse_lfs_pointer

    pointer = """version https://git-lfs.github.com/spec/v1
oid sha256:235cef753fc34d0168e97c145616bcfb3fe1c2f726038bef891639dfbec05722
size 29693169
"""
    parsed = parse_lfs_pointer(pointer, label="mrna")
    assert parsed == {
        "label": "mrna",
        "oid": "235cef753fc34d0168e97c145616bcfb3fe1c2f726038bef891639dfbec05722",
        "size": 29693169,
    }


def test_parse_lfs_pointer_rejects_non_pointer_payload():
    from fetch_manifest import parse_lfs_pointer

    with pytest.raises(ValueError, match="not a git LFS pointer"):
        parse_lfs_pointer("Hugo_Symbol\tC3L-00104\nEGFR\t1.0\n", label="mrna")


def test_build_lfs_batch_request_uses_exact_objects():
    from fetch_manifest import build_lfs_batch_payload

    payload = build_lfs_batch_payload(
        [
            {
                "label": "mrna",
                "oid": "235cef753fc34d0168e97c145616bcfb3fe1c2f726038bef891639dfbec05722",
                "size": 29693169,
            },
            {
                "label": "protein",
                "oid": "b5512312c26b68b1f137fa493448ecce0e9a8b44a5bd35b8cc9dfb67f68a6a0e",
                "size": 6852651,
            },
        ]
    )
    assert payload == {
        "operation": "download",
        "transfers": ["basic"],
        "objects": [
            {
                "oid": "235cef753fc34d0168e97c145616bcfb3fe1c2f726038bef891639dfbec05722",
                "size": 29693169,
            },
            {
                "oid": "b5512312c26b68b1f137fa493448ecce0e9a8b44a5bd35b8cc9dfb67f68a6a0e",
                "size": 6852651,
            },
        ],
    }


def test_batch_response_maps_download_urls_by_oid():
    from fetch_manifest import download_urls_from_batch_response

    urls = download_urls_from_batch_response(_load_json("lfs_batch_response.json"))
    assert urls == {
        "235cef753fc34d0168e97c145616bcfb3fe1c2f726038bef891639dfbec05722": "https://example.invalid/mrna",
        "b5512312c26b68b1f137fa493448ecce0e9a8b44a5bd35b8cc9dfb67f68a6a0e": "https://example.invalid/protein",
    }


def test_verify_downloaded_payload_checks_size_hash_and_pointer(tmp_path):
    from fetch_manifest import verify_downloaded_payload

    payload = tmp_path / "matrix.txt"
    payload.write_text("gene\tS1\nEGFR\t1.0\n", encoding="utf-8")
    import hashlib

    digest = hashlib.sha256(payload.read_bytes()).hexdigest()
    report = verify_downloaded_payload(payload, expected_oid=digest, expected_size=payload.stat().st_size)
    assert report == {
        "path": str(payload),
        "bytes": payload.stat().st_size,
        "sha256": digest,
        "is_lfs_pointer": False,
    }

    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        verify_downloaded_payload(payload, expected_oid="0" * 64, expected_size=payload.stat().st_size)

    pointer = tmp_path / "pointer.txt"
    pointer.write_text("version https://git-lfs.github.com/spec/v1\n", encoding="utf-8")
    pointer_digest = hashlib.sha256(pointer.read_bytes()).hexdigest()
    with pytest.raises(ValueError, match="still a git LFS pointer"):
        verify_downloaded_payload(pointer, expected_oid=pointer_digest, expected_size=pointer.stat().st_size)


def test_write_dry_run_records_metadata_and_validation(tmp_path):
    from fetch_manifest import StaticCbioPortalClient, write_dry_run

    client = StaticCbioPortalClient(
        study=_load_json("study.json"),
        molecular_profiles=_load_json("molecular_profiles.json"),
        sample_lists=_load_json("sample_lists.json"),
        pointers={
            "mrna": "version https://git-lfs.github.com/spec/v1\noid sha256:235cef753fc34d0168e97c145616bcfb3fe1c2f726038bef891639dfbec05722\nsize 29693169\n",
            "protein": "version https://git-lfs.github.com/spec/v1\noid sha256:b5512312c26b68b1f137fa493448ecce0e9a8b44a5bd35b8cc9dfb67f68a6a0e\nsize 6852651\n",
        },
    )

    report = write_dry_run(tmp_path, client=client)
    assert report["promotable"] is True
    assert report["study_id"] == "gbm_cptac_2021"
    assert report["import_date"] == "2026-01-07 13:14:46"
    assert report["profiles"] == {
        "mrna": "gbm_cptac_2021_mrna",
        "protein": "gbm_cptac_2021_protein_quantification",
    }

    validation = json.loads((tmp_path / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert validation["promotable"] is True
    assert validation["lfs_objects"]["mrna"]["size"] == 29693169
    assert validation["lfs_objects"]["protein"]["size"] == 6852651
    assert (tmp_path / "manifest" / "study.json").is_file()
    assert (tmp_path / "manifest" / "molecular_profiles.json").is_file()
    assert (tmp_path / "manifest" / "sample_lists.json").is_file()


def test_static_client_rejects_malformed_list_items():
    from fetch_manifest import _validated_mapping_list

    with pytest.raises(ValueError, match="molecular profiles item 1 must be a JSON object"):
        _validated_mapping_list([{"id": "ok"}, "bad"], label="molecular profiles")
