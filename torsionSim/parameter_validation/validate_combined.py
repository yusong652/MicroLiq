import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15.0, 4.9))


def add_panel_label(ax, label):
	# Place panel labels just outside the axes frame to avoid overlap with
	# legends/curves while keeping descriptive subcaptions in LaTeX.
	ax.text(
		-0.0, 1.005, label,
		transform=ax.transAxes,
		ha='left', va='bottom',
		fontsize=16, fontweight='bold',
		clip_on=False
	)

# ======================================================================
# (a) Effective stress path: p'-q (dilatancy)
# ======================================================================
df1 = pd.read_csv("undrained_monotonic/monotonic_dense/torsion_shear.csv", header=0)
df2 = pd.read_csv("undrained_monotonic/Nakata_p_q_dense.csv", header=None)

stresses_shear = df1["stress_shear"] / 1000.
stresses_out = df1["stress_outer"] / 1000.
stresses_in = df1["stress_inner"] / 1000.
rads_out = df1["rad_outer"]
rads_inner = df1["rad_inner"]
stresses_rad = (stresses_out * rads_out + stresses_in * rads_inner) / (rads_out + rads_inner)
stresses_cir = (stresses_out * rads_out - stresses_in * rads_inner) / (rads_out - rads_inner)
stresses_z = df1["stress_z"] / 1000.0
stresses_1 = (stresses_z + stresses_cir) / 2.0 + np.sqrt(((stresses_z - stresses_cir)/2.0)**2 + stresses_shear**2)
stresses_2 = stresses_rad
stresses_3 = (stresses_z + stresses_cir) / 2.0 - np.sqrt(((stresses_z - stresses_cir)/2.0)**2 + stresses_shear**2)
stresses_p = (stresses_in + stresses_out + stresses_z) / 3.0
stresses_dev = np.sqrt(0.5*((stresses_1 - stresses_2)**2 + (stresses_1 - stresses_3)**2 + (stresses_3 - stresses_2)**2))
time = df1["time_duration"]

stresses_p_ref = df2.to_numpy()[:, 0]
stresses_q_ref = df2.to_numpy()[:, 1]

flt = time < 1.86
ax1.plot(stresses_p[flt], stresses_dev[flt], linewidth=1.6,
	label=r'$DEM\ simulation$', color='tab:blue')
ax1.plot(stresses_p_ref, stresses_q_ref, label=r'$Nakata\ et\ al.,\ 1998$',
	color='tab:green', marker='s', markersize=7, markerfacecolor='None',
	markeredgewidth=1.2, linewidth=1.2, markevery=2)
ax1.set_xlim(0.0, 200.0)
ax1.set_ylim(0, 200)
ax1.set_xlabel(r"$Mean\ effective\ stress\ p'\ (kPa)$", fontsize=18)
ax1.set_ylabel(r'$Deviatoric\ stress\ q\ (kPa)$', fontsize=18)
ax1.legend(fontsize=14, loc='upper left')
ax1.tick_params(axis='both', which='major', labelsize=15)
ax1.grid(axis='both', which='major', color='grey', linestyle='--', lw=0.35, alpha=0.8)
add_panel_label(ax1, "(a)")

# ======================================================================
# (b) Stress-strain relationship (stiffness)
# ======================================================================
df3 = pd.read_csv("undrained_monotonic/Nakata_gamma_q_dense.csv", header=None)
strains_dev = df1["strain_dev"] * 100.0

strains_dev_ref = df3.to_numpy()[:, 0]
stresses_q_ref2 = df3.to_numpy()[:, 1]

flt2 = time < 1.0
ax2.plot(strains_dev[flt2], stresses_dev[flt2], linewidth=1.6,
	label=r'$DEM\ simulation$', color='tab:blue')
ax2.plot(strains_dev_ref, stresses_q_ref2, label=r'$Nakata\ et\ al.,\ 1998$',
	color='tab:green', marker='s', markersize=7, markerfacecolor='None',
	markeredgewidth=1.2, linewidth=1.2, markevery=2)
ax2.set_xlim(0.0, 2.0)
ax2.set_ylim(0, 200)
ax2.set_xlabel(r'$Deviatoric\ strain\ \epsilon_q\ (\%)$', fontsize=18)
ax2.set_ylabel(r'$Deviatoric\ stress\ q\ (kPa)$', fontsize=18)
ax2.legend(fontsize=14, loc='lower right')
ax2.tick_params(axis='both', which='major', labelsize=15)
ax2.grid(axis='both', which='major', color='grey', linestyle='--', lw=0.35, alpha=0.8)
add_panel_label(ax2, "(b)")

# ======================================================================
# (c) CSR vs N_L (cyclic liquefaction resistance)
# ======================================================================
csrs = [0.200, 0.250, 0.300, 0.350, 0.400]
cycles = []
for csr in csrs:
	df_c = pd.read_csv(f"undrained_cyclic/cyclic_dense/csr_{csr:.3f}/torsion_shear.csv", header=0)
	# strain_shear in CSV is tensorial shear strain epsilon_ztheta; gamma = 2 * epsilon
	epsilon_c = df_c["strain_shear"] * 100.0
	gamma_c = epsilon_c * 2.0
	threshold = 2.5  # gamma_SA = 2.5%
	index = np.argmax(abs(gamma_c) > threshold)
	time_c = df_c["time_duration"][index]
	cycle = time_c * 8.0
	cycles.append(cycle)

df_exp = pd.read_csv("undrained_cyclic/hca_Ishihara_Dr90.csv", header=None)
n_ref = df_exp.to_numpy()[:, 0]
csr_ref = df_exp.to_numpy()[:, 1]

ax3.scatter(cycles, csrs, label=r'$DEM\ simulation$',
	marker='o', color='tab:blue', s=86)
ax3.scatter(n_ref, csr_ref, label=r'$Ishihara\ et\ al.,\ 1985$',
	marker='s', facecolors='None', edgecolors='tab:green', linewidths=1.2, s=86)
ax3.set_xlim(1, 500.0)
ax3.set_ylim(0.10, 0.50)
ax3.set_xscale("log")
ax3.set_xlabel(r'$Number\ of\ cyclic\ loading\ N_{L}$', fontsize=18)
ax3.set_ylabel(r'$Cyclic\ stress\ ratio\ \tau_{z\theta,max}/p^\prime_{0}$', fontsize=18)
ax3.legend(fontsize=14)
ax3.tick_params(axis='both', which='major', labelsize=15)
ax3.grid(axis='both', which='major', color='grey', linestyle='--', lw=0.35, alpha=0.8)
ax3.annotate(r'$Liquefaction\ criterion:\ \gamma_{SA}=2.5\%$',
	xy=(0.98, 0.02), xycoords='axes fraction',
	fontsize=13, ha='right', va='bottom')
add_panel_label(ax3, "(c)")

plt.tight_layout()
plt.savefig("validate_combined.pdf", bbox_inches="tight")
plt.savefig("validate_combined.png", dpi=700, bbox_inches="tight")
plt.show()
