# Computers and Geotechnics (CG) Paper: Task List

Paper: *Influence of Initial Stress Anisotropy on Liquefaction Resistance in Undrained Cyclic Torsional Shear: DEM Simulation of Hollow Cylinder Tests*

Target: Computers and Geotechnics (Elsevier, CAS template)

Source: `thesis/04_1_anisotropic_consolidation_sim.md`

---

## Round 2 Revision (Current)

### Completed

- [x] **Section 2.3 narrative restructure**
  - Rewrote lab→DEM transition: lab paragraph introduces all 4 loading components ($p_i$, $p_o$, $p_z$, $T$) with symbols
  - Added pore water pressure measurement context ("monitored by pressure transducers")
  - Introduced effective pressures ($p_o'$, $p_i'$, $p_z'$) together with difference equations as foreshadowing
  - DEM paragraph: constant-volume method → 4 DOF vs 4 conditions → difference equations resolve the mapping
  - "Because $u$ drops out" narrative thread: introduction (b) → methodology §2.3 → consistent throughout

- [x] **Servo coefficient notation update**
  - $S_{cs}$ → $S_T$ (torsional, consistent with $e_T$)
  - Introduced $S_{rr}$, $S_{rz}$, $S_{zr}$, $S_{zz}$ for coupled servo (diagonal = direct, off-diagonal = coupling)
  - $S_{cr}$ → $S_{rr}$ (constant-height special case)
  - Updated both main text and Appendix B

- [x] **Torsional condition: unified error definition**
  - Added $e_T = T - T^{tar}$ to match $e_r$, $e_z$ style

- [x] **Torsional servo expression clarified**
  - Stated explicitly that the torsional condition is solved independently because it does not enter the radial--axial kinematic constraints
  - Defined the torsional update as $d\theta/dt = (e_T/\Delta t) S_T$
  - Introduced the contact-stiffness-weighted rotational stiffness $I_{rot}$ and the coefficient relation $S_T = 1/I_{rot}$
  - Kept the notation consistent between the main text, flowchart, and Appendix B

- [x] **Removed uncoupled servo equations from Radial/Axial paragraphs**
  - Conditions now define targets/errors only; servo equations appear after coupled derivation

- [x] **Moved prior-work comparison to end of §2.3**
  - Han2024/Ma2024 comparison as concise closing paragraph, not interrupting derivation

- [x] **Cyclic loading protocol split**
  - CSR definition removed (common knowledge)
  - Liquefaction criteria moved to §3.1
  - $u$ inference formula retained in §2.3

- [x] **Added servo flowchart (TikZ)**
  - Fig. 5: 7-step timestep loop with cycle arrow
  - Referenced after $u$ and $r_u$ definitions

- [x] **Introduction (b) revised**
  - "Individual effective pressures cannot serve as independent servo targets"
  - "Because the pore water pressure drops out of any difference of effective pressures"
  - Echoes methodology narrative

- [x] **Tightened the Introduction statement of the prior limitation**
  - Clarified that the difficulty is not merely the number of variables, but the mismatch between laboratory boundary conditions and DEM-accessible quantities
  - Stated that a naive formulation using four kinematic unknowns together with four effective-stress conditions plus the undrained condition is not a physically consistent closed system

- [x] **Clarified boundary-condition mapping and pore-pressure elimination**
  - Stated explicitly that DEM provides effective stresses directly, not pore water pressure
  - Emphasized that the individual effective stresses cannot be used directly as laboratory control inputs because each contains the unknown pore-pressure offset
  - Highlighted that the pressure-difference relations eliminate $u$ and provide the valid independent equations needed for closure

- [x] **Emphasized the rigorous coupled elastic/stiffness coefficient system**
  - Presented the servo coefficients as analytically derived from the coupled elastic stiffness equations under the constant-volume constraint
  - Contrasted the present formulation with the independent-control approximation used in earlier approaches

- [x] **Synchronized the Conclusions with the full servo formulation**
  - Updated the methodology conclusion to include laboratory-to-DEM boundary-condition mapping, pressure-difference servo targets, the constant-volume coupling, and the analytically closed servo system
  - Matched the conclusion wording to the revised derivation in Section 2.3

- [x] **Conclusions optimized**
  - Item 1: simplified, removed "in undrained cyclic shear"
  - Item 4: "two" → "three" descriptors, explicitly named $\rho_c$

- [x] **Figure widths adjusted for single-column**
  - Figs 2, 8, 10, 11, 12 → 0.7\linewidth

- [x] **Appendix B cleaned**
  - Removed experiment-specific conditions
  - $S_{cs}$ → $S_T$, $S_{cr}$ → $S_{rr}$

- [x] **Uzuoka sensei Comment 1**: Citation format fixed (longnamesfirst removed)

- [x] **Uzuoka sensei Comment 2**: HCA schematic and geometry definitions added
  - Added schematic figure defining $r$, $R$, and $H$
  - Clarified the four DEM kinematic degrees of freedom ($dr/dt$, $dR/dt$, $dH/dt$, $d\theta/dt$)
  - Introduced the figure at the start of §2.3 and aligned the text with the lab-to-DEM mapping discussion

- [x] **Responded to Ueda sensei comments**
  - Added a confirmation note regarding the final corresponding-author arrangement in `responses/round2_ueda_sensei.md`

- [x] **Responded to Uzuoka sensei comments**
  - The Round 2 response file contains the two requested items (citation format and definition of $r$, $R$, and $H$), and no additional response items remain

### TODO

---

## Priority 3: Quality & Polish

- [ ] **Review figure quality for submission**
  - Current figures are PNG/JPG; prefer vector PDF for line plots
  - Check resolution: minimum 300 dpi for raster images
  - Ensure consistent font sizes across all figures
  - Verify all axis labels, legends are legible at print size

- [ ] **Check self-plagiarism risk**
  - Run text similarity check between thesis and paper
  - Ensure results/conclusions are independently worded

- [ ] **Proofread and language check**
  - Consistent terminology: "liquefaction resistance" vs "liquefaction strength"
  - Consistent notation: K0 always as \Kzero{} macro
  - Check for orphaned cross-references

- [ ] **Prepare submission package**
  - Flatten directory structure for Editorial Manager
  - Prepare separate files: highlights, cover letter, graphical abstract
  - Verify compiled PDF matches Elsevier formatting requirements

---

## Completed (Round 1 & Initial)

<details>
<summary>Click to expand</summary>

- [x] Switch to CAS template (cas-dc → cas-sc)
- [x] Complete refs.bib (25 entries)
- [x] Write Abstract (~230 words)
- [x] Add DEM parameter table
- [x] Fill in Author/Affiliation/Corresponding author
- [x] Add HCA stress/strain equations as Appendix A
- [x] Add contact density definition
- [x] Add fabric tensor definition
- [x] Supplement key numerical values in results
- [x] Add Data Availability Statement
- [x] Add Declaration of Competing Interests
- [x] Add Acknowledgements section
- [x] Formalize in-text citations
- [x] Numbered conclusions

</details>

---

## Reference

- CG Guide for Authors: https://www.sciencedirect.com/journal/computers-and-geotechnics/publish/guide-for-authors
- CAS template docs: `els-cas-templates/doc/`
- Thesis source: `thesis/04_1_anisotropic_consolidation_sim.md`
