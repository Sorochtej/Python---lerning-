import random

words = ("home","friend","relax","take","it","easy")
word = random.choice(words)

correct = ' '
lenght = len(word)
hint = 5

print(""" \t\t\t Yo ! Welcome in my GaMe ! 
    Find a hidden word, u have 5 chance to ask me a hint
    Good luck bro ! """)

print("\n\n The hidden word have: {} letters".format(lenght))

print("Anyw way I will give you the hint, the word are made of this letters --->adefhiklmntrxy")

for quess in word:
    quess = input(" Check the leter: ")

    if quess.lower() in word:
        print("Yes, this letter is part of the word")
        hint-=1
        print("You have {}, hints left".format(hint))
    else:
        print("Wrong letter ! Try one more time")
        hint -=1
        print("You have {}, hints left".format(hint))

        if hint < 5:
            print("Niestety skonczyly ci sie szanse")

correct = input("If you figure out the word give me the answer: ")
if correct == word:
    print("Exelent you guesed it !")

else:
    print("Sorry you loose the goos :P But Thnak U for game !")


print("Good bay")
