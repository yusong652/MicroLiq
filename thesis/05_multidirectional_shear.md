---
title: "Chapter 5: Effects Of Multi-Directional Shear Stress On Liquefaction Resistance"
tags: [thesis, chapter-5, multidirectional-shear, double-8-loading, seismic-loading, fabric-anisotropy]
aliases: [Multidirectional Shear, Chapter 5, Double-8 Loading]
---

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

![](thesis/assets/media/image113.png)

Fig. 5.1. Grain size distribution of curves of Toyoura sand and DEM simulation

![](thesis/assets/media/image114.png)

Fig. 5.2. Particle and contact force distribution after initial compaction, along with boundary and shearing rib configuration

As shown in Fig. 5.1, spherical particles with diameters ranging from 1.0 to 3.0 mm, approximating the distribution of Toyoura sand, were generated within a cubic space enclosed by periodic boundaries. Sample compaction was then achieved by adjusting the positions of ribbed shear walls oriented in the vertical direction and periodic boundaries in the horizontal directions, using a servo mechanism for the compaction process. A sample in an isotropic stress state, with all three principal stresses set to 100 kPa, was prepared for subsequent undrained cyclic shear tests as shown in Fig. 5.2.

### Application of unidirectional and multidirectional shear force

In studying the effects of multidirectional shear loading on the liquefaction process, other factors, such as changes in the magnitude of shear force, were often introduced. The primary aim of this chapter is to minimize the influence of these additional factors when modifying the direction of shear stress. Inspired by previous studies, this research employs a single-8 pattern for the first type of multidirectional shear. As shown in Eqs (5-1) and (5-2), and Fig. 5.3 (c), the single-8 multidirectional shear loading consists of a sinusoidal component $\tau_{8,\ \ x}$ in the x-direction and a sinusoidal component $\tau_{8,\ \ y}$ in the y-direction, with the amplitude being half of that in the x-direction and the period being half of the x-direction's cycle.

$\tau_{8,\ \ x} = CSR\sin\left( \frac{t}{T} \right)p_{0}'$ (5-1)

$\tau_{8,\ \ y} = 0.5CSR\sin\left( \frac{2t}{T} \right)p_{0}'$ (5-2)

To more quantitatively evaluate the impact of multidirectional shear loading compared to unidirectional loading on the liquefaction process, the unidirectional shear stress $\tau_{uni,x}$ is defined to equal the total magnitude of the multidirectional shear stress, and its sign is unified with that of $\tau_{8x}$, as shown in Eq. (5-3) and Fig. 5.3 (a) and (b). By ensuring the unidirectional and multidirectional figure-8 shear stresses have the same magnitude throughout the cyclic shear, the only difference between them is their direction.

$\tau_{uni,x} = sign\left( \tau_{8,x} \right)\sqrt{\tau_{8,x}^{2} + \tau_{8,y}^{2}}$ (5-3)

Although the magnitudes of unidirectional and multidirectional single-8 shear stresses are controlled to be equal, the multidirectional shear not only experiences variations in the shear force magnitude but also undergoes continuous changes in direction. This results in completely different rates of change between the two types of shear forces. This study introduces a new double-8 shear loading method to eliminate the impact of differing shear stress variation rates during undrained shear processes. In odd-numbered cycles, the double-8 shear stress has the same x and y components as the standard single-8 pattern. However, in even-numbered cycles, the x and y components are swapped, with the x component equaling the y component of the single-8, and vice versa. As the cycles progress, the double-8 axes of the shear stress periodically alternate between odd and even cycles, as described by Eqs (5-4) and (5-5) and Fig. 5.3(d).

$$\tau_{d8,x} = \begin{cases} \tau_{8,x}, & 2nT < t \leq (2n + 1)T \\ \tau_{8,y}, & (2n + 1)T < t \leq 2(n + 1)T \end{cases}, \quad n \in \{0,1,2,\ldots\}$$ (5-4)

