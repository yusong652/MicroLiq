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

The stress paths for specimen preparation often entail linearly increasing $p'$ and $q$ to the state with target $K_{0}$ in both experimental (Vargas et al., 2020) and numerical (Yang and Taiebat, 2024) tests, thereby intriguing further investigation into the effects of stress paths by incorporating other consolidation stress paths. This study demonstrates DEM analysis of cyclic undrained HCA tests (Ma et al., 2024) and explores the effects of $K_{0}$ on liquefaction resistance. Specimens are prepared with two different stress paths in consolidation and subjected to an extensive range of cyclic shear stress ratios. By examining macroscopic and microscopic responses such as fabric evolution, this study aims to provide evidence that elucidates how stress anisotropy influences liquefaction resistance.

## DEM simulation setup

### Specimen preparation

Itasca PFC^3D^ (Itasca Consulting Group, Inc., 2021) was employed to implement DEM simulations of undrained cyclic torsional shear test. Unlike the periodic boundaries commonly used in element tests, the HCA in DEM simulation employs two cylinders, upper and lower planes, as well as six blades to provide torsional force, closely approximating the boundary conditions of HCA (Ishihara and Yasuda, 1975; Vargas et al., 2020; Li et al, 2014; Liu et al, 2021). As shown in Fig. 3.1(a), two rigid cylindrical walls with inner diameter of 6 cm and outer diameter of 10 cm are positioned coaxially and vertically, with the upper and lower planes placed 10 cm apart, resembling the geometric dimensions of laboratory tests (Vargas et al., 2020).

![](thesis/assets/media/image65.jpg)

(a) Pouring method for generating particles

![](thesis/assets/media/image66.jpg)

(b) Insertion of torsional blades

Fig. 3.1. Specimen generation process in the initial stage using the pouring method and insertion of torsional blades

This research employed a uniform particle size distribution ranging from 1.5 mm to 3.0 mm, and utilizes a rolling resistance contact model (Iwashita and Oda, 1998; Wensrich and Katterfeld, 2012) to mimic the non-spherical effects of sand particles. The specific parameters of the contact model are listed in Table 3-1. To ensure similarity with laboratory methods, the particles were initially generated in the upper part of the apparatus and then allowed to flow downward under the influence of gravity, forming the specimen as shown in Fig. 3.1(a). The stress calculations of HCA are summarized according to the formulas provided in Table 3-2 ,where the values of $\sigma_{z}$ and $\sigma_{\theta}$ are derived from the equilibrium relations, $\varepsilon_{z}$ and $\gamma_{z\theta}$ are based on strain compatibility, and the remaining stress and strain expressions align with the assumption of linear elasticity (Hight et al., 1983).

Table 3-1. Parameters in DEM simulation

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

To achieve the target stress levels for anisotropic consolidation, a servo mechanism (Itasca Consulting Group, 2021; Ma et al., 2024) is employed to manipulate the position of vertices of wall elements throughout the consolidation process. Fig. 3.2 shows the stress and void ratio evolution during the anisotropic consolidation process for three representative $K_{0}$ values.

![](thesis/assets/images/fig3_2a_aniso_stress.png)

(a) Mean effective stress $p'$ vs. deviator stress $q$

![](thesis/assets/images/fig3_2b_stress_void.png)

(b) Mean effective stress $p'$ vs. void ratio $e$

Fig. 3.2. Stress and void ratio evolution in anisotropic consolidation for specimens with three representative stress anisotropies ($K_{0}$=0.5, 1.0, 2.0) from isotropic consolidation state with $p'$=10.0kPa to target mean effective stress $p'$=100.0kPa

The specimen was initially compressed to a target void ratio of approximately 0.736 under a friction coefficient of 0.0. Subsequently, the friction coefficient was reset to 0.5, followed by anisotropic consolidation from a state with $p'$=10.0kPa and $K_{0}$=1.0 to $p'$=100.0kPa and the target $K_{0}$ (IC-AC protocol). Notably, during the AC process with an increasing $p'$, $K_{0}$ evolves from 1.0 to the corresponding target $K_{0}$. Three representative cases with $K_{0}$ values of 0.5, 1.0, and 2.0 are examined, representing compression ($K_{0}$<1.0), isotropic ($K_{0}$=1.0), and extension ($K_{0}$>1.0) states, respectively. During the AC process, both $p'$ and $q$ increase simultaneously, with the stress path depending on the target $K_{0}$ value, as illustrated in Fig. 3.2(a) and Fig. 3.2(b).

As indicated by Fig. 3.2(b), the void ratio decreases from approximately 0.736 at the initial state ($p'$=10 kPa) to around 0.732 at the target stress ($p'$=100 kPa) during anisotropic consolidation. The differences in final void ratio $e$ between different $K_{0}$ states after IC-AC are minimal, with $e$ ranging from 0.7315 to 0.7325. This small variation (approximately 0.001) makes it reasonable to emphasize the effects of microscopic quantities, such as coordination number and fabric anisotropy, rather than $e$, on liquefaction resistance.

![](thesis/assets/media/image67_k05.jpg)

(a) $K_{0}$=0.5

![](thesis/assets/media/image67_k10.jpg)

(b) $K_{0}$=1.0

![](thesis/assets/media/image67_k20.jpg)

(c) $K_{0}$=2.0

Fig 3.3. Visualization of hollow cylindrical specimens after anisotropic consolidation to $p'$=100 kPa with different $K_{0}$ values. Cross-sectional view shows particles (colored by radius) and contact forces (red vectors), corresponding to the final states in Fig. 3.2.

### Implementation of undrained condition

In DEM simulations of undrained tests, the interaction between water and particles is disregarded, employing a constant volume approach to replicate the undrained condition. The effectiveness of this constant volume approach has been validated in numerous DEM simulations (Sitharam et al., 2002; Yimsiri and Soga, 2010). To simultaneously achieve the stress boundary conditions and undrained condition observed in laboratory HCA tests, an innovative combined servo mechanism is proposed.

