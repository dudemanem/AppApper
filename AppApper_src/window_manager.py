import tkinter as tk
from shortcut import *
from metadata import *
import saveload as data_manager
import tkinter.messagebox
import os as os
import subprocess
import tkinter.simpledialog 
from tkinter import filedialog as fd
import stat
from PIL import Image, ImageOps,ImageTk
from tkinter import PhotoImage
import shutil




#--------------------------------------------------------------------------------------------------------- Variables

root = tk.Tk()
root.title(app_display_name + " - " + app_version)
#App Icon
#root.iconbitmap(r'AppApper.ico') # - this code is currently commented out because it would cause errors where the program couldn't find the path
root.geometry(default_window_scale)
root.resizable(1,1)

current_path = tkinter.StringVar() # - the path for each shortcut. Assigned in open_app() based on what is passed in create_loaded_shortcuts()
current_type = tkinter.StringVar() # - the type for each shortcut. Assigned in open_app() based on what is passed in create_loaded_shortcuts()
current_fpath = tkinter.StringVar() # - the file path for each shortcut. Assigned in open_app() based on what is passed in create_loaded_shortcuts()


#<<<<<<<<<<<<<<<
#Default Widgets
#<<<<<<<<<<<<<<<

#toolbar widgets
toolbar_container = tk.Frame(root,bg="grey")
toolbar_container.grid(row=0, column=0, sticky="nsew",columnspan=10,pady=0)
for i in range(30):
    toolbar_container.grid_columnconfigure(i, weight=1)
create_button = tk.Button(toolbar_container, text="Create Shortcut",command=lambda:create_new_shortcut())
load_profile = tk.Button(toolbar_container, text="Load Profile",command=lambda:load_profile_process())
profile_name = tk.Text(toolbar_container, height=1,width=15,)
save_profile = tk.Button(toolbar_container, text="Save Profile", command= lambda : data_manager.save_profile(profile_name.get("1.0",'1.end')))

#shortcut widgets
shortcut_container = tk.Frame(root,bg="silver")
shortcut_limit_text = tk.Label(root,width=10,height=10,text="Profiles created: 0/15")
    


#--------------------------------------------------------------------------------------------------------- Functions

########################################################
#Checks if given path is an executable file for windows#
########################################################
def is_executable_file(path):
    if os.path.isfile(path):
        # Check if the file has execute permissions
        st = os.stat(path)
        return bool(st.st_mode & stat.S_IEXEC)
    return False

#############################################################################################################################################
#This funciton runs through all the current shortcuts and makes all of their ids run in linear order.########################################
#This is important because if a shortcut is deleted with the id of say, 4, then the shortcut that had the id of 5 should now be 4, and so on#
#############################################################################################################################################
def reset_shortcut_ids():
    for i in range(len(data_manager.loaded_shortcuts)):
        data_manager.loaded_shortcuts[i].id = (i + 1)

#############################################################
#This function returns the path to an image selected by user#
#############################################################
def get_image():
    imagetypes = (
        ('png files', '*.png'),
    )
    ipath = fd.askopenfilename(
        title="Select An Image",
        filetypes=imagetypes
    )
    return ipath

######################################################################################################################################
#this function takes the image at the given path and copies/resizes it at a new location, then returns the path to this new location.#
######################################################################################################################################
def image_to_icon(ipath,name):
    icon = Image.open(ipath,"r")
    new_size = (200,150)
    icon = ImageOps.fit(icon,new_size,Image.Resampling.LANCZOS)
    ipath = data_dir + "\\" + name + ".png"
    icon.save(ipath, "PNG")
    return ipath

####################################################################################################################################
#This function sets the ipath of the shortcut in the given index to a resized version of the image at the path given by get_image()#
####################################################################################################################################
def set_shortcut_image(shortcut_index):
    ipath = get_image()
    icon = image_to_icon(ipath)
    

######################################################################################
#creates currently loaded shortcuts and displays them on the shortcut_container frame#
######################################################################################
def create_loaded_shortcuts():

    for child in shortcut_container.winfo_children():
        child.destroy()

    #column and row variables, determine column and row to place new shortcuts
    c = 1
    r = 1
    #this index variable will be passed to the delete_shortcut() function to let it know which shortcut needs to be deleted
    index = 0
    for selected in data_manager.loaded_shortcuts:
        if r > 3:
            tkinter.messagebox.showerror("No Good Amount Of Space :<","The program ran out of space, some shortcuts are not shown!")
            break
        sc = tk.Frame(shortcut_container, bg="red",width=100,height=100)
        sc_button = tk.Button(sc,text = "Launch: " + selected.name,command=lambda p = selected.app_path, t = selected.type, fp = selected.file_path: open_app(p,t,fp))
        sc_color = ""
        sc_image = ""
        icon = ""
        if selected.icon_path == "null":
            sc_color = tk.Frame(sc, bg="red", width=200, height=150)
        else:
            print(selected.icon_path)
            icon = ImageTk.PhotoImage(Image.open(selected.icon_path))
            sc_image = tk.Label(sc,image=icon,width=200,height=150)
        delete_button = tk.Button(sc,text = "X", command=lambda i = index: delete_shortcut(i))
        sc.grid(row=r,column=c,sticky="nsew", pady=10,padx=10)
        sc_button.pack(expand=True,fill="both")
        if selected.icon_path == "null":
            sc_color.pack(expand=True,fill="both")
        else:
            sc_image.pack(expand=True,fill="both")
        delete_button.pack(expand=True,fill="both")
        c += 1
        index += 1
        if c == 6:
            r += 1
            c = 1
    shortcut_limit_text.config(text="Shortcuts created: " + str(len(data_manager.loaded_shortcuts)) + "/15")

