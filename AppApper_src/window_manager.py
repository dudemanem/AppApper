import tkinter as tk
from shortcut import *
from metadata import *
from pathlib import Path
import saveload as data_manager
import tkinter.messagebox
import os as os
import subprocess
import tkinter.simpledialog 
from tkinter import filedialog as fd
import stat




#--------------------------------------------------------------------------------------------------------- Variables

#sets up root 
root = tk.Tk()
root.title(app_display_name + " - " + app_version)
#App Icon
#root.iconbitmap(r'AppApper.ico') # - old code, ignore this shit
root.geometry(default_window_scale)
root.resizable(1,1)

current_path = tkinter.StringVar()
current_type = tkinter.StringVar()
current_fpath = tkinter.StringVar()


#These are the default widgets of the app
#|
#\/


#toolbar - currently a placeholder for a toolbar
toolbar_container = tk.Frame(root,bg="grey")
toolbar_container.grid(row=0, column=0, sticky="nsew",columnspan=10,pady=0)
for i in range(30):
    toolbar_container.grid_columnconfigure(i, weight=1)

shortcut_container = tk.Frame(root,bg="silver")


shortcut_limit_text = tk.Label(root,width=10,height=10,text="Profiles created: 0/15")
    


create_button = tk.Button(toolbar_container, text="Create Shortcut",command=lambda:create_new_shortcut())
load_profile = tk.Button(toolbar_container, text="Load Profile",command=lambda:load_profile_process())
profile_name = tk.Text(toolbar_container, height=1,width=15,)
save_profile = tk.Button(toolbar_container, text="Save Profile", command= lambda : data_manager.save_profile(profile_name.get("1.0",'1.end')))

#--------------------------------------------------------------------------------------------------------- Functions


def is_executable_file(path):
    # Check if the path exists and is a file
    if os.path.isfile(path):
        # Check if the file has execute permissions
        st = os.stat(path)
        return bool(st.st_mode & stat.S_IEXEC)
    return False



#This funciton runs through all the current shortcuts and makes all of their ids run in linear order.
#This is important because if a shortcut is deleted with the id of say, 4, then the shortcut that had the id of 5 should now be 4, and so on
def reset_shortcut_ids():
    for i in range(len(data_manager.loaded_shortcuts)):
        data_manager.loaded_shortcuts[i].id = (i + 1)



#creates currently loaded shortcuts
def create_loaded_shortcuts():

    for child in shortcut_container.winfo_children():
        child.destroy()

    c = 1
    r = 1
    #this index variable will be passed to the delete_shortcut function to let it know which shortcut needs to be deleted
    index = 0
    for selected in data_manager.loaded_shortcuts:
        if r > 3:
            tkinter.messagebox.showerror("No Good Amount Of Space :<","The program ran out of space, some shortcuts are not shown!")
            break
        sc = tk.Frame(shortcut_container, bg="red",width=100,height=100)
        sc_button = tk.Button(sc,text = "Launch: " + selected.name,command=lambda p = selected.app_path, t = selected.type, fp = selected.file_path: open_app(p,t,fp))
        sc_color = tk.Frame(sc, bg="red", width=200, height=150)
        delete_button = tk.Button(sc,text = "X", command=lambda i = index: delete_shortcut(i))
        sc.grid(row=r,column=c,sticky="nsew", pady=10,padx=10)
        sc_button.pack(expand=True,fill="both")
        sc_color.pack(expand=True,fill="both")
        delete_button.pack(expand=True,fill="both")
        c += 1
        index += 1
        if c == 6:
            r += 1
            c = 1
    shortcut_limit_text.config(text="Shortcuts created: " + str(len(data_manager.loaded_shortcuts)) + "/15")

def open_app(path,type,fpath):
    current_path.set(path)
    current_type.set(type)
    current_fpath.set(fpath)

    if not os.path.exists(current_path.get()):
        tkinter.messagebox.showerror("System Cannot Find Path!","Please make sure the path is valid!")
        return

    if current_type.get() == "app":
        if is_executable_file(current_path.get()):
            try:
                # Attempt to run a command with a timeout of 5 seconds
                result = subprocess.run([current_path.get()],timeout=2, check=True)
                print("Command succeeded:", result)
            except subprocess.TimeoutExpired:
                print("The command timed out.")
            except subprocess.CalledProcessError as e:
                print("The command failed with return code:", e.returncode)
        else:
            tkinter.messagebox.showerror("NOT AN EXE", "That file is not an executable.")
    elif current_type.get() == "file":
        if is_executable_file(current_fpath.get()):
            try:
                # Attempt to run a command with a timeout of 5 seconds
                result = subprocess.run([current_fpath.get(), current_path.get()],timeout=5, check=True)
                print("Command succeeded:", result)
            except subprocess.TimeoutExpired:
                print("The command timed out.")
            except subprocess.CalledProcessError as e:
                print("The command failed with return code:", e.returncode)
        else:
            tkinter.messagebox.showerror("NOT AN EXE", "That file is not an executable.")


#index is obtained from lambda funcion in delete button
#this function removes the shortcut from the loaded list and calls the reset for the shortcut ids
def delete_shortcut(index):
    data_manager.loaded_shortcuts.pop(index)
    reset_shortcut_ids()
    create_loaded_shortcuts()
    
def create_new_shortcut():
    name = tkinter.simpledialog.askstring("Enter Name", "Enter a name for this shortcut.")
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt')
    )

    path = fd.askopenfilename(
        title="Select an app to launch",
        initialdir=profile_dir,
        filetypes=filetypes
    )

    sc_type = ""
    apath = ""

    if is_executable_file(path):
        sc_type = "app"
    else:
        sc_type = "file"
        apath = fd.askopenfilename(
        title="Select an app to launch this file",
        initialdir=profile_dir,
        filetypes=filetypes
        )

    id = 0
    if len(data_manager.loaded_shortcuts) > 0:
        id = data_manager.loaded_shortcuts[len(data_manager.loaded_shortcuts)-1].id+1
    else:
        id = 1

    sc = shortcut(id,name,sc_type,path,apath,"null",80,50)
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
    shortcut_container.grid(row=1, column=0, sticky="nsew",columnspan=10,pady=0,rowspan=100,)
    shortcut_limit_text.grid(row=1,column=9,sticky="nsew",columnspan=1)
    create_loaded_shortcuts()

    #load default save data
    data_manager.load_save_data()
    

    root.mainloop()