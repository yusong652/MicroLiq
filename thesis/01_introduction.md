---
title: "Chapter 1: Introduction"
tags: [thesis, chapter-1, introduction, liquefaction, motivation]
aliases: [Introduction, Chapter 1]
---

# Introduction

## Liquefaction and Its Engineering and Societal Consequences

Soil liquefaction is a major geotechnical hazard that occurs when saturated granular soils lose their strength due to elevated pore water pressure, often triggered by seismic loading. Under intense, short-duration shear stress, the rearrangement of soil particles weakens interparticle contacts, leading to a rise in pore water pressure. As a result, the soil temporarily loses its rigidity and behaves like a fluid, causing ground instability. This phenomenon poses significant risks to infrastructure and public safety, as it can lead to large-scale ground failure, structural collapse, and disruptions to lifeline systems. The consequences of liquefaction have been observed in numerous historical earthquakes, demonstrating the widespread damage it can inflict on urban environments.

One of the earliest and most extensively studied cases of liquefaction-induced failure is the 1964 Niigata Earthquake (M 7.6, Japan) (Kishida, 1966; Ohsaki, 1966; Seed and Idriss, 1967; Yoshimi and Tokimatsu, 1977; Ishihara and Koga, 1981; Ishihara and Yoshimine, 1992; Yoshida et al., 2007). The collapse of apartment buildings in Niigata City, as shown in Fig.1.1, despite their structural integrity, was attributed to liquefaction-induced bearing capacity failure of the underlying saturated sand layers. Similarly, widespread liquefaction led to severe damage to river embankments and bridges, as shown in Fig. 1.2, posing a significant threat to critical infrastructure.

![建筑的摆设布局 中度可信度描述已自动生成](thesis/assets/media/image1.png)

Fig. 1.1. Tilting and overturning of Kawagishi-cho apartment buildings due to liquefaction-induced foundation failure in the 1964 Niigata Earthquake, Japan (Source: Elnashai, A. S., 2015)

![图片包含 日历 描述已自动生成](thesis/assets/media/image2.png)

Fig. 1.2. Collapse of Showa bridge caused by liquefaction during the 1964 Niigata earthquake, Japan, (Source: Yoshida et al., 2007)

Another catastrophic example is the 1995 Hanshin-Awaji Earthquake (M 6.9, Japan), which caused extensive liquefaction across reclaimed lands in Kobe, particularly in Port Island, Rokko Island, and Fukae Island (Ishihara et al., 1997; Hatanaka et al., 1997). Severe damage was observed in port infrastructures (Fig. 1.3), such as the collapse of quay walls, lateral spreading of waterfront areas, and ground subsidence, significantly affecting Kobe Port, one of Japan's largest trading hubs. These failures disrupted maritime transportation for months, showing the vulnerability of reclaimed land to liquefaction-induced ground deformations.

![木船上 低可信度描述已自动生成](thesis/assets/media/image3.png)

Fig. 1.3 Liquefaction-induced ground deformation at Kobe Port during the 1995 Hanshin-Awaji Earthquake, causing severe damage to port infrastructure (Source: Ministry of Land, Infrastructure, Transport, and Tourism (MLIT))

Most recently, the 2024 Noto Peninsula Earthquake (M 7.5, Japan) once again demonstrated the catastrophic impact of liquefaction, with extensive ground deformations observed in coastal and reclaimed areas (Suppasri et al., 2024). Liquefaction-induced settlement and lateral spreading contributed to the collapse of buildings and road networks, further emphasizing the need for improved predictive models and mitigation strategies in seismic-prone regions.

Beyond physical destruction, the economic and social repercussions of liquefaction events can be profound. Recovery efforts following liquefaction-induced damage often require significant financial investment in rebuilding and retrofitting structures. In addition, the failure of lifeline infrastructure, such as water, gas, and power networks, can lead to prolonged disruptions, affecting communities and businesses.

Given the severity of its consequences, understanding the mechanisms of liquefaction and improving predictive models remain critical priorities in geotechnical engineering. This dissertation aims to contribute to this effort by investigating the microscopic factors influencing liquefaction resistance and evaluating soil response under different stress conditions.

## Motivation and Research Challenges

### The Need for a Microscopic Understanding of Liquefaction

#### Comparison with Laboratory Tests

While traditional laboratory experiments have greatly contributed to our understanding of liquefaction mechanisms, they are inherently limited in several ways:

Experimental results are often influenced by sample preparation methods, making it difficult to ensure identical initial states across tests. This variability complicates the assessment of factors affecting liquefaction resistance. Most laboratory tests focus on simplified stress conditions (e.g., unidirectional shear) due to experimental constraints, which do not fully capture the multi-directional shear loading experienced during real earthquakes. While macroscopic trends in liquefaction resistance are well-documented, the microscopic origins of these variations---such as changes in contact number, fabric anisotropy, and contact force evolution---remain insufficiently understood.

Given these limitations, a numerical approach such as the Discrete Element Method (DEM) is essential for achieving a deeper understanding of liquefaction processes. DEM allows for precise control over initial conditions, eliminates uncertainties from sample preparation, and enables simulations under realistic stress paths that are difficult to reproduce experimentally. The ability to track particle-scale fabric evolution provides unprecedented insight into liquefaction resistance mechanisms, making DEM an indispensable tool for advancing liquefaction research.

#### Comparison with Traditional Continuum-Based Methods

In addition to its advantages over laboratory experiments, DEM also addresses key limitations of continuum-based numerical models.

