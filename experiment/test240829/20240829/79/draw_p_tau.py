import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(6, 4))
ax = fig.gca()
df = pd.read_csv("shear.csv")

shear_stress = df["CH_1"]
pore_stress = df["CH_4"]

total_stress = 306.0

effe_stress = total_stress - pore_stress
stress_min = np.array(effe_stress).min()
effe_stress -= stress_min

ax.plot(effe_stress, shear_stress)

plt.show()