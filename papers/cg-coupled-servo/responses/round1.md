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

The contribution of the servo mechanism is a mathematically rigorous
formulation that (a) makes the volume-constraint coupling explicit
in the servo coefficients, (b) uses effective pressure differences
as servo targets to match the independent control channels of a
laboratory HCA, and (c) analytically captures the radial–axial
interaction. This is a theoretical/methodological advance; the
advantage lies in the correctness of the formulation rather than
in a numerical comparison with a previous approximate scheme.

The introduction now clearly articulates these three points. The
validation in Section 2.4 — simultaneous agreement with published
monotonic data (Nakata et al., 1998) and cyclic liquefaction
resistance data (Ishihara, 1985) — confirms that the coupled
servo accurately maintains the prescribed stress conditions
throughout both calibration and cyclic loading stages.

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

The $r_u$–$W_s$ relationship is a direct plot of two evolving
quantities during cyclic loading; it is independent of which
criterion is used to define the liquefaction endpoint. Since both
the stress-based and strain-based criteria yield the same $N_L$
ordering (Section 3.1), the conclusion that the energy-based
interpretation alone cannot fully distinguish $K_0 = 1.0$ from 2.0
remains unchanged.

Regarding the nature of $W_s$: Eq. (18) computes total shear work
input from boundary stress and strain rate, consistent with the
original formulation of Towhata and Ishihara (1985). It includes
both dissipated and elastically stored components. We have added a
clarification that the elastic portion becomes negligible relative
to the cumulative total as loading progresses, so the distinction
does not affect the observed trends or conclusions.

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