DEM directly models the fundamental physics of granular materials at the particle scale. Rather than relying on phenomenological stress-strain relations, DEM captures macroscopic behaviors through microscopic interactions, such as interparticle contacts, sliding, rolling, damping and energy transmission, providing a more physically grounded and direct approach to modeling liquefaction resistance.

DEM naturally captures localized deformation phenomena, such as shear banding, fracturing, and force concentration---all of which are crucial for understanding liquefaction initiation, as each particle moves independently while interacting with its neighbors. In traditional numerical models, the influence of fabric anisotropy on macroscopic responses must be incorporated through additional constitutive assumptions or correction factors. In contrast,

DEM inherently accounts for fabric anisotropy at the particle scale. This advantage is crucial in analyzing anisotropic consolidation, multi-directional cyclic shear when studying liquefaction resistance under complex loading paths.

### Unresolved Challenges in DEM-based Liquefaction Research

Despite previous research efforts, several key challenges remain unresolved. This dissertation addresses these critical gaps through DEM-based analyses, focusing on three major research challenges:

While Hollow Cylinder Apparatus (HCA) experiments provide valuable insights into liquefaction resistance under complex loading conditions, DEM-based undrained HCA simulations are lacking. Establishing a numerical approach to reproduce undrained cyclic torsional shear tests is crucial for linking experimental observations with microscopic interpretations. On the other hand, liquefaction resistance varies significantly with different stress anisotropy conditions, but the underlying microscopic drivers remain unclear. A major challenge is to identify how the microscopic factors influence liquefaction resistance under anisotropic stress states.

Real earthquakes impose multi-directional cyclic shear stress, yet conventional laboratory tests often simplify cyclic loading to a single direction due to experimental constraints. The insufficient systematic DEM studies on multi-directional shear loading limits our ability to quantify its effects on liquefaction resistance.

The above necessity of and existing challenges in DEM simulation for liquefaction analysis motivated this thesis.

## Objectives and Methodologies

This study aims to systematically explore how macroscopic stress conditions, including stress anisotropy from anisotropic consolidation and multi-directional shear stress, influence microscopic structural evolution in granular materials and ultimately affect liquefaction resistance. The hypothesis is that variations in stress conditions induce changes in microstructural indicators, which in turn control the soil's resistance to liquefaction. To investigate these relationships, DEM simulation serves as a numerical experimental tool, allowing precise analysis of particle-scale responses under controlled loading conditions.

**Objective 1: Microscopic Mechanisms Governing Liquefaction Resistance**

To examine how stress anisotropy influences liquefaction resistance, this study develops a DEM-based simulation framework to replicate undrained Hollow Cylinder Apparatus (HCA) tests. This approach ensures consistency with laboratory conditions while eliminating sample preparation biases. DEM simulations of anisotropic consolidation are conducted across different lateral-to-vertical stress ratios (K₀) to evaluate how initial stress anisotropy modifies contact fabric and its role in liquefaction resistance.

**Objective 2: Effects of Multi-Directional Shear Stress on Liquefaction Resistance**

To overcome the limitations of conventional unidirectional cyclic shear tests, which fail to fully represent real seismic loading, this study investigates the impact of multi-directional shear stress on liquefaction processes. DEM simulations implement innovative shear stress paths, such as single-8 and double-8 patterns, to examine how different shear loading conditions influence fabric evolution and structural adjustments. The study investigates how multi-directional shear stress influences microstructural evolution and its role in liquefaction processes, providing a more comprehensive understanding of the effects of complex loading conditions.

## Thesis Outline

Chapter 2 Literature Review

> This chapter provides a comprehensive review of past experimental studies on granular materials, focusing on key mechanical behaviors such as dilatancy and their responses under drained and undrained conditions. It then examines classical constitutive models used to describe granular soil behavior. The fundamentals of DEM are introduced, including contact models, essential data structures, and computational algorithms. Finally, the chapter reviews significant applications of DEM in liquefaction research.

Chapter 3 Fabric Evolution under General Stress Conditions

> This chapter investigates the morphological evolution of granular fabric under different stress paths, revealing its potential influence on liquefaction resistance. The findings highlight the role of stress anisotropy in shaping microstructural characteristics, motivating the subsequent exploration of its impact on liquefaction resistance in later chapters.

Chapter 4 Study on Factors Affecting Liquefaction Resistance during Anisotropic Consolidation

> This chapter develops a DEM-based approach to replicate undrained hollow cylinder apparatus (HCA) tests. Using this method, cyclic shear simulations are conducted on anisotropically consolidated samples to explore the influence of microscopic factors on liquefaction resistance. The findings provide a direct link between initial stress anisotropy, microstructural evolution, and liquefaction behavior, offering new insights into the role of fabric in liquefaction resistance.

Chapter 5 Effects of Multi-Directional Shear Stress on Liquefaction Resistance

> This chapter extends the investigation of liquefaction resistance by examining the impact of multi-directional shear stress, which is often oversimplified in conventional laboratory tests. Using DEM simulations, this study introduces innovative shear stress paths to evaluate how multi-directional loading influences microstructural evolution and liquefaction resistance. The findings offer new insights into the vulnerability of granular materials under complex seismic loading conditions.

Chapter 6 Conclusions and Future Studies

> This chapter consolidates the key findings, emphasizing the influence of stress anisotropy and multi-directional shear stress on liquefaction resistance. Future research directions focus on integrating multi-scale physics frameworks to enhance the predictive capability of DEM and bridge the gap between particle-scale modeling and real-world geotechnical applications.
