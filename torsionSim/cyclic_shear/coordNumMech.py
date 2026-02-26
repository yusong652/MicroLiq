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
k0s_comp = []
k0s_ext = []
cns_comp = []
cns_ext = []

fig1 = plt.figure(figsize=(6, 5))
ax1 = plt.gca()
plt.annotate(r"$CSR=0.250$", xy=(0.75, 3.1), fontsize=13)
ax2 = plt.axes([0,1,0,1])


# Manually set the position and relative size of the inset axes within ax1
ip = InsetPosition(ax1, [0.2,0.18,0.5,0.45])
ax2.set_axes_locator(ip)
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)

def plot_CN(k0, color, marker, csr=0.250):
	try:
		df1 = pd.read_csv("Dr90/k%.2fcsr%.3f/torsion_shear.csv"%(k0, csr),
			header=0)
		df2 = pd.read_csv("Dr90/k%.2fcsr%.3f/MechCoordinationNumber2.csv"%(k0, csr))
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
	period = 1.0 / 16.0
	ind_liq = 0
	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	time_liq = time[ind_liq]
	n_liq = time[ind_liq] / period
	cycles = time / period
	cycles_norm = cycles/n_liq
	#########################################################
	time_lmt = 1.03 * time_liq
	cns = df2["mechCN2"]
	if k0 < 1.0:
		k0s_comp.append(k0)
		cns_comp.append(cns[0])
	elif k0 > 1.0:
		k0s_ext.append(k0)
		cns_ext.append(cns[0])
	elif k0 == 1.0:
		k0s_comp.append(k0)
		cns_comp.append(cns[0])
		k0s_ext.append(k0)
		cns_ext.append(cns[0])
	times = np.arange(0, len(cns)*0.01, 0.01)
	flt = times <= time_lmt
	times_norm = times / time_liq

	ax1.plot(times_norm[flt],cns[flt],linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=0.012*np.log(n_liq*2), markersize=9,
		label=r"$%.2f$"%(k0))
	draw_cn_liq(k0, cns[0], color, marker)

def draw_cn_liq(cn_ini, n_liq, color, marker):
	ax2.scatter([cn_ini], [n_liq], color=color, marker=marker, 
		facecolors='None', s=80)

for k0, marker, color in zip(k0s, markers, colors):
	plot_CN(k0, color, marker)

handles_fit = []
def plot_fit(cns, k0s, state='comp'):
		coefs = np.polyfit(np.log(k0s), cns, deg=2)
		if state == 'comp':
			xs_fit = np.linspace(0.2, 1.0)
			color = 'tab:blue'
			linestyle = '-'
			label = r'$K_0\ <\ 1.0$'
		else: 
			xs_fit = np.linspace(1.0, 4.0)
			color = 'tab:green'
			linestyle = '-.'
			label = r'$K_0\ >\ 1.0$'
		ys_fit = (np.log(xs_fit)**2 * coefs[0] +
		 np.log(xs_fit)*coefs[1] +
		 coefs[2])
		line_fit, = ax2.plot(xs_fit, ys_fit, color=color,
			linestyle=linestyle, label=label)
		handles_fit.append(line_fit)

# plot_fit(cns_comp, k0s_comp, state='comp')
# plot_fit(cns_ext, k0s_ext, state='ext')
legends_fit = [r'$K_0\<1.0$', r'$K_0\>1.0$']
# ax2.legend(fontsize=13, framealpha=0.2, columnspacing=0.05, 
# 	handletextpad=0.1)

legend1 = ax1.legend(
	title=r'$Initial\ K_0\ in\ cyclic\ shear\ (AC,\ dense)$', title_fontsize=13,
	fontsize=13, loc=(-0.0, 1.068), ncol=5,
	framealpha=0.2, columnspacing=0.05, handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Mechanical\ Coordination\ number\ Z_m$', fontsize=13)
ax1.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$', 
	fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.set_xlim(0, 1.05)
ax1.set_ylim(2.4, 4.7)
ax2.set_ylim(4.0, 4.75)
ax2.set_xlim(0.2, 4.0)
ax2.set_xlabel(r'$K_0$', fontsize=13)
ax2.set_ylabel(r'$Initial\ Z_{m0}$', fontsize=13)
ax2.tick_params(axis='both', which='both', labelsize=13)
ax2.set_yscale('linear')
ax2.set_xscale('log')
ticks = [0.3, 0.5, 1.0, 3.0]
ax2.set_xticks(ticks)
ax2.set_xticklabels(ticks)
ax1.tick_params(axis='both', which='major', labelsize=13)
plt.tight_layout(rect=[0, 0, 1, 1.026])
plt.savefig("MechCoordNum.png",dpi=500)
plt.show()
