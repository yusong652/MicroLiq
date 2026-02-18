---
title: "Chapter 4: Study On Factors Affecting Liquefaction Resistance During Anisotropic Consolidation"
tags: [thesis, chapter-4, anisotropic-consolidation, K0-effect, HCA, liquefaction-resistance, experimental-validation]
aliases: [Anisotropic Consolidation, Chapter 4, K0 Effect]
---

# Study on Factors Affecting Liquefaction Resistance during Anisotropic Consolidation

This chapter employs DEM to investigate the effects of stress anisotropy on liquefaction resistance of sand soils through undrained cyclic shear simulations. A combined servo mechanism replicates undrained conditions and stress states in hollow cylinder apparatus (HCA) tests. The influence of lateral to vertical stress ratios ($K_{0}$) on the soil's response to cyclic loading is examined through three representative cases: compression ($K_{0}$=0.5), isotropic ($K_{0}$=1.0), and extension ($K_{0}$=2.0) states. Specimens are prepared following initial isotropic consolidation to $p'$=10 kPa followed by linear anisotropic consolidation (IC-AC) to $p'$=100 kPa. The factors that influence liquefaction resistance are attributed to changes in both macroscopic and microscopic quantities, such as void ratio and coordination number ($Z_{m}$). Anisotropic consolidation states with $K_{0}$<1.0 or $K_{0}$>1.0 produce different morphologies of contact density, affecting fabric anisotropy and liquefaction resistance.

##  Introduction

The phenomenon of liquefaction, which occurs with the loss of soil strength due to the buildup of pore water pressure during an earthquake, has been recognized for its potential to cause severe damage to infrastructure and buildings (Ishihara and Koga, 1981; Seed and Idriss, 1967). Triaxial tests have been extensively conducted to elucidate the mechanisms of liquefaction, where saturated specimens were subjected to cyclic loading under undrained conditions until liquefaction was triggered. The influence of factors such as cyclic stress ratio (CSR), relative density, as well as confining pressure on the resistance to liquefaction was examined (Hyodo et al., 1991; Seed and Lee, 1966; Silver et al., 1976; Toki et al., 1986; Yoshimi et al., 1984). However, vertically propagating shear waves in the ground apply gradually varying shear stress on soil elements, leading to a continuous rotation of principal stress axes (Arthur et al., 2009; Arthur et al., 1980; Ishihara and Yasuda, 1975; Ishihara and Towhata, 1983; Yamashita and Toki, 1993).

Alternative testing methods, such as the hollow torsional shear test, apply shear forces to specimens, allowing for continuous variation of principal stress axes and thereby addressing the limitations of the triaxial test. Ishihara and Yasuda (1975) pioneered the utilization of hollow torsional cylindrical apparatus (HCA) by subjecting the hollow cylindrical samples to irregular wave loading, studying the disparities compared to triaxial shear tests. Tatsuoka et al. (1986) performed both triaxial and torsional tests on specimens prepared using different methods and found that the results were inconsistent between the triaxial and torsional tests. Torsional and triaxial shear tests conducted by Yamashita and Toki (1993) and employed by Oka et al. (1999) to enhance the constitutive model for liquefiable sands also demonstrated that method of testing with torsional or triaxial shear, influences the results of liquefaction resistance. These studies highlight the significance of experimental methods, such as HCA tests, in liquefaction analyses and aroused great interest in numerical replication of these tests.

Soils under a natural state generally display various ratios of lateral to vertical effective stress, denoted as $K_{0}$. The impact of $K_{0}$ values on liquefaction strength frequently garners attention, yet the corresponding findings remain controversial. Ishihara and Takatsu (1979) observed that the liquefaction strength of Fuji River sand does not exhibit a notable dependency on the initial stress state with different $K_{0}$ values. Similar results were also obtained in the laboratory tests conducted by Yamashita and Toki (1993). On the other hand, the hollow torsional experiments conducted by Georgiannou and Konstadinou (2014) indicated that isotropically consolidated (IC) specimens demonstrate higher liquefaction resistance for loose sands than anisotropically consolidated (AC) specimens. By contrast, that pattern did not hold in dense states, where increasing relative density reversed the trend. Additionally, Vargas et al. (2020) concluded from similar laboratory tests on Ottawa sand with relative densities ranging from 50% to 80% that AC specimens with a $K_{0}$ of 0.5 showed a liquefaction strength approximately 20% higher than IC specimens. The experimental conclusions regarding the influence of $K_{0}$ on liquefaction resistance have been debated for decades, underscoring the necessity of elucidating $K_{0}$ effects on liquefaction resistance through alternative means. Additionally, the previous studies mentioned above focus primarily on a narrow range of initial states, typically involving $K_{0}$ values of 0.5, 1.0, and 2.0, without exploring a wider range of $K_{0}$.

The discrete element method (DEM) (Cundall and Strack, 1979) simulation provides an insight into granular material and offers advantages by eliminating concerns related to variations in initial states caused by sample preparation, making it a desirable numerical method to study the cause of changes in liquefaction resistance. Numerous examples utilizing DEM exist for undrained cyclic shear tests to find explanations of microscopic factors affecting liquefaction resistance. Huang et al. (2018) conducted undrained shear tests on triaxial specimens, trying to relate monotonic and cyclic behaviors. Yang et al. (2021) performed undrained simple shear tests and studied the influence of multi-directional shear stress on liquefaction resistance. Jiang et al. (2021) applied various forms of strain waves to specimens, investigating their impact on liquefaction resistance. Morimoto et al. (2021) examined the impact of pre-shearing on the liquefaction resistance using DEM simulation of undrained triaxial cyclic shear tests. Xie et al. (2023), as well as Yang and Huang (2023) explored the effect of liquefaction history-induced fabric on liquefaction resistance by conducting reliquefication simulation. Zhang et al. (2023) arranged ellipsoidal clumped pebbles and applied both vertical and horizontal shear loading in to discuss the influence of inherent fabric anisotropy on liquefaction resistance. Some of these studies included triaxial specimens, which do not account for principal stress axis rotation. Others utilized virtual periodic boundaries or cubic rigid box, which are difficult to implement in real-world scenarios. Replicating HCA tests through simulation provides a meaningful connection between numerical and experimental methods.

Using DEM to replicate HCA test is relatively specialized, but still has precedents. Li et al. (2014) conducted DEM simulations of drained tests and investigated the strain localization in HCA test. Liu et al. (2021) conducted analysis of torsional shear tests under drained conditions and investigated the development of cracks at different principal stress rotation angles. This study introduced an algorithm that realizes both undrained and stress conditions in HCA test, filling a gap in HCA simulation using DEM (Ma et al., 2024).

