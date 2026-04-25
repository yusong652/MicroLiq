"""Plot reverse-engineered aggregate stiffnesses against the
end-of-consolidation values, with the per-quantity safety floors
(10% on K_ri, K_ro, K_z; 20% on moment_inertial).

Used for the R2.5 stability validation in the COMGE-D-26-01109 r1
response letter.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from recover_stiffness import recover

DEFAULT_CSV = (
    "/Users/hanyusong/thesis/MicroLiq/torsionSim/cyclic_shear/"
    "Dr75/k1.00/csr_0.400/torsion_shear.csv"
)
DEFAULT_OUT = (
    "/Users/hanyusong/thesis/MicroLiq/papers/cg-coupled-servo/"
    "responses/COMGE-D-26-01109-r1/figs/fig_r2_5_floors.pdf"
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=DEFAULT_CSV)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--stiff-floor", type=float, default=0.10)
    ap.add_argument("--inertia-floor", type=float, default=0.20)
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    rec = recover(df)

    t = rec["time_duration"].to_numpy()

    # Initial values: first row with valid detS
    valid = rec["detK"].notna().to_numpy()
    i0 = int(np.argmax(valid))
    K_ri0 = rec["K_ri"].iloc[i0]
    K_ro0 = rec["K_ro"].iloc[i0]
    K_z0 = rec["K_z"].iloc[i0]
    I0 = df["moment_inertial"].iloc[i0]
    p0 = df["stress_p"].iloc[i0]

    # Ratios
    Kri_r = rec["K_ri"].to_numpy() / K_ri0
    Kro_r = rec["K_ro"].to_numpy() / K_ro0
    Kz_r = rec["K_z"].to_numpy() / K_z0
    I_r = df["moment_inertial"].to_numpy() / I0

    # Stress context
    p_r = df["stress_p"].to_numpy() / p0
    ru = 1.0 - p_r

    # ---------- figure ----------
    fig, axes = plt.subplots(
        3, 1, figsize=(7.0, 7.5), sharex=True,
        gridspec_kw={"height_ratios": [1.0, 1.6, 1.2]})

    # (a) excess pore-pressure ratio
    ax = axes[0]
    ax.plot(t, ru, color="tab:red", lw=1.2, label=r"$r_u = 1 - p'/p_0'$")
    ax.axhline(0.95, color="0.4", lw=0.8, ls=":")
    ax.text(t[-1] * 0.99, 0.93, r"$r_u = 0.95$ (liquefaction)",
            ha="right", va="top", color="0.3", fontsize=9)
    ax.set_ylabel(r"$r_u$")
    ax.set_ylim(-0.05, 1.05)
    ax.set_title(
        r"Dr$\approx$75%, $K_0=1.0$, CSR=0.400, "
        r"total-stress-controlled axial boundary",
        fontsize=10)
    ax.grid(alpha=0.3)

    # (b) radial / axial-cylinder / end-platen aggregate stiffnesses
    ax = axes[1]
    ax.plot(t, Kri_r, label=r"$K_{r,i}/K_{r,i}^{(0)}$",
            color="tab:blue", lw=1.0)
    ax.plot(t, Kro_r, label=r"$K_{r,o}/K_{r,o}^{(0)}$",
            color="tab:orange", lw=1.0)
    ax.plot(t, Kz_r, label=r"$K_{z}/K_{z}^{(0)}$",
            color="tab:green", lw=1.0)
    ax.axhline(args.stiff_floor, color="0.2", lw=1.0, ls="--",
               label=f"floor = {args.stiff_floor:.2f}")
    ax.set_ylabel("aggregate wall stiffness ratio")
    ax.set_ylim(0.0, 1.05)
    ax.legend(loc="lower left", fontsize=9, ncol=2)
    ax.grid(alpha=0.3)

    # annotate observed minima
    for label, arr, color in [
        (r"$K_{r,i}$", Kri_r, "tab:blue"),
        (r"$K_{r,o}$", Kro_r, "tab:orange"),
        (r"$K_{z}$", Kz_r, "tab:green"),
    ]:
        imin = int(np.nanargmin(arr))
        ax.plot(t[imin], arr[imin], "o", color=color, ms=4, zorder=5)

    # (c) torsional moment of inertia
    ax = axes[2]
    ax.plot(t, I_r, color="tab:purple", lw=1.0,
            label=r"$I_{\rm rot}/I_{\rm rot}^{(0)}$")
    ax.axhline(args.inertia_floor,
               color="0.2", lw=1.0, ls="--",
               label=f"floor = {args.inertia_floor:.2f}")
    ax.set_ylabel("torsional inertia ratio")
    ax.set_xlabel(r"time $t$ (s)")
    ax.set_ylim(0.0, 1.05)
    ax.legend(loc="lower left", fontsize=9)
    ax.grid(alpha=0.3)

    # mark contact with the inertia floor
    eps = 1e-3
    binding = I_r <= (args.inertia_floor + eps)
    if binding.any():
        # shade binding region(s)
        in_block = False
        for k in range(len(t)):
            if binding[k] and not in_block:
                t0 = t[k]
                in_block = True
            elif (not binding[k]) and in_block:
                ax.axvspan(t0, t[k], color="tab:purple", alpha=0.08)
                in_block = False
        if in_block:
            ax.axvspan(t0, t[-1], color="tab:purple", alpha=0.08)

    fig.tight_layout()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight")
    fig.savefig(out.with_suffix(".png"), dpi=180, bbox_inches="tight")
    print(f"wrote {out}")
    print(f"      {out.with_suffix('.png')}")


if __name__ == "__main__":
    main()
