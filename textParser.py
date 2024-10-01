import items
import rooms
import playerStats

def parse_input(user_input, player, current_room):
    # Initialize output response with message and room update flag
    response = {
        "message": "",
        "new_room_index": None,  # This will be used to update the room index
        "trigger": None          # This will be used to signal cutscenes or battles
    }

    # Split the user input into words
    words = user_input.lower().strip().split()

    # Remove common articles from the input
    articles = {"the", "a", "an", "at", "to"}
    words = [word for word in words if word not in articles]

    if len(words) == 1:
        command = words[0]
        if command == "inventory":
            response["message"] = player.lookInventory()
            return response

    # Check for valid commands and execute the corresponding action
    elif len(words) >= 2:
        command, target = words[0], " ".join(words[1:])

        if command == "go":
            if target in current_room.possibleDirections:
                # Get the new room index from the direction and add it to the response
                new_room_index = current_room.possibleDirections[target]
                response["new_room_index"] = new_room_index
                response["message"] = rooms.rooms_dict[new_room_index].entryDescription
            else:
                response["message"] = f"You cannot go {target} from here.\n"
        
        elif command == "take" or command == "get":
            item_to_take = next((i for i in current_room.items if i.name.lower() == target), None)
            if item_to_take:
                response["message"] = f"You took the {target.capitalize()}.\n"
                player.inventory.insert(0, item_to_take)
                current_room.items.remove(item_to_take)
            else:
                response["message"] = f"There is no {target} to take.\n"
        
        elif command == "use":
            item_to_use = next((i for i in player.inventory if i.name.lower() == target), None)
            if item_to_use:
                item_to_use.use(player)
            else:
                response["message"] = f"You don't have a {target}.\n"
        
        elif command == "look" and target == "room":
            response["message"] = current_room.specificDescription + "\n"
        
        elif command == "look" and target == "inventory":
            response["message"] = player.lookInventory()
        
        elif command == "look":
            item_to_look = current_room.findItem(target)
            if item_to_look:
                response["message"] = item_to_look.description + "\n"
            else:
                response["message"] = "There is nothing, by your description, to look at.\n"
        
        else:
            response["message"] = "I do not believe you can do such a thing...\n"
    
    else:
        response["message"] = "Please enter a valid command.\n"

    return response
