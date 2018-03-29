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
geom = "cylindrical"
geom = "cart"

if geom=="cylindrical":
    pars = {"gamma":4./3., "geometry":geom,
                "periodicity":(False,False,False)}


    ds = yt.load("Torus10.jnt.0099.vtk", parameters=pars)
else:
    ds = yt.load("Torus10.jnt.0099.vtk")


# dsi = yt.load("Torus10.jnt.009[0-9].vtk")


# print some stats
ds.print_stats()
ds.field_list
ds.derived_field_list
ds.index.max_level
gs =ds.index.select_grids(0)
print("z len = " , len(ds.r["z"].ndarray_view()))


# rotate some axes
if geom == "cart":
    print("x=", ds.coordinates.x_axis)
    print("y=", ds.coordinates.y_axis)
    
    ds.coordinates.x_axis[0]=2
    ds.coordinates.x_axis[1]=0
    ds.coordinates.y_axis[0]=1
    ds.coordinates.y_axis[1]=2

#%%
what2doI = ["LIC","Slice", "frb"]

what2do = what2doI[2]

fToSave = "Torus10.jnt.0099"

# splt.annotate_line_integral_convolution('cell_centered_B_x', 'cell_centered_B_z', lim=(0.5,0.65),
#                                      alpha=1, const_alpha=False)

if what2do == "LIC":
    splt = yt.SlicePlot(ds, "y", "density")
    
    

    # splt = ds.slice('y', 0)
    
    # splt = ds.proj('density', 1)

    splt.annotate_line_integral_convolution('cell_centered_B_x', 'cell_centered_B_z', lim=(0.5,0.65), 
                                          alpha=1., const_alpha=True)
    # splt.annotate_clearset_xlim("all", 0.0, 4.0)

    splt.hide_colorbar()

    
    splt.set_width

    splt.show()
    fToSave = fToSave+"_LIC"



if what2do == "Slice":
    splt = yt.SlicePlot(ds, "y", "density")
    splt.set_log('density', True)
    fToSave = fToSave+"_Slc"

    
    splt.hide_colorbar()

    splt.show()
if what2do == "frb":
    from matplotlib import pyplot as plt
    fToSave = fToSave+"_Frb"

    slc = ds.slice('y', 0)

    res = [1000, 1000] # create an image with nxm pixels
    width = (8, 'cm')
    frb = slc.to_frb(width, res)

    dn = np.array(frb['density']) 
    plt.imshow(np.log10(dn))
    plt.show()

splt.save(fToSave)
#%%

#  useful grid inspection:

# all_data_level_0 = ds.covering_grid(level=0, left_edge=[0,0.0,0.0],
#                                       dims=ds.domain_dimensions)
print(ds.covering_grid)

print(ds.domain_dimensions)

print(all_data_level_0['density'].shape)

# print(all_data_level_0['density'])

#%%
dn3 = np.array(all_data_level_0['density'])
dn2 = dn3[:,25,:]

print(dn2.shape)

plt.imshow(np.log10(np.abs(dn2)))
#%%
