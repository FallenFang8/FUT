# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag
import button_func as func
import window as win

root = tk.Tk()
app = win.MainWindow(root)

# Add buttons to main page
app.add_title("FUT - Fallen's Utility Toolkit", page="main")
app.add_button("Say Hello", action=func.say_hello, width=20, height=2, font_size=20)
app.add_button("Colour Grabber", action=func.colour_grabber, width=20, height=2, font_size=20)

root.mainloop()