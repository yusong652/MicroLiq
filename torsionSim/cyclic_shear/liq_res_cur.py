import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

csr_arr = np.arange(0.200, 0.425, 0.025).tolist()
# csr_arr.append(0.235)
k0s = [0.5, 1.0, 2.0]
markers = ['d', 'o', 'v']
colors = ['tab:orange', 'tab:blue', 'tab:green']
K0_INSET = [0.5, 0.67, 1.0, 1.5, 2.0]
K0_EXTRA_MAIN = [0.67, 1.5]
EXTRA_STYLE = {
	0.67: ('s', 'tab:red'),
	1.5: ('^', 'tab:purple'),
}

fig1 = plt.figure(figsize=(6.0,4))
ax1 = plt.gca()
FS_LABEL = 15
FS_TICK = 14
FS_LEGEND = 13
FS_INSET = 9
MARKER_SIZE = 100

def get_n_liq(k0, csr):
	file_name = BASE_DIR / ("Dr90/k%.2f/csr_%.3f/torsion_shear.csv"%(k0, csr))
	try:
		df1 = pd.read_csv(file_name,header=0)
	except FileNotFoundError:
		return None
	# overall data
	stresses_out = df1["stress_outer"] / 1000.
	stresses_in =df1["stress_inner"] / 1000.
	stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
	stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini
	time = df1["time_duration"]

	###################################################
	#  find the index when liquefaction occurs
	period = 1.0 / 8.0
	ind_liq = 0
	while ind_liq < len(stresses_u) and stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	if ind_liq >= len(stresses_u):
		return None
	n_liq = time[ind_liq] / period
	###################################################
	return n_liq

def plot_liq(k0, color, marker):
	ns_liq = []
	csrs = []
	for csr in csr_arr:
		n_liq = get_n_liq(k0, csr)
		if n_liq is None:
			continue
		ns_liq.append(n_liq)
		csrs.append(csr)
	ax1.scatter(ns_liq, csrs, label=r'$K_0=%.2f$'%k0,
				marker=marker, facecolors='None', edgecolors=color, s=MARKER_SIZE,
				linewidths=1.4)

for k0, marker, color in zip(k0s, markers, colors):
	plot_liq(k0, color, marker )

# Plot the two intermediate states only at CSR = 0.300 on the main panel.
for k0 in K0_EXTRA_MAIN:
	n_liq = get_n_liq(k0, 0.300)
	if n_liq is None:
		continue
	marker, color = EXTRA_STYLE[k0]
	ax1.scatter([n_liq], [0.300], label=r'$K_0=%.2f$'%k0,
				marker=marker, facecolors='None', edgecolors=color,
				s=0.75 * MARKER_SIZE, linewidths=1.3, zorder=4)
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
 fontsize=FS_LABEL)
ax1.set_xlabel(r'$Number\ of\ cyclic\ loading\ N_{L}$', fontsize=FS_LABEL)
ax1.legend(fontsize=FS_LEGEND, ncol=1)
ax1.set_xscale('log')
ax1.set_xticks([5, 10, 20, 40, 80])
ax1.set_xticklabels(['5', '10', '20', '40', '80'])
ax1.tick_params(axis='both', which='major', labelsize=FS_TICK)

# Inset: expanded K0 set at CSR = 0.300
axins = ax1.inset_axes([0.08, 0.10, 0.36, 0.28])
k0_to_style = {k0: (marker, color) for k0, marker, color in zip(k0s, markers, colors)}
k0_to_style.update(EXTRA_STYLE)
inset_x = []
inset_y = []
for k0 in K0_INSET:
	n_liq = get_n_liq(k0, 0.300)
	if n_liq is None:
		continue
	inset_x.append(k0)
	inset_y.append(n_liq)
	if k0 in k0_to_style:
		marker, color = k0_to_style[k0]
		axins.scatter(k0, n_liq, marker=marker, facecolors='None', edgecolors=color,
					  s=34, linewidths=1.1, zorder=3)
	else:
		axins.scatter(k0, n_liq, marker='o', color='0.35', s=18, zorder=3)
if len(inset_x) > 1:
	order = np.argsort(np.array(inset_x))
	axins.plot(np.array(inset_x)[order], np.array(inset_y)[order], color='0.65',
			   lw=0.8, ls='--', zorder=1)
axins.set_title(r'CSR = 0.300', fontsize=FS_INSET, pad=2)
axins.set_xlabel(r'$K_0$', fontsize=FS_INSET, labelpad=1)
axins.set_ylabel(r'$N_L$', fontsize=FS_INSET, labelpad=1)
axins.tick_params(axis='both', which='major', labelsize=FS_INSET-1, pad=1)
axins.grid(axis='both', which='major', color='0.8', linestyle='--', lw=0.25, alpha=0.7)
axins.set_xlim((0.40, 2.10))
if inset_y:
	ymin = max(1.0, min(inset_y) * 0.85)
	ymax = max(inset_y) * 1.10
	axins.set_ylim((ymin, ymax))

plt.tight_layout()
plt.savefig(BASE_DIR / "liq_res_cur.png", dpi=700)
plt.show()
