from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from collections.abc import Mapping
from pathlib import Path
from typing import Any
from urllib import request

CBIOPORTAL_API_BASE = "https://www.cbioportal.org/api"
DATAHUB_RAW_BASE = "https://raw.githubusercontent.com/cBioPortal/datahub/master/public/gbm_cptac_2021"
LFS_BATCH_URL = "https://github.com/cBioPortal/datahub.git/info/lfs/objects/batch"
DATASET_NAME = "cptac-gbm-2021-proteogenomics"
STUDY_ID = "gbm_cptac_2021"
DEFAULT_TIMEOUT_SECONDS = 60

MATRIX_FILES = {
    "mrna": "data_mrna_seq_fpkm.txt",
    "protein": "data_protein_quantification.txt",
}
REQUIRED_PROFILES = {
    "mrna": "gbm_cptac_2021_mrna",
    "protein": "gbm_cptac_2021_protein_quantification",
}
REQUIRED_SAMPLE_LISTS = {
    "mrna": "gbm_cptac_2021_rna_seq_mrna",
    "protein": "gbm_cptac_2021_protein_quantification",
}


def resolve_output_dir(output_dir: str | Path | None, env: Mapping[str, str] | None = None) -> Path:
    if output_dir:
        return Path(output_dir)
    environ = env or os.environ
    data_root = environ.get("SCIENCE_COMMONS_DATA_ROOT")
    if data_root:
        return Path(data_root) / DATASET_NAME
    raise ValueError("--output-dir is required unless SCIENCE_COMMONS_DATA_ROOT is set")


def _get_json(url: str, *, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Any:
    with request.urlopen(url, timeout=timeout) as response:
        return json.load(response)


def _post_json(url: str, payload: Mapping[str, Any], *, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Any:
    req = request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Accept": "application/vnd.git-lfs+json",
            "Content-Type": "application/vnd.git-lfs+json",
        },
        method="POST",
    )
    with request.urlopen(req, timeout=timeout) as response:
        return json.load(response)


