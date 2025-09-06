from enemy import enemy
import random

class Goblin(enemy):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color