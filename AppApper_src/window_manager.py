import tkinter as tk
from shortcut import *
from metadata import *
from pathlib import Path
import saveload as data_manager


#sets up root and grid system
root = tk.Tk()
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=0)


#These are the default widgets of the app
#|
#\/

#toolbar - currently a placeholder for a toolbar
toolbar = tk.Label(root,width=10, height=2, text="Toolbar", bg="green").grid(column=0,row=0,sticky=tk.NW)

#shortcut box
#shortcut_container = tk.Frame(width=100,height=100,bg="red")
shortcut_bg = tk.Label(root, width=20,height=20,bg="red").grid(column=0,row=1,sticky=tk.NW)



#creates currently loaded shortcuts - I don't yet have a system for loading shortcuts finished
def create_loaded_shortcuts():
    row = 1
    for selected in data_manager.loaded_shortcuts:
        sc = tk.Label(shortcut_bg, width=selected.width, height=selected.heigth,bg="blue",text=selected.name).grid(column=0,row=row,sticky=tk.NW)
        row += 1
        


#placeholder function for loading short
def load_shortcuts():
    pass


#creates window and assigns the base window to root
def innitialize_window():
    global root,toolbar
    root.title(app_display_name + " - " + app_version)
    #App Icon
    root.iconbitmap(r'AppApper_src\AppApper.ico')
    root.geometry(default_window_scale)

    #pack default elements
    #toolbar_container.pack(expand=True,fill=tk.X)
    
    create_loaded_shortcuts()
    

    #load data
    data_manager.load_metadata()
    

    root.mainloop()
    
    

