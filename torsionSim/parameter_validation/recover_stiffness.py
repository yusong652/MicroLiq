"""Recover aggregate wall stiffnesses (K_ri, K_ro, K_z) from logged
servo coefficients in a stress-control HollowTorsion run.

The HollowTorsion servo (torsionSim/cyclic_shear/hollow_torsion.py) writes
S_rr, S_rz, S_zr, S_zz alongside geometry. With S_hat = K_hat^{-1} and the
sign convention in compute_servo_coefficients(), the inverse mapping is
closed-form, so K_ri, K_ro, K_z (and the implicit 10% floors) can be
recovered exactly without rerunning the simulation.

K_hat assembly (see hollow_torsion.py:534-552):
    K_hat_11 = -K_ri / A_i  -  (r/R) * K_ro / A_o
    K_hat_12 =  ((R^2 - r^2) / (2 R H)) * K_ro / A_o
    K_hat_21 = -(K_ri - (r/R)*K_ro) / (A_i + A_o)             # consistency check
    K_hat_22 = -K_z / A_z  -  (R^2-r^2) * K_ro / (2 R H * (A_i+A_o))

with A_i = 2 pi r H, A_o = 2 pi R H, A_z = pi (R^2 - r^2).
"""

import argparse
import numpy as np
import pandas as pd


def recover(df: pd.DataFrame) -> pd.DataFrame:
    r = df["rad_inner"].to_numpy()
    R = df["rad_outer"].to_numpy()
    H = df["height"].to_numpy()

    A_i = 2.0 * np.pi * r * H
    A_o = 2.0 * np.pi * R * H
    A_z = np.pi * (R ** 2 - r ** 2)

    Srr = df["S_rr"].to_numpy()
    Srz = df["S_rz"].to_numpy()
    Szr = df["S_zr"].to_numpy()
    Szz = df["S_zz"].to_numpy()

    detS = Srr * Szz - Srz * Szr
    with np.errstate(divide="ignore", invalid="ignore"):
        detK = np.where(detS != 0.0, 1.0 / detS, np.nan)

    K11 = -Szz * detK
    K12 = Srz * detK
    K21 = Szr * detK
    K22 = -Srr * detK

    # K_ro from K12 alone
    K_ro = K12 * (4.0 * np.pi * R ** 2 * H ** 2) / (R ** 2 - r ** 2)
    # K_ri from K11 + K_ro
    K_ri = -2.0 * np.pi * r * H * K11 - (r ** 2 / R ** 2) * K_ro
    # K_z from K22 + K_ro
    K_z = (-np.pi * (R ** 2 - r ** 2) * K22
           - ((R ** 2 - r ** 2) ** 2 * K_ro) /
             (4.0 * R * (r + R) * H ** 2))

    # Consistency: predict K21 from recovered K_ri, K_ro
    K21_pred = -(K_ri - (r / R) * K_ro) / (A_i + A_o)
    K21_resid_rel = np.where(
        np.abs(K21) > 1e-30,
        (K21_pred - K21) / K21,
        K21_pred - K21,
    )

    out = pd.DataFrame({
        "time_duration": df["time_duration"].to_numpy(),
        "K_ri": K_ri,
        "K_ro": K_ro,
        "K_z": K_z,
        "K11": K11,
        "K12": K12,
        "K21": K21,
        "K22": K22,
        "detK": detK,
        "K21_resid_rel": K21_resid_rel,
    })
    return out


def report(df: pd.DataFrame, rec: pd.DataFrame, floor_ratio: float = 0.10) -> None:
    print("=== reverse-engineered aggregate stiffnesses ===")
    # Use first row with non-degenerate detS as initial
    valid = rec["detK"].notna().to_numpy()
    if not valid.any():
        print("no valid rows (det S == 0 throughout)")
        return
    i0 = int(np.argmax(valid))
    K_ri0 = rec["K_ri"].iloc[i0]
    K_ro0 = rec["K_ro"].iloc[i0]
    K_z0 = rec["K_z"].iloc[i0]
    print(f"row{i0}  K_ri0={K_ri0:.3e}  K_ro0={K_ro0:.3e}  K_z0={K_z0:.3e}")

    floor_inner = K_ri0 * floor_ratio
    floor_outer = K_ro0 * floor_ratio
    floor_z = K_z0 * floor_ratio
    print(f"floors (×{floor_ratio:.2f}):  K_ri={floor_inner:.3e}  "
          f"K_ro={floor_outer:.3e}  K_z={floor_z:.3e}")

    print()
    print("--- per-wall extrema and floor engagement ---")
    for label, series, floor, init in [
        ("K_ri", rec["K_ri"], floor_inner, K_ri0),
        ("K_ro", rec["K_ro"], floor_outer, K_ro0),
        ("K_z",  rec["K_z"],  floor_z,     K_z0),
    ]:
        s = series.to_numpy()
        smin = np.nanmin(s)
        smax = np.nanmax(s)
        ratio_min = smin / init
        # how many rows are within 5% of the floor (i.e. clipped or near-clipped)
        near = np.nansum(s <= floor * 1.05)
        total = np.sum(np.isfinite(s))
        print(f"  {label}: min={smin:.3e}  max={smax:.3e}  "
              f"min/init={ratio_min:.3f}  rows≤1.05·floor: {near}/{total}")

    print()
    print("--- K21 self-consistency (should be ~0) ---")
    rs = rec["K21_resid_rel"].abs().to_numpy()
    rs = rs[np.isfinite(rs)]
    if len(rs):
        print(f"  |K21_resid|/|K21|  median={np.median(rs):.2e}  "
              f"max={rs.max():.2e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=(
        "/Users/hanyusong/thesis/MicroLiq/torsionSim/cyclic_shear/"
        "Dr75/k1.00/csr_0.400/torsion_shear.csv"))
    ap.add_argument("--out", default=None,
                    help="optional output CSV with recovered columns")
    ap.add_argument("--floor", type=float, default=0.10)
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    rec = recover(df)
    report(df, rec, floor_ratio=args.floor)
    if args.out:
        rec.to_csv(args.out, index=False)
        print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
