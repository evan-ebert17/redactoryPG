lootTable = [];
lastLevel = [];

#stats according to index are [str, dex, int, lck, hp, mp, resil]

warriorStats = [5,1,0,2,19,0,7];
mageStats = [1,3,5,1,14,15,2];
thiefStats = [3,5,2,4,15,17,4];
 
class Hero:
    def __init__(self, name, inventory, stats, spells,xp):
        self.name = name;
        self.inventory = inventory;
        self.stats = stats;
        self.spells = spells;
        self.xp = xp;

#class FighterType:
   # def __init__(self,warrior,mage,theif):
        #stats according to index are [str, dex, int, lck, hp, mp, resil]
        #self.warrior = [