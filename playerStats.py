import json

lootTable = []
# lastLevel = []

# stats according to index are [str, dex, int, lck, hp, mp, resil]
warriorStats = [5, 1, 0, 2, 19, 0, 7]
mageStats = [1, 3, 5, 1, 14, 15, 2]
thiefStats = [3, 5, 2, 4, 15, 17, 4]

class Hero:
    def __init__(self, name, inventory, stats, spells, player_class, xp, current_room=None):
        self.name = name
        self.inventory = inventory
        self.stats = stats
        self.spells = spells
        self.player_class = player_class
        self.xp = xp
        self.level = 1  # Add a level attribute
        self.current_room = current_room
        self.equipped_items = {
            "head": None,
            "torso": None,
            "legs": None,
            "footwear": None,
            "hands": None,
            "weaponRight": None,
            "weaponLeft": None
        }

    def lookInventory(self):
        # Return inventory as a string
        inventory_output = "Inventory:\n"
        for item in self.inventory:
            inventory_output += f"{item}\n"
        return inventory_output.strip()

    def equip(self, item):
        output = ""

        item_type = item.item_type
        # If the item type is invalid
        if item_type not in self.equipped_items:
            output += f"You cannot equip the {item.name}.\n"
            return output

        # If there's an old item equipped, unequip it
        old_item = self.equipped_items[item_type]
        if old_item:
            output += f"Unequipping {old_item.name}.\n"
            self.unequip(old_item)

        output += f"Equipping {item.name}.\n"
        self.equipped_items[item_type] = item
        self.apply_stat_effects(item.stat_effects)
        
        return output

    def unequip(self, item):
        item_type = item.item_type
        if self.equipped_items[item_type] != item:
            return f"{item.name} is not currently equipped."

        self.equipped_items[item_type] = None
        self.remove_stat_effects(item.stat_effects)
        return f"Unequipping {item.name}."

    def apply_stat_effects(self, stat_effects):
        for stat, effect in stat_effects.items():
            self.stats[stat] += effect

    def remove_stat_effects(self, stat_effects):
        for stat, effect in stat_effects.items():
            self.stats[stat] -= effect

    def gain_experience(self, exp_points):
        output = f"{self.name} gained {exp_points} xp.\n"
        self.xp += exp_points

        # Check if the player has enough experience to level up
        while self.xp >= self.exp_to_next_level():
            output += self.level_up()
        
        return output

    def level_up(self):
        self.level += 1
        self.xp -= self.exp_to_next_level()
        output = f"{self.name} has reached level {self.level}!\n"

        # Increase stats based on player class
        if self.player_class == "warrior":
            self.stats[0] += 5  # Increase strength
            self.stats[1] += 2  # Increase dexterity
            self.stats[2] += 1  # Increase intelligence
            self.stats[4] += 10  # Increase HP
            self.stats[5] += 0  # Increase MP
            self.stats[6] += 7  # Increase Resilience
        elif self.player_class == "mage":
            self.stats[0] += 1  # Increase strength
            self.stats[1] += 2  # Increase dexterity
            self.stats[2] += 4  # Increase intelligence
            self.stats[4] += 5  # Increase HP
            self.stats[5] += 10  # Increase MP
            self.stats[6] += 3  # Increase Resilience
        elif self.player_class == "thief":
            self.stats[0] += 2  # Increase strength
            self.stats[1] += 4  # Increase dexterity
            self.stats[2] += 1  # Increase intelligence
            self.stats[4] += 7  # Increase HP
            self.stats[5] += 5  # Increase MP
            self.stats[6] += 5  # Increase Resilience

        return output

    def exp_to_next_level(self):
        return 112 * self.level

    def save(self, filename):
        save_data = {
            "name": self.name,
            "inventory": self.inventory,
            "stats": self.stats,
            "spells": self.spells,
            "player_class": self.player_class,
            "xp": self.xp,
            "level": self.level,
            "equipped_items": self.equipped_items,
            "current_room": self.current_room
        }
        with open(filename, 'w') as file:
            json.dump(save_data, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return cls(
                name=data["name"],
                inventory=data["inventory"],
                stats=data["stats"],
                spells=data["spells"],
                player_class=data["player_class"],
                xp=data["xp"],
                current_room=data["current_room"]
            )
