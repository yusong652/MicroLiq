# COMGE-D-26-01109 — Round 1 Revision Checklist

**Submission tag:** `submitted-r0` (0e9de81, 2026-03-21)

**Working branch:** `revision-r1`

**Decision:** Major revision — both reviewers recommend acceptance pending revisions

**Reviewers:** R1 (8 comments), R2 (8 comments)

## Legend

- Status: ⬜ not started · 🟨 in progress · ✅ done · 🟥 blocked / decision needed
- Effort: S (<1h) · M (few hours) · L (1–2 days) · XL (new sims)

---

## Reviewer 1

### R1.1 — Particle size scaling adequacy

**Comment (lines 112–114):** Particle size may influence dilatancy, peak friction angle, and liquefaction resistance. Clarify scaling factor adequacy (specimen-to-particle size ratio) or provide references.

**Geometric facts (corrected):**

- Radial thickness: R − r = 50 − 30 = **20 mm** → **20 / D_max = 6.67×** (D_max = 3 mm). Binding dimension.
- Height: 100 mm → 33× D_max
- Mid-radius circumference: 2π·40 mm ≈ 251 mm → 84× D_max
- Particle count: ~50 000

**Honest diagnosis:**

- The radial direction is inherently HCA's smallest coherent dimension — a geometric feature of the test, not a modelling oversight. All published DEM-HCA studies face the same constraint.
- We will not try to paper this over. The strategy is to **acknowledge the radial constraint and show it does not invalidate the specific quantity (N_L) we report**.

**Strategic framing — multiple independent prongs, none load-bearing alone:**

**Prong A — ASTM D4767 (primary codified anchor).** The most geometrically-analogous laboratory standard for our test type (cohesive-soil triaxial compression) specifies that the largest particle shall be smaller than 1/6 of the specimen diameter. Cited directly as ASTM D4767. Our radial/D_max = 6.67× satisfies this.

**Prong B — Comparability with DEM-HCA peer literature (rigid / stacked-wall precedents only).**

| Study | Boundary | Radial thickness | D_max | **radial/D_max** | H / D_outer |
|---|---|---|---|---|---|
| **This work** | rigid wall | 20 mm | 3 mm | **6.67** | 1.0 |
| Shi et al. 2021 *IJGeom* 21:04021127 | rigid wall | 12 mm | 1.6 mm | **7.5** | 2.0 |
| Li et al. 2015 *Acta Geotech* 10:449-467 | 20-stacked wall | 20 mm | 1.2 mm | 16.7 | 2.0 |

- **Shi 2021** is the closest peer: same rigid-wall boundary, very similar ratio (7.5 vs 6.67). Primary comparability anchor.
- **Li 2015** uses a 20-stacked-wall boundary — still made of rigid elements but with some compliance from the stacked arrangement, conceptually intermediate between rigid and flexible. Ratio 16.7 is larger, serving as a second, softer reference point.

Key response-letter sentence template: "Among DEM-HCA studies with rigid or quasi-rigid boundaries, the present radial/D_max ratio of 6.67 is directly comparable to Shi et al. (2021, rigid wall, 7.5) and within the same order of magnitude as Li et al. (2015, stacked wall, 16.7)."

**Song 2024 is deliberately excluded from this prong** — it uses a flexible membrane boundary, which fundamentally alters the kinematic constraint; its smaller ratio (~5) is permitted *because of* the compliant boundary, and citing it here would (a) conflate boundary type with ratio, and (b) invite the reviewer to ask why we did not also adopt a flexible membrane (a separate question addressed in R1.6 and R2.4). Song 2024 is instead cited in R2.4 (DEM-HCA literature review) and R1.6 (rigid vs flexible boundary discussion).

**Caveat:** reviewer cited "Li, Chen, Gutierrez 2017, CGeo 86:52-66" which could not be verified. Li 2015 (Li, Zhang, Gutierrez in *Acta Geotech*) is very likely the intended citation. Raise this politely in the letter.

**Prong C — Liquefaction is a strength / end-state problem, not a small-strain elastic one.**

- Liquefaction is defined at **finite strain** (γ_SA = 2.5% in Ishihara 1985 protocol, which we follow).
- N_L is governed by **end-state fabric collapse**, controlled by critical-state soil mechanics.
- Classical critical-state theory holds that ultimate shear strength is a material property independent of specimen size.
- Our comparative interest (**N_L vs K_0**, not absolute N_L) adds one more layer: any size-induced bias applies uniformly across K_0 states and does not distort the relative trends that form the paper's conclusions.

