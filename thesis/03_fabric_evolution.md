---
title: "Chapter 3: Fabric Evolution Under General Stress States"
tags: [thesis, chapter-3, fabric-evolution, true-triaxial, DEM, stress-states]
aliases: [Fabric Evolution, Chapter 3]
---

# Fabric Evolution under General Stress States

The fabric of granular geomaterials is related to properties such as shear strength, permeability, and liquefaction resistance. To evaluate the fabric evolution and behavior of geomaterials, a series of the true triaxial test simulations with flexible boundaries under general stress states in this study were performed using the three-dimensional discrete element method (DEM). First, the stress states at the axial strain of 20%, which indicates that the stress under the critical state conforms to the Matsuoka-Nakai criterion, were examined. Then the uniqueness of the coordination number and non-uniqueness of void ratio and invariant of anisotropic fabric tensor under the critical state were investigated based on the contact density, which indicates the relative number of contacts in different orientations. In particular, the contact density at the critical state under different mean effective principal stresses with its effects on the invariant of anisotropic fabric tensor were discussed. It was found that the contribution of the contact density to the fabric anisotropy decreased as the mean effective principal stress increased due to geometric limitations.

## Introduction 

To evaluate the failure criteria of the geostructures such as roads and embankments under the three-dimensional stress state, a three-principal stress test apparatus is required. Typical true triaxial apparatuses include all rigid types, all flexible types, and hybrid types. A device consisting of six plates was initially proposed by Pearce (1971) and Airey and Wood (1988). Ibsen and Praastrup (2022) improved it by modifying the boundary into six sliding rigid plates. However, even though the displacements on the boundary were uniform, friction-induced strain inhomogeneity is inevitable. Moreover, when the stress state was between the plane strain state and triaxial extension, the specimen was compressed from two directions, with stress concentration being reported in some studies (Shibata and Karube, 1965; Lo et al., 1994). An apparatus loaded with six flexible boundaries was proposed by Bell (1965) and improved by Ko and Scott (1967) and Sture and Desai (1979), with uniform pressure on the six surfaces of the cubic specimen being achieved. However, the strains at the corners between two adjacent flexible cells or bags might not be uniform (Yin et al., 2011). To overcome this disadvantage, the first true triaxial apparatus with hybrid (rigid and flexible) boundaries was developed by Green (1969, 1971). Further, Lade and Duncan (1973) modified the horizontal boundary to the composite material for compressibility. Nakai et al. (1986) improved the apparatus by applying major and minor principal stress using rigid plates and the intermediate principal stress using cell pressure to solve the interference and stress concentration problem. Nevertheless, friction between the rigid plate and specimen is inevitable in experiments, and achieving an ideal three-principal stress elemental test remains difficult.

