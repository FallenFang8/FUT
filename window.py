# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag
import button_func as func
import pyperclip
import json

with open("config.json", "r") as f:
    config = json.load(f)

#------------------------------------


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Dynamic Button App")

        # Fullscreen window
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f"{screen_width}x{screen_height}+0+0")

        master.lift()
        master.attributes('-topmost', True)
        master.after_idle(master.attributes, '-topmost', False)

        self.button_actions = {}
        self.pages = {}

        # Create main page
        self.create_page("main")
        self.show_page("main")

    def create_page(self, page_name):
        """Create a new page/frame that fills the window."""
        frame = tk.Frame(self.master)
        frame.place(x=0, y=0, relwidth=1, relheight=1)  # make it fill entire window
        self.pages[page_name] = frame
        return frame

    def show_page(self, page_name):
        """Show only the specified page."""
        frame = self.pages.get(page_name)
        if frame:
            frame.tkraise()
        else:
            print(f"No page named '{page_name}' exists.")

    def add_button(self, button_name, action=None, page="main", width=20, height=2, font="Arial", font_size=12):
        """Add a button to a specific page."""
        frame = self.pages.get(page)
        if not frame:
            frame = self.create_page(page)

        new_button = tk.Button(
            frame,
            text=button_name,
            width=width,
            height=height,
            font=(font, font_size),
            command=lambda: self._handle_button(button_name, action)
        )
        new_button.pack(pady=5)

    def _handle_button(self, button_name, action):
        """Trigger button action or navigate to page."""
        if action:
            action(self)  # Pass MainWindow instance to function
        else:
            act = self.button_actions.get(button_name)
            if act:
                act(self)
            else:
                print(f"No action assigned for '{button_name}'")

    def assign_action(self, button_name, action):
        self.button_actions[button_name] = action
            
    def add_title(self, text, page="main", font=("Arial", 30, "bold")):
        """Add a title label to a page at the top."""
        frame = self.pages.get(page)
        if frame:
            tk.Label(frame, text=text, font=font).pack(pady=20)
        else:
            print(f"No page named '{page}' exists.")
            
            
            
            
            
def create_page(app, page_name, page_title=""):
    """
    Creates a new page in the app with basic setup:
    - Adds a frame for the page
    - Adds a title at the top
    - Adds a 'Back' button to return to the main page
    Returns the frame so you can add other widgets.
    """
    # Create the page/frame
    frame = app.create_page(page_name)
    # Add a title if provided
    if page_title:
        app.add_title(page_title, page=page_name)
    # Add a back button (skip if this is the main page)
    if page_name != "main":
        back_btn = tk.Button(frame, text="Back", font=("Arial", 14),
                     command=lambda: app.show_page("main"))
        back_btn.place(relx=0.5, rely=1.0, anchor="s", y=-30)


    return frame


def hotkey_func(app, hotkey, name, function):
    print(f"Hotkey {name} is running")
    # Register a global hotkey that logs cursor position
    hotkey_id = keyboard.add_hotkey(hotkey, function, suppress=True)

    def disable_hotkey():
        keyboard.remove_hotkey(hotkey_id)

    # Disable hotkey when switching page
    app.on_page_change(disable_hotkey)
    

def sleep(x):
    time.sleepe(x)
    
def random(start, end):
    x = RNG.randint(start, end)
    return x

def get_setting(path, default=None):
    """
    path example: "hotkeys.colour_grabber"
    Searches nested keys safely and returns default if not found.
    """
    keys = path.split(".")
    value = config
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return default
    return value