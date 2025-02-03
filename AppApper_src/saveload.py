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

#creates save directory
def create_data_path_directory():
    os.mkdir(data_dir)
    tkinter.messagebox.showinfo("Directory Created!", "The save data directory has been created at " + data_dir)

#creates global save file
def create_data_save_file():
    with open(save_file_path, "w") as f:
        f.write("Test")
    tkinter.messagebox.showinfo("Save File Created!", "The save file at " + save_file_path + " has been created")

#--------------------------------------------------------------------------------------------------------- loading

#reads selected profile from dir
def read_profile_data(dir):
    global loaded_shortcuts

    if dir == "":
        tkinter.messagebox.showerror("No Path Given", "There was no path given to a profile!")
        return

    if not os.path.isfile(dir):
        tkinter.messagebox.showerror("Not a File", "The given directory is not a file!")
        return

    loaded_shortcuts = []

    file = open(dir,"r")
    data = file.read()

    name_index = data.index("@") + 1

    commas = [i for i, c in enumerate(data) if c == ","]

    #location of start and end of brackets in file. all shortcuts are contained in brackets
    shortcut_start = [i for i, c in enumerate(data) if c == "["]
    shortcut_end = [i for i, c in enumerate(data) if c == "]"]

    #loaded data variables
    profile_name = data[name_index:commas[0]]
    
    current_index = 0
    for i in range(len(shortcut_start)):

        sc_text = data[shortcut_start[current_index]+1:shortcut_end[current_index]]
        current_index += 1
        #location of commas in the bracket
        sc_commas = [i for i, c in enumerate(sc_text) if c == ","]
        id = sc_text[0:sc_commas[0]]
        type = sc_text[sc_commas[0]+1:sc_commas[1]]
        name = sc_text[sc_commas[1]+1:sc_commas[2]]
        app_path = sc_text[sc_commas[2]+1:sc_commas[3]]
        print(app_path)

        sc = shortcut(id,name,type,app_path,"null","null",80,50)
        loaded_shortcuts.append(sc)


#loads shortcut profile
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

#compiles current data in an encoded profile save to be written to a text file
def compile_profile_data(name):
    data = "@" + name + ","

    for sc in loaded_shortcuts:
        data = data + "[" + str(sc.id) + "," + sc.type + "," + sc.name + ","
        if sc.type == "app":
            data = data + sc.app_path + ",]" + ","
    return data

#saves data of current profile
def save_profile(text_field):
    name = text_field.get("1.0",'end-1c')
    contents = compile_profile_data(name)

    if not os.path.exists(profile_dir):
        tkinter.messagebox.showerror("Missing Profile Directory", "Profile directory at " + profile_dir + " is missing. it has now been created!")
        os.makedirs(profile_dir)

    if name == "":
        tkinter.messagebox.showerror("No Profile Name Provided", "Enter a name for the profile in the text box before you save it!")
        return
    
    with open(profile_dir + "\\" + name + ".txt", "w") as f:
        f.write(contents)
    tkinter.messagebox.showinfo("Profile Created", 'Profile "' + name + '" has been created!')

#--------------------------------------------------------------------------------------------------------- startup of app loading

#loads app settings (such as default profile path) from app data. This is just a placeholder, these settings don't exist yet
def load_metadata():

    #display message and create path if doesn't exist
    if not os.path.isdir(data_dir):
        tkinter.messagebox.showerror("Error", "The application data path at " + data_dir + " does not exist. It will now be created.")
        create_data_path_directory()
    #display message and create save file if doesn't exist
    if not os.path.exists(save_file_path):
        tkinter.messagebox.showerror("Directory Error", "There is no save file at " + save_file_path + " It will be created")
        create_data_save_file()



'''
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing. The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
'''