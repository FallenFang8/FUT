# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag
import window as win
import pyperclip
import json
import games
with open("config.json", "r") as f:
    config = json.load(f)


############################################################################
#                                                                          #
#                            Colour Grabber                                #
#                                                                          #
############################################################################

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

############################################################################
#                                                                          #
#                              Location Logger                             #
#                                                                          #
############################################################################

def location_logger(app):
    frame = win.create_page(app, "location_logger_page", "Press + to log location")
    coords = {}
    rep = 0
    
    def copy_coords():
        pyperclip.copy(str(coords))
    
    # Create a label 
    coords_label = tk.Label(frame, text=f"coords: {coords}", font=("Arial", 16), wraplength=400)
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
        
    # Update wraplength dynamically on window resize
    def update_wraplength(event):
        coords_label.config(wraplength=frame.winfo_width() - 50)  # Subtract padding

    frame.bind("<Configure>", update_wraplength)
    
    
    win.hotkey_func(app, win.get_setting("hotkeys.location_logger"), "Location Logger", log_location)
        
        
    #show page
    app.show_page("location_logger_page")    
    
############################################################################
#                                                                          #
#                               Autoclicker                                #
#                                                                          #
############################################################################
    
    
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

############################################################################
#                                                                          #
#                                  Keytyper                                #
#                                                                          #
############################################################################
    
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



############################################################################
#                                                                          #
#                                  Settings                                #
#                                                                          #
############################################################################
def edit_settings(app):
    frame = win.create_page(app, "edit_settings_page", "Edit Settings")
    app.add_button("Keybinds", action=hotkey_page, page="edit_settings_page", width=20, height=2, font_size=20)
    app.add_button("Toggle Fullscreen",action=win.toggle_fullscreen, page="edit_settings_page",width=20,height=2,font_size=20)


    
    app.show_page("edit_settings_page")


        

def hotkey_page(app):
    # Create the page/frame
    frame = win.alt_create_page(app, "hotkey_config_page", "Edit Keybinds", back_page="edit_settings_page")

    
    app.add_button("Colour Grabber", action=lambda a: win.set_new_hotkey(a, "Colour Grabber", "hotkeys.colour_grabber"), page="hotkey_config_page", width=config["main_buttons"]["width"], height=config["main_buttons"]["height"], font_size=config["main_buttons"]["font_size"])
    app.add_button("Location Logger", action=lambda a: win.set_new_hotkey(a, "Location Logger", "hotkeys.location_logger"), page="hotkey_config_page", width=config["main_buttons"]["width"], height=config["main_buttons"]["height"], font_size=config["main_buttons"]["font_size"])
    app.add_button("Autoclicker Toggle", action=lambda a: win.set_new_hotkey(a, "Autoclicker Toggle", "hotkeys.autoclicker_toggle"), page="hotkey_config_page", width=config["main_buttons"]["width"], height=config["main_buttons"]["height"], font_size=config["main_buttons"]["font_size"])
    app.add_button("Keytyper", action=lambda a: win.set_new_hotkey(a, "Keytyper", "hotkeys.keytyper"), page="hotkey_config_page", width=config["main_buttons"]["width"], height=config["main_buttons"]["height"], font_size=config["main_buttons"]["font_size"])
    app.add_button("Fullscreen Toggle", action=lambda a: win.set_new_hotkey(a, "Fullscreen Toggle", "hotkeys.fullscreen_toggle"), page="hotkey_config_page", width=config["main_buttons"]["width"], height=config["main_buttons"]["height"], font_size=config["main_buttons"]["font_size"])
    
    
    app.show_page("hotkey_config_page")


############################################################################
#                                                                          #
#                                  Games                                   #
#                                                                          #
############################################################################
def game_dir(app):
    frame = win.create_page(app, "games_page", "Games")
    
    #Buttons
    app.add_button("Tic Tac Toe", action=games.tic_tac_toe, page="games_page", width=config["main_buttons"]["width"], height=config["main_buttons"]["height"], font_size=config["main_buttons"]["font_size"])
    
    
    app.show_page("games_page")