import tkinter as tk

class shortcut():
    def __init__(self, id, name, type, apath, fpath, ipath, width, height):
        self.id = id
        self.name = name
        self.type = type
        self.app_path = apath
        self.file_path = fpath
        self.icon_path = ipath
        self.width = width
        self.heigth = height
