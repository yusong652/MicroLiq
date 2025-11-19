---
title: "Microscopic Analysis of Fabric Evolution in Liquefaction Using DEM"
author: "HAN YUSONG"
tags: [thesis, liquefaction, DEM, fabric-evolution, front-matter]
aliases: [Front Matter, Title Page, Abstract, TOC]
---

# Microscopic Analysis of Fabric Evolution in Liquefaction

**Using Discrete Element Method**

HAN YUSONG

## Abstract

Liquefaction, characterized by the loss of soil strength due to the buildup of pore water pressure during seismic events, poses significant risks to infrastructure and buildings. The Discrete Element Method (DEM) facilitated the direct analysis of particle interactions and microscopic fabric evolution, bridging the gap between micro-scale processes and macro-scale behaviors like liquefaction. This research established a methodology for evaluating seismic stability and liquefaction resistance using microscopic parameters with DEM.

Evolution of soil fabric under diverse stress states through drained true triaxial shear tests was explored using DEM. The distribution of contact density ($\rho_{c}$) evolves with increasing axial strain and different Lode angle during triaxial shear. The effects of stress anisotropy on liquefaction resistance of sand soils were investigated through undrained cyclic shear simulations.

A combined servo mechanism was innovatively proposed to replicate undrained conditions and stress states in hollow cylinder apparatus (HCA) shear tests. The results demonstrate a significant positive correlation between the initial coordination number ($Z_{m0}$) and liquefaction resistance. Experimental studies revealed a non-monotonic trend in liquefaction resistance with stress anisotropy.

A new double-8 shear loading method is proposed to isolate and analyse the impact of multi-directional shear stress on liquefaction. Microscopic fabric metrics, such as $Z_{m}$ and $F_{c}$, play a vital role in evaluating liquefaction resistance. The variations in $Z_{m}$ and fabric anisotropy ($F_{c}$) during the liquefaction process reflect the susceptibility of granular sand to different shear stress patterns.

**Keywords**: Liquefaction, Discrete element method, Fabric anisotropy, Multi-directional shear stress

## Table of contents

