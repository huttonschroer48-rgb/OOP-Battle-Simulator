class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 1803
        self.attack_powermain = 290
        self.attack_powerjump = 511


    def strike(self):
        if self.health > 1000:
            return self.attack_powermain
        else:
            return self.attack_powerjump
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return self.health
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    def is_alive(self):
        return self.health > 0