$$\tau_{d8,y} = \begin{cases} \tau_{8,y}, & 2nT < t \leq (2n + 1)T \\ \tau_{8,x}, & (2n + 1)T < t \leq 2(n + 1)T \end{cases}, \quad n \in \{0,1,2,\ldots\}$$ (5-5)

The introduction of a comparison between the double-8 shear loading and the single-8 shear loading provides several benefits. First, it ensures that the magnitude of the two multidirectional shear stresses always remains equivalent. Second, it maintains similarity in the change rate of shear stress: during odd-numbered cycles, the change rate of the double-8 loading matches that of the single-8 loading, while during even-numbered cycles, the change rates are opposite but share the equal magnitudes.

![](thesis/assets/media/image115.png)![](thesis/assets/media/image116.png)

(a) Unidirectional shear stress evolution

\(b\) Unidirectional shear stress path

![](thesis/assets/media/image117.png)![](thesis/assets/media/image118.png)

\(c\) Single-8 shear stress path

\(d\) Double-8 shear stress path

Fig. 5.3. Shear stress path in unidirectional and multidirectional loading

Finally, the phase change between odd and even cycles for double-8 results in an equivalent rate in two directions, ensuring a smooth transition in shear stress. Through this comparative analysis, other factors that may influence liquefaction can be effectively excluded, allowing for a more rational evaluation of the impact of shear direction on the liquefaction process.

### Parameter validation

To validate the micro-parameters and numerical implementation, simulations were compared with experimental data from hollow cylinder apparatus (HCA) tests on dense Toyoura sand under monotonic undrained loading conditions reported by Nakata et al. (1998). The specimen was isotropically consolidated to $p'_{0}$=100 kPa before applying monotonic shear.

It should be noted that inherent differences exist between the DEM simulation and laboratory experiments. The DEM model employs periodic boundaries to eliminate wall friction effects and simulate an idealized infinite medium, whereas the HCA tests involve hollow cylindrical specimens with inner and outer radii creating non-uniform stress distributions across the specimen thickness. Despite these fundamental differences in boundary conditions and specimen geometry, the comparison remains meaningful as both configurations aim to achieve simple shear deformation under undrained conditions.

![](multiDirection/validation/validate_p_q_dense.png)

(a) Effective stress path

![](multiDirection/validation/validate_gamma_q_dense.png)

(b) Stress-strain relationship

Fig. 5.4. Validation of DEM simulation against monotonic undrained shear tests (Nakata et al., 1998): dense Toyoura sand with Dr≈80%, $p'_{0}$=100 kPa

The DEM simulation successfully captures the characteristic undrained behavior of dense sand: (1) dilative response in effective stress space, with the stress path initially moving leftward as $p'$ decreases, then turning rightward as $p'$ increases due to dilation while approaching the critical state line; (2) strain-hardening typical of dense specimens, where deviatoric stress $q$ increases monotonically with deviatoric strain $\varepsilon_{q}$. Quantitatively, close agreement is achieved in the small-strain regime ($\varepsilon_{q}$ < 0.5%), where both the initial stiffness and the contractive-dilative transition are well reproduced. At larger strains, the simulation follows the experimental trend while exhibiting slightly higher deviatoric stress, which can be attributed to the idealized periodic boundary conditions that eliminate the boundary effects present in physical specimens. Overall, the validation demonstrates that the micro-parameters calibrated in Chapter 4 remain applicable under different boundary configurations, providing a reliable foundation for the subsequent multi-directional shear investigations.

## Results and discussion

### Macroscopic response

#### Stress strain relationship

With the application of unidirectional and multidirectional cyclic shear loads to undrained samples, the mean effective stress $p'$ gradually decreases as shown in Fig. 5.5. When $p'$ drops below approximately 50% of its initial value, an increase in shear load causes a slight rise in $p'$, while a decrease in shear load leads to a significant reduction in $p'$, eventually resulting in liquefaction as $p'$ reaches zero. Even as $p'$ continuously varies, the shear patterns of unidirectional, single-8, and double-8 modes project onto $\tau_{x}$ and $\tau_{y}$ as anticipated, effectively maintaining their respective linear, single-8, and double-8 stress path shapes.

