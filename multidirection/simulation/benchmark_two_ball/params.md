# Two-ball contact-law benchmark: PFC ↔ Yade parameter map

Single-contact calibration used to verify that the Yade `CohFrictMat` model
reproduces the PFC `rrlinear` contact law point-by-point (normal spring,
tangential spring, Coulomb slider, rolling resistance). Reference: v4
multidirectional-shear parameter set.

## Physical test geometry

| Quantity | Value |
|---|---|
| Ball radius $R$ | $1.05 \times 10^{-3}$ m (Toyoura $d_{50}$ × scale 10) |
| Ball density $\rho$ | 2650 kg/m³ |
| Fixed timestep $\Delta t$ | $5 \times 10^{-7}$ s (both codes) |

## Parameter mapping

| Physical meaning | PFC (`rrlinear`) | Yade (`CohFrictMat`) |
|---|---|---|
| Effective modulus | `emod = 3.0e8` Pa | `young = πE_{\mathrm{pfc}}/2 = 4.712e8` Pa |
| Stiffness ratio | `kratio = 2.0` | `poisson = 0.5` (gives $k_s/k_n = 1/2$) |
| Sliding friction | `fric = 0.5` | `frictionAngle = atan(0.5) = 0.4636` rad |
| Rolling friction | `rr_fric = 0.1` | `etaRoll = 0.05` |
| Rolling stiffness scale | auto ($k_r = k_s (R/2)^2$) | `alphaKr = 0.25` |
| Moment law activation | intrinsic | `always_use_moment_law = True`, `useIncrementalForm = True` |

**Why `etaRoll = rr_fric / 2` and `alphaKr = 0.25`**: PFC `rrlinear` uses the
reduced radius $R_\mathrm{eff} = r_1 r_2 / (r_1 + r_2) = R/2$ for equal balls
in both the rolling stiffness and the rolling-slip limit, while Yade
`CohFrictMat` uses the full $R$. The factor-of-2 (limit) and 1/4 (stiffness,
$R^2$) corrections bring the two onto the same physical law.

## Derived contact stiffnesses (measured, equal-ball case)

| Quantity | Both codes |
|---|---|
| $k_n$ | $4.95 \times 10^5$ N/m |
| $k_s$ | $2.47 \times 10^5$ N/m |
| $k_r$ | $6.8 \times 10^{-2}$ N·m/rad |
| Shear-slip threshold at $\|F_n\|=1.04$ N | $F_s^{\max} = 0.520$ N |
| Rolling-slip threshold at $\|F_n\|=1.04$ N | $M_r^{\max} = 5.46 \times 10^{-5}$ N·m |

## Files

- `pfc_test{1,2,3}_*.csv` — PFC reference curves (normal / shear / rolling)
- `yade_test{1,2,3}_*.csv` — Yade curves with the mapping above
- `pfc_vs_yade.png` — three-panel overlay, indistinguishable at this resolution

Generating scripts:
- `G:/Han/proj_multidirection_v4/benchmark/two_ball_pfc/two_ball_pfc.py`
- `G:/Han/proj_multidirection_yade/benchmark/two_ball_yade/two_ball_yade.py`

CSV columns are identical between codes so they can be loaded and plotted
with a single helper.
