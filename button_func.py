# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag
import window as win
import pyperclip


def colour_grabber(app):
    # Creates the frame
    frame = win.create_page(app, "colour_grabber_page", "Press + to grab the colour")

    # Create a label to show grabbed color
    color_label = tk.Label(frame, text="--------------", font=("Arial", 16))
    color_label.pack(pady=10)
    
    # Create a canvas to display the color (initialize it once)
    color_box = tk.Canvas(frame, width=200, height=100, bg="white", highlightthickness=2, highlightbackground="black")
    color_box.pack(pady=10)

    def grab_color(e=None):
        x, y = pag.position()  # Get current mouse position
        try:
            color = pag.pixel(x, y)  # Get RGB value at that position
            color_label.config(text=f"The RGB value is: {color}")
            # Update the canvas background with the grabbed color
            color_box.config(bg=f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
        except Exception as err:
            color_label.config(text=f"Error: {err}")

    # Start listening for the '+' key globally
    keyboard.add_hotkey('+', grab_color)

    # Store the hotkey id so we can remove it later
    hotkey_id = keyboard.add_hotkey('+', grab_color)

    def disable_hotkey():
        keyboard.remove_hotkey(hotkey_id)

    # Remove hotkey when switching page
    app.on_page_change(disable_hotkey)

    # Show page
    app.show_page("colour_grabber_page")

def location_logger(app):
    frame = win.create_page(app, "location_logger_page", "Press + to log location")
    coords = {}
    rep = 0
    
    def copy_coords():
        pyperclip.copy(str(coords))
    
    # Create a label to show grabbed color
    coords_label = tk.Label(frame, text=f"coords: {coords}", font=("Arial", 16))
    coords_label.pack(pady=10)
    
    copy_button = tk.Button(frame, text="Copy to clipboard", command=copy_coords)
    copy_button.pack(pady=10)

    
    def log_location(e=None):
        nonlocal rep
        x, y = pag.position()  # Get current mouse position 
        coords[rep] = (x, y)
        rep += 1
        print(f"coords: {x, y}")
        coords_label.config(text=f"coords: {coords}")
    
    # Register a global hotkey that logs cursor position
    hotkey_id = keyboard.add_hotkey('+', log_location)

    def disable_hotkey():
        keyboard.remove_hotkey(hotkey_id)

    # Disable hotkey when switching page
    app.on_page_change(disable_hotkey)
        
        
    #show page
    app.show_page("location_logger_page")    
    
    
    
    
def autoclicker(app):
    frame = win.create_page(app, "autoclicker_page", "Press + to start/stop autoclicker")
    
    clicking = False

    def toggle_clicking(e=None):
        nonlocal clicking
        clicking = not clicking
        if clicking:
            print("Autoclicker started.")
            run_autoclicker()
        else:
            print("Autoclicker stopped.")

    def run_autoclicker():
        if clicking:
            pag.click()
            frame.after(10, run_autoclicker)  # Click every 10 ms

    # Register a global hotkey that logs cursor position
    hotkey_id = keyboard.add_hotkey('+', toggle_clicking)

    def disable_hotkey():
        keyboard.remove_hotkey(hotkey_id)

    # Disable hotkey when switching page
    app.on_page_change(disable_hotkey)

    # Show page
    app.show_page("autoclicker_page")
    
# def keytyper(app):
#     print("Hello world!")