Figure 5.6 presents the liquefaction resistance under different forms of shear loading. The occurrence of liquefaction is defined as when the pore water pressure reaches 95% of the initial confining stress. It is evident that the unidirectional shear loading requires the highest cyclic number to reach liquefaction at the same CSR, compared to the multidirectional loadings. Following this, there is a difference between the required cyclic numbers for single-8 and double-8 shear stresses, with single-8 needing slightly more cycles than double-8. For instance, at CSR = 0.25, single-8 requires 30 cycles to reach liquefaction, whereas double-8 only requires about 22 cycles.

+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ![](thesis/assets/media/image119.jpeg) | ![](thesis/assets/media/image120.jpeg) |
+===============================================================================================================================+=======================================================================================================================+
| (a) Unidirectional loading                                                                                                    | (b) Single-8 loading                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ![](thesis/assets/media/image121.jpeg)         |                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| \(c\) double-8 loading                                                                                                        |                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

Fig. 5.5. Shear and mean effective stress evolution in unidirectional and multidirectional shear (CSR=0.250)

From a macroscopic perspective, the rotation of shear force direction has a significant impact on the liquefaction process. Although the magnitudes of unidirectional and multidirectional shear forces are equal at any given moment, the shear force direction in unidirectional loading remains fixed, unlike in multidirectional loading. This lack of directional rotation in unidirectional loading results in a higher number of cycles needed to reach liquefaction. Additionally, besides the influence of shear stress direction on the liquefaction process, the shear loading history also plays a role. For instance, although single-8 and double-8 paths share the same shear stress magnitude and rate of change at any given moment, the single-8 path maintains a

![](thesis/assets/media/image122.png)

Fig. 5.6. Liquefaction resistance under unidirectional and multidirectional shear stress

constant figure-8 orientation, while the double-8 path alternates its orientation with each odd and even cycle. This alternating orientation in the double-8 path results in a lower number of cycles needed to reach liquefaction. In addition to differences in the number of cycles required for liquefaction, the strain development behaviors of single-8 and double-8 also differ, as shown in Fig 5.7. As cyclic loading continues, both single-8 and double-8 shear paths exhibit figure-8 patterns in their strain development. However, distinct differences emerged in the two shear paths. The strain path under single-8 shear stress maintains a consistent orientation throughout the cycles, with each cycle expanding outward along both $\gamma_{zx}$ and $\gamma_{zy}$ directions. This results in a steady accumulation of strain that gradually shifts in a direction perpendicular to the primary single-8 axis. The strain path for double-8 stress alternates orientation with each cycle, causing the \"8-shape\" axis to shift periodically. As a result, the double-8 pattern shows more complex and irregular strain growth compared to the single-8 path, with less directional offset over time.

![](thesis/assets/media/image123.jpeg)![](thesis/assets/media/image124.jpeg)

(a) Strain evolution in single-8 loading

\(b\) Strain evolution in single-8 loading

Fig. 5.7. Comparison of strain evolution between single-8 and double-8 loading

#### Cumulative shear work

Shear work, defined as the work performed by the shearing rib on the specimen during cyclic loading, provides a scalar measure to evaluate liquefaction differences across various shear stress paths from a macroscopic perspective. In Fig. 5.8, before the EPWP reaches approximately 60 kPa, the double-8 path shows the highest EPWP at equivalent shear work levels, followed by single-8 path, with unidirectional path exhibiting the lowest EPWP. This order of EPWP increase is inversely related to the number of cycles required to reach liquefaction, with double-8 reaching liquefaction faster than single-8, and unidirectional taking the longest. Despite these differences, the shear work required to reach liquefaction is roughly similar across all three loading types. This indicates that while directional variations in shear stress influence the rate at which EPWP builds up, the total energy input needed to induce liquefaction remains consistent.

![](thesis/assets/media/image125.jpeg)

