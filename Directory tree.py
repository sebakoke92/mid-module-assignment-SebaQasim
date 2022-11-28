import os 
files = []
def Test1(rootDir):
    files.append(rootDir)
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for d in dirs: 
            files.append(os.path.join(root, d))      
        for f in files: 
            files.append(os.path.join(root, f))