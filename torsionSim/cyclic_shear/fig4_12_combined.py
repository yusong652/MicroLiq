import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
markers = ['d', 's', 'o', '^', 'v']
colors = ['tab:orange', 'tab:red', 'tab:blue', 'tab:purple', 'tab:green']

fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.5))
ax_a, ax_b, ax_c = axes


def compute_and_plot(k0, color, marker, csr=0.200):
	file_name = "Dr90/k%.2f/csr_%.3f/torsion_shear.csv" % (k0, csr)
	try:
		df1 = pd.read_csv(file_name, header=0)
	except FileNotFoundError:
		return

	stresses_shear = df1["stress_shear"] / 1000.
	stresses_out = df1["stress_outer"] / 1000.
	stresses_in = df1["stress_inner"] / 1000.
	stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
	stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini
	time = df1["time_duration"]
	strains = df1["strain_shear"]
	acc_ene = np.zeros(len(strains))
	for i in range(len(strains) - 1):
		acc_ene[i + 1] = acc_ene[i] + (strains[i + 1] - strains[i]) * stresses_shear[i]

	period = 1.0 / 8.0
	ind_liq = 0
	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	n_liq = time[ind_liq] / period
	cycles = time / period
	cycles_norm = cycles / n_liq
	EPWP_ratios = stresses_u / stress_ini
	ws_liq = acc_ene[ind_liq]
	flt = cycles_norm < 1.06
	mevery = 0.012 * np.log(n_liq * 2)
	label = r"$%.2f$" % k0

	# (a) r_u vs N_c/N_L
	ax_a.plot(cycles_norm[flt], EPWP_ratios[flt], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=mevery, markersize=9, label=label)

	# (b) W_s vs N_c/N_L
	ax_b.plot(cycles_norm[flt], acc_ene[flt], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=mevery, markersize=9, label=label)

	# (c) r_u vs W_s
	ax_c.plot(acc_ene[flt], EPWP_ratios[flt], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=mevery, markersize=9, label=label)


for k0, marker, color in zip(k0s, markers, colors):
	compute_and_plot(k0, color, marker)

# (a) formatting
ax_a.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$', fontsize=13)
ax_a.set_ylabel(r'$EPWP\ ratio\ r_u$', fontsize=13)
ax_a.tick_params(axis='both', which='major', labelsize=13)
ax_a.grid(axis='both', which='major', color='grey', linestyle='--', lw=0.35, alpha=0.8)
ax_a.axhline(y=0.95, color='tab:red', linestyle='dashed', linewidth=1.2)
ax_a.text(-0.05, 0.92, r"$0.95$", color='tab:red', fontsize=12)
ax_a.set_xlim(0, 1.05)
legend_a = ax_a.legend(
	title=r'$Initial\ K_0$', title_fontsize=12,
	fontsize=12, ncol=3, framealpha=0.2, columnspacing=0.05,
	loc=(0.0, 1.02), handletextpad=0.1)
legend_a._legend_box.align = "left"
ax_a.annotate(r"$CSR=0.200$", xy=(0.5, 0.15), fontsize=13)
ax_a.text(0.02, 0.02, '(a)', transform=ax_a.transAxes, fontsize=14,
	fontweight='bold', va='bottom')

# (b) formatting
ax_b.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$', fontsize=13)
ax_b.set_ylabel(r'$Cumulative\ shear\ work\ W_s\ (kJ/m^3)$', fontsize=13)
ax_b.tick_params(axis='both', which='major', labelsize=13)
ax_b.grid(axis='both', which='major', color='grey', linestyle='--', lw=0.35, alpha=0.8)
ax_b.set_ylim(-0.02, 0.4)
legend_b = ax_b.legend(
	title=r'$Initial\ K_0$', title_fontsize=12,
	fontsize=12, ncol=3, framealpha=0.2, columnspacing=0.05,
	loc=(0.0, 1.02), handletextpad=0.1)
legend_b._legend_box.align = "left"
ax_b.annotate(r"$CSR=0.200$", xy=(0.5, 0.2), fontsize=13)
ax_b.text(0.02, 0.95, '(b)', transform=ax_b.transAxes, fontsize=14,
	fontweight='bold', va='top')

# (c) formatting
ax_c.set_xlabel(r'$Cumulative\ shear\ work\ W_s\ (kJ/m^3)$', fontsize=13)
ax_c.set_ylabel(r'$EPWP\ ratio\ r_u$', fontsize=13)
ax_c.tick_params(axis='both', which='major', labelsize=13)
ax_c.grid(axis='both', which='major', color='grey', linestyle='--', lw=0.35, alpha=0.8)
ax_c.set_xlim(0, 0.45)
ax_c.set_xticks([0.0, 0.1, 0.2, 0.3, 0.4])
ax_c.axhline(y=0.95, color='tab:red', linestyle='dashed', linewidth=1.2)
ax_c.text(-0.04, 0.92, r"$0.95$", color='tab:red', fontsize=12)
legend_c = ax_c.legend(
	title=r'$Initial\ K_0$', title_fontsize=12,
	fontsize=12, ncol=3, framealpha=0.2, columnspacing=0.05,
	loc=(0.0, 1.02), handletextpad=0.1)
legend_c._legend_box.align = "left"
ax_c.annotate(r"$CSR=0.200$", xy=(0.03, 0.7), fontsize=13)
ax_c.text(0.02, 0.02, '(c)', transform=ax_c.transAxes, fontsize=14,
	fontweight='bold', va='bottom')

plt.tight_layout()
plt.savefig("fig4_12_combined.png", dpi=350)
plt.show()
