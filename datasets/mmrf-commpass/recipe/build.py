from __future__ import annotations

import argparse
import csv
import json
import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any
import hashlib

import pandas as pd

from fetch_manifest import discover_endpoint_fields

DEFAULT_SPLIT_SALT = "mmrf-commpass-heldout-patient-v1"
PROGRESSION_EVENT_STATUSES = {"yes", "progression", "recurrence", "true", "1"}
PROGRESSION_CENSORED_STATUSES = {"no", "false", "0"}
UNKNOWN_PROGRESSION_STATUSES = {"", "unknown", "not reported", "not_reported", "not applicable", "not_allowed_to_collect"}
SPLIT_NAMES = ("train", "validation", "test")
REQUIRED_MANIFEST_IDENTITY_FIELDS = (
    "case_id",
    "case_submitter_id",
    "sample_submitter_id",
    "file_id",
    "file_name",
)


def parse_expression_tsv(
    path: str | Path,
    *,
    sample_submitter_id: str,
    case_submitter_id: str,
    measure: str,
) -> list[dict[str, Any]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None:
            raise ValueError(f"Expression TSV {path} is missing a header row")
        required = {"gene_id", "gene_name", measure}
        missing = sorted(required - set(reader.fieldnames))
        if missing:
            raise ValueError(f"Expression TSV {path} is missing required columns: {', '.join(missing)}")

        rows: list[dict[str, Any]] = []
        for row in reader:
            gene_id = str(row.get("gene_id") or "")
            if gene_id.startswith("N_"):
                continue
            rows.append(
                {
                    "case_submitter_id": case_submitter_id,
                    "sample_submitter_id": sample_submitter_id,
                    "gene_id": gene_id,
                    "gene_name": row.get("gene_name"),
                    "measure": measure,
                    "value": float(row[measure]),
                }
            )
    return rows


def validate_no_patient_leakage(splits: pd.DataFrame) -> None:
    assignments = splits.groupby("case_submitter_id")["split"].nunique()
    leaked = sorted(assignments[assignments > 1].index.astype(str))
    if leaked:
        raise ValueError(f"Patient leakage detected across splits: {', '.join(leaked)}")


def validate_nonempty_splits(splits: pd.DataFrame) -> None:
    present = set(splits["split"].dropna().astype(str))
    missing = [split for split in SPLIT_NAMES if split not in present]
    if missing:
        raise ValueError(f"Splits must be nonempty; missing: {', '.join(missing)}")


def resolve_output_dir(output_dir: str | Path | None, env: Mapping[str, str] | None = None) -> Path:
    if output_dir:
        return Path(output_dir)
    environ = env or os.environ
    data_root = environ.get("SCIENCE_COMMONS_DATA_ROOT")
    if data_root:
        return Path(data_root) / "mmrf-commpass"
    raise ValueError("--output-dir is required unless SCIENCE_COMMONS_DATA_ROOT is set")


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _load_cases(path: Path) -> list[Mapping[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"{path} must contain a JSON list of GDC cases")
    cases: list[Mapping[str, Any]] = []
    for case in payload:
        if not isinstance(case, Mapping):
            raise ValueError(f"{path} must contain only JSON objects")
        cases.append(case)
    return cases


def _manifest_cases(cases: list[Mapping[str, Any]], manifest: pd.DataFrame) -> list[Mapping[str, Any]]:
    manifest_case_ids = set(manifest["case_id"].dropna().astype(str))
    indexed = {str(case.get("case_id")): case for case in cases if case.get("case_id")}
    missing = sorted(manifest_case_ids - set(indexed))
    if missing:
        raise ValueError(f"cases.json is missing manifest cases: {', '.join(missing)}")
    return [indexed[case_id] for case_id in sorted(manifest_case_ids)]


def _one_diagnosis(case: Mapping[str, Any]) -> Mapping[str, Any]:
    diagnoses = case.get("diagnoses")
    if not isinstance(diagnoses, list) or len(diagnoses) != 1:
        case_id = case.get("case_id") or case.get("submitter_id") or "<unknown>"
        raise ValueError(f"Case {case_id} must have exactly one diagnosis")
    diagnosis = diagnoses[0]
    if not isinstance(diagnosis, Mapping):
        raise ValueError("Diagnosis must be an object")
    return diagnosis


def _build_outcomes(cases: list[Mapping[str, Any]]) -> list[dict[str, Any]]:
    outcomes: list[dict[str, Any]] = []
    for case in cases:
        diagnosis = _one_diagnosis(case)
        status = str(diagnosis.get("progression_or_recurrence") or "").strip().lower()
        if status in PROGRESSION_EVENT_STATUSES:
            days = diagnosis.get("days_to_recurrence")
            event_observed = True
        elif status in PROGRESSION_CENSORED_STATUSES:
            days = diagnosis.get("days_to_last_follow_up")
            event_observed = False
        elif status in UNKNOWN_PROGRESSION_STATUSES:
            continue
        else:
            continue

        if days is None or days == "":
            continue
        outcomes.append(
            {
                "case_id": case.get("case_id"),
                "case_submitter_id": case.get("submitter_id"),
                "progression_or_recurrence": diagnosis.get("progression_or_recurrence"),
                "time_to_event_days": int(days),
                "event_observed": event_observed,
            }
        )

    if not outcomes:
        raise ValueError("No usable progression outcome rows were found")
    return outcomes


def _validate_manifest_outcome_coverage(samples: pd.DataFrame, outcomes: pd.DataFrame) -> None:
    manifest_case_submitter_ids = set(samples["case_submitter_id"].astype(str))
    outcome_case_submitter_ids = set(outcomes["case_submitter_id"].dropna().astype(str))
    missing = sorted(manifest_case_submitter_ids - outcome_case_submitter_ids)
    if missing:
        raise ValueError(f"Manifest cases lack outcome rows: {', '.join(missing)}")


def _build_splits(case_submitter_ids: list[str], split_salt: str) -> pd.DataFrame:
    if len(case_submitter_ids) != len(set(case_submitter_ids)):
        raise ValueError("case_submitter_id values must be unique before split generation")

    ranked = sorted(
        (
            {
                "case_submitter_id": case_submitter_id,
                "split_basis": hashlib.sha256(f"{case_submitter_id}{split_salt}".encode("utf-8")).hexdigest(),
            }
            for case_submitter_id in case_submitter_ids
        ),
        key=lambda row: row["split_basis"],
    )
    n = len(ranked)
    if n >= 3:
        train_count = max(1, int(n * 0.8))
        validation_count = max(1, int(n * 0.1))
        if train_count + validation_count >= n:
            train_count = n - 2
            validation_count = 1
        boundaries = (train_count, train_count + validation_count)
        for idx, row in enumerate(ranked):
            if idx < boundaries[0]:
                row["split"] = "train"
            elif idx < boundaries[1]:
                row["split"] = "validation"
            else:
                row["split"] = "test"
    else:
        for idx, row in enumerate(ranked):
            row["split"] = SPLIT_NAMES[idx]

    splits = pd.DataFrame(ranked, columns=["case_submitter_id", "split", "split_basis"])
    validate_no_patient_leakage(splits)
    if n >= 3:
        validate_nonempty_splits(splits)
    return splits


def _is_blank_manifest_value(value: Any) -> bool:
    if pd.isna(value):
        return True
    return isinstance(value, str) and not value.strip()


def _samples_from_manifest(manifest: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "case_id",
        "case_submitter_id",
        "sample_submitter_id",
        "sample_type",
        "file_id",
        "file_name",
    ]
    missing = sorted(set(columns) - set(manifest.columns))
    if missing:
        raise ValueError(f"Manifest is missing required sample columns: {', '.join(missing)}")
    invalid_fields = [
        field
        for field in REQUIRED_MANIFEST_IDENTITY_FIELDS
        if any(_is_blank_manifest_value(value) for value in manifest[field].to_list())
    ]
    if invalid_fields:
        raise ValueError(f"Manifest contains blank required identity fields: {', '.join(invalid_fields)}")
    samples = manifest[columns].copy()
    if samples["case_submitter_id"].duplicated().any():
        duplicated = sorted(samples.loc[samples["case_submitter_id"].duplicated(), "case_submitter_id"].astype(str))
        raise ValueError(f"Manifest has duplicate case_submitter_id values: {', '.join(duplicated)}")
    return samples


def build_package(
    output_dir: str | Path,
    *,
    measure: str = "tpm_unstranded",
    split_salt: str = DEFAULT_SPLIT_SALT,
) -> dict[str, Any]:
    out = Path(output_dir)
    manifest_path = out / "manifest" / "files.parquet"
    cases_path = out / "manifest" / "cases.json"
    expression_src_dir = out / "_src" / "expression"
    data_dir = out / "data"
    splits_dir = out / "splits"
    reports_dir = out / "reports"

    manifest = pd.read_parquet(manifest_path)
    samples = _samples_from_manifest(manifest)
    cases = _manifest_cases(_load_cases(cases_path), manifest)
    endpoint_report = discover_endpoint_fields(cases)
    if endpoint_report["status"] != "progression-ready":
        raise ValueError("MMRF-COMMPASS build requires a progression-ready endpoint")

    outcomes = pd.DataFrame(_build_outcomes(cases))
    _validate_manifest_outcome_coverage(samples, outcomes)

    expression_rows: list[dict[str, Any]] = []
    for row in samples.to_dict(orient="records"):
        file_id = str(row["file_id"])
        expression_rows.extend(
            parse_expression_tsv(
                expression_src_dir / f"{file_id}.tsv",
                sample_submitter_id=str(row["sample_submitter_id"]),
                case_submitter_id=str(row["case_submitter_id"]),
                measure=measure,
            )
        )
    if not expression_rows:
        raise ValueError("No expression rows were parsed")

    expression = pd.DataFrame(expression_rows)
    splits = _build_splits(sorted(samples["case_submitter_id"].astype(str)), split_salt)

    data_dir.mkdir(parents=True, exist_ok=True)
    splits_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    expression.to_parquet(data_dir / "expression.parquet", index=False)
    samples.to_parquet(data_dir / "samples.parquet", index=False)
    outcomes.to_parquet(data_dir / "outcomes.parquet", index=False)
    splits.to_parquet(splits_dir / "heldout_patient_v1.parquet", index=False)

    summary = {
        "measure": measure,
        "expression_rows": int(len(expression)),
        "sample_rows": int(len(samples)),
        "outcome_rows": int(len(outcomes)),
        "split_rows": int(len(splits)),
        "split_salt": split_salt,
        "split_method": "sha256(case_submitter_id || split_salt)",
    }
    _write_json(reports_dir / "build-summary.json", summary)
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the MMRF-COMMPASS fixture package.")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--measure", default="tpm_unstranded")
    parser.add_argument("--split-salt", default=DEFAULT_SPLIT_SALT)
    args = parser.parse_args(argv)

    output_dir = resolve_output_dir(args.output_dir)
    summary = build_package(output_dir, measure=args.measure, split_salt=args.split_salt)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
