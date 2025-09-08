import random


class Character:
    def __init__(self):
        self.strength = Character.ability(self)
        self.dexterity = Character.ability(self)
        self.constitution = Character.ability(self)
        self.intelligence = Character.ability(self)
        self.wisdom = Character.ability(self)
        self.charisma = Character.ability(self)
        self.constitution_modifier = modifier(self.constitution)
        self.hitpoints = self.constitution_modifier + 10

    def ability(self):
        self.rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(self.rolls) - min(self.rolls)
        

def modifier(value):
    return (value - 10) // 2