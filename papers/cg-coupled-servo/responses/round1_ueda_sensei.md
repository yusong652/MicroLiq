# Round 1 — Response to Ueda sensei

## Q1: Servo mechanism — where are the results demonstrating its advantages?

**Response:** The introduction now explicitly identifies three refinements over the servo formulation of Ma et al. (2024): (a) effective pressure differences — matching the physically independent control channels of a laboratory HCA — are adopted as servo targets, (b) the constant-volume constraint is used to eliminate $dR/dt$, reducing the system to two kinematic variables ($dr/dt$ and $dH/dt$), and (c) the resulting $2\times 2$ coupled stiffness matrix is inverted analytically, yielding exact servo coefficients at every timestep. Analytical correctness of the servo coefficients is a prerequisite for numerical accuracy and stability — this itself constitutes a significant contribution. Earlier independent-gain formulations are inherently approximate because they do not account for the cross-coupling between boundary movements; the closed-form coupled solution derived here eliminates this approximation, ensuring mathematically exact servo coefficients at every timestep.

The monotonic shear calibration (Section 2.4) provides direct experimental validation: the full coupled servo operates in stress-control mode, simultaneously adjusting both $dr/dt$ and $dH/dt$ to maintain $\sigma'_z = \sigma'_r$ throughout shearing. The accurate reproduction of the experimental stress path and stress–strain relationship of Nakata et al. (1998), together with the subsequent agreement with cyclic liquefaction resistance data of Ishihara (1985) under constant-height mode, confirms that the coupled servo maintains the prescribed boundary conditions across both operating modes.

**Changes:** Lines 5–10 (Highlights), Lines 22–27 (Abstract), Lines 92–108 (Introduction), Lines 169–185 (Section 2.3 opening)

---

## Q2: Multiple microscopic indicators used but overall conclusions not sufficiently clear

**Response:** The discussion has been restructured to build a single interpretive chain from macroscopic observations down to particle-scale mechanisms. (i) Section 3.2 now positions $V_s$ not as a standalone explanation but as a bridge that links the per-cycle energy accumulation rate differences (Section 3.1) to the evolving fabric examined in Section 3.3. (ii) Section 3.3 clarifies the complementary roles of the two key microscopic descriptors: $Z_{m0}$ is strongly coupled to relative density and governs the baseline resistance level across density groups, while $\alpha_0$ captures the directional fabric effect that differentiates $K_0$ states within a given density. (iii) A new schematic figure (Fig. 15) illustrates the physical mechanism: only contacts with normals in the $z$ and $\theta$ directions resist the applied torsional shear, and compression-state consolidation concentrates a larger fraction of contacts onto this plane. The conclusions have been rewritten to reflect this unified narrative, presenting each indicator's role in the interpretive chain rather than listing them as independent findings.

**Changes:** Lines 365–386 (Section 3.2 reframing), Lines 433–460 (Section 3.3), Fig. 15 (new), Lines 510–517 (Conclusions item 4)

---

## Q3: Abstract — "disentangle packing compactness from directional fabric effects" hard to understand

**Response:** Replaced with simpler wording: "separate the respective roles of relative density and stress anisotropy."

**Changes:** Line 36

---

## Q4: Abstract — z–θ plane not self-evident

**Response:** Added parenthetical clarification: "the plane on which the torsional shear stress acts."

**Changes:** Line 42

---

## Q5: Section 2.2 overlaps with introduction; Fig. 2 clarity

**Response:** The introduction paragraph has been simplified to a high-level roadmap (two-stage investigation) without repeating specific $K_0$ values, density numbers, or CSR levels that now appear only in Section 2.2. Section 2.2 has been expanded with a description of the AC process (ten equally spaced target stress states from 10 to 100 kPa) and an explanation of the minor stress fluctuations visible in Fig. 2(a). Fig. 2(a) and (b) have been updated: duplicated x-axis label fixed, $K_0 = 1.0$ markers changed from filled to open, legend simplified.

**Changes:** Lines 117–122 (Introduction), Lines 150–168 (Section 2.2), Fig. 2

---

## Q5b: Fig. 3 not referenced in the text

**Response:** A cross-reference to Fig. 3 has been added at the end of the anisotropic consolidation paragraph in Section 2.2, noting the visual contrast in force-chain directionality among the three $K_0$ states.

**Changes:** Line 167 (Section 2.2)

---

## Q6: Eq. (2) — Is an explanation of the servo coefficient unnecessary?

**Response:** A functional explanation of $S_{cr}$ has been added after Eq. (2): it is the radial servo coefficient, derived from the aggregate contact stiffness at the cylindrical walls, that converts the pressure error into the wall velocity needed to eliminate it.

