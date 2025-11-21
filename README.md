# FUT - Fallen's Utility Toolkit

Purpose:
This project is intended to be a lightweight, extensible utility toolkit built with Python's Tkinter GUI library.
It presents a simple interface that allows users to add buttons dynamically; each button is bound to a specific utility function.
Over time the repository will grow to include a collection of small, focused tools (file utilities, text processors, automation helpers, network testers, etc.) that users can enable or disable from the GUI.


## Project Structure

```
tkinter-button-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── ui
│   │   └── window.py    # Contains the MainWindow class for the Tkinter window
│   ├── actions
│   │   └── button_actions.py  # Defines functions for button actions
├── requirements.txt      # Lists the dependencies required for the project
└── README.md             # Documentation for the project
```

## Requirements

To run this application, you need to have Python installed on your machine. You can install the required dependencies by running:

```
pip install -r requirements.txt
```

## Running the Application

To start the application, navigate to the `src` directory and run the `main.py` file:

```
python main.py
```

## Adding Buttons

Once the application is running, you can add buttons dynamically. Each button can be associated with a specific action defined in the `button_actions.py` file. 

Feel free to explore and modify the code to add more functionality or customize the actions associated with the buttons!

## Git tracking
cd C:\Users\edu9174927\OneDrive - IKT Agder\Fag\VG2\IT2\FUT
git add <filename>