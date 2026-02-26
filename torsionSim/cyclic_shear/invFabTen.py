import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# setting style
# st.use("seaborn-deep")
k0s = [0.33, 0.4, 0.5, 0.67, 1.0,
1.5, 2.0]
markers = ['h', 'p', 'd', 's','o', '^', 'v',]
colors = ['tab:grey', 'tab:brown','tab:red', 'tab:orange',
 'tab:blue', 'tab:purple', 'tab:green']
# k0s = [0.3, 0.33, ]
# markers = ['*', 'h', ]
# colors = ['tab:cyan', 'tab:grey', ]
fig1 = plt.figure(figsize=(6.0,4))
ax1 = plt.gca()

ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
def plot_invFabTen(k0, color, marker, csr=0.250):
	try:
		df1 = pd.read_csv("Dr90/k%.2fcsr%.3f/torsion_shear.csv"%(k0, csr),
			header=0)
		df2 = pd.read_csv("Dr90/k%.2fcsr%.3f/invFabTen.csv"%(k0, csr))
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
	ifts = df2["invFabTen"]
	times = np.arange(0, len(ifts)*0.005, 0.005)
	flt = times <= time_lmt
	times_norm = times / time_liq

	ax1.plot(times_norm[flt],ifts[flt],linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=0.012*np.log(n_liq*2),
		label=r"$K_0=%.2f\ ,CSR=%.3f$"%(k0, csr))

for k0, marker, color in zip(k0s, markers, colors):
	plot_invFabTen(k0, color, marker)
ax1.legend(fontsize=10, framealpha=0.5, loc='upper left', ncol=2)
ax1.set_ylabel(r'$Second\ invariant\ of$' + '\n' +
	r'$anisotropic\ fabric\ tensor\ F_c$',
	fontsize=13)
ax1.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$', 
	fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=13)
# ax1.set_xlim(0)
ax1.set_ylim(0.0, 0.20)
plt.tight_layout()
plt.savefig("invFabTen.png",dpi=500)
plt.show()
