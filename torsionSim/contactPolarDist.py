import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.colors
import matplotlib.pyplot as plt
import csv

class PolarDist():

	def __init__(self):
		self.finesse = 8
		self.read_file(36,18,file_name='distContacts.csv')
		# self.density_max = self.df[:,:self.number_u*self.number_v].max()/53764
		# self.density_min = self.df[:,:self.number_u*self.number_v].min()/53764
		self.density_max = 0.5
		self.density_min = 0.0

	def read_file(self, number_u, number_v, file_name):
		self.df = pd.read_csv(file_name,header=0).to_numpy()
		self.file_n = file_name
		self.number_u = number_u
		self.number_v = number_v

	def get_density_color(self, row_index):
		self.density = \
		self.df[row_index][:self.number_u*self.number_v]/53764
		self.density = \
		self.density.reshape(self.number_u,self.number_v)
		self.color_map = self.density / (self.density_max - self.density_min)

	def get_fig_ax(self):
		self.fig = plt.figure(figsize=(6., 6.))
		self.ax = self.fig.add_subplot(111, projection='3d')
		self.ax.set_box_aspect((1, 1, 1))

	def get_sphere_surface(self, transp=0.5):
		"plotting the surface"
		for m in np.arange(self.number_u):
		    for n in np.arange(self.number_v):
		        start1 = m * 2 * np.pi / self.number_u
		        start2 = n * np.pi / self.number_v
		        u = np.linspace(start1, start1 + 2 * \
		            np.pi / self.number_u, self.finesse,
		            endpoint=True)
		        v = np.linspace(start2, start2 + np.pi / \
		            self.number_v, self.finesse,
		            endpoint=True)
		        r = self.density[m,n]
		        x = r * np.outer(np.cos(u), np.sin(v))
		        y = r * np.outer(np.sin(u), np.sin(v))
		        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
		        color_scalar = self.color_map[m,n]
		        if color_scalar > 1:
		        	color_scalar = 1
		        elif color_scalar < 0:
		        	color_scalar = 0
		        pot = np.outer(np.ones(np.size(u)), \
		            np.ones(np.size(v))) * color_scalar
		        colors = plt.cm.rainbow(pot) 
		        surf = self.ax.plot_surface(x,y,z, facecolors=colors,
		            linewidth=0.2, antialiased=True, alpha=transp)

	def get_plane_lr(self, transp=0.5):
		"plotting the plane on the left and right"
		for m in np.arange(self.number_u):
		    for n in np.arange(self.number_v):
		        start1 = n * np.pi / self.number_v
		        u = m * 2 * np.pi / self.number_u
		        r0 = self.density[m,n]
		        r = np.linspace(0, r0, self.finesse)
		        v = np.linspace(start1, start1 + np.pi/self.number_v,\
		         self.number_v)
		        x = np.cos(u) * np.outer(np.sin(v), r)
		        y = np.sin(u) * np.outer(np.sin(v), r)
		        z = np.outer(np.cos(v), r)
		        color_scalar = self.color_map[m,n]
		        pot = np.outer(np.ones(np.size(v)), \
		        np.ones(np.size(r))) * color_scalar
		        colors = plt.cm.rainbow(pot) 
		        plane_lr1 = self.ax.plot_surface(x,y,z,facecolors=colors,
		            linewidth=0.2, alpha=transp, antialiased=True)

		        x = np.cos(u + 2 * np.pi / self.number_u) *\
		         np.outer(np.sin(v), r)
		        y = np.sin(u + 2 * np.pi / self.number_u) *\
		         np.outer(np.sin(v), r)
		        z = np.outer(np.cos(v), r)
		        pot = np.outer(np.ones(np.size(v)), \
		        np.ones(np.size(r))) * color_scalar
		        colors = plt.cm.rainbow(pot) 
		        plane_lr2 = self.ax.plot_surface(x,y,z,facecolors=colors,
		            linewidth=0.2, alpha=transp, antialiased=True)

	def get_plane_tb(self, transp=0.5):
		"plotting the plane on the top and bottom"
		for m in np.arange(self.number_u):
		    for n in np.arange(self.number_v):
		        start1 = m * 2 * np.pi / self.number_u
		        v = n * np.pi / self.number_v
		        r0 = self.density[m,n]
		        r = np.linspace(0, r0, self.finesse)
		        u = np.linspace(start1, start1 + 2 * np.pi / \
		            self.number_u)
		        x = np.sin(v) * np.outer(np.cos(u), r)
		        y = np.sin(v) * np.outer(np.sin(u), r)
		        z = np.cos(v) * np.outer(np.ones(np.size(u)), r)
		        color_scalar = self.color_map[m,n]
		        pot = np.outer(np.ones(np.size(u)), \
		        np.ones(np.size(r))) * color_scalar
		        colors = plt.cm.rainbow(pot) 
		        plane_tb1 = self.ax.plot_surface(x,y,z,facecolors=colors,
		            linewidth=2, alpha=transp)

		        x = np.sin(v + np.pi / self.number_v) *\
		         np.outer(np.cos(u), r)
		        y = np.sin(v + np.pi / self.number_v) *\
		         np.outer(np.sin(u), r)
		        z = np.cos(v + np.pi / self.number_v) *\
		         np.outer(np.ones(np.size(u)), r)
		        pot = np.outer(np.ones(np.size(u)), \
		        np.ones(np.size(r))) * color_scalar
		        colors = plt.cm.rainbow(pot) 
		        plane_tb2 = self.ax.plot_surface(x,y,z,facecolors=colors,
		            linewidth=2, alpha=transp)

	def get_cb(self):
		"getting the colorbar"
		# norm = matplotlib.colors.SymLogNorm(1,
		#     vmin=self.density_min,vmax=self.density_max)

		sm = plt.cm.ScalarMappable(cmap=plt.cm.rainbow)
		sm.set_array(np.array([self.density_min, self.density_max]))
		#modify the position of colorbar
		cbaxes = self.fig.add_axes([0.85, 0.35, 0.02, 0.3]) 
		self.cb = self.fig.colorbar(sm,cax=cbaxes,)
		self.cb.set_label(r"$Contact\ Density$", fontsize=15)

	def get_dist_fig(self):
		for row in np.arange(0, 421):
			self.get_fig_ax()
			self.get_density_color(row*1)
			self.get_sphere_surface()
			self.get_plane_lr()
			self.get_plane_tb()
			self.get_cb()
			self.ax.zaxis.set_rotate_label(False)
			self.ax.set_xlabel(r"$Circumferential$", fontsize=16,
				labelpad=1)
			self.ax.set_ylabel(r"$Radial$", fontsize=16,
				labelpad=1)
			self.ax.set_zlabel(r"$Axial$", fontsize=16, rotation=90,
				labelpad=1)
			self.ax.set_xlim(-self.density_max,self.density_max)
			self.ax.set_ylim(-self.density_max,self.density_max)
			self.ax.set_zlim(-self.density_max,self.density_max)
			timeIncrement = 0.01
			time = row * timeIncrement
			# self.ax.set_title(r'$Contact\ Distribution\ (Deviatoric=)$',
			# 	fontsize=10)
			# remove formatter from the axes
			self.ax.xaxis.set_major_formatter(plt.NullFormatter())
			self.ax.yaxis.set_major_formatter(plt.NullFormatter())
			self.ax.zaxis.set_major_formatter(plt.NullFormatter())
			# Hide grid lines
			self.ax.grid(False)

			# Hide axes ticks
			self.ax.set_xticks([])
			self.ax.set_yticks([])
			self.ax.set_zticks([])
			# change view angle
			figName = "contact_density_time_" + str(round(time,3))
			self.ax.view_init(elev=15, azim=-110)
			plt.tight_layout()
			self.fig.savefig(f'{figName}.jpg', dpi=500)
			self.fig.clear()
			plt.close(self.fig)

polar_dist = PolarDist()
polar_dist.get_dist_fig()