import tkinter as tk
from metadata import *

root = tk.Tk()

#DEFAULT ELEMENTS TO BE CREATES ALWAYS
toolbar = tk.Label(root,width=100, height=10, text="Toolbar", bg="green")



#creates window and assigns the base window to root
def innitialize_window():
    global root,toolbar
    root.title(app_display_name + " - " + app_version)
    root.geometry(default_window_scale)

    #pack default elements
    toolbar.pack()
    root.mainloop()
    
    
#updates parts of the UI that need to scale with the screen
def update_ui():
    global root,toolbar

    scren_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #update individual elements
    toolbar.config(width=scren_width,height=2)
    toolbar.update()


    # run itself again after 1000 ms
    root.after(1000, update_ui) 

update_ui()
