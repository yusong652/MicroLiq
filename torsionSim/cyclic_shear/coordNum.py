import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)

# setting style
csr_arr = np.arange(0.200, 0.250, 0.05).tolist()
# csr_arr.append(0.235)
k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
markers = ['d', 's', 'o', '^', 'v']
colors = ['tab:orange', 'tab:red', 'tab:blue', 'tab:purple', 'tab:green']
fig1 = plt.figure(figsize=(6.0, 5.0))
ax1 = plt.gca()
ax2 = plt.axes([0,1,0,1])
ax2.set_ylim(20, 100)
ax2.set_xlim(4.7, 5.3)

# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.18,0.18,0.3,0.3])
ax2.set_axes_locator(ip)
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)

def plot_CN(k0, color, marker, csr=0.200):
	try:
		df1 = pd.read_csv("Dr80/k%.2f/csr_%.3f/torsion_shear.csv"%(k0, csr),
			header=0)
		df2 = pd.read_csv("Dr80/k%.2f/csr_%.3f/MechCoordinationNumber.csv"%(k0, csr))
	except FileNotFoundError:
		return
	# overall data
	stresses_shear = df1["stress_shear"] / 1000.
	stresses_out = df1["stress_outer"] / 1000.
	stresses_in =df1["stress_inner"] / 1000.
	stress_ini = stresses_out[0] + stresses_in[0] / 2.0
	stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini
	stresses_z = df1["stress_z"] / 1000.0

	stresses_p = (stresses_in + stresses_out + stresses_z) / 3.0
	# measurement ball data
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
	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	time_liq = time[ind_liq]
	n_liq = time[ind_liq] / period
	cycles = time / period
	cycles_norm = cycles/n_liq
	#########################################################
	time_lmt = 1.05 * time_liq
	cns = df2["mechCN"]
	times = np.arange(0, len(cns)*0.01, 0.01)
	flt = times <= time_lmt
	times_norm = times / time_liq

	ax1.plot(times_norm[flt],cns[flt],linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=0.012*np.log(n_liq*2), markersize=9,
		label=r"$K_0=%.2f$"%(k0))
	draw_cn_liq([cns[0]], [n_liq], color, marker)

def draw_cn_liq(cn_ini, n_liq, color, marker):
	ax2.scatter([cn_ini], [n_liq], color=color, marker=marker,
		facecolors='None', s=80, linewidths=1.5)

for k0, marker, color in zip(k0s, markers, colors):
	plot_CN(k0, color, marker)

# plot_CN('0.5', 0.400)

legend1 = ax1.legend(title=r'$Initial\ K_0\ in\ cyclic\ shear$', title_fontsize=13,
	fontsize=13, ncol=3, framealpha=0.2, columnspacing=0.8,
	loc=(-0.0, 1.02), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Coordination\ number\ Z_{m}$', fontsize=13)
ax1.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$', 
	fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.set_xlim(0, 1.05)
ax1.set_ylim(3.8, 5.2)
ax2.set_xlabel(r'$Z_{m0}$', fontsize=13)
ax2.set_ylabel(r'$N_L$', fontsize=13)
ax2.tick_params(axis='both', which='major', labelsize=13)
ax2.set_yscale('log')
ax2.set_yticks([20, 30, 50, 100])
ax2.set_yticklabels(['20', '30', '50', '100'])
ax2.yaxis.set_minor_formatter(plt.NullFormatter())
plt.tight_layout(rect=[0, 0, 1, 1])
plt.savefig("CoordNum.png",dpi=350)
plt.show()
