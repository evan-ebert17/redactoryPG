import items
import rooms
import playerStats

def parse_input(user_input, player, current_room):
    # Initialize output variable
    output = ""

    # Split the user input into words
    words = user_input.lower().strip().split()

    # Remove common articles from the input
    articles = {"the", "a", "an", "at", "to"}
    words = [word for word in words if word not in articles]

    if len(words) == 1:
        command = words[0]
        if command == "inventory":
            output += player.lookInventory()  # 

    # Check for valid commands and execute the corresponding action
    elif len(words) >= 2:
        command, target = words[0], " ".join(words[1:])

        if command == "go":
            if target in current_room.possibleDirections:
                # Get the new room index from the direction and update current_room
                new_room_index = current_room.possibleDirections[target]
                current_room = rooms.rooms_dict[new_room_index]  # Update the room
                return current_room.entryDescription  # Return the description of the new room
            else:
                output += f"You cannot go {target} from here.\n"
                return current_room.index
        
        elif command == "take" or command == "get":
            item_to_take = next((i for i in current_room.items if i.name.lower() == target), None)
            if item_to_take:
                output += f"You took the {target.capitalize()}.\n"
                player.inventory.insert(0, item_to_take)
                current_room.items.remove(item_to_take)
            else:
                output += f"There is no {target} to take.\n"
        
        elif command == "use":
            item_to_use = next((i for i in player.inventory if i.name.lower() == target), None)
            if item_to_use:
                item_to_use.use(player)
            else:
                output += f"You don't have a {target}.\n"
        
        elif command == "look" and target == "room":
            output += current_room.specificDescription + "\n"
        
        elif command == "look" and target == "inventory":
            output += player.lookInventory()  # Assuming lookInventory returns output
        
        elif command == "look":
            item_to_look = current_room.findItem(target)
            if item_to_look:
                output += item_to_look.description + "\n"
            else:
                output += "There is nothing, by your description, to look at.\n"
        
        else:
            output += "I do not believe you can do such a thing...\n"
    else:
        output += "Please enter a valid command.\n"

    return output
