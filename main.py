#rpgModel



import random
import enemies
import rooms
#import enemyTurn
import textParser
import items
import enemySelector
import battleSystem
import playerStats

#640x360 aspect ratio, 320x180, 160x90 and so on

def main():
    init = input("Hello Brave Champion! make your name known: ").capitalize();
    classInspect = input("Now, Brave Champion!, choose your class (Warrior, Mage, Thief): ").lower();
    if classInspect == "warrior":
        playerChar = playerStats.Hero(init, [items.potion], playerStats.warriorStats,[''],'warrior',0);
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
        current_room_index = 1;
        first_run = True
        while True:
            current_room = rooms.rooms_dict[current_room_index];

            if first_run:
                print(current_room.entryDescription)
                first_run = False

            #current_room = rooms.rooms_dict[current_room_index];
            user_input = input("What would you like to do?: ");
            new_room_index = textParser.parse_input(user_input, playerChar, current_room)

            if new_room_index is not None:
                current_room_index = new_room_index
        #print(playerChar);
        #battleSystem.battleStart(playerChar,enemySelector.enemySelect());
    if test1 == "talking":
        talkingStart();

main();