#Wymieszane litery
#Program miesza słowa i formuuje anagramy
#Pomaga Ci w odgadywaniu anagramów dając Ci podpowiedzi

import random

SŁOWA = ("miła","kochana","opiekuńcza","cierpliwa","wyrozumiała")

word = random.choice(SŁOWA)
dobrze = word

#Program miesza słowa i formuuje anagramy

jumbel =""
pomoc =(
while word:
    position = random.randrange(len(word))
    
    jumbel +=word[position]
    
    word = word[:position] + word[(position + 1):]

print(
"""
Witaj w grze 'Wymieszane litery'!
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print("Zgadnij, jakie to słowo:", jumbel)

guess = input("\nTwoja odpowiedź: ")
while guess != dobrze and guess != "":
    print("OoOooj Ewcia, to nie to słowo.")
    guess = input("Twoja odpowiedź: ")
    score = len(dobrze)*10
if guess != dobrze:
    print("\nNietety, nie o to mi chodziło")
else:
    print("\nUało Ci się myszko ! odgadłaś hasło gratuluje")
    print("\n\t\tNagroda to buziak (:*)\n\n\n")
if guess == pomoc:
    print("widzę że potrzebujesz pomocy, podpowiem CI pierwszą literkę wyrazu")
    print(dobrze[0:1])
        












print("\n\nDziękuję za udział w grze.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
