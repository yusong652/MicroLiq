"""Quick diagnostic: DEM CSR-N_L at D_r=75%, K0=1.0 vs Ishihara (1985)
digitized reference — fitted curve in the style of the original figure."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = "/Users/hanyusong/thesis/MicroLiq/torsionSim/cyclic_shear"
REF = "/Users/hanyusong/thesis/MicroLiq/torsionSim/parameter_validation/undrained_cyclic"


def compute_NL(csv_path, freq_hz=8.0, gamma_threshold=2.5):
    df = pd.read_csv(csv_path)
    gamma = df["strain_shear"] * 2.0 * 100.0           # engineering shear strain, %
    t = df["time_duration"]
    mask = np.abs(gamma) > gamma_threshold
    if not mask.any():
        return np.nan
    idx = int(np.argmax(mask))
    return float(t.iloc[idx]) * freq_hz


csrs_dem = [0.200, 0.250, 0.300]
nl_dem = [compute_NL(f"{BASE}/Dr75/k1.00/csr_{c:.3f}/torsion_shear.csv") for c in csrs_dem]

ref = pd.read_csv(f"{REF}/hca_Ishihara_Dr75.csv", header=None).to_numpy()
N_ref = ref[:, 0]
CSR_ref = ref[:, 1]

# Power-law fit in log-log space, all points included (matching Ishihara's
# original faired curve)
slope, intercept = np.polyfit(np.log10(N_ref), np.log10(CSR_ref), 1)
N_curve = np.logspace(np.log10(0.8), np.log10(500), 200)
CSR_curve = 10 ** (intercept + slope * np.log10(N_curve))

print(f"Ishihara Dr=75% power-law fit: CSR = {10**intercept:.4f} * N^{slope:.4f}")
print("DEM Dr=75%:", list(zip(csrs_dem, nl_dem)))

fig, ax = plt.subplots(figsize=(6.2, 5.0))

ax.scatter(ref[:, 0], ref[:, 1], marker='s', facecolors='none',
           edgecolors='tab:green', linewidths=1.2, s=80,
           label=r'Ishihara 1985 ($D_r\approx75\%$)')
ax.scatter(nl_dem, csrs_dem, marker='o', color='tab:blue', s=95,
           label=r'DEM simulation')

ax.set_xscale('log')
ax.set_xlim(0.7, 500)
ax.set_ylim(0.0, 0.6)
ax.set_xlabel(r'Number of cycles to liquefaction $N_L$', fontsize=13)
ax.set_ylabel(r'Cyclic stress ratio $\tau_{z\theta,\max}/p_0^\prime$', fontsize=13)
ax.grid(True, which='major', color='grey', linestyle='--', lw=0.35, alpha=0.8)
ax.legend(fontsize=11, loc='upper right')
ax.annotate(r'$D_r\approx75\%$, $K_0=1.0$, $\gamma_{SA}=2.5\%$',
            xy=(0.02, 0.02), xycoords='axes fraction', fontsize=11)

plt.tight_layout()
plt.savefig('/Users/hanyusong/thesis/MicroLiq/torsionSim/parameter_validation/validate_Dr75_check.png',
            dpi=150, bbox_inches='tight')
print("Saved validate_Dr75_check.png")
