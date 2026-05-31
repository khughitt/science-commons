# Human dbSNP rsID Variant Labels

This recipe builds `dataset:variant-labels-dbsnp-human`, the C4c rsID input resolver artifact.

Use archived NCBI dbSNP URLs only:

- `https://ftp.ncbi.nih.gov/snp/archive/b157/VCF/GCF_000001405.40.gz`
- `https://ftp.ncbi.nih.gov/snp/archive/b157/VCF/GCF_000001405.25.gz`

Do not use `https://ftp.ncbi.nih.gov/snp/latest_release/VCF/`; that path is mutable.

The built SQLite file is large and belongs under `$SCIENCE_COMMONS_DATA_ROOT/variant-labels-dbsnp-human/`.
The commons repository stores the recipe, lockfile, entity, and datapackage hashes, not the bulk SQLite
or VCF bytes.
