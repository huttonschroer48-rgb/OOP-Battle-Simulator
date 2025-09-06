from enemy import enemy

class Dart_Goblin(enemy):
    
    def __init__(self, name):
        super().__init__(name)
        self.health = 289
        self.attack_power = 632

    def attack(self):
        return self.attack_power
    

    def take_damage(self, damage):
        self.health -= damage
        print("*Didgeridoo sounds*")