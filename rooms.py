class Room:
    def __init__(self, name, index,items, commands, description,specialQual):
        self.name = name;
        self.index = index;
        self.items = items;
        self.commands = commands;
        self.description = description;
        self.specialQual = specialQual;

TempleRoom1 = Room("forest",1,["Rock","Rusted Sword","Dagger","Wooden Staff","Backpack","Minor Health Potion"],["look","look at","inspect","take","pick up","north"],
             "As your eyes begin to open and your senses come about you, you find yourself in an abandoned stone Temple. "
             "Its walls cracked and its ceilings collapsed in many places, the once-majestic structure now lies in ruin. "
             "It's as if time has stood still in this abandoned temple, as now the scent of decay and mustiness permeates the air. " 
             "The only source of light shimmers down as weak rays of sunshine filtering through the broken ceiling, casting a dusty glow on the crumbling stone pillars. "
             "It is hard to imagine a place, as grand as this, is all but helpless against the elements.",
             'spawnPoint');