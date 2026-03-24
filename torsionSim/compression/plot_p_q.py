import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.lines import Line2D

fig1 = plt.figure(figsize=(6, 5.0))
ax1 = plt.gca()
FS = 14
LW_MAIN = 1.6
xmajorFormatter = FormatStrFormatter('%.1f')
ymajorFormatter = FormatStrFormatter('%.1f')
ax1.xaxis.set_major_formatter(xmajorFormatter)
ax1.yaxis.set_major_formatter(ymajorFormatter)
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.grid(axis='y', which='minor', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.tick_params(axis='both', which='major', labelsize=FS)

# Anisotropic state scatter
k0s = [0.5, 1.0, 2.0]
markers = ['d', 'o', 'v']
colors = ['tab:orange', 'tab:blue', 'tab:green']


def plt_ani_stress(k0=0.3, marker='o', color='tab:blue'):
	file_name = "k%.2f/comp.csv" % (k0)
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
		idx = (np.abs(stresses_p - target_p)).argmin()
		if abs(stresses_p.iloc[idx] - target_p) < 5:
			marker_indices.append(idx)

	# All markers are open (unfilled)
	markerfacecolor = 'None'
	markersize = 11

	# Plot stress path (solid line)
	ax1.plot(stresses_p, stresses_q, color=color, linewidth=LW_MAIN,
		zorder=2)

	# Plot markers at target stress levels
	if marker_indices:
		ax1.scatter(stresses_p.iloc[marker_indices],
			stresses_q.iloc[marker_indices],
			marker=marker, s=markersize**2,
			facecolors=markerfacecolor, edgecolors=color,
			linewidths=1.8, zorder=3)


# Isotropic compression line (initialization phase)
ax1.plot([0, 10.0], [0, 0.0], color='tab:red', linestyle='--',
	linewidth=LW_MAIN)

for k0, marker, color in zip(k0s, markers, colors):
	plt_ani_stress(k0, marker, color=color)

# --- Legend: IC + K0 values ---
legend_handles = [
	Line2D([0], [0], color='tab:red', linestyle='--', linewidth=LW_MAIN),
]
legend_labels = ['IC']

for k0, m, c in zip(k0s, markers, colors):
	legend_handles.append(
		Line2D([0], [0], marker=m, color=c, linestyle='-',
			linewidth=LW_MAIN,
			markerfacecolor='None', markeredgecolor=c, markersize=10,
			markeredgewidth=1.8))
	legend_labels.append(r'$K_0=%.1f$' % k0)

legend1 = ax1.legend(
	legend_handles, legend_labels,
	fontsize=FS, framealpha=0.2, ncol=4,
	borderpad=0.3, columnspacing=0.5, handletextpad=0.3,
	loc='upper left', bbox_to_anchor=(0.0, 1.10))

xlabel = ax1.set_xlabel(r'$Mean\ effective\ stress\ p\prime\ (kPa)$',
	fontsize=FS)
ylabel = ax1.set_ylabel(r'$Deviator\ stress\ q\ (kPa)$', fontsize=FS)
ax1.set_ylim(-100, 100)
ax1.set_xlim(0.0, 110)

ax1.add_artist(legend1)
plt.tight_layout(rect=(0, 0, 1, 0.92))
plt.savefig("aniso_stress.png", dpi=500, bbox_inches="tight", pad_inches=0.02,
	bbox_extra_artists=(legend1,))
plt.show()
