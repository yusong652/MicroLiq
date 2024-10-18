import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(6, 4))
ax = fig.gca()
df = pd.read_csv("shear.csv")

pore_stress = df["CH_4"]

effe_stress = - pore_stress
stress_min = np.array(effe_stress).min()
effe_stress -= stress_min
shear_stress = df["CH_1"]*3/(np.pi*2*(0.05**3-0.03**3))/1.0e3

freq = 0.05
time = np.linspace(0, len(effe_stress)*freq, len(effe_stress))

def get_index_begin(shear_stress):
	index_begin = 0
	for stress in shear_stress:
		if stress <= 1.0:
			index_begin += 1
		else:
			break
	return index_begin

index_begin = get_index_begin(shear_stress)
ax.plot(time[index_begin:]-time[index_begin], pore_stress[index_begin:])
ax.set_xlabel(r"$Time\ (s)$")
ax.set_ylabel(r"$Pore\ water\ stress\ (kPa)$")

plt.savefig('time_u.png')
plt.show()