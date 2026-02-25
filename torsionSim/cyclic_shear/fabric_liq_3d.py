from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

BASE_DIR = Path(__file__).resolve().parent

k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
drs = ['Dr80', 'Dr75']
dr_dirs = {'Dr80': 'Dr80', 'Dr75': 'Dr60'}
dr_markers = {'Dr80': 'o', 'Dr75': 's'}
dr_labels = {'Dr80': r'$D_r=90\%$', 'Dr75': r'$D_r=75\%$'}
period = 1.0 / 8.0

FS_AX = 16
FS_TICK = 15
FS_LEG = 14
FS_ANN = 12

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
		print(f"{dr} K0={k0:.2f}: Zm0={zm0:.3f}, alpha0={alpha0:.4f}, N_L={n_liq:.1f}")

df = pd.DataFrame(results)

# --- 3D scatter plot ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

for dr in drs:
	mask = df['dr'] == dr
	ax.scatter(df[mask]['zm0'], df[mask]['alpha0'], df[mask]['n_liq'],
		marker=dr_markers[dr], s=100, label=dr_labels[dr],
		edgecolors='black', linewidths=0.8, depthshade=True)
	# annotate K0 values
	for _, row in df[mask].iterrows():
		ax.text(row['zm0'], row['alpha0'], row['n_liq'],
			'  %.2f' % row['k0'], fontsize=FS_ANN)

ax.view_init(elev=20, azim=-40)
ax.set_xlabel(r'$Z_{m0}$', fontsize=FS_AX, labelpad=10)
ax.set_ylabel(r'$\alpha_0$', fontsize=FS_AX, labelpad=10)
ax.set_zlabel(r'$N_L$', fontsize=FS_AX, labelpad=10)
ax.set_ylim(-0.10, 0.10)
ax.set_yticks([-0.10, -0.05, 0.00, 0.05, 0.10])
ax.legend(fontsize=FS_LEG)
ax.tick_params(axis='x', which='major', labelsize=FS_TICK)
ax.tick_params(axis='y', which='major', labelsize=FS_TICK)
ax.tick_params(axis='z', which='major', labelsize=FS_TICK)

plt.tight_layout()
plt.savefig(BASE_DIR / "fabric_liq_3d.png", dpi=350, bbox_inches="tight", pad_inches=0.02)
plt.show()
