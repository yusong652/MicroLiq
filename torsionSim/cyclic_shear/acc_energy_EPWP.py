import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# setting style
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

fig1 = plt.figure(figsize=(6.0, 5.))
ax1 = plt.gca()
plt.annotate(r"$CSR=0.200$", xy=(0.03, 0.7), fontsize=FS_ANN)
ax2 = plt.axes([0,1,0,1])
ax2.set_xlim((0.2, 4.0))
ax2.set_ylim(0.0, 0.6)

# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.58, 0.14, 0.4, 0.32])
ax2.set_axes_locator(ip)


def plot_acc_energy(k0, color, marker, csr=0.200):
	file_name = BASE_DIR / ("Dr80/k%.2f/csr_%.3f/torsion_shear.csv"%(k0, csr))
	try:
		df1 = pd.read_csv(file_name,header=0)
	except FileNotFoundError:
		return
	# overall data
	stresses_shear = df1["stress_shear"] / 1000.
	stresses_out = df1["stress_outer"] / 1000.
	stresses_in =df1["stress_inner"] / 1000.
	stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
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
	# print(k0)

	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	n_liq = time[ind_liq] / period
	cycles = time / period
	cycles_norm = cycles/n_liq
	EPWP_ratios = stresses_u / stress_ini
	ws_liq = acc_ene[ind_liq]
	print(EPWP_ratios[0])
	#########################################################
	flt = cycles_norm < 1.06

	ax1.plot(acc_ene[flt], EPWP_ratios[flt],linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=0.012*np.log(n_liq*2), markersize=9,
		label=r"$%.2f$"%(k0), 
		)
	draw_ws_liq(k0, ws_liq, color, marker)

def draw_ws_liq(k0, ws_liq, color, marker):
	ax2.scatter([k0], [ws_liq], color=color, marker=marker, 
		facecolors='None', s=80)

# plot_acc_strain('1.0')
for k0, marker, color in zip(k0s, markers, colors):
	plot_acc_energy(k0, color, marker)

legend1 = ax1.legend(
	title=r'$Initial\ K_0\ in\ cyclic\ shear$', title_fontsize=FS_LEGEND,
	fontsize=FS_LEGEND, ncol=3, framealpha=0.2, columnspacing=0.05, 
	loc=(-0.00, 1.02), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$EPWP\ ratio\ r_u$', fontsize=FS_LABEL)
ax1.set_xlabel(r'$Cumulative\ shear\ work\ W_s\ (kJ/m^3)$', 
	fontsize=FS_LABEL)
ax1.tick_params(axis='both', which='major', labelsize=FS_TICK)
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)

ax1.set_xlim(0, 0.45)
ax1.set_xticks([0.0, 0.1, 0.2, 0.3, 0.4])
ax1.plot((0.0, 0.45),(0.95, 0.95),
	color='tab:red', linestyle='dashed', linewidth=1.4)
ax1.text(-0.04, 0.92, r"$0.95$", color='tab:red',
	fontsize=FS_ANN)
ax2.set_ylabel(r'$W_{sL}\ (kJ/m^3)$', fontsize=FS_INSET)
ax2.set_xlabel(r'$K_0$', fontsize=FS_INSET)
ax2.tick_params(axis='both', which='both', labelsize=FS_INSET)
ax2.set_xscale('log')
ticks = [0.3, 0.5, 1.0, 3.0]
ax2.set_xticks(ticks)
ax2.set_xticklabels(['0.3', '0.5', '1.0', '3.0'])

plt.tight_layout()
plt.savefig(BASE_DIR / "acc_energy_EPWP.png",dpi=350)
plt.show()
