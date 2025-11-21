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

# Add buttons and assign functions
app.add_button("Say Hello", width=20, height=1, font_size=20)
app.assign_action("Say Hello", func.say_hello)

app.add_button("Click Mouse", width=20, height=1, font_size=20)
app.assign_action("Click Mouse", func.click_mouse)

root.mainloop()