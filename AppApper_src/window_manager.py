import tkinter as tk
from shortcut import *
from metadata import *
from pathlib import Path
import saveload as data_manager
import tkinter.messagebox
import os as os
import subprocess
import tkinter.simpledialog 




#--------------------------------------------------------------------------------------------------------- Variables

#sets up root 
root = tk.Tk()
root.title(app_display_name + " - " + app_version)
#App Icon
#root.iconbitmap(r'AppApper.ico')
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
    


create_button = tk.Button(toolbar_container, text="Create Shortcut",command=lambda:create_new_shortcut())
load_profile = tk.Button(toolbar_container, text="Load Profile",command=lambda:load_profile_process())
profile_name = tk.Text(toolbar_container, height=1,width=15,)
save_profile = tk.Button(toolbar_container, text="Save Profile", command= lambda : data_manager.save_profile(profile_name))

#--------------------------------------------------------------------------------------------------------- Functions
#creates currently loaded shortcuts
def create_loaded_shortcuts():

    for child in shortcut_container.winfo_children():
        child.destroy()

    c = 1
    r = 1
    for selected in data_manager.loaded_shortcuts:
        if r > 3:
            tkinter.messagebox.showerror("No Good Amount Of Space :<","The program ran out of space, some shortcuts are not shown!")
            break
        sc = tk.Frame(shortcut_container, bg="red",width=100,height=100)
        sc_button = tk.Button(sc,text = "Launch: " + selected.name,command=lambda : open_app(selected.app_path))
        sc_color = tk.Frame(sc, bg="red", width=200, height=150)
        sc.grid(row=r,column=c,sticky="nsew", pady=10,padx=10)
        sc_button.pack(expand=True,fill="both",)
        sc_color.pack(expand=True,fill="both")
        c += 1
        if c == 6:
            r += 1
            c = 1

def open_app(path):
    if not os.path.exists(path):
        tkinter.messagebox.showerror("System Cannot Find Path!","Please make sure the path is valid!")
        return
    subprocess.run([path])
    
def create_new_shortcut():
    name = tkinter.simpledialog.askstring("Enter Name", "Enter a name for this shortcut.")
    path = tkinter.simpledialog.askstring("Enter Path", "Please enter the path for the application you want to link with the shortcut. Do not type quotes around the path, just type the path.")
    
    id = 0
    if len(data_manager.loaded_shortcuts) > 0:
        id = data_manager.loaded_shortcuts[len(data_manager.loaded_shortcuts)-1].id+1
    else:
        id = 1
    sc = shortcut(id,name,"app",path,"null","null",80,50)
    data_manager.loaded_shortcuts.append(sc)
    create_loaded_shortcuts()
    print(data_manager.loaded_shortcuts)


def configure_grid():
    for i in range(10):
        root.grid_columnconfigure(i, weight=1)  
    for i in range(100):
        root.grid_rowconfigure(i, weight=1)
        


#loads profile and then tells program to reload shortcut widgets
def load_profile_process():
    data_manager.load_profile()
    create_loaded_shortcuts()

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