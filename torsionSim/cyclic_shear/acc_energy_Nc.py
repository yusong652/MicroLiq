import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
markers = ['d', 's', 'o', '^', 'v']
colors = ['tab:orange', 'tab:red', 'tab:blue', 'tab:purple', 'tab:green']

fig1 = plt.figure(figsize=(6.0, 4.5))
ax1 = plt.gca()

def plot_acc_energy_Nc(k0, color, marker, csr=0.200):
	file_name = "Dr80/k%.2f/csr_%.3f/torsion_shear.csv" % (k0, csr)
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
	flt = cycles < n_liq * 1.06

	ax1.plot(cycles[flt], acc_ene[flt], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=0.012 * np.log(n_liq * 2), markersize=9,
		label=r"$%.2f$" % (k0),
		)

for k0, marker, color in zip(k0s, markers, colors):
	plot_acc_energy_Nc(k0, color, marker)

legend1 = ax1.legend(
	title=r'$Initial\ K_0\ in\ cyclic\ shear$', title_fontsize=13,
	fontsize=13, ncol=3, framealpha=0.2, columnspacing=0.05,
	loc=(-0.00, 1.02), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Cumulative\ shear\ work\ W_s\ (kJ/m^3)$', fontsize=13)
ax1.set_xlabel(r'$Number\ of\ cyclic\ loading\ N_c$', fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
plt.annotate(r"$CSR=0.200$", xy=(15, 0.2), fontsize=13)
ax1.set_ylim(-0.02, 0.4)
plt.tight_layout()
plt.savefig("acc_energy_Nc.png", dpi=350)
plt.show()
