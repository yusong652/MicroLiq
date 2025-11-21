import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

csr_arr = np.arange(0.200, 0.425, 0.025).tolist()
# csr_arr.append(0.235)
k0s = [0.5, 1.0, 2.0]
markers = ['d','o', 'v',]
colors = ['tab:orange', 'tab:blue', 'tab:green']

fig1 = plt.figure(figsize=(6.0,4))
ax1 = plt.gca()

def plot_liq(k0, color, marker):
	ns_liq = []
	csrs = []
	for csr in csr_arr:
		file_name = "k%.2f/csr_%.3f/torsion_shear.csv"%(k0, csr)
		try:
			df1 = pd.read_csv(file_name,header=0)
		except FileNotFoundError:
			continue
		strains = df1["strain_shear"] * 100.
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

		###################################################
		#  find the index when liquefaction occurs
		period = 1.0 / 8.0
		ind_liq = 0
		while stresses_u[ind_liq] < 0.95 * stress_ini:
			ind_liq += 1
		n_liq = time[ind_liq] / period
		###################################################
		ns_liq.append(n_liq)
		csrs.append(csr)
	ax1.scatter(ns_liq, csrs, label=r'$K_0=%.2f$'%k0,
				marker=marker, facecolors='None', edgecolors=color, s=86)

for k0, marker, color in zip(k0s, markers, colors):
	plot_liq(k0, color, marker )
# ax1.set_title(r"$Triaxial\ Compression$")
# xmajorLocator = MultipleLocator(5)
# xmajorFormatter = FormatStrFormatter('%5.0f')
# ymajorLocator = MultipleLocator(1000)
# ymajorFormatter = FormatStrFormatter('%1.1f')
# ax1.xaxis.set_major_locator(xmajorLocator)
# ax1.xaxis.set_major_formatter(xmajorFormatter)
# ax1.yaxis.set_major_locator(ymajorLocator)
# ax1.yaxis.set_major_formatter(ymajorFormatter)
# xminorLocator = MultipleLocator(1)
# yminorLocator = MultipleLocator(200)
# ax1.xaxis.set_minor_locator(xminorLocator)
# ax1.yaxis.set_minor_locator(yminorLocator)
ax1.set_xlim((2.0, 80))
ax1.set_ylim((0.150, 0.450))
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)


ax1.set_ylabel(r'$Cyclic\ stress\ ratio\ \tau_{z\theta,max}/p^\prime_{0}$',
 fontsize=13)
ax1.set_xlabel(r'$Number\ of\ cyclic\ loading\ N_{L}$', fontsize=13)
ax1.legend(fontsize=10, ncol=1)
ax1.set_xscale('log')
ax1.set_xticks([5, 10, 20, 40, 80])
ax1.set_xticklabels(['5', '10', '20', '40', '80'])
ax1.tick_params(axis='both', which='major', labelsize=13)
plt.tight_layout()
plt.savefig("liq_res_cur.png",dpi=700)
plt.show()
