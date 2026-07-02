from __future__ import annotations

import argparse
import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any, NamedTuple

import yaml

from science_tool.commons.datapackage import OUTPUT_ROOT_TOKEN, stream_sha256_and_bytes

DATASET_NAME = "mmrf-commpass"
SPLIT_METHOD = "sha256(case_submitter_id || split_salt)"


class ResourceFile(NamedTuple):
    name: str
    rel_path: str


RESOURCE_FILES = (
    ResourceFile("files_manifest", "manifest/files.parquet"),
    ResourceFile("query", "manifest/query.json"),
    ResourceFile("cases", "manifest/cases.json"),
    ResourceFile("expression", "data/expression.parquet"),
    ResourceFile("samples", "data/samples.parquet"),
    ResourceFile("outcomes", "data/outcomes.parquet"),
    ResourceFile("heldout_patient_split", "splits/heldout_patient_v1.parquet"),
    ResourceFile("validation", "reports/validation.json"),
    ResourceFile("build_summary", "reports/build-summary.json"),
)


def build_datapackage_doc(
    data_dir: str | Path,
    *,
    split_salt: str,
    gdc_data_release: str,
) -> dict[str, Any]:
    root = Path(data_dir)
    resources: list[dict[str, Any]] = []
    for resource in RESOURCE_FILES:
        path = root / resource.rel_path
        digest, byte_count = stream_sha256_and_bytes(path)
        resources.append(
            {
                "name": resource.name,
                "path": resource.rel_path,
                "hash": digest,
                "bytes": byte_count,
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/{DATASET_NAME}/{resource.rel_path}",
                },
            }
        )

    return {
        "name": DATASET_NAME,
        "profile": "data-package",
        "gdc_data_release": gdc_data_release,
        "split": {
            "method": SPLIT_METHOD,
            "split_salt": split_salt,
        },
        "provenance": [{"tool": "recipe/build.py"}],
        "resources": resources,
    }


def render_datapackage_text(doc: Mapping[str, Any]) -> str:
    return yaml.safe_dump(dict(doc), sort_keys=False, allow_unicode=False)


def resolve_data_dir(data_dir: str | Path | None, env: Mapping[str, str] | None = None) -> Path:
    if data_dir:
        return Path(data_dir)
    environ = env or os.environ
    data_root = environ.get("SCIENCE_COMMONS_DATA_ROOT")
    if data_root:
        return Path(data_root) / DATASET_NAME
    raise ValueError("--data-dir is required unless SCIENCE_COMMONS_DATA_ROOT is set")


def default_output_path(data_dir: Path) -> Path:
    return data_dir / "datapackage.yaml"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render the MMRF-COMMPASS datapackage.yaml metadata.")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--split-salt", required=True)
    parser.add_argument("--gdc-data-release", required=True)
    args = parser.parse_args(argv)

    data_dir = resolve_data_dir(args.data_dir)
    output_path = args.output or default_output_path(data_dir)
    doc = build_datapackage_doc(
        data_dir,
        split_salt=args.split_salt,
        gdc_data_release=args.gdc_data_release,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_datapackage_text(doc), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
