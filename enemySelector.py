import enemies
import random

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