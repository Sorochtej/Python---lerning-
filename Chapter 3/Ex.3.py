
#Program jaka to liczba
#Po wykorzystaniu okreslonej liczby prób nastąpi reprymenda

print("\tWitam Cie tutaj spowortem")
print("\nTy razem niestety masz ogarniczone pole manewru \nbo są\
\\10\\ próby odgadnbięcia ukrytej cyfry")
import random
the_number = random.randint(1, 100)
guess = int(input("Ta liczba to: "))
tries = 1
while guess != the_number and tries <10:
    if guess > the_number:
        print("Za duża...")
    else:
        print("Za mała...")
    guess = int(input("Ta liczba to: "))
    tries +=1
    if guess == the_number:
        print("\t\t WOOOW !! UDAŁO CI SIĘ, JETEŚ NIESAMOWITY")
    if tries >10:  
        print("Niestety nie udało Ci się odgadnąć cyfry w danej ilości prób")

input("\n\n Aby zakończyć program wciśniej ENTER: ")
