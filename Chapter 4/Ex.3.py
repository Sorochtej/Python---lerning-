import random

words = ("love", "respect", "friendship", "patience")

word = random.choice(words)
correct = word
jumble = ' '
quess = ' '
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word [(position + 1):]
print(""" 
                 Welcome !!
    Lets, Play a game ! Put meesing around letters in right order to find a word !!
    Remamber !! You have only 10 chance """)


print("Guess a word:", jumble)
quess = input("\nYour answer ? : ")

prompt_check = False
score = 10

while quess!= correct and quess !="":
    print("Sorry, unfortunatly it is not the word we've been loking for")
    score -=1
    if not prompt_check:
        hint = input("Would like to use a hint ( y/n): ")
        if hint.lower == "y" :
            print("This word start by letter: ", correct[:1], "and ends on: ", correct[len(correct)-1])
            prompt_check = True
            score -= 1
    quess = input("Your answer: ")
if quess == correct:
    print("You find a very important word ! ")
    print("\n Mazeltow, Felicita")
    print("Your scores {}",format(score))





















































































































































































































































