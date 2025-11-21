import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# setting style
# st.use("seaborn-deep")
fig1 = plt.figure(figsize=(6,5.0))
ax1 = plt.gca()
xmajorFormatter = FormatStrFormatter('%.1f')
ymajorFormatter = FormatStrFormatter('%.3f')


ax1.xaxis.set_major_formatter(xmajorFormatter)
ax1.yaxis.set_major_formatter(ymajorFormatter)
# ax1.yaxis.set_major_formatter(ymajorFormatter)
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
# Manually set the position and relative size of the inset axes within ax1
# [left, bottom, width, height] in axes coordinates (0-1)
ax2 = ax1.inset_axes([0.5, 0.52, 0.4, 0.4])

# Anisotropic state scatter
k0s = [0.5, 1.0, 2.0]
markers = ['d', 'o', 'v']
colors = ['tab:orange', 'tab:blue', 'tab:green']

def plt_ani_stress(k0=0.3, marker='o', color='tab:blue'):
	file_name = "k%.2f/comp.csv"%(k0)
	try:
		df1 = pd.read_csv(file_name,header=0)
	except FileNotFoundError:
		return
	interval = 10
	stresses_z = df1['stress_z'][::interval] / 1.0e3
	stresses_out = df1['stress_outer'][::interval] / 1.0e3
	stresses_in = df1['stress_inner'][::interval] / 1.0e3
	stresses_p = (stresses_z + stresses_out + stresses_in) / 3.0
	void_ratios = df1['void_ratio'][::interval]
	markerfacecolor = 'None'
	markersize=9
	size_sct=80
	ax1.plot(stresses_p, void_ratios,
		label=r'$%.2f$'%k0, markevery=len(stresses_p)/1.5e4, color=color,
		marker=marker, markerfacecolor=markerfacecolor, markeredgecolor=color,
		markersize=markersize,)
	ax2.scatter([k0], [void_ratios.to_numpy()[-1]], color=color, marker=marker,
		facecolors=markerfacecolor, s=size_sct)

for k0, marker, color in zip(k0s, markers, colors):
	plt_ani_stress(k0, marker, color=color)
# handles_plt = []
# plt_line, = ax1.plot([0,0, 10.0], [0,0, 0.0], color='tab:red', 
# 	label=r'$Isotropic\ compression$', linestyle='--')
# handles_plt.append(plt_line)
# legends_plt=[r"$Isotropic\ consolidation$", ]

xlabel = ax1.set_xlabel(r'$Mean\ effective\ stress(kPa)\ p\prime\ (kPa)$',
 fontsize=13)
ylabel = ax1.set_ylabel(r'$Void\ ratio\ e$', fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.tick_params(axis='both', which='minor', labelsize=3)
ax1.set_ylim(0.730, 0.74)
ax1.set_xlim(10.0, 110)

def set_ax2_format():
	xmajorFormatter2 = FormatStrFormatter('%.2f')
	ymajorFormatter2 = FormatStrFormatter('%.3f')
	ax2.xaxis.set_major_formatter(xmajorFormatter2)
	ax2.yaxis.set_major_formatter(ymajorFormatter2)
	ax2.grid(axis='both',which='major',color='grey',linestyle='--',
		lw=0.35,alpha=0.8)
	ax2.set_ylim(0.731, 0.733)
	ax2.set_xscale('log')
	ticks = np.linspace(0.3, 1.0, 2).tolist()
	ticks.extend([3.0])
	ax2.set_xticks(ticks)
	ticklabels = ax2.get_xticks().tolist()


	ax2.set_xticklabels(ticklabels)
	ax2.set_xlabel(r'$K_0$', fontsize=13)
	ax2.set_ylabel(r'$e\ after\ AC$', fontsize=13)
	ax2.tick_params(axis='both', which='major', labelsize=13)
	ax2.tick_params(axis='x', which='minor', labelsize=0)  # 保留x轴小刻度但不显示标签

set_ax2_format()

legend1 = ax1.legend(
	title=r'$Target\ K_0\ after\ AC$', title_fontsize=13,
	fontsize=13, framealpha=0.2, ncol=4,
	borderpad=0.2, columnspacing=0.2, 
	loc=(0.0, 1.08))
legend1._legend_box.align = "left"  # type: ignore
box = ax1.get_position()
ax1.set_position((box.x0, box.y0, box.width, box.height*0.2))
ax1.add_artist(legend1)
plt.tight_layout(rect=(0, 0, 1, 0.72))
plt.savefig("stress_void.png",dpi=500)
plt.show()
