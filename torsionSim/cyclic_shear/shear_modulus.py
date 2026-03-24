import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# setting style
k0s = [0.5, 1.0, 2.0]
markers = ['d', 'o', 'v']
colors = ['tab:orange', 'tab:blue', 'tab:green']
FS_LABEL = 15
FS_TICK = 14
FS_LEGEND = 14
FS_ANN = 14
FS_INSET = 12

fig1 = plt.figure(figsize=(6.0, 5.0))
ax1 = plt.gca()

# inset axes for hysteresis loop schematic
ax2 = ax1.inset_axes([0.1, 0.15, 0.42, 0.36])

def plot_shear_modulus(k0, color, marker):
	csr = 0.200
	file_name = BASE_DIR / ("Dr90/k%.2f/csr_%.3f/torsion_shear.csv" % (k0, csr))
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
	N_loading = []
	N_unloading = []

	density_sat = (2600.0 + 1000.0 * df1['void_ratio'][0]) / (df1['void_ratio'][0] + 1.0)

	for i in range(n_quarters):
		t_start = i * quarter_period
		t_end = (i + 1) * quarter_period

		ind_start = np.searchsorted(time, t_start)
		ind_end = np.searchsorted(time, t_end)

		if ind_end >= len(time):
			ind_end = len(time) - 1
		if ind_start >= ind_end:
			continue

		d_strain = strains[ind_end] - strains[ind_start]
		d_stress = stresses_shear[ind_end] - stresses_shear[ind_start]

		if abs(d_strain) > 1e-11:
			# d_strain is tensorial strain epsilon; G = tau / gamma = tau / (2*epsilon)
			G = abs(d_stress / d_strain) * 1000. / 2.0  # Pa
			Vs = np.sqrt(G / density_sat)  # m/s

			if i % 2 == 0:  # loading
				Vs_loading.append(Vs)
				N_loading.append(t_end / period)
			else:  # unloading
				Vs_unloading.append(Vs)
				N_unloading.append(t_end / period)

	Vs_loading = np.array(Vs_loading)
	Vs_unloading = np.array(Vs_unloading)
	N_loading = np.array(N_loading)
	N_unloading = np.array(N_unloading)

	flt_load = N_loading <= n_liq * 1.05
	flt_unload = N_unloading <= n_liq * 1.05

	label_load = r'$%.1f,\ load$' % k0
	ax1.plot(N_loading[flt_load], Vs_loading[flt_load], linewidth=1.2,
		color=color, marker=marker, markerfacecolor='None',
		linestyle='-', markersize=7, label=label_load)

	label_unload = r'$%.1f,\ unload$' % k0
	ax1.plot(N_unloading[flt_unload], Vs_unloading[flt_unload], linewidth=1.2,
		color=color, marker=marker, markerfacecolor=color,
		linestyle='--', markersize=5, label=label_unload)

	print(f"{k0}, Vs0_load={Vs_loading[0]:.2f} m/s, N_L={n_liq:.1f}")

for k0, marker, color in zip(k0s, markers, colors):
	plot_shear_modulus(k0, color, marker)

# --- Inset: hysteresis loop schematic using K0=1.0, cycle 25 ---
df_inset = pd.read_csv(BASE_DIR / "Dr90/k1.00/csr_0.200/torsion_shear.csv", header=0)
# strain_shear is tensorial epsilon; convert to gamma = 2*epsilon for plotting
strains_in = df_inset["strain_shear"].to_numpy() * 100 * 2.0  # gamma in percent
stresses_in = df_inset["stress_shear"].to_numpy() / 1000.  # kPa
time_in = df_inset["time_duration"].to_numpy()

period = 1.0 / 8.0
quarter = period * 0.25
cyc = 25
t_start = cyc * period

iq = []
for q in range(5):
	tq = t_start + q * quarter
	iq.append(np.searchsorted(time_in, tq))

# plot each quarter
for q in range(4):
	seg = slice(iq[q], iq[q+1]+1)
	color_q = 'tab:blue' if q % 2 == 0 else 'tab:red'
	ls_q = '-' if q % 2 == 0 else '--'
	ax2.plot(strains_in[seg], stresses_in[seg], color=color_q,
		linewidth=1.5, linestyle=ls_q)

# mark quarter points
labels = [r'$0$', r'$T/4$', r'$T/2$', r'$3T/4$', r'$T$']
offsets = [(0.004, -4), (-0.016, -8), (0.016, -8.0), (0.0, 4.0), (-0.01, 0.6)]
ha_list = ['left', 'left', 'right', 'right', 'left']
for q in range(5):
	ax2.plot(strains_in[iq[q]], stresses_in[iq[q]], 'ko', markersize=4, zorder=5)
	ax2.annotate(labels[q],
		xy=(strains_in[iq[q]] + offsets[q][0], stresses_in[iq[q]] + offsets[q][1]),
		fontsize=FS_INSET-2, ha=ha_list[q], fontweight='bold')

# G labels
ax2.annotate(r'$G_{load}$', xy=(-0.02, 14), fontsize=FS_INSET, color='tab:blue',
	fontstyle='italic')
ax2.annotate(r'$G_{unload}$', xy=(0.04, -2), fontsize=FS_INSET, color='tab:red',
	fontstyle='italic')

ax2.set_xlabel(r'$\gamma_{z\theta}\ (\%)$', fontsize=FS_INSET, labelpad=-2)
ax2.set_ylabel(r'$\tau_{z\theta}\ (kPa)$', fontsize=FS_INSET, labelpad=-14)
ax2.set_xlim(-0.15, 0.15)
ax2.set_ylim(-25, 25)
ax2.tick_params(axis='both', which='major', labelsize=FS_INSET)
ax2.set_title(r'$K_0=1.0,\ N=25$', fontsize=FS_INSET)

# main axes settings
legend1 = ax1.legend(
	title=r'$Initial\ K_0\ and\ load\ condition\ in\ cyclic\ shear$',
	title_fontsize=FS_LEGEND,
	fontsize=FS_LEGEND, ncol=3, framealpha=0.2, columnspacing=0.8,
	loc=(-0.0, 1.02), handletextpad=0.1)
legend1._legend_box.align = "left"
ax1.set_ylabel(r'$Shear\ wave\ velocity\ V_s\ (m/s)$', fontsize=FS_LABEL)
ax1.set_xlabel(r'$Number\ of\ cyclic\ loading\ N$', fontsize=FS_LABEL)
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.tick_params(axis='both', which='major', labelsize=FS_TICK)
ax1.set_xlim(0, 42)
ax1.set_ylim(10, 160)
plt.annotate(r"$CSR=0.200$", xy=(30, 135), fontsize=FS_ANN)

plt.tight_layout()
plt.savefig(BASE_DIR / "shear_modulus.png", dpi=350)
plt.show()
