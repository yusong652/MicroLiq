import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# setting style
# st.use("seaborn-deep")

df1 = pd.read_csv("torsion_shear.csv",header=0)
strains = df1["strain_shear"] * 100.
# overall data
stresses_shear = df1["stress_shear"] / 1000.
stresses_out = df1["stress_outer"] / 1000.
stresses_in =df1["stress_inner"] / 1000.
stresses_ini = stresses_out[0] + stresses_in[0] / 2.0
stresses_u = -(stresses_in + stresses_out) / 2 + stresses_ini
stresses_z = df1["stress_z"] / 1000.0

stresses_p = (stresses_in + stresses_out + stresses_z) / 3.0
# measurement ball data
time = df1["time_duration"]
fig1 = plt.figure(figsize=(6.0,4))
ax1 = plt.gca()
# ax1.set_title(r"$Triaxial\ Compression$")
# xmajorLocator = MultipleLocator(5)
# xmajorFormatter = FormatStrFormatter('%5.0f')
# ymajorLocator = MultipleLocator(1000)
# ymajorFormatter = FormatStrFormatter('%1.1f')
# ax1.xaxis.set_major_locator(xmajorLocator)
# ax1.xaxis.set_major_formatter(xmajorFormatter)
# ax1.yaxis.set_major_locator(ymajorLocator)
# ax1.yaxis.set_major_formatter(ymajorFormatter)
# xminorLocator = MultipleLocator(1)
# yminorLocator = MultipleLocator(200)
# ax1.xaxis.set_minor_locator(xminorLocator)
# ax1.yaxis.set_minor_locator(yminorLocator)
# ax1.set_ylim((3000,9000))
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
flt = time < 5.4
ax1.plot(strains[flt][::16],stresses_shear[flt][::16],linewidth=1.2,
	label=r"$Stress-strain$" + '\n' + r"$relationship$",)
ax1.legend(fontsize=13, framealpha=0.5, loc='lower right')
ax1.set_ylabel(r'$Shear\ stress\ \tau\ (kPa)$', fontsize=13)
ax1.set_xlabel(r'$Shear\ strain\ \gamma\ (\%)$', fontsize=13)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-30, 30)
ax1.tick_params(axis='both', which='major', labelsize=13)
# ax1.legend(fontsize=8,loc=(0.55,0.38))

# ax2 = ax1.twinx()
# ax2.set_ylabel(r"$Stress_{x}(kPa)$")
# ymajorLocator = MultipleLocator(1000)
# ax2.yaxis.set_major_locator(ymajorLocator)
# ymajorFormatter = FormatStrFormatter('%1.1f')
# ax2.yaxis.set_major_formatter(ymajorFormatter)
# yminorLocator = MultipleLocator(200)
# ax2.yaxis.set_minor_locator(yminorLocator)
# ax2.set_ylim((3000,9000))
# stresses_x = df1["stress_x"] / 1000.
# # measurement ball data
# stresses_x_mid = -df1["stress_x_mb1"] / 1000.
# stresses_x_top = -df1["stress_x_mb2"] / 1000.
# stresses_x_bot = -df1["stress_x_mb3"] / 1000.
# ax2.plot(strains_z,stresses_x,linewidth=0.3,
# 	label=r"$Stress_{x}$",marker='<',
# 	markevery=0.1,markersize=5,markerfacecolor="none",
# 	)
# ax2.plot(strains_z,stresses_x_mid,linewidth=0.3,
# 	label=r"$Stress_{x}\ m_{mid}$",marker='<',
# 	markevery=0.1,markersize=5,markerfacecolor="none",
# 	)
# ax2.plot(strains_z,stresses_x_top,linewidth=0.3,
# 	label=r"$Stress_{x}\ m_{top}$",marker='<',
# 	markevery=0.1,markersize=5,markerfacecolor="none",
# 	)
# ax2.plot(strains_z,stresses_x_bot,linewidth=0.3,
# 	label=r"$Stress_{x}\ m_{bot}$",marker='<',
# 	markevery=0.1,markersize=5,markerfacecolor="none",
# 	)

# ax2.legend(fontsize=8,loc=(0.75,0.38))
plt.tight_layout()
plt.savefig("stress_strain.png",dpi=350)
plt.show()
