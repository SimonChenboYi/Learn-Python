import random

class Dice:
    def roll(self):
        number1 = random.randint(1,6)
        number2 = random.randint(1,6)
        return number1, number2


dice = Dice()
print(dice.roll())