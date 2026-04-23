"""
Figure for R1.1 prong (3) — HCA geometric argument.

Loads the Blender element-detail render as the canvas and overlays
  (i) τ_{zθ} shear-stress arrows on the z-face (top) and θ-face (side),
 (ii) a cylindrical coordinate triad (r, θ, z) anchored below the wedge,
(iii) side text listing the axial and circumferential specimen/d_max ratios.

Image-space positions are pre-computed from the Blender camera
(world_to_camera_view), so the overlay sits precisely on the rendered
faces without re-rendering anything.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import FancyArrowPatch
from matplotlib.gridspec import GridSpec


# ─── Style ───
# Figure aspect ≈ 2.2 (wider than fig_r1_1's 1.84) so it renders SHORTER
# than Figure 1 when both are included at \linewidth.  Text is bumped
# to compensate for the extra scale-down in the letter.
plt.rcParams.update({
    'text.usetex':     True,
    'font.family':     'serif',
    'font.size':       15,
    'axes.linewidth':  0.6,
})

C_STRESS = '#222222'     # τ_{zθ} arrows + baselines
C_R      = '#D6604D'     # r̂ (red)  — radial
C_TH     = '#2166AC'     # θ̂ (blue) — circumferential
C_Z      = '#2166AC'     # ẑ (blue) — axial


# ─── Projected 2D positions (u,v in [0,1], (0,0)=top-left of image) ───
# τ_{zθ} on TOP (z = +Z_HALF): straight 3D segments of uniform length
# (10 mm), all pointing in the tangential (+θ̂ at θ=0 ≡ +Y) direction.
# Tails distributed along the radial line from r_in to r_out.
TOP_ARROWS = [
    ((0.4282, 0.2692), (0.4895, 0.2264)),
    ((0.4934, 0.2799), (0.5521, 0.2360)),
    ((0.5602, 0.2908), (0.6162, 0.2458)),
    ((0.6149, 0.2997), (0.6686, 0.2538)),
]
# τ_{zθ} on θ-face at θ = −θ_half (camera-visible cut),
# arrows in −ẑ direction (downward), uniform Δz = 10 mm.
SIDE_ARROWS = [
    ((0.3268, 0.4813), (0.3317, 0.5906)),
    ((0.3763, 0.5043), (0.3799, 0.6156)),
    ((0.4281, 0.5282), (0.4302, 0.6416)),
    ((0.4711, 0.5482), (0.4720, 0.6632)),
]
# Coordinate triad, anchored just outside the wedge (lower-front corner)
TRIAD_O  = (0.81, 0.6)
TRIAD_R  = (0.905, 0.62)
TRIAD_TH = (0.88, 0.55)
TRIAD_Z  = (0.81, 0.5)


# ─── Load the Blender render ───
HERE = os.path.dirname(os.path.abspath(__file__))
img  = mpimg.imread(os.path.join(HERE, '..', 'rcell_detail.png'))


# ─── Figure layout ───
# Wider aspect → figure renders shorter at \linewidth than fig_r1_1.
fig = plt.figure(figsize=(10.0, 4.5))
gs  = GridSpec(1, 2, width_ratios=[1.0, 0.65], wspace=0.02,
               left=0.01, right=0.99, top=0.98, bottom=0.02)

ax_img = fig.add_subplot(gs[0])
ax_img.imshow(img, extent=[0, 1, 1, 0])
ax_img.set_xlim(0, 1); ax_img.set_ylim(1, 0)
ax_img.set_aspect('equal'); ax_img.axis('off')


def arrow(ax, tail, head, color, lw=1.0, ms=10):
    ax.add_patch(FancyArrowPatch(tail, head,
                                 arrowstyle='-|>',
                                 mutation_scale=ms,
                                 color=color, linewidth=lw,
                                 shrinkA=0, shrinkB=0))


# Stress arrows on TOP face + tail baseline
for t, h in TOP_ARROWS:
    arrow(ax_img, t, h, C_STRESS, lw=1.3, ms=13)
top_tails = np.array([a[0] for a in TOP_ARROWS])
ax_img.plot(top_tails[:, 0], top_tails[:, 1], color=C_STRESS, lw=1.0)

# Stress arrows on θ-face (side) + tail baseline
for t, h in SIDE_ARROWS:
    arrow(ax_img, t, h, C_STRESS, lw=1.3, ms=13)
side_tails = np.array([a[0] for a in SIDE_ARROWS])
ax_img.plot(side_tails[:, 0], side_tails[:, 1], color=C_STRESS, lw=1.0)

# τ_{zθ} label near the last top-face arrow
last_top_head = TOP_ARROWS[-1][1]
ax_img.text(last_top_head[0] - 0.12, last_top_head[1] - 0.06,
            r'$\tau_{z\theta}$', color=C_STRESS,
            fontsize=18, ha='left', va='center')

# Coordinate triad arrows
arrow(ax_img, TRIAD_O, TRIAD_R,  C_R,  lw=2.0, ms=18)
arrow(ax_img, TRIAD_O, TRIAD_TH, C_TH, lw=2.0, ms=18)
arrow(ax_img, TRIAD_O, TRIAD_Z,  C_Z,  lw=2.0, ms=18)
ax_img.text(TRIAD_R[0] + 0.025, TRIAD_R[1] + 0.005, r'$r$',
            color=C_R, fontsize=18, ha='center', va='center')
ax_img.text(TRIAD_TH[0] + 0.022, TRIAD_TH[1] - 0.015, r'$\theta$',
            color=C_TH, fontsize=18, ha='center', va='center')
ax_img.text(TRIAD_Z[0] - 0.025, TRIAD_Z[1] - 0.005, r'$z$',
            color=C_Z, fontsize=18, ha='center', va='center')


# ─── Right side: text annotations ───
ax_txt = fig.add_subplot(gs[1])
ax_txt.axis('off')
ax_txt.set_xlim(0, 1); ax_txt.set_ylim(0, 1)

ax_txt.text(0.00, 0.88, r'\textit{axial} ($z$):',
            fontsize=15, transform=ax_txt.transAxes)
ax_txt.text(0.05, 0.81,
            r'$H = 100\,\mathrm{mm} \approx 33\,d_{\max}$',
            fontsize=15, transform=ax_txt.transAxes)

ax_txt.text(0.00, 0.67, r'\textit{circumferential} ($\theta$):',
            fontsize=15, transform=ax_txt.transAxes)
ax_txt.text(0.05, 0.60,
            r'$\pi (r + R) \approx 251\,\mathrm{mm} \approx 84\,d_{\max}$',
            fontsize=15, transform=ax_txt.transAxes)

ax_txt.text(0.00, 0.38,
            r'\textit{$\tau_{z\theta}$ acts in the $(z,\theta)$ plane,}',
            fontsize=14, transform=ax_txt.transAxes, color='0.35')
ax_txt.text(0.00, 0.32,
            r'\textit{orthogonal to the radial direction.}',
            fontsize=14, transform=ax_txt.transAxes, color='0.35')


# ─── Save ───
out_pdf = os.path.join(HERE, 'fig_r1_1_shearplane.pdf')
plt.savefig(out_pdf, bbox_inches='tight', pad_inches=0.05)
print(f'Saved: {out_pdf}')
