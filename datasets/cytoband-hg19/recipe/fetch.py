from __future__ import annotations

import argparse
import gzip
import hashlib
import os
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import yaml

DATASET_NAME = "cytoband-hg19"
RESOURCE_NAME = "cytoBand"
DEFAULT_URL = "https://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/cytoBand.txt.gz"
SOURCE_RESOURCE_PATH = Path("sources/cytoBand.txt.gz")
LOCKFILE_PATH = Path(__file__).with_name("lockfile.yaml")
REJECTED_URL_PARTS = ("latest", "current", "download/test")


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


def load_lockfile(path: Path) -> dict[str, Any]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("resources"), dict):
        raise ValueError(f"{path}: expected lockfile with resources mapping")
    entry = raw["resources"].get(RESOURCE_NAME)
    if not isinstance(entry, dict):
        raise ValueError(f"{path}: missing {RESOURCE_NAME} resource")
    for key in ("url", "sha256", "bytes", "path"):
        if key not in entry:
            raise ValueError(f"{path}: {RESOURCE_NAME} missing {key}")
    validate_explicit_url(str(entry["url"]))
    return raw


def fetch_source(
    *,
    url: str,
    output_dir: Path,
    lockfile_path: Path = LOCKFILE_PATH,
    refresh_lockfile: bool = False,
) -> dict[str, Any]:
    normalized_url = validate_explicit_url(url)
    existing_lock = load_lockfile(lockfile_path) if lockfile_path.exists() else None
    if existing_lock is None and not refresh_lockfile:
        raise FileNotFoundError(f"missing lockfile: {lockfile_path}; pass --refresh-lockfile to create the pin")

    output_path = output_dir / SOURCE_RESOURCE_PATH
    candidate_path = output_path.with_name(output_path.name + ".candidate")
    try:
        sha256, byte_count = _download(normalized_url, candidate_path)
        decompressed_rows = count_source_rows(candidate_path)
        observed_lock = {
            "resources": {
                RESOURCE_NAME: {
                    "url": normalized_url,
                    "path": SOURCE_RESOURCE_PATH.as_posix(),
                    "sha256": sha256,
                    "bytes": byte_count,
                    "decompressed_rows": decompressed_rows,
                }
            }
        }
        if existing_lock is not None and not refresh_lockfile:
            validate_lock_matches_observed(existing_lock, observed_lock, lockfile_path)
            candidate_path.replace(output_path)
            return existing_lock
        lockfile_path.parent.mkdir(parents=True, exist_ok=True)
        lockfile_path.write_text(yaml.safe_dump(observed_lock, sort_keys=False), encoding="utf-8")
        candidate_path.replace(output_path)
        return observed_lock
    except Exception:
        candidate_path.unlink(missing_ok=True)
        candidate_path.with_suffix(candidate_path.suffix + ".tmp").unlink(missing_ok=True)
        raise


def validate_lock_matches_observed(existing_lock: dict[str, Any], observed_lock: dict[str, Any], lockfile_path: Path) -> None:
    existing = existing_lock["resources"][RESOURCE_NAME]
    observed = observed_lock["resources"][RESOURCE_NAME]
    mismatches = [key for key in ("url", "sha256", "bytes") if str(existing[key]) != str(observed[key])]
    if mismatches:
        mismatch_text = ", ".join(mismatches)
        raise ValueError(
            f"{lockfile_path}: observed download does not match existing pin "
            f"({mismatch_text}); pass --refresh-lockfile to intentionally repin"
        )


def resolve_commons_data_root() -> Path:
    if env := os.environ.get("SCIENCE_COMMONS_DATA_ROOT"):
        return Path(env)
    return Path("/data/science-commons")


def _download(url: str, output_path: Path) -> tuple[str, int]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    digest = hashlib.sha256()
    byte_count = 0
    with urllib.request.urlopen(url) as response, tmp_path.open("wb") as fh:
        for chunk in iter(lambda: response.read(1024 * 1024), b""):
            digest.update(chunk)
            byte_count += len(chunk)
            fh.write(chunk)
    tmp_path.replace(output_path)
    return digest.hexdigest(), byte_count


def count_source_rows(path: Path) -> int:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        return sum(1 for line in handle if line.rstrip("\n"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch pinned UCSC hg19 cytoBand source.")
    parser.add_argument("--url", default=DEFAULT_URL, help="Explicit cytoBand URL to download.")
    parser.add_argument("--output-dir", type=Path, help="Dataset data directory. Defaults under SCIENCE_COMMONS_DATA_ROOT.")
    parser.add_argument("--lockfile", type=Path, default=LOCKFILE_PATH, help="Path to recipe lockfile.")
    parser.add_argument("--refresh-lockfile", action="store_true", help="Rewrite the lockfile with observed URL/hash/bytes.")
    args = parser.parse_args()

    output_dir = args.output_dir or resolve_commons_data_root() / DATASET_NAME
    lock = fetch_source(
        url=args.url,
        output_dir=output_dir,
        lockfile_path=args.lockfile,
        refresh_lockfile=args.refresh_lockfile,
    )
    entry = lock["resources"][RESOURCE_NAME]
    print(f"wrote {entry['path']} ({entry['bytes']} bytes) to {output_dir}")


if __name__ == "__main__":
    main()
