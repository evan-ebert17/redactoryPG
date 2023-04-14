#enemy storage

import random

class Enemy:
    def  __init__(self, name, lootTable, stats, spellCache):
        self.name = name;
        self.lootTable = lootTable;
        self.stats = stats;
        self.spellCache = spellCache;

# enemy details are as follows ("Name", [gold drop, loot-table], [stat table],[spell list]);
# stat table reads as [str, dex, int, lck, hp, mp, resil];
# str corresponds to physical damage, int is magical dmg, lck is crit chance, hp, mp, resil is any bonus resistances (such as flame for dragons);  

slime = Enemy("Slime",[random.randint(2,5),"Sludge","Rusted Armor"],[random.randint(2,4),5,5,2,15,5,["water","poison"]],["Acid Spray"])

gob = Enemy("Goblin",[random.randint(2,7),"Leather Scrap","Dagger"],[random.randint(4,8),3,1,2,23,5,["poison"]],["Intimidating Leer (def down + 1 speed down)","Poison Gack (+1 dmg + 33% chance to poision)"]);

ogre = Enemy("Ogre",[random.randint(13,37),"Giant Club","Bile"],[random.randint(12,18),1,1,2,55,8,["water"]],["Polyphemus Rage (atk up)","Earthen Drag (phys dmg + AOE (if party))","Bile (hacks up... somethin' and lowers speed by 2"]);

drag = Enemy("Draygern",[random.randint(250,500),"Dragon Scale","Glistening Eyeball"],[random.randint(37,50),10,15,4,125,50,["poison","fire","water","frost"]],["Flame Boro (special dmg boro breath)","Scalapsular Crush (phys hardened tail slam)","Draconic Fortification (def + spdef up)","Blue Flame (heal)"]);

thief = Enemy("Thief",[random.randint(10,25),"Serrated Dagger","Smokebomb"],[random.randint(7,12),8,7,6,27,25,["lightning"]],["Shadowsneak (evaision up, speed down)","Shadowstep (speed up but slight dmg down)","Shadowform Bow (special dmg bow, slight piercing dmg)"]);

elemental = Enemy("Elemental",[random.randint(30,75),"Elemental Crystal","Crushed Powder"],[random.randint(5,20),6,12,2,45,49,["poison","water"]],["Frozen Shackle (speed way down + frost dmg)","Water Spear (physical dmg)"]);
