import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# setting style
# st.use("seaborn-deep")
def plot_csr_N_result():
	csrs = [0.200, 0.250, 0.300, 0.350, 0.400]
	cycles = []
	for csr in csrs:
		df1 = pd.read_csv(f"cyclic_dense/csr_{csr:.3f}/torsion_shear.csv",header=0)
		strains = df1["strain_shear"] * 100.0 * 2
		strains_abs = abs(strains)
		threshold = 2.0
		index = np.argmax(strains_abs > threshold)
		time = df1["time_duration"][index]
		cycle = time * 8.0
		cycles.append(cycle)
	ax1.scatter(cycles, csrs, label=r"$DEM\ Simulation$", color='tab:blue')

df2 = pd.read_csv("hca_Ishihara.csv", header=None)

stresses_p_ref = df2.to_numpy()[:, 0]
stresses_q_ref = df2.to_numpy()[:, 1]

# time = df1["time_duration"]
fig1 = plt.figure(figsize=(4.0,4.5))
ax1 = plt.gca()
ax1.set_xlim(1, 500.0)
ax1.set_ylim((0,0.5))
ax1.set_xscale("log")
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
plot_csr_N_result()
ax1.scatter(stresses_p_ref, stresses_q_ref, label=r"$Ishihara\ et\ al., 1985$", 
	color="tab:green", marker='s', facecolor="None", )
ax1.set_ylabel(r'$Cyclic\ stress\ ratio$', fontsize=13)
ax1.set_xlabel(r'$Cyclic\ number\ to\ liquefaction$', fontsize=13)
legend1 = ax1.legend(
	fontsize=13, ncol=1, framealpha=0.2, columnspacing=0.05, 
	loc=(-0.0, 1.05), handletextpad=0.1)
ax1.tick_params(axis='both', which='major', labelsize=13)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("validate_N_csr.png",dpi=350)
plt.show()
