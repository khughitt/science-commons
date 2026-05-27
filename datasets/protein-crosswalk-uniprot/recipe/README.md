# UniProt protein crosswalk build

1. Pin the current dated UniProt release handles in `sources.yaml`. Discover them
   at https://www.uniprot.org/help/downloads (knowledgebase `release-<N_M>`).
   Use a dated `previous_releases/release-<N_M>/...` path, never the
   `current_release` alias (C-D3). v1 scope = reviewed Swiss-Prot, human (9606):
   the idmapping handle must be the reviewed-human idmapping (or filter the
   per-organism idmapping to the reviewed accession set before building).
2. Build: `uv run --with httpx --with pyyaml python recipe/build.py` (writes `../crosswalk.csv`).
   `fetch_text` transparently gunzips a `.gz` handle, so the dated `.gz` files can
   be pinned directly in `sources.yaml`.
3. Pin the artifact hash + size into `datapackage.yaml`:
   `python - <<'PY'\nimport hashlib,os;p="crosswalk.csv";print("sha256:"+hashlib.sha256(open(p,'rb').read()).hexdigest(),os.path.getsize(p))\nPY`
4. Update `entity.md` `protein_count` to the row count.

The member key is an opaque composite `"<taxon>|uniprot|<accession>"`. Within-cell
multi-values use `;`. Each row carries the C2 `gene_key` (from the HGNC xref).
