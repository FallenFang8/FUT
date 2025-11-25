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
    
    win.hotkey_func(app, win.get_setting("hotkeys.colour_grabber"), "Colour Grabber", grab_color)

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
    
    
    win.hotkey_func(app, win.get_setting("hotkeys.location_logger"), "Location Logger", log_location)
        
        
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

    
    win.hotkey_func(app, win.get_setting("hotkeys.autoclicker_toggle"), "Autoclicker", toggle_clicking)
    
    # Show page
    app.show_page("autoclicker_page")
    
def keytyper(app):
    frame = win.create_page(app, "keytyper_page", "Press + to type")
    message = ""
    
    # Textbox for input
    entry = tk.Text(frame, font=("Arial", 16), width=75, height=10) 
    entry.pack(pady=10)

    
    def save_message():
        nonlocal message
        message = entry.get("1.0", tk.END).strip()  # Get all text from line 1, char 0 to the end
        entry.delete("1.0", tk.END)  # Clear text box

    
    # Confirm button
    confirm_btn = tk.Button(frame, text="Confirm message", font=("Arial", 14), command=save_message)
    confirm_btn.pack(pady=10)
    
    def type_key():
        keyboard.press('delete')
        if message.strip():
            keyboard.write(message)
    
    
    win.hotkey_func(app, win.get_setting("hotkeys.keytyper"), "Keytyper", type_key)

    # Show page
    app.show_page("keytyper_page")
    
def exit_app(app):
    app.master.destroy()


############################################################################
#                                                                          #
#                                  Config                                  #
#                                                                          #            
############################################################################
def edit_config(app):
    frame = win.create_page(app, "edit_config_page", "Edit Configuration")
    app.add_button("Hotkeys", action=hotkey_page, page="edit_config_page", width=20, height=2, font_size=20)
    
    
    app.show_page("edit_config_page")

def hotkey_page(app):
    # Create the page/frame
    frame = app.create_page("hotkey_config_page")
    # Add a title if provided
    app.add_title("Edit Hotkeys", page="hotkey_config_page")

    back_btn = tk.Button(frame, text="Back", font=("Arial", 14),
                     command=lambda: app.show_page("edit_config_page"))
    back_btn.place(relx=0.5, rely=1.0, anchor="s", y=-30)

    app.show_page("hotkey_config_page")