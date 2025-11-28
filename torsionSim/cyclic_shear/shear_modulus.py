import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

# setting style
k0s = [0.5, 1.0, 2.0]
markers = ['d', 'o', 'v']
colors = ['tab:orange', 'tab:blue', 'tab:green']
vs0_values = []  # store initial shear wave velocity for inset plot

fig1 = plt.figure(figsize=(6.0, 5.0))
ax1 = plt.gca()
ax2 = plt.axes([0, 1, 0, 1])  # inset axes for G0 vs K0

# Set position of inset axes (left bottom)
ip = InsetPosition(ax1, [0.18, 0.18, 0.36, 0.32])
ax2.set_axes_locator(ip)

def plot_shear_modulus(k0, color, marker):
	csr = 0.200
	file_name = "k%.2f/csr_%.3f/torsion_shear.csv" % (k0, csr)
	label = r'$%.2f$' % k0
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

	Vs_values = []
	N_norm_values = []

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

		if abs(d_strain) > 1e-10:
			G = abs(d_stress / d_strain) * 1000.  # Pa
			# convert G to Vs: Vs = sqrt(G / rho_sat)
			density_sat = (2600.0 + 1000.0 * df1['void_ratio'][0]) / (df1['void_ratio'][0] + 1.0)
			Vs = np.sqrt(G / density_sat)  # m/s
			Vs_values.append(Vs)
			N_norm_values.append((i * 0.25) / n_liq)  # normalized by N_L

	Vs_values = np.array(Vs_values)
	N_norm_values = np.array(N_norm_values)

	# filter to N/N_L <= 1.05
	flt = N_norm_values <= 1.05

	# plot main figure: Vs vs N/N_L
	ax1.plot(N_norm_values[flt], Vs_values[flt], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		markevery=max(1, int(0.05 * len(N_norm_values[flt]))), markersize=9,
		label=label)

	# store Vs0 for inset plot
	if len(Vs_values) > 0:
		vs0_values.append((k0, Vs_values[0], color, marker))
		print(f"K0={k0}, Vs0={Vs_values[0]:.2f} m/s, N_L={n_liq:.1f}")

# plot for each K0
for k0, marker, color in zip(k0s, markers, colors):
	plot_shear_modulus(k0, color, marker)

# plot inset: Vs0 vs K0
for k0, vs0, color, marker in vs0_values:
	ax2.scatter([k0], [vs0], color=color, marker=marker,
		facecolors='None', s=80)

# main axes settings
legend1 = ax1.legend(
	title=r'$Initial\ K_0\ in\ cyclic\ shear$', title_fontsize=13,
	fontsize=13, ncol=3, framealpha=0.2, columnspacing=0.05,
	loc=(-0.00, 1.02), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Shear\ wave\ velocity\ V_s\ (m/s)$', fontsize=13)
ax1.set_xlabel(r'$Normalized\ number\ of\ cyclic\ loading\ N_c/N_L$', fontsize=13)
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.set_xlim(0, 1.05)
plt.annotate(r"$CSR=0.200$", xy=(0.03, 5), fontsize=13)

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

plt.tight_layout()
plt.savefig("shear_modulus.png", dpi=350)
plt.show()
