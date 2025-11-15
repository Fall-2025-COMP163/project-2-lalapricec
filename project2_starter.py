# COMP 163 - Project 2: Character Abilities Showcase
# Author: Lauren Price
# Description:
# Demonstrates inheritance, method overriding, and unique character abilities.
# Only uses concepts up to the "Inheritance".

# AI Assistance Disclosure:
# I used AI assistance to help me improve code structure, understand functions,
# All final logic and testing were reviewed and verified by me.

# ==========================
# Base Class: Character
# ==========================
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def describe(self):
        return f"{self.name}: Health = {self.health}, Attack = {self.attack_power}"

    def attack(self, other):
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
        other.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")

    def is_alive(self):
        return self.health > 0


# ==========================
# Derived Class: Warrior
# ==========================
class Warrior(Character):
    def __init__(self, name, health, attack_power, weapon):
        super().__init__(name, health, attack_power)
        self.weapon = weapon

    def describe(self):
        base = super().describe()
        return f"{base} | Weapon: {self.weapon}"

    def attack(self, other):
        # Override to add warrior flavor
        print(f"{self.name} swings a {self.weapon} mightily!")
        super().attack(other)

    def special_ability(self, other):
        """Warrior special: Power Strike — deals double damage once"""
        damage = self.attack_power * 2
        print(f"{self.name} uses Power Strike! 💥 Double damage!")
        other.take_damage(damage)


# ==========================
# Derived from Warrior: Knight
# ==========================
class Knight(Warrior):
    def __init__(self, name):
        # Default knight stats
        super().__init__(name, health=120, attack_power=15, weapon="Sword of Valor")
        self.armor = 10

    def take_damage(self, damage):
        # Knights reduce incoming damage by armor value
        reduced = max(damage - self.armor, 0)
        print(f"{self.name}'s armor absorbs {self.armor} damage!")
        super().take_damage(reduced)

    def special_ability(self, other):
        """Knight special: Shield Bash — stuns the enemy (skips next turn)"""
        print(f"{self.name} uses Shield Bash! 🛡️ The enemy is stunned!")
        other.take_damage(self.attack_power // 2)
        print(f"{other.name} is stunned and cannot attack next round!")


# ==========================
# Derived Class: Mage
# ==========================
class Mage(Character):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def describe(self):
        base = super().describe()
        return f"{base} | Mana: {self.mana}"

    def special_ability(self, other):
        """Mage special: Fireball — costs mana and deals heavy magic damage"""
        if self.mana >= 10:
            print(f"{self.name} casts Fireball! 🔥")
            other.take_damage(self.attack_power + 10)
            self.mana -= 10
            print(f"{self.name}'s remaining mana: {self.mana}")
        else:
            print(f"{self.name} tries to cast Fireball, but doesn’t have enough mana!")


# ==========================
# Derived from Mage: Archmage
# ==========================
class Archmage(Mage):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=20, mana=50)

    def special_ability(self, other):
        """Archmage special: Elemental Storm — high mana cost, huge damage"""
        if self.mana >= 25:
            print(f"{self.name} unleashes Elemental Storm! ⚡🌊🔥")
            other.take_damage(self.attack_power + 25)
            self.mana -= 25
            print(f"{self.name}'s remaining mana: {self.mana}")
        else:
            print(f"{self.name} lacks the mana to summon the storm!")


# ==========================
# Bonus Class: Rogue
# ==========================
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=12)
        self.stealth = True

    def special_ability(self, other):
        """Rogue special: Backstab — deals triple damage when stealthed"""
        if self.stealth:
            print(f"{self.name} sneaks behind {other.name} for a Backstab! 🗡️")
            other.take_damage(self.attack_power * 3)
            self.stealth = False
        else:
            print(f"{self.name} can’t backstab — not in stealth mode!")

    def hide(self):
        """Re-enter stealth mode"""
        self.stealth = True
        print(f"{self.name} fades into the shadows... 🕶️")


# ==========================
# Test Showcase
# ==========================
if __name__ == "__main__":
    knight = Knight("Sir Valor")
    mage = Archmage("Eldra the Wise")
    rogue = Rogue("Shade")

    print("\n--- Character Descriptions ---")
    print(knight.describe())
    print(mage.describe())
    print(rogue.describe())

    print("\n--- Battle Simulation ---")
    knight.attack(mage)
    mage.special_ability(knight)
    rogue.special_ability(mage)
    knight.special_ability(rogue)
    rogue.hide()
    rogue.special_ability(knight)

    print("\n--- Final Health ---")
    print(knight.describe())
    print(mage.describe())
