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
import tkinter.font as tkFont
import json

#640x360 aspect ratio, 320x180, 160x90 and so on

# Define global variables for player and current room
player = None
current_room = None
name_entry = None
class_entry = None

# Function to start a new game and create the UI for character creation
def start_new_game():
    for widget in root.winfo_children():
        widget.destroy()

    # Character creation screen
    character_creation_frame = tk.Frame(root, bg='#0d0d0d')
    character_creation_frame.pack(fill=tk.BOTH, expand=True)

    # Entry for player name
    tk.Label(character_creation_frame, text="Enter your name:", fg='#2a9772', bg='#0d0d0d', font=custom_font).pack(pady=10)
    global name_entry
    name_entry = tk.Entry(character_creation_frame, width=40, font=custom_font, bg='#333333', fg='#2a9772')
    name_entry.pack(pady=5)

    # Entry for player class
    tk.Label(character_creation_frame, text="Choose your class (Warrior, Mage, Thief):", fg='#2a9772', bg='#0d0d0d', font=custom_font).pack(pady=10)
    global class_entry
    class_entry = tk.Entry(character_creation_frame, width=40, font=custom_font, bg='#333333', fg='#2a9772')
    class_entry.pack(pady=5)

    # Button to confirm and create the character
    button_frame = tk.Frame(character_creation_frame, bg='#0d0d0d')
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Create Character", command=create_character, fg='#2a9772', bg='#0d0d0d',
              activebackground='#333333', activeforeground='#2a9772', highlightthickness=0, font=custom_font).pack()

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

    # Set the background color for the main frame
    main_frame = tk.Frame(root, bg='#0d0d0d')
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Create the text box for displaying room descriptions and game messages
    text_box = tk.Text(main_frame, width=80, height=15, wrap=tk.WORD, bg='#0d0d0d', fg='#2a9772', 
                       font=custom_font, insertbackground='#2a9772')
    text_box.pack(pady=10, fill=tk.BOTH, expand=True)

    # Create a frame for the input and buttons
    bottom_frame = tk.Frame(main_frame, bg='#0d0d0d')
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # Create the input box for user commands, spanning the width
    input_box = tk.Entry(bottom_frame, width=40, bg='#333333', fg='#2a9772', font=custom_font, insertbackground='#2a9772')
    input_box.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
    input_box.bind("<Return>", lambda event: process_command(input_box, text_box))

    # Create a frame for the buttons
    button_frame = tk.Frame(bottom_frame, bg='#0d0d0d')
    button_frame.pack(side=tk.BOTTOM, pady=5)

    # Add buttons with updated styling
    save_button = tk.Button(button_frame, text="Save Game", command=save_game, fg='#2a9772', bg='#0d0d0d', 
                            activebackground='#333333', activeforeground='#2a9772', highlightthickness=0, font=custom_font)
    save_button.pack(side=tk.LEFT, padx=5)

    # Inventory button that toggles between showing the inventory and returning to the game
    inventory_button = tk.Button(button_frame, text="Open Inventory", 
                                 command=lambda: toggle_inventory(text_box, input_box, inventory_button), 
                                 fg='#2a9772', bg='#0d0d0d', activebackground='#333333', 
                                 activeforeground='#2a9772', highlightthickness=0, font=custom_font)
    inventory_button.pack(side=tk.LEFT, padx=5)

    main_menu_button = tk.Button(button_frame, text="Main Menu", command=show_menu, fg='#2a9772', bg='#0d0d0d', 
                                 activebackground='#333333', activeforeground='#2a9772', highlightthickness=0, font=custom_font)
    main_menu_button.pack(side=tk.LEFT, padx=5)

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

    command = input_box.get().lower().strip()  # Strip spaces and get the command
    input_box.delete(0, tk.END)  # Clear the input after command

    # Ensure that command is not empty before proceeding
    if not command:
        return  # Do nothing if the command is empty

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

