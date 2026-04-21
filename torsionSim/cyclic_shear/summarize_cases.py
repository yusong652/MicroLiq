"""Summarize all cyclic-shear cases (Dr, K0, CSR) with N_L for the R1.4 case table.

N_L criterion: first cycle where excess pore pressure ratio r_u = u/sigma_r0' >= 0.95.
Period = 1/8 s (loading frequency 8 Hz in DEM time).
"""
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
PERIOD = 1.0 / 8.0

PRIMARY_CSRS = [0.200, 0.250, 0.300, 0.350, 0.400]
EXPANDED_CSR = 0.300
PRIMARY_K0 = [0.50, 1.00, 2.00]
EXPANDED_K0 = [0.50, 0.67, 1.00, 1.50, 2.00]

rows = []

for dr_key, dr_label in [("Dr90", 90), ("Dr75", 75)]:
    k0_list = PRIMARY_K0 if dr_key == "Dr90" else EXPANDED_K0
    k0_list_used = EXPANDED_K0 if dr_key == "Dr90" else EXPANDED_K0  # Dr90 has all 5
    for k0 in EXPANDED_K0:
        csr_list = (
            PRIMARY_CSRS if (dr_key == "Dr90" and k0 in PRIMARY_K0) else [EXPANDED_CSR]
        )
        for csr in csr_list:
            f = BASE / dr_key / f"k{k0:.2f}" / f"csr_{csr:.3f}" / "torsion_shear.csv"
            if not f.exists():
                rows.append({"Dr": dr_label, "K0": k0, "CSR": csr, "N_L": None, "note": "missing"})
                continue
            df = pd.read_csv(f)
            stresses_out = df["stress_outer"].to_numpy() / 1000.0
            stresses_in = df["stress_inner"].to_numpy() / 1000.0
            stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
            u = -(stresses_in + stresses_out) / 2 + stress_ini
            time = df["time_duration"].to_numpy()
            threshold = 0.95 * stress_ini
            ind = 0
            while ind < len(u) and u[ind] < threshold:
                ind += 1
            if ind >= len(time):
                n_liq = None
                note = "not reached"
            else:
                n_liq = time[ind] / PERIOD
                note = ""
            rows.append({"Dr": dr_label, "K0": k0, "CSR": csr, "N_L": n_liq, "note": note})

out = pd.DataFrame(rows).sort_values(["Dr", "K0", "CSR"], ascending=[False, True, True])
print(out.to_string(index=False, float_format=lambda x: f"{x:.2f}" if pd.notna(x) else "-"))
print(f"\nTotal cases: {len(out)} ({(out['N_L'].notna()).sum()} with N_L)")
