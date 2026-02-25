from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent

k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
drs = ['Dr80', 'Dr75']
dr_dirs = {'Dr80': 'Dr80', 'Dr75': 'Dr60'}
dr_markers = {'Dr80': 'o', 'Dr75': 's'}
dr_labels = {'Dr80': r'$D_r=90\%$', 'Dr75': r'$D_r=75\%$'}
period = 1.0 / 8.0

FS_AX = 14
FS_TICK = 13
FS_LEG = 12
FS_ANN = 14
FS_PANEL = 12

results = []

for dr in drs:
	for k0 in k0s:
		dr_dir = dr_dirs[dr]
		shear_file = BASE_DIR / ("%s/k%.2f/csr_0.300/torsion_shear.csv" % (dr_dir, k0))
		cn_file = BASE_DIR / ("%s/k%.2f/csr_0.300/MechCoordinationNumber.csv" % (dr_dir, k0))
		alpha_file = BASE_DIR / ("%s/k%.2f/csr_0.300/alpha_mech.csv" % (dr_dir, k0))
		try:
			df_shear = pd.read_csv(shear_file, header=0)
			df_cn = pd.read_csv(cn_file, header=0)
			df_alpha = pd.read_csv(alpha_file, header=0)
		except FileNotFoundError as e:
			print(f"Missing: {e}")
			continue

		stresses_out = df_shear["stress_outer"].to_numpy() / 1000.
		stresses_in = df_shear["stress_inner"].to_numpy() / 1000.
		stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
		stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini
		time = df_shear["time_duration"].to_numpy()

		ind_liq = 0
		while ind_liq < len(stresses_u) and stresses_u[ind_liq] < 0.95 * stress_ini:
			ind_liq += 1
		n_liq = time[ind_liq] / period if ind_liq < len(time) else time[-1] / period

		zm0 = df_cn["mechCN"].iloc[0]
		alpha0 = df_alpha["alpha_mech"].iloc[0]

		results.append({
			'dr': dr, 'k0': k0, 'zm0': zm0, 'alpha0': alpha0, 'n_liq': n_liq
		})

df = pd.DataFrame(results)

# --- (a) Z_{m0} vs N_L ---
offsets_a = {
	('Dr80', 0.50): (12, 6), ('Dr80', 0.67): (12, 6),
	('Dr80', 1.00): (12, -3), ('Dr80', 1.50): (12, -12),
	('Dr80', 2.00): (12, 6),
	('Dr75', 0.50): (12, 6), ('Dr75', 0.67): (12, 6),
	('Dr75', 1.00): (12, -3), ('Dr75', 1.50): (-36, -16),
	('Dr75', 2.00): (12, -14),
}


def plot_zm_vs_nl(ax, show_panel_label=True):
	for dr in drs:
		mask = df['dr'] == dr
		ax.scatter(df[mask]['zm0'], df[mask]['n_liq'],
			marker=dr_markers[dr], s=100, label=dr_labels[dr],
			color='tab:blue' if dr == 'Dr80' else 'tab:orange',
			edgecolors='black', linewidths=0.8)
		for _, row in df[mask].iterrows():
			ofs = offsets_a[(row['dr'], row['k0'])]
			ax.annotate('%.2f' % row['k0'],
				xy=(row['zm0'], row['n_liq']),
				xytext=ofs, textcoords='offset points', fontsize=FS_ANN,
				arrowprops=dict(arrowstyle='-', color='grey', lw=0.5))

	ax.set_xlabel(r'$Z_{m0}$', fontsize=FS_AX)
	ax.set_ylabel(r'$N_L$', fontsize=FS_AX)
	ax.tick_params(axis='both', which='major', labelsize=FS_TICK)
	ax.grid(axis='both', which='major', color='grey', linestyle='--',
		lw=0.35, alpha=0.8)
	ax.legend(fontsize=FS_LEG, loc='upper left')
	ax.set_xlim(4.74, 5.02)
	ax.set_ylim(3.0, 12.5)
	if show_panel_label:
		ax.set_title('(a)', fontsize=FS_PANEL, loc='left')

# --- (b) alpha_0 vs N_L ---
offsets_b = {
	('Dr80', 0.50): (-18, -16), ('Dr80', 0.67): (-10, 8), ('Dr80', 1.00): (-10, 8),
	('Dr80', 1.50): (-10, 8), ('Dr80', 2.00): (8, -14),
	('Dr75', 0.50): (-18, -16), ('Dr75', 0.67): (-10, 8), ('Dr75', 1.00): (-10, 8),
	('Dr75', 1.50): (-10, -16), ('Dr75', 2.00): (8, -14),
}


def plot_alpha_vs_nl(ax, show_panel_label=True):
	for dr in drs:
		mask = df['dr'] == dr
		ax.scatter(df[mask]['alpha0'], df[mask]['n_liq'],
			marker=dr_markers[dr], s=100, label=dr_labels[dr],
			color='tab:blue' if dr == 'Dr80' else 'tab:orange',
			edgecolors='black', linewidths=0.8)
		for _, row in df[mask].iterrows():
			ofs = offsets_b[(row['dr'], row['k0'])]
			ax.annotate('%.2f' % row['k0'],
				xy=(row['alpha0'], row['n_liq']),
				xytext=ofs, textcoords='offset points', fontsize=FS_ANN)

	ax.set_xlabel(r'$\alpha_0$', fontsize=FS_AX)
	ax.set_ylabel(r'$N_L$', fontsize=FS_AX)
	ax.tick_params(axis='both', which='major', labelsize=FS_TICK)
	ax.grid(axis='both', which='major', color='grey', linestyle='--',
		lw=0.35, alpha=0.8)
	ax.legend(fontsize=FS_LEG, loc='upper left')
	ax.set_xlim(-0.10, 0.10)
	ax.set_xticks([-0.10, -0.05, 0.00, 0.05, 0.10])
	ax.set_ylim(3.0, 12.5)
	if show_panel_label:
		ax.set_title('(b)', fontsize=FS_PANEL, loc='left')


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
plot_zm_vs_nl(ax1, show_panel_label=True)
plot_alpha_vs_nl(ax2, show_panel_label=True)
plt.tight_layout()
plt.savefig(BASE_DIR / "fabric_liq_2d.png", dpi=350, bbox_inches="tight", pad_inches=0.02)
plt.close(fig)

fig_zm, ax_zm = plt.subplots(1, 1, figsize=(5.6, 4.5))
plot_zm_vs_nl(ax_zm, show_panel_label=False)
plt.tight_layout()
plt.savefig(BASE_DIR / "fabric_liq_2d_zm_nl.png", dpi=350, bbox_inches="tight", pad_inches=0.02)
plt.close(fig_zm)

fig_alpha, ax_alpha = plt.subplots(1, 1, figsize=(5.6, 4.5))
plot_alpha_vs_nl(ax_alpha, show_panel_label=False)
plt.tight_layout()
plt.savefig(BASE_DIR / "fabric_liq_2d_alpha_nl.png", dpi=350, bbox_inches="tight", pad_inches=0.02)
plt.close(fig_alpha)

plt.show()
