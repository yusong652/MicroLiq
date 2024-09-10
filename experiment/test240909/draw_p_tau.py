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

freq = 0.02
time = np.linspace(0, len(effe_stress)*freq, len(effe_stress))

ax.plot(effe_stress, shear_stress)
ax.set_xlabel(r"$Mean\ effective\ stress\ p\prime\ (kPa)$")
ax.set_ylabel(r"$Pore\ water\ stress\ (kPa)$")

plt.savefig('p-q.png')
plt.show()