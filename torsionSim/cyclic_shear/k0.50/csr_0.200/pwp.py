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
stress_ini = (stresses_out[0] + stresses_in[0]) / 2.0
stresses_u = -(stresses_in + stresses_out) / 2 + stress_ini
stresses_z = df1["stress_z"] / 1000.0

stresses_p = (stresses_in + stresses_out + stresses_z) / 3.0
# measurement ball data
time = df1["time_duration"]

###################################################
#  find the index when liquefaction occurs
period = 1.0 / 16.0
ind_liq = 0
while stresses_u[ind_liq] < 0.95 * stress_ini:
	ind_liq += 1
n_liq = time[ind_liq] / period
print(n_liq)
###################################################

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
time_lmt = 3.852
ax1.set_ylim((-0.1, 1.0))
ax1.set_xlim((0.0, time_lmt/period))
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
flt = time < time_lmt
ax1.plot(time[flt]/period,stresses_u[flt]/stress_ini,
	linewidth=1.2,label=r"$EPWP\ ratio\ time\ series$",)
ax1.plot((time[ind_liq]/period, time[ind_liq]/period), 
	(-0.1, stresses_u[ind_liq]/stress_ini), color='tab:red', 
	linestyle='dashed',linewidth=1.4)
ax1.plot((0.0, time[ind_liq]/period),
 (stresses_u[ind_liq]/stress_ini, stresses_u[ind_liq]/stress_ini),
 color='tab:red', linestyle='dashed', linewidth=1.4)
ax1.set_ylabel(r'$EPWP\ ratio\ u/\sigma_{h0}\prime$', fontsize=13)
ax1.set_xlabel(r'$Number\ of\ cyclic\ loading\ N_{c}$', fontsize=13)
ax1.legend(fontsize=13,loc=(0.06,0.72))

ax1.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 0.95, 1.0])
ax1.set_yticklabels([0.0, 0.2, 0.4, 0.6, 0.8, '', 1.0])
ax1.text(-time[ind_liq]/period*0.08-0.2, 0.92, r"$0.95$", color='tab:red',
 fontsize=13)
ax1.text(time[ind_liq]/period-0.36, -0.168, r"$N_{L}$", color='tab:red',
 fontsize=13)
ax1.tick_params(axis='both', which='major', labelsize=13)
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
plt.savefig("stress_u.png",dpi=350)
plt.show()
