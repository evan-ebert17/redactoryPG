def parse_input(user_input):
    # Split the user input into words
    words = user_input.lower().strip().split()

    # Remove common articles from the input
    articles = {"the", "a", "an"}
    words = [word for word in words if word not in articles]

    # Check for valid commands and execute the corresponding action
    if len(words) >= 2:
        command, target = words[0], " ".join(words[1:])
        
        if command == "go":
            go(target)
        elif command == "take":
            take(target)
        elif command == "use":
            use(target)
        elif command == "look":
            look(target)
        else:
            print("I don't understand that command.")
    else:
        print("Please enter a valid command.")