The key challenge in simulating undrained HCA tests lies in satisfying multiple conditions simultaneously. In laboratory tests, the inner and outer chamber pressures ($p_i$ and $p_o$) are maintained equal and constant, the additional axial pressure ($p_z$) or height ($H$) is controlled, and a target shear stress ($\tau_{z\theta,tar}$) is applied. Meanwhile, the undrained condition requires constant volume. This study addresses these challenges through a combined servo mechanism by controlling four variables: inner radius rate ($dr/dt$), outer radius rate ($dR/dt$), height rate ($dH/dt$), and additional axial pressure ($p_z$), to satisfy four condition equations simultaneously.

**Condition 1: Equal inner and outer chamber pressures**

To address the inhomogeneity in radial direction caused by the axial symmetry of HCA, the difference in effective stresses between the outer and inner cylinders is regulated by controlling the diameter variation. The inner radius rate is determined by Eq. (3-1), where $\sigma_{dif,r}'$ represents the effective stress difference between outer and inner cylinders, and $S_{cr}$ is the servo coefficient.

$$\frac{dr}{dt} = \frac{\left(\sigma_{dif,r}' - (p_o - p_i)\right)}{\Delta t}S_{cr}$$ (3-1)

**Condition 2: Constant additional axial pressure or constant height**

During undrained cyclic shear, the height can be controlled either as constant (dH/dt = 0) or through additional axial pressure regulation. The height rate is governed by Eq. (3-2), where $\sigma_{dif,z}'$ denotes the effective stress difference between axial and radial stress, and $S_{cz}$ is the corresponding servo coefficient.

$$\frac{dH}{dt} = \frac{\left(\sigma_{dif,z}' - p_z\right)}{\Delta t}S_{cz} \qquad \frac{dH}{dt} = 0\ \text{if constant}\ H$$ (3-2)

**Condition 3: Target shear stress**

The rotation angle rate is controlled to achieve the target shear stress through Eq. (3-3), where $T_{dif}$ represents the torque difference between target and current value, and $S_{cs}$ is the servo coefficient.

$$\frac{d\theta}{dt} = \frac{T_{dif}}{\Delta t}S_{cs}$$ (3-3)

**Condition 4: Undrained condition (constant volume)**

The undrained condition is ensured by maintaining constant volume throughout the cyclic shear test, as expressed in Eq. (3-4).

$$2\pi H\left(R\frac{dR}{dt} + r\frac{dr}{dt}\right) + \pi(R^2 - r^2)\frac{dH}{dt} = 0$$ (3-4)

By combining these four equations, the system of four variables ($dr/dt$, $dR/dt$, $dH/dt$, $p_z$) and four constraints is solved simultaneously at each timestep, achieving both the stress conditions and undrained condition in DEM simulation of HCA tests. This combined servo mechanism (Ma et al., 2024) elegantly replicates the boundary conditions observed in laboratory undrained cyclic torsional shear tests.

**Determination of servo coefficients**

The servo coefficients ($S_{cr}$, $S_{cz}$, $S_{cs}$) in the combined servo mechanism are determined based on the contact stiffness between boundaries and particles. For the torsional servo coefficient $S_{cs}$ in Condition 3, the moment of inertia of shear stiffness $I_{rot}$ is calculated considering the distance from the center of rotation. Fig. 3.4 illustrates the contact between a particle and a blade, where $r_{d}$ denotes the distance from the center of rotation to the contact point, and $\theta$ is the angle between the contact normal and the horizontal plane.

![](thesis/assets/media/image73.png)

Fig. 3.4. Determination of moment of inertia of shear stiffness in servo mechanism for torque application

The moment of inertia $I_{rot}$ is calculated by Eq. (3-5), where $k_{n}$ represents the normal contact stiffness. The contribution of each contact is adjusted by $\cos^{2}\theta$ because a larger $\theta$ reduces its contribution to the shear stiffness. The servo coefficient $S_{cs}$ for torsional control is then determined by Eq. (3-6).

$$I_{rot} = \Sigma r_{d}^{2}k_{n}\cos^{2}\theta$$ (3-5)

$$S_{cs} = \frac{1}{I_{rot}}$$ (3-6)

Similarly, the servo coefficients $S_{cr}$ and $S_{cz}$ for radial and axial directions are determined based on the equivalent stiffness of inner/outer cylinders and top/bottom plates, respectively. This stiffness-based approach ensures stable and efficient convergence of the combined servo mechanism.

**Excess pore water pressure calculation**

The effective stresses are evaluated by measuring the contact stresses between the boundary and particle skeleton. The assumptions of undrained condition and full saturation result in variations in effective stress on lateral cylinders and excess pore water pressure (EPWP) that are equal in magnitude but opposite in sign, as quantified in Eq. (3-7). Here, $u$ represents the EPWP, $\sigma_{r}'$ denotes the radial effective stress derived from the inner and outer effective stresses, and $\sigma_{r0}'$ is its initial value (Yimsiri and Soga, 2010).

$$u = \sigma_{r0}' - \sigma_{r}'$$ (3-7)

### Parameter validation

To validate the micro-parameters and numerical implementation, simulations were compared with experimental data from hollow cylinder apparatus tests on dense Toyoura sand under both monotonic and cyclic loading conditions. This validation demonstrates the model's capability to reproduce undrained behavior before investigating the effects of consolidation stress ratio ($K_{0}$) on liquefaction resistance.

#### Monotonic shear validation

Undrained monotonic shear simulations were compared with HCA tests reported by Nakata et al. (1998). The specimen was isotropically consolidated to $p'_{0}$=100 kPa ($K_{0}$=1.0) before applying monotonic torsional shear under constant height condition. The micro-parameters listed in Table 3-1 were employed.

![](thesis/assets/images/validate_p_q_dense.png)

(a) Effective stress path

![](thesis/assets/images/validate_gamma_q_dense.png)

(b) Stress-strain relationship

Fig. 3.5. Validation of DEM simulation against monotonic undrained shear tests (Nakata et al., 1998): dense Toyoura sand with Dr≈80%, $p'_{0}$=100 kPa, $K_{0}$=1.0

The DEM simulation successfully captures the characteristic undrained behavior of dense sand: (1) strain-softening in effective stress space, with the stress path approaching the phase transformation line as mean effective stress $p'$ decreases from the initial state; (2) stress-strain hardening typical of dense specimens, where deviatoric stress $q$ increases monotonically with deviatoric strain $\varepsilon_{q}$. The close agreement between simulation and experimental results validates both the micro-parameters and the combined servo mechanism described in Section 3.2.2.

#### Cyclic shear validation

Liquefaction resistance under cyclic loading was validated against the classical data of Ishihara et al. (1985). Specimens were isotropically consolidated to $p'_{0}$=100 kPa ($K_{0}$=1.0) and then subjected to sinusoidal torsional shear with 8 Hz frequency. Liquefaction was defined as the condition when single-amplitude shear strain reached $\gamma$=2.0%.

![](thesis/assets/images/validate_N_csr.png)

Fig. 3.6. Cyclic stress ratio (CSR) versus number of cycles to liquefaction: validation against Ishihara et al. (1985) for dense Toyoura sand

Five CSR levels (0.20, 0.25, 0.30, 0.35, 0.40) were simulated. The DEM results align well with experimental trends across the full range of cyclic stress ratios, demonstrating the model's capability to reproduce the characteristic CSR-N liquefaction resistance curve. Both monotonic and cyclic validations confirm that the DEM model can accurately reproduce undrained behavior of dense Toyoura sand under different loading modes.

Having validated the model against isotropic consolidation conditions ($K_{0}$=1.0), the following sections investigate how different consolidation stress ratios affect liquefaction resistance. Specimens with three representative $K_{0}$ values (0.5, 1.0, 2.0) obtained from the IC-AC protocol underwent undrained cyclic torsional shear until liquefaction occurred. The cyclic shear stress is applied as a sinusoidal wave with different cyclic stress ratios (CSR). The factors influencing liquefaction resistance are discussed from both macroscopic and microscopic perspectives.

## Results and discussion

### Macroscopic response

#### Stress strain relationship

Fig. 3.7, 3.8, 3.9, and 3.10 present typical stress and strain evolution during undrained cyclic shear for specimens with different initial $K_{0}$ values at CSR=0.200. Liquefaction is defined as occurring when EPWP ratio $r_{u}$ reaches 95% of initial radial effective stress $\sigma_{r0}'$.

![](thesis/assets/images/stress_rel.png)

Fig. 3.7. Shear stress $\tau_{z\theta}$ vs. mean effective stress $p'$ ($K_{0}$=1.0, CSR=0.200)

As the shear stress $\tau_{z\theta}$ cyclically acts on the hollow cylindrical specimen, the mean effective stress $p'$ exhibits an overall decrease. Once $p'$ falls below approximately 60 kPa, an increase in the magnitude of $\tau_{z\theta}$ drives an upward trend in $p'$, displaying a butterfly-shaped relationship. After liquefaction onset, $p'$ and $\tau_{z\theta}$ delineate the critical state line and converge at the origin periodically.

![](thesis/assets/images/stress_strain.png)

Fig. 3.8. Shear stress $\tau_{z\theta}$ vs. shear strain $\gamma_{z\theta}$ ($K_{0}$=1.0, CSR=0.200)

The stress-strain relationship shows stiff shear modulus with slight reduction in the initial stage. As cyclic loading progresses towards liquefaction, shear stiffness markedly decreases, plastic deformation occurs, and strong nonlinearity becomes evident in the hysteretic loops.

![](thesis/assets/images/stress_dev.png)

Fig. 3.9. Deviatoric stress $\sigma_{vM}$ vs. mean effective stress $p'$ for three $K_{0}$ values (CSR=0.200)

To compare the effects of initial stress anisotropy, the deviatoric von-Mises stress $\sigma_{vM}$ evolution is shown for three $K_{0}$ values. The $K_{0}$=1.0 specimen starts with $\sigma_{vM}$ at zero due to isotropic consolidation, while $K_{0}$=0.5 and $K_{0}$=2.0 specimens exhibit initial deviatoric stress due to anisotropic consolidation. As cyclic shear progresses, specimens with different $K_{0}$ values follow distinct stress paths toward the critical state line, with varying rates of stress degradation and liquefaction resistance.

![](thesis/assets/images/stress_u_compare.png)

Fig. 3.10. Excess pore water pressure ratio $r_{u}$ evolution for three $K_{0}$ values (CSR=0.200)

The EPWP responses differ significantly among the three $K_{0}$ states. The $K_{0}$=2.0 specimen shows the most rapid $r_{u}$ accumulation, reaching liquefaction after approximately 29 cycles. The $K_{0}$=1.0 specimen exhibits intermediate behavior with liquefaction occurring after 31 cycles. In contrast, the $K_{0}$=0.5 specimen demonstrates the highest liquefaction resistance, reaching the liquefaction criterion after 39 cycles. These observations provide clear evidence that initial stress anisotropy significantly influences liquefaction resistance.

#### Liquefaction resistance curves

To systematically investigate how liquefaction resistance varies with CSR and $K_{0}$, Fig. 3.11(a) and Fig. 3.11(b) compare the number of cycles required to reach liquefaction under varying conditions.

![](thesis/assets/images/liq_res_cur.png)

(a) Cyclic liquefaction resistance with various CSR

![](thesis/assets/media/image82.png)

(b) Number of cyclic loadings $N_{L}$ vs. $K_{0}$ under cyclic shear loading with cyclic shear stress ratio of 0.250

Fig. 3.11. Cyclic liquefaction resistance of specimens subjected to different initial stress anisotropies and cyclic shear stress ratios

Fig. 3.11(a) demonstrates liquefaction resistance for specimens prepared with IC-AC protocol. Under different CSR conditions, the number of cycles to liquefaction decreases with decreasing $K_{0}$ when $K_{0} < 1.0$, and decreases with increasing $K_{0}$ when $K_{0} > 1.0$. Hence, greater stress anisotropy results in fewer cycles needed to trigger liquefaction, indicating lower resistance. This observation is consistent with the findings by Georgiannou and Konstadinou (2014) regarding the loose state, but it diverges from the results reported by other experimental studies (Ishihara and Takatsu, 1979; Yamashita and Toki, 1993; Vargas et al., 2020).

The influence of stress paths on liquefaction resistance is also noteworthy. Fig. 3.11(b) analyses the variation in the number of cycles required for triggering liquefaction under CSR=0.25, including specimens prepared with both protocols. Observations reveal that the protocols for preparing specimens, whether following the IC-AC or IC-AC-TS protocol, does not significantly affect the liquefaction resistance for the same $K_{0}$. Yet, other forms of protocols for preparation may have an impact on liquefaction resistance and remains to be investigated, but this falls outside the scope of this study and should be noted.

#### Cumulative shear work

Cumulative shear work refers to the energy input during undrained cyclic shear in this study. It is valuable to examine the correlation between the liquefaction resistance of soils and their susceptibility to the input energy. Towhata and Ishihara (1985) conducted a series of experiments where specimens were subjected to undrained cyclic shear under various loading conditions. They revealed a unique relationship between excess pore water pressure and shear work, despite differences in stress anisotropy. Figueroa et al. (1994) similarly confirmed that the shear work required for triggering liquefaction is independent of the amplitude of strain through strain-controlled tests. Georgiannou and Konstadinou (2014) concluded from the comparison between IC and AC specimens that the energy associated with terminal water pressure is positively correlated with relative density. For equivalent relative densities, AC specimens require greater energy than IC specimens to induce liquefaction.

![](thesis/assets/media/image83.png)

(a) $W_{s}$ vs. $N_{c}/N_{L}$ (dense)

![](thesis/assets/media/image84.png)

(b) $r_{u}$ vs. $W_{s}$ (dense)

Fig. 3.12. Evolution of cumulative unit volume shear work and shear work required to trigger liquefaction for different $K_{0}$

The cumulative unit volume shear work $W_{s}$ is defined as shown in Eq. (3-8), expressed as an integral of shear strain rate $\dot{\gamma_{z\theta}}$, shear stress $\tau_{z\theta}$, and incremental time $dt$. This represents the accumulated input energy per unit volume in the specimen.

$W_{s} = \int_{0}^{t}{\dot{\gamma_{z\theta}}\tau_{z\theta}dt}$ (3-8)

As indicated by Fig. 3.12(a), in the liquefaction process normalized by $N_{L}$, it is difficult to distinguish the differences between the cases with different $K_{0}$ values. Fig. 3.12(b) explores the impact of different $K_{0}$ on the liquefaction by relating $W_{s}$ and $r_{u}$. For the initial stages, particularly when $r_{u}$ is less than 0.2, a larger $K_{0}$ contributes to a higher $r_{u}$ for the same amount of work $W_{s}$​. $r_{u}$ decreases as shear force performs positive work and increases as shear force performs negative work. The shear work required to achieve liquefaction $W_{sL}$ for different $K_{0}$ values range from 0.07 to 0.13, with a trend of increasing $W_{sL}$​ as stress anisotropy increases. This implies that although the IC state with $K_{0}$=1.0 specimen requires more cyclic numbers to reach liquefaction, its higher initial shear stiffness results in lower strain velocity, hence requiring the least shear work.

#### Initial shear wave velocity

The response in cumulative shear work inspired an exploration in relationship between initial stiffness and liquefaction resistance (Xu et al., 2015). The shear modulus is the derivative of shear stress $\tau$ with respect to shear strain $\gamma$ and Eq. (3-9) describes the initial shear wave velocity $V_{s0}$ in terms of the initial shear modulus $G_{0}$ and the saturated density $\rho_{sat}$ (Tokimatsu and Uchida, 1990; Chen et al., 2005).

$V_{s0} = \sqrt{\frac{G_{0}}{\rho_{sat}}}$ (3-9)

![](thesis/assets/media/image85.png)

Fig. 3.14. Relationship between cyclic number and initial shear wave velocity (CSR=0.250)

As shown in Fig. 3.14, for $K_{0}$=1.0 state, $V_{s0}$ reaches its highest value, nearly 450m/s. Regardless of whether $K_{0}$ is less than 1.0 or greater than 1.0, $V_{s0}$ decreases with increasing stress anisotropy, corresponding to the trend of evolution in liquefaction resistance. At $K_{0}$=0.33 and $K_{0}$=3.33, $V_{s0}$ drops to its lowest level, approximately 340m/s. This behavior provides a macroscopic guideline for assessing liquefaction strength: a higher $V_{s0}$ indicates greater liquefaction resistance. Additionally, the cases for $K_{0}$\<1.0 and $K_{0}$\>1.0 diverge: for the same $V_{s0}$, $K_{0}$\<1.0 exhibits higher liquefaction resistance compared to $K_{0}$\>1.0. For example, $K_{0}$=0.40 with $V_{s0}$ at 384m/s achieves $N_{L}$ close to 42, while $K_{0}$=2.50 with $V_{s0}$ around 400m/s has $N_{L}$ only at 37. Yet, these macroscopic findings remain difficult to elucidate the difference in liquefaction resistance under different initial stress conditions. This emphasizes the necessity for a more detailed discussion at the microscale to comprehend the factors influencing liquefaction resistance.

### Microscopic interpretation

#### Evolution of coordination number

The coordination number indicates the number of contacts each individual particle has. Its average value for all particles isotropically evaluates the compactness of fabric in granular materials (Oda, 1977; Shire and O'Sullivan, 2012; Fei and Narsilio, 2020). Particles with fewer than two contacts are generally unable to stably transmit interparticle forces and do not effectively contribute to the soil skeletons. These particles are classified as floaters and are excluded from the calculation of the coordination number (Thornton, 2000; Hu et al., 2023). As shown in Eq. (3-10),

$Z_{m} = \frac{2N_{c} - N_{1}}{N_{p} - N_{1} - N_{0}}$ (3-10)

$Z_{m}$ represents the mechanical coordination number. $N_{c}$ is the number of interparticle contacts, and $N_{p}$ is the total number of particles. $N_{1}$ and $N_{0}$ indicate the number of particles with one and zero contacts, respectively, to eliminate the influence of floaters.

Figure 3.13 shows the evolution of $Z_{m}$ under different initial $K_{0}$ states during the cyclic shear. The results indicate that the influence of initial stress states on the coordination number is significant, with greater stress anisotropy corresponding to lower coordination numbers both at the initial state and during the cyclic shear process. As cyclic loading was applied to the undrained specimen, $Z_{m}$ exhibited oscillatory behavior while progressively decreasing as shown in Fig. 3.13. The decline in $Z_{m}$ indicates a reduction in interparticle contacts and a loss of fabric integrity and robustness. Liquefaction was observed to occur when $Z_{m}$ fell to approximately 3.5, signifying a critical threshold where the specimen became susceptible to cyclic shear

![](thesis/assets/media/image86.png)

Fig. 3.15. Mechanical coordination number evolution in cyclic shear and relationship between cyclic number required for liquefaction and initial mechanical coordination number (CSR=0.250)

stresses. Regardless of the initial $K_{0}$, the post-liquefaction $Z_{m}$ repeatedly cycles between approximately 3.5 and lower values. This implies that the initial stress anisotropies have minimal impact on the post-liquefaction fabric.

#### Evolution of fabric anisotropy

The fabric tensor quantifies the directionality and distribution of the fabric in granular materials (Oda, 1972; Oda et al., 1982). It can be represented in various forms (Oda, 1982; Kanatani, 1984), with the second-order tensor product being widely used. As shown in Eq. (3-9), the fabric tensor $\mathbf{\Phi}_{\mathbf{ij}}$ is the sum of tensor products of contact normal vectors divided by the number of contacts, where $n_{i}$ and $n_{j}$ denote contact normal vectors and i, j refer to circumferential, radial or axial direction.

$\mathbf{\Phi}_{\mathbf{ij}} = \ \frac{1}{N_{c}}\Sigma\mathbf{n}_{\mathbf{i}}\mathbf{n}_{\mathbf{j}}$ (3-9)

The diagonal elements of $\mathbf{\Phi}_{\mathbf{ij}}$ are positive and sum to one. The fraction of the diagonal elements describes the concentration of contact normals, with higher value indicating a greter concentration in that direction. The off-diagonal elements represent the asymmetry of the distribution of contact normals. The fabric tensor is a crucial indicator for characterizing the state of granular materials, microscopically refining the critical state theory (Li and Dafalias, 2012).

![](thesis/assets/media/image87.png)

Fig. 3.16. Transformation of contact normal from global x-y-z orthogonal coordinate to circumferential-radial-axial local cylindrical coordinates

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

![](thesis/assets/media/image88.png)

Fig. 3.17. Evolution of second invariant of mechanical anisotropic fabric tensor $F_{c}$ for specimens subjected to different initial stress anisotropies

anisotropy. Compared to $Z_{m0}$\'s sensitivity to $K_{0}$, $F_{c0}$ exhibits diminished responsiveness to changes in $K_{0}$ between 0.5 and 2.5. However, as stress anisotropy increases beyond these thresholds, greater fabric anisotropy was observed, as indicated in Fig. 3.17. Additionally, with higher stress anisotropy, $F_{c}$ underwent more pronounced fluctuations. For the same level of initial fabric anisotropy $F_{c0}$, states with $K_{0}$\>1.0 fluctuate more significantly compared to states with $K_{0}$\<1.0. This difference in fabric anisotropy potentially influences the macroscopic behavior of liquefaction resistance.

#### Effect of fabric on liquefaction resistance

For differentiating the states with $K_{0}$\<1.0 or $K_{0}$\>1.0, Otsubo et al. (2022) recommended to adopt a signed fabric anisotropy indicator $\alpha$ (Yimsiri and Soga, 2010) to evaluate fabric anisotropy as shown in Eq. (3-13):

$\alpha_{0} = \frac{5\left( 3\varphi_{v0} - 1 \right)}{5\varphi_{v0} + 1}$ (3-13)

, where $\varphi_{v0}$ denotes the initial vertical principal component in fabric tensor $\mathbf{\Phi}_{\mathbf{ij}}$. A larger $\varphi_{v0}$ means a concentration of contact normal converging in the axial direction after specimen preparation. The impact of fabric on liquefaction resistance is investigated through a space of $\alpha_{0}$, $Z_{m0}$, and $N_{L}$ (Yang and Taiebat, 2024) for various $K_{0}$, as shown in Fig. 3.18(a) and (b). Specimens prepared using the IC-AC and IC-AC-TS protocols exhibit similar $Z_{m0}$ and $\alpha_{0}$, indicating that the two stress paths do not significantly affect the microscopic fabric, thereby explaining the similar $N_{L}$for different preparation protocols. For $K_{0}$=1.0, $Z_{m0}$ and liquefaction strength exhibit the highest levels. As stress anisotropy increases, AC states with $K_{0}$\<1.0 and $K_{0}$\>1.0 diverge along different routes.

To investigate the influence of $Z_{m0}$ and $\alpha_{0}$ on liquefaction resistance, an exponential function that linearly relates $Z_{m0}$ and $\alpha_{0}$ to $N_{L}$ (Yang and Huang, 2023; Yang and Taiebat, 2024), was introduced to fit their relationship, as shown in Eq. (3-14).

$N_{L} = \exp\left( {\zeta Z}_{m0} + \eta\alpha_{0}\  + \chi \right)$ (3-14)

The fitted surface equation produced positive $\zeta$=3.63 and $\eta$=0.19, suggesting that an increasing $Z_{m0}$ or $\alpha_{0}$ enhances liquefaction resistance, which contrasts with the literatures, where an increasing $\alpha_{0}$ reduces liquefaction resistance. The $K_{0}$ conditions of the specimens in this study vary considerably compared to the literature and could explain the distinct conclusions. For instance, unlike a comparison between two stress ratios of $K_{0}$=1.0 and $K_{0}$=0.5 (Yang and Taiebat, 2024), this study evaluates liquefaction resistance between and beyond the thresholds, with $K_{0}$ ranging from 0.33 to 3.33, under different relative densities. When comparing the IC state of $K_{0}$=1.0 with AC states of $K_{0}$≠1.0, as shown in Fig. 3.18(b), it is evident that for both dense and loose states, the $N_{L}$ for $K_{0}$=1.0 lies above the fitted lines for $K_{0}$\<1.0 or $K_{0}$\>1.0, indicating a stronger liquefaction resistance for $K_{0}$=1.0 state at the same $Z_{m0}$. This tendency aligns well with the conclusions found in the literatures. However, introducing multiple values of $\alpha_{0}$ emphasized the comparison between the AC states of $K_{0}$\<1.0 and $K_{0}$\>1.0, thus yielding a positive value of $\eta$ when fitting the relationship. On the other hand, through a comparison of different relative densities as shown in Fig. 3.18 (b), the fitted line for dense state is positioned above that of the loose state, indicating that not only the microscopic factors like $Z_{m0}$ and $\alpha_{0}$, but also a smaller void ratio, which evaluates the macroscopic compactness, strengthens liquefaction resistance.

![](thesis/assets/media/image89.png)

(a) Coupled effect of $Z_{m0}$ and $\alpha_{0}$ on liquefaction resistance

![](thesis/assets/media/image90.png)

(b) Effect of $Z_{m0}$ on liquefaction resistance

Fig. 3.18. Effect of initial coordination number $Z_{m0}$ and initial fabric anisotropy $\alpha_{0}$ on liquefaction resistance for specimens with different initial stress anisotropies (CSR=0.250)

While liquefaction resistance decreases with increasing initial stress anisotropy for both dense and loose states, primarily due to variation in $Z_{m0}$, subtle differences in liquefaction response are observed for states with $K_{0}$\<1.0 and $K_{0}$\>1.0. For instance, as shown in Fig. 3.18(b), which decouples $\alpha_{0}$ from Fig. 3.18(a), illustrates that when comparing $K_{0}$=0.4 and $K_{0}$=2.5 in the dense state, both share a similar $Z_{m0}$ value around 4.43. However, the $N_{L}$ is over 10% higher for $K_{0}$ = 0.4 compared to $K_{0}$ = 2.5. Additionally, for $K_{0}$=0.33 and $K_{0}$=3.0 in the dense state, although their $N_{L}$ values are similar, the $Z_{m0}$ for $K_{0}$=0.33 is at least 0.05 lower than that for $K_{0}$=3.0. This suggests that a smaller $Z_{m0}$ is sufficient to achieve the same level of liquefaction resistance for $K_{0}$=0.33 as for $K_{0}$=3.0. These differences contribute to the positive value of $\eta$ in Eq. (3-14). On the other hand, for the loose states, this difference between $K_{0}$\<1.0 and $K_{0}$\>1.0 is limited, where the fitted lines for $K_{0}$\<1.0 and $K_{0}$\>1.0 almost overlap. However, for comparison between $K_{0}$=0.33 and $K_{0}$=3.33, or comparison between $K_{0}$=0.40 and $K_{0}$=2.50, stronger liquefaction tendency was also observed, where smaller $Z_{m0}$ enables similar liquefaction resistance for $K_{0}$\<1.0 compared to $K_{0}$\>1.0. The overlapping of fitted lines are mainly attributed to a sightly high value for $K_{0}$=3.00 in loose state.

$K_{0} < 1.0$ and $K_{0} > 1.0$ states correspond to different intermediate principal stress $b$, as described in Eq. (2-15). Experimental results by Tastan and Carraro (2022) indicate that liquefaction resistance increases as $b$ increases from 0.0 to 0.8.

$b = \frac{{\sigma_{2}' - \sigma}_{3}'}{\sigma_{1}' - \sigma_{3}'}$ (3-15)

This observation contrasts this study, where $b = 0.0$ shows larger liquefaction resistance. The discussion in this study is focusing on comparing the influence of $b$ only at the extremes of 0.0 and 1.0. Yet, investigating how the liquefaction responses change with in-between values, and providing a microscopic explanation would also attract interest and warrants further study, but it lies beyond the scope of this study.

#### Interparticle contact force

To interpret the interparticle relationships, contact forces and individual particle movement in the initial state with $K_{0}$=0.33, post-liquefaction state with $K_{0}$=0.33, initial state with $K_{0}$=3.00, and post-liquefaction state with $K_{0}$=3.00 are depicted in Fig. 3.19(a), Fig. 3.19(b), Fig. 3.19(c), and Fig. 3.19(d). The specimens with $K_{0}$=0.33 and $K_{0}$=3.00 exhibit significant differences in the distribution of contact forces at the initial stages in cyclic shear. For $K_{0}$=0.33, the contact forces converge in the axial direction, whereas for $K_{0}$=3.00, the contact forces tend to be distributed horizontally, aligning with the direction of the maximum principal stress in both cases. As cyclic loading progresses, the number of interparticle force gradually decreases, and the magnitude of these forces diminishes, until liquefaction and large deformation occurs. From a macroscopic perspective, the liquefaction process involves a decline in stiffness and an increase in nonlinearity, as discussed in the macroscopic behavior section. From a microscopic viewpoint, liquefaction occurs because the particle-constituting skeleton becomes increasingly unable to sustain itself through particle interaction, such as the relative movement, hindering the transfer of external forces. In contrast to the influence of $K_{0}$ on contact forces in initial state, the effect of different initial $K_{0}$ values on the

![](thesis/assets/media/image91.jpeg)

(a) AC state with initial $K_{0}$=0.33

![](thesis/assets/media/image92.jpeg)

(b) Post-liquefaction state with initial $K_{0}$=0.33

![](thesis/assets/media/image93.jpeg)

(c) AC state with initial $K_{0}$=3.00

![](thesis/assets/media/image94.jpeg)

(d) Post-liquefaction state with initial $K_{0}$=3.00

Fig. 3.19. Contact force chain and displacement of particles under initial and post-liquefaction states subjected to different initial $K_{0}$

contact forces becomes insignificant in post-liquefaction stage. Whether $K_{0}$=0.33 or $K_{0}$=3.00, the contact forces no longer align with the initial direction of the maximum principal stress but tend to orient more randomly and concentrate locally.

#### Contact orientation 

The fabric tensor is orientation-dependent, meaning its elements vary based on the specified coordinate directions (Kanatani, 1984). This sparked interest in using statistical methods, such as spatial probability density function (PDF) to analyze the distribution of contact normal (Rothenburg and Bathurst, 1989). To simultaneously capture changes in both direction and quantity of contact normals during cyclic shear, it is recommended to use contact density for visualization. The contact density (Han et al., 2023) describes the average number of contacts per unit surface area for a particle with normalized radius, as shown in Eq. (3-16)

$\rho_{c}\left( \theta_{z},\ \phi_{cir} \right) = \frac{2N_{\theta_{z},\ \ \phi_{cir}}|n_{c} \in \left( \theta_{z},\theta_{z} + \Delta\theta_{z} \right) \cap (\phi_{cir},\ \phi_{cir} + \Delta\phi_{cir})}{N_{p}\int_{\phi_{cir}}^{\phi_{cir} + \Delta\phi_{cir}}{\sin\left( \phi_{cir} \right)d\phi_{cir}}\int_{\theta_{z}}^{\theta_{z} + \Delta\theta_{z}}{d\theta_{z}}}\ $ (3-16)

Here, $\rho_{c}$ represents the contact density, $\theta_{z}$ and $\phi_{cir}$ indicate the polar and azimuthal angles in the spherical polar coordinate system, respectively. $N_{\theta_{z},\ \ \phi_{cir}}$ indicates the number of contacts with normals within the range of $\left( \theta_{z},\theta_{z} + \Delta\theta_{z} \right) \cap (\phi_{cir},\ \phi_{cir} + \Delta\phi_{cir})$. $N_{p}$ and the subsequent integral denote the total number of particles and the corresponding surface area on the unit sphere, respectively. This method effectively evaluates contact orientation during an undrained cyclic shear and accommodates granular systems with various particle numbers.

The evolutions of contact density during the liquefaction process for $K_{0}$=0.33 and $K_{0}$=3.00, are shown in Fig. 3.20 and Fig. 3.21. Fig. 3.20(a) represents the dense state with initial $K_{0}$=0.33, exhibiting an elongated columnar shape extending along the axial direction, whereas Fig. 3.21(a) depicts the contact density with initial $K_{0}$=3.00, characterized by a dimpled ellipsoid oriented toward the axial direction. As cyclic shear progresses, the direction of maximum contact density varies following the rotating principal stress axis, and the overall contact density gradually decreases as shown in Fig. 3.20 (b) and Fig. 3.21 (b). The evolution of contact density indicates that the post-liquefaction distribution of contact density is largely independent of the initial state, shifting between two inclined elongated columnar distributions along varying directions.

![](thesis/assets/media/image95.jpeg) ![](thesis/assets/media/image96.jpeg)

(a) $N_{c}$/$N_{L}$=0.00 (b) $N_{c}$/$N_{L}$=0.75

![](thesis/assets/media/image97.jpeg) ![](thesis/assets/media/image98.jpeg)

\(c\) $N_{c}$/$N_{L}$=1.01 (d) $N_{c}$/$N_{L}$=1.04

Fig. 3.20. Contact density evolution in liquefaction process with initial $K_{0}$=0.33

![](thesis/assets/media/image99.jpeg) ![](thesis/assets/media/image100.jpeg)

(a) $N_{c}$/$N_{L}$=0.00 (b) $N_{c}$/$N_{L}$=0.73

![](thesis/assets/media/image101.jpeg) ![](thesis/assets/media/image102.jpeg)

\(c\) $N_{c}$/$N_{L}$=0.97 (d) $N_{c}$/$N_{L}$=1.03

Fig. 3.21. Contact density evolution in liquefaction process with initial $K_{0}$=3.00

Although $Z_{m0}$ has the dominant impact on liquefaction resistance, the variations in liquefaction resistance caused by morphological differences in fabric are also worth investigating. This morphological difference in fabric explains why, in the $Z_{mi}$-$N_{L}$ plane, as shown in Fig. 3.18 (b), paths with $K_{0}$\<1.0 and $K_{0}$\>1.0 diverge as stress anisotropy increases, and why $F_{c}$ exhibits more pronounced fluctuation with $K_{0}$\>1.0 than that with $K_{0}$\<1.0 during the cyclic shear in Fig. 3.16. The state with $K_{0}$\<1.0 corresponding to an elongated columnar morphology of fabric results in more contact normals along the axial direction, which is perpendicular to the shear force, potentially enhancing liquefaction resistance (Zhang et. al., 2023), compared to the dimpled ellipsoidal morphology observed for $K_{0}$\>1.0. Thus, a positive $\beta$ was obtained with the fitted surface in Fig. 3.17. Additionally, cyclic shear caused larger amplitude of fluctuations in $F_{c}$ during cyclic shear for $K_{0}$\>1.0 compared to $K_{0}$\<1.0 due to the instability in $F_{c}$ induced by the dimpled ellipsoidal morphology in fabric.

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

![](thesis/assets/media/image103.png)

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

![](thesis/assets/media/image104.jpeg)

Fig. 4.2. Air pluviation method for generating specimen

the funnel in a circular motion at a uniform speed, completing each circle in about 10 seconds. After filling, a ruler is used to level the surface by removing any uneven portions. The final weight of the added sand is measured to calculate the relative density. If the relative density falls within the acceptable range around the target value, the specimen preparation is deemed successful.

#### Installation of the torsional shear apparatus

The installation process begins by placing the upper torsional shear cap, designed to apply torsional shear forces, onto the top of the specimen. The membrane is carefully attached to the cap to ensure a secure fit. Tubes are then connected between the valves

![](thesis/assets/media/image105.jpeg)

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

![](thesis/assets/media/image107.png)

Fig. 4.5. Relationship between mean effective stress ($p'$) and shear stress ($\tau$) for $K_{0} =$`<!-- -->`{=html}1.0

loading causes $p'$ to oscillate along with the shear stress, forming closed loops that reflect the alternating shear directions. Figure 4.6 presents shear stress $\tau$ versus shear strain $\gamma$ relationship, highlighting the development of hysteretic loops typical of cyclic loading. These loops reflect the progressive deformation and energy dissipation within

![](thesis/assets/media/image108.png)

Fig. 4.6. Relationship between shear strain ($\gamma$) and shear stress ($\tau$) for $K_{0} =$`<!-- -->`{=html}1.0

the specimen. Figure 4.7 illustrates the evolution of pore water pressure over time during cyclic loading. The pore pressure increases incrementally with each shear cycle, eventually reaching a level comparable to the chamber pressure. This behavior aligns

![](thesis/assets/media/image109.png)

Fig. 4.7. Pore water pressure evolution during cyclic shear for $K_{0}$=1.0

with the expected trend for undrained conditions and confirms the occurrence of liquefaction. The results depicted in Fig. 4.5, 4.6, and 4.7 demonstrate characteristic responses under cyclic shear, validating the reliability and effectiveness of the experimental procedures.

#### Influence of $K_{0}$​ on liquefaction resistance: a comparison

Figures 4.5, 4.8, and 4.9 present the evolution of $p'$ and $\tau$ during cyclic loading under varying initial $K_{0}$. These results reveal both consistent characteristics of liquefaction behavior and notable differences, suggesting a relationship between $K_{0}$ and liquefaction resistance.

![](thesis/assets/media/image110.png)

Fig. 4.8. Relationship between mean effective stress ($p'$) and shear stress ($\tau$) for $K_{0} =$`<!-- -->`{=html}0.25

![](thesis/assets/media/image111.png)

Fig. 4.9. Relationship between mean effective stress ($p'$) and shear stress ($\tau$) for $K_{0} =$`<!-- -->`{=html}0.20

Across all three cases, $p'$ initially decreases progressively with cyclic loading, reflecting the buildup of pore pressure. The characteristic \"butterfly\" shape emerges as $p'$ approaches lower values, indicating a consistent progression toward liquefaction across all $K_{0}$ values.

A key difference lies in the number of cycles required to reach liquefaction, as reflected by the density of lines in the figures: Figure 4.5 ($K_{0} = 1.0$) shows the least line density, indicating that liquefaction occurred with the fewest cycles. This suggests the lowest liquefaction resistance under isotropic stress conditions. Figure 4.8 **(**$K_{0}$**=**0.25**)** exhibits the highest line density, meaning the largest number of cycles was required to reach liquefaction. Figure 4.9 **(**$K_{0}$=0.20**)**, while still requiring more cycles than $K_{0}$=1.0, shows a slightly reduced line density compared to $K_{0}$=0.25. This suggests a decrease in liquefaction resistance as $K_{0}$​ decreases further from 0.25 to 0.20.

The results suggest a non-linear relationship between $K_{0}$ and liquefaction resistance. As $K_{0}$​ decreases from 1.0 (isotropic) to 0.25, liquefaction resistance increases, as evidenced by the greater number of cycles required for liquefaction. However, when $K_{0}$ further decreases from 0.25 to 0.20, liquefaction resistance slightly diminishes. This observation raises the hypothesis that liquefaction resistance may peak at a specific $K_{0}$​ value and subsequently decrease with further reductions in $K_{0}$​.

#### Liquefaction resistance across a broader range of $K_{0}$

Figure 4.10 illustrates the variation in the number of cycles required for liquefaction ($N_{L}$) as a function of $K_{0}$, with liquefaction defined as the point where pore water pressure reaches 95% of the initial confining pressure. The figure covers a broad range of ​$K_{0}$ values, from isotropic stress conditions ($K_{0}$=1.0) to highly anisotropic states ($K_{0}$=0.2 and $K_{0}$=3.0), allowing for a comprehensive analysis of the influence of stress anisotropy on liquefaction resistance.

![](thesis/assets/media/image112.png)

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