Fig. 5.8. Cumulative shear work evolution in liquefaction under unidirectional, single-8, and double-8 cyclic shear stress

### Microscopic interpretation

#### Evolution of coordination number

The coordination number is a key indicator of the microstructural characteristics, representing the average number of contacts per particle. Particles with fewer than two contact are considered unable to effectively transmit contact forces and therefore do not contribute to the skeletal microstructure of the granular material. These particles are identified as \"floaters\" and are excluded from the coordination number calculation, as shown in Eq. (5-6). Here, $Z_{m}$ denotes the mechanical coordination number. $N_{c}$ is​ the total number of contacts, and $N_{p}$​, $N_{1}$, and $N_{0}$ represent the total number of particles, particles with one contact, and particles with zero contacts, respectively.

$Z_{m} = \frac{2N_{c} - N_{1}}{N_{p} - N_{1} - N_{0}}$ (5-6)

![](thesis/assets/media/image126.png)

Fig. 5.9. Coordination number evolution in liquefaction under unidirectional, single-8, and double-8 cyclic shear stress

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

![](thesis/assets/media/image127.png)

Fig. 5.10. Invariant of anisotropic fabric tensor evolution in liquefaction under unidirectional, single-8, and double-8 cyclic shear stress

Figure 5.10 illustrates the evolution of fabric anisotropy $F_{c}$ under unidirectional, single-8, and double-8 shear stress paths throughout the liquefaction process. As the normalized cyclic number $N_{cyc}/N_{L}$ increases, $F_{c}$ first rises to a peak value before decreasing to a lower level. With each successive cycle, the peak values continue to increase, showing a gradual upward trend as liquefaction approaches. This cyclic oscillation pattern, with peaks that grow progressively higher, reflects the increasing anisotropy in the microstructure induced by continuous cyclic shearing.

The double-8 path demonstrates the highest level of anisotropy development, with $F_{c}$ reaching the largest value. This indicates that frequent directional changes enhance contact alignment and orientation, fostering an increasingly anisotropic structure within the particle assembly. This intensified anisotropy likely contributes to double-8's lower liquefaction resistance, as seen by its fewer cycles to reach liquefaction. The single-8 path exhibits intermediate anisotropy levels, with $F_{c}$ values between those of double-8 and unidirectional. The pattern allows for some anisotropic structural formation, though less intense than in double-8. This aligns with the single-8\'s liquefaction resistance, requiring more cycles than double-8 but fewer than unidirectional. The unidirectional path exhibits the lowest increase in fabric anisotropy, with $F_{c}$ consistently lower compared to the other two paths. The absence of directional changes limits the rearrangement of particles, preserving a more isotropic structure that can better withstand cyclic loading, thus requiring the largest number of cycles to achieve liquefaction.

#### Contact orientation

Fig. 5.11, 5.12, and 5.13 display the contact density distribution for the unidirectional, single-8, and double-8 shear paths throughout the liquefaction process, respectively. Each sequence shows how the contact density evolves from an initial state (at $N_{c}/N_{L}$=0) to stages closer to (at $N_{c}/N_{L}$=0.81) and beyond liquefaction (at $N_{c}/N_{L}$=1.03 and 1.08)​, highlighting the distinctions in fabric evolution among these paths. Across all shear paths, the contact density reduces, indicating a loosening in the particle arrangement. The contact orientations become more pronounced, showing a tendency toward specific directional alignment, which reflects a strengthening of anisotropic characteristics within the skeleton of fabric.

![](thesis/assets/media/image128.png)![](thesis/assets/media/image129.png)

(a) $N_{c}/N_{L}$=0.0

(b) $N_{c}/N_{L}$=0.81

![](thesis/assets/media/image130.png)![](thesis/assets/media/image131.png)

(c) $N_{c}/N_{L}$=1.03

(d) $N_{c}/N_{L}$=1.08

Fig. 5.11. Contact density evolution in liquefaction under unidirectional cyclic shear stress

