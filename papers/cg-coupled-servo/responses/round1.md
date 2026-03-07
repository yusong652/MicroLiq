# Round 1 Responses

## Q1: Servo mechanism — where are the results demonstrating its advantages?

### Changes made

**Abstract**: Revised the servo description to focus on the
mathematical essence — coupled servo coefficients derived from a
volume-constrained stiffness matrix, enabling direct reproduction
of laboratory HCA boundary conditions.

**Introduction**: Clarified three specific aspects of Ma et al.
(2024) that the present formulation refines:

1. Each wall was assigned an independent gain based on its own
   contact stiffness, without reflecting the kinematic coupling
   among wall movements.
2. Servo targets were formulated as effective stresses on individual
   walls, whereas the physically independent control quantities in
   a laboratory HCA are effective pressure *differences* — the
   radial pressure difference (cell pressure) and the
   axial-to-radial pressure difference (loading piston).
3. Because the volume constraint links all wall movements, a
   displacement of one boundary inevitably affects the stress
   conditions at the others — moving the inner cylinder forces the
   outer cylinder to adjust, simultaneously altering both the
   radial and the axial pressure differences.

The present study addresses these points by formulating the servo
directly in terms of effective pressure differences and analytically
solving the resulting coupled system so that the volume-constraint-
induced radial–axial interaction is inherently captured in the
servo coefficients.

**Methodology (Section 2.3)**: Updated the opening paragraph to
align with the three-point structure in the introduction. Removed
speculative language about transient overshoots.

**Highlights**: Updated to match the revised framing.

### Response

The contribution of the servo mechanism is threefold: (a) the
volume-constraint coupling is made explicit in the servo
coefficients, (b) effective pressure differences — matching the
physically independent control channels of a laboratory HCA — are
adopted as servo targets, and (c) the resulting coupled system is
inverted analytically, yielding exact servo coefficients at every
timestep. Analytical correctness of the servo coefficients is a
prerequisite for numerical stability: because the radial and axial
boundary conditions are coupled through both the constant-volume
constraint and the shared dependence on wall contact forces, an
approximate or decoupled gain inevitably introduces residual errors
that accumulate over many thousands of timesteps in undrained cyclic
shear. The closed-form solution eliminates this source of error by
construction.

The introduction now clearly articulates these three points. Beyond
the mathematical formulation, the monotonic shear calibration
(Section 2.4) provides direct experimental validation: in this
stage the full coupled servo operates in stress-control mode,
simultaneously adjusting both the inner-cylinder radius and the
specimen height to maintain σ'_z = σ'_r throughout shearing. The
accurate reproduction of the experimental effective stress path and
stress–strain relationship of Nakata et al. (1998), together with
the subsequent agreement with the cyclic liquefaction resistance
data of Ishihara (1985) under constant-height mode, confirms that
the coupled servo accurately maintains the prescribed boundary
conditions across both operating modes.

---

## Q2: Abstract — "disentangle packing compactness from directional fabric effects" hard to understand

### Changes made

Replaced with simpler wording: "separate the respective roles of
relative density and stress anisotropy."

---

## Q3: Abstract — z–θ plane not self-evident

### Changes made

Added parenthetical clarification: "the plane on which the
torsional shear stress acts."

---

## Q4: Section 2.2 overlaps with introduction; Fig. 2 clarity

### Changes made

**Introduction**: Simplified the second paragraph to a high-level
roadmap (two-stage investigation) without repeating specific K₀
values, density numbers, or CSR levels that appear in Section 2.2.

**Fig. 2(a)**: Updated the stress path figure:

- Fixed duplicated x-axis label ("(kPa)" appeared twice).
- Changed K₀ = 1.0 markers from filled to open for consistency.
- Simplified legend to show IC and three K₀ states directly,
  removing the ambiguous "Target K₀ after AC" title.

**Fig. 2(b)**: Updated the void ratio figure with matching legend
style and corrected x-axis label.

**Section 2.2 text**: Added description of the AC process — ten
equally spaced target stress states from 10 to 100 kPa. Explained
that the fluctuations in Fig. 2(a) arise because compression-state
specimens require larger axial strain per increment, causing axial
stress to lag slightly between target states. The fluctuations
vanish at each target state, confirming that the servo satisfies
the prescribed stress conditions.

---

## Q5: Eq. (2) — Is an explanation of the servo coefficient unnecessary?

### Changes made

**Section 2.3 (Radial condition)**: Added a physical explanation
after Eq. (2): S_cr is described as "a gain factor, derived from
the aggregate contact stiffness at the cylindrical walls, that
converts the pressure error into the wall velocity needed to
eliminate it," with a forward reference to the explicit expression
given later (Eq. 14).

**Section 2.3 (end of Analytical servo)**: Promoted the inline
expression S_cr = −1/K̂₁₁ to a numbered equation with the full
expanded form and a label, so the forward reference resolves and
readers can see the concrete expression in the main text.

