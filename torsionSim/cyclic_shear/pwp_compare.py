import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


k0s = (0.50, 0.67, 1.00, 1.50, 2.00)
time_lmts = (5.40, 5.0, 4.2, 4.0, 3.9)
colors = ('tab:orange', 'tab:red', 'tab:blue', 'tab:purple', 'tab:green')
linestyles = ('-.', ':', '-', '--', '-.')
FS_LABEL = 15
FS_TICK = 14
FS_LEGEND = 14
FS_TEXT = 14
LW_MAIN = 1.5
LW_REF = 1.6
def plot_pwp(k0, time_lmt, color, linestyle):
	try:
		df1 = pd.read_csv("Dr90/k%.2f/csr_0.200/torsion_shear.csv"%k0,header=0)
	except FileNotFoundError:
		print(f"Missing data for K0={k0:.2f}, skipped")
		return
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
	idx_liq = 0
	while stresses_u[idx_liq] < 0.95 * stress_ini:
		idx_liq += 1
	n_liq = time[idx_liq] / period
	print(n_liq)
	###################################################
	flt = time < time_lmt
	ax1.plot(time[flt]/period,stresses_u[flt]/stress_ini,
		linewidth=LW_MAIN,label=r"$K_0=%.2f$"%k0,
		color=color, linestyle=linestyle)
	ax1.plot((time[idx_liq]/period, time[idx_liq]/period), 
		(-0.1, stresses_u[idx_liq]/stress_ini), color='tab:red', 
		linestyle='dashed',linewidth=LW_REF)
	ax1.text(time[idx_liq]/period, -0.088, r"$%d$"%(time[idx_liq]*8), color='tab:red',
		fontsize=FS_TEXT)

fig1 = plt.figure(figsize=(6.0, 4.0))
ax1 = plt.gca()
for i in range(5):
	plot_pwp(k0s[i], time_lmts[i], colors[i], linestyles[i])

ax1.set_ylim((-0.1, 1.0))
ax1.set_xlim((0.0, 44.0))
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.set_ylabel(r'$EPWP\ ratio\ r_u$', fontsize=FS_LABEL)
ax1.set_xlabel(r'$Number\ of\ cyclic\ loading\ N$', fontsize=FS_LABEL)
legend1 = ax1.legend(
	title=r'$EPWP\ ratio\ r_u$', title_fontsize=FS_LEGEND,
	fontsize=FS_LEGEND, ncol=1, framealpha=0.2, columnspacing=0.05, 
	loc=(0.03, 0.50), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 0.95, 1.0])
ax1.set_yticklabels([0.0, 0.2, 0.4, 0.6, 0.8, '', 1.0])
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width, box.height*0.5])

ax1.plot((0.0, 85),(0.95, 0.95),
	color='tab:red', linestyle='dashed', linewidth=LW_REF)
ax1.text(-4, 0.92, r"$0.95$", color='tab:red',
	fontsize=FS_TEXT)

ax1.tick_params(axis='both', which='major', labelsize=FS_TICK)

plt.tight_layout()
plt.savefig("stress_u_compare.png",dpi=350)
plt.show()
