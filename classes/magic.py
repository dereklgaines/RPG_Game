import random

class spell:
    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type


    # Calculates damage for magic spells
    def generate_damage(self,index):
        magicl = self.damage - 15
        magich = self.damage + 15
        return random.randrange(magicl,magich)
