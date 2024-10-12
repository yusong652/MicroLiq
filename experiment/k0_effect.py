import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

fig = plt.figure(figsize=(6, 4))
ax = fig.gca()
folders = os.listdir()

def get_index_begin(shear_stress):
	index_begin = 0
	for stress in shear_stress:
		if stress <= 0.5:
			index_begin += 1
		else:
			break
	return index_begin

def get_index_liq(lateral_stress, index_begin):
	index_liq = 0
	lateral_stress_begin = lateral_stress[index_begin]
	for stress in lateral_stress:
		if stress >= lateral_stress_begin * 0.05:
			index_liq += 1
		else:
			break
	return index_liq

def get_k0_cycle():
	for folder in folders:
		if "test" in folder:
			df = pd.read_csv("{}/shear.csv".format(folder))
			pore_stress = np.array(df["CH_4"])
			lateral_stress = pore_stress.max() - pore_stress 
			shear_stress = df["CH_1"]*3/(np.pi*2*(0.05**3-0.03**3))/1.0e3
			axial_force = df["CH_3"]
			axial_stress = axial_force / (np.pi*(0.05**2-0.03**2))/1.0e3
			effe_stress = (lateral_stress*3.0 + axial_stress) / 3.0

			freq_record = 0.05
			time = np.linspace(0, len(effe_stress)*freq_record, len(effe_stress))
			index_begin = get_index_begin(shear_stress)
			index_liq = get_index_liq(lateral_stress, index_begin)

			k0 = (lateral_stress[index_begin]/
				(lateral_stress[index_begin]+axial_stress[index_begin]))


			time_begin = time[index_begin]
			time_liq = time[index_liq] - time_begin
			cycle_liq = time_liq/10.0
			ax.scatter([k0], [cycle_liq])

get_k0_cycle()

ax.set_xlabel(r"$Ratio\ of\ lateral\ to\ vertical\ stress\ K_0$")
ax.set_ylabel(r"$Number\ of\ cycle\ to\ liquefaction\ N_L$")
# ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xticks([0.2, 0.3, 0.4, 0.5, 1.0, 2.0])
# ax.set_xticklabels([0.2, 0.3, 0.4, 0.5, 1.0])
ax.get_xaxis().set_minor_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
# ax.get_xaxis().get_major_formatter().labelOnlyBase = False


plt.savefig('k0_effect.png')
plt.show()