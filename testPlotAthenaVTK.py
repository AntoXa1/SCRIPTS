#!/Users/dora/anaconda3/bin/python

#%%

from matplotlib import pyplot as plt
import numpy as np
# from AthenaModelVTK import *

import AthenaModelVTK
import socket
import importlib

AthenaModelVTK=importlib.reload(AthenaModelVTK)

vtkFile="Torus10.0000.vtk"
vtkFile="Torus10.jnt.0099.vtk" 

dat = AthenaModelVTK.athDataVTK()
dat.loadSimDataVTK(vtkFile)



Z, X = np.meshgrid(dat.z[0,0,:], dat.r[:,0,0])

# X,Z = np.meshgrid(dat.x[:,0,0], dat.z[0,0,:])
# print(np.shape(dat.x))

#%%
f = plt.figure()    


# ax = f.add_subplot(111)
# im=plt.imshow(  np.transpose(dat.u2[:,0,:]), origin="lower" )

# print(np.shape(X))
# print(np.shape(dat.u3[:,0,:]))
# print(dat.u3[:,0,:])

stp=10

ist = 0
ie = dat.nr-1

ks = 0
ke = dat.nz-1

jp=20

        
Mx = np.transpose(dat.u1)
Mz = np.transpose(dat.u3)

qp1 = plt.quiver((Mx[ist:ie:stp,jp,ks:ke:stp]),\
        (Mz[ist:ie:stp, jp, ks:ke:stp]),\
        width=0.003, scale=10,\
        pivot='mid', color='black',\
        edgecolors=('black'))



# qp1 = plt.quiver(X, Z, (momx), 
#                         (momz), width=0.008, scale=7.,                            
#         pivot='mid', color='black', 
#         units='x' , headwidth =5, headlength =7,
#         linewidths=(0.5,), edgecolors=('black'))


plt.show()

#%%
# im=plt.imshow(  np.transpose(np.log10(dat.d[:,0,:])), origin="lower" )

