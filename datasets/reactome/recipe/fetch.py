from __future__ import annotations

import argparse
import hashlib
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import yaml
from science_tool.commons.config import resolve_commons_data_root

# science:code
# status: active
# science:end

SOURCE_FILES = (
    "NCBI2Reactome_All_Levels.txt",
    "ReactomePathways.txt",
    "ReactomePathwaysRelation.txt",
)


def normalize_base_url(base_url: str) -> str:
    normalized = base_url.strip()
    if not normalized:
        raise ValueError("--base-url must be non-empty")
    parsed = urllib.parse.urlparse(normalized)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"--base-url must be an absolute http(s) URL, got {base_url!r}")
    if "download/current" in parsed.path:
        raise ValueError("Reactome download/current/ is mutable; use an archived release URL")
    return normalized.rstrip("/") + "/"


def fetch_sources(*, release: str | None, base_url: str | None, output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    lock_path = output_dir / "lockfile.yaml"
    if lock_path.exists():
        lock = _load_lockfile(lock_path)
        if release is not None and str(lock["reactome_release"]) != release:
            raise ValueError(f"lockfile release {lock['reactome_release']!r} does not match --release {release!r}")
        if base_url is not None and normalize_base_url(str(lock["base_url"])) != normalize_base_url(base_url):
            raise ValueError("lockfile base_url does not match --base-url")
        _materialize_locked_files(lock, output_dir)
        return lock

    if release is None or base_url is None:
        raise ValueError("first run requires both --release and --base-url")
    normalized_base_url = normalize_base_url(base_url)
    lock = {
        "reactome_release": release,
        "base_url": normalized_base_url,
        "files": {},
    }
    for filename in SOURCE_FILES:
        url = urllib.parse.urljoin(normalized_base_url, filename)
        sha256, byte_count = _download(url, output_dir / filename)
        lock["files"][filename] = {"url": url, "sha256": sha256, "bytes": byte_count}
    lock_path.write_text(yaml.safe_dump(lock, sort_keys=False), encoding="utf-8")
    return lock


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch pinned Reactome source files.")
    parser.add_argument("--release")
    parser.add_argument("--base-url")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    output_dir = args.output_dir or resolve_commons_data_root() / "reactome" / "_src"
    lock = fetch_sources(release=args.release, base_url=args.base_url, output_dir=output_dir)
    print(f"Reactome release {lock['reactome_release']} sources verified in {output_dir}")


def _load_lockfile(path: Path) -> dict[str, Any]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("files"), dict):
        raise ValueError(f"{path}: expected lockfile with files mapping")
    normalize_base_url(str(raw.get("base_url", "")))
    return raw


def _materialize_locked_files(lock: dict[str, Any], output_dir: Path) -> None:
    files = lock["files"]
    for filename in SOURCE_FILES:
        entry = files.get(filename)
        if not isinstance(entry, dict):
            raise ValueError(f"lockfile missing entry for {filename}")
        path = output_dir / filename
        if not path.exists():
            _download(str(entry["url"]), path)
        sha256, byte_count = _hash_file(path)
        if sha256 != entry.get("sha256") or byte_count != entry.get("bytes"):
            raise ValueError(f"{path}: hash/bytes mismatch against lockfile")


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


def _hash_file(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    byte_count = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
            byte_count += len(chunk)
    return f"sha256:{digest.hexdigest()}", byte_count


if __name__ == "__main__":
    main()