**Prong D — HCA geometry: torsional loading is perpendicular to the radial direction.**

- Primary shear strain γ_zθ lies in the tangential–axial plane.
- The smallest geometric dimension (radial) is **not** the primary loading direction, unlike direct-shear where loading acts across the thin dimension.
- Wall-induced inhomogeneity in the radial direction affects the σ'_r measurement accuracy (already absorbed by annulus averaging), but does not directly distort the primary γ_zθ response.
- This is a test-specific geometric argument that REV-type guidelines (framed for cubic/cylindrical samples under axial loading) do not capture.

**Prong E — Empirical calibration / validation (supporting, not load-bearing).** The calibrated parameters reproduce monotonic stress–strain + dilatancy (Nakata 1998) and cyclic N_L–CSR (Ishihara 1985). Mentioned briefly, not leaned on. Reason: the triple-match argument will recur across several reviewer points (notably R1.2, R1.6), so it should not be consumed here as the primary defense.

**Prong F — Letter-only: cost trade-off.** Halving D50 to reach a "preferred" ratio raises computational cost by ~16× (8× particles + 2× timestep reduction) with marginal scientific return for a comparative K_0 study. Out of scope for the present work; noted as future-work direction.

**Deliberately NOT cited (and why):**

- **Huang 2014 / Kuhn–Bagi 2009 / Marketos–Bolton 2010** — all use cubic or solid-cylindrical geometries with more generous radial ratios than HCA can offer. Citing them implicitly invites the reviewer to ask "why not replicate their ratio?" — a question we cannot answer without conceding ground.
- **Wang 2022 MDPI** — argues the ASTM 10× rule is insufficient and recommends 60×. Against us.
- **General DEM REV papers** — same issue: frames written for cubic specimens do not apply cleanly to HCA geometry.

**Effort:** M

**Target:**

- `01_introduction.tex` paragraph 4: expanded the DEM-HCA precedent citation into a two-sentence taxonomy note; now cites `LiGuoZhang2014` (reviewer-requested JCSU paper), `LiZhangGutierrez2015` (renamed from the old `Li2014` key to match actual authorship + year), `Shi2021`, `Liu2021`, and `Song2024` (dual-purpose: also covers R2.4 literature-review request)
- `02_methodology.tex` §2.1: integrated one clause noting that 10× Toyoura PSD scaling is an established DEM practice \citep{Song2024} — **no numerical specimen-to-D_max ratios exposed in manuscript**
- `refs.bib`: old `Li2014` key renamed to `LiZhangGutierrez2015` (Acta Geotech 10:449-467, year corrected to 2015); new entries added for `LiGuoZhang2014` (J Cent South Univ 21:2950-2961), `Shi2021`, and `Song2024`
- All prongs A–F of the full argument (dimensional ratios, ASTM D4767, peer ratio comparison, liquefaction-as-end-state, HCA geometric defense, cost trade-off) remain in `response_letter.tex` — manuscript stays deliberately light

**Deliberate design:** avoid exposing the 6.7× radial ratio in the manuscript. Respond to "provide supporting references" prong in reviewer's question by pointing to Song 2024 as the Toyoura-scaling precedent; the quantitative justification is reserved for the response letter.

**Known gap (for follow-up 2026-04-21):** R1.1 letter currently lacks a research-paper citation that specifically studies DEM specimen-to-particle-size ratios and supports small ratios (~6–10) as adequate for averaged / end-state quantities. Today's survey (Huang 2014, Kuhn–Bagi 2009, Marketos–Bolton 2010, Wang 2022) either showed size effects exist (ambiguous) or argued for larger ratios (against us). Current defense leans on ASTM D4767 + Shi2021/Song2024 precedent + theoretical + geometric prongs. Candidates to pursue tomorrow:

- **Ni et al.** (cited by LiGuoZhang2014): "beyond 15 000 particles, little effect on model results" — if the primary source confirms this in clean language, it directly supports our ~50k particle count.
- **O'Sullivan (2011) textbook** §7 for explicit numeric threshold statements usable as textbook-level backing.
- **Specific DEM cyclic-loading / liquefaction papers** where modest ratios were accepted and results validated — liquefaction being an end-state problem may have independent treatments.
- **Particle-count-convergence studies** (rather than size-ratio): a different angle that plays to our strength (~50 000 particles ≫ typical thresholds).

