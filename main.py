#rpgModel

import random
import enemies
#import enemyTurn
import battleSystem
import playerStats

def main():
    init = input("Hello Brave Champion! make your name known: ").capitalize();
    classInspect = input("Now, Brave Champion!, choose your class (Warrior, Mage, Thief): ").capitalize();
    if classInspect == "Warrior":
        playerChar = playerStats.Hero(init, [], playerStats.warriorStats,['b'],0);
    if classInspect == "Mage":
        playerChar = playerStats.Hero(init, [], playerStats.mageStats,['Firebolt','Heal'],0);
    #,'Icebolt','Aegis','Smogon','Draconic Breath' other spells to learn as you level up
    if classInspect == "Thief":
        playerChar = playerStats.Hero(init, [], playerStats.thiefStats,['Shadowsneak','Shadowstep'],0);
    # , 'Shadowform Bow' - other spells to learnas you level up

    print(playerChar.name, playerChar.inventory, playerChar.stats);

    def enemySelect():
    #depending on terrain + location determine what enemy you encounter (add later)
        whatEnemy = random.randint(1,100)
        print(whatEnemy);
        if whatEnemy >= 85:
            print("you encountered a",enemies.drag.name,"!\n");
            return enemies.drag
        if whatEnemy < 85  and whatEnemy >= 70:
            print("you encountered a",enemies.ogre.name,"!\n");
            return enemies.ogre
        if whatEnemy < 70 and whatEnemy >= 55:
            print("you encountered a",enemies.elemental.name,"!\n");
            return enemies.elemental
        if whatEnemy < 55 and whatEnemy >=35:
            print("you encountered a",enemies.thief.name,"!\n");
            return enemies.thief
        if whatEnemy < 35:
            print("you encountered a",enemies.gob.name,"!\n");
            return enemies.gob
        
    def talkingStart():
        print("hello!");
    
    test1 = input("Explore or sim talking: ").capitalize();
    if test1 == "Explore":
        battleSystem.battleStart(playerChar,enemySelect());
    if test1 == "Talking":
        talkingStart();

main();