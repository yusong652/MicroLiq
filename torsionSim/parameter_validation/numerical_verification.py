"""Numerical verification of the coupled HollowTorsion servo (§2.5).

Three-panel figure (1x3 layout, figsize matching validate_combined.py):
  (a) Volume conservation            -- V(t)/V_0 - 1, in 1e-7 units
  (b) Servo tracking errors          -- e_r, e_z over time (kPa)
  (c) Inertial number I(t)           -- |dgamma/dt| d sqrt(rho/p')
                                        on log-y, with the GDR-MiDi
                                        (2004) quasi-static threshold
                                        I=1e-3 and the da Cruz et al.
                                        (2005) dense-regime upper bound
                                        I~1e-1 marked as references.

Stiffness-floor diagnostics (the previous panel (c) content) are
retained in `recover_stiffness.py` for the R2.5 letter response.

Default case: Dr75 / K0=1.0 / CSR=0.400, total-stress-controlled
axial boundary -- the 2x2 servo run added for response R2.6.
"""

import argparse
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DEFAULT_CSV = (
    "/Users/hanyusong/thesis/MicroLiq/torsionSim/cyclic_shear/"
    "Dr75/k1.00/csr_0.400/torsion_shear.csv"
)
PAPER_FIG_DIR = Path(
    "/Users/hanyusong/thesis/MicroLiq/papers/cg-coupled-servo/figures")
LOCAL_OUT = Path(__file__).parent / "numerical_verification"


# ----------------------------------------------------------------------
# Style helpers (matched to validate_combined.py)
# ----------------------------------------------------------------------
# Style aligned with validate_combined.py (the sibling §2.4 calibration
# figure) so the two methodology figures share consistent typography.
AXLABEL_FS = 18
TICK_FS = 15
LEGEND_FS = 14
PANEL_FS = 16
GRID_KW = dict(color='grey', linestyle='--', lw=0.35, alpha=0.8)

# Plot every STRIDE-th sample to thin the per-timestep servo oscillation
# without blurring sharp floor-engagement events on I_rot.
STRIDE = 4

# Explicit y-limits with breathing room above the observed envelope.
YLIM_DRIFT = (-2.0, 2.0)   # in 1e-7 units
YLIM_ERR = (-5.0, 5.0)     # kPa
YLIM_I = (1.0e-6, 1.0e0)   # log-y range for inertial number

# Inertial-number inputs (Methodology Section 2.1).
D50 = 2.0e-3       # m, mean particle diameter from PSD 1.0-3.0 mm
RHO_S = 2650.0     # kg/m^3, Toyoura particle density (Table 1)

# Reference thresholds:
#  - GDR-MiDi (2004) p. 344, Section 3.2 plane shear: I<1e-3 is the strict
#    quasi-static threshold below which the effective friction becomes
#    shear-rate independent.
#  - da Cruz et al. (2005) p. 2, Fig. 1(a) caption: I=1e-2 is the
#    representative value used to illustrate the quasi-static regime in
#    plane shear.
I_QS = 1.0e-3
I_DC = 1.0e-2


def add_panel_label(ax, label):
    ax.text(
        -0.0, 1.005, label,
        transform=ax.transAxes,
        ha='left', va='bottom',
        fontsize=PANEL_FS, fontweight='bold',
        clip_on=False)


def style(ax):
    ax.tick_params(axis='both', which='major', labelsize=TICK_FS)
    ax.grid(axis='both', which='major', **GRID_KW)


# ----------------------------------------------------------------------
# Stiffness recovery (legacy fallback)
# ----------------------------------------------------------------------
def reverse_stiffness(df: pd.DataFrame) -> pd.DataFrame:
    r = df["rad_inner"].to_numpy()
    R = df["rad_outer"].to_numpy()
    H = df["height"].to_numpy()
    Srr = df["S_rr"].to_numpy()
    Srz = df["S_rz"].to_numpy()
    Szr = df["S_zr"].to_numpy()
    Szz = df["S_zz"].to_numpy()
    detS = Srr * Szz - Srz * Szr
    with np.errstate(divide='ignore', invalid='ignore'):
        detK = np.where(detS != 0.0, 1.0 / detS, np.nan)
    K11 = -Szz * detK
    K12 = Srz * detK
    K22 = -Srr * detK
    K_ro = K12 * (4.0 * np.pi * R ** 2 * H ** 2) / (R ** 2 - r ** 2)
    K_ri = -2.0 * np.pi * r * H * K11 - (r ** 2 / R ** 2) * K_ro
    K_z = (-np.pi * (R ** 2 - r ** 2) * K22
           - ((R ** 2 - r ** 2) ** 2 * K_ro) /
             (4.0 * R * (r + R) * H ** 2))
    return pd.DataFrame({"K_ri": K_ri, "K_ro": K_ro, "K_z": K_z})


