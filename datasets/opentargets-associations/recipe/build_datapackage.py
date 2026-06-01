from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from science_tool.commons.config import resolve_commons_data_root
from science_tool.commons.datapackage import OUTPUT_ROOT_TOKEN, stream_sha256_and_bytes

# science:code
# status: exploratory
# science:end

# Omit branch (design §8): only graph.jsonl / nodes.csv / build-summary.yaml. No edges.csv.
RESOURCE_FILES = {
    "graph": "graph.jsonl",
    "nodes": "nodes.csv",
    "build_summary": "build-summary.yaml",
}


def _format(filename: str) -> str:
    if filename.endswith(".jsonl"):
        return "ndjson"
    if filename.endswith(".yaml"):
        return "yaml"
    return "csv"


def _mediatype(filename: str) -> str:
    if filename.endswith(".jsonl"):
        return "application/x-ndjson"
    if filename.endswith(".yaml"):
        return "application/yaml"
    return "text/csv"


def build_datapackage_doc(data_dir: Path) -> dict[str, Any]:
    resources: list[dict[str, Any]] = []
    for name, filename in RESOURCE_FILES.items():
        path = data_dir / filename
        sha256, byte_count = stream_sha256_and_bytes(path)
        resources.append(
            {
                "name": name,
                "path": filename,
                "format": _format(filename),
                "mediatype": _mediatype(filename),
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/opentargets-associations/{filename}",
                },
                "hash": sha256,
                "bytes": byte_count,
            }
        )
    return {"name": "opentargets-associations", "resources": resources}


def render_datapackage_text(doc: dict[str, Any]) -> str:
    return yaml.safe_dump(doc, sort_keys=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render Open Targets datapackage.yaml.")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output-path", type=Path)
    args = parser.parse_args()
    data_dir = args.data_dir or resolve_commons_data_root() / "opentargets-associations"
    output_path = args.output_path or Path(__file__).parent.parent / "datapackage.yaml"
    output_path.write_text(render_datapackage_text(build_datapackage_doc(data_dir)), encoding="utf-8")
    print(f"wrote {output_path}")


if __name__ == "__main__":
    main()
