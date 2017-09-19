# C:\Users\Tonja\Desktop\file_transfer_Study
# -*- coding: utf-8 -*-
# Python Ver: 3.6
# Author: Tonja Owen


from tkinter import ttk
import time
import ft_func


def load_gui(self):

    ft_func.create_db(self)

    # Source/Destination Boxes
    self.sourceEntry = ttk.Entry(self.master, width=40)
    self.destEntry = ttk.Entry(self.master, width=40)
    self.sourceEntry.grid(row=1, column=0, columnspan=2, padx=(20, 0), pady=(0, 20), sticky="new")
    self.destEntry.grid(row=3, column=0, columnspan=2, padx=(20, 0), pady=(0, 20), sticky="new")
    
    # Buttons for Source, Destination and Transfer
    ttk.Button(self.master, text="Select Source",
               command=lambda: ft_func.source_select(self)).grid(row=0, column=1, pady=(15, 0), sticky="se")
    ttk.Button(self.master, text="Select Destination",
               command=lambda: ft_func.dest_select(self)).grid(row=2, column=1, pady=(15, 0), sticky="se")
    ttk.Button(self.master, text="Transfer",
               command=lambda: ft_func.validate(self)).grid(row=4, column=0, padx=(20, 0), sticky="w")
    
    # Last Transfer Label
    self.timeLabel = ttk.Label(self.master, text="Last Transfer Occurred:\n" + (time.ctime(self.lastTrans)))
    self.timeLabel.grid(row=4, column=1, sticky="e")
    
    
if __name__ == "__main__":
    pass
