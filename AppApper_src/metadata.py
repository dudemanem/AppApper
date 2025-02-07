from tkinter import PhotoImage
import os

#contains basic data about app
app_version = "v0.2.5"
app_display_name = "AppApper"
default_window_scale = "1300x750"
#icon_path = 'images\icon\AppApper.png'
data_dir = os.environ["USERPROFILE"] + "\\AppData\\Local\\AppApper"
profile_dir = os.environ["USERPROFILE"] + "\\AppData\\Local\\AppApper\\Profiles"
save_file_path = data_dir + "\\save.txt"



