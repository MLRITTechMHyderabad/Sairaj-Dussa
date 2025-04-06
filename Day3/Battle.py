import random

class Character:
    def __init__(self, name, attack_power, health, speed, defence):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.speed = speed
        self.defence = defence

    def attack(self, target):
        damage = max(attack_power - target.defence, 1)
        target.take_damage(damage)
        

    def take_damage(self, amount):
        self.health -= amount
    
    def is_alive(self):
        if self.health <= 0:
            return false
class Warrior(Character):
    def __init__(self, name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage = 0

    def attack(self, target):
        if self.health < 0.3 * self.health:
            damage = max(self.attack_power * 2 - target.defense, 1)
            target.take_damage(damage)
            print(f"{self.name} enters Berserk Mode and attacks {target.name}, dealing {damage} damage!")
        else:
            super().attack(target)

class Mage(Character):
    def __init__(self, name, attack_power, health, speed, defence, mana):
        super().__init__(self, attack_power, health, speed, defence)
        self.mana = mana

    def fireball(self, target):
        if self.mana > 10:
            damage = max(self.attack_power *2 - target.defence,1)
            target.take_damage(damage)
            self.health -= 5
            self.mana -= 10

            print(f"{self.name} casts Fireball on {target.name} dealing {damage} damage!")

        else:
            print(f"{self.name} tries to cast fireball but does not have mana!")

class Archer(Character):
    def __init__(self, name, attack_power, health, speed, defence, critical_chance):
        super().__init__(self, attack_power, health, speed, defence)
        self.critical_chance = critical_chance

    def attack(self, target):
        if random.random() < self.critical_chance:
            damage = max(self.attach_power *2 - target.defence, 1)
            target.take_damage(damage)
            print(f"{self.name} lands a Critical Hit on {target.name} dealing {damage} damage!")
        else:
            super().attack(taget)
def battle_simulation(characters):
    while len([c for c in characters if c.is_alive()]) > 1:
        character.sort(key=lambda x: x.speed, reverse = True)
        for character in characters:
            if character.is_alive():
                targets = [c for c in characters if c != character and c.is_alive()]
                if targets:
                    target = random.choice(targets)
                    character.attack(target)
                if not target.is_alive():
                    print(f"{target.name} has been defeated!")
        print("\n--- End of Round ---\n")

    winner = next((c for c in characters if c.is_alive()), None)
    if winner:
        print(f"{winner.name} wins the battle!")

thor = Warrior("Thor", 120, 15, 10, 5)
gandalf = Mage("Gandalf", 80, 20, 5, 4, 30)
alex = Archer("Alex", 100, 12, 8, 6, 0.3)

battle_simulation([thor, gandalf, alex])
            
            

 






            