# ----------------------------------------------------------------------
# Main figure
# ----------------------------------------------------------------------
def compute_N_over_NL(df: pd.DataFrame, freq: float = 8.0,
                      ru_threshold: float = 0.95) -> tuple:
    """Return (N_over_NL array, N_L scalar, t_L scalar).

    N_L is the cycle at which the excess pore-pressure ratio
    r_u = 1 - p'/p'_0 first reaches the threshold (default 0.95),
    matching the stress-based liquefaction criterion adopted in
    Section 3.1 of the manuscript.
    """
    t = df["time_duration"].to_numpy()
    N = freq * t
    if "ru" in df.columns:
        ru = df["ru"].to_numpy()
    else:
        p = df["stress_p"].to_numpy()
        ru = 1.0 - p / p[0]
    over = ru >= ru_threshold
    if not over.any():
        raise RuntimeError(
            f"r_u >= {ru_threshold} not reached in this run")
    iL = int(np.argmax(over))
    t_L = float(t[iL])
    N_L = float(N[iL])
    return N / N_L, N_L, t_L


def make_figure(csv_path: str, out_stem: Path, freq: float = 8.0):
    df = pd.read_csv(csv_path)
    t = df["time_duration"].to_numpy()
    x, _, _ = compute_N_over_NL(df, freq=freq)

    # ---- (a) volume conservation ----
    V = np.pi * (df["rad_outer"] ** 2 - df["rad_inner"] ** 2) * df["height"]
    V0 = V.iloc[0]
    drift = (V.to_numpy() / V0 - 1.0) * 1e7  # in 1e-7 units
    drift_max_abs = float(np.max(np.abs(drift)))

    # ---- (b) tracking errors ----
    e_r = (df["stress_dif_r"] - df["stress_dif_r_tgt"]).to_numpy() / 1e3
    e_z = (df["stress_dif_z_r"] - df["stress_dif_z_tgt"]).to_numpy() / 1e3

    # ---- (c) inertial number I = |gamma_dot| d sqrt(rho/p') ----
    # Engineering shear strain gamma = 2 * tensorial epsilon_z_theta.
    gamma = 2.0 * df["strain_shear"].to_numpy()
    gdot = np.gradient(gamma, t)
    p = df["stress_p"].to_numpy()
    p_safe = np.maximum(p, 1.0)  # avoid 1/0 if p' touches zero in transient
    I_n = np.abs(gdot) * D50 * np.sqrt(RHO_S / p_safe)

    # ---- figure ----
    _, axes = plt.subplots(1, 3, figsize=(15.0, 4.9))
    ax_a, ax_b, ax_c = axes

    x_label = r'$N_{c}/N_{L}$'
    x_max = float(x[-1])

    # Thin every STRIDE-th sample for plotting only; max-drift annotation
    # and stiffness-source diagnostics still use the full series.
    s = slice(None, None, STRIDE)
    x_p = x[s]
    drift_p = drift[s]
    e_r_p = e_r[s]
    e_z_p = e_z[s]
    I_n_p = I_n[s]
    liq_kw = dict(color='tab:red', linestyle='dashed', linewidth=1.2)

    def mark_liquefaction(ax, y_pos):
        ax.axvline(1.0, **liq_kw)
        ax.text(1.02, y_pos, r'$N_{c}/N_{L}=1$',
                color='tab:red', fontsize=LEGEND_FS,
                ha='left', va='top',
                transform=ax.get_xaxis_transform())

    # (a) volume drift
    ax_a.plot(x_p, drift_p, color='tab:blue', linewidth=1.6,
              label=r'$DEM\ simulation$')
    ax_a.axhline(0.0, color='grey', lw=0.6)
    mark_liquefaction(ax_a, 0.97)
    ax_a.set_xlim(0.0, x_max)
    ax_a.set_ylim(*YLIM_DRIFT)
    ax_a.set_xlabel(x_label, fontsize=AXLABEL_FS)
    ax_a.set_ylabel(
        r'$V/V_{0}-1\ (\times 10^{-7})$',
        fontsize=AXLABEL_FS)
    ax_a.annotate(
        (r'$\max|V/V_{0}-1|$'
         '\n'
         r'$=%.1f\times 10^{-7}$' % drift_max_abs),
        xy=(0.03, 0.05), xycoords='axes fraction',
        fontsize=LEGEND_FS, ha='left', va='bottom')
    style(ax_a)
    add_panel_label(ax_a, '(a)')

    # (b) tracking errors
    ax_b.plot(x_p, e_r_p, color='tab:blue', linewidth=1.2,
              label=r'$e_{r}=p_{dif,r}^{\prime}-p_{dif,r}^{tar}$')
    ax_b.plot(x_p, e_z_p, color='tab:orange', linewidth=1.2,
              label=r'$e_{z}=p_{dif,z}^{\prime}-p_{dif,z}^{tar}$')
    ax_b.axhline(0.0, color='grey', lw=0.6)
    mark_liquefaction(ax_b, 0.97)
    ax_b.set_xlim(0.0, x_max)
    ax_b.set_ylim(*YLIM_ERR)
    ax_b.set_xlabel(x_label, fontsize=AXLABEL_FS)
    ax_b.set_ylabel(r'$Tracking\ error\ (kPa)$', fontsize=AXLABEL_FS)
    ax_b.legend(fontsize=LEGEND_FS, loc='lower left')
    style(ax_b)
    add_panel_label(ax_b, '(b)')

    # (c) inertial number
    ax_c.semilogy(x_p, I_n_p, color='tab:blue', linewidth=1.2,
                  label=r'$DEM\ simulation$')
    ax_c.axhline(I_QS, color='tab:orange', linestyle='dashed',
                 linewidth=1.2)
    ax_c.text(0.02, I_QS * 1.4,
              r'$\mathrm{GDR\!-\!MiDi\ (2004)}$',
              color='tab:orange', fontsize=LEGEND_FS,
              ha='left', va='bottom')
    ax_c.axhline(I_DC, color='tab:green', linestyle='dashed',
                 linewidth=1.2)
    ax_c.text(0.02, I_DC * 1.4,
              r'$\mathrm{da\ Cruz\ et\ al.\ (2005)}$',
              color='tab:green', fontsize=LEGEND_FS,
              ha='left', va='bottom')
    mark_liquefaction(ax_c, 0.97)
    ax_c.set_xlim(0.0, x_max)
    ax_c.set_ylim(*YLIM_I)
    ax_c.set_xlabel(x_label, fontsize=AXLABEL_FS)
    ax_c.set_ylabel(r'$Inertial\ number\ I$',
                    fontsize=AXLABEL_FS)
    style(ax_c)
    add_panel_label(ax_c, '(c)')

    plt.tight_layout()
    out_stem.parent.mkdir(parents=True, exist_ok=True)
    pdf = out_stem.with_suffix(".pdf")
    png = out_stem.with_suffix(".png")
    plt.savefig(pdf, bbox_inches='tight')
    plt.savefig(png, dpi=700, bbox_inches='tight')
    print(f"wrote {pdf}")
    print(f"wrote {png}")
    return pdf, png


