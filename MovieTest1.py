#!/Users/dora/anaconda3/bin/python
#%%

import os
from AthenaModelVTK import *
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as manimation



HOME_DIR = "/local/data/atorus2/dora/Athena-tau/Torus10/bin/JOINT"
HOME_DIR = "/Volumes/USB_Drive/JOINT_VTK/"
HOME_DIR = "/Users/dora/WORK/SCRIPTS/JOINT/"

from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

os.chdir(HOME_DIR)
cdat = athDataVTK()

print("done..")
#%%
vtkFile=HOME_DIR+"Torus10.jnt.0002.vtk"


print(vtkFile)

cdat = athDataVTK()
cdat.loadSimDataVTK(vtkFile)

Z, X = np.meshgrid(cdat.z[0,0,:], cdat.r[:,0,0])
fig = plt.figure()
ax = fig.add_subplot(111)
im=plt.imshow(  np.transpose(cdat.d[:,0,:]), origin="lower" )

plt.show() 
plt.imsave(HOME_DIR+'test.png',np.transpose(cdat.d[:,0,:]))


# plt.imsave('test.png', ax)


#%%

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()
MOV = False
if MOV:

    with writer.saving(fig, "writer_test.mp4", 100):

        for vtkFile in os.listdir(HOME_DIR):
            print(vtkFile)
            if vtkFile.startswith("Torus10.jnt.000"):
                print(vtkFile)
                
                cdat.loadSimDataVTK(vtkFile)
                Z, X = np.meshgrid(cdat.z[0,0,:], cdat.r[:,0,0])

                # ax = fig.add_subplot(111)
                im=plt.imshow(  np.transpose(cdat.d[:,0,:]), origin="lower" )
                writer.grab_frame()

else:
    for vtkFile in os.listdir(HOME_DIR):

            if vtkFile.startswith("Torus10.jnt.000"):
                print(vtkFile)

                cdat = athDataVTK()

                cdat.loadSimDataVTK(vtkFile)

                Z, X = np.meshgrid(cdat.z[0,0,:], cdat.r[:,0,0])

                ax = fig.add_subplot(111)
                
                im=plt.imshow(np.transpose(cdat.d[:,0,:]), origin="lower" )
                plt.show()  
                # plt.imsave(vtkFile+'.png', im)


#%%

# import matplotlib.pyplot as plt
# import numpy as np

# from moviepy.video.io.bindings import mplfig_to_npimage
# from moviepy.editor import VideoClip
# import moviepy.editor as mpy

# # DRAW A FIGURE WITH MATPLOTLIB

# duration = 20

# fig_mpl, ax = plt.subplots(1,figsize=(5,3), facecolor='white')

# xx = np.linspace(-2,2,200) # the x vector
# zz = lambda d: np.sinc(xx**2)+np.sin(xx+d) # the (changing) z vector
# ax.set_title("Elevation in y=0")
# ax.set_ylim(-1.5,2.5)
# line, = ax.plot(xx, zz(0), lw=3)
# print(line)


# # ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.

# def make_frame_mpl(t):
#     line.set_ydata( zz(2*np.pi*t/duration))  # <= Update the curve
#     return mplfig_to_npimage(fig_mpl) # RGB image of the figure

# # clip =mpy.VideoClip(make_frame_mpl, duration=duration)

# # clip.write_videofile("my_animation.mp4", fps=24)

# # animation.write_gif("sinc_mpl.gif", fps=20)

# # ============================================================

