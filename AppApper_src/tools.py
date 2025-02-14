from PIL import Image, ImageOps
import os
from metadata import *
import stat
import random as random


#####################################################################################
#This function generates a random string to be added to the name of a shortcut image#
#####################################################################################
def gen_string():
    s = ""
    for i in range(5):
        s = s + icon_name_extenstion_characters[random.randint(0,len(icon_name_extenstion_characters))]
    return s



#####################################################################################################
#this function extracts icon from an exe and returns path to newly copied png file in data directory#
#####################################################################################################
def extract_icon_from_exe(path,name,icon_out_path):
    import win32ui
    import win32gui
    import win32con
    import win32api

    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

    large, small = win32gui.ExtractIconEx(path,0)
    win32gui.DestroyIcon(small[0])

    hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap( hdc, ico_x, ico_x )
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject( hbmp )
    hdc.DrawIcon( (0,0), large[0] )

    bmpstr = hbmp.GetBitmapBits(True)
    icon = Image.frombuffer(
        'RGBA',
        (32,32),
        bmpstr, 'raw', 'BGRA', 0, 1
    )

    full_outpath = os.path.join(icon_out_path, "{}.png".format(name + gen_string()))
    icon.resize((200, 150))
    icon.save(full_outpath, 'PNG')
    return full_outpath



######################################################################################################################################
#this function takes the image at the given path and copies/resizes it at a new location, then returns the path to this new location.#
######################################################################################################################################
def image_to_icon(ipath,name):
    if ipath == None:
        return
    icon = Image.open(ipath,"r")
    new_size = (200,150)
    icon = ImageOps.fit(icon,new_size,Image.Resampling.LANCZOS)
    ipath = data_dir + "\\" + name + ".png"
    icon.save(ipath, "PNG")
    return ipath


########################################################
#Checks if given path is an executable file for windows#
########################################################
def is_executable_file(path):
    if os.path.isfile(path):
        # Check if the file has execute permissions
        st = os.stat(path)
        return bool(st.st_mode & stat.S_IEXEC)
    return False