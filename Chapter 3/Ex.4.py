#Program w, którym gracz i komputer zamienią się rolami.
#To znaczygracz wybierasz losowo liczbę z przedziału...
#...od 1 do 100,a komputer ma jąodgadnąć.

import random

print("\t Witam was w emocjonującej zabawie 'ZGADNIJ JAKA TO LICZBA'")
print("\nZasadą gry jest wybór gry przez użytkownika a następnie zgadnięcie jej przez komputer")
print("\n\t\t\t\t Lets BEGIN ! ")

x = int(input("Pomyśl o jaką liczbe mi chodzi oraz powiedz mi ją w tajemnicy!: "))
y = random.randint(1,100)
z = 1
while y != x:
    y = random.randint(1,100)
    print("Czy Twoja liczba to: ",y,"?")
    odpowiedź=input("Czy to taa liczba? tak/nie")
    if y > x:
        print("liczba jest za duza...")
        z +=1
    elif y < x:
        print("liczba jest za mała...")
        z +=1
    elif y == x:
        print("\t\n EXTRA! Udało Ci się")

print("Komputer odgadł liczbę w: ",z,"próbie")
input("\n\nAby zakończyć program naciśniej ENTER : ")
