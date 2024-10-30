import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(6, 4))
ax = fig.gca()
df = pd.read_csv("shear.csv")

shear_stress = df["CH_1"]*3/(np.pi*2*(0.05**3-0.03**3))/1.0e3
shear_strain = df["CH_2"]/180.*np.pi*(0.05**3-0.03**3)/((0.05**2-0.03**2)*3*0.1)*100.0

shear_strain = np.array(shear_strain)
shear_strain = shear_strain - shear_strain[0]

def get_index_begin(shear_stress):
	index_begin = 0
	for stress in shear_stress:
		if stress <= 1.0:
			index_begin += 1
		else:
			break
	return index_begin

index_begin = get_index_begin(shear_stress)
ax.plot(shear_strain[index_begin:len(shear_strain)-0], shear_stress[index_begin:len(shear_strain)-0])
ax.set_xlabel(r"$Shear\ strain(\%)$")
ax.set_ylabel(r"$Shear\ stress\ \tau\ (kPa)$")

plt.savefig('gamma-tau.png')
plt.show()
