import items
import rooms
import playerStats

def parse_input(user_input,player,current_room):
        # Split the user input into words
        words = user_input.lower().strip().split()

        # Remove common articles from the input
        articles = {"the", "a", "an","at","to"}
        words = [word for word in words if word not in articles]

        if len(words) == 1:
            command = words[0]
            if command == "inventory":
                player.lookInventory()
        
        # Check for valid commands and execute the corresponding action
        elif len(words) >= 2:
            command, target = words[0], " ".join(words[1:])

            if command == "go":
                # Check if the direction is valid for the current room
                if target in current_room.possibleDirections:
                # Update the current_room_index based on the transition mapping
                    return current_room.possibleDirections[target]
                else:
                    print(f"You cannot go {target} from here.")
                    # \/ keep an eye on this...
                    return current_room.index;
                
            elif command == "take":
                #take(target)
                print('h');
            
            elif command == "use":
                #next is "finding 1st item that matches";
                #reads as: the first item in your inventory that matches the item you're calling in the chat box gets used, IF it can be, otherwise nothing happens.
                item_to_use = next((i for i in player.inventory if i.name.lower() == target), None);
                if item_to_use:
                    item_to_use.use(player)
                else:
                    print(f"You don't have a {target}.")
            
            elif command == "look" and target == "inventory":
                player.lookInventory()
            
            elif command == "look" and target == "inventory":
                player.lookInventory()

            elif command == "look":
                item_to_look = current_room.findItem(target);
                if item_to_look:
                    print(item_to_look.description);
                else:
                    print("there is nothing, by your description, to look at.");
            
            else:
                print("I do not believe you can do such a thing...");
        else:
            print("Please enter a valid command.")
