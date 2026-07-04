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