On the other hand, the classical critical state theory proposed by Roscoe et al. (1963) describes a dynamic equilibrium state: the stress state is stable while the strain evolves under large deformation conditions. However, this theory is mainly based on axisymmetric triaxial compression experiments. Thus, the uniqueness of the stress ratio and void ratio along other stress paths remain of great interest. The critical state line (CSL) in the void ratio ($e$) -- mean effective stress ($p'$) space was considered unique and independent of the stress paths from the triaxial compression and extension tests performed by Been et al. (1991). On the other hand, Wanatowski and Chu (2007) conducted drained and undrained laboratory tests under triaxial and plane strain conditions. The results exhibited a clear dependence on the stress paths: although the CSL is independent of the drainage condition, it varies with the intermediate principal stress ratio 'b'. Moreover, the discrete element method (DEM) proposed by Cundall (1971), a Lagrangian method explicitly describing the motion of individual particles, has been extensively applied in geotechnical engineering analyses. Many true triaxial tests have utilized DEM to analyze the CSL along varying stress paths. For instance, granular assemblies were monotonically sheared with various constant 'b' values in drained and undrained conditions in the DEM simulation performed by Zhao and Guo (2013). The obtained results revealed the uniqueness of the CSL in the $e$ -- $p'$ space. Furthermore, simple shear states and triaxial states were compared using DEM by Nguyen et al. (2021), and it was found that the CSL of void ratio depends on the stress states. The dependency of the CSL of the void ratio and fabric anisotropy on the intermediate principal stress ratio under various stress states was also reported in the DEM studies by Huang et al (2014a). Although the uniqueness or nonuniqueness of CSL was concluded in the early studies, detailed interpretations and discussions based on the morphology of fabric in the granular system under general stress states remain to be provided. In addition, only the comparison between different 'b' values has been emphasized and highlighted. In contrast, the variation of fabric anisotropy under different mean effective stress p' needs to be clarified. On the other hand, most of the past studies involved only a type of boundary (periodic or rigid boundaries) (Chang et al., 2021). True triaxial tests with hybrid boundaries, such as the flexible membrane boundary are needed to be developed as well.

In this study, the difference in true triaxial tests with a flexible membrane in the intermediate principal stress direction and rigid plates in the major and minor principal stress directions is examined by the DEM simulations. The stress ratios and void ratios under the critical states are also presented and compared for different stress paths. Microscopic quantities, such as the coordination number ($Z$) and invariant of anisotropic fabric tensor under the critical state, are examined. Thereafter, the variation in those quantities with different stress paths and mean effective stress is interpreted by utilizing a newly proposed contact density method, which represents both contact orientation and $Z$ and refined the evaluation system for granular microstructures.

## Simulation modeling

### Contact model

The DEM simulations in this study were implemented using PFC3D (Itasca, 2005). The contact model in the DEM determines the interparticle relationship, such as the friction and contact force between particles. The contact models employed to represent cohesionless sands typically include linear models, in which the stiffness (Wei et al., 2022) or modulus (Zhao and Guo, 2013) is constant, and nonlinear models such as the Hertz-Mindlin model (Tsuji et al., 1992). The contact stiffness has a direct impact on the timestep. For instance, the study conducted by O\'Sullivan (2004) indicates that the critical timestep is proportional to the value of (*m*/*k*)^0.5^, where *m* is the mass of the particle at the end of the contact, and *k* denotes the stiffness of the contact. Thus, excessive stiffness increases the computational effort, but an appropriate contact stiffness guarantees the convergence and efficiency of the calculation. Table 2-1 and Fig 2.1 summarize the input parameters of a linear model applied in this study (Kim et al., 2012 & 2021).

![](thesis/assets/media/image12.png)

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

![](thesis/assets/media/image17.png)

Fig. 2.4. Specimen state after isotropic compression of p = 5.1 MPa

Subsequently, isotropic compression with gradually increasing confining stress was performed, during which three measurement ball function (Itasaca, 2005) with radii of 1.5 mm are positioned vertically inside the specimen to measure the void ratio. The measurement ball function is built into the program, which sets a spherical spatial domain for measurement and measures parameters such as void ratio, average stress, and coordination number for particles that exist within this domain. When measuring the average value of the void ratio in the domain, the obtained result can be regarded as the average void ratio at the center point of the domain. The stability of the stresses acting on the wall elements and the void ratio of the specimen served as the completion condition for each compression stage. The current compression stage was completed when stress and strain stabilized, and a quasi-static state was accordingly reproduced in the specimen. Figures 2.3 and 2.4 show the variation in the void ratio under isotropic compression and the specimen under a confining pressure of 5.1 MPa, respectively. Simulation by Cao et al. (2021) involved low confining pressures for consistency with laboratory tests. On the other hand, some simulations covered a wide range of confining pressures from tens kPa to tens MPa (ex., Huang et al., 2014a; Zhao and Guo, 2013). Moreover, the particle crushing was modeled by Zhu et al (2022) when the specimen was subjected to high confining pressure. Unlike these studies, this study aims to compare the mechanical behavior of theoretical spherical aggregates under a wide range of pressures. Thus, particle crushing is not considered. Isotropically compressed specimens under confining pressures of 0.7MPa, 1.4MPa, 1.9MPa, 2.6MPa, 3.7MPa, 5.1MPa, 7.0MPa, 9.7MPa, 13.5MPa, 18.7MPa, and 26.0MPa were selected for the subsequent shear tests under general stress states.

![](thesis/assets/media/image18.png)

Fig. 2.5. Loading paths in shear tests

### Shear process in the DEM simulation

During shearing, the Lode angle and the mean effective stress were maintained constant. Five loading paths corresponding to each mean effective stress state were considered: Lode angles of 60°, 75°, 90°, 105°, and 120° as shown in Fig. 2.5. Lode angle refers to the angle between the stress path and the axis of the principal stress in the stress state of a material. Lode angles of 60° and 120°indicate the triaxial extension and triaxial compression states, respectively. On the other hand, the stress path can also be described by using the intermediate principal stress ratio (*b* = (*σ~2~'*-*σ~3~'*)/(*σ~1~'*-σ~3~')), where *b*=0 for triaxial com-pression and *b*=1 for the triaxial extension. Typical boundaries in DEM triaxial tests include the nondeformable wall boundary (Zhao and Guo, 2013; Cao et al., 2021), the periodic boundary (Thornton, 2000; González-Montellano et al., 2011), and the membrane boundaries. Multiple membrane boundaries exist in DEM simulations. One of the membrane boundaries is implemented by applying additional force to the outmost particles (Cui et al., 2007; Cheung and O'Sullivan, 2008; O\'Sullivan and Cui, 2009). Another type of membrane boundary is modeled by assigning tensile and shear strength between the membrane particles (Kim and Park, 2020). Recently, a coupled FDM-DEM approach using the shell element was proposed to model the membrane boundary (Zhu et al., 2022). Although the wall boundary can effectively maintain the specimen symmetry under deformation, local deformation such as the shear band, which originates from irregular displacement on the deformable flexible boundary, is inhibited. In this study, the major and minor principal stresses were applied by wall element boundaries, and the membrane boundary with applied force was adopted in the intermediate principal stress direction, which is consistent with the apparatus developed by Nakai et al. (1986).

> ![](thesis/assets/media/image19.png)
>
> Fig. 2.6. Membrane zone detection

The method for identifying the membrane particles is similar to that proposed by Cui et al. (2007) and only differs in coordinate transformation because the specimen in previous studies was a cylinder, whereas the specimen in this study is a cuboid. The boundary in the direction of intermediate principal stress, which serves as the membrane, was determined using the following procedure. As illustrated in Fig. 2.6, a membrane zone with a thickness of three times the mean particle diameter was designated from the outmost particle in the intermediate principal stress direction. The particles in the membrane zone were further identified depending on whether they were prevented from contact with the outside. Each particle in the membrane zone had a corresponding cone with its vertex coinciding with the center of the particle, as shown in Fig. 2.7. If no other particle is detected inside this conical region, this particle is in direct contact with the outside and is, consequently, identified as a membrane particle.

> ![](thesis/assets/media/image20.png)
>
> Fig. 2.7. Membrane particle identification
>
> ![](thesis/assets/media/image21.png)
>
> Fig. 2.8. Specimen after Membrane particle identification

Figure 2.8 shows the specimen after membrane particle identification in the DEM simulation. The yellow particles in this figure denote the membrane particles directly subject to the intermediate principal stress. The boundary stress was subsequently applied to each membrane particle in the form of applied forces for the coordinate axis. To obtain the applied force corresponding to each membrane particle, a two-dimensional Voronoi tessellation based on the membrane particle positions was employed.

![](thesis/assets/media/image23.svg)

Fig. 2.9. Voronoi geometry corresponding Membrane particles

![](thesis/assets/media/image24.png)

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

![](thesis/assets/media/image31.png)

> \(a\) Rigid boundary

![](thesis/assets/media/image32.png)

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

> ![](thesis/assets/media/image40.png)

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

![](thesis/assets/media/image55.png)

Fig. 2.21. Unit sphere for contact classification

Figure 2.21 shows a unit sphere with a radius of 1.0 separated into grids every 10° of latitude and longitude for classifying contacts in different directions. The area and number of contacts located in one grid vary with latitudes and longitudes; therefore, contact density (*ρ~c~*) was applied to normalize and visualize the contact characteristics. A probability density function (*E*) was proposed by Rothenburg and Bathurst (1989), as given in Eq. (2-8), and 10° of δ*θ* and δ*ϕ* were applied in this study. Notably, the integral following the number of total contacts (*N~c~*) in the denominator in Eq. (2-8) is the area of each grid, and it differs from the original form given by Rothenburg and Bathurst (1989): it is in a three-dimensional case. In contrast to the contact probability density function ($E$), the contact density ($\rho_{c}$) is defined in Eq. (2-9), indicating that the number of contacts per unit area on the unit sphere for a single particle is the product of $E$ and 2$N_{c}$/$N_{p}$ ($Z$), where *N~c~* and *N~p~* denote the total number of contacts and particles in the granular material. It also differs from the form provided by Huang et al (2014a) because it is normalized by counting the total number of particles and is independent of the number of particles within the granular assemblage.

By modifying $E$ to $\rho_{c}$, both the anisotropies of contact distribution and the evolution of $Z$ induced by compactness or shear can be represented. For instance, in an undrained test, the $Z$ changes dramatically. However, although $E$, with its integral over the unit sphere surface is 1.0, is mathematically elegant, it can scarcely reflect the variation in isotropic quantities, such as $Z$. The other forms by Huang et al (2014a) are not able to evaluate different granular systems with various particle numbers. $\rho_{c}$ indicates the mathematic expectation of contact number in different directions per unit area for each particle. It represents the contact distribution characteristics and the trend of changes in the number of contacts and is independent of the number of particles.

The morphological evolution of contact density during the compression test under the mean effective stress of 5.1MPa is shown in Fig. 2.22. Here, Figures 2.22(a)\~(d) correspond to the axial strains of 0%, 2%, 5%, and 20%, respectively. The contact density distribution at the axial strain of 0% is almost a sphere with a mean density of approximately 0.3445, which indicates an isotropic state in the fabric. As the strain and stress develop, the contact density gradually evolves toward the direction of the major principal stress. At the axial strain of 2%, the morphology evolves into an ellipsoid with a mean density of 0.3940 and 0.2919 in the direction of *σ~1~'* (0^o^ \< *ϕ* \< 20^o^) and *σ~3~'/σ~2~'* (80^o^ \< *ϕ* \< 100^o^), respectively. This indicates a slight concentration of interparticle contacts in the direction of *σ~1~'* and fabric anisotropy. On the other hand, when the major principal strain exceeds 5%, the mean density in the direction of *σ~1~'* increases to 0.4143, and the mean density in the direction of *σ~3~'/σ~2~'* decreases to 0.2716. This indicates a more significant concentration of interparticle contacts. The contact density at the axial strain of 20% in the critical state exhibits the greatest fabric anisotropy: a mean density of 0.4009 in the direction of *σ~1~'* and 0.2385 in the direction of *σ~3~'/σ~2~'*. The mean contact density in the direction of *σ~1~'* under the critical state was slightly lower than that when

+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ![](thesis/assets/media/image56.png) | ![](thesis/assets/media/image57.png)     |
+:=================================================================================================================================:+:================================================================================================================================:+
| \(a\) ε~a~=0%                                                                                                                     | \(b\) ε~a~=2%                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ![](thesis/assets/media/image58.png) | ![](thesis/assets/media/image59.png) |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| \(c\) ε~a~=5%                                                                                                                     | \(d\) ε~a~=20%                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Fig. 2.22. Distribution of contact density (*ρ~c~*) at different axial strain in compression test: (a) ε~a~=0%, (b) ε~a~=2%, (c) ε~a~=5%, (d) ε~a~=20%                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

the axial strain *ε~1~* is 5%, however, the lower contact density in the direction of *σ~3~'/σ~2~'* resulted in greater fabric anisotropy in the critical state. Furthermore, at the critical state, the morphology of contact density was an elongated cylinder with a contracted body and *z*-axis oriented to the direction of major principal stress. Thus, the consistency of microstructure with macroscopic stress was verified in the triaxial compression test. The distribution morphology evolution of the contact density also implies a variation in the magnitude of *F~c~*. A greater difference between the anisotropic morphology and an isotropic sphere indicates a higher degree of anisotropy and a larger *F~c~*. Therefore, the evolution of the contact distribution morphologically estimates the gradual increase of *F~c~* in the triaxial compression test.

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![](thesis/assets/media/image60.png) | ![](thesis/assets/media/image61.png) |
+:=================================================================================================================================:+:=================================================================================================================================:+
| \(a\) *θ*=120°                                                                                                                    | \(b\) *θ*=90°                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![](thesis/assets/media/image62.png)      |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| \(c\) *θ*=60°                                                                                                                     |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Fig. 2.23. Comparison of the distribution of contact density (*ρ~c~*) for shear tests with different Lode angles at the critical state: (a) *θ*=120°, (b) *θ*=90°, (c) *θ*=60°                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The distributions of contact density for tests with Lode angles of 120°, 90°, and 60° are illustrated in Fig. 2.23, considering the uniqueness of $Z$ and nonuniqueness of *F~c~* and $e$ in tests with different Lode angles at the critical state under the same mean effective principal stress. In contrast to the compression test (*θ* = 120°), the morphology of contact density in the extension test (*θ* = 60°) was a dimpled flat pie with a concave oriented toward the direction of the minor principal stress. The contact density distribution for a Lode angle of 90° is an intermediate transition state. The contact density distribution microscopically reveals the intrinsic difference in critical states under different stress paths and is indicative of the anisotropy in the void ratio and fabric tensor. Although the CSL of $Z$ is uniquely presented, the contact anisotropy varies with the Lode angle, resulting in the *F~c~* and void ratio (*e*) of the triaxial extension being greater than that in the triaxial compression.

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![](thesis/assets/media/image63.png) | ![](thesis/assets/media/image60.png) |
+:=================================================================================================================================:+:=================================================================================================================================:+
| \(a\) *p'*= 1.9 MPa                                                                                                               | \(b\) *p'*= 5.1 MPa                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                   |                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ![](thesis/assets/media/image64.png)           |                                                                                                                                   |
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

