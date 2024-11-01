import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(6, 4))
ax = fig.gca()
df = pd.read_csv("shear.csv")

pore_stress = df["CH_4"]
shear_stress = df["CH_1"]*3/(np.pi*2*(0.05**3-0.03**3))/1.0e3
effe_stress = - pore_stress
stress_min = np.array(effe_stress).min()
effe_stress -= stress_min

freq = 0.05
time = np.linspace(0, len(effe_stress)*freq, len(effe_stress))

ax.plot(time, shear_stress)
ax.set_xlabel(r"$Time\ (s)$")
ax.set_ylabel(r"$Shear\ stress\ \tau\ (kPa)$")

plt.savefig('time_u.png')
plt.show()