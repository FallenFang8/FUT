# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Dynamic Button App")
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)

        self.add_button_frame = tk.Frame(self.master)
        self.add_button_frame.pack(pady=20)

        self.button_name_entry = tk.Entry(self.add_button_frame)
        self.button_name_entry.pack(side=tk.LEFT)
        self.add_button = tk.Button(self.add_button_frame, text="Add Button", command=self.add_button_action)
        self.add_button.pack(side=tk.LEFT)

        self.button_actions = {}

    def add_button_action(self):
        button_name = self.button_name_entry.get()
        if button_name:
            new_button = tk.Button(self.buttons_frame, text=button_name, command=lambda: self.trigger_action(button_name))
            new_button.pack(pady=5)
            self.button_name_entry.delete(0, tk.END)

    def trigger_action(self, button_name):
        action = self.button_actions.get(button_name)
        if action:
            action()
        else:
            print(f"No action assigned for {button_name}")

    def assign_action(self, button_name, action):
        self.button_actions[button_name] = action