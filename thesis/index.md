---
title: "Microscopic Analysis of Fabric Evolution in Liquefaction Using DEM"
author: "HAN YUSONG"
tags: [thesis, index, navigation, table-of-contents]
aliases: [Thesis Index, Main Index, TOC]
---

# Microscopic Analysis of Fabric Evolution in Liquefaction Using DEM

**Author:** HAN YUSONG

## Abstract

Liquefaction, characterized by the loss of soil strength due to the buildup of pore water pressure during seismic events, poses significant risks to infrastructure and buildings. The Discrete Element Method (DEM) facilitated the direct analysis of particle interactions and microscopic fabric evolution, bridging the gap between micro-scale processes and macro-scale behaviors like liquefaction. This research established a methodology for evaluating seismic stability and liquefaction resistance using microscopic parameters with DEM.

Evolution of soil fabric under diverse stress states through drained true triaxial shear tests was explored using DEM. A combined servo mechanism was innovatively proposed to replicate undrained conditions and stress states in hollow cylinder apparatus (HCA) shear tests. A new double-8 shear loading method is proposed to isolate and analyse the impact of multi-directional shear stress on liquefaction.

**Keywords:** Liquefaction, Discrete element method, Fabric anisotropy, Multi-directional shear stress

---

## Thesis Chapters

### [[00_front_matter|Front Matter]]
Title page, abstract, keywords, and complete table of contents

### [[01_introduction|Chapter 1: Introduction]]
Overview of liquefaction phenomena, historical earthquake damage cases (1964 Niigata, 1995 Kobe, 2024 Noto), and the motivation for using DEM to understand microscopic mechanisms. Establishes research objectives and methodologies for investigating stress anisotropy and multi-directional shear effects on liquefaction resistance.

### [[02_literature_review|Chapter 2: Literature Review]]
Comprehensive review of granular material behavior under monotonic and cyclic shear, covering dilatancy, undrained responses, and liquefaction mechanisms. Examines constitutive models from critical state soil mechanics to advanced fabric-based approaches, and introduces DEM fundamentals including contact models and computational algorithms.

### [[03_fabric_evolution|Chapter 3: Fabric Evolution Under General Stress States]]
Investigation of fabric evolution in true triaxial DEM simulations under various stress paths and Lode angles. Analyzes critical state behavior of void ratio, coordination number, and fabric anisotropy. Explores contact orientation distributions and their evolution with axial strain, revealing the role of stress anisotropy in microstructural development.

### [[04_anisotropic_consolidation|Chapter 4: Study On Factors Affecting Liquefaction Resistance During Anisotropic Consolidation]]
Development of a combined servo mechanism for DEM-based hollow cylinder apparatus (HCA) simulations. Examines the influence of K₀ (horizontal-to-vertical stress ratio) on liquefaction resistance through both DEM simulations and experimental validation. Identifies the critical role of initial coordination number ($Z_{m0}$) in liquefaction resistance and reveals non-monotonic trends with stress anisotropy.

### [[05_multidirectional_shear|Chapter 5: Effects Of Multi-Directional Shear Stress On Liquefaction Resistance]]
Introduction of innovative double-8 shear loading method to isolate multi-directional shear effects on liquefaction. Compares unidirectional versus multi-directional loading patterns through DEM simulations. Analyzes microscopic fabric metrics ($Z_m$, $F_c$) and their evolution during liquefaction under complex loading paths, demonstrating increased vulnerability under multi-directional shear.

### [[06_conclusions|Chapter 6: Conclusions And Future Studies]]
Synthesis of key findings on stress anisotropy and multi-directional shear effects on liquefaction resistance. Discusses the importance of microscopic parameters in evaluating seismic stability. Proposes future research directions for multi-scale physics integration and enhanced predictive capabilities.

---

## References and Appendices

### [[07_references|References]]
Complete bibliography of cited works

### [[08_appendix1_hpc|Appendix 1: Implementation Of High-Performance Computing In DEM]]
GPU-accelerated DEM implementation using TaichiLang, covering efficient neighbor search algorithms, contact detection, and validation through slope generation and triaxial shear demonstrations. Includes force chain visualization and stress path analysis.

### [[09_appendix2_raytracing|Appendix 2: Ray Tracing For Enhanced Visualization In DEM]]
Ray tracing fundamentals for high-fidelity DEM visualization, including camera models, ray-object intersection, lighting models (ambient, point, directional), reflection/refraction physics, and optimization techniques (supersampling, spatial partitioning).

---

## Quick Navigation

**Core Research Chapters:**
- [[01_introduction|Introduction]] → [[02_literature_review|Literature]] → [[03_fabric_evolution|Fabric Evolution]] → [[04_anisotropic_consolidation|K₀ Effects]] → [[05_multidirectional_shear|Multi-Directional Shear]] → [[06_conclusions|Conclusions]]

**Technical Implementation:**
- [[08_appendix1_hpc|HPC/GPU Computing]] | [[09_appendix2_raytracing|Visualization & Ray Tracing]]

**Research Focus Areas:**
- #fabric-evolution #anisotropic-consolidation #multidirectional-shear #K0-effect #liquefaction-resistance

---

*This thesis investigates microscopic mechanisms of liquefaction through Discrete Element Method simulations, with emphasis on stress anisotropy and multi-directional seismic loading effects.*
