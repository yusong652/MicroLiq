import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(6, 4))
ax = fig.gca()
df = pd.read_csv("shear.csv")

pore_stress = df["CH_4"]
shear_strain = df["CH_2"]/180.*np.pi*(0.05**3-0.03**3)/((0.05**2-0.03**2)*3*0.1)*100.0
shear_strain = shear_strain - shear_strain[0]

freq = 0.05
time = np.linspace(0, len(shear_strain)*freq, len(shear_strain))

ax.plot(time, shear_strain)
ax.set_ylim(-5, 5)
ax.set_xlabel(r"$Time\ (s)$")
ax.set_ylabel(r"$Shear\ srtain (\%)$")

plt.savefig('time_u.png')
plt.show()