import tkinter as tk
from shortcut import *
from metadata import *

root = tk.Tk()
root.columnconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

#DEFAULT ELEMENTS TO BE CREATED ALWAYS
#toolbar
toolbar = tk.Label(root,width=100, height=10, text="Toolbar", bg="green")

#shortcut box
shortcut_container = tk.Label(root,width=100,height=100,bg="red")
shortcut_bg = tk.Label(shortcut_container, width=100,height=100,)

#test shortcut
test = shortcut(20,10,"crap")


#creates currently loaded shortcuts
def create_loaded_shortcuts():
    global test
    #this will be changed to for shortcuts in shortcuts_loaded, which will be an array to store the loaded shortcut class instances
    for i in range(1):
        sc = tk.Label(shortcut_container, width=test.width, height=test.heigth,bg="blue")
        sc.pack()
#creates window and assigns the base window to root
def innitialize_window():
    global root,toolbar,shortcut_container,test
    root.title(app_display_name + " - " + app_version)
    root.geometry(default_window_scale)

    #pack default elements
    toolbar.pack()
    create_loaded_shortcuts()
    shortcut_bg.pack()
    shortcut_container.pack()
    
    

    root.mainloop()
    
    
#updates parts of the UI that need to scale with the screen
def update_ui():
    global root,toolbar,shortcut_container

    scren_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #update individual elements

    #toolbar
    toolbar.config(width=scren_width,height=2)
    toolbar.update()

    #shortcut box
    shortcut_bg.config(width=scren_width)
    shortcut_bg.update()


    # run itself again after 1000 ms
    root.after(1000, update_ui) 

update_ui()
