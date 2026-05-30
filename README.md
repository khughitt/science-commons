# Science Commons

This directory is a shared knowledge store for the Science framework. It holds
curated, citable entities — datasets, papers, topics, themes — consumed across
projects via the `science commons` CLI.

Files are the source of truth. `registry.sqlite` is a regenerable index built
by `science commons index rebuild` and is gitignored. `.migrations/` is the
audit log written by `science promote` (Phase E and later); each successful
promotion commits one log file there.

See [science/docs/plans/2026-05-13-multiproject-schema-and-shared-store-design.md](https://github.com/khughitt/science/blob/main/docs/plans/2026-05-13-multiproject-schema-and-shared-store-design.md) 
for the design.
