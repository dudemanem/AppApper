import tkinter as tk
from shortcut import *
from metadata import *
from pathlib import Path
import saveload as data_manager


#sets up root 
root = tk.Tk()
root.title(app_display_name + " - " + app_version)
#App Icon
root.iconbitmap(r'AppApper_src\AppApper.ico')
root.geometry(default_window_scale)


#These are the default widgets of the app
#|
#\/


#toolbar - currently a placeholder for a toolbar
toolbar_container = tk.Frame(root,bg="green")
toolbar_container.grid(row=0, column=0, sticky="ew",columnspan=30)
for i in range(30):
    toolbar_container.grid_columnconfigure(i, weight=1)


create_button = tk.Button(toolbar_container, text="Click Me")
extra_button = tk.Button(toolbar_container, text="Testing Button :3")

def configure_grid():
    for i in range(30):
        root.grid_columnconfigure(i, weight=1)  
    for i in range(60):
        root.grid_rowconfigure(i, weight=1)
        
#creates currently loaded shortcuts - I don't yet have a system for loading shortcuts finished
def create_loaded_shortcuts():
    row = 1
    for selected in data_manager.loaded_shortcuts:
        pass
        


#creates window and assigns the base window to root
def innitialize_window():
    global root,create_button

    configure_grid()
    #add default elements
    create_button.grid(row=0,column=0,sticky="ew",pady=1)
    extra_button.grid(row=0,column=1,sticky="ew",pady=1)
    

    #load data
    data_manager.load_metadata()
    

    root.mainloop()