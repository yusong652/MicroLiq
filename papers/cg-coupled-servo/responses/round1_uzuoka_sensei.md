# Round 1 — Response to Uzuoka sensei

## Comment 1: Add serial line numbers throughout the entire manuscript

**Response:** Line numbers have been added throughout the manuscript using the `lineno` LaTeX package to facilitate review.

---

## Comment 2: Research gap and novelty unclear — what is novel compared with Han et al. (2024) and Ma et al. (2024)?

**Response:** The introduction has been revised to explicitly identify three refinements over the servo formulation of Ma et al. (2024):

1. Servo targets should be formulated as effective pressure *differences* (the physically independent control quantities in a laboratory HCA), not as absolute effective stresses on individual walls.
2. Under undrained conditions, the constant-volume constraint should be used to eliminate one kinematic variable ($dR/dt$), reducing the system to two variables ($dr/dt$ and $dH/dt$), rather than appending it as a separate condition.
3. Each of the two remaining variables affects both the radial and axial pressure differences simultaneously, so the servo coefficients must be obtained by solving the coupled system rather than from contact stiffness in a single direction alone.

Analytical correctness of the servo coefficients is a prerequisite for numerical accuracy and stability — this itself constitutes a significant contribution. Earlier independent-gain formulations are inherently approximate because they do not account for the cross-coupling between boundary movements; the closed-form coupled solution derived here eliminates this approximation, ensuring mathematically exact servo coefficients at every timestep.

**Changes:** Lines 92–108 (Introduction)

---

## Comment 3: One-sentence paragraph on p.7 (CSR–N_L relationship)

**Response:** The standalone sentence has been merged into the following paragraph as its opening clause, so the figure reference and the discussion of results now form a single coherent paragraph.

**Changes:** Lines 326–335
