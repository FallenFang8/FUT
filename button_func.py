# IMPORTS
import tkinter as tk
import random as RNG
import time
import keyboard
import pyautogui as pag

def say_hello(app):
    # Create the page (or get it if it already exists)
    app.create_page("hello_page")

    # Add a title using the helper
    app.add_title("Hello!", page="hello_page")

    # Add other widgets
    frame = app.pages["hello_page"]
    tk.Label(frame, text="Welcome to the Hello Page!", font=("Arial", 20)).pack(pady=10)
    tk.Entry(frame).pack(pady=10)

    # Back button
    tk.Button(frame, text="Back", font=("Arial", 14), command=lambda: app.show_page("main")).pack(pady=10)

    # Show the new page
    app.show_page("hello_page")


def click_mouse(app):
    import pyautogui as pag
    pag.click()
    print("Mouse clicked!")