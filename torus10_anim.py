#!/Users/dora/anaconda3/bin/python

#%%

import yt
import os
import numpy as np
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib import rc_context
from moviepy.video.io.bindings import mplfig_to_npimage
from moviepy.editor import VideoClip
import moviepy.editor as mpy

HOME_DIR = "/local/data/atorus2/dora/Athena-tau/Torus10/bin/JOINT"
HOME_DIR = "/Volumes/USB_Drive/JOINT_VTK/"
HOME_DIR = "/Users/dora/WORK/SCRIPTS"

os.chdir(HOME_DIR)
print("WORK DIR=", os.getcwd())

ds=None
parameters = {"gamma":4./3., "geometry":"cylindrical",
              "periodicity":(False,False,False)}
ds = yt.load("Torus10.jnt.0099.vtk")

# dsi = yt.load("Torus10.jnt.009[0-9].vtk")

#%%
# print some stats
# ds.print_stats()
# ds.field_list
# ds.derived_field_list
# ds.index.max_level
# gs =ds.index.select_grids(0)

print(len(ds.r["z"].ndarray_view()))


# rotate some axes
print("x=", ds.coordinates.x_axis)
print("y=", ds.coordinates.y_axis)
ds.coordinates.x_axis[0]=2
ds.coordinates.x_axis[1]=0
ds.coordinates.y_axis[0]=1
ds.coordinates.y_axis[1]=2


#%%

#%%


#%%


#%%

plot = yt.SlicePlot(ds, "y", "density")

plot.show()

#%%

dat = dsi[0].all_data()

dn = dat["density"].to_ndarray()


#%%

print(dn[0][:][0])

#%%


# import matplotlib
# matplotlib.use("Agg")
# plot = yt.SlicePlot(ts[0], 'z', 'density')
# plot.set_zlim('density', 8e-29, 3e-26)
# fig = plot.plots['density'].figure


plot = yt.SlicePlot(dsi[0], "y", "density")

plot.show()

#%%

from matplotlib import pyplot as plt

slc = ds.slice('y', 0)

width = (4.9, 'cm')

res = [1000, 1000] # create an image with 1000x1000 pixels

frb = slc.to_frb(width, res)

# frb = slc.to_frb((20, (0,1)),'cm', 512)

dn = np.array(frb['density']) 

plt.imshow(np.log10(dn))

plt.savefig('my_perfect_figure.png')

plt.show()


# fig = plot.plots['density'].figure
# animate must accept an integer frame number. We use the frame number
# to identify which dataset in the time series we want to load
#%%

dn.shape
#%%

#%%
def make_frame_mpl(i):
    ds = dsi[i]
    return plot._switch_ds(ds)

make_frame_mpl(0)

#%%


duration = 20

clip =mpy.VideoClip(make_frame_mpl, duration=duration)

clip.write_videofile("my_animation.mp4", fps=24)    


#%%

plot = yt.SlicePlot(dsi[0], 'z', 'density')

fig = plot.plots['density'].figure

def animate(i):
    ds = dsi[i]
    plot._switch_ds(ds)


animation = FuncAnimation(fig, animate, frames=2)

FFMpegWriter = matplotlib.animation.writers['ffmpeg']

animation.save('animation.mp4', fps=30)