# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag
import button_func as func
import window as win
import pyperclip
from PIL import Image, ImageTk
import json


############################################################################
#                                                                          #
#                             Create window                                #
#                                                                          #
############################################################################
root = tk.Tk()
app = win.MainWindow(root)
app.add_title("FUT - Fallen's Utility Toolkit", page="main")


############################################################################
#                                                                          #
#                             Settings icon                                #
#                                                                          #
############################################################################

frame = app.pages["main"]

# Load and resize icon
img = Image.open("assets/settings_icon.png").resize((40, 40))
icon = ImageTk.PhotoImage(img)

# Create button with icon
settings_btn = tk.Button(frame, image=icon, command=lambda: func.edit_settings(app))
settings_btn.image = icon  # keep reference, otherwise icon disappears

# Place in top-right
settings_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)



############################################################################
#                                                                          #
#                                Buttons                                   #
#                                                                          #
############################################################################

app.add_button("Settings", action=func.edit_settings, width=20, height=2, font_size=20)
app.add_button("Colour Grabber", action=func.colour_grabber, width=20, height=2, font_size=20)
app.add_button("Location Logger", action=func.location_logger, width=20, height=2, font_size=20)
app.add_button("Autoclicker", action=func.autoclicker, width=20, height=2, font_size=20)
app.add_button("Keytyper", action=func.keytyper, width=20, height=2, font_size=20)

app.add_button("Exit", action=win.exit_app, width=5, height=1, font_size=15)
# Register fullscreen hotkey
win.register_fullscreen_hotkey(app)


root.mainloop()
