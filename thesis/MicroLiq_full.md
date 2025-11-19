**Microscopic Analysis of Fabric Evolution in Liquefaction**

**Using Discrete Element Method**

HAN YUSONG

**Abstract**

Liquefaction, characterized by the loss of soil strength due to the buildup of pore water pressure during seismic events, poses significant risks to infrastructure and buildings. The Discrete Element Method (DEM) facilitated the direct analysis of particle interactions and microscopic fabric evolution, bridging the gap between micro-scale processes and macro-scale behaviors like liquefaction. This research established a methodology for evaluating seismic stability and liquefaction resistance using microscopic parameters with DEM.

Evolution of soil fabric under diverse stress states through drained true triaxial shear tests was explored using DEM. The distribution of contact density ($\rho_{c}$) evolves with increasing axial strain and different Lode angle during triaxial shear. The effects of stress anisotropy on liquefaction resistance of sand soils were investigated through undrained cyclic shear simulations.

A combined servo mechanism was innovatively proposed to replicate undrained conditions and stress states in hollow cylinder apparatus (HCA) shear tests. The results demonstrate a significant positive correlation between the initial coordination number ($Z_{m0}$) and liquefaction resistance. Experimental studies revealed a non-monotonic trend in liquefaction resistance with stress anisotropy.

A new double-8 shear loading method is proposed to isolate and analyse the impact of multi-directional shear stress on liquefaction. Microscopic fabric metrics, such as $Z_{m}$ and $F_{c}$, play a vital role in evaluating liquefaction resistance. The variations in $Z_{m}$ and fabric anisotropy ($F_{c}$) during the liquefaction process reflect the susceptibility of granular sand to different shear stress patterns.

**Keywords**: Liquefaction, Discrete element method, Fabric anisotropy, Multi-directional shear stress

**Table of contents**

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

# Literature Review

## Macroscopic Behavior of Granular Materials under Monotonic and Cyclic Shear

This section provides a comprehensive review of the fundamental mechanical behavior of granular materials, focusing on both monotonic and cyclic undrained shear responses. It begins with an introduction to dilatancy, a key characteristic governing volume changes in granular assemblies. The discussion then progresses to monotonic undrained shear tests, highlighting the evolution of excess pore water pressure and its impact on stress-strain behavior. Finally, cyclic undrained shear tests are examined, demonstrating the progressive accumulation of pore water pressure under repeated loading, ultimately leading to liquefaction. These experimental findings establish the foundation for understanding stress-strain evolution in granular materials.

### Dilatancy in Granular Materials

Granular materials, such as sand, exhibit complex mechanical behaviors, including permeability, shear strength, and dilatancy, as first systematically described by Reynolds (1885). As illustrated in Fig. 2.1, the spatial configuration of particles within a granular material undergoes significant rearrangements during shear deformation. The left configuration represents a loosely packed state with a higher void ratio, allowing for greater potential volumetric reduction under shear. In contrast, the right configuration corresponds to a densely packed state, where the void ratio is lower, and particle rearrangements are more constrained. These spatial rearrangements of particles can lead to either volume expansion or contraction, depending on the initial packing density and applied stress conditions.

![图示 描述已自动生成](thesis/assets/media/image4.png)

Fig. 2.1. Variation in the spatial configuration of granular material under shear loading, obtained from (Reynolds, 1885)

In densely packed configurations, particles are pushed to move apart during shear, leading to volume expansion---a phenomenon known as dilatancy. Conversely, in loosely packed configurations, particles move closer together, resulting in volume contraction. If no additional constraints are imposed, these volume changes occur freely, altering the pore space and interparticle contacts. Dilatancy governs the evolution of these microstructural properties, influencing the mechanical behavior of granular materials under external loading.

### Undrained Responses of Granular Materials under Monotonic Shear

![图示 描述已自动生成](thesis/assets/media/image5.png)

Fig. 2.2. Pore water pressure changes in a dilating sample by an undrained monotonic shear test (Bishop and Eldin, 1950)

Research on undrained shear behavior of granular materials can be traced back to the undrained triaxial tests by Bishop and Eldin (1950). Figure 2.2 illustrates the evolution of pore water pressure in a saturated granular material under undrained shear conditions. Initially, as shear strain is applied, the sample experiences contractive behavior, where particles attempt to rearrange into a denser configuration. However, due to the undrained condition, the volume remains constant, and this contractive tendency in soil skeleton results in an increase in pore water pressure. As shear deformation progresses, the material transitions to a positive dilatancy phase, where particle rearrangement induces an expansive tendency. Since the volume is constrained, this expansion leads to a reduction in pore water pressure.

### Undrained Responses of Granular Materials under Cyclic Shear

![图示 描述已自动生成](thesis/assets/media/image6.png) ![图示, 工程绘图 描述已自动生成](thesis/assets/media/image7.png)

Fig. 2.3. Stress-strain behavior under cyclic undrained triaxial shear on Masado soil (Source: Hatanaka et al., 1997): (a) Deviatoric stress vs. axial strain (b) Deviatoric stress vs. effective mean principal stress

While monotonic shear tests provide insight into fundamental pore pressure evolution trends, cyclic shear loading introduces additional complexities due to the repeated stress reversals and accumulation of pore pressure. Figure 2.3(a) and (b) present the response of deviatoric stress versus axial strain and effective mean principal stress, respectively, from triaxial cyclic shear tests on Masado soil conducted by Hatanaka et al. (1997). Under undrained cyclic shear conditions, granular materials experience a progressive increase in pore water pressure, leading to a gradual reduction in effective stress. As cyclic loading progresses, the strain amplitude increases, indicating the accumulation of plastic deformation and strain softening effects. Eventually, the effective stress diminishes to near zero, as seen in Figure 2.3(b), signaling the complete loss of shear strength and the onset of liquefaction. While these experimental findings reveal the fundamental stress-strain response under seismic loading, a comprehensive model is necessary to systematically describe and predict the liquefaction process across various loading conditions.

## Constitutive Models for Granular Materials: Advances and Limitations

This section reviews classical constitutive models developed to describe the mechanical behavior of granular materials. It first introduces the establishment of the critical state soil mechanics framework, which provides a fundamental basis for understanding stress-strain relationships and volume change tendencies in granular soils. Next, the Modified Cam-Clay model is discussed.

### From Experimental Observation to Unified Theoretical Framework: the Critical State Soil Mechanics

![图示 描述已自动生成](thesis/assets/media/image8.png)

Fig. 2.4. Consolidation line and critical state line in volume $v$ -- mean effective stress $p'$ - deviatoric stress $q$ space (Source: Atkinson and Bransby, 2012)

