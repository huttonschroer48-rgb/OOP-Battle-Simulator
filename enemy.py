import random
class enemy:
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name):
        self.name = name
        self.health = random.randint(584,793)
        self.attack_power = random.randint(146, 172)

    def attack(self):
        return self.attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return self.health
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0