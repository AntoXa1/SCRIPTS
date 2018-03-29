#!/Users/dora/anaconda3/bin/python


import subprocess, os, fnmatch

def getListDatFilesInDir(fileHeadMatch, dir0):    
    fileList=[]    
    for file in os.listdir(dir0):
        if fnmatch.fnmatch(file, fileHeadMatch+'*.vtk'):                
            res = file.split('.')[1]
            fileList.append(res)           
    return(fileList)
# ========================================================
PATH = "/Users/dora/WORK/ECLIPSE_SPACE/AthenaWind"
binDir = PATH+ "/bin/"
# binDir ="./"

listDir = []

for file in os.listdir(binDir):
    if file.startswith("id"):
        listDir.append(file)

dir0 = binDir+'id0'

fName = 'Torus10'
fName = 'mhdTorus'

fileTimeStampList = getListDatFilesInDir(fName, dir0)


# try:
#     os.stat("./"+binJntDir)
# except:
#     os.mkdir("./"+binJntDir)    


os.chdir(binDir)


for tStamp in fileTimeStampList:
    fileToJoin = []
    jntFileName = fName+'.jnt.'+tStamp + '.vtk'

    for iddir in listDir:
        if iddir=='id0':                        
            nName = fName+'.'+tStamp + '.vtk'
        else:                     
            nName = fName+'-'+iddir + '.'+ tStamp + '.vtk'        
        fileToJoin.append(binDir+iddir + '/'+ nName)        
    
    print(fileToJoin)

    togetherFile = PATH + '/bin/' + jntFileName

    args = [binDir+'./join_vtk.exe', '-o', jntFileName]

    [  args.append(x) for x in fileToJoin ]
    
    cwd = os.getcwd()   
    
    subprocess.call(args)

    print(args)
    

print("done")    
