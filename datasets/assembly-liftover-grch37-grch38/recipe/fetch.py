from __future__ import annotations

import argparse
import hashlib
import os
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import yaml

# science:code
# status: exploratory
# science:end

DATASET_NAME = "assembly-liftover-grch37-grch38"
DEFAULT_CHAIN_URL = "https://hgdownload.soe.ucsc.edu/goldenPath/hg19/liftOver/hg19ToHg38.over.chain.gz"
CHAIN_RESOURCE_PATH = Path("chains/hg19ToHg38.over.chain.gz")
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


def fetch_chain(*, url: str, output_dir: Path, lockfile_path: Path = LOCKFILE_PATH) -> dict[str, Any]:
    normalized_url = validate_explicit_url(url)
    output_path = output_dir / CHAIN_RESOURCE_PATH
    sha256, byte_count = _download(normalized_url, output_path)
    lock = {
        "resources": {
            "hg19ToHg38_chain": {
                "url": normalized_url,
                "path": CHAIN_RESOURCE_PATH.as_posix(),
                "sha256": sha256,
                "bytes": byte_count,
            }
        }
    }
    lockfile_path.write_text(yaml.safe_dump(lock, sort_keys=False), encoding="utf-8")
    return lock


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch pinned UCSC GRCh37 to GRCh38 liftover chains.")
    parser.add_argument("--url", default=DEFAULT_CHAIN_URL, help="Explicit chain URL to download.")
    parser.add_argument("--output-dir", type=Path, help="Dataset data directory. Defaults under SCIENCE_COMMONS_DATA_ROOT.")
    parser.add_argument("--lockfile", type=Path, default=LOCKFILE_PATH, help="Path to write recipe lockfile.")
    args = parser.parse_args()

    output_dir = args.output_dir or resolve_commons_data_root() / DATASET_NAME
    lock = fetch_chain(url=args.url, output_dir=output_dir, lockfile_path=args.lockfile)
    entry = lock["resources"]["hg19ToHg38_chain"]
    print(f"wrote {entry['path']} ({entry['bytes']} bytes) to {output_dir}")


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


if __name__ == "__main__":
    main()
