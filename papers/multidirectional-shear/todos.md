# Soil Dynamics and Earthquake Engineering (SDEE) Paper: Task List

Paper: *Isolating the Effect of Shear Stress Directionality on Liquefaction Resistance through Controlled Multidirectional DEM Simulations*

Target: Soil Dynamics and Earthquake Engineering (Elsevier, CAS template, single-column)

Source: `thesis/05_multidirectional_shear.md`

---

## Simulation Plan

### Switching frequency parameterization (core extension)

Introduce switching period ratio $\lambda = T_s / T$ as the sole variable:

| $\lambda$ | Description | Status |
|-----------|-------------|--------|
| 1 | Every-cycle switch (= double-8) | Done |
| 2 | Switch every 2 cycles | TODO |
| 5 | Switch every 5 cycles | TODO |
| 10 | Switch every 10 cycles | TODO |
| $\infty$ | Never switch (= single-8) | Done |

- CSR values to run: pick 2--3 representative values (e.g., 0.20, 0.25, 0.30)
- Implementation: add $\lambda$ parameter to loading function, swap $x$/$y$ components every $\lambda$ cycles
- Model and micro-parameters unchanged from existing simulations

### Key questions to answer

1. **$N_L$ vs $\lambda$ relationship** — linear, logarithmic, or threshold/saturation?
2. **Fabric memory time** — does fabric "forget" the previous direction within a few cycles? If $\lambda \geq 10$ behaves like single-8, that defines the memory horizon
3. **Correction factor** — fit $N_L = N_L^{s8}(\mathrm{CSR}) \cdot g(\lambda)$ where $g(\infty) = 1$

### Expected deliverables

- New section in Methodology: define $\lambda$, explain parametric design
- New figure: $N_L$ vs $\lambda$ at multiple CSR
- New figure: $Z_m$ and $F_c$ evolution at intermediate $\lambda$
- Discussion: physical interpretation of $g(\lambda)$, engineering implications

---

## Writing Tasks

### Priority 1: Content from existing simulations

- [x] Scaffold all sections from thesis
- [x] Write abstract
- [x] Set up refs.bib
- [ ] Refine Introduction — sharpen the three confounding factors argument
- [ ] Refine Methodology — check DEM parameter table against actual simulation
- [ ] Refine Results — add numerical values, tighten prose
- [ ] Refine Discussion — strengthen mechanism explanation

### Priority 2: New content from $\lambda$ parameterization

- [ ] Run simulations for $\lambda = 2, 5, 10$ at selected CSR
- [ ] Add $\lambda$ definition to Methodology (§2.2)
- [ ] Add $N_L(\lambda)$ results to Results (§3.1)
- [ ] Add fabric evolution at intermediate $\lambda$ to Results (§3.3)
- [ ] Fit and discuss $g(\lambda)$ correction factor in Discussion (§3.4)
- [ ] Update Abstract and Conclusions to reflect $\lambda$ findings

### Priority 3: Quality & Polish

- [ ] Replace thesis-quality figures with publication-quality versions (vector PDF for line plots)
- [ ] Check self-plagiarism: ensure independent wording from thesis
- [ ] Proofread and consistent terminology
- [ ] Prepare submission package (flatten for Editorial Manager, highlights, cover letter)

---

## Reference

- SDEE Guide for Authors: https://www.sciencedirect.com/journal/soil-dynamics-and-earthquake-engineering/publish/guide-for-authors
- CAS template docs: `els-cas-templates/doc/`
- Thesis source: `thesis/05_multidirectional_shear.md`
- Companion paper: Han et al. (2025), Computers and Geotechnics (under review)
