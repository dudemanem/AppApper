from tkinter import PhotoImage
import os

#contains basic data about app
app_version = "v1.1.9 - beta"
app_display_name = "AppApper"
default_window_scale = "1300x750"
#stores a bunch of random characters that can be assigned to the end of each image name. This is so that the chance of two shortcuts sharing the same image, and therefore both relying on it not getting deleted, won't happen.
icon_name_extenstion_characters = 'uygehuiygefayggFBUyrbfuyrbow8y3gvyvbfg378gfvfugw9guyfugd8gu23fuytfayrfhgaerfaeff37gfuygfayfgoapapppqgvhkklsvytievgh'
#icon_path = 'images\icon\AppApper.png'
data_dir = os.environ["USERPROFILE"] + "\\AppData\\Local\\AppApper"
profile_dir = os.environ["USERPROFILE"] + "\\AppData\\Local\\AppApper\\Profiles"
save_file_path = data_dir + "\\save.txt"



