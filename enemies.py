#enemy storage

import random

class Enemy:
    def  __init__(self, name, lootTable,min_damage, max_damage,stats, spellCache):
        self.name = name;
        self.lootTable = lootTable;
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.stats = stats;
        self.spellCache = spellCache;
    
    #just takes the min_damage as the lowest integer and the max_damage as the highest and generates numbers based on that
    def random_damage(self):
        return random.randint(self.min_damage, self.max_damage)

# enemy details are as follows ("Name", [gold drop, loot-table], [stat table.[resistances]],[spell list]);
# stat table reads as [str, dex, int, lck, hp, mp, resil];
# str corresponds to physical damage, int is magical dmg, lck is crit chance, hp, mp, resil is any bonus resistances (such as fire for dragons);  

slime = Enemy("Slime",[random.randint(2,5),"Sludge","Rusted Armor"],2,4,[5,5,2,15,5,["water","poison"]],["Acid Spray"])

gob = Enemy("Goblin",[random.randint(2,7),"Leather Scrap","Dagger"],4,8,[3,2,1,1,23,5,["poison"]],["Intimidating Leer (def down + 1 speed down)","Poison Gack (+1 dmg + 33% chance to poision)"]);

ogre = Enemy("Ogre",[random.randint(13,37),"Giant Club","Bile"],12,18,[1,1,2,55,8,["water"]],["Polyphemus Rage (atk up)","Earthen Drag (phys dmg + AOE (if party))","Bile (hacks up... somethin' and lowers speed by 2"]);

drag = Enemy("Draygern",[random.randint(250,500),"Dragon Scale","Glistening Eyeball"],37,50,[10,15,4,125,50,["poison","fire","water","frost"]],["Flame Boro (special dmg boro breath)","Scalapsular Crush (phys hardened tail slam)","Draconic Fortification (def + spdef up)","Blue Flame (heal)"]);

thief = Enemy("Thief",[random.randint(10,25),"Serrated Dagger","Smokebomb"],7,12,[8,7,6,27,25,["lightning"]],["Shadowsneak (evaision up, speed down)","Shadowstep (speed up but slight dmg down)","Shadowform Bow (special dmg bow, slight piercing dmg)"]);

#water elemental WoW
elemental = Enemy("Elemental",[random.randint(30,75),"Elemental Crystal","Crushed Powder"],5,20,[6,12,2,45,49,["poison","water"]],["Frozen Shackle (speed way down + frost dmg)","Water Spear (physical dmg)"]);

#think wall-masters from LoZ
grabbler = Enemy("Grabbler",[random.randint(25,45),"Fingernail","Runic Inscription","Pair of Keys"],10,19,[6,12,2,45,49,["water"]],["Paralyzing Grip","Nail Shot","Taunt (wags its finger at you)"]);