To clarify the influence of the $K_{0}$ on liquefaction resistance, Yang and Taiebat\'s (2024) consolidated specimens with different preparation methods and conducted undrained cyclic shear tests. They found that both preparation protocols and $K_{0}$ influence liquefaction resistance. As the relative density increased, the difference in liquefaction resistance narrowed gradually for IC and AC states. Otsubo et al. (2022) employed $K_{0}$ to induce inherent fabric anisotropy in specimen under a low stress condition and then consolidated it to the target $p'$ and examined its effects on liquefaction resistance. A specimen with higher anisotropy has weaker stiffness in its minor direction and resulted a lower liquefaction resistance. Still, $K_{0}$ values discussed in the mentioned numerical studies lie in a limited range. For instance, comparison between $K_{0}$=1.0 and $K_{0}$=0.5 (Yang and Taiebat\'s, 2024) or from $K_{0}$=0.75 to $K_{0}$=1.35 (Otsubo et al., 2022), and exploration beyond these thresholds is lacking.

The stress paths for specimen preparation often entail linearly increasing $p'$ and $q$ to the state with target $K_{0}$ in both experimental (Vargas et al., 2020) and numerical (Yang and Taiebat, 2024) tests. This study demonstrates DEM analysis of cyclic undrained HCA tests (Ma et al., 2024) and explores the effects of $K_{0}$ on liquefaction resistance. Specimens are prepared via an IC-AC stress path, where initial isotropic consolidation is followed by linear anisotropic consolidation to the target $K_0$, and subjected to a range of cyclic shear stress ratios. By examining macroscopic and microscopic responses such as fabric evolution, this study aims to provide evidence that elucidates how stress anisotropy influences liquefaction resistance.

## DEM simulation setup

### Specimen preparation

Itasca PFC^3D^ (Itasca Consulting Group, Inc., 2021) was employed to implement DEM simulations of undrained cyclic torsional shear test. Unlike the periodic boundaries commonly used in element tests, the HCA in DEM simulation employs two cylinders, upper and lower planes, as well as six blades to provide torsional force, closely approximating the boundary conditions of HCA (Ishihara and Yasuda, 1975; Vargas et al., 2020; Li et al, 2014; Liu et al, 2021). As shown in Fig. 4.1(a), two rigid cylindrical walls with inner diameter of 6 cm and outer diameter of 10 cm are positioned coaxially and vertically, with the upper and lower planes placed 10 cm apart, resembling the geometric dimensions of laboratory tests (Vargas et al., 2020).

![](thesis/assets/media/image65.jpg)

(a) Pouring method for generating particles

![](thesis/assets/media/image66.jpg)

(b) Insertion of torsional blades

Fig. 4.1. Specimen generation process in the initial stage using the pouring method and insertion of torsional blades

This research employed a uniform particle size distribution ranging from 1.5 mm to 3.0 mm, and utilizes a rolling resistance contact model (Iwashita and Oda, 1998; Wensrich and Katterfeld, 2012) to mimic the non-spherical effects of sand particles. The specific parameters of the contact model are listed in Table 4-1. To ensure similarity with laboratory methods, the particles were initially generated in the upper part of the apparatus and then allowed to flow downward under the influence of gravity, forming the specimen as shown in Fig. 4.1(a). The stress calculations of HCA are summarized according to the formulas provided in Table 4-2 ,where the values of $\sigma_{z}$ and $\sigma_{\theta}$ are derived from the equilibrium relations, $\varepsilon_{z}$ and $\gamma_{z\theta}$ are based on strain compatibility, and the remaining stress and strain expressions align with the assumption of linear elasticity (Hight et al., 1983).

Table 4-1. Parameters in DEM simulation

  ------------------------------------------------------------------------------------------
  Description                                                               Value
  ------------------------------------------------------------------------- ----------------
  Number of particles $N_{p}$                                               53,764

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

\*\*AC, and Cyclic shear

The typical approach of applying shear force to cuboidal (Wei et al., 2020; Yang et al., 2021; Banerjee et al., 2023) or cylindrical (Li et al., 2014; Liu et al., 2021) elements involves selecting and regulating the flexibility of the particles on both sides of the specimen. However, this method for providing torque on HCA specimens raises concerns, as the selected and constrained particles interfere with the cylinders' expansion or contraction, affecting the measurement of radial stresses. Therefore, using

Table 4-2. Equations of stress and strain in the HCA

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

wall elements that solely interact with particles to apply shear loads is preferred. The gravity was removed to achieve a uniform stress state and then, as shown in Fig. 4.1(b), vertically arranged torsional blades consisting of six wall elements were inserted into the specimen.

To achieve the target stress levels for anisotropic consolidation, a servo mechanism (Itasca Consulting Group, 2021; Ma et al., 2024) is employed to manipulate the position of vertices of wall elements throughout the consolidation process. Fig. 4.2 shows the stress and void ratio evolution during the anisotropic consolidation process for three representative $K_{0}$ values.

![](thesis/assets/images/fig3_2a_aniso_stress.png)

(a) Mean effective stress $p'$ vs. deviator stress $q$

![](thesis/assets/images/fig3_2b_stress_void.png)

(b) Mean effective stress $p'$ vs. void ratio $e$

Fig. 4.2. Stress and void ratio evolution in anisotropic consolidation for specimens with three representative stress anisotropies ($K_{0}$=0.5, 1.0, 2.0) from isotropic consolidation state with $p'$=10.0kPa to target mean effective stress $p'$=100.0kPa

The specimen was initially compressed to a target void ratio of approximately 0.736 under a friction coefficient of 0.0. Subsequently, the friction coefficient was reset to 0.5, followed by anisotropic consolidation from a state with $p'$=10.0kPa and $K_{0}$=1.0 to $p'$=100.0kPa and the target $K_{0}$ (IC-AC protocol). Notably, during the AC process with an increasing $p'$, $K_{0}$ evolves from 1.0 to the corresponding target $K_{0}$. Three representative cases with $K_{0}$ values of 0.5, 1.0, and 2.0 are examined, representing compression ($K_{0}$<1.0), isotropic ($K_{0}$=1.0), and extension ($K_{0}$>1.0) states, respectively. During the AC process, both $p'$ and $q$ increase simultaneously, with the stress path depending on the target $K_{0}$ value, as illustrated in Fig. 4.2(a) and Fig. 4.2(b).

As indicated by Fig. 4.2(b), the void ratio decreases from approximately 0.736 at the initial state ($p'$=10 kPa) to around 0.732 at the target stress ($p'$=100 kPa) during anisotropic consolidation. The differences in final void ratio $e$ between different $K_{0}$ states after IC-AC are minimal, with $e$ ranging from 0.7315 to 0.7325. This small variation (approximately 0.001) makes it reasonable to emphasize the effects of microscopic quantities, such as coordination number and fabric anisotropy, rather than $e$, on liquefaction resistance.

![](thesis/assets/media/image67_k05.jpg)

(a) $K_{0}$=0.5

![](thesis/assets/media/image67_k10.jpg)

(b) $K_{0}$=1.0

![](thesis/assets/media/image67_k20.jpg)

(c) $K_{0}$=2.0

Fig. 4.3. Visualization of hollow cylindrical specimens after anisotropic consolidation to $p'$=100 kPa with different $K_{0}$ values. Cross-sectional view shows particles (colored by radius) and contact forces (red vectors), corresponding to the final states in Fig. 4.2.

### Implementation of undrained condition

In DEM simulations of undrained tests, the interaction between water and particles is disregarded, employing a constant volume approach to replicate the undrained condition. The effectiveness of this constant volume approach has been validated in numerous DEM simulations (Sitharam et al., 2002; Yimsiri and Soga, 2010). To simultaneously achieve the stress boundary conditions and undrained condition observed in laboratory HCA tests, an innovative combined servo mechanism is proposed.

The key challenge in simulating undrained HCA tests lies in satisfying multiple conditions simultaneously. In laboratory tests, the inner and outer chamber pressures ($p_i$ and $p_o$) are maintained equal and constant, the additional axial pressure ($p_z$) or height ($H$) is controlled, and a target shear stress ($\tau_{z\theta,tar}$) is applied. Meanwhile, the undrained condition requires constant volume. This study addresses these challenges through a combined servo mechanism by controlling four kinematic variables: inner radius rate ($dr/dt$), outer radius rate ($dR/dt$), height rate ($dH/dt$), and rotation angle rate ($d\theta/dt$), to satisfy four condition equations simultaneously.

**Condition 1: Equal inner and outer chamber pressures**

To address the inhomogeneity in radial direction caused by the axial symmetry of HCA, the difference in effective stresses between the outer and inner cylinders is regulated by controlling the diameter variation. The inner radius rate is determined by Eq. (4-1), where $\sigma_{dif,r}'$ represents the effective stress difference between outer and inner cylinders, and $S_{cr}$ is the servo coefficient.

$$\frac{dr}{dt} = \frac{\left(\sigma_{dif,r}' - (p_o - p_i)\right)}{\Delta t}S_{cr}$$ (4-1)

**Condition 2: Constant additional axial pressure or constant height**

During undrained cyclic shear, the height can be controlled either as constant (dH/dt = 0) or through additional axial pressure regulation. The height rate is governed by Eq. (4-2), where $\sigma_{dif,z}'$ denotes the effective stress difference between axial and radial stress, and $S_{cz}$ is the corresponding servo coefficient.

$$\frac{dH}{dt} = \frac{\left(\sigma_{dif,z}' - p_z\right)}{\Delta t}S_{cz} \qquad \frac{dH}{dt} = 0\ \text{if constant}\ H$$ (4-2)

**Condition 3: Target shear stress**

The rotation angle rate is controlled to achieve the target shear stress through Eq. (4-3), where $T_{dif}$ represents the torque difference between target and current value, and $S_{cs}$ is the servo coefficient.

$$\frac{d\theta}{dt} = \frac{T_{dif}}{\Delta t}S_{cs}$$ (4-3)

**Condition 4: Undrained condition (constant volume)**

The undrained condition is ensured by maintaining constant volume throughout the cyclic shear test, as expressed in Eq. (4-4).

$$2\pi H\left(R\frac{dR}{dt} + r\frac{dr}{dt}\right) + \pi(R^2 - r^2)\frac{dH}{dt} = 0$$ (4-4)

By combining these four equations, the system of four kinematic variables ($dr/dt$, $dR/dt$, $dH/dt$, $d\theta/dt$) and four constraints is solved simultaneously at each timestep, achieving both the stress conditions and undrained condition in DEM simulation of HCA tests. This combined servo mechanism (Ma et al., 2024) elegantly replicates the boundary conditions observed in laboratory undrained cyclic torsional shear tests.

**Determination of servo coefficients**

The servo coefficients ($S_{cr}$, $S_{cz}$, $S_{cs}$) in the combined servo mechanism are determined based on the contact stiffness between boundaries and particles. For the torsional servo coefficient $S_{cs}$ in Condition 3, the moment of inertia of shear stiffness $I_{rot}$ is calculated considering the distance from the center of rotation. Fig. 4.4 illustrates the contact between a particle and a blade, where $r_{d}$ denotes the distance from the center of rotation to the contact point, and $\theta$ is the angle between the contact normal and the horizontal plane.

![](thesis/assets/media/image73.png)

Fig. 4.4. Determination of moment of inertia of shear stiffness in servo mechanism for torque application

The moment of inertia $I_{rot}$ is calculated by Eq. (4-5), where $k_{n}$ represents the normal contact stiffness. The contribution of each contact is adjusted by $\cos^{2}\theta$ because a larger $\theta$ reduces its contribution to the shear stiffness. The servo coefficient $S_{cs}$ for torsional control is then determined by Eq. (4-6).

$$I_{rot} = \Sigma r_{d}^{2}k_{n}\cos^{2}\theta$$ (4-5)

$$S_{cs} = \frac{1}{I_{rot}}$$ (4-6)

Similarly, the servo coefficients $S_{cr}$ and $S_{cz}$ for radial and axial directions are determined based on the equivalent stiffness of inner/outer cylinders and top/bottom plates, respectively. This stiffness-based approach ensures stable and efficient convergence of the combined servo mechanism.

**Excess pore water pressure calculation**

The effective stresses are evaluated by measuring the contact stresses between the boundary and particle skeleton. The assumptions of undrained condition and full saturation result in variations in effective stress on lateral cylinders and excess pore water pressure (EPWP) that are equal in magnitude but opposite in sign, as quantified in Eq. (4-7). Here, $u$ represents the EPWP, $\sigma_{r}'$ denotes the radial effective stress derived from the inner and outer effective stresses, and $\sigma_{r0}'$ is its initial value (Yimsiri and Soga, 2010).

$$u = \sigma_{r0}' - \sigma_{r}'$$ (4-7)

### Parameter calibration and validation

The micro-parameters listed in Table 4-1 were determined through a systematic iterative calibration procedure against experimental data from hollow cylinder apparatus tests on dense Toyoura sand. Since the micro-parameters collectively influence macroscopic responses including shear stiffness, dilatancy, and liquefaction resistance, the calibration followed an iterative strategy targeting these behaviors in sequence.

Starting from a base set of parameters at a given void ratio, the contact Young's modulus $E$ and rolling friction coefficient $\mu_r$ were adjusted while keeping the normal-to-shear stiffness ratio $\kappa$ constant, aiming to reproduce the macroscopic shear stiffness observed in undrained monotonic shear tests. The effective stress path in $p'$-$\tau_{z\theta}$ space was then examined, where the evolution of $p'$ reflects the dilatancy characteristics of the specimen. If the simulated dilatancy was insufficient, the specimen was further compacted to a lower void ratio, which increased both dilatancy and shear stiffness; the contact modulus $E$ was then reduced accordingly to restore the target shear stiffness. This iterative process between void ratio, contact modulus, and rolling friction was repeated until both the shear stiffness (stress-strain relationship) and dilatancy (effective stress path) simultaneously matched the monotonic experimental data. Finally, the calibrated parameters were verified against cyclic liquefaction resistance curves, with minor adjustments made as needed to achieve satisfactory agreement across all three aspects. The resulting parameters (Table 4-1) were employed for all subsequent simulations.

#### Monotonic shear validation

Undrained monotonic shear simulations were compared with HCA tests reported by Nakata et al. (1998). The specimen was isotropically consolidated to $p'_{0}$=100 kPa ($K_{0}$=1.0) before applying monotonic torsional shear. Following the experimental protocol, the additional axial pressure $p_z$ was maintained at zero (i.e., $\sigma_{dif,z}' = 0$ in Eq. 4-2) to ensure the axial effective stress equals the radial effective stress during shearing. The micro-parameters listed in Table 4-1 were employed.

![](thesis/assets/images/validate_p_q_dense.png)

(a) Effective stress path

![](thesis/assets/images/validate_gamma_q_dense.png)

(b) Stress-strain relationship

Fig. 4.5. Validation of DEM simulation against monotonic undrained shear tests (Nakata et al., 1998): dense Toyoura sand with Dr≈80%, $p'_{0}$=100 kPa, $K_{0}$=1.0

The DEM simulation successfully captures the characteristic undrained behavior of dense sand: (1) dilative response in effective stress space, with the stress path initially moving leftward as $p'$ decreases, then turning rightward as $p'$ increases due to dilation while approaching the critical state line; (2) strain-hardening typical of dense specimens, where deviatoric stress $q$ increases monotonically with deviatoric strain $\varepsilon_{q}$. The close agreement between simulation and experimental results validates both the micro-parameters and the combined servo mechanism described in Section 4.2.2.

#### Cyclic shear validation

Liquefaction resistance under cyclic loading was validated against the classical data of Ishihara et al. (1985). Specimens were isotropically consolidated to $p'_{0}$=100 kPa ($K_{0}$=1.0) and then subjected to sinusoidal torsional shear with 8 Hz frequency. Liquefaction was defined as the condition when single-amplitude shear strain reached $\gamma$=2.0%.

![](thesis/assets/images/validate_N_csr.png)

Fig. 4.6. Cyclic stress ratio (CSR) versus number of cycles to liquefaction: validation against Ishihara et al. (1985) for dense Toyoura sand

Five CSR levels (0.20, 0.25, 0.30, 0.35, 0.40) were simulated. The DEM results align well with experimental trends across the full range of cyclic stress ratios, demonstrating the model's capability to reproduce the characteristic CSR-N liquefaction resistance curve. Both monotonic and cyclic validations confirm that the DEM model can accurately reproduce undrained behavior of dense Toyoura sand under different loading modes.

Having validated the model against isotropic consolidation conditions ($K_{0}$=1.0), the following sections investigate how different consolidation stress ratios affect liquefaction resistance. Specimens with three representative $K_{0}$ values (0.5, 1.0, 2.0) obtained from the IC-AC protocol underwent undrained cyclic torsional shear until liquefaction occurred. The cyclic shear stress is applied as a sinusoidal wave with different cyclic stress ratios (CSR). Unlike the monotonic shear validation where zero additional axial pressure was maintained, constant height (dH/dt = 0) is adopted for all cyclic shear simulations to match typical HCA test protocols and maintain consistent boundary conditions across different $K_{0}$ states. The factors influencing liquefaction resistance are discussed from both macroscopic and microscopic perspectives.

## Results and discussion

### Macroscopic response

#### Stress strain relationship

Fig. 4.7, 4.8, 4.9, and 4.10 present typical stress and strain evolution during undrained cyclic shear for specimens with different initial $K_{0}$ values at CSR=0.200. Liquefaction is defined as occurring when EPWP ratio $r_{u}$ reaches 95% of initial radial effective stress $\sigma_{r0}'$.

![](thesis/assets/images/stress_rel.png)

Fig. 4.7. Shear stress $\tau_{z\theta}$ vs. mean effective stress $p'$ ($K_{0}$=1.0, CSR=0.200)

As the shear stress $\tau_{z\theta}$ cyclically acts on the hollow cylindrical specimen, the mean effective stress $p'$ exhibits an overall decrease. Once $p'$ falls below approximately 60 kPa, an increase in the magnitude of $\tau_{z\theta}$ drives an upward trend in $p'$, displaying a butterfly-shaped relationship. After liquefaction onset, $p'$ and $\tau_{z\theta}$ delineate the critical state line and converge at the origin periodically.

![](thesis/assets/images/stress_strain.png)

Fig. 4.8. Shear stress $\tau_{z\theta}$ vs. shear strain $\gamma_{z\theta}$ ($K_{0}$=1.0, CSR=0.200)

The stress-strain relationship shows stiff shear modulus with slight reduction in the initial stage. As cyclic loading progresses towards liquefaction, shear stiffness markedly decreases, plastic deformation occurs, and strong nonlinearity becomes evident in the hysteretic loops.

![](thesis/assets/images/stress_dev.png)

Fig. 4.9. Deviatoric stress $\sigma_{vM}$ vs. mean effective stress $p'$ for three $K_{0}$ values (CSR=0.200)

To compare the effects of initial stress anisotropy, the deviatoric von-Mises stress $\sigma_{vM}$ evolution is shown for three $K_{0}$ values. The $K_{0}$=1.0 specimen starts with $\sigma_{vM}$ at zero due to isotropic consolidation, while $K_{0}$=0.5 and $K_{0}$=2.0 specimens exhibit initial deviatoric stress due to anisotropic consolidation. As cyclic shear progresses, specimens with different $K_{0}$ values follow distinct stress paths toward the critical state line, with varying rates of stress degradation and liquefaction resistance.

![](thesis/assets/images/stress_u_compare.png)

Fig. 4.10. Excess pore water pressure ratio $r_{u}$ evolution for three $K_{0}$ values (CSR=0.200)

The EPWP responses differ significantly among the three $K_{0}$ states. The $K_{0}$=2.0 specimen shows the most rapid $r_{u}$ accumulation, reaching liquefaction after approximately 29 cycles. The $K_{0}$=1.0 specimen exhibits intermediate behavior with liquefaction occurring after 31 cycles. In contrast, the $K_{0}$=0.5 specimen demonstrates the highest liquefaction resistance, reaching the liquefaction criterion after 39 cycles. These observations provide clear evidence that initial stress anisotropy significantly influences liquefaction resistance.

#### Liquefaction resistance curves

To systematically investigate how liquefaction resistance varies with CSR and $K_{0}$, Fig. 4.11 presents the cyclic stress ratio versus number of cycles to liquefaction for three representative $K_{0}$ values.

![](thesis/assets/images/liq_res_cur.png)

Fig. 4.11. Cyclic liquefaction resistance curves for specimens with three representative stress anisotropies ($K_{0}$=0.5, 1.0, 2.0)

The liquefaction resistance curves demonstrate clear dependency on initial stress anisotropy. For all CSR levels tested, the isotropic consolidation state ($K_{0}$=1.0) exhibits intermediate liquefaction resistance. The compression state ($K_{0}$=0.5) shows the highest resistance, requiring more cycles to reach liquefaction at the same CSR. Conversely, the extension state ($K_{0}$=2.0) demonstrates the lowest resistance, reaching liquefaction with fewer cycles. This trend reveals that the effect of $K_{0}$ on liquefaction resistance depends not only on the magnitude of stress anisotropy but also on its direction: compression conditions ($K_{0}$<1.0) enhance liquefaction resistance relative to the isotropic state, while extension conditions ($K_{0}$>1.0) reduce it. The observed directional dependency is consistent with the findings by Georgiannou and Konstadinou (2014) for dense sand states and the experimental results of Vargas et al. (2020) who reported approximately 20% higher liquefaction strength for $K_{0}$=0.5 specimens compared to isotropic conditions. This contrasts with some earlier experimental studies (Ishihara and Takatsu, 1979; Yamashita and Toki, 1993) that reported minimal $K_{0}$ dependency.

#### Cumulative shear work

Cumulative shear work refers to the energy input during undrained cyclic shear in this study. It is valuable to examine the correlation between the liquefaction resistance of soils and their susceptibility to the input energy. Towhata and Ishihara (1985) conducted a series of experiments where specimens were subjected to undrained cyclic shear under various loading conditions. They revealed a unique relationship between excess pore water pressure and shear work, despite differences in stress anisotropy. Figueroa et al. (1994) similarly confirmed that the shear work required for triggering liquefaction is independent of the amplitude of strain through strain-controlled tests. Georgiannou and Konstadinou (2014) concluded from the comparison between IC and AC specimens that the energy associated with terminal water pressure is positively correlated with relative density. For equivalent relative densities, AC specimens require greater energy than IC specimens to induce liquefaction.

![](thesis/assets/images/acc_energy.png)

(a) $W_{s}$ vs. $N_{c}/N_{L}$

![](thesis/assets/images/acc_energy_EPWP.png)

(b) $r_{u}$ vs. $W_{s}$

Fig. 4.12. Evolution of cumulative unit volume shear work and shear work required to trigger liquefaction for different $K_{0}$

The cumulative unit volume shear work $W_{s}$ is defined as shown in Eq. (4-8), expressed as an integral of shear strain rate $\dot{\gamma_{z\theta}}$, shear stress $\tau_{z\theta}$, and incremental time $dt$. This represents the accumulated input energy per unit volume in the specimen.

$W_{s} = \int_{0}^{t}{\dot{\gamma_{z\theta}}\tau_{z\theta}dt}$ (4-8)

As indicated by Fig. 4.12(a), in the liquefaction process normalized by $N_{L}$, the cumulative shear work evolution is nearly identical for all three $K_{0}$ values, indicating that the normalized energy accumulation pattern is independent of initial stress anisotropy. Fig. 4.12(b) explores the relationship between $W_{s}$ and $r_{u}$. For the same amount of shear work, the $K_{0}$=0.5 specimen exhibits lower $r_{u}$ compared to $K_{0}$=1.0 and $K_{0}$=2.0, indicating greater resistance to pore pressure buildup. Consequently, the shear work required to trigger liquefaction $W_{sL}$ is highest for the $K_{0}$=0.5 specimen. Notably, the $K_{0}$=1.0 specimen exhibits the lowest $W_{sL}$ despite requiring more loading cycles than $K_{0}$=2.0, because its higher initial shear stiffness results in smaller strain amplitude per cycle and hence less energy input per cycle.

#### Shear wave velocity evolution

The response in cumulative shear work inspired an exploration of the relationship between shear stiffness and liquefaction resistance (Xu et al., 2015). The shear modulus $G$ is defined as the ratio of shear stress increment to shear strain increment, and Eq. (4-9) describes the shear wave velocity $V_{s}$ in terms of the shear modulus $G$ and the saturated density $\rho_{sat}$ (Tokimatsu and Uchida, 1990; Chen et al., 2005).

$V_{s} = \sqrt{\frac{G}{\rho_{sat}}}$ (4-9)

![](thesis/assets/images/shear_wave_velocity.png)

Fig. 4.13. Evolution of shear wave velocity during cyclic shear for different $K_{0}$ values, showing loading and unloading stiffness separately (CSR=0.200)

Fig. 4.13 presents the evolution of shear wave velocity $V_s$ during undrained cyclic shear, with loading and unloading phases plotted separately. The loading $V_s$ is calculated from the first and third quarter-periods of each cycle, while the unloading $V_s$ is calculated from the second and fourth quarter-periods. The inset shows the initial shear wave velocity $V_{s0}$ for both loading and unloading conditions. For all three $K_0$ states, unloading stiffness is consistently higher than loading stiffness, reflecting the typical hysteretic behavior of granular materials under cyclic loading.

The $K_0$=1.0 specimen exhibits the highest $V_s$ throughout the cyclic shear process for both loading and unloading conditions, with initial values of approximately 195 m/s (loading) and 210 m/s (unloading). The $K_0$=0.5 and $K_0$=2.0 specimens show lower and comparable values, with initial loading $V_s$ around 175-180 m/s. During the early stages of cyclic loading ($N_c/N_L < 0.6$), all specimens show gradual degradation of $V_s$. However, as the specimens approach liquefaction ($N_c/N_L > 0.6$), the degradation rate accelerates dramatically, with loading $V_s$ dropping to approximately 25-40 m/s and unloading $V_s$ to approximately 90 m/s at liquefaction. Notably, as the specimens approach liquefaction, the $V_s$ curves for all three $K_0$ states converge, indicating that the influence of initial stress anisotropy on shear stiffness diminishes as the fabric structure progressively degrades.

Combining Fig. 4.12 and Fig. 4.13 provides a comprehensive macroscopic interpretation of how anisotropic consolidation affects liquefaction resistance. For $K_0$=1.0 and $K_0$=2.0, Fig. 4.12(b) shows similar $r_u$-$W_s$ relationships and comparable $W_{sL}$ values, suggesting similar energy dissipation characteristics. However, Fig. 4.13 reveals that the $K_0$=1.0 specimen maintains consistently higher $V_s$ throughout the cyclic shear process compared to $K_0$=2.0. This higher stiffness results in smaller strain amplitude per cycle, requiring more cycles to accumulate sufficient strain for liquefaction. Thus, the $K_0$=1.0 specimen exhibits greater liquefaction resistance than $K_0$=2.0 despite similar energy requirements.

For the $K_0$=0.5 specimen, although both loading and unloading stiffness during cyclic shear are comparable to those of $K_0$=2.0 (Fig. 4.13), Fig. 4.12(b) clearly demonstrates that achieving the same $r_u$ level requires substantially more shear work for $K_0$=0.5 compared to $K_0$=1.0 and $K_0$=2.0. This indicates that the $K_0$=0.5 specimen possesses greater resistance to pore pressure buildup per unit energy input. Consequently, the $K_0$=0.5 specimen requires the most cycles to reach liquefaction and exhibits the highest liquefaction resistance among the three states, despite having similar shear stiffness to the extension state ($K_0$=2.0).

While shear stiffness and energy dissipation provide useful macroscopic characterizations, they do not explain why the compression state ($K_0$=0.5) exhibits greater resistance to pore pressure buildup, or why specimens with similar energy requirements show different liquefaction resistance. Macroscopic parameters such as void ratio and stiffness cannot capture the underlying particle-scale fabric structure that ultimately governs the mechanical response. To elucidate the fundamental mechanisms, the following sections examine microscopic quantities and their evolution under different $K_0$ states.

### Microscopic interpretation

#### Evolution of coordination number

The coordination number quantifies the average number of contacts per particle, serving as a scalar measure of fabric compactness in granular materials (Oda, 1977; Shire and O'Sullivan, 2012; Fei and Narsilio, 2020). To focus on load-bearing particles, the mechanical coordination number $Z_m$ excludes "floaters"—particles with fewer than two contacts that cannot stably transmit interparticle forces (Thornton, 2000; Hu et al., 2023):

$Z_{m} = \frac{2N_{c} - N_{1}}{N_{p} - N_{1} - N_{0}}$ (4-10)

where $N_c$ is the total number of interparticle contacts, $N_p$ is the total number of particles, and $N_1$ and $N_0$ are the numbers of particles with one and zero contacts, respectively.

![](thesis/assets/images/CoordNum.png)

Fig. 4.14. Mechanical coordination number evolution in cyclic shear and relationship between cyclic number required for liquefaction and initial mechanical coordination number (CSR=0.200)

Figure 4.14 shows the evolution of $Z_{m}$ under different initial $K_{0}$ states during cyclic shear. The initial mechanical coordination number $Z_{m0}$ varies with stress anisotropy: the isotropically consolidated specimen ($K_0$=1.0) exhibits the highest $Z_{m0}$ of approximately 5.0, while the anisotropically consolidated specimens ($K_0$=0.5 and $K_0$=2.0) show lower values around 4.9. This difference in $Z_{m0}$ may contribute to the higher initial shear stiffness observed in the $K_0$=1.0 specimen (Fig. 4.13), as more interparticle contacts generally lead to a stiffer fabric structure.

As cyclic loading progressed, $Z_{m}$ decreased gradually during the early stage ($N_c/N_L < 0.8$), followed by an accelerated decline as the specimen approached liquefaction. This reduction in $Z_{m}$ reflects the progressive loss of interparticle contacts and fabric integrity. Liquefaction was triggered when $Z_{m}$ dropped to approximately 4.0. Regardless of the initial $K_{0}$, the post-liquefaction $Z_{m}$ fluctuates around similar values, suggesting that the initial stress anisotropies have minimal influence on the post-liquefaction fabric structure.

The inset in Fig. 4.14 shows the relationship between $Z_{m0}$ and liquefaction resistance $N_L$. While the comparison between $K_0$=1.0 and $K_0$=2.0 shows that higher $Z_{m0}$ corresponds to slightly higher liquefaction resistance (Fig. 4.11), the comparison between $K_0$=0.5 and $K_0$=1.0 reveals a different pattern: despite having lower $Z_{m0}$, the $K_0$=0.5 specimen exhibits considerably higher liquefaction resistance. Moreover, although $K_0$=0.5 and $K_0$=2.0 have similar $Z_{m0}$ values, they exhibit markedly different liquefaction resistance. These observations suggest that coordination number alone cannot fully account for liquefaction resistance, and that the direction of stress anisotropy—compression versus extension—may influence fabric structure in ways that affect liquefaction behavior.

#### Evolution of fabric anisotropy

The fabric tensor quantifies the directionality and distribution of the fabric in granular materials (Oda, 1972; Oda et al., 1982). It can be represented in various forms (Oda, 1982; Kanatani, 1984), with the second-order tensor product being widely used. As shown in Eq. (4-11), the fabric tensor $\mathbf{\Phi}_{\mathbf{ij}}$ is the sum of tensor products of contact normal vectors divided by the number of contacts, where $n_{i}$ and $n_{j}$ denote contact normal vectors.

$\mathbf{\Phi}_{\mathbf{ij}} = \ \frac{1}{N_{c}}\Sigma\mathbf{n}_{\mathbf{i}}\mathbf{n}_{\mathbf{j}}$ (4-11)

The diagonal elements of $\mathbf{\Phi}_{\mathbf{ij}}$ are positive and sum to one. The fraction of the diagonal elements describes the concentration of contact normals, with higher value indicating a greater concentration in that direction. The off-diagonal elements represent the asymmetry of the distribution of contact normals. The fabric tensor is a crucial indicator for characterizing the state of granular materials, microscopically refining the critical state theory (Li and Dafalias, 2012).

$\mathbf{F}_{\mathbf{ij}} = \frac{15\left( \mathbf{\Phi}_{\mathbf{ij}} - \mathbf{\delta}_{\mathbf{ij}} \right)}{2}$ (4-12)

$F_{c} = \sqrt{\frac{3}{2}\mathbf{F}_{\mathbf{ij}}\mathbf{F}_{\mathbf{ij}}}$ (4-13)

Eq. (4-12) defines the anisotropic fabric tensor $\mathbf{F}_{\mathbf{ij}}$, which subtracts 1/3 from the diagonal elements of the fabric tensor and then multiplied by 15/2, where $\mathbf{\delta}_{\mathbf{ij}}$ represents the Kronecker delta. As the second invariant of $\mathbf{F}_{\mathbf{ij}}$, $F_{c}$ measures the magnitude of fabric anisotropy (Zhao and Guo, 2013), as shown in Eq. (4-13), where the Einstein summation convention is applied.

However, as noted in the coordination number analysis, specimens with $K_0$=0.5 and $K_0$=2.0 exhibit similar $Z_{m0}$ values yet markedly different liquefaction resistance. This suggests that the direction of fabric anisotropy—whether contacts are concentrated axially (compression) or horizontally (extension)—may play an important role. Since $F_c$ only captures the magnitude of anisotropy without indicating its direction, a signed indicator is needed to distinguish between compression and extension states. Following Otsubo et al. (2022), the fabric anisotropy indicator $\alpha$ (Yimsiri and Soga, 2010) is adopted, as shown in Eq. (4-14):

$\alpha = \frac{5\left( 3\varphi_{v} - 1 \right)}{5\varphi_{v} + 1}$ (4-14)

where $\varphi_{v}$ denotes the vertical principal component in fabric tensor $\mathbf{\Phi}_{\mathbf{ij}}$. A larger $\varphi_{v}$ indicates a concentration of contact normals in the axial direction. Positive $\alpha$ values correspond to axially-concentrated contacts (typical for $K_0 < 1.0$), while negative values correspond to horizontally-concentrated contacts (typical for $K_0 > 1.0$). This signed indicator allows for a more complete characterization of fabric evolution during cyclic shear.

![](thesis/assets/media/fabric_anisotropy.png)

Fig. 4.15. Evolution of fabric anisotropy indicator $\alpha$ during cyclic shear for different $K_{0}$ values (CSR=0.200)

Fig. 4.15 presents the evolution of fabric anisotropy indicator $\alpha$ during undrained cyclic shear. The inset shows the initial fabric anisotropy $\alpha_0$ for different $K_0$ states. The $K_0$=0.5 specimen exhibits positive $\alpha_0$ (approximately 0.07), indicating contact normals concentrated in the axial direction. The $K_0$=1.0 specimen shows $\alpha_0$ close to zero (approximately 0.02), reflecting a nearly isotropic fabric. The $K_0$=2.0 specimen exhibits negative $\alpha_0$ (approximately -0.05), indicating contact normals concentrated in the horizontal direction. During the early stages of cyclic loading ($N_c/N_L < 0.8$), $\alpha$ remains relatively stable for all three $K_0$ states. As the specimens approach liquefaction, $\alpha$ begins to fluctuate significantly and converge toward zero, indicating that the directional fabric anisotropy diminishes as the fabric structure degrades.

While the fabric anisotropy indicator $\alpha$ provides a scalar measure of directional bias, the morphological basis for the sign of $\alpha_0$ can be visualized through contact density distributions. To simultaneously capture changes in both direction and quantity of contact normals during cyclic shear, contact density is used for visualization. The contact density (Han et al., 2023) describes the average number of contacts per unit surface area for a particle with normalized radius, as shown in Eq. (4-15):

$\rho_{c}\left( \theta_{z},\ \phi_{cir} \right) = \frac{2N_{\theta_{z},\ \ \phi_{cir}}|n_{c} \in \left( \theta_{z},\theta_{z} + \Delta\theta_{z} \right) \cap (\phi_{cir},\ \phi_{cir} + \Delta\phi_{cir})}{N_{p}\int_{\phi_{cir}}^{\phi_{cir} + \Delta\phi_{cir}}{\sin\left( \phi_{cir} \right)d\phi_{cir}}\int_{\theta_{z}}^{\theta_{z} + \Delta\theta_{z}}{d\theta_{z}}}$ (4-15)

Here, $\rho_{c}$ represents the contact density, $\theta_{z}$ and $\phi_{cir}$ indicate the polar and azimuthal angles in the spherical polar coordinate system, respectively. $N_{\theta_{z},\ \ \phi_{cir}}$ indicates the number of contacts with normals within the specified angular range. $N_{p}$ and the subsequent integral denote the total number of particles and the corresponding surface area on the unit sphere, respectively. This method effectively evaluates contact orientation during undrained cyclic shear and accommodates granular systems with various particle numbers.

Fig. 4.16 presents the evolution of contact density during the liquefaction process for $K_0$=0.5 and $K_0$=2.0 specimens. At the initial state, the $K_0$=0.5 specimen exhibits an axially-extended distribution with higher density (orange/red) at the poles and lower density (green) around the equator, corresponding to the positive $\alpha_0$ value. In contrast, the $K_0$=2.0 specimen displays a dimpled sphere distribution with lower contact density at the poles and higher density around the equator, corresponding to the negative $\alpha_0$ value. These distinct morphologies arise from the stress-induced fabric rearrangement during anisotropic consolidation: contacts tend to align perpendicular to the maximum principal stress direction.

As cyclic shear progresses, the contact density distributions gradually evolve. During the intermediate stage, the overall contact density decreases notably while the morphological characteristics of the initial distribution are largely preserved. As the specimens approach liquefaction, the contact density further diminishes and the direction of maximum contact density varies following the rotating principal stress axis. In the post-liquefaction state, the distinct initial morphologies converge toward similar patterns—both specimens exhibit an inclined distribution aligned with the rotated principal stress direction, rather than the original axial or horizontal orientations. This convergence is consistent with the observed convergence of $\alpha$, $V_s$, and $Z_m$ as specimens approach liquefaction.

|           | $N/N_L$=0.00 | $N/N_L$≈0.61 | $N/N_L$≈1.05 | $N/N_L$≈1.07 |
| :-------: | :--------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: |
| $K_0$=0.5 | ![](thesis/assets/media/contact_density_k050_t0.jpg) | ![](thesis/assets/media/contact_density_k050_t302.jpg) | ![](thesis/assets/media/contact_density_k050_t523.jpg) | ![](thesis/assets/media/contact_density_k050_t529.jpg) |
| $K_0$=2.0 | ![](thesis/assets/media/contact_density_k200_t0.jpg) | ![](thesis/assets/media/contact_density_k200_t226.jpg) | ![](thesis/assets/media/contact_density_k200_t379.jpg) | ![](thesis/assets/media/contact_density_k200_t386.jpg) |

Fig. 4.16. Evolution of contact density distribution during the liquefaction process for $K_0$=0.5 ($N_L$=39.5) and $K_0$=2.0 ($N_L$=29.5) specimens (CSR=0.200)

#### Interparticle contact force and displacement

The initial distribution of contact forces for different $K_0$ states was presented in Fig. 4.3, where the contact forces align with the direction of the maximum principal stress: axially for $K_0$=0.5 and horizontally for $K_0$=2.0. Fig. 4.17 presents the evolution of contact force chains (left half, colored by force magnitude) and particle displacement fields (right half, colored by displacement magnitude) during the liquefaction process for both $K_0$ states.

At the initial state, the force chains exhibit distinct patterns corresponding to the initial stress anisotropy. For $K_0$=0.5, the contact forces are predominantly aligned in the axial direction, while for $K_0$=2.0, they are concentrated in the horizontal direction. As cyclic loading progresses, the number of interparticle contacts gradually decreases and the average contact force magnitude diminishes. The amplitude of particle displacement also increases with each loading cycle, reflecting the progressive degradation of the fabric structure.

As the specimens approach liquefaction, the force chains become increasingly sparse while the contact forces reorient to align with the rotated principal stress direction. In the post-liquefaction state, regardless of the initial $K_0$ value, the contact force distributions converge toward similar patterns—forces no longer align with the initial axial or horizontal directions but concentrate along the rotated principal stress axis. This convergence is consistent with the observed convergence of contact density, $\alpha$, $V_s$, and $Z_m$ as specimens approach liquefaction. From a microscopic viewpoint, liquefaction occurs because cyclic loading induces periodic reorganization of interparticle contacts, with the number of contacts progressively decreasing. This gradual loss of contacts reduces the ability of the particle skeleton to transfer external forces. Furthermore, the convergence of post-liquefaction contact density distributions toward similar patterns provides microscopic evidence supporting the uniqueness of the critical state stress ratio. It should be noted that the post-liquefaction state observed here does not constitute the critical state in a strict sense, as the critical state requires sustained large deformation at the void ratio and effective stress corresponding to the critical state line. Nevertheless, the observed convergence of fabric structure regardless of initial $K_0$ suggests that shear loading drives granular assemblies toward a common fabric configuration, which underlies the uniqueness of the critical state stress ratio.

|           | $N/N_L$=0.00 | $N/N_L$≈0.61 | $N/N_L$≈1.05 | $N/N_L$≈1.07 |
| :-------: | :--------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: |
| $K_0$=0.5 | ![](thesis/assets/media/force_disp_k050_t0.jpg) | ![](thesis/assets/media/force_disp_k050_t302.jpg) | ![](thesis/assets/media/force_disp_k050_t523.jpg) | ![](thesis/assets/media/force_disp_k050_t529.jpg) |
| $K_0$=2.0 | ![](thesis/assets/media/force_disp_k200_t0.jpg) | ![](thesis/assets/media/force_disp_k200_t226.jpg) | ![](thesis/assets/media/force_disp_k200_t379.jpg) | ![](thesis/assets/media/force_disp_k200_t386.jpg) |

Fig. 4.17. Evolution of contact force chains (left half) and particle displacement (right half) during the liquefaction process for $K_0$=0.5 ($N_L$=39.5) and $K_0$=2.0 ($N_L$=29.5) specimens (CSR=0.200)

#### Effect of fabric on liquefaction resistance

To disentangle the microscopic factors governing liquefaction resistance under different $K_0$ states, two sets of simulations are conducted at $D_r \approx 80\%$ and $D_r \approx 60\%$, each comprising five $K_0$ values (0.5, 0.67, 1.0, 1.5, 2.0) at CSR=0.300. The initial coordination number $Z_{m0}$ and fabric anisotropy indicator $\alpha_0$ are extracted for each of the ten specimens, and their relationships with the number of cycles to liquefaction $N_L$ are plotted in Fig. 4.18. Circular and square markers distinguish the two relative densities.

The most immediate observation from Fig. 4.18(a) is that $D_r \approx 80\%$ specimens consistently exhibit higher $N_L$ than $D_r \approx 60\%$ specimens across all five $K_0$ states. Correspondingly, $Z_{m0}$ is systematically higher for $D_r \approx 80\%$ specimens (4.89–4.98) than for $D_r \approx 60\%$ specimens (4.77–4.88). This is consistent with the well-established understanding that denser packings develop more inter-particle contacts and thus greater liquefaction resistance. The clear separation of the two density groups along the $Z_{m0}$ axis confirms that the initial coordination number is an important microscopic indicator reflecting the macroscopic influence of relative density on liquefaction resistance.

However, $Z_{m0}$ alone does not fully explain the observed trends. Within each density group, $Z_{m0}$ shows no monotonic correlation with $N_L$. For instance, among $D_r \approx 80\%$ specimens, $K_0$=0.5 exhibits the highest $N_L$ but not the highest $Z_{m0}$, while $K_0$=2.0 has a comparable $Z_{m0}$ to $K_0$=0.5 yet demonstrates considerably lower $N_L$. A similar pattern is observed for $D_r \approx 60\%$ specimens, where $K_0$=0.5 and $K_0$=2.0 share nearly identical $Z_{m0}$ values but differ markedly in $N_L$. This is consistent with the earlier observation from Fig. 4.14, where the inset plot of $Z_{m0}$ versus $N_L$ for the original three $K_0$ states already hinted that coordination number cannot fully account for the differences in liquefaction resistance caused by stress anisotropy. With five $K_0$ values and two relative densities, this insufficiency becomes even more evident.

The fabric anisotropy indicator $\alpha_0$ resolves this gap. As shown in Fig. 4.18(b), $\alpha_0$ exhibits a clear positive correlation with $N_L$ across both relative densities. Specimens consolidated under compression states ($K_0 < 1.0$) develop larger $\alpha_0$ values and demonstrate higher $N_L$, while those under extension states ($K_0 > 1.0$) develop smaller $\alpha_0$ values and generally exhibit lower $N_L$. A minor exception is observed for the $D_r \approx 60\%$ specimen at $K_0$=2.0, which shows a slightly higher $N_L$ than $K_0$=1.5; however, the difference is less than one loading cycle and falls within the range of statistical fluctuation inherent to DEM simulations. The overall trend remains clear: the two density groups follow a similar pattern along the $\alpha_0$ axis, indicating that the influence of fabric anisotropy on liquefaction resistance is consistent regardless of packing density.

The three-dimensional view of $Z_{m0}$–$\alpha_0$–$N_L$ (Fig. 4.19) synthesizes these observations. The ten data points form two distinct clusters separated primarily along the $Z_{m0}$ axis, while within each cluster $N_L$ varies systematically with $\alpha_0$. Both microscopic parameters contribute to liquefaction resistance, albeit along different dimensions: $Z_{m0}$ characterizes the overall contact density related to packing state, accounting for the inter-group separation between the two relative densities, whereas $\alpha_0$ captures the directional bias of the contact network induced by anisotropic consolidation, accounting for the intra-group variation among different $K_0$ states.

![](thesis/assets/media/fabric_liq_2d.png)

Fig. 4.18. Relationship between initial microscopic fabric parameters and liquefaction resistance $N_L$ for five $K_0$ states at two relative densities (CSR=0.300): (a) $Z_{m0}$ vs. $N_L$; (b) $\alpha_0$ vs. $N_L$. Labels indicate $K_0$ values.

![](thesis/assets/media/fabric_liq_3d.png)

Fig. 4.19. Combined effect of initial coordination number $Z_{m0}$ and fabric anisotropy indicator $\alpha_0$ on liquefaction resistance $N_L$ in three-dimensional space (CSR=0.300). Labels indicate $K_0$ values.

It should be noted, however, that $Z_{m0}$ and $\alpha_0$ do not fully determine liquefaction resistance. A cross-group comparison highlights the significant role of macroscopic relative density: the $D_r \approx 80\%$ specimen at $K_0$=2.0 ($Z_{m0}$=4.885, $\alpha_0$=-0.046) and the $D_r \approx 60\%$ specimen at $K_0$=1.0 ($Z_{m0}$=4.880, $\alpha_0$=+0.022) share nearly identical $Z_{m0}$ values, while the former exhibits a considerably more negative $\alpha_0$. If liquefaction resistance were solely determined by these two microscopic parameters, the $D_r \approx 80\%$/$K_0$=2.0 specimen should exhibit lower $N_L$. In reality, however, its $N_L$ (8.5) is nearly double that of the $D_r \approx 60\%$/$K_0$=1.0 specimen (4.5). This indicates that relative density influences liquefaction resistance through additional mechanisms beyond what $Z_{m0}$ and $\alpha_0$ can capture—such as particle interlocking, force chain stability, and the distribution of contact forces—that collectively render the denser packing more resistant to cyclic loading regardless of the directional fabric bias.

The physical mechanism underlying the $\alpha_0$ effect can be interpreted through the orientation of contact normals relative to the shear direction. For compression states ($K_0 < 1.0$), the axially-concentrated contact normal distribution (positive $\alpha_0$) means that a greater proportion of contacts are oriented perpendicular to the horizontally applied cyclic shear. This orientation is hypothesized to enhance the stability of individual contacts against shear-induced sliding and detachment, thereby maintaining more robust force chains and slowing fabric degradation during cyclic loading. This is supported by the observation that the $K_0$=0.5 specimen requires substantially more shear work than the $K_0$=1.0 and $K_0$=2.0 specimens to reach the same $r_u$ level (Fig. 4.12b), despite exhibiting comparable initial shear stiffness to the $K_0$=2.0 specimen (Fig. 4.13). Conversely, for extension states ($K_0 > 1.0$), the horizontally-concentrated contact normals (smaller $\alpha_0$) are more aligned with the shear direction, rendering the contacts more susceptible to sliding and the force chains more prone to collapse under cyclic loading, which accelerates fabric degradation and pore pressure accumulation.

It should be recognized, however, that granular soils are complex systems in which liquefaction resistance emerges from the interplay of both microscopic and macroscopic factors. As demonstrated by the cross-group comparison above, macroscopic relative density exerts a strong influence on liquefaction resistance that cannot be fully captured by $Z_{m0}$ and $\alpha_0$ alone. A comprehensive understanding of liquefaction resistance therefore requires integrating macroscopic characterization (relative density, stress state) with microscopic fabric analysis (coordination number, fabric anisotropy), rather than relying on either perspective in isolation.

## Summary

This study utilized the DEM with a combined servo mechanism to simulate undrained cyclic torsional shear tests in hollow cylinder apparatus (HCA), investigating the impact of initial stress anisotropy on the liquefaction resistance of sand soils. The DEM micro-parameters were calibrated and validated against undrained monotonic and cyclic HCA test data for dense Toyoura sand, reproducing the characteristic dilative response, strain-hardening behavior, and CSR-$N_L$ liquefaction resistance relationship. Specimens were prepared via an IC-AC stress path (isotropic consolidation to $p'$=10 kPa, then linear anisotropic consolidation to $p'$=100 kPa), which produced minimal void ratio variation ($\Delta e < 0.001$) between $K_0$ states, enabling isolation of fabric effects from packing density effects. Macroscopic responses including liquefaction resistance curves, cumulative shear work, and shear wave velocity were investigated for three representative $K_0$ values (0.5, 1.0, 2.0) across multiple CSR levels at $D_r \approx 80\%$. To further disentangle the microscopic factors, additional simulations at $K_0$=0.67 and 1.5, together with a second relative density ($D_r \approx 60\%$), were conducted at CSR=0.300. The findings are summarized as follows:

(1) The CSR-$N_L$ liquefaction resistance curves demonstrate a clear directional dependency on initial stress anisotropy: the compression state ($K_0$=0.5) exhibits the highest resistance, the isotropic state ($K_0$=1.0) intermediate resistance, and the extension state ($K_0$=2.0) the lowest resistance, for all CSR levels tested. Beyond the macroscopic observation of $K_0$-dependent liquefaction resistance, this study provides a microscopic perspective: the differences in liquefaction resistance among $K_0$ states are associated with distinct contact fabric structures induced by anisotropic consolidation.

(2) The normalized cumulative shear work $W_s$ evolves nearly identically for all three $K_0$ states when normalized by $N_L$, confirming the $K_0$-independence of the normalized energy accumulation pattern. However, the compression state ($K_0$=0.5) exhibits greater resistance to pore pressure buildup per unit energy input compared to the isotropic and extension states. Meanwhile, the isotropic state ($K_0$=1.0) maintains the highest shear wave velocity $V_s$ throughout cyclic shear, resulting in smaller strain amplitude per cycle and thus requiring more cycles than the extension state ($K_0$=2.0) despite comparable energy requirements. As specimens approach liquefaction, the $V_s$ values for all $K_0$ states converge, indicating that the influence of initial stress anisotropy on shear stiffness diminishes as the fabric structure progressively degrades.

(3) The initial mechanical coordination number $Z_{m0}$ is systematically higher for $D_r \approx 80\%$ specimens (4.89–4.98) than for $D_r \approx 60\%$ specimens (4.77–4.88), corresponding to their higher $N_L$ (8.5–11.0 vs. 4.0–5.5). This confirms that $Z_{m0}$ reflects the effect of packing compactness on liquefaction resistance. However, within each density group, $Z_{m0}$ shows no monotonic correlation with $N_L$—for example, specimens with $K_0$=0.5 and $K_0$=2.0 share comparable $Z_{m0}$ yet exhibit markedly different $N_L$—indicating that $Z_{m0}$ alone cannot account for the influence of stress anisotropy on liquefaction resistance.

(4) The initial fabric anisotropy indicator $\alpha_0$ resolves the gap left by $Z_{m0}$, exhibiting a clear positive correlation with liquefaction resistance across both relative densities. Specimens with higher $\alpha_0$ (axially-concentrated contacts in the compression state) generally exhibit greater liquefaction resistance than those with lower $\alpha_0$ (horizontally-concentrated contacts in the extension state). Contact density distributions provide morphological evidence for this correlation: the $K_0$=0.5 specimen exhibits an axially-extended distribution with higher density at the poles, while the $K_0$=2.0 specimen shows a dimpled sphere distribution with higher density around the equator. The axially-concentrated contact normals are oriented perpendicular to the horizontally applied cyclic shear, which is hypothesized to enhance the stability of individual contacts against shear-induced sliding, thereby maintaining more robust force chains and sustaining higher macroscopic resistance to pore pressure buildup. Conversely, in the extension state, the horizontally-concentrated distribution means that fewer contact normals are oriented perpendicular to the shear direction, reducing the number of contacts that can effectively resist shear-induced sliding and rendering force chains more prone to collapse.

(5) Both $Z_{m0}$ and $\alpha_0$ contribute to liquefaction resistance, albeit along different dimensions. In the three-dimensional space of $Z_{m0}$–$\alpha_0$–$N_L$, data from the two relative densities form two distinct clusters separated primarily along the $Z_{m0}$ axis, while within each cluster $N_L$ varies systematically with $\alpha_0$. However, a cross-group comparison reveals that specimens with nearly identical $Z_{m0}$ and less favorable $\alpha_0$ can still exhibit substantially higher $N_L$ when they possess higher relative density, indicating that macroscopic relative density influences liquefaction resistance through mechanisms beyond what $Z_{m0}$ and $\alpha_0$ alone can capture. A comprehensive assessment of liquefaction resistance therefore requires integrating both macroscopic and microscopic perspectives.

(6) Regardless of the initial $K_0$ state, the microscopic indicators—$Z_m$, $\alpha$, and contact density distribution—converge toward similar values as specimens approach and enter the post-liquefaction state. The contact force chains, initially aligned with the direction of the maximum principal stress corresponding to each $K_0$ state, reorient to align with the rotated principal stress axis in the post-liquefaction state. This convergence of fabric structure provides microscopic evidence supporting the uniqueness of the critical state stress ratio.
