import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
drs = ['Dr80', 'Dr60']
dr_markers = {'Dr80': 'o', 'Dr60': 's'}
dr_labels = {'Dr80': r'$D_r=80\%$', 'Dr60': r'$D_r=60\%$'}
period = 1.0 / 8.0

results = []

for dr in drs:
	for k0 in k0s:
		shear_file = "%s/k%.2f/csr_0.300/torsion_shear.csv" % (dr, k0)
		cn_file = "%s/k%.2f/csr_0.300/MechCoordinationNumber.csv" % (dr, k0)
		alpha_file = "%s/k%.2f/csr_0.300/alpha_mech.csv" % (dr, k0)
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

# --- (a) Z_{m0} vs N_L ---
offsets_a = {
	('Dr80', 0.50): (12, 6), ('Dr80', 0.67): (12, 6),
	('Dr80', 1.00): (12, -3), ('Dr80', 1.50): (12, -12),
	('Dr80', 2.00): (12, 6),
	('Dr60', 0.50): (12, 6), ('Dr60', 0.67): (12, 6),
	('Dr60', 1.00): (12, -3), ('Dr60', 1.50): (-36, -16),
	('Dr60', 2.00): (12, -14),
}
for dr in drs:
	mask = df['dr'] == dr
	ax1.scatter(df[mask]['zm0'], df[mask]['n_liq'],
		marker=dr_markers[dr], s=100, label=dr_labels[dr],
		color='tab:blue' if dr == 'Dr80' else 'tab:orange',
		edgecolors='black', linewidths=0.8)
	for _, row in df[mask].iterrows():
		ofs = offsets_a[(row['dr'], row['k0'])]
		ax1.annotate('%.2f' % row['k0'],
			xy=(row['zm0'], row['n_liq']),
			xytext=ofs, textcoords='offset points', fontsize=13,
			arrowprops=dict(arrowstyle='-', color='grey', lw=0.5))

ax1.set_xlabel(r'$Z_{m0}$', fontsize=13)
ax1.set_ylabel(r'$N_L$', fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.legend(fontsize=11, loc='upper left')
ax1.set_xlim(4.74, 5.02)
ax1.set_ylim(3.0, 12.5)
ax1.set_title('(a)', fontsize=11, loc='left')

# --- (b) alpha_0 vs N_L ---
offsets_b = {
	('Dr80', 0.50): (-18, -16), ('Dr80', 0.67): (-10, 8), ('Dr80', 1.00): (-10, 8),
	('Dr80', 1.50): (-10, 8), ('Dr80', 2.00): (8, -14),
	('Dr60', 0.50): (-18, -16), ('Dr60', 0.67): (-10, 8), ('Dr60', 1.00): (-10, 8),
	('Dr60', 1.50): (-10, -16), ('Dr60', 2.00): (8, -14),
}
for dr in drs:
	mask = df['dr'] == dr
	ax2.scatter(df[mask]['alpha0'], df[mask]['n_liq'],
		marker=dr_markers[dr], s=100, label=dr_labels[dr],
		color='tab:blue' if dr == 'Dr80' else 'tab:orange',
		edgecolors='black', linewidths=0.8)
	for _, row in df[mask].iterrows():
		ofs = offsets_b[(row['dr'], row['k0'])]
		ax2.annotate('%.2f' % row['k0'],
			xy=(row['alpha0'], row['n_liq']),
			xytext=ofs, textcoords='offset points', fontsize=13)

ax2.set_xlabel(r'$\alpha_0$', fontsize=13)
ax2.set_ylabel(r'$N_L$', fontsize=13)
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax2.legend(fontsize=11, loc='upper left')
ax2.set_ylim(3.0, 12.5)
ax2.set_title('(b)', fontsize=11, loc='left')

plt.tight_layout()
plt.savefig("fabric_liq_2d.png", dpi=350)
plt.show()
