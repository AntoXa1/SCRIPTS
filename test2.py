#!/Users/dora/anaconda3/bin/python
#%%

import yt
import os
import numpy as np
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib import rc_context

# from moviepy.video.io.bindings import mplfig_to_npimage
# from moviepy.editor import VideoClip
# import moviepy.editor as mpy

import matplotlib.pyplot as plt


HOME_DIR = "/local/data/atorus2/dora/Athena-tau/Torus10/bin/JOINT"
HOME_DIR = "/Volumes/USB_Drive/JOINT_VTK/"
os.chdir(HOME_DIR)

ds=None
parameters = {"gamma":4./3., "geometry":"cylindrical",
              "periodicity":(False,False,False)}

# dsi = yt.load("Torus10.jnt.009[0-9].vtk", parameters=parameters)

ds= yt.load("Torus10.jnt.0099.vtk", parameters=parameters)

#%%
# dsi = yt.load("Torus10.jnt.009[0-9].vtk")


# dsi = yt.load("Torus10.jnt.009[0-9].vtk ")

plot = yt.SlicePlot(ds, "x", "density")

# plot = yt.SlicePlot(dsi[0], "z", "density")

fig = plot.plots['density'].figure


plot.show()
#%%

ds.derived_field_list
#%%

yt.ProjectionPlot(ds, "theta", "density")

#%%


print( ds.coordinates.x_axis)
print( ds.coordinates.y_axis)

#%%
# # 

# def animate(i):
#     ds = dsi[i]
#     plot._switch_ds(ds)

# animation = FuncAnimation(fig, animate, frames=len(dsi) )

# # Override matplotlib's defaults to get a nicer looking font
# with rc_context({'mathtext.fontset': 'stix'}):
#     animation.save('animation.mp4')

