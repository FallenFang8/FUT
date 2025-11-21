# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag
import button_func as func


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Dynamic Button App")

        # Get the screen dimensions
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Set the window size to match the screen
        master.geometry(f"{screen_width}x{screen_height}+0+0")

        # Bring window to front and focus
        master.lift()
        master.attributes('-topmost', True)
        master.after_idle(master.attributes, '-topmost', False)

        # Frame for buttons
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)

        self.button_actions = {}

    def add_button(self, button_name, width=20, height=2, font="Arial", font_size=12):
        new_button = tk.Button(
            self.buttons_frame,
            text=button_name,
            command=lambda: self.trigger_action(button_name),
            width=width, # characters wide
            height=height, # lines tall
            font=(font, font_size)  # font family and size
        )
        new_button.pack(pady=5)

    def trigger_action(self, button_name):
        action = self.button_actions.get(button_name)
        if action:
            action()
        else:
            print(f"No action assigned for {button_name}")

    def assign_action(self, button_name, action):
        self.button_actions[button_name] = action