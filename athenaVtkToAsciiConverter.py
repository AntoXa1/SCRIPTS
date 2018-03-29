#!/Users/dora/anaconda3/bin/python
#%%


from AthenaModelVTK import *
import socket
import numpy as np

vtkFile="Torus10.0000.vtk"
vtkFile="Torus10.jnt.0099.vtk" 

dat = athDataVTK()
dat.loadSimDataVTK(vtkFile)
        


#%%

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

print(paramFile[0])


dat.loadSimulationParam(paramFile[0], print_res=True)


tmp = vtkFile.split('.')
fileToWrite = tmp[0]+'.'+tmp[2]+".ascii.dat"
print(fileToWrite)

#%%
Mx = np.transpose(dat.u1)
Mz = np.transpose(dat.u3)

f = open(fileToWrite, 'w')

f.write("Fortran-style indexing: F(i,j,k) \n:\
do z=>k =slowest, phi=>j, x=>i=fastest \n\n " )

strToWrite ="nr:" +str(dat.nx-1)+' nph:'+str(dat.nt-1)+' nz:'+str(dat.nz-1)+"\n"
f.write(strToWrite)

print("writing x-coord")
f.write("i-coord: cyl. radius [cm]\n")
for i in range(0,dat.nx):
    f.write(str(dat.Rsc*dat.x[i,0,0])+"\n")       

print("writing phi-coord")
f.write("\n")
f.write("j-coord: theta [rad] \n")
for j in range(0,dat.nt):
    f.write(str(dat.t[0,j,0])+"\n")       

print("writing z-coord, [cm]")
f.write("\n")
f.write("k-coord: z \n")
for k in range(0,dat.nz):
    f.write(str(dat.Rsc*dat.z[0,0,k])+"\n")       


print("writing number density [cm^-3]")
f.write("\n")
f.write("density [cm^-3] \n")
for k in range(0,dat.nz-1):
    for j in range(0,dat.nt-1):
        for i in range(0,dat.nx-1):
            # strToWrite = str(i)+str(j)+str(k)+' '+str(dat.nc0*dat.d[i,j,k])+ "\n"
            strToWrite = str(dat.nc0*dat.d[i,j,k])+ "\n"
            f.write(strToWrite)       

print("writing Vr_cyl velocity [cm s^-1]")
f.write("\n")
f.write("Vr_cyl velocity [cm s^-1]\n")
for k in range(0,dat.nz-1):
    for j in range(0,dat.nt-1):
        for i in range(0,dat.nx-1):
            # strToWrite = str(i)+str(j)+str(k)+' '+str(dat.Usc*Mx[i,j,k])+ "\n"
            strToWrite = str(dat.Usc*Mx[i,j,k])+ "\n"
            f.write(strToWrite)   

print("writing Vz velocity [cm s^-1]")
f.write("\n")
f.write("Vr_cyl velocity [cm s^-1]\n")

for k in range(0,dat.nz-1):
    for j in range(0,dat.nt-1):
        for i in range(0,dat.nx-1):
            # strToWrite = str(i)+str(j)+str(k)+' '+str(dat.Usc*Mz[i,j,k])+ "\n"
            strToWrite = str(dat.Usc*Mz[i,j,k])+ "\n"
            f.write(strToWrite)    


print("athenaVtkToAsciiConverter ... done")
f.close()