def make_stiffness_panel(csv_path: str, out_stem: Path,
                         stiff_floor: float = 0.10,
                         inertia_floor: float = 0.20):
    """Generate a 1x1 standalone figure containing the wall-stiffness /
    moment-of-inertia ratio panel. Used in the response letter for
    R2.5 to give the reviewer direct visual evidence that the clip
    floors keep $\\det\\hat{\\mathbf{K}}$ bounded away from zero.

    If the CSV lacks logged stiff_* columns (legacy schema), the
    aggregate stiffnesses are reverse-engineered from the logged
    servo coefficients S_rr / S_rz / S_zr / S_zz."""
    df = pd.read_csv(csv_path)
    x, _, _ = compute_N_over_NL(df, freq=8.0)

    if {"stiff_inner", "stiff_outer", "stiff_top",
            "stiff_bot"}.issubset(df.columns):
        K_ri = df["stiff_inner"].to_numpy()
        K_ro = df["stiff_outer"].to_numpy()
        K_z = 0.5 * (df["stiff_top"].to_numpy()
                     + df["stiff_bot"].to_numpy())
    else:
        rec = reverse_stiffness(df)
        K_ri = rec["K_ri"].to_numpy()
        K_ro = rec["K_ro"].to_numpy()
        K_z = rec["K_z"].to_numpy()

    I_rot = df["moment_inertial"].to_numpy()
    valid = np.isfinite(K_ri) & np.isfinite(K_ro) & np.isfinite(K_z)
    i0 = int(np.argmax(valid))
    Kri_r = K_ri / K_ri[i0]
    Kro_r = K_ro / K_ro[i0]
    Kz_r = K_z / K_z[i0]
    I_r = I_rot / I_rot[i0]

    s = slice(None, None, STRIDE)
    x_max = float(x[-1])

    fig, ax = plt.subplots(figsize=(5.0, 4.9))
    ax.plot(x[s], Kri_r[s], color='tab:blue', linewidth=1.2,
            label=r'$K_{r,i}/K_{r,i}^{(0)}$')
    ax.plot(x[s], Kro_r[s], color='tab:orange', linewidth=1.2,
            label=r'$K_{r,o}/K_{r,o}^{(0)}$')
    ax.plot(x[s], Kz_r[s], color='tab:green', linewidth=1.2,
            label=r'$K_{z}/K_{z}^{(0)}$')
    ax.plot(x[s], I_r[s], color='tab:purple', linewidth=1.2,
            label=r'$I_{rot}/I_{rot}^{(0)}$')

    ax.axhline(stiff_floor, color='black', linestyle='dashed',
               linewidth=1.0)
    ax.text(0.02, stiff_floor + 0.015,
            r'$10\%\ stiffness\ floor$',
            color='black', fontsize=LEGEND_FS - 1,
            ha='left', va='bottom')
    ax.axhline(inertia_floor, color='black', linestyle='dotted',
               linewidth=1.0)
    ax.text(0.02, inertia_floor + 0.015,
            r'$20\%\ I_{rot}\ floor$',
            color='black', fontsize=LEGEND_FS - 1,
            ha='left', va='bottom')

    ax.axvline(1.0, color='tab:red', linestyle='dashed', linewidth=1.2)
    ax.text(1.02, 0.97, r'$N_{c}/N_{L}=1$',
            color='tab:red', fontsize=LEGEND_FS,
            ha='left', va='top',
            transform=ax.get_xaxis_transform())

    ax.set_xlim(0.0, x_max)
    ax.set_ylim(0.0, 1.05)
    ax.set_xlabel(r'$N_{c}/N_{L}$', fontsize=AXLABEL_FS)
    ax.set_ylabel(r'$Aggregate\ stiffness\ ratio$', fontsize=AXLABEL_FS)
    ax.tick_params(axis='both', which='major', labelsize=TICK_FS)
    ax.grid(axis='both', which='major', **GRID_KW)
    ax.legend(fontsize=LEGEND_FS - 2, loc='lower left',
              bbox_to_anchor=(-0.002, 0.24),
              ncol=2, columnspacing=0.6, handletextpad=0.4,
              framealpha=0.85)

    plt.tight_layout()
    out_stem.parent.mkdir(parents=True, exist_ok=True)
    pdf = out_stem.with_suffix(".pdf")
    png = out_stem.with_suffix(".png")
    plt.savefig(pdf, bbox_inches='tight')
    plt.savefig(png, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"wrote {pdf}")
    print(f"wrote {png}")
    return pdf, png