def _get_text(url: str, *, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> str:
    with request.urlopen(url, timeout=timeout) as response:
        return response.read().decode("utf-8")


class CbioPortalClient:
    def study(self) -> Mapping[str, Any]:
        payload = _get_json(f"{CBIOPORTAL_API_BASE}/studies/{STUDY_ID}")
        if not isinstance(payload, Mapping):
            raise ValueError("Study response must be a JSON object")
        return payload

    def molecular_profiles(self) -> list[Mapping[str, Any]]:
        payload = _get_json(f"{CBIOPORTAL_API_BASE}/studies/{STUDY_ID}/molecular-profiles")
        if not isinstance(payload, list):
            raise ValueError("Molecular profiles response must be a JSON list")
        return _validated_mapping_list(payload, label="molecular profiles")

    def sample_lists(self) -> list[Mapping[str, Any]]:
        payload = _get_json(f"{CBIOPORTAL_API_BASE}/studies/{STUDY_ID}/sample-lists")
        if not isinstance(payload, list):
            raise ValueError("Sample lists response must be a JSON list")
        return _validated_mapping_list(payload, label="sample lists")

    def lfs_pointer(self, label: str) -> str:
        return _get_text(f"{DATAHUB_RAW_BASE}/{MATRIX_FILES[label]}")

    def lfs_batch(self, objects: list[Mapping[str, Any]]) -> Mapping[str, Any]:
        payload = build_lfs_batch_payload(objects)
        response = _post_json(LFS_BATCH_URL, payload)
        if not isinstance(response, Mapping):
            raise ValueError("LFS batch response must be a JSON object")
        return response


class StaticCbioPortalClient:
    def __init__(
        self,
        *,
        study: Mapping[str, Any],
        molecular_profiles: list[Mapping[str, Any]],
        sample_lists: list[Mapping[str, Any]],
        pointers: Mapping[str, str],
        batch_response: Mapping[str, Any] | None = None,
    ) -> None:
        self._study = study
        self._molecular_profiles = molecular_profiles
        self._sample_lists = sample_lists
        self._pointers = pointers
        self._batch_response = batch_response or {"objects": []}

    def study(self) -> Mapping[str, Any]:
        return self._study

    def molecular_profiles(self) -> list[Mapping[str, Any]]:
        return self._molecular_profiles

    def sample_lists(self) -> list[Mapping[str, Any]]:
        return self._sample_lists

    def lfs_pointer(self, label: str) -> str:
        return self._pointers[label]

    def lfs_batch(self, objects: list[Mapping[str, Any]]) -> Mapping[str, Any]:
        return self._batch_response


def _validated_mapping_list(items: list[Any], *, label: str) -> list[Mapping[str, Any]]:
    mappings: list[Mapping[str, Any]] = []
    for index, item in enumerate(items):
        if not isinstance(item, Mapping):
            raise ValueError(f"{label} item {index} must be a JSON object")
        mappings.append(item)
    return mappings


def parse_lfs_pointer(text: str, *, label: str) -> dict[str, Any]:
    if not text.startswith("version https://git-lfs.github.com/spec/v1"):
        raise ValueError(f"{label} is not a git LFS pointer")
    oid_match = re.search(r"^oid sha256:([0-9a-f]{64})$", text, flags=re.MULTILINE)
    size_match = re.search(r"^size ([0-9]+)$", text, flags=re.MULTILINE)
    if not oid_match or not size_match:
        raise ValueError(f"{label} LFS pointer is missing oid or size")
    return {"label": label, "oid": oid_match.group(1), "size": int(size_match.group(1))}


def build_lfs_batch_payload(objects: list[Mapping[str, Any]]) -> dict[str, Any]:
    return {
        "operation": "download",
        "transfers": ["basic"],
        "objects": [{"oid": str(obj["oid"]), "size": int(obj["size"])} for obj in objects],
    }


def download_urls_from_batch_response(payload: Mapping[str, Any]) -> dict[str, str]:
    objects = payload.get("objects")
    if not isinstance(objects, list):
        raise ValueError("LFS batch response is missing objects")
    urls: dict[str, str] = {}
    for obj in objects:
        if not isinstance(obj, Mapping):
            raise ValueError("LFS batch object must be a JSON object")
        oid = str(obj.get("oid") or "")
        href = (((obj.get("actions") or {}).get("download") or {}).get("href"))
        if not re.fullmatch(r"[0-9a-f]{64}", oid) or not href:
            raise ValueError(f"LFS batch object {oid or '<missing>'} is missing a download action")
        urls[oid] = str(href)
    return urls


def verify_downloaded_payload(path: str | Path, *, expected_oid: str, expected_size: int) -> dict[str, Any]:
    target = Path(path)
    data = target.read_bytes()
    byte_count = len(data)
    digest = hashlib.sha256(data).hexdigest()
    if byte_count != expected_size:
        raise ValueError(f"{target} byte count mismatch: expected {expected_size}, found {byte_count}")
    if digest != expected_oid:
        raise ValueError(f"{target} SHA-256 mismatch: expected {expected_oid}, found {digest}")
    is_pointer = data.startswith(b"version https://git-lfs.github.com/spec/v1")
    if is_pointer:
        raise ValueError(f"{target} is still a git LFS pointer")
    return {"path": str(target), "bytes": byte_count, "sha256": digest, "is_lfs_pointer": False}


def _profile_ids(profiles: list[Mapping[str, Any]]) -> set[str]:
    return {str(profile.get("molecularProfileId")) for profile in profiles}


def _sample_list_ids(sample_lists: list[Mapping[str, Any]]) -> set[str]:
    return {str(sample_list.get("sampleListId")) for sample_list in sample_lists}


def _validate_source_surface(
    study: Mapping[str, Any],
    profiles: list[Mapping[str, Any]],
    sample_lists: list[Mapping[str, Any]],
) -> None:
    if study.get("studyId") != STUDY_ID:
        raise ValueError(f"Unexpected study id: {study.get('studyId')}")
    if study.get("publicStudy") is not True:
        raise ValueError(f"{STUDY_ID} is not public")
    missing_profiles = sorted(set(REQUIRED_PROFILES.values()) - _profile_ids(profiles))
    if missing_profiles:
        raise ValueError(f"Missing required molecular profiles: {', '.join(missing_profiles)}")
    missing_sample_lists = sorted(set(REQUIRED_SAMPLE_LISTS.values()) - _sample_list_ids(sample_lists))
    if missing_sample_lists:
        raise ValueError(f"Missing required sample lists: {', '.join(missing_sample_lists)}")


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_dry_run(output_dir: str | Path, *, client: CbioPortalClient | StaticCbioPortalClient | None = None) -> dict[str, Any]:
    out = Path(output_dir)
    active_client = client or CbioPortalClient()
    study = active_client.study()
    profiles = active_client.molecular_profiles()
    sample_lists = active_client.sample_lists()
    _validate_source_surface(study, profiles, sample_lists)
    objects = [parse_lfs_pointer(active_client.lfs_pointer(label), label=label) for label in ("mrna", "protein")]

    _write_json(out / "manifest" / "study.json", study)
    _write_json(out / "manifest" / "molecular_profiles.json", profiles)
    _write_json(out / "manifest" / "sample_lists.json", sample_lists)
    validation = {
        "study_id": STUDY_ID,
        "import_date": study.get("importDate"),
        "sample_counts": {
            "all": study.get("allSampleCount"),
            "mrna": study.get("mrnaRnaSeqSampleCount"),
            "mass_spectrometry": study.get("massSpectrometrySampleCount"),
        },
        "profiles": REQUIRED_PROFILES,
        "sample_lists": REQUIRED_SAMPLE_LISTS,
        "lfs_objects": {str(obj["label"]): {"oid": obj["oid"], "size": obj["size"]} for obj in objects},
        "promotable": True,
    }
    _write_json(out / "reports" / "validation.json", validation)
    return validation


def download_lfs_payloads(
    output_dir: str | Path,
    *,
    client: CbioPortalClient | StaticCbioPortalClient | None = None,
) -> dict[str, Any]:
    out = Path(output_dir)
    active_client = client or CbioPortalClient()
    validation_path = out / "reports" / "validation.json"
    if not validation_path.is_file():
        write_dry_run(out, client=active_client)
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    objects = [
        {"label": label, "oid": spec["oid"], "size": spec["size"]}
        for label, spec in validation["lfs_objects"].items()
    ]
    urls = download_urls_from_batch_response(active_client.lfs_batch(objects))
    raw_dir = out / "_src" / "datahub"
    raw_dir.mkdir(parents=True, exist_ok=True)
    reports: dict[str, Any] = {}
    for obj in objects:
        label = str(obj["label"])
        target = raw_dir / MATRIX_FILES[label]
        with request.urlopen(urls[str(obj["oid"])], timeout=DEFAULT_TIMEOUT_SECONDS) as response:
            target.write_bytes(response.read())
        reports[label] = verify_downloaded_payload(
            target,
            expected_oid=str(obj["oid"]),
            expected_size=int(obj["size"]),
        )
    _write_json(out / "reports" / "download-summary.json", reports)
    return reports


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch CPTAC GBM cBioPortal/DataHub metadata and payloads.")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args(argv)
    output_dir = resolve_output_dir(args.output_dir)
    if args.dry_run and args.download:
        parser.error("--dry-run is not allowed with --download")
    if args.download:
        report = download_lfs_payloads(output_dir)
    else:
        report = write_dry_run(output_dir)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