**Section 2.3 (Analytical servo)**: Added det(K̂) = K̂₁₁K̂₂₂ −
K̂₁₂K̂₂₁ as a numbered equation before the coupled servo equations,
since the general form is used in monotonic shear calibration.

---

## Q6: Axial condition — What is the physical significance of taking the difference?

### Changes made

**Section 2.3 (Axial condition)**: Rewrote the opening sentence.
Instead of explaining piston mechanics (which varies by machine
type), stated that laboratory HCA tests operate under either
constant total axial stress or constant specimen height, and that
reproducing the former requires controlling the difference between
vertical and radial effective stresses, analogous to the radial
condition.

Explicitly listed two operating modes:
(i) *Stress-control mode* — coupled servo adjusts both dr/dt and
dH/dt; used during AC and monotonic calibration to match the
experimental protocol of Nakata et al. (1998).
(ii) *Displacement-control mode* — dH/dt = 0, p'_{dif,z} evolves
freely; adopted for all cyclic shear simulations to match Ishihara
(1985).

This directly addresses the follow-up concern that Eqs. (3)–(4)
appear unused: stress-control mode activates the full coupled servo
during monotonic shear, distinguishing the present formulation from
Ma et al. (2024).

---

## Q7: Torsional condition — also considered in Han et al. and Ma et al.?

### Changes made

**Section 2.3 (Torsional condition)**: Added an opening sentence
acknowledging that the torsional servo is independent of the
radial–axial system and follows the same formulation adopted in
earlier DEM-based HCA studies (Han et al., 2024; Ma et al., 2024).

---

## Q8: Section 2.4 — monotonic shear involves principal stress rotation; not mentioned?

### Changes made

**Section 2.4**: Rather than adding a separate sentence about
principal stress rotation (which is an inherent feature of torsional
shear already discussed in the introduction), we incorporated the
reference to Ma et al. (2024) directly into the calibration sentence
as a parenthetical citation: "…calibrated against the undrained
monotonic torsional shear data of Nakata et al. (1998) … (see also
Ma et al., 2024)." This acknowledges that Ma et al. also calibrated
against the same dataset, without restating what is already evident
from the test type.

---

## Q9: Description of Ma et al. (2024) — volume constraint claim

### Changes made

**Introduction**: Removed the claim that Ma et al. did not
incorporate the constant-volume condition into their servo
derivation (their paper is ambiguous on this point). Retained only
the objective observation: each wall was assigned an independent
gain without reflecting the kinematic coupling among wall movements.
Updated our contribution statement correspondingly.

**Methodology (Section 2.3)**: Applied the same correction to the
background paragraph.

---

## Q10: r_u–W_s conclusion under strain-based criterion; total vs. plastic shear work?

### Changes made

**Section 3.2 (Cumulative shear work definition)**: Clarified that
$W_s$ represents the total shear work input computed from boundary
quantities, rather than the plastic (dissipated) component alone.
Added a note that the recoverable elastic strain energy becomes
negligibly small relative to the cumulative work as loading
progresses, so the two measures follow closely similar trends.

**Section 3.2 (end of r_u–W_s paragraph)**: Added a sentence
confirming that adopting the strain-based criterion
($\gamma_{SA}=2.5\%$) in place of $r_u=0.95$ does not alter the
conclusion, as both criteria yield the same $N_L$ ordering among
$K_0$ states (already established in Section 3.1).

### Response

The $r_u$–$W_s$ relationship plotted in Fig. 8(d) traces the
co-evolution of two quantities throughout cyclic loading and does
not depend on a specific liquefaction criterion. The conclusion
drawn from it — that the energy-based interpretation alone cannot
fully distinguish $K_0 = 1.0$ from 2.0 — holds regardless of
whether the stress-based ($r_u = 0.95$) or strain-based
($\gamma_{SA} = 2.5\%$) criterion is adopted, because both
criteria yield the same $N_L$ ordering among $K_0$ states
(Section 3.1). A sentence confirming this has been added at the
end of the $r_u$–$W_s$ paragraph.

Regarding the nature of $W_s$: the definition in Eq. (18) computes
total shear work input from boundary stress and strain rate, which
is the same quantity originally proposed by Towhata and Ishihara
(1985). Their formulation was likewise defined as cumulative input
energy rather than the dissipated (plastic) component alone. We
have added a clarification that the recoverable elastic strain
energy becomes negligibly small relative to the cumulative total
as loading progresses, so the two measures follow closely similar
trends and the distinction does not affect the conclusions.

---

## Q11: V_s discussion — role relative to energy; stiffness vs. pore pressure

### Changes made

**Section 3.2 (V_s opening paragraph)**: Reframed the motivation.
Rather than presenting $V_s$ as a separate explanation for what the
energy approach cannot resolve (which risks circular reasoning),
the paragraph now positions $V_s$ as identifying the mechanism
behind the different per-cycle energy accumulation rates already
visible in Fig. 8(c). Emphasized that $V_s$, evaluated within each
quarter-cycle from the secant modulus, tracks the current stiffness
state as loading progresses — unlike cumulative energy, it provides
a direct link between the macroscopic energy picture and the
particle-scale fabric evolution examined in Section 3.3.

