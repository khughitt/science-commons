# HGNC gene crosswalk build

1. Pin the current dated quarterly handles in `sources.yaml`. Discover them at
   https://www.genenames.org/download/archive/ (the `quarterly/tsv/` directory).
   Use a dated file (`hgnc_complete_set_<date>.txt`, `withdrawn_<date>.txt`),
   never the `latest`/`current` alias (C-D3).
2. Build: `uv run --with httpx --with pyyaml python recipe/build.py` (writes `../crosswalk.csv`).
3. Pin the artifact hash + size into `datapackage.yaml`:
   `python - <<'PY'\nimport hashlib,os;p="crosswalk.csv";print("sha256:"+hashlib.sha256(open(p,'rb').read()).hexdigest(),os.path.getsize(p))\nPY`
4. Update `entity.md` `gene_count` to the row count.

The member key is an opaque composite `"<taxon>|hgnc|<hgnc_id>"`. Within-cell
multi-values use `;` (never `|`, which is the gene_key field delimiter).
