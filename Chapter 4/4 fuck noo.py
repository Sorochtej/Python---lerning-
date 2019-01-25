#Komputer wybiera losowo słowo, które gracz musi odgadnąc
#Komputer informuje graczaa, ile literek znajduje sie w słowie
#Gracz ma 5 szans na zadanie pytania"czy jakaś litera jest zawarta w tym słowie"
#Komputer może odpowidać tylko "tak/nie"

import random


WORDS =("pies","kot","mysz","patryk","ewa")
word = random.choice(WORDS)
correct = word
słowo = len(word)
szansa = 5
pomoc = ("t")
print("""\t\t\t Ewa, WItaj w Grze!!,\n
    \tMusisz odgadnąć ukryte słowo przez komputer, możesz aż 5 raazy zapytać
 komputer o wystepująco literke w słowie a Kompuś odpowie Ci "tak albo nie""")

print("\n\nUkryte słowo ma: ",len(word),"elementy")

for letter in word:
    letter = input("\nSprawdź literkę: ")

    if letter.lower() in word:
        print("\n Tak ")
        szansa -= 1
        letter = input("\nSprawdź literkę: ")
    else:
        print("\nW tym słowie NII ma tej literki: ", end="")
        szansa -= 1
        letter = input("\nSprawdź literkę: ")
    odpowiedz = input("\nWprowadź swoją odpowiedź: ")
    
    if odpowiedz == correct :
        print("\n Brawo !! Odgadłaś ukryte słowo !!")
    else:
        print("\nNiestety nie o to słowo mi chodziło")
        odpowiedz = input("\nWprowadź swoją odpowiedź: ")
 
                
        print("\nZostało Ci :",szansa,"szans" )

        print("\n Dzięki za udział w mojej grze !")
        input("\n\n\nAby zakończyć wciśnij klawisz Enter: ")


