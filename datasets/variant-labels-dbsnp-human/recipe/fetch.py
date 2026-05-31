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

DATASET_NAME = "variant-labels-dbsnp-human"
LOCKFILE_PATH = Path(__file__).with_name("lockfile.yaml")
DEFAULT_ARCHIVE_URLS = (
    "https://ftp.ncbi.nih.gov/snp/archive/b157/VCF/GCF_000001405.40.gz",
    "https://ftp.ncbi.nih.gov/snp/archive/b157/VCF/GCF_000001405.25.gz",
)


def fetch_sources(
    *,
    urls: tuple[str, ...] = DEFAULT_ARCHIVE_URLS,
    output_dir: Path,
    lockfile_path: Path = LOCKFILE_PATH,
    refresh_lockfile: bool = False,
) -> dict[str, Any]:
    if lockfile_path.exists() and not refresh_lockfile:
        lock = load_lockfile(lockfile_path)
        _materialize_locked_files(lock, output_dir)
        return lock
    if not refresh_lockfile:
        raise FileNotFoundError(f"missing lockfile: {lockfile_path}; pass --refresh-lockfile to create the pin")

    output_dir.mkdir(parents=True, exist_ok=True)
    lock = {"resources": {}}
    for url in urls:
        normalized_url = validate_archive_url(url)
        filename = Path(urllib.parse.urlparse(normalized_url).path).name
        if not filename.endswith(".gz"):
            raise ValueError(f"dbSNP source URL must end with .gz: {url}")
        gz_path = output_dir / filename
        sha256, byte_count = _download(normalized_url, gz_path)

        md5_url = normalized_url + ".md5"
        md5_path = output_dir / f"{filename}.md5"
        _download(md5_url, md5_path)
        md5 = _parse_md5_sidecar(md5_path)
        if md5:
            actual_md5 = _hash_file(gz_path, "md5")[0].removeprefix("md5:")
            if actual_md5 != md5:
                raise ValueError(f"{gz_path}: md5 mismatch against {md5_path}")

        lock["resources"][filename] = {
            "url": normalized_url,
            "path": filename,
            "md5_url": md5_url,
            "md5_path": f"{filename}.md5",
            "md5": md5,
            "sha256": sha256,
            "bytes": byte_count,
        }

    lockfile_path.parent.mkdir(parents=True, exist_ok=True)
    lockfile_path.write_text(yaml.safe_dump(lock, sort_keys=False), encoding="utf-8")
    return lock


def validate_archive_url(url: str) -> str:
    normalized = url.strip()
    if not normalized:
        raise ValueError("URL must be non-empty")
    parsed = urllib.parse.urlparse(normalized)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"URL must be an absolute http(s) URL, got {url!r}")
    if "/latest_release/" in normalized.lower():
        raise ValueError(f"dbSNP latest_release URLs are mutable: {url}")
    return normalized


def load_lockfile(path: Path) -> dict[str, Any]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("resources"), dict):
        raise ValueError(f"{path}: expected lockfile with resources mapping")
    for name, entry in raw["resources"].items():
        if not isinstance(entry, dict):
            raise ValueError(f"{path}: resource {name!r} must be a mapping")
        for key in ("url", "path", "sha256", "bytes"):
            if key not in entry:
                raise ValueError(f"{path}: resource {name!r} missing {key}")
        validate_archive_url(str(entry["url"]))
    return raw


def _materialize_locked_files(lock: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, entry in lock["resources"].items():
        gz_path = output_dir / str(entry["path"])
        if not gz_path.exists():
            _download(str(entry["url"]), gz_path)
        sha256, byte_count = _hash_file(gz_path, "sha256")
        if sha256 != str(entry["sha256"]) or byte_count != int(entry["bytes"]):
            raise ValueError(f"{gz_path}: hash/bytes mismatch against lockfile")

        md5_path_value = entry.get("md5_path")
        md5_url_value = entry.get("md5_url")
        if md5_path_value and md5_url_value:
            md5_path = output_dir / str(md5_path_value)
            if not md5_path.exists():
                _download(str(md5_url_value), md5_path)
            expected_md5 = str(entry.get("md5") or "")
            if expected_md5:
                actual_md5 = _hash_file(gz_path, "md5")[0].removeprefix("md5:")
                if actual_md5 != expected_md5:
                    raise ValueError(f"{gz_path}: md5 mismatch against lockfile resource {name!r}")


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
    return f"sha256:{digest.hexdigest()}", byte_count


def _hash_file(path: Path, algorithm: str) -> tuple[str, int]:
    digest = hashlib.new(algorithm)
    byte_count = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
            byte_count += len(chunk)
    return f"{algorithm}:{digest.hexdigest()}", byte_count


def _parse_md5_sidecar(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return ""
    return text.split()[0].lower()


def resolve_commons_data_root() -> Path:
    if env := os.environ.get("SCIENCE_COMMONS_DATA_ROOT"):
        return Path(env)
    return Path("/data/science-commons")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch pinned dbSNP b157 human VCF archives.")
    parser.add_argument(
        "--url",
        action="append",
        dest="urls",
        help="Explicit dbSNP archive URL. May be passed twice; defaults to GRCh38 and GRCh37 b157 archives.",
    )
    parser.add_argument("--output-dir", type=Path, help="Source directory. Defaults under SCIENCE_COMMONS_DATA_ROOT.")
    parser.add_argument("--lockfile", type=Path, default=LOCKFILE_PATH, help="Path to recipe lockfile.")
    parser.add_argument(
        "--refresh-lockfile",
        action="store_true",
        help="Download sources and rewrite lockfile.yaml with observed hashes.",
    )
    args = parser.parse_args()

    urls = tuple(args.urls) if args.urls else DEFAULT_ARCHIVE_URLS
    output_dir = args.output_dir or resolve_commons_data_root() / DATASET_NAME / "_src"
    lock = fetch_sources(
        urls=urls,
        output_dir=output_dir,
        lockfile_path=args.lockfile,
        refresh_lockfile=args.refresh_lockfile,
    )
    print(f"verified {len(lock['resources'])} dbSNP source archives in {output_dir}")


if __name__ == "__main__":
    main()
