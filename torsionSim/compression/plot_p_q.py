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
FS_LABEL = 17
FS_TICK = 16
FS_LEGEND = 16
LW_MAIN = 1.6
xmajorFormatter = FormatStrFormatter('%.1f')
ymajorFormatter = FormatStrFormatter('%.1f')
ax1.xaxis.set_major_formatter(xmajorFormatter)
ax1.yaxis.set_major_formatter(ymajorFormatter)
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.tick_params(axis='both', which='major', labelsize=FS_TICK)
# Anisotropic state scatter
k0s = [0.5, 1.0, 2.0]
markers = ['d', 'o', 'v']
colors = ['tab:orange', 'tab:blue', 'tab:green']

def plt_ani_stress(k0=0.3, marker='o', color='tab:blue'):
	file_name = "k%.2f/comp.csv"%(k0)
	try:
		df1 = pd.read_csv(file_name, header=0)
	except FileNotFoundError:
		return

	# Read stress data from CSV and convert to kPa
	stresses_z = df1['stress_z'] / 1.0e3
	stresses_outer = df1['stress_outer'] / 1.0e3
	stresses_inner = df1['stress_inner'] / 1.0e3

	# Calculate mean effective stress p' and deviatoric stress q
	stresses_p = (stresses_z + stresses_outer + stresses_inner) / 3.0
	stresses_q = stresses_z - (stresses_outer + stresses_inner) / 2.0

	# Define target p' values for markers (every 10 kPa from 10 to 100)
	target_p_values = np.arange(10, 101, 10)
	marker_indices = []

	for target_p in target_p_values:
		# Find index closest to target p' value
		idx = (np.abs(stresses_p - target_p)).argmin()
		if abs(stresses_p.iloc[idx] - target_p) < 5:  # Within 5 kPa tolerance
			marker_indices.append(idx)

	# Marker settings
	if k0 == 1.0:
		markerfacecolor = color
		markersize = 10
	else:
		markerfacecolor = 'None'
		markersize = 11

	# Plot full line
	ax1.plot(stresses_p, stresses_q, color=color, linewidth=LW_MAIN)

	# Plot markers at target stress levels
	if marker_indices:
		ax1.scatter(stresses_p.iloc[marker_indices], stresses_q.iloc[marker_indices],
			label=r'$%.2f$'%k0, marker=marker, s=markersize**2,
			facecolors=markerfacecolor, edgecolors=color, linewidths=1.8)

# Isotropic compression line (initialization phase, before anisotropic consolidation)
handles_plt = []
plt_line, = ax1.plot([0, 10.0], [0, 0.0], color='tab:red',
	label=r'$IC$', linestyle='--')
handles_plt.append(plt_line)

for k0, marker, color in zip(k0s, markers, colors):
	plt_ani_stress(k0, marker, color=color)

legend1 = ax1.legend(
	title=r'$Target\ K_0\ after\ AC$', title_fontsize=FS_LEGEND,
	fontsize=FS_LEGEND, framealpha=0.2, ncol=4,
	borderpad=0.2, columnspacing=0.2, loc=(0.0, 1.00))
legend1._legend_box.align = "left"  # type: ignore
xlabel = ax1.set_xlabel(r'$Mean\ effective\ stress(kPa)\ p\prime\ (kPa)$',
 fontsize=FS_LABEL)
ylabel = ax1.set_ylabel(r'$Deviator\ stress\ q\ (kPa)$', fontsize=FS_LABEL)
ax1.set_ylim(-100, 100)
ax1.set_xlim(0.0, 110)

ax1.add_artist(legend1)
plt.tight_layout(rect=(0, 0, 1, 0.88))
plt.savefig("aniso_stress.png", dpi=500, bbox_inches="tight", pad_inches=0.02,
	bbox_extra_artists=(legend1,))
plt.show()
