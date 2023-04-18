#rpgModel

import random
import enemies
import rooms
#import enemyTurn
import battleSystem
import playerStats

def main():
    init = input("Hello Brave Champion! make your name known: ").capitalize();
    classInspect = input("Now, Brave Champion!, choose your class (Warrior, Mage, Thief): ").lower();
    if classInspect == "warrior":
        playerChar = playerStats.Hero(init, [], playerStats.warriorStats,[''],'warrior',0);
    if classInspect == "mage":
        playerChar = playerStats.Hero(init, [], playerStats.mageStats,['Firebolt','Heal'],'mage',0);
    #,'Icebolt','Aegis','Smogon','Draconic Breath' other spells to learn as you level up
    if classInspect == "thief":
        playerChar = playerStats.Hero(init, [], playerStats.thiefStats,['Shadowsneak','Shadowstep'],'thief',0);
    # , 'Shadowform Bow' - other spells to learnas you level up

    print();

    #enemySelect went here
        
    def talkingStart():
        print("hello!");
    
    test1 = input("Explore or sim talking: ").lower();
    if test1 == "explore":
        print(rooms.TempleRoom1.description);
        print(playerChar);
        #battleSystem.battleStart(playerChar,enemySelect());
    if test1 == "talking":
        talkingStart();

main();