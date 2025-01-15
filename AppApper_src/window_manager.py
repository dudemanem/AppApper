import tkinter as tk
from shortcut import *
from metadata import *

#sets up root and grid system
root = tk.Tk()
root.columnconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

#These are the default widgets of the app
#|
#\/

#toolbar - currently a placeholder for a toolbar
toolbar_container = tk.Frame(root, width=100, height=2)
toolbar = tk.Label(toolbar_container,width=100, height=2, text="Toolbar", bg="green")

#shortcut box
shortcut_container = tk.Frame(width=100,height=100,bg="red")
shortcut_bg = tk.Label(shortcut_container, width=100,height=100,bg="red")

#test shortcut
test = shortcut(20,10,"TEST")


#creates currently loaded shortcuts - I don't yet have a system for loading shortcuts finished
def create_loaded_shortcuts():
    global test
    #this will be changed to for shortcuts in shortcuts_loaded, which will be an array to store the loaded shortcut class instances
    for i in range(1):
        sc = tk.Label(shortcut_container, width=test.width, height=test.heigth,bg="blue",text=test.name)
        sc.pack()


#placeholder function for loading short
def load_shortcuts():
    pass


#creates window and assigns the base window to root
def innitialize_window():
    global root,toolbar,shortcut_container,test

    root.title(app_display_name + " - " + app_version)
    root.geometry(default_window_scale)

    #pack default elements
    toolbar_container.pack(expand=True,fill=tk.X)
    toolbar.pack(expand=True,fill=tk.X)
    create_loaded_shortcuts()
    shortcut_bg.pack(expand=True,fill=tk.BOTH)
    shortcut_container.pack(expand=True,fill=tk.BOTH)
    

    root.mainloop()
    
    

