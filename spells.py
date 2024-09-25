import random

class Spell:
    def __init__(self, name, damage_type, base_damage, effect=None):
        self.name = name
        self.damage_type = damage_type  # e.g., "fire", "ice", "poison"
        self.base_damage = base_damage  # Base damage dealt by the spell
        self.effect = effect  # Optional additional effects (burn, freeze, poison, etc.)

    def cast(self, caster, target):
        """Casts the spell from the caster (hero/enemy) to the target."""
        damage = self.base_damage
        # Apply caster's intelligence to boost spell damage
        if hasattr(caster, 'stats') and "int" in caster.stats:
            damage += caster.stats["int"]

        # Check for target's resistances
        if hasattr(target, 'stats') and self.damage_type in target.stats[-1]:
            damage = int(damage * 0.5)  # Half damage if resistant

        # Apply the damage
        target.stats["hp"] -= damage
        result = f"{caster.name} casts {self.name} on {target.name}, dealing {damage} {self.damage_type} damage!"

        # Apply any special effects
        if self.effect:
            result += f" {target.name} is affected by {self.effect}!"
        
        return result

# Example spells
fireball = Spell("Fireball", "fire", base_damage=10, effect="burn")
ice_shard = Spell("Ice Shard", "ice", base_damage=8, effect="freeze")
poison_blast = Spell("Poison Blast", "poison", base_damage=7, effect="poison")

# Add more spells for both heroes and enemies to use
