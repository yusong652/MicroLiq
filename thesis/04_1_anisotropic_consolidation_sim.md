---
title: "Chapter 4: Study On Factors Affecting Liquefaction Resistance During Anisotropic Consolidation"
tags: [thesis, chapter-4, anisotropic-consolidation, K0-effect, HCA, liquefaction-resistance, experimental-validation]
aliases: [Anisotropic Consolidation, Chapter 4, K0 Effect]
---

# Study on Factors Affecting Liquefaction Resistance during Anisotropic Consolidation

This chapter employs DEM to investigate the effects of stress anisotropy on liquefaction resistance of sand soils through undrained cyclic shear simulations. A combined servo mechanism replicates undrained conditions and stress states in hollow cylinder apparatus (HCA) tests. Specimens are prepared following initial isotropic consolidation to $p'$=10 kPa followed by linear anisotropic consolidation (IC-AC) to $p'$=100 kPa. The investigation proceeds in two stages. First, the macroscopic $K_{0}$-dependent liquefaction resistance trend is established using three representative cases—compression ($K_{0}$=0.5), isotropic ($K_{0}$=1.0), and extension ($K_{0}$=2.0)—at a dense state ($D_r \approx 90\%$) across multiple cyclic stress ratios, accompanied by macroscopic energy and stiffness analyses and microscopic fabric evolution. Second, to disentangle the roles of packing compactness and directional fabric anisotropy, a medium-dense state ($D_r \approx 75\%$) is introduced alongside the dense state, and the $K_{0}$ range is extended to five values (0.5, 0.67, 1.0, 1.5, and 2.0) at CSR = 0.300, yielding ten cases. The factors that influence liquefaction resistance are attributed to changes in both macroscopic and microscopic quantities, such as void ratio and coordination number ($Z_{m}$). The signed fabric anisotropy indicator $\alpha_0$, which distinguishes compression-type and extension-type contact orientations, is shown to correlate directly with the variation in liquefaction resistance among different $K_{0}$ states.

##  Introduction

During earthquake loading, saturated granular soils can experience a rapid rise in pore pressure that drastically reduces their shear strength. This phenomenon, termed liquefaction, has caused severe damage to infrastructure and buildings (Ishihara and Koga, 1981; Seed and Idriss, 1967). Triaxial tests have been extensively conducted to elucidate the mechanisms of liquefaction, where saturated specimens were subjected to cyclic loading under undrained conditions until liquefaction was triggered. The influence of factors such as cyclic stress ratio (CSR), relative density, as well as confining pressure on the resistance to liquefaction was examined (Hyodo et al., 1991; Seed and Lee, 1966; Silver et al., 1976; Toki et al., 1986; Yoshimi et al., 1984). However, vertically propagating shear waves in the ground apply gradually varying shear stress on soil elements, leading to a continuous rotation of principal stress axes (Arthur et al., 2009; Arthur et al., 1980; Ishihara and Yasuda, 1975; Ishihara and Towhata, 1983; Yamashita and Toki, 1993).

Alternative testing methods, such as the hollow torsional shear test, apply shear forces to specimens, allowing for continuous variation of principal stress axes and thereby addressing the limitations of the triaxial test. Ishihara and Yasuda (1975) pioneered the utilization of hollow torsional cylindrical apparatus (HCA) by subjecting the hollow cylindrical samples to irregular wave loading, studying the disparities compared to triaxial shear tests. Tatsuoka et al. (1986) performed both triaxial and torsional tests on specimens prepared using different methods and found that the results were inconsistent between the triaxial and torsional tests. Torsional and triaxial shear tests conducted by Yamashita and Toki (1993) and employed by Oka et al. (1999) to enhance the constitutive model for liquefiable sands also demonstrated that method of testing with torsional or triaxial shear, influences the results of liquefaction resistance. These studies highlight the significance of experimental methods, such as HCA tests, in liquefaction analyses and aroused great interest in numerical replication of these tests.

Soils under a natural state generally display various ratios of lateral to vertical effective stress, denoted as $K_{0}$. The influence of $K_{0}$ on liquefaction resistance has been investigated extensively, yet the reported findings vary considerably depending on test conditions. Ishihara and Takatsu (1979) observed that the liquefaction strength of Fuji River sand does not exhibit a notable dependency on the initial stress state with different $K_{0}$ values. Similar results were also obtained in the laboratory tests conducted by Yamashita and Toki (1993). On the other hand, the hollow torsional experiments conducted by Georgiannou and Konstadinou (2014) indicated that isotropically consolidated (IC) specimens demonstrate higher liquefaction resistance for loose sands than anisotropically consolidated (AC) specimens. By contrast, that pattern did not hold in dense states, where increasing relative density reversed the trend. Additionally, Vargas et al. (2020) concluded from similar laboratory tests on Ottawa sand with relative densities ranging from 50% to 80% that AC specimens with a $K_{0}$ of 0.5 showed a liquefaction strength approximately 20% higher than IC specimens. The experimental conclusions regarding the influence of $K_{0}$ on liquefaction resistance have been debated for decades, underscoring the necessity of elucidating $K_{0}$ effects on liquefaction resistance through alternative means. Despite extensive experimental work, the particle-scale mechanisms through which stress anisotropy alters liquefaction resistance remain insufficiently clarified.

The discrete element method (DEM) (Cundall and Strack, 1979) simulation provides an insight into granular material and offers advantages by eliminating concerns related to variations in initial states caused by sample preparation, making it a desirable numerical method to study the cause of changes in liquefaction resistance. Numerous examples utilizing DEM exist for undrained cyclic shear tests to find explanations of microscopic factors affecting liquefaction resistance. Huang et al. (2018) conducted undrained shear tests on triaxial specimens, trying to relate monotonic and cyclic behaviors. Yang et al. (2021) performed undrained simple shear tests and studied the influence of multi-directional shear stress on liquefaction resistance. Jiang et al. (2021) applied various forms of strain waves to specimens, investigating their impact on liquefaction resistance. Morimoto et al. (2021) examined the impact of pre-shearing on the liquefaction resistance using DEM simulation of undrained triaxial cyclic shear tests. Xie et al. (2023), as well as Yang and Huang (2023) explored the effect of liquefaction history-induced fabric on liquefaction resistance by conducting reliquefication simulation. Zhang et al. (2023) arranged ellipsoidal clumped pebbles and applied both vertical and horizontal shear loading in to discuss the influence of inherent fabric anisotropy on liquefaction resistance. Wu and Yang (2022) implemented undrained rotational shear on polyhedral specimens with 26 boundary walls, providing microscopic insights into fabric evolution under principal stress rotation. Some of these studies included triaxial specimens, which do not account for principal stress axis rotation. Others utilized virtual periodic boundaries or cubic rigid box, which are difficult to implement in real-world scenarios. Replicating HCA tests through simulation provides a meaningful connection between numerical and experimental methods.

Using DEM to replicate HCA test is relatively specialized, but still has precedents. Li et al. (2014) conducted DEM simulations of drained tests and investigated the strain localization in HCA test. Liu et al. (2021) conducted analysis of torsional shear tests under drained conditions and investigated the development of cracks at different principal stress rotation angles. This study introduced an algorithm that realizes both undrained and stress conditions in HCA test, filling a gap in HCA simulation using DEM (Ma et al., 2024).

To clarify the influence of the $K_{0}$ on liquefaction resistance, Yang and Taiebat\'s (2024) consolidated specimens with different preparation methods and conducted undrained cyclic shear tests. They found that both preparation protocols and $K_{0}$ influence liquefaction resistance. As the relative density increased, the difference in liquefaction resistance narrowed gradually for IC and AC states. Otsubo et al. (2022) employed $K_{0}$ to induce inherent fabric anisotropy in specimen under a low stress condition and then consolidated it to the target $p'$ and examined its effects on liquefaction resistance. A specimen with higher anisotropy has weaker stiffness in its minor direction and resulted a lower liquefaction resistance. However, triaxial configurations do not incorporate principal stress axis rotation, while periodic-boundary and polyhedral specimen settings, though capable of applying general stress paths, lack direct counterparts in standard laboratory apparatus. DEM simulations that explicitly reproduce HCA-type boundary conditions remain relatively limited, particularly for systematic investigation of $K_{0}$ effects under undrained cyclic torsional shear.

