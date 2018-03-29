#!/Users/dora/anaconda3/bin/python

#%%
import numpy as nm
from vtk import vtkStructuredPointsReader
from vtk.util import numpy_support as VN
from physics_const import * 
import re

class athDataVTK:
    """ reads data from VTK file    """

    def __init__(self):
        self.vec=None
        self.nr=None
        self.nt=None
        self.nz=None
        self.data=None
        self.file=None

        self.r = None
        self.t = None
        self.z = None
        self.d = None
        self.P = None
        self.u1 = None
        self.u2 = None
        self.u3 = None

        self.Mbh=0
        self.MBH_g=None

        self.beta=0.
        self.nc0=0.
        self.Rsc=0
        self.Usc=0.
        self.Dsc=0.
        self.tsc=None

        self.nvar =0    
        self.nscalars=0
        self.ifselfg=0
        self.ifpart=0
        self.par=None

        
        self.xmin   = None
        self.xmx    = None
        self.zmin   = None
        self.zmx    = None

        self.reader = vtkStructuredPointsReader()
        print("athDataVTK :: constructor")
    
    # def __del__(self):
    #     print('died')

    def loadSimDataVTK(self,fileN):
        
        self.fileName=fileN
        
        try:
            self.reader.SetFileName(self.fileName)
            print("trying .. ",self.fileName)
        
        except IOError:
            print ("Could not read file:", self.fileName)
    
        self.reader.ReadAllVectorsOn()
        self.reader.ReadAllScalarsOn()
        self.reader.Update()

        self.data = self.reader.GetOutput()

        dim = self.data.GetDimensions()
        self.vec = list(dim)
        self.vec = [i-1 for i in dim]
        self.vec.append(3)

        print("dimensions (nr, nt, nz) :", self.vec)

        self.nr = dim[0]
        self.nt = dim[1]
        self.nz = dim[2]

        self.r = nm.zeros(self.data.GetNumberOfPoints())
        self.t = nm.zeros(self.data.GetNumberOfPoints())
        self.z = nm.zeros(self.data.GetNumberOfPoints())


        for i in range(0,self.data.GetNumberOfPoints()):
            self.r[i],self.t[i],self.z[i]= self.data.GetPoint(i)
        
        ord = 'F'
        # ord = 'C'

        if ord == 'F':
            self.r = self.r.reshape(dim,order='F')
            self.t = self.t.reshape(dim,order='F')
            self.z = self.z.reshape(dim,order='F')

        else:
            self.r = self.r.reshape(dim,order='C')
            self.t = self.t.reshape(dim,order='C')
            self.z = self.z.reshape(dim,order='C')
       
        self.xmin = self.r[0,0,0]
        self.xmx = self.r[self.nr-1,0,0]
        self.zmin = self.z[0,0,0]
        self.zmx = self.z[0,0,self.nz-1]
        
        # self.t = 0.5*(self.t[:,:-1,:]+self.t[:,1:,:])
        # self.z = 0.5*(self.z[:,:,:-1]+self.z[:,:,1:])


        print("coordinates loaded")                
        print("shape = self.r: \n", nm.shape(self.r))


        self.d = VN.vtk_to_numpy(self.data.GetCellData().GetArray('density'))

        self.P = VN.vtk_to_numpy(self.data.GetCellData().GetArray('pressure')) 
        u = VN.vtk_to_numpy(self.data.GetCellData().GetArray('velocity'))
        
        self.u1 = u[:,0]
        self.u2 = u[:,1]
        self.u3 = u[:,2]
        

        # print(type(self.u1), "u1=", self.u1  )

        # Trad = (dat.erad[i, j]*TEFF**4)**0.25        
        # ro = max(Dsc*dat.dd[i, j], small)
        # Tgas = 2./3.* dat.ee[i,j]*dat.Esc /RGAS/(Dsc*dat.dd[i, j])

        if ord == 'F':
            self.d = self.d.reshape((self.vec[0], self.vec[1], self.vec[2]),order='F')
            self.P = self.P.reshape((self.vec[0], self.vec[1], self.vec[2]),order='F')
            self.u1 = self.u1.reshape((self.vec[0], self.vec[1], self.vec[2]),order='F')
            self.u2 = self.u2.reshape((self.vec[0], self.vec[1], self.vec[2]),order='F')
            self.u3 = self.u3.reshape((self.vec[0], self.vec[1], self.vec[2]),order='F')
        else:
            self.d = self.d.reshape((self.vec[0], self.vec[1], self.vec[2]),order='C')
            self.P = self.P.reshape((self.vec[0], self.vec[1], self.vec[2]),order='C')
            self.u1 = self.u1.reshape((self.vec[0], self.vec[1], self.vec[2]),order='C')
            self.u2 = self.u2.reshape((self.vec[0], self.vec[1], self.vec[2]),order='C')
            self.u3 = self.u3.reshape((self.vec[0], self.vec[1], self.vec[2]),order='C')
        

        print("shape U= ", nm.shape(self.u1))
        print("class loaded...")


    def loadSimulationParam(self, fileNameFullPath, print_res):
        import os

        locdir=os.getcwd()
   
        try:

            for dataLine in open( fileNameFullPath, 'r').read().splitlines():
                
                print(dataLine)
                
                if 'Nx1' in dataLine:
                    self.nr = int(re.findall('Nx1\s*=\s*(\d*)', dataLine)[0])            
                    self.i_s=0
                    self.ie=self.nr-1

        
                if 'Nx2' in dataLine:
                    self.nt = int(re.findall('Nx2\s*=\s*(\d*)', dataLine)[0])
                    # print nx2
        
                if 'Nx3' in dataLine:
                    self.nz = int(re.findall('Nx3\s*=\s*(\d*)', dataLine)[0])            
                    self.js=0
                    self.je=self.nz-1

                
                if 'nc0' in dataLine:            
                                    
                    self.n0 = float(re.findall('nc0\s*=\s*(\d*\.\d*e\d*)', dataLine)[0])                                
                    self.Dsc = MP* self.n0            
                    print ("self.Dsc=", self.Dsc)
                    
                if 'F2Fedd' in dataLine:         
                    F2Fedd = re.findall('F2Fedd\s*=\s*(\d*\.\d*)', dataLine)[0]                
                    F2Fedd_str=re.sub(r'\.', "", F2Fedd)
                    self.F2Fedd = float(F2Fedd)

                if 'dt' in dataLine:         
                    dt_bin = re.findall('dt\s*=\s*(\d*\.\d*)', dataLine)[0]                
                    dt_bin_str=re.sub(r'\.', "", dt_bin)
                    self.dt_bin = float(dt_bin)               
    #                print(" inforcing dt =0.1  this needs to be corrected \n" )
                    self.dt_bin = 0.1

            
                if 'r0' in dataLine:                                 
                        self.Rsc =  float( re.findall('r0\s*=\s*(\d*.*\d)', dataLine)[0] )                                                                      
                        # print ("Rc=", self.Rsc)
                                                                      
             

                if 'M2Msun' in dataLine:                                 
                        self.Mbh =  float(  re.findall('M2Msun\s*=\s*(\d*.*\d)', dataLine)[0] )
                        print ("M/Msun=", self.Mbh)        
                        
                        self.MBH_g = self.Mbh *MSUN  

                        print ("MBH_g=", self.MBH_g)  
                         
                if 'beta' in dataLine:         
                    beta = re.findall('beta\s*=\s*(\d*.\d*)', dataLine)[0]
                    beta_str=re.sub(r'\.', "", beta)
                    self.beta = float(beta)
    #                 print("beta=", beta)
                               
        except Exception as e:
            print(str(e))
         
        rg = 2.*G*self.MBH_g/CL**2            
        self.Rsc *= rg
                      
        self.Usc = nm.sqrt(G*self.MBH_g/self.Rsc)  
        self.Esc = self.Dsc*self.Usc**2
        self.tsc=self.Rsc/self.Usc
        #print(self.tsc/YR)
        self.par= {'Dsc': self.Dsc, 'tsc':self.tsc,  'Usc':self.Usc, 'Mbh':self.Mbh,  'Usc' :self.Usc,
                        'nc0':self.n0,' Rsc': self.Rsc
                        }
        if print_res:
            print('Mbh =', self.Mbh);
            print('Rsc =', self.Rsc);
            print('MBH_g =', self.MBH_g);

            print( 'nc0 = %10.3e' % (self.n0))            
            print("r0 = %10.3e cm "% (self.Rsc))      
            print('F2Fedd = %1.1f ' % self.F2Fedd)
            print( "beta = %10.2f" % (self.beta)  )    
            print( "dt_bin = %10.2f" % (self.dt_bin)  )    
            print( 'Usc = %10.3e' % (self.Usc))
            print( 'Esc = %10.3e' % (self.Esc))
            print( 'tsc = %10.3e' % (self.tsc))
    
    # def initParamFilePath(self)


# from matplotlib import pyplot as plt
# vtkFile="Torus10.0000.vtk"
# vtkFile="Torus10.jnt.0099.vtk" 
# dat = athDataVTK()
# dat.loadSimDataVTK(vtkFile)
# im=plt.imshow(  nm.transpose(dat.u3[:,0,:]), origin="lower" )
