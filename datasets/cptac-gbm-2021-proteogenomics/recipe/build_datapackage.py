from __future__ import annotations

import argparse
import hashlib
import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any, NamedTuple

import yaml

OUTPUT_ROOT_TOKEN = "${OUTPUT_ROOT}"
DATASET_NAME = "cptac-gbm-2021-proteogenomics"
STUDY_ID = "gbm_cptac_2021"


class ResourceFile(NamedTuple):
    name: str
    rel_path: str


RESOURCE_FILES = (
    ResourceFile("mrna_fpkm_uq", "expression/mrna_fpkm_uq.parquet"),
    ResourceFile("protein_abundance_log2", "proteomics/protein_abundance_log2.parquet"),
    ResourceFile("samples", "metadata/samples.parquet"),
    ResourceFile("validation", "reports/validation.json"),
    ResourceFile("download_summary", "reports/download-summary.json"),
    ResourceFile("build_summary", "reports/build-summary.json"),
)


def stream_sha256_and_bytes(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    byte_count = 0
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            byte_count += len(chunk)
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()}", byte_count


def build_datapackage_doc(data_dir: str | Path, *, import_date: str) -> dict[str, Any]:
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
                "format": "parquet" if resource.rel_path.endswith(".parquet") else "json",
                "mediatype": "application/vnd.apache.parquet" if resource.rel_path.endswith(".parquet") else "application/json",
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/{DATASET_NAME}/{resource.rel_path}",
                },
            }
        )
    return {
        "name": DATASET_NAME,
        "title": "CPTAC GBM proteogenomics aligned mRNA/protein package",
        "profile": "data-package",
        "licenses": [{"name": "ODbL-1.0"}],
        "cBioPortal": {"study_id": STUDY_ID, "import_date": import_date},
        "provenance": [{"tool": "recipe/fetch_manifest.py"}, {"tool": "recipe/build.py"}],
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render CPTAC GBM datapackage metadata.")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output", type=Path, default=Path("../datapackage.yaml"))
    parser.add_argument("--import-date", required=True)
    args = parser.parse_args(argv)
    data_dir = resolve_data_dir(args.data_dir)
    doc = build_datapackage_doc(data_dir, import_date=args.import_date)
    args.output.write_text(render_datapackage_text(doc), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
