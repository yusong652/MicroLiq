"""Plot GSD comparison: Toyoura sand vs DEM (×10 scaling).

Edit the TOYOURA_GSD control points below, then run to compare.
Once satisfied, the DEM_GSD will be used for particle generation.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import matplotlib.pyplot as plt
from plot_style import apply_style
apply_style()

# ── Control points: (particle diameter mm, percentage finer %) ──
TOYOURA_GSD = [
    (0.10,   0),
    (0.125,   5),
    (0.15,  10),
    (0.1638,  20),
    (0.18,  30),
    (0.20,  40),
    (0.21,  50),
    (0.225,  60),
    (0.24,  70),
    (0.26,  80),
    (0.30,  90),
    (0.34,  95),
    (0.38, 100),
]

SCALE_FACTOR = 10.0  # DEM = Toyoura × 10

# ── Derived DEM GSD ──
DEM_GSD = [(d * SCALE_FACTOR, pct) for d, pct in TOYOURA_GSD]

# ── Plot ──
fig, ax = plt.subplots(figsize=(3.5, 2.8))

toyoura_d = [p[0] for p in TOYOURA_GSD]
toyoura_pct = [p[1] for p in TOYOURA_GSD]
dem_d = [p[0] for p in DEM_GSD]
dem_pct = [p[1] for p in DEM_GSD]

ax.semilogx(toyoura_d, toyoura_pct, 'o-', color='#E24A33',
            markerfacecolor='white', markeredgewidth=0.8,
            label='Toyoura sand')
ax.semilogx(dem_d, dem_pct, 's-', color='#348ABD',
            markerfacecolor='white', markeredgewidth=0.8,
            label=r'DEM ($\times$%g)' % SCALE_FACTOR)

ax.set_xlabel('Particle size (mm)')
ax.set_ylabel('Percentage finer (%)')
ax.set_xlim(0.01, 50)
ax.set_ylim(0, 105)
ax.grid(True, which='both', linewidth=0.3, alpha=0.5)
ax.legend(loc='upper left', frameon=False)

fig.tight_layout(pad=0.3)
fig.savefig('grain_size_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Print DEM GSD info
print("DEM GSD control points (diameter mm, finer %):")
for d, pct in DEM_GSD:
    print("  D=%.2f mm  ->  %3.0f%%" % (d, pct))
d50 = np.interp(50, toyoura_pct, toyoura_d)
print("\nD50 (Toyoura) = %.3f mm -> DEM D50 = %.2f mm" % (d50, d50 * SCALE_FACTOR))
print("\nSaved: grain_size_distribution.png")
