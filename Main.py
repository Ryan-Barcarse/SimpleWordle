"""
March 19, 2025
Ryan Bacarse

This is a recreation of the game Wordle. There are new upcommming modes such as a two player mode as well as a single player mode.

"""

from tkinter import *
import tkinter.messagebox 
from PvsP import game

def gameStart():
    box.destroy()
    game()
# creates a tkinter box window 
box = tkinter.Tk()
box.configure(bg="#FFF8E7")
width = box.winfo_screenwidth()
height = box.winfo_screenheight()
box.geometry("%dx%d" % (width,height)) 
 
# box window title and dimension 
box.title("Simple Wordle Version 1.0.0") 
        
Title = Label(box, text="Welcome to Simple Wordle!")
Title.pack()

P_Button = tkinter.Button(box, text="1 vs 1", width=25, command=gameStart)
P_Button.pack()

box.mainloop()
