# Reference Backups

Persisted backups of externally provided material, kept here so it survives across
ephemeral remote sessions and is available for recurring reference and usage.

## Contents

- `_archives/` — exact, byte-for-byte copies of the originally attached archives.
  - `shiftedprimetension-with-claudemd.tar`
    sha256 `9b2009bfe09ab4f08970eb410f0d0d5907c69ba84d0bd6f09689db31816284eb`
  - `shiftedprimetension.tar`
    sha256 `3900e7611c05054a8fb7181179ce31d5875e05be6e6fc029785d61cb6a63cf69`

The **live working copy** of the project now lives at the repository root as
`../shifted-prime-tension/` (with `../CLAUDE.md`), extracted from the
`with-claudemd` archive. This folder keeps only the immutable tar backups.

## Notes

- The two archives contain an **identical** `shifted-prime-tension/` project tree;
  the only difference is that `shiftedprimetension-with-claudemd.tar` additionally
  bundles the top-level `CLAUDE.md`, making it a strict superset.
- The archives' `data/` and `docs/` directories were empty.
- To re-extract from scratch: `tar -xf reference/_archives/<name>.tar -C <dest>`