def make_inertial_panel(csv_path: str, out_stem: Path):
    """Generate a 1x1 standalone figure containing only the inertial
    number panel (panel (c) of the main figure). Used in the
    response letter for R1.5 so the reviewer can read the QS argument
    without flipping to the manuscript."""
    df = pd.read_csv(csv_path)
    t = df["time_duration"].to_numpy()
    x, _, _ = compute_N_over_NL(df, freq=8.0)
    gamma = 2.0 * df["strain_shear"].to_numpy()
    gdot = np.gradient(gamma, t)
    p = df["stress_p"].to_numpy()
    p_safe = np.maximum(p, 1.0)
    I_n = np.abs(gdot) * D50 * np.sqrt(RHO_S / p_safe)

    s = slice(None, None, STRIDE)
    x_p = x[s]
    I_n_p = I_n[s]
    x_max = float(x[-1])

    # Match the per-panel proportions of the main 3-panel figure
    # (figsize=(15.0, 4.9), so each panel is ~5.0 x 4.9 inches).
    fig, ax = plt.subplots(figsize=(5.0, 4.9))
    ax.semilogy(x_p, I_n_p, color='tab:blue', linewidth=1.2,
                label=r'$DEM\ simulation$')
    ax.axhline(I_QS, color='tab:orange', linestyle='dashed', linewidth=1.2)
    ax.text(0.02, I_QS * 1.4,
            r'$\mathrm{GDR\!-\!MiDi\ (2004)}$',
            color='tab:orange', fontsize=LEGEND_FS,
            ha='left', va='bottom')
    ax.axhline(I_DC, color='tab:green', linestyle='dashed', linewidth=1.2)
    ax.text(0.02, I_DC * 1.4,
            r'$\mathrm{da\ Cruz\ et\ al.\ (2005)}$',
            color='tab:green', fontsize=LEGEND_FS,
            ha='left', va='bottom')
    ax.axvline(1.0, color='tab:red', linestyle='dashed', linewidth=1.2)
    ax.text(1.02, 0.97, r'$N_{c}/N_{L}=1$',
            color='tab:red', fontsize=LEGEND_FS,
            ha='left', va='top',
            transform=ax.get_xaxis_transform())
    ax.set_xlim(0.0, x_max)
    ax.set_ylim(*YLIM_I)
    ax.set_xlabel(r'$N_{c}/N_{L}$', fontsize=AXLABEL_FS)
    ax.set_ylabel(r'$Inertial\ number\ I$', fontsize=AXLABEL_FS)
    ax.tick_params(axis='both', which='major', labelsize=TICK_FS)
    ax.grid(axis='both', which='major', **GRID_KW)

    plt.tight_layout()
    out_stem.parent.mkdir(parents=True, exist_ok=True)
    pdf = out_stem.with_suffix(".pdf")
    png = out_stem.with_suffix(".png")
    plt.savefig(pdf, bbox_inches='tight')
    plt.savefig(png, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"wrote {pdf}")
    print(f"wrote {png}")
    return pdf, png


