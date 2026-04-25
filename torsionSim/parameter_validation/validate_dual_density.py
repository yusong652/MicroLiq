"""Dual-density validation: DEM CSR-N_L at K0=1.0 for both D_r ~ 90% and
D_r ~ 75%, overlaid with Ishihara (1985) digitized reference data for the
very dense (88-95%) and dense (75-82%) bands."""
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


csrs_dr90 = [0.200, 0.250, 0.300, 0.350, 0.400]
nl_dr90 = [compute_NL(f"{BASE}/Dr90/k1.00/csr_{c:.3f}/torsion_shear.csv") for c in csrs_dr90]

csrs_dr75 = [0.200, 0.250, 0.300]
nl_dr75 = [compute_NL(f"{BASE}/Dr75/k1.00/csr_{c:.3f}/torsion_shear.csv") for c in csrs_dr75]

ref_vd = pd.read_csv(f"{REF}/hca_Ishihara_Dr90.csv", header=None).to_numpy()
ref_d = pd.read_csv(f"{REF}/hca_Ishihara_Dr75.csv", header=None).to_numpy()

print("DEM Dr=90%:", list(zip(csrs_dr90, nl_dr90)))
print("DEM Dr=75%:", list(zip(csrs_dr75, nl_dr75)))

fig, ax = plt.subplots(figsize=(7.0, 5.2))

ax.scatter(ref_vd[:, 0], ref_vd[:, 1], marker='s', facecolors='none',
           edgecolors='tab:blue', linewidths=1.3, s=85,
           label=r'Ishihara 1985, very dense ($D_r = 88\!-\!95\%$)')
ax.scatter(ref_d[:, 0], ref_d[:, 1], marker='s', facecolors='none',
           edgecolors='tab:orange', linewidths=1.3, s=85,
           label=r'Ishihara 1985, dense ($D_r = 75\!-\!82\%$)')

ax.scatter(nl_dr90, csrs_dr90, marker='o', color='tab:blue', s=95,
           label=r'DEM $D_r \approx 90\%$')
ax.scatter(nl_dr75, csrs_dr75, marker='o', color='tab:orange', s=95,
           label=r'DEM $D_r \approx 75\%$')

ax.set_xscale('log')
ax.set_xlim(0.7, 500)
ax.set_ylim(0.0, 0.6)
ax.set_xlabel(r'Number of cycles to liquefaction $N_L$', fontsize=13)
ax.set_ylabel(r'Cyclic stress ratio $\tau_{z\theta,\max}/p_0^\prime$', fontsize=13)
ax.grid(True, which='major', color='grey', linestyle='--', lw=0.35, alpha=0.8)
ax.legend(fontsize=10, loc='upper right')
ax.annotate(r'$K_0=1.0$, $\gamma_{SA}=2.5\%$',
            xy=(0.02, 0.02), xycoords='axes fraction', fontsize=11)

plt.tight_layout()
plt.savefig('/Users/hanyusong/thesis/MicroLiq/torsionSim/parameter_validation/validate_dual_density.png',
            dpi=150, bbox_inches='tight')
print("Saved validate_dual_density.png")