**Status:** ✅ manuscript edits complete (2026-04-20); response-letter text drafted but R1.1 Prong 2 / supporting-ratio citation pending literature follow-up

### R1.2 — Void ratio range too narrow for Toyoura "dense/medium-dense"

**Comment:** e ranges of 0.736 and 0.742 imply total e spread of only 0.04, which doesn't match Toyoura's physical e_max/e_min range. Terms "dense" and "medium-dense" questionable.

**Response plan:** Reframe Dr as *behavior-matching label* (matching Nakata monotonic + Ishihara cyclic), not e_max/e_min-based. Add **CSR=0.40 Dr=75% new data point** for validation. Acknowledge Dr=75% monotonic reference is missing (Nakata has no such data) as limitation.

**Effort:** L (requires new sim)

**Target:** `02_methodology` calibration section + Fig 7 (validation)

**Status:** 🟥 decision pending — confirm new sim

### R1.3 — CSR, K₀ formulas missing

**Comment:** CSR and K₀ used without computational formulas.

**Response plan:** Add `CSR = τ_cyc / σ'_{z0}` and `K₀ = σ'_r / σ'_z` definitions when first introduced.

**Effort:** S

**Target:** `02_methodology` §2.3 area

**Status:** ⬜

### R1.4 — Need consolidated case table

**Comment:** Simulation program described in brief statements; recommend a table listing all cases (Dr × K₀ × CSR combinations).

**Response plan:** Add a consolidated table: cases × Dr × K₀ × CSR + resulting N_L.

**Effort:** S

**Target:** end of `02_methodology` or start of `03_results`

**Status:** ⬜

### R1.5 — Loading rate / quasi-static condition

**Comment:** Loading rate not specified. Excessive rates cause inertial effects / distorted contact forces. Confirm quasi-static condition.

**Response plan:** Report inertial number I = γ̇·d·√(ρ/p). Show I ≪ 10⁻³ across loading. Cite da Cruz/Roux threshold.

**Effort:** M

**Target:** `02_methodology` §2.3

**Status:** ⬜

### R1.6 — Rigid walls vs flexible membrane

**Comment:** Rigid walls may overestimate stiffness and liquefaction resistance. Discuss limitations and justify with references.

**Response plan:** Acknowledge limitation. Justify: HCA physical chambers are rigid-walled with membrane as interface; present work focuses on fabric-level comparison, not local shear bands; direct cross-reference to R2.4 Song 2024 flex-membrane as complementary / future work.

**Effort:** M

**Target:** `02_methodology` §2.1 end, or discussion

**Status:** ⬜

### R1.7 — CSL source in Fig 8(c)

**Comment:** CSL origin unclear; add citation.

**Response plan:** Update caption to explicitly cite Ishihara (1985) experimental envelope (or whichever is actual source — verify).

**Effort:** S

**Target:** `03_results` Fig 8(c) caption

**Status:** ⬜

### R1.8 — Fig 12 K₀=1.0 "enhancement" in coordination plane

**Comment:** N_L decreases monotonically with K₀ in Figs 8, 10; but Fig 12 shows K₀=1.0 *enhancement*. Explain.

**Response plan:** Add 1–2 sentences: isotropic consolidation produces no preferred force-chain direction → contact normals distribute more uniformly → slightly higher Z_m0. Reaffirm Z_m0 alone is insufficient to predict N_L; α is needed (already stated).

**Effort:** S

**Target:** `03_results` §3.2 Fig 12 discussion paragraph

**Status:** ⬜

---

## Reviewer 2

### R2.1 — Particle-wall friction = 0 in Table 1

**Comment:** Why is particle-wall friction zero?

**Response plan:** Clarify that torque is transmitted via blade geometry (normal contact with blade faces), not wall tangential friction. Setting wall friction to zero avoids introducing an additional unconstrained parameter while still providing full torque transfer through geometrically-constrained blade contacts.

**Effort:** S

**Target:** Table 1 caption / `02_methodology` §2.1

**Status:** ⬜

### R2.2 — Torsional blade size

**Comment:** What is the size of the torsional blades?

**Response plan:** Read actual dimensions from `generate.py`; add to methodology or Table 1.

**Effort:** S

**Target:** `02_methodology` §2.1

**Status:** ⬜

### R2.3 — Difference vs Han (2024) servo

**Comment:** What differs from the servo in Han (2024)?

**Response plan:** Methodology line 326 already addresses this in contribution statement. Expand in response letter: Han (2024) solves only radial + torsional, keeps height fixed; present work adds axial DOF + analytically derives cross-coupling matrix K̂.

