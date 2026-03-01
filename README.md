# Microscopic Analysis of Fabric Evolution in Liquefaction Using DEM

PhD thesis research investigating microscopic mechanisms of soil liquefaction through Discrete Element Method (DEM) simulations, with an emerging research line on LLM-driven workflows for numerical simulations.

## Thesis Chapters

### Chapter 1: Introduction
Overview of liquefaction phenomena, historical earthquake damage cases (1964 Niigata, 1995 Kobe, 2024 Noto), and research objectives.

### Chapter 2: Literature Review
Critical state soil mechanics, constitutive models, DEM fundamentals, and contact models.

### Chapter 3: Fabric Evolution Under General Stress States
Investigation of fabric evolution in true triaxial DEM simulations under various stress paths and Lode angles. Analyzes critical state behavior of coordination number ($Z_m$), void ratio, and fabric anisotropy.

### Chapter 4: Study on Factors Affecting Liquefaction Resistance During Anisotropic Consolidation
Development of a combined servo mechanism for DEM-based hollow cylinder apparatus (HCA) simulations. Examines the influence of $K_0$ on liquefaction resistance through both DEM simulations and experimental validation.

### Chapter 5: Effects of Multi-Directional Shear Stress on Liquefaction Resistance
Introduction of double-8 shear loading method to isolate multi-directional shear effects. Demonstrates increased vulnerability under multi-directional shear compared to unidirectional loading.

### Chapter 6: Conclusions and Future Studies

## Appendices

### Appendix 1: High-Performance Computing in DEM
GPU-accelerated DEM implementation using TaichiLang with efficient neighbor search algorithms.

[taichiDEM](https://github.com/yusong652/taichiDEM)

### Appendix 2: Ray Tracing for DEM Visualization
Ray tracing fundamentals for high-fidelity particle visualization, including reflection and refraction effects.

[ray-tracing](https://github.com/yusong652/ray-tracing)

### Appendix 3: LLM-Driven Workflow for DEM Simulations
Application of LLM-based agents to numerical simulation workflows. Addresses the gap between general-purpose AI agents and domain-specific scientific computing tools (PFC, FLAC, ABAQUS) through documentation-driven approaches.

Two standalone projects have been developed from this research:

- **[toyoura-nagisa](https://github.com/yusong652/toyoura-nagisa)** — AI agent platform for PFC simulations. FastAPI + React frontend, multi-provider LLM support, real-time WebSocket connection to ITASCA PFC.
- **[pfc-mcp](https://github.com/yusong652/pfc-mcp)** — MCP (Model Context Protocol) server extracted from toyoura-nagisa. Provides PFC documentation browsing/search tools and a bridge runtime for script-based task execution inside PFC GUI. Usable with any MCP-compatible client (Claude Code, Claude Desktop, etc.).

## Interactive Visualizations

Web-based interactive visualizations for each chapter:

- `index.html` - Main landing page with chapter navigation
- `triaxial/` - True triaxial apparatus simulation
- `torsionSim/` - Hollow cylinder apparatus (HCA) simulation
- `experiment/` - Experimental data analysis
- `multiDirection/` - Multi-directional shear visualization

## Thesis Documentation

The complete thesis is available in Markdown format under `thesis/` for use with Obsidian:

```
thesis/
├── index.md
├── 00_front_matter.md
├── 01_introduction.md
├── 02_literature_review.md
├── 03_fabric_evolution.md
├── 04_1_anisotropic_consolidation_sim.md
├── 04_2_anisotropic_consolidation_exp.md
├── 05_multidirectional_shear.md
├── 06_conclusions.md
├── 07_references.md
├── 08_appendix1_hpc.md
├── 09_appendix2_raytracing.md
├── 10_appendix3_toyouraNagisa.md
└── assets/media/
```

## Keywords

Liquefaction, Discrete Element Method, Fabric Anisotropy, Coordination Number, Multi-directional Shear Stress, $K_0$ Consolidation, LLM Agent, Model Context Protocol
