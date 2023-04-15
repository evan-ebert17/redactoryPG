import random
import enemies

def enemyFight(enemy):
        print(enemy.name, "is getting ready to attack!");
        spellChance = random.random();
        print(spellChance);
        enemySpellLen = len(enemy.spellCache);
        if spellChance > 0.3:
            print("The", enemy.name, "attacks! and deals", enemy.stats[0], "points of physical damage!");
        else:
            print("The", enemy.name, "prepares to cast a spell!");
            #IF YOU HAVENT! make sure to implement an array containing at least one spell named "spellCache" which
            #holds an enemies individual spells
            print("The", enemy.name, "casts", enemy.spellCache[random.randint(0,enemySpellLen-1)]);