############################################################################
#This opens the app or the file and an associated app that are passed to it#
############################################################################
def open_app(path,type,fpath):
    current_path.set(path)
    current_type.set(type)
    current_fpath.set(fpath)

    if not os.path.exists(current_path.get()):
        tkinter.messagebox.showerror("Directory Error","Please make sure the path is valid!")
        return

    if current_type.get() == "app":
        if is_executable_file(current_path.get()):
            try:
                result = subprocess.Popen([current_path.get()])
                print("Command succeeded:", result)
            except subprocess.TimeoutExpired:
                print("The command timed out.")
            except subprocess.CalledProcessError as e:
                print("The command failed with return code:", e.returncode)
        else:
            tkinter.messagebox.showerror("Not an EXE", "That file is not an executable.")
            return
    elif current_type.get() == "file":
        if is_executable_file(current_fpath.get()):
            try:
                result = subprocess.Popen([current_fpath.get(), current_path.get()])
                print("Command succeeded:", result)
            except subprocess.TimeoutExpired:
                print("The command timed out.")
            except subprocess.CalledProcessError as e:
                print("The command failed with return code:", e.returncode)
        else:
            tkinter.messagebox.showerror("Not an EXE", "That file is not an executable.")
            return

##################################################################################################
#index is obtained from lambda funcion in delete button###########################################
#this function removes the shortcut from the loaded list and calls the reset for the shortcut ids#
##################################################################################################
def delete_shortcut(index):
    data_manager.loaded_shortcuts.pop(index)
    reset_shortcut_ids()
    create_loaded_shortcuts()

######################################################################################################
#opens dialogue for file picker and name of shortcut. If they choose an exe, it will create shortcut.#
#If they choose file it will ask for another file that is an exe to open the file with################
######################################################################################################
def create_new_shortcut():
    #ask for name and exit if none is given
    name = tkinter.simpledialog.askstring("Enter Name", "Enter a name for this shortcut.")
    if name == "":
        return
    
    #set file types that are supported when picking path
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt')
    )
    
    #Get base path to file or app
    path = ""    
    path = fd.askopenfilename(
        title="Select An App Or File To Launch",
        filetypes=filetypes
    )
    if path == "":
        tkinter.messagebox.showerror("Directory Error", "No file or app was given.")
        return

    sc_type = ""

    #ask for an app if the path leads to a file instead of exe
    apath = ""
    if is_executable_file(path):
        sc_type = "app"
    else:
        sc_type = "file"
        apath = fd.askopenfilename(
        title="Select An App To Launch This File",
        filetypes=filetypes
        )
        if apath == "":
            tkinter.messagebox.showerror("Directory Error", "No app was given.")
            return
        
    ipath = get_image()
    if ipath == "":
        tkinter.messagebox.showerror("Directory Error", "No image was given.")
        return
    ipath = image_to_icon(ipath,name)
    

    #set id of shortcut based on previous ones
    id = 0
    if len(data_manager.loaded_shortcuts) > 0:
        id = data_manager.loaded_shortcuts[len(data_manager.loaded_shortcuts)-1].id+1
    else:
        id = 1

    sc = shortcut(id,name,sc_type,path,apath,ipath,80,50)
    data_manager.loaded_shortcuts.append(sc)

    create_loaded_shortcuts()
    print(data_manager.loaded_shortcuts)

########################################################
#configures the organization of the root window's grid.#
########################################################
def configure_grid():
    for i in range(10):
        root.grid_columnconfigure(i, weight=1)  
    for i in range(100):
        root.grid_rowconfigure(i, weight=1)
        
#################################################################
#loads profile and then tells program to reload shortcut widgets#
#################################################################
def load_profile_process():
    data_manager.load_profile()
    create_loaded_shortcuts()

#######################################################################################
#creates window and assigns the base window to root. ALso adds default widgets to grid#
#######################################################################################
def innitialize_window():
    global root,create_button

    configure_grid()
    #add default elements
    create_button.grid(row=0,column=0,sticky="ew",pady=2,padx=2)
    profile_name.grid(row=0,column=1,sticky="ew",padx=2,pady=2)
    save_profile.grid(row=0,column=2,sticky="ew",pady=2,padx=2)
    load_profile.grid(row=0,column=3,sticky="ew",pady=2,padx=2)
    shortcut_container.grid(row=1, column=0, sticky="nsew",columnspan=10,pady=0,rowspan=100,)
    shortcut_limit_text.grid(row=1,column=9,sticky="nsew",columnspan=1)
    create_loaded_shortcuts()

    #load default save data
    data_manager.load_save_data()
    

    root.mainloop()