**Section 3.2 (V_s closing paragraph)**: Revised to frame the
degradation trajectories as explaining the observations in
Fig. 8(c), and explicitly stated the bridging role of $V_s$ as a
cycle-by-cycle state indicator connecting cumulative energy to
evolving fabric.

### Response

The energy accumulation plot (Fig. 8(c)) already shows that the
three $K_0$ states input energy at different rates per cycle.
The $V_s$ analysis identifies *why*: different stiffness degradation
trajectories lead to different strain amplitudes and hence different
per-cycle energy inputs. Because $V_s$ is derived from the secant
modulus at each quarter-cycle, it serves as a per-cycle state
indicator — unlike cumulative $W_s$, it can be directly related to
the evolving particle contact network. This bridging role motivates
the microscopic fabric analysis in Section 3.3, where the
particle-scale origin of the different degradation rates is
examined.

---

## Q12: Section 3.3 — does this suggest microscopic indicators are inadequate and macroscopic ones are preferable?

### Changes made

**Section 3.3 (Combined effect paragraph)**: Rewrote the
interpretation of the cross-density comparison. The previous
wording ("macroscopic relative density contributes to liquefaction
resistance beyond what is captured by $Z_{m0}$ and $\alpha_0$")
implied that microscopic descriptors are insufficient and that
conventional macroscopic indicators are needed instead. The revised
text emphasizes the complementary roles of the two microscopic
parameters: $Z_{m0}$ is strongly coupled to macroscopic relative
density and governs the baseline resistance level across density
groups, while $\alpha_0$ captures the directional fabric effect
that differentiates $K_0$ states within a given density. Together,
they provide a two-parameter microscopic characterization in which
$Z_{m0}$ reflects packing compactness and $\alpha_0$ reflects the
directional concentration of torsion-resisting contacts.

**Section 3.4 (Limitation)**: Reframed accordingly — the limitation
is no longer that microscopic parameters are inadequate, but that
the strong coupling between $Z_{m0}$ and relative density prevents
full isolation of each descriptor's independent contribution within
the present dataset.

**Conclusions (item 4)**: Updated to use the "complementary roles"
framework consistent with the revised Section 3.3.

### Response

We do not intend to suggest that microscopic indicators are
inadequate. Rather, the two descriptors capture different aspects
of the contact network and play complementary roles. The mechanical
coordination number $Z_{m0}$ is strongly coupled to macroscopic
relative density (denser packing → more contacts), so the
cross-density difference in $N_L$ is already reflected at the
particle scale through $Z_{m0}$. Within a given density group,
where $Z_{m0}$ varies only weakly with $K_0$, the signed fabric
anisotropy indicator $\alpha_0$ effectively discriminates the
$K_0$-dependent liquefaction resistance: specimens with larger
$\alpha_0$ (compression-state consolidation) consistently exhibit
higher $N_L$. The fabric tensor decomposition further confirms that
$\alpha_0$ tracks the fraction of contacts on the $z$–$\theta$
shear plane that directly resist torsional shear. The revised text
and conclusions now clearly present $Z_{m0}$ and $\alpha_0$ as
complementary microscopic characterizations rather than as
indicators that fall short of macroscopic measures.

---

## Q13: Sections 3.3–3.4 — can figures or illustrations enhance the clarity of the physical explanation?

### Changes made

**New Figure (Fig. 15)**: Added a two-panel schematic figure to
accompany the fabric tensor decomposition discussion:

- Panel (a): 3D cylindrical element in $(r, \theta, z)$ coordinates
  with $\tau_{z\theta}$ arrows on the top and side faces. The $z$
  and $\theta$ axes are colored blue (torsion-resisting) and the
  $r$ axis red (mechanically neutral), visually conveying the key
  distinction that only contacts with normals in the $z$ or
  $\theta$ directions resist torsional shear.

- Panel (b): Zoomed bar chart of the torsion-resisting fraction
  $1 - \Phi_{rr}$ for five $K_0$ states at two relative densities
  (data from Table 3 / Appendix C). The y-axis is scaled to
  0.650–0.670 to clearly reveal the monotonic decrease with
  increasing $K_0$ in both density groups. The 2/3 reference line
  marks the isotropic value.

**Section 3.3**: Added a cross-reference to the new figure at the
opening of the fabric tensor decomposition paragraph.

### Response

A new schematic figure (Fig. 15) has been added to illustrate the
physical mechanism discussed in Sections 3.3 and 3.4. Panel (a)
shows which contact orientations are active versus neutral for
torsional resistance in the HCA geometry, and Panel (b) quantifies
the monotonic decrease of the torsion-resisting fraction
$1 - \Phi_{rr}$ with $K_0$ using data from both density groups.
This figure provides the visual support that was previously missing
from the purely text-based explanation.
