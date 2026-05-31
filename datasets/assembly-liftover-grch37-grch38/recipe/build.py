from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import urllib.parse
from pathlib import Path
from typing import Any

import yaml

# science:code
# status: exploratory
# science:end

DATASET_NAME = "assembly-liftover-grch37-grch38"
OUTPUT_ROOT_TOKEN = "${OUTPUT_ROOT}"
CHAIN_RESOURCE_NAME = "hg19ToHg38_chain"
CHAIN_RESOURCE_PATH = Path("chains/hg19ToHg38.over.chain.gz")
COMPATIBILITY_RESOURCE_PATH = Path("compatibility_relations.csv")
LOCKFILE_PATH = Path(__file__).with_name("lockfile.yaml")
DATAPACKAGE_PATH = Path(__file__).parents[1] / "datapackage.yaml"
REJECTED_URL_PARTS = ("latest", "current", "download/test")
FIELDNAMES = [
    "source_seqcol_digest",
    "target_seqcol_digest",
    "relation",
    "method",
    "chain_resource",
    "direction",
    "source_label",
    "target_label",
    "source_url",
    "chain_sha256",
]
SEQCOL_DIGEST_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")


def build_dataset(
    *,
    source_seqcol: str,
    target_seqcol: str,
    data_dir: Path,
    lockfile_path: Path = LOCKFILE_PATH,
    datapackage_path: Path = DATAPACKAGE_PATH,
) -> None:
    source_seqcol = validate_seqcol_digest(source_seqcol, "--source-seqcol")
    target_seqcol = validate_seqcol_digest(target_seqcol, "--target-seqcol")
    if source_seqcol == target_seqcol:
        raise ValueError("--source-seqcol and --target-seqcol must differ")

    lock = load_lockfile(lockfile_path)
    chain_entry = lock["resources"][CHAIN_RESOURCE_NAME]
    source_url = validate_explicit_url(str(chain_entry["url"]))
    chain_sha256 = str(chain_entry["sha256"])
    chain_path = data_dir / CHAIN_RESOURCE_PATH
    if not chain_path.is_file():
        raise FileNotFoundError(f"required chain file is absent: {chain_path}")

    actual_chain_sha256, actual_chain_bytes = stream_sha256_and_bytes(chain_path)
    if actual_chain_sha256.removeprefix("sha256:") != chain_sha256:
        raise ValueError(f"{chain_path}: sha256 mismatch against lockfile")
    if actual_chain_bytes != int(chain_entry["bytes"]):
        raise ValueError(f"{chain_path}: byte count mismatch against lockfile")

    compatibility_path = data_dir / COMPATIBILITY_RESOURCE_PATH
    write_compatibility_relations(
        compatibility_path,
        {
            "source_seqcol_digest": source_seqcol,
            "target_seqcol_digest": target_seqcol,
            "relation": "liftover_possible",
            "method": "ucsc_chain",
            "chain_resource": CHAIN_RESOURCE_PATH.as_posix(),
            "direction": "forward",
            "source_label": "GRCh37",
            "target_label": "GRCh38",
            "source_url": source_url,
            "chain_sha256": f"sha256:{chain_sha256}",
        },
    )
    compatibility_sha256, compatibility_bytes = stream_sha256_and_bytes(compatibility_path)
    write_datapackage(
        datapackage_path,
        compatibility_hash=compatibility_sha256,
        compatibility_bytes=compatibility_bytes,
        chain_hash=actual_chain_sha256,
        chain_bytes=actual_chain_bytes,
    )


def load_lockfile(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"missing lockfile: {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("resources"), dict):
        raise ValueError(f"{path}: expected lockfile with resources mapping")
    entry = raw["resources"].get(CHAIN_RESOURCE_NAME)
    if not isinstance(entry, dict):
        raise ValueError(f"{path}: missing {CHAIN_RESOURCE_NAME} resource")
    for key in ("url", "sha256", "bytes"):
        if key not in entry:
            raise ValueError(f"{path}: {CHAIN_RESOURCE_NAME} missing {key}")
    validate_explicit_url(str(entry["url"]))
    return raw


def validate_explicit_url(url: str) -> str:
    normalized = url.strip()
    if not normalized:
        raise ValueError("URL must be non-empty")
    parsed = urllib.parse.urlparse(normalized)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"URL must be an absolute http(s) URL, got {url!r}")
    lowered = normalized.lower()
    for rejected in REJECTED_URL_PARTS:
        if rejected in lowered:
            raise ValueError(f"URL contains mutable or disallowed segment {rejected!r}: {url}")
    return normalized


def validate_seqcol_digest(value: str, label: str) -> str:
    stripped = value.strip()
    if not stripped:
        raise ValueError(f"{label} must be non-empty")
    if value != stripped:
        raise ValueError(f"{label} must not contain leading or trailing whitespace")
    if not SEQCOL_DIGEST_PATTERN.fullmatch(value):
        raise ValueError(f"{label} must match [A-Za-z0-9_-]+")
    return value


def write_compatibility_relations(path: Path, row: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES, extrasaction="raise")
        writer.writeheader()
        writer.writerow(row)


def write_datapackage(
    path: Path,
    *,
    compatibility_hash: str,
    compatibility_bytes: int,
    chain_hash: str,
    chain_bytes: int,
) -> None:
    doc = {
        "name": DATASET_NAME,
        "profile": "data-package",
        "resources": [
            {
                "name": "compatibility_relations",
                "path": COMPATIBILITY_RESOURCE_PATH.as_posix(),
                "format": "csv",
                "mediatype": "text/csv",
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/{DATASET_NAME}/{COMPATIBILITY_RESOURCE_PATH.as_posix()}",
                },
                "hash": compatibility_hash,
                "bytes": compatibility_bytes,
            },
            {
                "name": CHAIN_RESOURCE_NAME,
                "path": CHAIN_RESOURCE_PATH.as_posix(),
                "format": "chain.gz",
                "mediatype": "application/gzip",
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/{DATASET_NAME}/{CHAIN_RESOURCE_PATH.as_posix()}",
                },
                "hash": chain_hash,
                "bytes": chain_bytes,
            },
        ],
    }
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")


def stream_sha256_and_bytes(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    byte_count = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
            byte_count += len(chunk)
    return f"sha256:{digest.hexdigest()}", byte_count


def resolve_commons_data_root() -> Path:
    if env := os.environ.get("SCIENCE_COMMONS_DATA_ROOT"):
        return Path(env)
    return Path("/data/science-commons")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build GRCh37 to GRCh38 liftover compatibility resources.")
    parser.add_argument("--source-seqcol", required=True, help="GRCh37 seqcol digest.")
    parser.add_argument("--target-seqcol", required=True, help="GRCh38 seqcol digest.")
    parser.add_argument("--data-dir", type=Path, help="Dataset data directory. Defaults under SCIENCE_COMMONS_DATA_ROOT.")
    parser.add_argument("--lockfile", type=Path, default=LOCKFILE_PATH, help="Path to recipe lockfile.")
    parser.add_argument("--datapackage", type=Path, default=DATAPACKAGE_PATH, help="Path to rewrite datapackage.yaml.")
    args = parser.parse_args()

    data_dir = args.data_dir or resolve_commons_data_root() / DATASET_NAME
    build_dataset(
        source_seqcol=args.source_seqcol,
        target_seqcol=args.target_seqcol,
        data_dir=data_dir,
        lockfile_path=args.lockfile,
        datapackage_path=args.datapackage,
    )
    print(f"wrote liftover compatibility resources to {data_dir}")


if __name__ == "__main__":
    main()
