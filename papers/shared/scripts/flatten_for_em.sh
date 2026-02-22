#!/usr/bin/env bash
set -euo pipefail

# Flatten a paper directory into a submission package suitable for
# Elsevier Editorial Manager (which generally expects no subfolders).
#
# Usage:
#   ./papers/shared/scripts/flatten_for_em.sh papers/sdee-k0-anisotropy
#
# Output:
#   <paper-dir>/submission/

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <paper-dir>" >&2
  exit 1
fi

paper_dir="${1%/}"
submission_dir="$paper_dir/submission"

if [[ ! -d "$paper_dir" ]]; then
  echo "Error: paper directory not found: $paper_dir" >&2
  exit 1
fi

mkdir -p "$submission_dir"
rm -f "$submission_dir"/*

echo "Flattening LaTeX package for Editorial Manager..."
echo "Source:      $paper_dir"
echo "Destination: $submission_dir"

# Copy top-level manuscript files
find "$paper_dir" -maxdepth 1 -type f \
  \( -name "*.tex" -o -name "*.bib" -o -name "*.bst" -o -name "*.cls" -o -name "*.sty" -o -name "*.txt" \) \
  -exec cp {} "$submission_dir"/ \;

# Copy section files (flattened)
if [[ -d "$paper_dir/sections" ]]; then
  find "$paper_dir/sections" -maxdepth 1 -type f -name "*.tex" -exec cp {} "$submission_dir"/ \;
fi

# Copy figures (flattened)
if [[ -d "$paper_dir/figures" ]]; then
  find "$paper_dir/figures" -maxdepth 1 -type f \
    \( -name "*.pdf" -o -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.eps" -o -name "*.tif" -o -name "*.tiff" \) \
    -exec cp {} "$submission_dir"/ \;
fi

# Rewrite path references in flattened TeX files so the package is directly uploadable.
# This handles common local-authoring patterns:
# - \input{sections/foo}   -> \input{foo}
# - \include{sections/foo} -> \include{foo}
# - \graphicspath{{figures/}} -> \graphicspath{{./}}
# - \includegraphics{figures/foo.pdf} -> \includegraphics{foo.pdf}
if compgen -G "$submission_dir/*.tex" > /dev/null; then
  for tex_file in "$submission_dir"/*.tex; do
    perl -0pi -e '
      s/\\input\{sections\/([^}]+)\}/\\input{$1}/g;
      s/\\include\{sections\/([^}]+)\}/\\include{$1}/g;
      s/\\graphicspath\{\{figures\/\}\}/\\graphicspath{{.\/}}/g;
      s/(\\(?:includegraphics|safeincludegraphics)(?:\[[^\]]*\])?\{)figures\/([^}]+)\}/$1$2}/g;
    ' "$tex_file"
  done
fi

echo
echo "Done. Review the package manually before upload:"
echo "- Ensure all figure filenames referenced in .tex match the flattened copies."
echo "- Common subfolder references (sections/, figures/) were rewritten in submission .tex files."
echo "- Include Elsevier class/style files if required by the journal workflow."
