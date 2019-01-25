"""
Popraw program wymieszane litery tak, żeby każdemu słowu towarzyszyła podpowiedź. Gracz powinien mieć możliwość
zobaczenia podpowiedzi, jeśli utknie w martwym punkcie. Dodaj system punktacji, który nagradza graczy
rozwiązujących anagram bez uciekania się do podpowiedzi.
"""

import random

# utwórz sekwencję słów do wyboru
WORDS = ("miłośc", "kocham", "zaufanie", "cierpliwość", "myszka", "szacunek")
# wybierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)
# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# utwórz 'pomieszaną' wersję słowa
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
"""
           Witaj w grze 'Wymieszane litery'!
   Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
Zapamiętaj, masz 10 szans na zgadnięcie, jeśli popełnisz błąd masz -1 pkt."""
)
print("Zgadnij, jakie to słowo:", jumble)

guess = input("\nTwoja odpowiedź: ")

prompt_check = False
score = 10
while guess != correct and guess != "":
    print("Niestety, to nie to słowo.")
    score -= 1
    if not prompt_check:
        hint = input("Czy chcesz skorzystać z podpowiedzi?(t/n): ")
        if hint.lower() == "t":
            print("To słowo rozpoczyna się na literę:", correct[:1], "a kończy na:", correct[len(correct)-1:])
            prompt_check = True
            score -= 1
    guess = input("Twoja odpowiedź: ")


if guess == correct:
    print("Zgadza się! Zgadłeś!")
    print("Twoje punkty:", score,"\n")

print("Dziękuję za udział w grze.\n")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")



