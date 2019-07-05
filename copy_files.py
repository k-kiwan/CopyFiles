import shutil
import os
import re


src_path = r'//eutct.internal.towerswatson.com/nonclients/EMEADDU/Documents/2019/Data_Collection_Worksheets_by_Company/Belgium'
dest_path = r'//eutct.internal.towerswatson.com/nonclients/GECATAnalysisBelgium/Documents/2019/LTI Valuations/Test'

source_folders_list = os.listdir(src_path)


for folder in source_folders_list:
        source_folder = src_path + '/' + folder
        files_list = os.listdir(source_folder)
        for element in files_list:
            if re.match('^.*QA.*$',element):
            #newf = folder.split('.')[0] 
            #newf is name of new folder where you want to move 
            #change Folder name as per yourrequirement
                destination = dest_path
                if not os.path.exists(destination):
                    os.makedirs(destination)
                shutil.copy(src_path+'/'+folder+'/'+element,destination) #change move to copy if you want to copy insted of moving 
                print('done copying')
            else: print('no such file in ' + folder)

stop = input("Press Enter to close")