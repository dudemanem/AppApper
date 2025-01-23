import tkinter.messagebox
from shortcut import *
from metadata import *
import os
import tkinter 
from shortcut import *


loaded_shortcuts = [shortcut(1,"test1","app",r"C:\Program Files (x86)\Steam\steamapps\common\Clone Drone in the Danger Zone\Clone Drone in the Danger Zone.exe","null","null",80,50)]
loaded_profile_path = ""
loaded_profile_name = ""

#creates save directory
def create_data_path_directory():
    os.mkdir(data_dir)
    tkinter.messagebox.showinfo("Directory Created!", "The save data directory has been created at " + data_dir)

#creates save file
def create_data_save_file():
    with open(profile_dir, "w") as f:
        f.write("Test")
    tkinter.messagebox.showinfo("Save File Created!", "The save file at " + save_file_path + " has been created")

#loads shortcut profile
def load_profile():
    pass

#saves data of current profile
def save_profile(text_field):
    name = text_field.get("1.0",'end-1c')
    if not os.path.exists(profile_dir):
        tkinter.messagebox.showerror("Missing Profile Directory", "Profile directory at " + profile_dir + " is missing. it has now been created!")
        os.mkdir(profile_dir)
    if name == "":
        tkinter.messagebox.showerror("No Profile Name Provided", "Enter a name for the profile in the text box before you save it!")
        return
    with open(data_dir + "\\" + name + ".txt", "w") as f:
        f.write("Profile " + name + " Saved")
    tkinter.messagebox.showinfo("Profile Created", 'Profile "' + name + '" has been created!')

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