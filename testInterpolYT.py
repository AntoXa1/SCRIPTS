
#!/Users/dora/anaconda3/bin/python
#%%
# %load_ext autoreload
# %autoreload 2

import numpy as np
import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as mpl

from scipy.interpolate import interp1d
from scipy.ndimage import map_coordinates


def polar2cartesian(r, t, grid, x, y, order=3):

    X, Y = np.meshgrid(x, y)

    new_r = np.sqrt(X*X+Y*Y)
    new_t = np.arctan2(X, Y)

    ir = interp1d(r, np.arange(len(r)), bounds_error=False)
    it = interp1d(t, np.arange(len(t)))

    new_ir = ir(new_r.ravel())
    new_it = it(new_t.ravel())

    new_ir[new_r.ravel() > r.max()] = len(r)-1
    new_ir[new_r.ravel() < r.min()] = 0

    return map_coordinates(grid, np.array([new_ir, new_it]),
                            order=order).reshape(new_r.shape)

# Define original polar grid

nr = 10
nt = 10

r = np.linspace(1, 100, nr)
t = np.linspace(0., np.pi, nt)
z = np.random.random((nr, nt))

# Define new cartesian grid

nx = 100
ny = 200

x = np.linspace(0., 100., nx)
y = np.linspace(-100., 100., ny)

# Interpolate polar grid to cartesian grid (nearest neighbor)

fig = mpl.figure()
ax = fig.add_subplot(111)
ax.imshow(polar2cartesian(r, t, z, x, y, order=0), interpolation='nearest')

print("done")

# # Interpolate polar grid to cartesian grid (cubic spline)

# fig = mpl.figure()
# ax = fig.add_subplot(111)
# ax.imshow(polar2cartesian(r, t, z, x, y, order=3), interpolation='nearest')




#%%



#%%


from AthenaModelVTK import *
import yt
import numpy as np

vtkFile="Torus10.jnt.0099.vtk"
vtkFile="Torus10.0000.vtk"

cdat = athDataVTK()
cdat.loadSimDataVTK(vtkFile)

ncx = max(cdat.nr, cdat.nt, cdat.nz)
dims =(cdat.nr, cdat.nt, cdat.nz)
print("cart box size", ncx)

#%%

# from scipy.interpolate import griddata
# cdat.r[:,0,:]
# x=zeros(24).reshape((4,6))
# # x.tolist()
# print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in x]))

# x
#%%

# x = 0.5*(cdat.x[0,0,:-1]+cdat.x[0,0,1:])
# t = 0.5*(cdat.t[0,:-1,0]+cdat.t[0,1:,0])
# z = 0.5*(cdat.z[:-1,0,0]+cdat.z[1:,0,0])


r = 0.5*(cdat.r[:-1,0,0]+cdat.r[1:,0,0])
t = 0.5*(cdat.t[0,:-1,0]+cdat.t[0,1:,0])
z = 0.5*(cdat.z[0,0,:-1]+cdat.z[0,0,1:])

d_rt = cdat.d[:,:,0]
x = nm.zeros(cdat.nr)
x=r
y = nm.zeros(cdat.nr)
y = nm.linspace(0,2,cdat.nr)


polar2cartesian(r, t, d_rt, x, y, order=0)

# X,T = nm.meshgrid(r,t)
# xg = X*nm.cos(T)
# yg = X*nm.sin(T)
# X,Y = nm.meshgrid(r,r)
# griddata(xg, yg, cdat.d, X, Y )

# xg


#%%



#%%
xg[0,:]
# nm.shape(xg)
#%%
# cdat.z[:,0,0]
# len(cdat.t[0,:,0])


# self.t = 0.5*(self.t[:,:-1,:]+self.t[:,1:,:])
# self.z = 0.5*(self.z[:,:,:-1]+self.z[:,:,1:])

# len(z[10,:,10])

# len(cdat.x[:,0,0])


#%%

import socket
machine =socket.gethostname()
if machine=='atorus':
     putToDataDirs= '/local/data/atorus1/dora/PROJECTS/'

     locdirList = [ 'AthenaWind_cln3/bin/', 'AthenaWind_cln2/bin/']
     paramFile =  [  putToDataDirs + x.replace('/bin',"") +'/tst/cylindrical' for  x in locdirList ]
     print(paramFile);

     put_out= '/local/data/atorus1/dora/PROJECTS/SCRIPTS/T9/'
     put_FIG = '/local/data/atorus1/dora/PROJECTS/SCRIPTS/T9/'

     filelist = ['mhdXwind.0150.bin', 'mhdXwind.0350.bin', 'mhdXwind.0595.bin']     
     dataFileList = [filelist, filelist]

elif machine=='Antons-MacBook-Pro.local':
     putToDataDirs= '/Users/dora/WORK/SCRIPTS'
     locdirList = ['/']
     paramFile =  [  putToDataDirs + x  for  x in locdirList ]
     paramFile[0] += 'athinput.torus10'
     
    #  put_out= '/Users/dora/WORK/ECLIPSE_SPACE/torus9'
    #  put_FIG = '/Users/dora/Documents/TEX/torus9/'
    #  dataFileList = [['mhdXwind.0050.bin', 'mhdXwind.0150.bin', 'mhdXwind.0340.bin'], \
    #                             ['mhdXwind.0050.bin', 'mhdXwind.0150.bin', 'mhdXwind.0340.bin']]
else:
    pass

print("paramFile = ", paramFile[0])
cdat.loadSimulationParam(paramFile[0], print_res=False)


#%%

# projecting on a cart. grid

x = nm.zeros(cdat.nx)
y = nm.zeros(cdat.nx)

x = cdat.x[:,0,0]
y=x

print(cdat.x[:,0,0].size, x.size)


# print(x)

#%%



#%%

x2 = cdat.x[:,:,0]*nm.cos(cdat.t[:,:,0])
y2 = cdat.x[:,:,0]*nm.sin(cdat.t[:,:,0])


print(nm.shape(y2), nm.shape(cdat.d), nm.shape(cdat.x))


#%%








# data = dict(density = (cdat.d, "1"), r=(cdat.x,'cm'), z=(cdat.z,'cm'))
# bbox = np.array([[0.1, 5], [-2.5, 2.5], [-2.5, 2.5]])
# ds = yt.load_uniform_grid(data, cdat.d.shape, length_unit="cm", \
#                           geometry="cylindrical", bbox=bbox, nprocs=1)
# slc = yt.SlicePlot(ds, "r", ["density"])
# slc.show()
# s1 = ds.slice(2,np.pi/2)

# @yt.derived_field(name = "xcl", units = "cm", take_log=False)
# def xcl(field, data):
#     return np.cos(data["theta"])*data["r"]

# @yt.derived_field(name = "ycl", units = "cm", take_log=False)
# def ycl(field, data):
#     return np.sin(data["theta"])*data["r"]

# @yt.derived_field(name = "zcl", units = "cm", take_log=False)
# def zcl(field, data):
#         return data["z"]

# def funfield(field, data):
#     return (np.cos(data["theta"])**2)
# s = yt.SlicePlot(ds, "theta", ["xcl", "ycl", "zcl"])
# s.show()
    
    
    
