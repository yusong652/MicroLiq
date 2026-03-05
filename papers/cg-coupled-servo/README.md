# Paper LaTeX Skeleton (Elsevier / Computers and Geotechnics)

This directory is a local authoring skeleton for preparing a manuscript for **Computers and Geotechnics** (Elsevier) using LaTeX.

## Structure

- `main.tex`: manuscript entry point (`elsarticle` style)
- `sections/`: section files split for easier editing
- `figures/`: final submission figures (prefer vector PDF for plots)
- `tables/`: optional table source files
- `refs.bib`: BibTeX database
- `highlights.txt`: separate highlights file (Elsevier submission item)

## Local Authoring vs Editorial Manager Submission

This local structure uses subfolders (`sections/`, `figures/`) for maintainability.

Before uploading to Editorial Manager, Elsevier support indicates that **LaTeX source files should not be in subfolders**. Prepare a flattened submission package (all `.tex`, `.bib`, and figure files in one folder) for upload.

## Recommended Workflow

1. Draft in this folder using `latexmk`.
2. Keep generated plot scripts outside this folder; only place final figures in `figures/`.
3. Use labels/references (`\\label`, `\\ref`, `\\cref`) instead of hard-coded figure numbers.
4. Near submission, flatten the folder structure for Editorial Manager upload.

## Compile (example)

```bash
cd papers/cg-coupled-servo
latexmk -pdf -interaction=nonstopmode -output-directory=build main.tex
```

## Notes for This Project

- Replace thesis-style numbering references (e.g., `Fig. 4.x`) with LaTeX labels.
- Use `subcaption` for combined figures such as the 4-panel macroscopic response figure.
- If a plot is generated as PNG/JPG during exploration, export a publication-quality PDF/PNG copy into `figures/` for the manuscript.

## Multi-paper Repository Layout

This manuscript now lives under `papers/cg-coupled-servo/`.
Shared assets for multiple papers (macros, common bibliography entries, helper scripts) live under `papers/shared/`.
An Editorial Manager flattening helper script skeleton is provided at `papers/shared/scripts/flatten_for_em.sh`.

