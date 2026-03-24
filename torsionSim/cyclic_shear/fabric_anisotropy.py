import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# setting style
k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
markers = ['d', 's', 'o', '^', 'v']
colors = ['tab:orange', 'tab:red', 'tab:blue', 'tab:purple', 'tab:green']
alpha0_values = []  # store initial alpha for inset plot
FS_LABEL = 15
FS_TICK = 14
FS_LEGEND = 14
FS_ANN = 14
FS_INSET = 12

fig1, ax1 = plt.subplots(figsize=(6.0, 5.0))
# inset axes for alpha0 vs K0 (left bottom position)
ax2 = ax1.inset_axes([0.68, 0.74, 0.30, 0.22])

def plot_fabric_anisotropy(k0, color, marker):
	csr = 0.200
	shear_file = BASE_DIR / ("Dr90/k%.2f/csr_%.3f/torsion_shear.csv" % (k0, csr))
	alpha_file = BASE_DIR / ("Dr90/k%.2f/csr_%.3f/alpha_mech.csv" % (k0, csr))

	try:
		df_shear = pd.read_csv(shear_file, header=0)
		df_alpha = pd.read_csv(alpha_file, header=0)
	except FileNotFoundError:
		print(f"File not found for K0={k0}")
		return

	time = df_shear["time_duration"].to_numpy()
	alpha = df_alpha["alpha_mech"].to_numpy()

	# ensure same length
	min_len = min(len(time), len(alpha))
	time = time[:min_len]
	alpha = alpha[:min_len]

	stresses_out = df_shear["stress_outer"].to_numpy()[:min_len] / 1000.
	stresses_in = df_shear["stress_inner"].to_numpy()[:min_len] / 1000.
	stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
	stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini

	# find the index when liquefaction occurs
	period = 1.0 / 8.0
	ind_liq = 0
	while ind_liq < len(stresses_u) and stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	n_liq = time[ind_liq] / period if ind_liq < len(time) else time[-1] / period

	# calculate normalized cycle number
	N_normalized = (time / period) / n_liq

	# filter to N/N_L <= 1.05
	flt = N_normalized <= 1.05

	# plot main curve
	label = r'$K_0=%.1f$' % k0
	ax1.plot(N_normalized[flt][::2], alpha[flt][::2], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		linestyle='-', markersize=9, markevery=0.04*np.log(n_liq*2), label=label)

	# store alpha0 for inset plot
	alpha0_values.append((k0, alpha[0], color, marker))
	print(f"K0={k0}, alpha_0={alpha[0]:.4f}, N_L={n_liq:.1f}")

# plot for each K0
for k0, marker, color in zip(k0s, markers, colors):
	plot_fabric_anisotropy(k0, color, marker)

# plot inset: alpha0 vs K0
for k0, alpha0, color, marker in alpha0_values:
	ax2.scatter([k0], [alpha0], color=color, marker=marker,
		facecolors='None', s=80, linewidths=1.5)

# main axes settings
legend1 = ax1.legend(title=r'$Initial\ K_0\ in\ cyclic\ shear$', title_fontsize=FS_LEGEND,
	fontsize=FS_LEGEND, ncol=3, framealpha=0.2, columnspacing=0.8,
	loc=(-0.0, 1.02), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Fabric\ anisotropy\ indicator\ \alpha$', fontsize=FS_LABEL)
ax1.set_xlabel(r'$Normalized\ number\ of\ cycles\ N/N_L$', fontsize=FS_LABEL)
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.tick_params(axis='both', which='major', labelsize=FS_TICK)
ax1.set_xlim(0, 1.05)
ax1.set_ylim(-0.08, 0.16)
ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
plt.annotate(r"$CSR=0.200$", xy=(0.2, 0.10), fontsize=FS_ANN)

# inset axes settings
ax2.set_ylabel(r'$\alpha_{0}$', fontsize=FS_INSET)
ax2.set_xlabel(r'$K_0$', fontsize=FS_INSET)
ax2.tick_params(axis='both', which='both', labelsize=FS_INSET)
ax2.set_xscale('log')
ax2.set_xticks([0.5, 1.0, 2.0])
ax2.set_xticklabels(['0.5', '1.0', '2.0'])
ax2.xaxis.set_minor_formatter(plt.NullFormatter())
ax2.set_xlim(0.3, 3.0)
ax2.set_ylim(-0.08, 0.10)
ax2.set_yticks([-0.05, 0, 0.05])
ax2.set_yticklabels(['-0.05', '0', '0.05'])
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.savefig(BASE_DIR / "fabric_anisotropy.png", dpi=350)
plt.show()
