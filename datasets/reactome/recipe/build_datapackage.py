from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from science_tool.commons.config import resolve_commons_data_root
from science_tool.commons.datapackage import OUTPUT_ROOT_TOKEN, stream_sha256_and_bytes

# science:code
# status: exploratory
# science:end

RESOURCE_FILES = {
    "sets": "sets.csv",
    "ncbi_gene_pathway": "ncbi_gene_pathway.csv",
    "pathways": "pathways.csv",
    "pathway_relations": "pathway_relations.csv",
    "gene_set_panel": "gene_set_panel.csv",
    "resolution_report": "resolution_report.csv",
}


def build_datapackage_doc(data_dir: Path) -> dict[str, Any]:
    resources: list[dict[str, Any]] = []
    for name, filename in RESOURCE_FILES.items():
        sha256, byte_count = stream_sha256_and_bytes(data_dir / filename)
        resources.append(
            {
                "name": name,
                "path": filename,
                "format": "csv",
                "mediatype": "text/csv",
                "hash": sha256,
                "bytes": byte_count,
                "source": {
                    "type": "local",
                    "ref": f"{OUTPUT_ROOT_TOKEN}/reactome/{filename}",
                },
            }
        )
    return {"name": "reactome", "resources": resources}


def render_datapackage_text(doc: dict[str, Any]) -> str:
    return json.dumps(doc, indent=2, sort_keys=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the Reactome datapackage.yaml sidecar.")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output-path", type=Path)
    args = parser.parse_args()

    data_dir = args.data_dir or resolve_commons_data_root() / "reactome"
    output_path = args.output_path or Path(__file__).with_name("datapackage.yaml")
    doc = build_datapackage_doc(data_dir)
    output_path.write_text(render_datapackage_text(doc), encoding="utf-8")
    print(f"wrote {output_path}")


if __name__ == "__main__":
    main()
