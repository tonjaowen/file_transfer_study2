# C:\Users\Tonja\Desktop\file_transfer_study
# -*- coding: utf-8 -*-
#
# Python Ver: 3.6
#
# Author: Tonja Owen
#               
from tkinter import *
import tkinter as tk
import ft_gui
import ft_func


class ParentWindow(Frame):

    def __init__(self, master):
    
        # master frame config and center window
        self.master = master
        self.master.minsize(300, 200)
        self.master.maxsize(300, 200)
        ft_func.center_window(self, 300, 200)

        # title and color scheme
        self.master.title("File Transfer")
        self.master.configure(bg="#F0F0F0")

        # sourcePath
        self.sourcePath = ""
        self.destPath = ""
        self.lastTrans = 0.0
        
        # widgets in gui
        ft_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