def make_volume_error_panels(csv_path: str, out_stem: Path,
                             freq: float = 8.0):
    """Generate a 1x2 standalone figure containing panels (a) volume
    drift and (b) servo tracking errors. Used in the response letter
    for R2.6 so the reviewer sees the constant-volume and (e_r, e_z)
    evidence in scope, without panel (c) which addresses R1.5."""
    df = pd.read_csv(csv_path)
    x, _, _ = compute_N_over_NL(df, freq=freq)

    V = np.pi * (df["rad_outer"] ** 2 - df["rad_inner"] ** 2) * df["height"]
    V0 = V.iloc[0]
    drift = (V.to_numpy() / V0 - 1.0) * 1e7
    drift_max_abs = float(np.max(np.abs(drift)))

    e_r = (df["stress_dif_r"] - df["stress_dif_r_tgt"]).to_numpy() / 1e3
    e_z = (df["stress_dif_z_r"] - df["stress_dif_z_tgt"]).to_numpy() / 1e3

    s = slice(None, None, STRIDE)
    x_p = x[s]
    drift_p = drift[s]
    e_r_p = e_r[s]
    e_z_p = e_z[s]
    x_max = float(x[-1])
    liq_kw = dict(color='tab:red', linestyle='dashed', linewidth=1.2)

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10.0, 4.9))

    def mark_liquefaction(ax, y_pos):
        ax.axvline(1.0, **liq_kw)
        ax.text(1.02, y_pos, r'$N_{c}/N_{L}=1$',
                color='tab:red', fontsize=LEGEND_FS,
                ha='left', va='top',
                transform=ax.get_xaxis_transform())

    ax_a.plot(x_p, drift_p, color='tab:blue', linewidth=1.6,
              label=r'$DEM\ simulation$')
    ax_a.axhline(0.0, color='grey', lw=0.6)
    mark_liquefaction(ax_a, 0.97)
    ax_a.set_xlim(0.0, x_max)
    ax_a.set_ylim(*YLIM_DRIFT)
    ax_a.set_xlabel(r'$N_{c}/N_{L}$', fontsize=AXLABEL_FS)
    ax_a.set_ylabel(r'$V/V_{0}-1\ (\times 10^{-7})$', fontsize=AXLABEL_FS)
    ax_a.annotate(
        (r'$\max|V/V_{0}-1|$'
         '\n'
         r'$=%.1f\times 10^{-7}$' % drift_max_abs),
        xy=(0.03, 0.05), xycoords='axes fraction',
        fontsize=LEGEND_FS, ha='left', va='bottom')
    style(ax_a)
    add_panel_label(ax_a, '(a)')

    ax_b.plot(x_p, e_r_p, color='tab:blue', linewidth=1.2,
              label=r'$e_{r}=p_{dif,r}^{\prime}-p_{dif,r}^{tar}$')
    ax_b.plot(x_p, e_z_p, color='tab:orange', linewidth=1.2,
              label=r'$e_{z}=p_{dif,z}^{\prime}-p_{dif,z}^{tar}$')
    ax_b.axhline(0.0, color='grey', lw=0.6)
    mark_liquefaction(ax_b, 0.97)
    ax_b.set_xlim(0.0, x_max)
    ax_b.set_ylim(*YLIM_ERR)
    ax_b.set_xlabel(r'$N_{c}/N_{L}$', fontsize=AXLABEL_FS)
    ax_b.set_ylabel(r'$Tracking\ error\ (kPa)$', fontsize=AXLABEL_FS)
    ax_b.legend(fontsize=LEGEND_FS, loc='lower left')
    style(ax_b)
    add_panel_label(ax_b, '(b)')

    plt.tight_layout()
    out_stem.parent.mkdir(parents=True, exist_ok=True)
    pdf = out_stem.with_suffix(".pdf")
    png = out_stem.with_suffix(".png")
    plt.savefig(pdf, bbox_inches='tight')
    plt.savefig(png, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"wrote {pdf}")
    print(f"wrote {png}")
    return pdf, png


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=DEFAULT_CSV)
    ap.add_argument("--out", default=str(LOCAL_OUT))
    ap.add_argument("--no-copy", action="store_true",
                    help="skip copying the output into papers/.../figures/")
    ap.add_argument("--panel-c-only", action="store_true",
                    help="emit only the inertial-number panel as a standalone "
                         "figure (used by the response letter R1.5).")
    ap.add_argument("--panel-stiff-only", action="store_true",
                    help="emit only the wall-stiffness / inertia-ratio panel "
                         "as a standalone figure (used by R2.5).")
    ap.add_argument("--panel-ab-only", action="store_true",
                    help="emit only panels (a) volume drift and (b) tracking "
                         "errors as a standalone figure (used by R2.6).")
    ap.add_argument("--letter-out", default=(
        "/Users/hanyusong/thesis/MicroLiq/papers/cg-coupled-servo/"
        "responses/COMGE-D-26-01109-r1/figs/fig_r1_5"),
                    help="output stem for the letter panel-c figure.")
    ap.add_argument("--letter-stiff-out", default=(
        "/Users/hanyusong/thesis/MicroLiq/papers/cg-coupled-servo/"
        "responses/COMGE-D-26-01109-r1/figs/fig_r2_5"),
                    help="output stem for the letter stiffness-ratio figure.")
    ap.add_argument("--letter-ab-out", default=(
        "/Users/hanyusong/thesis/MicroLiq/papers/cg-coupled-servo/"
        "responses/COMGE-D-26-01109-r1/figs/fig_r2_6"),
                    help="output stem for the letter (a)+(b) figure.")
    args = ap.parse_args()

    if args.panel_c_only:
        make_inertial_panel(args.csv, Path(args.letter_out))
        return
    if args.panel_stiff_only:
        make_stiffness_panel(args.csv, Path(args.letter_stiff_out))
        return
    if args.panel_ab_only:
        make_volume_error_panels(args.csv, Path(args.letter_ab_out))
        return

    pdf, png = make_figure(args.csv, Path(args.out))

    if not args.no_copy:
        for src in (pdf, png):
            dst = PAPER_FIG_DIR / src.name
            shutil.copy2(src, dst)
            print(f"copied -> {dst}")


if __name__ == "__main__":
    main()
