import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(6, 4))
ax = fig.gca()
df = pd.read_csv("shear.csv")

shear_stress = df["CH_1"]*3/(np.pi*2*(0.05**3-0.03**3))/1.0e3
pore_stress = df["CH_4"]

effe_stress = - pore_stress
stress_min = np.array(effe_stress).min()
effe_stress -= stress_min

ax.plot(effe_stress, shear_stress)
ax.set_xlabel(r"$Mean\ effective\ stress\ p\prime\ (kPa)$")
ax.set_ylabel(r"$Shear\ stress\ \tau\ (kPa)$")

plt.savefig('p-tau.png')
plt.show()