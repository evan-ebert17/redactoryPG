import random
import enemies
from tkinterMain import update_text

def calculate_damage(attacker, defender, attack_type="physical"):
    if attack_type == "physical":
        damage = random.randint(attacker.stats[0] - 2, attacker.stats[0] + 2)  # Strength-based attack
    elif attack_type == "magical":
        damage = random.randint(attacker.stats[2] - 2, attacker.stats[2] + 2)  # Intelligence-based attack

    final_damage = max(damage - defender.stats[6], 0)  # Defender's resilience reduces damage
    return final_damage

def player_attack(player, enemy, text_box):
    damage = calculate_damage(player, enemy, "physical")
    enemy.stats[4] -= damage
    update_text(f"You attack {enemy.name} for {damage} damage!\n", text_box)
    if enemy.stats[4] <= 0:
        update_text(f"You defeated {enemy.name}!\n", text_box)

def player_cast_spell(player, enemy, text_box):
    if player.stats[2] == 0:
        update_text("You have no magical abilities!\n", text_box)
        return
    spell_name = "Fireball"  # This could be customized later
    damage = calculate_damage(player, enemy, "magical")
    enemy.stats[4] -= damage
    update_text(f"You cast {spell_name} and dealt {damage} damage to {enemy.name}!\n", text_box)
    if enemy.stats[4] <= 0:
        update_text(f"{enemy.name} has been defeated!\n", text_box)

def player_use_item(player, text_box):
    if not player.inventory:
        update_text("Your inventory is empty!\n", text_box)
        return
    item_name = "Health Potion"  # You can expand this logic
    update_text(f"You used {item_name}!\n", text_box)

def enemy_turn(player, enemy, text_box):
    if enemy.stats[4] > 0:
        enemy_attack = calculate_damage(enemy, player, "physical")
        player.stats[4] -= enemy_attack
        update_text(f"The {enemy.name} attacks you for {enemy_attack} damage!\n", text_box)
        if player.stats[4] <= 0:
            update_text(f"You have been defeated by {enemy.name}...\n", text_box)

def attempt_flee(player, enemy, text_box):
    flee_chance_player = random.randint(1, 20) + player.stats[1]
    flee_chance_enemy = random.randint(1, 20) + enemy.stats[1]
    if flee_chance_player > flee_chance_enemy:
        update_text("You successfully fled the battle!\n", text_box)
        return True  # Successfully fled
    else:
        update_text("You failed to flee!\n", text_box)
        return False  # Failed to flee

def battle_start(player, enemy, text_box, input_box):
    """Start a battle between player and enemy."""
    update_text(f"A wild {enemy.name} appeared!\n", text_box)

    def process_battle_command():
        action = input_box.get().capitalize()
        input_box.delete(0, 'end')  # Clear the input after the command

        if action == "Attack":
            player_attack(player, enemy, text_box)
        elif action == "Spell":
            player_cast_spell(player, enemy, text_box)
        elif action == "Inventory":
            player_use_item(player, text_box)
        elif action == "Flee":
            if attempt_flee(player, enemy, text_box):
                return  # End battle if player successfully flees
        else:
            update_text("Invalid action!\n", text_box)

        # Enemy's turn if they are still alive
        if enemy.stats[4] > 0 and player.stats[4] > 0:
            enemy_turn(player, enemy, text_box)

        # After both actions, check for victory or defeat
        if player.stats[4] > 0 and enemy.stats[4] > 0:
            update_text("What will you do next? (Attack, Spell, Inventory, Flee):\n", text_box)
        elif player.stats[4] <= 0:
            update_text("You were defeated!\n", text_box)
        elif enemy.stats[4] <= 0:
            update_text("You won the battle!\n", text_box)

    # The input box needs to be bound to the process battle command
    input_box.bind("<Return>", lambda event: process_battle_command())
    update_text("What will you do? (Attack, Spell, Inventory, Flee):\n", text_box)
