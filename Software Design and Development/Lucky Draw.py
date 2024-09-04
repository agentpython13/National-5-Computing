#bennetthomas
#lucky draw

import random

names = []
for x in range(10):
    name = input("Enter name of person who would like to enter the lucky draw:")
    names.append(name)
    
print()

prizes = []
for x in range(4):
    prize = input("Enter prize that could be given to winner:")
    prizes.append(prize)


winner = random.choice(names)
winprize = random.choice(prizes)

print()

print(f"{winner} has won a {winprize}")
    
