# Computers and Geotechnics (CG) Paper: Task List

Paper: *Influence of Initial Stress Anisotropy on Liquefaction Resistance in Undrained Cyclic Torsional Shear: DEM Simulation of Hollow Cylinder Tests*

Target: Computers and Geotechnics (Elsevier, CAS template)

Source: `thesis/04_1_anisotropic_consolidation_sim.md`

---

## Priority 1: Must Fix (Submission Blockers)

- [x] **Switch to CAS template (`cas-dc`)** ✓
  - ✓ Replaced `elsarticle` document class with `cas-dc`
  - ✓ Switched bibliography style to `cas-model2-names` (author-year with natbib)
  - Note: citations are currently plain text — will convert to `\citep{}`/`\citet{}` when refs.bib is complete
  - ✓ Adapted frontmatter to CAS format (`\shorttitle`, `\shortauthors`, `\cormark`, `\credit`, etc.)
  - ✓ Integrated highlights into `\begin{highlights}` environment
  - ✓ Copied `cas-dc.cls`, `cas-common.sty`, `cas-model2-names.bst` to paper root
  - ✓ Removed duplicate `graphicx` (loaded by `cas-dc.cls`)
  - ✓ Added `\printcredits` for CRediT statement

- [x] **Complete refs.bib** ✓
  - ✓ 25 complete bib entries (12 cited, 13 reserve)
  - ✓ All placeholders replaced with full bibliographic info + DOI
  - ✓ Nakata et al. (1998) verified and added to thesis refs too

- [x] **Write Abstract** ✓
  - ✓ ~230 words covering objective, method, macro findings, micro interpretation, convergence

- [x] **Add DEM parameter table** ✓
  - ✓ Table 1 added to 02_methodology.tex with all 9 parameters from thesis Table 4-1
  - ✓ Footnotes for friction coefficient change (IC vs AC/cyclic)

- [x] **Fill in Author / Affiliation / Corresponding author** ✓
  - ✓ Han (Kyoto U), Uzuoka (DPRI), Nakamura (MAEDA), Ueda (DPRI, corresponding)
  - ✓ CRediT statements assigned per author
  - Note: ORCID can be added later if needed

---

## Priority 2: Content Completeness

- [x] **Add HCA stress/strain equations as Appendix** ✓
  - ✓ Created `sections/appendix_a.tex` with Table A.1 (9 rows: vertical, inner/outer pressure, circumferential, radial, shear, major/intermediate/minor principal)
  - ✓ Added Hight (1983) citation for HCA equations derivation
  - ✓ Updated methodology text to reference Appendix A instead of "omitted for brevity"

- [x] **Add contact density definition** ✓
  - ✓ Eq. ρc(θz, φcir) added to microscopic descriptors subsection with citation

- [x] **Add fabric tensor definition** ✓
  - ✓ Φij definition (Eq. 4) added before α definition, with Oda (1982) citations

- [x] **Supplement key numerical values in results** ✓
  - ✓ Vs: initial and 28-cycle values for all three K0 states
  - ✓ Zm0: 4.98 (K0=1.0), 4.89 (K0=0.5), 4.88 (K0=2.0)
  - ✓ α0: +0.07 (K0=0.5), +0.02 (K0=1.0), -0.05 (K0=2.0)

- [x] **Add Data Availability Statement** ✓

- [x] **Add Declaration of Competing Interests** ✓

- [ ] **Add Acknowledgements section**
  - Funding sources, computational resources, etc.

---

## Priority 3: Quality & Polish

- [x] **Formalize in-text citations** ✓
  - ✓ All 12 plain-text citations replaced with `\citep{}`/`\citet{}` commands
  - ✓ Zero undefined citation warnings

- [x] **Numbered conclusions** ✓
  - ✓ Reformatted to 5 numbered findings (enumerate environment)

- [ ] **Review figure quality for submission**
  - Current figures are PNG/JPG; prefer vector PDF for line plots
  - Check resolution: minimum 300 dpi for raster images
  - Ensure consistent font sizes across all figures
  - Verify all axis labels, legends are legible at print size

- [ ] **Check self-plagiarism risk**
  - Run text similarity check between thesis and paper
  - Ensure results/conclusions are independently worded even when conveying same findings
  - Particular attention to Introduction and Conclusions sections

- [ ] **Proofread and language check**
  - Consistent terminology: "liquefaction resistance" vs "liquefaction strength"
  - Consistent notation: K0 always as \Kzero{} macro
  - Check for orphaned cross-references after template switch

- [ ] **Prepare submission package**
  - Flatten directory structure for Editorial Manager (use `papers/shared/scripts/flatten_for_em.sh`)
  - Prepare separate files: highlights, cover letter, graphical abstract (if applicable)
  - Verify compiled PDF matches all Elsevier formatting requirements

---

## Reference

- CG Guide for Authors: https://www.sciencedirect.com/journal/computers-and-geotechnics/publish/guide-for-authors
- CAS template docs: `els-cas-templates/doc/`
- Thesis source: `thesis/04_1_anisotropic_consolidation_sim.md`