def toggle_inventory(text_box, input_box, button):
    global last_displayed_text, is_scrolling

    # Stop any ongoing scrolling before switching views
    if is_scrolling:
        skip_scrolling(text_box, input_box)

    if button["text"] == "Open Inventory":
        # Save the full message that was being displayed before showing the inventory
        last_displayed_text = text_box.get(1.0, tk.END)
        # Immediately show the inventory without scrolling
        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)  # Clear the text box
        text_box.insert(tk.END, player.lookInventory())  # Insert inventory text directly
        text_box.config(state=tk.DISABLED)
        # Change the button text to "Return to Game"
        button.config(text="Return to Game")
    else:
        # Restore the full last displayed game message (even if it was mid-scroll)
        update_text(last_displayed_text, text_box, input_box)
        # Change the button text back to "Open Inventory"
        button.config(text="Open Inventory")

def update_text(message, text_box, input_box):
    global is_scrolling, scrolling_message

    # Stop scrolling if we are switching views or showing the inventory
    if is_scrolling:
        skip_scrolling(text_box, input_box)

    # Clear the text box and disable it to prevent any interaction while scrolling
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.config(state=tk.DISABLED)

    # Set scrolling flag to True and store the full message
    is_scrolling = True
    scrolling_message = message

    # Call the helper function to display text character by character
    display_text(message, 0, text_box, input_box)

def display_text(message, index, text_box, input_box):
    global is_scrolling

    if not is_scrolling:
        return

    text_box.config(state=tk.NORMAL)

    if index < len(message):
        # Insert the next character
        text_box.insert(tk.END, message[index])
        # Re-disable text box to prevent interaction
        text_box.config(state=tk.DISABLED)
        # Schedule the next character after a short delay
        text_box.after(25, display_text, message, index + 1, text_box, input_box)
    else:
        # Once done, stop scrolling and make the text box read-only again
        text_box.config(state=tk.DISABLED)
        input_box.config(state=tk.NORMAL)
        is_scrolling = False

def skip_scrolling(text_box, input_box):
    global is_scrolling, scrolling_message

    if is_scrolling:
        # If text is still scrolling, instantly show the entire message
        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)  # Clear the box before printing full text
        text_box.insert(tk.END, scrolling_message)  # Show full message
        text_box.config(state=tk.DISABLED)  # Re-disable text box
        input_box.config(state=tk.NORMAL)  # Enable input box for commands
        is_scrolling = False  # Set the scrolling flag to False

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

    # Set up menu frame with the updated background color
    menu_frame = tk.Frame(root, bg='#0d0d0d')
    menu_frame.pack(fill=tk.BOTH, expand=True)

    # Set up the title label with the new font and colors
    tk.Label(menu_frame, text="Welcome to redactoryPG", fg='#2a9772', bg='#0d0d0d', font=custom_font).pack(pady=10)

    # Create the buttons with updated styles
    tk.Button(menu_frame, text="Start New Game", command=start_new_game, fg='#2a9772', bg='#0d0d0d', 
              activebackground='#333333', activeforeground='#2a9772', highlightthickness=0, font=custom_font).pack(pady=10)

    tk.Button(menu_frame, text="Load Game", command=load_game, fg='#2a9772', bg='#0d0d0d', 
              activebackground='#333333', activeforeground='#2a9772', highlightthickness=0, font=custom_font).pack(pady=5)

    tk.Button(menu_frame, text="Exit", command=root.quit, fg='#2a9772', bg='#0d0d0d', 
              activebackground='#333333', activeforeground='#2a9772', highlightthickness=0, font=custom_font).pack(pady=5)


# Create the GUI
root = tk.Tk()
root.title("Text Adventure Game")

# this changes the background color
root.config(bg='#2e2e2e')

root.geometry("640x360")
root.minsize(400, 420)  # Enforce a minimum window size

custom_font = tkFont.Font(family="Fixedsys", size=12)

# Start by showing the menu
show_menu()
root.mainloop()