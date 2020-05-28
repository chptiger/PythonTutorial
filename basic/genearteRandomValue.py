import random
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

print(random.choice(['Thomas', 'Mosh', 'Mary']))


class Dice:
    def roll(self):
        result = ()
        return random.randint(1, 6), random.randint(1, 6)


dice = Dice()
print(dice.roll())
