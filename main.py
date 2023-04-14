#rpgModel

import random
import enemies

lootTable = []

#stats according to index are [str, dex, int, lck, hp, mp, resil]

warriorStats = [5,1,0,2,19,0,7];
mageStats = [1,3,5,1,5,15,2];
thiefStats = [3,5,2,4,4,17,4];
 
class Hero:
    def __init__(self, name, inventory, stats, spells):
        self.name = name;
        self.inventory = inventory;
        self.stats = stats;
        self.spells = spells;

#class FighterType:
   # def __init__(self,warrior,mage,theif):
        #stats according to index are [str, dex, int, lck, hp, mp, resil]
        #self.warrior = [

def main():
    init = input("Hello Brave Champion! make your name known: ").capitalize();
    classInspect = input("Now, Brave Champion!, choose your class (Warrior, Mage, Thief): ").capitalize();
    if classInspect == "Warrior":
        playerChar = Hero(init, [], warriorStats,['b']);
    if classInspect == "Mage":
        playerChar = Hero(init, [], mageStats,['Firebolt','Icebolt','Aegis','Heal','Smogon','Draconic Breath']);
    if classInspect == "Thief":
        playerChar = Hero(init, [], thiefStats,['Shadowsneak','Shadowstep','Shadowform Bow']);

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
            
    def battleStart(enemyName):
        while enemyName.health > 0:
            #print(enemyName)
            hpHeadsUp = print(playerChar.name,":", playerChar.stats[4],"HP");
            battleUserPrompt = input("What would you like to do? (Attack, Spell, Inventory, Flee): ").capitalize();
            if battleUserPrompt == "Attack":
                print(enemyName.health);
                damagedEnemyPhys = enemyName.health - (playerChar.stats[0]*2)
                print(damagedEnemyPhys);
                enemyName.health = damagedEnemyPhys;
                print(enemyName.health);
                enemyFight(enemyName);
            if battleUserPrompt == "Spell":
                if playerChar.stats[2] == 0:
                    print("Warrior... I hate to have to be the one to break it to you, but you do not have a knack for the arcane.");
                else:
                    spellBattlePrompt = input("Which Spell will you cast?: ").capitalize();
                    damagedEnemyInt = playerChar.stats[2]*2 - enemyName.health;
                    enemyFight(enemyName);
            
            if battleUserPrompt == "Inventory":
                print(playerChar.inventory)
                selectedItem = input("What item from your inventory would you like to use?: ");
                if selectedItem == '':
                    print("you don't got nothin'");
                else:
                    print("you used the ",);#item);
                    enemyFight(enemyName);
                
            if battleUserPrompt == "Flee":
                fleeChancePlayer = playerChar.stats[1]*13
                fleeChanceEnemy = enemyName.stats[1]*13
                
                if fleeChancePlayer > fleeChanceEnemy:
                    print("You ran away successfully!");
                    return;
                else:
                    print("You failed to run away!");
                    enemyFight(enemyName);

#replace every instance of damage and health with their requisite stats

    def enemyFight(enemy):
        print(enemy.name, "is getting ready to attack!");
        spellChance = random.random();
        print(spellChance);
        enemySpellLen = len(enemy.spellCache);
        if spellChance > 0.3:
            print("The", enemy.name, "attacks! and deals", enemy.damage, "points of physical damage!");
        else:
            print("The", enemy.name, "prepares to cast a spell!");
            #IF YOU HAVENT! make sure to implement an array containing at least one spell named "spellCache" which
            #holds an enemies individual spells
            print("The", enemy.name, "casts", enemy.spellCache[random.randint(0,enemySpellLen)]);
            #if enemy.spellCache[random.randint(0,3) == null or enemy.spellCache[random.randint(0,3) == undefined:
                #castedSpell = enemy.spellCache[0];
                #print("bro")
        
    def talkingStart():
        print("hello!");
    
    test1 = input("Explore or sim talking: ").capitalize();
    if test1 == "Explore":
        battleStart(enemySelect());
    if test1 == "Talking":
        talkingStart();

        

main();






   


