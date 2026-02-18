import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

# setting style
k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
markers = ['d', 's', 'o', '^', 'v']
colors = ['tab:orange', 'tab:red', 'tab:blue', 'tab:purple', 'tab:green']
vs0_loading_values = []   # store initial loading Vs for inset plot
vs0_unloading_values = [] # store initial unloading Vs for inset plot

fig1 = plt.figure(figsize=(6.0, 5.0))
ax1 = plt.gca()
ax2 = plt.axes([0, 1, 0, 1])  # inset axes for Vs0 vs K0

# Set position of inset axes (left bottom)
ip = InsetPosition(ax1, [0.16, 0.18, 0.32, 0.32])
ax2.set_axes_locator(ip)

def plot_shear_modulus(k0, color, marker):
	csr = 0.200
	file_name = "Dr80/k%.2f/csr_%.3f/torsion_shear.csv" % (k0, csr)
	try:
		df1 = pd.read_csv(file_name, header=0)
	except FileNotFoundError:
		return

	strains = df1["strain_shear"].to_numpy()
	stresses_shear = df1["stress_shear"].to_numpy() / 1000.
	stresses_out = df1["stress_outer"].to_numpy() / 1000.
	stresses_in = df1["stress_inner"].to_numpy() / 1000.
	stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
	stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini
	time = df1["time_duration"].to_numpy()

	# find the index when liquefaction occurs
	period = 1.0 / 8.0
	ind_liq = 0
	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	n_liq = time[ind_liq] / period

	# calculate shear modulus at every 1/4 period
	quarter_period = period * 0.25
	n_quarters = int(time[ind_liq] / quarter_period) + 1

	# separate loading and unloading
	Vs_loading = []
	Vs_unloading = []
	N_loading = []    # cycle number for loading points
	N_unloading = []  # cycle number for unloading points

	density_sat = (2600.0 + 1000.0 * df1['void_ratio'][0]) / (df1['void_ratio'][0] + 1.0)

	for i in range(n_quarters):
		t_start = i * quarter_period
		t_end = (i + 1) * quarter_period

		# find indices for this quarter period
		ind_start = np.searchsorted(time, t_start)
		ind_end = np.searchsorted(time, t_end)

		if ind_end >= len(time):
			ind_end = len(time) - 1
		if ind_start >= ind_end:
			continue

		# calculate secant shear modulus
		d_strain = strains[ind_end] - strains[ind_start]
		d_stress = stresses_shear[ind_end] - stresses_shear[ind_start]

		if abs(d_strain) > 1e-11:
			G = abs(d_stress / d_strain) * 1000.  # Pa
			Vs = np.sqrt(G / density_sat)  # m/s

			# i=0,2,4,... -> loading (1/4T, 3/4T, 5/4T, ...)
			# i=1,3,5,... -> unloading (2/4T, 4/4T, 6/4T, ...)
			if i % 2 == 0:  # loading
				Vs_loading.append(Vs)
				N_loading.append((t_end / period) / n_liq)  # normalize by N_L
			else:  # unloading
				Vs_unloading.append(Vs)
				N_unloading.append((t_end / period) / n_liq)

	Vs_loading = np.array(Vs_loading)
	Vs_unloading = np.array(Vs_unloading)
	N_loading = np.array(N_loading)
	N_unloading = np.array(N_unloading)

	# filter to N/N_L <= 1.0
	flt_load = N_loading <= 1.05
	flt_unload = N_unloading <= 1.05

	# plot loading curve (solid line)
	label_load = r'$%.1f,\ load$' % k0
	ax1.plot(N_loading[flt_load], Vs_loading[flt_load], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		linestyle='-', markersize=7, label=label_load)

	# plot unloading curve (dashed line)
	label_unload = r'$%.1f,\ unload$' % k0
	ax1.plot(N_unloading[flt_unload], Vs_unloading[flt_unload], linewidth=1.2,
		color=color, marker=marker, markerfacecolor=color,
		linestyle='--', markersize=5, label=label_unload)

	# store Vs0 for inset plot
	if len(Vs_loading) > 0:
		vs0_loading_values.append((k0, Vs_loading[0], color, marker))
		print(f"{k0}, Vs0_load={Vs_loading[0]:.2f} m/s, N_L={n_liq:.1f}")
	if len(Vs_unloading) > 0:
		vs0_unloading_values.append((k0, Vs_unloading[0], color, marker))
		print(f"{k0}, Vs0_unload={Vs_unloading[0]:.2f} m/s")

# plot for each K0
for k0, marker, color in zip(k0s, markers, colors):
	plot_shear_modulus(k0, color, marker)

# plot inset: Vs0 vs K0 (loading - hollow, unloading - filled)
for k0, vs0, color, marker in vs0_loading_values:
	ax2.scatter([k0], [vs0], color=color, marker=marker,
		facecolors='None', s=80, linewidths=1.5)
for k0, vs0, color, marker in vs0_unloading_values:
	ax2.scatter([k0], [vs0], color=color, marker=marker,
		facecolors=color, s=50)

# main axes settings
legend1 = ax1.legend(title=r'$Initial\ K_0\ and\ load\ condition\ in\ cyclic\ shear$',title_fontsize=13,
	fontsize=13, ncol=3, framealpha=0.2, columnspacing=0.8,
	loc=(-0.0, 1.02), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Shear\ wave\ velocity\ V_s\ (m/s)$', fontsize=13)
ax1.set_xlabel(r'$Normalized\ number\ of\ cycles\ N_c/N_L$', fontsize=13)
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.set_xlim(0, 1.05)
ax1.set_ylim(20, 220)
plt.annotate(r"$CSR=0.200$", xy=(0.55, 125), fontsize=13)

# inset axes settings
ax2.set_ylabel(r'$V_{s0}\ (m/s)$', fontsize=13)
ax2.set_xlabel(r'$K_0$', fontsize=13)
ax2.tick_params(axis='both', which='both', labelsize=13)
ax2.set_xscale('log')
ax2.set_xticks([0.5, 1.0, 2.0])
ax2.set_xticklabels(['0.5', '1.0', '2.0'])
ax2.xaxis.set_minor_formatter(plt.NullFormatter())
ax2.set_xlim(0.3, 3.0)
ax2.set_ylim(160, 220)

plt.tight_layout(rect=[0, 0, 1, 1])
plt.savefig("shear_modulus.png", dpi=350)
plt.show()
