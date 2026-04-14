"""Plot GSD comparison: Toyoura sand vs DEM (scaled)."""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..')))
from plot_style import apply_style
from toyoura import TOYOURA_GSD

apply_style()

SCALE_FACTOR = 10.0

DEM_GSD = [(d * SCALE_FACTOR, pct) for d, pct in TOYOURA_GSD]

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
fig.savefig(os.path.join(_HERE, 'grain_size_distribution.png'),
            dpi=300, bbox_inches='tight')
plt.show()

print("DEM GSD control points (diameter mm, finer %):")
for d, pct in DEM_GSD:
    print("  D=%.2f mm  ->  %3.0f%%" % (d, pct))
d50 = np.interp(50, toyoura_pct, toyoura_d)
print("\nD50 (Toyoura) = %.3f mm -> DEM D50 = %.2f mm" % (d50, d50 * SCALE_FACTOR))
print("\nSaved: grain_size_distribution.png")
