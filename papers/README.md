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

- `cg-coupled-servo/`: Coupled servo for undrained HCA — Computers and Geotechnics

## Revision Diff SOP

Generate a tracked-changes PDF (`latexdiff`) to visualize modifications between revisions.

### Prerequisites

- `latexdiff` and `latexpand` (included in TeX Live)
- A git commit as the "old" checkpoint

### Steps

```bash
cd papers/<paper-slug>

# 1. Identify the old checkpoint commit
git log --oneline -- papers/<paper-slug>/sections/

# 2. Extract old versions of section files
mkdir -p diff/old_sections
for f in 01_introduction 02_methodology 03_results_discussion 04_conclusions; do
  git show <OLD_COMMIT>:papers/<paper-slug>/sections/${f}.tex > diff/old_sections/${f}.tex
done
git show <OLD_COMMIT>:papers/<paper-slug>/main.tex > diff/old_main.tex

# 3. Flatten both versions (resolve \input commands)
sed 's|sections/|old_sections/|g' diff/old_main.tex > diff/old_main_patched.tex
latexpand diff/old_main_patched.tex > diff/old_flat.tex
latexpand main.tex > diff/new_flat.tex

# 4. Generate diff tex
latexdiff diff/old_flat.tex diff/new_flat.tex > diff/diff_output.tex

# 5. Compile (copy to paper root so figure paths resolve)
cp diff/diff_output.tex .
latexmk -pdf -outdir=build diff_output.tex

# 6. Clean up
rm diff_output.tex
```

### Output

- `build/diff_output.pdf` — red strikethrough for deletions, blue bold for additions
- `diff/diff_output.tex` — kept in repo as a record

### Tips

- Commit before generating diff so the "new" version is clean
- Appendix warnings from `latexpand` (e.g., "Could not find file") are safe to ignore if appendices are unchanged
- After all revisions are done, create a checkpoint commit with a clear message for future diffs
