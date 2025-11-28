import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
# setting style
# st.use("seaborn-deep")
k0s = [0.33, 0.4, 0.5, 0.67, 1.0,
1.5, 2.0, 2.5, 3.0, 3.33]
markers = ['h', 'p', 'd', 's','o', '^', 'v', '<', '>', 'P']
colors = ['tab:grey', 'tab:brown', 'tab:red', 'tab:orange',
 'tab:blue', 'tab:purple', 'tab:green', 'tab:pink', 'tab:olive', 'gold']
# k0s = [0.3, 0.33, ]
# markers = ['*', 'h', ]
# colors = ['tab:cyan', 'tab:grey', ]
fig1 = plt.figure(figsize=(6.0,5))
ax1 = plt.gca()
plt.annotate(r"$CSR=0.250$", xy=(0.76, 0.86), fontsize=13)
ax2 = plt.axes([0,1,0,1])


# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.25,0.58,0.45,0.36])
ax2.set_axes_locator(ip)
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)

def plot_invFabTen(k0, color, marker, csr=0.250):
	try:
		df1 = pd.read_csv("k%.2fcsr%.3f/torsion_shear.csv"%(k0, csr),
			header=0)
		df2 = pd.read_csv("k%.2fcsr%.3f/invFabTen_mech2.csv"%(k0, csr))
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

	#########################################################
	#  get the index of liquefaction
	period = 1.0 / 16.0
	ind_liq = 0
	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	time_liq = time[ind_liq]
	n_liq = time[ind_liq] / period
	cycles = time / period
	cycles_norm = cycles/n_liq
	#########################################################
	time_lmt = 1.05 * time_liq
	ifts = df2["invFabTen_mech2"] * 15./ 2.
	times = np.arange(0, len(ifts)*0.01, 0.01)
	flt = times <= time_lmt
	times_norm = times / time_liq

	ax1.plot(times_norm[flt],ifts[flt],linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=0.012*np.log(n_liq*2), markersize=9,
		label=r"$%.2f$"%(k0))
	draw_fc_liq(k0, ifts[0], color, marker)

def draw_fc_liq(fc_ini, n_liq, color, marker):
	ax2.scatter([fc_ini], [n_liq], color=color, marker=marker,
		facecolor='None', s=80)

for k0, marker, color in zip(k0s, markers, colors):
	plot_invFabTen(k0, color, marker)

legend1 = ax1.legend(
	title=r'$Initial\ K_0\ in\ cyclic\ shear\ (AC,\ Dense)$', title_fontsize=13,
	fontsize=13, loc=(-0.00, 1.068), ncol=5,
	framealpha=0.2, columnspacing=0.05, handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Second\ invariant\ of\ mechanical$' + '\n' +
	r'$anisotropic\ fabric\ tensor\ F_{c}$',
	fontsize=13)
ax1.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$', 
	fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.set_xlim(0.0, 1.08)
ax1.set_ylim(0.0, 1.0)
ax2.set_yscale('linear')
ax2.set_xscale('log')
ticks = [0.3, 0.5, 1.0, 3.0]
ax2.set_xticks(ticks)
ax2.set_xticklabels(ticks)
ax2.set_ylim(0.0, 0.5)
ax2.set_xlim(0.2, 4.0)
ax2.set_xlabel(r'$K_0$', fontsize=13)
ax2.set_ylabel(r'$Initial\ F_{c0}$', fontsize=13)
ax2.tick_params(axis='both', which='both', labelsize=13)

plt.tight_layout(rect=[0, 0, 1.0, 1.0])
plt.savefig("invFabTen_mech2.png",dpi=500)
plt.show()
