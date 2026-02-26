import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

k0s = [0.5, 1.0, 2.0]
markers = ['d', 'o', 'v']
colors = ['tab:orange', 'tab:blue', 'tab:green']
FS_LABEL = 15
FS_TICK = 14
FS_LEGEND = 14
FS_ANN = 14

fig1 = plt.figure(figsize=(6.0, 4.5))
ax1 = plt.gca()

def plot_normalized_ru(k0, color, marker, csr=0.200):
	file_name = BASE_DIR / ("Dr90/k%.2f/csr_%.3f/torsion_shear.csv" % (k0, csr))
	try:
		df1 = pd.read_csv(file_name, header=0)
	except FileNotFoundError:
		print("File not found:", file_name)
		return

	stresses_shear = df1["stress_shear"] / 1000.
	stresses_out = df1["stress_outer"] / 1000.
	stresses_in = df1["stress_inner"] / 1000.
	stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
	stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini
	time = df1["time_duration"]

	period = 1.0 / 8.0
	ind_liq = 0
	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	n_liq = time[ind_liq] / period
	cycles = time / period
	cycles_norm = cycles / n_liq
	EPWP_ratios = stresses_u / stress_ini

	flt = cycles_norm < 1.06

	ax1.plot(cycles_norm[flt], EPWP_ratios[flt], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=0.012 * np.log(n_liq * 2), markersize=9,
		label=r"$%.2f$" % (k0),
		)

for k0, marker, color in zip(k0s, markers, colors):
	plot_normalized_ru(k0, color, marker)

legend1 = ax1.legend(
	title=r'$Initial\ K_0\ in\ cyclic\ shear$', title_fontsize=FS_LEGEND,
	fontsize=FS_LEGEND, ncol=3, framealpha=0.2, columnspacing=0.05,
	loc=(-0.00, 1.02), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$EPWP\ ratio\ r_u$', fontsize=FS_LABEL)
ax1.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$',
	fontsize=FS_LABEL)
ax1.tick_params(axis='both', which='major', labelsize=FS_TICK)
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.axhline(y=0.95, color='tab:red', linestyle='dashed', linewidth=1.2)
ax1.text(-0.08, 0.92, r"$0.95$", color='tab:red', fontsize=FS_ANN)
ax1.set_xlim(0, 1.05)
plt.annotate(r"$CSR=0.200$", xy=(0.25, 0.45), fontsize=FS_ANN)
plt.tight_layout()
plt.savefig(BASE_DIR / "normalized_ru.png", dpi=350)
plt.show()
