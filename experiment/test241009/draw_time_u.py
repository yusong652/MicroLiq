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

freq = 0.05
time = np.linspace(0, len(effe_stress)*freq, len(effe_stress))

ax.plot(time, pore_stress)
ax.set_xlabel(r"$Time\ (s)$")
ax.set_ylabel(r"$Pore\ water\ stress\ (kPa)$")

plt.savefig('time_u.png')
plt.show()