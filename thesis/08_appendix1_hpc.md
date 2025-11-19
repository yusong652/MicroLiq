---
title: "Appendix 1: Implementation Of High-Performance Computing In DEM"
tags: [thesis, appendix-1, HPC, GPU-computing, TaichiLang, neighbor-search]
aliases: [Appendix 1, HPC Implementation, TaichiDEM]
---

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