At the stage of $N_{c}/N_{L}$=0.81, notable differences emerge among the three shear paths, reflecting their distinct responses to shear stress. For unidirectional path, contact density remains relatively uniform with limited directionality, indicating a weaker development of anisotropy compared to the other two paths. This is consistent with the previously observed lower fabric anisotropy $F_{c}$​, suggesting that the unidirectional path promotes a more isotropic structure, contributing to its higher liquefaction resistance.

![](thesis/assets/media/image132.png)![](thesis/assets/media/image133.png)

(a) $N_{c}/N_{L}$=0.0

\(b\) $N_{c}/N_{L}$=0.81

![](thesis/assets/media/image134.png)![](thesis/assets/media/image135.png)

\(c\) $N_{c}/N_{L}$=1.03

\(d\) $N_{c}/N_{L}$=1.08

Fig. 5.12. Contact density evolution in liquefaction under single-8 cyclic shear stress

For single-8 case, contact density shows moderate alignment along certain directions, revealing an intermediate degree of anisotropy. The contact density distribution is less uniform than in the unidirectional path but not as concentrated as in the double-8 path. This intermediate anisotropy level aligns with the fabric tensor $F_{c}$​ observed for single-8, reflecting moderate liquefaction resistance. For double-8 pattern, contact density exhibits more pronounced alignment in contact density and the highest degree of fabric concentration among the three paths. This is consistent with the high $F_{c}$ for double-8, as the directional changes in the shear path enhance the formation of an anisotropic structure.

![](thesis/assets/media/image136.png)![](thesis/assets/media/image137.png)

(a) $N_{c}/N_{L}$=0.0

(b) $N_{c}/N_{L}$=0.81

![](thesis/assets/media/image138.png)![](thesis/assets/media/image139.png)

(c) $N_{c}/N_{L}$=1.03

(d) $N_{c}/N_{L}$=1.08

Fig. 5.13. Contact density evolution in liquefaction under double-8 cyclic shear stress

After liquefaction, the differences in anisotropy among the three paths become less pronounced. However, a unique feature of the double-8 path is observed: The anisotropic alignment in the double-8 path shows a slight orientation toward the y-axis. This directional bias corresponds with the alternating stress direction characteristic of the double-8 path, where shear stress periodically changes direction in an \"8\" pattern. This alignment further reflects the macroscopic behavior of the double-8 path, where directional shifts in stress promote specific structural adaptations at the particle level.

### Discussion based on anisotropic critical state theory

The classical critical state theory provides foundational insight into the behavior of granular materials under large shear deformations. According to this theory, granular assemblies reach a \"critical state\" where both the void ratio and the stress ratio stabilize under continuous shear strain, maintaining constant values at a given principal stress. This theory has been widely used to describe the macroscopic characteristics of granular materials in soil mechanics and geotechnical engineering.

However, classical critical state theory does not explicitly account for the evolution of fabric anisotropy observed in granular materials. To address this, the anisotropic critical state theory extends the classical framework by integrating directional fabric properties and considering anisotropy as a critical factor influencing the material response.

## Summary

Chapter 5 delves into the influence of multi-directional shear stress paths on the liquefaction resistance of granular materials. Using numerical simulations, this chapter introduces innovative shear stress paths to isolate and analyze the impacts of directional changes. The findings highlight critical insights into how shear stress directionality alters both macroscopic and microscopic behaviors:

The unidirectional shear loading requires the highest cyclic number to reach liquefaction at the same CSR, compared to the multidirectional loadings. Single-8 needs slightly more cycles than double-8.

Although single-8 and double-8 paths share the same shear stress magnitude and rate of change at any given moment, the single-8 path maintains a constant figure-8 orientation, while the double-8 path alternates its orientation with each odd and even cycle. This alternating orientation in the double-8 path results in a lower number of cycles needed to reach liquefaction.

The directional shifts in stress under the double-8 shear pattern induce more pronounced structural adjustments at the particle level. These adjustments contribute to an accelerated liquefaction process.

