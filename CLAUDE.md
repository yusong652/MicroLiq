# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

PhD thesis research on **microscopic analysis of fabric evolution in liquefaction using DEM (Discrete Element Method)**. The repository contains:
- Thesis documentation (Markdown/Obsidian)
- Interactive web visualizations for each thesis chapter
- Experimental data analysis scripts (Python)
- DEM simulation tools
- Journal paper manuscripts (LaTeX)

## Repository Structure

```
thesis/           Thesis chapters in Markdown (Obsidian vault)
papers/           Journal paper manuscripts (LaTeX)
  cg-coupled-servo/    Paper 1: Coupled servo for undrained HCA → Computers and Geotechnics (near complete)
  multidirectional-shear/ Paper 2: Multi-directional shear (planned)
  shared/               Common macros, bib entries, scripts
triaxial/         Ch3: True triaxial apparatus simulation
torsionSim/       Ch4: HCA simulation with combined-servo-mechanism
experiment/       Ch4: Experimental data and analysis scripts
multidirection/   Ch5: Multi-directional shear effects
taichiDEM/        Appendix: GPU-accelerated DEM (TaichiLang)
graphics/         Appendix: Ray tracing visualization
quadTree/         Landing page particle animation (p5.js)
js/, css/         Shared web utilities and styles
index.html        Main landing page
```

### Papers Workspace

Each paper under `papers/<slug>/` is a self-contained LaTeX project:
- `main.tex` — root document, `sections/` — chapter .tex files
- `figures/` — paper-specific figures, `refs.bib` — bibliography
- `submission/` — flattened files for editorial manager upload
- Elsevier CAS double-column template (`cas-dc.cls`)
- Build: `latexmk -pdf -outdir=build main.tex` — all build artifacts must go to `build/`, never the paper root
- `papers/shared/` — reusable macros (`tex/macros-common.tex`), common bib entries, helper scripts

### Thesis (Obsidian)

- Vault root: `MicroLiq/` (not `MicroLiq/thesis/`)
- Navigate from `thesis/index.md` via wikilinks
- Image paths: `thesis/assets/media/imageX.png`
- LaTeX math: `$Z_m$`, `$$\tau = F/A$$`

### Experimental Data

- Test data in `experiment/testYYMMDD/` folders (CSV format)
- Channel mappings: CH_1 (shear stress), CH_3 (axial force), CH_4 (pore pressure)
- Script naming: `draw_[x-axis]_[y-axis].py`
- HCA specimen geometry: outer radius 0.05m, inner radius 0.03m

## Technology Stack

- **Web**: HTML/CSS/JS, p5.js — static site, no build step
- **Data analysis**: Python, matplotlib, pandas, numpy
- **DEM simulation**: PFC3D (commercial), TaichiLang (GPU-accelerated)
- **Papers**: LaTeX (Elsevier CAS template), BibTeX

## Research Context

### Key Concepts
- **Soil liquefaction**: Loss of soil strength during earthquakes
- **Fabric tensor**: Quantifies directional distribution of particle contacts
- $Z_m$ — Mechanical coordination number; $F_c$ — Fabric anisotropy invariant
- $\rho_c$ — Contact density; $e$ — Void ratio; $K_0$ — Lateral stress ratio

### Main Findings
- $Z_m$ shows uniqueness at critical state (void ratio and fabric anisotropy do not)
- Initial $Z_{m0}$ strongly correlates with liquefaction resistance
- $K_0$ effects on liquefaction are non-monotonic (validated by DEM + experiments)
- Multi-directional shear causes faster liquefaction than unidirectional

### Publications
- Han, Y., Kato, S. & Kim, BS. (2023) — True triaxial DEM analysis (KSCE J Civ Eng)
- Ma, Q., et al. (2024) — HCA simulation approach (Computers and Geotechnics)

## Related Projects

- **toyoura-nagisa** (`/Users/hanyusong/toyoura-nagisa`) — AI agent platform for PFC simulations; FastAPI + React, multi-provider LLM, real-time WebSocket to ITASCA PFC (formerly aiNagisa)
- **pfc-mcp** (`/Users/hanyusong/pfc-mcp`) — MCP server for PFC workflows + bridge runtime inside PFC GUI; provides documentation tools and script-based task execution