The development of critical state soil mechanics by Roscoe et al. (1958) established a systematic framework linking stress, strain, and void ratio in soils. Fig. 2.4 is a three-dimensional representation of the critical state soil mechanics framework in terms of the mean effective stress ($p'$), deviatoric stress ($q$), and specific volume (𝑣). It integrates key soil behavior concepts under different loading conditions.

When $q$ is zero, soil states lie on the bottom plane, representing isotropic stress conditions in the $p'$ - $v$ space. The normal consolidation line (NCL) represents states where the soil has not experienced a greater historical stress than its current effective mean stress $p'$. In contrast, states located below the NCL indicate over-consolidation, meaning the soil has previously been subjected to a higher effective stress than its current state.

![图示 描述已自动生成](thesis/assets/media/image9.png)

Fig. 2.5. Evolution of soil state during triaxial drained shear in $p'$-$v$--$q$ space (Source: Atkinson and Bransby, 2012)

Figure 2.5 illustrates the evolution of soil states during a triaxial drained shear test. Different initial consolidation states evolve along the shaded plane, representing the variation of stress and void ratio during shear. For a normally consolidated state, the stress path follows the outermost curve AB. As shear deformation increases, all initial states eventually reach the same point B, known as the critical state, regardless of their initial consolidation conditions. At this critical state, both void ratio and stress ratio remain constant despite further shear deformation, forming the critical state line (CSL).

![图示, 工程绘图 描述已自动生成](thesis/assets/media/image10.png)

Fig. 2.6. Evolution of soil state during triaxial undrained shear in $p'$-$v$--$q$ space (Source: Atkinson and Bransby, 2012)

Figure 2.6 illustrates the evolution of soil states in undrained shear tests within the $p'$-$v$-$q$ space. The shaded plane represents the shear paths corresponding to different initial consolidation states but with the same initial void ratio. For an initially normally consolidated state, the stress path follows the outermost curve, progressing toward the critical state. For an over-consolidated state, the path originates from the inner regions and evolves along the plane, ultimately reaching the same critical state as normally consolidated specimens. At the critical state, both void ratio and stress ratio remain constant despite continued shear deformation. Notably, the CSL obtained from undrained shear tests is identical to that from drained shear tests, underscoring its uniqueness. Along the CSL, the stress ratio $q/p'$ remains constant, independent of their absolute magnitudes.

![图表, 散点图 描述已自动生成](thesis/assets/media/image11.png)

Fig. 2.7. Normalized state paths during drained and undrained triaxial shear tests, and Roscoe surface (Source: Atkinson and Bransby, 2012)

During undrained shear of a normally consolidated state, the stress state is constrained by a distinct surface, known as the Roscoe surface. The stress path of undrained samples follows a curved trajectory on this surface. Similarly, in drained shear tests under constant $p'$ and constant radial stress conditions, the state also evolves along this surface. Notably, the Roscoe surface is not only unique but also exhibits a cross-sectional shape that remains invariant with respect to $p'$, as illustrated in Fig. 2.7.

### The Modified Cam-Clay model

### Limitations in classical theories and models

The classical critical state theory proposed by Roscoe et al. (1963) describes a dynamic equilibrium state: the stress state is stable while the strain evolves under large deformation conditions. However, this theory is mainly based on axisymmetric triaxial compression experiments. Thus, the uniqueness of the stress ratio and void ratio along other stress paths remain of great interest.

## Stress-induced-anisotropy 

### Stress-induced-anisotropy and critical state

To evaluate the failure criteria of the geostructures such as roads and embankments under the three-dimensional stress state, a three-principal stress test apparatus is required. Typical true triaxial apparatuses include all rigid types, all flexible types, and hybrid types. A device consisting of six plates was initially proposed by Pearce (1971) and Airey and Wood (1988). Ibsen and Praastrup (2022) improved it by modifying the boundary into six sliding rigid plates. However, even though the displacements on the boundary were uniform, friction-induced strain inhomogeneity is inevitable. Moreover, when the stress state was between the plane strain state and triaxial extension, the specimen was compressed from two directions, with stress concentration being reported in some studies (Shibata and Karube, 1965; Lo et al., 1994). An apparatus loaded with six flexible boundaries was proposed by Bell (1965) and improved by Ko and Scott (1967) and Sture and Desai (1979), with uniform pressure on the six surfaces of the cubic specimen being achieved. However, the strains at the corners between two adjacent flexible cells or bags might not be uniform (Yin et al., 2011). To overcome this disadvantage, the first true triaxial apparatus with hybrid (rigid and flexible) boundaries was developed by Green (1969, 1971). Further, Lade and Duncan (1973) modified the horizontal boundary to the composite material for compressibility. Nakai et al. (1986) improved the apparatus by applying major and minor principal stress using rigid plates and the intermediate principal stress using cell pressure to solve the interference and stress concentration problem. Nevertheless, friction between the rigid plate and specimen is inevitable in experiments, and achieving an ideal three-principal stress elemental test remains difficult.

The critical state line (CSL) in the void ratio ($e$) -- mean effective stress ($p'$) space was considered unique and independent of the stress paths from the triaxial compression and extension tests performed by Been et al. (1991). On the other hand, Wanatowski and Chu (2007) conducted drained and undrained laboratory tests under triaxial and plane strain conditions. The results exhibited a clear dependence on the stress paths: although the CSL is independent of the drainage condition, it varies with the intermediate principal stress ratio 'b'.

### Stress-induced-anisotropy and liquefaction

Soils under a natural state generally display various ratios of lateral to vertical effective stress, denoted as $K_{0}$. The impact of $K_{0}$ values on liquefaction strength frequently garners attention, yet the corresponding findings remain controversial. Ishihara and Takatsu (1979) observed that the liquefaction strength of Fuji River sand does not exhibit a notable dependency on the initial stress state with different $K_{0}$ values. Similar results were also obtained in the laboratory tests conducted by Yamashita and Toki (1993). On the other hand, the hollow torsional experiments conducted by Georgiannou and Konstadinou (2014) indicated that isotropically consolidated (IC) specimens demonstrate higher liquefaction resistance for loose sands than anisotropically consolidated (AC) specimens. By contrast, that pattern did not hold in dense states, where increasing relative density reversed the trend. Additionally, Vargas et al. (2020) concluded from similar laboratory tests on Ottawa sand with relative densities ranging from 50% to 80% that AC specimens with a $K_{0}$ of 0.5 showed a liquefaction strength approximately 20% higher than IC specimens. The experimental conclusions regarding the influence of $K_{0}$ on liquefaction resistance have been debated for decades, underscoring the necessity of elucidating $K_{0}$ effects on liquefaction resistance through alternative means.

## From Macroscopic to Microscopic: Insights into the Soil

### True Triaxial Test with Discrete Element Analysis

The discrete element method (DEM), proposed by Cundall (1971), is a Lagrangian method explicitly describing the motion of individual particles, and has been extensively applied in geotechnical engineering analyses. Many true triaxial tests have utilized DEM to analyze the CSL along varying stress paths. For instance, granular assemblies were monotonically sheared with various constant 'b' values in drained and undrained conditions in the DEM simulation performed by Zhao and Guo (2013). The obtained results revealed the uniqueness of the CSL in the $e$ -- $p'$ space. Furthermore, simple shear states and triaxial states were compared using DEM by Nguyen et al. (2021), and it was found that the CSL of void ratio depends on the stress states. The dependency of the CSL of the void ratio and fabric anisotropy on the intermediate principal stress ratio under various stress states was also reported in the DEM studies by Huang et al (2014a). Although the uniqueness or nonuniqueness of CSL was concluded in the early studies, detailed interpretations and discussions based on the morphology of fabric in the granular system under general stress states remain to be provided. In addition, only the comparison between different 'b' values has been emphasized and highlighted. In contrast, the variation of fabric anisotropy under different mean effective stress p' needs to be clarified. On the other hand, most of the past studies involved only a type of boundary (periodic or rigid boundaries) (Chang et al., 2021). True triaxial tests with hybrid boundaries, such as the flexible membrane boundary are needed to be developed as well.

### Hollow Torsional Cyclic Shear Test

Triaxial tests have been extensively conducted to elucidate the mechanisms of liquefaction, where saturated specimens were subjected to cyclic loading under undrained conditions until liquefaction was triggered. The influence of factors such as cyclic stress ratio (CSR), relative density, as well as confining pressure on the resistance to liquefaction was examined (Hyodo et al., 1991; Seed and Lee, 1966; Silver et al., 1976; Toki et al., 1986; Yoshimi et al., 1984). However, vertically propagating shear waves in the ground apply gradually varying shear stress on soil elements, leading to a continuous rotation of principal stress axes (Arthur et al., 2009; Arthur et al., 1980; Ishihara and Yasuda, 1975; Ishihara and Towhata, 1983; Yamashita and Toki, 1993).

Alternative testing methods, such as the hollow torsional shear test, apply shear forces to specimens, allowing for continuous variation of principal stress axes and thereby addressing the limitations of the triaxial test. Ishihara and Yasuda (1975) pioneered the utilization of hollow torsional cylindrical apparatus (HCA) by subjecting the hollow cylindrical samples to irregular wave loading, studying the disparities compared to triaxial shear tests. Tatsuoka et al. (1986) performed both triaxial and torsional tests on specimens prepared using different methods and found that the results were inconsistent between the triaxial and torsional tests. Torsional and triaxial shear tests conducted by Yamashita and Toki (1993) and employed by Oka et al. (1999) to enhance the constitutive model for liquefiable sands also demonstrated that method of testing with torsional or triaxial shear, influences the results of liquefaction resistance. These studies highlight the significance of experimental methods, such as HCA tests, in liquefaction analyses and aroused great interest in numerical replication of these tests.

The DEM simulation provides an insight into granular material and offers advantages by eliminating concerns related to variations in initial states caused by sample preparation, making it a desirable numerical method to study the cause of changes in liquefaction resistance. Numerous examples utilizing DEM exist for undrained cyclic shear tests to find explanations of microscopic factors affecting liquefaction resistance. Huang et al. (2018) conducted undrained shear tests on triaxial specimens, trying to relate monotonic and cyclic behaviors. Yang et al. (2021) performed undrained simple shear tests and studied the influence of multi-directional shear stress on liquefaction resistance. Jiang et al. (2021) applied various forms of strain waves to specimens, investigating their impact on liquefaction resistance. Morimoto et al. (2021) examined the impact of pre-shearing on the liquefaction resistance using DEM simulation of undrained triaxial cyclic shear tests. Xie et al. (2023), as well as Yang and Huang (2023) explored the effect of liquefaction history-induced fabric on liquefaction resistance by conducting reliquefication simulation. Zhang et al. (2023) arranged ellipsoidal clumped pebbles and applied both vertical and horizontal shear loading to discuss the influence of inherent fabric anisotropy on liquefaction resistance. Some of these studies included triaxial specimens, which do not account for principal stress axis rotation. Others utilized virtual periodic boundaries or cubic rigid box, which are difficult to implement in real-world scenarios. Replicating HCA tests through simulation provides a meaningful connection between numerical and experimental methods. Using DEM to replicate HCA test is relatively specialized, but still has precedents. Li et al. (2014) conducted DEM simulations of drained tests and investigated the strain localization in HCA test. Liu et al. (2021) conducted analysis of torsional shear tests under drained conditions and investigated the development of cracks at different principal stress rotation angles. This study introduced an algorithm that realizes both undrained and stress conditions in HCA test, filling a gap in HCA simulation using DEM (Ma et al., 2024).

To clarify the influence of the $K_{0}$ on liquefaction resistance, Yang and Taiebat\'s (2024) consolidated specimens with different preparation methods and conducted undrained cyclic shear tests. They found that both preparation protocols and $K_{0}$ influence liquefaction resistance. As the relative density increased, the difference in liquefaction resistance narrowed gradually for IC and AC states. Otsubo et al. (2022) employed $K_{0}$ to induce inherent fabric anisotropy in specimen under a low stress condition and then consolidated it to the target $p'$ and examined its effects on liquefaction resistance. A specimen with higher anisotropy has weaker stiffness in its minor direction and resulted a lower liquefaction resistance. Still, $K_{0}$ values discussed in the mentioned numerical studies lie in a limited range. For instance, comparison between $K_{0}$=1.0 and $K_{0}$=0.5 (Yang and Taiebat\'s, 2024) or from $K_{0}$=0.75 to $K_{0}$=1.35 (Otsubo et al., 2022), and exploration beyond these thresholds is lacking.

The stress paths for specimen preparation often entail linearly increasing $p'$ and $q$ to the state with target $K_{0}$ in both experimental (Vargas et al., 2020) and numerical (Yang and Taiebat, 2024) tests, thereby intriguing further investigation into the effects of stress paths by incorporating other consolidation stress paths. This study demonstrates DEM analysis of cyclic undrained HCA tests and explores the effects of $K_{0}$ on liquefaction resistance. Specimens are prepared with two different stress paths in consolidation and subjected to an extensive range of cyclic shear stress ratios. By examining macroscopic and microscopic responses such as fabric evolution, this study aims to provide evidence that elucidates how stress anisotropy influences liquefaction resistance.

### Multi-directional effects on liquefaction

Soil is subjected to a complex three-dimensional stress state during seismic loadings. To simulate the liquefaction process under seismic conditions, horizontal loading is often simplified to unidirectional cyclic loading due to the limitations of laboratory testing equipment. However, such simplification raised concerns about underestimating the impact of multi-directional cyclic shear on liquefaction resistance. Findings by Ishihara and Yamazaki (1980) indicated that multi-directional shear with equal amplitude in different directions requires only about 70% of the cyclic stress ratio of unidirectional shear to achieve the same shear strain. To better understand the role of multidirectional shear conditions on liquefaction, Kammerer et al. (2005) conducted simple shear tests on Monterey 0/30 Sand with varying relative densities and initial shear stresses, using linear, oval/circular, and figure-8 shaped loading paths. The results demonstrated that, compared to equivalent unidirectional shear with the same relative density and cyclic stress ratio, multidirectional shear induced faster liquefaction. The rotation of stresses in multidirectional shear likely accounts for the more pronounced build-up of pore pressure.

In addition to laboratory experiments, model tests have also provided evidence of the susceptibility of liquefaction behavior to multidirectional shaking. Pyke et al. (1975) found that multidirectional shaking on dry sand caused greater settlement and required less stress to induce liquefaction compared to unidirectional shaking. Results from Su and Li\'s (2008) centrifuge experiments indicate that, compared to unidirectional shaking, multi-directional shaking accelerates excess pore water pressure build-up as depth increases. A series of centrifuge tests conducted by El Shafee et al. (2017) compared uniaxial and biaxial excitations, showing that an increase of 40% in the uniaxial shaking amplitude was required to produce a similar excess pore water pressure response to that of biaxial shaking. This suggests that the common practice of increasing uniaxial shaking amplitude by 10% to approximate 2D shaking effects underestimates the true response of multidirectional shaking on soil liquefaction behavior.

Wei et al. (2020) investigated the effects of different shear stress paths, including unidirectional, oval, circular, and figure-8, on the number of cycles to liquefaction using DEM from the perspective of micro-scale fabric evolution. They found that the stress ratio in different directions and the shear path significantly influenced the number of cycles required to reach initial liquefaction, and fabric anisotropy evolved progressively throughout the liquefaction process. Yang et al. (2022) also explored the factors influencing the number of cycles to liquefaction in DEM simulations using similar unidirectional and multidirectional shear stress paths. They found that the figure-8 stress path required fewer cycles to reach liquefaction compared to the circular stress path. The coordination number and particle connectivity revealed that the system becomes temporarily under-constrained during 1-D linear and figure-8 shear paths at the moment when mean stress vanishes, whereas it remains over-constrained under 2-D linear and circular shear paths.

These studies have made significant contributions to understanding liquefaction by comparing unidirectional and multidirectional shear stress paths and their influence on liquefaction resistance. However, the methodologies used remain questionable. For instance, despite maintaining the same maximum shear force, the magnitude of unidirectional and multidirectional shear stress differs throughout the shear process. On the other hand, 2D shear paths like oval or circular maintain shear forces, preventing the effective stress from reaching zero. In contrast, unidirectional and figure-8 shear paths allow the effective stress to repeatedly cycle to zero, making it difficult to evaluate the impact of shear stress direction on liquefaction based on stress criterion. These factors introduced additional factors influencing the liquefaction, complicating the assessment of the specific influence of stress direction on the liquefaction process. Therefore, this chapter aims to present an improved approach that minimizes these limitations to explore whether changes in direction of shear stress affect the liquefaction behavior under different cyclic shear.

# Fabric Evolution under General Stress States

The fabric of granular geomaterials is related to properties such as shear strength, permeability, and liquefaction resistance. To evaluate the fabric evolution and behavior of geomaterials, a series of the true triaxial test simulations with flexible boundaries under general stress states in this study were performed using the three-dimensional discrete element method (DEM). First, the stress states at the axial strain of 20%, which indicates that the stress under the critical state conforms to the Matsuoka-Nakai criterion, were examined. Then the uniqueness of the coordination number and non-uniqueness of void ratio and invariant of anisotropic fabric tensor under the critical state were investigated based on the contact density, which indicates the relative number of contacts in different orientations. In particular, the contact density at the critical state under different mean effective principal stresses with its effects on the invariant of anisotropic fabric tensor were discussed. It was found that the contribution of the contact density to the fabric anisotropy decreased as the mean effective principal stress increased due to geometric limitations.

## Introduction 

To evaluate the failure criteria of the geostructures such as roads and embankments under the three-dimensional stress state, a three-principal stress test apparatus is required. Typical true triaxial apparatuses include all rigid types, all flexible types, and hybrid types. A device consisting of six plates was initially proposed by Pearce (1971) and Airey and Wood (1988). Ibsen and Praastrup (2022) improved it by modifying the boundary into six sliding rigid plates. However, even though the displacements on the boundary were uniform, friction-induced strain inhomogeneity is inevitable. Moreover, when the stress state was between the plane strain state and triaxial extension, the specimen was compressed from two directions, with stress concentration being reported in some studies (Shibata and Karube, 1965; Lo et al., 1994). An apparatus loaded with six flexible boundaries was proposed by Bell (1965) and improved by Ko and Scott (1967) and Sture and Desai (1979), with uniform pressure on the six surfaces of the cubic specimen being achieved. However, the strains at the corners between two adjacent flexible cells or bags might not be uniform (Yin et al., 2011). To overcome this disadvantage, the first true triaxial apparatus with hybrid (rigid and flexible) boundaries was developed by Green (1969, 1971). Further, Lade and Duncan (1973) modified the horizontal boundary to the composite material for compressibility. Nakai et al. (1986) improved the apparatus by applying major and minor principal stress using rigid plates and the intermediate principal stress using cell pressure to solve the interference and stress concentration problem. Nevertheless, friction between the rigid plate and specimen is inevitable in experiments, and achieving an ideal three-principal stress elemental test remains difficult.

On the other hand, the classical critical state theory proposed by Roscoe et al. (1963) describes a dynamic equilibrium state: the stress state is stable while the strain evolves under large deformation conditions. However, this theory is mainly based on axisymmetric triaxial compression experiments. Thus, the uniqueness of the stress ratio and void ratio along other stress paths remain of great interest. The critical state line (CSL) in the void ratio ($e$) -- mean effective stress ($p'$) space was considered unique and independent of the stress paths from the triaxial compression and extension tests performed by Been et al. (1991). On the other hand, Wanatowski and Chu (2007) conducted drained and undrained laboratory tests under triaxial and plane strain conditions. The results exhibited a clear dependence on the stress paths: although the CSL is independent of the drainage condition, it varies with the intermediate principal stress ratio 'b'. Moreover, the discrete element method (DEM) proposed by Cundall (1971), a Lagrangian method explicitly describing the motion of individual particles, has been extensively applied in geotechnical engineering analyses. Many true triaxial tests have utilized DEM to analyze the CSL along varying stress paths. For instance, granular assemblies were monotonically sheared with various constant 'b' values in drained and undrained conditions in the DEM simulation performed by Zhao and Guo (2013). The obtained results revealed the uniqueness of the CSL in the $e$ -- $p'$ space. Furthermore, simple shear states and triaxial states were compared using DEM by Nguyen et al. (2021), and it was found that the CSL of void ratio depends on the stress states. The dependency of the CSL of the void ratio and fabric anisotropy on the intermediate principal stress ratio under various stress states was also reported in the DEM studies by Huang et al (2014a). Although the uniqueness or nonuniqueness of CSL was concluded in the early studies, detailed interpretations and discussions based on the morphology of fabric in the granular system under general stress states remain to be provided. In addition, only the comparison between different 'b' values has been emphasized and highlighted. In contrast, the variation of fabric anisotropy under different mean effective stress p' needs to be clarified. On the other hand, most of the past studies involved only a type of boundary (periodic or rigid boundaries) (Chang et al., 2021). True triaxial tests with hybrid boundaries, such as the flexible membrane boundary are needed to be developed as well.

In this study, the difference in true triaxial tests with a flexible membrane in the intermediate principal stress direction and rigid plates in the major and minor principal stress directions is examined by the DEM simulations. The stress ratios and void ratios under the critical states are also presented and compared for different stress paths. Microscopic quantities, such as the coordination number ($Z$) and invariant of anisotropic fabric tensor under the critical state, are examined. Thereafter, the variation in those quantities with different stress paths and mean effective stress is interpreted by utilizing a newly proposed contact density method, which represents both contact orientation and $Z$ and refined the evaluation system for granular microstructures.

## Simulation modeling

### Contact model

The DEM simulations in this study were implemented using PFC3D (Itasca, 2005). The contact model in the DEM determines the interparticle relationship, such as the friction and contact force between particles. The contact models employed to represent cohesionless sands typically include linear models, in which the stiffness (Wei et al., 2022) or modulus (Zhao and Guo, 2013) is constant, and nonlinear models such as the Hertz-Mindlin model (Tsuji et al., 1992). The contact stiffness has a direct impact on the timestep. For instance, the study conducted by O\'Sullivan (2004) indicates that the critical timestep is proportional to the value of (*m*/*k*)^0.5^, where *m* is the mass of the particle at the end of the contact, and *k* denotes the stiffness of the contact. Thus, excessive stiffness increases the computational effort, but an appropriate contact stiffness guarantees the convergence and efficiency of the calculation. Table 2-1 and Fig 2.1 summarize the input parameters of a linear model applied in this study (Kim et al., 2012 & 2021).

![图标 描述已自动生成](thesis/assets/media/image12.png)

Fig. 2.1. Contact model in DEM simulation

Table 2-1. Input parameters of the linear model

  ------------------------------------------------------------------------
  Parameter                                             Value
  ----------------------------------------------------- ------------------
  Normal stiffness of ball, *k~n~*                      1×10^6^ N/m

  Shear stiffness of ball, *k~s~*                       5×10^5^ N/m

  Friction coefficient between balls, *μ~b~*            0.5

  Normal stiffness of wall, *k~n~*                      1×10^6^ N/m

  Friction coefficient between ball and wall, *μ~bw~*   0.0

  Density                                               2600 kg/m^3^

  Local damping                                         0.7
  ------------------------------------------------------------------------

### Specimen preparation

A uniform size distribution, similar to the typical grain size distribution of Toyoura sand, ranging from 0.1mm to 0.3mm with a median particle size of 0.2mm was adopted in this study, as shown in Fig. 2.2. Initially, approximately 29000 spherical particles

![](thesis/assets/media/image14.svg)

Fig. 2.2. Particle size distribution curve in the DEM analysis for Toyoura sand

were randomly generated in a cubic space enclosed by six frictionless flat wall elements. The length, width, and height of the cubic space are 0.005m, 0.005m, and 0.01m, respectively. The specimens used in the actual test device are mostly cubes with equal length, width, and height (Nakai et al., 1986; Ye et al., 2012; Yin et al., 2011). However, considering that the length of the major principal stress direction undergoes a significant reduction at the critical state, the initial axial length of the specimen is approximately set to be twice the width. The initial random spatial distribution of the particles leads to large overlaps between particles. To reduce the overlaps and relieve the initial interparticle force, a servo mechanism (Itasaca, 2005) was employed to displace the wall elements until the relatively small confining stress of 50 kPa was reached, and the initial void ratio for 50 kPa was 0.696 as shown in Fig. 2.3.

![](thesis/assets/media/image16.svg)

Fig. 2.3. Variation of void ratio under the isotropic compression

![图表 描述已自动生成](thesis/assets/media/image17.png)

Fig. 2.4. Specimen state after isotropic compression of p = 5.1 MPa

Subsequently, isotropic compression with gradually increasing confining stress was performed, during which three measurement ball function (Itasaca, 2005) with radii of 1.5 mm are positioned vertically inside the specimen to measure the void ratio. The measurement ball function is built into the program, which sets a spherical spatial domain for measurement and measures parameters such as void ratio, average stress, and coordination number for particles that exist within this domain. When measuring the average value of the void ratio in the domain, the obtained result can be regarded as the average void ratio at the center point of the domain. The stability of the stresses acting on the wall elements and the void ratio of the specimen served as the completion condition for each compression stage. The current compression stage was completed when stress and strain stabilized, and a quasi-static state was accordingly reproduced in the specimen. Figures 2.3 and 2.4 show the variation in the void ratio under isotropic compression and the specimen under a confining pressure of 5.1 MPa, respectively. Simulation by Cao et al. (2021) involved low confining pressures for consistency with laboratory tests. On the other hand, some simulations covered a wide range of confining pressures from tens kPa to tens MPa (ex., Huang et al., 2014a; Zhao and Guo, 2013). Moreover, the particle crushing was modeled by Zhu et al (2022) when the specimen was subjected to high confining pressure. Unlike these studies, this study aims to compare the mechanical behavior of theoretical spherical aggregates under a wide range of pressures. Thus, particle crushing is not considered. Isotropically compressed specimens under confining pressures of 0.7MPa, 1.4MPa, 1.9MPa, 2.6MPa, 3.7MPa, 5.1MPa, 7.0MPa, 9.7MPa, 13.5MPa, 18.7MPa, and 26.0MPa were selected for the subsequent shear tests under general stress states.

![图表, 雷达图 描述已自动生成](thesis/assets/media/image18.png)

Fig. 2.5. Loading paths in shear tests

### Shear process in the DEM simulation

During shearing, the Lode angle and the mean effective stress were maintained constant. Five loading paths corresponding to each mean effective stress state were considered: Lode angles of 60°, 75°, 90°, 105°, and 120° as shown in Fig. 2.5. Lode angle refers to the angle between the stress path and the axis of the principal stress in the stress state of a material. Lode angles of 60° and 120°indicate the triaxial extension and triaxial compression states, respectively. On the other hand, the stress path can also be described by using the intermediate principal stress ratio (*b* = (*σ~2~'*-*σ~3~'*)/(*σ~1~'*-σ~3~')), where *b*=0 for triaxial com-pression and *b*=1 for the triaxial extension. Typical boundaries in DEM triaxial tests include the nondeformable wall boundary (Zhao and Guo, 2013; Cao et al., 2021), the periodic boundary (Thornton, 2000; González-Montellano et al., 2011), and the membrane boundaries. Multiple membrane boundaries exist in DEM simulations. One of the membrane boundaries is implemented by applying additional force to the outmost particles (Cui et al., 2007; Cheung and O'Sullivan, 2008; O\'Sullivan and Cui, 2009). Another type of membrane boundary is modeled by assigning tensile and shear strength between the membrane particles (Kim and Park, 2020). Recently, a coupled FDM-DEM approach using the shell element was proposed to model the membrane boundary (Zhu et al., 2022). Although the wall boundary can effectively maintain the specimen symmetry under deformation, local deformation such as the shear band, which originates from irregular displacement on the deformable flexible boundary, is inhibited. In this study, the major and minor principal stresses were applied by wall element boundaries, and the membrane boundary with applied force was adopted in the intermediate principal stress direction, which is consistent with the apparatus developed by Nakai et al. (1986).

> ![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image19.png)
>
> Fig. 2.6. Membrane zone detection

The method for identifying the membrane particles is similar to that proposed by Cui et al. (2007) and only differs in coordinate transformation because the specimen in previous studies was a cylinder, whereas the specimen in this study is a cuboid. The boundary in the direction of intermediate principal stress, which serves as the membrane, was determined using the following procedure. As illustrated in Fig. 2.6, a membrane zone with a thickness of three times the mean particle diameter was designated from the outmost particle in the intermediate principal stress direction. The particles in the membrane zone were further identified depending on whether they were prevented from contact with the outside. Each particle in the membrane zone had a corresponding cone with its vertex coinciding with the center of the particle, as shown in Fig. 2.7. If no other particle is detected inside this conical region, this particle is in direct contact with the outside and is, consequently, identified as a membrane particle.

> ![图表, 表面图 描述已自动生成](thesis/assets/media/image20.png)
>
> Fig. 2.7. Membrane particle identification
>
> ![图片包含 文本 描述已自动生成](thesis/assets/media/image21.png)
>
> Fig. 2.8. Specimen after Membrane particle identification

Figure 2.8 shows the specimen after membrane particle identification in the DEM simulation. The yellow particles in this figure denote the membrane particles directly subject to the intermediate principal stress. The boundary stress was subsequently applied to each membrane particle in the form of applied forces for the coordinate axis. To obtain the applied force corresponding to each membrane particle, a two-dimensional Voronoi tessellation based on the membrane particle positions was employed.

![](thesis/assets/media/image23.svg)

Fig. 2.9. Voronoi geometry corresponding Membrane particles

![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image24.png)

Fig. 2.10. Boundary force application

Figure 2.9 illustrates the principle of the Voronoi polygon; the perpendicular bisectors between adjacent points (particle centers) partition the plane into cells corresponding to each point. The area of each cell is the corresponding area under force for each membrane particle. The applied force is calculated based on the corresponding area and the boundary stress as shown in Fig. 2.10. As the shear test proceeded, the non-fixed top and bottom of the specimen have different velocities in the *x*-direction and led to a bending moment acting on the specimen. Meanwhile, the cumulative displacement of membrane particles distorted the Voronoi polygon. Thus, as an additional constraint, two pairs of edges were installed in the *x*-direction as shown in Fig. 2.10. As the shear test proceeded, the non-fixed top and bottom of the specimen have different velocities in the *x*-direction and led to a bending moment acting on the specimen. Meanwhile, the cumulative displacement of membrane particles distorted the Voronoi polygon. Thus, as an additional constraint, two pairs of edges were installed in the *x*-direction as shown in Fig. 2.10. The velocities of the edges in the *y*-direction were fixed to zero, and the velocities in the *z*-direction were set to the same as the corresponding top or bottom rigid wall. Velocities of the top or bottom edges in the *x*-direction are in opposite directions and have the same magnitude to maintain the symmetry of the specimen to avoid the bending moment. On the other hand, the Voronoi tessellation was periodically updated to reflect the membrane deformation. To reduce the time consumption in updating the Voronoi polygon, it was updated every 100 cycles without renewing the membrane particles for computational efficiency. The membrane particles were redetected and reidentified only when the accumulative displacement exceeds 0.1 times the median diameter from the last update of the membrane particle.

## Results and discussion

### Relationship between deviatoric stress and strain

![](thesis/assets/media/image26.svg)

Fig. 2.11. Deviatoric stress and volumetric strain in shear test (*p* = 26.0 MPa)

Figure 2.11 shows the comparison of volumetric strain and deviatoric stress between different stress paths. A contraction before an expansion in volume is evident for all cases. After the axial strain increases to approximately 18%, the increase rate of volumetric strain reduced significantly and remained almost constant. Similarly, a hardening before a slight softening in deviatoric stress is observed in Fig. 2.11. Further, the deviatoric stresses in the five cases were steady beyond the axial strain of approximately 18%. Considering the convergence of the deviatoric stress and volumetric strain (i.e., steady state), states at the axial strain of 20% in this study were employed for the subsequent critical state analyses. The volumetric strains under the critical states exhibited apparent dependence on the loading paths: the volumetric strain gradually decreased as the Lode angle increased from 60° to 120°. On the other hand, there are some exceptions where a larger volumetric strain corresponds to a larger Lode angle, such as the cases with Lode angles of 60° and 75°. This error is attributed to the differences in deviatoric strain rates and measurement balls, which is discussed in the subsection on the critical state. Although some exceptions exist in the volumetric strain results under the critical states, the difference in volumetric strain between triaxial compression and triaxial extension is significant. Therefore, the volumetric strain is

![](thesis/assets/media/image28.svg)

> \(a\) Axial strain vs. deviatoric stress

![](thesis/assets/media/image30.svg)

> \(b\) Axial strain vs. void ratio

Fig. 2.12. Comparison of deviatoric stress and void ratio in tests with rigid and flexible boundary (*p'*=1.4MPa): (a) Axial strain vs. deviatoric stress, (b) Axial strain vs. void ratio

stress-path dependent. The deviatoric stresses under the critical states are markedly dependent on the stress paths: larger deviatoric stress corresponds to a larger Lode angle. Accordingly, the anisotropic failure criterion under the critical states was predictable from the deviatoric stress results under the critical states. Some experimental results (Ye et al., 2012; Yin et al., 2011) obtained using a true triaxial apparatus can serve as valuable evidence to validate the numerical simulation in this study.

Figure 2.12 compares the stress and void ratio variation between the true triaxial tests with and without flexible boundaries. In agreement with the findings of Cheung and O'Sullivan (2008) and Qu et al. (2019), the boundary type has little effect on the macroscopic response, such as deviatoric stress and void ratio. The changes in particle position after the application of membrane boundary could lead to an inevitable disturbance to the specimen and account for the slight difference in stress and void ratio. A shear band is a common form of highly localized deformation in ductile solids (Rice, 1976). It is more likely to develop in the middle of the specimen under a flexible membrane boundary, and through the entire specimen under a rigid boundary (Cheung and O'Sullivan, 2007; Qu et al., 2019, Kim and Park, 2020). The rotational velocity of particles could be employed as an indicator of the deformation localization of granular materials (Kim and Park, 2020). On the other hand, in the specimen under a rigid boundary, as shown in Fig. 2.13 (a), the particles with a relatively higher rotational angular velocity (over 100 rad/s) tended to concentrate in the middle part of the cross-section. The particles with high rotational angular velocities in the specimen under flexible boundary as shown in Fig. 2.13 (b) concentrated at the top left and lower right of the *x*-*z* cross-section. Bono et al. (2015) pointed out that the interparticle bonds contribute to the emergence of shear bands. In contrast, because a linear model without any bonds for modeling cohesionless sands was adopted in this study, it can be understood that the typical *x*-shaped shear bond was not observed.

![电脑合成图 低可信度描述已自动生成](thesis/assets/media/image31.png)

> \(a\) Rigid boundary

![墙上挂着一幅画 中度可信度描述已自动生成](thesis/assets/media/image32.png)

\(b\) Flexible boundary

Fig. 2.13. Comparison of particle rotational velocity between rigid boundary and flexible boundary under the critical state (compression, *p'*=1.4MPa): (a) Rigid boundary, (b) Flexible boundary

Two-hundred measurement balls with a radius of 0.5 mm were uniformly placed in the specimens with rigid and flexible boundaries along the x-direction to obtain the local void ratio. When distant from the boundaries, the local void ratio under the two boundaries is similar, whereas when close to the boundaries, the void ratio near the rigid boundary is almost always larger than that near the membrane boundary as shown in Fig. 2.14. The particles in contact with the rigid boundary are tightly attached to it, forming a constraint perpendicular to the rigid boundary. On the other hand, the

![](thesis/assets/media/image34.svg)

Fig. 2.14. Comparison of local void ratios between rigid and flexible boundaries under the critical state (*p'*=1.4MPa)

membrane boundary has no displacement constraints, and the membrane particles are only subjected to boundary forces. Therefore, the restricted particles produced larger local void ratios, and the local void ratio close to the rigid boundary is larger than that to the flexible boundary except for the result of the compression test at *x* = -0.002m, as shown in Fig. 2.14. In both triaxial compression and triaxial extension tests, because the rigid wall is close to the average position of the membrane particles, the rigid wall and the membrane boundary are not to be distinguished. In the compression test, the possible reasons for the similarity of the local void ratios between the two tests at *x* = -0.002m are considered to be the small size of the measurement balls and the fact that those are generated only at a height of *z* = 0.0m, which cannot completely and accurately evaluate the overall trend at different heights. However, in most cases, a larger local pore ratio near the rigid boundary could be observed. Notably, in the triaxial extension test, the membrane was subjected to a larger intermediate principal stress (*σ~1~'* = *σ~2~'*) than that in the triaxial compression test (*σ~2~'* = *σ~3~'*). Thus, the dimension in *σ~2~'* direction in the triaxial extension test was smaller after shearing, and a narrower range of local void ratio distribution was given.

Although the boundary type has little effect on the macroscopic behaviors, such as the strength, it affects the distribution and rotational velocities of particles and results in fabric variation near the boundary. Considering that the boundary in the intermediate principal stress direction produces the maximum area, especially in the extension test, it is preferable to design a flexible boundary to reduce its influence on the fabric.

The relationship between the angle of shearing resistance (*ϕ'~cs~=arcsin*((*σ~1~'*-*σ~3~'*)/(*σ~1~'*+*σ~3~'*))) and intermediate stress ratio (*b*=(*σ~2~'*-*σ~3~'*)/(*σ~1~'*-*σ~3~'*)) under peak and critical stress states has been widely studied using DEM (Thornton, 2000; O\'Sullivan et al., 2013; Huang et al., 2014a) and the results analyzed and compared with several typical failure criteria. The maximum of *ϕ'~cs~* in those studies was observed when the intermediate stress ratio (*b*) is between 0.2 and 0.6. The lateral support provided by the intermediate principal stress to the major principal stress presumably restricts the buckling of the force chain and accounts for the sensitivity of *ϕ'~cs~* to *b* (O\'Sullivan et al., 2013). The Ogawa and Lade criterion, which predicts a higher shear resistance angle for triaxial extension (*b*=1.0) than triaxial compression (*b*=0), agreed with a previous study (Huang et al., 2014a). Still, the failure criterion with varying mean effective stress has not been sufficiently discussed.

In this study, the results on the angle of shearing resistance (*ϕ'~cs~*) are compared with those of the Matsuoka-Nakai (Matsuoka and Nakai, 1974), Lade (Lade and Duncan, 1975), and Mohr-Coulomb criteria, expressed as Eqs. (2-1), (2-2), and (2-3), respectively.

![](thesis/assets/media/image35.wmf) (2-1)

![](thesis/assets/media/image36.wmf) (2-2)

![](thesis/assets/media/image37.wmf) (2-3)

where *σ~1~'*, *σ~2~'*, and *σ~3~'* are the maximum and intermediate, and minimum principal stresses; *η~Matsuoka-Nakai~* is the Matsuoka--Nakai criterion, *η~Lade~* is the Lade criterion, and *η~Mohr-Coulomb~* is Mohr--Coulomb criterion.

> ![](thesis/assets/media/image39.svg)

Fig. 2.15. Sensitivity of angle of shearing resistance to intermediate stress ratio at the critical states

The parameters in the three equations were obtained via regression analysis, and the results are shown in Fig. 2.15. The peak of *ϕ'~cs~* is obtained when *b*$\ $is between 0.2 and 0.6 for all cases in this study. Unlike the results by Huang et al. (2014a), the Matsuoka-Nakai criterion, which predicts an equivalent angle of shearing resistance (*ϕ'~cs~*) in triaxial extension (*b*=1.0) and compression (*b*=0.0) with a minimum deviation of 0.004, is generally consistent with all data. At low mean effective stress, *ϕ'~cs~* in the triaxial extension (*b*=1.0) is slightly higher than that in the triaxial compression (*b*=0.0), making the Lade criterion preferable. On the other hand, the increasing mean effective stress *p'* leads to a higher *ϕ'~cs~* in triaxial compression and a lower *ϕ'~cs~* in other stress paths, which is more consistent with the Matsuoka-Nakai criterion, or even the Mohr-Coulomb criterion. The stress states and failure surface are shown in Fig. 2.16. Notably, the stress state under a mean effective stress *p'* with a medium magnitude of approximately 10 MPa exhibits the greatest consistency with the Matsuoka-Nakai criterion. Other studies were inconclusive due to a narrow range of mean effective stress *p'*.

> ![图表, 图示 描述已自动生成](thesis/assets/media/image40.png)

Fig. 2.16. Critical stress state and Matsuoka-Nakai criterion in stress space

### Critical state line of void ratio

Li and Wang (1998) proposed a scaling method employing a power function to obtain a linear relationship between void ratio and mean effective stress (*p'*) under a steady state. In this study, the CSL in the *e* -- *p'* space was rescaled with the method shown in Fig. 2.17. The index applied for Toyoura sand was 0.7 based on the research conducted by Huang et al (2014a). Noticeably, $e$ increases with increasing *p'* when *p'* is low, which corroborates the findings of Huang et al (2014b). According to their studies, a large friction coefficient, such as 0.5, as used in this study, may lead to an anomalous variation trend of the CLS in the *e*-*p'* space when *p'* is small. The uniqueness

![](thesis/assets/media/image42.svg)

Fig. 2.17. Critical states in ![](thesis/assets/media/image43.wmf) space

and non-uniqueness of the void ratio under critical states can be a controversial topic: the uniqueness of the CSL for the void ratio is observed in some studies (Zhao and Guo, 2013), whereas in other studies, the CSL for the void ratio exhibits dependency on the stress path, and the uniqueness of the void ratio is attributed to a low contact stiffness (Huang et al., 2014a). The results reported herein reveal that dependency of the CSL on the stress path was drawn for different mean effective principal stresses *p'*, as shown in Fig. 2.17. The void ratio of the intermediate Lode angle is larger than the triaxial extension or less than the triaxial compression in some exceptions for other *p'* values. Presumably, the constant axial velocity could lead to a larger deviatoric strain ratio in cases with a smaller Lode angle, resulting in a more intensive fluctuation in the void ratio. Meanwhile, the void ratio was obtained using three measurement balls, contributing to the fluctuation in the void ratio during the shear tests because the location of the center of the ball---whether within the measurement sphere surface---affects the calculated porosity. Thus, those fluctuations cause some CSL exceptions. Although they exist in the critical state, the *e* gap between triaxial compression and triaxial extension is great, and sufficient and explicit evidence exists to support the CSL dependency on the stress path in the *e* -- *p'* space.

### Critical state line of coordination number

The coordination number $Z$, unlike the void ratio, which macroscopically describes the compactness, is a scalar for evaluating the microstructure compactness in granular materials and is defined as the average contact number per particle in Eq. (2-4).

$Z = \frac{2N_{c}}{N_{p}}$ (2-4)

where $Z$ is the coordination number, $N_{c}$ is the total number of contacts between particles, and $N_{p}$ is the number of particles.

![](thesis/assets/media/image45.svg)

Fig. 2.18. Variation of coordination number ($Z$) for Lode angle in the shear process (*p* = 7.0 MPa)

![](thesis/assets/media/image47.svg)

Fig. 2.19. Variation in coordination number (CN) for Lode angle at the critical state

The variation in $Z$ during the shear test under the mean effective stress of 7.0 MPa is presented in Fig. 2.18. A significant decrease before a slight increase and a steady state after the axial strain of 10% can be observed. In the steady state, $Z$ is not sensitive and exhibits no clear dependence on the stress paths. In the $Z$ -- $p'$ space at the critical state, a unique $Z$ CSL is prominent, indicating that $Z$ is independent of the stress paths at the critical state as shown in Fig. 2.19. Although the CN microscopically reflects the isotropic compactness of granular materials, it does not represent their structural anisotropy and directionality (Stershic et al., 2015). Thus, $Z$ is not sufficient for elucidating the soil structure.

### Critical state line of anisotropic fabric

The fabric tensor (*Φ~ij~*) is a classical method pioneered by Satake (1982) and Kanatani (1984) and has been frequently employed to describe granular structure anisotropy. The anisotropic fabric tensor (*F~ij~*) as shown in Eq. (2-6) is the deviatoric part of *Φ~ij~*. Notably, an invariant of anisotropic fabric (*F~c~*) in this study differs from that of the aforementioned studies and is related to multiples of the results in the study by Zhao and Guo (2013). In particular, the same value of *Φ~d~* was applied for comparison with the results of Huang et al. (2014a).

![](thesis/assets/media/image48.wmf) (2-5)

![](thesis/assets/media/image49.wmf) (2-6)

![](thesis/assets/media/image50.wmf) (2-7)

where *Φ~ij~* is the fabric tensor, *N~c~* is the total contact number between particles, *F~ij~* is the anisotropic fabric tensor, *δ~ij~* is the Kronecker delta, *n~i~* is the unit direction vector that joins the centroids of two particles in contact, and *F~c~* is the degree of anisotropy in granular materials and refers to the second invariant of *F~ij~*.

![](thesis/assets/media/image52.svg)

\(a\) Results in this study

![](thesis/assets/media/image54.svg)

\(b\) Results obtained from Huang et al. (2014a)

Fig. 2.20. Comparison of invariant of anisotropic fabric (*F~c~*) at critical state: (a) Results in this study, (b) Results obtained from Huang et al. (2014a)

Figure 2.20 presents the comparison between the results of *F~c~* in this study and *Φ~c~* in the study by Huang et al (2014a). Here, VC, VE, and HE indicate vertical compression, vertical extension, and horizontal extension under constant-$p'$ conditions, respectively. The results from both studies (i.e., the datasets in this and the study by Huang et al. (2014a)) exhibit a similar trend: fabric anisotropy decreases with increasing *p'*. However, in the latter, an increasing *p'* distinguishes the anisotropy of different stress paths, and the fabric anisotropy at the critical state converged to an equivalent value when *p'* was low, which did not occur in this study. The larger CN under a higher *p'* was considered able to interpret the decrease of *F~c~*: the higher *p'* leads to more contacts on one particle and less room for the particles around that particle to redistribute from an isotropic state to an anisotropic state and thereby lower anisotropy in the critical state. The critical fabric anisotropy of a compression test is always lower than that of an extension test under the same mean effective principal stress in both studies. The contact evolution is discussed, and the trend of *F~c~* is explained with the contact orientation in the next subsection.

### Contact orientation

A contact density rose diagram is proposed as a straightforward representation of the distribution in this study.

$E(\theta,\ \ \phi) = N_{\theta,\phi}|n_{c} \in \frac{\lbrack\theta,\theta + \delta\theta) \cap \lbrack\phi,\ \phi + \delta\phi)}{N_{c}\int_{\phi}^{\phi + \delta\phi}{\sin(\phi)d\phi}\int_{\theta}^{\theta + \delta\theta}{d\theta}}$ (2-8)

$\rho_{c}(\theta,\phi) = \frac{2E(\theta,\phi)N_{c}}{N_{p}}$ (2-9)

where E is the probability density function of contact, $N_{\theta,\phi}$is the number of contacts with normal falling in the interval \[θ, θ + δθ)∩\[ϕ, ϕ + δϕ), $N_{c}$ corresponds to the number of total contacts, the contact density, $N_{c}$ is the total contact number between particles, and $N_{p}$is the number of particles.

![图片包含 名片, 游戏机 描述已自动生成](thesis/assets/media/image55.png)

Fig. 2.21. Unit sphere for contact classification

Figure 2.21 shows a unit sphere with a radius of 1.0 separated into grids every 10° of latitude and longitude for classifying contacts in different directions. The area and number of contacts located in one grid vary with latitudes and longitudes; therefore, contact density (*ρ~c~*) was applied to normalize and visualize the contact characteristics. A probability density function (*E*) was proposed by Rothenburg and Bathurst (1989), as given in Eq. (2-8), and 10° of δ*θ* and δ*ϕ* were applied in this study. Notably, the integral following the number of total contacts (*N~c~*) in the denominator in Eq. (2-8) is the area of each grid, and it differs from the original form given by Rothenburg and Bathurst (1989): it is in a three-dimensional case. In contrast to the contact probability density function ($E$), the contact density ($\rho_{c}$) is defined in Eq. (2-9), indicating that the number of contacts per unit area on the unit sphere for a single particle is the product of $E$ and 2$N_{c}$/$N_{p}$ ($Z$), where *N~c~* and *N~p~* denote the total number of contacts and particles in the granular material. It also differs from the form provided by Huang et al (2014a) because it is normalized by counting the total number of particles and is independent of the number of particles within the granular assemblage.

By modifying $E$ to $\rho_{c}$, both the anisotropies of contact distribution and the evolution of $Z$ induced by compactness or shear can be represented. For instance, in an undrained test, the $Z$ changes dramatically. However, although $E$, with its integral over the unit sphere surface is 1.0, is mathematically elegant, it can scarcely reflect the variation in isotropic quantities, such as $Z$. The other forms by Huang et al (2014a) are not able to evaluate different granular systems with various particle numbers. $\rho_{c}$ indicates the mathematic expectation of contact number in different directions per unit area for each particle. It represents the contact distribution characteristics and the trend of changes in the number of contacts and is independent of the number of particles.

The morphological evolution of contact density during the compression test under the mean effective stress of 5.1MPa is shown in Fig. 2.22. Here, Figures 2.22(a)\~(d) correspond to the axial strains of 0%, 2%, 5%, and 20%, respectively. The contact density distribution at the axial strain of 0% is almost a sphere with a mean density of approximately 0.3445, which indicates an isotropic state in the fabric. As the strain and stress develop, the contact density gradually evolves toward the direction of the major principal stress. At the axial strain of 2%, the morphology evolves into an ellipsoid with a mean density of 0.3940 and 0.2919 in the direction of *σ~1~'* (0^o^ \< *ϕ* \< 20^o^) and *σ~3~'/σ~2~'* (80^o^ \< *ϕ* \< 100^o^), respectively. This indicates a slight concentration of interparticle contacts in the direction of *σ~1~'* and fabric anisotropy. On the other hand, when the major principal strain exceeds 5%, the mean density in the direction of *σ~1~'* increases to 0.4143, and the mean density in the direction of *σ~3~'/σ~2~'* decreases to 0.2716. This indicates a more significant concentration of interparticle contacts. The contact density at the axial strain of 20% in the critical state exhibits the greatest fabric anisotropy: a mean density of 0.4009 in the direction of *σ~1~'* and 0.2385 in the direction of *σ~3~'/σ~2~'*. The mean contact density in the direction of *σ~1~'* under the critical state was slightly lower than that when

+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ![卡通人物 中度可信度描述已自动生成](thesis/assets/media/image56.png) | ![图片包含 文本 描述已自动生成](thesis/assets/media/image57.png)     |
+:=================================================================================================================================:+:================================================================================================================================:+
| \(a\) ε~a~=0%                                                                                                                     | \(b\) ε~a~=2%                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ![卡通人物 中度可信度描述已自动生成](thesis/assets/media/image58.png) | ![卡通人物 中度可信度描述已自动生成](thesis/assets/media/image59.png) |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| \(c\) ε~a~=5%                                                                                                                     | \(d\) ε~a~=20%                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Fig. 2.22. Distribution of contact density (*ρ~c~*) at different axial strain in compression test: (a) ε~a~=0%, (b) ε~a~=2%, (c) ε~a~=5%, (d) ε~a~=20%                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

the axial strain *ε~1~* is 5%, however, the lower contact density in the direction of *σ~3~'/σ~2~'* resulted in greater fabric anisotropy in the critical state. Furthermore, at the critical state, the morphology of contact density was an elongated cylinder with a contracted body and *z*-axis oriented to the direction of major principal stress. Thus, the consistency of microstructure with macroscopic stress was verified in the triaxial compression test. The distribution morphology evolution of the contact density also implies a variation in the magnitude of *F~c~*. A greater difference between the anisotropic morphology and an isotropic sphere indicates a higher degree of anisotropy and a larger *F~c~*. Therefore, the evolution of the contact distribution morphologically estimates the gradual increase of *F~c~* in the triaxial compression test.

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![卡通人物 中度可信度描述已自动生成](thesis/assets/media/image60.png) | ![卡通人物 中度可信度描述已自动生成](thesis/assets/media/image61.png) |
+:=================================================================================================================================:+:=================================================================================================================================:+
| \(a\) *θ*=120°                                                                                                                    | \(b\) *θ*=90°                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![图片包含 图表 描述已自动生成](thesis/assets/media/image62.png)      |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| \(c\) *θ*=60°                                                                                                                     |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Fig. 2.23. Comparison of the distribution of contact density (*ρ~c~*) for shear tests with different Lode angles at the critical state: (a) *θ*=120°, (b) *θ*=90°, (c) *θ*=60°                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The distributions of contact density for tests with Lode angles of 120°, 90°, and 60° are illustrated in Fig. 2.23, considering the uniqueness of $Z$ and nonuniqueness of *F~c~* and $e$ in tests with different Lode angles at the critical state under the same mean effective principal stress. In contrast to the compression test (*θ* = 120°), the morphology of contact density in the extension test (*θ* = 60°) was a dimpled flat pie with a concave oriented toward the direction of the minor principal stress. The contact density distribution for a Lode angle of 90° is an intermediate transition state. The contact density distribution microscopically reveals the intrinsic difference in critical states under different stress paths and is indicative of the anisotropy in the void ratio and fabric tensor. Although the CSL of $Z$ is uniquely presented, the contact anisotropy varies with the Lode angle, resulting in the *F~c~* and void ratio (*e*) of the triaxial extension being greater than that in the triaxial compression.

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![卡通人物 中度可信度描述已自动生成](thesis/assets/media/image63.png) | ![卡通人物 中度可信度描述已自动生成](thesis/assets/media/image60.png) |
+:=================================================================================================================================:+:=================================================================================================================================:+
| \(a\) *p'*= 1.9 MPa                                                                                                               | \(b\) *p'*= 5.1 MPa                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![卡通人物 描述已自动生成](thesis/assets/media/image64.png)           |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| \(c\) *p'*= 26.0 MPa                                                                                                              |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Fig. 2.24. Comparison of the distribution of contact density (*ρ~c~*) between triaxial compression tests with different mean effective principal stresses: (a) *p'*= 1.9 MPa, (b) *p'*= 5.1 MPa, (c) *p'*= 26.0 MPa                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Figure 2.24 compares the distribution of contact density of triaxial compression tests under different mean effective principal stress. The morphologies of those tests were all elongated columns with a contracted body, and the contact density was generally greater under larger effective stress, which further confirms the CSL trend of CN. However, contact density growth away from the direction of the major principal stress is more significant. For instance, as the mean effective principal stress increases from 1.9 MPa to 5.1 MPa, the contact density in the direction of minor principal stress (mean value for 80^o^ \< *ϕ* \< 100^o^) increases from approximately 0.19 to 0.24, whereas the contact density in the direction of major principal stress (mean value for 0^o^ \< *ϕ* \< 20^o^) increases from 0.37 to 0.40. Thus, the growth difference in different directions leads to a reduction in the fabric anisotropy, validating a decreasing *F~c~* with a growing *p'*.

The gradation and geometry of the aggregates set the upper bound of the contact density. A comparison of the two cases under mean effective principal stresses of 5.1 MPa and 26.0 MPa indicates that an increase in the mean effective principal stress does not contribute to a significant increase in the contact density in the direction of the major principal stress *σ~1~'*. On the other hand, an increase in the contact density was observed in neighboring directions around the direction of *σ~1~'*. Thus, when a specimen is sheared from an isotropic state under great confining stress, the particles are redistributed, and the interparticle contacts tend to be concentrated in the direction of *σ~1~'*. However, the particles interact and cannot overlap with each other, forcing the interparticle contacts to be redistributed to the neighboring directions and resulting in a geometry-limited finite contact density in one direction. Thus, the contact densities in the neighboring directions become greater. Compared to the increase in contact density in the direction of the major principal stress *σ~1~'*, the increase of contact density in the neighboring directions has little contribution to *F~c~* when the mean stress is large. Accordingly, *F~c~* decreases at the critical state when *p'* is relatively high.

## Summary

In this chapter, three-dimensional DEM analyses were performed for 51 cases of true triaxial tests subjected to hybrid (i.e., rigid and flexible) boundary conditions under a constant mean principal stress with varying Lode angles. The cuboid specimen was made of approximately 29000 ball elements with a flexible boundary using membrane particles. The stress ratios and void ratios under the critical states were presented and compared for different stress paths. The uniqueness of the coordination number and nonuniqueness of void ratio and invariant of anisotropic fabric tensor under the critical state were examined based on the contact density. The following conclusions were derived.

(1) To obtain the applied force corresponding to each membrane particle in DEM analyses for true triaxial tests in this study, a two-dimensional Voronoi tessellation based on the membrane particle positions was employed. The obtained results indicated that the rigid boundary has little influence on the macroscopic mechanical behavior. However, the rigid boundary affected the particle rotation and restricts the particle distribution, producing larger local void ratios close to it.

(2) Mohr--Coulomb, Lade, and Matsuoka--Nakai failure criteria were examined by considering the resistance angle for the critical state. The analytical results indicate that the Matsuoka--Nakai, Lade, and Mohr--Coulomb criteria correspond to fitting residuals of 0.004, 0.013, and 0.018, respectively. Thus, the Matsuoka--Nakai criterion exhibited the closest match to the obtained results. However, the Matsuoka--Nakai Criterion was inappropriate when the specimen was subjected to too large or small mean effective stress.

(3) The uniqueness of the CSL in the $e$-$p'$ space was examined. No unique CSL in the *e* - *p* space was observed, and the void ratio under the critical state exhibited dependence on the intermediate principal stress ratio. On the other hand, an apparent unique CSL existed in the $Z$ -- $p'$ space, indicating that $Z$ is independent of the intermediate principal stress ratio. *F~c~* under the critical state was investigated in the $F_{c}$ -- $p'$ space, where $F_{c}$ decreases with increasing $p'$ and Lode angle.

(4) A method to quantitatively characterize the distribution of contact for granular material is proposed. Unlike in previous studies, an intuitive equiangular partition was adopted, and the contact density was newly recommended as the product of the probability density function (*E*) and $Z$. The contact density revealed that the number of contacts per unit area for a single particle is indicative of the variation in coordination number. Moreover, it avoids the influence of the total number of particles in a specimen. Using this visualization method, the contact distribution characteristics in the true triaxial shear tests with different Lode angles were clarified. The contact density distribution of triaxial compression changed, becoming an elongated cylinder with a contracted body whose long axis pointed in the direction of the major principal stress. In contrast, the contact density distribution of the triaxial extension appeared as a dimpled flat pie with the concave oriented toward the direction of the minor principal stress. The distributions of the in-between paths were transition states between triaxial compression and extension.

(5) The difference in the morphologies of contact density microscopically accounted for the uniqueness of CSL in the $Z$-- *p'* space and the nonuniqueness of CSL in the $e$ -- $p'$ space. The pie-like distribution in triaxial extension resulted in a larger void ratio than that of the cylindrical distribution in triaxial compression, despite the coordination number under the equal mean principal effective stress being the same. The comparison of contact density between the different $p'$ values revealed the reason for a lower $F_{c}$ with increasing $p'$. In the critical states, it was found that the increment in $p'$ led to a greater increase in the contact density in the direction of minor principal stress than that of the major principal stress, resulting in a decrease in the fabric anisotropy.

# Study on Factors Affecting Liquefaction Resistance during Anisotropic Consolidation

This chapter employs DEM to investigate the effects of stress anisotropy on liquefaction resistance of sand soils through undrained cyclic shear simulations. A combined servo mechanism replicates undrained conditions and stress states in hollow cylinder apparatus (HCA) tests. The influence of lateral to vertical stress ratios ($K_{0}$), as well as the stress path for specimen preparation, on the soil\'s response to cyclic loading are examined across a wide range of $K_{0}$ values from 0.33 to 3.33. Results demonstrate that increasing stress anisotropy reduces liquefaction resistance and the stress path, whether through initial isotropic consolidation followed by linear anisotropic consolidation (IC-AC) or initial isotropic consolidation followed by constant-$p'$ triaxial shear (IC-AC-TS), does not significantly affect liquefaction resistance. The factors that influence liquefaction resistance are attributed to changes in both macroscopic and microscopic quantities, such as relative density and coordination number ($Z_{m}$). Anisotropic consolidation states with $K_{0}$\<1.0 or $K_{0}$\>1.0 produce different morphologies of contact density, affecting fabric anisotropy and liquefaction resistance.

##  Introduction

The phenomenon of liquefaction, which occurs with the loss of soil strength due to the buildup of pore water pressure during an earthquake, has been recognized for its potential to cause severe damage to infrastructure and buildings (Ishihara and Koga, 1981; Seed and Idriss, 1967). Triaxial tests have been extensively conducted to elucidate the mechanisms of liquefaction, where saturated specimens were subjected to cyclic loading under undrained conditions until liquefaction was triggered. The influence of factors such as cyclic stress ratio (CSR), relative density, as well as confining pressure on the resistance to liquefaction was examined (Hyodo et al., 1991; Seed and Lee, 1966; Silver et al., 1976; Toki et al., 1986; Yoshimi et al., 1984). However, vertically propagating shear waves in the ground apply gradually varying shear stress on soil elements, leading to a continuous rotation of principal stress axes (Arthur et al., 2009; Arthur et al., 1980; Ishihara and Yasuda, 1975; Ishihara and Towhata, 1983; Yamashita and Toki, 1993).

Alternative testing methods, such as the hollow torsional shear test, apply shear forces to specimens, allowing for continuous variation of principal stress axes and thereby addressing the limitations of the triaxial test. Ishihara and Yasuda (1975) pioneered the utilization of hollow torsional cylindrical apparatus (HCA) by subjecting the hollow cylindrical samples to irregular wave loading, studying the disparities compared to triaxial shear tests. Tatsuoka et al. (1986) performed both triaxial and torsional tests on specimens prepared using different methods and found that the results were inconsistent between the triaxial and torsional tests. Torsional and triaxial shear tests conducted by Yamashita and Toki (1993) and employed by Oka et al. (1999) to enhance the constitutive model for liquefiable sands also demonstrated that method of testing with torsional or triaxial shear, influences the results of liquefaction resistance. These studies highlight the significance of experimental methods, such as HCA tests, in liquefaction analyses and aroused great interest in numerical replication of these tests.

Soils under a natural state generally display various ratios of lateral to vertical effective stress, denoted as $K_{0}$. The impact of $K_{0}$ values on liquefaction strength frequently garners attention, yet the corresponding findings remain controversial. Ishihara and Takatsu (1979) observed that the liquefaction strength of Fuji River sand does not exhibit a notable dependency on the initial stress state with different $K_{0}$ values. Similar results were also obtained in the laboratory tests conducted by Yamashita and Toki (1993). On the other hand, the hollow torsional experiments conducted by Georgiannou and Konstadinou (2014) indicated that isotropically consolidated (IC) specimens demonstrate higher liquefaction resistance for loose sands than anisotropically consolidated (AC) specimens. By contrast, that pattern did not hold in dense states, where increasing relative density reversed the trend. Additionally, Vargas et al. (2020) concluded from similar laboratory tests on Ottawa sand with relative densities ranging from 50% to 80% that AC specimens with a $K_{0}$ of 0.5 showed a liquefaction strength approximately 20% higher than IC specimens. The experimental conclusions regarding the influence of $K_{0}$ on liquefaction resistance have been debated for decades, underscoring the necessity of elucidating $K_{0}$ effects on liquefaction resistance through alternative means. Additionally, the previous studies mentioned above focus primarily on a narrow range of initial states, typically involving $K_{0}$ values of 0.5, 1.0, and 2.0, without exploring a wider range of $K_{0}$.

The discrete element method (DEM) (Cundall and Strack, 1979) simulation provides an insight into granular material and offers advantages by eliminating concerns related to variations in initial states caused by sample preparation, making it a desirable numerical method to study the cause of changes in liquefaction resistance. Numerous examples utilizing DEM exist for undrained cyclic shear tests to find explanations of microscopic factors affecting liquefaction resistance. Huang et al. (2018) conducted undrained shear tests on triaxial specimens, trying to relate monotonic and cyclic behaviors. Yang et al. (2021) performed undrained simple shear tests and studied the influence of multi-directional shear stress on liquefaction resistance. Jiang et al. (2021) applied various forms of strain waves to specimens, investigating their impact on liquefaction resistance. Morimoto et al. (2021) examined the impact of pre-shearing on the liquefaction resistance using DEM simulation of undrained triaxial cyclic shear tests. Xie et al. (2023), as well as Yang and Huang (2023) explored the effect of liquefaction history-induced fabric on liquefaction resistance by conducting reliquefication simulation. Zhang et al. (2023) arranged ellipsoidal clumped pebbles and applied both vertical and horizontal shear loading in to discuss the influence of inherent fabric anisotropy on liquefaction resistance. Some of these studies included triaxial specimens, which do not account for principal stress axis rotation. Others utilized virtual periodic boundaries or cubic rigid box, which are difficult to implement in real-world scenarios. Replicating HCA tests through simulation provides a meaningful connection between numerical and experimental methods.

Using DEM to replicate HCA test is relatively specialized, but still has precedents. Li et al. (2014) conducted DEM simulations of drained tests and investigated the strain localization in HCA test. Liu et al. (2021) conducted analysis of torsional shear tests under drained conditions and investigated the development of cracks at different principal stress rotation angles. This study introduced an algorithm that realizes both undrained and stress conditions in HCA test, filling a gap in HCA simulation using DEM (Ma et al., 2024).

To clarify the influence of the $K_{0}$ on liquefaction resistance, Yang and Taiebat\'s (2024) consolidated specimens with different preparation methods and conducted undrained cyclic shear tests. They found that both preparation protocols and $K_{0}$ influence liquefaction resistance. As the relative density increased, the difference in liquefaction resistance narrowed gradually for IC and AC states. Otsubo et al. (2022) employed $K_{0}$ to induce inherent fabric anisotropy in specimen under a low stress condition and then consolidated it to the target $p'$ and examined its effects on liquefaction resistance. A specimen with higher anisotropy has weaker stiffness in its minor direction and resulted a lower liquefaction resistance. Still, $K_{0}$ values discussed in the mentioned numerical studies lie in a limited range. For instance, comparison between $K_{0}$=1.0 and $K_{0}$=0.5 (Yang and Taiebat\'s, 2024) or from $K_{0}$=0.75 to $K_{0}$=1.35 (Otsubo et al., 2022), and exploration beyond these thresholds is lacking.

The stress paths for specimen preparation often entail linearly increasing $p'$ and $q$ to the state with target $K_{0}$ in both experimental (Vargas et al., 2020) and numerical (Yang and Taiebat, 2024) tests, thereby intriguing further investigation into the effects of stress paths by incorporating other consolidation stress paths. This study demonstrates DEM analysis of cyclic undrained HCA tests (Ma et al., 2024) and explores the effects of $K_{0}$ on liquefaction resistance. Specimens are prepared with two different stress paths in consolidation and subjected to an extensive range of cyclic shear stress ratios. By examining macroscopic and microscopic responses such as fabric evolution, this study aims to provide evidence that elucidates how stress anisotropy influences liquefaction resistance.

## DEM simulation setup

### Specimen preparation

Itasca PFC^3D^ (Itasca Consulting Group, Inc., 2021) was employed to implement DEM simulations of undrained cyclic torsional shear test. Unlike the periodic boundaries commonly used in element tests, the HCA in DEM simulation employs two cylinders, upper and lower planes, as well as six blades to provide torsional force, closely approximating the boundary conditions of HCA (Ishihara and Yasuda, 1975; Vargas et al., 2020; Li et al, 2014; Liu et al, 2021). As shown in Fig. 3.1(a), two rigid cylindrical walls with inner diameter of 6 cm and outer diameter of 10 cm are positioned coaxially and vertically, with the upper and lower planes placed 10 cm apart, resembling the geometric dimensions of laboratory tests (Vargas et al., 2020).

![图片包含 应用程序 描述已自动生成](thesis/assets/media/image65.png)

(a) Pouring method for generating particles

![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image66.png)

(b) Insertion of torsional blades

Fig. 3.1. Specimen generation process in the initial stage using the pouring method and insertion of torsional blades

This research employed a uniform particle size distribution ranging from 1.5 mm to 3.0 mm, and utilizes a rolling resistance contact model (Iwashita and Oda, 1998; Wensrich and Katterfeld, 2012) to mimic the non-spherical effects of sand particles. The specific parameters of the contact model are listed in Table 3-1. To ensure similarity with laboratory methods, the particles were initially generated in the upper part of the apparatus and then allowed to flow downward under the influence of gravity, forming the specimen as shown in Fig. 3.1(a). The stress calculations of HCA are summarized according to the formulas provided in Table 3-2 ,where the values of $\sigma_{z}$ and $\sigma_{\theta}$ are derived from the equilibrium relations, $\varepsilon_{z}$ and $\gamma_{z\theta}$ are based on strain compatibility, and the remaining stress and strain expressions align with the assumption of linear elasticity (Hight et al., 1983).

Table 3-1. Parameters in DEM simulation

  ------------------------------------------------------------------------------------------
  Description                                                               Value
  ------------------------------------------------------------------------- ----------------
  Number of particles $N_{p}$                                               40,249

  Density, $\rho_{s}$ (kg/m3)                                               2650

  Young's modulus, $E$ (GPa)                                                0.3

  Normal-to-shear stiffness, $\kappa$                                       2.0

  Tangential frictional coefficient between particles, $\mu_{pp}$           0.0\*/0.50\*\*

  Tangential frictional coefficient between particle and wall, $\mu_{pw}$   0.0

  Normal critical damping ratio, $\beta_{n}$                                0.7

  Shear critical damping ratio, $\beta_{s}$                                 0.5

  Rolling friction coefficient, $\mu_{r}$                                   0.1
  ------------------------------------------------------------------------------------------

\*IC

\*\* Generation, AC, TS, and Cyclic shear

The typical approach of applying shear force to cuboidal (Wei et al., 2020; Yang et al., 2021; Banerjee et al., 2023) or cylindrical (Li et al., 2014; Liu et al., 2021) elements involves selecting and regulating the flexibility of the particles on both sides of the specimen. However, this method for providing torque on HCA specimens raises concerns, as the selected and constrained particles interfere with the cylinders' expansion or contraction, affecting the measurement of radial stresses. Therefore, using

Table 3-2. Equations of stress and strain in the HCA

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Description       Stress                                                                                                                                            Strain
  ----------------- ------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Vertical          $$\sigma_{z} = \frac{W}{\pi\left( R^{2} - r^{2} \right)}$$                                                                                        $$\varepsilon_{z} = - \frac{H - H_{0}}{H_{0}}$$

  Inner             $$p_{i} = \Sigma\sqrt{{f_{pw_{x}}^{i}}^{2} + {f_{pw_{y}}^{i}}^{2}}$$                                                                              

  Outer             $$p_{o} = \Sigma\sqrt{{f_{pw_{x}}^{o}}^{2} + {f_{pw_{y}}^{o}}^{2}}$$                                                                              

  Circumferential   $$\sigma_{\theta} = \frac{p_{o}R - p_{i}r}{R - r}$$                                                                                               $$\varepsilon_{\theta} = - \frac{u_{o} + u_{i}}{R + r}$$

  Radial            $$\sigma_{r} = \frac{p_{o}R + p_{i}r}{R + r}$$                                                                                                    $$\varepsilon_{r} = - \frac{u_{o} - u_{i}}{R - r}$$

  Shear             $$\tau_{z\theta} = \frac{3M_{T}}{2\pi\left( R^{3} - r^{3} \right)}$$                                                                              $$\gamma_{z\theta} = \frac{\theta(R^{3} - r^{3})}{3H\left( R^{2} - r^{2} \right)}$$

  Major             $$\sigma_{1} = \frac{\sigma_{z} + \sigma_{\theta}}{2} + \sqrt{\left( \frac{\sigma_{z} - \sigma_{\theta}}{2} \right)^{2} + \tau_{z\theta}^{2}}$$   $$\varepsilon_{1} = \frac{\varepsilon_{z} + \varepsilon_{\theta}}{2} + \sqrt{\left( \frac{\varepsilon_{z} - \varepsilon_{\theta}}{2} \right)^{2} + \left( \frac{\gamma_{z\theta}}{2} \right)^{2}}$$

  Intermediate      $$\sigma_{2} = \sigma_{r}$$                                                                                                                       $$\varepsilon_{2} = \varepsilon_{r}$$

  Minor             $$\sigma_{3} = \frac{\sigma_{z} + \sigma_{\theta}}{2} - \sqrt{\left( \frac{\sigma_{z} - \sigma_{\theta}}{2} \right)^{2} + \tau_{z\theta}^{2}}$$   $$\varepsilon_{3} = \frac{\varepsilon_{z} + \varepsilon_{\theta}}{2} - \sqrt{\left( \frac{\varepsilon_{z} - \varepsilon_{\theta}}{2} \right)^{2} + \left( \frac{\gamma_{z\theta}}{2} \right)^{2}}$$
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

wall elements that solely interact with particles to apply shear loads is preferred. The gravity was removed to achieve a uniform stress state and then, as shown in Fig. 3.1(b), vertically arranged torsional blades consisting of six wall elements were inserted into the specimen.

Soils not merely encounter diverse levels of $K_{0}$, but also frequently undergo complex stress histories, potentially influencing the liquefaction resistance. For instance, Pan et al. (2019) observed that the stress history of triaxial extension-unloading can enhance liquefaction resistance compared to IC specimen, whereas the triaxial compression-unloading history yields a contrary effect. To investigate the impact of stress path on the liquefaction resistance, two protocols employing distinct stress paths were utilized to prepare specimens. To achieve the desired target stress

![图表 描述已自动生成](thesis/assets/media/image67.png)

(a) Mean effective stress $p'$ vs. deviator stress $q$

![图表 描述已自动生成](thesis/assets/media/image68.png)

(b) Mean effective stress $p'$ vs. void ratio $e$

Fig. 3.2. Stress and void ratio evolution in anisotropic consolidation for specimens with different stress anisotropies from isotropic consolidation state with $p'$=10.0kPa and different target $K_{0}$

levels, a servo mechanism (Itasca Consulting Group, 2021; Ma et al., 2024) is employed to manipulate the position of vertices of wall elements throughout the consolidation process.

In the first approach, the specimen was initially compressed to a target void ratio of 0.808 under a friction coefficient of 0.1. Subsequently, the friction coefficient was reset to 0.5, followed by anisotropic consolidation from a state with $p'$=10.0kPa and $K_{0}$=1.0 to $p'$=133.33kPa and the target $K_{0}$ (IC-AC protocol), as shown in Fig. 3.2 (a) and Fig. 3.2(b). Notably, during the AC process with an increasing $p'$, $K_{0}$ evolves from 1.0 to the corresponding target $K_{0}$. Ten cases of specimens with $K_{0}$ values ranging from 0.33 to 3.33 were obtained.

The other approach adopted a constant-$p'$ triaxial shear method, where triaxial compression ($K_{0}$\<1.0) and extension ($K_{0}$\>1.0) shear tests were performed on the specimen with $p'$=133.33kPa and $K_{0}$=1.0 obtained using the first IC-AC protocol. The axial strain rate was set as ±1%/second, and the lateral cylinders were controlled to maintain a constant-$p'$ condition along the π-plane in stress space (IC-AC-TS protocol). For clarity, the term \"triaxial shear\" here refers to the shearing process applied to HCA specimens, which simulates the same stress state as in triaxial shear tests. Fig. 3.3(a) and Fig. 3.3(b) respectively show the relationship between deviator stress $q$ and axial strain $\varepsilon_{\alpha}$, as well as the variation in void ratio $e$ up to ±1.6% $\varepsilon_{\alpha}$.

Compared to the gradually increasing $q$ at a constant $p'$ for the IC-AC-TS approach, the IC-AC method initiates $q$ at a lower $p'$, with $q$ increasing as $p'$ rises.

![图形用户界面, 应用程序, 表格, Excel 描述已自动生成](thesis/assets/media/image69.png)

(a) Axial strain $\varepsilon_{a}$ vs. deviator stress $q$

![图表, 折线图 描述已自动生成](thesis/assets/media/image70.png)

(b) Relationship between e and $\varepsilon_{a}$

Fig. 3.3. Stress and void ratio evolution in constant-$p'$ triaxial shear for specimens with different stress anisotropies after anisotropic consolidation with $p'$=133.33kPa and target $K_{0}$=1.0

The impact of these differences on liquefaction resistance is worth exploring. To simplify, the results with the first IC-AC protocol is labeled as \"AC\", whereas the results with IC-AC-TS specimens refer to "TS" in the accompanying figures. As indicated by Fig. 3.2(b) and Fig. 3.3(b), the differences in $e$ between different $K_{0}$ states after IC-AC or IC-AC-TS were minimal, with $e$ ranging from 0.8080 to 0.8083. This variation is small compared to the changes during the IC-AC or IC-AC-TS processes, making it reasonable to emphasize the effects of microscopic quantities, instead of $e$, on liquefaction resistance. The specification of specimens for cyclic shear are summarized in Table 3-3 and Table 3-4.

Table 3-3. Specification of dense specimens in initial cyclic undrained shear stage

![表格 描述已自动生成](thesis/assets/media/image71.png)

Table 3-4. Specification of loose specimens in initial cyclic undrained shear stage

![表格 描述已自动生成](thesis/assets/media/image72.png)

### Implementation of undrained condition

In DEM simulations of undrained tests, the interaction between water and particles is disregarded, employing a constant volume approach to replicate the undrain condition. The effectiveness of this constant volume approach has been validated in numerous DEM simulations. (Sitharam et al., 2002; Yimsiri and Soga, 2010). With the specimen height held constant, following laboratory testing procedures (Vargas et al., 2020), an unchanged cross-sectional area ensures the overall volume remains consistent. As described by Eq. (3-1), the variation of the outer and inner radii was controlled proportionally to maintain a constant cross-sectional area of the specimen, where $R$ and $r$ denote the inner and outer radii, respectively, and $t$ represents time.

$\frac{dR}{dt} = \frac{r}{R}\frac{dr}{dt}$ (3-1)

As shown in Eq. (3-2), the difference in effective stresses between the inner and outer cylinders is regulated by controlling diameter variation, aiming to achieve equivalent stresses acting on inner and outer cylinders, with respect to laboratory tests. Here, $H$ represents the height of the specimen, $\sigma_{dif}'$ denotes the difference in effective stresses between the outer and inner cylinders, and $E_{eq}$ is an averaged equivalent modulus.

$\frac{dr}{dt} = \frac{2\pi H\sigma_{dif}'}{E_{eq}\Delta t}$ (3-2)

$E_{eq}$ is influenced by the dimensions of the inner and outer cylinders, along with the contact stiffness between the cylinders and particles, $K_{i}$ and $K_{o}$, as defined in Eq. (3-3).

$E_{eq} = \frac{r}{R}\frac{K_{o}}{R} + \frac{K_{i}}{r}$ (3-3)

The essence of the method lies in a combined servo mechanism. This mechanism achieves two objectives simultaneously: maintaining constant volume to replicate undrained conditions and minimizing differences in effective stress between the inner and outer cylinders to replicate stress boundary conditions observed in laboratory tests. This method is equivalent to the mixed stress and strain-controlled loading with $v_{z}$ being zero described in algorithm Ⅱ by Ma et al. (2024), trickily achieving the simulation of undrained condition and stress condition in HCA tests.

The effective stresses were evaluated by measuring the contact stresses between the boundary and particle skeleton. The assumptions of undrained condition and full saturation result in variations in effective stress on lateral cylinders and EPWP that are equal in magnitude but opposite in sign, quantifying this relationship in Eq. (3-4). Here, $u$ represents the excess pore water pressure, $\sigma_{r}'$ denotes the radial effective stress, which is derived from the inner and outer effective stress $p_{i}'$ and $p_{o}'$, and $\sigma_{r0}'$ is its initial value (Yimsiri and Soga, 2010).

$u = \sigma_{r0}' - \sigma_{r}'$ (3-4)

### Application of shear force

Shear forces are applied to the specimens in the form of a sine wave. Similar to the servo mechanism in consolidation process, the torque application method also considers the difference between the target and current values, along with the total contact stiffness between the blades and particles. The main distinction from the servo

![图示 中度可信度描述已自动生成](thesis/assets/media/image73.png)

Fig. 3.4. Determination of moment of inertia of shear stiffness in servo mechanism for torque application

mechanism for the lateral cylinder is in how stiffness is calculated, specifically considering the distance from the center of rotation. Fig. 3.4 illustrates the contact between a particle and a blade, where the distance from the center of rotation to the contact point is denoted as $r_{d}$, and the angle between the contact normal and the horizontal plane is $\theta$. Eq. (3-5) describes the angular velocity of the torsional blade, where $T_{dif}$ represents the difference between the target torque and the current value, and $I_{rot}$ denotes the moment of inertia of the contact stiffness. As indicated by Eq. (3-6), $I_{rot}$ is determined by the contact stiffness $k_{n}$ and square of the distance $r_{d}$. $I_{rot}$ is adjusted by $\cos^{2}\theta$ because a larger $\theta$ reduces its contribution to the shear stiffness.

$\omega = \frac{T_{dif}}{I_{rot}\Delta t}$ (3-5)

$I_{rot} = \Sigma r_{d}^{2}k_{n}\cos^{2}\theta$ (3-6)

AC and IC specimens obtained from both the IC-AC and IC-AC-TS protocols, with $K_{0}$ ranging from 0.33 to 3.33, underwent shear forces with 4 different cyclic stress ratios CSR ranging from 0.25 to 0.40 until liquefaction occurred. A discussion concerning the factors influencing liquefaction strength is provided from both macroscopic and microscopic perspectives.

## Results and discussion

### Macroscopic response

#### Stress strain relationship

Fig. 3.5, 3.6, and 3.7 respectively depict the relationships between mean principal stress $p'$ and shear stress $\tau$, shear strain $\gamma$ and shear stress $\tau$, as well as the variation in EPWP ratio $r_{u}$ during the cyclic shear, for the IC state with $K_{0}$=1.0 and AC state with $K_{0}$=0.40. The AC state with $K_{0}$=0.40 state was obtained with the IC-AC protocol and liquefaction here is defined as occurring when $r_{u}$ reaches 95% of $\sigma_{r0}'$.

In Fig. 3.5(a) and (b), as the shear stress $\tau$ cyclically acts on the hollow cylindrical specimen, the mean principal stress $p'$ exhibited an overall decrease for both IC and AC specimens. Once $p'$ falls below approximately 60 kPa, an increase in the magnitude of $\tau$ drove an upward trend in $p'$, displaying a butterfly-shaped relationship in $p'$-$q$ space. After liquefaction onset, $p'$ and $\tau$ delineate the critical state line and then converge at the origin, periodically. To better understand the

![图表 描述已自动生成](thesis/assets/media/image74.png)

(a) Shear stress $\tau$ vs. mean effective stress $p'$ (CSR = 0.250, $K_{0}$=1.00, dense)

![图表 描述已自动生成](thesis/assets/media/image75.png)

(b) Shear stress $\tau$ vs. mean effective stress $p'$ (CSR = 0.250, $K_{0}$=0.40, dense)

![图表 描述已自动生成](thesis/assets/media/image76.png)

(c) Deviatoric stress $\sigma_{vM}$ vs. mean effective stress $p'$ (CSR=0.250, dense)

![图表 中度可信度描述已自动生成](thesis/assets/media/image77.png)

(d) Deviatoric stress $\sigma_{vM}$ vs. mean effective stress $p'$, CSR=0.350

Fig. 3.5. Stress evolution of IC with $K_{0}$=1.0 and AC specimen with $K_{0}$=0.40 in undrained cyclic shear

evolution of stress state for the $K_{0}$=1.0 and $K_{0}$=0.40, the relationship between $p'$ and deviatoric von-Mises stress $\sigma_{vM}$ is depicted in Fig. 3.5(c) and Fig. 3.5(d) for CSR=0.250 and CSR=0.350, respectively. The $K_{0}$=1.0 specimen started with $\sigma_{vM}$ at 0, while the $K_{0}$=0.40 specimen initially exhibited higher level of initial $\sigma_{vM}$. As cyclic shear progressed, the $K_{0}$=1.0 specimen exhibited larger fluctuation in $\sigma_{vM}$. In contrast, the AC specimen initially showed smaller amplitude in $\sigma_{vM}$, which gradually increased in amplitude while decreasing in magnitude over time, as illustrated in Fig. 3.5(c) or Fig. 3.5(d).

![图表, 折线图 描述已自动生成](thesis/assets/media/image78.png)

(a) Shear stress $\tau$ vs. shear strain $\gamma$, CSR = 0.250, $K_{0}$=1.00

![图表, 折线图 描述已自动生成](thesis/assets/media/image79.png)

(b) Shear stress $\tau$ vs. shear strain $\gamma$, CSR = 0.250, $K_{0}$=0.40

Fig. 3.6. Evolution of shear stress $\tau$ and shear strain $\gamma$ in undrained cyclic shear loading

In Fig. 3.6, stiff shear modulus with slight reduction was observed in initial stage. As cyclic loading progressed towards the liquefaction state, shear stiffness markedly decreased, plastic deformation occurred, and strong nonlinearity became evident. As shown in Fig. 3.7, pore water pressure responses differ between $K_{0}$=1.0 and $K_{0}$=0.40 states. For the $K_{0}$=1.0 state, $r_{u}$ increased more rapidly in the initial stages. However, after approximately 20 cycles, $r_{u}$ for the $K_{0}$=0.40 state surpassed that of the $K_{0}$=1.0 state. Liquefaction occurred after about 41 cycles for $K_{0}$=0.40, whereas $K_{0}$=1.0 case

![图表, 折线图 描述已自动生成](thesis/assets/media/image80.png)

Fig. 3.7. Comparison of evolution of excess pore water pressure ratio $r_{u}$ between IC state with $K_{0} = 1.0$ and AC state with $K_{0}$=0.40

Reached liquefaction after approximately 84 cycles, nearly twice as many as the $K_{0}$=0.40 state, suggesting a higher liquefaction strength for initially IC state with $K_{0}$=1.0. Fig. 3.5, 3.6, and 3.7 demonstrate that typical stress and strain evolution in laboratory tests has been replicated in DEM simulations, providing preliminary evidence for the effectiveness of the method proposed. On the other hand, it is crucial to investigate how this resistance changes with varying CSR and $K_{0}$. Fig. 3.8(a) and Fig. 3.8(b) compare the number of cycles required to reach liquefaction under varying CSR and initial $K_{0}$ values. Fig. 3.8(a) demonstrates liquefaction resistance for specimens prepared with IC-AC protocol and found that under different CSR conditions, the number of cycles to liquefaction decreases with decreasing $K_{0}$ when

![图表, 散点图 描述已自动生成](thesis/assets/media/image81.png)

(a) Cyclic liquefaction resistance with various CSR

![图表, 散点图 描述已自动生成](thesis/assets/media/image82.png)

(b) Number of cyclic loadings $N_{L}$ vs. $K_{0}$ under cyclic shear loading with cyclic shear stress ratio of 0.250

Fig. 3.8. Cyclic liquefaction resistance of specimens subjected to different initial stress anisotropies and cyclic shear stress ratios

$K_{0} < 1.0$, and decreases with increasing $K_{0}$ when $K_{0} > 1.0$. Hence, greater stress anisotropy results in fewer cycles needed to trigger liquefaction, indicating lower resistance. This observation is consistent with the findings by Georgiannou and Konstadinou (2014) regarding the loose state, but it diverges from the results reported by other experimental studies (Ishihara and Takatsu, 1979; Yamashita and Toki, 1993; Vargas et al., 2020).

The influence of stress paths on liquefaction resistance is also noteworthy. Fig. 3.8(b) analyses the variation in the number of cycles required for triggering liquefaction under CSR=0.25, including specimens prepared with both protocols. Observations reveal that the protocols for preparing specimens, whether following the IC-AC or IC-AC-TS protocol, does not significantly affect the liquefaction resistance for the same $K_{0}$. Yet, other forms of protocols for preparation may have an impact on liquefaction resistance and remains to be investigated, but this falls outside the scope of this study and should be noted.

#### Cumulative shear work

Cumulative shear work refers to the energy input during undrained cyclic shear in this study. It is valuable to examine the correlation between the liquefaction resistance of soils and their susceptibility to the input energy. Towhata and Ishihara (1985) conducted a series of experiments where specimens were subjected to undrained cyclic shear under various loading conditions. They revealed a unique relationship between excess pore water pressure and shear work, despite differences in stress anisotropy. Figueroa et al. (1994) similarly confirmed that the shear work required for triggering liquefaction is independent of the amplitude of strain through strain-controlled tests. Georgiannou and Konstadinou (2014) concluded from the comparison between IC and AC specimens that the energy associated with terminal water pressure is positively correlated with relative density. For equivalent relative densities, AC specimens require greater energy than IC specimens to induce liquefaction.

![图表 描述已自动生成](thesis/assets/media/image83.png)

(a) $W_{s}$ vs. $N_{c}/N_{L}$ (dense)

![图表 描述已自动生成](thesis/assets/media/image84.png)

(b) $r_{u}$ vs. $W_{s}$ (dense)

Fig. 3.9. Evolution of cumulative unit volume shear work and shear work required to trigger liquefaction for different $K_{0}$

The cumulative unit volume shear work $W_{s}$ is defined as shown in Eq. (3-7), expressed as an integral of shear strain rate $\dot{\gamma_{z\theta}}$, shear stress $\tau_{z\theta}$, and incremental time $dt$. This represents the accumulated input energy per unit volume in the specimen.

$W_{s} = \int_{0}^{t}{\dot{\gamma_{z\theta}}\tau_{z\theta}dt}$ (3-7)

As indicated by Fig. 3.9(a), in the liquefaction process normalized by $N_{L}$, it is difficult to distinguish the differences between the cases with different $K_{0}$ values. Fig. 3.9(b) explores the impact of different $K_{0}$ on the liquefaction by relating $W_{s}$ and $r_{u}$. For the initial stages, particularly when $r_{u}$ is less than 0.2, a larger $K_{0}$ contributes to a higher $r_{u}$ for the same amount of work $W_{s}$​. $r_{u}$ decreases as shear force performs positive work and increases as shear force performs negative work. The shear work required to achieve liquefaction $W_{sL}$ for different $K_{0}$ values range from 0.07 to 0.13, with a trend of increasing $W_{sL}$​ as stress anisotropy increases. This implies that although the IC state with $K_{0}$=1.0 specimen requires more cyclic numbers to reach liquefaction, its higher initial shear stiffness results in lower strain velocity, hence requiring the least shear work.

#### Initial shear wave velocity

The response in cumulative shear work inspired an exploration in relationship between initial stiffness and liquefaction resistance (Xu et al., 2015). The shear modulus is the derivative of shear stress $\tau$ with respect to shear strain $\gamma$ and Eq. (3-8) describes the initial shear wave velocity $V_{s0}$ in terms of the initial shear modulus $G_{0}$ and the saturated density $\rho_{sat}$ (Tokimatsu and Uchida, 1990; Chen et al., 2005).

$V_{s0} = \sqrt{\frac{G_{0}}{\rho_{sat}}}$ (3-8)

![图表, 折线图 描述已自动生成](thesis/assets/media/image85.png)

Fig. 3.10. Relationship between cyclic number and initial shear wave velocity (CSR=0.250)

As shown in Fig. 3.10, for $K_{0}$=1.0 state, $V_{s0}$ reaches its highest value, nearly 450m/s. Regardless of whether $K_{0}$ is less than 1.0 or greater than 1.0, $V_{s0}$ decreases with increasing stress anisotropy, corresponding to the trend of evolution in liquefaction resistance. At $K_{0}$=0.33 and $K_{0}$=3.33, $V_{s0}$ drops to its lowest level, approximately 340m/s. This behavior provides a macroscopic guideline for assessing liquefaction strength: a higher $V_{s0}$ indicates greater liquefaction resistance. Additionally, the cases for $K_{0}$\<1.0 and $K_{0}$\>1.0 diverge: for the same $V_{s0}$, $K_{0}$\<1.0 exhibits higher liquefaction resistance compared to $K_{0}$\>1.0. For example, $K_{0}$=0.40 with $V_{s0}$ at 384m/s achieves $N_{L}$ close to 42, while $K_{0}$=2.50 with $V_{s0}$ around 400m/s has $N_{L}$ only at 37. Yet, these macroscopic findings remain difficult to elucidate the difference in liquefaction resistance under different initial stress conditions. This emphasizes the necessity for a more detailed discussion at the microscale to comprehend the factors influencing liquefaction resistance.

### Microscopic interpretation

#### Evolution of coordination number

The coordination number indicates the number of contacts each individual particle has. Its average value for all particles isotropically evaluates the compactness of fabric in granular materials (Oda, 1977; Shire and O'Sullivan, 2012; Fei and Narsilio, 2020). Particles with fewer than two contacts are generally unable to stably transmit interparticle forces and do not effectively contribute to the soil skeletons. These particles are classified as floaters and are excluded from the calculation of the coordination number (Thornton, 2000; Hu et al., 2023). As shown in Eq. (3-8),

$Z_{m} = \frac{2N_{c} - N_{1}}{N_{p} - N_{1} - N_{0}}$ (3-8)

$Z_{m}$ represents the mechanical coordination number. $N_{c}$ is the number of interparticle contacts, and $N_{p}$ is the total number of particles. $N_{1}$ and $N_{0}$ indicate the number of particles with one and zero contacts, respectively, to eliminate the influence of floaters.

Figure 3.11 shows the evolution of $Z_{m}$ under different initial $K_{0}$ states during the cyclic shear. The results indicate that the influence of initial stress states on the coordination number is significant, with greater stress anisotropy corresponding to lower coordination numbers both at the initial state and during the cyclic shear process. As cyclic loading was applied to the undrained specimen, $Z_{m}$ exhibited oscillatory behavior while progressively decreasing as shown in Fig. 3.11. The decline in $Z_{m}$ indicates a reduction in interparticle contacts and a loss of fabric integrity and robustness. Liquefaction was observed to occur when $Z_{m}$ fell to approximately 3.5, signifying a critical threshold where the specimen became susceptible to cyclic shear

![图表, 散点图 描述已自动生成](thesis/assets/media/image86.png)

Fig. 3.11. Mechanical coordination number evolution in cyclic shear and relationship between cyclic number required for liquefaction and initial mechanical coordination number (CSR=0.250)

stresses. Regardless of the initial $K_{0}$, the post-liquefaction $Z_{m}$ repeatedly cycles between approximately 3.5 and lower values. This implies that the initial stress anisotropies have minimal impact on the post-liquefaction fabric.

#### Evolution of fabric anisotropy

The fabric tensor quantifies the directionality and distribution of the fabric in granular materials (Oda, 1972; Oda et al., 1982). It can be represented in various forms (Oda, 1982; Kanatani, 1984), with the second-order tensor product being widely used. As shown in Eq. (3-9), the fabric tensor $\mathbf{\Phi}_{\mathbf{ij}}$ is the sum of tensor products of contact normal vectors divided by the number of contacts, where $n_{i}$ and $n_{j}$ denote contact normal vectors and i, j refer to circumferential, radial or axial direction.

$\mathbf{\Phi}_{\mathbf{ij}} = \ \frac{1}{N_{c}}\Sigma\mathbf{n}_{\mathbf{i}}\mathbf{n}_{\mathbf{j}}$ (3-9)

The diagonal elements of $\mathbf{\Phi}_{\mathbf{ij}}$ are positive and sum to one. The fraction of the diagonal elements describes the concentration of contact normals, with higher value indicating a greter concentration in that direction. The off-diagonal elements represent the asymmetry of the distribution of contact normals. The fabric tensor is a crucial indicator for characterizing the state of granular materials, microscopically refining the critical state theory (Li and Dafalias, 2012).

![图形用户界面 描述已自动生成](thesis/assets/media/image87.png)

Fig. 3.12. Transformation of contact normal from global x-y-z orthogonal coordinate to circumferential-radial-axial local cylindrical coordinates

The local circumferential, radial, and axial components of contact normals are position-dependent, requiring transformation from the global coordinate system as shown in Fig 3.12. Here, $\phi_{rot}$​ refers to the rotated angle from the global x-y-z coordinate system to the local circumferential-radial-axial coordinate system around z-axis because z-direction and axial direction are aligned. Eq. (3-10) describes the transformation from global components $n_{x}$, $n_{y}$, and $n_{z}$ to local components $n_{cir}$, $n_{rad}$, and $n_{ax}$.

$\begin{pmatrix}
n_{cir} \\
n_{rad} \\
n_{ax}
\end{pmatrix} = \begin{pmatrix}
\cos(\phi_{rot}) & sin(\phi_{rot}) & 0 \\
 - sin(\phi_{rot}) & cos(\phi_{rot}) & 0 \\
0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
n_{x} \\
n_{y} \\
n_{z}
\end{pmatrix}$ (3-10)

$\mathbf{F}_{\mathbf{ij}} = \frac{15\left( \mathbf{\Phi}_{\mathbf{ij}} - \mathbf{\delta}_{\mathbf{ij}} \right)}{2}$ (3-11)

$F_{c} = \sqrt{\frac{3}{2}\mathbf{F}_{\mathbf{ij}}\mathbf{F}_{\mathbf{ij}}}$ (3-12)

Eq. (3-11) defines the anisotropic fabric tensor $\mathbf{F}_{\mathbf{ij}}$, which subtracts 1/3 from the diagonal elements of the fabric tensor and then multiplied by 15/2, where $\mathbf{\delta}_{\mathbf{ij}}$ represents the Kronecker delta. As the second invariant of $\mathbf{F}_{\mathbf{ij}}$, $F_{c}$ measures the development of fabric anisotropy (Zhao and Guo, 2013), as shown in Eq. (3-12), where the Einstein summation convention is applied, and indicates the magnitude of fabric

![图表 描述已自动生成](thesis/assets/media/image88.png)

Fig. 3.13. Evolution of second invariant of mechanical anisotropic fabric tensor $F_{c}$ for specimens subjected to different initial stress anisotropies

anisotropy. Compared to $Z_{m0}$\'s sensitivity to $K_{0}$, $F_{c0}$ exhibits diminished responsiveness to changes in $K_{0}$ between 0.5 and 2.5. However, as stress anisotropy increases beyond these thresholds, greater fabric anisotropy was observed, as indicated in Fig. 3.13. Additionally, with higher stress anisotropy, $F_{c}$ underwent more pronounced fluctuations. For the same level of initial fabric anisotropy $F_{c0}$, states with $K_{0}$\>1.0 fluctuate more significantly compared to states with $K_{0}$\<1.0. This difference in fabric anisotropy potentially influences the macroscopic behavior of liquefaction resistance.

#### Effect of fabric on liquefaction resistance

For differentiating the states with $K_{0}$\<1.0 or $K_{0}$\>1.0, Otsubo et al. (2022) recommended to adopt a signed fabric anisotropy indicator $\alpha$ (Yimsiri and Soga, 2010) to evaluate fabric anisotropy as shown in Eq. (3-13):

$\alpha_{0} = \frac{5\left( 3\varphi_{v0} - 1 \right)}{5\varphi_{v0} + 1}$ (3-13)

, where $\varphi_{v0}$ denotes the initial vertical principal component in fabric tensor $\mathbf{\Phi}_{\mathbf{ij}}$. A larger $\varphi_{v0}$ means a concentration of contact normal converging in the axial direction after specimen preparation. The impact of fabric on liquefaction resistance is investigated through a space of $\alpha_{0}$, $Z_{m0}$, and $N_{L}$ (Yang and Taiebat, 2024) for various $K_{0}$, as shown in Fig. 3.14(a) and (b). Specimens prepared using the IC-AC and IC-AC-TS protocols exhibit similar $Z_{m0}$ and $\alpha_{0}$, indicating that the two stress paths do not significantly affect the microscopic fabric, thereby explaining the similar $N_{L}$for different preparation protocols. For $K_{0}$=1.0, $Z_{m0}$ and liquefaction strength exhibit the highest levels. As stress anisotropy increases, AC states with $K_{0}$\<1.0 and $K_{0}$\>1.0 diverge along different routes.

To investigate the influence of $Z_{m0}$ and $\alpha_{0}$ on liquefaction resistance, an exponential function that linearly relates $Z_{m0}$ and $\alpha_{0}$ to $N_{L}$ (Yang and Huang, 2023; Yang and Taiebat, 2024), was introduced to fit their relationship, as shown in Eq. (3-14).

$N_{L} = \exp\left( {\zeta Z}_{m0} + \eta\alpha_{0}\  + \chi \right)$ (3-14)

The fitted surface equation produced positive $\zeta$=3.63 and $\eta$=0.19, suggesting that an increasing $Z_{m0}$ or $\alpha_{0}$ enhances liquefaction resistance, which contrasts with the literatures, where an increasing $\alpha_{0}$ reduces liquefaction resistance. The $K_{0}$ conditions of the specimens in this study vary considerably compared to the literature and could explain the distinct conclusions. For instance, unlike a comparison between two stress ratios of $K_{0}$=1.0 and $K_{0}$=0.5 (Yang and Taiebat, 2024), this study evaluates liquefaction resistance between and beyond the thresholds, with $K_{0}$ ranging from 0.33 to 3.33, under different relative densities. When comparing the IC state of $K_{0}$=1.0 with AC states of $K_{0}$≠1.0, as shown in Fig. 3.14(b), it is evident that for both dense and loose states, the $N_{L}$ for $K_{0}$=1.0 lies above the fitted lines for $K_{0}$\<1.0 or $K_{0}$\>1.0, indicating a stronger liquefaction resistance for $K_{0}$=1.0 state at the same $Z_{m0}$. This tendency aligns well with the conclusions found in the literatures. However, introducing multiple values of $\alpha_{0}$ emphasized the comparison between the AC states of $K_{0}$\<1.0 and $K_{0}$\>1.0, thus yielding a positive value of $\eta$ when fitting the relationship. On the other hand, through a comparison of different relative densities as shown in Fig. 3.14 (b), the fitted line for dense state is positioned above that of the loose state, indicating that not only the microscopic factors like $Z_{m0}$ and $\alpha_{0}$, but also a smaller void ratio, which evaluates the macroscopic compactness, strengthens liquefaction resistance.

![图表 描述已自动生成](thesis/assets/media/image89.png)

(a) Coupled effect of $Z_{m0}$ and $\alpha_{0}$ on liquefaction resistance

![图表 描述已自动生成](thesis/assets/media/image90.png)

(b) Effect of $Z_{m0}$ on liquefaction resistance

Fig. 3.14. Effect of initial coordination number $Z_{m0}$ and initial fabric anisotropy $\alpha_{0}$ on liquefaction resistance for specimens with different initial stress anisotropies (CSR=0.250)

While liquefaction resistance decreases with increasing initial stress anisotropy for both dense and loose states, primarily due to variation in $Z_{m0}$, subtle differences in liquefaction response are observed for states with $K_{0}$\<1.0 and $K_{0}$\>1.0. For instance, as shown in Fig. 3.14(b), which decouples $\alpha_{0}$ from Fig. 3.14(a), illustrates that when comparing $K_{0}$=0.4 and $K_{0}$=2.5 in the dense state, both share a similar $Z_{m0}$ value around 4.43. However, the $N_{L}$ is over 10% higher for $K_{0}$ = 0.4 compared to $K_{0}$ = 2.5. Additionally, for $K_{0}$=0.33 and $K_{0}$=3.0 in the dense state, although their $N_{L}$ values are similar, the $Z_{m0}$ for $K_{0}$=0.33 is at least 0.05 lower than that for $K_{0}$=3.0. This suggests that a smaller $Z_{m0}$ is sufficient to achieve the same level of liquefaction resistance for $K_{0}$=0.33 as for $K_{0}$=3.0. These differences contribute to the positive value of $\eta$ in Eq. (3-14). On the other hand, for the loose states, this difference between $K_{0}$\<1.0 and $K_{0}$\>1.0 is limited, where the fitted lines for $K_{0}$\<1.0 and $K_{0}$\>1.0 almost overlap. However, for comparison between $K_{0}$=0.33 and $K_{0}$=3.33, or comparison between $K_{0}$=0.40 and $K_{0}$=2.50, stronger liquefaction tendency was also observed, where smaller $Z_{m0}$ enables similar liquefaction resistance for $K_{0}$\<1.0 compared to $K_{0}$\>1.0. The overlapping of fitted lines are mainly attributed to a sightly high value for $K_{0}$=3.00 in loose state.

$K_{0} < 1.0$ and $K_{0} > 1.0$ states correspond to different intermediate principal stress $b$, as described in Eq. (2-15). Experimental results by Tastan and Carraro (2022) indicate that liquefaction resistance increases as $b$ increases from 0.0 to 0.8.

$b = \frac{{\sigma_{2}' - \sigma}_{3}'}{\sigma_{1}' - \sigma_{3}'}$ (3-15)

This observation contrasts this study, where $b = 0.0$ shows larger liquefaction resistance. The discussion in this study is focusing on comparing the influence of $b$ only at the extremes of 0.0 and 1.0. Yet, investigating how the liquefaction responses change with in-between values, and providing a microscopic explanation would also attract interest and warrants further study, but it lies beyond the scope of this study.

#### Interparticle contact force

To interpret the interparticle relationships, contact forces and individual particle movement in the initial state with $K_{0}$=0.33, post-liquefaction state with $K_{0}$=0.33, initial state with $K_{0}$=3.00, and post-liquefaction state with $K_{0}$=3.00 are depicted in Fig. 3.15(a), Fig. 3.15(b), Fig. 3.15(c), and Fig. 3.15(d). The specimens with $K_{0}$=0.33 and $K_{0}$=3.00 exhibit significant differences in the distribution of contact forces at the initial stages in cyclic shear. For $K_{0}$=0.33, the contact forces converge in the axial direction, whereas for $K_{0}$=3.00, the contact forces tend to be distributed horizontally, aligning with the direction of the maximum principal stress in both cases. As cyclic loading progresses, the number of interparticle force gradually decreases, and the magnitude of these forces diminishes, until liquefaction and large deformation occurs. From a macroscopic perspective, the liquefaction process involves a decline in stiffness and an increase in nonlinearity, as discussed in the macroscopic behavior section. From a microscopic viewpoint, liquefaction occurs because the particle-constituting skeleton becomes increasingly unable to sustain itself through particle interaction, such as the relative movement, hindering the transfer of external forces. In contrast to the influence of $K_{0}$ on contact forces in initial state, the effect of different initial $K_{0}$ values on the

![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image91.jpeg)

(a) AC state with initial $K_{0}$=0.33

![图形用户界面 中度可信度描述已自动生成](thesis/assets/media/image92.jpeg)

(b) Post-liquefaction state with initial $K_{0}$=0.33

![电脑萤幕画面 中度可信度描述已自动生成](thesis/assets/media/image93.jpeg)

(c) AC state with initial $K_{0}$=3.00

![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image94.jpeg)

(d) Post-liquefaction state with initial $K_{0}$=3.00

Fig. 3.15. Contact force chain and displacement of particles under initial and post-liquefaction states subjected to different initial $K_{0}$

contact forces becomes insignificant in post-liquefaction stage. Whether $K_{0}$=0.33 or $K_{0}$=3.00, the contact forces no longer align with the initial direction of the maximum principal stress but tend to orient more randomly and concentrate locally.

#### Contact orientation 

The fabric tensor is orientation-dependent, meaning its elements vary based on the specified coordinate directions (Kanatani, 1984). This sparked interest in using statistical methods, such as spatial probability density function (PDF) to analyze the distribution of contact normal (Rothenburg and Bathurst, 1989). To simultaneously capture changes in both direction and quantity of contact normals during cyclic shear, it is recommended to use contact density for visualization. The contact density (Han et al., 2023) describes the average number of contacts per unit surface area for a particle with normalized radius, as shown in Eq. (3-16)

$\rho_{c}\left( \theta_{z},\ \phi_{cir} \right) = \frac{2N_{\theta_{z},\ \ \phi_{cir}}|n_{c} \in \left( \theta_{z},\theta_{z} + \Delta\theta_{z} \right) \cap (\phi_{cir},\ \phi_{cir} + \Delta\phi_{cir})}{N_{p}\int_{\phi_{cir}}^{\phi_{cir} + \Delta\phi_{cir}}{\sin\left( \phi_{cir} \right)d\phi_{cir}}\int_{\theta_{z}}^{\theta_{z} + \Delta\theta_{z}}{d\theta_{z}}}\ $ (3-16)

Here, $\rho_{c}$ represents the contact density, $\theta_{z}$ and $\phi_{cir}$ indicate the polar and azimuthal angles in the spherical polar coordinate system, respectively. $N_{\theta_{z},\ \ \phi_{cir}}$ indicates the number of contacts with normals within the range of $\left( \theta_{z},\theta_{z} + \Delta\theta_{z} \right) \cap (\phi_{cir},\ \phi_{cir} + \Delta\phi_{cir})$. $N_{p}$ and the subsequent integral denote the total number of particles and the corresponding surface area on the unit sphere, respectively. This method effectively evaluates contact orientation during an undrained cyclic shear and accommodates granular systems with various particle numbers.

The evolutions of contact density during the liquefaction process for $K_{0}$=0.33 and $K_{0}$=3.00, are shown in Fig. 3.16 and Fig. 3.17. Fig. 3.16(a) represents the dense state with initial $K_{0}$=0.33, exhibiting an elongated columnar shape extending along the axial direction, whereas Fig. 3.17(a) depicts the contact density with initial $K_{0}$=3.00, characterized by a dimpled ellipsoid oriented toward the axial direction. As cyclic shear progresses, the direction of maximum contact density varies following the rotating principal stress axis, and the overall contact density gradually decreases as shown in Fig. 3.16 (b) and Fig. 3.17 (b). The evolution of contact density indicates that the post-liquefaction distribution of contact density is largely independent of the initial state, shifting between two inclined elongated columnar distributions along varying directions.

![图表, 雷达图 描述已自动生成](thesis/assets/media/image95.jpeg) ![图表, 图示 描述已自动生成](thesis/assets/media/image96.jpeg)

(a) $N_{c}$/$N_{L}$=0.00 (b) $N_{c}$/$N_{L}$=0.75

![图表 中度可信度描述已自动生成](thesis/assets/media/image97.jpeg) ![图表 描述已自动生成](thesis/assets/media/image98.jpeg)

\(c\) $N_{c}$/$N_{L}$=1.01 (d) $N_{c}$/$N_{L}$=1.04

Fig. 3.16. Contact density evolution in liquefaction process with initial $K_{0}$=0.33

![图表 描述已自动生成](thesis/assets/media/image99.jpeg) ![图表 描述已自动生成](thesis/assets/media/image100.jpeg)

(a) $N_{c}$/$N_{L}$=0.00 (b) $N_{c}$/$N_{L}$=0.73

![图表 描述已自动生成](thesis/assets/media/image101.jpeg) ![图表 描述已自动生成](thesis/assets/media/image102.jpeg)

\(c\) $N_{c}$/$N_{L}$=0.97 (d) $N_{c}$/$N_{L}$=1.03

Fig. 3.17. Contact density evolution in liquefaction process with initial $K_{0}$=3.00

Although $Z_{m0}$ has the dominant impact on liquefaction resistance, the variations in liquefaction resistance caused by morphological differences in fabric are also worth investigating. This morphological difference in fabric explains why, in the $Z_{mi}$-$N_{L}$ plane, as shown in Fig. 3.14 (b), paths with $K_{0}$\<1.0 and $K_{0}$\>1.0 diverge as stress anisotropy increases, and why $F_{c}$ exhibits more pronounced fluctuation with $K_{0}$\>1.0 than that with $K_{0}$\<1.0 during the cyclic shear in Fig. 3.12. The state with $K_{0}$\<1.0 corresponding to an elongated columnar morphology of fabric results in more contact normals along the axial direction, which is perpendicular to the shear force, potentially enhancing liquefaction resistance (Zhang et. al., 2023), compared to the dimpled ellipsoidal morphology observed for $K_{0}$\>1.0. Thus, a positive $\beta$ was obtained with the fitted surface in Fig. 3.13. Additionally, cyclic shear caused larger amplitude of fluctuations in $F_{c}$ during cyclic shear for $K_{0}$\>1.0 compared to $K_{0}$\<1.0 due to the instability in $F_{c}$ induced by the dimpled ellipsoidal morphology in fabric.

## Summary

This study utilized the DEM to investigate the impact of initial stress anisotropy on the liquefaction resistance of sand soils under undrained cyclic shear conditions. By employing a combined servo mechanism, the evolution of stress resembling that in laboratory HCA tests were observed, indicating that the undrained condition, stress variation, as well as principal stress axes rotation have been successfully reproduced with the method. The analysis covered a broad range of $K_{0}$ values from 0.33 to 3.33 and incorporated shear loading with CSR from 0.250 to 0.400. It explored the effects of different initial stress conditions and stress paths on undrained cyclic behavior. The findings are summarized as follows:

(1) Initial stress anisotropy, represented by $K_{0}$, significantly affects liquefaction resistance. Liquefaction resistance decreases with decreasing $K_{0}$ when $K_{0}$ is less than 1.0, and with increasing $K_{0}$ when $K_{0}$is greater than 1.0. Thus, greater stress anisotropy results in reduced liquefaction resistance. The protocols for specimen preparation, whether through initial isotropic consolidation followed by linear anisotropic consolidation (IC-AC) or initial isotropic consolidation followed by constant-$p'$ triaxial shear (IC-AC-TS), does not significantly impact liquefaction resistance.

(2) Greater initial stress anisotropy is associated with a lower initial mechanical coordination number $Z_{m0}$. A correlation is observed between $Z_{m0}$ and the cyclic number required for liquefaction $N_{L}$, which indicates liquefaction resistance, providing a microscopic explanation for the influence on liquefaction strength. In addition to $Z_{m0}$, a smaller void ratio, which evaluates the macroscopic compactness, contributes to liquefaction resistance as well.

(3) For $K_{0}$\<1.0, which corresponds to an intermediate principal stress ratio $b$=0.0, a higher $N_{L}$ at a similar $Z_{m0}$ or a smaller $Z_{m0}$ at a similar $N_{L}$ was observed for $K_{0}$\<0.0 compared to $K_{0}$\>1.0, especially when stress anisotropy is large. This indicates that slightly greater liquefaction resistance was confirmed for $K_{0}$\<1.0 than that for $K_{0}$\>1.0. In the $\alpha_{0}$-$Z_{mi}$-$N_{L}$ space, as stress anisotropy increases, the predicted relationship for $K_{0}$\<1.0 and $K_{0}$\>1.0 further diverged, producing a positive $\eta$ in the fitted surface.

(4) Contact density not only reflects the distribution characteristics of contact normals in different orientations, like a probability density function (PDF), but also captures the overall changes in contact number during undrained cyclic shear, with the advantage of being independent of the total number of particles. With this approach, it was found that anisotropic consolidation states with $K_{0}$\<1.0 or $K_{0}$\>1.0 produce different morphologies of contact density. When $K_{0}$\<1.0, an elongated columnar distribution tends to result in smaller fluctuation in $F_{c}$, compared to the dimpled ellipsoidal distribution for $K_{0}$\>1.0. Additionally, when $K_{0}$\<1.0, more contact normals converge in the axial direction, aligning perpendicular to the shear force, potentially enhancing liquefaction resistance.

## Experimental Validation of K0 Effects on Liquefaction Resistance 

As introduced in Chapter 3, soils exhibit diverse lateral pressure coefficients ($K_{0}$) under varying confinement conditions. For instance, when retaining structures move away from the soil, the lateral pressure decreases, whereas it increases when the structures move toward the soil. Assuming no significant variation in vertical loading, the lateral pressure coefficient, defined as the ratio of lateral to vertical pressure, changes correspondingly. The influence of K~0~​ on liquefaction resistance under the same mean principal stress $p'$ has garnered research interest. Chapter 3 findings reveal that liquefaction resistance decreases as $K_{0}$ deviates from 1.0, with greater stress anisotropy ($K_{0}$\<1.0 or $K_{0}$​\>1.0) leading to reduced resistance. This behavior is tied to a lower initial coordination number ($Z_{m0}$​), which is strongly correlated with the cyclic number required for liquefaction ($N_{L}$​), providing a microscopic explanation for these trends.

However, most previous laboratory studies have focused on a limited range of $K_{0}$ values, such as $K_{0}$=1.0, 0.5, and 2.0, representing specific isotropic or anisotropic stress conditions. The transition of liquefaction resistance from isotropic conditions to anisotropic conditions remains unclear. Additionally, Chapter 3 highlighted that for $K_{0}$\<1.0, contact normals align more in the axial direction, perpendicular to the shear force, potentially enhancing liquefaction resistance compared to $K_{0}$\>1.0. The liquefaction resistance beyond these typical values also deserves further experimental verification and discussion.

The objective of this chapter is to experimentally validate the effects of $K_{0}$ on the liquefaction resistance of soils and compare the experimental results with the numerical findings from the previous chapters.

### Introduction

The limitations of traditional triaxial tests lie primarily in their inability to replicate the principal stress axis rotation that occurs during shaking (Hyodo et al., 1991; Seed and Lee, 1966; Silver et al., 1976; Toki et al., 1986; Yoshimi et al., 1984). In another type of simple shear tests, where cubic samples are wrapped by a membrane, the frictional and interlocking contact between soil elements cannot be accurately reproduced. To address these limitations, the hollow cylindrical torsional shear apparatus (HCA) was developed. This apparatus not only allows for the application of cyclic shear forces during shaking, effectively replicating principal stress axis rotation, but also utilizes hollow cylindrical samples that approximate the lateral interactions between soil elements, such as interlocking contacts. This makes it an ideal laboratory method for simulating the liquefaction behavior of soil elements.

Ishihara and Yasuda's (1975) findings highlighted significant disparities between the triaxial and HCA tests, suggesting the importance of incorporating realistic stress states in liquefaction studies. Subsequent research by Tatsuoka et al. (1986) compared triaxial and torsional tests on specimens prepared with varying methods, revealing inconsistencies in liquefaction resistance between the two testing approaches. Further investigations by Yamashita and Toki (1993) utilized torsional and triaxial tests to refine constitutive models for liquefiable sands. These studies demonstrated that the chosen testing method---whether torsional or triaxial---influenced the measured liquefaction resistance. Collectively, these findings underscore the critical role of experimental techniques, such as HCA, in advancing the understanding of liquefaction mechanisms.

Soils in their natural state typically exhibit varying lateral-to-vertical stress ratios, represented by $K_{0}$. The influence of $K_{0}$ on liquefaction resistance has been a focal point of research, yet conclusions remain conflicting. For instance, Ishihara and Takatsu (1979) observed negligible dependency of liquefaction resistance on $K_{0}$ for Fuji River sand, a result echoed by Yamashita and Toki (1993). Conversely, Georgiannou and Konstadinou (2014) found that isotropically consolidated (IC) specimens demonstrated greater liquefaction resistance in loose sands than anisotropically consolidated (AC) specimens, a trend that reversed for denser states. Furthermore, Vargas et al. (2020), through HCA tests on Ottawa sand, concluded that AC specimens with $K_{0}$=0.5 exhibited approximately 20% higher liquefaction resistance than IC specimens for both relative densities of 50% and 80%.

While these studies provide valuable insights, they often focus on a limited range of $K_{0}$ values---typically 0.5, 1.0, and 2.0---leaving the effects of broader $K_{0}$ ranges unexplored. Moreover, the discrepancies in findings highlight a lack of consensus regarding the role of initial stress anisotropy on liquefaction resistance, suggesting the need for more systematic investigations.

The limitations and inconsistencies in previous studies inspired the experimental framework of Chapter 4. Unlike prior research, which often constrained investigations to narrow ranges of $K_{0}$, this study employs a broader spectrum of $K_{0}$ values and considers their influence across various stress conditions. By leveraging HCA, Chapter 4 aims to bridge the gaps in understanding and provide a more comprehensive assessment of how initial stress anisotropy impacts liquefaction resistance. The experimental design seeks to clarify the debated trends observed in previous studies and offer new insights into the microscopic mechanisms underpinning these macroscopic behaviors.

### Experimental apparatus

As shown in Fig. 4.1, the experimental apparatus is divided into five main components, each designed to fulfill a specific function in conducting hollow torsional shear tests: the Pressure control system, water injection and control system, Torsional shear apparatus, Servo pressure control system, and Data acquisition system.

![房间里有许多电脑 中度可信度描述已自动生成](thesis/assets/media/image103.png)

Fig. 4.1. Experimental apparatus: Pressure system, Water system, Torsional shear system, Servo system, Data acquisition system

#### Pressure control system

The Pressure Control System independently regulates four key pressures essential to the experimental setup: negative pressure, outer pressure, internal pressure, and back pressure. Negative pressure, provided by a vacuum pump, is critical during specimen preparation to ensure the membrane tightly adheres to the mold, allowing for precise control of specimen volume. Additionally, before pressurizing the chamber, negative pressure helps induce effective stress under atmospheric conditions, enabling the specimen to resist gravitational effects and deformation, which facilitates the installation of the shearing apparatus and pressure chamber. External pressure is applied to the outer surface of the hollow cylindrical specimen, while internal pressure is exerted on the inner hollow cylinder, both of which are carefully controlled during consolidation and shearing to apply confining stress. Back pressure, applied inside the membrane and connected to the specimen via a volume gauge, is adjusted in coordination with internal and external pressures to compress void spaces, enhance pore pressure, and increase the degree of saturation. This system is critical for achieving the stress conditions required in this study.

#### Water injection and control system

This component manages the flow of water into and out of the specimen. It includes pipelines, valves, and a volume gauge that allows precise measurement of volume changes during the back pressure application and consolidation processes. Degassed water is introduced to replace carbon dioxide in the specimen\'s pores, ensuring full saturation for undrained testing conditions.

#### Torsional shear apparatus

The Torsional shear apparatus consists of several critical components designed to apply and measure torsional forces on the specimen. These include the specimen base, an upper torsional loading cap with ribs to ensure effective shear force application, an axial loading rod, and tubes connecting the top and bottom of the specimen to the water system. Additionally, the apparatus is equipped with a pore water pressure gauge for monitoring internal pressure changes, a torsional displacement gauge for measuring rotational deformation, an axial displacement gauge for tracking vertical movement, and a pressure chamber to maintain controlled testing conditions. This setup ensures precise replication of stress and deformation behaviors under cyclic loading conditions.

#### Servo pressure control system

The servo system adjusts the hydraulic pressure based on the target torsional shear stress and axial stress, as well as the real-time torsional and axial stresses measured by sensors. By continuously regulating the hydraulic mechanism, it ensures the apparatus achieves the desired torsional shear stress and axial stress levels. The target stresses can be configured as cyclic loading patterns, and the intensity of the hydraulic loading can be fine-tuned by adjusting the gain factor.

#### Data acquisition system

The data acquisition system records and processes experimental measurements in real time. It collects data on stress, strain, pore water pressure, and specimen deformation during experimental stages, including the pre-consolidation process, axial loading process, undrained shear process, and post-liquefaction reconsolidation process. The data is then transferred to a computer for visualization and analysis, providing detailed insights into the soil\'s liquefaction behavior.

### Experimental procedures

#### Specimen preparation: Air pluviation method

The specimen preparation process begins with the installation of the inner and outer rigid molds, which have an inner diameter of 6 cm and an outer diameter of 10 cm. A membrane is carefully placed around the molds, and negative pressure is applied to ensure the membrane tightly adheres to the mold, maintaining the intended shape and volume of the specimen. The funnel is held approximately 26 cm above the surface of the specimen, as shown in Fig. 4.2 and sand is evenly distributed by moving

![图片包含 室内, 桌子, 厨房, 小 描述已自动生成](thesis/assets/media/image104.jpeg)

Fig. 4.2. Air pluviation method for generating specimen

the funnel in a circular motion at a uniform speed, completing each circle in about 10 seconds. After filling, a ruler is used to level the surface by removing any uneven portions. The final weight of the added sand is measured to calculate the relative density. If the relative density falls within the acceptable range around the target value, the specimen preparation is deemed successful.

#### Installation of the torsional shear apparatus

The installation process begins by placing the upper torsional shear cap, designed to apply torsional shear forces, onto the top of the specimen. The membrane is carefully attached to the cap to ensure a secure fit. Tubes are then connected between the valves

![图片包含 室内, 厨房, 搅拌机, 柜台 描述已自动生成](thesis/assets/media/image105.jpeg)

Fig. 4.3. Specimen with installed torsional shear cap after mold removal

and the specimen to facilitate the application of pressure. A negative pressure of -20 kPa is applied inside the specimen to induce sufficient effective stress, providing stability against gravitational deformation. With the specimen stabilized, the rigid molds are carefully removed as shown in Fig. 4.3.

Next, a transparent resin pressure chamber is installed onto the torsional shear apparatus. The chamber\'s valve is initially opened to connect it to atmospheric pressure, and water is injected into the chamber using the pressure control system. Once the chamber is filled, the valve connecting it to the atmosphere is closed, and the internal pressure of the chamber is increased to 20 kPa using the pressure system. At this stage, the valve connecting the negative pressure inside the specimen is closed, establishing an effective stress of 20 kPa on the specimen. This setup ensures the specimen is ready for subsequent stages of the experiment.

#### Saturation

Figure 4.4 illustrates the process of carbon dioxide saturation for the specimen. The specimen is housed within the transparent pressure chamber, and tubes are connected to its top and bottom. Carbon dioxide is introduced from the bottom of the specimen, while the top is connected to the atmosphere to allow for gas displacement. This setup ensures a controlled flow of carbon dioxide into the specimen, aiding in the removal of air from the pore spaces and preparing it for subsequent saturation with degassed water. The pressure chamber and connected components are configured to maintain the stability and integrity of the specimen during this process. The carbon dioxide is allowed to flow for over 30 minutes to ensure the specimen is fully saturated with carbon dioxide.

![](thesis/assets/media/image106.jpeg)

Fig. 4.4. Process of carbon dioxide saturation for the specimen

After this step, the tubes connecting the torsional apparatus and the water injection control system are reconnected. The valves are adjusted to link the top of the specimen to the vacuum chamber and the bottom of the specimen to the degassed water reservoir. A vacuum pump is then activated to draw degassed water into the specimen. The carbon dioxide filling the specimen facilitates a higher degree of saturation during this process, as it is displaced by the incoming water. This ensures the specimen achieves the necessary saturation level for undrained testing conditions.

#### Pre-consolidation

The top of the specimen is disconnected to the water injection system. The bottom of the specimen is then connected to the lower part of the volume gauge via the water control system, while the upper part of the volume gauge is linked to the back pressure chamber. At this point, the specimen is subjected only to the 20 kPa positive pressure from the pressure chamber, resulting in an effective stress of 20 kPa.

Subsequently, the back pressure and chamber pressure are simultaneously increased by 200 kPa using a synchronized control system. This step compresses any remaining air bubbles within the specimen, further enhancing the degree of saturation. With the external chamber pressure at 220 kPa and the internal pore water pressure at 200 kPa, the effective stress on the specimen remains 20 kPa. The connection between the specimen and the water injection system is then closed, placing the specimen in an undrained state. The chamber pressure is further increased to the target value, and the change in pore water pressure relative to the chamber pressure is used to calculate the B-value of the specimen. If the B-value exceeds 0.95, the specimen is considered fully saturated.

After determining the B-value, the data recording system is activated. The valve connecting the bottom of the specimen to the volume gauge is opened, allowing the pore water pressure within the specimen to gradually decrease to match the back pressure. The pre-consolidation process continues until the drainage volume stabilizes, ensuring the specimen is ready for subsequent experimental phases.

#### Axial Loading

This study aims to investigate the effect of the horizontal-to-vertical stress ratio on liquefaction resistance, requiring the application of additional axial pressure to achieve the target stress state. After calculating the required axial force, the data acquisition system is activated. The servo system\'s axial pressure control knob is adjusted slowly, while monitoring the axial displacement to prevent rapid deformation. Once the target axial force is reached, the loading rod is allowed to stabilize, ensuring the axial displacement remains steady. After stabilization, axial limit clamps are fixed onto the axial loading rod to prevent further vertical movement of the specimen during subsequent testing stages.

#### Undrained cyclic shear

The undrained cyclic shear process begins by closing the valve connecting the specimen to the volume gauge, ensuring the specimen is in an undrained state. The hydraulic servo system is then configured with the target parameters, including the peak value of the torsional load, the gain factor, and the maximum number of shear cycles. These settings prepare the system to apply sinusoidal shear loads to the specimen. The data acquisition system is activated, and the torsional shear process begins.

During cyclic shearing, the specimen undergoes progressive changes: the axial pressure gradually decreases, the pore water pressure increases steadily, and the torsional displacement incrementally grows. As the pore water pressure approaches the pressure chamber\'s value and the torsional shear deformation angle exceeds 10 degrees, indicating significant deformation, the torsional shear servo load is stopped. The data acquisition system is then deactivated, marking the completion of the undrained cyclic shear process.

#### Post-liquefaction reconsolidation

The Post-Liquefaction Reconsolidation Process begins following the undrained cyclic shear phase, during which the specimen retains elevated pore water pressure. The data recording system is activated, and the valve connecting the bottom of the specimen to the volume gauge is opened, allowing the pore water pressure to gradually return to its pre-shear level. This marks the completion of the reconsolidation process.

Once reconsolidation is complete, the back pressure and axial pressure are gradually unloaded, and the upper and lower limit clamps are removed. Subsequently, the system is dismantled in an orderly manner: the water in the pressure chamber is drained, the chamber pressure is released, and the torsional shear system along with the specimen is disassembled. Finally, the apparatus is cleaned and reset for the next experiment.

#### Data processing and analysis

During the data processing and analysis phase, key information is extracted from various stages of the experiment. This includes changes in pore water pressure and volume during the pre-consolidation process, variations in axial pressure and specimen volume during the axial loading phase, and fluctuations in torsional shear stress, torsional deformation, axial pressure, and pore water pressure throughout the cyclic shear process. Additionally, pore water pressure and volume changes during the post-liquefaction reconsolidation phase are recorded and analyzed. The collected data from specimens subjected to different $K_{0}$​ states is systematically organized and analyzed to discuss the influence of ​$K_{0}$ on liquefaction resistance and validate the conclusions drawn in simulations.

### Results and discussion

#### Overview of experimental cases

Table 4-1 summarizes the experimental parameters for the tested cases, covering a range of initial horizontal-to-vertical stress ratios ($K_{0}$​) from 0.20 to 3.00. These cases include isotropic stress conditions ($K_{0} = 1.0$) and a variety of anisotropic stress states ($K_{0} \neq 1.0$) to investigate the effects of stress anisotropy on liquefaction resistance.

Table 4-1. Summary of experiment parameters for different $K_{0}$ states

  -----------------------------------------------------------------------------------------------------------------------------------
  $$K_{0}$$   $$\sigma_{ax}(kPa)$$   $$\sigma_{lat}(kPa)$$   $$\sigma_{dif}(kPa)$$   $$F_{dif}(N)$$   $$B$$   $$m(g)$$   $$Dr(\%)$$
  ----------- ---------------------- ----------------------- ----------------------- ---------------- ------- ---------- ------------
  0.200       214.29                 42.86                   171.43                  861.69           0.97    699.86     58.45

  0.220       208.33                 45.83                   162.50                  816.81           0.99    692.29     54.71

  0.225       206.90                 46.55                   160.34                  805.98           0.91    699.00     58.03

  0.230       205.48                 47.26                   158.22                  795.30           0.97    691.18     54.16

  0.250       200.00                 50.00                   150.00                  753.98           0.93    696.89     56.99

  0.300       187.50                 56.25                   131.25                  659.73           0.94    695.00     56.06

  0.330       180.72                 59.64                   121.08                  608.64           0.95    689.15     53.14

  0.330       180.72                 59.64                   121.08                  608.64           0.95    688.13     52.62

  0.400       166.67                 66.67                   100.00                  502.66           0.92    689.80     53.47

  0.500       150.00                 75.00                   75.00                   376.99           0.95    703.45     60.19

  0.500       150.00                 75.00                   75.00                   376.99           0.94    689.75     53.44

  1.000       100.00                 100.00                  0.00                    0.00             0.95    688.50     52.81

  1.000       100.00                 100.00                  0.00                    0.00             0.90    690.42     53.78

  1.500       75.00                  112.50                  -37.50                  -188.50          0.99    696.78     56.94

  2.000       60.00                  120.00                  -60.00                  -301.59          0.96    701.14     59.07

  3.000       42.86                  128.57                  -85.71                  -430.85          0.94    691.00     54.07
  -----------------------------------------------------------------------------------------------------------------------------------

The axial stresses ($\sigma_{ax}$) range from 42.86 kPa to 214.29 kPa, while the lateral stresses ($\sigma_{lat}$) vary between 42.86 kPa and 128.57 kPa, resulting in differential stresses ($\sigma_{dif}$) spanning both positive and negative values. For instance, cases with $K_{0}$\<1.0 exhibit positive differential stresses, indicating higher axial stress relative to lateral stress, whereas cases with $K_{0}$\>1.0 show negative differential stresses due to the dominance of lateral stress. The $B$-values, which represent the degree of saturation of the specimen, are above 0.90, indicating effective specimen saturation. Cases with $B$-values exceeding 0.95 are considered fully saturated, ensuring reliable undrained test conditions.

Overall, this comprehensive range of $K_{0}$ values and associated stress conditions allows for a detailed investigation into how initial stress anisotropy influences liquefaction resistance and soil behavior during cyclic loading. This broad spectrum provides valuable insights into the transition from isotropic to anisotropic states and the resulting mechanical responses of the specimens.

#### Validation of experimental effectiveness through typical stress-strain relationships

Figure 4.5 illustrates the relationship between mean effective stress ($p'$) and shear stress ($\tau$) for the isotropic stress condition ($K_{0}$=1.0) during cyclic loading. Initially, as cyclic shearing progresses, $p'$ decreases steadily from approximately 100 kPa, reflecting the buildup of pore pressure. When $p'$ decreases to around 40 kPa, the relationship begins to exhibit a characteristic \"butterfly\" shape. In this stage, the cyclic

![图表 描述已自动生成](thesis/assets/media/image107.png)

Fig. 4.5. Relationship between mean effective stress ($p'$) and shear stress ($\tau$) for $K_{0} =$`<!-- -->`{=html}1.0

loading causes $p'$ to oscillate along with the shear stress, forming closed loops that reflect the alternating shear directions. Figure 4.6 presents shear stress $\tau$ versus shear strain $\gamma$ relationship, highlighting the development of hysteretic loops typical of cyclic loading. These loops reflect the progressive deformation and energy dissipation within

![图表, 直方图 描述已自动生成](thesis/assets/media/image108.png)

Fig. 4.6. Relationship between shear strain ($\gamma$) and shear stress ($\tau$) for $K_{0} =$`<!-- -->`{=html}1.0

the specimen. Figure 4.7 illustrates the evolution of pore water pressure over time during cyclic loading. The pore pressure increases incrementally with each shear cycle, eventually reaching a level comparable to the chamber pressure. This behavior aligns

![图表, 直方图 描述已自动生成](thesis/assets/media/image109.png)

Fig. 4.7. Pore water pressure evolution during cyclic shear for $K_{0}$=1.0

with the expected trend for undrained conditions and confirms the occurrence of liquefaction. The results depicted in Fig. 4.5, 4.6, and 4.7 demonstrate characteristic responses under cyclic shear, validating the reliability and effectiveness of the experimental procedures.

#### Influence of $K_{0}$​ on liquefaction resistance: a comparison

Figures 4.5, 4.8, and 4.9 present the evolution of $p'$ and $\tau$ during cyclic loading under varying initial $K_{0}$. These results reveal both consistent characteristics of liquefaction behavior and notable differences, suggesting a relationship between $K_{0}$ and liquefaction resistance.

![图表 描述已自动生成](thesis/assets/media/image110.png)

Fig. 4.8. Relationship between mean effective stress ($p'$) and shear stress ($\tau$) for $K_{0} =$`<!-- -->`{=html}0.25

![图表 描述已自动生成](thesis/assets/media/image111.png)

Fig. 4.9. Relationship between mean effective stress ($p'$) and shear stress ($\tau$) for $K_{0} =$`<!-- -->`{=html}0.20

Across all three cases, $p'$ initially decreases progressively with cyclic loading, reflecting the buildup of pore pressure. The characteristic \"butterfly\" shape emerges as $p'$ approaches lower values, indicating a consistent progression toward liquefaction across all $K_{0}$ values.

A key difference lies in the number of cycles required to reach liquefaction, as reflected by the density of lines in the figures: Figure 4.5 ($K_{0} = 1.0$) shows the least line density, indicating that liquefaction occurred with the fewest cycles. This suggests the lowest liquefaction resistance under isotropic stress conditions. Figure 4.8 **(**$K_{0}$**=**0.25**)** exhibits the highest line density, meaning the largest number of cycles was required to reach liquefaction. Figure 4.9 **(**$K_{0}$=0.20**)**, while still requiring more cycles than $K_{0}$=1.0, shows a slightly reduced line density compared to $K_{0}$=0.25. This suggests a decrease in liquefaction resistance as $K_{0}$​ decreases further from 0.25 to 0.20.

The results suggest a non-linear relationship between $K_{0}$ and liquefaction resistance. As $K_{0}$​ decreases from 1.0 (isotropic) to 0.25, liquefaction resistance increases, as evidenced by the greater number of cycles required for liquefaction. However, when $K_{0}$ further decreases from 0.25 to 0.20, liquefaction resistance slightly diminishes. This observation raises the hypothesis that liquefaction resistance may peak at a specific $K_{0}$​ value and subsequently decrease with further reductions in $K_{0}$​.

#### Liquefaction resistance across a broader range of $K_{0}$

Figure 4.10 illustrates the variation in the number of cycles required for liquefaction ($N_{L}$) as a function of $K_{0}$, with liquefaction defined as the point where pore water pressure reaches 95% of the initial confining pressure. The figure covers a broad range of ​$K_{0}$ values, from isotropic stress conditions ($K_{0}$=1.0) to highly anisotropic states ($K_{0}$=0.2 and $K_{0}$=3.0), allowing for a comprehensive analysis of the influence of stress anisotropy on liquefaction resistance.

![图表, 散点图 描述已自动生成](thesis/assets/media/image112.png)

Fig. 4.10. Liquefaction resistance for states with different $K_{0}$

As $K_{0}$decreases from the isotropic stress condition ($K_{0} = 1.0$), liquefaction resistance initially increases, reaching its first peak at $K_{0}$=0.25. This indicates that the dominance of axial stress enhances the soil's stability, likely due to better interlocking and alignment of particles under anisotropic stress conditions. However, as $K_{0}$​ is reduced further to 0.20, liquefaction resistance decreases slightly. This suggests that excessive axial stress dominance disrupts the favorable soil fabric, leading to a marginal reduction in resistance. Therefore, liquefaction resistance for $K_{0}$\<1.0 exhibits a peak at $K_{0}$=0.25, with diminishing resistance as $K_{0}$​ decreases further.

For $K_{0}$\>1.0, liquefaction resistance initially increases as $K_{0}$​ rises from the isotropic state, reaching a second peak at $K_{0}$=1.5. This indicates that moderate lateral stress dominance provides enhanced stability, potentially due to an optimal redistribution of stresses and improved structural support within the soil fabric. Beyond $K_{0}$=1.5, however, liquefaction resistance decreases as $K_{0}$​ increases further to $K_{0}$=2.0 and $K_{0}$=3.0. This reduction in resistance is likely caused by excessive lateral stress dominance, which may destabilize the soil structure and weaken its ability to resist liquefaction.

The observed results demonstrate that liquefaction resistance does not vary monotonically with $K_{0}$​. Instead, as $K_{0}$ transitions from isotropic ($K_{0}$=1.0) to anisotropic conditions ($K_{0}$\<1.0 or $K_{0}$\>1.0), liquefaction resistance first increases and then decreases, resulting in two distinct peaks. This trend underscores the complex interaction between stress anisotropy and soil fabric evolution. Moderate anisotropy in either axial or lateral stresses enhances resistance, while extreme anisotropy in either direction leads to a reduction in stability.

#### Comparison with numerical analysis and past studies

The experimental results presented in this chapter reveal that liquefaction resistance evolves in a non-monotonic manner with increasing stress anisotropy, displaying two distinct peaks. This pattern, characterized by an initial increase in resistance followed by a decrease as stress anisotropy develops, differs from the findings of the numerical analyses discussed in Chapter 3, where the highest liquefaction resistance was observed under isotropic stress conditions ($K_{0}$=1.0). However, an important agreement between the experiments and numerical simulations is observed in the behavior beyond the peak resistance: as stress anisotropy increases beyond the peak, liquefaction resistance consistently decreases, converging toward the critical state.

One plausible explanation for the differences lies in the definition of relative density. In laboratory experiments, the maximum and minimum relative densities are determined according to standardized testing procedures. Conversely, in DEM simulations, relative density is indirectly defined through particle properties and packing configurations, without strict standardization. For instance, in the numerical simulations discussed in Chapter 3, the minimum density was measured under a target confining stress of 10 kPa with particle friction coefficients of 0.5 (the same as used during shearing). This approach may lead to an underestimation of relative density, making the simulated samples more comparable to dense specimens in the experiments. As a result, the numerical conclusions might reflect a denser state than the experimental tests, potentially explaining why resistance in the isotropic state was highest in the simulations.

Previous experimental studies have typically focused on limited stress anisotropy conditions, such as $K_{0}$=1.0, $K_{0}$=0.5, and $K_{0}$=2.0, without examining how liquefaction resistance evolves across a broader $K_{0}$ range. The findings here suggest that the liquefaction resistance of these intermediate $K_{0}$ states depends critically on their position relative to the peak. If these anisotropic stress states lie between the peak and the isotropic state, they may exhibit greater liquefaction resistance than the isotropic state. If they fall beyond the peak, they might show lower, higher, or equal liquefaction resistance, depending on how close they are to the peak and the rate of resistance decline.

#### Discussion on K₀ \< 1.0 and K₀ \> 1.0

The experimental results reveal significant differences in how liquefaction resistance evolves for axial stress dominance ($K_{0}$\<1.0) and lateral stress dominance ($K_{0}$\>1.0), despite their similar overall trends of initially increasing with stress anisotropy, reaching a peak, and then decreasing.

For $K_{0}$\<1.0, the peak liquefaction resistance occurs at a higher level of stress anisotropy compared to $K_{0}$\>1.0. This indicates that soils under axial stress dominance can tolerate greater levels of anisotropy before reaching the maximum liquefaction resistance. In contrast, for $K_{0}$\>1.0, the peak liquefaction resistance occurs closer to isotropic conditions, suggesting a more limited range of stability as lateral stress dominance develops. The peak liquefaction resistance for $K_{0}$\<1.0 corresponds to a significantly higher number of cycles compared to $K_{0}$\>1.0. This demonstrates that soils under axial stress dominance exhibit greater resistance to liquefaction.

The differences in liquefaction resistance between $K_{0}$\<1.0 and $K_{0}$\>1.0 can be explained by the directionality of fabric development. For $K_{0}$\<1.0, vertical fabric alignment provides greater and more sustained stability, resulting in a later peak and a broader range of resistance exceeding the isotropic state. In contrast, the horizontal alignment of contacts for $K_{0}$ leads to a peak closer to isotropic conditions and a more limited range of superior resistance. These findings emphasize the critical role of fabric direction in determining liquefaction behavior.

### Summary

This chapter presented a detailed investigation into the effects of the initial stress anisotropy on the liquefaction resistance of soils, using experimental results from hollow torsional shear tests. The findings reveal that liquefaction resistance is not a monotonic function of $K_{0}$​, but rather follows a non-monotonic trend with two distinct peaks, dependent on the degree and direction of stress anisotropy.

(1) Liquefaction resistance increases with stress anisotropy up to a peak, after which it decreases as stress anisotropy develops further. This trend is consistent for both $K_{0}$\<1.0 (axial stress dominance) and $K_{0}$\>1.0 (lateral stress dominance), but with notable differences in the magnitude and location of the peaks. The trend characterized by an initial increase in resistance followed by a decrease as stress anisotropy develops differs from the findings of the numerical analyses discussed in Chapter 3, where the highest liquefaction resistance was observed under isotropic stress conditions ($K_{0}$=1.0).

(2) For $K_{0}$\<1.0, the peak resistance occurs at a higher level of stress anisotropy and corresponds to a greater number of cycles, indicating higher liquefaction resistance. For $K_{0}$\>1.0, the peak resistance is observed closer to isotropic state, with a smaller number of cycles at the peak. This suggests that soils under lateral stress dominance are less resistant to liquefaction compared to those under axial stress dominance. For $K_{0}$\<1.0, Chapter 3 showed that particle contacts align more vertically, perpendicular to the shear stress direction. This vertical alignment enhances the soil's ability to resist pore pressure buildup and deformation, contributing to the higher resistance and broader range of stability observed in experiments. For $K_{0}$\>1.0, the contact orientations tend to align more horizontally, parallel to the shear stress. This horizontal alignment is less effective at resisting liquefaction, leading to lower resistance and a narrower stability range.

(3) The results highlight the limitations of simply comparing anisotropic and isotropic stress conditions. Past studies often examined a limited number of stress states, such as $K_{0}$=1.0, $K_{0}$=0.5, and $K_{0}$=2.0, without considering the full range of stress anisotropy or how resistance evolves with it. This study demonstrates that liquefaction resistance is influenced not only by the anisotropic state itself but also by the initial conditions, such as relative density.

# Effects of Multi-Directional Shear Stress on Liquefaction Resistance 

A 3D discrete element method (DEM) was used to simulate the liquefaction process under cyclic loading with multi-directional shear stress paths. Compared to previous approaches that primarily compared unidirectional and multidirectional loading patterns, the newly proposed method, which contrasts the 8-like and double 8-like stress paths, offers the following advantages: First, both the 8-like and double 8-like paths maintain equal stress magnitudes throughout the simulation. Second, the shear stress variation rates in both paths remain consistent and smooth, eliminating the influence of stress variation rate on liquefaction resistance. Moreover, in the double 8-like loading mode, the major axis periodically rotates, allowing for an investigation of the influence of shear stress directionality on liquefaction resistance.

## Introduction

Soil is subjected to a complex three-dimensional stress state during seismic loadings. To simulate the liquefaction process under seismic conditions, horizontal loading is often simplified to unidirectional cyclic loading due to the limitations of laboratory testing equipment. However, such simplification raised concerns about underestimating the impact of multi-directional cyclic shear on liquefaction resistance. Findings by Ishihara and Yamazaki (1980) indicated that multi-directional shear with equal amplitude in different directions requires only about 70% of the cyclic stress ratio of unidirectional shear to achieve the same shear strain. To better understand the role of multidirectional shear conditions on liquefaction, Kammerer et al. (2005) conducted simple shear tests on Monterey 0/30 Sand with varying relative densities and initial shear stresses, using linear, oval/circular, and figure-8 shaped loading paths. The results demonstrated that, compared to equivalent unidirectional shear with the same relative density and cyclic stress ratio, multidirectional shear induced faster liquefaction. The rotation of stresses in multidirectional shear likely accounts for the more pronounced build-up of pore pressure.

In addition to laboratory experiments, model tests have also provided evidence of the susceptibility of liquefaction behavior to multidirectional shaking. Pyke et al. (1975) found that multidirectional shaking on dry sand caused greater settlement and required less stress to induce liquefaction compared to unidirectional shaking. Results from Su and Li\'s (2008) centrifuge experiments indicate that, compared to unidirectional shaking, multi-directional shaking accelerates excess pore water pressure build-up as depth increases. A series of centrifuge tests conducted by El Shafee et al. (2017) compared uniaxial and biaxial excitations, showing that an increase of 40% in the uniaxial shaking amplitude was required to produce a similar excess pore water pressure response to that of biaxial shaking. This suggests that the common practice of increasing uniaxial shaking amplitude by 10% to approximate 2D shaking effects underestimates the true response of multidirectional shaking on soil liquefaction behavior.

Wei et al. (2020) investigated the effects of different shear stress paths, including unidirectional, oval, circular, and figure-8, on the number of cycles to liquefaction using DEM from the perspective of micro-scale fabric evolution. They found that the stress ratio in different directions and the shear path significantly influenced the number of cycles required to reach initial liquefaction, and fabric anisotropy evolved progressively throughout the liquefaction process. Yang et al. (2022) also explored the factors influencing the number of cycles to liquefaction in DEM simulations using similar unidirectional and multidirectional shear stress paths. They found that the figure-8 stress path required fewer cycles to reach liquefaction compared to the circular stress path. The coordination number and particle connectivity revealed that the system becomes temporarily under-constrained during 1-D linear and figure-8 shear paths at the moment when mean stress vanishes, whereas it remains over-constrained under 2-D linear and circular shear paths.

These studies have made significant contributions to understanding liquefaction by comparing unidirectional and multidirectional shear stress paths and their influence on liquefaction resistance. However, the methodologies used remain questionable. For instance, despite maintaining the same maximum shear force, the magnitude of unidirectional and multidirectional shear stress differs throughout the shear process. On the other hand, 2D shear paths like oval or circular maintain shear forces, preventing the effective stress from reaching zero. In contrast, unidirectional and figure-8 shear paths allow the effective stress to repeatedly cycle to zero, making it difficult to evaluate the impact of shear stress direction on liquefaction based on stress criterion. These factors introduced additional factors influencing the liquefaction, complicating the assessment of the specific influence of stress direction on the liquefaction process. Therefore, this chapter aims to present an improved approach that minimizes these limitations to explore whether changes in direction of shear stress affect the liquefaction behavior under different cyclic shear.

## DEM simulation setup

### Specimen preparation

The discrete element method (DEM) simulates the mechanical response of granular materials, such as sand, by calculating the interparticle contacts and the motion of individual particles. This approach effectively overcomes the limitations of laboratory experiments, where replicating the same initial state for comparative analyses can be challenging. Additionally, DEM enables the application of multi-directional shear and the use of periodic boundaries, which mimic the continuous conditions in natural soil. In this study, the software Itasca PFC3D was used to simulate simple shear tests on granular sand. The rolling resistance contact model was employed to replicate the inter-particle interactions of non-spherical sand grains.

![图表, 折线图 描述已自动生成](thesis/assets/media/image113.png)

Fig. 5.1. Grain size distribution of curves of Toyoura sand and DEM simulation

![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image114.png)

Fig. 5.2. Particle and contact force distribution after initial compaction, along with boundary and shearing rib configuration

As shown in Fig. 5.1, spherical particles with diameters ranging from 1.0 to 3.0 mm, approximating the distribution of Toyoura sand, were generated within a cubic space enclosed by periodic boundaries. Sample compaction was then achieved by adjusting the positions of ribbed shear walls oriented in the vertical direction and periodic boundaries in the horizontal directions, using a servo mechanism for the compaction process. A sample in an isotropic stress state, with all three principal stresses set to 100 kPa, was prepared for subsequent undrained cyclic shear tests as shown in Fig. 5.2.

### Application of unidirectional and multidirectional shear force

In studying the effects of multidirectional shear loading on the liquefaction process, other factors, such as changes in the magnitude of shear force, were often introduced. The primary aim of this chapter is to minimize the influence of these additional factors when modifying the direction of shear stress. Inspired by previous studies, this research employs a single-8 pattern for the first type of multidirectional shear. As shown in Eqs (5-1) and (5-2), and Fig. 5.3 (c), the single-8 multidirectional shear loading consists of a sinusoidal component $\tau_{8,\ \ x}$ in the x-direction and a sinusoidal component $\tau_{8,\ \ y}$ in the y-direction, with the amplitude being half of that in the x-direction and the period being half of the x-direction's cycle.

$\tau_{8,\ \ x} = CSR\sin\left( \frac{t}{T} \right)p_{0}'$ (5-1)

$\tau_{8,\ \ y} = 0.5CSR\sin\left( \frac{2t}{T} \right)p_{0}'$ (5-2)

To more quantitatively evaluate the impact of multidirectional shear loading compared to unidirectional loading on the liquefaction process, the unidirectional shear stress $\tau_{uni,x}$ is defined to equal the total magnitude of the multidirectional shear stress, and its sign is unified with that of $\tau_{8x}$, as shown in Eq. (5-3) and Fig. 5.3 (a) and (b). By ensuring the unidirectional and multidirectional figure-8 shear stresses have the same magnitude throughout the cyclic shear, the only difference between them is their direction.

$\tau_{uni,x} = sign\left( \tau_{8,x} \right)\sqrt{\tau_{8,x}^{2} + \tau_{8,y}^{2}}$ (5-3)

Although the magnitudes of unidirectional and multidirectional single-8 shear stresses are controlled to be equal, the multidirectional shear not only experiences variations in the shear force magnitude but also undergoes continuous changes in direction. This results in completely different rates of change between the two types of shear forces. This study introduces a new double-8 shear loading method to eliminate the impact of differing shear stress variation rates during undrained shear processes. In odd-numbered cycles, the double-8 shear stress has the same x and y components as the standard single-8 pattern. However, in even-numbered cycles, the x and y components are swapped, with the x component equaling the y component of the single-8, and vice versa. As the cycles progress, the double-8 axes of the shear stress periodically alternate between odd and even cycles, as described by Eqs (5-4) and (5-5) and Fig. 5.3(d).

$\tau_{d8,x} = \left\{ \begin{array}{r}
\tau_{8,x},2nT < t \leq (2n + 1)T,\ n \in \{ 0,1,2,\ldots\} \\
\tau_{8,y},(2n + 1)T < t \leq 2(n + 1)T,\ n \in \{ 0,1,2,\ldots\}
\end{array} \right.\ $ (5-4)

$\tau_{d8,y} = \left\{ \begin{array}{r}
\tau_{8,y},2nT < t \leq (2n + 1)T,\ n \in \{ 0,1,2,\ldots\} \\
\tau_{8,x},(2n + 1)T < t \leq 2(n + 1)T,\ n \in \{ 0,1,2,\ldots\}
\end{array} \right.\ $ (5-5)

The introduction of a comparison between the double-8 shear loading and the single-8 shear loading provides several benefits. First, it ensures that the magnitude of the two multidirectional shear stresses always remains equivalent. Second, it maintains similarity in the change rate of shear stress: during odd-numbered cycles, the change rate of the double-8 loading matches that of the single-8 loading, while during even-numbered cycles, the change rates are opposite but share the equal magnitudes.

![图表, 折线图, 直方图 描述已自动生成](thesis/assets/media/image115.png)![图表 描述已自动生成](thesis/assets/media/image116.png)

(a) Unidirectional shear stress evolution

\(b\) Unidirectional shear stress path

![图表, 折线图 描述已自动生成](thesis/assets/media/image117.png)![图表 描述已自动生成](thesis/assets/media/image118.png)

\(c\) Single-8 shear stress path

\(d\) Double-8 shear stress path

Fig. 5.3. Shear stress path in unidirectional and multidirectional loading

Finally, the phase change between odd and even cycles for double-8 results in an equivalent rate in two directions, ensuring a smooth transition in shear stress. Through this comparative analysis, other factors that may influence liquefaction can be effectively excluded, allowing for a more rational evaluation of the impact of shear direction on the liquefaction process.

## Results and discussion

### Macroscopic response

#### Stress strain relationship

With the application of unidirectional and multidirectional cyclic shear loads to undrained samples, the mean effective stress $p'$ gradually decreases as shown in Fig. 5.4. When $p'$ drops below approximately 50% of its initial value, an increase in shear load causes a slight rise in $p'$, while a decrease in shear load leads to a significant reduction in $p'$, eventually resulting in liquefaction as $p'$ reaches zero. Even as $p'$ continuously varies, the shear patterns of unidirectional, single-8, and double-8 modes project onto $\tau_{x}$ and $\tau_{y}$ as anticipated, effectively maintaining their respective linear, single-8, and double-8 stress path shapes.

Figure 5.5 presents the liquefaction resistance under different forms of shear loading. The occurrence of liquefaction is defined as when the pore water pressure reaches 95% of the initial confining stress. It is evident that the unidirectional shear loading requires the highest cyclic number to reach liquefaction at the same CSR, compared to the multidirectional loadings. Following this, there is a difference between the required cyclic numbers for single-8 and double-8 shear stresses, with single-8 needing slightly more cycles than double-8. For instance, at CSR = 0.25, single-8 requires 30 cycles to reach liquefaction, whereas double-8 only requires about 22 cycles.

+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ![图表, 雷达图 描述已自动生成](thesis/assets/media/image119.jpeg) | ![图表 描述已自动生成](thesis/assets/media/image120.jpeg) |
+===============================================================================================================================+=======================================================================================================================+
| (a) Unidirectional loading                                                                                                    | (b) Single-8 loading                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ![图表 描述已自动生成](thesis/assets/media/image121.jpeg)         |                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| \(c\) double-8 loading                                                                                                        |                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

Fig. 5.4. Shear and mean effective stress evolution in unidirectional and multidirectional shear (CSR=0.250)

From a macroscopic perspective, the rotation of shear force direction has a significant impact on the liquefaction process. Although the magnitudes of unidirectional and multidirectional shear forces are equal at any given moment, the shear force direction in unidirectional loading remains fixed, unlike in multidirectional loading. This lack of directional rotation in unidirectional loading results in a higher number of cycles needed to reach liquefaction. Additionally, besides the influence of shear stress direction on the liquefaction process, the shear loading history also plays a role. For instance, although single-8 and double-8 paths share the same shear stress magnitude and rate of change at any given moment, the single-8 path maintains a

![图表, 散点图 描述已自动生成](thesis/assets/media/image122.png)

Fig. 5.5. Liquefaction resistance under unidirectional and multidirectional shear stress

constant figure-8 orientation, while the double-8 path alternates its orientation with each odd and even cycle. This alternating orientation in the double-8 path results in a lower number of cycles needed to reach liquefaction. In addition to differences in the number of cycles required for liquefaction, the strain development behaviors of single-8 and double-8 also differ, as shown in Fig 5.6. As cyclic loading continues, both single-8 and double-8 shear paths exhibit figure-8 patterns in their strain development. However, distinct differences emerged in the two shear paths. The strain path under single-8 shear stress maintains a consistent orientation throughout the cycles, with each cycle expanding outward along both $\gamma_{zx}$ and $\gamma_{zy}$ directions. This results in a steady accumulation of strain that gradually shifts in a direction perpendicular to the primary single-8 axis. The strain path for double-8 stress alternates orientation with each cycle, causing the \"8-shape\" axis to shift periodically. As a result, the double-8 pattern shows more complex and irregular strain growth compared to the single-8 path, with less directional offset over time.

![图表 描述已自动生成](thesis/assets/media/image123.jpeg)![图表 描述已自动生成](thesis/assets/media/image124.jpeg)

(a) Strain evolution in single-8 loading

\(b\) Strain evolution in single-8 loading

Fig. 5.6. Comparison of strain evolution between single-8 and double-8 loading

#### Cumulative shear work

Shear work, defined as the work performed by the shearing rib on the specimen during cyclic loading, provides a scalar measure to evaluate liquefaction differences across various shear stress paths from a macroscopic perspective. In Fig. 5.7, before the EPWP reaches approximately 60 kPa, the double-8 path shows the highest EPWP at equivalent shear work levels, followed by single-8 path, with unidirectional path exhibiting the lowest EPWP. This order of EPWP increase is inversely related to the number of cycles required to reach liquefaction, with double-8 reaching liquefaction faster than single-8, and unidirectional taking the longest. Despite these differences, the shear work required to reach liquefaction is roughly similar across all three loading types. This indicates that while directional variations in shear stress influence the rate at which EPWP builds up, the total energy input needed to induce liquefaction remains consistent.

![图表 描述已自动生成](thesis/assets/media/image125.jpeg)

Fig. 5.7. Cumulative shear work evolution in liquefaction under unidirectional, single-8, and double-8 cyclic shear stress

### Microscopic interpretation

#### Evolution of coordination number

The coordination number is a key indicator of the microstructural characteristics, representing the average number of contacts per particle. Particles with fewer than two contact are considered unable to effectively transmit contact forces and therefore do not contribute to the skeletal microstructure of the granular material. These particles are identified as \"floaters\" and are excluded from the coordination number calculation, as shown in Eq. (5-6). Here, $Z_{m}$ denotes the mechanical coordination number. $N_{c}$ is​ the total number of contacts, and $N_{p}$​, $N_{1}$, and $N_{0}$ represent the total number of particles, particles with one contact, and particles with zero contacts, respectively.

$Z_{m} = \frac{2N_{c} - N_{1}}{N_{p} - N_{1} - N_{0}}$ (5-6)

![图表, 散点图 描述已自动生成](thesis/assets/media/image126.png)

Fig. 5.8. Coordination number evolution in liquefaction under unidirectional, single-8, and double-8 cyclic shear stress

The evolution of $Z_{m}$​ under different shear stress paths shows distinct patterns. Initially, the three shear stress types exhibit large $Z_{m}$ around 5.00, indicating a well-structured granular skeleton with significant interparticle contacts. As cyclic shear progresses and the cyclic number normalized by the total cycles $N_{cyc}/N_{L}$​ approaches 1.0, the coordination number decreases in all cases, reflecting structural degradation and the approach toward liquefaction. However, the rate and extent of $Z_{m}$ reduction differ among the three shear stress types.

The unidirectional shear stress maintains a relatively higher coordination number compared to single-8 and double-8 stresses throughout the process, suggesting greater structural integrity under unidirectional cyclic loading. Single-8 shear exhibits a moderate decrease, compared to double-8, which shows the most rapid reduction in $Z_{m}$, indicating that the double-8 stress path leads to more frequent structural rearrangements and a weaker granular skeleton.

This difference in $Z_{m}$ evolution helps explain the varying cyclic numbers required to reach liquefaction under different shear paths. The unidirectional path, with its relatively stable $Z_{m}$, requires the highest cycles to induce liquefaction. In contrast, the double-8 path, with its rapid $Z_{m}$ loss, reaches liquefaction more quickly, requiring fewer cycles. The single-8 path falls in between, requiring a moderate number of cycles to liquefy. This trend aligns with the increased instability and structural degradation induced by complex shear paths like double-8.

#### Evolution of fabric anisotropy

In addition to coordination number, which describes isotropic contact in the microstructure, the directional characteristics within granular materials are also worth considering. To capture this directionality, the fabric tensor is employed. Eq. (5-7) defines the fabric tensor $\mathbf{\Phi}_{\mathbf{ij}}$*,* calculated as the average of the product of contact normal vectors $n_{i}$​ and $n_{j}$ over all contacts $N_{c}$​. This tensor quantifies the orientation of contacts within the material.

$\mathbf{\Phi}_{\mathbf{ij}} = \ \frac{1}{N_{c}}\Sigma\mathbf{n}_{\mathbf{i}}\mathbf{n}_{\mathbf{j}}$ (5-7)

Eq. (5-8) introduces the anisotropic fabric tensor $\mathbf{F}_{\mathbf{ij}}$, which adjusts $\mathbf{\Phi}_{\mathbf{ij}}$​ using the Kronecker delta $\mathbf{\delta}_{\mathbf{ij}}$ to emphasize directional dependencies in the contact network, revealing anisotropic characteristics in the material\'s structure.

$\mathbf{F}_{\mathbf{ij}} = \frac{15\left( \mathbf{\Phi}_{\mathbf{ij}} - \mathbf{\delta}_{\mathbf{ij}} \right)}{2}$ (5-8)

Eq. (5-9) present**s the** invariant of the anisotropic fabric **tensor** $F_{c}$, calculated from $\mathbf{F}_{\mathbf{ij}}$**​**, representing the magnitude of anisotropy as a scalar. This invariant encapsulates the overall degree of anisotropy in the contact fabric.

$F_{c} = \sqrt{\frac{3}{2}\mathbf{F}_{\mathbf{ij}}\mathbf{F}_{\mathbf{ij}}}$ (5-9)

![图表, 直方图 描述已自动生成](thesis/assets/media/image127.png)

Fig. 5.9. Invariant of anisotropic fabric tensor evolution in liquefaction under unidirectional, single-8, and double-8 cyclic shear stress

Figure 5.9 illustrates the evolution of fabric anisotropy $F_{c}$ under unidirectional, single-8, and double-8 shear stress paths throughout the liquefaction process. As the normalized cyclic number $N_{cyc}/N_{L}$ increases, $F_{c}$ first rises to a peak value before decreasing to a lower level. With each successive cycle, the peak values continue to increase, showing a gradual upward trend as liquefaction approaches. This cyclic oscillation pattern, with peaks that grow progressively higher, reflects the increasing anisotropy in the microstructure induced by continuous cyclic shearing.

The double-8 path demonstrates the highest level of anisotropy development, with $F_{c}$ reaching the largest value. This indicates that frequent directional changes enhance contact alignment and orientation, fostering an increasingly anisotropic structure within the particle assembly. This intensified anisotropy likely contributes to double-8's lower liquefaction resistance, as seen by its fewer cycles to reach liquefaction. The single-8 path exhibits intermediate anisotropy levels, with $F_{c}$ values between those of double-8 and unidirectional. The pattern allows for some anisotropic structural formation, though less intense than in double-8. This aligns with the single-8\'s liquefaction resistance, requiring more cycles than double-8 but fewer than unidirectional. The unidirectional path exhibits the lowest increase in fabric anisotropy, with $F_{c}$ consistently lower compared to the other two paths. The absence of directional changes limits the rearrangement of particles, preserving a more isotropic structure that can better withstand cyclic loading, thus requiring the largest number of cycles to achieve liquefaction.

#### Contact orientation

Fig. 5.10, 5.11, and 5.12 display the contact density distribution for the unidirectional, single-8, and double-8 shear paths throughout the liquefaction process, respectively. Each sequence shows how the contact density evolves from an initial state (at $N_{c}/N_{L}$=0) to stages closer to (at $N_{c}/N_{L}$=0.81) and beyond liquefaction (at $N_{c}/N_{L}$=1.03 and 1.08)​, highlighting the distinctions in fabric evolution among these paths. Across all shear paths, the contact density reduces, indicating a loosening in the particle arrangement. The contact orientations become more pronounced, showing a tendency toward specific directional alignment, which reflects a strengthening of anisotropic characteristics within the skeleton of fabric.

![图表, 雷达图 描述已自动生成](thesis/assets/media/image128.png)![图表, 雷达图 描述已自动生成](thesis/assets/media/image129.png)

(a) $N_{c}/N_{L}$=0.0

(b) $N_{c}/N_{L}$=0.81

![图表 描述已自动生成](thesis/assets/media/image130.png)![图表 描述已自动生成](thesis/assets/media/image131.png)

(c) $N_{c}/N_{L}$=1.03

(d) $N_{c}/N_{L}$=1.08

Fig. 5.10. Contact density evolution in liquefaction under unidirectional cyclic shear stress

At the stage of $N_{c}/N_{L}$=0.81, notable differences emerge among the three shear paths, reflecting their distinct responses to shear stress. For unidirectional path, contact density remains relatively uniform with limited directionality, indicating a weaker development of anisotropy compared to the other two paths. This is consistent with the previously observed lower fabric anisotropy $F_{c}$​, suggesting that the unidirectional path promotes a more isotropic structure, contributing to its higher liquefaction resistance.

![图表, 雷达图 描述已自动生成](thesis/assets/media/image132.png)![图表 描述已自动生成](thesis/assets/media/image133.png)

(a) $N_{c}/N_{L}$=0.0

\(b\) $N_{c}/N_{L}$=0.81

![图表 描述已自动生成](thesis/assets/media/image134.png)![图表 描述已自动生成](thesis/assets/media/image135.png)

\(c\) $N_{c}/N_{L}$=1.03

\(d\) $N_{c}/N_{L}$=1.08

Fig. 5.11. Contact density evolution in liquefaction under single-8 cyclic shear stress

For single-8 case, contact density shows moderate alignment along certain directions, revealing an intermediate degree of anisotropy. The contact density distribution is less uniform than in the unidirectional path but not as concentrated as in the double-8 path. This intermediate anisotropy level aligns with the fabric tensor $F_{c}$​ observed for single-8, reflecting moderate liquefaction resistance. For double-8 pattern, contact density exhibits more pronounced alignment in contact density and the highest degree of fabric concentration among the three paths. This is consistent with the high $F_{c}$ for double-8, as the directional changes in the shear path enhance the formation of an anisotropic structure.

![图表, 雷达图 描述已自动生成](thesis/assets/media/image136.png)![图表 描述已自动生成](thesis/assets/media/image137.png)

(a) $N_{c}/N_{L}$=0.0

(b) $N_{c}/N_{L}$=0.81

![图表 描述已自动生成](thesis/assets/media/image138.png)![图表 描述已自动生成](thesis/assets/media/image139.png)

(c) $N_{c}/N_{L}$=1.03

(d) $N_{c}/N_{L}$=1.08

Fig. 5.12. Contact density evolution in liquefaction under double-8 cyclic shear stress

After liquefaction, the differences in anisotropy among the three paths become less pronounced. However, a unique feature of the double-8 path is observed: The anisotropic alignment in the double-8 path shows a slight orientation toward the y-axis. This directional bias corresponds with the alternating stress direction characteristic of the double-8 path, where shear stress periodically changes direction in an \"8\" pattern. This alignment further reflects the macroscopic behavior of the double-8 path, where directional shifts in stress promote specific structural adaptations at the particle level.

### Discussion based on anisotropic critical state theory

The classical critical state theory provides foundational insight into the behavior of granular materials under large shear deformations. According to this theory, granular assemblies reach a \"critical state\" where both the void ratio and the stress ratio stabilize under continuous shear strain, maintaining constant values at a given principal stress. This theory has been widely used to describe the macroscopic characteristics of granular materials in soil mechanics and geotechnical engineering.

However, classical critical state theory does not explicitly account for the evolution of fabric anisotropy observed in granular materials. To address this, the anisotropic critical state theory extends the classical framework by integrating directional fabric properties and considering anisotropy as a critical factor influencing the material response.

## Summary

Chapter 5 delves into the influence of multi-directional shear stress paths on the liquefaction resistance of granular materials. Using numerical simulations, this chapter introduces innovative shear stress paths to isolate and analyze the impacts of directional changes. The findings highlight critical insights into how shear stress directionality alters both macroscopic and microscopic behaviors:

The unidirectional shear loading requires the highest cyclic number to reach liquefaction at the same CSR, compared to the multidirectional loadings. Single-8 needs slightly more cycles than double-8.

Although single-8 and double-8 paths share the same shear stress magnitude and rate of change at any given moment, the single-8 path maintains a constant figure-8 orientation, while the double-8 path alternates its orientation with each odd and even cycle. This alternating orientation in the double-8 path results in a lower number of cycles needed to reach liquefaction.

The directional shifts in stress under the double-8 shear pattern induce more pronounced structural adjustments at the particle level. These adjustments contribute to an accelerated liquefaction process.

# Conclusions and Future Studies

## Conclusions

This dissertation bridges the gap between microscopic behaviors and macroscopic phenomena in granular materials, with a particular focus on liquefaction resistance. By leveraging the Discrete Element Method (DEM) as a primary tool, the research addresses longstanding challenges in understanding the complex interplay of particle-scale interactions, stress anisotropy, and liquefaction resistance.

The subsequent chapters detail contributions that address these objectives, exploring a range of phenomena from stress anisotropy to cyclic liquefaction processes. This conclusion consolidates the key findings of each chapter and highlights their implications for future research and practical applications.

**Chapter 2. Fabric Evolution under General Stress States**

Chapter 2 explores the evolution of granular fabric under diverse stress states using monotonic drained true triaxial shear tests. Through DEM simulations, the study systematically investigates how stress anisotropy influences microscopic structural adjustments, such as contact normal distributions, and their impact on macroscopic behavior. The chapter quantifies changes in key fabric descriptors (e.g., coordination number, contact orientation) under general stress states, providing insights into how stress anisotropy governs fabric restructuring.

(a) No unique CSL in the *e* - *p* space was observed, and the void ratio under the critical state exhibited dependence on the intermediate principal stress ratio. An apparent unique CSL existed in the $Z$ -- $p'$ space, indicating that $Z$ is independent of the intermediate principal stress ratio. *F~c~* under the critical state was investigated in the $F_{c}$ -- $p'$ space, where $F_{c}$ decreases with increasing $p'$ and Lode angle.

(b) The contact density distribution of triaxial compression changed, becoming an elongated cylinder with a contracted body whose long axis pointed in the direction of the major principal stress. The contact density distribution of the triaxial extension appeared as a dimpled flat pie with the concave oriented toward the direction of the minor principal stress. The distributions of the in-between paths were transition states between triaxial compression and extension.

(c) The difference in the morphologies of contact density microscopically accounted for the uniqueness of CSL in the $Z$-- *p'* space and the nonuniqueness of CSL in the $e$ -- $p'$ space. The pie-like distribution in triaxial extension resulted in a larger void ratio than that of the cylindrical distribution in triaxial compression, despite the coordination number under the equal mean principal effective stress being the same.

This chapter sets the foundation for understanding granular behavior under realistic loading scenarios, paving the way for subsequent chapters that delve into liquefaction resistance and complex multi-directional stress paths.

**Chapter 3. Study on Factors Affecting Liquefaction Resistance during Anisotropic Consolidation**

Chapter 3 pioneers the application of DEM to replicate hollow cylinder apparatus (HCA) stress paths, marking the first successful simulation of undrained HCA tests. This chapter bridges the gap between experimental and DEM approaches in liquefaction studies, offering a powerful tool for analyzing the mechanisms governing liquefaction resistance under anisotropic stress states.

The chapter investigates the role of fabric evolution during anisotropic consolidation, highlighting how changes in coordination number and contact orientation influence liquefaction resistance. The findings are summarized as follows:

(a) Initial stress anisotropy, represented by $K_{0}$, results in reduced liquefaction resistance. The protocols for specimen preparation does not significantly impact liquefaction resistance.

(b) Greater initial stress anisotropy is associated with a lower initial mechanical coordination number $Z_{m0}$. A correlation is observed between $Z_{m0}$ and the cyclic number required for liquefaction $N_{L}$, which indicates liquefaction resistance, providing a microscopic explanation for the influence on liquefaction strength. In addition to $Z_{m0}$, a smaller void ratio, which evaluates the macroscopic compactness, contributes to liquefaction resistance as well.

(c) Greater liquefaction resistance was confirmed for $K_{0}$\<1.0 than that for $K_{0}$\>1.0. In the $\alpha_{0}$-$Z_{mi}$-$N_{L}$ space, as stress anisotropy increases, the predicted relationship for $K_{0}$\<1.0 and $K_{0}$\>1.0 further diverged, producing a positive $\eta$ in the fitted surface.

(d) Anisotropic consolidation states with $K_{0}$\<1.0 or $K_{0}$\>1.0 produce different morphologies of contact density, potentially influencing liquefaction resistance.

**Chapter 4. Experimental Validation of K~0~ Effects on Liquefaction Resistance**

In Chapter 4, an investigation into the effects of the initial stress anisotropy on the liquefaction resistance is presented, using experimental results from hollow torsional shear tests. The findings reveal that liquefaction resistance is not a monotonic function of $K_{0}$​, but rather follows a non-monotonic trend with two distinct peaks, dependent on the degree and direction of stress anisotropy. The trend characterized by an initial increase in resistance followed by a decrease as stress anisotropy develops differs from the findings of the numerical analyses discussed in Chapter 3, where the highest liquefaction resistance was observed under isotropic stress conditions ($K_{0}$=1.0).

For $K_{0}$\<1.0, the peak liquefaction resistance occurs at a higher level of stress anisotropy compared to $K_{0}$\>1.0. This indicates that soils under axial stress dominance can tolerate greater levels of anisotropy before reaching the maximum liquefaction resistance. In contrast, for $K_{0}$\>1.0, the peak liquefaction resistance occurs closer to isotropic conditions, suggesting a more limited range of stability as lateral stress dominance develops. The peak liquefaction resistance for $K_{0}$\<1.0 corresponds to a significantly higher number of cycles compared to $K_{0}$\>1.0. This demonstrates that soils under axial stress dominance exhibit greater resistance to liquefaction.

**Chapter 5. Effects of Multi-Directional Shear Stress on Liquefaction Resistance**

Chapter 5 delves into the influence of multi-directional shear stress paths on the liquefaction resistance of granular materials. Using numerical simulations, this chapter introduces innovative shear stress paths to isolate and analyze the impacts of directional changes. The findings highlight critical insights into how shear stress directionality alters both macroscopic and microscopic behaviors:

(a) The unidirectional shear loading requires the highest cyclic number to reach liquefaction at the same CSR, compared to the multidirectional loadings. Single-8 needs slightly more cycles than double-8 to trigger liquefaction.

(b) Although single-8 and double-8 paths share the same shear stress magnitude and rate of change at any given moment, the single-8 path maintains a constant figure-8 orientation, while the double-8 path alternates its orientation with each odd and even cycle. This alternating orientation in the double-8 path results in a lower number of cycles needed to reach liquefaction.

(c) The directional shifts in stress under the double-8 shear pattern induce more pronounced structural adjustments at the particle level. These adjustments contribute to an accelerated liquefaction process.

Microscopic fabric metrics, such as $Z_{m}$ and $F_{c}$, play a vital role in evaluating liquefaction resistance. Chapter 2 shows how $Z_{m}$ evolves under constant-$p'$ monotonic shear, providing insights into stress anisotropy's influence on granular microstructure. Chapter 3 demonstrates that during anisotropic consolidation, stress anisotropy significantly impacts $Z_{m}$, with higher anisotropy correlating with reduced liquefaction resistance. Chapter 5 further investigates how $Z_{m}$ reflects the soil\'s susceptibility to different shear stress patterns, with the double-8 pattern showing the most pronounced reduction in $Z_{m}$ and fluctuation in $F_{c}$, indicating higher susceptibility to liquefaction. These findings emphasize the critical importance of $Z_{m}$ and $F_{c}$ as microscopic indicators, bridging particle-scale fabric evolution with macro-scale liquefaction behaviors, and advancing the predictive understanding of soil stability under complex stress conditions.

## Future studies

While this dissertation advances the understanding of micro-macro behavior of granular materials in the liquefaction process, several promising directions remain for future research.

(a) Future studies could explore more complex loading conditions, such as initial shear stress, intermediate principal stress ratios, and cyclic axial stress, to deepen the understanding of stress anisotropy effects and its implications on liquefaction resistance.

(b) Currently, undrained liquefaction simulations using DEM primarily focus on element tests, where gravity effects can be neglected, and the process is approximated using the constant-volume-assumption. However, in non-quasi-static scenarios, such as dynamic model tests or field-scale studies where gravity-induced effects are significant, simulating the liquefaction process requires a robust coupling of DEM with fluid dynamics. Accurately capturing the interaction between pore water pressure evolution and granular behavior under these conditions remains a critical challenge and a promising direction for future research.

(c) Furthermore, integrating DEM-derived insights into continuum models holds potential to significantly improve their predictive capabilities. This is particularly relevant for anisotropic and cyclic loading conditions, where DEM simulations have shown promising results.

(d) Lastly, the development of GPU-accelerated algorithms and high-performance computing techniques offers opportunities to scale DEM simulations to unprecedented particle counts.

# References

Airey, D., & Wood, D. (1988). The Cambridge true triaxial apparatus. *Advanced Triaxial Testing of Soil and Rock*, 796--805. https://doi.org/10.1520/stp29115s

Arthur, J. R., Rodriguez del C., J. I., Dunstan, T., & Chua, K. S. (1980). Principal stress rotation: A missing parameter. Journal of the Geotechnical Engineering Division, 106(4), 419--433. https://doi.org/10.1061/ajgeb6.0000946

Arthur, J., Bekenstein, S., Germaine, J., & Ladd, C. (1981). Stress path tests with controlled rotation of principal stress directions. Laboratory Shear Strength of Soil, 516--540. https://doi.org/10.1520/stp28768s

Banerjee, S. K., Yang, M., & Taiebat, M. (2023). Effect of coefficient of uniformity on cyclic liquefaction resistance of granular materials. Computers and Geotechnics, 155, 105232. https://doi.org/10.1016/j.compgeo.2022.105232

Atkinson, J. H., & Bransby, P. L. (2012). The mechanics of Soils: An introduction to critical state soil mechanics. Indo American Books.

Been, K., Jefferies, M. G., & Hachey, J. (1991). The Critical State of Sands. Géotechnique, 41(3), 365--381. https://doi.org/10.1680/geot.1991.41.3.365

Bell, J. M. (1965) Stress-strain characteristics of cohesionless granular materials subjected to statically applied homogenous loads in an open system. PhD Thesis, California Institute of Technology, USA.

Bishop, A. W., & Eldin, G. (1950). Undrained triaxial tests on saturated sands and their significance in the general theory of shear strength. Géotechnique, 2(1), 13--32. https://doi.org/10.1680/geot.1950.2.1.13

Bono, J., McDowell, G., & Wanatowski, D. (2014). Investigating the micro mechanics of cemented sand using dem. International Journal for Numerical and Analytical Methods in Geomechanics, 39(6), 655--675. https://doi.org/10.1002/nag.2340

Cambou B (1998). Micromechanical Approach in Granular Materials. In: Cambou, B. (eds) Behaviour of Granular Materials. International Centre for Mechanical Sciences, vol 385. Springer, Vienna.

Cao, X., Zhu, Y., & Gong, J. (2021). Effect of the intermediate principal stress on the mechanical responses of binary granular mixtures with different fines contents. Granular Matter, 23(2). https://doi.org/10.1007/s10035-021-01110-9

Chang, J., Wang, W., Niu, Q., Wen, L., & Yuan, W. (2021). Effect of fabric anisotropy on bifurcation and shear band evolution in granular geomaterials. KSCE Journal of Civil Engineering, 25(8), 2893--2910. https://doi.org/10.1007/s12205-021-2164-5

Chen, Y., Ke, H., & Chen, R. (2005). Correlation of shear wave velocity with liquefaction resistance based on laboratory tests. Soil Dynamics and Earthquake Engineering, 25(6), 461--469. https://doi.org/10.1016/j.soildyn.2005.03.003

Cheung, G., & O'Sullivan, C. (2008). Effective simulation of flexible lateral boundaries in two- and three-dimensional DEM simulations. Particuology, 6(6), 483--500. https://doi.org/10.1016/j.partic.2008.07.018

Cui, L., O'Sullivan, C., & O'Neill, S. (2007). An analysis of the triaxial apparatus using a mixed boundary three-dimensional discrete element model. Géotechnique, 57(10), 831--844. https://doi.org/10.1680/geot.2007.57.10.831

Cundall, P. A. (1971) A computer model for simulating progressive, large scale movement in blocky rock systems. Proceedings of the international symposium on rock mechanics, Nancy, France, 2:129-136.

Cundall, P. A., & Strack, O. D. (1979). A discrete numerical model for granular assemblies. Géotechnique, 29(1), 47--65. https://doi.org/10.1680/geot.1979.29.1.47

El Shafee, O., Abdoun, T., & Zeghal, M. (2017). Centrifuge modelling and analysis of site liquefaction subjected to biaxial dynamic excitations. Géotechnique, 67(3), 260--271. https://doi.org/10.1680/jgeot.16.p.049

Elnashai, A. S. (2015). Fundamentals of earthquake engineering from source to fragility. John Wiley & Sons, Incorporated.

Fei, W., & Narsilio, G. A. (2020). Impact of three-dimensional sphericity and roundness on coordination number. Journal of Geotechnical and Geoenvironmental Engineering, 146(12). https://doi.org/10.1061/(asce)gt.1943-5606.0002389

Figueroa, J. L., Saada, Adel. S., Liang, L., & Dahisaria, N. M. (1994). Evaluation of soil liquefaction by energy principles. Journal of Geotechnical Engineering, 120(9), 1554--1569. https://doi.org/10.1061/(asce)0733-9410(1994)120:9(1554)

Georgiannou, V. N., & Konstadinou, M. (2014). Effects of density on cyclic behaviour of anisotropically consolidated Ottawa sand under undrained torsional loading. Géotechnique, 64(4), 287--302. https://doi.org/10.1680/geot.13.p.090

González-Montellano, C., Ramírez, Gallego, E., & Ayuga, F. (2011). Validation and experimental calibration of 3D discrete element models for the simulation of the discharge flow in Silos. Chemical Engineering Science, 66(21), 5116--5126. https://doi.org/10.1016/j.ces.2011.07.009

Green GE (1969) Strength and compressibility of granular materials under generalized strain conditions. PhD Thesis, University of London, UK.

Han, Y., Kato, S., & Kim, B. S. (2023). DEM analysis of fabric evolution and behavior of granular geomaterials in true triaxial test with flexible boundary. KSCE Journal of Civil Engineering, 27(8), 3341--3354. https://doi.org/10.1007/s12205-023-0336-1

Hatanaka, M., Uchida, A., & Ohara, J. (1997). Liquefaction characteristics of a gravelly fill liquefied during the 1995 Hyogo-Ken Nanbu earthquake. Soils and Foundations, 37(3), 107--115. https://doi.org/10.3208/sandf.37.3_107

Hight, D. W., Gens, A., & Symes, M. J. (1983). The development of a new hollow cylinder apparatus for investigating the effects of principal stress rotation in soils. Géotechnique, 33(4), 355--383. https://doi.org/10.1680/geot.1983.33.4.355

Hu, J., Wu, H., Gu, X., & Zhou, Q. (2023). Particle shape effects on dynamic properties of granular soils: A DEM study. Computers and Geotechnics, 161, 105578. https://doi.org/10.1016/j.compgeo.2023.105578

Huang, X., Hanley, K. J., O'Sullivan, C., Kwok, C. Y., & Wadee, M. A. (2014a). DEM analysis of the influence of the intermediate stress ratio on the critical-state behaviour of granular materials. Granular Matter, 16(5), 641--655. https://doi.org/10.1007/s10035-014-0520-6

Huang, X., Hanley, K. J., O'Sullivan, C., & Kwok, C. Y. (2014b). Exploring the influence of interparticle friction on critical state behaviour using DEM. International Journal for Numerical and Analytical Methods in Geomechanics, 38(12), 1276--1297. https://doi.org/10.1002/nag.2259

Huang, X., Kwok, C., Hanley, K. J., & Zhang, Z. (2018). DEM analysis of the onset of flow deformation of sands: Linking monotonic and cyclic undrained behaviours. Acta Geotechnica, 13(5), 1061--1074. https://doi.org/10.1007/s11440-018-0664-3

Hyodo, M., Murata, H., Yasufuku, N., & Fujii, T. (1991). Undrained cyclic shear strength and residual shear strain of saturated sand by cyclic triaxial tests. Soils and Foundations, 31(3), 60--76. https://doi.org/10.3208/sandf1972.31.3_60

Ibsen, L. B., & Prasstrup, U. (2002). The Danish rigid boundary true triaxial apparatus for soil testing. Geotechnical Testing Journal, 25(3), 254--265. https://doi.org/10.1520/gtj11096j

Ishihara, K., & Koga, Y. (1981). Case studies of liquefaction in the 1964 niigata earthquake. Soils and Foundations, 21(3), 35--52. https://doi.org/10.3208/sandf1972.21.3_35

Ishihara, K., & Takatsu, H. (1979). Effects of overconsolidation and K0, conditions on the liquefaction characteristics of sands. Soils and Foundations, 19(4), 59--68. https://doi.org/10.3208/sandf1972.19.4_59

Ishihara, K., & Towhata, I. (1983). Sand response to cyclic rotation of principal stress directions as induced by wave loads. Soils and Foundations, 23(4), 11--26. https://doi.org/10.3208/sandf1972.23.4_11

Ishihara, K., & Yoshimine, M. (1992). Evaluation of settlements in sand deposits following liquefaction during earthquakes. Soils and Foundations, 32(1), 173--188. https://doi.org/10.3208/sandf1972.32.173

Ishihara, K., & Yamazaki, F. (1980). Cyclic simple shear tests on saturated sand in multi-directional loading. Soils and Foundations, 20(1), 45--59. https://doi.org/10.3208/sandf1972.20.45

Ishihara, K., & Yasuda, S. (1975). Sand liquefaction in hollow cylinder torsion under irregular excitation. Soils and Foundations, 15(1), 45--59. https://doi.org/10.3208/sandf1972.15.45

Ishihara, K., Yamazaki, A., & Haga, K. (1985). Liquefaction of K0-consolidated sand under cyclic rotation of principal stress direction with lateral constraint. Soils and Foundations, 25(4), 63--74. https://doi.org/10.3208/sandf1972.25.4_63

Ishihara, K., Yoshida, K., & Kato, M. (1997). Characteristics of lateral spreading in liquefied deposits during the 1995 Hanshin-Awaji earthquake. Journal of Earthquake Engineering, 1(1), 23--55. https://doi.org/10.1080/13632469708962360

Itasca Consulting Group, Inc. (2021) PFC --- Particle Flow Code, Ver. 7.0. Minneapolis: Itasca.

Iwashita, K., & Oda, M. (1998). Rolling resistance at contacts in simulation of shear band development by Dem. Journal of Engineering Mechanics, 124(3), 285--292. https://doi.org/10.1061/(asce)0733-9399(1998)124:3(285)

Jiang, M., Kamura, A., & Kazama, M. (2021). Comparison of liquefaction behavior of granular material under SH- and love-wave strain conditions by 3D DEM. Soils and Foundations, 61(5), 1235--1250. https://doi.org/10.1016/j.sandf.2021.06.013

Kammerer, A. M., Pestana, J. M., & Seed, R. B. (2005). Behavior of monterey 0/30 sand under multidirectional loading conditions. Geomechanics, 154--173. https://doi.org/10.1061/40797(172)8

Kanatani, K. (1984). Distribution of directional data and fabric tensors. International Journal of Engineering Science, 22(2), 149--164. https://doi.org/10.1016/0020-7225(84)90090-9

Kim, B. S., Park, S. W., & Kato, S. (2012). DEM simulation of collapse behaviours of unsaturated granular materials under general stress states. Computers and Geotechnics, 42, 52--61. https://doi.org/10.1016/j.compgeo.2011.12.010

Kim, B. S., Sakakibara, T., Park, S. W., & Kato, S. (2021). Effects of grain shape on mechanical behavior of granular materials using DEM analysis. KSCE Journal of Civil Engineering, 25(6), 1939--1950. https://doi.org/10.1007/s12205-021-0582-z

Kim, H., & Park, S. W. (2020). DEM simulation for shear behavior in unsaturated granular materials at low-stress state. Computers and Geotechnics, 122, 103551. https://doi.org/10.1016/j.compgeo.2020.103551

Kishida, H. (1966). Damage to reinforced concrete buildings in Niigata City with special reference to foundation engineering. Soils and Foundations, 6(1), 71--88. https://doi.org/10.3208/sandf1960.6.71

Ko, H. Y., & Scott, R. F. (1967). A new soil testing apparatus. Géotechnique, 17(1), 40--57. https://doi.org/10.1680/geot.1967.17.1.40

Lade, P. V., & Duncan, J. M. (1973). Cubical triaxial tests on cohesionless soil. Journal of the Soil Mechanics and Foundations Division, 99(10), 793--812. https://doi.org/10.1061/jsfeaq.0001934

Lade, P. V., & Duncan, J. M. (1975). Elastoplastic stress-strain theory for cohesionless soil. Journal of the Geotechnical Engineering Division, 101(10), 1037--1053. https://doi.org/10.1061/ajgeb6.0000204

Li, B., Zhang, F., & Gutierrez, M. (2014). A numerical examination of the hollow cylindrical torsional shear test using dem. Acta Geotechnica, 10(4), 449--467. https://doi.org/10.1007/s11440-014-0329-9

Li, X. S., & Wang, Y. (1998). Linear representation of steady-state line for Sand. Journal of Geotechnical and Geoenvironmental Engineering, 124(12), 1215--1217. https://doi.org/10.1061/(asce)1090-0241(1998)124:12(1215)

Li, X. S., & Dafalias, Y. F. (2012). Anisotropic critical state theory: Role of Fabric. Journal of Engineering Mechanics, 138(3), 263--275. https://doi.org/10.1061/(asce)em.1943-7889.0000324

Liu, Y., Mao, H., Xu, C., & Zhang, Y. (2021). DEM investigation on the mechanical behavior of mudstone in the hollow cylinder torsional shear test. Computers and Geotechnics, 137, 104236. https://doi.org/10.1016/j.compgeo.2021.104236

Lo, S. C., Chu, J., & Lee, I. (1994). Investigation of the strain-softening behavior of granular soils with a new multiaxial cell. Geotechnical Testing Journal, 17(3), 325--336. https://doi.org/10.1520/gtj10107j

Matsuoka H., Nakai T. (1974) Stress-deformation and strength characteristics of soil under three different principal stresses. Proceedings of the Japan Society of Civil Engineers, Japan Society of Civil Engineers, 59-70.

Ma, Q., He, X., Zhou, Y. G., Chen, Y. M., & Han, Y. S. (2024). An approach to DEM simulation of hollow torsional shear tests for achieving general loading paths. Computers and Geotechnics, 172, 106402. https://doi.org/10.1016/j.compgeo.2024.106402

Manzari, M. T., & Dafalias, Y. F. (1997). A critical state two-surface plasticity model for sands. Géotechnique, 47(2), 255--272. https://doi.org/10.1680/geot.1997.47.2.255

Mijic, Z., Bray, J. D., Riemer, M. F., Rees, S. D., & Cubrinovski, M. (2021). Cyclic and monotonic simple shear testing of native Christchurch silty soil. Soil Dynamics and Earthquake Engineering, 148, 106834. https://doi.org/10.1016/j.soildyn.2021.106834

Ministry of Land, Infrastructure, Transport, and Tourism (MLIT). The Hanshin-Awaji Great Earthquake Disaster and Transport. Available at: https://www.mlit.go.jp/english/white-paper/unyu-whitepaper/1995/1995010101.html. (Accessed 2 February 2025).

Morimoto, T., Otsubo, M., & Koseki, J. (2021). Microscopic investigation into liquefaction resistance of pre-sheared sand: Effects of particle shape and initial anisotropy. Soils and Foundations, 61(2), 335--351. https://doi.org/10.1016/j.sandf.2020.12.008

Nakai, T., Matsuoka, H., Okuno, N., & Tsuzuki, K. (1986). True triaxial tests on normally consolidated clay and analysis of the observed shear behavior using elastoplastic constitutive models. Soils and Foundations, 26(4), 67--78. https://doi.org/10.3208/sandf1972.26.4_67

Nguyen, H. B., Rahman, M. M., & Fourie, A. (2021). The critical state behaviour of granular material in triaxial and direct simple shear condition: A DEM approach. Computers and Geotechnics, 138, 104325. https://doi.org/10.1016/j.compgeo.2021.104325

Oda, M., Nemat‐Nasser, S., & Mehrabadi, M. M. (1982). A statistical study of fabric in a random assembly of spherical granules. International Journal for Numerical and Analytical Methods in Geomechanics, 6(1), 77--94. https://doi.org/10.1002/nag.1610060106

Oda, M. (1972). Initial fabrics and their relations to mechanical properties of granular material. Soils and Foundations, 12(1), 17--36. https://doi.org/10.3208/sandf1960.12.17

Oda, M. (1977). Co-ordination number and its relation to shear strength of granular material. Soils and Foundations, 17(2), 29--42. https://doi.org/10.3208/sandf1972.17.2_29

Oda, M. (1982). Fabric tensor for discontinuous geological materials. Soils and Foundations, 22(4), 96--108. https://doi.org/10.3208/sandf1972.22.4_96

Oka, F., Yashima, A., Tateishi, A., Taguchi, Y., & Yamashita, A. (1999). A cyclic elasto-plastic constitutive model for sand considering a plastic-strain dependence of the shear modulus. Géotechnique, 49(5), 661--680. https://doi.org/10.1680/geot.1999.49.5.661

Ohsaki, Y. (1966). Niigata earthquakes, 1964 building damage and soil condition. Soils and Foundations, 6(2), 14--37. https://doi.org/10.3208/sandf1960.6.2_14

Otsubo, M., Chitravel, S., Kuwano, R., Hanley, K. J., Kyokawa, H., & Koseki, J. (2022). Linking inherent anisotropy with liquefaction phenomena of granular materials by means of dem analysis. Soils and Foundations, 62(5), 101202. https://doi.org/10.1016/j.sandf.2022.101202

O'Sullivan, C., Wadee, M. A., Hanley, K. J., & BARRETO, D. (2013). Use of DEM and elastic stability analysis to explain the influence of the intermediate principal stress on shear strength. Géotechnique, 63(15), 1298--1309. https://doi.org/10.1680/geot.12.p.153

O'Sullivan, C., & Bray, J. D. (2004). Selecting a suitable time step for discrete element simulations that use the Central Difference Time Integration Scheme. Engineering Computations, 21(2/3/4), 278--303. https://doi.org/10.1108/02644400410519794

O'Sullivan, C., & Cui, L. (2009). Micromechanics of granular material response during load reversals: Combined DEM and experimental study. Powder Technology, 193(3), 289--302. https://doi.org/10.1016/j.powtec.2009.03.003

Pan, K., Cai, Y. Q., Yang, Z. X., & Pan, X. D. (2019). Liquefaction of sand under monotonic and cyclic shear conditions: Impact of drained preloading history. Soil Dynamics and Earthquake Engineering, 126, 105775. https://doi.org/10.1016/j.soildyn.2019.105775

Pearce J. A. (1971) A new true triaxial apparatus, stress strain behavior of soils. Proceedings of Roscoe Memorial Symposium, 330-339.

Pyke, R. M., Chan, C. K., & Seed, H. B. (1975). Settlement of sands under multidirectional shaking. Journal of the Geotechnical Engineering Division, 101(4), 379--398. https://doi.org/10.1061/ajgeb6.0000162

Qu, T., Feng, Y. T., Wang, Y., & Wang, M. (2019). Discrete element modelling of flexible membrane boundaries for triaxial tests. Computers and Geotechnics, 115, 103154. https://doi.org/10.1016/j.compgeo.2019.103154

Reynolds, O. (1885). LVII. on the dilatancy of media composed of rigid particles in contact. with experimental illustrations. The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, 20(127), 469--481. https://doi.org/10.1080/14786448508627791

Rice J. R. (1976) The localization of plastic deformation. Proceedings of the 14th international congress of theoretical and applied mechanics, 1:207-20.

Roscoe, K. H., Schofield, A. N., & Thurairajah, A. (1963). Yielding of clays in states wetter than critical. Géotechnique, 13(3), 211--240. https://doi.org/10.1680/geot.1963.13.3.211

Roscoe, K. H., Schofield, A. N., & Wroth, C. P. (1958). On the yielding of Soils. Géotechnique, 8(1), 22--53. https://doi.org/10.1680/geot.1958.8.1.22

Rothenburg, L., & Bathurst, R. J. (1989). Analytical study of induced anisotropy in idealized granular materials. Géotechnique, 39(4), 601--614. https://doi.org/10.1680/geot.1989.39.4.601

Satake M. (1982) Fabric tensor in granular materials. Proceedings of UTAM Conference on Deformation and Flow of Granular Materials, 1982. AA Balkema, 63-68.

Seed, H. B., & Idriss, I. M. (1967). Analysis of soil liquefaction: Niigata earthquake. Journal of the Soil Mechanics and Foundations Division, 93(3), 83--108. https://doi.org/10.1061/jsfeaq.0000981

Seed, H. B., & Lee, K. L. (1966). Liquefaction of saturated sands during cyclic loading. Journal of the Soil Mechanics and Foundations Division, 92(6), 105--134. https://doi.org/10.1061/jsfeaq.0000913

Shibata T., Karube D. (1965) Influence of the variation of the intermediate principal stress on the mechanical properties of normally consolidated clays. Proceedings of 6th International Conference, SMFE, 1965, 1:361-367.

Shire, T., & O'Sullivan, C. (2012). Micromechanical assessment of an internal stability criterion. Acta Geotechnica, 8(1), 81--90. https://doi.org/10.1007/s11440-012-0176-5

Silver, M. L., Chan, C. K., Ladd, R. S., Lee, K. L., Tiedemann, D. A., Townsend, F. C., Valera, J. E., & Wilson, J. H. (1976). Cyclic triaxial strength of standard Test Sand. Journal of the Geotechnical Engineering Division, 102(5), 511--523. https://doi.org/10.1061/ajgeb6.0000272

Sitharam, T. G., Dinesh, S. V., & Shimizu, N. (2002). Micromechanical modelling of monotonic drained and undrained shear behaviour of granular media using three‐dimensional dem. International Journal for Numerical and Analytical Methods in Geomechanics, 26(12), 1167--1189. https://doi.org/10.1002/nag.240

Stershic, A. J., Simunovic, S., & Nanda, J. (2015). Modeling the evolution of lithium-ion particle contact distributions using a fabric tensor approach. Journal of Power Sources, 297, 540--550. https://doi.org/10.1016/j.jpowsour.2015.07.088

Sture, S., & Desai, C. (1979). Fluid cushion truly triaxial or multiaxial testing device. Geotechnical Testing Journal, 2(1), 20--33. https://doi.org/10.1520/gtj10585j

Su, D., & Li, X. S. (2008). Impact of multidirectional shaking on liquefaction potential of level sand deposits. Géotechnique, 58(4), 259--267. https://doi.org/10.1680/geot.2008.58.4.259

Suppasri, A., Kitamura, M., Alexander, D., Seto, S., & Imamura, F. (2024). The 2024 Noto Peninsula earthquake: Preliminary observations and lessons to be learned. International Journal of Disaster Risk Reduction, 110, 104611. https://doi.org/10.1016/j.ijdrr.2024.104611

Tastan, E. O., & Carraro, J. A. (2022). Effect of principal stress rotation and intermediate principal stress changes on the liquefaction resistance and undrained cyclic response of Ottawa sand. Journal of Geotechnical and Geoenvironmental Engineering, 148(5). https://doi.org/10.1061/(asce)gt.1943-5606.0002772

Tatsuoka, F., Ochi, K., Fujii, S., & Okamoto, M. (1986). Cyclic undrained triaxial and torsional shear strength of sands for different sample preparation methods. Soils and Foundations, 26(3), 23--41. https://doi.org/10.3208/sandf1972.26.3_23

Thornton, C. (2000). Numerical simulations of deviatoric shear deformation of granular media. Géotechnique, 50(1), 43--53. https://doi.org/10.1680/geot.2000.50.1.43

Tobita, Y. (1989). Fabric tensors in constitutive equations for granular materials. Soils and Foundations, 29(4), 91--104. https://doi.org/10.3208/sandf1972.29.4_91

Tokimatsu, K., & Uchida, A. (1990). Correlation between liquefaction resistance and shear wave velocity. Soils and Foundations, 30(2), 33--42. https://doi.org/10.3208/sandf1972.30.2_33

Tori, S., Tatsuoka, F., Miura, S., Yoshimi, Y., Yasuda, S., & Makihara, Y. (1986). Cyclic undrained triaxial strength of sand by a cooperative test program. Soils and Foundations, 26(3), 117--128. https://doi.org/10.3208/sandf1972.26.3_117

Towhata, I., & Ishihara, K. (1985). Shear work and pore water pressure in undrained shear. Soils and Foundations, 25(3), 73--84. https://doi.org/10.3208/sandf1972.25.3_73

Tsuji, Y., Tanaka, T., & Ishida, T. (1992). Lagrangian numerical simulation of plug flow of cohesionless particles in a horizontal pipe. Powder Technology, 71(3), 239--250. https://doi.org/10.1016/0032-5910(92)88030-l

Vargas, R. R., Ueda, K., & Uemura, K. (2020). Influence of the relative density and K0 effects in the cyclic response of Ottawa F-65 sand - cyclic torsional hollow-cylinder shear tests for leap-Asia-2019. Soil Dynamics and Earthquake Engineering, 133, 106111. https://doi.org/10.1016/j.soildyn.2020.106111

Wanatowski, D., & Chu, J. (2007). Static liquefaction of sand in plane strain. Canadian Geotechnical Journal, 44(3), 299--313. https://doi.org/10.1139/t06-078

Wei, J., Huang, D., & Wang, G. (2020). Fabric evolution of granular soils under multidirectional cyclic loading. Acta Geotechnica, 15(9), 2529--2543. https://doi.org/10.1007/s11440-020-00942-8

Wei, J., Ren, J., & Fu, H. (2022). The weakening of inter-particle friction and its effect on mechanical behaviors of granular soils. Computers and Geotechnics, 147, 104764. https://doi.org/10.1016/j.compgeo.2022.104764

Wen, Y., & Zhang, Y. (2023). Evidence of a unique critical fabric surface for granular soils. Géotechnique, 73(5), 439--454. https://doi.org/10.1680/jgeot.21.00126

Wensrich, C. M., & Katterfeld, A. (2012). Rolling friction as a technique for modelling particle shape in Dem. Powder Technology, 217, 409--417. https://doi.org/10.1016/j.powtec.2011.10.057

Xie, X., Ye, B., Zhao, T., Feng, X., & Zhang, F. (2023). DEM investigation into the effects of liquefaction history--induced anisotropy on sand behaviors. International Journal of Geomechanics, 23(3). https://doi.org/10.1061/ijgnai.gmeng-7492

Xu, X. M., Ling, D. S., Cheng, Y. P., & Chen, Y. M. (2015). Correlation between liquefaction resistance and shear wave velocity of granular soils: A micromechanical perspective. Géotechnique, 65(5), 337--348. https://doi.org/10.1680/geot.sip.15.p.022

Yamashita, S., & Toki, S. (1993). Effects of fabric anisotropy of sand on cyclic undrained triaxial and torsional strengths. Soils and Foundations, 33(3), 92--104. https://doi.org/10.3208/sandf1972.33.3_92

Yang, M., & Taiebat, M. (2024). Effect of anisotropic consolidation on cyclic liquefaction resistance of granular materials via 3D-Dem modeling. Journal of Geotechnical and Geoenvironmental Engineering, 150(5). https://doi.org/10.1061/jggefk.gteng-11970

Yang, M., Taiebat, M., Mutabaruka, P., & Radjaï, F. (2021). Evolution of granular media under constant-volume multidirectional cyclic shearing. Acta Geotechnica, 17(3), 779--802. https://doi.org/10.1007/s11440-021-01239-0

Yang, S., & Huang, D. (2023). Investigating the influence of inherent soil fabrics on reliquefaction resistance of sands using DEM-clump simulation. Computers and Geotechnics, 164, 105817. https://doi.org/10.1016/j.compgeo.2023.105817

Ye, G., Sheng, J., Ye, B., & Wang, J. (2012). Automated true triaxial apparatus and its application to over-consolidated Clay. Geotechnical Testing Journal, 35(4), 517--528. https://doi.org/10.1520/gtj104260

Yimsiri S., & Soga, K. (2010). DEM analysis of soil fabric effects on behaviour of sand. Géotechnique, 60(6), 483--495. https://doi.org/10.1680/geot.2010.60.6.483

Yin, J. H., Zhou, W.H., Kumruzzaman, M., & Cheng, C.-M. (2011). A rigid-flexible boundary true triaxial apparatus for testing soils in a three-dimensional stress state. Geotechnical Testing Journal, 34(3), 265--272. https://doi.org/10.1520/gtj102886

Yoshida, N., Tazoh, T., Wakamatsu, K., Yasuda, S., Towhata, I., Nakazawa, H., & Kiku, H. (2007). Causes of showa bridge collapse in the 1964 niigata earthquake based on eyewitness testimony. Soils and Foundations, 47(6), 1075--1087. https://doi.org/10.3208/sandf.47.1075

Yoshimi, Y., & Tokimatsu, K. (1977). Settlement of buildings on saturated sand during earthquakes. Soils and Foundations, 17(1), 23--38. https://doi.org/10.3208/sandf1972.17.23

Yoshimi, Y., Tokimatsu, K., Kaneko, O., & Makihara, Y. (1984). Undrained cyclic shear strength of a dense Niigata Sand. Soils and Foundations, 24(4), 131--145. https://doi.org/10.3208/sandf1972.24.4_131

Zhang, A., Jiang, M., & Wang, D. (2023). Effect of fabric anisotropy on the cyclic liquefaction of sands: Insight from DEM simulations. Computers and Geotechnics, 155, 105188. https://doi.org/10.1016/j.compgeo.2022.105188

Zhao, J., & Guo, N. (2013). Unique critical state characteristics in granular media considering fabric anisotropy. Géotechnique, 63(8), 695--704. https://doi.org/10.1680/geot.12.p.040

Zhu, Z., Wang, J., & Wu, M. (2022). DEM simulation of particle crushing in a triaxial test considering the influence of particle morphology and coordination number. Computers and Geotechnics, 148, 104769. https://doi.org/10.1016/j.compgeo.2022.104769

# Appendix 1 Implementation of High-Performance Computing in DEM

## A1.1 Introduction

The rapid evolution of computer hardware has significantly impacted numerical modeling in geophysics. Modern computing platforms, such as GPUs and clusters, now rival and exceed the performance of earlier supercomputers. For example, current GPUs offer tremendous computational power at a fraction of the cost and energy consumption of traditional clusters​. However, implementing efficient parallelized solutions for high-performance computing (HPC) remains critical, particularly for computationally intensive methods like DEM.

Taichi is a high-performance parallel programming language designed to maximize computational efficiency while maintaining simplicity and flexibility for developers. Initially developed to bridge the gap between low-level optimization and high-level usability, Taichi provides an intuitive Python-based syntax with backend support for multicore CPUs and GPUs. Its architecture allows it to execute complex numerical tasks efficiently, leveraging the massive parallel processing capabilities of modern GPUs​.

Compared to traditional GPU programming languages like CUDA and OpenCL, Taichi offers several advantages. Its Python-based syntax lowers the learning curve for researchers unfamiliar with low-level programming languages. Taichi supports various hardware backends, ensuring compatibility with multicore CPUs and GPUs without significant code modifications, enabling faster and more scalable simulations. Compared to deep learning frameworks like PyTorch, Taichi offers a distinct advantage in its fine-grained control at the element level, making it highly suitable for numerical simulations that require precise operations on particle or element interactions. This fine granularity allows researchers to efficiently develop high-performance parallelized numerical models for DEM, overcoming the challenges of large-scale particle simulations.

## A1.2 Methods and framework

### A1.2.1 Efficient neighbor search

The discrete element method is widely used for simulating the motion and interaction of granular materials, but its computational intensity poses significant challenges. Among these, collision detection is the most computationally expensive step due to its potential $Ο(N^{2})$ complexity, where $N$ is the number of particles. This quadratic scaling arises from brute-force methods, which evaluate interactions between all particle pairs. For large-scale simulations, this approach is computationally prohibitive, necessitating more efficient algorithms and data structures.

To address this challenge, neighbor search algorithms are commonly used to reduce the number of potential interactions by focusing on nearby particles. These algorithms partition the computational domain into smaller regions, such as grids, and limit collision detection to particles within neighboring regions. This approach reduces the complexity of collision detection to $Ο(N)$, significantly improving computational efficiency.

#### A1.2.1.1. Spatial partition with grids

In the discrete element method (DEM), spatial partitioning using grids is a fundamental approach to optimize collision detection. The computational domain is divided into grid cells, each with the grid length set to at least the diameter of the largest particle in the system. This ensures that any particle potentially interacting with a given particle is located either within the same grid cell or in one of its neighboring cells.

![图片包含 形状 描述已自动生成](thesis/assets/media/image140.png)

Fig. A1.1. Spatial grid partitioning and neighbor search scope for grid cell (1,1)

As illustrated in Fig. A1.1, the search area for particles in grid cell (1,1) includes their own cell and adjacent cells. By ensuring the grid length is sufficient to encapsulate the largest particle diameter, this approach guarantees that all potential neighbors are included in the local search while minimizing unnecessary computations. This technique reduces the computational burden of collision detection, enabling efficient simulations for large-scale DEM systems.

#### A1.2.1.2. Particle counting process for neighbor search

![图形用户界面, 应用程序 描述已自动生成](thesis/assets/media/image141.png)

(a) Particle to grid mapping

![图片包含 图标 描述已自动生成](thesis/assets/media/image142.png)

(b) Grid cell counts

Fig. A1.2 Particle-to-grid mapping and counting process for neighbor search optimization

As illustrated in Fig. A1.2(a), each particle is mapped to its corresponding grid cell by calculating its grid index based on spatial coordinates. For a particle located at a specific position, the grid index is computed by dividing its coordinates by the grid length and taking the integer part. 

After determining the grid index, the particle immediately updates the count of its respective grid cell, as shown in Fig. A1.2(b). This update is performed using an atomic add operation to prevent conflicts when multiple particles in the same grid cell attempt to modify the count simultaneously. The atomic add operation ensures thread-safe access, allowing only one thread to update the grid cell count at any given time. This guarantees the accuracy of the particle counts in each grid.

Once this step is complete, the total number of particles in each grid cell is accurately calculated. Let $N_{grid}(i,\ j)$ denote the number of particles within the grid cell located at index $(i,\ j)$.

#### A1.2.1.3. Efficient calculation of prefix and postfix particle counts for grids

To efficiently search the particles in neighboring grids and all preceding grids, concepts of $N_{prefix}$ and $N_{postfix}$​ are introduced.

$N_{prefix}$ represents the cumulative count of particles in all grid cells from the first cell up to the grid cell at row $i$ and column $j$, excluding the particles in the current grid cell $(i,j)$. $N_{postfix}$ represents the cumulative count of particles in all grid cells from the first cell up to and including the grid cell at row $i$ and column $j$. The process leverages parallel and sequential computation strategies to optimize efficiency while ensuring correctness.

##### A1.2.1.3.1. Row-wise summation ($N_{sum\_ row}$)

As illustrated in Fig. A1.3(a), the first step involves calculating the total number of particles in each row ($N_{sum\_ row}$​) by summing the particle counts across all columns for each row. Since each row\'s calculation is independent of the others, similar to the calculation process of $N_{grid}$, this operation is fully parallel, allowing for high computational efficiency.

![图形用户界面, 应用程序, 图标 描述已自动生成](thesis/assets/media/image143.png)

(a) Row-wise summation of particle counts ($N_{sum\_ row}$​)

![蓝色的背景和白色的字 描述已自动生成](thesis/assets/media/image144.png)

(b) Serial calculation of prefix particle count for the first column ($N_{prefix}(i,\ 0)$)

![蓝色的标志 描述已自动生成](thesis/assets/media/image145.png)

(c) Parallel-serial calculation of prefix particle counts ($N_{prefix}(i,j)$)

![手机屏幕的截图 描述已自动生成](thesis/assets/media/image146.png)

(d) Calculation of total particle counts including current grid ($N_{postfix}(i,j)$)

Fig. A1.3. Calculation procedure of prefix and postfix particle counts for grids

##### A1.2.1.3.2. Serial calculation of $N_{prefix}$ for the first column

Next, the prefix count for the first column of each row is calculated sequentially. As shown in Fig. A1.3(b), $N_{prefix}(i,\ 0)$ for row $i$ is obtained by adding the total particle count from the previous row $N_{sum\_ row}(i - 1)$ to $N_{prefix}(i - 1,0)$. This operation has a one-dimensional dependency and is performed serially. However, because the computation is limited to a single column, its overhead is minimal compared to a full two-dimensional serial operation.

##### A1.2.1.3.3. Parallel-serial calculation of $N_{prefix}$ within each row

Once $N_{prefix}(i,\ 0)$ is determined, the prefix count for the remaining columns in each row is computed. As illustrated in Fig. A1.3(c), this step is performed in parallel for all rows, but within each row, the prefix counts are calculated sequentially using the relationship:

$N_{prefix}(i,j) = N_{prefix}(i,j - 1) + N_{grid}(i,j - 1)$ (A1-1)

The serial dependency is confined to the one-dimensional row, allowing for efficient computation compared to a fully serial approach.

##### A1.2.1.3.4. Calculation of $N_{postfix}$

Finally, the total particle count including the current grid cell $N_{prefix}$ is computed in parallel across all grid cells. As shown in Fig. A1.3(d), this is achieved by summing the prefix count $N_{prefix}(i,j)$ and the particle count $N_{grid}(i,\ j)$ for each grid cell:\
$N_{postfix}(i,j) = N_{prefix}(i,j) + N_{grid}(i,j)$ (A1-2)

By combining parallel row-wise operations and efficient one-dimensional serial operations, this method achieves a significant improvement in computational efficiency. The computed $N_{prefix}$ and $N_{postfix}$ arrays provide essential inputs for subsequent neighbor search algorithms.

#### A1.2.1.4. Particle grouping and index arrangement for neighbor search

To enable efficient neighbor search, particles are grouped, and their IDs are rearranged based on the grids they occupy. This process involves initializing $N_{cur}$​, which tracks the current position for recording particle IDs in each grid. By cloning $N_{prefix}$​, $N_{cur}$​ inherits the cumulative particle counts already computed.

![图形用户界面, 应用程序 描述已自动生成](thesis/assets/media/image147.png)

(a) Particle ID assignment using $N_{cur}$ for rearrangement

![图形用户界面 描述已自动生成](thesis/assets/media/image148.png)

(b) Final rearranged particle IDs grouped by grid for neighbor search

Fig. A1.4. Particle grouping and index arrangement

As shown in Fig. A1.4(a), each particle calculates its grid index from its spatial position. Using this index, the particle retrieves the current write position for its grid from $N_{cur}$​. The particle\'s ID is then placed at this position in the rearranged ID array. $N_{cur}$​ is atomically incremented to update the write position for the next particle assigned to the same grid. The use of atomic operations prevents conflicts when multiple particles are assigned to the same grid simultaneously. This parallel process allows for rapid and independent updates for all particles.

The rearranged ID array, illustrated in Fig. A1.4(b), organizes particles according to their grid locations. This grouping reduces the scope of neighbor searches, confining interactions to particles within the same or adjacent grids. By structuring the particle data in this way, the computational efficiency of DEM simulations is significantly improved, making this method well-suited for large-scale parallel computations.

#### A1.2.1.5. Neighbor search after particle ID rearrangement

![手机屏幕的截图 描述已自动生成](thesis/assets/media/image149.png)

Fig. A1.5. Neighbor Search After Particle ID Rearrangement

With particle IDs rearranged and the $N_{prefix}$​ and $N_{postfix}$ arrays established, neighbor search becomes highly efficient. The grid-based structure allows quick determination of neighboring particles by leveraging the spatial organization.

As shown in Fig. A1.5, for each particle, the grid it belongs to is first identified based on its spatial coordinates. For instance, particle 1 is located in grid $(1,1)$. To find its neighbors, the algorithm considers all adjacent grids within a $3 \times 3$ region, encompassing grids from $(0,0)$ to $(2,2)$. 

For each neighboring grid, the start and end positions of particle IDs are retrieved from $N_{prefix}$​ and $N_{postfix}$. For example, for the grid $(0,0)$, the start position is 0, and the end position is 1. Using this range, the particle IDs within grid $(0,0)$ can be quickly identified, such as particle 6 in this case. The algorithm then proceeds to examine all particles in the identified neighboring grids, repeating this process for each neighboring grid around the particle\'s grid.

This process is executed in parallel for every particle, allowing each particle to independently compute its neighbors. Leveraging parallelism further enhances the computational efficiency, making the approach highly scalable for large-scale simulations.

### A1.2.2. Interparticle contact 

#### A1.2.2.1. Contact detection

After identifying a particle and its neighboring particles through the neighbor search process, the next step is to determine their relative spatial relationship, specifically whether they are in contact. To avoid redundant calculations and self-comparisons, the contact detection is restricted to particle pairs where the ID of one particle $(i)$ is smaller than the other $(j)$, i.e., $i < j$.

For typical cases where particles are either two-dimensional circles or three-dimensional spheres, the gap between the particles is determined based on their positions and radii. The gap is defined as:

$g = \parallel \mathbf{x}_{\mathbf{i}} - \mathbf{x}_{\mathbf{j}} \parallel - (r_{i} + r_{j})$ (A1-3)

,where $\parallel \mathbf{x}_{\mathbf{i}} - \mathbf{x}_{\mathbf{j}} \parallel$ is the Euclidean distance between the centers of particle $i$ and particle $j$. $r_{i}$ and $r_{j}$ are radii of particles $i$ and $j$, respectively.

If $g < 0$, the two particles are considered to be in contact. Once contact is detected, further calculations related to the contact model are initiated. These include computing interaction forces such as the normal and tangential forces, which depend on the overlap and the material properties of the particles.

#### A1.2.2.2. Contact model

![图标 描述已自动生成](thesis/assets/media/image12.png)

Fig. A1.6. Contact model in HPC-DEM framework

In this study, the contact models include a linear contact model and a Hertz-Mindlin model, as it is sufficient for the current scope of research. The contact forces are divided into two components: normal force and tangential force, both of which include an elastic part and a viscous damping part as shown in Fig. A1.6.

The elastic part of the normal contact force is determined by the normal stiffness coefficient $k_{n}$​ and the gap ($g$) between particles:

$\mathbf{F}_{\mathbf{n}}^{\mathbf{l}} = k_{n} \bullet g \bullet \mathbf{n}$ (A1-4)

, where $\mathbf{n}$ is the unit contact normal. The damping part depends on the relative normal velocity of at the contact point ($\dot{\mathbf{u}_{\mathbf{n}}}$) and the equivalent mass $m_{c}$, which is defined as:

$m_{c} = \frac{2m_{i}m_{j}}{m_{i} + m_{j}}$ (A1-5)

The normal viscous force is then calculated as:

$\mathbf{F}_{\mathbf{n}}^{\mathbf{d}} = \left( 2\beta_{n}\sqrt{m_{c}k_{n}} \right)\dot{\mathbf{u}_{\mathbf{n}}}$ (A1-6)

, where $\beta_{n}$ indicates normal critical damping ratio. The total normal contact force is the sum of these two components:

$\mathbf{F}_{\mathbf{n}} = \mathbf{F}_{\mathbf{n}}^{\mathbf{l}} + \mathbf{F}_{\mathbf{n}}^{\mathbf{d}}$ (A1-7)

The tangential elastic force is updated incrementally based on the tangential displacement ($\Delta\mathbf{s}_{\mathbf{t}}$) and tangential stiffness coefficient $k_{s}$:

$\left( \mathbf{F}_{\mathbf{s}}^{\mathbf{l}} \right)^{1} = \left( \mathbf{F}_{\mathbf{s}}^{\mathbf{l}} \right)^{0} + k_{s} \cdot \Delta\mathbf{s}_{\mathbf{t}}$( ()(A1-8)

, where $\left( \mathbf{F}_{\mathbf{s}}^{\mathbf{l}} \right)^{1}$ and $\left( \mathbf{F}_{\mathbf{s}}^{\mathbf{l}} \right)^{0}$ refer to the tangential shear force at current and previous timestep, respectively. Similar to the normal component, the tangential viscous force is proportional to the tangential relative velocity ($\dot{\mathbf{u}_{\mathbf{t}}}$):

$\mathbf{F}_{\mathbf{s}}^{\mathbf{d}} = \left( 2\beta_{s}\sqrt{m_{c}k_{s}} \right)\dot{\mathbf{u}_{\mathbf{s}}}$ (A1-9)

The total tangential contact force is the sum of these two components:

$\mathbf{F}_{\mathbf{s}} = \mathbf{F}_{\mathbf{s}}^{\mathbf{l}} + \mathbf{F}_{\mathbf{s}}^{\mathbf{d}}$ (A1-10)

The tangential force is constrained by Coulomb\'s friction law to ensure it does not exceed the frictional limit, which depends on the friction coefficient ($\mu$) and the normal contact force ($\mathbf{F}_{\mathbf{n}}$):

$\parallel \mathbf{F}_{\mathbf{s}} \parallel \leq \mu \bullet \parallel \mathbf{F}_{\mathbf{n}} \parallel$ (A1-11)

If the tangential force exceeds this limit, it is scaled down to satisfy the Coulomb criterion. This contact model provides a simple yet robust framework for simulating particle interactions, balancing computational efficiency and physical accuracy. The combination of elastic and viscous components ensures realistic dynamic responses, while the Coulomb criterion accounts for sliding and frictional behavior.

## A1.3. Demonstration: slope generation

### A1.3.1. Simulation setup

In this validation case, 524,288 particles were randomly generated within a cuboid domain of dimensions 0.2 m×0.2 m×0.8 m, with diameters uniformly distributed between 2 mm and 3.2 mm as shown in Fig. A1.7(a). The particles, assigned a density of 2650 kg/m³, interacted via a linear contact model, with parameters detailed in Table A1-1. Initially, the random particle placement resulted in overlapping configurations, creating significant elastic potential energy. To stabilize the system, particle velocities were periodically nullified every 200 timesteps to dissipate excess energy and prevent numerical instability. Under gravitational forces, particles settled onto a fixed bottom boundary while lateral walls provided support.

Table. A1-1 Parameters used in slope generation demo

  -----------------------------------------------------------------------------------------
  Description                                                               Value
  ------------------------------------------------------------------------- ---------------
  Number of particles $N_{p}$                                               1024×512

  Density, $\rho_{s}$ (kg/m^3^)                                             2650

  Contact model                                                             Hertz-Mindlin

  Interparticle equivalent Young's modulus $E_{pp}^{\star}$                 5.0e8

  Interparticle equivalent shear modulus $G_{pp}^{\star}$                   2.5e8

  Interparticle-wall equivalent Young's modulus $E_{pw}^{\star}$            5.0e8

  Interparticle-wall equivalent shear modulus $G_{pw}^{\star}$              2.5e8

  Tangential frictional coefficient between particles, $\mu_{pp}$           0.50

  Tangential frictional coefficient between particle and wall, $\mu_{pw}$   0.50

  Normal critical damping ratio, $\beta_{n}$                                0.7

  Shear critical damping ratio, $\beta_{s}$                                 0.1
  -----------------------------------------------------------------------------------------

(a) 100,000-time step

(b) 250,000-time step

![图形用户界面 低可信度描述已自动生成](thesis/assets/media/image152.png) ![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image153.png)

(c) 300,000-time step

(d) 2,000,000-time step

Fig. A1.7. Particle arrangement at different timesteps during the settling phase

### A1.3.2. Slope formation after wall movement

Following the stabilization process, the right wall element, which initially provided lateral support to the particles, was shifted to the right boundary of the simulation domain. This adjustment removed the lateral confinement, allowing particles to move and redistribute under gravitational forces. The system evolved as particles slid downward and rearranged themselves, ultimately forming a stable slope. The progression of this slope formation is depicted in Fig. A1.8.

![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image154.png) ![图表, 表面图 描述已自动生成](thesis/assets/media/image155.png)

(a) 2,060,000-time step

\(b\) 2,220,000-time step

![图片包含 图形用户界面 描述已自动生成](thesis/assets/media/image156.png) ![图表 低可信度描述已自动生成](thesis/assets/media/image157.png)

\(c\) 2,520,000-time step

\(d\) 4,260,000-time step

Fig. A1.8. Evolution of particle configuration during slope formation after the removal of lateral confinement. 

### A1.3.3. Discussion of validation results

The successful formation of a stable slope after the removal of lateral confinement confirms the robustness of the implemented neighbor search algorithm. The neighbor search algorithm efficiently handled the computationally intensive task of identifying interaction among the 524,288 particles, ensuring computational efficiency. This was achieved through the grid-based spatial partitioning approach, which significantly reduced the computational complexity from $Ο(N^{2})$ to $Ο(N)$.

The contact model, combining elastic and damping components for normal and tangential forces, successfully captured the essential mechanics of particle interactions. The observed behavior during slope formation---where particles redistributed and stabilized under gravitational forces---showed that the contact forces were inherited and incremented accurately, even during high-density and dynamic conditions. The resulting slope geometry, as shown in Fig. A1.8, further supports the model\'s ability to simulate realistic particle interactions.

This validation also highlighted the computational benefits of utilizing GPU-accelerated high-performance computing for DEM simulations. The ability to handle over half a million particles with complex interactions and to track their evolution efficiently underscores the scalability and potential of this HPC-DEM framework.

## A1.4. Demonstration of drained and undrained monotonic triaxial shear

To demonstrate the robustness and accuracy of the HPC-DEM implementation, behaviors of granular materials in both drained and undrained monotonic triaxial shear were simulated following isotropic consolidation. The analysis incorporates macroscopic stress-strain responses, void ratio evolution, force chain visualization, and stress paths to comprehensively assess the algorithm\'s validity.

Table. A1-2 Parameters used in monotonic triaxial shear demonstration

  -----------------------------------------------------------------------------------------
  Description                                                               Value
  ------------------------------------------------------------------------- ---------------
  Number of particles $N_{p}$                                               1024×8

  Density, $\rho_{s}$ (kg/m^3^)                                             2650

  Contact model                                                             Hertz-Mindlin

  Interparticle equivalent Young's modulus $E_{p}^{\star}$                  5.0e8

  Interparticle equivalent shear modulus $G_{p}^{\star}$                    2.5e8

  Interparticle-wall equivalent Young's modulus $E_{p}^{\star}$             5.0e8

  Interparticle-wall equivalent shear modulus $G_{p}^{\star}$               2.5e8

  Tangential frictional coefficient between particles, $\mu_{pp}$           0.5

  Tangential frictional coefficient between particle and wall, $\mu_{pw}$   0.0

  Normal critical damping ratio, $\beta_{n}$                                0.7

  Shear critical damping ratio, $\beta_{s}$                                 0.5
  -----------------------------------------------------------------------------------------

### A1.4.1. Drained shear behavior

This demonstration involves two triaxial shear simulations under drained and undrained conditions. Prior to shearing, an isotropic consolidation phase was applied to the granular assembly, where all particles were consolidated under an isotropic confining stress ($\sigma_{1}' = \sigma_{2}' = \sigma_{3}' = 200kPa$). After achieving a stable isotropic state, the drained triaxial shear test was conducted under a constant confining stress ($\sigma_{2}' = \sigma_{3}' = 200kPa$) while incrementally increasing the axial stress ($\sigma_{1}'$) by applying a constant axial displacement rate of 0.01m/s.

![图表, 折线图 描述已自动生成](thesis/assets/media/image158.png)

Fig. A1.9. Deviatoric stress ($q$) versus axial strain ($\varepsilon_{a}$) during drained triaxial shear

Figure A1.9 depicts the deviatoric stress ($q = \sigma_{1}' - \sigma_{3}'$) versus axial strain ($\varepsilon_{a}$​) relationship during drained triaxial shear. The stress gradually increases with strain, exhibiting strain-hardening behavior of granular materials. This result indicates that the implemented contact model correctly captures the progressive mobilization of interparticle forces and resistance under drained conditions.

Correspondingly, Fig. A1.10 shows the void ratio ($e$) evolution. Initially, the void ratio decreased due to particle rearrangements and compaction (increasing $p'$). After reaching a minimum, it began to increase slightly as the sample dilated at larger strains, indicative of a transition from a contractive to a dilative response.

![图表, 折线图 描述已自动生成](thesis/assets/media/image159.png)

Fig. A1.10. Void ratio ($e$) evolution versus axial strain ($\varepsilon_{a}$) during drained triaxial shear

### A1.4.2. Monotonic undrained shear behavior

For the undrained condition, isotropic consolidation to 200 kPa was also performed before shearing. Here too, the axial displacement rate was fixed at 0.01m/s, ensuring consistency across the simulations. The evolution of deviatoric stress ($q$) and pore water pressure buildup, shown in Fig. A1.11, reveals a distinct pattern. Initially, the sample

![图表, 折线图 描述已自动生成](thesis/assets/media/image160.png)

Fig. A1.11. Deviatoric stress ($q$) versus axial strain ($\varepsilon_{a}$) during undrained triaxial shear

exhibited strain hardening up to approximately $\varepsilon_{a} = 2.5\%$, after which slight softening occurred due to pore pressure accumulation. Beyond $\varepsilon_{a}$=7.5%, the sample demonstrated renewed strain hardening, corresponding to the decreasing pore water pressure and redistribution of force chains and particle rearrangement.

### A1.4.3. Force chain evolution

The force chain network, represented in Fig. A1.12, highlights particle interactions at various stages of shearing. Strong force chains are visibly aligned with the major principal stress direction as shearing progresses, illustrating the stress redistribution within the granular assembly.

![图片包含 图示 描述已自动生成](thesis/assets/media/image161.png) ![图片包含 图示 描述已自动生成](thesis/assets/media/image162.png)

(a) $\varepsilon_{a}$=0%

\(b\) $\varepsilon_{a}$=5%

![图片包含 图表 描述已自动生成](thesis/assets/media/image163.png) ![图片包含 图表 描述已自动生成](thesis/assets/media/image164.png)

\(c\) $\varepsilon_{a}$=10%

\(d\) $\varepsilon_{a}$=20%

Fig. A1.12. Visualization of particle configurations and force chains at different stage in drained triaxial shear

### A1.4.4. Analysis of stress paths in drained and undrained shear conditions 

Figure A1.13 compares the stress paths ($p'$-$q$) for drained and undrained shear tests, providing critical insights into the material response under different drainage conditions.

Under the drained condition, the confining stress was held constant ($\sigma_{2}' = \sigma_{3}' = 200kPa$). The stress path follows the expected trajectory, with incremental changes in $q$ and $p'$ maintaining a consistent ratio of $\frac{\Delta q}{\Delta p'} = 3$. This reflects the effective control of lateral stresses by the servo system and demonstrates the model\'s ability to maintain boundary conditions accurately during shearing. The drained stress path progresses smoothly toward the critical state line (CSL), confirming the equilibrium behavior of granular materials under large deformation.

![图表, 折线图 描述已自动生成](thesis/assets/media/image165.png)

Fig. A1.13. Stress paths ($p'$-$q$) for drained and undrained triaxial shear, with critical state line (CSL)

In the undrained condition, the stress path exhibits distinct behavior due to the constant volume constraint and resulting pore pressure changes. Initially, as $q$ increases, $p'$ decreases gradually, reflecting the buildup of pore water pressure as axial strain increases. Beyond approximately $\varepsilon_{a} = 2.5\%$, as pore water pressure continues to rise, the monotonic shear leads to a reduction in $q$, resulting in a softening behavior, which could also be observed in Fig. A1.11. When $p'$ drops to approximately 100kPa, large deformations in the sample cause a reversal. Both $q$ and $p'$ increase along the CSL, signifying the material\'s transition to the critical state under undrained conditions. As the strain approaches 20%, the granular assembly reaches the critical state, where $q$ and $p'$ stabilize, reflecting the equilibrium condition for undrained shear.

By comparing the stress paths for drained and undrained conditions, the results demonstrate that both cases converge to the same critical state line. This agreement highlights the robustness of the model in replicating fundamental soil mechanics principles, particularly the unique and invariant nature of the critical state under the triaxial compression condition. The ability to capture both drained and undrained responses with consistency further validates the accuracy of the simulation and underscores the effectiveness of the developed HPC-DEM approach.

## A1.5. Summary 

Appendix 1 delves into the integration of high-performance computing (HPC) with the Discrete Element Method (DEM) to enable large-scale simulations of granular systems, addressing computational limitations in traditional DEM applications. This chapter highlights significant advancements in computational efficiency, scalability, and the verification of DEM models through rigorous testing.

A slope generation test involving half a million particles was conducted to validate the large-scale capabilities of the HPC-DEM framework. The test demonstrated the system\'s ability to effectively model complex granular behaviors under gravitational forces.

The accuracy of the DEM implementation was rigorously validated through drained and undrained triaxial shear tests. These tests revealed that the model accurately captured key mechanical behaviors of granular materials under different stress conditions.

# Appendix 2 Ray Tracing for Enhanced Visualization in DEM

In Appendix 1, we explored the use of GPUs for general-purpose high-performance computing (GPGPU), leveraging their massively parallel architecture for DEM simulations. While modern GPUs are widely recognized for accelerating scientific computing, their origins lie in a fundamentally different domain: visual rendering. GPUs were initially designed to handle graphics-intensive tasks such as image rendering, shading, and texture mapping. These tasks required the calculation of pixel colors across millions of pixels in real-time, a process naturally suited to parallel computation.

Among the many techniques developed for visual rendering, ray tracing emerged as one of the most powerful methods for producing highly realistic images. Ray tracing simulates the behavior of light in the real world by tracing the paths of rays from a virtual camera through a viewport and into a 3D scene. When these rays intersect with objects, the interactions---such as reflections, refractions, and shading---are computed to determine the final color of each pixel.

This parallelism aligns with the requirements of DEM, where particle interactions can similarly be computed independently. The adoption of GPUs in general computing thus stems from their ability to handle high-dimensional, parallelizable problems across diverse domains, from scientific simulations to image rendering. This chapter explores the application of ray tracing in DEM visualization, covering its fundamental principles and implementation. By integrating ray tracing into DEM studies, we aim to enhance the interpretability and communicability of complex granular behaviors, bridging the gap between computation and visual analysis.

## A2.1. Fundamentals of ray tracing

Ray tracing is a rendering technique that models the interaction of light with objects in a virtual scene, producing images with exceptional realism. At its core, the process involves calculating the path of rays from a virtual camera through a viewport into a 3D scene, determining how these rays interact with objects, and ultimately assigning colors to the pixels they represent. This section introduces key concepts such as the camera, viewport, and the computational pipeline of ray tracing.

### A2.1.1. Camera, ray, viewport, and scene

![示意图 低可信度描述已自动生成](thesis/assets/media/image166.png)

Fig. A2.1. Ray tracing workflow: Rays originate from the camera, pass through the viewport, and interact with objects in the 3D scene, determining the color information for each pixel.

The camera in ray tracing acts as the observer\'s eye, defining the origin of rays and their direction. It is characterized by parameters such as position, orientation, and field of view. The viewport represents the screen or image plane onto which the scene is projected. Each pixel on the viewport corresponds to a ray that originates from the camera and passes through that pixel's location in the scene.

The goal of ray tracing is to calculate the color (RGB values) of each pixel on the viewport by simulating the interaction of its corresponding ray with objects in the scene. This requires solving the fundamental problem of determining where and how each ray intersects with objects.

Fig. A2.1 illustrates the basic workflow of ray tracing, where rays originate from the camera, pass through the viewport, and interact with objects in the 3D scene. The resulting interactions determine the color information for each pixel on the viewport.

### A2.1.2. Determining pixel colors: ray-object intersection

The ray tracing process begins by iterating over every pixel in the viewport, generating a primary ray for each. These rays are traced into the 3D scene to identify intersections with objects. For each intersection, additional calculations are performed to evaluate lighting, material properties, and other effects such as shadows or reflections. If a ray intersects with an object, the nearest intersection point is determined. The object\'s material properties, combined with lighting conditions, are then used to compute the pixel\'s final color. Rays that do not intersect with any object are typically assigned a background color, representing the environment or sky. To visualize the setup, Fig. A2.2 presents two spheres rendered with refined, elegant colors---muted green (RGB: 0.45, 0.55, 0.47) and muted violet (RGB: 0.35, 0.30, 0.37).

![图表, 气泡图 描述已自动生成](thesis/assets/media/image167.png)

Fig. A2.2. Rendered spheres with purple and green colors

## A2.2. Lighting models in ray tracing

In ray tracing, lighting models play a critical role in determining the appearance of objects in a rendered scene. The interplay between light sources and object surfaces determines the final pixel color, achieved by applying illumination coefficients to the object\'s base color. This section introduces three fundamental types of light sources commonly employed in rendering: ambient light, point light, and directional light.

### A2.2.1. Ambient Light

Ambient light represents a constant, uniform light source present throughout the scene, simulating indirect lighting from all directions. Unlike other light types, ambient light does not originate from a specific location. Instead, it provides a baseline illumination to ensure that surfaces not directly exposed to light sources are still visible. The contribution of ambient light to the object's color is determined by an ambient coefficient, typically a small value (e.g., 0.1 or 0.2). Mathematically, the ambient lighting contribution​ is given by:

$I_{a} = C \bullet k_{a}$ (A2-1)

where $C$ is the object's base color, and $k_{a}$ is the ambient coefficient.

### A2.2.2. Point light

Point lights represent localized sources of light that radiate uniformly in all directions from a specific position. They mimic real-world light sources like bulbs or candles. The intensity of light decreases with distance from the source, modeled by an attenuation factor.

![图片包含 形状 描述已自动生成](thesis/assets/media/image168.png)

Fig. A2.3. Diffuse reflection of light, showing the relationship between the light direction, surface normal, and reflection distribution

![黑暗中的灯光 中度可信度描述已自动生成](thesis/assets/media/image169.png)

Fig. A2.4. Specular reflection, illustrating the relationship between the light ray, surface normal, and viewer position

For point light, the diffuse and specular contributions depend on the light direction, surface normal, and viewer position. Diffuse lighting is proportional to the cosine of the angle between the light direction vector $L$ and the surface normal $N$, as illustrated in Fig. A2.3. Specular lighting depends on the angle between the reflected light vector　$R$ and the viewer direction $V$, as shown in Fig. A2.4.

The intensity $I_{p}$ at a point is computed as:

$I_{p} = C \cdot (k_{d}\left( \mathbf{L} \cdot \mathbf{N} \right) + k_{s}\left( \mathbf{R} \cdot \mathbf{V} \right)^{n})$ (A2-2)

, where $k_{d}$ and $k_{s}$ ​are diffuse and specular coefficients,$n$ is the shininess factor.

### A2.2.3. Directional light

Directional light represents a distant light source, such as sunlight, where the light rays are considered parallel. Unlike point lights, directional light does not attenuate with distance. The illumination model for directional light is similar to that of point light but simplifies calculations as the light direction remains constant for the entire scene.

![桌子上有一些彩色的球 低可信度描述已自动生成](thesis/assets/media/image170.png)

Fig. A2.5. Rendering of two spheres under directional light showcasing diffuse and specular reflections.

The interaction of objects with light sources, combining ambient, diffuse, and specular reflections, is demonstrated in Fig. A2.5. This figure depicts two spheres illuminated with ambient light, directional light, and specular reflections, where the lighting highlights the material properties.

## A2.3. Reflection and refraction between objects

Previous sections focused on light interactions with individual objects, such as diffuse and specular reflections influenced by various light sources. However, these computations only accounted for direct lighting effects and did not include interactions between objects within the scene. To realistically simulate the intricate interplay of light, it becomes necessary to account for reflections and refractions between objects, which are essential for capturing phenomena such as mirrored surfaces and transparent materials.

This process is achieved through recursive ray tracing. When a ray intersects an object, secondary rays are spawned to model light interactions with other objects in the environment.

### A2.3.1. Reflection 

Reflections are crucial to creating realistic scenes in ray tracing, as they simulate how light bounces off surfaces and interacts with other objects in the environment. When a light ray strikes a reflective surface, part of its energy is reflected. The direction of the reflected ray is determined by the surface normal and the incident ray according to the law of reflection.

In the ray tracing process, reflections are computed by generating a secondary ray at the point of intersection between the primary ray and the reflective surface. This reflected ray continues to propagate through the scene, checking for further intersections with other objects. Each subsequent intersection contributes to the pixel's final color by considering the material properties and lighting conditions at each reflection point. This iterative process allows for the simulation of mirrored surfaces and multi-object reflections.

![图片包含 形状 描述已自动生成](thesis/assets/media/image171.png)

Fig. A2.6. Illustration of inter-object reflection showing ray paths

Fig. A2.6 illustrates how a light ray interacts with a reflective surface. The incident ray strikes the surface of one object, and the reflected ray intersects with a second object. The color and lighting contributions from the second object are then calculated and combined with those of the first to produce the final reflected effect. The reflection is computed using Eq. (A2-3):

$\mathbf{r} = \mathbf{i} - 2(\mathbf{i} \cdot \mathbf{N})\mathbf{N}$ (A2-3)

, where $\mathbf{r}$ is the reflected ray direction, $\mathbf{i}$ is the incident ray direction, and $\mathbf{N}$ is the normal vector at the point of intersection.

In Fig. A2.7, the visual results of reflections are demonstrated. Both spheres possess reflective properties, but their reflectivity coefficients differ. The sphere on the right exhibits a higher reflectivity, creating a pronounced mirror-like appearance that reflects the checkerboard floor and adjacent sphere. In contrast, the left sphere, with a lower reflectivity coefficient, produces a subtler reflection.

![蓝色的球 描述已自动生成](thesis/assets/media/image172.png)

Fig. A2.7. Spheres with high (right) and low (left) reflectivity

To prevent infinite recursion in complex scenes, a recursion depth is typically set. This parameter defines the maximum number of times a ray can reflect before being terminated. By limiting recursion depth, computational resources are managed efficiently while maintaining realistic results.

### A2.3.2. Refraction

In addition to reflection, ray tracing also accounts for refraction, where rays pass through transparent or semi-transparent objects, altering their trajectory according to Snell\'s law. Refraction is calculated using the indices of refraction of the two media involved. Fig. A2.8, illustrates this process, where a ray transitions from the purple object into the green object, resulting in a refracted direction.

![图示 中度可信度描述已自动生成](thesis/assets/media/image173.png)

Fig. A2.8. Refraction of a ray between two objects

Snell\'s law is applied to compute the refracted ray direction:

$\frac{\sin\left( \theta_{i} \right)}{\sin\left( \theta_{refract} \right)} = \frac{n_{2}}{n_{1}}$ (A2-4)

, where $\theta_{i}$ is the angle of incidence, $\theta_{refract}$ is the angle of refraction, and $n_{1}$ and $n_{2}$ are the indices of the refraction for the two media. The refracted ray can further interact with other objects in the scene, contributing to the final color and transparency effects.

![图片包含 建筑, 桌子, 板子, 大 描述已自动生成](thesis/assets/media/image174.png)

Fig. A2.9. Combined effects of reflection and refraction on two spheres

This rendered image shown in Fig. A2.9 demonstrates the simultaneous application of reflection and refraction in ray tracing. The sphere on the left primarily showcases refraction, with rays bending as they pass through the transparent surface, distorting the checkerboard pattern behind it. The sphere on the right exhibits reflective properties, with the surrounding environment and nearby objects mirrored on its surface.

## A2.4. Techniques for enhancing quality and efficiency

### A2.4.1. Supersampling and anti-aliasing

Supersampling is a fundamental technique to mitigate aliasing, a common artifact in computer graphics where jagged edges appear along diagonal or curved boundaries due to insufficient sampling resolution. By subdividing each pixel into multiple subpixels, rays are cast through each subpixel to calculate individual color contributions, which are then averaged to determine the final pixel color. This process ensures smoother transitions and more visually appealing results.

![](thesis/assets/media/image175.png)

Fig. A2.10. Supersampled render with 64 samples per pixel, illustrating significant quality improvement and reduced aliasing

In Fig. A2.10, supersampling with 64 samples per pixel is compared to Fig. A2.9, which lacks supersampling. The difference is striking: the jagged edges on the spherical surfaces and the ground plane in Fig. A2.9 are significantly reduced in Fig. A2.10, demonstrating the effectiveness of this technique in enhancing render quality.

Furthermore, anti-aliasing filters, such as box or Gaussian filters, can be applied to further refine the results by blending the subpixel colors, achieving seamless transitions across edges and gradients. While supersampling incurs additional computational cost, its impact on the final render quality makes it indispensable for high-quality visualizations.

### A2.4.2. Spatial partitioning for efficiency

Rendering complex scenes with numerous objects involves a significant computational challenge, particularly when calculating intersections for ray tracing, reflections, and refractions. Without optimization, every ray must be tested against all objects in the scene, leading to a prohibitive computational cost as the scene\'s complexity grows. Spatial partitioning techniques provide an effective solution by organizing objects into a hierarchical or grid-based structure, thereby reducing the number of intersection tests required.

Borrowing concepts from the neighbor search technique introduced in Appendix 1, spatial partitioning in rendering can be enhanced using structures like uniform grids， octrees, or bounding volume hierarchies (BVH). Each of these methods optimizes ray-object interactions by focusing computational effort on relevant regions of the scene.

In uniform grid-based spatial partitioning, the scene is divided into evenly spaced cells. As a ray propagates through the scene, it interacts with all the cells it traverses. Within each cell, only the objects present in that cell are considered for intersection tests. This approach minimizes unnecessary calculations and focuses computational resources on objects the ray is likely to encounter. While straightforward to implement, uniform grids are best suited for scenes with evenly distributed objects and can be less efficient in handling sparse or clustered object distributions.

Octrees divide the scene into a recursive hierarchy of eight cubic regions. Each node of the octree represents a spatial partition, which is further subdivided if it contains multiple objects. Rays only interact with objects in the partitions they traverse, significantly reducing the number of unnecessary intersection tests.

BVH is a hierarchical tree structure designed to optimize ray-object intersection tests by organizing objects into nested bounding volumes. Each node in the BVH represents a bounding volume, which completely encloses either individual objects (leaf nodes) or smaller bounding volumes (internal nodes). While uniform grids divide the space into fixed cells and octrees adaptively refine the space, BVH organizes objects based on their bounding volumes. This dynamic adaptability makes BVH especially effective in scenes with uneven object distributions.

Fig. A2.11 demonstrates the capability of ray tracing to handle scenes with many objects efficiently. Each sphere in this dense granular assembly is rendered with accurate lighting effects, such as reflections and refractions, showcasing the robustness of ray tracing algorithms in managing complex object interactions. The rendering highlights the application of spatial data structures, such as Bounding Volume Hierarchies (BVH) or uniform grids, to optimize the computational workload and achieve high-quality visualizations even for scenes with thousands of objects.

![图片包含 食物, 游戏机, 许多, 束 描述已自动生成](thesis/assets/media/image176.png)

Fig. A2.11. Large-scale ray tracing of granular assemblies with accurate reflections

## A2.5. Summary 

Appendix 2 explores the application of ray tracing for enhanced visualization in DEM simulations, showcasing its potential to improve the interpretability of granular material behavior.

Through successive sections, the chapter delves into lighting models, reflection, and refraction, illustrating how these factors are incorporated into ray tracing to achieve photorealistic renderings. The integration of diffuse and specular reflections, coupled with the recursive tracing of rays for inter-object interactions, demonstrates the intricate interplay of physics and computation in creating realistic visuals. This is exemplified through various figures, showcasing improvements in rendering quality with techniques like anti-aliasing.

Efficiency and scalability are addressed through spatial partitioning methods such as uniform grids, octrees, and bounding volume hierarchies, enabling ray tracing to handle complex DEM datasets with many objects. These techniques enhance the capability to visualize highly detailed granular assemblies.
