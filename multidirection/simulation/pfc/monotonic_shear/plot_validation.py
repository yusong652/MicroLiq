"""Plot monotonic shear results vs Nakata experimental data.

Uses generalised deviatoric stress and strain:
  q  = sqrt(1/2*[(sx-sy)^2 + (sy-sz)^2 + (sz-sx)^2] + 3*tau_xz^2)
  eq = sqrt(2/9*[(e1-e2)^2 + (e2-e3)^2 + (e3-e1)^2])
       where e1,e2,e3 are principal strains from (ex,ey,ez,gamma_xz)

Usage:
    python plot_validation.py
"""

import sys, os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plot_style import apply_style
apply_style()

# ── Data paths ────────────────────────────────────────────────

HERE = os.path.dirname(__file__)
DEM_CSV = os.path.join(HERE, 'shear.csv')
NAKATA_GAMMA_Q = os.path.join(HERE, 'Nakata_gamma_q_dense.csv')
NAKATA_P_Q = os.path.join(HERE, 'Nakata_p_q_dense.csv')
FIGURES_DIR = os.path.join(HERE, '..', '..', '..',
                           'papers', 'multidirectional-shear', 'figures')

# ── Load data ─────────────────────────────────────────────────

dem = pd.read_csv(DEM_CSV)
dem_sx = dem['stress_x'] / 1e3
dem_sy = dem['stress_y'] / 1e3
dem_sz = dem['stress_z'] / 1e3
dem_tau = dem['shear_stress_x'] / 1e3
dem_p = dem['stress_p'] / 1e3
dem_ex = dem['strain_x']
dem_ey = dem['strain_y']
dem_ez = dem['strain_z']
dem_gamma = dem['shear_strain_x']

# Generalised deviatoric stress
dem_q = np.sqrt(0.5 * ((dem_sx - dem_sy)**2 + (dem_sy - dem_sz)**2 +
                        (dem_sz - dem_sx)**2) + 3 * dem_tau**2)

# Principal strains from (ex, ey, ez, gamma_xz)
dem_R = np.sqrt(((dem_ex - dem_ez) / 2)**2 + (dem_gamma / 2)**2)
dem_e1 = (dem_ex + dem_ez) / 2 + dem_R
dem_e3 = (dem_ex + dem_ez) / 2 - dem_R
dem_e2 = dem_ey

# Deviatoric strain
dem_eq = np.sqrt(2.0/9.0 * ((dem_e1 - dem_e2)**2 + (dem_e2 - dem_e3)**2 +
                              (dem_e3 - dem_e1)**2)) * 100  # to %

nakata_gq = np.loadtxt(NAKATA_GAMMA_Q, delimiter=',')
nakata_pq = np.loadtxt(NAKATA_P_Q, delimiter=',')

# ── Common plot settings ──────────────────────────────────────

exp_kw = dict(marker='o', color='#E24A33', markerfacecolor='white',
              markeredgewidth=0.8, markersize=3.5, linestyle='none',
              label='Nakata (1998)')
dem_kw = dict(color='#348ABD', linewidth=1.2, label='DEM')

# ── (a) Effective stress path: p' - q ─────────────────────────

fig1, ax1 = plt.subplots(figsize=(3.2, 2.8))
ax1.plot(nakata_pq[:, 0], nakata_pq[:, 1], **exp_kw)
ax1.plot(dem_p, dem_q, **dem_kw)
ax1.set_xlabel(r"Mean effective stress $p'$ (kPa)")
ax1.set_ylabel(r'Deviatoric stress $q$ (kPa)')
ax1.set_xlim(0, 200)
ax1.set_ylim(0, 200)
ax1.legend(frameon=False)
ax1.grid(True, linewidth=0.3, alpha=0.5)
fig1.tight_layout(pad=0.3)
fig1.savefig(os.path.join(FIGURES_DIR, 'validation_effective_stress_path.png'),
             dpi=300, bbox_inches='tight')
print("Saved: validation_effective_stress_path.png")

# ── (b) Stress-strain: eq - q ─────────────────────────────────

fig2, ax2 = plt.subplots(figsize=(3.2, 2.8))
ax2.plot(nakata_gq[:, 0], nakata_gq[:, 1], **exp_kw)
ax2.plot(dem_eq, dem_q, **dem_kw)
ax2.set_xlabel(r'Deviatoric strain $\varepsilon_q$ (%)')
ax2.set_ylabel(r'Deviatoric stress $q$ (kPa)')
ax2.set_xlim(0, 2.0)
ax2.set_ylim(0, None)
ax2.legend(frameon=False, loc='lower right')
ax2.grid(True, linewidth=0.3, alpha=0.5)
fig2.tight_layout(pad=0.3)
fig2.savefig(os.path.join(FIGURES_DIR, 'validation_stress_strain.png'),
             dpi=300, bbox_inches='tight')
print("Saved: validation_stress_strain.png")

plt.show()
