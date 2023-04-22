import json

lootTable = [];
#lastLevel = [];

# stats according to index are [str, dex, int, lck, hp, mp, resil]
warriorStats = [5, 1, 0, 2, 19, 0, 7]
mageStats = [1, 3, 5, 1, 14, 15, 2]
thiefStats = [3, 5, 2, 4, 15, 17, 4]

class Hero:
    def __init__(self, name, inventory, stats, spells, player_class, xp):
        self.name = name
        self.inventory = inventory
        self.stats = stats
        self.spells = spells
        self.player_class = player_class;
        self.xp = xp
        self.level = 1  # Add a level attribute
        self.equipped_items = {
            "head": None,
            "torso": None,
            "legs":None,
            "footwear":None,
            "hands":None,
            "weaponRight":None,
            "weaponLeft":None
        }
    
    def lookInventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print(item)

    def equip(self, item):
        item_type = item.item_type
        #if the item you are trying to equpid is not a valid slot type, (head, torso etc), you cannot equip it, else...
        if item_type not in self.equipped_items:
            print(f"You cannot equip the {item.name}.");
    
        #this is an already equpped item
        old_item = self.equipped_items[item_type]
        if old_item:
            #probably remove this line later for brevity sakes.
            print(f"Unequipping {old_item.name}.")
            self.unequip(old_item)

        print(f"Equipping {item.name}.")
        self.equipped_items[item_type] = item
        self.apply_stat_effects(item.stat_effects)

    def unequip(self, item):
        item_type = item.item_type
        if self.equipped_items[item_type] != item:
            print(f"{item.name} is not currently equipped.")
            return

        print(f"Unequipping {item.name}.")
        self.equipped_items[item_type] = None
        self.remove_stat_effects(item.stat_effects)

    def apply_stat_effects(self, stat_effects):
        for stat, effect in stat_effects.items():
            self.stats[stat] += effect

    def remove_stat_effects(self, stat_effects):
        for stat, effect in stat_effects.items():
            self.stats[stat] -= effect

    def gain_experience(self, exp_points):
        self.xp += exp_points
        print(f"{self.name} gained {exp_points} xp.")

        # Check if the player has enough experience to level up
        while self.xp >= self.exp_to_next_level():
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.exp_to_next_level()
        print(f"{self.name} has reached level {self.level}!")

        if self.player_class == "warrior":
            self.stats[0] += 5  # Increase strength
            self.stats[1] += 2  # Increase dexterity
            self.stats[2] += 1  # Increase intelligence
            self.stats[4] += 10 # Increase HP
            self.stats[5] += 0  # Increase MP
            self.stats[6] += 7  # Increase Resillience
        elif self.player_class == "mage":
            self.stats[0] += 1  # Increase strength
            self.stats[1] += 2  # Increase dexterity
            self.stats[2] += 4  # Increase intelligence
            self.stats[4] += 5  # Increase HP
            self.stats[5] += 10  # Increase MP
            self.stats[6] += 3  # Increase Resillience
        elif self.player_class == "thief":
            self.stats[0] += 2  # Increase strength
            self.stats[1] += 4  # Increase dexterity
            self.stats[2] += 1  # Increase intelligence
            self.stats[4] += 7  # Increase HP
            self.stats[5] += 5  # Increase MP
            self.stats[6] += 5  # Increase Resillience

    def exp_to_next_level(self):
        return 112 * self.level
    
    #converts 'Hero' to a dictionary that can be serialized as JSON
    def to_dict(self):
        return {
            "name": self.name,
            "inventory": self.inventory,
            "stats": self.stats,
            "spells": self.spells,
            "xp": self.xp,
            "level": self.level,
            "player_class": self.player_class,
        }

    #creates new 'Hero' object from a dictionary containing the JSON data
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["inventory"],
            data["stats"],
            data["spells"],
            data["xp"],
            data["player_class"],
        )

    #writes the JSON-serializable dictionary to a file using 'json.dump' function
    def save(self, filename):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file)
        print(f"Game saved to {filename}")

    #reads the JSON data from the file using 'json.load' function and creates a new 'Hero' object using 'from.dict'
    @classmethod
    def load(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        hero = cls.from_dict(data)
        print(f"Game loaded from {filename}")
        return hero

# Example usage

# This will trigger a level-up
# player.gain_experience(200)