The stress paths for specimen preparation often entail linearly increasing $p'$ and $q$ to the state with target $K_{0}$ in both experimental (Vargas et al., 2020) and numerical (Yang and Taiebat, 2024) tests. This study demonstrates DEM analysis of cyclic undrained HCA tests (Ma et al., 2024) and explores the effects of $K_{0}$ on liquefaction resistance. Specimens are prepared via an IC-AC stress path, where initial isotropic consolidation is followed by linear anisotropic consolidation to the target $K_0$. The investigation is organized in two stages. In the first stage, three representative $K_0$ states (0.5, 1.0, and 2.0) at a dense state ($D_r \approx 90\%$) are subjected to cyclic loading across multiple CSR levels to establish the macroscopic liquefaction resistance ordering and to examine the associated energy, stiffness, and fabric evolution in detail. In the second stage, a medium-dense state ($D_r \approx 75\%$) is introduced alongside the dense state, and the $K_0$ range is extended to five values (0.5, 0.67, 1.0, 1.5, and 2.0) at CSR = 0.300, yielding ten cases designed to disentangle the respective contributions of packing compactness and directional fabric anisotropy to liquefaction resistance.

## DEM simulation setup

### Specimen preparation

Itasca PFC^3D^ (Itasca Consulting Group, Inc., 2021) was employed to implement DEM simulations of undrained cyclic torsional shear test. Unlike the periodic boundaries commonly used in element tests, the HCA in DEM simulation employs two cylinders, upper and lower planes, as well as six blades to provide torsional force, closely approximating the boundary conditions of HCA (Ishihara and Yasuda, 1975; Vargas et al., 2020; Li et al, 2014; Liu et al, 2021). As shown in Fig. 4.1(a), two rigid cylindrical walls with inner diameter of 6 cm and outer diameter of 10 cm are positioned coaxially and vertically, with the upper and lower planes placed 10 cm apart, resembling the geometric dimensions of laboratory tests (Vargas et al., 2020).

![](thesis/assets/media/image65.jpg)

(a) Pouring method for generating particles

![](thesis/assets/media/image66.jpg)

(b) Insertion of torsional blades

Fig. 4.1. Specimen generation process in the initial stage using the pouring method and insertion of torsional blades

This research employed a particle size distribution ranging from 1.0 mm to 3.0 mm, which is a 10× scaled-up analogue of the grain size distribution of Toyoura sand, and utilizes a rolling resistance contact model (Iwashita and Oda, 1998; Wensrich and Katterfeld, 2012) to mimic the non-spherical effects of sand particles. The specific parameters of the contact model are listed in Table 4-1. To ensure similarity with laboratory methods, the particles were initially generated in the upper part of the apparatus and then allowed to flow downward under the influence of gravity, forming the specimen as shown in Fig. 4.1(a). The stress calculations of HCA are summarized according to the formulas provided in Table 4-2 ,where the values of $\sigma_{z}$ and $\sigma_{\theta}$ are derived from the equilibrium relations, $\varepsilon_{z}$ and $\gamma_{z\theta}$ are based on strain compatibility, and the remaining stress and strain expressions align with the assumption of linear elasticity (Hight et al., 1983).

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

The specimen was initially compressed under a friction coefficient of 0.0 to a target void ratio, which is determined through the iterative calibration procedure described in Section 4.2.3: approximately 0.736 for the dense state ($D_r \approx 90\%$) and 0.742 for the medium-dense state ($D_r \approx 75\%$). Subsequently, the friction coefficient was reset to 0.5, followed by anisotropic consolidation from a state with $p'$=10.0kPa and $K_{0}$=1.0 to $p'$=100.0kPa and the target $K_{0}$ (IC-AC protocol). Notably, during the AC process with an increasing $p'$, $K_{0}$ evolves from 1.0 to the corresponding target $K_{0}$.

The cyclic shear simulation program consists of two sets. In the primary set, three representative $K_{0}$ states—0.5 (compression), 1.0 (isotropic), and 2.0 (extension)—are examined at a dense state ($D_r \approx 90\%$) across multiple CSR levels to characterize how liquefaction resistance varies with the direction and magnitude of stress anisotropy, and to trace the associated energy dissipation, stiffness degradation, and fabric evolution. In the expanded set, a medium-dense state ($D_r \approx 75\%$) is introduced alongside the dense state, and two additional $K_{0}$ values (0.67 and 1.5) are included to refine the coverage of anisotropy levels, yielding ten cases ($2 \times 5$) at a single CSR = 0.300. This expanded set allows examination of whether the $K_{0}$-dependent liquefaction resistance trend observed at $D_r \approx 90\%$ persists at a lower density, and provides a broader parametric basis for the subsequent microscopic analysis.

During the AC process, both $p'$ and $q$ increase simultaneously, with the stress path depending on the target $K_{0}$ value, as illustrated in Fig. 4.2(a) and Fig. 4.2(b).

As indicated by Fig. 4.2(b), the void ratio decreases from approximately 0.736 at the initial state ($p'$=10 kPa) to around 0.732 at the target stress ($p'$=100 kPa) during anisotropic consolidation. The differences in final void ratio $e$ between different $K_{0}$ states after IC-AC are minimal, with $e$ ranging from 0.7315 to 0.7325. This small variation (approximately 0.001) makes it reasonable to emphasize the effects of microscopic quantities, such as coordination number and fabric anisotropy, rather than $e$, on liquefaction resistance.

![](thesis/assets/media/image67_k05.jpg)

(a) $K_{0}$=0.5

![](thesis/assets/media/image67_k10.jpg)

(b) $K_{0}$=1.0

![](thesis/assets/media/image67_k20.jpg)

(c) $K_{0}$=2.0

Fig. 4.3. Visualization of hollow cylindrical specimens after anisotropic consolidation to $p'$=100 kPa with different $K_{0}$ values. Cross-sectional view shows particles (colored by radius) and contact forces (red vectors), corresponding to the final states in Fig. 4.2.

### Implementation of undrained condition

In DEM simulations of undrained tests, the interaction between water and particles is disregarded, employing a constant volume approach to replicate the undrained condition. The effectiveness of this constant volume approach has been validated in numerous DEM simulations (Sitharam et al., 2002; Yimsiri and Soga, 2010). To simultaneously achieve the stress boundary conditions and undrained condition observed in laboratory HCA tests, a combined servo mechanism was first proposed by Han et al. (2024) for undrained cyclic torsional shear and subsequently generalized by Ma et al. (2024) to accommodate a broader range of loading conditions, including drained stress paths, combined axial--torsional loading, and strain-controlled modes.

The key challenge in simulating undrained HCA tests lies in satisfying multiple conditions simultaneously. In laboratory tests, the inner and outer chamber pressures ($p_i$ and $p_o$) are maintained equal and constant, the additional axial pressure ($p_z$) or height ($H$) is controlled, and a target shear stress ($\tau_{z\theta,tar}$) is applied. Meanwhile, the undrained condition requires constant volume. This study addresses these challenges through a combined servo mechanism by controlling four kinematic variables: inner radius rate ($dr/dt$), outer radius rate ($dR/dt$), height rate ($dH/dt$), and rotation angle rate ($d\theta/dt$), to satisfy four condition equations simultaneously. The servo operates on two effective stress differences measured from particle–wall contact forces: $\sigma_{dif,r}' = \sigma_o' - \sigma_i'$ (outer minus inner radial effective stress) and $\sigma_{dif,z}' = \sigma_z' - \sigma_r'$ (axial minus average radial effective stress). Their target values are prescribed as total stress differences from the HCA boundary conditions.

**Condition 1: Target radial stress difference**

The inner radius rate is determined by the radial stress error, as expressed in Eq. (4-1), where $\sigma_{dif,r}^{tar} = p_o - p_i$ is the target value, $p_o$ and $p_i$ are the outer and inner chamber pressures of the HCA, and $S_{cr}$ is the servo coefficient. In the present study, $p_o = p_i$ (equal chamber pressures) is adopted, so $\sigma_{dif,r}^{tar} = 0$.

