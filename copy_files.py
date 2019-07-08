import shutil
import os
import re
from tkinter import *


def copy_files(country_input):
    src_path_1 = '//eutct.internal.towerswatson.com/nonclients/EMEADDU/Documents/2019/Data_Collection_Worksheets_by_Company/'
    dest_path_1 = '//eutct.internal.towerswatson.com/nonclients/GECATAnalysis'
    dest_path_2= '/Documents/2019/LTI_Valuations/Test'

    country = country_input.capitalize()

    src_path = src_path_1 + country
    dest_path = dest_path_1 + country + dest_path_2

    source_folders_list = os.listdir(src_path)

    if '1_TURNAROUNDS' in source_folders_list:  
        source_folders_list.remove('1_TURNAROUNDS')
    try:
        for folder in source_folders_list:
                source_folder = src_path + '/' + folder
                files_list = os.listdir(source_folder)
                try:
                    for element in files_list:
                        if re.match('^.*Valuation.*QA.*',element) or re.match('^.*valuation.*QA.*',element):
                            destination = dest_path
                            if not os.path.exists(destination):
                                os.makedirs(destination)
                            shutil.copy(src_path+'/'+folder+'/'+element,destination) #change move to copy if you want to copy insted of moving 
                            print(folder + ' - copied: ' + element)
                        else: print(folder + ' - not copied: ' + element)
                except:
                    print(folder +' - already exists: ' + element)
                    pass
    except:
        print('Oh no ' + folder + ' is not a folder')
        pass


#main()

window = Tk()
window.title("Welcome to copy me")
window.geometry('350x200')

lbl = Label(window, text="Please choose the country:")
lbl.grid(column=0, row=0)

lbl_space = Label(window, text=" ")
lbl_space.grid(column=0, row=1)

COUNTRIES = ['Belgium', 'Denmark', 'France', 'Germany', 'Ireland', 'Italy', 'Netherlands', 'Norway', 'Spain', 'Sweden', 'Switzerland', 'UK']
variable = StringVar(window)
variable.set(COUNTRIES[0])
dropdown = OptionMenu(window, variable, *COUNTRIES)
dropdown.grid(column=1, row=0)


btn = Button(window, text="Copy",command= lambda: copy_files(variable.get()))
btn.grid(column=1, row=5)

def close():
    window.destroy()

close_btn = Button(window, text="Close",command=close)
close_btn.grid(column=2, row=5)



window.mainloop()

