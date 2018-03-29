
#%%
import yt
import os
import numpy as np
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib import rc_context

print("done")

#%%
HOME_DIR = "/local/data/atorus2/dora/Athena-tau/Torus10/bin/JOINT"
HOME_DIR = "/Volumes/USB_Drive/JOINT_VTK/"
HOME_DIR = "/Users/dora/WORK/SCRIPTS/JOINT/"

os.chdir(HOME_DIR)

ds=None
parameters = {"gamma":4./3., "geometry":"cylindrical",
              "periodicity":(False,False,False)}

# ds = yt.load("Torus10.jnt.0090.vtk")

dsi = yt.load("Torus10.jnt.000[0-9].vtk")

print("done")

#%%
plot = yt.SlicePlot(dsi[0], "y", "density")

plot.show()


#%%

fig = plot.plots['density'].figure

def animate(i):
    ds = dsi[i]
    plot._switch_ds(dsi)

animation = FuncAnimation(fig, animate, frames=2)

FFMpegWriter = matplotlib.animation.writers['ffmpeg']

print("done 2")
#%%

animation.save('animation.mp4')

#%%

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1)

def update(data):
   line.set_ydata(data)
return line,

def data_gen():
   while True: yield np.random.rand(10)

ani = animation.FuncAnimation(fig, update, data_gen, interval=1000)
anim.save('basic_animation.mp4', fps=30)
plt.show()

#%%



import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

x = np.linspace(-2, 2, 200)

duration = 2

fig, ax = plt.subplots()
def make_frame(t):
    ax.clear()
    ax.plot(x, np.sinc(x**2) + np.sin(x + 2*np.pi/duration * t), lw=3)
    ax.set_ylim(-1.5, 2.5)
    return mplfig_to_npimage(fig)

animation = VideoClip(make_frame, duration=duration)
animation.ipython_display(fps=20, loop=True, autoplay=True)

#%%


import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()
l, = plt.plot([], [], 'k-o')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()

#%%
