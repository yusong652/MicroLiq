import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def plot_csr_N_result():
	csrs = [0.200, 0.250, 0.300, 0.350, 0.400]
	cycles = []
	for csr in csrs:
		df1 = pd.read_csv(f"cyclic_dense/csr_{csr:.3f}/torsion_shear.csv",header=0)
		# strain_shear in CSV is tensorial shear strain epsilon_ztheta; gamma = 2 * epsilon
		epsilon = df1["strain_shear"] * 100.0
		gamma = epsilon * 2.0
		threshold = 2.5  # gamma_SA = 2.5%
		index = np.argmax(abs(gamma) > threshold)
		time = df1["time_duration"][index]
		cycle = time * 8.0
		cycles.append(cycle)
	ax1.scatter(cycles, csrs, label=r'$DEM\ simulation$',
		marker='o', color='tab:blue', s=86)

df2 = pd.read_csv("hca_Ishihara.csv", header=None)
stresses_p_ref = df2.to_numpy()[:, 0]
stresses_q_ref = df2.to_numpy()[:, 1]

fig1 = plt.figure(figsize=(6.0, 4.0))
ax1 = plt.gca()
ax1.set_xlim(1, 500.0)
ax1.set_ylim((0.10, 0.50))
ax1.set_xscale("log")
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.grid(axis='y', which='minor', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
plot_csr_N_result()
ax1.scatter(stresses_p_ref, stresses_q_ref, label=r'$Ishihara\ et\ al.,\ 1985$',
	marker='s', facecolors='None', edgecolors='tab:green', linewidths=1.2, s=86)
ax1.set_ylabel(r'$Cyclic\ stress\ ratio\ \tau_{z\theta,max}/p^\prime_{0}$', fontsize=13)
ax1.set_xlabel(r'$Number\ of\ cyclic\ loading\ N_{L}$', fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.legend(fontsize=12, ncol=1)

# Annotate liquefaction criterion
ax1.annotate(r'$Liquefaction\ criterion:\ \gamma_{SA}=2.5\%$',
	xy=(0.98, 0.02), xycoords='axes fraction',
	fontsize=11, ha='right', va='bottom',
	)

plt.tight_layout()
plt.savefig("validate_N_csr.png", dpi=700)
plt.show()