[1 Introduction [6](#introduction)](#introduction)

[1.1 Liquefaction And Its Engineering And Societal Consequences [6](#liquefaction-and-its-engineering-and-societal-consequences)](#liquefaction-and-its-engineering-and-societal-consequences)

[1.2 Motivation And Research Challenges [9](#motivation-and-research-challenges)](#motivation-and-research-challenges)

[1.2.1 The Need For A Microscopic Understanding Of Liquefaction [9](#the-need-for-a-microscopic-understanding-of-liquefaction)](#the-need-for-a-microscopic-understanding-of-liquefaction)

[1.2.2 Unresolved Challenges In Dem-Based Liquefaction Research [11](#unresolved-challenges-in-dem-based-liquefaction-research)](#unresolved-challenges-in-dem-based-liquefaction-research)

[1.3 Objectives And Methodologies [12](#objectives-and-methodologies)](#objectives-and-methodologies)

[1.4 Thesis Outline [13](#thesis-outline)](#thesis-outline)

[2 Literature Review [16](#literature-review)](#literature-review)

[2.1 Macroscopic Behavior Of Granular Materials Under Monotonic And Cyclic Shear [16](#macroscopic-behavior-of-granular-materials-under-monotonic-and-cyclic-shear)](#macroscopic-behavior-of-granular-materials-under-monotonic-and-cyclic-shear)

[2.1.1 Dilatancy In Granular Materials [16](#dilatancy-in-granular-materials)](#dilatancy-in-granular-materials)

[2.1.2 Undrained Responses Of Granular Materials Under Monotonic Shear [18](#undrained-responses-of-granular-materials-under-monotonic-shear)](#undrained-responses-of-granular-materials-under-monotonic-shear)

[2.1.3 Undrained Responses Of Granular Materials Under Cyclic Shear [19](#undrained-responses-of-granular-materials-under-cyclic-shear)](#undrained-responses-of-granular-materials-under-cyclic-shear)

[2.2 Constitutive Models For Granular Materials: Advances And Limitations [20](#constitutive-models-for-granular-materials-advances-and-limitations)](#constitutive-models-for-granular-materials-advances-and-limitations)

[2.2.1 From Experimental Observation To Unified Theoretical Framework: The Critical State Soil Mechanics [20](#from-experimental-observation-to-unified-theoretical-framework-the-critical-state-soil-mechanics)](#from-experimental-observation-to-unified-theoretical-framework-the-critical-state-soil-mechanics)

[3 Fabric Evolution Under General Stress States [34](#fabric-evolution-under-general-stress-states)](#fabric-evolution-under-general-stress-states)

[3.1 Introduction [35](#introduction-1)](#introduction-1)

[3.2 Simulation Modeling [38](#simulation-modeling)](#simulation-modeling)

[3.2.1 Contact Model [38](#contact-model)](#contact-model)

[3.2.2 Specimen Preparation [39](#specimen-preparation)](#specimen-preparation)

[3.2.3 Shear Process In The Dem Simulation [42](#shear-process-in-the-dem-simulation)](#shear-process-in-the-dem-simulation)

[3.3 Results And Discussion [48](#results-and-discussion)](#results-and-discussion)

[3.3.1 Relationship Between Deviatoric Stress And Strain [48](#relationship-between-deviatoric-stress-and-strain)](#relationship-between-deviatoric-stress-and-strain)

[3.3.2 Critical State Line Of Void Ratio [56](#critical-state-line-of-void-ratio)](#critical-state-line-of-void-ratio)

[3.3.3 Critical State Line Of Coordination Number [57](#critical-state-line-of-coordination-number)](#critical-state-line-of-coordination-number)

[3.3.4 Critical State Line Of Anisotropic Fabric [59](#critical-state-line-of-anisotropic-fabric)](#critical-state-line-of-anisotropic-fabric)

[3.3.5 Contact Orientation [61](#contact-orientation)](#contact-orientation)

[3.4 Summary [68](#summary)](#summary)

[4 Study On Factors Affecting Liquefaction Resistance During Anisotropic Consolidation [71](#study-on-factors-affecting-liquefaction-resistance-during-anisotropic-consolidation)](#study-on-factors-affecting-liquefaction-resistance-during-anisotropic-consolidation)

[4.1 Introduction [72](#introduction-2)](#introduction-2)

[4.2 Dem Simulation Setup [76](#dem-simulation-setup)](#dem-simulation-setup)

[4.2.1 Specimen Preparation [76](#specimen-preparation-1)](#specimen-preparation-1)

[4.2.2 Implementation Of Undrained Condition [84](#implementation-of-undrained-condition)](#implementation-of-undrained-condition)

[4.2.3 Application Of Shear Force [86](#application-of-shear-force)](#application-of-shear-force)

[4.3 Results And Discussion [87](#results-and-discussion-1)](#results-and-discussion-1)

[4.3.1 Macroscopic Response [87](#macroscopic-response)](#macroscopic-response)

[4.3.2 Microscopic Interpretation [97](#microscopic-interpretation)](#microscopic-interpretation)

[4.4 Summary [111](#summary-1)](#summary-1)

[4.5 Experimental Validation Of K0 Effects On Liquefaction Resistance [114](#experimental-validation-of-k0-effects-on-liquefaction-resistance)](#experimental-validation-of-k0-effects-on-liquefaction-resistance)

[4.5.1 Introduction [116](#introduction-3)](#introduction-3)

[4.5.2 Experimental Apparatus [118](#experimental-apparatus)](#experimental-apparatus)

[4.5.3 Experimental Procedures [121](#experimental-procedures)](#experimental-procedures)

[4.5.4 Results And Discussion [128](#results-and-discussion-2)](#results-and-discussion-2)

[4.5.5 Summary [138](#summary-2)](#summary-2)

[5 Effects Of Multi-Directional Shear Stress On Liquefaction Resistance [140](#effects-of-multi-directional-shear-stress-on-liquefaction-resistance)](#effects-of-multi-directional-shear-stress-on-liquefaction-resistance)

[5.1 Introduction [141](#introduction-4)](#introduction-4)

[5.2 Dem Simulation Setup [143](#dem-simulation-setup-1)](#dem-simulation-setup-1)

[5.2.1 Specimen Preparation [143](#specimen-preparation-2)](#specimen-preparation-2)

[5.2.2 Application Of Unidirectional And Multidirectional Shear Force [145](#application-of-unidirectional-and-multidirectional-shear-force)](#application-of-unidirectional-and-multidirectional-shear-force)

[5.3 Results And Discussion [148](#results-and-discussion-3)](#results-and-discussion-3)

[5.3.1 Macroscopic Response [148](#macroscopic-response-1)](#macroscopic-response-1)

[5.3.2 Microscopic Interpretation [152](#microscopic-interpretation-1)](#microscopic-interpretation-1)

[5.3.3 Discussion Based On Anisotropic Critical State Theory [160](#discussion-based-on-anisotropic-critical-state-theory)](#discussion-based-on-anisotropic-critical-state-theory)

[5.4 Summary [160](#summary-3)](#summary-3)

[6 Conclusions And Future Studies [162](#conclusions-and-future-studies)](#conclusions-and-future-studies)

[6.1 Conclusions [162](#conclusions)](#conclusions)

[6.2 Future Studies [167](#future-studies)](#future-studies)

[References [169](#references)](#references)

[Appendix 1 Implementation Of High-Performance Computing In Dem [180](#appendix-1-implementation-of-high-performance-computing-in-dem)](#appendix-1-implementation-of-high-performance-computing-in-dem)

[A1.1 Introduction [180](#a1.1-introduction)](#a1.1-introduction)

[A1.2 Methods And Framework [181](#a1.2-methods-and-framework)](#a1.2-methods-and-framework)

[A1.2.1 Efficient Neighbor Search [181](#a1.2.1-efficient-neighbor-search)](#a1.2.1-efficient-neighbor-search)

[A1.2.2. Interparticle Contact [189](#a1.2.2.-interparticle-contact)](#a1.2.2.-interparticle-contact)

[A1.3. Demonstration: Slope Generation [192](#a1.3.-demonstration-slope-generation)](#a1.3.-demonstration-slope-generation)

[A1.3.1. Simulation Setup [192](#a1.3.1.-simulation-setup)](#a1.3.1.-simulation-setup)

[A1.3.2. Slope Formation After Wall Movement [194](#a1.3.2.-slope-formation-after-wall-movement)](#a1.3.2.-slope-formation-after-wall-movement)

[A1.3.3. Discussion Of Validation Results [195](#a1.3.3.-discussion-of-validation-results)](#a1.3.3.-discussion-of-validation-results)

[A1.4. Demonstration Of Drained And Undrained Monotonic Triaxial Shear [195](#a1.4.-demonstration-of-drained-and-undrained-monotonic-triaxial-shear)](#a1.4.-demonstration-of-drained-and-undrained-monotonic-triaxial-shear)

[A1.4.1. Drained Shear Behavior [196](#a1.4.1.-drained-shear-behavior)](#a1.4.1.-drained-shear-behavior)

[A1.4.2. Monotonic Undrained Shear Behavior [198](#a1.4.2.-monotonic-undrained-shear-behavior)](#a1.4.2.-monotonic-undrained-shear-behavior)

[A1.4.3. Force Chain Evolution [199](#a1.4.3.-force-chain-evolution)](#a1.4.3.-force-chain-evolution)

[A1.4.4. Analysis Of Stress Paths In Drained And Undrained Shear Conditions [200](#a1.4.4.-analysis-of-stress-paths-in-drained-and-undrained-shear-conditions)](#a1.4.4.-analysis-of-stress-paths-in-drained-and-undrained-shear-conditions)

[A1.5. Summary [201](#a1.5.-summary)](#a1.5.-summary)

[Appendix 2 Ray Tracing For Enhanced Visualization In Dem [203](#appendix-2-ray-tracing-for-enhanced-visualization-in-dem)](#appendix-2-ray-tracing-for-enhanced-visualization-in-dem)

[A2.1. Fundamentals Of Ray Tracing [204](#a2.1.-fundamentals-of-ray-tracing)](#a2.1.-fundamentals-of-ray-tracing)

[A2.1.1. Camera, Ray, Viewport, And Scene [204](#a2.1.1.-camera-ray-viewport-and-scene)](#a2.1.1.-camera-ray-viewport-and-scene)

[A2.1.2. Determining Pixel Colors: Ray-Object Intersection [205](#a2.1.2.-determining-pixel-colors-ray-object-intersection)](#a2.1.2.-determining-pixel-colors-ray-object-intersection)

[A2.2. Lighting Models In Ray Tracing [206](#a2.2.-lighting-models-in-ray-tracing)](#a2.2.-lighting-models-in-ray-tracing)

[A2.2.1. Ambient Light [206](#a2.2.1.-ambient-light)](#a2.2.1.-ambient-light)

[A2.2.2. Point Light [207](#a2.2.2.-point-light)](#a2.2.2.-point-light)

[A2.2.3. Directional Light [208](#a2.2.3.-directional-light)](#a2.2.3.-directional-light)

[A2.3. Reflection And Refraction Between Objects [209](#a2.3.-reflection-and-refraction-between-objects)](#a2.3.-reflection-and-refraction-between-objects)

[A2.3.1. Reflection [209](#a2.3.1.-reflection)](#a2.3.1.-reflection)

[A2.3.2. Refraction [211](#a2.3.2.-refraction)](#a2.3.2.-refraction)

[A2.4. Techniques For Enhancing Quality And Efficiency [213](#a2.4.-techniques-for-enhancing-quality-and-efficiency)](#a2.4.-techniques-for-enhancing-quality-and-efficiency)

[A2.4.1. Supersampling And Anti-Aliasing [213](#a2.4.1.-supersampling-and-anti-aliasing)](#a2.4.1.-supersampling-and-anti-aliasing)

[A2.4.2. Spatial Partitioning For Efficiency [214](#a2.4.2.-spatial-partitioning-for-efficiency)](#a2.4.2.-spatial-partitioning-for-efficiency)

[A2.5. Summary [216](#a2.5.-summary)](#a2.5.-summary)
