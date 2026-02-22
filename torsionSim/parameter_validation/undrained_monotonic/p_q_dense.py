import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

df1 = pd.read_csv("monotonic_dense/torsion_shear.csv",header=0)
df2 = pd.read_csv("Nakata_p_q_dense.csv", header=None)
strains = df1["strain_shear"] * 100.0
stresses_shear = df1["stress_shear"] / 1000.
stresses_out = df1["stress_outer"] / 1000.
stresses_in =df1["stress_inner"] / 1000.
rads_out = df1["rad_outer"]
rads_inner = df1["rad_inner"]
stresses_rad = (stresses_out * rads_out + stresses_in * rads_inner) / (rads_out + rads_inner)
stresses_cir = (stresses_out * rads_out - stresses_in * rads_inner) / (rads_out - rads_inner)
stresses_lat = (stresses_rad + stresses_cir) / 2.0
stresses_ini = stresses_lat[0]
stresses_u = -(stresses_in + stresses_out) / 2 + stresses_ini
stresses_z = df1["stress_z"] / 1000.0
stresses_1 = (stresses_z + stresses_cir) / 2.0 + np.sqrt(((stresses_z - stresses_cir)/2.0)**2 + stresses_shear**2)
stresses_2 = stresses_rad
stresses_3 = (stresses_z + stresses_cir) / 2.0 - np.sqrt(((stresses_z - stresses_cir)/2.0)**2 + stresses_shear**2)
stresses_p = (stresses_in + stresses_out + stresses_z) / 3.0
stresses_dev = np.sqrt(0.5*((stresses_1 - stresses_2)**2 + (stresses_1 - stresses_3)**2 + (stresses_3 - stresses_2)**2))

stresses_p_ref = df2.to_numpy()[:, 0]
stresses_q_ref = df2.to_numpy()[:, 1]

time = df1["time_duration"]
fig1 = plt.figure(figsize=(6.0, 4.0))
ax1 = plt.gca()
ax1.set_xlim(0.0, 200.0)
ax1.set_ylim((0, 200))
ax1.grid(axis='both', which='major', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
ax1.grid(axis='y', which='minor', color='grey', linestyle='--',
	lw=0.35, alpha=0.8)
flt = time < 1.86
ax1.plot(stresses_p[flt][::1], stresses_dev[flt][::1], linewidth=1.6,
	label=r'$DEM\ simulation$', color='tab:blue')
ax1.plot(stresses_p_ref, stresses_q_ref, label=r'$Nakata\ et\ al.,\ 1998$',
	color='tab:green', marker='s', markersize=8, markerfacecolor='None', markeredgewidth=1.2, linewidth=1.2, markevery=2)
ax1.set_ylabel(r'$Deviatoric\ stress\ q\ (kPa)$', fontsize=13)
ax1.set_xlabel(r'$Mean\ effective\ stress\ p\prime\ (kPa)$', fontsize=13)
ax1.legend(fontsize=12, ncol=1)
ax1.tick_params(axis='both', which='major', labelsize=13)

plt.tight_layout()
plt.savefig("validate_p_q_dense.png", dpi=700)
plt.show()
