import tkinter.messagebox
from shortcut import *
from metadata import *
import os
import tkinter 
from shortcut import *
from tkinter import filedialog as fd


loaded_shortcuts = []
loaded_profile_path = ""
loaded_profile_name = ""

#--------------------------------------------------------------------------------------------------------- path creation
####################################################
#creates save directory in the local AppData folder#
####################################################
def create_data_path_directory():
    os.mkdir(data_dir)
    tkinter.messagebox.showinfo("Directory Created!", "The save data directory has been created at " + data_dir)

###################################################################################################################################
#creates global save file for user settings, last loaded profile, etc. stuff that always should be loaded, currently a placeholder#
###################################################################################################################################
def create_data_save_file():
    with open(save_file_path, "w") as f:
        f.write("Test")
    tkinter.messagebox.showinfo("Save File Created!", "The save file at " + save_file_path + " has been created")

#--------------------------------------------------------------------------------------------------------- loading

###############################
#reads selected profile's data#
###############################
def read_profile_data(dir):
    global loaded_shortcuts

    #if path is empty return error to user
    if dir == "":
        tkinter.messagebox.showerror("No Path Given", "There was no path given to a profile!")
        return

    #if somehow a directory that is not a file is given, return error to user
    if not os.path.isfile(dir):
        tkinter.messagebox.showerror("Not a File", "The given directory is not a file!")
        return

    #reset loaded shortcuts
    loaded_shortcuts = []

    try:
        file = open(dir,"r")
    except:
        tkinter.messagebox.showerror("Error Opening Profile!", "The app was unable to open the profile file!")
        return
    data = file.read()

    name_index = data.index("@") + 1

    commas = [i for i, c in enumerate(data) if c == ","]

    #location of start and end of brackets in file. all shortcuts are contained in brackets, so this can be used to isolate the shortcut text.
    #this will create errors if the shortcut has a bracket in it's path
    shortcut_start = [i for i, c in enumerate(data) if c == "["]
    shortcut_end = [i for i, c in enumerate(data) if c == "]"]

    #loaded name - not currently used for anything
    profile_name = data[name_index:commas[0]]
    
    current_index = 0
    for i in range(len(shortcut_start)):

        sc_text = data[shortcut_start[current_index]+1:shortcut_end[current_index]]
        current_index += 1
        #location of commas in the specific isolated shortcut text
        sc_commas = [i for i, c in enumerate(sc_text) if c == ","]
        #loaded values for the shortcut class
        id = int(sc_text[0:sc_commas[0]])
        type = sc_text[sc_commas[0]+1:sc_commas[1]]
        name = sc_text[sc_commas[1]+1:sc_commas[2]]
        app_path = sc_text[sc_commas[2]+1:sc_commas[3]]
        icon_path = sc_text[sc_commas[4]+1:sc_commas[5]]
        file_path = ""
        if type == "file":
            
            file_path = sc_text[sc_commas[3]+1:sc_commas[4]]
        else:
            file_path = "null"
        print(f"app_path is {app_path}, and file_path is {file_path}")
        #fpath and ipath are null right now, they will be implemented later
        sc = shortcut(id,name,type,app_path,file_path,icon_path,80,50)
        loaded_shortcuts.append(sc)

####################################################################################
#opens file prompt and passes profile file data to the read_profile_data() function#
####################################################################################
def load_profile():

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    file_path = fd.askopenfilename(
        title="Select an AppApper Profile",
        initialdir=profile_dir,
        filetypes=filetypes
    )
    print(file_path)
    read_profile_data(file_path)

#--------------------------------------------------------------------------------------------------------- saving

###############################################################################
#compiles current data in an encoded profile save to be written to a text file#
###############################################################################
def compile_profile_data(name):
    data = "@" + name + ","

    for sc in loaded_shortcuts:
        data = data + "[" + str(sc.id) + "," + sc.type + "," + sc.name + ","
        data = data + sc.app_path + "," + sc.file_path + "," + sc.icon_path + ",]" + ","
    return data

###############################
#saves data of current profile#
###############################
def save_profile(text_field):
    name = text_field
    contents = compile_profile_data(name)
    print(name)
    if not os.path.exists(profile_dir):
        tkinter.messagebox.showerror("Missing Profile Directory", "Profile directory at " + profile_dir + " is missing. it has now been created!")
        os.makedirs(profile_dir)

    if name == "":
        tkinter.messagebox.showerror("No Profile Name Provided", "Enter a name for the profile in the text box before you save it!")
        return
    
    with open(profile_dir + "\\" + name + ".txt", "w") as f:
        f.write(contents)
    tkinter.messagebox.showinfo("Profile Created", 'Profile "' + name + '" has been created!')

#--------------------------------------------------------------------------------------------------------- loading default save files and confirming that needed directories exist

##############################################################################################################################
#loads app settings (such as default profile path) from save file. This is just a placeholder, these settings don't exist yet#
##############################################################################################################################
def load_save_data():

    #display message and create path if doesn't exist
    if not os.path.isdir(data_dir):
        tkinter.messagebox.showerror("Error", "The application data path at " + data_dir + " does not exist. It will now be created.")
        create_data_path_directory()
    #display message and create save file if doesn't exist
    if not os.path.exists(save_file_path):
        tkinter.messagebox.showerror("Directory Error", "There is no save file at " + save_file_path + " It will be created")
        create_data_save_file()


#key for opening files in python
'''
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing. The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
'''