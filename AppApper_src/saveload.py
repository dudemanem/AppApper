import tkinter.messagebox
from shortcut import *
from metadata import *
import os
import tkinter 
from shortcut import *


loaded_shortcuts = [shortcut(1,"test1","app","app_path","null","null",40,20)]
loaded_profile_path = ""
loaded_profile_name = ""

#creates save directory
def create_data_path_directory():
    os.mkdir(data_dir)
    tkinter.messagebox.showinfo("Directory Created!", "The save data directory has been created at " + data_dir)

#creates save file
def create_data_save_file():
    with open(save_file_path, "w") as f:
        f.write("Test")
    tkinter.messagebox.showinfo("Save File Created!", "The save file at " + save_file_path + " has been created")

#loads shortcut profile
def load_profile():
    pass

#saves data of current profile
def save_profile():
    pass

#loads app settings (such as default profile path) from app data
def load_metadata():
    #display message and create path if doesn't exist
    if not os.path.isdir(data_dir):
        tkinter.messagebox.showerror("Error", "The application data path at " + data_dir + " does not exist. It will now be created.")
        create_data_path_directory()
    #display message and create save file if doesn't exist
    if not os.path.exists(save_file_path):
        tkinter.messagebox.showerror("Directory Error", "There is no save file at " + save_file_path + " It will be created")
        create_data_save_file()