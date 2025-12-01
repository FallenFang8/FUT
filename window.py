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
        self.master.title(config["main_window"]["title"])
        

        # Load fullscreen setting from config
        self.fullscreen = get_setting("window.fullscreen", True)

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        if self.fullscreen:
            master.geometry(f"{screen_width}x{screen_height}+0+0")
            master.attributes("-fullscreen", True)
            master.overrideredirect(True)
        else:
            master.geometry("1280x720")
            master.attributes("-fullscreen", False)
            master.overrideredirect(False)

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
   
############################################################################
#                                                                          #
#                        Toggle Fullscreen                                 #
#                                                                          #
############################################################################


def toggle_fullscreen(app):
    """Toggle fullscreen and save choice to config.json."""
    app.fullscreen = not app.fullscreen  # flip the state

    if app.fullscreen:
        app.master.attributes("-fullscreen", True)
        screen_width = app.master.winfo_screenwidth()
        screen_height = app.master.winfo_screenheight()
        app.master.geometry(f"{screen_width}x{screen_height}+0+0")
    else:
        app.master.attributes("-fullscreen", False)
        app.master.geometry(config["mainwindow"]["non_fullscreen_size"])

    # Save to config.json
    if "window" not in config:
        config["window"] = {}
    config["window"]["fullscreen"] = app.fullscreen
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)


def register_fullscreen_hotkey(app):
    """Register hotkey to toggle fullscreen globally."""
    def toggle():
        toggle_fullscreen(app)

    print(f"Hotkey Toggle Fullscreen is running")
    # Register a global hotkey that logs cursor position
    hotkey_id = keyboard.add_hotkey(get_setting("hotkeys.fullscreen_toggle"), toggle, suppress=True)


            
############################################################################
#                                                                          #
#                              Create page                                 #
#                                                                          #
############################################################################      
            
            
            
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

def alt_create_page(app, page_name, page_title="", back_page="main"):
    """
    Creates a new page in the app with basic setup:
    - Adds a frame for the page
    - Adds a title at the top
    - Adds a 'Back' button to return to the any page
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
                     command=lambda: app.show_page(back_page))
        back_btn.place(relx=0.5, rely=1.0, anchor="s", y=-30)


    return frame


############################################################################
#                                                                          #
#                                  Hotkey                                  #
#                                                                          #
############################################################################

def hotkey_func(app, hotkey, name, function):
    print(f"Hotkey {name} is running")
    # Register a global hotkey that logs cursor position
    hotkey_id = keyboard.add_hotkey(hotkey, function, suppress=True)

    def disable_hotkey():
        keyboard.remove_hotkey(hotkey_id)

    # Disable hotkey when switching page
    app.on_page_change(disable_hotkey)
    
def set_new_hotkey(app, hotkey_display_name, new_hotkey):
    # Create page
    page_name = "set_hotkey_page_" + new_hotkey.replace('.', '_')
    frame = alt_create_page(app, page_name, f"Set hotkey for {hotkey_display_name}", back_page="hotkey_config_page")

    # Show current value
    keys = new_hotkey.split('.')
    cur = config
    for k in keys:
        cur = cur.get(k, None) if isinstance(cur, dict) else None
    cur_label = tk.Label(frame, text=f"Current hotkey: {cur}")
    cur_label.pack(pady=8)

    instr = tk.Label(frame, text="Press a key now (Esc to cancel)...", font=("Arial", 12))
    instr.pack(pady=6)

    def save_key(key_name):
        # set nested value in config
        node = config
        for k in keys[:-1]:
            node = node.setdefault(k, {})
        node[keys[-1]] = key_name
        with open("config.json", "w") as f:
            json.dump(config, f, indent=4)

    def on_key(event):
        # Use keysym for named keys (Escape, Shift_L, etc.)
        key_name = event.keysym
        if key_name == "Escape":
            instr.config(text="Cancelled.")
        else:
            save_key(key_name)
            instr.config(text=f"Saved new hotkey: {key_name}")
        # stop listening after one key
        frame.unbind_all("<Key>")

    # Bind globally while this page is shown; one key press will register
    frame.bind_all("<Key>", on_key)

    app.show_page(page_name)

############################################################################
#                                                                          #
#                                  Random                                  #
#                                                                          #
############################################################################
def sleep(x):
    time.sleepe(x)
    
def random(start, end):
    x = RNG.randint(start, end)
    return x

def get_setting(path, default=None):
    """
    path example: get_setting("hotkeys.colour_grabber")
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

def exit_app(app):
    app.master.destroy()