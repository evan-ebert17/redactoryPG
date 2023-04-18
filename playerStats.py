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

# Example usage

# This will trigger a level-up
# player.gain_experience(200)