**Effort:** S

**Target:** existing text + response letter

**Status:** ⬜

### R2.4 — DEM-HCA literature review + H=D choice

**Comment:** Introduction should review DEM-HCA work: Li 2014, Li 2017 (stacked wall); Song 2024a, Song 2024b (flexible membrane); Shi 2021 (H=2D). Height=outer diameter vs typical H=2D — any requirement?

**Response plan:** (a) Add an Introduction paragraph surveying these DEM-HCA models with boundary-type taxonomy (stacked wall, rigid wall, flex membrane); (b) Justify H=D as computational cost trade-off; cite PFC precedents; note that present study focuses on average fabric response where end-plate effects are minimal.

**Effort:** M

**Target:** `01_introduction` + brief note in `02_methodology`

**Status:** ⬜

### R2.5 — Servo stability near singular stiffness matrix

**Comment:** Drastic contact loss near liquefaction may make stiffness matrix near-singular. How is numerical oscillation prevented?

**Response plan:** First audit actual servo code. Options:

- If regularization exists: describe (damping / condition-number check)
- If not: argue that constant-volume constraint eliminates radial DOF singularity; axial and torsional DOFs are independently stable; post-liquefaction oscillations are physical not numerical

**Effort:** M

**Target:** `02_methodology` servo section or appendix

**Status:** 🟥 needs code audit first

### R2.6 — Validation: add e_r, e_z, volume evolution

**Comment:** Show evolution of e_r and e_z over time or volume change.

**Response plan:** Add figure(s) tracking r, H, volume during monotonic calibration and cyclic validation. Demonstrates constant-volume constraint is strictly satisfied.

**Effort:** S–M (post-processing of existing sim dumps)

**Target:** `02_methodology` validation section

**Status:** ⬜

### R2.7 — Contact force anisotropy (3D rose)

**Comment:** Contact density anisotropy analyzed but not normal contact force anisotropy. Add 3D rose diagrams per Song 2024 etc.

**Response plan:** Compute contact force rose diagrams (in addition to contact density). Decide post-processing from pickled contact dumps vs re-run.

**Effort:** M

**Target:** `03_results` §3.2 near Fig 14

**Status:** 🟥 confirm data availability for post-processing

### R2.8 — Fig 15 quantitative differences

**Comment:** Displacement between K₀=0.5 and 2.0 hard to distinguish at N/NL=0.00 and 0.61; force chain hard to distinguish at N/NL=1.05 and 1.07. Quantify.

**Response plan:** Add quantitative metrics — e.g., displacement magnitude CDF or force-chain principal-direction angle histogram. Either as new panel or in caption text.

**Effort:** M

**Target:** Fig 15 caption / new panel

**Status:** ⬜

---

## Cross-cutting items

### New references to add

- Li, B., Guo, L., Zhang, F. S. (2014) — JCSU, stacked wall DEM-HCA
- Li, B., Chen, L., Gutierrez, M. (2017) — CGeo, stacked wall
- Song, S., Wang, P., Yin, Z., Cheng, Y. P. (2024) — JRMGE, flex-membrane DEM-HCA
- Song, S. X., Yin, Z. Y., Liu, Y. J., Wang, P., Cheng, Y. P. (2024) — IJNAMG, CFD-DEM
- Shi, C., Yang, J., Chu, W., Tang, H., Zhang, Y. (2021) — IJGeo, HCA H=2D
- O'Sullivan / Jiang — DEM REV size-ratio guideline (R1.1)
- da Cruz / Roux — inertial number quasi-static threshold (R1.5)

### Output artifacts

- **This checklist** — internal tracking, not submitted
- **`response_letter.tex`** — point-by-point reply, compiled to PDF, submitted
- **`sections/*.tex` edits** — committed directly to `revision-r1`
- **Marked-up manuscript** — `latexdiff` against `submitted-r0` tag, submitted

### Suggested execution order

1. Quick items first (R1.3, R1.4, R1.7, R2.1, R2.2, R2.3) — half-day, clears baseline
2. R1.8 and R2.4 — text-only argument + citations
3. Decide R1.2 — if yes, kick off CSR=0.40 Dr=75% sim early (longest lead time)
4. R2.5 after code audit
5. R2.6, R2.7, R2.8 post-processing in parallel
6. R1.1, R1.5, R1.6 — text + citations
7. Consolidate into response letter last
