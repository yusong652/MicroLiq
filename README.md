# Microscopic Analysis of Fabric Evolution in Liquefaction Using DEM

PhD thesis research at Kyoto University (DPRI) investigating microscopic mechanisms of soil liquefaction through Discrete Element Method simulations, with a parallel research line on AI-driven workflows for numerical simulations.

**[Live site](https://yusong652.github.io/MicroLiq/)**

## Research

### Microscopic Fabric Analysis
Fabric evolution in granular soils through true triaxial DEM simulations under general stress conditions, including various stress paths and Lode angles.

### DEM-Based HCA Simulation
A coupled analytical servo mechanism that simultaneously satisfies undrained conditions and complex stress states in hollow cylinder apparatus simulations, enabling DEM-based cyclic torsional shear under arbitrary stress conditions.

### Multi-Directional Seismic Loading
The double-8 loading path to quantitatively isolate multi-directional shear effects on liquefaction, maintaining equal shear stress magnitudes across different loading patterns.

### Agentic DEM Workflow
A full-stack AI agent platform ([toyoura-nagisa](https://github.com/yusong652/toyoura-nagisa)) for autonomous DEM simulation, featuring multi-agent architecture, multi-provider LLM support, web and terminal frontends, and a "Script is Context" philosophy with git-versioned PFC executions. The documentation and execution layer was extracted into a standalone MCP server ([pfc-mcp](https://github.com/yusong652/pfc-mcp)) usable with any MCP-compatible client.

## Publications

- **Han, Y.**, Kato, S. & Kim, B.S. (2023). DEM Analysis of Fabric Evolution and Behavior of Granular Geomaterials in True Triaxial Test with Flexible Boundary. *KSCE Journal of Civil Engineering*, 27, 3341-3354. [DOI](https://doi.org/10.1007/s12205-023-0336-1)
- Ma, Q., He, X., Zhou, Y.-G., Chen, Y.-M. & **Han, Y.-S.** (2024). An approach to DEM simulation of hollow torsional shear tests for achieving general loading paths. *Computers and Geotechnics*, 172, 106402. [DOI](https://doi.org/10.1016/j.compgeo.2024.106402)

## Repository Structure

```
papers/           Journal paper manuscripts (LaTeX)
thesis/           Thesis chapters (Markdown/Obsidian)
triaxial/         Ch3: True triaxial apparatus simulation
torsionSim/       Ch4: HCA simulation with coupled servo mechanism
experiment/       Ch4: Experimental data and analysis
multiDirection/   Ch5: Multi-directional shear effects
taichiDEM/        Appendix: GPU-accelerated DEM (TaichiLang)
graphics/         Appendix: Ray tracing visualization
site/             Static site assets (animation, CSS, JS)
index.html        Landing page
```

## Related Projects

- **[toyoura-nagisa](https://github.com/yusong652/toyoura-nagisa)** — AI agent platform for PFC simulations (FastAPI + React + CLI, multi-provider LLM, WebSocket bridge)
- **[pfc-mcp](https://github.com/yusong652/pfc-mcp)** — MCP server for Itasca PFC (documentation browsing, task execution, plot capture)
- **[taichiDEM](https://github.com/yusong652/taichiDEM)** — GPU-accelerated DEM engine built with TaichiLang
- **[ray-tracing](https://github.com/yusong652/ray-tracing)** — Offline particle renderer with reflection and refraction
