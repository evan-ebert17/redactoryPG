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

# Define global variables for player and current room
player = None
current_room = None
name_entry = None
class_entry = None

def start_new_game():
    # Destroy the menu screen and move to the character creation screen
    for widget in root.winfo_children():
        widget.destroy()

    # Character creation screen
    character_creation_frame = tk.Frame(root)
    character_creation_frame.pack()

    tk.Label(character_creation_frame, text="Enter your name:").pack(pady=5)
    global name_entry
    name_entry = tk.Entry(character_creation_frame, width=30)
    name_entry.pack(pady=5)

    tk.Label(character_creation_frame, text="Choose your class (Warrior, Mage, Thief):").pack(pady=5)
    global class_entry
    class_entry = tk.Entry(character_creation_frame, width=30)
    class_entry.pack(pady=5)

    # Button to confirm and create the character
    tk.Button(character_creation_frame, text="Create Character", command=create_character).pack(pady=10)

def create_character():
    # Function to handle character creation after input
    global player, current_room
    
    name = name_entry.get().capitalize()
    player_class = class_entry.get().lower()

    # Validate class choice and start the game
    if player_class == "warrior":
        player = playerStats.Hero(name, [], playerStats.warriorStats, [], "Warrior", 0, 1)
    elif player_class == "mage":
        player = playerStats.Hero(name, [], playerStats.mageStats, [], "Mage", 0, 1)
    elif player_class == "thief":
        player = playerStats.Hero(name, [], playerStats.thiefStats, [], "Thief", 0, 1)
    else:
        messagebox.showinfo("Error", "Invalid class selection. Please choose Warrior, Mage, or Thief.")
        return

    # After character creation, start the game
    start_game()

def start_game():
    global current_room
    current_room = rooms.rooms_dict[1]

    # Destroy character creation widgets and start the game UI
    for widget in root.winfo_children():
        widget.destroy()

    # Create the text box for displaying room descriptions and game messages
    text_box = tk.Text(root, width=60, height=15, wrap=tk.WORD)
    text_box.pack(pady=10)

    # Create the input box for user commands
    input_box = tk.Entry(root, width=40)
    input_box.pack(pady=10)
    input_box.bind("<Return>", lambda event: process_command(input_box, text_box))

    # Create a label for instructions
    command_label = tk.Label(root, text="Type your command and press Enter")
    command_label.pack(pady=5)

    # Create a frame for the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Add a "Save Game" button
    save_button = tk.Button(button_frame, text="Save Game", command=save_game)
    save_button.grid(row=0, column=0, padx=5)

    # Add an "Open Inventory" button
    inventory_button = tk.Button(button_frame, text="Open Inventory", command=lambda: update_text(player.lookInventory(), text_box, input_box))
    inventory_button.grid(row=0, column=1, padx=5)

    # Add a "Main Menu" button
    main_menu_button = tk.Button(button_frame, text="Main Menu", command=show_menu)
    main_menu_button.grid(row=0, column=2, padx=5)

    # Display the current room description
    update_text(current_room.entryDescription, text_box, input_box)

def load_game():
    global player, current_room, text_box
    
    player = playerStats.Hero.load("save_game.json")
    if player:
        current_room = rooms.rooms_dict[player.current_room]

        # Destroy the initial menu screen widgets and create the game screen
        for widget in root.winfo_children():
            widget.destroy()

        text_box = tk.Text(root, width=60, height=15, wrap=tk.WORD)
        text_box.pack(pady=10)

        input_box = tk.Entry(root, width=40)
        input_box.pack(pady=10)
        input_box.bind("<Return>", lambda event: process_command(input_box, text_box))

        command_label = tk.Label(root, text="Type your command and press Enter")
        command_label.pack(pady=5)

        update_text(current_room.entryDescription, text_box)

def save_game():
    if player:
        player.save("save_game.json")

def process_command(input_box, text_box):
    global is_scrolling, current_room

    # If text is still scrolling, skip the scrolling and show full message
    if is_scrolling:
        skip_scrolling(text_box, input_box)
        return

    command = input_box.get().lower()
    input_box.delete(0, tk.END)  # Clear the input after command

    # Get the result from the textParser (the new room description or message)
    output = textParser.parse_input(command, player, current_room)

    if isinstance(output, str):  # Check if the output is a string (room description or message)
        if "You cannot go" not in output:  # This check assumes "go" is only for movement
            new_room_index = current_room.possibleDirections.get(command.split()[-1])
            if new_room_index:  # Update the global current_room if there's a valid new room
                current_room = rooms.rooms_dict[new_room_index]
        update_text(output, text_box, input_box)
    else:
        # If output is not a string, handle it (though it should always be a string after the fix)
        update_text("Unknown command result.", text_box, input_box)




# Add a flag to track if text is currently being scrolled
is_scrolling = False
scrolling_message = ""

def update_text(message, text_box, input_box):
    global is_scrolling, scrolling_message

    # Clear the text box and disable it to prevent any interaction while scrolling
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.config(state=tk.DISABLED)

    # Set scrolling flag to True and store the message
    is_scrolling = True
    scrolling_message = message

    # Call the helper function to display text character by character
    display_text(message, 0, text_box, input_box)

def display_text(message, index, text_box, input_box):
    global is_scrolling

    if not is_scrolling:  # Prevent re-displaying text if already skipped
        return

    text_box.config(state=tk.NORMAL)  # Allow inserting characters

    if index < len(message):
        # Insert the next character
        text_box.insert(tk.END, message[index])
        # Re-disable text box to prevent interaction
        text_box.config(state=tk.DISABLED)
        # Schedule the next character after a short delay
        text_box.after(25, display_text, message, index + 1, text_box, input_box)
    else:
        # Once done, make the text box fully read-only and enable the input box again
        text_box.config(state=tk.DISABLED)
        input_box.config(state=tk.NORMAL)
        is_scrolling = False

def skip_scrolling(text_box, input_box):
    global is_scrolling, scrolling_message

    if is_scrolling:
        # If text is still scrolling, instantly print the entire message
        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)  # Clear the box before printing full text
        text_box.insert(tk.END, scrolling_message)  # Show full message
        text_box.config(state=tk.DISABLED)  # Re-disable text box
        input_box.config(state=tk.NORMAL)  # Enable input box for commands
        is_scrolling = False  # Set the scrolling flag to False


def show_menu():
    global name_entry, class_entry

    for widget in root.winfo_children():
        widget.destroy()

    menu_frame = tk.Frame(root)
    menu_frame.pack()

    tk.Label(menu_frame, text="Welcome to redactoryPG").pack(pady=10)
    tk.Button(menu_frame, text="Start New Game", command=start_new_game).pack(pady=10)
    tk.Button(menu_frame, text="Load Game", command=load_game).pack(pady=5)
    tk.Button(menu_frame, text="Exit", command=root.quit).pack(pady=5)

# Create the GUI
root = tk.Tk()
root.title("Text Adventure Game")

# Start by showing the menu
show_menu()
root.mainloop()
