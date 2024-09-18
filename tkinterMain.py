import random
import enemies
import rooms  # Import rooms from rooms.py
#import enemyTurn
import textParser
import items
import enemySelector
import battleSystem
import playerStats

import tkinter as tk
from tkinter import messagebox
import json

# Define the game functions and variables
def start_new_game():
    global player, current_room
    name = input("Enter your hero's name: ")
    player_class = input("Choose your class (Warrior, Mage, Thief): ").lower()
    
    if player_class == "warrior":
        player = playerStats.Hero(name, [], playerStats.warriorStats, [], "Warrior", 0, 1)
    elif player_class == "mage":
        player = playerStats.Hero(name, [], playerStats.mageStats, [], "Mage", 0, 1)
    elif player_class == "thief":
        player = playerStats.Hero(name, [], playerStats.thiefStats, [], "Thief", 0, 1)
    else:
        messagebox.showinfo("Error", "Invalid class selection.")
        return
    
    # Start in room #1
    current_room = rooms.rooms_dict[1]
    update_text(current_room.entryDescription)

def load_game():
    global player, current_room
    player = playerStats.Hero.load("save_game.json")
    if player:
        current_room = rooms.rooms_dict[player.current_room]  # Load current room based on saved data
        update_text(current_room.entryDescription)

def save_game():
    if player:
        player.save("save_game.json")

def process_command():
    command = input_box.get().lower()
    input_box.delete(0, tk.END)  # Clear the text input after command is processed
    
    # Parse the command
    if "go" in command:
        direction = command.split()[-1]  # Get the last word (e.g., "north" from "go north")
        move(direction)
    elif "pick up" in command:
        item = command.split("pick up ")[1]  # Get the item to pick up
        # Implement item picking logic here
        update_text(f"You attempt to pick up {item}.")  # Replace with actual pick-up logic
    else:
        update_text("Command not recognized.")

def move(direction):
    global current_room
    # Use the possibleDirections attribute from the Room class
    new_room_index = current_room.possibleDirections.get(direction)
    if new_room_index:
        current_room = rooms.rooms_dict[new_room_index]
        player.current_room = new_room_index  # Update player's current room
        update_text(current_room.entryDescription)
    else:
        update_text("You cannot go that way.")

def update_text(message):
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, message)
    text_box.config(state=tk.DISABLED)

def show_menu():
    for widget in root.winfo_children():
        widget.destroy()

    menu_frame = tk.Frame(root)
    menu_frame.pack()

    tk.Label(menu_frame, text="Welcome to the RPG!").pack(pady=10)
    
    tk.Button(menu_frame, text="Start New Game", command=start_new_game).pack(pady=5)
    tk.Button(menu_frame, text="Load Game", command=load_game).pack(pady=5)
    tk.Button(menu_frame, text="Exit", command=root.quit).pack(pady=5)

# Create the GUI
root = tk.Tk()
root.title("Text Adventure Game")

# Create a text box for game messages
text_box = tk.Text(root, width=60, height=15, wrap=tk.WORD)
text_box.pack(pady=10)

# Create an input box for entering commands
input_box = tk.Entry(root, width=40)
input_box.pack(pady=10)

# Bind the Enter key to process commands
input_box.bind("<Return>", lambda event: process_command())

# Create a text label to show hints or commands
command_label = tk.Label(root, text="Type your command and press Enter")
command_label.pack(pady=5)

# Start by showing the menu
show_menu()
root.mainloop()
