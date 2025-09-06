from enemy import enemy
import random

class Goblin_Giant(enemy):

    def __init__(self, name):
        self.name = name
        self.health = 1831
        self.attack_spear_throw = random.randint(185, 225)
        self.attack_smash = 999

    def attack(self):
        AngryMode = random.randint(1,3)
        if AngryMode == 3:
            AngryMode = random.randint(1,3)
            return self.attack_smash
        else:
            AngryMode = random.randint(1,3)
            return self.attack_spear_throw
            