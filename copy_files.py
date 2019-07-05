import shutil
import os
import re


src_path = r'\\eutct.internal.towerswatson.com\DavWWWRoot\nonclients\GECATAnalysisBelgium\Documents\FromFolder'
dest_path = r'\\eutct.internal.towerswatson.com\DavWWWRoot\nonclients\GECATAnalysisBelgium\Documents\ToFolder'
source_files = os.listdir(src_path)
source_folders = os.listdir(r'\\eutct.internal.towerswatson.com\DavWWWRoot\nonclients\GECATAnalysisBelgium\Documents')


for element in source_files:
    if re.match('WE',element):
        #newf = folder.split('.')[0] 
    #newf is name of new folder where you want to move 
    #change Folder name as per yourrequirement
        destination = dest_path
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.copy(src_path+'\\'+element,destination) #change move to copy if you want to copy insted of moving 
        print('done moving')
    else: print('no such file')