import enemies
import playerStats
import enemyTurn

def battleStart(playerInfo,enemyName):
        while enemyName.stats[4] > 0:
            hpHeadsUp = print(playerInfo.name,":", playerInfo.stats[4],"HP");
            battleUserPrompt = input("What would you like to do? (Attack, Spell, Inventory, Flee): ").capitalize();
            if battleUserPrompt == "Attack":
                print(enemyName.stats[4]);
                damagedEnemyPhys = enemyName.stats[4] - (playerInfo.stats[0]*2)
                print(damagedEnemyPhys);
                enemyName.stats[4] = damagedEnemyPhys;
                print(enemyName.stats[4]);
                if enemyName.stats[4] > 0:
                    enemyTurn.enemyFight(enemyName);
            if battleUserPrompt == "Spell":
                if playerInfo.stats[2] == 0:
                    print("Warrior... I hate to have to be the one to break it to you, but you do not have a knack for the arcane.");
                else:
                    spellBattlePrompt = input("Which Spell will you cast?: ").capitalize();
                    damagedEnemyInt = playerInfo.stats[2]*2 - enemyName.stats[4];
                    if enemyName.stats[4] > 0:
                        enemyTurn.enemyFight(enemyName);
            
            if battleUserPrompt == "Inventory":
                print(playerInfo.inventory)
                selectedItem = input("What item from your inventory would you like to use?: ");
                if selectedItem == '':
                    print("you don't got nothin'");
                else:
                    print("you used the ",);#item);
                    enemyTurn.enemyFight(enemyName);
                
            if battleUserPrompt == "Flee":
                fleeChancePlayer = playerInfo.stats[1]*13
                fleeChanceEnemy = enemyName.stats[1]*13
                
                if fleeChancePlayer > fleeChanceEnemy:
                    print("You ran away successfully!");
                    return;
                else:
                    print("You failed to run away!");
                    enemyTurn.enemyFight(enemyName);