$$\frac{dr}{dt} = \frac{\sigma_{dif,r}' - \sigma_{dif,r}^{tar}}{\Delta t}S_{cr}$$ (4-1)

**Condition 2: Axial boundary condition**

Two modes are available. In stress-control mode, the height rate is governed by a servo equation targeting the additional axial pressure, as shown in Eq. (4-2), where $\sigma_{dif,z}^{tar} = p_z$ is the target additional axial pressure and $S_{cz}$ is the corresponding servo coefficient. This mode is used during anisotropic consolidation and monotonic shear validation (Section 4.2.3).

$$\frac{dH}{dt} = \frac{\sigma_{dif,z}' - \sigma_{dif,z}^{tar}}{\Delta t}S_{cz}$$ (4-2)

In displacement-control mode, the height is held constant ($dH/dt = 0$), which is adopted for all cyclic shear simulations in this study.

**Condition 3: Target shear stress**

The rotation angle rate is controlled to achieve the target shear stress through Eq. (4-3), where $T$ is the current torque, $T^{tar}$ is the target torque, and $S_{cs}$ is the servo coefficient.

$$\frac{d\theta}{dt} = \frac{T - T^{tar}}{\Delta t}S_{cs}$$ (4-3)

**Condition 4: Undrained condition (constant volume)**

The undrained condition is ensured by maintaining constant volume throughout the cyclic shear test, as expressed in Eq. (4-4).

$$2\pi H\left(R\frac{dR}{dt} + r\frac{dr}{dt}\right) + \pi(R^2 - r^2)\frac{dH}{dt} = 0$$ (4-4)

By combining these four equations, the system of four kinematic variables ($dr/dt$, $dR/dt$, $dH/dt$, $d\theta/dt$) and four constraints is solved simultaneously at each timestep, achieving both the stress conditions and undrained condition in DEM simulation of HCA tests. This combined servo mechanism (Han et al., 2024; Ma et al., 2024) replicates the boundary conditions observed in laboratory undrained cyclic torsional shear tests. The analytical solution of the coupled radial–axial servo is derived below.

**Determination of servo coefficients**

The servo coefficients ($S_{cr}$, $S_{cz}$, $S_{cs}$) in the combined servo mechanism are determined based on the contact stiffness between boundaries and particles. For the torsional servo coefficient $S_{cs}$ in Condition 3, the moment of inertia of shear stiffness $I_{rot}$ is calculated considering the distance from the center of rotation. Fig. 4.4 illustrates the contact between a particle and a blade, where $r_{d}$ denotes the distance from the center of rotation to the contact point, and $\theta$ is the angle between the contact normal and the horizontal plane.

![](thesis/assets/media/image73.png)

Fig. 4.4. Determination of moment of inertia of shear stiffness in servo mechanism for torque application

The moment of inertia $I_{rot}$ is calculated by Eq. (4-5), where $k_{n}$ represents the normal contact stiffness. The contribution of each contact is adjusted by $\cos^{2}\theta$ because a larger $\theta$ reduces its contribution to the shear stiffness. The servo coefficient $S_{cs}$ for torsional control is then determined by Eq. (4-6).

$$I_{rot} = \Sigma r_{d}^{2}k_{n}\cos^{2}\theta$$ (4-5)

$$S_{cs} = \frac{1}{I_{rot}}$$ (4-6)

The servo coefficients $S_{cr}$ and $S_{cz}$ for the radial and axial directions are determined analogously, but their derivation requires consideration of the volume-coupling effect. From the constant-volume constraint (Eq. 4-4), the outer radius rate is:

$$\frac{dR}{dt} = -\frac{r}{R}\frac{dr}{dt} - \frac{R^2 - r^2}{2RH}\frac{dH}{dt}$$ (4-7)

Movement of both the inner wall ($dr$) and the top/bottom plates ($dH$) induces outer wall displacement through Eq. (4-7), which in turn affects both the radial and axial stress differences. Let $K_{r,i} = \sum_{c \in \text{inner}} k_n$ and $K_{r,o} = \sum_{c \in \text{outer}} k_n$ denote the aggregate normal contact stiffness at the inner and outer cylinders, respectively, and $K_z = \frac{1}{2}\sum_{c \in \text{top/bottom}} k_n$ the effective axial contact stiffness, where the summations run over all particle–wall contacts on the respective rigid boundaries. The factor $\frac{1}{2}$ arises because the top and bottom plates move symmetrically (each by $dH/2$) to achieve the total height change $dH$.
The stress responses to the kinematic increments $dr$ and $dH$ can be expressed in matrix form:

$$\begin{pmatrix} \delta\sigma'_{dif,r} \\ \delta\sigma'_{dif,z} \end{pmatrix} = \begin{pmatrix} K_{11} & K_{12} \\ -K_{11} & K_z - K_{12} \end{pmatrix} \begin{pmatrix} dr \\ dH \end{pmatrix}$$ (4-8)

where $K_{11} = K_{r,i} + \frac{r}{R}K_{r,o}$ and $K_{12} = \frac{R^2 - r^2}{2RH}K_{r,o}$. The off-diagonal term $K_{12}$ represents the cross-coupling from the volume constraint: an axial displacement $dH$ induces an outer wall displacement through Eq. (4-7), which alters the radial stress. Since $\sigma'_{dif,z} = \sigma'_z - \sigma'_r$, the axial stress difference is affected by both the axial displacement (through $K_z$) and the radial displacement (through $-K_{11}$), because changes in the radial stress enter $\sigma'_{dif,z}$ with opposite sign. Similarly, $dH$ affects $\sigma'_{dif,z}$ through both the direct axial stiffness $K_z$ and the volume-constraint-induced radial stress change $-K_{12}$.

The determinant of the stiffness matrix is $\det(\mathbf{K}) = K_{11}(K_z - K_{12}) + K_{11}K_{12} = K_{11}K_z$, so the fully coupled servo equations are:

$$\frac{dr}{dt} = \frac{K_z - K_{12}}{K_{11}K_z}\frac{e_r}{\Delta t} - \frac{K_{12}}{K_{11}K_z}\frac{e_z}{\Delta t}$$ (4-9)

$$\frac{dH}{dt} = \frac{1}{K_z}\frac{e_r}{\Delta t} + \frac{1}{K_z}\frac{e_z}{\Delta t}$$ (4-10)

where $e_r = \sigma'_{dif,r} - \sigma_{dif,r}^{tar}$ and $e_z = \sigma'_{dif,z} - \sigma_{dif,z}^{tar}$ are the stress errors for the radial and axial conditions, respectively. The remaining kinematic variable $dR/dt$ is then obtained by substituting $dr/dt$ and $dH/dt$ into Eq. (4-4).

Under the constant-height condition ($dH/dt = 0$) adopted for all cyclic shear simulations in this study, only the radial condition remains active, and the servo coefficient simplifies to:

$$S_{cr} = \frac{1}{K_{r,i} + \frac{r}{R}K_{r,o}}$$ (4-11)

For the general case ($dH/dt \neq 0$), such as the monotonic shear validation in Section 4.2.3, the fully coupled servo equations (Eq. 4-9 and 4-10) are applied at each timestep. In practice, a relaxation factor less than unity is applied to the servo coefficients to ensure numerical stability and suppress oscillation.

**Excess pore water pressure calculation**

The effective stresses are evaluated by measuring the contact stresses between the boundary and particle skeleton. The assumptions of undrained condition and full saturation result in variations in effective stress on lateral cylinders and excess pore water pressure (EPWP) that are equal in magnitude but opposite in sign, as quantified in Eq. (4-7). Here, $u$ represents the EPWP, $\sigma_{r}'$ denotes the radial effective stress derived from the inner and outer effective stresses, and $\sigma_{r0}'$ is its initial value (Yimsiri and Soga, 2010).

$$u = \sigma_{r0}' - \sigma_{r}'$$ (4-7)

### Parameter calibration and validation

The micro-parameters listed in Table 4-1 were determined through a systematic iterative calibration procedure against experimental data from hollow cylinder apparatus tests on dense Toyoura sand. Since the micro-parameters collectively influence macroscopic responses including shear stiffness, dilatancy, and liquefaction resistance, the calibration followed an iterative strategy targeting these behaviors in sequence.

Starting from a base set of parameters at a given void ratio, the contact Young's modulus $E$ and rolling friction coefficient $\mu_r$ were adjusted while keeping the normal-to-shear stiffness ratio $\kappa$ constant, aiming to reproduce the shear stiffness observed in undrained monotonic shear tests. The effective stress path in $p'$-$\tau_{z\theta}$ space was then examined to assess dilatancy. If the simulated dilatancy was insufficient---i.e., the mean effective stress at phase transformation was lower than the experimental value---the specimen was further compacted to a lower void ratio, which increased both dilatancy and shear stiffness; $E$ was then reduced accordingly to restore the target shear stiffness. This iterative process between void ratio, contact modulus, and rolling friction was repeated until both the shear stiffness and dilatancy simultaneously matched the monotonic experimental data. The calibrated parameters were then verified against cyclic liquefaction resistance curves, with minor adjustments made as needed to achieve satisfactory agreement across all three aspects. The resulting parameters (Table 4-1) were employed for all subsequent simulations.

The calibrated parameters were validated against experimental data for dense Toyoura sand ($D_r \approx 90\%$, $p'_{0}$=100 kPa, $K_{0}$=1.0) under both monotonic and cyclic loading conditions, targeting three macroscopic behaviors: shear stiffness, dilatancy, and cyclic liquefaction resistance. For monotonic validation, undrained torsional shear simulations were compared with HCA tests reported by Nakata et al. (1998), where the additional axial pressure $p_z$ was maintained at zero (i.e., $\sigma_{dif,z}' = 0$ in Eq. 4-2) to ensure the axial effective stress equals the radial effective stress during shearing. For cyclic validation, specimens were subjected to sinusoidal torsional shear at five CSR levels (0.20, 0.25, 0.30, 0.35, 0.40) and compared with the classical data of Ishihara et al. (1985), with liquefaction defined as single-amplitude shear strain reaching $\gamma_{SA}$=2.5%.

![](thesis/assets/images/validate_p_q_dense.png)

(a) Effective stress path

![](thesis/assets/images/validate_gamma_q_dense.png)

(b) Stress-strain relationship

![](thesis/assets/images/validate_N_csr.png)

(c) Liquefaction resistance curve

Fig. 4.5. Validation of DEM simulation against experimental data for dense Toyoura sand ($D_r \approx 90\%$, $p'_{0}$=100 kPa, $K_{0}$=1.0): (a) effective stress path and (b) stress-strain relationship from undrained monotonic shear (Nakata et al., 1998); (c) cyclic stress ratio versus number of cycles to liquefaction (Ishihara et al., 1985)

Fig. 4.5 demonstrates that the DEM model simultaneously reproduces three key aspects of undrained behavior. The effective stress path (Fig. 4.5(a)) captures the initial contraction followed by dilation towards the critical state line, matching the experimental trend. The stress-strain relationship (Fig. 4.5(b)) reproduces the shear stiffness and strain-hardening behavior. The liquefaction resistance curve (Fig. 4.5(c)) shows good agreement across the full range of CSR. The simultaneous agreement across stiffness, dilatancy, and cyclic liquefaction resistance validates both the micro-parameters (Table 4-1) and the combined servo mechanism described in Section 4.2.2.

Having validated the model against isotropic consolidation conditions ($K_{0}$=1.0), the following sections investigate how different consolidation stress ratios affect liquefaction resistance. Specimens with three representative $K_{0}$ values (0.5, 1.0, 2.0) obtained from the IC-AC protocol underwent undrained cyclic torsional shear until liquefaction occurred. The cyclic shear stress is applied as a sinusoidal wave with different cyclic stress ratios (CSR). Unlike the monotonic shear validation where zero additional axial pressure was maintained, constant height (dH/dt = 0) is adopted for all cyclic shear simulations to match typical HCA test protocols. The factors influencing liquefaction resistance are discussed from both macroscopic and microscopic perspectives.

## Results and discussion

### Macroscopic response

#### Stress strain relationship

Fig. 4.6(a)-(d) present typical stress and strain evolution during undrained cyclic shear for specimens with different initial $K_{0}$ values at CSR=0.200.

|  |  |
| :--: | :--: |
| ![](thesis/assets/images/stress_rel.png) | ![](thesis/assets/images/stress_strain.png) |
| (a) Shear stress $\tau_{z\theta}$ vs. mean effective stress $p'$ ($K_{0}$=1.0, CSR=0.200) | (b) Shear stress $\tau_{z\theta}$ vs. shear strain $\gamma_{z\theta}$ ($K_{0}$=1.0, CSR=0.200) |
| ![](thesis/assets/images/stress_dev.png) | ![](thesis/assets/images/stress_u_compare.png) |
| (c) Deviatoric stress $\sigma_{vM}$ vs. mean effective stress $p'$ for three $K_{0}$ values (CSR=0.200) | (d) Excess pore water pressure ratio $r_{u}$ evolution for three $K_{0}$ values (CSR=0.200) |

Fig. 4.6. Typical macroscopic response during undrained cyclic shear at CSR=0.200: (a) $\tau_{z\theta}$-$p'$ relationship for $K_{0}$=1.0; (b) $\tau_{z\theta}$-$\gamma_{z\theta}$ relationship for $K_{0}$=1.0; (c) $\sigma_{vM}$-$p'$ relationship for three $K_{0}$ values; (d) excess pore water pressure ratio $r_{u}$ evolution for three $K_{0}$ values

As the shear stress $\tau_{z\theta}$ cyclically acts on the hollow cylindrical specimen, the mean effective stress $p'$ exhibits an overall decrease. Once $p'$ falls below approximately 60 kPa, an increase in the magnitude of $\tau_{z\theta}$ drives an upward trend in $p'$, displaying a butterfly-shaped relationship. After liquefaction onset, $p'$ and $\tau_{z\theta}$ delineate the critical state line and converge at the origin periodically.

Fig. 4.6(b) shows that the stress-strain relationship exhibits stiff shear modulus with slight reduction in the initial stage. As cyclic loading progresses towards liquefaction, shear stiffness markedly decreases, plastic deformation occurs, and strong nonlinearity becomes evident in the hysteretic loops.

Fig. 4.6(c) compares the deviatoric von-Mises stress $\sigma_{vM}$ evolution for three $K_{0}$ values. The $K_{0}$=1.0 specimen starts with $\sigma_{vM}$ at zero due to isotropic consolidation, while $K_{0}$=0.5 and $K_{0}$=2.0 specimens exhibit initial deviatoric stress due to anisotropic consolidation. As cyclic shear progresses, specimens with different $K_{0}$ values follow distinct stress paths toward the critical state line, with varying rates of stress degradation and liquefaction resistance.

Fig. 4.6(d) shows that the EPWP responses differ significantly among the three $K_{0}$ states. The $K_{0}$=2.0 specimen shows the most rapid $r_{u}$ accumulation, while the $K_{0}$=0.5 specimen exhibits the slowest, with the $K_{0}$=1.0 specimen intermediate between the two. These observations provide clear evidence that initial stress anisotropy significantly influences liquefaction resistance.

Two commonly used liquefaction criteria are considered in this study: a stress-based criterion, defined as excess pore water pressure reaching 95% of the initial radial effective stress $\sigma_{r0}'$ (i.e., $r_{u}$ = 0.95), and a strain-based criterion, defined as single-amplitude shear strain reaching $\gamma_{SA}$ = 2.5% (as adopted in Section 4.2.3.2 for validation against Ishihara et al. (1985)). A comparison of the two criteria across all simulated cases confirms that they yield nearly identical conclusions: the strain-based criterion consistently produces $N_L$ values approximately 1–2 cycles higher than the stress-based criterion (e.g., for CSR=0.200, $N_L$ = 39.5 vs. 33.8 for $K_0$=0.5, 31.5 vs. 33.8 for $K_0$=1.0, and 29.5 vs. 30.8 for $K_0$=2.0), and the relative ordering among $K_0$ states remains unchanged. Since this study focuses on comparing specimens with different initial stress states, the stress-based criterion ($r_{u}$ = 0.95) is adopted for all subsequent analyses, as it directly reflects the loss of effective stress that constitutes the fundamental mechanism of liquefaction.

#### Liquefaction resistance curves

To systematically investigate how liquefaction resistance varies with CSR and $K_{0}$, Fig. 4.7 presents the cyclic stress ratio versus number of cycles to liquefaction for three representative $K_{0}$ values.

![](thesis/assets/images/liq_res_cur.png)

Fig. 4.7. Cyclic liquefaction resistance curves for specimens with three representative stress anisotropies ($K_{0}$=0.5, 1.0, 2.0)

The liquefaction resistance curves demonstrate clear dependency on initial stress anisotropy. For all CSR levels tested, the isotropic consolidation state ($K_{0}$=1.0) exhibits intermediate liquefaction resistance. The compression state ($K_{0}$=0.5) shows the highest resistance, requiring more cycles to reach liquefaction at the same CSR. Conversely, the extension state ($K_{0}$=2.0) demonstrates the lowest resistance, reaching liquefaction with fewer cycles. This trend reveals that the effect of $K_{0}$ on liquefaction resistance depends not only on the magnitude of stress anisotropy but also on its direction: compression conditions ($K_{0}$<1.0) enhance liquefaction resistance relative to the isotropic state, while extension conditions ($K_{0}$>1.0) reduce it. The observed directional dependency is consistent with the findings by Georgiannou and Konstadinou (2014) for dense sand states and the experimental results of Vargas et al. (2020) who reported approximately 20% higher liquefaction strength for $K_{0}$=0.5 specimens compared to isotropic conditions. More recently, Zhao et al. (2024) conducted systematic HCA torsional shear tests covering both compressional and extensional consolidation states and reported higher shear strengths under compressive anisotropic consolidation, further supporting this directional dependency. This contrasts with some earlier experimental studies (Ishihara and Takatsu, 1979; Yamashita and Toki, 1993) that reported minimal $K_{0}$ dependency.

#### Cumulative shear work

Cumulative shear work refers to the energy input during undrained cyclic shear in this study. It is valuable to examine the correlation between the liquefaction resistance of soils and their susceptibility to the input energy. Towhata and Ishihara (1985) conducted a series of experiments where isotropically consolidated sand specimens were subjected to undrained cyclic shear under various combinations of torsional and axial shear stresses with continuous rotation of principal stress axes. They revealed a unique relationship between excess pore water pressure and shear work that is independent of the shear stress paths applied. Figueroa et al. (1994) similarly confirmed that the shear work required for triggering liquefaction is independent of the amplitude of strain through strain-controlled tests. Georgiannou and Konstadinou (2014) concluded from the comparison between IC and AC specimens that the energy associated with terminal water pressure is positively correlated with relative density. For equivalent relative densities, AC specimens require greater energy than IC specimens to induce liquefaction.

![](thesis/assets/images/normalized_ru.png)

(a) $r_{u}$ vs. $N_{c}/N_{L}$

![](thesis/assets/images/acc_energy.png)

(b) $W_{s}$ vs. $N_{c}/N_{L}$

![](thesis/assets/images/acc_energy_Nc.png)

(c) $W_{s}$ vs. $N_{c}$

![](thesis/assets/images/acc_energy_EPWP.png)

(d) $r_{u}$ vs. $W_{s}$

Fig. 4.8. EPWP ratio and cumulative shear work evolution during cyclic shear, and relationship between EPWP ratio and shear work for different $K_{0}$ (CSR=0.200)

The cumulative unit volume shear work $W_{s}$ is defined as shown in Eq. (4-8), expressed as an integral of shear strain rate $\dot{\gamma_{z\theta}}$, shear stress $\tau_{z\theta}$, and incremental time $dt$. This represents the accumulated input energy per unit volume in the specimen.

$W_{s} = \int_{0}^{t}{\dot{\gamma_{z\theta}}\tau_{z\theta}dt}$ (4-8)

Fig. 4.8(a) presents the normalized EPWP ratio evolution during cyclic shear. The three $K_{0}$ states all start from $r_{u} = 0$ and follow a similar exponential-like growth pattern. During the intermediate stage ($0.2 < N_c/N_L < 0.8$), clear divergence emerges: the $K_{0}$=0.5 specimen consistently exhibits the lowest $r_{u}$, while the $K_{0}$=2.0 specimen shows the highest. This indicates that, at equivalent proportions of their respective liquefaction processes, the pore pressure ratio accumulates more slowly under compression-state consolidation than under extension-state consolidation. As the specimens approach liquefaction ($N_c/N_L > 0.8$), however, the differences diminish as all three curves converge toward $r_{u} = 0.95$ with increasing oscillation, reflecting the progressive loss of effective stress common to all states at liquefaction.

Fig. 4.8(b) shows the corresponding cumulative shear work evolution. The $W_{s}$–$N_c/N_L$ curves exhibit a similar three-stage behavior: the three states depart from the same origin, develop discernible differences during the intermediate stage—the $K_{0}$=0.5 specimen accumulates slightly more energy per normalized cycle while the $K_{0}$=1.0 specimen accumulates the least—and then converge again as the specimens approach liquefaction, indicating that the energy accumulation process follows a common progression toward liquefaction regardless of initial stress anisotropy.

It is worth noting that the ordering of $W_{s}$ in the normalized plot (Fig. 4.8(b))—$K_{0}$=0.5 highest, $K_{0}$=2.0 intermediate, $K_{0}$=1.0 lowest—does not directly reflect the per-cycle energy input rate, because the normalization compresses different numbers of actual cycles onto the same horizontal axis. Fig. 4.8(c) presents the cumulative shear work against the actual number of cycles $N_c$, where the ordering reverses to match the liquefaction resistance: the $K_{0}$=2.0 specimen accumulates energy fastest, the $K_{0}$=1.0 specimen is intermediate, and the $K_{0}$=0.5 specimen is the slowest. This is consistent with expectations, as lower liquefaction resistance corresponds to faster energy accumulation per cycle.

Inspired by the energy-based approach of Towhata and Ishihara (1985), Fig. 4.8(d) examines whether the $r_{u}$–$W_{s}$ relationship can explain the observed differences in liquefaction resistance among the three $K_{0}$ states. The $K_{0}$=0.5 specimen exhibits a distinctly lower $r_{u}$ at any given $W_{s}$ compared to the other two states, which partially explains its higher liquefaction resistance—the compression-state fabric requires more energy input to generate the same level of pore pressure ratio. However, when comparing $K_{0}$=1.0 and $K_{0}$=2.0, no clear distinction emerges in the $r_{u}$–$W_{s}$ relationship despite their different liquefaction resistance (Fig. 4.7), limiting the explanatory power of this energy-based approach. It should be noted that the comparison has inherent limitations: Towhata and Ishihara (1985) demonstrated a unique $W_{s}$–$u$ relationship for specimens under the same isotropic initial consolidation state but subjected to different shear stress paths, whereas the present study compares specimens with different initial stress anisotropies under the same loading path. Moreover, the quantity compared here is $r_{u}$ (EPWP normalized by the initial lateral stress) rather than the absolute pore water pressure $u$, and the different initial stress states result in different normalization bases. These factors suggest that the energy-based interpretation alone is insufficient to fully account for the $K_0$ effect on liquefaction resistance.

#### Shear wave velocity evolution

The inability of the energy-based approach to distinguish between $K_0$=1.0 and $K_0$=2.0 suggests that the difference in liquefaction resistance between these two states arises not from how much energy is needed to generate pore pressure, but from how rapidly energy is input per cycle. Since the per-cycle energy input is governed by strain amplitude, which in turn depends on shear stiffness, this motivates an examination of the relationship between shear stiffness evolution and liquefaction resistance (Xu et al., 2015). The shear modulus $G$ is defined as the ratio of shear stress increment to shear strain increment, and Eq. (4-9) describes the shear wave velocity $V_{s}$ in terms of the shear modulus $G$ and the saturated density $\rho_{sat}$ (Tokimatsu and Uchida, 1990; Chen et al., 2005).

$V_{s} = \sqrt{\frac{G}{\rho_{sat}}}$ (4-9)

![](thesis/assets/images/shear_wave_velocity.png)

Fig. 4.9. Evolution of shear wave velocity during cyclic shear for different $K_{0}$ values, showing loading and unloading stiffness separately (CSR=0.200)

Fig. 4.9 presents the evolution of shear wave velocity $V_s$ during undrained cyclic shear, with loading and unloading phases plotted separately. The loading $V_s$ is calculated from the first and third quarter-periods of each cycle, while the unloading $V_s$ is calculated from the second and fourth quarter-periods. The inset shows the initial shear wave velocity $V_{s0}$ for both loading and unloading conditions. For all three $K_0$ states, unloading stiffness is consistently higher than loading stiffness, reflecting the typical hysteretic behavior of granular materials under cyclic loading.

The $K_0$=1.0 specimen exhibits the highest initial $V_s$, with values of approximately 195 m/s (loading) and 210 m/s (unloading). The $K_0$=0.5 and $K_0$=2.0 specimens show lower and comparable initial values, with loading $V_s$ around 176-180 m/s. However, the subsequent stiffness degradation differs markedly among the three states. During the early stage ($N_c < 15$), $K_0$=1.0 maintains the highest stiffness. As cycling progresses, the degradation rates diverge: the $K_0$=1.0 and $K_0$=2.0 specimens degrade relatively rapidly, while the $K_0$=0.5 specimen degrades much more slowly. By approximately 20 cycles, the $K_0$=0.5 specimen surpasses $K_0$=1.0 in loading $V_s$, and by 28 cycles, the contrast becomes striking—the $K_0$=0.5 specimen retains a loading $V_s$ of approximately 144 m/s, compared to 108 m/s for $K_0$=1.0 and 62 m/s for $K_0$=2.0. These different degradation rates directly explain the energy accumulation ordering observed in Fig. 4.8(c): the $K_0$=0.5 specimen, whose stiffness degrades most slowly, develops the smallest strain amplitude per cycle and thus accumulates energy most gradually; the $K_0$=2.0 specimen, with the fastest stiffness degradation, develops the largest strain amplitude per cycle and accumulates energy most rapidly; and the $K_0$=1.0 specimen exhibits intermediate behavior in both stiffness degradation and energy accumulation.

Compared with the energy-based approach, which cannot distinguish between $K_0$=1.0 and $K_0$=2.0 (Fig. 4.8(d)), the stiffness degradation rate provides a unified macroscopic explanation for the liquefaction resistance ordering across all three $K_0$ states. Notably, the initial stiffness alone cannot predict these outcomes—the $K_0$=0.5 and $K_0$=2.0 specimens share comparable initial $V_s$ yet exhibit markedly different degradation trajectories. It is the rate of stiffness degradation during cyclic loading, rather than the initial stiffness, that ultimately governs the energy accumulation behavior and liquefaction resistance.

While stiffness degradation provides a consistent macroscopic explanation, it does not reveal why different $K_0$ states exhibit different degradation rates. These macroscopic observations point to fundamental differences in the underlying particle-scale fabric structure. To elucidate the microscopic mechanisms, the following sections examine the evolution of coordination number, fabric anisotropy, and contact density under different $K_0$ states.

### Microscopic interpretation

#### Evolution of coordination number

The coordination number quantifies the average number of contacts per particle, serving as a scalar measure of fabric compactness in granular materials (Oda, 1977; Shire and O'Sullivan, 2012; Fei and Narsilio, 2020). To focus on load-bearing particles, the mechanical coordination number $Z_m$ excludes "floaters"—particles with fewer than two contacts that cannot stably transmit interparticle forces (Thornton, 2000; Hu et al., 2023):

$Z_{m} = \frac{2N_{c} - N_{1}}{N_{p} - N_{1} - N_{0}}$ (4-10)

where $N_c$ is the total number of interparticle contacts, $N_p$ is the total number of particles, and $N_1$ and $N_0$ are the numbers of particles with one and zero contacts, respectively.

![](thesis/assets/images/CoordNum.png)

Fig. 4.10. Mechanical coordination number evolution in cyclic shear and relationship between cyclic number required for liquefaction and initial mechanical coordination number (CSR=0.200)

Figure 4.10 shows the evolution of $Z_{m}$ under different initial $K_{0}$ states during cyclic shear. The initial mechanical coordination number $Z_{m0}$ varies with stress anisotropy: the isotropically consolidated specimen ($K_0$=1.0) exhibits the highest $Z_{m0}$ of approximately 4.98, while the anisotropically consolidated specimens ($K_0$=0.5 and $K_0$=2.0) show lower values of 4.89 and 4.88, respectively. This difference in $Z_{m0}$ may contribute to the higher initial shear stiffness observed in the $K_0$=1.0 specimen (Fig. 4.9), as more interparticle contacts generally lead to a stiffer fabric structure.

As cyclic loading progressed, $Z_{m}$ decreased gradually during the early stage ($N_c/N_L < 0.8$), followed by an accelerated decline as the specimen approached liquefaction. This reduction in $Z_{m}$ reflects the progressive loss of interparticle contacts and fabric integrity. Liquefaction was triggered when $Z_{m}$ dropped to approximately 4.0. Regardless of the initial $K_{0}$, the post-liquefaction $Z_{m}$ fluctuates around similar values, suggesting that the initial stress anisotropies have minimal influence on the post-liquefaction fabric structure.

The inset in Fig. 4.10 shows the relationship between $Z_{m0}$ and liquefaction resistance $N_L$. While the comparison between $K_0$=1.0 and $K_0$=2.0 shows that higher $Z_{m0}$ corresponds to slightly higher liquefaction resistance (Fig. 4.7), the comparison between $K_0$=0.5 and $K_0$=1.0 reveals a different pattern: despite having lower $Z_{m0}$, the $K_0$=0.5 specimen exhibits considerably higher liquefaction resistance. Moreover, although $K_0$=0.5 and $K_0$=2.0 have similar $Z_{m0}$ values, they exhibit markedly different liquefaction resistance. These observations suggest that coordination number alone cannot fully account for liquefaction resistance, and that the direction of stress anisotropy—compression versus extension—may influence fabric structure in ways that affect liquefaction behavior.

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

Fig. 4.11. Evolution of fabric anisotropy indicator $\alpha$ during cyclic shear for different $K_{0}$ values (CSR=0.200)

Fig. 4.11 presents the evolution of fabric anisotropy indicator $\alpha$ during undrained cyclic shear. The inset shows the initial fabric anisotropy $\alpha_0$ for different $K_0$ states. The $K_0$=0.5 specimen exhibits positive $\alpha_0$ (approximately 0.07), indicating contact normals concentrated in the axial direction. The $K_0$=1.0 specimen shows $\alpha_0$ close to zero (approximately 0.02), reflecting a nearly isotropic fabric. The $K_0$=2.0 specimen exhibits negative $\alpha_0$ (approximately -0.05), indicating contact normals concentrated in the horizontal direction. During the early stages of cyclic loading ($N_c/N_L < 0.8$), $\alpha$ remains relatively stable for all three $K_0$ states. As the specimens approach liquefaction, $\alpha$ begins to fluctuate significantly and converge toward zero, indicating that the directional fabric anisotropy diminishes as the fabric structure degrades.

While the fabric anisotropy indicator $\alpha$ provides a scalar measure of directional bias, the morphological basis for the sign of $\alpha_0$ can be visualized through contact density distributions. To simultaneously capture changes in both direction and quantity of contact normals during cyclic shear, contact density is used for visualization. The contact density (Han et al., 2023) describes the average number of contacts per unit surface area for a particle with normalized radius, as shown in Eq. (4-15):

$\rho_{c}\left( \theta_{z},\ \phi_{cir} \right) = \frac{2N_{\theta_{z},\ \ \phi_{cir}}|n_{c} \in \left( \theta_{z},\theta_{z} + \Delta\theta_{z} \right) \cap (\phi_{cir},\ \phi_{cir} + \Delta\phi_{cir})}{N_{p}\int_{\phi_{cir}}^{\phi_{cir} + \Delta\phi_{cir}}{\sin\left( \phi_{cir} \right)d\phi_{cir}}\int_{\theta_{z}}^{\theta_{z} + \Delta\theta_{z}}{d\theta_{z}}}$ (4-15)

Here, $\rho_{c}$ represents the contact density, $\theta_{z}$ and $\phi_{cir}$ indicate the polar and azimuthal angles in the spherical polar coordinate system, respectively. $N_{\theta_{z},\ \ \phi_{cir}}$ indicates the number of contacts with normals within the specified angular range. $N_{p}$ and the subsequent integral denote the total number of particles and the corresponding surface area on the unit sphere, respectively. This method effectively evaluates contact orientation during undrained cyclic shear and accommodates granular systems with various particle numbers.

Fig. 4.12 presents the evolution of contact density during the liquefaction process for $K_0$=0.5 and $K_0$=2.0 specimens. At the initial state, the $K_0$=0.5 specimen exhibits an axially-extended distribution with higher density (orange/red) at the poles and lower density (green) around the equator, corresponding to the positive $\alpha_0$ value. In contrast, the $K_0$=2.0 specimen displays a dimpled sphere distribution with lower contact density at the poles and higher density around the equator, corresponding to the negative $\alpha_0$ value. These distinct morphologies arise from the stress-induced fabric rearrangement during anisotropic consolidation: contacts tend to align perpendicular to the maximum principal stress direction.

As cyclic shear progresses, the contact density distributions gradually evolve. During the intermediate stage, the overall contact density decreases notably while the morphological characteristics of the initial distribution are largely preserved. As the specimens approach liquefaction, the contact density further diminishes and the direction of maximum contact density varies following the rotating principal stress axis. In the post-liquefaction state, the distinct initial morphologies converge toward similar patterns—both specimens exhibit an inclined distribution aligned with the rotated principal stress direction, rather than the original axial or horizontal orientations. This convergence is consistent with the observed convergence of $\alpha$, $V_s$, and $Z_m$ as specimens approach liquefaction.

|           |                     $N/N_L$=0.00                     |                      $N/N_L$≈0.61                      |                      $N/N_L$≈1.05                      |                      $N/N_L$≈1.07                      |
| :-------: | :--------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: |
| $K_0$=0.5 | ![](thesis/assets/media/contact_density_k050_t0.jpg) | ![](thesis/assets/media/contact_density_k050_t302.jpg) | ![](thesis/assets/media/contact_density_k050_t523.jpg) | ![](thesis/assets/media/contact_density_k050_t529.jpg) |
| $K_0$=2.0 | ![](thesis/assets/media/contact_density_k200_t0.jpg) | ![](thesis/assets/media/contact_density_k200_t226.jpg) | ![](thesis/assets/media/contact_density_k200_t379.jpg) | ![](thesis/assets/media/contact_density_k200_t386.jpg) |
|           |                                                      |                                                        |                                                        |                                                        |

Fig. 4.12. Evolution of contact density distribution during the liquefaction process for $K_0$=0.5 ($N_L$=39.5) and $K_0$=2.0 ($N_L$=29.5) specimens (CSR=0.200)

#### Interparticle contact force and displacement

The initial distribution of contact forces for different $K_0$ states was presented in Fig. 4.3, where the contact forces align with the direction of the maximum principal stress: axially for $K_0$=0.5 and horizontally for $K_0$=2.0. Fig. 4.13 presents the evolution of contact force chains (left half, colored by force magnitude) and particle displacement fields (right half, colored by displacement magnitude) during the liquefaction process for both $K_0$ states.

At the initial state, the force chains exhibit distinct patterns corresponding to the initial stress anisotropy. For $K_0$=0.5, the contact forces are predominantly aligned in the axial direction, while for $K_0$=2.0, they are concentrated in the horizontal direction. As cyclic loading progresses, the number of interparticle contacts gradually decreases and the average contact force magnitude diminishes. The amplitude of particle displacement also increases with each loading cycle, reflecting the progressive degradation of the fabric structure.

As the specimens approach liquefaction, the force chains become increasingly sparse while the contact forces reorient to align with the rotated principal stress direction. In the post-liquefaction state, regardless of the initial $K_0$ value, the contact force distributions converge toward similar patterns—forces no longer align with the initial axial or horizontal directions but concentrate along the rotated principal stress axis. This convergence is consistent with the observed convergence of contact density, $\alpha$, $V_s$, and $Z_m$ as specimens approach liquefaction. From a microscopic viewpoint, liquefaction occurs because cyclic loading induces periodic reorganization of interparticle contacts, with the number of contacts progressively decreasing. This gradual loss of contacts reduces the ability of the particle skeleton to transfer external forces. Furthermore, the convergence of post-liquefaction contact density distributions toward similar patterns provides microscopic evidence supporting the uniqueness of the critical state stress ratio. It should be noted that the post-liquefaction state observed here does not constitute the critical state in a strict sense, as the critical state requires sustained large deformation at the void ratio and effective stress corresponding to the critical state line. Nevertheless, the observed convergence of fabric structure regardless of initial $K_0$ suggests that shear loading drives granular assemblies toward a common fabric configuration, which underlies the uniqueness of the critical state stress ratio.

|           | $N/N_L$=0.00 | $N/N_L$≈0.61 | $N/N_L$≈1.05 | $N/N_L$≈1.07 |
| :-------: | :--------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: |
| $K_0$=0.5 | ![](thesis/assets/media/force_disp_k050_t0.jpg) | ![](thesis/assets/media/force_disp_k050_t302.jpg) | ![](thesis/assets/media/force_disp_k050_t523.jpg) | ![](thesis/assets/media/force_disp_k050_t529.jpg) |
| $K_0$=2.0 | ![](thesis/assets/media/force_disp_k200_t0.jpg) | ![](thesis/assets/media/force_disp_k200_t226.jpg) | ![](thesis/assets/media/force_disp_k200_t379.jpg) | ![](thesis/assets/media/force_disp_k200_t386.jpg) |

Fig. 4.13. Evolution of contact force chains (left half) and particle displacement (right half) during the liquefaction process for $K_0$=0.5 ($N_L$=39.5) and $K_0$=2.0 ($N_L$=29.5) specimens (CSR=0.200)

#### Effect of fabric on liquefaction resistance

The preceding analyses based on the primary set of three $K_0$ cases demonstrate that $Z_{m0}$ and $\alpha$ capture different aspects of the fabric state, but three data points at a single density provide limited statistical power for separating their respective contributions. To address this, the expanded simulation set described in the specimen preparation section is now examined: two relative densities ($D_r \approx 90\%$ and $75\%$) combined with five $K_0$ values (0.5, 0.67, 1.0, 1.5, 2.0) at CSR=0.300, yielding ten cases. The initial coordination number $Z_{m0}$ and fabric anisotropy indicator $\alpha_0$ are extracted for each of the ten specimens, and their relationships with the number of cycles to liquefaction $N_L$ are plotted in Fig. 4.14. Circular and square markers distinguish the two relative densities.

The most immediate observation from Fig. 4.14(a) is that $D_r \approx 90\%$ specimens consistently exhibit higher $N_L$ than $D_r \approx 75\%$ specimens across all five $K_0$ states. Correspondingly, $Z_{m0}$ is systematically higher for $D_r \approx 90\%$ specimens (4.89–4.98) than for $D_r \approx 75\%$ specimens (4.77–4.88). This is consistent with the well-established understanding that denser packings develop more inter-particle contacts and thus greater liquefaction resistance. The clear separation of the two density groups along the $Z_{m0}$ axis confirms that the initial coordination number is an important microscopic indicator reflecting the macroscopic influence of relative density on liquefaction resistance.

However, $Z_{m0}$ alone does not fully explain the observed trends. Within each density group, $Z_{m0}$ shows no monotonic correlation with $N_L$. For instance, among $D_r \approx 90\%$ specimens, $K_0$=0.5 exhibits the highest $N_L$ but not the highest $Z_{m0}$, while $K_0$=2.0 has a comparable $Z_{m0}$ to $K_0$=0.5 yet demonstrates considerably lower $N_L$. A similar pattern is observed for $D_r \approx 75\%$ specimens, where $K_0$=0.5 and $K_0$=2.0 share nearly identical $Z_{m0}$ values but differ markedly in $N_L$. This is consistent with the earlier observation from Fig. 4.10, where the inset plot of $Z_{m0}$ versus $N_L$ for the original three $K_0$ states already hinted that coordination number cannot fully account for the differences in liquefaction resistance caused by stress anisotropy. With five $K_0$ values and two relative densities, this insufficiency becomes even more evident.

The fabric anisotropy indicator $\alpha_0$ resolves this gap. As shown in Fig. 4.14(b), $\alpha_0$ exhibits a clear positive correlation with $N_L$ across both relative densities. Specimens consolidated under compression states ($K_0 < 1.0$) develop larger $\alpha_0$ values and demonstrate higher $N_L$, while those under extension states ($K_0 > 1.0$) develop smaller $\alpha_0$ values and generally exhibit lower $N_L$. A minor exception is observed for the $D_r \approx 75\%$ specimen at $K_0$=2.0, which shows a slightly higher $N_L$ than $K_0$=1.5; however, the difference is less than one loading cycle and falls within the range of statistical fluctuation inherent to DEM simulations. The overall trend remains clear: the two density groups follow a similar pattern along the $\alpha_0$ axis, indicating that the influence of fabric anisotropy on liquefaction resistance is consistent regardless of packing density.

The three-dimensional view of $Z_{m0}$–$\alpha_0$–$N_L$ (Fig. 4.15) synthesizes these observations. The ten data points form two distinct clusters separated primarily along the $Z_{m0}$ axis, while within each cluster $N_L$ varies systematically with $\alpha_0$. Both microscopic parameters contribute to liquefaction resistance, albeit along different dimensions: $Z_{m0}$ characterizes the overall contact density related to packing state, accounting for the inter-group separation between the two relative densities, whereas $\alpha_0$ captures the directional bias of the contact network induced by anisotropic consolidation, accounting for the intra-group variation among different $K_0$ states.

![](thesis/assets/media/fabric_liq_2d.png)

Fig. 4.14. Relationship between initial microscopic fabric parameters and liquefaction resistance $N_L$ for five $K_0$ states at two relative densities (CSR=0.300): (a) $Z_{m0}$ vs. $N_L$; (b) $\alpha_0$ vs. $N_L$. Labels indicate $K_0$ values.

![](thesis/assets/media/fabric_liq_3d.png)

Fig. 4.15. Combined effect of initial coordination number $Z_{m0}$ and fabric anisotropy indicator $\alpha_0$ on liquefaction resistance $N_L$ in three-dimensional space (CSR=0.300). Labels indicate $K_0$ values.

It should be noted, however, that $Z_{m0}$ and $\alpha_0$ do not fully determine liquefaction resistance. A cross-group comparison highlights the significant role of macroscopic relative density: the $D_r \approx 90\%$ specimen at $K_0$=2.0 ($Z_{m0}$=4.885, $\alpha_0$=-0.046) and the $D_r \approx 75\%$ specimen at $K_0$=1.0 ($Z_{m0}$=4.880, $\alpha_0$=+0.022) share nearly identical $Z_{m0}$ values, while the former exhibits a considerably more negative $\alpha_0$. If liquefaction resistance were solely determined by these two microscopic parameters, the $D_r \approx 90\%$/$K_0$=2.0 specimen should exhibit lower $N_L$. In reality, however, its $N_L$ (8.5) is nearly double that of the $D_r \approx 75\%$/$K_0$=1.0 specimen (4.5). This indicates that relative density influences liquefaction resistance through additional mechanisms beyond what $Z_{m0}$ and $\alpha_0$ can capture—such as particle interlocking, force chain stability, and the distribution of contact forces—that collectively render the denser packing more resistant to cyclic loading regardless of the directional fabric bias.

The physical mechanism underlying the $\alpha_0$ effect can be interpreted through the orientation of contact normals relative to the shear direction. For compression states ($K_0 < 1.0$), the axially-concentrated contact normal distribution (positive $\alpha_0$) means that a greater proportion of contacts are oriented perpendicular to the horizontally applied cyclic shear. This orientation is hypothesized to enhance the stability of individual contacts against shear-induced sliding and detachment, thereby maintaining more robust force chains and slowing fabric degradation during cyclic loading. This is supported by the observation that the $K_0$=0.5 specimen requires substantially more shear work than the $K_0$=1.0 and $K_0$=2.0 specimens to reach the same $r_u$ level (Fig. 4.8(d)), despite exhibiting comparable initial shear stiffness to the $K_0$=2.0 specimen (Fig. 4.9). Conversely, for extension states ($K_0 > 1.0$), the horizontally-concentrated contact normals (smaller $\alpha_0$) are more aligned with the shear direction, rendering the contacts more susceptible to sliding and the force chains more prone to collapse under cyclic loading, which accelerates fabric degradation and pore pressure accumulation.

It should be recognized, however, that granular soils are complex systems in which liquefaction resistance emerges from the interplay of both microscopic and macroscopic factors. As demonstrated by the cross-group comparison above, macroscopic relative density exerts a strong influence on liquefaction resistance that cannot be fully captured by $Z_{m0}$ and $\alpha_0$ alone. A comprehensive understanding of liquefaction resistance therefore requires integrating macroscopic characterization (relative density, stress state) with microscopic fabric analysis (coordination number, fabric anisotropy), rather than relying on either perspective in isolation.

## Summary

This study utilized the DEM with a combined servo mechanism to simulate undrained cyclic torsional shear tests in hollow cylinder apparatus (HCA), investigating the impact of initial stress anisotropy on the liquefaction resistance of sand soils. The DEM micro-parameters were calibrated and validated against undrained monotonic and cyclic HCA test data for dense Toyoura sand, reproducing the characteristic dilative response, strain-hardening behavior, and CSR-$N_L$ liquefaction resistance relationship. Specimens were prepared via an IC-AC stress path (isotropic consolidation to $p'$=10 kPa, then linear anisotropic consolidation to $p'$=100 kPa), which produced minimal void ratio variation ($\Delta e < 0.001$) between $K_0$ states, enabling isolation of fabric effects from packing density effects. Macroscopic responses including liquefaction resistance curves, cumulative shear work, and shear wave velocity were investigated for three representative $K_0$ values (0.5, 1.0, 2.0) across multiple CSR levels at $D_r \approx 90\%$. To further disentangle the microscopic factors, additional simulations at $K_0$=0.67 and 1.5, together with a second relative density ($D_r \approx 75\%$), were conducted at CSR=0.300. The findings are summarized as follows:

(1) The CSR-$N_L$ liquefaction resistance curves demonstrate a clear directional dependency on initial stress anisotropy: the compression state ($K_0$=0.5) exhibits the highest resistance, the isotropic state ($K_0$=1.0) intermediate resistance, and the extension state ($K_0$=2.0) the lowest resistance, for all CSR levels tested. Beyond the macroscopic observation of $K_0$-dependent liquefaction resistance, this study provides a microscopic perspective: the differences in liquefaction resistance among $K_0$ states are associated with distinct contact fabric structures induced by anisotropic consolidation.

(2) The normalized cumulative shear work $W_s$ evolves nearly identically for all three $K_0$ states when normalized by $N_L$, confirming the $K_0$-independence of the normalized energy accumulation pattern. However, the compression state ($K_0$=0.5) exhibits greater resistance to pore pressure buildup per unit energy input compared to the isotropic and extension states. Meanwhile, the isotropic state ($K_0$=1.0) maintains the highest shear wave velocity $V_s$ throughout cyclic shear, resulting in smaller strain amplitude per cycle and thus requiring more cycles than the extension state ($K_0$=2.0) despite comparable energy requirements. As specimens approach liquefaction, the $V_s$ values for all $K_0$ states converge, indicating that the influence of initial stress anisotropy on shear stiffness diminishes as the fabric structure progressively degrades.

(3) The initial mechanical coordination number $Z_{m0}$ is systematically higher for $D_r \approx 90\%$ specimens (4.89–4.98) than for $D_r \approx 75\%$ specimens (4.77–4.88), corresponding to their higher $N_L$ (8.5–11.0 vs. 4.0–5.5). This confirms that $Z_{m0}$ reflects the effect of packing compactness on liquefaction resistance. However, within each density group, $Z_{m0}$ shows no monotonic correlation with $N_L$—for example, specimens with $K_0$=0.5 and $K_0$=2.0 share comparable $Z_{m0}$ yet exhibit markedly different $N_L$—indicating that $Z_{m0}$ alone cannot account for the influence of stress anisotropy on liquefaction resistance.

(4) The initial fabric anisotropy indicator $\alpha_0$ resolves the gap left by $Z_{m0}$, exhibiting a clear positive correlation with liquefaction resistance across both relative densities. Specimens with higher $\alpha_0$ (axially-concentrated contacts in the compression state) generally exhibit greater liquefaction resistance than those with lower $\alpha_0$ (horizontally-concentrated contacts in the extension state). Contact density distributions provide morphological evidence for this correlation: the $K_0$=0.5 specimen exhibits an axially-extended distribution with higher density at the poles, while the $K_0$=2.0 specimen shows a dimpled sphere distribution with higher density around the equator. The axially-concentrated contact normals are oriented perpendicular to the horizontally applied cyclic shear, which is hypothesized to enhance the stability of individual contacts against shear-induced sliding, thereby maintaining more robust force chains and sustaining higher macroscopic resistance to pore pressure buildup. Conversely, in the extension state, the horizontally-concentrated distribution means that fewer contact normals are oriented perpendicular to the shear direction, reducing the number of contacts that can effectively resist shear-induced sliding and rendering force chains more prone to collapse.

(5) Both $Z_{m0}$ and $\alpha_0$ contribute to liquefaction resistance, albeit along different dimensions. In the three-dimensional space of $Z_{m0}$–$\alpha_0$–$N_L$, data from the two relative densities form two distinct clusters separated primarily along the $Z_{m0}$ axis, while within each cluster $N_L$ varies systematically with $\alpha_0$. However, a cross-group comparison reveals that specimens with nearly identical $Z_{m0}$ and less favorable $\alpha_0$ can still exhibit substantially higher $N_L$ when they possess higher relative density, indicating that macroscopic relative density influences liquefaction resistance through mechanisms beyond what $Z_{m0}$ and $\alpha_0$ alone can capture. A comprehensive assessment of liquefaction resistance therefore requires integrating both macroscopic and microscopic perspectives.

(6) Regardless of the initial $K_0$ state, the microscopic indicators—$Z_m$, $\alpha$, and contact density distribution—converge toward similar values as specimens approach and enter the post-liquefaction state. The contact force chains, initially aligned with the direction of the maximum principal stress corresponding to each $K_0$ state, reorient to align with the rotated principal stress axis in the post-liquefaction state. This convergence of fabric structure provides microscopic evidence supporting the uniqueness of the critical state stress ratio.
