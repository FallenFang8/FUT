# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag
import window as win
import pyperclip

def say_hello(app):
    frame = win.create_page(app, "hello_page", "Hello!")
    # Add widgets
    tk.Label(frame, text="Welcome to the Hello Page!", font=("Arial", 20)).pack(pady=10)
    tk.Entry(frame).pack(pady=10)
    # Show the page
    app.show_page("hello_page")


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

    # Bind the '+' key when this page is shown
    def on_show_page(event):
        frame.focus_set()  # Ensure frame has focus
        frame.bind("+", grab_color)

    def on_hide_page(event):
        frame.unbind("+")  # Clean up binding when leaving page
        

    # Bind showing and hiding events
    frame.bind("<Map>", on_show_page)     # Called when frame is mapped (shown)
    frame.bind("<Unmap>", on_hide_page)   # Called when frame is unmapped (hidden)

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
    

    
    def log_location(e=None):
        nonlocal rep
        x, y = pag.position()  # Get current mouse position 
        coords[rep] = (x, y)
        rep += 1
        print(f"coords: {x, y}")
        coords_label.config(text=f"coords: {coords}")
    
    # Bind the '+' key when this page is shown
    def on_show_page(event):
        frame.focus_set()  # Ensure frame has focus
        frame.bind("+", log_location)
        tk.Button(frame, text="Copy to clipboard", command=copy_coords).pack(pady=10)

    def on_hide_page(event):
        frame.unbind("+")  # Clean up binding when leaving page
        
    # Bind showing and hiding events
    frame.bind("<Map>", on_show_page)  # Called when the frame is shown
    frame.bind("<Unmap>", on_hide_page)
        
        
    #show page
    app.show_page("location_logger_page")    