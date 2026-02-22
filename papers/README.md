# Papers Workspace

This repository can host multiple manuscripts under `papers/`.

## Layout

- `papers/<paper-slug>/`: one self-contained manuscript project (own `main.tex`, `refs.bib`, `figures/`, `sections/`)
- `papers/shared/`: reusable assets and helper scripts across manuscripts

## Conventions

1. Each paper directory should compile independently.
2. Keep manuscript-specific figures in that paper's `figures/` directory.
3. Use `papers/shared/` only for stable reusable content (macros, common bib entries, scripts).
4. For Elsevier Editorial Manager submission, generate a flattened package per paper (no subfolders).

## Current Papers

- `sdee-k0-anisotropy/`: SDEE submission draft on anisotropic consolidation and liquefaction resistance

