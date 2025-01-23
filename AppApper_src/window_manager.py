import tkinter as tk
from shortcut import *
from metadata import *
from pathlib import Path
import saveload as data_manager
import tkinter.messagebox
import os as os
import subprocess



#--------------------------------------------------------------------------------------------------------- Variables

#sets up root 
root = tk.Tk()
root.title(app_display_name + " - " + app_version)
#App Icon
root.iconbitmap(r'AppApper_src\AppApper.ico')
root.geometry(default_window_scale)
root.resizable(0,0)


#These are the default widgets of the app
#|
#\/


#toolbar - currently a placeholder for a toolbar
toolbar_container = tk.Frame(root,bg="grey")
toolbar_container.grid(row=0, column=0, sticky="nsew",columnspan=10,pady=0)
for i in range(30):
    toolbar_container.grid_columnconfigure(i, weight=1)

shortcut_container = tk.Frame(root,bg="silver")
shortcut_container.grid(row=1, column=0, sticky="nsew",columnspan=10,pady=0,rowspan=100,)
    


create_button = tk.Button(toolbar_container, text="Create Shortcut")
load_profile = tk.Button(toolbar_container, text="Load Profile")
profile_name = tk.Text(toolbar_container, height=1,width=15,)
save_profile = tk.Button(toolbar_container, text="Save Profile", command= lambda : data_manager.save_profile(profile_name))

#--------------------------------------------------------------------------------------------------------- Functions

def open_app(path):
    subprocess.Popen(path)


def configure_grid():
    for i in range(10):
        root.grid_columnconfigure(i, weight=1)  
    for i in range(100):
        root.grid_rowconfigure(i, weight=1)
        
#creates currently loaded shortcuts - I don't yet have a system for loading shortcuts finished
def create_loaded_shortcuts():
    c = 1
    r = 1
    for selected in data_manager.loaded_shortcuts:
        if r > 3:
            tkinter.messagebox.showerror("No Good Amount Of Space :<","The program ran out of space, some shortcuts are not shown!")
            break
        sc = tk.Frame(shortcut_container, bg="red",width=100,height=100)
        sc_button = tk.Button(sc,text = "Launch",command=lambda : open_app(selected.app_path))
        sc_color = tk.Frame(sc, bg="red", width=200, height=150)
        sc.grid(row=r,column=c,sticky="nsew", pady=10,padx=10)
        sc_button.pack(expand=True,fill="both",)
        sc_color.pack(expand=True,fill="both")
        c += 1
        if c == 6:
            r += 1
            c = 1
        


#creates window and assigns the base window to root
def innitialize_window():
    global root,create_button

    configure_grid()
    #add default elements
    create_button.grid(row=0,column=0,sticky="ew",pady=2,padx=2)
    profile_name.grid(row=0,column=1,sticky="ew",padx=2,pady=2)
    save_profile.grid(row=0,column=2,sticky="ew",pady=2,padx=2)
    load_profile.grid(row=0,column=3,sticky="ew",pady=2,padx=2)
    create_loaded_shortcuts()

    #load data
    data_manager.load_metadata()
    

    root.mainloop()