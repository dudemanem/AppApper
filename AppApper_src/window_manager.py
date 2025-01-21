import tkinter as tk
from shortcut import *
from metadata import *
from pathlib import Path
import saveload as data_manager


#sets up root 
root = tk.Tk()



#These are the default widgets of the app
#|
#\/


#toolbar - currently a placeholder for a toolbar
toolbar_container = tk.Frame(root, width=400,height=20,bg="green")
create_button = tk.Button(toolbar_container, width=10, height=2, text="Click Me!",pady=0)

#shortcut box
shortcut_container = tk.Frame(root, width=300,height=300,bg="red")


#creates currently loaded shortcuts - I don't yet have a system for loading shortcuts finished
def create_loaded_shortcuts():
    row = 1
    for selected in data_manager.loaded_shortcuts:
        sc = tk.Label(shortcut_container, width=selected.width, height=selected.heigth,bg="orange",text=selected.name).pack(side="left",fill="none",pady=10,padx=10)
        row += 1
        


#placeholder function for loading short
def load_shortcuts():
    pass


#creates window and assigns the base window to root
def innitialize_window():
    global root,create_button
    root.title(app_display_name + " - " + app_version)
    #App Icon
    root.iconbitmap(r'AppApper_src\AppApper.ico')
    root.geometry(default_window_scale)

    #pack default elements
    toolbar_container.pack(side="top",fill="x",padx=0,pady=0)
    shortcut_container.pack(side="top",fill="both",pady=10)
    create_button.pack(side="left",fill="none",pady=10)
    create_loaded_shortcuts()
    

    #load data
    data_manager.load_metadata()
    

    root.mainloop()
    
    

