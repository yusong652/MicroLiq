# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a PhD thesis research project on **microscopic analysis of fabric evolution in liquefaction using Discrete Element Method (DEM)**. The repository contains interactive web visualizations, experimental data analysis tools, and DEM simulations focused on soil liquefaction research.

## Repository Structure

The project is organized into chapter-based directories corresponding to thesis chapters:

- **index.html** - Main landing page with tabbed navigation for all thesis chapters
- **triaxial/** - Chapter 1: True triaxial apparatus simulation (fabric evolution under general stress states)
- **torsionSim/** - Chapter 2: Hollow cylindrical apparatus (HCA) simulation with combined-servo-mechanism
- **experiment/** - Chapter 3: Experimental validation data and analysis scripts
- **multiDirection/** - Chapter 4: Multi-directional shear stress effects on liquefaction
- **taichiDEM/** - Chapter 5: GPU-accelerated DEM implementation using TaichiLang
- **graphics/** - Chapter 6: Ray tracing visualization for DEM (ray_tracer/ and rasterizer/ subdirectories)
- **quadTree/** - Interactive p5.js particle simulation with quadtree collision detection (used in landing page)
- **js/** - Shared JavaScript utilities:
  - `navigation.js` - Tab navigation with drag/scroll support
  - `theme.js` - Dark/light mode toggle
  - `tooltip.js` - Tooltip functionality for UI elements
- **css/** - Shared styles with CSS variables for theming

## Technology Stack

### Frontend
- **HTML/CSS/JavaScript** - Core web technologies
- **p5.js** - Creative coding library for particle animations in quadTree
- **Font Awesome** - Icon library for UI elements
- Interactive canvas-based visualizations with theme support (dark/light modes)

### Data Analysis
- **Python** - Primary language for experimental data processing
- **matplotlib** - Plotting and visualization
- **pandas** - Data manipulation and CSV processing
- **numpy** - Numerical computations

### DEM Simulation
- **TaichiLang** - GPU-accelerated physics simulations (referenced in taichiDEM)
- External repositories referenced:
  - [taichiDEM](https://github.com/yusong652/taichiDEM)
  - [ray-tracing](https://github.com/yusong652/ray-tracing)

## Key Architecture Details

### Navigation System
The main index.html implements a sophisticated tab-based navigation:
- Tab buttons with drag-to-scroll and auto-centering behavior
- Smooth scrolling with active state management
- Touch and mouse event handling for cross-platform support
- Dynamic content section switching without page reloads

### Theme System
Implemented via CSS variables and JavaScript toggle:
- Dark mode: Deep blue backgrounds (rgb(30, 40, 55)) for canvas
- Light mode: Green backgrounds (rgb(30, 160, 120)) for canvas
- Synchronized across p5.js canvas and DOM elements
- Theme state persisted via localStorage

### Particle Animation (quadTree)
Interactive p5.js simulation on landing page:
- QuadTree spatial partitioning for efficient collision detection
- Particle physics with boundary interactions
- Dynamic particle addition on mouse interaction
- "Clear particles" animation with accelerating boundary movement
- Canvas-only mouse interaction detection to prevent conflicts with UI buttons

### Experimental Data Processing
Python scripts in experiment/ subdirectories follow consistent patterns:
- Read CSV data from test folders (test240829/, test240910/, etc.)
- Channel mappings: CH_1 (shear stress), CH_3 (axial force), CH_4 (pore pressure)
- Stress calculations based on hollow cylindrical specimen geometry (outer: 0.05m, inner: 0.03m)
- K₀ (horizontal to vertical stress ratio) analysis for liquefaction resistance
- Relative density correlation with liquefaction cycles

## Development Workflow

### Running the Project
This is a static web project - no build step required:
1. Open `index.html` in a web browser directly, or
2. Use a local server: `python -m http.server 8000` (or similar)
3. Navigate to individual chapter HTML files for specific content

### Experimental Data Analysis
For processing experiment data:
```bash
cd experiment/
python k0_effect.py  # Generates K₀ effect visualization
```

Individual test folder scripts:
```bash
cd experiment/test241126/  # or any test folder
python draw_gamma_tau.py   # Strain vs shear stress
python draw_time_tau.py    # Time series shear stress
python draw_time_u.py      # Time series pore pressure
python draw_p_tau.py       # Effective stress path
```

### File Organization Conventions
- Each chapter has a standalone HTML file with self-contained content
- Demo assets stored in chapter-specific `demo/` subdirectories
- Experimental test data organized by date (testYYMMDD format)
- Python scripts use consistent naming: `draw_[x-axis]_[y-axis].py`

## Important Context

### Research Domain
This is geotechnical engineering research focused on:
- Soil liquefaction during earthquakes
- Discrete Element Method (DEM) numerical simulations
- Fabric tensor evolution and anisotropic consolidation effects
- K₀ consolidation stress states
- Multi-directional seismic loading

### Citations and Publications
The work references published research:
- Han, Y., Kato, S. & Kim, BS. (2023) - True triaxial DEM analysis (KSCE J Civ Eng)
- Ma, Q., et al. (2024) - HCA simulation approach (Computers and Geotechnics)

### Visualization Philosophy
The project emphasizes interactive visualizations over static images:
- Canvas-based animations for particle interactions
- GPU-accelerated rendering for DEM scenes
- Ray tracing for high-fidelity offline rendering
- No dependency on external visualization tools (e.g., Paraview)

## Special Considerations

### Canvas Loading Transition
The quadTree sketch implements a loading placeholder with fade transition:
- Shows spinner during p5.js initialization
- Fades in canvas and removes placeholder after setup
- Prevents flash of unstyled content

### Boundary Animations
The "Clear particles" feature uses physics-based animation:
- Acceleration variable: starts at 0, increments by 0.008
- Velocity caps at 32.0 units
- Boundary wall moves from left, pushing particles off-canvas
- State resets when wall_x_min >= width

### Stress Calculations
Hollow cylindrical specimen geometry:
- Outer radius: 0.05 m
- Inner radius: 0.03 m
- Shear stress: τ = T × 3 / (π × 2 × (r_o³ - r_i³)) / 1000
- Axial stress: σ = F / (π × (r_o² - r_i²)) / 1000
- Units converted to kPa

### Data File Formats
- Experimental data: CSV with channel columns (CH_1, CH_3, CH_4)
- Recording frequency: 0.05 Hz (20 second intervals)
- Liquefaction criterion: p' < 5% of initial p'
