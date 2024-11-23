import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(6, 4))
ax = fig.gca()
df = pd.read_csv("shear.csv")

pore_stress = np.array(df["CH_4"])
lateral_stress = pore_stress.max() - pore_stress 
shear_stress = df["CH_1"]*3/(np.pi*2*(0.05**3-0.03**3))/1.0e3
axial_force = df["CH_3"]
axial_stress = axial_force / (np.pi*(0.05**2-0.03**2))/1.0e3
effe_stress = (lateral_stress*3.0 + axial_stress) / 3.0

freq_record = 0.05
time = np.linspace(0, len(effe_stress)*freq_record, len(effe_stress))

def get_index_begin(shear_stress):
	index_begin = 0
	for stress in shear_stress:
		if stress <= 1.0:
			index_begin += 1
		else:
			break
	return index_begin

index_begin = get_index_begin(shear_stress)

def get_index_liq(lateral_stress, index_begin):
	index_liq = 0
	lateral_stress_begin = lateral_stress[index_begin]
	for stress in lateral_stress:
		if stress >= lateral_stress_begin * 0.05:
			index_liq += 1
		else:
			break
	return index_liq

index_liq = get_index_liq(lateral_stress, index_begin)

effe_stress = effe_stress[index_begin:-200]
shear_stress = shear_stress[index_begin:-200]

time_begin = time[index_begin]
time_liq = time[index_liq] - time_begin
print(time_begin)
print(time_liq/10.)

ax.plot(effe_stress, shear_stress)
ax.set_xlabel(r"$Mean\ effective\ stress\ p\prime\ (kPa)$")
ax.set_ylabel(r"$Shear\ stress\ \tau(kPa)$")

plt.savefig('p-tau.png')
plt.show()