**Changes:** Lines 191–192 (physical explanation), Line 240 (Eq. 14, $S_{cr}$)

---

## Q7: Axial condition — What is the physical significance of taking the difference?

**Response:** The axial condition now states that laboratory HCA tests operate under either constant total axial stress or constant specimen height, and that reproducing the former requires controlling the difference between vertical and radial effective stresses. Two operating modes are explicitly listed: (i) stress-control mode (both $dr/dt$ and $dH/dt$ adjusted; used during AC and monotonic calibration), and (ii) displacement-control mode ($dH/dt = 0$; used for all cyclic shear simulations). This also addresses the concern that Eqs. (3)–(4) appear unused: stress-control mode activates the full coupled servo during monotonic shear.

**Changes:** Lines 193–205

---

## Q8: Torsional condition — also considered in Han et al. and Ma et al.?

**Response:** Added an opening sentence acknowledging that the torsional servo is independent of the radial–axial system and follows the same formulation adopted in Han et al. (2024) and Ma et al. (2024).

**Changes:** Lines 206–208

---

## Q9: Section 2.4 — monotonic shear involves principal stress rotation; not mentioned?

**Response:** Rather than adding a separate sentence about principal stress rotation (an inherent feature of torsional shear already discussed in the introduction), a parenthetical citation to Ma et al. (2024) has been added to the calibration sentence, acknowledging that they also calibrated against the same dataset.

**Changes:** Line 253

---

## Q10: r_u–W_s conclusion under strain-based criterion; total vs. plastic shear work?

**Response:** The $r_u$–$W_s$ relationship traces the co-evolution of two quantities throughout cyclic loading and does not depend on a specific liquefaction criterion. Adopting the strain-based criterion ($\gamma_{SA} = 2.5\%$) instead of the stress-based one ($r_u = 0.95$) increases $N_L$ by only one to two cycles at CSR = 0.200, which does not affect the conclusions. A confirming sentence has been added.

Regarding $W_s$: the definition computes total shear work input from boundary stress and strain rate, the same quantity proposed by Towhata and Ishihara (1985). A clarification has been added that the recoverable elastic strain energy becomes negligibly small relative to the cumulative total as loading progresses.

**Changes:** Lines 340–344 ($W_s$ definition), Lines 363–364 (strain-based criterion)

---

## Q11: V_s discussion — role relative to energy; stiffness vs. pore pressure

**Response:** The $V_s$ section has been reframed. The per-cycle energy accumulation rate is indeed linked to shear stiffness, as a softer specimen absorbs more irrecoverable work per cycle. However, stiffness is a material property that reflects the evolving state of the contact network, whereas energy is a cumulative output quantity. The revised text therefore positions $V_s$ as a bridge between the macroscopic energy picture (Section 3.1) and the particle-scale fabric analysis (Section 3.3).

**Changes:** Lines 365–370 (opening paragraph), Lines 381–386 (closing paragraph)

---

## Q12: Section 3.3 — does this suggest microscopic indicators are inadequate and macroscopic ones are preferable?

**Response:** The two descriptors play complementary roles: $Z_{m0}$ is strongly coupled to macroscopic relative density and governs the baseline resistance level across density groups, while $\alpha_0$ captures the directional fabric effect that differentiates $K_0$ states within a given density. The fabric tensor decomposition further confirms that $\alpha_0$ tracks the fraction of contacts on the $z$–$\theta$ shear plane that directly resist torsional shear. The revised text and conclusions now present $Z_{m0}$ and $\alpha_0$ as complementary microscopic characterizations rather than as indicators that fall short of macroscopic measures. The limitation (Section 3.4) has been reframed: the issue is that the strong coupling between $Z_{m0}$ and relative density prevents full isolation of each descriptor's independent contribution within the present dataset.

**Changes:** Lines 433–460 (Section 3.3), Lines 487–492 (Section 3.4), Lines 510–517 (Conclusions item 4)

---

## Q13: Sections 3.3–3.4 — can figures or illustrations enhance the clarity of the physical explanation?

**Response:** A new two-panel schematic figure (Fig. 15) has been added. Panel (a) shows a 3D cylindrical element with the $z$ and $\theta$ axes colored as torsion-resisting and the $r$ axis as mechanically neutral, conveying that only contacts with normals in the $z$ or $\theta$ directions resist torsional shear. Panel (b) plots the torsion-resisting fraction $1 - \Phi_{rr}$ for five $K_0$ states at two densities, clearly revealing the monotonic decrease with increasing $K_0$. A cross-reference has been added at the opening of the fabric tensor decomposition paragraph.

**Changes:** Fig. 15 (new), Lines 461–462 (cross-reference)

---

## Q14: Corresponding author

Corresponding author の件については、改めてご相談させてください。
