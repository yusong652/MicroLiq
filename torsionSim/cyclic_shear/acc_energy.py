import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# setting style
# st.use("seaborn-deep")
csr_arr = np.arange(0.200, 0.250, 0.05).tolist()
# csr_arr.append(0.235)
k0s = [0.5, 1.0, 2.0]
markers = ['d', 'o', 'v']
colors = ['tab:orange', 'tab:blue', 'tab:green']
FS_LABEL = 15
FS_TICK = 14
FS_LEGEND = 14
FS_ANN = 14
FS_INSET = 12
# k0s = [0.33, 0.5,  1.0,
#  2.0, 3.0]
# markers = [ 'h', 'd', 'o', 'v', '>']
# colors = [ 'tab:grey', 'tab:red',
#  'tab:blue', 'tab:green', 'tab:olive']

fig1 = plt.figure(figsize=(6.0, 4.5))
ax1 = plt.gca()

# inset axes for zoom region
ax_inset = ax1.inset_axes([0.14, 0.45, 0.4, 0.35])

def plot_acc_energy(k0, color, marker, csr=0.200):
	file_name = BASE_DIR / ("Dr80/k%.2f/csr_%.3f/torsion_shear.csv"%(k0, csr))
	print(file_name)
	try:
		df1 = pd.read_csv(file_name,header=0)
	except FileNotFoundError:
		print("File not found:", file_name)
		return
	# overall data
	stresses_shear = df1["stress_shear"] / 1000.
	stresses_out = df1["stress_outer"] / 1000.
	stresses_in =df1["stress_inner"] / 1000.
	stress_ini = stresses_out[0] + stresses_in[0] / 2.0
	stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini
	stresses_z = df1["stress_z"] / 1000.0

	stresses_p = (stresses_in + stresses_out + stresses_z) / 3.0
	time = df1["time_duration"]
	strains = df1["strain_shear"]
	acc_ene = np.zeros(len(strains))
	for index_strain in np.arange(len(strains)-1):
		acc_ene[index_strain+1] = (acc_ene[index_strain] + 
			(strains[index_strain+1] - strains[index_strain])*
			stresses_shear[index_strain])


	#########################################################
	#  get the index of liquefaction
	period = 1.0 / 8.0
	ind_liq = 0
	print(k0)
	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	n_liq = time[ind_liq] / period
	cycles = time / period
	cycles_norm = cycles/n_liq
	#########################################################
	flt = cycles_norm < 1.06

	ax1.plot(cycles_norm[flt],acc_ene[flt],linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=0.012*np.log(n_liq*2), markersize=9,
		label=r"$%.2f$"%(k0),
		)
	mevery = 0.012*np.log(n_liq*2)
	# scale markevery for inset zoom range (0.6~0.8 out of 0~1.06)
	inset_mevery = mevery * (1.06) / (0.8 - 0.6)
	ax_inset.plot(cycles_norm[flt],acc_ene[flt],linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=inset_mevery, markersize=9,
		)

# plot_acc_strain('1.0')
for k0, marker, color in zip(k0s, markers, colors):
	plot_acc_energy(k0, color, marker)

legend1 = ax1.legend(
	title=r'$Initial\ K_0\ in\ cyclic\ shear$', title_fontsize=FS_LEGEND,
	fontsize=FS_LEGEND, ncol=3, framealpha=0.2, columnspacing=0.05, 
	loc=(0.02, 0.8), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Cumulative\ shear\ work\ W_s\ (kJ/m^3)$', fontsize=FS_LABEL)
ax1.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$', 
	fontsize=FS_LABEL)
ax1.tick_params(axis='both', which='major', labelsize=FS_TICK)
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
plt.annotate(r"$CSR=0.200$", xy=(0.6, 0.2), fontsize=FS_ANN)
# ax1.set_xlim(0)
ax1.set_ylim(-0.02, 0.4)
# inset zoom region
ax_inset.set_xlim(0.6, 0.8)
ax_inset.set_ylim(0.03, 0.10)
ax_inset.tick_params(axis='both', which='major', labelsize=FS_INSET)
ax_inset.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.indicate_inset_zoom(ax_inset, edgecolor='grey', linewidth=1.2)
plt.tight_layout()
plt.savefig(BASE_DIR / "acc_energy.png",dpi=350)
plt.show()
