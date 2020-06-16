# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:21:36 2020

@author: Kam Look
"""

import tkinter as tk 

root = tk.Tk()

alphaLabel = tk.Label(root, text='Alpha: ')
alphaLabel.grid(row=0,column=0)
e = tk.Entry(root)
e.grid(row =0, column =1)

def storeEntry():
    alpha = e.get()
    #once all fields are working, print all fields 
    validLabel = tk.Label(root,text=alpha)
    validLabel.pack()
    
    
submitButton = tk.Button(root, text="Save and Insert Data", command=storeEntry)
submitButton.grid(row=0, column = 2)


root.mainloop()
