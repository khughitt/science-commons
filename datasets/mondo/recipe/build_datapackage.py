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

RESOURCE_FILES = {
    "graph": "_src/mondo.json",
    "nodes": "nodes.csv",
    "edges": "edges.csv",
    "build_summary": "build-summary.yaml",
}


def build_datapackage_doc(data_dir: Path) -> dict[str, Any]:
    resources: list[dict[str, Any]] = []
    for name, filename in RESOURCE_FILES.items():
        path = data_dir / filename
        sha256, byte_count = stream_sha256_and_bytes(path)
        resources.append(
            {
                "name": name,
                "path": filename,
                "format": "json" if filename.endswith(".json") else ("yaml" if filename.endswith(".yaml") else "csv"),
                "mediatype": _mediatype(filename),
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/mondo/{filename}",
                },
                "hash": sha256,
                "bytes": byte_count,
            }
        )
    return {"name": "mondo", "resources": resources}


def _mediatype(filename: str) -> str:
    if filename.endswith(".json"):
        return "application/json"
    if filename.endswith(".yaml"):
        return "application/yaml"
    return "text/csv"


def render_datapackage_text(doc: dict[str, Any]) -> str:
    return yaml.safe_dump(doc, sort_keys=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render MONDO datapackage.yaml.")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output-path", type=Path)
    args = parser.parse_args()
    data_dir = args.data_dir or resolve_commons_data_root() / "mondo"
    output_path = args.output_path or Path(__file__).parent.parent / "datapackage.yaml"
    output_path.write_text(render_datapackage_text(build_datapackage_doc(data_dir)), encoding="utf-8")
    print(f"wrote {output_path}")


if __name__ == "__main__":
    main()
