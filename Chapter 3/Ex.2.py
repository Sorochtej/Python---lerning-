#An amazing program that throws a coin 20 times.

print("\tThis program imitates a coin toss")
print("\nThe coin will be thrown 100 times")

import random

chance = 0
Heads = 0
Tails = 0
throw = 0
while chance <100:
    chance += 1
    throwing = random.randint(1, 2)
    if throwing == 1:
        Heads +=1
        print("Heads")
    else:
        Tails +=1
        print("Tails")
print("\nWith 100 throws it appeared that the tails was thrown out:",Tails,"times heads :",Heads,"times")
input("\n To end the program press ENTER: ")
