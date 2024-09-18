#rpgModel



import random
import enemies
import rooms
#import enemyTurn
import textParser
import items
import enemySelector
import battleSystem
import playerStats

#640x360 aspect ratio, 320x180, 160x90 and so on

import tkinter as tk
from tkinter import messagebox
import pickle

# Define the game functions and variables
def start_game():
    global current_room
    current_room = rooms["entrance"]
    update_text("You are at the entrance. Choose your path.")

def update_text(message):
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, message)
    text_box.config(state=tk.DISABLED)

def save_game():
    global current_room
    with open("save_game.pkl", "wb") as f:
        pickle.dump(current_room, f)
    messagebox.showinfo("Saved", "Game saved successfully!")

def load_game():
    global current_room
    try:
        with open("save_game.pkl", "rb") as f:
            current_room = pickle.load(f)
        messagebox.showinfo("Loaded", "Game loaded successfully!")
        update_text("Welcome back! You are at the {}.".format(current_room["name"]))
    except FileNotFoundError:
        messagebox.showinfo("Error", "No saved game found.")

def move(direction):
    global current_room
    new_room = current_room["exits"].get(direction)
    if new_room:
        current_room = rooms[new_room]
        update_text("You are at the {}. Choose your path.".format(current_room["name"]))
    else:
        update_text("You cannot go that way.")

# Define the rooms and exits
rooms = {
    "entrance": {
        "name": "Entrance Hall",
        "exits": {"north": "hallway1", "east": "dining_room"},
    },
    "hallway1": {
        "name": "Hallway 1",
        "exits": {"south": "entrance", "east": "living_room"},
    },
    "dining_room": {
        "name": "Dining Room",
        "exits": {"west": "entrance"},
    },
    "living_room": {
        "name": "Living Room",
        "exits": {"west": "hallway1"},
    },
}

# Create the GUI
root = tk.Tk()
root.title("Text Adventure Game")

text_box = tk.Text(root, width=40, height=10, wrap=tk.WORD)
text_box.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

save_button = tk.Button(button_frame, text="Save Game", command=save_game)
save_button.grid(row=0, column=0, padx=10)

load_button = tk.Button(button_frame, text="Load Game", command=load_game)
load_button.grid(row=0, column=1, padx=10)

north_button = tk.Button(button_frame, text="Go North", command=lambda: move("north"))
north_button.grid(row=1, column=1, pady=5)

east_button = tk.Button(button_frame, text="Go East", command=lambda: move("east"))
east_button.grid(row=2, column=2, padx=5)

south_button = tk.Button(button_frame, text="Go South", command=lambda: move("south"))
south_button.grid(row=3, column=1, pady=5)

west_button = tk.Button(button_frame, text="Go West", command=lambda: move("west"))
west_button.grid(row=2, column=0, padx=5)

start_game()
root.mainloop()