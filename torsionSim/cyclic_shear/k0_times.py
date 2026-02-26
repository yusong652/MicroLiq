import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import style as st
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# setting style
# st.use("seaborn-deep")
csr_arr = np.arange(0.20, 0.25, 0.05).tolist()
# csr_arr.append(0.235)
# k0s = [0.30, 0.33, 0.4, 0.5, 0.67, 1.0,
# 1.5, 2.0, 2.5, 3.0, 3.33]
k0s = [0.5, 0.67, 1.0, 1.5, 2.0]
ns_liq_total = []
# markers = ['*', 'h', 'p', 'd', 's','o', '^', 'v', '<', '>', 'P']
# colors = ['tab:cyan', 'tab:grey', 'tab:brown', 'tab:red', 'tab:orange',
#  'tab:blue', 'tab:purple', 'tab:green', 'tab:pink', 'tab:olive', 'gold']
markers = ['d', 's', 'o', '^', 'v']
colors = ['tab:orange', 'tab:red', 'tab:blue', 'tab:purple', 'tab:green']
fig1 = plt.figure(figsize=(6.0,5.0))
ax1 = plt.gca()

def plot_liq(k0, color, marker, state='AC'):
	ns_liq = []
	k0s = []
	csr=0.200
	file_name = "Dr90/k%.2f/csr_%.3f/torsion_shear.csv"%(k0, csr)
	facecolors = 'None'
	label = r'$K_0=:%.2f$'%k0
	size = 86
	try:
		df1 = pd.read_csv(file_name,header=0)
	except FileNotFoundError:
		return
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
	period = 1.0 / 8.0
	ind_liq = 0
	while stresses_u[ind_liq] < 0.95 * stress_ini:
		ind_liq += 1
	n_liq = time[ind_liq] / period
	###################################################
	ns_liq.append(n_liq)
	ns_liq_total.append(n_liq)
	k0s.append(k0)
	ax1.scatter(k0s, ns_liq, label=label,
		marker=marker, facecolors=facecolors, edgecolors=color,
		s=size)

for k0, marker, color in zip(k0s, markers, colors):
	plot_liq(k0, color, marker)

legend1 = ax1.legend(
	fontsize=13, ncol=4, framealpha=0.2, columnspacing=0.05, 
	loc=(-0.03, 1.08), handletextpad=0.1)
legend1._legend_box.align = "left"
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width, box.height*0.5])

# fitting line
handles_plt = []
def draw_fit():
	coefs_comp = np.polyfit(np.log(k0s[:6]), np.log(ns_liq_total[:6]),
		deg=2)
	xs_fit_comp = np.linspace(0.2, 1.0, 801)
	ys_fit_comp = (np.log(xs_fit_comp)**2 * coefs_comp[0] + 
		np.log(xs_fit_comp) * coefs_comp[1] +
		coefs_comp[2])
	ys_fit_comp = np.exp(ys_fit_comp)
	plt_line, = ax1.plot(xs_fit_comp, ys_fit_comp,
		label=r"$N_L-K_0\ fitting\ in\ compression\ state$",
		linestyle='-')
	handles_plt.append(plt_line)
	ax1.annotate(
		r"$Log(N_L)=%.1fLog^2(K_0)+%.1fLog(K_0)+%.1f$"%(coefs_comp[0], 
			coefs_comp[1], coefs_comp[2]),
		xy=(xs_fit_comp[200], ys_fit_comp[200]), 
		xytext=(0, -28),
		textcoords="offset points",
		bbox=dict(boxstyle="round", fc="w"),
		arrowprops=dict(arrowstyle='->',connectionstyle=\
		'arc3,rad=-0.12'),
		fontsize=8)

	coefs_comp = np.polyfit(np.log(k0s[5:]), np.log(ns_liq_total[5:]),
		deg=2)
	xs_fit_comp = np.linspace(1, 4.5, 901)
	ys_fit_comp = (np.log(xs_fit_comp)**2 * coefs_comp[0] + 
		np.log(xs_fit_comp) * coefs_comp[1] +
		coefs_comp[2])
	ys_fit_comp = np.exp(ys_fit_comp)
	plt_line, = ax1.plot(xs_fit_comp, ys_fit_comp,
		label=r"$N_L-K_0\ fitting\ in\ extension\ state$",
		linestyle='-.')
	handles_plt.append(plt_line)
	ax1.annotate(
		r"$Log(N_L)=%.1fLog^2(K_0)+%.1fLog(K_0)+%.1f$"%(coefs_comp[0], 
			coefs_comp[1], coefs_comp[2]),
		xy=(xs_fit_comp[580], ys_fit_comp[580]), 
		xytext=(-180, -38),
		textcoords="offset points",
		bbox=dict(boxstyle="round", fc="w"),
		arrowprops=dict(arrowstyle='->',connectionstyle=\
		'arc3,rad=0.2'),
		fontsize=8)

# draw_fit()

legends_plt = [r"$N_L-K_0\ fitting\ in\ compression\ state$",
r"$N_L-K_0\ fitting\ in\ extension\ state$"]
# ax1.legend(handles_plt, legends_plt,
# 	fontsize=10, framealpha=0.5, loc=(0.38, 0.82), ncol=1)
ax1.add_artist(legend1)

# plt.annotate(r"$Dense\ state$" + "\n" + r"$CSR=0.250$",
#  xy=(2.0, 15), fontsize=10)
plt.annotate(r"$CSR=0.200$", xy=(1.5, 15), fontsize=13)
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

ax1.set_xlim((0.2, 4.0))

ax1.set_ylim((10, 100))
ax1.grid(axis='both',which='major',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)
ax1.grid(axis='y',which='minor',color='grey',linestyle='--',
	lw=0.35,alpha=0.8)

ax1.set_xlabel(r'$Ratio\ of\ initial\ horizontal\ to\ vertical\ stress\ K_{0}$',
 fontsize=13)
ax1.set_ylabel(r'$Number\ of\ cyclic\ loading\ N_{L}$', fontsize=13)
ax1.set_yscale('log')
ax1.set_xscale('log')
ticks = [0.3, 0.5, 0.7, 1.0]
ticks.extend([1.5, 2.0, 3.0])
ax1.set_xticks(ticks)
ticklabels = ax1.get_xticks().tolist()
ax1.set_xticklabels(ticklabels)
ax1.tick_params(axis='both', which='major', labelsize=13)
ax1.tick_params(axis='both', which='minor', labelsize=13)
plt.tight_layout()
plt.savefig("k0_times.png",dpi=700)
plt.show()
