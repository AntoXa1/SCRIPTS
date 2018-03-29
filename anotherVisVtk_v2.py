


#%%

import os

HOME_DIR = "/Users/dora/WORK/SCRIPTS/"
os.chdir(HOME_DIR)

# BinDir =  HOME_DIR+"JOINT/"

BinDir =  "/Volumes/USB_Drive/JOINT_VTK/"

import importlib

import AthenaModelVTK

AthenaModelVTK=importlib.reload(AthenaModelVTK)
from AthenaModelVTK import *
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as manimation
from matplotlib.axes import subplot_class_factory
from mpl_toolkits.axes_grid1 import make_axes_locatable
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
import os, fnmatch

    
def getListDataFilesInDir(fileHeadMatch, dir0, MaxNumFiles):        
    FileList=[]
    for file in os.listdir(dir0):
        if fnmatch.fnmatch(file, fileHeadMatch+'*.vtk'):                
            FileList.append(file)     
    if MaxNumFiles:
        del FileList[MaxNumFiles:]        
    return(FileList)

def getDataFromFileByName(vtkFile):    
    global extent_glob
    # print(vtkFile)    
    if os.path.exists(vtkFile):
        try:           
            cdat = athDataVTK()    
            cdat.loadSimDataVTK(vtkFile)            
            dat=np.transpose(cdat.d[:,0,:]) 
            xmin,xmx,zmin,zmx = cdat.r[0],cdat.r[cdat.nr-1],cdat.z[0],cdat.z[cdat.nz-1]            
            extent_glob=[cdat.xmin,cdat.xmx,cdat.zmin,cdat.zmx]                  
            return(dat)
        except IOError:
            print ("Could not read file:", vtkFile)
    else:
        print(print ("file does not exist in the path:", vtkFile))    

def set_fonts_etc():
    fontsize_bar=14
    fontsize_x = 16
   
    ax.set_ylabel('z(pc)', fontsize = 22)
    for ylabel in ax.get_yticklabels():
        ylabel.set_fontsize(fontsize_x)
    
    ax.set_xlabel('R(pc)', fontsize = 22)
    for xlabel in ax.get_xticklabels():
        xlabel.set_fontsize(fontsize_x)
    
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes("right", size="5%", pad=0.05)                        
    # cb =plt.colorbar(im, cax=cax)        
    # for t in cb.ax.get_yticklabels():
    #     t.set_fontsize(fontsize_bar)

def getFrameByLOCALFileName(vtkFile):     
    global extent_glob   
    file = BinDir + vtkFile
    dat = getDataFromFileByName(file)                
    ax.clear()        
    dat = nm.log10(dat)    
    print("extent_glob = \n",extent_glob)  
    
    im=plt.imshow(dat, origin="lower", extent=extent_glob)  
    # useful code snippet, do not remove
    # plt.tick_params(    
    #     which='both',      # both major and minor ticks are affected    
    #     bottom='off',      # ticks along the bottom edge are off
    #     # top='off',         # ticks along the top edge are off
    #     left='off',
    #     # right='off',
    #     labelbottom='off', # labels along the bottom edge are off
    #     labelleft = 'off')

    set_fonts_etc()
    return mplfig_to_npimage(fig)
        

        
def MakeFrame1(t):
    global IdCurFrame_glob, FileList_glob, CurFrameRef_glob, dt_glob

    iframe = int(t//dt_glob)
    
    if iframe > IdCurFrame_glob:
        
        file = FileList_glob[iframe]

        CurFrameRef_glob = getFrameByLOCALFileName(file)

        IdCurFrame_glob = iframe
    
    return(CurFrameRef_glob)
    


fig,ax = plt.subplots(figsize=(15,15))


# initialize first accurence
# CurFrameRef_glob = mplfig_to_npimage(fig)


# to get all files let NumFrames = big number > number of files in dir
NumFrames = 1000000

FileList_glob=getListDataFilesInDir("Torus10.jnt", BinDir, MaxNumFiles=NumFrames)

fps=20
NumFrames = len(FileList_glob)
duration = NumFrames/fps
print('NumFrames=' , NumFrames, 'duration = ', duration, '\n')


dt_glob = duration/NumFrames
IdCurFrame_glob = -1 #not yet a frame exists

animation = VideoClip(MakeFrame1, duration=duration)
animation.write_videofile("test1.mp4", fps=fps)
