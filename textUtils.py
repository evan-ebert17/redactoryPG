import tkinter as tk;

# Add a flag to track if text is currently being scrolled
is_scrolling = False
scrolling_message = ""

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
        # If text is still scrolling, instantly print the entire message
        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)  # Clear the box before printing full text
        text_box.insert(tk.END, scrolling_message)  # Show full message
        text_box.config(state=tk.DISABLED)  # Re-disable text box
        input_box.config(state=tk.NORMAL)  # Enable input box for commands
        is_scrolling = False  # Set the scrolling flag to False